"""
Chapter 2: Những Lá Thư (The Letters)
Linh reads the first letters and learns about her grandmother's life and regrets.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 2."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["seal", "unfold", "ink"]
    vocab_2 = ["regret", "argument", "forgive"]
    vocab_3 = ["recipe", "memory", "childhood"]
    vocab_4 = ["lonely", "neighbour", "comfort"]
    vocab_5 = ["courage", "truth", "secret"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "The next morning, Linh sat at the kitchen table with the letters in front of "
        "her. There were forty-seven envelopes in total. She had counted them twice. "
        "All sealed. All addressed to her mother in Melbourne.\n\n"
        "She picked up the oldest one. The date on the back said March 1996. That was "
        "the year her mother left England. Linh carefully broke the seal and took out "
        "the letter inside.\n\n"
        "The paper was thin and soft. She unfolded it slowly. The writing was in blue "
        "ink, small and neat. It began: \"My dearest daughter, I am writing this letter "
        "because I cannot say these words to your face.\"\n\n"
        "Linh's hands were shaking. She felt like she was opening a door into a world "
        "she had never known. She made a cup of tea to calm herself, then sat back "
        "down. She took a deep breath and continued reading."
    )

    passage_2 = (
        "The first letter was about the day Linh's mother left. Her grandmother wrote "
        "about a terrible argument they had. They shouted at each other in the kitchen. "
        "Her mother wanted to move to Australia with Linh's father. Her grandmother "
        "wanted her to stay.\n\n"
        "\"I said things I did not mean,\" the letter said. \"I told you that if you "
        "left, you should never come back. I have carried the regret of those words "
        "every day since. They sit in my chest like stones.\"\n\n"
        "The letter ended with: \"I hope one day you can forgive me. I was afraid of "
        "losing you, and my fear made me cruel. I am sorry.\"\n\n"
        "Linh put the letter down. She understood now why her mother never talked about "
        "England. There was pain here — old pain that had never healed. She sat quietly "
        "for a moment, then picked up the next envelope."
    )

    passage_3 = (
        "The second letter was from December 1996. It was warmer, softer. Her "
        "grandmother wrote about Christmas in Willowbrook. She described the village "
        "market, the carol singers, and the snow on the hills.\n\n"
        "\"I made your favourite recipe today — the apple cake with cinnamon. I made "
        "it for myself, but I kept thinking of you sitting at this table, eating it "
        "with cream on top.\"\n\n"
        "She wrote about a memory from Linh's mother's childhood. How she used to run "
        "through the garden in summer, picking flowers and bringing them inside in big "
        "messy bunches. \"The house always smelled like roses when you were here.\"\n\n"
        "Linh smiled. She could almost see it — a little girl running through the "
        "garden that was now wild and overgrown. These letters were like windows into "
        "a life she had never known."
    )

    passage_4 = (
        "Linh read five more letters that morning. Each one told a small story. Her "
        "grandmother wrote about the seasons changing, about the garden, about the "
        "people in the village. But under every story, there was sadness.\n\n"
        "In one letter, she wrote: \"I am lonely today. The house is too quiet. Mrs. "
        "Patterson next door brought me soup, but it is not the same as having family "
        "here.\"\n\n"
        "Her neighbour Mrs. Patterson appeared in many letters. She seemed to be her "
        "grandmother's closest friend. She brought food, helped in the garden, and "
        "sat with her on cold evenings.\n\n"
        "\"Margaret is a great comfort to me,\" her grandmother wrote. \"But she is "
        "not you. Nobody can replace a daughter.\"\n\n"
        "Linh felt tears in her eyes. Her grandmother had spent thirty years missing "
        "her daughter. And her mother had spent thirty years not knowing."
    )

    passage_5 = (
        "The last letter Linh read that day was different from the others. It was "
        "written in 2020, just four years ago. The handwriting was less steady, but "
        "the words were clear.\n\n"
        "\"I have been thinking about courage,\" her grandmother wrote. \"It takes "
        "courage to say sorry. It takes courage to tell the truth. I have written "
        "you forty-six letters and I have not had the courage to post a single one.\"\n\n"
        "\"There is something I need to tell you. A secret I have kept for too long. "
        "It is about the garden — about what I buried there, and why. But I am afraid "
        "that if I tell you, you will be angry again.\"\n\n"
        "The letter stopped there. It was not finished. There was no signature, no "
        "\"with love.\" Just those words about a secret in the garden.\n\n"
        "Linh looked out the window at the wild garden below. What had her grandmother "
        "buried there? And why was she so afraid to tell?"
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Linh bắt đầu đọc 47 lá thư bà ngoại viết cho mẹ cô suốt 30 năm nhưng chưa "
        "bao giờ gửi đi. Từ lá thư đầu tiên về cuộc cãi vã đau lòng ngày mẹ cô rời "
        "nước Anh, đến những ký ức ấm áp về Giáng sinh và khu vườn hoa hồng, mỗi lá "
        "thư mở ra một mảnh ghép của quá khứ. Nhưng lá thư cuối cùng tiết lộ điều bất "
        "ngờ — bà ngoại giấu một bí mật trong khu vườn. Bạn sẽ ôn lại 15 từ vựng quen "
        "thuộc: seal, unfold, ink, regret, argument, forgive, recipe, memory, childhood, "
        "lonely, neighbour, comfort, courage, truth, secret. Mỗi buổi học gồm thẻ từ "
        "vựng nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn "
        "toàn bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 2: Linh đọc những lá thư bà ngoại viết cho mẹ cô suốt 30 năm — từ "
        "nỗi hối hận về cuộc cãi vã đến những ký ức tuổi thơ ấm áp, và một bí mật "
        "được chôn giấu trong khu vườn. Luyện đọc 5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 2: Những Lá Thư (The Letters)",
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
                "title": "Flashcards: Ôn tập Những Lá Thư",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Những Lá Thư.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
