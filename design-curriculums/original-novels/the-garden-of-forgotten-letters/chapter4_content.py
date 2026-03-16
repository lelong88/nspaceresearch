"""
Chapter 4: Đào Bới (The Dig)
Linh starts digging in the garden and finds a metal box with old photographs and a map.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 4."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["shovel", "root", "sweat"]
    vocab_2 = ["metal", "rust", "lid"]
    vocab_3 = ["treasure", "bundle", "ribbon"]
    vocab_4 = ["portrait", "wedding", "generation"]
    vocab_5 = ["sketch", "location", "clue"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Linh woke up early the next morning. She put on old clothes and went to the "
        "garden shed. Inside, she found tools — a shovel, a rake, and gardening gloves. "
        "She carried the shovel to the rose garden at the back.\n\n"
        "The rose bushes grew in a circle around a flat stone. Linh remembered Mrs. "
        "Patterson's words: dig where the roses grow. She pushed the shovel into the "
        "earth next to the stone.\n\n"
        "The ground was hard. Thick roots from the rose bushes made it difficult. Linh "
        "had to cut through them carefully. She did not want to damage the plants. After "
        "thirty minutes, she had made a hole about half a metre deep.\n\n"
        "The morning sun was warm on her back. Sweat ran down her face. She stopped to "
        "drink water and looked at the hole. Nothing yet. She picked up the shovel and "
        "kept digging."
    )

    passage_2 = (
        "After another twenty minutes, the shovel hit something hard. Linh dropped to "
        "her knees and used her hands to clear away the soil. She could feel something "
        "flat and solid. She brushed away more dirt and saw it — a metal box, about the "
        "size of a large book.\n\n"
        "The box was dark green, covered in rust and dirt. Linh pulled it out of the "
        "ground carefully. It was heavy. She wiped the top with her sleeve. There were "
        "letters pressed into the metal, but she could not read them yet.\n\n"
        "She tried to open the lid. It was stuck. Years of being underground had sealed "
        "it shut. Linh carried the box inside to the kitchen table. She used a knife to "
        "work around the edges. Slowly, the lid began to move. With one final pull, it "
        "came open.\n\n"
        "Inside, the box was dry. Whatever was in there had been protected from the water "
        "and the earth."
    )

    passage_3 = (
        "Linh looked inside the box. On top, there was a small cloth bag tied with a "
        "blue ribbon. She untied it carefully and opened it. Inside was a treasure she "
        "had not expected — old photographs, dozens of them.\n\n"
        "She spread them on the table. They showed people she did not know, in clothes "
        "from long ago. Women in long dresses. Men in hats. Children playing in a "
        "garden — this garden.\n\n"
        "Under the photographs, there was a bundle of papers tied together with another "
        "ribbon, this one red and faded. Linh untied it. The papers were old documents "
        "— birth certificates, land records, and letters written in beautiful old "
        "handwriting.\n\n"
        "At the very bottom of the box, there was a small leather notebook. Linh picked "
        "it up. The cover was soft and worn. She opened it to the first page. In her "
        "grandmother's handwriting, it said: \"The story of our family. For Linh.\""
    )

    passage_4 = (
        "Linh spent the afternoon looking through the photographs. Many had names and "
        "dates written on the back. She began to understand — these were her family, "
        "going back over a hundred years.\n\n"
        "There was a portrait of a serious-looking woman in a dark dress. On the back "
        "it said: \"Eleanor Tran, 1920.\" Linh stared at the name. Tran. Her family "
        "name. But this woman was English.\n\n"
        "Another photograph showed a wedding. A young English woman stood next to a "
        "Vietnamese man in a suit. They were smiling. The back said: \"Eleanor and "
        "Minh Tran, wedding day, 1918.\"\n\n"
        "Linh's heart was beating fast. Her family's connection to Vietnam was not just "
        "through her father. It went back generations — over a hundred years. Her "
        "great-great-grandmother had married a Vietnamese man in England in 1918. This "
        "house, this garden, had been in her family all that time."
    )

    passage_5 = (
        "The leather notebook was the most interesting thing in the box. Her grandmother "
        "had written the family history in it, starting from 1918. But on the last few "
        "pages, there was something different — a sketch.\n\n"
        "It was a drawing of the garden, seen from above. Linh recognised the shape — "
        "the rose circle, the greenhouse, the orchard. But there were marks on the "
        "drawing that she did not understand. Small crosses in different locations, "
        "each with a number next to it.\n\n"
        "Under the sketch, her grandmother had written: \"Seven gifts for seven "
        "generations. Each one in its place. Each one a clue to the next.\"\n\n"
        "Linh counted the crosses on the map. There were seven. She had found the first "
        "one — the metal box under the roses. That meant there were six more things "
        "buried in the garden. Six more secrets waiting to be found.\n\n"
        "She looked out at the wild garden with new eyes. It was not just a garden. It "
        "was a map. And she was going to follow it."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh bắt đầu đào khu vườn theo lời dặn của bà ngoại và tìm thấy một chiếc "
        "hộp kim loại chôn dưới gốc hoa hồng. Bên trong là kho báu bất ngờ — hàng chục "
        "bức ảnh cũ của gia đình qua nhiều thế hệ, giấy tờ cổ, và một cuốn sổ da ghi "
        "lịch sử gia đình. Linh phát hiện gia đình mình có gốc Việt từ năm 1918 khi "
        "cụ bà kết hôn với một người đàn ông Việt Nam. Trang cuối cuốn sổ là bản vẽ "
        "khu vườn với 7 dấu chéo — 7 món quà cho 7 thế hệ. Bạn sẽ ôn lại 15 từ vựng: "
        "shovel, root, sweat, metal, rust, lid, treasure, bundle, ribbon, portrait, "
        "wedding, generation, sketch, location, clue. Mỗi buổi học gồm thẻ từ vựng "
        "nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn "
        "bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 4: Linh đào khu vườn và tìm thấy hộp kim loại chứa ảnh gia đình cổ, "
        "bí mật về gốc Việt từ năm 1918, và bản đồ 7 món quà chôn giấu trong vườn. "
        "Luyện đọc 5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 4: Đào Bới (The Dig)",
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
                "title": "Flashcards: Ôn tập Đào Bới",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Đào Bới.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
