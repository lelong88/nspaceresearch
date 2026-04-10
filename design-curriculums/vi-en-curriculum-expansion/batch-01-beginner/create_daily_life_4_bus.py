"""
Create curriculum: Taking the Bus (Đi Xe Buýt — Bước Đầu Tiên)
Level: beginner | Skill focus: balanced_skills | Content type: []
Topic: Daily life | 12 words (2 groups of 6) | 4 sessions | Bilingual (vi/en)
Tone: bold_declaration | Farewell tone: introspective_guide
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
# Group 1 (Session 1): bus, stop, ticket, driver, passenger, route
# Group 2 (Session 2): schedule, seat, fare, transfer, station, arrive

W1 = ["bus", "stop", "ticket", "driver", "passenger", "route"]
W2 = ["schedule", "seat", "fare", "transfer", "station", "arrive"]
ALL_WORDS = W1 + W2

content = {
    "title": "Đi Xe Buýt — Bước Đầu Tiên",
    "contentTypeTags": [],
    "description": (
        "ĐI XE BUÝT BẰNG TIẾNG ANH KHÔNG KHÓ — KHÓ LÀ BẠN CHƯA BAO GIỜ ĐƯỢC AI CHỈ CHO.\n\n"
        "Bạn đứng ở trạm xe buýt. Xe đến. Bạn muốn hỏi tài xế: 'Xe này có đi qua bệnh viện không?' "
        "Bạn muốn nói: 'Cho tôi một vé.' Nhưng câu tiếng Anh cứ mắc kẹt trong đầu, "
        "và xe buýt thì không chờ ai cả.\n\n"
        "Đi xe buýt ở nước ngoài mà không biết từ vựng giống như lên nhầm tuyến — "
        "bạn cứ đi mãi nhưng không bao giờ đến nơi cần đến. "
        "12 từ vựng trong bài học này chính là tấm bản đồ giúp bạn đi đúng hướng.\n\n"
        "Sau bài học, bạn sẽ tự tin mua vé, hỏi tuyến đường, và đổi xe buýt bằng tiếng Anh — "
        "dù ở Sài Gòn hay bất kỳ thành phố nào trên thế giới.\n\n"
        "Vừa học từ vựng giao thông thực tế, vừa nâng cấp khả năng giao tiếp — "
        "mỗi từ là một bước tiến gần hơn đến sự tự do khi di chuyển bằng tiếng Anh."
    ),
    "preview": {
        "text": (
            "You stand at a bus stop in a new city. A bus pulls up. "
            "You want to ask: 'Does this bus go to the hospital?' "
            "But you freeze. This curriculum gives you 12 essential bus and transportation words — "
            "bus, stop, ticket, driver, passenger, route, schedule, seat, fare, transfer, station, and arrive. "
            "Across four sessions, you will learn each word through flashcards, reading passages about real bus rides in Vietnam, "
            "and guided writing exercises. By the end, you will confidently buy tickets, ask about routes, "
            "and navigate public transportation in English — whether riding a city bus in Ho Chi Minh City or catching a coach abroad."
        )
    },
    "learningSessions": [
        # ════════════════════════════════════════════
        # SESSION 1 — Phần 1 (Words: bus, stop, ticket, driver, passenger, route)
        # ════════════════════════════════════════════
        {
            "title": "Phần 1",
            "activities": [
                # ── introAudio: Welcome + Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về đi xe buýt bằng tiếng Anh.",
                    "data": {
                        "text": (
                            "Xin chào và chào mừng bạn đến với bài học 'Đi Xe Buýt'! "
                            "Hôm nay chúng ta sẽ học 6 từ vựng tiếng Anh rất quan trọng khi bạn đi xe buýt. "
                            "Những từ này sẽ giúp bạn tự tin hơn khi hỏi đường, mua vé, và nói chuyện với tài xế. "
                            "Sáu từ hôm nay là: bus, stop, ticket, driver, passenger, và route.\n\n"

                            "Từ đầu tiên là 'bus'. Bus là danh từ, nghĩa là 'xe buýt'. "
                            "Ví dụ: 'I take the bus to school every day.' — Tôi đi xe buýt đến trường mỗi ngày. "
                            "Trong bài đọc, bạn sẽ thấy từ 'bus' khi nhân vật đi xe buýt đến chỗ làm.\n\n"

                            "Từ thứ hai là 'stop'. Stop là danh từ, nghĩa là 'trạm' hoặc 'điểm dừng'. "
                            "Ví dụ: 'The bus stop is near my house.' — Trạm xe buýt ở gần nhà tôi. "
                            "Trong bài đọc, từ 'stop' xuất hiện khi nhân vật đợi xe ở trạm.\n\n"

                            "Từ thứ ba là 'ticket'. Ticket là danh từ, nghĩa là 'vé'. "
                            "Ví dụ: 'How much is a bus ticket?' — Vé xe buýt giá bao nhiêu? "
                            "Trong bài đọc, bạn sẽ thấy từ 'ticket' khi nhân vật mua vé xe buýt.\n\n"

                            "Từ thứ tư là 'driver'. Driver là danh từ, nghĩa là 'tài xế' hoặc 'người lái xe'. "
                            "Ví dụ: 'The bus driver is very friendly.' — Tài xế xe buýt rất thân thiện. "
                            "Trong bài đọc, 'driver' là người lái xe buýt mà nhân vật hỏi đường.\n\n"

                            "Từ thứ năm là 'passenger'. Passenger là danh từ, nghĩa là 'hành khách'. "
                            "Ví dụ: 'There are many passengers on the bus.' — Có nhiều hành khách trên xe buýt. "
                            "Trong bài đọc, 'passenger' là những người cùng đi xe buýt với nhân vật.\n\n"

                            "Từ cuối cùng là 'route'. Route là danh từ, nghĩa là 'tuyến đường' hoặc 'lộ trình'. "
                            "Ví dụ: 'This bus route goes to the city center.' — Tuyến xe buýt này đi đến trung tâm thành phố. "
                            "Trong bài đọc, bạn sẽ thấy từ 'route' khi nhân vật tìm hiểu tuyến xe buýt.\n\n"

                            "Bây giờ, hãy bắt đầu học từ vựng qua flashcards nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Đi xe buýt (Phần 1)",
                    "description": "Học 6 từ: bus, stop, ticket, driver, passenger, route",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Đi xe buýt (Phần 1)",
                    "description": "Học 6 từ: bus, stop, ticket, driver, passenger, route",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Đi xe buýt (Phần 1)",
                    "description": "Học 6 từ: bus, stop, ticket, driver, passenger, route",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Đi xe buýt (Phần 1)",
                    "description": "Học 6 từ: bus, stop, ticket, driver, passenger, route",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Buổi sáng ở trạm xe buýt",
                    "description": "Hoa takes the bus to work for the first time.",
                    "data": {
                        "text": (
                            "Hoa has a new job in the city. "
                            "She takes the bus to work every morning. "
                            "The bus stop is near her house.\n\n"
                            "Today is her first day. She walks to the stop. "
                            "She sees other passengers waiting. "
                            "A big blue bus comes. It is route number seven.\n\n"
                            "Hoa gets on the bus. She buys a ticket. "
                            "The driver smiles and says, 'Good morning!' "
                            "Hoa says, 'Good morning!' back.\n\n"
                            "The bus has many passengers. "
                            "Hoa looks out the window. "
                            "She is happy. The bus ride is easy."
                        ),
                        "vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Buổi sáng ở trạm xe buýt",
                    "description": "Hoa takes the bus to work for the first time.",
                    "data": {
                        "text": (
                            "Hoa has a new job in the city. "
                            "She takes the bus to work every morning. "
                            "The bus stop is near her house.\n\n"
                            "Today is her first day. She walks to the stop. "
                            "She sees other passengers waiting. "
                            "A big blue bus comes. It is route number seven.\n\n"
                            "Hoa gets on the bus. She buys a ticket. "
                            "The driver smiles and says, 'Good morning!' "
                            "Hoa says, 'Good morning!' back.\n\n"
                            "The bus has many passengers. "
                            "Hoa looks out the window. "
                            "She is happy. The bus ride is easy."
                        ),
                        "vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Buổi sáng ở trạm xe buýt",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Hoa has a new job in the city. "
                            "She takes the bus to work every morning. "
                            "The bus stop is near her house.\n\n"
                            "Today is her first day. She walks to the stop. "
                            "She sees other passengers waiting. "
                            "A big blue bus comes. It is route number seven.\n\n"
                            "Hoa gets on the bus. She buys a ticket. "
                            "The driver smiles and says, 'Good morning!' "
                            "Hoa says, 'Good morning!' back.\n\n"
                            "The bus has many passengers. "
                            "Hoa looks out the window. "
                            "She is happy. The bus ride is easy."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Đi xe buýt (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về đi xe buýt.",
                    "data": {
                        "vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route"],
                        "items": [
                            {
                                "targetVocab": "bus",
                                "prompt": "Hãy dùng từ 'bus' để viết một câu về việc đi xe buýt. Ví dụ: I take the bus to school every morning."
                            },
                            {
                                "targetVocab": "stop",
                                "prompt": "Hãy dùng từ 'stop' để viết một câu về trạm xe buýt. Ví dụ: The bus stop is across the street from my house."
                            },
                            {
                                "targetVocab": "ticket",
                                "prompt": "Hãy dùng từ 'ticket' để viết một câu về việc mua vé. Ví dụ: A bus ticket costs five thousand dong."
                            },
                            {
                                "targetVocab": "driver",
                                "prompt": "Hãy dùng từ 'driver' để viết một câu về tài xế xe buýt. Ví dụ: The bus driver knows every stop on the route."
                            },
                            {
                                "targetVocab": "passenger",
                                "prompt": "Hãy dùng từ 'passenger' để viết một câu về hành khách. Ví dụ: The passengers wait at the stop in the rain."
                            },
                            {
                                "targetVocab": "route",
                                "prompt": "Hãy dùng từ 'route' để viết một câu về tuyến xe buýt. Ví dụ: Route number ten goes to the hospital."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 2 — Phần 2 (Words: schedule, seat, fare, transfer, station, arrive)
        # ════════════════════════════════════════════
        {
            "title": "Phần 2",
            "activities": [
                # ── introAudio: Recap + New Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng mới",
                    "description": "Ôn lại từ vựng Phần 1 và giới thiệu 6 từ mới về đi xe buýt.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong Phần 1, bạn đã học 6 từ rất hữu ích: "
                            "bus (xe buýt), stop (trạm), ticket (vé), driver (tài xế), passenger (hành khách), và route (tuyến đường). "
                            "Bạn còn nhớ không? Tuyệt vời!\n\n"
                            "Hôm nay chúng ta sẽ học thêm 6 từ mới. Những từ này giúp bạn đọc lịch trình, "
                            "tìm chỗ ngồi, và đổi xe buýt một cách dễ dàng. "
                            "Sáu từ mới là: schedule, seat, fare, transfer, station, và arrive.\n\n"

                            "Từ đầu tiên là 'schedule'. Schedule là danh từ, nghĩa là 'lịch trình' hoặc 'thời gian biểu'. "
                            "Ví dụ: 'The bus schedule says the next bus comes at eight.' — Lịch trình xe buýt nói xe tiếp theo đến lúc tám giờ. "
                            "Trong bài đọc, bạn sẽ thấy từ 'schedule' khi nhân vật xem giờ xe chạy.\n\n"

                            "Từ thứ hai là 'seat'. Seat là danh từ, nghĩa là 'ghế ngồi' hoặc 'chỗ ngồi'. "
                            "Ví dụ: 'Is this seat taken?' — Chỗ này có ai ngồi chưa? "
                            "Trong bài đọc, từ 'seat' xuất hiện khi nhân vật tìm chỗ ngồi trên xe.\n\n"

                            "Từ thứ ba là 'fare'. Fare là danh từ, nghĩa là 'giá vé' hoặc 'tiền xe'. "
                            "Ví dụ: 'The bus fare is seven thousand dong.' — Giá vé xe buýt là bảy nghìn đồng. "
                            "Trong bài đọc, bạn sẽ thấy từ 'fare' khi nhân vật trả tiền xe.\n\n"

                            "Từ thứ tư là 'transfer'. Transfer là động từ, nghĩa là 'chuyển' hoặc 'đổi xe'. "
                            "Ví dụ: 'You need to transfer to bus number three.' — Bạn cần đổi sang xe buýt số ba. "
                            "Trong bài đọc, từ 'transfer' xuất hiện khi nhân vật phải đổi xe để đến nơi.\n\n"

                            "Từ thứ năm là 'station'. Station là danh từ, nghĩa là 'bến xe' hoặc 'nhà ga'. "
                            "Ví dụ: 'The bus station is in the center of the city.' — Bến xe ở trung tâm thành phố. "
                            "Trong bài đọc, 'station' là nơi nhân vật đổi xe buýt.\n\n"

                            "Từ cuối cùng là 'arrive'. Arrive là động từ, nghĩa là 'đến nơi'. "
                            "Ví dụ: 'The bus arrives at nine o'clock.' — Xe buýt đến lúc chín giờ. "
                            "Trong bài đọc, bạn sẽ thấy từ 'arrive' khi nhân vật đến nơi cần đến.\n\n"

                            "Hãy bắt đầu với flashcards để ghi nhớ 6 từ mới này nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Đi xe buýt (Phần 2)",
                    "description": "Học 6 từ: schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Đi xe buýt (Phần 2)",
                    "description": "Học 6 từ: schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Đi xe buýt (Phần 2)",
                    "description": "Học 6 từ: schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Đi xe buýt (Phần 2)",
                    "description": "Học 6 từ: schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Đổi xe buýt",
                    "description": "Tuan rides the bus across the city and learns to transfer.",
                    "data": {
                        "text": (
                            "Tuan wants to visit his friend across the city. "
                            "He goes to the bus station near his house. "
                            "He looks at the schedule on the wall.\n\n"
                            "The next bus arrives at ten o'clock. "
                            "Tuan waits. The bus comes on time. "
                            "He gets on and pays the fare.\n\n"
                            "The bus is full. There is one empty seat. "
                            "Tuan sits down. He rides for twenty minutes.\n\n"
                            "The driver says, 'Last stop!' "
                            "Tuan needs to transfer to another bus. "
                            "He walks to the station and waits. "
                            "Bus number twelve arrives. "
                            "Tuan gets on. He is almost there."
                        ),
                        "vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Đổi xe buýt",
                    "description": "Tuan rides the bus across the city and learns to transfer.",
                    "data": {
                        "text": (
                            "Tuan wants to visit his friend across the city. "
                            "He goes to the bus station near his house. "
                            "He looks at the schedule on the wall.\n\n"
                            "The next bus arrives at ten o'clock. "
                            "Tuan waits. The bus comes on time. "
                            "He gets on and pays the fare.\n\n"
                            "The bus is full. There is one empty seat. "
                            "Tuan sits down. He rides for twenty minutes.\n\n"
                            "The driver says, 'Last stop!' "
                            "Tuan needs to transfer to another bus. "
                            "He walks to the station and waits. "
                            "Bus number twelve arrives. "
                            "Tuan gets on. He is almost there."
                        ),
                        "vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Đổi xe buýt",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Tuan wants to visit his friend across the city. "
                            "He goes to the bus station near his house. "
                            "He looks at the schedule on the wall.\n\n"
                            "The next bus arrives at ten o'clock. "
                            "Tuan waits. The bus comes on time. "
                            "He gets on and pays the fare.\n\n"
                            "The bus is full. There is one empty seat. "
                            "Tuan sits down. He rides for twenty minutes.\n\n"
                            "The driver says, 'Last stop!' "
                            "Tuan needs to transfer to another bus. "
                            "He walks to the station and waits. "
                            "Bus number twelve arrives. "
                            "Tuan gets on. He is almost there."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Đi xe buýt (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng mới về đi xe buýt.",
                    "data": {
                        "vocabList": ["schedule", "seat", "fare", "transfer", "station", "arrive"],
                        "items": [
                            {
                                "targetVocab": "schedule",
                                "prompt": "Hãy dùng từ 'schedule' để viết một câu về lịch trình xe buýt. Ví dụ: I check the bus schedule before I leave home."
                            },
                            {
                                "targetVocab": "seat",
                                "prompt": "Hãy dùng từ 'seat' để viết một câu về chỗ ngồi trên xe buýt. Ví dụ: I always give my seat to old people on the bus."
                            },
                            {
                                "targetVocab": "fare",
                                "prompt": "Hãy dùng từ 'fare' để viết một câu về giá vé xe buýt. Ví dụ: The bus fare in my city is very cheap."
                            },
                            {
                                "targetVocab": "transfer",
                                "prompt": "Hãy dùng từ 'transfer' để viết một câu về việc đổi xe buýt. Ví dụ: I transfer to bus number five at the main station."
                            },
                            {
                                "targetVocab": "station",
                                "prompt": "Hãy dùng từ 'station' để viết một câu về bến xe. Ví dụ: The bus station is next to the big supermarket."
                            },
                            {
                                "targetVocab": "arrive",
                                "prompt": "Hãy dùng từ 'arrive' để viết một câu về việc đến nơi. Ví dụ: The bus arrives at my stop at seven thirty."
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
                            "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về đi xe buýt. Thật tuyệt vời!\n\n"
                            "Trong Phần 1, bạn đã học: bus (xe buýt), stop (trạm), ticket (vé), "
                            "driver (tài xế), passenger (hành khách), và route (tuyến đường). "
                            "Bạn đã đọc về Hoa đi xe buýt đến chỗ làm mới.\n\n"
                            "Trong Phần 2, bạn đã học: schedule (lịch trình), seat (chỗ ngồi), "
                            "fare (giá vé), transfer (đổi xe), station (bến xe), và arrive (đến nơi). "
                            "Bạn đã đọc về Tuấn đổi xe buýt để đến nhà bạn.\n\n"
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
                    "title": "Flashcards: Ôn tập đi xe buýt",
                    "description": "Ôn tập 12 từ: bus, stop, ticket, driver, passenger, route, schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── speakFlashcards (all 12) ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập đi xe buýt",
                    "description": "Ôn tập 12 từ: bus, stop, ticket, driver, passenger, route, schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── vocabLevel1 (all 12) ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập đi xe buýt",
                    "description": "Ôn tập 12 từ: bus, stop, ticket, driver, passenger, route, schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── vocabLevel2 (all 12) ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập đi xe buýt",
                    "description": "Ôn tập 12 từ: bus, stop, ticket, driver, passenger, route, schedule, seat, fare, transfer, station, arrive",
                    "data": {"vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"]}
                },
                # ── writingSentence (all 12) ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập đi xe buýt",
                    "description": "Viết câu sử dụng tất cả 12 từ vựng về đi xe buýt.",
                    "data": {
                        "vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"],
                        "items": [
                            {
                                "targetVocab": "bus",
                                "prompt": "Hãy dùng từ 'bus' để viết một câu về phương tiện giao thông yêu thích. Ví dụ: The bus is the cheapest way to travel in the city."
                            },
                            {
                                "targetVocab": "stop",
                                "prompt": "Hãy dùng từ 'stop' để viết một câu về trạm xe buýt gần nhà bạn. Ví dụ: There is a bus stop right in front of my school."
                            },
                            {
                                "targetVocab": "ticket",
                                "prompt": "Hãy dùng từ 'ticket' để viết một câu về việc mua vé xe. Ví dụ: You can buy a ticket from the driver when you get on."
                            },
                            {
                                "targetVocab": "driver",
                                "prompt": "Hãy dùng từ 'driver' để viết một câu về tài xế bạn gặp. Ví dụ: The driver always waits for late passengers."
                            },
                            {
                                "targetVocab": "passenger",
                                "prompt": "Hãy dùng từ 'passenger' để viết một câu về hành khách trên xe. Ví dụ: Every passenger must have a ticket on the bus."
                            },
                            {
                                "targetVocab": "route",
                                "prompt": "Hãy dùng từ 'route' để viết một câu về tuyến xe bạn hay đi. Ví dụ: My favorite route passes through the park."
                            },
                            {
                                "targetVocab": "schedule",
                                "prompt": "Hãy dùng từ 'schedule' để viết một câu về giờ xe chạy. Ví dụ: The schedule changes on weekends and holidays."
                            },
                            {
                                "targetVocab": "seat",
                                "prompt": "Hãy dùng từ 'seat' để viết một câu về chỗ ngồi. Ví dụ: The front seat on the bus has the best view."
                            },
                            {
                                "targetVocab": "fare",
                                "prompt": "Hãy dùng từ 'fare' để viết một câu về giá vé. Ví dụ: Students pay a lower fare than adults."
                            },
                            {
                                "targetVocab": "transfer",
                                "prompt": "Hãy dùng từ 'transfer' để viết một câu về việc đổi xe. Ví dụ: I transfer at the central station to get to the airport."
                            },
                            {
                                "targetVocab": "station",
                                "prompt": "Hãy dùng từ 'station' để viết một câu về bến xe. Ví dụ: The new bus station has a waiting room with air conditioning."
                            },
                            {
                                "targetVocab": "arrive",
                                "prompt": "Hãy dùng từ 'arrive' để viết một câu về việc đến nơi. Ví dụ: I always arrive at work on time when I take the bus."
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
                            "Chào mừng bạn đến với phần cuối cùng của bài học 'Đi Xe Buýt'!\n\n"
                            "Bạn đã học 12 từ vựng quan trọng: bus, stop, ticket, driver, passenger, route, "
                            "schedule, seat, fare, transfer, station, và arrive. "
                            "Trong Phần 1, bạn đọc về Hoa đi xe buýt đến chỗ làm mới. "
                            "Trong Phần 2, bạn đọc về Tuấn đổi xe buýt để đến nhà bạn.\n\n"
                            "Bây giờ, bạn sẽ đọc một bài đọc dài hơn. Bài đọc này kết hợp tất cả 12 từ vựng "
                            "trong một câu chuyện về một chuyến đi xe buýt. Hãy chú ý cách mỗi từ được sử dụng trong ngữ cảnh thực tế.\n\n"
                            "Hãy đọc chậm, tận hưởng câu chuyện, và nhận ra những từ bạn đã học. Bạn sẽ ngạc nhiên "
                            "vì mình hiểu được nhiều hơn bạn nghĩ đấy!"
                        )
                    }
                },
                # ── reading: Full article ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Chuyến đi xe buýt qua thành phố",
                    "description": "A full story about a bus journey across the city using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "It is Sunday morning. Hoa and Tuan want to go to the park across the city. "
                            "They decide to take the bus. It is cheap and easy.\n\n"
                            "They walk to the bus stop near Hoa's house. "
                            "Tuan looks at the schedule on the sign. "
                            "The next bus arrives at nine fifteen. They wait for five minutes.\n\n"
                            "A green bus comes. It is route number three. "
                            "Hoa and Tuan get on the bus. "
                            "Hoa buys two tickets. The fare is six thousand dong each. "
                            "The driver takes the money and gives them the tickets.\n\n"
                            "The bus has many passengers this morning. "
                            "Hoa finds an empty seat near the window. "
                            "Tuan stands because there are no more seats. "
                            "An old woman gets on at the next stop. "
                            "Hoa gives her seat to the woman. The woman smiles and says thank you.\n\n"
                            "After fifteen minutes, the driver says, 'Central station!' "
                            "Hoa and Tuan need to transfer here. "
                            "They get off and walk to the station. "
                            "They look at the schedule for route number eight.\n\n"
                            "Bus number eight arrives in three minutes. "
                            "They get on. This bus has more empty seats. "
                            "Tuan sits by the window. He watches the city go by.\n\n"
                            "After ten more minutes, the bus arrives at the park. "
                            "Hoa and Tuan get off. The park is big and green. "
                            "Hoa says, 'That was easy! The bus is great.' "
                            "Tuan says, 'Yes, and the fare is so cheap.' "
                            "They both laugh and walk into the park."
                        ),
                        "vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chuyến đi xe buýt qua thành phố",
                    "description": "A full story about a bus journey across the city using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "It is Sunday morning. Hoa and Tuan want to go to the park across the city. "
                            "They decide to take the bus. It is cheap and easy.\n\n"
                            "They walk to the bus stop near Hoa's house. "
                            "Tuan looks at the schedule on the sign. "
                            "The next bus arrives at nine fifteen. They wait for five minutes.\n\n"
                            "A green bus comes. It is route number three. "
                            "Hoa and Tuan get on the bus. "
                            "Hoa buys two tickets. The fare is six thousand dong each. "
                            "The driver takes the money and gives them the tickets.\n\n"
                            "The bus has many passengers this morning. "
                            "Hoa finds an empty seat near the window. "
                            "Tuan stands because there are no more seats. "
                            "An old woman gets on at the next stop. "
                            "Hoa gives her seat to the woman. The woman smiles and says thank you.\n\n"
                            "After fifteen minutes, the driver says, 'Central station!' "
                            "Hoa and Tuan need to transfer here. "
                            "They get off and walk to the station. "
                            "They look at the schedule for route number eight.\n\n"
                            "Bus number eight arrives in three minutes. "
                            "They get on. This bus has more empty seats. "
                            "Tuan sits by the window. He watches the city go by.\n\n"
                            "After ten more minutes, the bus arrives at the park. "
                            "Hoa and Tuan get off. The park is big and green. "
                            "Hoa says, 'That was easy! The bus is great.' "
                            "Tuan says, 'Yes, and the fare is so cheap.' "
                            "They both laugh and walk into the park."
                        ),
                        "vocabList": ["bus", "stop", "ticket", "driver", "passenger", "route", "schedule", "seat", "fare", "transfer", "station", "arrive"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chuyến đi xe buýt qua thành phố",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "It is Sunday morning. Hoa and Tuan want to go to the park across the city. "
                            "They decide to take the bus. It is cheap and easy.\n\n"
                            "They walk to the bus stop near Hoa's house. "
                            "Tuan looks at the schedule on the sign. "
                            "The next bus arrives at nine fifteen. They wait for five minutes.\n\n"
                            "A green bus comes. It is route number three. "
                            "Hoa and Tuan get on the bus. "
                            "Hoa buys two tickets. The fare is six thousand dong each. "
                            "The driver takes the money and gives them the tickets.\n\n"
                            "The bus has many passengers this morning. "
                            "Hoa finds an empty seat near the window. "
                            "Tuan stands because there are no more seats. "
                            "An old woman gets on at the next stop. "
                            "Hoa gives her seat to the woman. The woman smiles and says thank you.\n\n"
                            "After fifteen minutes, the driver says, 'Central station!' "
                            "Hoa and Tuan need to transfer here. "
                            "They get off and walk to the station. "
                            "They look at the schedule for route number eight.\n\n"
                            "Bus number eight arrives in three minutes. "
                            "They get on. This bus has more empty seats. "
                            "Tuan sits by the window. He watches the city go by.\n\n"
                            "After ten more minutes, the bus arrives at the park. "
                            "Hoa and Tuan get off. The park is big and green. "
                            "Hoa says, 'That was easy! The bus is great.' "
                            "Tuan says, 'Yes, and the fare is so cheap.' "
                            "They both laugh and walk into the park."
                        )
                    }
                },
                # ── introAudio: Farewell (introspective_guide tone) ──
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay đầy suy ngẫm.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học 'Đi Xe Buýt'. "
                            "Hãy dừng lại một chút và nhìn lại hành trình bạn vừa đi qua.\n\n"

                            "Từ 'bus' nghĩa là xe buýt — phương tiện đưa bạn đi khắp nơi. "
                            "Hãy nghĩ xem: 'I take the bus to the library on Saturdays.' — "
                            "Tôi đi xe buýt đến thư viện vào thứ Bảy. "
                            "Mỗi chuyến xe buýt là một cơ hội để khám phá.\n\n"

                            "Từ 'route' nghĩa là tuyến đường. "
                            "Hãy nghĩ xem: 'The longest route in the city passes through twelve stops.' — "
                            "Tuyến đường dài nhất trong thành phố đi qua mười hai trạm. "
                            "Biết tuyến đường giúp bạn không bao giờ bị lạc.\n\n"

                            "Từ 'fare' nghĩa là giá vé. "
                            "Hãy nghĩ xem: 'The fare for children is half the adult price.' — "
                            "Giá vé cho trẻ em bằng nửa giá người lớn. "
                            "Một từ nhỏ nhưng rất cần thiết mỗi ngày.\n\n"

                            "Từ 'transfer' nghĩa là đổi xe. "
                            "Hãy nghĩ xem: 'I transfer at the hospital to get to the university.' — "
                            "Tôi đổi xe ở bệnh viện để đến trường đại học. "
                            "Biết cách đổi xe mở ra cả thành phố cho bạn.\n\n"

                            "Từ 'passenger' nghĩa là hành khách. "
                            "Hãy nghĩ xem: 'A kind passenger helped me find the right stop.' — "
                            "Một hành khách tốt bụng đã giúp tôi tìm đúng trạm. "
                            "Trên xe buýt, bạn không bao giờ đi một mình.\n\n"

                            "Từ 'arrive' nghĩa là đến nơi. "
                            "Hãy nghĩ xem: 'We arrive at the beach just before sunset.' — "
                            "Chúng tôi đến bãi biển ngay trước khi mặt trời lặn. "
                            "Đến nơi — đó là phần thưởng của mỗi chuyến đi.\n\n"

                            "Bạn đã học 12 từ vựng về giao thông công cộng. "
                            "Nhưng hơn cả từ vựng, bạn đã học được cách tự tin di chuyển. "
                            "Lần tới khi bạn đứng ở trạm xe buýt, hãy tự hỏi: "
                            "'Mình có thể nói gì bằng tiếng Anh?' "
                            "Câu trả lời sẽ nhiều hơn bạn tưởng.\n\n"

                            "Hãy nhớ: mỗi chuyến đi là một bài học. "
                            "Cảm ơn bạn đã học cùng mình. Hẹn gặp lại ở bài học tiếp theo."
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
