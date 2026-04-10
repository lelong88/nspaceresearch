"""
Create curriculum: Making Friends (Kết Bạn — Bước Đầu Tiên)
Level: beginner | Skill focus: balanced_skills | Content type: []
Topic: Relationships | 12 words (2 groups of 6) | 4 sessions | Bilingual (vi/en)
Tone: provocative_question | Farewell tone: team_building_energy
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from validate_curriculum import validate_balanced_skills_beginner, validate_content_type_tags, validate_bilingual_prompts

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Vocabulary ──
# Group 1 (Session 1): friend, introduce, invite, greet, hobby, share
# Group 2 (Session 2): trust, smile, conversation, polite, together, enjoy

W1 = ["friend", "introduce", "invite", "greet", "hobby", "share"]
W2 = ["trust", "smile", "conversation", "polite", "together", "enjoy"]
ALL_WORDS = W1 + W2

content = {
    "title": "Kết Bạn — Bước Đầu Tiên",
    "contentTypeTags": [],
    "description": (
        "BẠN CÓ BAO GIỜ MUỐN LÀM QUEN VỚI AI ĐÓ BẰNG TIẾNG ANH — NHƯNG KHÔNG BIẾT MỞ LỜI THẾ NÀO?\n\n"
        "Bạn gặp một người mới ở lớp học, ở công ty, hay ở quán cà phê. "
        "Bạn muốn nói 'Chào, mình tên là...' nhưng câu tiếng Anh cứ biến mất trong đầu. "
        "Bạn muốn hỏi sở thích, muốn rủ đi chơi — nhưng chỉ biết cười và im lặng.\n\n"
        "Kết bạn bằng tiếng Anh giống như đứng trước cánh cửa mà không có chìa khóa — "
        "bạn thấy bên trong ấm áp, vui vẻ, nhưng không thể bước vào. "
        "12 từ vựng trong bài học này chính là chiếc chìa khóa đó.\n\n"
        "Sau bài học, bạn sẽ tự tin chào hỏi, giới thiệu bản thân, và bắt đầu cuộc trò chuyện "
        "bằng tiếng Anh — dù ở trường, ở công ty, hay bất cứ đâu.\n\n"
        "Vừa học từ vựng giao tiếp, vừa mở rộng thế giới bạn bè — "
        "mỗi từ là một bước tiến gần hơn đến những mối quan hệ ý nghĩa bằng tiếng Anh."
    ),
    "preview": {
        "text": (
            "You meet someone new. You want to say hello. You want to ask about their hobbies. "
            "You want to invite them for coffee. But the English words just won't come. "
            "This curriculum gives you 12 essential friendship words — "
            "friend, introduce, invite, greet, hobby, share, trust, smile, conversation, polite, together, and enjoy. "
            "Across four sessions, you will learn each word through flashcards, reading passages about making friends "
            "at school and at work, and guided writing exercises. By the end, you will confidently greet new people, "
            "introduce yourself, start conversations, and build friendships in English — "
            "whether in a classroom, an office, or your neighborhood."
        )
    },
    "learningSessions": [
        # ════════════════════════════════════════════
        # SESSION 1 — Phần 1 (Words: friend, introduce, invite, greet, hobby, share)
        # ════════════════════════════════════════════
        {
            "title": "Phần 1",
            "activities": [
                # ── introAudio: Welcome + Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về kết bạn bằng tiếng Anh.",
                    "data": {
                        "text": (
                            "Xin chào và chào mừng bạn đến với bài học 'Kết Bạn — Bước Đầu Tiên'! "
                            "Hôm nay chúng ta sẽ học 6 từ vựng tiếng Anh rất quan trọng khi bạn muốn làm quen với người mới. "
                            "Những từ này sẽ giúp bạn tự tin hơn khi chào hỏi, giới thiệu bản thân, và bắt đầu tình bạn. "
                            "Sáu từ hôm nay là: friend, introduce, invite, greet, hobby, và share.\n\n"

                            "Từ đầu tiên là 'friend'. Friend là danh từ, nghĩa là 'bạn' hoặc 'bạn bè'. "
                            "Ví dụ: 'She is my best friend.' — Cô ấy là bạn thân nhất của tôi. "
                            "Trong bài đọc, bạn sẽ thấy từ 'friend' khi nhân vật nói về người bạn mới ở trường.\n\n"

                            "Từ thứ hai là 'introduce'. Introduce là động từ, nghĩa là 'giới thiệu'. "
                            "Ví dụ: 'Let me introduce myself. My name is Hoa.' — Để tôi giới thiệu. Tên tôi là Hoa. "
                            "Trong bài đọc, từ 'introduce' xuất hiện khi nhân vật giới thiệu bản thân với bạn mới.\n\n"

                            "Từ thứ ba là 'invite'. Invite là động từ, nghĩa là 'mời' hoặc 'rủ'. "
                            "Ví dụ: 'I invite my friend to my house.' — Tôi mời bạn tôi đến nhà. "
                            "Trong bài đọc, bạn sẽ thấy từ 'invite' khi nhân vật rủ bạn mới đi uống cà phê.\n\n"

                            "Từ thứ tư là 'greet'. Greet là động từ, nghĩa là 'chào hỏi'. "
                            "Ví dụ: 'I greet my teacher every morning.' — Tôi chào thầy giáo mỗi sáng. "
                            "Trong bài đọc, 'greet' là hành động đầu tiên khi nhân vật gặp người mới.\n\n"

                            "Từ thứ năm là 'hobby'. Hobby là danh từ, nghĩa là 'sở thích'. "
                            "Ví dụ: 'My hobby is reading books.' — Sở thích của tôi là đọc sách. "
                            "Trong bài đọc, bạn sẽ thấy từ 'hobby' khi hai nhân vật nói về sở thích của mình.\n\n"

                            "Từ cuối cùng là 'share'. Share là động từ, nghĩa là 'chia sẻ'. "
                            "Ví dụ: 'I share my lunch with my friend.' — Tôi chia sẻ bữa trưa với bạn tôi. "
                            "Trong bài đọc, từ 'share' xuất hiện khi hai nhân vật chia sẻ câu chuyện với nhau.\n\n"

                            "Bây giờ, hãy bắt đầu học từ vựng qua flashcards nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Kết bạn (Phần 1)",
                    "description": "Học 6 từ: friend, introduce, invite, greet, hobby, share",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Kết bạn (Phần 1)",
                    "description": "Học 6 từ: friend, introduce, invite, greet, hobby, share",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Kết bạn (Phần 1)",
                    "description": "Học 6 từ: friend, introduce, invite, greet, hobby, share",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Kết bạn (Phần 1)",
                    "description": "Học 6 từ: friend, introduce, invite, greet, hobby, share",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Bạn mới ở lớp",
                    "description": "Hoa meets a new classmate and makes a friend.",
                    "data": {
                        "text": (
                            "Hoa is a student. Today is her first day at a new school. "
                            "She does not know anyone. She feels a little shy.\n\n"
                            "A girl walks to Hoa. She greets Hoa with a big smile. "
                            "'Hi! My name is Mai,' she says. "
                            "'Let me introduce myself. I am in your class.'\n\n"
                            "Hoa is happy. She says, 'Nice to meet you, Mai.' "
                            "They talk about their hobbies. Mai likes drawing. "
                            "Hoa likes singing. They share stories about their families.\n\n"
                            "Mai says, 'I invite you to eat lunch with me.' "
                            "Hoa smiles. 'Yes! I would love that.' "
                            "Now Hoa has a new friend. She is not shy anymore."
                        ),
                        "vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Bạn mới ở lớp",
                    "description": "Hoa meets a new classmate and makes a friend.",
                    "data": {
                        "text": (
                            "Hoa is a student. Today is her first day at a new school. "
                            "She does not know anyone. She feels a little shy.\n\n"
                            "A girl walks to Hoa. She greets Hoa with a big smile. "
                            "'Hi! My name is Mai,' she says. "
                            "'Let me introduce myself. I am in your class.'\n\n"
                            "Hoa is happy. She says, 'Nice to meet you, Mai.' "
                            "They talk about their hobbies. Mai likes drawing. "
                            "Hoa likes singing. They share stories about their families.\n\n"
                            "Mai says, 'I invite you to eat lunch with me.' "
                            "Hoa smiles. 'Yes! I would love that.' "
                            "Now Hoa has a new friend. She is not shy anymore."
                        ),
                        "vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Bạn mới ở lớp",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Hoa is a student. Today is her first day at a new school. "
                            "She does not know anyone. She feels a little shy.\n\n"
                            "A girl walks to Hoa. She greets Hoa with a big smile. "
                            "'Hi! My name is Mai,' she says. "
                            "'Let me introduce myself. I am in your class.'\n\n"
                            "Hoa is happy. She says, 'Nice to meet you, Mai.' "
                            "They talk about their hobbies. Mai likes drawing. "
                            "Hoa likes singing. They share stories about their families.\n\n"
                            "Mai says, 'I invite you to eat lunch with me.' "
                            "Hoa smiles. 'Yes! I would love that.' "
                            "Now Hoa has a new friend. She is not shy anymore."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Kết bạn (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về kết bạn.",
                    "data": {
                        "vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share"],
                        "items": [
                            {
                                "targetVocab": "friend",
                                "prompt": "Hãy dùng từ 'friend' để viết một câu về người bạn của bạn. Ví dụ: My friend lives near my house."
                            },
                            {
                                "targetVocab": "introduce",
                                "prompt": "Hãy dùng từ 'introduce' để viết một câu về việc giới thiệu bản thân. Ví dụ: I introduce myself to the new student."
                            },
                            {
                                "targetVocab": "invite",
                                "prompt": "Hãy dùng từ 'invite' để viết một câu về việc mời ai đó. Ví dụ: I invite my friend to my birthday party."
                            },
                            {
                                "targetVocab": "greet",
                                "prompt": "Hãy dùng từ 'greet' để viết một câu về việc chào hỏi. Ví dụ: I greet my neighbors every morning."
                            },
                            {
                                "targetVocab": "hobby",
                                "prompt": "Hãy dùng từ 'hobby' để viết một câu về sở thích của bạn. Ví dụ: My hobby is playing the guitar."
                            },
                            {
                                "targetVocab": "share",
                                "prompt": "Hãy dùng từ 'share' để viết một câu về việc chia sẻ. Ví dụ: I share my snacks with my classmates."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 2 — Phần 2 (Words: trust, smile, conversation, polite, together, enjoy)
        # ════════════════════════════════════════════
        {
            "title": "Phần 2",
            "activities": [
                # ── introAudio: Recap + New Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng mới",
                    "description": "Ôn lại từ vựng Phần 1 và giới thiệu 6 từ mới về tình bạn.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong Phần 1, bạn đã học 6 từ rất hữu ích: "
                            "friend (bạn), introduce (giới thiệu), invite (mời), greet (chào hỏi), hobby (sở thích), và share (chia sẻ). "
                            "Bạn còn nhớ không? Tuyệt vời!\n\n"
                            "Hôm nay chúng ta sẽ học thêm 6 từ mới. Những từ này giúp bạn xây dựng tình bạn sâu hơn, "
                            "trò chuyện tự nhiên hơn, và tận hưởng thời gian bên bạn bè. "
                            "Sáu từ mới là: trust, smile, conversation, polite, together, và enjoy.\n\n"

                            "Từ đầu tiên là 'trust'. Trust có thể là danh từ hoặc động từ. "
                            "Là danh từ, nó nghĩa là 'sự tin tưởng'. Là động từ, nó nghĩa là 'tin tưởng'. "
                            "Ví dụ: 'I trust my best friend.' — Tôi tin tưởng bạn thân nhất của tôi. "
                            "Trong bài đọc, bạn sẽ thấy từ 'trust' khi nhân vật nói về sự tin tưởng trong tình bạn.\n\n"

                            "Từ thứ hai là 'smile'. Smile có thể là danh từ hoặc động từ. "
                            "Là danh từ, nó nghĩa là 'nụ cười'. Là động từ, nó nghĩa là 'mỉm cười'. "
                            "Ví dụ: 'Her smile makes everyone happy.' — Nụ cười của cô ấy làm mọi người vui. "
                            "Trong bài đọc, từ 'smile' xuất hiện khi nhân vật mỉm cười với bạn mới.\n\n"

                            "Từ thứ ba là 'conversation'. Conversation là danh từ, nghĩa là 'cuộc trò chuyện'. "
                            "Ví dụ: 'We have a long conversation about music.' — Chúng tôi có một cuộc trò chuyện dài về âm nhạc. "
                            "Trong bài đọc, bạn sẽ thấy từ 'conversation' khi hai nhân vật nói chuyện với nhau.\n\n"

                            "Từ thứ tư là 'polite'. Polite là tính từ, nghĩa là 'lịch sự'. "
                            "Ví dụ: 'He is very polite to everyone.' — Anh ấy rất lịch sự với mọi người. "
                            "Trong bài đọc, từ 'polite' xuất hiện khi nhân vật mô tả cách cư xử lịch sự.\n\n"

                            "Từ thứ năm là 'together'. Together là trạng từ, nghĩa là 'cùng nhau'. "
                            "Ví dụ: 'We study together after school.' — Chúng tôi học cùng nhau sau giờ học. "
                            "Trong bài đọc, bạn sẽ thấy từ 'together' khi hai nhân vật làm việc cùng nhau.\n\n"

                            "Từ cuối cùng là 'enjoy'. Enjoy là động từ, nghĩa là 'tận hưởng' hoặc 'thích'. "
                            "Ví dụ: 'I enjoy spending time with my friends.' — Tôi thích dành thời gian với bạn bè. "
                            "Trong bài đọc, từ 'enjoy' xuất hiện khi nhân vật tận hưởng thời gian bên bạn mới.\n\n"

                            "Hãy bắt đầu với flashcards để ghi nhớ 6 từ mới này nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Kết bạn (Phần 2)",
                    "description": "Học 6 từ: trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Kết bạn (Phần 2)",
                    "description": "Học 6 từ: trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Kết bạn (Phần 2)",
                    "description": "Học 6 từ: trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Kết bạn (Phần 2)",
                    "description": "Học 6 từ: trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Đồng nghiệp mới",
                    "description": "Tùng meets a new coworker and they become friends.",
                    "data": {
                        "text": (
                            "Tùng starts a new job today. He is nervous. "
                            "He does not know anyone at the office.\n\n"
                            "A man walks to his desk. He has a warm smile. "
                            "'Hello! I am Bình,' he says. He is very polite. "
                            "'Welcome to our team.'\n\n"
                            "They start a conversation about work. "
                            "Bình asks, 'What do you enjoy doing after work?' "
                            "Tùng says, 'I enjoy playing football.'\n\n"
                            "Bình smiles. 'Me too! Let us play together this weekend.' "
                            "Tùng feels happy. He can trust Bình. "
                            "They are going to be good friends."
                        ),
                        "vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Đồng nghiệp mới",
                    "description": "Tùng meets a new coworker and they become friends.",
                    "data": {
                        "text": (
                            "Tùng starts a new job today. He is nervous. "
                            "He does not know anyone at the office.\n\n"
                            "A man walks to his desk. He has a warm smile. "
                            "'Hello! I am Bình,' he says. He is very polite. "
                            "'Welcome to our team.'\n\n"
                            "They start a conversation about work. "
                            "Bình asks, 'What do you enjoy doing after work?' "
                            "Tùng says, 'I enjoy playing football.'\n\n"
                            "Bình smiles. 'Me too! Let us play together this weekend.' "
                            "Tùng feels happy. He can trust Bình. "
                            "They are going to be good friends."
                        ),
                        "vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Đồng nghiệp mới",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Tùng starts a new job today. He is nervous. "
                            "He does not know anyone at the office.\n\n"
                            "A man walks to his desk. He has a warm smile. "
                            "'Hello! I am Bình,' he says. He is very polite. "
                            "'Welcome to our team.'\n\n"
                            "They start a conversation about work. "
                            "Bình asks, 'What do you enjoy doing after work?' "
                            "Tùng says, 'I enjoy playing football.'\n\n"
                            "Bình smiles. 'Me too! Let us play together this weekend.' "
                            "Tùng feels happy. He can trust Bình. "
                            "They are going to be good friends."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Kết bạn (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng mới về tình bạn.",
                    "data": {
                        "vocabList": ["trust", "smile", "conversation", "polite", "together", "enjoy"],
                        "items": [
                            {
                                "targetVocab": "trust",
                                "prompt": "Hãy dùng từ 'trust' để viết một câu về sự tin tưởng trong tình bạn. Ví dụ: I trust my friend to keep my secret."
                            },
                            {
                                "targetVocab": "smile",
                                "prompt": "Hãy dùng từ 'smile' để viết một câu về nụ cười. Ví dụ: A smile can make a stranger feel welcome."
                            },
                            {
                                "targetVocab": "conversation",
                                "prompt": "Hãy dùng từ 'conversation' để viết một câu về cuộc trò chuyện. Ví dụ: We have a fun conversation at lunch every day."
                            },
                            {
                                "targetVocab": "polite",
                                "prompt": "Hãy dùng từ 'polite' để viết một câu về sự lịch sự. Ví dụ: It is polite to say thank you when someone helps you."
                            },
                            {
                                "targetVocab": "together",
                                "prompt": "Hãy dùng từ 'together' để viết một câu về việc làm gì đó cùng nhau. Ví dụ: My friend and I walk to school together."
                            },
                            {
                                "targetVocab": "enjoy",
                                "prompt": "Hãy dùng từ 'enjoy' để viết một câu về điều bạn thích làm. Ví dụ: I enjoy cooking dinner with my family."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 3 — Ôn tập (Review: all 12 words)
        # ════════════════════════════════════════════
        {
            "title": "Ôn tập",
            "activities": [
                # ── introAudio: Review ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 12 từ vựng! Hãy ôn tập lại tất cả.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về kết bạn và giao tiếp xã hội. Thật tuyệt vời!\n\n"
                            "Trong Phần 1, bạn đã học: friend (bạn), introduce (giới thiệu), invite (mời), "
                            "greet (chào hỏi), hobby (sở thích), và share (chia sẻ). "
                            "Bạn đã đọc về Hoa làm quen với Mai ở trường mới.\n\n"
                            "Trong Phần 2, bạn đã học: trust (tin tưởng), smile (mỉm cười), "
                            "conversation (cuộc trò chuyện), polite (lịch sự), together (cùng nhau), và enjoy (tận hưởng). "
                            "Bạn đã đọc về Tùng gặp đồng nghiệp mới Bình ở công ty.\n\n"
                            "Bây giờ là lúc ôn tập! Bạn sẽ xem lại tất cả 12 từ qua flashcards, "
                            "luyện tập qua các bài tập từ vựng, và viết câu với mỗi từ. "
                            "Sau phần ôn tập này, bạn sẽ sẵn sàng đọc toàn bộ bài đọc trong Phần 4. "
                            "Hãy cố gắng nhé!"
                        )
                    }
                },
                # ── viewFlashcards (all 12) ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập kết bạn",
                    "description": "Ôn tập 12 từ: friend, introduce, invite, greet, hobby, share, trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── speakFlashcards (all 12) ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập kết bạn",
                    "description": "Ôn tập 12 từ: friend, introduce, invite, greet, hobby, share, trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── vocabLevel1 (all 12) ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập kết bạn",
                    "description": "Ôn tập 12 từ: friend, introduce, invite, greet, hobby, share, trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── vocabLevel2 (all 12) ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập kết bạn",
                    "description": "Ôn tập 12 từ: friend, introduce, invite, greet, hobby, share, trust, smile, conversation, polite, together, enjoy",
                    "data": {"vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"]}
                },
                # ── writingSentence (all 12) ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập kết bạn",
                    "description": "Viết câu sử dụng tất cả 12 từ vựng về kết bạn.",
                    "data": {
                        "vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"],
                        "items": [
                            {
                                "targetVocab": "friend",
                                "prompt": "Hãy dùng từ 'friend' để viết một câu về tình bạn. Ví dụ: A good friend always listens to you."
                            },
                            {
                                "targetVocab": "introduce",
                                "prompt": "Hãy dùng từ 'introduce' để viết một câu về việc giới thiệu ai đó. Ví dụ: I introduce my friend to my parents."
                            },
                            {
                                "targetVocab": "invite",
                                "prompt": "Hãy dùng từ 'invite' để viết một câu về việc mời bạn bè. Ví dụ: I invite my friends to watch a movie together."
                            },
                            {
                                "targetVocab": "greet",
                                "prompt": "Hãy dùng từ 'greet' để viết một câu về cách bạn chào hỏi. Ví dụ: I always greet people with a friendly hello."
                            },
                            {
                                "targetVocab": "hobby",
                                "prompt": "Hãy dùng từ 'hobby' để viết một câu về sở thích chung với bạn. Ví dụ: My friend and I have the same hobby."
                            },
                            {
                                "targetVocab": "share",
                                "prompt": "Hãy dùng từ 'share' để viết một câu về việc chia sẻ với bạn bè. Ví dụ: Good friends share both happy and sad moments."
                            },
                            {
                                "targetVocab": "trust",
                                "prompt": "Hãy dùng từ 'trust' để viết một câu về sự tin tưởng. Ví dụ: Trust is the most important thing in a friendship."
                            },
                            {
                                "targetVocab": "smile",
                                "prompt": "Hãy dùng từ 'smile' để viết một câu về nụ cười. Ví dụ: Her warm smile makes me feel comfortable."
                            },
                            {
                                "targetVocab": "conversation",
                                "prompt": "Hãy dùng từ 'conversation' để viết một câu về cuộc trò chuyện. Ví dụ: A good conversation can start a new friendship."
                            },
                            {
                                "targetVocab": "polite",
                                "prompt": "Hãy dùng từ 'polite' để viết một câu về sự lịch sự. Ví dụ: Being polite helps you make friends easily."
                            },
                            {
                                "targetVocab": "together",
                                "prompt": "Hãy dùng từ 'together' để viết một câu về việc làm gì đó cùng bạn. Ví dụ: We eat lunch together every day at school."
                            },
                            {
                                "targetVocab": "enjoy",
                                "prompt": "Hãy dùng từ 'enjoy' để viết một câu về điều bạn thích làm cùng bạn bè. Ví dụ: I enjoy playing games with my friends on weekends."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 4 — Đọc toàn bài (Final Reading)
        # ════════════════════════════════════════════
        {
            "title": "Đọc toàn bài",
            "activities": [
                # ── introAudio: Final reading intro ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc cuối",
                    "description": "Giới thiệu bài đọc tổng hợp với tất cả 12 từ vựng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của bài học 'Kết Bạn — Bước Đầu Tiên'!\n\n"
                            "Bạn đã học 12 từ vựng quan trọng: friend, introduce, invite, greet, hobby, share, "
                            "trust, smile, conversation, polite, together, và enjoy. "
                            "Trong Phần 1, bạn đọc về Hoa làm quen với Mai ở trường mới. "
                            "Trong Phần 2, bạn đọc về Tùng gặp đồng nghiệp mới Bình ở công ty.\n\n"
                            "Bây giờ, bạn sẽ đọc một bài đọc dài hơn. Bài đọc này kết hợp tất cả 12 từ vựng "
                            "trong một câu chuyện về việc kết bạn. Hãy chú ý cách mỗi từ được sử dụng trong ngữ cảnh thực tế.\n\n"
                            "Hãy đọc chậm, tận hưởng câu chuyện, và nhận ra những từ bạn đã học. Bạn sẽ ngạc nhiên "
                            "vì mình hiểu được nhiều hơn bạn nghĩ đấy!"
                        )
                    }
                },
                # ── reading: Full article ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Ngày hội kết bạn",
                    "description": "A full story about a friendship day event using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "Today is Friendship Day at Hoa's school. "
                            "The teacher says, 'Today you will meet new people. Be polite and have fun!'\n\n"
                            "Hoa is excited. She wants to make a new friend. "
                            "She sees a girl sitting alone. The girl looks shy. "
                            "Hoa walks to her and greets her with a warm smile. "
                            "'Hi! My name is Hoa. Let me introduce myself. I like music and cooking.'\n\n"
                            "The girl smiles back. 'I am Linh. Nice to meet you.' "
                            "They start a conversation about their hobbies. "
                            "Linh says, 'My hobby is painting. I paint every weekend.' "
                            "Hoa says, 'That is so cool! I enjoy singing.'\n\n"
                            "They share stories about their families. "
                            "Linh has a younger brother. Hoa has an older sister. "
                            "They laugh together about funny things at home.\n\n"
                            "Hoa says, 'I invite you to come to my house this Saturday. "
                            "We can paint and sing together!' "
                            "Linh is very happy. 'Yes! I would love that.'\n\n"
                            "At lunch, they sit together. They talk and laugh. "
                            "Hoa shares her sandwich with Linh. "
                            "Linh shares her fruit with Hoa. "
                            "They enjoy their meal and their new friendship.\n\n"
                            "After school, Hoa tells her mother about Linh. "
                            "'I made a new friend today! She is very polite and kind.' "
                            "Her mother smiles. 'That is wonderful, Hoa.'\n\n"
                            "Hoa thinks about her day. She is happy. "
                            "She knows that trust and kindness are important in friendship. "
                            "A good friend listens, shares, and enjoys time together. "
                            "Hoa cannot wait to see Linh again."
                        ),
                        "vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Ngày hội kết bạn",
                    "description": "A full story about a friendship day event using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "Today is Friendship Day at Hoa's school. "
                            "The teacher says, 'Today you will meet new people. Be polite and have fun!'\n\n"
                            "Hoa is excited. She wants to make a new friend. "
                            "She sees a girl sitting alone. The girl looks shy. "
                            "Hoa walks to her and greets her with a warm smile. "
                            "'Hi! My name is Hoa. Let me introduce myself. I like music and cooking.'\n\n"
                            "The girl smiles back. 'I am Linh. Nice to meet you.' "
                            "They start a conversation about their hobbies. "
                            "Linh says, 'My hobby is painting. I paint every weekend.' "
                            "Hoa says, 'That is so cool! I enjoy singing.'\n\n"
                            "They share stories about their families. "
                            "Linh has a younger brother. Hoa has an older sister. "
                            "They laugh together about funny things at home.\n\n"
                            "Hoa says, 'I invite you to come to my house this Saturday. "
                            "We can paint and sing together!' "
                            "Linh is very happy. 'Yes! I would love that.'\n\n"
                            "At lunch, they sit together. They talk and laugh. "
                            "Hoa shares her sandwich with Linh. "
                            "Linh shares her fruit with Hoa. "
                            "They enjoy their meal and their new friendship.\n\n"
                            "After school, Hoa tells her mother about Linh. "
                            "'I made a new friend today! She is very polite and kind.' "
                            "Her mother smiles. 'That is wonderful, Hoa.'\n\n"
                            "Hoa thinks about her day. She is happy. "
                            "She knows that trust and kindness are important in friendship. "
                            "A good friend listens, shares, and enjoys time together. "
                            "Hoa cannot wait to see Linh again."
                        ),
                        "vocabList": ["friend", "introduce", "invite", "greet", "hobby", "share", "trust", "smile", "conversation", "polite", "together", "enjoy"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ngày hội kết bạn",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Today is Friendship Day at Hoa's school. "
                            "The teacher says, 'Today you will meet new people. Be polite and have fun!'\n\n"
                            "Hoa is excited. She wants to make a new friend. "
                            "She sees a girl sitting alone. The girl looks shy. "
                            "Hoa walks to her and greets her with a warm smile. "
                            "'Hi! My name is Hoa. Let me introduce myself. I like music and cooking.'\n\n"
                            "The girl smiles back. 'I am Linh. Nice to meet you.' "
                            "They start a conversation about their hobbies. "
                            "Linh says, 'My hobby is painting. I paint every weekend.' "
                            "Hoa says, 'That is so cool! I enjoy singing.'\n\n"
                            "They share stories about their families. "
                            "Linh has a younger brother. Hoa has an older sister. "
                            "They laugh together about funny things at home.\n\n"
                            "Hoa says, 'I invite you to come to my house this Saturday. "
                            "We can paint and sing together!' "
                            "Linh is very happy. 'Yes! I would love that.'\n\n"
                            "At lunch, they sit together. They talk and laugh. "
                            "Hoa shares her sandwich with Linh. "
                            "Linh shares her fruit with Hoa. "
                            "They enjoy their meal and their new friendship.\n\n"
                            "After school, Hoa tells her mother about Linh. "
                            "'I made a new friend today! She is very polite and kind.' "
                            "Her mother smiles. 'That is wonderful, Hoa.'\n\n"
                            "Hoa thinks about her day. She is happy. "
                            "She knows that trust and kindness are important in friendship. "
                            "A good friend listens, shares, and enjoys time together. "
                            "Hoa cannot wait to see Linh again."
                        )
                    }
                },
                # ── introAudio: Farewell (team_building_energy tone) ──
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay đầy năng lượng.",
                    "data": {
                        "text": (
                            "Tuyệt vời! Bạn đã hoàn thành bài học 'Kết Bạn — Bước Đầu Tiên'! "
                            "Hãy cùng ôn lại những từ quan trọng nhất nhé.\n\n"

                            "Từ 'friend' nghĩa là bạn bè. Khi bạn muốn nói về tình bạn, hãy nói: "
                            "'She became my closest friend after just one week.' — Cô ấy trở thành bạn thân nhất của tôi chỉ sau một tuần.\n\n"

                            "Từ 'introduce' nghĩa là giới thiệu. "
                            "Khi bạn gặp người mới, hãy nói: "
                            "'Let me introduce you to my classmate.' — Để tôi giới thiệu bạn với bạn cùng lớp của tôi.\n\n"

                            "Từ 'conversation' nghĩa là cuộc trò chuyện. "
                            "Khi bạn muốn bắt chuyện, hãy nói: "
                            "'Can we have a conversation over coffee?' — Chúng ta có thể trò chuyện bên tách cà phê không?\n\n"

                            "Từ 'trust' nghĩa là tin tưởng. "
                            "Khi bạn muốn nói về sự tin tưởng, hãy nói: "
                            "'I trust you because you always tell the truth.' — Tôi tin bạn vì bạn luôn nói thật.\n\n"

                            "Từ 'polite' nghĩa là lịch sự. "
                            "Khi bạn muốn khen ai đó, hãy nói: "
                            "'You are always so polite to everyone.' — Bạn luôn rất lịch sự với mọi người.\n\n"

                            "Từ 'enjoy' nghĩa là tận hưởng. "
                            "Khi bạn muốn nói về niềm vui, hãy nói: "
                            "'I really enjoy our time together.' — Tôi thật sự tận hưởng thời gian bên nhau.\n\n"

                            "Bạn đã học 12 từ vựng thực tế về kết bạn và giao tiếp xã hội. "
                            "Và bạn biết không? Bạn không học một mình đâu — hàng ngàn người cũng đang học cùng bạn! "
                            "Chúng ta là một đội. Mỗi từ bạn học hôm nay là một viên gạch xây nên cầu nối "
                            "giữa bạn và thế giới.\n\n"

                            "Lần tới khi bạn gặp ai đó mới, hãy mạnh dạn chào hỏi bằng tiếng Anh. "
                            "Giới thiệu bản thân. Hỏi về sở thích. Mỉm cười. "
                            "Bạn đã có đủ từ vựng để bắt đầu rồi!\n\n"

                            "Hãy nhớ: mỗi tình bạn đều bắt đầu bằng một câu chào đơn giản. "
                            "Và bạn — bạn đã sẵn sàng. Hẹn gặp lại ở bài học tiếp theo nhé! Cùng tiến lên nào!"
                        )
                    }
                }
            ]
        }
    ]
}

# ── Validation ──
validate_content_type_tags(content)
validate_balanced_skills_beginner(content)
validate_bilingual_prompts(content, "beginner")

print("✅ Validation passed!")

# ── Create curriculum ──
token = get_firebase_id_token(UID)
res = requests.post(f"{API_BASE}/curriculum/create", json={
    "firebaseIdToken": token,
    "language": "en",
    "userLanguage": "vi",
    "content": json.dumps(content)
})
res.raise_for_status()
data = res.json()
print(f"Created curriculum: {data['id']}")
print(f"Title: {content['title']}")
