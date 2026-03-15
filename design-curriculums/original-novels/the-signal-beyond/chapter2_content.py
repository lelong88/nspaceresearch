"""
Chapter 2: The Archive
Setup continues — Lena drives to the university, reviews data with Raj, discovers her father's
redacted files, and meets Dr. Elena Torres, the archive librarian.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 2."""

    # --- Vocabulary: 20 B2-level words, 4 per passage ---
    vocab_1 = ["corridor", "retrieve", "meticulous", "anticipation"]
    vocab_2 = ["verify", "legitimate", "peculiar", "consensus"]
    vocab_3 = ["classified", "redacted", "deteriorate", "fragment"]
    vocab_4 = ["discreet", "implication", "reluctant", "archive"]
    vocab_5 = ["intuition", "obscure", "revelation", "unsettle"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-290 words each, B2-level prose) ---

    passage_1 = (
        "Lena barely slept. By seven in the morning she was already driving east along the "
        "desert highway, her laptop bag on the passenger seat and a thermos of cold coffee wedged "
        "between her knees. The sun climbed fast over the mesas, flooding the car with pale gold "
        "light, but she hardly noticed. Her mind was still turning over the data from the night "
        "before, replaying every graph and every timestamp.\n\n"
        "The university campus was quiet at this hour. She parked near the physics building and "
        "walked through the long corridor that led to Raj's office, her footsteps echoing on the "
        "polished floor. She had sent him the complete dataset overnight, but she needed to see "
        "his face when he looked at it properly — needed to know whether his reaction matched "
        "her own.\n\n"
        "Raj was already at his desk, two monitors glowing with spectral plots. He glanced up "
        "when she entered but did not smile. That was a good sign. It meant he was taking it "
        "seriously. Lena set her bag down and pulled a chair beside him, feeling a sharp sense "
        "of anticipation. She had spent the drive preparing herself for disappointment — for Raj "
        "to find some meticulous error she had overlooked, some ordinary explanation that would "
        "make the whole thing collapse. But she also knew, deep down, that she wanted him to "
        "retrieve the same conclusion she had reached alone in the dark."
    )

    passage_2 = (
        "They worked side by side for two hours, barely speaking. Raj ran his own analysis "
        "software, cross-referencing the signal against every catalogue of known sources he could "
        "access. He checked solar activity logs, satellite schedules, and atmospheric data from "
        "the previous night. Each time he eliminated a possibility, he made a small mark in his "
        "notebook.\n\n"
        "Finally, he leaned back in his chair and rubbed his eyes. \"I cannot find a conventional "
        "explanation,\" he said quietly. \"The pattern is too regular to be natural noise, and it "
        "does not match anything in the database. If your equipment readings are accurate — and I "
        "have no reason to doubt them — then this is legitimate.\"\n\n"
        "Lena exhaled slowly. \"So we have consensus?\"\n\n"
        "\"We have agreement between two scientists, which is not quite the same thing.\" He gave "
        "her a careful look. \"Before we tell anyone else, we need to verify the signal is still "
        "active tonight. One detection is interesting. Two detections in a row would be peculiar "
        "enough to justify a formal report.\"\n\n"
        "Lena nodded. She understood the caution. In their field, reputations could be destroyed "
        "by a single premature announcement. They agreed to observe together that evening and "
        "keep the findings between themselves until then."
    )

    passage_3 = (
        "After leaving Raj's office, Lena crossed the campus toward the Hargrove Library. The "
        "building was old — red brick with narrow windows — and housed the university's special "
        "collections on the third floor. She had not visited in years, but the thought had been "
        "growing since last night: her father, Dr. Marco Vasquez, had spent the final decade of "
        "his career studying deep-space radio emissions from the same region of sky. His research "
        "files were supposed to be stored here.\n\n"
        "The reading room was cool and dim. Rows of metal shelving held boxes of papers, old "
        "hard drives, and bound journals. Lena found the section labelled V and located her "
        "father's name on three grey boxes. She carried them to a table and opened the first.\n\n"
        "What she found made her stomach tighten. The files were incomplete. Entire sections had "
        "been redacted — pages removed, folders emptied, labels crossed out with black ink. Notes "
        "that should have contained raw data held only fragment after fragment of disconnected "
        "sentences. It looked as though someone had gone through the collection systematically "
        "and stripped out anything of substance. The remaining pages were beginning to deteriorate "
        "at the edges, yellowed and brittle, as if they had been classified and then abandoned "
        "rather than properly preserved."
    )

    passage_4 = (
        "Lena was still staring at the half-empty boxes when a voice spoke from behind her.\n\n"
        "\"You must be Marco's daughter.\"\n\n"
        "She turned. A woman in her late fifties stood at the end of the table, holding a stack "
        "of cataloguing cards. She had silver-streaked hair pulled back in a loose knot and wore "
        "reading glasses on a chain around her neck. Her expression was calm but watchful.\n\n"
        "\"I am Dr. Elena Torres. I manage the archive and special collections.\" She set the "
        "cards down and studied Lena with quiet attention. \"I remember your father. He was a "
        "discreet man. Very careful about who saw his work.\"\n\n"
        "\"Someone removed half his files,\" Lena said, not bothering to hide her frustration.\n\n"
        "Torres nodded slowly. \"Yes. About eight years ago, a formal request came through to "
        "have certain materials sealed. I was reluctant to approve it, but the authorisation came "
        "from the department chair at the time. I had no grounds to refuse.\"\n\n"
        "\"Who made the request?\"\n\n"
        "Torres hesitated. The implication of her silence was clear — she knew more than she was "
        "willing to say in a public reading room. \"That information is not something I can share "
        "here,\" she said carefully. \"But if you come back during my office hours, we might have "
        "a more productive conversation.\""
    )

    passage_5 = (
        "Lena drove back toward the observatory as the afternoon light turned amber across the "
        "desert. Her mind was crowded with questions. Why had her father's files been sealed? Who "
        "had authorised it, and what were they trying to hide? She had always assumed his research "
        "was ordinary — important to specialists, perhaps, but not the kind of work that attracted "
        "secrecy.\n\n"
        "Now she was not so sure. Her intuition told her that the signal she had detected and her "
        "father's missing research were connected, though she could not yet see how. The obscure "
        "region of sky where the signal originated was the same area Marco Vasquez had studied for "
        "years. That could not be coincidence.\n\n"
        "She thought about Elena Torres — the careful way the librarian had chosen her words, the "
        "guarded look in her eyes. Torres had all but promised a revelation if Lena returned. "
        "Whether that promise was genuine or simply a way to manage an upset visitor, Lena could "
        "not tell.\n\n"
        "By the time she reached the observatory, the first stars were appearing above the ridge. "
        "Raj would arrive in an hour for their second observation. She unlocked the control room "
        "and powered up the array, trying to focus on the task ahead. But the image of those "
        "empty folders continued to unsettle her, lingering at the edge of every thought."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- English metadata ---

    preview_text = (
        "The morning after her extraordinary discovery, Lena drives to the university to share "
        "the data with her colleague Raj. Together they confirm the signal is genuinely anomalous "
        "— no known natural or artificial source can explain it. But Lena's investigation takes "
        "an unexpected turn when she visits the university archive to examine her late father's "
        "research files. Entire sections have been removed, pages redacted, and folders emptied. "
        "She meets Dr. Elena Torres, the archive librarian, who hints that someone deliberately "
        "sealed the files years ago. In this chapter, you will encounter 20 vocabulary words "
        "woven into the story: corridor, retrieve, meticulous, anticipation, verify, legitimate, "
        "peculiar, consensus, classified, redacted, deteriorate, fragment, discreet, implication, "
        "reluctant, archive, intuition, obscure, revelation, unsettle. Across five passages and "
        "six learning sessions, you will reinforce familiar vocabulary through compelling science "
        "fiction prose and follow Lena deeper into a mystery that reaches back into her own past."
    )

    description = (
        "Chapter 2 follows Lena to the university where she and Raj confirm the signal is real. "
        "She then discovers that her late father's research files have been partially redacted, "
        "and meets Dr. Elena Torres, who knows more than she reveals."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "The Signal Beyond \u2014 Chapter 2: The Archive",
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
        "Morning at the University",
        "Confirming the Data",
        "The Missing Files",
        "The Librarian",
        "More Questions Than Answers"
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
