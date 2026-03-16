"""
Chapter 10: Món Quà Cuối Cùng (The Last Gift)
Linh and her mother find the seventh gift and decide the future of the garden.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 10."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["ceremony", "speech", "audience"]
    vocab_2 = ["deed", "ownership", "legal"]
    vocab_3 = ["decision", "future", "opportunity"]
    vocab_4 = ["farewell", "departure", "platform"]
    vocab_5 = ["roots", "journey", "home"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "On their last day together in Willowbrook, Linh and her mother went to find "
        "the seventh gift. The final cross on the map was in the centre of the rose "
        "circle — the heart of the garden.\n\n"
        "Mrs. Patterson and the volunteers came to watch. It felt like a ceremony. "
        "Everyone stood in a circle around the roses while Linh and her mother dug "
        "together.\n\n"
        "Tom made a short speech. \"This garden has brought our village together,\" he "
        "said. \"Rose would be proud of what her granddaughter has done here.\"\n\n"
        "The small audience clapped. Linh smiled and kept digging. After ten minutes, "
        "the shovel hit something. She knelt down and brushed away the soil. It was "
        "another metal box, smaller than the first one.\n\n"
        "Linh lifted it out and placed it on the grass. Everyone leaned forward. She "
        "looked at her mother. \"You open it,\" she said. \"This one is for you too.\""
    )

    passage_2 = (
        "Linh's mother opened the box with shaking hands. Inside, there were two "
        "things. The first was a document — old, yellow, and folded carefully. She "
        "opened it and read it slowly.\n\n"
        "It was the deed to Maple Cottage. The original ownership document from 1920, "
        "when Minh and Eleanor bought the house. Every generation had signed it — Minh, "
        "Eleanor, their daughter, their grandson, and finally Rose.\n\n"
        "At the bottom, Rose had written: \"This house belongs to the Tran family. It "
        "always has. It always will.\"\n\n"
        "The second item was a legal envelope from a lawyer in the nearby town. Inside "
        "was Rose's will. She had left the house and garden to Linh — not to her mother, "
        "but to Linh specifically.\n\n"
        "\"She left it to you,\" her mother said, looking at Linh with surprise. \"Not "
        "to me. To you.\"\n\n"
        "Linh stared at the document. She was seventeen years old, and she owned a "
        "cottage in England."
    )

    passage_3 = (
        "That afternoon, Linh and her mother sat in the garden and talked about the "
        "future. The decision was not simple. Linh lived in Australia. She had school, "
        "friends, her whole life there. She could not move to England.\n\n"
        "\"But I do not want to sell it,\" Linh said firmly. \"This house has been in "
        "our family for over a hundred years. I cannot be the one who lets it go.\"\n\n"
        "Her mother nodded. \"I agree. But what do we do with it?\"\n\n"
        "They talked about different options. They could rent it out. They could come "
        "every summer. They could let Mrs. Patterson look after it.\n\n"
        "Then Linh had an idea. \"What if we turn the garden into a community garden? "
        "Open it to the village. Let people grow things here. It would be an opportunity "
        "for the whole village, not just our family.\"\n\n"
        "Her mother smiled. \"Your grandmother would love that. A garden for everyone. "
        "That is exactly what Minh and Eleanor would have wanted.\""
    )

    passage_4 = (
        "The next morning was Linh's last day. Her mother was staying one more week to "
        "arrange things with the lawyer, but Linh had to go back to school in Melbourne.\n\n"
        "She packed her suitcase slowly. She put the locket around her neck and the "
        "compass in her pocket. She left the photographs and the notebook in the house "
        "— they belonged here.\n\n"
        "Mrs. Patterson came to say farewell. She brought a jar of homemade jam and a "
        "card signed by everyone in the village. \"Come back soon,\" she said, hugging "
        "Linh tightly.\n\n"
        "Tom drove Linh and her mother to the train station. The departure was harder "
        "than Linh expected. She had only been here for three weeks, but Willowbrook "
        "felt like a second home.\n\n"
        "On the platform, her mother held her hands. \"Thank you, Linh. You did "
        "something I could not do for thirty years. You brought me home.\""
    )

    passage_5 = (
        "Linh sat on the train and watched Willowbrook disappear behind the hills. "
        "The fields were golden in the autumn light. Sheep stood under the trees, just "
        "like the day she arrived.\n\n"
        "She thought about everything that had happened. She had come to England to "
        "inherit a house. Instead, she had found her roots — a family story that "
        "stretched back a hundred years, from Vietnam to England to Australia and back "
        "again.\n\n"
        "The journey had changed her. She understood now that identity is not one thing. "
        "It is many things — many places, many people, many stories woven together. She "
        "was Vietnamese and English and Australian. She was Minh and Eleanor and Rose "
        "and her mother and herself.\n\n"
        "She touched the locket around her neck. Inside were two faces — a nurse and a "
        "soldier who had started everything with a few words and a lot of courage.\n\n"
        "Linh took out her notebook and began to write. She had a story to tell. And "
        "she knew exactly where it began — in a garden, with a letter that was never "
        "sent, and a girl who finally brought it home."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh và mẹ tìm món quà cuối cùng — giấy tờ nhà gốc từ 1920 và di chúc của "
        "bà ngoại để lại ngôi nhà cho Linh. Họ quyết định biến khu vườn thành vườn "
        "cộng đồng cho cả làng. Linh chia tay Willowbrook với chiếc mề đay trên cổ "
        "và la bàn trong túi, mang theo câu chuyện gia đình trải dài trăm năm từ Việt "
        "Nam đến Anh đến Úc. Bạn sẽ ôn lại 15 từ vựng: ceremony, speech, audience, "
        "deed, ownership, legal, decision, future, opportunity, farewell, departure, "
        "platform, roots, journey, home. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một "
        "đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và "
        "nghe lại cả chương."
    )

    description = (
        "Chương 10: Linh và mẹ tìm món quà cuối cùng, quyết định tương lai khu vườn, "
        "và Linh chia tay Willowbrook mang theo di sản gia đình trăm năm. Luyện đọc "
        "5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 10: Món Quà Cuối Cùng (The Last Gift)",
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
                "title": "Flashcards: Ôn tập Món Quà Cuối Cùng",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Món Quà Cuối Cùng.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
