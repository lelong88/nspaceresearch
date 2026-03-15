"""
Chapter 7: 去南方 (Đi Về Phía Nam) — Going South
Linh and Xiaoming travel south to find Mr. Zhao and learn more about the painting.
"""


def get_content():
    vocab_1 = ["远", "坐", "小时"]
    vocab_2 = ["大", "街", "多"]
    vocab_3 = ["问", "地址", "先"]
    vocab_4 = ["白", "头发", "老"]
    vocab_5 = ["进", "客厅", "请"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "阿玲和小明决定去南方找赵先生。小明的爷爷告诉他们，赵先生可能住在一个叫青山市的地方。青山市离小镇很远，坐火车要四个小时。星期天早上，他们很早就出发了。火车上人不多，阿玲看着窗外的风景，心里想着见到赵先生以后要问什么问题。"

    passage_2 = "四个小时以后，他们到了青山市。这是一个很大的城市，街上有很多人和车。和安静的小镇完全不一样。小明说：这么大的城市，我们怎么找到赵先生呢？阿玲说：我们可以先去问问当地的画家协会，也许他们知道赵先生住在哪里。他们在手机上查到了画家协会的地址。"

    passage_3 = "他们找到了画家协会的办公室。一个工作人员问他们：你们找谁？阿玲说：我们想找一个叫赵明远的画家，他大概二十年前来到这个城市。工作人员查了一下电脑，说：我们这里有一个赵明远的地址，但是不确定他现在还住不住在那里。你们可以先去看看。阿玲谢了他，拿到了地址。"

    passage_4 = "他们按照地址找到了一个老小区。楼很旧，但是很干净。他们找到了三楼的一个门，敲了敲。门开了，一个头发白了的老人站在门口。他看起来大概七十岁，穿着一件旧的白衬衫。老人看着他们问：你们找谁？阿玲说：请问您是赵明远先生吗？老人愣了一下，然后慢慢地点了点头。"

    passage_5 = "赵先生让他们进了屋子。客厅不大，但是墙上挂着很多画，都是山和日出的画。赵先生请他们坐下，给他们倒了水。阿玲说：赵先生，我们从北方的小镇来，想问您一些关于《山中日出》的事情。赵先生听到这个名字，眼睛里闪过一丝光。他沉默了一会儿，然后说：那幅画，是我一生中最好的作品。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Cuộc phiêu lưu mở rộng! Linh và Tiểu Minh quyết định đi về phía nam để tìm họa sĩ Triệu Minh Viễn. "
        "Sau bốn giờ đi tàu, họ đến thành phố Thanh Sơn — một thành phố lớn hoàn toàn khác với thị trấn nhỏ yên tĩnh. "
        "Qua hội họa sĩ địa phương, họ tìm được địa chỉ của ông Triệu. Khi gõ cửa một căn hộ cũ ở tầng ba, "
        "một ông lão tóc bạc mở cửa — chính là Triệu Minh Viễn. Phòng khách của ông treo đầy tranh núi và bình minh. "
        "Khi nghe nhắc đến bức 《山中日出》, ánh mắt ông sáng lên. "
        "Bạn sẽ ôn lại 15 từ vựng: 远, 坐, 小时, 大, 街, 多, 问, 地址, 先, "
        "白, 头发, 老, 进, 客厅, 请. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện "
        "và luyện nghe. Chương này mở ra một bước ngoặt quan trọng trong cuộc điều tra. "
        "Phần ôn tập cuối chương giúp bạn củng cố từ vựng và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 7 kể về hành trình của Linh và Tiểu Minh đi về phía nam tìm họa sĩ Triệu Minh Viễn. "
        "Họ tìm được ông và bắt đầu cuộc trò chuyện quan trọng về bức tranh. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 7: Đi Về Phía Nam (去南方)",
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
                "title": "Flashcards: Ôn tập Đi Về Phía Nam",
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
