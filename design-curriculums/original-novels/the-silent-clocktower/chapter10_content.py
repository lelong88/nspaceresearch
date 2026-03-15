"""
Chapter 10: Tiếng Chuông Trở Lại (The Clock Strikes Again)
Resolution chapter — mystery solved, all plot threads resolved, the clock strikes again.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 10."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["charge", "elect", "celebrate"]
    vocab_2 = ["restore", "tool", "patient"]
    vocab_3 = ["publish", "proud", "inspire"]
    vocab_4 = ["strike", "correct", "cheer"]
    vocab_5 = ["farewell", "grateful", "remember"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "A week had passed since the town meeting. The news had spread far beyond "
        "Eldermere. Mr. Graves had been formally charged by the police for threatening "
        "Mr. Whitfield and trying to sell town property without permission. He would "
        "have to go to court.\n\n"
        "The town council held a special meeting to elect a new head. Mrs. Chen was "
        "the clear choice. She had lived in Eldermere for over thirty years and everyone "
        "trusted her. She accepted the position with a quiet smile.\n\n"
        "\"I will do my best for this town,\" she said. \"We have learned a hard lesson. "
        "From now on, every decision will be open and honest.\"\n\n"
        "That evening, the people of Eldermere came together in the square to celebrate. "
        "Tom brought food from the pub. Lily brought flowers from her garden. Mrs. "
        "Blackwood made her famous apple cake. Children ran between the tables while "
        "the adults talked and laughed. For the first time in months, the town felt "
        "whole again. The old deed had been officially recognized — the clocktower "
        "belonged to the people of Eldermere, as the Hargrove family had always intended."
    )

    passage_2 = (
        "The next morning, Mr. Whitfield returned to his workshop inside the clocktower. "
        "He had not been there for three months. Dust covered every surface. His drawings "
        "were still on the wall. His leather journal sat on the workbench where Mai had "
        "first found it.\n\n"
        "He opened his old bag and took out each tool carefully. Wrenches, small hammers, "
        "oil cans, and delicate brushes. He laid them on the bench in a neat row. Then "
        "he looked up at the machinery above him.\n\n"
        "\"It will take time to restore the clock,\" he told David, who stood beside "
        "him. \"Some parts are old and worn. I need to be patient and work carefully.\"\n\n"
        "David rolled up his sleeves. \"I am staying in Eldermere for a while, Uncle. "
        "Show me what to do. I want to help.\"\n\n"
        "Mr. Whitfield smiled. It was the first real smile Mai had seen on his face. "
        "He handed David a cloth and pointed to the gears. \"Start by cleaning. Every "
        "good repair begins with clean hands and clean parts.\""
    )

    passage_3 = (
        "Mai sat at the small desk in her room at Mrs. Blackwood's bed and breakfast. "
        "Her laptop was open. She had been writing for two days. The article was almost "
        "finished.\n\n"
        "It was not the travel piece her editor had asked for. It was something much "
        "bigger. She had written about the clocktower, the missing clockmaker, the "
        "hidden deed, and the corruption on the town council. She planned to publish "
        "it in a national newspaper, not just her small travel magazine.\n\n"
        "She read the last paragraph again: \"Eldermere is a small town, but its story "
        "is not small. It is about ordinary people who stood up for what was right. It "
        "is about a clockmaker who chose to hide rather than give up his town's history. "
        "And it is about the truth — which, like a stopped clock, always waits to be "
        "found.\"\n\n"
        "Mai felt proud of this article. It was the best thing she had ever written. "
        "She hoped it would inspire other people to protect the places and stories "
        "that matter to them. She pressed send and closed her laptop."
    )

    passage_4 = (
        "On Mai's last afternoon in Eldermere, the whole town gathered in the square. "
        "Mr. Whitfield and David had been working day and night. The clock was ready.\n\n"
        "Mai stood next to Tom, Mrs. Chen, and Lily. Mrs. Blackwood held her hand. "
        "Everyone looked up at the tower. Mr. Whitfield appeared at the small window "
        "near the top. He waved down at the crowd.\n\n"
        "Then it happened. The old machinery began to move. The gears turned. The hands "
        "of the clock shifted slowly. They moved to the correct time — half past four "
        "on a warm Friday afternoon.\n\n"
        "A deep, beautiful sound rang out across the valley. The clock began to strike. "
        "One. Two. Three. Four. The bells had not been heard for months. People covered "
        "their mouths. Some cried. Then the whole square broke into a loud cheer. "
        "Children jumped up and down. Tom lifted his hat in the air. Mrs. Chen clapped "
        "her hands together. The clocktower was alive again."
    )

    passage_5 = (
        "The next morning, Mai packed her suitcase. It was time to go home. She walked "
        "through the town one last time. At the pub, Tom shook her hand. \"You are "
        "always welcome here,\" he said.\n\n"
        "At the tea shop, Mrs. Chen gave her a small box of tea. \"Something to remember "
        "us by.\" Lily hugged her at the post office door. \"Write to us,\" she said.\n\n"
        "At the clocktower, Mr. Whitfield and David were waiting. The old man took "
        "Mai's hand. \"You gave this town its voice back,\" he said. \"I am grateful "
        "for everything you did.\"\n\n"
        "David smiled. \"This is not a farewell forever. Come back and visit.\"\n\n"
        "Mai promised she would. She walked down the hill to the station. The train "
        "was already waiting. She climbed on and found a seat by the window. As the "
        "train pulled away, she looked back at Eldermere one last time. The clocktower "
        "stood tall against the blue sky. Its hands were moving. Its bells would ring "
        "again at five o'clock. Mai smiled and opened her notebook. She had come to "
        "find a story. She had found so much more."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Một tuần sau cuộc họp thị trấn, mọi chuyện dần ổn định. Graves bị truy tố "
        "chính thức, bà Chen được bầu làm trưởng hội đồng mới, và tờ chứng thư được "
        "công nhận — tháp đồng hồ thuộc về người dân Eldermere. Ông Whitfield trở lại "
        "xưởng sửa chữa đồng hồ với sự giúp đỡ của David. Mai viết bài báo điều tra "
        "và gửi đăng trên báo quốc gia. Vào ngày cuối cùng, cả thị trấn tụ họp tại "
        "quảng trường. Đồng hồ gõ nhịp trở lại lần đầu tiên sau nhiều tháng. Bạn sẽ "
        "ôn lại 15 từ vựng quen thuộc: charge, elect, celebrate, restore, tool, "
        "patient, publish, proud, inspire, strike, correct, cheer, farewell, grateful, "
        "remember. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn truyện hấp dẫn "
        "và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe lại cả chương — "
        "giúp bạn đọc trôi chảy và tự tin hơn với tiếng Anh."
    )

    description = (
        "Chương 10 là chương kết thúc câu chuyện. Graves bị truy tố, bà Chen được "
        "bầu làm trưởng hội đồng, ông Whitfield sửa lại đồng hồ, và Mai viết bài "
        "báo điều tra. Tháp đồng hồ gõ nhịp trở lại khi Mai nói lời tạm biệt với "
        "Eldermere. Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung "
        "cấp, rèn kỹ năng đọc hiểu qua ngữ cảnh tự nhiên."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 10: Tiếng Chuông Trở Lại (The Clock Strikes Again)",
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
                "title": "Flashcards: Ôn tập Tiếng Chuông Trở Lại",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Tiếng Chuông Trở Lại.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
