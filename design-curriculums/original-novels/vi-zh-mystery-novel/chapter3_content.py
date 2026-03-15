"""
Chapter 3: 第一个线索 (Manh Mối Đầu Tiên) — The First Clue
Linh finds a clue — a piece of red cloth near the gallery's back door.
"""


def get_content():
    vocab_1 = ["后面", "找到", "红"]
    vocab_2 = ["告诉", "知道", "可能"]
    vocab_3 = ["咖啡", "旁边", "听"]
    vocab_4 = ["时候", "外面", "下雨"]
    vocab_5 = ["想", "帮助", "重要"]
    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    passage_1 = "第三天，阿玲又去了画廊。这次她没有从前门进去，而是走到了画廊的后面。她想看看后面有没有什么线索。在后门旁边的地上，她找到了一小块红色的布。这块布很新，不像是很久以前掉在这里的。阿玲小心地把它捡起来，放进了口袋里。她觉得这可能是一个重要的线索。"

    passage_2 = "阿玲把红布拿给小明看。小明说他不知道这是什么，但是他可以帮阿玲问问别人。阿玲决定先去告诉王老师。王老师看了看那块布，想了一会儿说：我不确定，但是画廊里有一些旧的红布，以前用来盖画的。也许可能是从那里来的。阿玲记下了这个信息。"

    passage_3 = "中午，阿玲去了画廊旁边的一家咖啡店。咖啡店的老板是李阿姨，一个很热情的女人。阿玲点了一杯咖啡，坐在窗户旁边。她问李阿姨：那天晚上你有没有听到什么声音？李阿姨想了想说：我记得那天晚上大概九点的时候，我听到画廊后面好像有人说话的声音。"

    passage_4 = "李阿姨继续说：那个时候外面在下雨，声音不太清楚。我只听到好像有两个人在说话，但是我没有出去看。因为下雨天，街上没有人，我觉得可能是路过的人在躲雨。阿玲听了以后，在本子上写下了这些信息：九点，下雨，两个人的声音，画廊后面。"

    passage_5 = "晚上回到旅馆，阿玲坐在床上想今天发现的事情。她找到了一块红布，李阿姨听到了两个人的声音。这说明那天晚上可能有两个人去了画廊后面。阿玲觉得帮助警察找到画是很重要的事情。她决定明天去画廊后面再仔细看看，也许还能找到更多的线索。这个谜题越来越有意思了。"

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    preview_text = (
        "Linh bắt đầu tự mình điều tra! Trong chương này, cô đi ra phía sau phòng tranh và tìm thấy "
        "manh mối đầu tiên — một mảnh vải đỏ bí ẩn gần cửa sau. Cô mang mảnh vải cho thầy Vương xem "
        "và được biết phòng tranh từng có những tấm vải đỏ dùng để phủ tranh. Tại quán cà phê bên cạnh, "
        "cô Lý kể rằng đêm hôm đó cô nghe thấy tiếng hai người nói chuyện phía sau phòng tranh lúc trời mưa. "
        "Linh ghi chép cẩn thận mọi thông tin và bắt đầu ghép nối các mảnh ghép. "
        "Bạn sẽ ôn lại 15 từ vựng: 后面, 找到, 红, 告诉, 知道, 可能, 咖啡, 旁边, 听, "
        "时候, 外面, 下雨, 想, 帮助, 重要. Mỗi phần gồm thẻ từ vựng nhanh, đọc truyện trinh thám "
        "và luyện nghe theo. Câu chuyện ngày càng hấp dẫn khi Linh phát hiện ra rằng có hai người "
        "đã đến phòng tranh vào đêm bức tranh biến mất. Phần ôn tập cuối chương giúp bạn "
        "củng cố toàn bộ từ vựng và nghe lại cả chương."
    )

    description = (
        "Chương 3 kể về việc Linh tìm thấy manh mối đầu tiên — một mảnh vải đỏ — và nghe được "
        "lời kể của cô Lý về tiếng nói chuyện bí ẩn vào đêm mất tranh. "
        "Bạn sẽ luyện đọc 5 đoạn văn tiếng Trung với 15 từ vựng HSK2-3 quen thuộc."
    )

    curriculum = {
        "title": "Bức Tranh Biến Mất (消失的画) — Chương 3: Manh Mối Đầu Tiên (第一个线索)",
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
                "title": "Flashcards: Ôn tập Manh Mối Đầu Tiên",
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
