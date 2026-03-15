"""
Chapter 5: Cuộc Gặp Gỡ Bất Ngờ (The Unexpected Meeting)
Mid-story twist — Mai meets the stranger, who reveals he is the clockmaker's nephew.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 5."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["garden", "bench", "approach"]
    vocab_2 = ["nephew", "relative", "explain"]
    vocab_3 = ["envelope", "handwriting", "warn"]
    vocab_4 = ["afraid", "danger", "protect"]
    vocab_5 = ["realize", "puzzle", "careful"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "The next morning, Mai walked to the inn on the edge of town. It was an old "
        "building with white walls and a dark roof. A small sign said \"The Fox and "
        "Lantern\" above the door.\n\n"
        "Mai did not go inside. Instead, she walked around the side of the building. "
        "There was a garden at the back with a few wooden tables and chairs. The grass "
        "was wet from the morning rain. Flowers grew along the stone wall.\n\n"
        "She saw the man sitting alone on a bench near the far wall. He was not wearing "
        "his dark coat today. He had a cup of coffee in his hand and a small bag on the "
        "ground beside him. He was looking at the hills.\n\n"
        "Mai took a deep breath. She decided to approach him directly. There was no "
        "point in watching from far away. She needed answers.\n\n"
        "\"Good morning,\" she said. \"My name is Mai. I am a journalist. I have been "
        "writing about the clocktower, and I think you might know something about it.\"\n\n"
        "The man looked at her. He did not seem surprised. \"I was wondering when "
        "someone would come to talk to me,\" he said."
    )

    passage_2 = (
        "The man put down his coffee and stood up. He was tall with brown hair and "
        "tired eyes. He held out his hand.\n\n"
        "\"My name is David Whitfield,\" he said. \"I am Arthur Whitfield's nephew. "
        "He is my uncle.\"\n\n"
        "Mai felt her heart beat faster. She had not expected this. The stranger was "
        "not a stranger at all — he was a relative of the missing clockmaker.\n\n"
        "\"Please, sit down,\" David said, pointing to the bench. \"I will explain "
        "everything I can.\"\n\n"
        "They sat together in the quiet garden. David told Mai that he lived in London "
        "and worked in a bookshop. He and his uncle were not very close. They saw each "
        "other once or twice a year, usually at Christmas.\n\n"
        "\"But three weeks ago, I received a letter from him,\" David said. \"It was "
        "strange. He never wrote letters. He always called on the phone. When I read "
        "the letter, I knew something was wrong. So I came here.\"\n\n"
        "\"What did the letter say?\" Mai asked.\n\n"
        "David reached into his bag. \"I will show you.\""
    )

    passage_3 = (
        "David pulled out a white envelope from his bag. It was old and slightly bent "
        "at the corners. Mai could see a name written on the front in small, neat "
        "handwriting — \"David Whitfield, 14 Rose Lane, London.\"\n\n"
        "\"This is my uncle's writing,\" David said. \"I know it well. He always wrote "
        "like this — small and careful.\"\n\n"
        "He opened the envelope and took out a single sheet of paper. He handed it to "
        "Mai. She read it slowly.\n\n"
        "\"Dear David, I am writing because I do not know who else to ask. I have found "
        "something inside the clocktower. Something important. I cannot say what it is "
        "in a letter. But I need you to come to Eldermere. There is a thing behind the "
        "wall that must be kept safe. Please come soon. And David — I must warn you — "
        "be careful who you trust in this town. Not everyone is what they seem. Your "
        "uncle, Arthur.\"\n\n"
        "Mai read the letter twice. The words were simple, but the meaning was heavy. "
        "Whitfield had been afraid. He had wanted help. And he had not trusted the "
        "people around him."
    )

    passage_4 = (
        "Mai gave the letter back to David. Her mind was full of questions.\n\n"
        "\"Your uncle was afraid of someone here,\" she said. \"He wrote that he could "
        "not trust the people in this town.\"\n\n"
        "David nodded slowly. \"That is why I did not talk to anyone when I arrived. I "
        "did not know who was safe. My uncle said there was danger, and I believed him.\"\n\n"
        "\"And the journal,\" Mai said. \"You took it from the tower.\"\n\n"
        "David looked down. \"Yes. I am sorry about that. I went to the tower the night "
        "before last. I still have a key — my uncle gave me one years ago. I found the "
        "journal on the table. I was afraid someone else would find it first. I wanted "
        "to protect it.\"\n\n"
        "He reached into his bag again and pulled out the leather journal. Mai recognized "
        "it immediately — the brown cover, the drawings inside.\n\n"
        "\"Here,\" David said, handing it to her. \"You should have it. You are trying "
        "to find the truth. I think my uncle would want someone like you to help.\"\n\n"
        "Mai took the journal carefully. She felt its weight in her hands."
    )

    passage_5 = (
        "Mai and David sat in the garden for a long time. She told him about the "
        "workshop, the drawings of the hidden compartment, and the loose stone in the "
        "north wall. David listened quietly.\n\n"
        "\"My uncle was a careful man,\" David said. \"If he hid something behind that "
        "wall, it was important. And if he was afraid, the danger was real.\"\n\n"
        "Mai looked at the letter again. \"Be careful who you trust in this town.\" She "
        "thought about Mrs. Blackwood, Tom, Mrs. Chen, Lily at the post office. They "
        "all seemed kind. But Whitfield had written those words for a reason.\n\n"
        "She began to realize that this mystery was bigger than a missing clockmaker. "
        "Someone in Eldermere had made Whitfield afraid enough to run. The hidden "
        "compartment, the letter, the journal — they were all pieces of a puzzle, and "
        "Mai did not yet have the full picture.\n\n"
        "\"We should open that compartment together,\" Mai said to David. \"But we "
        "need to be careful. If your uncle was right, then someone in this town is "
        "watching.\"\n\n"
        "David agreed. They would go to the tower tomorrow, early in the morning, "
        "before anyone else was awake."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai đến quán trọ để điều tra người lạ bí ẩn. Cô tìm thấy anh ta trong khu "
        "vườn phía sau và phát hiện một sự thật bất ngờ — anh ta là David Whitfield, "
        "cháu trai của người thợ đồng hồ mất tích. David cho Mai xem một lá thư từ "
        "chú Arthur, trong đó ông cảnh báo David phải cẩn thận với người dân trong "
        "thị trấn. David thú nhận đã lấy cuốn nhật ký từ tháp để bảo vệ nó và trả "
        "lại cho Mai. Bạn sẽ ôn lại 15 từ vựng quen thuộc: garden, bench, approach, "
        "nephew, relative, explain, envelope, handwriting, warn, afraid, danger, "
        "protect, realize, puzzle, careful. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc "
        "một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng "
        "và nghe lại cả chương — giúp bạn đọc trôi chảy và tự tin hơn với tiếng Anh."
    )

    description = (
        "Chương 5 là bước ngoặt giữa truyện — Mai gặp David Whitfield, cháu trai của "
        "người thợ đồng hồ. Anh ta tiết lộ lá thư cảnh báo từ chú mình và trả lại "
        "cuốn nhật ký. Mai nhận ra bí ẩn lớn hơn cô tưởng. Bạn sẽ luyện đọc 5 đoạn "
        "văn với 15 từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 5: Cuộc Gặp Gỡ Bất Ngờ (The Unexpected Meeting)",
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
                "title": "Flashcards: Ôn tập Cuộc Gặp Gỡ Bất Ngờ",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Cuộc Gặp Gỡ Bất Ngờ.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
