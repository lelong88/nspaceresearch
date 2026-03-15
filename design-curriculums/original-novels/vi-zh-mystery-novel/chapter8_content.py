"""
Chapter 8: 真相 (Sự Thật) — The Truth
Mr. Zhao reveals the truth: his son took the painting back, believing it belonged to his father.
"""


def get_content():
    vocab_1 = ["儿子", "大学", "毕业"]
    vocab_2 = ["错", "对不起", "难过"]
    vocab_3 = ["电话", "已经", "送"]
    vocab_4 = ["明白", "办法", "最后"]
    vocab_5 = ["希望", "一定", "谢谢"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "赵先生开始讲他的故事。他说：我离开小镇以后，在这里生活了二十年。我结了婚，有了一个儿子。儿子叫赵小飞，今年刚从大学毕业。他学的是艺术，和我一样喜欢画画。我经常给他讲小镇的故事，讲那幅《山中日出》。他知道那幅画是我画的，也知道我一直很想念它。"

    passage_2 = "赵先生的眼睛红了。他说：小飞觉得画廊拿了我的画是错的。他很生气，想帮我把画拿回来。我不知道他的计划。上个星期，他突然带着那幅画回来了。我看到画的时候，又高兴又难过。我对他说：你做错了，这样不对。对不起，我没有教好他。赵先生说完，低下了头。"

    passage_3 = "阿玲问：画现在在哪里？赵先生站起来，走进里面的房间，拿出了那幅《山中日出》。画和阿玲在画廊看到的一模一样，非常美丽。赵先生说：小飞已经知道自己做错了。我打了电话给他，让他回来。我想把画送回去，但是我不知道怎么做。我老了，不能自己去那么远的地方。"

    passage_4 = "阿玲明白了整件事情。赵先生的儿子因为爱父亲，所以偷了画。张叔叔可能帮了忙，因为他需要钱。阿玲对赵先生说：我有一个办法。我们可以一起把画送回画廊，然后跟王老师和警察说清楚。赵先生想了很久，最后点了点头说：好，这是最好的办法。我应该亲自去道歉。"

    passage_5 = "离开赵先生家的时候，阿玲心里有很多感受。她觉得赵先生不是坏人，他的儿子也不是。他们只是太想要回自己的东西了。阿玲对赵先生说：我希望一切都会好起来的。赵先生说：谢谢你们来找我。我一定会把画送回去的。阿玲和小明坐上了回小镇的火车，他们知道这个故事快要结束了。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Sự thật cuối cùng được tiết lộ! Ông Triệu kể rằng con trai ông — Triệu Tiểu Phi, vừa tốt nghiệp đại học "
        "ngành nghệ thuật — đã lấy bức tranh vì tin rằng nó thuộc về cha mình. Ông Triệu vừa vui vừa buồn khi thấy "
        "bức tranh, và biết con trai đã làm sai. Bức tranh 《山中日出》 vẫn còn nguyên vẹn trong nhà ông. "
        "Linh đề xuất một giải pháp: cùng nhau mang tranh trở về phòng tranh và giải thích mọi chuyện. "
        "Ông Triệu đồng ý — ông sẽ đích thân đi xin lỗi. "
        "Bạn sẽ ôn lại 15 từ vựng: 儿子, 大学, 毕业, 错, 对不起, 难过, 电话, 已经, 送, "
        "明白, 办法, 最后, 希望, 一定, 谢谢. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện "
        "và luyện nghe. Chương này đầy cảm xúc khi sự thật được phơi bày. "
        "Phần ôn tập cuối chương giúp bạn củng cố từ vựng và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 8 tiết lộ sự thật: con trai ông Triệu đã lấy bức tranh vì nghĩ nó thuộc về cha mình. "
        "Linh tìm ra giải pháp và ông Triệu đồng ý trả lại bức tranh. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 8: Sự Thật (真相)",
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
                "title": "Flashcards: Ôn tập Sự Thật",
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
