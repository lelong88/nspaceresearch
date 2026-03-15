"""
Chapter 3: The Second Night
Setup deepens — Lena and Raj observe together at the observatory. The signal is stronger.
Lena tells Raj about her father's sealed files. Late at night, she discovers a repeating
mathematical sequence embedded in the signal's pattern.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 3."""

    # --- Vocabulary: 20 B2-level words, 4 per passage ---
    vocab_1 = ["illuminate", "precise", "interval", "resolve"]
    vocab_2 = ["fluctuate", "duration", "adjacent", "configuration"]
    vocab_3 = ["conceal", "integrity", "suppress", "contradiction"]
    vocab_4 = ["sequence", "embed", "deliberate", "recur"]
    vocab_5 = ["profound", "isolation", "certainty", "overwhelming"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-290 words each, B2-level prose) ---

    passage_1 = (
        "Raj arrived at the observatory just after nine, carrying a bag of equipment and a "
        "paper cup of tea that had long since gone cold. The sky was clear — no clouds, no moon, "
        "just a vast black canvas scattered with stars. Lena met him at the entrance and led him "
        "inside without small talk. They both understood what was at stake.\n\n"
        "She had spent the afternoon preparing the array, running every check she could think of "
        "to ensure the readings would be precise. If the signal appeared again tonight, there "
        "could be no question about the data. Raj set up his own laptop beside hers and connected "
        "to the receiver feed. For a few minutes they worked in silence, adjusting filters and "
        "setting recording parameters.\n\n"
        "At nine forty-two, the signal appeared. It came in at the same frequency band as the "
        "previous night, but this time the waveform was stronger — the peaks sharper, the pattern "
        "more defined. The monitors seemed to illuminate with new energy as the data streamed in. "
        "Raj leaned forward, his expression unreadable. Lena watched the interval between each "
        "pulse, counting silently. The spacing was identical to what she had recorded twenty-four "
        "hours earlier. Whatever this was, it had not changed. It had not moved. It was waiting "
        "for them, steady and patient, like a lighthouse beam sweeping across an empty ocean. "
        "She felt her resolve harden. Tonight, they would record everything."
    )

    passage_2 = (
        "They recorded for three hours without interruption. The signal held steady throughout, "
        "never dropping below detection level, never shifting in frequency. Raj monitored the "
        "amplitude readings while Lena tracked the waveform structure, watching the signal "
        "fluctuate only slightly around its central value. There were small variations — tiny dips and rises that "
        "might mean nothing or might mean everything — but the core signal remained constant.\n\n"
        "\"The duration of each pulse is remarkably stable,\" Raj said, scrolling through the "
        "data on his screen. \"Less than a millisecond of variation over three hours. Natural "
        "sources do not behave like this.\"\n\n"
        "Lena nodded. She had been thinking the same thing. She pulled up a map of the sky and "
        "marked the signal's origin point. It sat in the same empty region as before — no "
        "catalogued objects, no adjacent stars bright enough to produce radio emissions. The "
        "configuration of the nearest stellar systems offered no obvious explanation.\n\n"
        "\"Two nights in a row,\" she said quietly. \"Same location, same structure, same "
        "timing.\"\n\n"
        "Raj removed his glasses and cleaned them slowly, a habit he had when he was thinking "
        "hard. \"We should consider writing a preliminary internal report. Not for publication "
        "— just for the department. Something on record.\"\n\n"
        "\"Not yet,\" Lena said. \"Not until we understand what we are looking at.\""
    )

    passage_3 = (
        "Around one in the morning, they took a break. Lena made coffee in the small kitchen "
        "at the back of the control room while Raj stretched his legs outside, walking along "
        "the gravel path that circled the base of the dish. When he came back in, she handed "
        "him a mug and sat down across from him at the folding table.\n\n"
        "\"There is something else I need to tell you,\" she said. \"Yesterday I went to the "
        "university library. I looked for my father's research files — his work on deep-space "
        "radio emissions.\"\n\n"
        "Raj raised an eyebrow. \"And?\"\n\n"
        "\"They have been gutted. Someone went through the collection and removed anything of "
        "substance. Pages torn out, data missing, entire folders empty. It looked like someone "
        "was trying to conceal whatever he had found.\"\n\n"
        "Raj set his mug down carefully. \"That is a serious claim, Lena.\"\n\n"
        "\"I know. But the integrity of the archive has clearly been compromised. The librarian "
        "— Dr. Torres — confirmed that a formal request was made to suppress certain materials "
        "about eight years ago. She would not say who made the request.\"\n\n"
        "Raj was quiet for a long moment. \"Your father studied the same region of sky.\"\n\n"
        "\"Exactly the same region.\"\n\n"
        "He looked at her steadily. \"That is either a remarkable coincidence or a very "
        "troubling contradiction — because if he found something similar, why is there no "
        "record of it?\""
    )

    passage_4 = (
        "Raj left shortly after two, promising to return the following evening. Lena walked him "
        "to his car and watched his tail lights disappear down the mountain road. Then she went "
        "back inside.\n\n"
        "The signal was still active. She sat down at her workstation and began reviewing the "
        "night's recordings, scrolling through hours of waveform data. She was tired, but her "
        "mind refused to rest. Something about the pattern had been bothering her — a subtle "
        "regularity beneath the main pulse that she had not had time to examine closely.\n\n"
        "She isolated a ten-minute segment and expanded the waveform on her largest monitor. "
        "Then she saw it. Buried within the signal's noise floor, there was a secondary pattern "
        "— a sequence of short and long pulses that repeated every ninety-three seconds. She "
        "ran a frequency analysis and confirmed it: the pulses were not random. They followed "
        "a mathematical progression — prime numbers, spaced in groups of three, with a deliberate "
        "pause between each set.\n\n"
        "Lena stared at the screen. Prime numbers did not occur naturally in radio signals. They "
        "did not recur in atmospheric noise or stellar emissions. A prime number sequence embedded "
        "in a deep-space transmission meant one thing and one thing only: intelligence. Someone "
        "— or something — had placed it there on purpose."
    )

    passage_5 = (
        "She sat motionless for a long time. The control room hummed around her — the soft whir "
        "of cooling fans, the occasional click of a hard drive, the low electrical murmur of "
        "machines that never slept. Outside, the desert was perfectly still. There was no wind "
        "tonight, no coyotes, nothing but the profound silence of a landscape that stretched "
        "for hundreds of kilometres in every direction.\n\n"
        "Lena looked at the data on her screen and felt the weight of what she had found settle "
        "over her like a physical thing. This was not a hardware fault. This was not interference "
        "from a satellite or a military installation. This was a structured, repeating message "
        "from forty-two light-years away, and she was the only person on Earth who knew about "
        "the mathematical pattern hidden inside it.\n\n"
        "The isolation of the moment was almost unbearable. She wanted to call Raj, to call "
        "anyone, but it was nearly three in the morning and she needed to be certain before she "
        "spoke. Certainty required more analysis, more data, more time. She saved the files to "
        "every drive she had and began writing notes in her logbook, her handwriting tight and "
        "fast.\n\n"
        "The signal pulsed on, steady and patient. Lena sat alone in the dark, staring at a "
        "pattern that should not exist, feeling the overwhelming reality of it press against "
        "everything she thought she knew about the universe."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- English metadata ---

    preview_text = (
        "On the second night, Lena and Raj observe together at the Cerro Alto Observatory. The "
        "signal is still there — stronger and more defined than before. They record hours of "
        "data, confirming it is no accident. During a break, Lena reveals what she found in the "
        "university archive: her father's research files have been gutted, his work deliberately "
        "concealed. After Raj leaves, Lena makes a discovery that changes everything — a "
        "repeating mathematical sequence of prime numbers embedded deep within the signal. "
        "In this chapter, you will encounter 20 vocabulary words woven into the story: "
        "illuminate, precise, interval, resolve, fluctuate, duration, adjacent, configuration, "
        "conceal, integrity, suppress, contradiction, sequence, embed, deliberate, recur, "
        "profound, isolation, certainty, overwhelming. Across five passages and six learning "
        "sessions, you will reinforce familiar vocabulary through gripping science fiction "
        "prose and follow Lena to a revelation she cannot share with anyone — not yet."
    )

    description = (
        "Chapter 3 follows Lena and Raj through a second night of observation. The signal is "
        "stronger. Lena tells Raj about her father's sealed files. Alone after midnight, she "
        "discovers a prime number sequence embedded in the signal — proof of intelligence."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "The Signal Beyond \u2014 Chapter 3: The Second Night",
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
        "The Signal Returns",
        "Recording the Data",
        "The Sealed Files",
        "The Hidden Pattern",
        "Alone in the Dark"
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
