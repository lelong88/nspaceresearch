"""
Chapter 5: Cuốn Sổ Gia Đình (The Family Notebook)
Linh reads the family history and discovers the story of Eleanor and Minh Tran.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 5."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["soldier", "wound", "hospital"]
    vocab_2 = ["gentle", "patient", "recover"]
    vocab_3 = ["prejudice", "accept", "community"]
    vocab_4 = ["plant", "seed", "tradition"]
    vocab_5 = ["heritage", "identity", "belong"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Linh sat in the living room with the leather notebook open on her lap. Her "
        "grandmother had written the family story in clear, simple English. It began "
        "in 1917, during the First World War.\n\n"
        "Minh Tran was a young Vietnamese man who had come to Europe as a soldier in "
        "the French army. Vietnam was part of France's empire at that time. Minh fought "
        "in the trenches in northern France. In 1917, he received a serious wound to "
        "his leg during a battle.\n\n"
        "He was sent to a hospital in southern England to recover. The hospital was in "
        "a large country house, not far from Willowbrook. It had been turned into a "
        "place for wounded soldiers from many countries.\n\n"
        "Linh looked at the old photograph of Minh. He was young, perhaps twenty-two, "
        "with dark eyes and a serious face. He was standing with other soldiers, his "
        "arm in a sling. She touched the photograph gently. This was her great-great-"
        "grandfather."
    )

    passage_2 = (
        "Eleanor Marsh was nineteen years old and worked as a nurse at the hospital. "
        "She was from Willowbrook. Her father was a farmer and her mother made bread "
        "for the village bakery.\n\n"
        "Eleanor was gentle and kind. She took care of all the soldiers, but she spent "
        "extra time with Minh because he spoke very little English. She was patient "
        "with him. She taught him words, one by one, using pictures and gestures.\n\n"
        "\"She drew pictures of things,\" the notebook said. \"A cup. A tree. A bird. "
        "And he would say the English word. Then he would teach her the Vietnamese "
        "word. They learned from each other.\"\n\n"
        "Slowly, Minh began to recover. His leg healed, but he did not want to leave "
        "the hospital. He did not want to leave Eleanor. And Eleanor did not want him "
        "to go.\n\n"
        "Linh smiled as she read. It was a love story. Her family began with a nurse "
        "and a soldier, learning each other's language one word at a time."
    )

    passage_3 = (
        "The war ended in November 1918. Minh was free to go home to Vietnam, but he "
        "chose to stay in England. He and Eleanor married in December 1918, in the "
        "small church in Willowbrook.\n\n"
        "Not everyone was happy. Some people in the village showed prejudice against "
        "Minh because he was different. They did not understand why Eleanor had married "
        "a man from so far away. Her own father did not accept the marriage at first.\n\n"
        "But Minh was a hard worker. He helped on the farms. He fixed things. He was "
        "quiet and polite. Slowly, the community began to accept him. The children "
        "loved him because he told them stories about dragons and rice fields and "
        "mountains covered in clouds.\n\n"
        "\"It took time,\" the notebook said. \"But Minh won them over with his hands "
        "and his heart. By the time their first child was born, even Eleanor's father "
        "called Minh his son.\""
    )

    passage_4 = (
        "Minh and Eleanor bought Maple Cottage in 1920. The house had a large garden, "
        "and Minh began to plant things. He grew vegetables he remembered from Vietnam "
        "— herbs, beans, and greens. He also grew English flowers that Eleanor loved.\n\n"
        "\"The garden was their shared language,\" the notebook said. \"Minh brought "
        "seeds from his world, and Eleanor brought seeds from hers. Together they "
        "created something new.\"\n\n"
        "Every generation of the family added something to the garden. Minh and "
        "Eleanor's daughter planted the apple orchard. Their grandson built the "
        "greenhouse. Rose — Linh's grandmother — planted the rose circle.\n\n"
        "The garden was a tradition passed down through the family. Each generation "
        "left their mark. Each generation added their own plants, their own paths, "
        "their own stories.\n\n"
        "Linh understood now why the garden was so important. It was not just a garden. "
        "It was a family tree, growing in soil instead of on paper."
    )

    passage_5 = (
        "The last pages of the notebook were written directly to Linh. Her grandmother's "
        "handwriting was shaky but clear.\n\n"
        "\"Dear Linh, you carry a special heritage. You are Vietnamese and English and "
        "Australian. You are the child of two worlds, just like Minh was. Do not let "
        "anyone tell you that you do not belong. You belong everywhere.\"\n\n"
        "\"I buried this box because I wanted you to know your identity. Your mother "
        "left England angry, and I was too proud to say sorry. But our family story is "
        "bigger than one argument. It goes back a hundred years, to a soldier and a "
        "nurse who chose love over fear.\"\n\n"
        "\"The garden holds six more gifts. Each one was left by a different generation. "
        "Find them, and you will find us. We are all here, in the soil and the roots "
        "and the flowers.\"\n\n"
        "Linh closed the notebook. Tears ran down her face, but she was smiling. She "
        "finally understood where she came from. And she knew what she had to do next."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh đọc cuốn sổ gia đình và khám phá câu chuyện tình yêu đẹp đẽ của cụ cố "
        "— Eleanor, cô y tá người Anh, và Minh Tran, người lính Việt Nam bị thương "
        "trong Thế chiến I. Họ gặp nhau trong bệnh viện, dạy nhau ngôn ngữ qua hình "
        "vẽ, và kết hôn năm 1918 bất chấp định kiến. Khu vườn Maple Cottage trở thành "
        "ngôn ngữ chung của họ — nơi mỗi thế hệ để lại dấu ấn riêng. Bà ngoại viết "
        "cho Linh: 'Con mang trong mình di sản đặc biệt.' Bạn sẽ ôn lại 15 từ vựng: "
        "soldier, wound, hospital, gentle, patient, recover, prejudice, accept, "
        "community, plant, seed, tradition, heritage, identity, belong. Mỗi buổi học "
        "gồm thẻ từ vựng nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. "
        "Buổi 6 tổng ôn toàn bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 5: Linh đọc lịch sử gia đình — câu chuyện tình yêu giữa cô y tá Anh "
        "và người lính Việt Nam trong Thế chiến I, và cách khu vườn trở thành di sản "
        "qua nhiều thế hệ. Luyện đọc 5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 5: Cuốn Sổ Gia Đình (The Family Notebook)",
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
                "title": "Flashcards: Ôn tập Cuốn Sổ Gia Đình",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Cuốn Sổ Gia Đình.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
