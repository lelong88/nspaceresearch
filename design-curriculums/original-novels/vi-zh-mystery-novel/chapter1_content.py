"""
Chapter 1: 新的开始 (Khởi Đầu Mới) — A New Beginning
Linh arrives in a small Chinese town for a summer art program and visits the town gallery.
"""


def get_content():
    # Vocabulary: 15 HSK2-3 words, 3 per passage
    vocab_1 = ["学校", "火车", "到"]
    vocab_2 = ["小", "房间", "漂亮"]
    vocab_3 = ["画", "老师", "有名"]
    vocab_4 = ["朋友", "一起", "高兴"]
    vocab_5 = ["晚上", "安静", "开始"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "阿玲是一个越南女孩，她在中国的一所学校学习画画。今年夏天，她坐火车去了一个小镇。火车走了很长时间，但是阿玲不觉得累。她看着窗外的山和树，心里很开心。火车到了小镇的车站，阿玲拿着行李走了出来。车站很小，但是很干净。她看了看手机上的地图，准备去学校。"

    passage_2 = "小镇不大，街道很安静。阿玲走了十分钟，就看到了学校。学校旁边有一个小旅馆，她的房间在二楼。房间虽然小，但是很干净。窗户外面可以看到一条小河和几棵大树。阿玲觉得这个地方很漂亮，她很喜欢。她把行李放好，洗了脸，准备出去看看小镇。"

    passage_3 = "阿玲走到小镇的中心，看到了一个很大的画廊。画廊里面有很多画，都是有名的画家画的。一位王老师在画廊门口欢迎大家。王老师说这个画廊已经有五十年了，里面最有名的一幅画叫《山中日出》。阿玲看了那幅画，觉得非常美。她想，这个夏天一定会学到很多东西。"

    passage_4 = "在画廊里，阿玲认识了一个叫小明的男孩。小明是本地人，也喜欢画画。他们一起看了画廊里的画，聊了很多。小明告诉阿玲，这个小镇虽然小，但是有很多有意思的地方。阿玲很高兴认识了小明，因为在这里她还没有朋友。小明说明天可以带她去看看小镇的其他地方。"

    passage_5 = "晚上，阿玲回到旅馆。小镇的晚上很安静，没有大城市的声音。她坐在窗户旁边，看着外面的星星。她在本子上写道：今天是我在小镇的第一天，我看到了美丽的画廊和有名的画，还认识了新朋友。明天开始上课，我很期待。阿玲关了灯，很快就睡着了。新的生活开始了。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Chào mừng bạn đến với câu chuyện bí ẩn hấp dẫn về một bức tranh biến mất! "
        "Trong chương mở đầu này, bạn sẽ theo chân Linh — một cô gái Việt Nam đến một thị trấn nhỏ ở Trung Quốc "
        "để học vẽ trong chương trình nghệ thuật mùa hè. Linh đi tàu hỏa đến thị trấn, khám phá phòng trọ nhỏ xinh, "
        "và ghé thăm phòng tranh nổi tiếng của thị trấn. Tại đây, cô gặp thầy Vương và kết bạn với Tiểu Minh — "
        "một chàng trai địa phương cũng yêu thích hội họa. Bạn sẽ ôn lại 15 từ vựng quen thuộc: "
        "学校, 火车, 到, 小, 房间, 漂亮, 画, 老师, 有名, 朋友, 一起, 高兴, 晚上, 安静, 开始. "
        "Mỗi phần học gồm thẻ từ vựng nhanh, đọc một đoạn truyện hấp dẫn bằng tiếng Trung, và luyện nghe theo. "
        "Qua năm đoạn văn ngắn, bạn sẽ cảm nhận được không khí yên bình của thị trấn nhỏ và sự háo hức "
        "của Linh khi bắt đầu cuộc sống mới. Phần ôn tập cuối cùng giúp bạn củng cố toàn bộ từ vựng "
        "và nghe lại cả chương để đọc trôi chảy hơn."
    )

    description = (
        "Chương 1 giới thiệu Linh đến thị trấn nhỏ ở Trung Quốc, nơi cô khám phá phòng tranh nổi tiếng "
        "và kết bạn mới. Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc, "
        "rèn kỹ năng đọc hiểu qua ngữ cảnh tự nhiên của câu chuyện."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 1: Khởi Đầu Mới (新的开始)",
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
                "title": "Flashcards: Ôn tập Khởi Đầu Mới",
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
