"""
Chapter 4: 可疑的人 (Người Đáng Ngờ) — The Suspect
Linh discovers the guard Zhang was in debt and had a secret meeting that night.
"""


def get_content():
    vocab_1 = ["钱", "工作", "每天"]
    vocab_2 = ["说话", "声音", "害怕"]
    vocab_3 = ["以前", "认识", "别人"]
    vocab_4 = ["打电话", "等", "出来"]
    vocab_5 = ["相信", "事情", "秘密"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "阿玲想了解更多关于张叔叔的事情。她问小明：张叔叔在画廊工作多长时间了？小明说：他在这里工作了十年，每天都来。但是最近他好像不太开心。听说他需要很多钱，因为他的儿子要去大城市上大学。阿玲听了以后，心里有了一个想法。"

    passage_2 = "下午，阿玲在画廊附近散步。她看到张叔叔站在一棵树下面，正在和一个穿黑衣服的男人说话。他们的声音很小，好像不想让别人听到。阿玲躲在墙后面，虽然听不清他们说什么，但是她看到张叔叔的表情很紧张，好像很害怕的样子。那个黑衣服的男人说完话就走了。"

    passage_3 = "阿玲去问李阿姨：你认识那个穿黑衣服的男人吗？李阿姨想了想说：我以前好像见过他，但是不太确定。他不是我们镇上的人，可能是从别人介绍来的。阿玲又问：张叔叔以前有没有和这样的人见过面？李阿姨说：我不太清楚，但是最近张叔叔确实有点奇怪。"

    passage_4 = "晚上，阿玲在旅馆门口看到张叔叔。他正在打电话，说话的声音很小。阿玲假装在看手机，站在旁边等着。张叔叔打完电话以后，看到阿玲，脸色变了一下。他很快走了出来，对阿玲说：你怎么在这里？阿玲笑着说：我住在这里啊。张叔叔没有再说什么，转身就走了。"

    passage_5 = "回到房间，阿玲把今天的事情都写在本子上。张叔叔需要钱，他和一个陌生男人有秘密的见面，打电话的时候很紧张。这些事情让阿玲觉得张叔叔可能知道一些关于画的秘密。但是她还不能确定，因为她不想冤枉好人。她需要更多的证据。阿玲决定明天继续调查，她相信真相很快就会出现。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Cuộc điều tra của Linh ngày càng hấp dẫn! Trong chương này, Linh phát hiện bác bảo vệ Trương "
        "đang gặp khó khăn về tài chính — con trai bác cần tiền đi học đại học. Linh tình cờ thấy bác Trương "
        "bí mật gặp một người đàn ông lạ mặc đồ đen, hai người nói chuyện rất nhỏ với vẻ mặt căng thẳng. "
        "Buổi tối, Linh lại thấy bác Trương gọi điện thoại một cách bí ẩn gần khách sạn. "
        "Tất cả những điều này khiến Linh nghi ngờ bác Trương có liên quan đến vụ mất tranh. "
        "Bạn sẽ ôn lại 15 từ vựng: 钱, 工作, 每天, 说话, 声音, 害怕, 以前, 认识, 别人, "
        "打电话, 等, 出来, 相信, 事情, 秘密. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện trinh thám "
        "và luyện nghe. Linh đang dần ghép nối các mảnh ghép — nhưng cô vẫn cần thêm bằng chứng. "
        "Phần ôn tập cuối chương giúp bạn củng cố từ vựng và nghe lại toàn bộ câu chuyện."
    )

    description = (
        "Chương 4 tập trung vào bác bảo vệ Trương — người có vấn đề tài chính và những cuộc gặp bí mật. "
        "Linh thu thập thêm manh mối nhưng vẫn chưa đủ bằng chứng. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 4: Người Đáng Ngờ (可疑的人)",
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
                "title": "Flashcards: Ôn tập Người Đáng Ngờ",
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
