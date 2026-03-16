"""
Chapter 9: Mẹ Về Nhà (Mother Comes Home)
Linh's mother arrives in Willowbrook and they explore the garden together.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 9."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["arrival", "embrace", "tremble"]
    vocab_2 = ["wander", "recognise", "unchanged"]
    vocab_3 = ["dig", "jar", "preserve"]
    vocab_4 = ["forgiveness", "burden", "release"]
    vocab_5 = ["transform", "blossom", "renewal"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Linh stood at the bus stop in Willowbrook, waiting. It was a cool October "
        "morning. The leaves on the trees were turning gold and red. She checked her "
        "phone again. Her mother's bus was due in five minutes.\n\n"
        "She had spent the last week preparing the house. She cleaned every room, "
        "washed the curtains, and put fresh flowers on the kitchen table. Mrs. Patterson "
        "had helped her make the spare bedroom comfortable.\n\n"
        "Then she saw the bus coming around the corner. Her heart started beating fast. "
        "The bus stopped and the doors opened. A woman stepped out — small, with dark "
        "hair and Linh's eyes.\n\n"
        "Her mother looked around at the village. Her face was pale. Then she saw Linh "
        "and her expression changed. The arrival she had avoided for thirty years was "
        "finally happening.\n\n"
        "They walked toward each other. Linh's mother opened her arms and pulled her "
        "into a tight embrace. Linh could feel her mother tremble. Neither of them "
        "spoke. They just held each other in the autumn sunlight."
    )

    passage_2 = (
        "They walked to Maple Cottage together. Linh's mother was quiet, looking at "
        "everything. She stopped at the corner shop, at the old church, at the bridge "
        "over the stream.\n\n"
        "\"I used to wander these streets every day after school,\" she said softly. "
        "\"I know every stone, every tree.\"\n\n"
        "When they reached the cottage, her mother stood at the gate for a long time. "
        "She looked at the house, the garden, the red chimney. Her eyes were wet.\n\n"
        "\"It looks the same,\" she whispered. \"I can recognise everything. The door, "
        "the windows, the path. It is like time stopped here.\"\n\n"
        "\"Some things have changed,\" Linh said gently. \"But the important things "
        "are unchanged. Come inside.\"\n\n"
        "Her mother walked through the front door and stopped in the hallway. She "
        "touched the wallpaper, the coat hooks, the small table by the door. Then she "
        "saw the photograph above the fireplace — Rose holding a baby.\n\n"
        "\"That is me,\" she said. \"That is me and my mother.\" And she began to cry."
    )

    passage_3 = (
        "The next morning, Linh and her mother went to the garden together. Linh had "
        "the notebook and the map. Three crosses remained — three more gifts to find.\n\n"
        "The fifth cross was near the old stone wall at the back of the garden. They "
        "took turns with the shovel. After twenty minutes, they found a glass jar, "
        "sealed with wax. Inside were dried flower petals — roses, lavender, and "
        "jasmine.\n\n"
        "\"Your grandmother used to dig up flowers and preserve them like this,\" her "
        "mother said, holding the jar up to the light. The petals were faded but still "
        "beautiful. \"She said flowers should last forever.\"\n\n"
        "The notebook said: \"These flowers are from three gardens — Eleanor's roses, "
        "Minh's jasmine from Vietnam, and my lavender. Three generations in one jar.\"\n\n"
        "Linh's mother held the jar against her chest. \"She kept everything,\" she "
        "whispered. \"She kept every memory alive.\""
    )

    passage_4 = (
        "The sixth gift was buried near the front gate. It was a small tin box "
        "containing a folded letter — not one of the unsent letters to Linh's mother, "
        "but something older. It was written by Eleanor to Minh, dated 1945.\n\n"
        "In the letter, Eleanor wrote about forgiveness. During the Second World War, "
        "some people in the village had been unkind to their family because of Minh's "
        "foreign background. Eleanor wrote: \"I have decided to forgive them. Carrying "
        "anger is a burden too heavy for my heart.\"\n\n"
        "She continued: \"I choose to release the pain. Our garden grows because we "
        "put love into the soil, not bitterness. I want our children to learn this — "
        "that forgiveness is not weakness. It is the strongest thing a person can do.\"\n\n"
        "Linh's mother read the letter twice. Then she looked at Linh. \"Your "
        "great-great-grandmother was very wise,\" she said. \"I wish I had learned "
        "this lesson thirty years ago.\""
    )

    passage_5 = (
        "They sat together in the garden as the sun began to set. The garden looked "
        "different now. The volunteers had cleared most of the weeds. New plants were "
        "growing. The paths were clean. The greenhouse had new glass panels.\n\n"
        "\"It is starting to transform,\" Linh's mother said, looking around. \"I can "
        "see what it used to be. And I can see what it could become.\"\n\n"
        "The rose bush by the greenhouse was covered in flowers now. Red, pink, and "
        "white roses in full blossom. The garden was coming back to life.\n\n"
        "\"This garden is about renewal,\" Linh said. \"Every generation plants "
        "something new. Every generation makes it grow.\"\n\n"
        "Her mother took her hand. \"You are right. And you have planted something "
        "too, Linh. You have planted us — back together, back in this garden, back "
        "in this house.\"\n\n"
        "Linh leaned against her mother's shoulder. One more gift remained in the "
        "garden. They would find it tomorrow. But tonight, sitting here together, "
        "they had already found the most important thing."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mẹ Linh đến Willowbrook lần đầu sau 30 năm. Hai mẹ con ôm nhau ở trạm xe "
        "buýt, rồi cùng bước vào ngôi nhà đầy ký ức. Mẹ cô khóc khi thấy bức ảnh "
        "trên lò sưởi. Họ cùng đào vườn và tìm thêm hai món quà — lọ hoa khô ba thế "
        "hệ và lá thư của cụ Eleanor về sự tha thứ. Khu vườn đang hồi sinh, và gia "
        "đình cũng vậy. Bạn sẽ ôn lại 15 từ vựng: arrival, embrace, tremble, wander, "
        "recognise, unchanged, dig, jar, preserve, forgiveness, burden, release, "
        "transform, bloom, renewal. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn "
        "truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ vựng và nghe "
        "lại cả chương."
    )

    description = (
        "Chương 9: Mẹ Linh về Willowbrook sau 30 năm. Hai mẹ con cùng đào vườn, tìm "
        "thêm hai món quà gia đình, và bắt đầu hàn gắn mối quan hệ. Luyện đọc 5 đoạn "
        "văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 9: Mẹ Về Nhà (Mother Comes Home)",
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
                "title": "Flashcards: Ôn tập Mẹ Về Nhà",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Mẹ Về Nhà.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
