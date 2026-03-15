"""
Chapter 5: 地下室 (Tầng Hầm) — The Basement
Linh and Xiaoming discover a hidden basement under the gallery with old paintings.
"""


def get_content():
    vocab_1 = ["下面", "黑", "手机"]
    vocab_2 = ["旧", "放", "东西"]
    vocab_3 = ["照片", "年", "记得"]
    vocab_4 = ["快", "跑", "上面"]
    vocab_5 = ["回去", "应该", "明天"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "星期六，画廊没有课。阿玲和小明决定再去画廊看看。他们走到画廊后面，发现地上有一个旧的木门。小明说：这个门通向画廊的下面，是一个地下室。他们打开门，里面很黑，什么都看不见。阿玲拿出手机，打开了手机上的灯。一条很窄的楼梯出现在他们面前。"

    passage_2 = "他们小心地走下楼梯。地下室不大，但是里面放着很多旧的东西：旧桌子、旧椅子，还有几个大箱子。阿玲打开一个箱子，里面是一些旧的画。这些画看起来很老了，颜色已经不太清楚了。小明说：这些可能是画廊以前的画，放在这里很多年了。阿玲仔细看了看每一幅画。"

    passage_3 = "在一个箱子的最下面，阿玲找到了一张旧照片。照片上是一个年轻的男人，站在画廊门口，手里拿着一幅画。照片后面写着一个名字和一个年份：赵先生，二十年前。小明看了照片说：我不记得这个人，但是我可以问问我爷爷，他在这个镇上住了一辈子，应该认识很多人。"

    passage_4 = "突然，他们听到上面有脚步声。有人来了！阿玲和小明互相看了一眼，心跳得很快。脚步声越来越近，好像在往地下室的方向走。小明小声说：我们快走！他们赶紧跑上楼梯，从后门出去了。他们跑到街上，回头看了看，没有人跟出来。阿玲的心还在跳得很快。"

    passage_5 = "阿玲和小明坐在公园的椅子上休息。小明说：刚才好危险！我们赶快回去吧。阿玲说：是啊，但是我们发现了很重要的东西。那张照片上的赵先生是谁？他和画廊有什么关系？阿玲觉得他们应该去问问小明的爷爷。小明说：好，我们明天去我爷爷家。阿玲把照片小心地放进口袋，她觉得答案越来越近了。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Một khám phá bất ngờ! Linh và Tiểu Minh tìm thấy một tầng hầm bí mật dưới phòng tranh. "
        "Bên trong tối om, chứa đầy đồ cũ và những bức tranh cổ. Đặc biệt, họ phát hiện một tấm ảnh cũ "
        "chụp một người đàn ông tên Triệu đứng trước phòng tranh hai mươi năm trước. Người này là ai? "
        "Có liên quan gì đến vụ mất tranh không? Đúng lúc đó, có tiếng bước chân từ phía trên — "
        "ai đó đang đến! Hai người phải chạy thoát ra ngoài. "
        "Bạn sẽ ôn lại 15 từ vựng: 下面, 黑, 手机, 旧, 放, 东西, 照片, 年, 记得, "
        "快, 跑, 上面, 回去, 应该, 明天. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện phiêu lưu "
        "và luyện nghe. Chương này đầy kịch tính khi Linh và Tiểu Minh khám phá bí mật "
        "ẩn giấu dưới phòng tranh. Phần ôn tập cuối chương giúp bạn củng cố từ vựng "
        "và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 5 kể về việc Linh và Tiểu Minh khám phá tầng hầm bí mật dưới phòng tranh, "
        "tìm thấy tấm ảnh cũ bí ẩn và phải chạy trốn khi có người đến. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 5: Tầng Hầm (地下室)",
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
                "title": "Flashcards: Ôn tập Tầng Hầm",
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
