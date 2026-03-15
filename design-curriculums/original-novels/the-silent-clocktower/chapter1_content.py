"""
Chapter 1: Thị Trấn Trên Đồi (The Town on the Hill)
Setup chapter — introduces Mai Nguyen, the mountain town, and the stopped clocktower.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 1."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["journalist", "assignment", "village"]
    vocab_2 = ["ancient", "tower", "square"]
    vocab_3 = ["narrow", "cobblestone", "chimney"]
    vocab_4 = ["stranger", "curious", "rumour"]
    vocab_5 = ["silent", "clocktower", "mystery"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Mai Nguyen looked out of the train window. The green hills of England moved "
        "past like a slow painting. She was a journalist from Melbourne, Australia. Her "
        "parents had come from Vietnam before she was born. Now she worked for a small "
        "travel magazine.\n\n"
        "Her editor had given her a new assignment last week. \"There is a town in the "
        "mountains,\" he said. \"Nobody writes about it. Go there and find a story.\"\n\n"
        "The town was called Eldermere. It was a small village in the north of England, "
        "far from any city. Mai had found very little about it online. There were a few "
        "old photographs and a short paragraph on a tourism website. That was all.\n\n"
        "She checked her notebook. She had the address of a bed and breakfast, a map she "
        "had printed, and a list of questions. She was ready. The train slowed down. A "
        "sign appeared outside: Eldermere Station."
    )

    passage_2 = (
        "Mai stepped off the train and looked around. The station was small and empty. "
        "There was one bench, one lamp, and a wooden sign that said \"Welcome to "
        "Eldermere.\"\n\n"
        "She walked out of the station and up a steep path. After ten minutes, she "
        "reached the top of the hill. The town was spread out below her. It was "
        "beautiful. Old stone houses sat close together. In the centre, there was a "
        "large square with a few shops and a café.\n\n"
        "But the first thing Mai noticed was the tower. It stood at the edge of the "
        "square, tall and ancient. It was made of dark grey stone. A large clock face "
        "was near the top. The clock showed twenty past three. Mai looked at her phone. "
        "It was half past five.\n\n"
        "The clock was wrong. Or maybe it had stopped. She took a photograph and "
        "continued walking down the hill toward the town."
    )

    passage_3 = (
        "The main street of Eldermere was narrow and quiet. Mai walked slowly, looking "
        "at everything. The buildings were old but well kept. Some had flower boxes in "
        "the windows. Others had small signs for shops — a bakery, a post office, a "
        "hardware store.\n\n"
        "The road was made of cobblestone. Her suitcase wheels made a loud noise as she "
        "pulled it along. A woman standing outside the bakery looked up and smiled.\n\n"
        "\"You must be the journalist,\" the woman said. \"Mrs. Blackwood at the bed and "
        "breakfast told us someone was coming.\"\n\n"
        "Mai smiled back. \"News travels fast here.\"\n\n"
        "\"It is a small town,\" the woman said. She pointed up the street. \"You will "
        "see the bed and breakfast on the left. The house with the red chimney.\"\n\n"
        "Mai thanked her and walked on. She could already feel that this town had its "
        "own rhythm, slow and steady, like the ticking of a clock."
    )

    passage_4 = (
        "Mrs. Blackwood was a short woman with grey hair and kind eyes. She showed Mai "
        "to a small room on the second floor. The room had a window that looked out "
        "over the square and the clocktower.\n\n"
        "\"That clock has not worked for three months,\" Mrs. Blackwood said, noticing "
        "Mai looking at it. \"It stopped one night and nobody knows why.\"\n\n"
        "\"Who used to look after it?\" Mai asked.\n\n"
        "\"Old Mr. Whitfield. He was the clockmaker. He took care of that tower for "
        "forty years.\" Mrs. Blackwood paused. \"But he is gone now. Disappeared. One "
        "morning his house was empty. No note, no goodbye. He was not a stranger here "
        "— everyone knew him.\"\n\n"
        "Mai felt curious. A missing clockmaker and a stopped clock. That was more "
        "interesting than a travel article. There was a rumour, Mrs. Blackwood added "
        "quietly, that Mr. Whitfield had found something inside the tower before he "
        "vanished."
    )

    passage_5 = (
        "That evening, Mai sat by her window and looked at the clocktower. The town was "
        "silent. No cars, no music, just the wind moving through the trees. The tower "
        "stood dark against the purple sky. Its clock face was pale in the moonlight, "
        "the hands frozen at twenty past three.\n\n"
        "She opened her notebook and wrote: \"Eldermere. Small mountain town. Beautiful "
        "but strange. The clocktower is silent. The clockmaker is missing. Everyone "
        "talks about it but nobody has answers.\"\n\n"
        "She thought about what Mrs. Blackwood had said. A rumour about something "
        "hidden inside the tower. What could an old clockmaker find in a clock? And "
        "why would he leave without telling anyone?\n\n"
        "Mai closed her notebook and looked out at the dark hills. She had come here "
        "to write a simple travel article. But now she felt something else — the pull "
        "of a mystery. She decided she would stay a little longer. Tomorrow, she would "
        "start asking questions."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai Nguyen, một nhà báo trẻ người Úc gốc Việt, được giao nhiệm vụ viết bài "
        "về một thị trấn nhỏ trên đồi ở miền bắc nước Anh. Khi đến Eldermere, cô phát "
        "hiện tháp đồng hồ cổ đã ngừng hoạt động và người thợ đồng hồ già đã biến mất "
        "một cách bí ẩn. Trong chương mở đầu đầy hấp dẫn này, bạn sẽ theo chân Mai "
        "khám phá thị trấn yên tĩnh với những con đường lát đá và ngôi nhà cổ kính. "
        "Bạn sẽ ôn lại 15 từ vựng quen thuộc: journalist, assignment, village, ancient, "
        "tower, square, narrow, cobblestone, chimney, stranger, curious, rumour, silent, "
        "clocktower, mystery. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn truyện "
        "hấp dẫn và luyện nghe theo. Qua 5 đoạn văn ngắn, bạn sẽ cảm nhận được bầu "
        "không khí bí ẩn của Eldermere và sự tò mò ngày càng lớn của Mai. Buổi 6 tổng "
        "ôn toàn bộ từ vựng và nghe lại cả chương — giúp bạn đọc trôi chảy và tự tin "
        "hơn với tiếng Anh."
    )

    description = (
        "Chương 1 giới thiệu Mai Nguyen đến thị trấn Eldermere trên đồi, nơi tháp "
        "đồng hồ cổ đã ngừng chạy và người thợ đồng hồ biến mất bí ẩn. Bạn sẽ luyện "
        "đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung cấp, rèn kỹ năng đọc hiểu "
        "qua ngữ cảnh tự nhiên."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 1: Thị Trấn Trên Đồi (The Town on the Hill)",
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
                "title": "Flashcards: Ôn tập Thị Trấn Trên Đồi",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Thị Trấn Trên Đồi.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
