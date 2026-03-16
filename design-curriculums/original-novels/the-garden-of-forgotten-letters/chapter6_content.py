"""
Chapter 6: Những Món Quà Trong Vườn (The Garden Gifts)
Linh finds more buried items and the village learns about her project.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 6."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["compass", "brass", "polish"]
    vocab_2 = ["pottery", "crack", "delicate"]
    vocab_3 = ["locket", "chain", "precious"]
    vocab_4 = ["volunteer", "eager", "restore"]
    vocab_5 = ["gather", "celebrate", "grateful"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Over the next three days, Linh followed the map in the notebook. The second "
        "cross was near the old apple tree in the orchard. She dug carefully and found "
        "a small wooden box.\n\n"
        "Inside was a compass. It was old and beautiful, made of brass. The glass was "
        "scratched but the needle still moved. On the back, someone had carved the "
        "letters M.T. — Minh Tran.\n\n"
        "Linh held it in her hand. This compass had belonged to her great-great-"
        "grandfather. He had probably carried it during the war. She used her sleeve "
        "to polish the surface until it shone.\n\n"
        "She checked the notebook. Next to the second cross, her grandmother had "
        "written: \"Minh's compass. He said it always pointed him toward home. After "
        "he met Eleanor, home was Willowbrook.\"\n\n"
        "Linh put the compass on the kitchen table next to the photographs. Her "
        "collection of family treasures was growing."
    )

    passage_2 = (
        "The third gift was buried near the herb garden. It was a small piece of "
        "pottery — a bowl, painted with blue flowers. It was Vietnamese in style, "
        "very different from anything English.\n\n"
        "There was a crack running down one side, but it had been repaired with gold "
        "paint. The repair made it more beautiful, not less. Linh had seen this "
        "technique before — it was a Japanese art called kintsugi, fixing broken "
        "things with gold.\n\n"
        "The bowl was delicate and light. Linh turned it over. On the bottom, in tiny "
        "letters, it said: \"Made in Hanoi, 1910.\"\n\n"
        "The notebook explained: \"This bowl came with Minh from Vietnam. It broke "
        "during the journey. Eleanor fixed it with gold paint. She said broken things "
        "can be more beautiful than perfect things.\"\n\n"
        "Linh thought about her own family — broken by an argument, separated for "
        "thirty years. Could they be repaired too? Could the cracks become something "
        "beautiful?"
    )

    passage_3 = (
        "The fourth gift was the most personal. Buried near the greenhouse, Linh found "
        "a small silver locket on a thin chain. She opened it. Inside were two tiny "
        "photographs — one of Eleanor as a young woman, and one of Minh in his "
        "soldier's uniform.\n\n"
        "The locket was precious. Not because of the silver, but because of what it "
        "held. Two people who had chosen each other across every difference — language, "
        "culture, country.\n\n"
        "Linh put the chain around her neck. The locket sat against her chest, warm "
        "from the sun. She felt connected to Eleanor and Minh in a way she had never "
        "felt connected to anyone before.\n\n"
        "She sat in the garden for a long time, holding the locket and looking at the "
        "sky. The birds were singing. The wind moved through the apple trees. For the "
        "first time since arriving in Willowbrook, Linh did not feel like a stranger. "
        "She felt like she was home."
    )

    passage_4 = (
        "Word spread through the village about what Linh was doing. Mrs. Patterson "
        "told a few people, and soon everyone knew about the garden treasures and the "
        "family history.\n\n"
        "One morning, a man named Tom Harris knocked on the door. He was a gardener "
        "who worked at the big estate outside the village. \"I heard you are fixing up "
        "Rose's garden,\" he said. \"I would like to volunteer to help.\"\n\n"
        "Then came Sarah, a young woman who ran the village café. She was eager to "
        "help too. \"My grandmother knew your grandmother,\" she said. \"They were in "
        "the same gardening club.\"\n\n"
        "By the end of the week, Linh had a team of five volunteers. They came every "
        "morning to help restore the garden. Tom cut back the overgrown bushes. Sarah "
        "cleared the paths. Two teenagers from the village pulled weeds.\n\n"
        "Linh was amazed. These people did not know her, but they wanted to help. The "
        "garden was bringing the village together."
    )

    passage_5 = (
        "On Saturday evening, Mrs. Patterson organised a small dinner at her house. "
        "She invited Linh and all the volunteers. They sat around a big table in her "
        "garden and ate together.\n\n"
        "Linh told them about the family notebook — about Minh and Eleanor, about the "
        "compass and the bowl and the locket. Everyone listened quietly. When she "
        "finished, there was silence. Then Tom raised his glass.\n\n"
        "\"To Rose,\" he said. \"And to the garden.\"\n\n"
        "Everyone raised their glasses. Linh felt tears in her eyes. She looked around "
        "at the faces gathered around the table — people who had become friends in just "
        "a few days.\n\n"
        "\"Thank you,\" she said. \"I came here alone, and I did not know what to "
        "expect. I am so grateful for your help. This garden is not just my family's "
        "story. It belongs to this village too.\"\n\n"
        "Mrs. Patterson squeezed her hand. \"Your grandmother would be so happy to "
        "see this. She always wanted to celebrate the garden with the village. She "
        "just never found the right time.\""
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh tiếp tục theo bản đồ và tìm thêm ba món quà chôn trong vườn: chiếc la "
        "bàn đồng của cụ Minh từ thời chiến tranh, chiếc bát gốm Hà Nội được sửa bằng "
        "vàng, và chiếc mề đay bạc chứa ảnh Eleanor và Minh. Tin tức lan khắp làng và "
        "dân làng tình nguyện giúp Linh phục hồi khu vườn. Bữa tối cùng nhau kết thúc "
        "chương với cảm giác ấm áp về cộng đồng. Bạn sẽ ôn lại 15 từ vựng: compass, "
        "brass, polish, pottery, crack, delicate, locket, chain, precious, volunteer, "
        "eager, restore, gather, celebrate, grateful. Mỗi buổi học gồm thẻ từ vựng "
        "nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn "
        "bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 6: Linh tìm thêm ba món quà gia đình trong vườn — la bàn, bát gốm, "
        "mề đay — và dân làng tình nguyện giúp phục hồi khu vườn. Luyện đọc 5 đoạn "
        "văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 6: Những Món Quà Trong Vườn (The Garden Gifts)",
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
                "title": "Flashcards: Ôn tập Những Món Quà Trong Vườn",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Những Món Quà Trong Vườn.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
