"""
Chapter 10: 美丽的夏天 (Mùa Hè Tươi Đẹp) — A Beautiful Summer
The mystery is resolved. The painting returns to the gallery. Linh finishes her summer with new friendships.
"""


def get_content():
    vocab_1 = ["今天", "特别", "开"]
    vocab_2 = ["名字", "写", "旁边"]
    vocab_3 = ["拍照", "笑", "快乐"]
    vocab_4 = ["夏天", "学", "经验"]
    vocab_5 = ["再见", "记住", "永远"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "画回到画廊的那天，整个小镇都很开心。王老师决定今天举办一个特别的活动，邀请大家来画廊看画。画廊的门一早就开了，很多人来了。大家都想看看那幅失而复得的《山中日出》。阿玲站在人群中，看着大家开心的样子，她也觉得很满足。这个夏天发生了很多事情。"

    passage_2 = "王老师在画的旁边挂了一个小牌子，上面写着：画家赵明远。赵先生看到自己的名字写在那里，眼睛湿了。他对王老师说：谢谢你。王老师握着他的手说：这幅画本来就应该有你的名字。二十年的误会，今天终于解开了。阿玲在旁边看着，觉得这是她见过的最美的画面。"

    passage_3 = "活动结束以后，大家一起在画廊门口拍照。赵先生站在中间，旁边是王老师和阿玲。大家都在笑，连张叔叔也笑了。李阿姨从咖啡店端来了蛋糕和咖啡，大家一起吃。小明对阿玲说：多亏了你，这件事才能解决。阿玲说：不是我一个人，是大家一起的。这是一个快乐的下午。"

    passage_4 = "夏天快要结束了。阿玲在小镇学到了很多东西，不只是画画。她学会了观察，学会了倾听，也学会了理解别人。这次的经验让她成长了很多。王老师对她说：你是一个很特别的学生。你不只会画画，你还会用心去看这个世界。阿玲听了，心里很感动。"

    passage_5 = "离开小镇的那天早上，小明和李阿姨来车站送阿玲。阿玲对他们说再见，眼泪差点掉下来。小明说：你要记住这个小镇，以后一定要回来。阿玲笑着说：我永远不会忘记这里的。火车慢慢开动了，阿玲看着窗外越来越远的小镇。她知道，这个夏天的故事，她会永远记住。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Câu chuyện kết thúc tốt đẹp! Bức tranh 《山中日出》 trở về phòng tranh và thầy Vương tổ chức "
        "một buổi lễ đặc biệt. Tên họa sĩ Triệu Minh Viễn được ghi bên cạnh bức tranh — hai mươi năm "
        "hiểu lầm cuối cùng được giải tỏa. Mọi người cùng chụp ảnh, cười vui và ăn mừng. "
        "Mùa hè sắp kết thúc, Linh nhận ra cô đã học được nhiều hơn chỉ là vẽ tranh — cô học cách quan sát, "
        "lắng nghe và thấu hiểu. Khi rời thị trấn, Linh hứa sẽ mãi nhớ nơi này. "
        "Bạn sẽ ôn lại 15 từ vựng: 今天, 特别, 开, 名字, 写, 旁边, 拍照, 笑, 快乐, "
        "夏天, 学, 经验, 再见, 记住, 永远. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện "
        "và luyện nghe. Chương cuối cùng này mang đến kết thúc ấm áp và ý nghĩa cho toàn bộ câu chuyện. "
        "Phần ôn tập cuối chương giúp bạn củng cố từ vựng và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 10 — chương cuối cùng — kể về ngày bức tranh trở về phòng tranh và buổi lễ ăn mừng. "
        "Linh chia tay thị trấn với những kỷ niệm đẹp và tình bạn mới. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 10: Mùa Hè Tươi Đẹp (美丽的夏天)",
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
                "title": "Flashcards: Ôn tập Mùa Hè Tươi Đẹp",
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
