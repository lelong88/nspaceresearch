"""
Chapter 8: Cuộc Gọi (The Phone Call)
Linh talks to her mother for the first time about England and the family history.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 8."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["nervous", "dial", "silence"]
    vocab_2 = ["apologise", "blame", "misunderstand"]
    vocab_3 = ["emotion", "tears", "relief"]
    vocab_4 = ["flight", "arrange", "suitcase"]
    vocab_5 = ["heal", "bridge", "reconnect"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Linh sat at the kitchen table the next morning with her phone in her hand. "
        "Her mother had replied to her message: \"Of course we can talk. Call me when "
        "you are ready.\"\n\n"
        "But Linh was nervous. She had never talked to her mother about England, about "
        "her grandmother, about any of this. It was a subject they had always avoided. "
        "Like a door that was always closed.\n\n"
        "She took a deep breath and pressed dial. The phone rang three times. Then her "
        "mother answered.\n\n"
        "\"Linh? Are you okay?\"\n\n"
        "\"I am fine, Mum. I just... I found some things in the house. Things I think "
        "you should know about.\"\n\n"
        "There was a long silence on the other end. Linh could hear her mother "
        "breathing. Finally, her mother said: \"Tell me.\"\n\n"
        "Linh began with the letters. She told her mother about the forty-seven "
        "envelopes in the desk drawer. She heard her mother's breath catch."
    )

    passage_2 = (
        "\"She wrote to me?\" her mother whispered. \"All those years?\"\n\n"
        "\"Every year, Mum. Sometimes two or three times a year. She wanted to "
        "apologise. She said she was wrong to say those things when you left.\"\n\n"
        "Her mother was quiet for a long time. When she spoke again, her voice was "
        "shaking. \"I was wrong too. I blamed her for everything. I told myself she "
        "did not love me. But that was not true, was it?\"\n\n"
        "\"No,\" Linh said softly. \"She loved you very much. She just did not know "
        "how to say it.\"\n\n"
        "\"We used to misunderstand each other,\" her mother said. \"For thirty years, we both "
        "thought the other person did not care. And all that time, she was writing "
        "letters she could not send, and I was missing her but too proud to call.\"\n\n"
        "Linh held the phone tightly. She could feel the weight of thirty years of "
        "silence between her mother and grandmother. Two stubborn women who loved each "
        "other but could not find the words."
    )

    passage_3 = (
        "Linh told her mother about the garden — the buried box, the photographs, the "
        "family notebook. She told her about Minh and Eleanor, about the compass and "
        "the locket.\n\n"
        "Her mother listened without speaking. Linh could hear the emotion in her "
        "breathing — small catches, long pauses. Then she heard something she had "
        "rarely heard before. Her mother was crying.\n\n"
        "\"Mum? Are you okay?\"\n\n"
        "\"These are happy tears, Linh. I did not know any of this. My mother never "
        "told me about Minh and Eleanor. She never told me about the garden gifts.\"\n\n"
        "\"I think she was saving it,\" Linh said. \"She wanted to tell you in person. "
        "She was waiting for you to come home.\"\n\n"
        "Her mother cried harder. Linh felt tears on her own face too. But they were "
        "tears of relief — the kind that come when something heavy is finally put down. "
        "The silence between them was breaking, like ice in spring."
    )

    passage_4 = (
        "They talked for two hours. Her mother told stories Linh had never heard — "
        "about growing up in Willowbrook, about playing in the garden, about her "
        "mother's cooking and her father's quiet laugh.\n\n"
        "\"I want to come,\" her mother said suddenly. \"I want to see the house. I "
        "want to see the garden. I want to read those letters.\"\n\n"
        "\"Really?\" Linh could not believe it.\n\n"
        "\"I will book a flight tomorrow. I can arrange things at work. It might take "
        "a week, but I will come.\"\n\n"
        "Linh's heart was racing. Her mother had not been to England in thirty years. "
        "And now she was coming. Because of the letters, because of the garden, because "
        "of a seventeen-year-old girl who had opened a drawer full of envelopes.\n\n"
        "\"Pack a warm suitcase,\" Linh said, laughing. \"It is cold here. And bring "
        "your gardening gloves. We have work to do.\"\n\n"
        "Her mother laughed too. It was the best sound Linh had heard in weeks."
    )

    passage_5 = (
        "After the call, Linh sat in the garden. The afternoon sun was warm. The rose "
        "bush near the greenhouse had two new flowers — red and bright against the "
        "green leaves.\n\n"
        "She thought about what had just happened. One phone call had started to heal "
        "thirty years of silence. It was not perfect. There was still pain, still "
        "questions, still things to work through. But the first step had been taken.\n\n"
        "The garden was like a bridge between past and present. Minh and Eleanor had "
        "started it. Rose had kept it alive. And now Linh was using it to reconnect "
        "her family.\n\n"
        "She looked at the map in the notebook. She had found four of the seven gifts. "
        "Three more were waiting. She decided to save them for when her mother arrived. "
        "They would find them together.\n\n"
        "Linh closed the notebook and smiled. The garden was not finished. The story "
        "was not finished. But for the first time, she felt like everything was going "
        "to be okay."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh gọi điện cho mẹ và kể về những lá thư, khu vườn, và lịch sử gia đình. "
        "Lần đầu tiên sau 30 năm im lặng, mẹ cô khóc khi biết bà ngoại đã viết thư "
        "suốt bao năm. Hai mẹ con nói chuyện hai tiếng — chia sẻ ký ức, nước mắt, và "
        "tiếng cười. Mẹ Linh quyết định bay sang Anh lần đầu sau 30 năm. Linh quyết "
        "để dành 3 món quà còn lại để cùng mẹ tìm. Bạn sẽ ôn lại 15 từ vựng: nervous, "
        "dial, silence, apologise, blame, misunderstand, emotion, tears, relief, flight, "
        "arrange, suitcase, heal, bridge, reconnect. Mỗi buổi học gồm thẻ từ vựng "
        "nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn "
        "bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 8: Linh gọi điện cho mẹ, chia sẻ về những lá thư và khu vườn. Mẹ cô "
        "quyết định bay sang Anh lần đầu sau 30 năm. Sự im lặng bắt đầu tan vỡ. "
        "Luyện đọc 5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 8: Cuộc Gọi (The Phone Call)",
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
                "title": "Flashcards: Ôn tập Cuộc Gọi",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Cuộc Gọi.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
