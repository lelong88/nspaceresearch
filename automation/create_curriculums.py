#!/usr/bin/env python3
"""
Create and upload curriculums for chapters 2-20 of
"The Last Light of Alder House" to the API.
"""

import json
import os
import re
import sys
import requests
import math

API_URL = "https://helloapi.step.is/curriculum/create"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
LANGUAGE = "en"
USER_LANGUAGE = "en"

# Map chapter numbers to their file paths (relative to project root)
CHAPTER_PATHS = {}
PARTS = {
    "part-1": [1, 2, 3, 4],
    "part-2": [5, 6, 7, 8],
    "part-3": [9, 10, 11, 12],
    "part-4": [13, 14, 15, 16],
    "part-5": [17, 18, 19, 20],
}
BASE = "original-novels/the-last-light-of-alder-house"
for part, chapters in PARTS.items():
    for ch in chapters:
        CHAPTER_PATHS[ch] = os.path.join(BASE, part, f"{ch}.txt")

# Chapter titles (will be extracted from text or defined here)
CHAPTER_TITLES = {
    1: "The Letter",
    2: "Alder House",
    3: "The Journal",
    4: "The Town",
    5: "The Fisherman",
    6: "The Library",
    7: "The Storm",
    8: "The Basement Door",
    9: "The Light Below",
    10: "The History",
    11: "The Warning",
    12: "The Stranger",
    13: "The Secret Room",
    14: "The Photograph",
    15: "The Truth",
    16: "The Descent",
    17: "The Light",
    18: "The Choice",
    19: "The Return",
    20: "The Last Light",
}

# Curated vocabulary words per chapter (20 words each, intermediate level)
# These are selected to be useful, contextual, and learnable
CHAPTER_VOCAB = {}


def extract_title_from_text(text: str, chapter_num: int) -> str:
    """Extract chapter title from the text content."""
    match = re.match(r"Chapter\s+\d+:\s*(.+)", text.strip())
    if match:
        return match.group(1).strip()
    return CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")


def select_vocab_from_text(text: str, count: int = 20) -> list[str]:
    """
    Select intermediate-level vocabulary words from chapter text.
    Picks words that are useful for English learners.
    """
    # Common words to exclude (too basic for intermediate learners)
    basic_words = set("""
        the a an is was were are am be been being have has had do does did
        will would shall should can could may might must need dare
        i me my mine we us our ours you your yours he him his she her hers
        it its they them their theirs this that these those
        who whom whose which what where when why how
        and but or nor for yet so if then than because although though
        in on at to from by with about between through during before after
        above below up down out off over under again further once
        not no never none neither nor nothing nowhere
        all each every both few many much more most some any
        here there now just also very too quite rather really
        said says say told tell go went gone come came get got
        make made take took give gave see saw know knew think thought
        want like look use find way day time year people
        new good great first last long little own old right big
        high small large next young important different
        back still even also well just already always
        into only other after over such
        thing man woman child hand part place case week
        point work world house number group problem fact
        mr mrs ms dr
        door room floor wall window table chair desk bed book
        hand head eyes face voice name word letter water
        left right side front turned walked stood looked
        opened closed pulled pushed held felt found
        something nothing everything anything someone
        away down inside outside around through
        dark light white black long short
        three four five second third
        morning night today tonight
        asked answered called heard
        began started stopped tried
        knew thought felt seemed
        sure enough still again
        before behind between
        read reading write writing
        life live living dead death
        home town road street
        back came going coming
        keep kept left leave
        kind sort type
        hard easy full empty
        same another
        body mind heart
        mother father family
        house room door
        wood wooden stone
        sound heard voice
        moment later
        half whole
        almost never
        already still
        enough quite
        rather really
        perhaps maybe
        however though
        toward towards
        across along
        against beside
        beneath beyond
        within without
        upon until
        since while
        during until
        certain clear
        early late
        near close
        open shut
        true real
        deep wide
        cold warm
        fast slow
        heavy light
        young girl
        small town
        covered
    """.split())

    # Also exclude proper nouns from the story
    proper_nouns = set("""
        maya chen eleanor voss whitfield alder bay house oregon portland
        oliver cliff road thomas alderhouse aldert alderho
        james ruth helen margaret samuel daniel
        nora lena finn rose lily
    """.split())

    exclude = basic_words | proper_nouns

    # Extract all words
    words = re.findall(r"\b[a-z]+(?:-[a-z]+)?\b", text.lower())

    # Count frequency
    freq = {}
    for w in words:
        if w not in exclude and len(w) > 4:
            freq[w] = freq.get(w, 0) + 1

    # Sort by frequency (prefer words that appear 2-5 times — used but not too common)
    scored = []
    for word, count_val in freq.items():
        # Prefer words appearing 1-5 times
        if 1 <= count_val <= 8:
            score = count_val if count_val <= 5 else 5 - (count_val - 5) * 0.5
            # Prefer longer words (more likely to be intermediate)
            score += min(len(word) - 5, 4) * 0.8
            scored.append((word, score))

    scored.sort(key=lambda x: -x[1])

    # Take top words
    selected = [w for w, _ in scored[:count]]
    return selected


def split_text_into_sections(text: str, num_sections: int = 5) -> list[tuple[str, str]]:
    """
    Split chapter text into roughly equal sections for reading activities.
    Returns list of (section_title, section_text) tuples.
    """
    # Remove the chapter title line
    lines = text.strip().split("\n")
    if lines and re.match(r"Chapter\s+\d+:", lines[0]):
        lines = lines[1:]

    full_text = "\n".join(lines).strip()

    # Split by paragraph breaks (double newline)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", full_text) if p.strip()]

    if not paragraphs:
        return [("Reading", full_text)]

    # Group paragraphs into sections
    total_chars = sum(len(p) for p in paragraphs)
    target_per_section = total_chars / num_sections

    sections = []
    current_section = []
    current_length = 0

    for para in paragraphs:
        current_section.append(para)
        current_length += len(para)

        if current_length >= target_per_section and len(sections) < num_sections - 1:
            sections.append("\n\n".join(current_section))
            current_section = []
            current_length = 0

    # Add remaining paragraphs to last section
    if current_section:
        sections.append("\n\n".join(current_section))

    # If we got fewer sections than desired, that's fine
    # Generate section titles
    result = []
    for i, section in enumerate(sections):
        title = f"Part {i + 1}"
        result.append((title, section))

    return result


def build_curriculum(chapter_num: int, chapter_text: str) -> dict:
    """Build a curriculum JSON for a chapter."""
    title = extract_title_from_text(chapter_text, chapter_num)
    vocab = select_vocab_from_text(chapter_text, 20)
    sections = split_text_into_sections(chapter_text, 5)

    # Distribute vocab across sessions (4 words per session for 5 sessions)
    vocab_per_session = 4
    num_sessions = min(len(sections), 5)

    # Ensure we have enough vocab
    while len(vocab) < num_sessions * vocab_per_session:
        vocab.append(vocab[-1] if vocab else "word")

    learning_sessions = []

    for i in range(num_sessions):
        session_vocab = vocab[i * vocab_per_session : (i + 1) * vocab_per_session]
        section_title, section_text = sections[i]

        # Estimate reading time (avg 200 wpm for learners, slower)
        word_count = len(section_text.split())
        read_minutes = max(2, min(8, math.ceil(word_count / 150)))

        session = {
            "title": f"Session {i + 1}: {section_title}",
            "activities": [
                {
                    "title": f"Flashcards: {section_title}",
                    "description": f"Study {len(session_vocab)} words: {', '.join(session_vocab)}",
                    "activityType": "viewFlashcards",
                    "practiceMinutes": 2,
                    "data": {
                        "vocabList": session_vocab,
                        "audioSpeed": -0.2,
                    },
                },
                {
                    "title": f"Read: {section_title}",
                    "description": f"Read section {i + 1} of the chapter.",
                    "activityType": "reading",
                    "practiceMinutes": read_minutes,
                    "data": {
                        "text": section_text,
                        "audioSpeed": -0.2,
                    },
                },
                {
                    "title": f"Listen: {section_title}",
                    "description": "Listen to the passage you just read and follow along.",
                    "activityType": "readAlong",
                    "practiceMinutes": max(2, read_minutes - 1),
                    "data": {
                        "text": section_text,
                        "audioSpeed": -0.2,
                    },
                },
            ],
        }
        learning_sessions.append(session)

    # Add a full review session
    full_text_clean = chapter_text.strip()
    if re.match(r"Chapter\s+\d+:", full_text_clean):
        full_text_clean = "\n".join(full_text_clean.split("\n")[1:]).strip()

    full_word_count = len(full_text_clean.split())
    full_read_minutes = max(5, min(15, math.ceil(full_word_count / 150)))

    review_session = {
        "title": f"Session {num_sessions + 1}: Full Chapter Review",
        "activities": [
            {
                "title": f"Flashcards: Chapter {chapter_num} Review",
                "description": f"Review all {len(vocab)} vocabulary words from the full chapter.",
                "activityType": "viewFlashcards",
                "practiceMinutes": 5,
                "data": {
                    "vocabList": vocab,
                    "audioSpeed": -0.2,
                },
            },
            {
                "title": "Listen: The Full Chapter",
                "description": f"Listen to the complete story of Chapter {chapter_num}.",
                "activityType": "readAlong",
                "practiceMinutes": full_read_minutes,
                "data": {
                    "text": full_text_clean,
                    "audioSpeed": -0.2,
                },
            },
        ],
    }
    learning_sessions.append(review_session)

    # Build preview text
    preview_text = (
        f"Continue the mystery of Alder House in Chapter {chapter_num}: {title}. "
        f"This curriculum teaches 20 English vocabulary words through the next part of "
        f"Maya's story, written for intermediate learners."
    )

    curriculum = {
        "title": f"The Last Light of Alder House — Chapter {chapter_num}: {title}",
        "taskId": None,
        "preview": {"text": preview_text},
        "description": (
            f"Learn 20 intermediate English vocabulary words through Chapter {chapter_num} "
            f"of a mystery novel. Across {num_sessions + 1} sessions you will study "
            f"flashcards and read sections of the story, absorbing new words in context."
        ),
        "learningSessions": learning_sessions,
    }

    return curriculum


FIREBASE_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhYWM0MWY3NTA4OGZlOGUwOWEwN2Q0NDRjZmQ2YjhjZTQ4MTJhMzEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbnNwYWNlLTRmOWIxIiwiYXVkIjoibnNwYWNlLTRmOWIxIiwiYXV0aF90aW1lIjoxNzczMTI4MjE0LCJ1c2VyX2lkIjoienM1QU1wVmZxa2NmRGY4Q0o5cXJYZEg1OGQ3MyIsInN1YiI6InpzNUFNcFZmcWtjZkRmOENKOXFyWGRINThkNzMiLCJpYXQiOjE3NzMxMjgyMTQsImV4cCI6MTc3MzEzMTgxNCwiZW1haWwiOiJsZWxvbmc4OEBvdXRsb29rLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImxlbG9uZzg4QG91dGxvb2suY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.uMZ97qEdJONOqUqJp1LOZN8Dvj7HYIrcXrEM7lG50tQ91qjbhHrCaWuGd4ouIzO002w6eC7GhMQ7OGjsdUk_iTjCX1UM-U074LZ5RecvTV3YvlTboydnvhHF6XF46vHsUdCSV316A_skerHFWlsJVve5O5kVArs__Pq4A-1wzL4usLVdncVcCbXSBM6vhB62C3P2qLRnCy4ZtyCV7EHapgWS2ltgy6PAJph4LbAH9diBjM3tG0uMVWdAmbI0ntbC086uzEo5JSNRSi9xuxwREYWI_wnEjZzPNWM5TjH3JK6dhuiq8SH0ykVBE4SvlDybTRhdugb6BER83LLTdzPVhA"


def upload_curriculum(content: dict) -> dict:
    """Upload a curriculum to the API."""
    payload = {
        "uid": UID,
        "language": LANGUAGE,
        "userLanguage": USER_LANGUAGE,
        "content": json.dumps(content),
        "firebaseIdToken": FIREBASE_TOKEN,
    }

    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()


def main():
    start_chapter = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    end_chapter = int(sys.argv[2]) if len(sys.argv) > 2 else 20

    print(f"Creating curriculums for chapters {start_chapter}-{end_chapter}...")

    # Change to project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    os.chdir(project_root)

    results = []

    for ch in range(start_chapter, end_chapter + 1):
        path = CHAPTER_PATHS.get(ch)
        if not path or not os.path.exists(path):
            print(f"  Chapter {ch}: FILE NOT FOUND at {path}")
            continue

        print(f"\n  Chapter {ch}: Reading {path}...")
        with open(path, "r") as f:
            text = f.read()

        print(f"  Chapter {ch}: Building curriculum...")
        curriculum = build_curriculum(ch, text)

        # Save locally for reference
        out_dir = os.path.join(BASE, f"chapter-{ch}-curriculum.json")
        with open(out_dir, "w") as f:
            json.dump(curriculum, f, indent=2)
        print(f"  Chapter {ch}: Saved locally to {out_dir}")

        print(f"  Chapter {ch}: Uploading to API...")
        try:
            result = upload_curriculum(curriculum)
            curriculum_id = result.get("id", "unknown")
            print(f"  Chapter {ch}: SUCCESS — id={curriculum_id}")
            results.append({"chapter": ch, "id": curriculum_id, "status": "success"})
        except Exception as e:
            print(f"  Chapter {ch}: FAILED — {e}")
            results.append({"chapter": ch, "error": str(e), "status": "failed"})

    print("\n\n=== SUMMARY ===")
    for r in results:
        status = "✓" if r["status"] == "success" else "✗"
        ch = r["chapter"]
        if r["status"] == "success":
            print(f"  {status} Chapter {ch}: {r['id']}")
        else:
            print(f"  {status} Chapter {ch}: {r['error']}")

    failed = [r for r in results if r["status"] == "failed"]
    if failed:
        print(f"\n{len(failed)} chapters failed. Re-run with specific range to retry.")
    else:
        print(f"\nAll {len(results)} chapters uploaded successfully!")


if __name__ == "__main__":
    main()
