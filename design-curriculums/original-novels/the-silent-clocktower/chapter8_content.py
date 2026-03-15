"""
Chapter 8: Đường Hầm (The Tunnel)
Climax begins — Mai and David explore the tunnels beneath the clocktower and discover Mr. Whitfield alive.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 8."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["basement", "passage", "damp"]
    vocab_2 = ["vault", "shelf", "crate"]
    vocab_3 = ["blanket", "recent", "flashlight"]
    vocab_4 = ["footstep", "alive", "recognize"]
    vocab_5 = ["escape", "survive", "courage"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Mai met David at the clocktower that evening. She told him about her visit "
        "to Mr. Graves and the threat he had made. David listened carefully.\n\n"
        "\"We need to find out what is in those tunnels,\" he said. \"The map shows "
        "an entrance in the basement of the tower. If my uncle hid something down "
        "there, we need to see it before Graves can stop us.\"\n\n"
        "They went inside the tower and found the stairs going down. The basement "
        "was dark and cold. Old tools and broken furniture filled the corners. Mai "
        "held up her phone light and looked at the map.\n\n"
        "\"There,\" she said, pointing at the far wall. \"The passage should be "
        "behind those shelves.\"\n\n"
        "They moved the heavy wooden shelves to one side. Behind them was a low "
        "stone doorway. Cool air came through it. The walls inside were damp and "
        "the smell of earth was strong.\n\n"
        "David looked at Mai. \"Are you ready?\"\n\n"
        "She nodded. They stepped through the doorway and into the darkness below."
    )

    passage_2 = (
        "The tunnel was narrow and low. Mai and David walked slowly, using their "
        "phone lights to see. The walls were made of old brick, and the floor was "
        "hard stone. It was quiet except for the sound of their breathing.\n\n"
        "They followed the main tunnel for about ten minutes. It went straight for "
        "a while, then turned left. After the turn, the tunnel became wider. Mai "
        "could see that the ceiling was higher here.\n\n"
        "Then the tunnel opened into a large room. It was like an underground vault "
        "— a big space with a high ceiling and stone walls. Along the walls, there "
        "were old wooden shelves. One shelf still held glass jars and metal boxes. In the "
        "centre of the room, there were several large wooden crates, some open and "
        "some still closed.\n\n"
        "\"This must be from the Hargrove days,\" David said quietly. He touched one "
        "of the crates. The wood was old and dry. \"They used this place to store "
        "things. Maybe valuable things they wanted to keep safe.\"\n\n"
        "Mai looked around the vault. It was like stepping back in time."
    )

    passage_3 = (
        "Mai walked to the far corner of the room. Something looked different there. "
        "The dust on the floor had been moved. She knelt down and looked more "
        "closely.\n\n"
        "There was a blanket folded neatly on the ground. Next to it, she found "
        "empty food wrappers, a plastic water bottle, and a small flashlight. These "
        "were not old things from the Hargrove era. They were modern.\n\n"
        "\"David, come here,\" she whispered. \"Someone has been living down here.\"\n\n"
        "David came over and looked at the items. He picked up one of the food "
        "wrappers. The date on it was recent — only two weeks old.\n\n"
        "\"This is not possible,\" he said. \"Who would live underground?\"\n\n"
        "Mai felt her heart beating fast. She looked at the blanket, the food, the "
        "flashlight. Someone had made a small camp in this corner. They had been "
        "sleeping here, eating here. The person knew about the tunnels and knew how "
        "to get in and out without being seen.\n\n"
        "\"We need to be careful,\" Mai said. \"They could come back at any time.\""
    )

    passage_4 = (
        "Before they could move, Mai heard something. A footstep. Then another. "
        "Someone was coming through the tunnel toward the room.\n\n"
        "\"Hide,\" David whispered. They moved quickly behind the large crates in "
        "the centre of the vault. Mai pressed her back against the wood and held "
        "her breath.\n\n"
        "A light appeared at the tunnel entrance. A figure walked into the room. "
        "It was an old man. He was thin and his clothes were dirty. He carried a "
        "bag in one hand and a torch in the other. He walked to the corner where "
        "the blanket was and put the bag down.\n\n"
        "David stood up slowly. His face was white. \"Uncle?\" he said.\n\n"
        "The old man turned around fast. His eyes were wide with shock. Mai could "
        "see that David was right. She did not recognize the man at first because "
        "he looked so different from the photographs. But it was him. Mr. Whitfield "
        "was alive.\n\n"
        "\"David?\" the old man whispered. His hands were shaking. \"How did you "
        "find me?\""
    )

    passage_5 = (
        "Mr. Whitfield sat down on one of the crates. His hands were still shaking. "
        "David sat next to him. Mai stood nearby, watching quietly.\n\n"
        "\"I thought you were dead,\" David said. His voice was thick with emotion. "
        "\"Everyone thought you were dead.\"\n\n"
        "The old man shook his head. \"I had to escape. Graves found out about the "
        "deed. He came to my workshop one night and told me to give it to him. When "
        "I refused, he said he would make sure I could never tell anyone. I was "
        "afraid. So I hid the deed in the wall and came down here.\"\n\n"
        "\"You have been living in these tunnels for three months?\" Mai asked.\n\n"
        "\"I go out at night sometimes, to get food and water. But yes, I survive "
        "down here. It is not easy, but it is safe.\" He looked at David. \"I wrote "
        "you that letter because I hoped you would come. I did not have the courage "
        "to go to the police myself. Graves has friends everywhere.\"\n\n"
        "Mai looked at the old clockmaker. He had been hiding underground, alone and "
        "afraid, for three months. It was time to bring him back into the light."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai và David quyết định khám phá đường hầm bí mật bên dưới tháp đồng hồ. "
        "Họ tìm thấy lối vào trong tầng hầm và đi sâu vào lòng đất. Đường hầm dẫn "
        "đến một căn hầm lớn từ thời gia đình Hargrove, với những kệ gỗ và thùng hàng "
        "cũ. Nhưng điều bất ngờ nhất là có ai đó đang sống ở đây — chăn, đèn pin và "
        "thức ăn mới. Rồi họ nghe tiếng bước chân. Người bước vào chính là ông "
        "Whitfield — ông vẫn còn sống! Bạn sẽ ôn lại 15 từ vựng quen thuộc: "
        "basement, passage, damp, vault, shelf, crate, blanket, recent, flashlight, "
        "footstep, alive, recognize, escape, survive, courage. Mỗi buổi học gồm thẻ "
        "từ vựng nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng "
        "ôn toàn bộ từ vựng và nghe lại cả chương — giúp bạn đọc trôi chảy và tự tin "
        "hơn với tiếng Anh."
    )

    description = (
        "Chương 8 đưa Mai và David vào đường hầm bí mật dưới tháp đồng hồ, nơi họ "
        "phát hiện một căn hầm cổ và dấu hiệu có người đang sống. Bất ngờ lớn nhất "
        "là ông Whitfield vẫn còn sống — ông đã trốn dưới lòng đất vì bị đe dọa. "
        "Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 8: Đường Hầm (The Tunnel)",
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
                "title": "Flashcards: Ôn tập Đường Hầm",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Đường Hầm.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
