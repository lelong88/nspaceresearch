"""
Chapter 1: Ngôi Nhà Trên Đồi (The House on the Hill)
Setup chapter — introduces Linh, the old house, and the overgrown garden.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 1."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["inherit", "countryside", "luggage"]
    vocab_2 = ["overgrown", "fence", "pathway"]
    vocab_3 = ["dusty", "furniture", "photograph"]
    vocab_4 = ["garden", "wildflower", "greenhouse"]
    vocab_5 = ["envelope", "drawer", "handwriting"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Linh Tran sat on the bus and watched the English countryside pass by. Green "
        "fields stretched in every direction. Sheep stood in groups under old trees. She "
        "was seventeen years old and had never been to England before.\n\n"
        "Her grandmother had died two months ago. Linh had never met her. Her mother "
        "had left England thirty years ago and never went back. Now Linh had come to "
        "inherit the house. Her mother could not travel because of her work, so Linh "
        "came alone.\n\n"
        "The bus stopped in a small village called Willowbrook. Linh picked up her "
        "luggage — one big suitcase and a backpack — and stepped off. The air smelled "
        "like grass and rain. A woman at the bus stop smiled at her.\n\n"
        "\"Are you looking for Maple Cottage?\" the woman asked. \"You must be Rose's "
        "granddaughter. She talked about you all the time.\""
    )

    passage_2 = (
        "Linh walked up a narrow lane for ten minutes. At the end, she found the house. "
        "It was a small stone cottage with a red roof. But it looked tired. The paint on "
        "the door was old and cracked. The windows were dark.\n\n"
        "The front garden was completely overgrown. Tall grass and weeds covered "
        "everything. Linh could see the shape of what had once been a flower bed, but "
        "now it was wild and messy.\n\n"
        "A wooden fence ran around the property. Some parts were broken. Linh pushed "
        "open the gate, which made a loud sound. She walked up the pathway to the front "
        "door. Small stones crunched under her shoes.\n\n"
        "She took the key from her pocket. The lawyer had sent it to her in Australia. "
        "She put it in the lock and turned. The door opened slowly with a long creak."
    )

    passage_3 = (
        "Inside, the house was dark and quiet. Linh found a light switch and turned it "
        "on. A warm yellow light filled the hallway. The walls were covered with old "
        "wallpaper — small blue flowers on a cream background.\n\n"
        "Everything was dusty. A thin layer of dust covered every surface. Linh walked "
        "into the living room. There was old furniture everywhere — a sofa with a "
        "blanket on it, a bookshelf full of books, and a small table with a teacup "
        "still sitting on it.\n\n"
        "On the wall above the fireplace, there was a photograph in a wooden frame. "
        "Linh stepped closer. It showed a young woman standing in a beautiful garden, "
        "holding a baby. The woman was smiling. Linh looked at the baby's face and "
        "felt her heart beat faster. That baby was her mother.\n\n"
        "She touched the glass gently. This was the first time she had seen her "
        "grandmother's face."
    )

    passage_4 = (
        "Linh opened the back door and stepped outside. The back garden was much bigger "
        "than the front. It stretched down a gentle slope toward a line of trees. Like "
        "the front, it was wild and untidy, but Linh could see that it had once been "
        "something special.\n\n"
        "There were paths made of flat stones, now hidden under grass. Old rose bushes "
        "grew in thick tangles. And everywhere, there were wildflowers — yellow, purple, "
        "white — growing freely between the weeds.\n\n"
        "At the bottom of the garden, half hidden by climbing plants, Linh saw a small "
        "greenhouse. Its glass walls were dirty and some panels were cracked, but it was "
        "still standing. She walked down to it and looked through the glass. Inside, she "
        "could see empty plant pots, bags of soil, and a wooden workbench.\n\n"
        "This garden had been loved once. Linh could feel it. She wondered what it had "
        "looked like when her grandmother was alive."
    )

    passage_5 = (
        "That evening, Linh explored the house more carefully. In the bedroom upstairs, "
        "she found a large wooden desk by the window. The desk had three drawers on "
        "each side.\n\n"
        "She opened the first drawer. Inside, there were pens, a ruler, and some old "
        "stamps. The second drawer had notebooks. But the third drawer was different. "
        "It was full of envelopes — dozens of them, all sealed, all with stamps, all "
        "with addresses written on them.\n\n"
        "Linh picked one up. The envelope was yellow with age. The address was in "
        "Australia — her mother's address. The handwriting was neat and careful, with "
        "small round letters.\n\n"
        "She picked up another envelope. Same address. And another. They were all "
        "addressed to her mother. But none of them had been posted. Her grandmother "
        "had written all these letters but never sent them.\n\n"
        "Linh sat on the bed and held the letters in her hands. Why had her grandmother "
        "written so many letters and never posted them? What did they say?"
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh Tran, cô gái 17 tuổi người Úc gốc Việt, một mình đến ngôi làng nhỏ "
        "Willowbrook ở nước Anh để nhận ngôi nhà thừa kế từ bà ngoại — người mà cô "
        "chưa bao giờ gặp. Khi bước vào Maple Cottage, cô khám phá ngôi nhà phủ bụi "
        "với đồ đạc cũ kỹ, bức ảnh bà ngoại bế mẹ cô khi còn nhỏ, và khu vườn hoang "
        "dại từng rất đẹp. Nhưng phát hiện lớn nhất nằm trong ngăn kéo bàn — hàng chục "
        "lá thư viết cho mẹ cô nhưng chưa bao giờ được gửi đi. Bạn sẽ ôn lại 15 từ "
        "vựng quen thuộc: inherit, countryside, luggage, overgrown, fence, pathway, "
        "dusty, furniture, photograph, garden, wildflower, greenhouse, envelope, drawer, "
        "handwriting. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn truyện hấp dẫn "
        "và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 1 giới thiệu Linh Tran đến ngôi nhà thừa kế ở Willowbrook, nơi cô "
        "khám phá khu vườn hoang dại và những lá thư bí ẩn chưa bao giờ được gửi đi "
        "của bà ngoại. Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung "
        "cấp, rèn kỹ năng đọc hiểu qua ngữ cảnh tự nhiên."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 1: Ngôi Nhà Trên Đồi (The House on the Hill)",
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
                "title": "Flashcards: Ôn tập Ngôi Nhà Trên Đồi",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Ngôi Nhà Trên Đồi.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
