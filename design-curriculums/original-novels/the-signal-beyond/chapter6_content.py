"""
Chapter 6: The Pattern
Rising action, complications and new discoveries — Mara makes a breakthrough: the signal's
layered structure contains a coordinate system pointing to specific locations on Earth,
including the Cerro Alto Observatory itself. Meanwhile, Lena notices a black SUV parked near
the observatory entrance for the second day in a row. Raj discovers someone has been accessing
the observatory's network remotely. The team decides to move their data to an offline system.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 6."""

    # --- Vocabulary: 20 B2-level words, 4 per passage ---
    vocab_1 = ["correlate", "terrestrial", "longitude", "latitude"]
    vocab_2 = ["anomalous", "perimeter", "conspicuous", "discretion"]
    vocab_3 = ["breach", "proxy", "intercept", "audit"]
    vocab_4 = ["safeguard", "partition", "migrate", "redundant"]
    vocab_5 = ["precaution", "volatile", "imperative", "solidarity"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-290 words each, B2-level prose) ---

    passage_1 = (
        "Mara had been working for three days straight, sleeping in short bursts on the old sofa "
        "in the secondary control room. Her laptop screen was covered in overlapping windows — "
        "graphs, tables, frequency maps, and lines of code she had written to pull apart the "
        "signal's deepest layers. Lena brought her coffee and a sandwich around noon, but Mara "
        "barely looked up.\n\n"
        "\"I think I have found something,\" Mara said, her voice flat with exhaustion. \"The "
        "third layer — the one I could not identify before — it is not random structure. It is "
        "a coordinate system.\"\n\n"
        "Lena set the coffee down and leaned over Mara's shoulder. On the screen was a grid of "
        "paired values, extracted from the repeating clusters in the signal. Mara had mapped "
        "each pair to a point on a sphere, and the result was unmistakable: the values appeared "
        "to correlate with positions on a planetary surface.\n\n"
        "\"These are terrestrial coordinates,\" Mara continued, pointing at the screen. \"Each "
        "pair gives a longitude and a latitude. There are seven locations in total, spread "
        "across four continents.\"\n\n"
        "Lena stared at the map. Seven red dots glowed on a projection of the Earth — one in "
        "the mountains of New Mexico, one in the Chilean Andes, one in central Australia, one "
        "in northern India, one in West Africa, one in Scandinavia, and one in eastern Siberia.\n\n"
        "\"The first coordinate,\" Mara said quietly, \"is this observatory.\""
    )

    passage_2 = (
        "Lena stepped outside to clear her head. The afternoon sun was fierce, and the desert "
        "shimmered in every direction. She walked along the gravel path toward the main gate, "
        "trying to process what Mara had shown her. A signal from forty-two light-years away "
        "that contained the exact location of the place where it was being received — the "
        "implications were staggering.\n\n"
        "She stopped at the edge of the car park and looked toward the access road. A black SUV "
        "was parked about fifty metres from the observatory entrance, just off the shoulder of "
        "the road. She had noticed it yesterday as well — same vehicle, same position, facing "
        "the gate. It was anomalous. The observatory sat on a remote ridge with no reason for "
        "anyone to park there unless they had business inside.\n\n"
        "Lena walked closer, staying on the perimeter of the car park. The SUV's windows were "
        "tinted dark, and she could not see inside. There were no markings on the vehicle — no "
        "government plates, no university stickers, nothing. It was conspicuous precisely because "
        "it was trying not to be.\n\n"
        "She turned back toward the building, keeping her pace steady. She did not want to show "
        "that she had noticed. Discretion, she reminded herself, was more useful than confrontation "
        "right now. But her pulse was faster than it should have been."
    )

    passage_3 = (
        "Back inside, Lena found Raj in the main control room, reviewing the observatory's "
        "system logs on one of the administrative terminals. He looked up when she entered, and "
        "his expression told her something was wrong before he spoke.\n\n"
        "\"We have a problem,\" he said. \"I was checking the network activity reports — something "
        "I do routinely as part of my maintenance duties. There has been a breach. External "
        "connections to our data servers over the past five days — someone has been downloading "
        "observation logs, receiver configurations, and scheduling records.\"\n\n"
        "\"From where?\"\n\n"
        "\"The connections route through a proxy server in Virginia. I cannot trace them further "
        "without better tools, but the pattern is clear — someone is pulling data from our "
        "systems remotely, and they have been doing it since the night you first detected the "
        "signal.\"\n\n"
        "Lena felt cold despite the heat outside. \"Could it be routine? An automatic backup or "
        "a university audit?\"\n\n"
        "Raj shook his head. \"University systems do not route through Virginia. And the files "
        "being accessed are not administrative — they are raw observation data. Whoever is doing "
        "this knows exactly what to look for. They are trying to intercept our recordings.\"\n\n"
        "\"There is a black SUV parked outside,\" Lena said. \"It has been there for two days. "
        "No one signed the visitor log.\"\n\n"
        "Raj closed his laptop slowly. \"Then we need to assume we are being watched.\""
    )

    passage_4 = (
        "They called Mara into the main control room and explained the situation. She listened "
        "without interrupting, her arms crossed, her expression shifting from concentration to "
        "something harder — a quiet anger that Lena had not seen in her before.\n\n"
        "\"If they are pulling data from the network, then nothing stored on these servers is "
        "safe,\" Mara said. \"We need to safeguard everything we have collected — the raw signal "
        "recordings, my analysis files, the coordinate data. All of it needs to move off the "
        "network immediately.\"\n\n"
        "\"I have three external drives,\" Lena said. \"We can partition the data across them — "
        "one copy of the raw recordings, one copy of the analysis, one complete backup.\"\n\n"
        "\"And then we migrate the working files to a machine that has never been connected to "
        "the internet,\" Mara added. \"I have an old laptop in my office at the university. No "
        "wireless card, no Bluetooth. It is completely air-gapped.\"\n\n"
        "Raj nodded. \"We should also delete the copies on the observatory servers. If they are "
        "downloading our data, we need to make sure there is nothing redundant left for them to "
        "find.\"\n\n"
        "\"Agreed,\" Lena said. \"But we need to be careful about how we do it. If we suddenly "
        "wipe the servers, whoever is watching will know we are aware of them. We need to make "
        "it look like routine maintenance.\""
    )

    passage_5 = (
        "They worked through the evening in careful, measured steps. Raj handled the server-side "
        "cleanup, deleting files in small batches and replacing them with dummy data that would "
        "look normal to anyone monitoring the network. Mara copied her analysis onto the external "
        "drives while Lena kept watch on the building's internal cameras, checking for any sign "
        "that someone had entered the facility.\n\n"
        "By ten o'clock, the transfer was complete. Lena locked the drives in the bottom drawer "
        "of her desk — a temporary measure until Mara could bring the air-gapped laptop. Every "
        "precaution they took felt both necessary and insufficient. The situation was volatile, "
        "and they all knew it.\n\n"
        "\"The coordinates change everything,\" Mara said as they sat together in the dim light "
        "of the secondary control room. \"If the signal really does point to seven locations on "
        "Earth, then whoever sent it knew about us — about this planet, about specific places "
        "on it. That is not a general broadcast. That is a targeted message.\"\n\n"
        "\"Which makes protecting the data imperative,\" Raj said quietly. \"If someone in our "
        "own government is already trying to suppress this, imagine what happens when they "
        "realise we have decoded the coordinates.\"\n\n"
        "Lena looked at both of them — Mara with her sharp eyes and restless energy, Raj with "
        "his careful logic and steady hands. They were three people against something much larger "
        "than themselves. But there was a solidarity between them now that had not been there "
        "before — a shared understanding that they would see this through, whatever came next."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- English metadata ---

    preview_text = (
        "Mara makes a stunning breakthrough — the signal's deepest layer contains a coordinate "
        "system pointing to seven specific locations on Earth, and one of them is the Cerro Alto "
        "Observatory itself. But the discovery comes with danger. Lena notices a black SUV parked "
        "near the entrance for the second day running, and Raj finds that someone has been "
        "remotely accessing the observatory's network, downloading raw observation data. The team "
        "realises they are under surveillance and decides to move all sensitive data to an offline "
        "system. In this chapter, you will encounter 20 vocabulary words woven into the story: "
        "correlate, terrestrial, longitude, latitude, anomalous, perimeter, conspicuous, "
        "discretion, breach, proxy, intercept, audit, safeguard, partition, migrate, redundant, "
        "precaution, volatile, imperative, solidarity. Across five passages and six learning "
        "sessions, you will build reading fluency and follow the team as the stakes rise sharply."
    )

    description = (
        "Chapter 6 follows the team as Mara decodes Earth coordinates from the signal — including "
        "the observatory itself. Lena spots a suspicious vehicle outside, and Raj discovers their "
        "network has been compromised. They move their data offline to protect it."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "The Signal Beyond \u2014 Chapter 6: The Pattern",
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
        "The Coordinate Breakthrough",
        "The Black SUV",
        "Network Intrusion",
        "Going Offline",
        "A Targeted Message"
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
