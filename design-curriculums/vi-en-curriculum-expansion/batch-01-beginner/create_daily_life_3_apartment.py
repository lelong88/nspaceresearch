"""
Create curriculum: Finding an Apartment (Tìm Nhà Trọ — Bước Đầu Tiên)
Level: beginner | Skill focus: balanced_skills | Content type: []
Topic: Daily life | 12 words (2 groups of 6) | 4 sessions | Bilingual (vi/en)
Tone: surprising_fact | Farewell tone: practical_momentum
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
# Group 1 (Session 1): rent, apartment, landlord, deposit, furniture, bedroom
# Group 2 (Session 2): bathroom, kitchen, neighbor, lease, utility, move

W1 = ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]
W2 = ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]
ALL_WORDS = W1 + W2

content = {
    "title": "Tìm Nhà Trọ — Bước Đầu Tiên",
    "contentTypeTags": [],
    "description": (
        "NGƯỜI VIỆT NAM TRẺ TRUNG BÌNH CHUYỂN NHÀ 5 LẦN TRƯỚC TUỔI 30 — NHƯNG CHƯA BAO GIỜ HỌC CÁCH NÓI VỀ VIỆC ĐÓ BẰNG TIẾNG ANH.\n\n"
        "Bạn muốn hỏi giá thuê phòng. Bạn muốn nói \"tiền cọc bao nhiêu?\" Bạn muốn hỏi về nội thất, "
        "về phòng ngủ, về hợp đồng — nhưng mỗi từ đều biến mất khi bạn đứng trước chủ nhà người nước ngoài.\n\n"
        "Tìm nhà bằng tiếng Anh giống như đi vào một căn phòng tối — "
        "bạn biết mình cần gì, nhưng không thể gọi tên bất cứ thứ gì xung quanh. "
        "12 từ vựng trong bài học này chính là chiếc đèn pin soi sáng con đường đó.\n\n"
        "Sau bài học, bạn sẽ tự tin hỏi giá thuê, thương lượng hợp đồng, và mô tả căn phòng mơ ước "
        "bằng tiếng Anh — dù ở Việt Nam hay bất kỳ đâu trên thế giới.\n\n"
        "Vừa học từ vựng thực tế, vừa nâng cấp khả năng giao tiếp — "
        "mỗi từ là một bước gần hơn đến ngôi nhà mới của bạn."
    ),
    "preview": {
        "text": (
            "You walk into a new apartment. The rooms are empty. The landlord is waiting. "
            "You want to ask: 'How much is the rent?' You want to say: 'Is the deposit refundable?' "
            "But the words don't come. This curriculum gives you 12 essential housing words — "
            "rent, apartment, landlord, deposit, furniture, bedroom, bathroom, kitchen, neighbor, lease, utility, and move. "
            "Across four sessions, you will learn each word through flashcards, reading passages about real apartment-hunting situations, "
            "and guided writing exercises. By the end, you will confidently ask about rent, discuss lease terms, "
            "and describe your living space in English — whether renting in Vietnam or abroad."
        )
    },
    "learningSessions": [
        # ════════════════════════════════════════════
        # SESSION 1 — Phần 1 (Words: rent, apartment, landlord, deposit, furniture, bedroom)
        # ════════════════════════════════════════════
        {
            "title": "Phần 1",
            "activities": [
                # ── introAudio: Welcome + Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về tìm nhà trọ bằng tiếng Anh.",
                    "data": {
                        "text": (
                            "Xin chào và chào mừng bạn đến với bài học 'Tìm Nhà Trọ'! "
                            "Hôm nay chúng ta sẽ học 6 từ vựng tiếng Anh rất quan trọng khi bạn tìm nhà ở. "
                            "Những từ này sẽ giúp bạn tự tin hơn khi nói chuyện với chủ nhà, hỏi giá thuê, và hiểu hợp đồng. "
                            "Sáu từ hôm nay là: rent, apartment, landlord, deposit, furniture, và bedroom.\n\n"

                            "Từ đầu tiên là 'rent'. Rent có thể là danh từ hoặc động từ. "
                            "Là danh từ, nó nghĩa là 'tiền thuê nhà'. Là động từ, nó nghĩa là 'thuê'. "
                            "Ví dụ: 'The rent is three hundred dollars a month.' — Tiền thuê nhà là ba trăm đô la một tháng. "
                            "Trong bài đọc, bạn sẽ thấy từ 'rent' khi nhân vật hỏi giá thuê phòng.\n\n"

                            "Từ thứ hai là 'apartment'. Apartment là danh từ, nghĩa là 'căn hộ' hoặc 'phòng trọ'. "
                            "Ví dụ: 'I live in a small apartment near the school.' — Tôi sống trong một căn hộ nhỏ gần trường. "
                            "Trong bài đọc, từ 'apartment' xuất hiện khi nhân vật đi xem phòng mới.\n\n"

                            "Từ thứ ba là 'landlord'. Landlord là danh từ, nghĩa là 'chủ nhà' hoặc 'người cho thuê'. "
                            "Ví dụ: 'The landlord is very friendly.' — Chủ nhà rất thân thiện. "
                            "Trong bài đọc, bạn sẽ thấy từ 'landlord' khi nhân vật gặp người cho thuê phòng.\n\n"

                            "Từ thứ tư là 'deposit'. Deposit là danh từ, nghĩa là 'tiền cọc' hoặc 'tiền đặt cọc'. "
                            "Ví dụ: 'You need to pay a deposit before you move in.' — Bạn cần trả tiền cọc trước khi dọn vào. "
                            "Trong bài đọc, 'deposit' xuất hiện khi nhân vật hỏi về tiền cọc.\n\n"

                            "Từ thứ năm là 'furniture'. Furniture là danh từ, nghĩa là 'nội thất' hoặc 'đồ đạc'. "
                            "Ví dụ: 'The apartment has new furniture.' — Căn hộ có nội thất mới. "
                            "Trong bài đọc, bạn sẽ thấy từ 'furniture' khi nhân vật xem đồ đạc trong phòng.\n\n"

                            "Từ cuối cùng là 'bedroom'. Bedroom là danh từ, nghĩa là 'phòng ngủ'. "
                            "Ví dụ: 'This apartment has two bedrooms.' — Căn hộ này có hai phòng ngủ. "
                            "Trong bài đọc, từ 'bedroom' xuất hiện khi nhân vật xem phòng ngủ trong căn hộ.\n\n"

                            "Bây giờ, hãy bắt đầu học từ vựng qua flashcards nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tìm nhà (Phần 1)",
                    "description": "Học 6 từ: rent, apartment, landlord, deposit, furniture, bedroom",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tìm nhà (Phần 1)",
                    "description": "Học 6 từ: rent, apartment, landlord, deposit, furniture, bedroom",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tìm nhà (Phần 1)",
                    "description": "Học 6 từ: rent, apartment, landlord, deposit, furniture, bedroom",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tìm nhà (Phần 1)",
                    "description": "Học 6 từ: rent, apartment, landlord, deposit, furniture, bedroom",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Đi xem phòng trọ",
                    "description": "Hoa visits an apartment and talks to the landlord.",
                    "data": {
                        "text": (
                            "Hoa needs a new place to live. "
                            "She finds an apartment near her office. "
                            "She calls the landlord to see the room.\n\n"
                            "The landlord opens the door. "
                            "The apartment is small but clean. "
                            "It has one bedroom with a big window.\n\n"
                            "Hoa looks at the furniture. "
                            "There is a bed, a desk, and a chair. "
                            "She likes the bedroom. It is bright.\n\n"
                            "Hoa asks, 'How much is the rent?' "
                            "The landlord says, 'Three million dong a month.' "
                            "Hoa asks about the deposit. "
                            "The landlord says, 'One month deposit.' "
                            "Hoa thinks the rent is good."
                        ),
                        "vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Đi xem phòng trọ",
                    "description": "Hoa visits an apartment and talks to the landlord.",
                    "data": {
                        "text": (
                            "Hoa needs a new place to live. "
                            "She finds an apartment near her office. "
                            "She calls the landlord to see the room.\n\n"
                            "The landlord opens the door. "
                            "The apartment is small but clean. "
                            "It has one bedroom with a big window.\n\n"
                            "Hoa looks at the furniture. "
                            "There is a bed, a desk, and a chair. "
                            "She likes the bedroom. It is bright.\n\n"
                            "Hoa asks, 'How much is the rent?' "
                            "The landlord says, 'Three million dong a month.' "
                            "Hoa asks about the deposit. "
                            "The landlord says, 'One month deposit.' "
                            "Hoa thinks the rent is good."
                        ),
                        "vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Đi xem phòng trọ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Hoa needs a new place to live. "
                            "She finds an apartment near her office. "
                            "She calls the landlord to see the room.\n\n"
                            "The landlord opens the door. "
                            "The apartment is small but clean. "
                            "It has one bedroom with a big window.\n\n"
                            "Hoa looks at the furniture. "
                            "There is a bed, a desk, and a chair. "
                            "She likes the bedroom. It is bright.\n\n"
                            "Hoa asks, 'How much is the rent?' "
                            "The landlord says, 'Three million dong a month.' "
                            "Hoa asks about the deposit. "
                            "The landlord says, 'One month deposit.' "
                            "Hoa thinks the rent is good."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tìm nhà (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về tìm nhà.",
                    "data": {
                        "vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom"],
                        "items": [
                            {
                                "targetVocab": "rent",
                                "prompt": "Hãy dùng từ 'rent' để viết một câu về tiền thuê nhà. Ví dụ: The rent for this room is two hundred dollars a month."
                            },
                            {
                                "targetVocab": "apartment",
                                "prompt": "Hãy dùng từ 'apartment' để viết một câu về nơi bạn sống. Ví dụ: My apartment is on the third floor of a tall building."
                            },
                            {
                                "targetVocab": "landlord",
                                "prompt": "Hãy dùng từ 'landlord' để viết một câu về chủ nhà. Ví dụ: The landlord fixes the broken door every time."
                            },
                            {
                                "targetVocab": "deposit",
                                "prompt": "Hãy dùng từ 'deposit' để viết một câu về tiền cọc. Ví dụ: I paid a deposit of one month before I moved in."
                            },
                            {
                                "targetVocab": "furniture",
                                "prompt": "Hãy dùng từ 'furniture' để viết một câu về đồ đạc trong nhà. Ví dụ: The furniture in my room is old but comfortable."
                            },
                            {
                                "targetVocab": "bedroom",
                                "prompt": "Hãy dùng từ 'bedroom' để viết một câu về phòng ngủ. Ví dụ: My bedroom has a window that faces the park."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 2 — Phần 2 (Words: bathroom, kitchen, neighbor, lease, utility, move)
        # ════════════════════════════════════════════
        {
            "title": "Phần 2",
            "activities": [
                # ── introAudio: Recap + New Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng mới",
                    "description": "Ôn lại từ vựng Phần 1 và giới thiệu 6 từ mới về nhà ở.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong Phần 1, bạn đã học 6 từ rất hữu ích: "
                            "rent (tiền thuê), apartment (căn hộ), landlord (chủ nhà), deposit (tiền cọc), "
                            "furniture (nội thất), và bedroom (phòng ngủ). "
                            "Bạn còn nhớ không? Tuyệt vời!\n\n"
                            "Hôm nay chúng ta sẽ học thêm 6 từ mới. Những từ này giúp bạn mô tả căn nhà, "
                            "hiểu hợp đồng thuê, và nói về việc chuyển nhà. "
                            "Sáu từ mới là: bathroom, kitchen, neighbor, lease, utility, và move.\n\n"

                            "Từ đầu tiên là 'bathroom'. Bathroom là danh từ, nghĩa là 'phòng tắm'. "
                            "Ví dụ: 'The bathroom is next to the bedroom.' — Phòng tắm ở cạnh phòng ngủ. "
                            "Trong bài đọc, bạn sẽ thấy từ 'bathroom' khi nhân vật xem phòng tắm trong căn hộ mới.\n\n"

                            "Từ thứ hai là 'kitchen'. Kitchen là danh từ, nghĩa là 'nhà bếp' hoặc 'phòng bếp'. "
                            "Ví dụ: 'I cook dinner in the kitchen every evening.' — Tôi nấu cơm tối trong bếp mỗi buổi chiều. "
                            "Trong bài đọc, từ 'kitchen' xuất hiện khi nhân vật kiểm tra nhà bếp.\n\n"

                            "Từ thứ ba là 'neighbor'. Neighbor là danh từ, nghĩa là 'hàng xóm' hoặc 'người láng giềng'. "
                            "Ví dụ: 'My neighbor is very quiet and kind.' — Hàng xóm của tôi rất yên tĩnh và tốt bụng. "
                            "Trong bài đọc, bạn sẽ thấy từ 'neighbor' khi nhân vật gặp hàng xóm mới.\n\n"

                            "Từ thứ tư là 'lease'. Lease là danh từ, nghĩa là 'hợp đồng thuê nhà'. "
                            "Ví dụ: 'The lease is for one year.' — Hợp đồng thuê là một năm. "
                            "Trong bài đọc, 'lease' xuất hiện khi nhân vật ký hợp đồng thuê phòng.\n\n"

                            "Từ thứ năm là 'utility'. Utility là danh từ, nghĩa là 'tiện ích' hoặc 'chi phí điện nước'. "
                            "Ví dụ: 'The utility bill is fifty dollars a month.' — Hóa đơn điện nước là năm mươi đô la một tháng. "
                            "Trong bài đọc, bạn sẽ thấy từ 'utility' khi nhân vật hỏi về chi phí điện nước.\n\n"

                            "Từ cuối cùng là 'move'. Move là động từ, nghĩa là 'chuyển nhà' hoặc 'di chuyển'. "
                            "Ví dụ: 'I will move to the new apartment next week.' — Tôi sẽ chuyển đến căn hộ mới tuần sau. "
                            "Trong bài đọc, từ 'move' xuất hiện khi nhân vật quyết định chuyển vào ở.\n\n"

                            "Hãy bắt đầu với flashcards để ghi nhớ 6 từ mới này nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tìm nhà (Phần 2)",
                    "description": "Học 6 từ: bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tìm nhà (Phần 2)",
                    "description": "Học 6 từ: bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tìm nhà (Phần 2)",
                    "description": "Học 6 từ: bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tìm nhà (Phần 2)",
                    "description": "Học 6 từ: bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Chuyển vào nhà mới",
                    "description": "Tùng signs a lease and moves into his new apartment.",
                    "data": {
                        "text": (
                            "Tùng finds a nice apartment. "
                            "He likes the kitchen. It is big and clean. "
                            "The bathroom has hot water. That is important.\n\n"
                            "Tùng reads the lease carefully. "
                            "The lease says he must stay for one year. "
                            "The utility bill is not included in the rent.\n\n"
                            "Tùng signs the lease. He is happy. "
                            "He will move in on Saturday. "
                            "His friends help him carry boxes.\n\n"
                            "On the first day, a neighbor says hello. "
                            "The neighbor lives next door. "
                            "She says, 'Welcome to the building!' "
                            "Tùng smiles. He likes his new home."
                        ),
                        "vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chuyển vào nhà mới",
                    "description": "Tùng signs a lease and moves into his new apartment.",
                    "data": {
                        "text": (
                            "Tùng finds a nice apartment. "
                            "He likes the kitchen. It is big and clean. "
                            "The bathroom has hot water. That is important.\n\n"
                            "Tùng reads the lease carefully. "
                            "The lease says he must stay for one year. "
                            "The utility bill is not included in the rent.\n\n"
                            "Tùng signs the lease. He is happy. "
                            "He will move in on Saturday. "
                            "His friends help him carry boxes.\n\n"
                            "On the first day, a neighbor says hello. "
                            "The neighbor lives next door. "
                            "She says, 'Welcome to the building!' "
                            "Tùng smiles. He likes his new home."
                        ),
                        "vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chuyển vào nhà mới",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Tùng finds a nice apartment. "
                            "He likes the kitchen. It is big and clean. "
                            "The bathroom has hot water. That is important.\n\n"
                            "Tùng reads the lease carefully. "
                            "The lease says he must stay for one year. "
                            "The utility bill is not included in the rent.\n\n"
                            "Tùng signs the lease. He is happy. "
                            "He will move in on Saturday. "
                            "His friends help him carry boxes.\n\n"
                            "On the first day, a neighbor says hello. "
                            "The neighbor lives next door. "
                            "She says, 'Welcome to the building!' "
                            "Tùng smiles. He likes his new home."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tìm nhà (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng mới về nhà ở.",
                    "data": {
                        "vocabList": ["bathroom", "kitchen", "neighbor", "lease", "utility", "move"],
                        "items": [
                            {
                                "targetVocab": "bathroom",
                                "prompt": "Hãy dùng từ 'bathroom' để viết một câu về phòng tắm. Ví dụ: The bathroom in my apartment is small but very clean."
                            },
                            {
                                "targetVocab": "kitchen",
                                "prompt": "Hãy dùng từ 'kitchen' để viết một câu về nhà bếp. Ví dụ: I like to cook breakfast in the kitchen every morning."
                            },
                            {
                                "targetVocab": "neighbor",
                                "prompt": "Hãy dùng từ 'neighbor' để viết một câu về hàng xóm. Ví dụ: My neighbor always says good morning to me."
                            },
                            {
                                "targetVocab": "lease",
                                "prompt": "Hãy dùng từ 'lease' để viết một câu về hợp đồng thuê nhà. Ví dụ: I signed a lease for six months."
                            },
                            {
                                "targetVocab": "utility",
                                "prompt": "Hãy dùng từ 'utility' để viết một câu về chi phí điện nước. Ví dụ: The utility bill goes up in the summer because of the air conditioner."
                            },
                            {
                                "targetVocab": "move",
                                "prompt": "Hãy dùng từ 'move' để viết một câu về việc chuyển nhà. Ví dụ: We will move to a bigger apartment next month."
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
                            "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về tìm nhà trọ. Thật tuyệt vời!\n\n"
                            "Trong Phần 1, bạn đã học: rent (tiền thuê), apartment (căn hộ), landlord (chủ nhà), "
                            "deposit (tiền cọc), furniture (nội thất), và bedroom (phòng ngủ). "
                            "Bạn đã đọc về Hoa đi xem phòng trọ và nói chuyện với chủ nhà.\n\n"
                            "Trong Phần 2, bạn đã học: bathroom (phòng tắm), kitchen (nhà bếp), "
                            "neighbor (hàng xóm), lease (hợp đồng thuê), utility (chi phí điện nước), và move (chuyển nhà). "
                            "Bạn đã đọc về Tùng ký hợp đồng và chuyển vào nhà mới.\n\n"
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
                    "title": "Flashcards: Ôn tập tìm nhà",
                    "description": "Học 12 từ: rent, apartment, landlord, deposit, furniture, bedroom, bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── speakFlashcards (all 12) ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tìm nhà",
                    "description": "Học 12 từ: rent, apartment, landlord, deposit, furniture, bedroom, bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── vocabLevel1 (all 12) ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tìm nhà",
                    "description": "Học 12 từ: rent, apartment, landlord, deposit, furniture, bedroom, bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── vocabLevel2 (all 12) ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tìm nhà",
                    "description": "Học 12 từ: rent, apartment, landlord, deposit, furniture, bedroom, bathroom, kitchen, neighbor, lease, utility, move",
                    "data": {"vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"]}
                },
                # ── writingSentence (all 12) ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập tìm nhà",
                    "description": "Viết câu sử dụng tất cả 12 từ vựng về tìm nhà.",
                    "data": {
                        "vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"],
                        "items": [
                            {
                                "targetVocab": "rent",
                                "prompt": "Hãy dùng từ 'rent' để viết một câu về giá thuê nhà ở thành phố. Ví dụ: The rent in the city center is higher than in the suburbs."
                            },
                            {
                                "targetVocab": "apartment",
                                "prompt": "Hãy dùng từ 'apartment' để viết một câu về căn hộ bạn thích. Ví dụ: I want an apartment with a balcony and a nice view."
                            },
                            {
                                "targetVocab": "landlord",
                                "prompt": "Hãy dùng từ 'landlord' để viết một câu về chủ nhà tốt. Ví dụ: A good landlord repairs things quickly when they break."
                            },
                            {
                                "targetVocab": "deposit",
                                "prompt": "Hãy dùng từ 'deposit' để viết một câu về việc trả tiền cọc. Ví dụ: The landlord returns the deposit when you leave the apartment clean."
                            },
                            {
                                "targetVocab": "furniture",
                                "prompt": "Hãy dùng từ 'furniture' để viết một câu về đồ đạc bạn cần. Ví dụ: I need to buy new furniture for my living room."
                            },
                            {
                                "targetVocab": "bedroom",
                                "prompt": "Hãy dùng từ 'bedroom' để viết một câu về phòng ngủ lý tưởng. Ví dụ: A quiet bedroom helps me sleep better at night."
                            },
                            {
                                "targetVocab": "bathroom",
                                "prompt": "Hãy dùng từ 'bathroom' để viết một câu về phòng tắm trong nhà. Ví dụ: This apartment has two bathrooms, one for guests."
                            },
                            {
                                "targetVocab": "kitchen",
                                "prompt": "Hãy dùng từ 'kitchen' để viết một câu về nhà bếp bạn muốn. Ví dụ: I dream of a kitchen with a big window and lots of light."
                            },
                            {
                                "targetVocab": "neighbor",
                                "prompt": "Hãy dùng từ 'neighbor' để viết một câu về hàng xóm của bạn. Ví dụ: My neighbor shares food with me on holidays."
                            },
                            {
                                "targetVocab": "lease",
                                "prompt": "Hãy dùng từ 'lease' để viết một câu về hợp đồng thuê. Ví dụ: Always read the lease before you sign it."
                            },
                            {
                                "targetVocab": "utility",
                                "prompt": "Hãy dùng từ 'utility' để viết một câu về hóa đơn điện nước. Ví dụ: The utility cost is about fifty dollars every month."
                            },
                            {
                                "targetVocab": "move",
                                "prompt": "Hãy dùng từ 'move' để viết một câu về kế hoạch chuyển nhà. Ví dụ: I plan to move closer to my workplace next year."
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
                            "Chào mừng bạn đến với phần cuối cùng của bài học 'Tìm Nhà Trọ'!\n\n"
                            "Bạn đã học 12 từ vựng quan trọng: rent, apartment, landlord, deposit, furniture, bedroom, "
                            "bathroom, kitchen, neighbor, lease, utility, và move. "
                            "Trong Phần 1, bạn đọc về Hoa đi xem phòng trọ và nói chuyện với chủ nhà. "
                            "Trong Phần 2, bạn đọc về Tùng ký hợp đồng và chuyển vào nhà mới.\n\n"
                            "Bây giờ, bạn sẽ đọc một bài đọc dài hơn. Bài đọc này kết hợp tất cả 12 từ vựng "
                            "trong một câu chuyện về việc tìm nhà. Hãy chú ý cách mỗi từ được sử dụng trong ngữ cảnh thực tế.\n\n"
                            "Hãy đọc chậm, tận hưởng câu chuyện, và nhận ra những từ bạn đã học. Bạn sẽ ngạc nhiên "
                            "vì mình hiểu được nhiều hơn bạn nghĩ đấy!"
                        )
                    }
                },
                # ── reading: Full article ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Ngôi nhà mới của Mai",
                    "description": "A full story about Mai finding and moving into a new apartment using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "Mai works at a company in the city. "
                            "She lives far from her office. Every day, she takes the bus for one hour. "
                            "She wants to find an apartment closer to work.\n\n"
                            "Mai looks online. She finds three apartments. "
                            "The first apartment is big. It has two bedrooms and a large kitchen. "
                            "But the rent is very high. Mai cannot pay that much.\n\n"
                            "The second apartment is small. It has one bedroom and a tiny bathroom. "
                            "The furniture is old. The landlord does not want to change it. "
                            "Mai does not like this one.\n\n"
                            "The third apartment is just right. It has one bedroom, a clean bathroom, "
                            "and a nice kitchen. The furniture is simple but new. "
                            "The rent is four million dong a month. Mai can pay that.\n\n"
                            "Mai meets the landlord. He is a kind old man. "
                            "He shows her the apartment. Mai asks about the deposit. "
                            "The landlord says, 'One month deposit. You get it back when you leave.'\n\n"
                            "Mai asks about the utility bill. "
                            "The landlord says, 'You pay for water and electricity yourself.' "
                            "Mai reads the lease. It is for one year. She agrees.\n\n"
                            "Mai signs the lease and pays the deposit. "
                            "She will move in next weekend. "
                            "Her brother helps her carry the boxes.\n\n"
                            "On the first morning, Mai makes coffee in her new kitchen. "
                            "A neighbor knocks on the door. "
                            "She says, 'Hello! I live next door. Welcome!' "
                            "Mai smiles. She feels at home already."
                        ),
                        "vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Ngôi nhà mới của Mai",
                    "description": "A full story about Mai finding and moving into a new apartment using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "Mai works at a company in the city. "
                            "She lives far from her office. Every day, she takes the bus for one hour. "
                            "She wants to find an apartment closer to work.\n\n"
                            "Mai looks online. She finds three apartments. "
                            "The first apartment is big. It has two bedrooms and a large kitchen. "
                            "But the rent is very high. Mai cannot pay that much.\n\n"
                            "The second apartment is small. It has one bedroom and a tiny bathroom. "
                            "The furniture is old. The landlord does not want to change it. "
                            "Mai does not like this one.\n\n"
                            "The third apartment is just right. It has one bedroom, a clean bathroom, "
                            "and a nice kitchen. The furniture is simple but new. "
                            "The rent is four million dong a month. Mai can pay that.\n\n"
                            "Mai meets the landlord. He is a kind old man. "
                            "He shows her the apartment. Mai asks about the deposit. "
                            "The landlord says, 'One month deposit. You get it back when you leave.'\n\n"
                            "Mai asks about the utility bill. "
                            "The landlord says, 'You pay for water and electricity yourself.' "
                            "Mai reads the lease. It is for one year. She agrees.\n\n"
                            "Mai signs the lease and pays the deposit. "
                            "She will move in next weekend. "
                            "Her brother helps her carry the boxes.\n\n"
                            "On the first morning, Mai makes coffee in her new kitchen. "
                            "A neighbor knocks on the door. "
                            "She says, 'Hello! I live next door. Welcome!' "
                            "Mai smiles. She feels at home already."
                        ),
                        "vocabList": ["rent", "apartment", "landlord", "deposit", "furniture", "bedroom", "bathroom", "kitchen", "neighbor", "lease", "utility", "move"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ngôi nhà mới của Mai",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Mai works at a company in the city. "
                            "She lives far from her office. Every day, she takes the bus for one hour. "
                            "She wants to find an apartment closer to work.\n\n"
                            "Mai looks online. She finds three apartments. "
                            "The first apartment is big. It has two bedrooms and a large kitchen. "
                            "But the rent is very high. Mai cannot pay that much.\n\n"
                            "The second apartment is small. It has one bedroom and a tiny bathroom. "
                            "The furniture is old. The landlord does not want to change it. "
                            "Mai does not like this one.\n\n"
                            "The third apartment is just right. It has one bedroom, a clean bathroom, "
                            "and a nice kitchen. The furniture is simple but new. "
                            "The rent is four million dong a month. Mai can pay that.\n\n"
                            "Mai meets the landlord. He is a kind old man. "
                            "He shows her the apartment. Mai asks about the deposit. "
                            "The landlord says, 'One month deposit. You get it back when you leave.'\n\n"
                            "Mai asks about the utility bill. "
                            "The landlord says, 'You pay for water and electricity yourself.' "
                            "Mai reads the lease. It is for one year. She agrees.\n\n"
                            "Mai signs the lease and pays the deposit. "
                            "She will move in next weekend. "
                            "Her brother helps her carry the boxes.\n\n"
                            "On the first morning, Mai makes coffee in her new kitchen. "
                            "A neighbor knocks on the door. "
                            "She says, 'Hello! I live next door. Welcome!' "
                            "Mai smiles. She feels at home already."
                        )
                    }
                },
                # ── introAudio: Farewell (practical_momentum tone) ──
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay với năng lượng hành động.",
                    "data": {
                        "text": (
                            "Xuất sắc! Bạn đã hoàn thành bài học 'Tìm Nhà Trọ'! "
                            "Hãy cùng ôn lại những từ quan trọng nhất — và bàn về bước tiếp theo nhé.\n\n"

                            "Từ 'rent' nghĩa là tiền thuê nhà. Khi bạn muốn hỏi giá thuê, hãy nói: "
                            "'How much is the rent per month?' — Tiền thuê mỗi tháng là bao nhiêu?\n\n"

                            "Từ 'landlord' nghĩa là chủ nhà. "
                            "Khi bạn cần liên hệ chủ nhà, hãy nói: "
                            "'I need to talk to the landlord about the broken window.' — Tôi cần nói với chủ nhà về cửa sổ bị hỏng.\n\n"

                            "Từ 'deposit' nghĩa là tiền cọc. "
                            "Khi bạn muốn hỏi về tiền cọc, hãy nói: "
                            "'Is the deposit refundable when I move out?' — Tiền cọc có được trả lại khi tôi chuyển đi không?\n\n"

                            "Từ 'lease' nghĩa là hợp đồng thuê nhà. "
                            "Khi bạn cần hỏi về hợp đồng, hãy nói: "
                            "'How long is the lease?' — Hợp đồng thuê bao lâu?\n\n"

                            "Từ 'utility' nghĩa là chi phí điện nước. "
                            "Khi bạn muốn hỏi về chi phí, hãy nói: "
                            "'Are utilities included in the rent?' — Chi phí điện nước có bao gồm trong tiền thuê không?\n\n"

                            "Từ 'neighbor' nghĩa là hàng xóm. "
                            "Khi bạn muốn chào hàng xóm, hãy nói: "
                            "'Hello, I just moved in next door. Nice to meet you!' — Xin chào, tôi vừa chuyển đến ở cạnh. Rất vui được gặp bạn!\n\n"

                            "Bạn đã có 12 từ vựng thực tế về nhà ở. "
                            "Đây là bước tiếp theo của bạn: lần tới khi bạn thấy một bài đăng cho thuê phòng, "
                            "hãy thử đọc nó bằng tiếng Anh. Tìm những từ bạn đã học — rent, deposit, lease, utility. "
                            "Bạn sẽ ngạc nhiên vì mình hiểu được nhiều hơn trước.\n\n"

                            "Nếu bạn có cơ hội nói chuyện với chủ nhà bằng tiếng Anh, hãy thử. "
                            "Hỏi về rent. Hỏi về deposit. Hỏi về lease. "
                            "Mỗi lần bạn dùng một từ trong thực tế, nó sẽ trở thành của bạn mãi mãi.\n\n"

                            "Cảm ơn bạn đã học cùng mình. Bây giờ hãy ra ngoài và tìm ngôi nhà mơ ước nhé! "
                            "Hẹn gặp lại ở bài học tiếp theo!"
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
