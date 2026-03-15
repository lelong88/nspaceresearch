"""
Chapter 3: Bên Trong Tháp (Inside the Tower)
Investigation begins — Mai visits the clocktower, finds Whitfield's workshop and the first real clues.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 3."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["permission", "council", "borrow"]
    vocab_2 = ["dust", "machinery", "staircase"]
    vocab_3 = ["workshop", "repair", "leather"]
    vocab_4 = ["drawing", "hidden", "compartment"]
    vocab_5 = ["photograph", "evidence", "clue"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "The next morning, Mai decided to visit the clocktower. But the door at the "
        "bottom of the tower was locked. She needed to find the key.\n\n"
        "She walked to the town council office, a small stone building next to the "
        "post office. Inside, an older man sat behind a desk covered in papers. He "
        "looked up when Mai came in.\n\n"
        "\"I would like permission to go inside the clocktower,\" Mai said. \"I am "
        "writing an article about the town.\"\n\n"
        "The man shook his head slowly. \"Nobody has been inside since Mr. Whitfield "
        "left. I am not sure I can help you.\"\n\n"
        "Just then, Lily came through the door with a bag of letters. \"Oh, let her "
        "go in,\" Lily said with a smile. \"She is a journalist. She will be careful.\"\n\n"
        "The man thought for a moment, then opened a drawer. He took out a large iron "
        "key. \"You can borrow this for one day,\" he said. \"Please bring it back "
        "before five o'clock.\"\n\n"
        "Mai thanked him and held the heavy key in her hand. It felt very old."
    )

    passage_2 = (
        "Mai walked across the square to the clocktower. The wooden door was thick and "
        "heavy. She put the key in the lock and turned it. The door opened with a long, "
        "low sound.\n\n"
        "Inside, the air was cold and smelled old. A thin layer of dust covered "
        "everything — the floor, the walls, the wooden shelves along the sides. Nobody "
        "had been here for months.\n\n"
        "Mai looked up. The inside of the tower was tall and open. She could see the "
        "machinery of the clock high above her — large metal wheels, thick ropes, and "
        "heavy weights hanging in the dark. It was like looking inside a giant machine "
        "that had fallen asleep.\n\n"
        "A narrow staircase made of stone went up along the wall. The steps were worn "
        "smooth from many years of use. Mai put her hand on the cold stone wall and "
        "began to climb. Her footsteps echoed in the empty tower. With each step, she "
        "felt she was getting closer to something important."
    )

    passage_3 = (
        "On the second floor, Mai found a small room. It was Mr. Whitfield's workshop. "
        "A long wooden table stood against the wall, covered with tools — small hammers, "
        "screwdrivers, tiny metal pieces, and glass jars full of screws and springs.\n\n"
        "Everything was neatly arranged. Mr. Whitfield had been a careful man. On one "
        "end of the table, there was a clock that looked half finished. He had been in "
        "the middle of a repair when he left. The back of the clock was open, and some "
        "of the small parts were laid out in a row.\n\n"
        "Mai looked around the room. There was a chair, a small lamp, and a shelf with "
        "a few books about clocks. On the corner of the table, she noticed a thick "
        "notebook with a leather cover. It was dark brown and worn from use.\n\n"
        "She picked it up carefully. The pages were filled with small, neat handwriting. "
        "There were numbers, diagrams, and notes about the clock. This was Whitfield's "
        "journal."
    )

    passage_4 = (
        "Mai sat down in Whitfield's chair and opened the leather journal. Most of the "
        "pages were about the clock — how to oil the gears, when to replace the ropes, "
        "which parts needed attention each season.\n\n"
        "But the last few pages were different. The handwriting was faster, less neat. "
        "There were strange drawings — shapes that looked like parts of the tower wall. "
        "One drawing showed a section of stone with an arrow pointing to a gap between "
        "two blocks.\n\n"
        "Next to the drawing, Whitfield had written: \"Found it. Behind the north wall. "
        "Hidden for a long time. Must be careful.\"\n\n"
        "Mai felt her heart beat faster. She looked at the north wall of the workshop. "
        "It was made of large grey stones, just like the rest of the tower. She ran her "
        "fingers along the wall, pressing each stone. Near the bottom, one stone moved "
        "slightly. There was a compartment behind it.\n\n"
        "She tried to pull the stone out, but it was too heavy. She could not open it "
        "alone."
    )

    passage_5 = (
        "Mai stepped back from the wall and took a deep breath. She could not open the "
        "hidden compartment today, but she had found something important.\n\n"
        "She took out her phone and began to take photographs. She photographed the "
        "workshop, the tools on the table, the half-finished clock, and the leather "
        "journal. She took close pictures of the last pages with the strange drawings. "
        "She also photographed the loose stone in the north wall.\n\n"
        "\"This is real evidence,\" she said quietly to herself. She was not just "
        "writing a travel article anymore. She was following a trail that the clockmaker "
        "had left behind.\n\n"
        "Mai put the journal back on the table exactly where she had found it. She did "
        "not want anyone to know she had been looking through it. She walked down the "
        "staircase and locked the tower door behind her.\n\n"
        "As she walked back across the square, she felt excited. She had found her "
        "first real clue. The mystery of the silent clocktower was beginning to open."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai quyết định vào bên trong tháp đồng hồ để tìm câu trả lời. Với sự giúp đỡ "
        "của Lily, cô mượn được chìa khóa từ văn phòng hội đồng thị trấn. Bên trong "
        "tháp, cô khám phá xưởng làm việc của ông Whitfield trên tầng hai — nơi mọi "
        "thứ vẫn còn nguyên vẹn như ngày ông rời đi. Mai tìm thấy một cuốn nhật ký "
        "bằng da với những bản vẽ kỳ lạ và phát hiện một viên đá lỏng trong tường. "
        "Bạn sẽ ôn lại 15 từ vựng quen thuộc: permission, council, borrow, dust, "
        "machinery, staircase, workshop, repair, leather, drawing, hidden, compartment, "
        "photograph, evidence, clue. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn "
        "truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe "
        "lại cả chương — giúp bạn đọc trôi chảy và tự tin hơn với tiếng Anh."
    )

    description = (
        "Chương 3 kể về chuyến khám phá tháp đồng hồ của Mai. Cô tìm thấy xưởng làm "
        "việc của ông Whitfield, một cuốn nhật ký bí ẩn và dấu vết của một ngăn bí mật "
        "trong tường. Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 3: Bên Trong Tháp (Inside the Tower)",
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
                "title": "Flashcards: Ôn tập Bên Trong Tháp",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Bên Trong Tháp.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
