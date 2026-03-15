"""
Chapter 5: The Team
Rising action begins — Lena decides she cannot do this alone. She shows Raj the prime number
sequence and her father's notes. Raj is shaken but agrees to help. They recruit Dr. Mara Chen,
a computational linguist who specialises in pattern recognition. The three begin working in
secret at the observatory, setting up a dedicated analysis station. Mara identifies additional
structure in the signal — it is not just primes, it is a layered encoding. The chapter ends
with the team energised but aware they are operating outside official channels.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 5."""

    # --- Vocabulary: 20 B2-level words, 4 per passage ---
    vocab_1 = ["collaborate", "expertise", "unconventional", "intricate"]
    vocab_2 = ["dedicate", "clandestine", "protocol", "vulnerable"]
    vocab_3 = ["decipher", "methodology", "rigorous", "convene"]
    vocab_4 = ["formidable", "encryption", "stratify", "autonomous"]
    vocab_5 = ["contingency", "consolidate", "pivotal", "endeavour"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-290 words each, B2-level prose) ---

    passage_1 = (
        "Lena met Raj in the university cafeteria the following afternoon. She had not slept "
        "since reading her father's final message, and the weight of it showed on her face. Raj "
        "was already seated at a corner table, two cups of coffee in front of him. He looked at "
        "her carefully as she sat down.\n\n"
        "\"You look terrible,\" he said.\n\n"
        "\"I need your help,\" she replied. \"Not just as a colleague. I need you to collaborate "
        "with me on something that could end both our careers.\"\n\n"
        "She placed the USB drive on the table between them and explained everything — the prime "
        "number sequence, Torres's visit, her father's sealed files, the warning. Raj listened "
        "without interrupting, his expression shifting from curiosity to disbelief to something "
        "harder to read. When she finished, he picked up the drive and turned it over in his "
        "fingers.\n\n"
        "\"Your father had the expertise to detect this fifteen years ago, and someone buried "
        "it,\" he said slowly. \"And now you have found it again.\"\n\n"
        "\"Yes. And I cannot do this alone. The signal is too intricate — there are layers I "
        "do not understand yet. I need someone with an unconventional approach to pattern "
        "analysis. Someone outside the astronomy department.\"\n\n"
        "Raj set the drive down. \"You are talking about Mara Chen.\"\n\n"
        "\"I am.\""
    )

    passage_2 = (
        "Dr. Mara Chen was a computational linguist at the university, known equally for her "
        "brilliance and her refusal to follow academic norms. She had published papers on pattern "
        "recognition in ancient scripts, machine translation of extinct languages, and the "
        "mathematical structures underlying human communication. She was also, according to "
        "departmental gossip, impossible to manage.\n\n"
        "Raj arranged a meeting at his apartment that evening. Mara arrived twenty minutes late, "
        "carrying a laptop under one arm and a paper bag of takeaway food under the other. She "
        "was tall, with short dark hair and sharp eyes that moved quickly around the room.\n\n"
        "\"Raj says you have something interesting,\" she said, sitting down without ceremony. "
        "\"I dedicate most of my time to interesting things, so this had better be worth it.\"\n\n"
        "Lena explained the situation again, this time more carefully. She described the signal, "
        "the prime sequence, and the clandestine nature of what they were doing. She made it "
        "clear that sharing this data violated observatory protocol and that anyone involved "
        "would be vulnerable to disciplinary action — or worse, if Director Hale's people were "
        "watching.\n\n"
        "Mara listened, ate a spring roll, and then opened her laptop. \"Show me the data,\" "
        "she said."
    )

    passage_3 = (
        "They worked through the night at Raj's kitchen table, the three of them hunched over "
        "laptops with the curtains drawn. Mara was fast — faster than Lena had expected. Within "
        "two hours, she had written a script to decipher the repeating structure of the signal "
        "and had begun mapping its internal patterns.\n\n"
        "\"Your prime sequence is real,\" Mara confirmed, scrolling through her results. \"But "
        "it is only the surface layer. Underneath, there is a second pattern — a set of grouped "
        "values that repeat at different intervals. The methodology I am using treats the signal "
        "as a linguistic object rather than a purely mathematical one. If someone designed this, "
        "they built it with layers.\"\n\n"
        "Raj leaned forward. \"Layers of what?\"\n\n"
        "\"Structure. Think of it like a sentence — the primes are the alphabet, but there is "
        "grammar underneath.\" Mara paused and looked at both of them. \"I want to be rigorous "
        "about this. I am not going to claim it is a message until I can prove it. But the "
        "patterns are not random.\"\n\n"
        "Lena felt something shift inside her — a sense of momentum she had not felt before. "
        "They needed a proper workspace. She suggested they convene at the observatory, where "
        "she could give them access to the raw data and the full processing power of the array."
    )

    passage_4 = (
        "The next evening, Lena let Raj and Mara into the observatory through a side entrance "
        "that was rarely monitored. She had prepared a workstation in the secondary control room "
        "— a small space behind the main operations centre that had not been used in years. She "
        "had cleaned it, connected three monitors, and routed a direct feed from the receiver "
        "array.\n\n"
        "\"This is our station,\" she said. \"No one comes back here. The security cameras cover "
        "the main corridor and the dish platform, but this room is a blind spot.\"\n\n"
        "Mara sat down and immediately began loading her analysis tools. \"The formidable thing "
        "about this signal is its encryption — not in the cryptographic sense, but in the way "
        "the information is packed. Each layer seems to stratify the data into categories. Primes "
        "on top, then grouped values, then something else I have not identified yet.\"\n\n"
        "\"How long will it take to map all the layers?\" Raj asked.\n\n"
        "\"Weeks, maybe. It depends on whether the structure is autonomous — self-contained — "
        "or whether it references external information we do not have.\" Mara glanced at Lena. "
        "\"Either way, we need uninterrupted access to this room.\"\n\n"
        "\"You will have it,\" Lena said. \"I control the schedule for the secondary systems. "
        "No one will question it.\""
    )

    passage_5 = (
        "By midnight, the three of them had established a routine. Mara ran her pattern analysis "
        "on the live feed while Raj cross-referenced the results against known astrophysical "
        "catalogues. Lena monitored the signal strength and kept watch on the observatory's "
        "internal communications to ensure no one noticed the extra activity.\n\n"
        "They worked well together. Mara was direct and impatient, but her instincts were sharp. "
        "Raj was methodical, always asking for evidence before accepting a conclusion. Lena held "
        "the operation together — she knew the equipment, the building, and the risks.\n\n"
        "\"We need a contingency plan,\" Raj said during a break. \"If someone discovers what "
        "we are doing, we need to consolidate the data somewhere safe — off-site, encrypted, "
        "accessible only to us.\"\n\n"
        "\"Agreed,\" Lena said. \"This is a pivotal moment. If we lose the data now, we may "
        "never get it back.\"\n\n"
        "Mara looked up from her screen. \"I have found something. The third layer — it is not "
        "just structure. It contains repeating clusters that look like they could be symbols. "
        "If I am right, this is not just a signal. It is a language.\"\n\n"
        "The room went quiet. Lena looked at Raj, then at Mara. They were three people in a "
        "forgotten room, working outside every official channel, and they had just taken the "
        "first real step in an endeavour that none of them fully understood."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- English metadata ---

    preview_text = (
        "Lena decides she cannot face this alone. She shows Raj the prime number sequence and "
        "her father's hidden notes, and he agrees to help despite the danger. Together they "
        "recruit Dr. Mara Chen, a brilliant and unconventional computational linguist who "
        "specialises in pattern recognition. The three of them set up a secret workstation at "
        "the observatory and begin analysing the signal in earnest. Mara quickly identifies "
        "additional layers of structure beneath the prime sequence — what appears to be a "
        "grammar embedded in the transmission. In this chapter, you will encounter 20 vocabulary "
        "words woven into the story: collaborate, expertise, unconventional, intricate, dedicate, "
        "clandestine, protocol, vulnerable, decipher, methodology, rigorous, convene, formidable, "
        "encryption, stratify, autonomous, contingency, consolidate, pivotal, endeavour. Across "
        "five passages and six learning sessions, you will build reading fluency and follow Lena "
        "as her secret team takes shape."
    )

    description = (
        "Chapter 5 follows Lena as she recruits Raj and computational linguist Dr. Mara Chen "
        "to form a secret team. Working from a hidden station at the observatory, Mara discovers "
        "the signal contains layered encoding — not just primes, but what may be a language."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "The Signal Beyond \u2014 Chapter 5: The Team",
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
        "Asking for Help",
        "Meeting Mara Chen",
        "The First Analysis",
        "The Hidden Station",
        "A Language in the Signal"
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
