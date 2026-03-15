"""
Chapter 6: 爷爷的故事 (Câu Chuyện Của Ông Nội) — Grandfather's Story
Xiaoming's grandfather reveals the history of the painting and the mysterious Mr. Zhao.
"""


def get_content():
    vocab_1 = ["爷爷", "家", "坐"]
    vocab_2 = ["故事", "年轻", "喜欢"]
    vocab_3 = ["离开", "城市", "生气"]
    vocab_4 = ["孩子", "长大", "回来"]
    vocab_5 = ["现在", "地方", "住"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "第二天，阿玲和小明去了小明爷爷的家。爷爷住在镇子东边的一个小房子里。爷爷今年八十岁了，但是身体还很好。他们坐在院子里，爷爷给他们倒了茶。阿玲把那张旧照片拿出来给爷爷看。爷爷戴上眼镜，仔细看了看照片，然后慢慢地说：这个人，我认识。"

    passage_2 = "爷爷开始讲一个故事。他说：照片上的人叫赵明远。他年轻的时候是一个很有才华的画家，也是画廊的第一个老师。他非常喜欢画画，特别喜欢画山和日出。那幅《山中日出》就是他画的。阿玲和小明听了都很吃惊。原来那幅有名的画是赵先生画的！"

    passage_3 = "爷爷继续说：但是后来，赵明远和画廊的主人吵了一架。画廊的主人说那幅画是画廊的，赵明远说那是他自己的画。他们非常生气，最后赵明远离开了小镇，去了南方的一个大城市。从那以后，他再也没有回来过。阿玲问：那是多少年前的事？爷爷说：大概二十年了。"

    passage_4 = "阿玲又问：赵先生有没有家人在这里？爷爷想了想说：他走的时候还没有结婚。但是听说他后来在城市里结了婚，有了一个孩子。那个孩子现在应该长大了。也许赵明远想回来拿那幅画，所以让人来把画拿走了。阿玲觉得这个想法很有道理。"

    passage_5 = "离开爷爷家以后，阿玲对小明说：我们现在知道了很多新的信息。赵先生画了那幅画，他觉得画是他的，他离开了这个地方去了南方。如果他想拿回自己的画，他可能会派人来。那个穿黑衣服的男人会不会就是赵先生派来的人？小明说：有可能。但是赵先生现在住在哪里呢？我们怎么找到他？"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Bí mật về bức tranh dần được hé lộ! Linh và Tiểu Minh đến nhà ông nội của Tiểu Minh "
        "để hỏi về tấm ảnh cũ. Ông nội kể một câu chuyện đáng kinh ngạc: người trong ảnh là Triệu Minh Viễn — "
        "một họa sĩ tài năng, chính là người đã vẽ bức tranh nổi tiếng 《山中日出》. Hai mươi năm trước, "
        "ông Triệu và chủ phòng tranh cãi nhau về quyền sở hữu bức tranh, và ông Triệu đã rời thị trấn "
        "đi về phía nam. Linh bắt đầu nghi ngờ rằng ông Triệu có thể đã cử người đến lấy lại bức tranh. "
        "Bạn sẽ ôn lại 15 từ vựng: 爷爷, 家, 坐, 故事, 年轻, 喜欢, 离开, 城市, 生气, "
        "孩子, 长大, 回来, 现在, 地方, 住. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện "
        "và luyện nghe. Câu chuyện ngày càng rõ ràng khi quá khứ của bức tranh được tiết lộ. "
        "Phần ôn tập cuối chương giúp bạn củng cố từ vựng và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 6 tiết lộ lịch sử của bức tranh qua lời kể của ông nội Tiểu Minh. "
        "Linh biết được họa sĩ Triệu Minh Viễn chính là người vẽ bức tranh và đã rời thị trấn vì tranh chấp. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 6: Câu Chuyện Của Ông Nội (爷爷的故事)",
        "language": "zh",
        "userLanguage": "vi",
        "level": "preintermediate",
        "audioSpeed": -0.2,
        "preview": {"text": preview_text},
        "description": description,
        "learningSessions": []
    }

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

    review_session = {
        "title": "Ôn tập",
        "activities": [
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập Câu Chuyện Của Ông Nội",
                "description": f"Ôn lại toàn bộ 15 từ vựng trong chương: {', '.join(all_vocab)}",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
