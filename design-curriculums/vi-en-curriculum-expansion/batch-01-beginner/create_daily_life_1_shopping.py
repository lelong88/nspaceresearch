"""
Create curriculum: Shopping & Bargaining (Mua Sắm & Trả Giá — Bước Đầu Tiên)
Level: beginner | Skill focus: balanced_skills | Content type: []
Topic: Daily life | 12 words (2 groups of 6) | 4 sessions | Bilingual (vi/en)
Tone: vivid_scenario | Farewell tone: warm_accountability
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
# Group 1 (Session 1): price, cheap, expensive, market, vendor, cash
# Group 2 (Session 2): discount, bargain, receipt, change, quality, size

W1 = ["price", "cheap", "expensive", "market", "vendor", "cash"]
W2 = ["discount", "bargain", "receipt", "change", "quality", "size"]
ALL_WORDS = W1 + W2

content = {
    "title": "Mua Sắm & Trả Giá — Bước Đầu Tiên",
    "contentTypeTags": [],
    "description": (
        "HÃY TƯỞNG TƯỢNG BẠN ĐANG ĐỨNG GIỮA CHỢ BẾN THÀNH, TAY CẦM TỜ TIỀN, MIỆNG MUỐN NÓI MÀ KHÔNG BIẾT BẮT ĐẦU TỪ ĐÂU.\n\n"
        "Bạn muốn hỏi giá một chiếc áo. Bạn muốn nói \"rẻ hơn được không?\" Bạn muốn đếm tiền thối — "
        "nhưng tất cả những từ đó đều biến mất khi bạn cần chúng nhất.\n\n"
        "Mua sắm bằng tiếng Anh giống như đi chợ mà không mang theo ví — "
        "bạn nhìn thấy mọi thứ nhưng không thể \"mua\" được gì. "
        "12 từ vựng trong bài học này chính là chiếc ví đó.\n\n"
        "Sau bài học, bạn sẽ tự tin hỏi giá, trả giá, và hoàn tất giao dịch bằng tiếng Anh — "
        "dù ở chợ Việt Nam hay cửa hàng nước ngoài.\n\n"
        "Vừa học từ vựng thực tế, vừa nâng cấp khả năng giao tiếp — "
        "mỗi từ là một bước tiến gần hơn đến sự tự tin khi mua sắm bằng tiếng Anh."
    ),
    "preview": {
        "text": (
            "Imagine standing in a busy market. You see something you love. "
            "You want to ask: \"How much?\" You want to say: \"Too expensive!\" "
            "But the words don't come. This curriculum gives you 12 essential shopping words — "
            "price, cheap, expensive, market, vendor, cash, discount, bargain, receipt, change, quality, and size. "
            "Across four sessions, you will learn each word through flashcards, reading passages about real shopping situations, "
            "and guided writing exercises. By the end, you will confidently ask prices, negotiate deals, "
            "and complete transactions in English — whether at a Vietnamese market or a store abroad."
        )
    },
    "learningSessions": [
        # ════════════════════════════════════════════
        # SESSION 1 — Phần 1 (Words: price, cheap, expensive, market, vendor, cash)
        # ════════════════════════════════════════════
        {
            "title": "Phần 1",
            "activities": [
                # ── introAudio: Welcome + Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về mua sắm và trả giá bằng tiếng Anh.",
                    "data": {
                        "text": (
                            "Xin chào và chào mừng bạn đến với bài học 'Mua Sắm & Trả Giá'! "
                            "Hôm nay chúng ta sẽ học 6 từ vựng tiếng Anh rất quan trọng khi bạn đi mua sắm. "
                            "Những từ này sẽ giúp bạn tự tin hơn khi hỏi giá, so sánh giá cả, và trả tiền. "
                            "Sáu từ hôm nay là: price, cheap, expensive, market, vendor, và cash.\n\n"

                            "Từ đầu tiên là 'price'. Price là danh từ, nghĩa là 'giá' hoặc 'giá cả'. "
                            "Ví dụ: 'The price of this shirt is ten dollars.' — Giá của chiếc áo này là mười đô la. "
                            "Trong bài đọc, bạn sẽ thấy từ 'price' khi nhân vật hỏi giá một món đồ ở chợ.\n\n"

                            "Từ thứ hai là 'cheap'. Cheap là tính từ, nghĩa là 'rẻ'. "
                            "Ví dụ: 'This bag is very cheap.' — Chiếc túi này rất rẻ. "
                            "Trong bài đọc, từ 'cheap' xuất hiện khi nhân vật tìm thấy một món hàng giá tốt.\n\n"

                            "Từ thứ ba là 'expensive'. Expensive là tính từ, nghĩa là 'đắt' hoặc 'mắc'. "
                            "Ví dụ: 'That watch is too expensive for me.' — Chiếc đồng hồ đó quá đắt đối với tôi. "
                            "Trong bài đọc, bạn sẽ thấy từ 'expensive' khi nhân vật so sánh giá cả giữa các cửa hàng.\n\n"

                            "Từ thứ tư là 'market'. Market là danh từ, nghĩa là 'chợ' hoặc 'thị trường'. "
                            "Ví dụ: 'I go to the market every morning.' — Tôi đi chợ mỗi sáng. "
                            "Trong bài đọc, 'market' là nơi nhân vật đến mua sắm.\n\n"

                            "Từ thứ năm là 'vendor'. Vendor là danh từ, nghĩa là 'người bán hàng'. "
                            "Ví dụ: 'The vendor sells fresh fruit.' — Người bán hàng bán trái cây tươi. "
                            "Trong bài đọc, 'vendor' là người mà nhân vật nói chuyện khi mua đồ.\n\n"

                            "Từ cuối cùng là 'cash'. Cash là danh từ, nghĩa là 'tiền mặt'. "
                            "Ví dụ: 'I pay with cash, not a card.' — Tôi trả bằng tiền mặt, không dùng thẻ. "
                            "Trong bài đọc, bạn sẽ thấy từ 'cash' khi nhân vật trả tiền cho món hàng.\n\n"

                            "Bây giờ, hãy bắt đầu học từ vựng qua flashcards nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Mua sắm (Phần 1)",
                    "description": "Học 6 từ: price, cheap, expensive, market, vendor, cash",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Mua sắm (Phần 1)",
                    "description": "Học 6 từ: price, cheap, expensive, market, vendor, cash",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Mua sắm (Phần 1)",
                    "description": "Học 6 từ: price, cheap, expensive, market, vendor, cash",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Mua sắm (Phần 1)",
                    "description": "Học 6 từ: price, cheap, expensive, market, vendor, cash",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Đi chợ buổi sáng",
                    "description": "Lan goes to the market and asks about prices.",
                    "data": {
                        "text": (
                            "Lan goes to the market every Saturday. "
                            "She likes the big market near her house. "
                            "Today she wants to buy a new bag.\n\n"
                            "She sees a nice bag at a small shop. "
                            "She asks the vendor, 'What is the price?' "
                            "The vendor says, 'It is twenty dollars.'\n\n"
                            "Lan thinks it is expensive. "
                            "She walks to another shop. "
                            "She finds a bag that looks the same. "
                            "This one is cheap. It is only eight dollars.\n\n"
                            "Lan is happy. She pays with cash. "
                            "The vendor gives her the bag. "
                            "'Thank you!' Lan says. "
                            "She loves shopping at the market."
                        ),
                        "vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Đi chợ buổi sáng",
                    "description": "Lan goes to the market and asks about prices.",
                    "data": {
                        "text": (
                            "Lan goes to the market every Saturday. "
                            "She likes the big market near her house. "
                            "Today she wants to buy a new bag.\n\n"
                            "She sees a nice bag at a small shop. "
                            "She asks the vendor, 'What is the price?' "
                            "The vendor says, 'It is twenty dollars.'\n\n"
                            "Lan thinks it is expensive. "
                            "She walks to another shop. "
                            "She finds a bag that looks the same. "
                            "This one is cheap. It is only eight dollars.\n\n"
                            "Lan is happy. She pays with cash. "
                            "The vendor gives her the bag. "
                            "'Thank you!' Lan says. "
                            "She loves shopping at the market."
                        ),
                        "vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Đi chợ buổi sáng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Lan goes to the market every Saturday. "
                            "She likes the big market near her house. "
                            "Today she wants to buy a new bag.\n\n"
                            "She sees a nice bag at a small shop. "
                            "She asks the vendor, 'What is the price?' "
                            "The vendor says, 'It is twenty dollars.'\n\n"
                            "Lan thinks it is expensive. "
                            "She walks to another shop. "
                            "She finds a bag that looks the same. "
                            "This one is cheap. It is only eight dollars.\n\n"
                            "Lan is happy. She pays with cash. "
                            "The vendor gives her the bag. "
                            "'Thank you!' Lan says. "
                            "She loves shopping at the market."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Mua sắm (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về mua sắm.",
                    "data": {
                        "vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash"],
                        "items": [
                            {
                                "targetVocab": "price",
                                "prompt": "Hãy dùng từ 'price' để viết một câu về việc hỏi giá một món đồ. Ví dụ: The price of this book is five dollars."
                            },
                            {
                                "targetVocab": "cheap",
                                "prompt": "Hãy dùng từ 'cheap' để viết một câu về một món đồ giá rẻ. Ví dụ: The food at the market is cheap and delicious."
                            },
                            {
                                "targetVocab": "expensive",
                                "prompt": "Hãy dùng từ 'expensive' để viết một câu về một món đồ đắt tiền. Ví dụ: The new phone is very expensive."
                            },
                            {
                                "targetVocab": "market",
                                "prompt": "Hãy dùng từ 'market' để viết một câu về việc đi chợ. Ví dụ: My mother goes to the market every morning."
                            },
                            {
                                "targetVocab": "vendor",
                                "prompt": "Hãy dùng từ 'vendor' để viết một câu về người bán hàng. Ví dụ: The vendor at the corner sells fresh vegetables."
                            },
                            {
                                "targetVocab": "cash",
                                "prompt": "Hãy dùng từ 'cash' để viết một câu về việc trả tiền mặt. Ví dụ: I always pay with cash when I go to the market."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 2 — Phần 2 (Words: discount, bargain, receipt, change, quality, size)
        # ════════════════════════════════════════════
        {
            "title": "Phần 2",
            "activities": [
                # ── introAudio: Recap + New Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng mới",
                    "description": "Ôn lại từ vựng Phần 1 và giới thiệu 6 từ mới về mua sắm.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong Phần 1, bạn đã học 6 từ rất hữu ích: "
                            "price (giá), cheap (rẻ), expensive (đắt), market (chợ), vendor (người bán hàng), và cash (tiền mặt). "
                            "Bạn còn nhớ không? Tuyệt vời!\n\n"
                            "Hôm nay chúng ta sẽ học thêm 6 từ mới. Những từ này giúp bạn trả giá, "
                            "kiểm tra chất lượng, và hoàn tất việc mua sắm. "
                            "Sáu từ mới là: discount, bargain, receipt, change, quality, và size.\n\n"

                            "Từ đầu tiên là 'discount'. Discount là danh từ, nghĩa là 'giảm giá'. "
                            "Ví dụ: 'Can I get a discount?' — Tôi có thể được giảm giá không? "
                            "Trong bài đọc, bạn sẽ thấy từ 'discount' khi nhân vật xin giảm giá ở cửa hàng.\n\n"

                            "Từ thứ hai là 'bargain'. Bargain có thể là danh từ hoặc động từ. "
                            "Là danh từ, nó nghĩa là 'món hời'. Là động từ, nó nghĩa là 'trả giá' hoặc 'mặc cả'. "
                            "Ví dụ: 'This dress is a real bargain!' — Chiếc váy này thật sự là món hời! "
                            "Trong bài đọc, từ 'bargain' xuất hiện khi nhân vật mặc cả với người bán.\n\n"

                            "Từ thứ ba là 'receipt'. Receipt là danh từ, nghĩa là 'hóa đơn' hoặc 'biên lai'. "
                            "Ví dụ: 'Please give me the receipt.' — Làm ơn đưa tôi hóa đơn. "
                            "Trong bài đọc, bạn sẽ thấy từ 'receipt' khi nhân vật xin hóa đơn sau khi mua hàng.\n\n"

                            "Từ thứ tư là 'change'. Change là danh từ, nghĩa là 'tiền thối' hoặc 'tiền thừa'. "
                            "Ví dụ: 'Here is your change.' — Đây là tiền thối của bạn. "
                            "Trong bài đọc, từ 'change' xuất hiện khi người bán trả lại tiền thừa.\n\n"

                            "Từ thứ năm là 'quality'. Quality là danh từ, nghĩa là 'chất lượng'. "
                            "Ví dụ: 'The quality of this fabric is very good.' — Chất lượng của vải này rất tốt. "
                            "Trong bài đọc, bạn sẽ thấy từ 'quality' khi nhân vật kiểm tra chất lượng sản phẩm.\n\n"

                            "Từ cuối cùng là 'size'. Size là danh từ, nghĩa là 'kích cỡ' hoặc 'cỡ'. "
                            "Ví dụ: 'What size do you need?' — Bạn cần cỡ nào? "
                            "Trong bài đọc, từ 'size' xuất hiện khi nhân vật chọn cỡ áo phù hợp.\n\n"

                            "Hãy bắt đầu với flashcards để ghi nhớ 6 từ mới này nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Mua sắm (Phần 2)",
                    "description": "Học 6 từ: discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Mua sắm (Phần 2)",
                    "description": "Học 6 từ: discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Mua sắm (Phần 2)",
                    "description": "Học 6 từ: discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Mua sắm (Phần 2)",
                    "description": "Học 6 từ: discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Mua áo ở cửa hàng",
                    "description": "Minh shops for a shirt and learns to bargain.",
                    "data": {
                        "text": (
                            "Minh needs a new shirt for work. "
                            "He goes to a big store in the city. "
                            "He sees many shirts in different colors.\n\n"
                            "He picks a blue shirt. He checks the size. "
                            "It is medium — perfect for him. "
                            "He looks at the quality. The fabric feels soft.\n\n"
                            "The shirt costs thirty dollars. "
                            "Minh asks, 'Can I get a discount?' "
                            "The seller says, 'Yes, ten percent off.' "
                            "What a bargain!\n\n"
                            "Minh pays and gets his change. "
                            "He also asks for a receipt. "
                            "He puts the receipt in his wallet. "
                            "Minh is happy with his new shirt."
                        ),
                        "vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Mua áo ở cửa hàng",
                    "description": "Minh shops for a shirt and learns to bargain.",
                    "data": {
                        "text": (
                            "Minh needs a new shirt for work. "
                            "He goes to a big store in the city. "
                            "He sees many shirts in different colors.\n\n"
                            "He picks a blue shirt. He checks the size. "
                            "It is medium — perfect for him. "
                            "He looks at the quality. The fabric feels soft.\n\n"
                            "The shirt costs thirty dollars. "
                            "Minh asks, 'Can I get a discount?' "
                            "The seller says, 'Yes, ten percent off.' "
                            "What a bargain!\n\n"
                            "Minh pays and gets his change. "
                            "He also asks for a receipt. "
                            "He puts the receipt in his wallet. "
                            "Minh is happy with his new shirt."
                        ),
                        "vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Mua áo ở cửa hàng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Minh needs a new shirt for work. "
                            "He goes to a big store in the city. "
                            "He sees many shirts in different colors.\n\n"
                            "He picks a blue shirt. He checks the size. "
                            "It is medium — perfect for him. "
                            "He looks at the quality. The fabric feels soft.\n\n"
                            "The shirt costs thirty dollars. "
                            "Minh asks, 'Can I get a discount?' "
                            "The seller says, 'Yes, ten percent off.' "
                            "What a bargain!\n\n"
                            "Minh pays and gets his change. "
                            "He also asks for a receipt. "
                            "He puts the receipt in his wallet. "
                            "Minh is happy with his new shirt."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Mua sắm (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng mới về mua sắm.",
                    "data": {
                        "vocabList": ["discount", "bargain", "receipt", "change", "quality", "size"],
                        "items": [
                            {
                                "targetVocab": "discount",
                                "prompt": "Hãy dùng từ 'discount' để viết một câu về việc xin giảm giá. Ví dụ: The store gives a discount on weekends."
                            },
                            {
                                "targetVocab": "bargain",
                                "prompt": "Hãy dùng từ 'bargain' để viết một câu về một món hời khi mua sắm. Ví dụ: I found a great bargain at the market today."
                            },
                            {
                                "targetVocab": "receipt",
                                "prompt": "Hãy dùng từ 'receipt' để viết một câu về việc giữ hóa đơn. Ví dụ: Always keep your receipt after you buy something."
                            },
                            {
                                "targetVocab": "change",
                                "prompt": "Hãy dùng từ 'change' để viết một câu về tiền thối. Ví dụ: The vendor gives me two dollars in change."
                            },
                            {
                                "targetVocab": "quality",
                                "prompt": "Hãy dùng từ 'quality' để viết một câu về chất lượng sản phẩm. Ví dụ: I always check the quality before I buy clothes."
                            },
                            {
                                "targetVocab": "size",
                                "prompt": "Hãy dùng từ 'size' để viết một câu về kích cỡ quần áo. Ví dụ: This shirt is the wrong size for me."
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
                            "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về mua sắm và trả giá. Thật tuyệt vời!\n\n"
                            "Trong Phần 1, bạn đã học: price (giá), cheap (rẻ), expensive (đắt), "
                            "market (chợ), vendor (người bán hàng), và cash (tiền mặt). "
                            "Bạn đã đọc về Lan đi chợ mua túi xách.\n\n"
                            "Trong Phần 2, bạn đã học: discount (giảm giá), bargain (món hời), "
                            "receipt (hóa đơn), change (tiền thối), quality (chất lượng), và size (kích cỡ). "
                            "Bạn đã đọc về Minh mua áo sơ mi ở cửa hàng.\n\n"
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
                    "title": "Flashcards: Ôn tập mua sắm",
                    "description": "Học 12 từ: price, cheap, expensive, market, vendor, cash, discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── speakFlashcards (all 12) ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập mua sắm",
                    "description": "Học 12 từ: price, cheap, expensive, market, vendor, cash, discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── vocabLevel1 (all 12) ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập mua sắm",
                    "description": "Học 12 từ: price, cheap, expensive, market, vendor, cash, discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── vocabLevel2 (all 12) ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập mua sắm",
                    "description": "Học 12 từ: price, cheap, expensive, market, vendor, cash, discount, bargain, receipt, change, quality, size",
                    "data": {"vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"]}
                },
                # ── writingSentence (all 12) ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập mua sắm",
                    "description": "Viết câu sử dụng tất cả 12 từ vựng về mua sắm.",
                    "data": {
                        "vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"],
                        "items": [
                            {
                                "targetVocab": "price",
                                "prompt": "Hãy dùng từ 'price' để viết một câu về giá cả ở chợ. Ví dụ: The price of fruit is low at the morning market."
                            },
                            {
                                "targetVocab": "cheap",
                                "prompt": "Hãy dùng từ 'cheap' để viết một câu về một thứ giá rẻ bạn thích. Ví dụ: Street food in Vietnam is cheap and tasty."
                            },
                            {
                                "targetVocab": "expensive",
                                "prompt": "Hãy dùng từ 'expensive' để viết một câu về một thứ đắt tiền. Ví dụ: Shoes at the mall are more expensive than at the market."
                            },
                            {
                                "targetVocab": "market",
                                "prompt": "Hãy dùng từ 'market' để viết một câu về chợ gần nhà bạn. Ví dụ: The market near my house opens at six in the morning."
                            },
                            {
                                "targetVocab": "vendor",
                                "prompt": "Hãy dùng từ 'vendor' để viết một câu về người bán hàng bạn quen. Ví dụ: The fruit vendor always smiles at her customers."
                            },
                            {
                                "targetVocab": "cash",
                                "prompt": "Hãy dùng từ 'cash' để viết một câu về cách bạn trả tiền. Ví dụ: Most people at the market pay with cash."
                            },
                            {
                                "targetVocab": "discount",
                                "prompt": "Hãy dùng từ 'discount' để viết một câu về việc được giảm giá. Ví dụ: If you buy three, you get a discount."
                            },
                            {
                                "targetVocab": "bargain",
                                "prompt": "Hãy dùng từ 'bargain' để viết một câu về việc mặc cả hoặc mua được món hời. Ví dụ: My mother is good at finding a bargain."
                            },
                            {
                                "targetVocab": "receipt",
                                "prompt": "Hãy dùng từ 'receipt' để viết một câu về hóa đơn mua hàng. Ví dụ: I keep every receipt in a small box."
                            },
                            {
                                "targetVocab": "change",
                                "prompt": "Hãy dùng từ 'change' để viết một câu về tiền thối. Ví dụ: The cashier counts the change carefully."
                            },
                            {
                                "targetVocab": "quality",
                                "prompt": "Hãy dùng từ 'quality' để viết một câu về chất lượng sản phẩm. Ví dụ: Good quality shoes last a long time."
                            },
                            {
                                "targetVocab": "size",
                                "prompt": "Hãy dùng từ 'size' để viết một câu về kích cỡ. Ví dụ: I need a bigger size for this jacket."
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
                            "Chào mừng bạn đến với phần cuối cùng của bài học 'Mua Sắm & Trả Giá'!\n\n"
                            "Bạn đã học 12 từ vựng quan trọng: price, cheap, expensive, market, vendor, cash, "
                            "discount, bargain, receipt, change, quality, và size. "
                            "Trong Phần 1, bạn đọc về Lan đi chợ mua túi xách. "
                            "Trong Phần 2, bạn đọc về Minh mua áo sơ mi ở cửa hàng.\n\n"
                            "Bây giờ, bạn sẽ đọc một bài đọc dài hơn. Bài đọc này kết hợp tất cả 12 từ vựng "
                            "trong một câu chuyện về việc mua sắm. Hãy chú ý cách mỗi từ được sử dụng trong ngữ cảnh thực tế.\n\n"
                            "Hãy đọc chậm, tận hưởng câu chuyện, và nhận ra những từ bạn đã học. Bạn sẽ ngạc nhiên "
                            "vì mình hiểu được nhiều hơn bạn nghĩ đấy!"
                        )
                    }
                },
                # ── reading: Full article ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Một ngày mua sắm",
                    "description": "A full story about a shopping day using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "It is Saturday morning. Lan and Minh go to the market together. "
                            "The market is big and busy. There are many vendors selling food, clothes, and bags.\n\n"
                            "First, Lan wants to buy fruit. She walks to a fruit vendor. "
                            "The vendor has oranges, bananas, and mangoes. "
                            "Lan asks, 'What is the price of the mangoes?' "
                            "The vendor says, 'Two dollars for one kilo.' "
                            "Lan thinks it is cheap. She buys two kilos. She pays with cash.\n\n"
                            "Next, Minh wants to buy a hat. He sees a nice hat at a small shop. "
                            "He checks the size. It fits his head well. "
                            "He looks at the quality. The hat feels strong and well-made. "
                            "But the price is fifteen dollars. Minh thinks it is expensive.\n\n"
                            "Minh asks the vendor, 'Can I get a discount?' "
                            "The vendor smiles and says, 'I can give you ten percent off.' "
                            "Now the hat is only thirteen dollars and fifty cents. "
                            "Minh is happy. That is a good bargain!\n\n"
                            "Minh gives the vendor fifteen dollars. "
                            "The vendor gives him one dollar and fifty cents in change. "
                            "Minh asks for a receipt. The vendor writes a receipt on a small paper.\n\n"
                            "After that, Lan and Minh walk around the market. "
                            "They see many things. Some things are cheap. Some things are expensive. "
                            "Lan finds a scarf. The quality is good and the size is perfect. "
                            "The price is only five dollars. What a bargain!\n\n"
                            "At the end of the day, Lan and Minh sit down for coffee. "
                            "They look at their bags. They are happy with their shopping. "
                            "Lan says, 'I love this market. The prices are good.' "
                            "Minh says, 'Yes, and the vendors are very friendly.' "
                            "They both smile. It is a good day."
                        ),
                        "vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Một ngày mua sắm",
                    "description": "A full story about a shopping day using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "It is Saturday morning. Lan and Minh go to the market together. "
                            "The market is big and busy. There are many vendors selling food, clothes, and bags.\n\n"
                            "First, Lan wants to buy fruit. She walks to a fruit vendor. "
                            "The vendor has oranges, bananas, and mangoes. "
                            "Lan asks, 'What is the price of the mangoes?' "
                            "The vendor says, 'Two dollars for one kilo.' "
                            "Lan thinks it is cheap. She buys two kilos. She pays with cash.\n\n"
                            "Next, Minh wants to buy a hat. He sees a nice hat at a small shop. "
                            "He checks the size. It fits his head well. "
                            "He looks at the quality. The hat feels strong and well-made. "
                            "But the price is fifteen dollars. Minh thinks it is expensive.\n\n"
                            "Minh asks the vendor, 'Can I get a discount?' "
                            "The vendor smiles and says, 'I can give you ten percent off.' "
                            "Now the hat is only thirteen dollars and fifty cents. "
                            "Minh is happy. That is a good bargain!\n\n"
                            "Minh gives the vendor fifteen dollars. "
                            "The vendor gives him one dollar and fifty cents in change. "
                            "Minh asks for a receipt. The vendor writes a receipt on a small paper.\n\n"
                            "After that, Lan and Minh walk around the market. "
                            "They see many things. Some things are cheap. Some things are expensive. "
                            "Lan finds a scarf. The quality is good and the size is perfect. "
                            "The price is only five dollars. What a bargain!\n\n"
                            "At the end of the day, Lan and Minh sit down for coffee. "
                            "They look at their bags. They are happy with their shopping. "
                            "Lan says, 'I love this market. The prices are good.' "
                            "Minh says, 'Yes, and the vendors are very friendly.' "
                            "They both smile. It is a good day."
                        ),
                        "vocabList": ["price", "cheap", "expensive", "market", "vendor", "cash", "discount", "bargain", "receipt", "change", "quality", "size"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Một ngày mua sắm",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "It is Saturday morning. Lan and Minh go to the market together. "
                            "The market is big and busy. There are many vendors selling food, clothes, and bags.\n\n"
                            "First, Lan wants to buy fruit. She walks to a fruit vendor. "
                            "The vendor has oranges, bananas, and mangoes. "
                            "Lan asks, 'What is the price of the mangoes?' "
                            "The vendor says, 'Two dollars for one kilo.' "
                            "Lan thinks it is cheap. She buys two kilos. She pays with cash.\n\n"
                            "Next, Minh wants to buy a hat. He sees a nice hat at a small shop. "
                            "He checks the size. It fits his head well. "
                            "He looks at the quality. The hat feels strong and well-made. "
                            "But the price is fifteen dollars. Minh thinks it is expensive.\n\n"
                            "Minh asks the vendor, 'Can I get a discount?' "
                            "The vendor smiles and says, 'I can give you ten percent off.' "
                            "Now the hat is only thirteen dollars and fifty cents. "
                            "Minh is happy. That is a good bargain!\n\n"
                            "Minh gives the vendor fifteen dollars. "
                            "The vendor gives him one dollar and fifty cents in change. "
                            "Minh asks for a receipt. The vendor writes a receipt on a small paper.\n\n"
                            "After that, Lan and Minh walk around the market. "
                            "They see many things. Some things are cheap. Some things are expensive. "
                            "Lan finds a scarf. The quality is good and the size is perfect. "
                            "The price is only five dollars. What a bargain!\n\n"
                            "At the end of the day, Lan and Minh sit down for coffee. "
                            "They look at their bags. They are happy with their shopping. "
                            "Lan says, 'I love this market. The prices are good.' "
                            "Minh says, 'Yes, and the vendors are very friendly.' "
                            "They both smile. It is a good day."
                        )
                    }
                },
                # ── introAudio: Farewell (warm_accountability tone) ──
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay ấm áp.",
                    "data": {
                        "text": (
                            "Tuyệt vời! Bạn đã hoàn thành bài học 'Mua Sắm & Trả Giá'! "
                            "Hãy cùng ôn lại những từ quan trọng nhất nhé.\n\n"

                            "Từ 'price' nghĩa là giá cả. Khi bạn muốn hỏi giá, hãy nói: "
                            "'What is the price of this jacket?' — Giá của chiếc áo khoác này là bao nhiêu?\n\n"

                            "Từ 'bargain' nghĩa là món hời hoặc mặc cả. "
                            "Khi bạn mua được giá tốt, hãy nói: "
                            "'I got a great bargain on these shoes!' — Tôi mua được đôi giày này giá hời lắm!\n\n"

                            "Từ 'discount' nghĩa là giảm giá. "
                            "Khi bạn muốn xin giảm giá, hãy nói: "
                            "'Is there a discount for students?' — Có giảm giá cho sinh viên không?\n\n"

                            "Từ 'quality' nghĩa là chất lượng. "
                            "Khi bạn muốn khen chất lượng, hãy nói: "
                            "'The quality of this leather bag is excellent.' — Chất lượng chiếc túi da này rất tuyệt.\n\n"

                            "Từ 'receipt' nghĩa là hóa đơn. "
                            "Khi bạn cần hóa đơn, hãy nói: "
                            "'Could I have a receipt, please?' — Cho tôi xin hóa đơn được không?\n\n"

                            "Từ 'change' nghĩa là tiền thối. "
                            "Khi bạn cần kiểm tra tiền thối, hãy nói: "
                            "'I think the change is not correct.' — Tôi nghĩ tiền thối không đúng.\n\n"

                            "Bạn đã học 12 từ vựng thực tế về mua sắm. "
                            "Đây không chỉ là từ vựng trong sách — đây là những từ bạn sẽ dùng mỗi ngày. "
                            "Lần tới khi bạn đi mua sắm, hãy thử dùng những từ này bằng tiếng Anh. "
                            "Hỏi giá bằng tiếng Anh. Trả giá bằng tiếng Anh. Xin hóa đơn bằng tiếng Anh.\n\n"

                            "Mỗi lần bạn dùng một từ mới trong thực tế, bạn sẽ nhớ nó mãi mãi. "
                            "Đó là cách tốt nhất để học. Hãy bắt đầu từ hôm nay nhé!\n\n"

                            "Cảm ơn bạn đã học cùng mình. Hẹn gặp lại ở bài học tiếp theo!"
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
