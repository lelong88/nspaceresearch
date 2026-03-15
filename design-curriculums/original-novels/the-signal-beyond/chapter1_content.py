"""
Chapter 1: The Frequency
Setup chapter — introduces Lena Vasquez, the Cerro Alto Observatory, and the anomalous signal.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 1."""

    # --- Vocabulary: 20 B2-level words, 4 per passage ---
    vocab_1 = ["anomaly", "frequency", "calibrate", "persistent"]
    vocab_2 = ["spectrum", "transmission", "faint", "coordinates"]
    vocab_3 = ["hypothesis", "interference", "diagnostic", "threshold"]
    vocab_4 = ["skeptical", "colleague", "preliminary", "deviation"]
    vocab_5 = ["compelling", "ambient", "magnitude", "surveillance"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-290 words each, B2-level prose) ---

    passage_1 = (
        "The Cerro Alto Observatory sat on a ridge above the desert, where the air was thin "
        "and the sky stretched endlessly in every direction. Lena Vasquez had worked here for "
        "four years, spending most of her nights alone with the hum of machines and the slow "
        "rotation of the radio dish overhead. She preferred it that way. The solitude gave her "
        "space to think, and thinking was what she did best.\n\n"
        "Tonight, the equipment was behaving strangely. A persistent signal had appeared on her "
        "monitor around midnight — a narrow band of noise that refused to disappear. She leaned "
        "forward and adjusted the display, watching the waveform repeat with unsettling regularity. "
        "It was not random. It was not a glitch.\n\n"
        "Lena reached for her logbook and noted the time. She would need to calibrate the receiver "
        "again to rule out hardware error, but something in her gut told her this was different. "
        "In her years of scanning deep space, she had encountered plenty of false alarms — solar "
        "bursts, satellite reflections, atmospheric distortion. But this signal had a frequency "
        "she had never seen before. It sat in a part of the spectrum that was supposed to be silent.\n\n"
        "She pulled up the anomaly detection software and let it run. Whatever this was, she "
        "intended to find out."
    )

    passage_2 = (
        "The analysis took nearly an hour. Lena sat motionless at her desk, watching numbers scroll "
        "across the screen while the mountains outside turned from black to deep blue. The software "
        "confirmed what she had suspected: the signal did not match any known natural source. It was "
        "not a pulsar, not a quasar, not hydrogen emission from a distant galaxy. The transmission "
        "was structured — repeating at precise intervals with a pattern that suggested intention.\n\n"
        "She checked the coordinates. The signal originated from a region of space between two "
        "unremarkable stars in the constellation Lyra, roughly forty-two light-years away. There "
        "was nothing catalogued at that location — no known objects, no previous detections. The "
        "spectrum analysis showed a clean, narrow band with almost no background noise, which was "
        "itself extraordinary. Natural signals were messy. This one was faint but remarkably clean.\n\n"
        "Lena saved the data to three separate drives. She had learned long ago that extraordinary "
        "claims required extraordinary evidence, and she was not about to lose a single byte. Her "
        "hands trembled slightly as she labelled the files. She told herself it was the cold."
    )

    passage_3 = (
        "Before making any calls, Lena ran a full diagnostic on the receiver array. She checked "
        "every cable, every connection, every amplifier in the signal chain. If there was a fault "
        "somewhere — a loose connector, a damaged filter — she needed to know before she told "
        "anyone what she had found. The last thing she wanted was to announce a discovery only to "
        "retract it the next day.\n\n"
        "The diagnostic came back clean. Every component was functioning within normal parameters. "
        "She then tested for interference from terrestrial sources: mobile phone towers, military "
        "radar, weather satellites. Nothing matched. The signal's frequency sat well above the "
        "threshold of any known human-made transmission, in a band that international agreements "
        "reserved specifically for radio astronomy.\n\n"
        "Lena formed a working hypothesis. If the signal was not equipment error, not terrestrial "
        "interference, and not a recognised natural phenomenon, then it was either something "
        "entirely new to astrophysics or something deliberately sent. Both possibilities made her "
        "pulse quicken. She stared at the waveform on her screen, watching it repeat — steady, "
        "patient, as though it had been waiting a very long time to be heard."
    )

    passage_4 = (
        "At three in the morning, Lena picked up the phone and called Dr. Raj Patel. He answered "
        "on the fifth ring, his voice thick with sleep.\n\n"
        "\"Raj, I need you to look at something,\" she said, keeping her tone as neutral as she "
        "could manage.\n\n"
        "\"Lena, it is three a.m. Can it wait until morning?\"\n\n"
        "\"I do not think so.\"\n\n"
        "There was a pause. Raj was her closest colleague at the university, a careful scientist "
        "who distrusted excitement and valued preliminary data above all else. If anyone could "
        "find a flaw in her analysis, it was him.\n\n"
        "She sent him the files and waited. Twenty minutes later, he called back. His voice had "
        "changed — the sleepiness was gone, replaced by something cautious and alert.\n\n"
        "\"Where did you get this?\" he asked.\n\n"
        "\"Live capture. Tonight. The array picked it up around midnight.\"\n\n"
        "\"And you have ruled out equipment error?\"\n\n"
        "\"Full diagnostic. Everything is clean.\"\n\n"
        "Raj was quiet for a long moment. She could hear him breathing. \"I am skeptical, Lena. "
        "You know I have to be. But this deviation from the baseline — it is significant. I have "
        "never seen anything like it.\"\n\n"
        "\"Neither have I,\" she said."
    )

    passage_5 = (
        "After Raj hung up, Lena turned back to her monitors. The signal was still there, pulsing "
        "steadily in the darkness like a heartbeat from across the universe. She put on her "
        "headphones and listened to the audio conversion — a low, rhythmic tone that rose and fell "
        "with a compelling regularity. It was almost musical.\n\n"
        "Outside, the desert was silent except for the ambient sounds of wind and distant coyotes. "
        "The observatory's dish continued its slow sweep, but Lena had locked it onto the signal's "
        "source. She was not going to lose it. Not tonight.\n\n"
        "She thought about her father. Fifteen years ago, Dr. Marco Vasquez had worked at this "
        "same observatory, studying deep-space radio emissions. He had died before finishing his "
        "research, and his files had been archived — or so she had been told. She had never looked "
        "into them. There had never been a reason to.\n\n"
        "Now, sitting alone in the control room with a signal of unknown magnitude and origin "
        "filling her headphones, she wondered. The surveillance cameras on the wall blinked their "
        "red lights steadily. Dawn was still hours away. Lena opened a new notebook, wrote the "
        "date at the top, and began to document everything. She would not sleep tonight. She was "
        "certain of that."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])


    # --- English metadata ---

    preview_text = (
        "Late one night at a remote mountain observatory, radio astronomer Lena Vasquez detects "
        "a signal that defies explanation. It is not a pulsar, not a satellite, not interference "
        "— it is something structured, deliberate, and coming from deep space. As she races to "
        "verify her findings, she calls the one colleague she trusts, and together they confront "
        "a mystery that could change everything. In this opening chapter, you will encounter 20 "
        "vocabulary words woven naturally into the story: anomaly, frequency, calibrate, persistent, "
        "spectrum, transmission, faint, coordinates, hypothesis, interference, diagnostic, threshold, "
        "skeptical, colleague, preliminary, deviation, compelling, ambient, magnitude, surveillance. "
        "Across five reading passages and six learning sessions, you will reinforce familiar "
        "vocabulary through vivid science fiction prose, sharpen your reading fluency, and follow "
        "Lena into a discovery that will keep you turning pages."
    )

    description = (
        "Chapter 1 introduces Lena Vasquez, a radio astronomer who detects an anomalous deep-space "
        "signal during a late shift at the Cerro Alto Observatory. She runs diagnostics, rules out "
        "interference, and calls her colleague Dr. Raj Patel, who is skeptical but intrigued."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "The Signal Beyond \u2014 Chapter 1: The Frequency",
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
        "The Late Shift",
        "Analysing the Signal",
        "Ruling Out Error",
        "The Phone Call",
        "Listening in the Dark"
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
