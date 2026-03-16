"""
Chapter 3: Người Hàng Xóm (The Neighbour)
Linh meets Mrs. Patterson and learns more about her grandmother's life.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 3."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["knock", "elderly", "apron"]
    vocab_2 = ["orchard", "harvest", "basket"]
    vocab_3 = ["stubborn", "pride", "refuse"]
    vocab_4 = ["soil", "seedling", "bloom"]
    vocab_5 = ["promise", "buried", "beneath"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "On her third morning in Willowbrook, Linh heard a knock at the front door. "
        "She opened it and found a small elderly woman standing there. She had white "
        "hair, bright blue eyes, and a warm smile. She was wearing a green apron over "
        "her dress.\n\n"
        "\"Hello, dear. I am Margaret Patterson. I live next door.\" She held up a "
        "plate covered with a cloth. \"I brought you some scones. Fresh from the oven.\"\n\n"
        "Linh smiled and invited her in. They sat in the kitchen and Linh made tea. "
        "Mrs. Patterson looked around the room with soft eyes.\n\n"
        "\"It looks the same,\" she said quietly. \"Rose kept everything the same for "
        "thirty years. She always said she wanted the house to be ready, in case your "
        "mother came home.\"\n\n"
        "Linh felt a lump in her throat. Her grandmother had been waiting all that time."
    )

    passage_2 = (
        "Mrs. Patterson told Linh about her grandmother's life in Willowbrook. Rose "
        "had been a gardener — not just a hobby gardener, but a real expert. She grew "
        "vegetables, herbs, and flowers. She had an orchard at the back of the property "
        "with apple and pear trees.\n\n"
        "\"Every autumn, the whole village came for the harvest,\" Mrs. Patterson said. "
        "\"Rose would fill basket after basket with apples. She made jam, cider, and "
        "pies. She gave most of it away.\"\n\n"
        "\"The garden was her life,\" she continued. \"After your mother left, Rose "
        "put all her love into that garden. It was the most beautiful garden in the "
        "county. People came from other villages just to see it.\"\n\n"
        "Linh thought about the wild, overgrown garden outside. It was hard to imagine "
        "it as a place of beauty. But she could see the bones of it — the stone paths, "
        "the rose arches, the greenhouse."
    )

    passage_3 = (
        "\"Why did the garden become so wild?\" Linh asked.\n\n"
        "Mrs. Patterson sighed. \"Rose became ill about two years ago. She could not "
        "work in the garden anymore. I offered to help, but she was stubborn. She said "
        "the garden was her responsibility.\"\n\n"
        "\"She had too much pride to accept help?\" Linh asked.\n\n"
        "\"Not exactly. She said the garden had a purpose, and only she understood it. "
        "She would refuse any help. Even from me, and I had been her friend for twenty "
        "years.\"\n\n"
        "Mrs. Patterson paused and looked at Linh carefully. \"Your grandmother was a "
        "wonderful woman, but she kept things to herself. She had secrets. I think the "
        "garden was one of them.\"\n\n"
        "Linh remembered the last letter — the one about something buried in the garden. "
        "She wanted to ask Mrs. Patterson about it, but something told her to wait."
    )

    passage_4 = (
        "After tea, Mrs. Patterson took Linh outside to look at the garden together. "
        "They walked slowly along the old stone path. Mrs. Patterson pointed out "
        "different areas.\n\n"
        "\"This was the herb garden. Rose grew rosemary, thyme, and lavender here. "
        "The soil was perfect for herbs — sandy and well-drained.\" She bent down and "
        "pulled away some weeds. Underneath, Linh could see small green plants still "
        "growing.\n\n"
        "\"Look,\" Mrs. Patterson said with surprise. \"There are seedlings here. "
        "Someone — or something — has been planting.\"\n\n"
        "They walked further. Near the greenhouse, they found a rose bush that was "
        "still alive. It had one red flower in full bloom, bright against the green "
        "weeds around it.\n\n"
        "\"That was Rose's favourite,\" Mrs. Patterson whispered. \"She planted it the "
        "year your mother was born. And look — it is still blooming, even without care.\""
    )

    passage_5 = (
        "Before she left, Mrs. Patterson stopped at the door and turned back to Linh. "
        "Her expression was serious.\n\n"
        "\"There is something you should know,\" she said. \"A few weeks before Rose "
        "died, she asked me to make a promise. She said: 'When my granddaughter comes, "
        "tell her to look in the garden. Tell her to dig where the roses grow.'\"\n\n"
        "\"She knew I would come?\" Linh asked.\n\n"
        "\"She was certain. She said you would come, and you would understand.\" Mrs. "
        "Patterson took Linh's hand. \"I do not know what she buried there, or what "
        "is beneath those roses. But she wanted you to find it. Not your mother — you.\"\n\n"
        "Linh stood in the doorway after Mrs. Patterson left. The afternoon sun lit "
        "up the garden. Somewhere under the wild grass and tangled roses, her "
        "grandmother had hidden something meant only for her. Tomorrow, she would "
        "start digging."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh gặp bà Margaret Patterson, người hàng xóm thân thiết nhất của bà ngoại "
        "suốt 20 năm. Qua câu chuyện của bà Patterson, Linh biết được bà ngoại từng "
        "là một nghệ nhân làm vườn tài ba — khu vườn đẹp nhất vùng với vườn cây ăn quả "
        "và hoa hồng. Nhưng khi bà ngoại bệnh, bà từ chối mọi sự giúp đỡ vì khu vườn "
        "giấu một bí mật. Trước khi mất, bà ngoại nhắn: 'Khi cháu gái đến, bảo nó đào "
        "chỗ hoa hồng mọc.' Bạn sẽ ôn lại 15 từ vựng quen thuộc: knock, elderly, apron, "
        "orchard, harvest, basket, stubborn, pride, refuse, soil, seedling, bloom, "
        "promise, buried, beneath. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn "
        "truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe "
        "lại cả chương."
    )

    description = (
        "Chương 3: Linh gặp bà Patterson và biết được bà ngoại từng là nghệ nhân làm "
        "vườn tài ba. Trước khi mất, bà ngoại để lại lời nhắn bí ẩn: hãy đào chỗ hoa "
        "hồng mọc. Luyện đọc 5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 3: Người Hàng Xóm (The Neighbour)",
        "language": "en",
        "userLanguage": "vi",
        "level": "preintermediate",
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

    for i in range(5):
        session_num = i + 1
        vocab = vocab_groups[i]
        passage = passages[i]
        desc_preview = passage[:80].rstrip() + "..."

        session = {
            "title": f"Phần {session_num}",
            "activities": [
                {
                    "activityType": "viewFlashcards",
                    "title": f"Flashcards: Phần {session_num}",
                    "description": f"Học 3 từ: {', '.join(vocab)}",
                    "data": {
                        "vocabList": vocab,
                        "audioSpeed": -0.2
                    }
                },
                {
                    "activityType": "reading",
                    "title": f"Đọc: Phần {session_num}",
                    "description": desc_preview,
                    "data": {
                        "text": passage,
                        "audioSpeed": -0.2
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": f"Nghe: Phần {session_num}",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": passage
                    }
                }
            ]
        }
        curriculum["learningSessions"].append(session)

    # --- Session 6: Review ---
    review_session = {
        "title": "Ôn tập",
        "activities": [
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập Người Hàng Xóm",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Người Hàng Xóm.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
