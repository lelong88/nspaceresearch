"""
Chapter 2: 消失的画 (Bức Tranh Biến Mất) — The Vanishing Painting
The famous painting "山中日出" disappears from the gallery overnight.
"""


def get_content():
    vocab_1 = ["早上", "发现", "没有"]
    vocab_2 = ["门", "窗户", "关"]
    vocab_3 = ["警察", "问题", "回答"]
    vocab_4 = ["昨天", "看见", "走"]
    vocab_5 = ["觉得", "奇怪", "为什么"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "第二天早上，阿玲去画廊上课。但是画廊门口站着很多人，大家都在说话。阿玲走过去，发现王老师的脸色很不好。王老师说：昨天晚上，画廊里最有名的那幅画不见了。《山中日出》没有了！阿玲非常吃惊，那幅画昨天她还看过，怎么会不见呢？"

    passage_2 = "阿玲和小明一起走进画廊。他们看到墙上空了一块地方，那就是《山中日出》以前挂的位置。小明检查了画廊的门和窗户，门上的锁没有坏，窗户也都关着。小明说：如果门和窗户都是关着的，那画是怎么出去的呢？阿玲也觉得很奇怪，她仔细看了看四周。"

    passage_3 = "很快，两个警察来到了画廊。他们问了王老师很多问题。王老师一个一个地回答：画廊每天晚上六点关门，他是最后一个离开的人。他走的时候，画还在墙上。警察又问了其他人，但是没有人知道发生了什么。阿玲站在旁边，认真地听着每一个人的回答。"

    passage_4 = "警察问张叔叔：你昨天晚上在哪里？张叔叔是画廊的保安。他说他昨天晚上在画廊门口，一直到十点才走回家。他没有看见任何人进来。但是阿玲注意到，张叔叔说话的时候，眼睛一直看着地上，好像不太自然。阿玲心里想：他是不是有什么事情没有说？她决定以后再问问他。"

    passage_5 = "回到旅馆，阿玲坐在桌子前面想这件事。她觉得这件事很奇怪：门和窗户都是关着的，保安说没有看见人，但是画就是不见了。为什么会这样呢？阿玲在本子上画了一张画廊的地图，把她知道的事情都写了下来。她想，也许明天去画廊再看看，能发现什么新的线索。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Câu chuyện bắt đầu gay cấn! Sáng hôm sau khi Linh đến phòng tranh để học vẽ, cô phát hiện bức tranh "
        "nổi tiếng nhất — 《山中日出》 — đã biến mất một cách bí ẩn trong đêm. Cửa vẫn khóa, cửa sổ vẫn đóng, "
        "nhưng bức tranh không còn trên tường. Cảnh sát đến điều tra và hỏi mọi người, nhưng không ai biết chuyện gì "
        "đã xảy ra. Linh bắt đầu chú ý đến những chi tiết nhỏ — đặc biệt là thái độ kỳ lạ của bác bảo vệ Trương. "
        "Trong chương này, bạn sẽ ôn lại 15 từ vựng: 早上, 发现, 没有, 门, 窗户, 关, 警察, 问题, 回答, "
        "昨天, 看见, 走, 觉得, 奇怪, 为什么. Mỗi phần gồm thẻ từ vựng, đọc truyện và luyện nghe. "
        "Bạn sẽ cùng Linh tìm kiếm manh mối đầu tiên trong vụ mất tranh bí ẩn này. "
        "Phần ôn tập cuối chương giúp bạn củng cố từ vựng và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 2 kể về sự biến mất bí ẩn của bức tranh nổi tiếng trong phòng tranh. "
        "Cảnh sát đến điều tra nhưng không tìm được câu trả lời. Linh bắt đầu quan sát và ghi chép. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 2: Bức Tranh Biến Mất (消失的画)",
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
                "title": "Flashcards: Ôn tập Bức Tranh Biến Mất",
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
