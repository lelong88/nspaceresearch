"""
Chapter 4: Người Lạ Trong Thị Trấn (The Stranger in Town)
Deeper investigation — the journal disappears, Mai discovers someone else is interested in the clocktower.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 4."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["discover", "shock", "overnight"]
    vocab_2 = ["lock", "entrance", "impossible"]
    vocab_3 = ["notice", "coat", "newspaper"]
    vocab_4 = ["inn", "edge", "direction"]
    vocab_5 = ["uneasy", "suspect", "connection"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "The next morning, Mai went to find Tom at the pub. She needed someone strong "
        "to help her move the loose stone in the tower wall. She told him about the "
        "workshop, the leather journal, and the hidden compartment.\n\n"
        "Tom listened carefully. \"A secret compartment? That sounds like something "
        "from a film,\" he said. But he could see Mai was serious. \"All right. Let "
        "me close the pub for an hour. I will come with you.\"\n\n"
        "They walked across the square together. Mai unlocked the tower door and led "
        "Tom up the narrow staircase to the workshop. Everything looked the same — the "
        "tools, the half-finished clock, the chair.\n\n"
        "But when Mai looked at the table, she stopped. The leather journal was gone. "
        "She felt a wave of shock. \"It was right here,\" she said, pointing at the "
        "empty space on the table. \"I left it here yesterday.\"\n\n"
        "Tom looked around the room. \"Are you sure?\" Mai nodded. Someone had come "
        "into the tower overnight and taken the journal. She could not believe what "
        "she had just discovered. The only question was — who?"
    )

    passage_2 = (
        "Mai and Tom searched the workshop carefully. They looked under the table, "
        "behind the shelves, and in every corner. The journal was not there. Someone "
        "had taken it.\n\n"
        "\"Who else has a key to this tower?\" Mai asked.\n\n"
        "\"Only the council man,\" Tom said. \"He keeps the key in his office. You "
        "borrowed it yesterday, and you returned it before five.\"\n\n"
        "Mai thought about this. She had locked the door when she left. The lock "
        "on the tower door was old but strong. There was only one entrance — the "
        "wooden door at the bottom.\n\n"
        "\"So it is impossible for someone to get in without a key,\" Mai said slowly.\n\n"
        "\"Unless they had their own key,\" Tom replied. \"Or unless someone made a "
        "copy.\"\n\n"
        "Mai felt cold. Someone knew she had been inside the tower. Someone knew about "
        "the journal. And that person had come in the night to take it. This was not "
        "just a story about a missing clockmaker anymore. Someone in this town was "
        "hiding something."
    )

    passage_3 = (
        "Mai needed to think. She thanked Tom and walked to Mrs. Chen's tea shop. A "
        "cup of tea always helped her clear her mind.\n\n"
        "The tea shop was warm and busy. Two women sat near the window, talking quietly. "
        "An old man was reading a book in the corner. And at a table near the door, Mai "
        "noticed someone she had not seen before.\n\n"
        "He was a tall man, perhaps forty years old, wearing a long dark coat. He sat "
        "alone, holding a newspaper in front of his face. He did not look up when Mai "
        "came in. There was something careful about him, as if he did not want to be "
        "seen.\n\n"
        "Mai sat down at her usual table. Mrs. Chen brought her tea without being "
        "asked. \"Who is that man?\" Mai whispered, looking toward the door.\n\n"
        "Mrs. Chen glanced over. \"He is new,\" she said quietly. \"He came in here "
        "yesterday for the first time. He ordered black tea and sat for two hours. He "
        "did not talk to anyone.\" She paused. \"He asked me one question — where is "
        "the clocktower?\""
    )

    passage_4 = (
        "Mai watched the man from the corner of her eye. He turned the pages of his "
        "newspaper slowly, but she was not sure he was really reading. His eyes moved "
        "around the room from time to time.\n\n"
        "After he left, Mai asked Mrs. Chen more questions. \"Do you know where he is "
        "staying?\"\n\n"
        "\"At the inn,\" Mrs. Chen said. \"The old one on the edge of town, past the "
        "church. Mrs. Palmer runs it. He arrived two days ago, she told me.\"\n\n"
        "\"Two days ago,\" Mai repeated. That was the same day Mai had first gone to "
        "the council office to ask about the tower.\n\n"
        "\"Did he say why he was here?\" Mai asked.\n\n"
        "Mrs. Chen shook her head. \"He did not say much. But he walked in the "
        "direction of the clocktower yesterday afternoon. I saw him from the window. "
        "He stood in the square and looked up at the tower for a long time.\"\n\n"
        "Mai wrote everything down in her notebook. A stranger who arrived two days "
        "ago, who asked about the clocktower, who walked toward it. The timing was "
        "too close to be nothing."
    )

    passage_5 = (
        "That evening, Mai sat in her room at the bed and breakfast. She looked out "
        "at the clocktower. The hands still pointed to twenty past three. The square "
        "was empty and dark.\n\n"
        "She opened her notebook and read her notes from the day. The journal was "
        "gone. The tower had been locked. A stranger had arrived in town and was "
        "asking about the clocktower. Mai felt uneasy. Too many things were happening "
        "at the same time.\n\n"
        "She wrote: \"The stranger — who is he? Why is he here? He is my main suspect "
        "for now. He arrived at the right time. He asked about the tower. He could "
        "have taken the journal.\"\n\n"
        "But she also wrote: \"I need more than feelings. I need to find a real "
        "connection between this man and the missing journal. Or between him and "
        "Mr. Whitfield.\"\n\n"
        "Mai closed her notebook and turned off the light. Tomorrow she would go to "
        "the inn and try to learn more about the stranger. She had a feeling that "
        "this man was a piece of the puzzle she could not yet see."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai nhờ Tom giúp mở ngăn bí mật trong tháp, nhưng khi họ quay lại, cuốn nhật "
        "ký của ông Whitfield đã biến mất. Ai đó đã vào tháp trong đêm và lấy nó đi. "
        "Mai bắt đầu điều tra — ai có chìa khóa? Tháp chỉ có một lối vào duy nhất. "
        "Tại tiệm trà của bà Chen, Mai nhận ra một người đàn ông lạ mặc áo khoác tối "
        "đang đọc báo — ông ta mới đến thị trấn hai ngày trước và đã hỏi về tháp đồng "
        "hồ. Bạn sẽ ôn lại 15 từ vựng quen thuộc: discover, shock, overnight, lock, "
        "entrance, impossible, notice, coat, newspaper, inn, edge, direction, uneasy, "
        "suspect, connection. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn truyện "
        "hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe lại cả "
        "chương — giúp bạn đọc trôi chảy và tự tin hơn với tiếng Anh."
    )

    description = (
        "Chương 4 kể về sự biến mất bí ẩn của cuốn nhật ký và sự xuất hiện của một "
        "người lạ trong thị trấn. Mai bắt đầu nghi ngờ và tìm kiếm mối liên hệ giữa "
        "người đàn ông lạ mặt và tháp đồng hồ. Bạn sẽ luyện đọc 5 đoạn văn với 15 "
        "từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 4: Người Lạ Trong Thị Trấn (The Stranger in Town)",
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
                "title": "Flashcards: Ôn tập Người Lạ Trong Thị Trấn",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Người Lạ Trong Thị Trấn.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
