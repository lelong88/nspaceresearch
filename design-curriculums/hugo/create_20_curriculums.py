#!/usr/bin/env python3
"""
Create 20 new curriculums based on the structure of 'Rewriting Extinction' (gA1W24Ga6lXwdHHx),
each on a diverse different topic but matching the same difficulty level and structure.
"""

import json
import requests
import time

API_URL = "https://helloapi.step.is/curriculum/create"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
LANGUAGE = "en"
USER_LANGUAGE = "en"
FIREBASE_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhYWM0MWY3NTA4OGZlOGUwOWEwN2Q0NDRjZmQ2YjhjZTQ4MTJhMzEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbnNwYWNlLTRmOWIxIiwiYXVkIjoibnNwYWNlLTRmOWIxIiwiYXV0aF90aW1lIjoxNzczMTI4MjE0LCJ1c2VyX2lkIjoienM1QU1wVmZxa2NmRGY4Q0o5cXJYZEg1OGQ3MyIsInN1YiI6InpzNUFNcFZmcWtjZkRmOENKOXFyWGRINThkNzMiLCJpYXQiOjE3NzMxMjgyMTQsImV4cCI6MTc3MzEzMTgxNCwiZW1haWwiOiJuZ3V5ZW5oYWlkdW9uZzI2MTBAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibmd1eWVuaGFpZHVvbmcyNjEwQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.Vy-Vy0ynECMOJGFCaDJBgWMwFMBMGLJqID3a3x_bfJJMqHqJqEqJqEqJqEqJqEq"

KEYS_TO_STRIP = {"mp3Url", "illustrationSet", "chapterBookmarks", "segments",
                  "whiteboardItems", "userReadingId", "lessonUniqueId",
                  "curriculumTags", "taskId", "imageId"}


def strip_keys(obj, keys_to_remove):
    if isinstance(obj, dict):
        return {k: strip_keys(v, keys_to_remove) for k, v in obj.items() if k not in keys_to_remove}
    if isinstance(obj, list):
        return [strip_keys(item, keys_to_remove) for item in obj]
    return obj


def build_writing_sentence_items(vocab_list, topic_context):
    """Build writingSentence items for a vocab list."""
    items = []
    for word in vocab_list:
        items.append({
            "prompt": f"Use the word '{word.lower()}' in a sentence related to {topic_context}.",
            "targetVocab": word.lower()
        })
    return items


def build_session1(topic):
    """Build Session 1: first 5 vocab words + reading + writing."""
    vocab = topic["s1_vocab"]
    return {
        "title": topic["s1_title"],
        "activities": [
            {
                "title": "Welcome & Vocabulary Introduction",
                "description": f"Listen to an introduction about the topic and learn all five vocabulary words for Session 1: {', '.join(v.lower() for v in vocab)}",
                "activityType": "introAudio",
                "practiceMinutes": 1,
                "data": {
                    "text": f"Welcome to '{topic['title']}'! In this first session, you'll learn five vocabulary words that introduce the core ideas of our article. The words are: {', '.join(vocab)}. Let's explore each one in the context of our fascinating topic.",
                    "audioSpeed": 0.01
                }
            },
            {
                "title": f"Flashcards: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": f"Study the words: {', '.join(vocab)}",
                "activityType": "viewFlashcards",
                "practiceMinutes": 4,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Speak Flashcards: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": f"Practice saying the words: {', '.join(vocab)}",
                "activityType": "speakFlashcards",
                "practiceMinutes": 3,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Recognition Drill: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": "Choose the correct definition for each vocabulary word",
                "activityType": "vocabLevel1",
                "practiceMinutes": 5,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Active Recall: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": "Supply the correct word without any hints",
                "activityType": "vocabLevel2",
                "practiceMinutes": 5,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Understand: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": "Demonstrate understanding of each vocabulary word in context",
                "activityType": "vocabLevel3",
                "practiceMinutes": 5,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Short Reading: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": "Read a short passage containing the vocabulary from Session 1",
                "activityType": "reading",
                "practiceMinutes": 5,
                "data": {"text": topic["s1_reading"], "audioSpeed": 0.01}
            },
            {
                "title": f"Speak Along: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": "Practice speaking the short passage by repeating it aloud",
                "activityType": "speakReading",
                "practiceMinutes": 5,
                "data": {"text": topic["s1_reading"], "audioSpeed": 0.01}
            },
            {
                "title": f"Listen: {topic['s1_title'].replace('Session 1: ', '')}",
                "description": "Listen to the short reading passage from Session 1",
                "activityType": "readAlong",
                "practiceMinutes": 2,
                "data": {"text": topic["s1_reading"], "audioSpeed": 0.01}
            },
            {
                "title": "Write Sentences with Target Vocabulary",
                "description": f"Write English sentences using target vocabulary from Session 1: {', '.join(vocab)}",
                "activityType": "writingSentence",
                "practiceMinutes": 8,
                "data": {
                    "vocabList": vocab,
                    "audioSpeed": 0.01,
                    "items": build_writing_sentence_items(vocab, topic["title"].lower())
                }
            },
            {
                "title": "Write a Short Paragraph",
                "description": f"Write a 4-6 sentence paragraph using at least 3 out of 5 vocabulary words from Session 1",
                "activityType": "writingParagraph",
                "practiceMinutes": 10,
                "data": {
                    "vocabList": vocab,
                    "audioSpeed": 0.01,
                    "instructions": "Choose one of the prompts below. Write 4-6 sentences in English. Use at least 3 out of 5 vocabulary words you have learned.",
                    "prompts": [
                        f"Using vocabulary from Session 1, explain one key concept from the article about {topic['title'].lower()}.",
                        f"Share your thoughts on {topic['title'].lower()} using at least 3 vocabulary words from this session."
                    ],
                    "rubric": [
                        "Correctly uses at least 3 out of 5 vocabulary words",
                        "Vocabulary is used in appropriate context",
                        "Sentences have clear grammatical structure",
                        "Paragraph has a clear main idea and logical coherence"
                    ]
                }
            }
        ]
    }


def build_session2(topic):
    """Build Session 2: next 5 vocab words + reading + writing."""
    vocab = topic["s2_vocab"]
    s1_vocab = topic["s1_vocab"]
    return {
        "title": topic["s2_title"],
        "activities": [
            {
                "title": "Session 2 Introduction & Vocabulary",
                "description": f"Recap of Session 1 and learn all five vocabulary words for Session 2: {', '.join(v.lower() for v in vocab)}",
                "activityType": "introAudio",
                "practiceMinutes": 1,
                "data": {
                    "text": f"Welcome back! In Session 1, you learned {', '.join(s1_vocab)}. Today, you'll learn five new words: {', '.join(vocab)}. Let's dive deeper into our topic.",
                    "audioSpeed": 0.01
                }
            },
            {
                "title": f"Flashcards: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": f"Study the words: {', '.join(vocab)}",
                "activityType": "viewFlashcards",
                "practiceMinutes": 4,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Speak Flashcards: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": f"Practice saying the words: {', '.join(vocab)}",
                "activityType": "speakFlashcards",
                "practiceMinutes": 3,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Recognition Drill: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": "Choose the correct definition for each vocabulary word",
                "activityType": "vocabLevel1",
                "practiceMinutes": 5,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Active Recall: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": "Supply the correct word without any hints",
                "activityType": "vocabLevel2",
                "practiceMinutes": 5,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Understand: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": "Demonstrate understanding of each vocabulary word in context",
                "activityType": "vocabLevel3",
                "practiceMinutes": 5,
                "data": {"vocabList": vocab, "audioSpeed": 0.01}
            },
            {
                "title": f"Short Reading: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": "Read a short passage containing the vocabulary from Session 2",
                "activityType": "reading",
                "practiceMinutes": 5,
                "data": {"text": topic["s2_reading"], "audioSpeed": 0.01}
            },
            {
                "title": f"Speak Along: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": "Practice speaking the short passage by repeating it aloud",
                "activityType": "speakReading",
                "practiceMinutes": 5,
                "data": {"text": topic["s2_reading"], "audioSpeed": 0.01}
            },
            {
                "title": f"Listen: {topic['s2_title'].replace('Session 2: ', '')}",
                "description": "Listen to the short reading passage from Session 2",
                "activityType": "readAlong",
                "practiceMinutes": 2,
                "data": {"text": topic["s2_reading"], "audioSpeed": 0.01}
            },
            {
                "title": "Write Sentences with Target Vocabulary",
                "description": f"Write English sentences using target vocabulary from Session 2: {', '.join(vocab)}",
                "activityType": "writingSentence",
                "practiceMinutes": 8,
                "data": {
                    "vocabList": vocab,
                    "audioSpeed": 0.01,
                    "items": build_writing_sentence_items(vocab, topic["title"].lower())
                }
            },
            {
                "title": "Write a Short Paragraph",
                "description": f"Write a 4-6 sentence paragraph using at least 3 out of 5 vocabulary words from Session 2",
                "activityType": "writingParagraph",
                "practiceMinutes": 10,
                "data": {
                    "vocabList": vocab,
                    "audioSpeed": 0.01,
                    "instructions": "Choose one of the prompts below. Write 4-6 sentences in English. Use at least 3 out of 5 vocabulary words you have learned.",
                    "prompts": [
                        f"Using vocabulary from Session 2, discuss the challenges or debates surrounding {topic['title'].lower()}.",
                        f"Describe what you found most interesting about {topic['title'].lower()} using at least 3 vocabulary words."
                    ],
                    "rubric": [
                        "Correctly uses at least 3 out of 5 vocabulary words",
                        "Vocabulary is used in appropriate context",
                        "Sentences have clear grammatical structure",
                        "Paragraph has a clear main idea and logical coherence"
                    ]
                }
            }
        ]
    }


def build_session3(topic):
    """Build Session 3: Full vocabulary review."""
    all_vocab = topic["s1_vocab"] + topic["s2_vocab"]
    return {
        "title": "Session 3: Full Vocabulary Review",
        "activities": [
            {
                "title": "Review Introduction",
                "description": "Listen to guidance on reviewing all vocabulary from the course",
                "activityType": "introAudio",
                "practiceMinutes": 1,
                "data": {
                    "text": f"Congratulations on learning all 10 vocabulary words! Today is all about review and consolidation. You'll go through all 10 words with flashcards, then test yourself with recognition and recall exercises. Make sure you're confident with every word before we tackle the full article in Session 4!",
                    "audioSpeed": 0.01
                }
            },
            {
                "title": "Review All Vocabulary",
                "description": "Review flashcards for all 10 vocabulary words from the entire course",
                "activityType": "viewFlashcards",
                "practiceMinutes": 1,
                "data": {"vocabList": all_vocab, "audioSpeed": 0.01}
            },
            {
                "title": "Quick Check: Recognition",
                "description": "Multiple choice quiz covering all 10 vocabulary words",
                "activityType": "vocabLevel1",
                "practiceMinutes": 10,
                "data": {"vocabList": all_vocab, "audioSpeed": 0.01}
            },
            {
                "title": "Deep Check: Active Recall",
                "description": "Supply the correct word from memory for all 10 vocabulary words",
                "activityType": "vocabLevel2",
                "practiceMinutes": 10,
                "data": {"vocabList": all_vocab, "audioSpeed": 0.01}
            },
            {
                "title": "Understand: All Vocabulary",
                "description": "Demonstrate understanding of all 10 vocabulary words in context",
                "activityType": "vocabLevel3",
                "practiceMinutes": 10,
                "data": {"vocabList": all_vocab, "audioSpeed": 0.01}
            },
            {
                "title": "Write a Comprehensive Paragraph",
                "description": "Write a 5-7 sentence paragraph using at least 6 out of 10 vocabulary words from both sessions",
                "activityType": "writingParagraph",
                "practiceMinutes": 12,
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": 0.01,
                    "instructions": "Choose one of the prompts below. Write 5-7 sentences in English. Use at least 6 out of 10 vocabulary words you have learned from both sessions.",
                    "prompts": [
                        f"Explain in your own words the key ideas from '{topic['title']}'. Cover the main concepts and share your perspective.",
                        f"If you were explaining {topic['title'].lower()} to a friend, what would you say? Use vocabulary words from both sessions."
                    ],
                    "rubric": [
                        "Correctly uses at least 6 out of 10 vocabulary words",
                        "Vocabulary is drawn from both sessions",
                        "Sentences have clear grammatical structure",
                        "Paragraph has a clear main idea and logical coherence",
                        f"Shows understanding of {topic['title'].lower()} and its implications"
                    ]
                }
            }
        ]
    }


def build_session4(topic):
    """Build Session 4: Full article reading."""
    all_vocab = topic["s1_vocab"] + topic["s2_vocab"]
    return {
        "title": "Session 4: Read the Full Article",
        "activities": [
            {
                "title": "Final Reading Introduction",
                "description": "Guidance before reading the complete article",
                "activityType": "introAudio",
                "practiceMinutes": 1,
                "data": {
                    "text": f"Welcome to your final session! You've learned all 10 vocabulary words, reviewed them thoroughly, and read short passages from each section. Now it's time to read the complete article about {topic['title'].lower()}. As you read, notice how each vocabulary word fits naturally into the text. Enjoy the reading!",
                    "audioSpeed": 0.01
                }
            },
            {
                "title": f"Full Article: {topic['title']}",
                "description": "Read the complete article containing all 10 vocabulary words to consolidate your learning",
                "activityType": "reading",
                "practiceMinutes": 15,
                "data": {"text": topic["full_article"], "audioSpeed": 0.01}
            },
            {
                "title": "Speak Along: Full Article",
                "description": "Practice speaking the complete article by repeating it aloud",
                "activityType": "speakReading",
                "practiceMinutes": 15,
                "data": {"text": topic["full_article"], "audioSpeed": 0.01}
            },
            {
                "title": "Listen: Full Article",
                "description": f"Listen to the complete article about {topic['title'].lower()}",
                "activityType": "readAlong",
                "practiceMinutes": 3,
                "data": {"text": topic["full_article"], "audioSpeed": 0.01}
            },
            {
                "title": "Advanced Comprehensive Writing",
                "description": "Write a 6-8 sentence paragraph using at least 8 out of 10 vocabulary words, demonstrating comprehensive understanding and deeper analysis",
                "activityType": "writingParagraph",
                "practiceMinutes": 15,
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": 0.01,
                    "instructions": "Choose one of the prompts below. Write 6-8 sentences in English. Use at least 8 out of 10 vocabulary words you have learned. Try to demonstrate deep analysis and connect ideas from all sessions.",
                    "prompts": [
                        f"Write a letter to a friend explaining what you learned about {topic['title'].lower()}. Cover the key concepts, the debates, and your personal opinion.",
                        f"Imagine you are a journalist writing a brief report about {topic['title'].lower()}. Summarize the main ideas and discuss why this topic matters."
                    ],
                    "rubric": [
                        "Correctly uses at least 8 out of 10 vocabulary words",
                        "Vocabulary is drawn from both sessions",
                        f"Shows deep understanding of {topic['title'].lower()}",
                        "Demonstrates ability to connect ideas across all themes",
                        "Sentences have clear grammatical structure and varied complexity",
                        "Paragraph has a compelling argument with logical flow"
                    ]
                }
            },
            {
                "title": "Vocabulary Overview & Congratulations",
                "description": "Listen to a summary of all vocabulary learned and a farewell message",
                "activityType": "introAudio",
                "practiceMinutes": 4,
                "data": {
                    "text": f"Congratulations on completing '{topic['title']}'! You've mastered all 10 vocabulary words: {', '.join(all_vocab)}. You started by learning the foundational concepts, then explored the deeper implications and debates. You've read the full article and demonstrated your understanding through writing. These words and ideas will stay with you. Thank you for joining me on this journey! Goodbye, and happy reading!",
                    "audioSpeed": 0.01
                }
            }
        ]
    }


def build_curriculum(topic):
    """Build a complete curriculum content JSON for a topic."""
    return {
        "title": topic["title"],
        "preview": {"text": topic["preview"]},
        "description": topic["description"],
        "learningSessions": [
            build_session1(topic),
            build_session2(topic),
            build_session3(topic),
            build_session4(topic)
        ]
    }


def upload_curriculum(content):
    """Upload a curriculum to the API."""
    payload = {
        "uid": UID,
        "language": LANGUAGE,
        "userLanguage": USER_LANGUAGE,
        "content": json.dumps(content),
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()


def main():
    print(f"Creating {len(TOPICS)} curriculums...")
    results = []

    for i, topic in enumerate(TOPICS):
        print(f"\n[{i+1}/{len(TOPICS)}] Creating: {topic['title']}")
        content = build_curriculum(topic)
        try:
            result = upload_curriculum(content)
            curriculum_id = result.get("id", "unknown")
            print(f"  ✓ Created with ID: {curriculum_id}")
            results.append({"title": topic["title"], "id": curriculum_id, "status": "success"})
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            results.append({"title": topic["title"], "id": None, "status": f"failed: {e}"})
        time.sleep(1)  # Be nice to the API

    print(f"\n{'='*60}")
    print(f"Results: {sum(1 for r in results if r['status'] == 'success')}/{len(results)} succeeded")
    for r in results:
        status = "✓" if r["status"] == "success" else "✗"
        print(f"  {status} {r['title']} -> {r['id']}")


if __name__ == "__main__":
    main()
