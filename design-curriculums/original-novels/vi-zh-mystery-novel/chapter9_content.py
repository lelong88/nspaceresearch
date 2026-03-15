"""
Chapter 9: 回到小镇 (Trở Về Thị Trấn) — Return to the Town
Mr. Zhao returns to the town with the painting and confesses to the police.
"""


def get_content():
    vocab_1 = ["带", "早", "准备"]
    vocab_2 = ["站", "等", "紧张"]
    vocab_3 = ["解释", "原来", "因为"]
    vocab_4 = ["哭", "眼泪", "感动"]
    vocab_5 = ["同意", "决定", "新"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "三天以后，赵先生带着那幅画来到了小镇。阿玲和小明一早就在车站等他。赵先生从火车上下来的时候，手里小心地抱着一个大包裹。他看起来很累，但是眼睛里有一种坚定的光。阿玲帮他拿行李，小明带路。他们准备先去画廊，把画还给王老师。"

    passage_2 = "他们走到画廊门口。王老师和两个警察已经站在那里等他们了，因为阿玲提前打了电话告诉他们。张叔叔也在，他站在旁边，看起来很紧张。赵先生走上前，把包裹打开，那幅美丽的《山中日出》出现在大家面前。所有人都看着那幅画，画廊门口一下子变得很安静。"

    passage_3 = "赵先生开始向大家解释。他说：这幅画是我二十年前画的。我一直觉得它是我的。我的儿子知道这件事以后，就来把画拿走了。原来张叔叔认识我儿子，因为我儿子以前来过小镇找我的老朋友。张叔叔帮他打开了画廊的后门。我知道他们做错了，所以我亲自把画带回来了。"

    passage_4 = "王老师听完以后，眼睛红了，忍不住哭了。他说：赵老师，我记得你。你是画廊最好的老师。这幅画确实是你画的，但是你把它留给了画廊。赵先生的眼泪流了下来。他说：是的，当时我太生气了，说了很多不好的话。现在我老了，我明白了，画放在画廊里，大家都能看到，这才是最好的。很多人都被感动了。"

    passage_5 = "警察说：虽然拿画的方式不对，但是赵先生主动把画送回来了，我们会考虑这一点。张叔叔低着头说对不起。王老师想了想，做了一个决定：他同意在画的旁边加一个牌子，写上画家赵明远的名字。赵先生听了，笑了。阿玲看着这一切，心里觉得很温暖。一个新的开始，对每个人来说都是好的。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Khoảnh khắc đầy cảm xúc! Ông Triệu mang bức tranh trở về thị trấn. Tại phòng tranh, trước mặt thầy Vương, "
        "cảnh sát và bác bảo vệ Trương, ông giải thích toàn bộ sự việc. Hóa ra bác Trương quen con trai ông Triệu "
        "và đã giúp mở cửa sau phòng tranh. Ông Triệu xin lỗi và trả lại bức tranh. Thầy Vương xúc động và quyết định "
        "gắn tên họa sĩ Triệu Minh Viễn bên cạnh bức tranh. Mọi người đều cảm động trước kết cục đẹp này. "
        "Bạn sẽ ôn lại 15 từ vựng: 带, 早, 准备, 站, 等, 紧张, 解释, 原来, 因为, "
        "哭, 眼泪, 感动, 同意, 决定, 新. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện "
        "và luyện nghe. Chương này là cao trào cảm xúc của câu chuyện khi sự thật được phơi bày "
        "và mọi người tìm được sự hòa giải. Phần ôn tập cuối chương giúp bạn củng cố từ vựng "
        "và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 9 kể về việc ông Triệu trở về thị trấn trả lại bức tranh và giải thích mọi chuyện. "
        "Thầy Vương quyết định ghi tên họa sĩ bên cạnh bức tranh. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 9: Trở Về Thị Trấn (回到小镇)",
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
                "title": "Flashcards: Ôn tập Trở Về Thị Trấn",
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
