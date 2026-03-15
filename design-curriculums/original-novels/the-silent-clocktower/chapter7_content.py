"""
Chapter 7: Hồ Sơ Cũ (The Old Records)
Final investigation leads before climax — Mai researches the Hargrove family and confronts Mr. Graves.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 7."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["library", "research", "article"]
    vocab_2 = ["wealthy", "build", "generation"]
    vocab_3 = ["transfer", "legal", "claim"]
    vocab_4 = ["confront", "demand", "refuse"]
    vocab_5 = ["threaten", "silence", "truth"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "The next morning, Mai walked to the Eldermere library. It was a small "
        "building at the end of the high street, with tall windows and a green door. "
        "Inside, it smelled like old paper and wood.\n\n"
        "An elderly woman sat behind the front desk. She looked up and smiled. "
        "\"Can I help you?\"\n\n"
        "\"I am doing some research on the history of the town,\" Mai said. \"I am "
        "looking for information about a family called Hargrove.\"\n\n"
        "The woman thought for a moment. \"Hargrove. That is a name I have not heard "
        "in a long time. You should look in the local history section. We also have "
        "old newspapers on the shelves at the back.\"\n\n"
        "Mai thanked her and went to the back of the library. There were rows of "
        "large books and folders full of old newspaper pages. She found a shelf "
        "marked \"Eldermere Herald — 1880 to 1970.\" She pulled out the first folder "
        "and began to read. An article from 1890 caught her eye immediately. The "
        "headline said: \"Hargrove Family Builds Clocktower for Eldermere.\""
    )

    passage_2 = (
        "Mai read the article carefully. The Hargrove family had been one of the most "
        "wealthy families in the area. They owned land, farms, and several buildings "
        "in Eldermere. In 1890, the head of the family, Mr. George Hargrove, decided "
        "to build a clocktower in the centre of town.\n\n"
        "The article said the tower was a gift to the people of Eldermere, but it "
        "remained private property of the Hargrove family. George Hargrove wanted "
        "the town to enjoy the clock, but the land and the building belonged to his "
        "family.\n\n"
        "Mai found more articles from later years. The Hargroves lived in a large "
        "house on the hill above the town. Generation after generation, they took "
        "care of the tower and paid for repairs. But the family became smaller over "
        "time. Children moved away to London or abroad.\n\n"
        "The last article about the family was from 1960. It was short and sad. "
        "\"Eleanor Hargrove, the last of the Hargrove family in Eldermere, died "
        "yesterday at the age of eighty-two. She had no children.\""
    )

    passage_3 = (
        "Mai kept reading. After Eleanor died, the town council held a meeting. They "
        "said the clocktower was abandoned property because no one from the Hargrove "
        "family came to claim it. The council voted to take control of the tower and "
        "the land around it.\n\n"
        "But Mai now knew something important. The deed she had found in the hidden "
        "compartment showed that the tower was never given to the town. There was no "
        "legal transfer of ownership. The council simply took it because nobody "
        "stopped them.\n\n"
        "She wrote in her notebook: \"1960 — Eleanor dies. No legal transfer. Council "
        "takes tower. Deed stays hidden.\"\n\n"
        "Mai thought about Mr. Whitfield, the old clockmaker. He had worked in the "
        "tower for forty years. He must have found the deed inside the wall. And "
        "when he found it, someone wanted him to be quiet. Maybe that was why he "
        "disappeared.\n\n"
        "She closed the folder and sat back in her chair. She needed to find out "
        "who on the town council had the most to lose if the truth came out."
    )

    passage_4 = (
        "Mai went back to the front desk. \"Can you tell me who is the head of the "
        "town council?\" she asked.\n\n"
        "\"That would be Mr. Graves,\" the woman said. \"He has been on the council "
        "for over twenty years. His office is on Market Street, next to the bank.\"\n\n"
        "Mai walked to Market Street and found the office. She did not wait. She "
        "went inside and asked to see Mr. Graves. A young man at the front desk "
        "looked surprised, but he led her to a small room at the back.\n\n"
        "Mr. Graves was a tall man with thin grey hair and cold eyes. He did not "
        "stand up when Mai came in.\n\n"
        "\"I want to ask about the clocktower,\" Mai said. She decided to confront "
        "him directly. \"I found a deed from 1890. The tower is private property. "
        "It was never given to the town.\"\n\n"
        "Mr. Graves did not move. \"I do not know what you are talking about.\"\n\n"
        "\"I demand an honest answer,\" Mai said. \"The council took the tower "
        "without any right. You know this.\"\n\n"
        "Mr. Graves looked at her for a long moment. Then he said, \"I refuse to "
        "discuss this. Please leave my office.\""
    )

    passage_5 = (
        "Mai did not leave immediately. She stood her ground. \"I also know that you "
        "bought your house from the Hargrove estate,\" she said. \"You knew about "
        "the family. You knew about the deed.\"\n\n"
        "Mr. Graves stood up slowly. His face was red. \"You are a visitor here,\" "
        "he said in a low voice. \"You do not understand how things work in this "
        "town. I am telling you to stop asking questions. If you do not stop, there "
        "will be problems for you.\"\n\n"
        "Mai felt a chill. He was trying to threaten her. But she did not look away. "
        "\"You cannot silence everyone,\" she said quietly. \"Mr. Whitfield found "
        "the truth, and I think that is why he is gone.\"\n\n"
        "Mr. Graves pointed at the door. Mai turned and walked out. Her hands were "
        "shaking, but her mind was clear. Graves knew about the deed. He wanted it "
        "to stay hidden because the tower sat on valuable land. If the truth came "
        "out, the council would lose everything.\n\n"
        "She walked back toward the square. She needed to talk to David. They were "
        "getting closer to the answer — and closer to danger."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai đến thư viện Eldermere để tìm hiểu về gia đình Hargrove — những người "
        "đã xây tháp đồng hồ vào năm 1890. Qua những bài báo cũ, cô phát hiện gia "
        "đình Hargrove từng rất giàu có và sở hữu tháp đồng hồ như tài sản riêng. "
        "Người cuối cùng của dòng họ, Eleanor, qua đời năm 1960 mà không có con. Hội "
        "đồng thị trấn đã chiếm quyền kiểm soát tháp mà không có giấy tờ chuyển "
        "nhượng hợp pháp. Mai đối mặt với ông Graves, chủ tịch hội đồng, nhưng ông "
        "ta từ chối trả lời và đe dọa cô. Bạn sẽ ôn lại 15 từ vựng quen thuộc: "
        "library, research, article, wealthy, build, generation, transfer, legal, "
        "claim, confront, demand, refuse, threaten, silence, truth. Mỗi buổi học gồm "
        "thẻ từ vựng nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 "
        "tổng ôn toàn bộ từ vựng và nghe lại cả chương — giúp bạn đọc trôi chảy và "
        "tự tin hơn với tiếng Anh."
    )

    description = (
        "Chương 7 đưa Mai đến thư viện để nghiên cứu lịch sử gia đình Hargrove và "
        "phát hiện hội đồng thị trấn đã chiếm tháp đồng hồ bất hợp pháp. Khi đối "
        "mặt với ông Graves, cô bị đe dọa nhưng càng tin rằng sự thật đang bị che "
        "giấu. Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 7: Hồ Sơ Cũ (The Old Records)",
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
                "title": "Flashcards: Ôn tập Hồ Sơ Cũ",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Hồ Sơ Cũ.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
