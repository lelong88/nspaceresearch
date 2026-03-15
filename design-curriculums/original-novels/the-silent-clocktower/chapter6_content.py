"""
Chapter 6: Ngăn Bí Mật (The Secret Compartment)
Investigation intensifies — Mai and David open the hidden compartment and find old documents.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 6."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["torch", "shadow", "beneath"]
    vocab_2 = ["metal", "document", "property"]
    vocab_3 = ["tunnel", "underground", "valuable"]
    vocab_4 = ["figure", "opposite", "pretend"]
    vocab_5 = ["benefit", "ownership", "investigate"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Mai woke up before the sun. The sky outside her window was still dark grey. "
        "She dressed quickly and quietly, picked up the leather journal, and went "
        "downstairs. Mrs. Blackwood was not awake yet. The house was silent.\n\n"
        "David was waiting outside the bed and breakfast. He had a small torch in his "
        "hand. \"We should go now,\" he whispered. \"Before anyone sees us.\"\n\n"
        "They walked across the empty square toward the clocktower. Their footsteps "
        "were the only sound. The tower stood tall and dark against the early morning "
        "sky. A long shadow fell across the cobblestones.\n\n"
        "David used his key to open the side door. Inside, the air was cold and still. "
        "Mai could smell the old wood and dust. They climbed the narrow staircase to "
        "the workshop on the second floor.\n\n"
        "Mai opened the journal to the page with the drawing. It showed the north wall "
        "of the workshop. There was a mark beneath the third stone from the left. "
        "\"This is it,\" she said. \"The compartment is behind this wall.\""
    )

    passage_2 = (
        "David knelt down beside the north wall. He ran his fingers along the stones "
        "until he found the one that was loose. It moved slightly when he pushed it.\n\n"
        "\"Help me with this,\" he said.\n\n"
        "Together, they pulled the stone out carefully. Behind it, there was a dark "
        "space in the wall, about the size of a shoebox. Mai pointed the torch inside. "
        "Something was there — a small metal box, covered in dust.\n\n"
        "David reached in and lifted the box out. It was heavy for its size. The lid "
        "was not locked. He opened it slowly.\n\n"
        "Inside, there were several old papers. The first was a document with a red "
        "stamp at the bottom. Mai picked it up carefully. It was a deed — a legal "
        "paper that showed who owned a building. The date at the top said 1890.\n\n"
        "\"This is a deed for the clocktower,\" Mai said, reading slowly. \"It says "
        "the tower is private property. It belongs to a family called Hargrove.\" She "
        "looked at David. \"The town does not own this tower. A family does.\""
    )

    passage_3 = (
        "David took the deed and read it again. \"The Hargrove family,\" he said. "
        "\"I have never heard that name in Eldermere.\"\n\n"
        "Mai looked at the other papers in the box. There was a second document — a "
        "hand-drawn map on old yellow paper. It showed the clocktower from above, and "
        "beneath the tower, there were lines going in different directions.\n\n"
        "\"These are tunnels,\" Mai said, tracing the lines with her finger. \"There "
        "is an underground network below the tower. Look — one tunnel goes toward the "
        "river, and another goes under the square.\"\n\n"
        "David stared at the map. \"Why would there be tunnels under a clocktower?\"\n\n"
        "\"I do not know yet,\" Mai said. \"But this land must be valuable. The tower "
        "sits on top of something — tunnels, maybe old rooms or storage. If the "
        "Hargrove family owned all of this, then the clocktower is worth much more "
        "than anyone thinks.\"\n\n"
        "She put the papers back in the box carefully. \"Your uncle found this. And "
        "I think someone else wanted to find it too.\""
    )

    passage_4 = (
        "They put the stone back in the wall and made sure everything looked the same "
        "as before. Mai carried the metal box inside her bag. They went back down the "
        "staircase and out through the side door.\n\n"
        "The square was still quiet. The sun was just coming up over the hills. A few "
        "birds were singing. It looked like a peaceful morning.\n\n"
        "But as they walked across the square, Mai stopped. She had seen something. "
        "On the opposite side of the square, near the post office, there was a figure "
        "standing in the shadow of a doorway. The person was watching them.\n\n"
        "\"David,\" Mai said quietly. \"Do not look now. Someone is across the square.\"\n\n"
        "David kept walking. \"Who is it?\"\n\n"
        "\"I cannot see clearly. They are standing in the dark.\" Mai's heart was "
        "beating fast. She tried to pretend that everything was normal. She smiled and "
        "talked about the weather as they walked toward the bed and breakfast.\n\n"
        "When she looked back a moment later, the figure was gone."
    )

    passage_5 = (
        "Back in Mai's room, they spread the papers on the bed. The deed, the map, "
        "and a few other old notes. Mai took photographs of everything with her phone.\n\n"
        "\"We need to keep this secret for now,\" she said. \"If someone was watching "
        "us, they already know we went to the tower. But they do not know what we "
        "found.\"\n\n"
        "David agreed. \"My uncle hid these papers for a reason. He did not want "
        "certain people to find them.\"\n\n"
        "Mai thought about the deed. The clocktower was private property, not town "
        "property. But everyone in Eldermere believed the town owned it. The town "
        "council managed the tower and made decisions about it.\n\n"
        "\"Who would benefit from hiding the true ownership?\" Mai asked. \"Someone "
        "on the town council, maybe. If the tower is actually private property, the "
        "council has no right to control it.\"\n\n"
        "She picked up her notebook and wrote a list of questions. She needed to "
        "investigate the Hargrove family, the town council records, and the history "
        "of the clocktower. The mystery was getting deeper, and Mai felt they were "
        "running out of time."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai và David đến tháp đồng hồ vào sáng sớm để mở ngăn bí mật trong bức "
        "tường. Họ tìm thấy một hộp kim loại chứa những tài liệu cũ — một giấy chứng "
        "nhận quyền sở hữu từ năm 1890 cho thấy tháp đồng hồ là tài sản tư nhân, "
        "không phải của thị trấn. Bên trong còn có bản đồ vẽ tay về hệ thống đường "
        "hầm ngầm bên dưới tháp. Khi rời đi, Mai nhận thấy có người đang theo dõi "
        "họ từ phía bên kia quảng trường. Bạn sẽ ôn lại 15 từ vựng quen thuộc: "
        "torch, shadow, beneath, metal, document, property, tunnel, underground, "
        "valuable, figure, opposite, pretend, benefit, ownership, investigate. Mỗi "
        "buổi học gồm thẻ từ vựng nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe "
        "theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe lại cả chương — giúp bạn đọc "
        "trôi chảy và tự tin hơn với tiếng Anh."
    )

    description = (
        "Chương 6 đánh dấu bước ngoặt quan trọng — Mai và David mở ngăn bí mật trong "
        "tháp đồng hồ, phát hiện tài liệu chứng minh tháp là tài sản tư nhân và bản "
        "đồ đường hầm ngầm. Ai đó đang theo dõi họ. Bạn sẽ luyện đọc 5 đoạn văn với "
        "15 từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 6: Ngăn Bí Mật (The Secret Compartment)",
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
                "title": "Flashcards: Ôn tập Ngăn Bí Mật",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Ngăn Bí Mật.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
