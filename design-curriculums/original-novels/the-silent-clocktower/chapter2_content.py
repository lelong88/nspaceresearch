"""
Chapter 2: Những Người Hàng Xóm (The Neighbours)
Setup continues — Mai explores the town, meets key townspeople, and learns about the clockmaker.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 2."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["neighbour", "friendly", "introduce"]
    vocab_2 = ["counter", "regular", "customer"]
    vocab_3 = ["deliver", "package", "postcard"]
    vocab_4 = ["worried", "disappear", "lonely"]
    vocab_5 = ["trust", "secret", "ordinary"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Mai woke up early on her first full day in Eldermere. The morning sun came "
        "through the window and lit up the small room. She could hear birds singing "
        "outside and the sound of someone sweeping the street below.\n\n"
        "At breakfast, Mrs. Blackwood told her about the town. \"Everyone here is a "
        "good neighbour,\" she said. \"We look after each other. It is that kind of "
        "place.\"\n\n"
        "After eating, Mai walked outside. The air was cool and fresh. A man was "
        "standing in front of the pub across the square. He had a round face and a "
        "friendly smile. He waved at Mai.\n\n"
        "\"You must be the writer!\" he called out. \"Mrs. Blackwood told me about "
        "you. I am Tom. I run the pub.\" He walked over and shook her hand. \"Let me "
        "introduce you to some people. Everyone will want to meet you. We do not get "
        "many visitors here.\"\n\n"
        "Mai smiled. She liked Tom already. He seemed warm and open, the kind of "
        "person who talked to everyone."
    )

    passage_2 = (
        "Tom took Mai to a small tea shop on the corner of the square. Inside, it was "
        "warm and smelled like fresh bread and jasmine. An older woman stood behind the "
        "counter, arranging cups on a shelf.\n\n"
        "\"Mrs. Chen,\" Tom said, \"this is Mai. She is a journalist from Australia.\"\n\n"
        "Mrs. Chen looked at Mai with sharp, kind eyes. \"Welcome, dear. Sit down. I "
        "will make you some tea.\" She moved quickly, filling a teapot with hot water.\n\n"
        "\"Mrs. Chen knows everything about this town,\" Tom said with a laugh. \"She "
        "has been here for thirty years.\"\n\n"
        "\"I know what I see,\" Mrs. Chen said simply. She placed a cup in front of "
        "Mai. \"People come in here every day. I am a regular part of their morning. "
        "And they are regular parts of mine.\"\n\n"
        "Mai noticed a small sign near the door: \"Every customer is a friend.\" She "
        "took out her notebook. This tea shop seemed like a good place to learn about "
        "the town."
    )

    passage_3 = (
        "After tea, Tom walked Mai down the main street to the post office. It was a "
        "tiny building with a blue door and a window full of notices. Inside, a young "
        "woman with short dark hair was sorting letters behind the desk.\n\n"
        "\"This is Lily,\" Tom said. \"She runs the post office. She knows where every "
        "letter goes.\"\n\n"
        "Lily looked up and smiled. \"Hello! Are you the journalist? Everyone has been "
        "talking about you.\" She laughed. \"In a small town, news moves fast.\"\n\n"
        "\"Do you deliver the post yourself?\" Mai asked.\n\n"
        "\"Sometimes,\" Lily said. \"When there is a package too big for the letterbox, "
        "I walk it to the door myself. Last week I delivered a postcard from France. "
        "Old Mrs. Davies was so happy she made me stay for cake.\"\n\n"
        "Mai laughed. She could see that Lily loved her job. In a town like Eldermere, "
        "the post office was more than a place for letters. It was a place where people "
        "connected."
    )

    passage_4 = (
        "Later that afternoon, Mai sat in Tom's pub with a cup of coffee. The pub was "
        "quiet. Only two old men sat in the corner, playing cards. Tom wiped a glass "
        "and leaned against the bar.\n\n"
        "\"You want to know about Mr. Whitfield,\" Tom said. It was not a question.\n\n"
        "Mai nodded. \"Mrs. Blackwood told me he disappeared. What was he like?\"\n\n"
        "Tom thought for a moment. \"He was a quiet man. He lived alone in a small "
        "house near the tower. He spent most of his time up there, looking after the "
        "clock. He did not come to the pub often. I think he was a bit lonely.\"\n\n"
        "\"Did anyone notice anything before he left?\" Mai asked.\n\n"
        "\"He seemed worried,\" Tom said slowly. \"In the last few weeks before he "
        "was gone, he came in here twice. He sat alone and drank his tea without "
        "talking. That was not like him. He was quiet, yes, but not like that. "
        "Something was on his mind.\""
    )

    passage_5 = (
        "That evening, Mai walked back to the bed and breakfast. The sky was turning "
        "orange and pink. She stopped in the square and looked up at the clocktower. "
        "The hands still pointed to twenty past three.\n\n"
        "She thought about what she had learned today. Everyone liked Mr. Whitfield, "
        "but nobody really knew him. He was a kind, ordinary man who fixed clocks and "
        "kept to himself. But something had changed before he left.\n\n"
        "Mrs. Chen had said something interesting at the tea shop. \"Mr. Whitfield "
        "did not trust easily,\" she told Mai. \"He was polite to everyone, but he "
        "kept his thoughts to himself. If he had a secret, he would not share it.\"\n\n"
        "Mai wrote in her notebook: \"Whitfield — quiet, private, worried before he "
        "left. What did he find in the tower? Who did he talk to?\"\n\n"
        "She closed the notebook and went inside. Tomorrow she would visit the "
        "clocktower herself. The answers had to be somewhere."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Trong ngày đầu tiên khám phá Eldermere, Mai gặp gỡ những người dân thân thiện "
        "của thị trấn: Tom chủ quán pub vui vẻ, bà Chen chủ tiệm trà sắc sảo, và cô "
        "Lily trẻ trung ở bưu điện. Qua những cuộc trò chuyện, Mai dần hiểu thêm về "
        "ông Whitfield — người thợ đồng hồ sống một mình, ít nói nhưng được mọi người "
        "quý mến. Tom tiết lộ rằng ông Whitfield có vẻ lo lắng trong những tuần trước "
        "khi biến mất. Bạn sẽ ôn lại 15 từ vựng quen thuộc: neighbour, friendly, "
        "introduce, counter, regular, customer, deliver, package, postcard, worried, "
        "disappear, lonely, trust, secret, ordinary. Mỗi buổi học gồm thẻ từ vựng "
        "nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn "
        "bộ từ vựng và nghe lại cả chương — giúp bạn đọc trôi chảy và tự tin hơn với "
        "tiếng Anh."
    )

    description = (
        "Chương 2 kể về ngày đầu tiên Mai khám phá thị trấn Eldermere. Cô gặp Tom "
        "chủ quán pub, bà Chen chủ tiệm trà và Lily ở bưu điện. Qua họ, Mai tìm hiểu "
        "thêm về người thợ đồng hồ bí ẩn đã biến mất. Bạn sẽ luyện đọc 5 đoạn văn "
        "với 15 từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 2: Những Người Hàng Xóm (The Neighbours)",
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
                "title": "Flashcards: Ôn tập Những Người Hàng Xóm",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Những Người Hàng Xóm.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
