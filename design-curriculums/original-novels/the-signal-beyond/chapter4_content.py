"""
Chapter 4: The Warning
Setup concludes, stakes are established — Lena visits Dr. Torres during office hours and learns
that a government liaison named Director Hale ordered her father's files sealed. Torres gives
Lena a USB drive containing fragments of Marco's research notes. Back at her apartment, Lena
reads the notes and discovers her father detected the same signal 15 years ago. His final entry
is a warning: "They will come for this. Do not let them bury it again."
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 4."""

    # --- Vocabulary: 20 B2-level words, 4 per passage ---
    vocab_1 = ["apprehensive", "comply", "authorise", "scrutiny"]
    vocab_2 = ["confiscate", "allegation", "covert", "jurisdiction"]
    vocab_3 = ["decrypt", "annotation", "deterioration", "correspondence"]
    vocab_4 = ["replicate", "apparatus", "wavelength", "notation"]
    vocab_5 = ["urgency", "testimony", "inevitable", "confrontation"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-290 words each, B2-level prose) ---

    passage_1 = (
        "Lena arrived at the Hargrove Library just before ten the following morning. She had "
        "barely slept — the prime number sequence kept turning in her mind like a wheel that "
        "would not stop. She climbed the stairs to the third floor and found Dr. Torres's office "
        "at the end of a narrow hallway, the door slightly open.\n\n"
        "Torres looked up from her desk and gestured for Lena to sit. The room was small and "
        "lined with bookshelves, the air heavy with the smell of old paper. Torres closed the "
        "door behind her and sat down again, folding her hands on the desk.\n\n"
        "\"I was apprehensive about this conversation,\" Torres began. \"But I have thought about "
        "it carefully, and I believe you deserve to know what happened.\" She paused, choosing "
        "her words. \"Eight years ago, a man named Director Hale visited the university. He "
        "represented a government liaison office — I was never told which agency. He carried "
        "documents that required the department to comply with a formal order to seal your "
        "father's research files.\"\n\n"
        "\"On what grounds?\" Lena asked.\n\n"
        "\"National security. He said the materials were subject to authorise — to authorised "
        "scrutiny only, and that public access posed a risk. The department chair signed off "
        "without argument. I was told to remove the files from the open collection and transfer "
        "them to a restricted vault.\""
    )

    passage_2 = (
        "Lena sat very still. \"Did Hale say what specifically was dangerous about my father's "
        "work?\"\n\n"
        "Torres shook her head. \"He did not explain. He simply presented the order and expected "
        "compliance. I asked questions, but he made it clear that further inquiry was not welcome. "
        "He implied that the university could face consequences — funding reviews, audits — if "
        "anyone resisted. It was not an allegation of wrongdoing, exactly. It was more like a "
        "quiet threat.\"\n\n"
        "\"And no one pushed back?\"\n\n"
        "\"The department chair at the time was close to retirement. He did not want trouble. "
        "And Hale's jurisdiction seemed broad enough that no one was sure how far his authority "
        "extended.\" Torres opened a drawer and took out a small object — a USB drive, plain "
        "and unmarked. She placed it on the desk between them.\n\n"
        "\"Before the files were confiscate — confiscated and moved to the vault, I made a copy "
        "of certain materials. Notes, data fragments, personal correspondence. It was a covert "
        "decision — I told no one. I kept the drive in my personal safe at home for eight years.\" "
        "She pushed it toward Lena. \"I think your father would have wanted you to have this.\"\n\n"
        "Lena picked up the drive. It weighed almost nothing, but it felt heavy in her hand."
    )

    passage_3 = (
        "Lena drove home in silence, the USB drive in her jacket pocket. Her apartment was a "
        "small one-bedroom unit on the edge of town, sparsely furnished — a desk, a bookshelf, "
        "a narrow bed. She locked the door behind her, sat down at her laptop, and inserted the "
        "drive.\n\n"
        "The contents were disorganised — dozens of folders with dates for names, containing "
        "scanned pages, typed notes, and data files in formats she did not immediately recognise. "
        "She began with the most recent folder and worked backward. Her father's handwriting was "
        "small and careful, each page covered in dense annotation. He had been meticulous in his "
        "record-keeping, even when writing quickly.\n\n"
        "The early files described routine observations — hydrogen emission surveys, pulsar "
        "timing studies, equipment calibration logs. But as she moved deeper into the archive, "
        "the tone shifted. The notes became more urgent, the language more guarded. References "
        "to a specific signal began appearing, always described in cautious terms. He never named "
        "it directly. Instead, he used a personal code — Greek letters and numbers that she would "
        "need to decrypt before she could understand the full picture.\n\n"
        "Some pages showed signs of deterioration — water damage, faded ink, torn edges — as "
        "though they had been stored carelessly before Torres rescued them. The correspondence "
        "between her father and an unnamed colleague hinted at growing alarm."
    )

    passage_4 = (
        "It took Lena two hours to piece together the core of her father's research. The coded "
        "references, once she recognised the pattern, were not difficult to read. Marco Vasquez "
        "had detected a structured radio signal from the same region of sky — the same coordinates "
        "in Lyra — fifteen years ago. He had recorded it over a period of several weeks, using "
        "the same apparatus at Cerro Alto that Lena now operated.\n\n"
        "His data showed the same characteristics she had observed: a narrow-band transmission "
        "with a repeating pulse structure, stable over time, with no natural explanation. He had "
        "even identified the prime number sequence, though his notation described it differently "
        "— as a 'nested arithmetic progression' rather than a simple prime series.\n\n"
        "But what struck Lena most was not the similarity of the findings. It was the fact that "
        "her father had tried to replicate the detection using a second receiver at a partner "
        "observatory in Chile, and had succeeded. The signal was real. It was consistent. And "
        "fifteen years ago, someone had known about it — and had chosen to make it disappear.\n\n"
        "She sat back in her chair and stared at the screen. The wavelength data matched her own "
        "recordings almost exactly. Her father had found the same thing she had found. And then "
        "his work had been buried."
    )

    passage_5 = (
        "The last file on the drive was dated three months before her father's death. It was a "
        "single page — not a research note but a personal message, typed rather than handwritten. "
        "The tone was different from everything else in the archive. It was direct, almost raw, "
        "stripped of the careful academic language that characterised his other writing.\n\n"
        "\"If you are reading this,\" it began, \"then someone has found these files, and I am "
        "no longer able to protect them myself. What I have documented here is real. The signal "
        "is real. I have verified it independently, and I am certain of its origin. But there "
        "are people who do not want this known. They came to me with urgency and told me to stop. "
        "I refused. I do not know what will happen next, but I want to leave this testimony for "
        "whoever comes after me.\"\n\n"
        "Lena's hands were trembling. She read the final lines slowly.\n\n"
        "\"They will come for this. Do not let them bury it again. The confrontation is "
        "inevitable — they will try to silence you as they silenced me. But the signal does not "
        "belong to any government or agency. It belongs to all of us. Protect it.\"\n\n"
        "She closed the laptop and sat in the dark for a long time. Outside, the desert wind "
        "pressed against the windows. Her father had known. He had found exactly what she had "
        "found — and it had cost him everything."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- English metadata ---

    preview_text = (
        "Lena returns to the university library to meet Dr. Torres during office hours. Torres "
        "reveals that a government official named Director Hale visited eight years ago and "
        "ordered Marco Vasquez's research files sealed under national security grounds. Before "
        "the files were taken, Torres secretly copied key materials onto a USB drive, which she "
        "now gives to Lena. Back at her apartment, Lena reads her father's notes and discovers "
        "he detected the same signal fifteen years ago — and was told to stop. His final entry "
        "is a warning: they will come for this. In this chapter, you will encounter 20 vocabulary "
        "words woven into the story: apprehensive, comply, authorise, scrutiny, confiscate, "
        "allegation, covert, jurisdiction, decrypt, annotation, deterioration, correspondence, "
        "replicate, apparatus, wavelength, notation, urgency, testimony, inevitable, confrontation. "
        "Across five passages and six learning sessions, you will reinforce familiar vocabulary "
        "and follow Lena as the stakes of her discovery become terrifyingly clear."
    )

    description = (
        "Chapter 4 follows Lena to Dr. Torres's office, where she learns a government liaison "
        "sealed her father's files. Torres gives her a secret USB copy. Lena discovers her father "
        "found the same signal 15 years ago — and left a warning."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "The Signal Beyond \u2014 Chapter 4: The Warning",
        "language": "en",
        "userLanguage": "en",
        "level": "upperintermediate",
        "audioSpeed": -0.2,
        "preview": {
            "text": preview_text
        },
        "description": description,
        "learningSessions": []
    }

    # --- Helper to build sessions 1-5 ---
    passages = [passage_1, passage_2, passage_3, passage_4, passage_5]
    vocab_groups = [vocab_1, vocab_2, vocab_3, vocab_4, vocab_5]

    session_topics = [
        "The Sealed Order",
        "The Secret Copy",
        "Reading the Notes",
        "The Same Signal",
        "The Final Warning"
    ]

    for i in range(5):
        session_num = i + 1
        vocab = vocab_groups[i]
        passage = passages[i]
        topic = session_topics[i]
        desc_preview = passage[:80].rstrip() + "..."

        session = {
            "title": f"Session {session_num}",
            "activities": [
                {
                    "activityType": "viewFlashcards",
                    "title": f"Flashcards: {topic}",
                    "description": f"Learn 4 words: {', '.join(vocab)}",
                    "practiceMinutes": 2,
                    "data": {
                        "vocabList": vocab,
                        "audioSpeed": -0.2
                    }
                },
                {
                    "activityType": "reading",
                    "title": f"Read: {topic}",
                    "description": desc_preview,
                    "practiceMinutes": 5,
                    "data": {
                        "text": passage,
                        "audioSpeed": -0.2
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": f"Listen: {topic}",
                    "description": "Listen to the passage and follow along.",
                    "practiceMinutes": 5,
                    "data": {
                        "text": passage,
                        "audioSpeed": -0.2
                    }
                }
            ]
        }
        curriculum["learningSessions"].append(session)

    # --- Session 6: Review ---
    review_session = {
        "title": "Review",
        "activities": [
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Review all vocabulary",
                "description": f"Learn 20 words: {', '.join(all_vocab)}",
                "practiceMinutes": 5,
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Listen: Full Chapter",
                "description": "Listen to the full chapter and follow along.",
                "practiceMinutes": 15,
                "data": {
                    "text": full_chapter_text,
                    "audioSpeed": -0.2
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
