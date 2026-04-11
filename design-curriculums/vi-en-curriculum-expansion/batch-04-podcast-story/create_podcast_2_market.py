import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from firebase_token import get_firebase_id_token
from validate_curriculum import (
    validate_balanced_skills_beginner,
    validate_content_type_tags,
    validate_bilingual_prompts,
)

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Curriculum #42: Easy English: At the Market
# Level: beginner | Skill focus: balanced_skills | Content type: ["podcast"]
# Topic: Food | 12 words (2 groups of 6), 4 sessions, bilingual (vi-en)
# Description tone: empathetic_observation (different from Morning Routines' provocative_question)
# Farewell tone: warm_accountability (different from Morning Routines' introspective_guide)
# W1: vendor, bargain, fresh, ingredient, portion, ripe
# W2: spice, stall, weigh, price, basket, sample

content = {
    "title": "Easy English: At the Market",
    "contentTypeTags": ["podcast"],
    "description": "BẠN ĐÃ BAO GIỜ ĐỨNG GIỮA CHỢ, MUỐN HỎI GIÁ MỘT MÓN ĐỒ BẰNG TIẾNG ANH — NHƯNG KHÔNG BIẾT BẮT ĐẦU TỪ ĐÂU?\n\nĐi chợ là một trong những trải nghiệm gần gũi nhất trong cuộc sống. Bạn nhìn thấy những quả xoài chín vàng, ngửi mùi gia vị thơm nồng, nghe tiếng người bán hàng mời chào. Nhưng khi đặt chân vào một khu chợ ở nước ngoài, mọi thứ bỗng trở nên xa lạ — không phải vì đồ ăn khác, mà vì bạn thiếu từ ngữ để kết nối.\n\nChợ không chỉ là nơi mua bán — chợ là nơi bạn học cách giao tiếp thực sự. Khi bạn biết cách hỏi giá, trả giá, chọn nguyên liệu, và nói về độ tươi của thực phẩm, bạn không chỉ mua được đồ ăn ngon — bạn còn xây dựng sự tự tin trong giao tiếp hàng ngày.\n\nHai nhân vật Hà và Tuấn sẽ dẫn bạn đi chợ sáng — từ quầy rau quả đến hàng gia vị, từ việc cân đo đến trả giá. Bạn sẽ nghe họ nói chuyện với người bán, chọn nguyên liệu, và chia sẻ bí quyết mua sắm thông minh.\n\n12 từ vựng trong bài học này — từ vendor đến sample — sẽ giúp bạn tự tin bước vào bất kỳ khu chợ nào trên thế giới, vừa nâng cao kỹ năng tiếng Anh, vừa khám phá văn hóa ẩm thực qua từng gian hàng.",
    "preview": {
        "text": "Have you ever walked through a busy market and wished you could describe everything you see, smell, and taste in English? In this podcast-inspired lesson, you will learn 12 essential English words about markets and food shopping: vendor, bargain, fresh, ingredient, portion, ripe, spice, stall, weigh, price, basket, and sample. Follow Hà and Tuấn as they explore a morning market together — Hà is an experienced shopper who knows every vendor by name, while Tuấn is learning how to pick the best ingredients and bargain for a good price. Through two conversational reading passages, a full review session, and a final combined reading, you will practice talking about food, shopping, and market culture in English. By the end, you will be able to describe fresh produce, ask about prices, and share your own market experiences with confidence."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về đi chợ — giới thiệu 6 từ vựng đầu tiên.",
                    "data": {
                        "text": "Chào mừng bạn đến với Easy English: At the Market — bài học thứ hai trong chuỗi podcast tiếng Anh dành cho người mới bắt đầu. Hôm nay chúng ta sẽ nói về một chủ đề rất quen thuộc với người Việt Nam: đi chợ. Bạn có thích đi chợ không? Bạn thường mua gì? Bạn có hay trả giá không? Đây là những câu hỏi đơn giản, nhưng khi nói bằng tiếng Anh, bạn cần biết đúng từ.\n\nTrong phần này, bạn sẽ học 6 từ vựng tiếng Anh: vendor, bargain, fresh, ingredient, portion, và ripe. Đây là những từ bạn sẽ dùng khi nói về việc mua sắm thực phẩm.\n\nTừ đầu tiên là vendor — danh từ — nghĩa là người bán hàng. Vendor là người bán đồ ở chợ hoặc trên đường phố. Ví dụ: 'The vendor sells fruit every morning.' Trong bài đọc, Hà quen biết nhiều vendor ở chợ gần nhà.\n\nTừ thứ hai là bargain — động từ và danh từ — nghĩa là trả giá, mặc cả, hoặc món hời. Bargain là khi bạn thương lượng để mua với giá thấp hơn. Ví dụ: 'She likes to bargain for a better price.' Trong bài đọc, Hà rất giỏi bargain — cô ấy luôn mua được giá tốt.\n\nTừ thứ ba là fresh — tính từ — nghĩa là tươi, mới. Fresh là khi thực phẩm vừa được thu hoạch hoặc chế biến, chưa bị hỏng. Ví dụ: 'These vegetables are very fresh.' Trong bài đọc, Hà luôn chọn rau và trái cây fresh nhất.\n\nTừ thứ tư là ingredient — danh từ — nghĩa là nguyên liệu. Ingredient là những thứ bạn cần để nấu một món ăn. Ví dụ: 'I need three ingredients for this soup.' Trong bài đọc, Hà mua ingredient để nấu bữa tối cho gia đình.\n\nTừ thứ năm là portion — danh từ — nghĩa là phần, khẩu phần. Portion là lượng thức ăn dành cho một người hoặc một lần dùng. Ví dụ: 'This portion is enough for two people.' Trong bài đọc, Hà biết cách chọn đúng portion cho gia đình mình.\n\nTừ cuối cùng là ripe — tính từ — nghĩa là chín. Ripe là khi trái cây đã sẵn sàng để ăn — mềm, ngọt, và thơm. Ví dụ: 'The mangoes are ripe and ready to eat.' Trong bài đọc, Hà dạy Tuấn cách nhận biết trái cây ripe.\n\nBạn đã có 6 từ vựng đầu tiên rồi! Hãy bắt đầu với flashcard, sau đó đọc bài về buổi đi chợ của Hà nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Mua sắm ở chợ",
                    "description": "Học 6 từ: vendor, bargain, fresh, ingredient, portion, ripe",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Mua sắm ở chợ",
                    "description": "Học 6 từ: vendor, bargain, fresh, ingredient, portion, ripe",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Mua sắm ở chợ",
                    "description": "Học 6 từ: vendor, bargain, fresh, ingredient, portion, ripe",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Mua sắm ở chợ",
                    "description": "Học 6 từ: vendor, bargain, fresh, ingredient, portion, ripe",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Buổi đi chợ của Hà",
                    "description": "Hà shares her morning market routine and how she picks the best ingredients.",
                    "data": {
                        "text": "Hà goes to the market every morning. She wakes up early and walks there before seven. The market is close to her house.\n\nHà knows every vendor by name. She buys vegetables from Mrs. Lan. She buys fish from Mr. Tùng. They always smile when they see her.\n\nToday, Hà needs ingredients for dinner. She wants to make soup and fried rice. She needs onions, carrots, and chicken.\n\nFirst, she goes to the vegetable vendor. She picks up some tomatoes. They are red and ripe. She smells them. They smell sweet. She puts them in her basket.\n\nHà always checks if the food is fresh. She looks at the color. She touches the skin. If it is soft and smells good, it is fresh. If it is hard or has brown spots, she does not buy it.\n\nNext, she buys chicken. She asks for a small portion. She does not need a lot. Just enough for her family of three.\n\nThe vendor says the price is fifty thousand dong. Hà thinks it is too high. She bargains. She says forty thousand. The vendor agrees. Hà smiles.\n\nHà likes going to the market. It is not just about food. It is about people. She talks, she laughs, she learns. The market is her favorite place in the morning."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Buổi đi chợ của Hà",
                    "description": "Hà shares her morning market routine and how she picks the best ingredients.",
                    "data": {
                        "text": "Hà goes to the market every morning. She wakes up early and walks there before seven. The market is close to her house.\n\nHà knows every vendor by name. She buys vegetables from Mrs. Lan. She buys fish from Mr. Tùng. They always smile when they see her.\n\nToday, Hà needs ingredients for dinner. She wants to make soup and fried rice. She needs onions, carrots, and chicken.\n\nFirst, she goes to the vegetable vendor. She picks up some tomatoes. They are red and ripe. She smells them. They smell sweet. She puts them in her basket.\n\nHà always checks if the food is fresh. She looks at the color. She touches the skin. If it is soft and smells good, it is fresh. If it is hard or has brown spots, she does not buy it.\n\nNext, she buys chicken. She asks for a small portion. She does not need a lot. Just enough for her family of three.\n\nThe vendor says the price is fifty thousand dong. Hà thinks it is too high. She bargains. She says forty thousand. The vendor agrees. Hà smiles.\n\nHà likes going to the market. It is not just about food. It is about people. She talks, she laughs, she learns. The market is her favorite place in the morning."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Buổi đi chợ của Hà",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Hà goes to the market every morning. She wakes up early and walks there before seven. The market is close to her house.\n\nHà knows every vendor by name. She buys vegetables from Mrs. Lan. She buys fish from Mr. Tùng. They always smile when they see her.\n\nToday, Hà needs ingredients for dinner. She wants to make soup and fried rice. She needs onions, carrots, and chicken.\n\nFirst, she goes to the vegetable vendor. She picks up some tomatoes. They are red and ripe. She smells them. They smell sweet. She puts them in her basket.\n\nHà always checks if the food is fresh. She looks at the color. She touches the skin. If it is soft and smells good, it is fresh. If it is hard or has brown spots, she does not buy it.\n\nNext, she buys chicken. She asks for a small portion. She does not need a lot. Just enough for her family of three.\n\nThe vendor says the price is fifty thousand dong. Hà thinks it is too high. She bargains. She says forty thousand. The vendor agrees. Hà smiles.\n\nHà likes going to the market. It is not just about food. It is about people. She talks, she laughs, she learns. The market is her favorite place in the morning."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Mua sắm ở chợ",
                    "description": "Viết câu sử dụng từ vựng về đi chợ và mua thực phẩm.",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe"],
                        "items": [
                            {
                                "targetVocab": "vendor",
                                "prompt": "Hãy dùng từ 'vendor' để viết một câu về người bán hàng ở chợ. Ví dụ: The fruit vendor near my house sells the best oranges in town."
                            },
                            {
                                "targetVocab": "bargain",
                                "prompt": "Hãy dùng từ 'bargain' để viết một câu về việc trả giá khi mua đồ. Ví dụ: My mother always bargains at the market to get a lower price."
                            },
                            {
                                "targetVocab": "fresh",
                                "prompt": "Hãy dùng từ 'fresh' để viết một câu về thực phẩm tươi. Ví dụ: I only buy fresh fish because it tastes much better than frozen fish."
                            },
                            {
                                "targetVocab": "ingredient",
                                "prompt": "Hãy dùng từ 'ingredient' để viết một câu về nguyên liệu nấu ăn. Ví dụ: You need four main ingredients to make this simple soup."
                            },
                            {
                                "targetVocab": "portion",
                                "prompt": "Hãy dùng từ 'portion' để viết một câu về khẩu phần ăn. Ví dụ: I bought a small portion of chicken for dinner tonight."
                            },
                            {
                                "targetVocab": "ripe",
                                "prompt": "Hãy dùng từ 'ripe' để viết một câu về trái cây chín. Ví dụ: These bananas are perfectly ripe — they are yellow and sweet."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Ôn lại phần 1 và giới thiệu 6 từ vựng mới về gia vị, quầy hàng, và mua sắm.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với phần 2 của Easy English: At the Market! Trong phần trước, bạn đã học 6 từ vựng: vendor là người bán hàng, bargain là trả giá hoặc món hời, fresh là tươi, ingredient là nguyên liệu, portion là khẩu phần, và ripe là chín. Bạn cũng đã đọc về buổi đi chợ của Hà — cô ấy biết cách chọn rau tươi, trả giá giỏi, và quen biết mọi người bán hàng.\n\nBây giờ, hãy gặp Tuấn — anh ấy mới bắt đầu tập đi chợ và còn nhiều điều phải học! Trong phần này, bạn sẽ học thêm 6 từ vựng mới: spice, stall, weigh, price, basket, và sample.\n\nTừ đầu tiên là spice — danh từ — nghĩa là gia vị. Spice là những thứ như tiêu, ớt, quế, hồi — dùng để làm món ăn thêm hương vị. Ví dụ: 'This soup needs more spice.' Trong bài đọc, Tuấn khám phá quầy spice ở chợ và rất ngạc nhiên vì có quá nhiều loại.\n\nTừ thứ hai là stall — danh từ — nghĩa là quầy hàng, sạp hàng. Stall là một chỗ nhỏ ở chợ nơi người bán bày đồ để bán. Ví dụ: 'There are many stalls at the morning market.' Trong bài đọc, Tuấn đi qua nhiều stall khác nhau — từ quầy rau đến quầy gia vị.\n\nTừ thứ ba là weigh — động từ — nghĩa là cân. Weigh là khi bạn đặt thứ gì đó lên cân để biết nó nặng bao nhiêu. Ví dụ: 'The vendor weighs the fish before telling the price.' Trong bài đọc, Tuấn học cách nhờ người bán weigh thực phẩm trước khi mua.\n\nTừ thứ tư là price — danh từ — nghĩa là giá, giá tiền. Price là số tiền bạn phải trả để mua một thứ gì đó. Ví dụ: 'What is the price of these mangoes?' Trong bài đọc, Tuấn hỏi price của nhiều thứ nhưng không biết giá nào là hợp lý.\n\nTừ thứ năm là basket — danh từ — nghĩa là giỏ, rổ. Basket là đồ dùng để đựng thực phẩm khi đi chợ. Ví dụ: 'She carries a big basket to the market every day.' Trong bài đọc, Tuấn quên mang basket và phải xách đồ bằng tay.\n\nTừ cuối cùng là sample — động từ và danh từ — nghĩa là nếm thử, mẫu thử. Sample là khi bạn ăn thử một ít trước khi quyết định mua. Ví dụ: 'Can I sample this fruit before I buy it?' Trong bài đọc, Tuấn được mời sample trái cây và gia vị ở chợ.\n\nSáu từ mới đã sẵn sàng! Hãy học flashcard rồi đọc về lần đầu đi chợ của Tuấn nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Gia vị và mua sắm",
                    "description": "Học 6 từ: spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Gia vị và mua sắm",
                    "description": "Học 6 từ: spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Gia vị và mua sắm",
                    "description": "Học 6 từ: spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Gia vị và mua sắm",
                    "description": "Học 6 từ: spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tuấn lần đầu đi chợ",
                    "description": "Tuấn visits the market for the first time and learns how to shop.",
                    "data": {
                        "text": "Tuấn does not go to the market often. He usually buys food at the supermarket. But today, his sister Hà asks him to come with her.\n\nThe market is busy and loud. There are many stalls on both sides. Tuấn sees vegetables, meat, fish, and fruit. He does not know where to start.\n\n'Follow me,' Hà says. She walks to a spice stall first. There are bags of pepper, chili, and cinnamon. Tuấn smells the air. It is strong and warm.\n\n'Can I sample this?' Tuấn asks the vendor. The vendor gives him a small piece of dried ginger. It is spicy but good.\n\nNext, they go to the fruit stall. Tuấn picks up a mango. 'How do I know if it is ripe?' he asks.\n\n'Press it gently,' Hà says. 'If it is a little soft, it is ripe. If it is hard, wait a few days.'\n\nTuấn wants to buy some oranges. 'What is the price?' he asks the vendor. 'Thirty thousand for one kilo,' the vendor says. Tuấn does not know if that is a good price. Hà tells him it is fair.\n\nThe vendor puts the oranges on a scale to weigh them. One kilo exactly. Tuấn pays and puts them in a plastic bag. He forgot to bring a basket.\n\n'Next time, bring a basket,' Hà says. 'It is easier to carry everything.'\n\nThey buy a few more things — some herbs, tofu, and a small portion of pork. Tuấn carries the bags. His hands are full.\n\n'The market is fun,' Tuấn says. 'But it is also tiring. How do you do this every day?'\n\nHà laughs. 'Practice,' she says. 'Just like learning English.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tuấn lần đầu đi chợ",
                    "description": "Tuấn visits the market for the first time and learns how to shop.",
                    "data": {
                        "text": "Tuấn does not go to the market often. He usually buys food at the supermarket. But today, his sister Hà asks him to come with her.\n\nThe market is busy and loud. There are many stalls on both sides. Tuấn sees vegetables, meat, fish, and fruit. He does not know where to start.\n\n'Follow me,' Hà says. She walks to a spice stall first. There are bags of pepper, chili, and cinnamon. Tuấn smells the air. It is strong and warm.\n\n'Can I sample this?' Tuấn asks the vendor. The vendor gives him a small piece of dried ginger. It is spicy but good.\n\nNext, they go to the fruit stall. Tuấn picks up a mango. 'How do I know if it is ripe?' he asks.\n\n'Press it gently,' Hà says. 'If it is a little soft, it is ripe. If it is hard, wait a few days.'\n\nTuấn wants to buy some oranges. 'What is the price?' he asks the vendor. 'Thirty thousand for one kilo,' the vendor says. Tuấn does not know if that is a good price. Hà tells him it is fair.\n\nThe vendor puts the oranges on a scale to weigh them. One kilo exactly. Tuấn pays and puts them in a plastic bag. He forgot to bring a basket.\n\n'Next time, bring a basket,' Hà says. 'It is easier to carry everything.'\n\nThey buy a few more things — some herbs, tofu, and a small portion of pork. Tuấn carries the bags. His hands are full.\n\n'The market is fun,' Tuấn says. 'But it is also tiring. How do you do this every day?'\n\nHà laughs. 'Practice,' she says. 'Just like learning English.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tuấn lần đầu đi chợ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Tuấn does not go to the market often. He usually buys food at the supermarket. But today, his sister Hà asks him to come with her.\n\nThe market is busy and loud. There are many stalls on both sides. Tuấn sees vegetables, meat, fish, and fruit. He does not know where to start.\n\n'Follow me,' Hà says. She walks to a spice stall first. There are bags of pepper, chili, and cinnamon. Tuấn smells the air. It is strong and warm.\n\n'Can I sample this?' Tuấn asks the vendor. The vendor gives him a small piece of dried ginger. It is spicy but good.\n\nNext, they go to the fruit stall. Tuấn picks up a mango. 'How do I know if it is ripe?' he asks.\n\n'Press it gently,' Hà says. 'If it is a little soft, it is ripe. If it is hard, wait a few days.'\n\nTuấn wants to buy some oranges. 'What is the price?' he asks the vendor. 'Thirty thousand for one kilo,' the vendor says. Tuấn does not know if that is a good price. Hà tells him it is fair.\n\nThe vendor puts the oranges on a scale to weigh them. One kilo exactly. Tuấn pays and puts them in a plastic bag. He forgot to bring a basket.\n\n'Next time, bring a basket,' Hà says. 'It is easier to carry everything.'\n\nThey buy a few more things — some herbs, tofu, and a small portion of pork. Tuấn carries the bags. His hands are full.\n\n'The market is fun,' Tuấn says. 'But it is also tiring. How do you do this every day?'\n\nHà laughs. 'Practice,' she says. 'Just like learning English.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Gia vị và mua sắm",
                    "description": "Viết câu sử dụng từ vựng về gia vị, quầy hàng, và mua sắm ở chợ.",
                    "data": {
                        "vocabList": ["spice", "stall", "weigh", "price", "basket", "sample"],
                        "items": [
                            {
                                "targetVocab": "spice",
                                "prompt": "Hãy dùng từ 'spice' để viết một câu về gia vị trong nấu ăn. Ví dụ: Vietnamese food uses a lot of spice like chili and pepper."
                            },
                            {
                                "targetVocab": "stall",
                                "prompt": "Hãy dùng từ 'stall' để viết một câu về quầy hàng ở chợ. Ví dụ: My favorite stall at the market sells fresh herbs and vegetables."
                            },
                            {
                                "targetVocab": "weigh",
                                "prompt": "Hãy dùng từ 'weigh' để viết một câu về việc cân thực phẩm. Ví dụ: The vendor weighs the fish on a small scale before I pay."
                            },
                            {
                                "targetVocab": "price",
                                "prompt": "Hãy dùng từ 'price' để viết một câu về giá cả ở chợ. Ví dụ: The price of vegetables is cheaper at the market than at the supermarket."
                            },
                            {
                                "targetVocab": "basket",
                                "prompt": "Hãy dùng từ 'basket' để viết một câu về giỏ đi chợ. Ví dụ: I always bring a big basket when I go to the morning market."
                            },
                            {
                                "targetVocab": "sample",
                                "prompt": "Hãy dùng từ 'sample' để viết một câu về việc nếm thử thực phẩm. Ví dụ: The vendor let me sample a piece of mango before I bought it."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 12 từ vựng — ôn lại tất cả trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về at the market — đi chợ. Hãy cùng ôn lại nhanh nhé.\n\nTrong phần 1, bạn đã học 6 từ cùng Hà: vendor là người bán hàng — Hà quen biết mọi vendor ở chợ. Bargain là trả giá — Hà rất giỏi bargain, luôn mua được giá tốt. Fresh là tươi — Hà chỉ mua rau và trái cây fresh nhất. Ingredient là nguyên liệu — Hà mua ingredient để nấu bữa tối. Portion là khẩu phần — Hà biết chọn đúng portion cho gia đình. Ripe là chín — Hà biết cách nhận biết trái cây ripe bằng cách ấn nhẹ.\n\nTrong phần 2, bạn đã học 6 từ cùng Tuấn: spice là gia vị — Tuấn ngạc nhiên vì có rất nhiều loại spice ở chợ. Stall là quầy hàng — Tuấn đi qua nhiều stall khác nhau. Weigh là cân — người bán weigh cam trước khi tính tiền. Price là giá — Tuấn hỏi price nhưng không biết giá nào là hợp lý. Basket là giỏ — Tuấn quên mang basket nên phải xách đồ bằng tay. Sample là nếm thử — Tuấn được mời sample gừng khô ở quầy gia vị.\n\nBây giờ, bạn sẽ ôn lại tất cả 12 từ qua flashcard và bài tập viết. Sau đó, trong phần cuối, bạn sẽ đọc một bài tổng hợp về Hà và Tuấn cùng đi chợ. Sẵn sàng chưa? Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: vendor, bargain, fresh, ingredient, portion, ripe, spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe", "spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: vendor, bargain, fresh, ingredient, portion, ripe, spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe", "spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: vendor, bargain, fresh, ingredient, portion, ripe, spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe", "spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: vendor, bargain, fresh, ingredient, portion, ripe, spice, stall, weigh, price, basket, sample",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe", "spice", "stall", "weigh", "price", "basket", "sample"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập đi chợ",
                    "description": "Viết câu ôn tập sử dụng tất cả 12 từ vựng về đi chợ.",
                    "data": {
                        "vocabList": ["vendor", "bargain", "fresh", "ingredient", "portion", "ripe", "spice", "stall", "weigh", "price", "basket", "sample"],
                        "items": [
                            {
                                "targetVocab": "vendor",
                                "prompt": "Hãy dùng từ 'vendor' để viết một câu về mối quan hệ giữa người mua và người bán. Ví dụ: A friendly vendor makes shopping at the market more enjoyable."
                            },
                            {
                                "targetVocab": "bargain",
                                "prompt": "Hãy dùng từ 'bargain' để viết một câu về kinh nghiệm trả giá. Ví dụ: If you bargain politely, most vendors will give you a better price."
                            },
                            {
                                "targetVocab": "fresh",
                                "prompt": "Hãy dùng từ 'fresh' để viết một câu so sánh thực phẩm tươi và đông lạnh. Ví dụ: Fresh vegetables from the market taste better than frozen ones from the store."
                            },
                            {
                                "targetVocab": "ingredient",
                                "prompt": "Hãy dùng từ 'ingredient' để viết một câu về việc chuẩn bị nấu ăn. Ví dụ: I always make a list of ingredients before I go to the market."
                            },
                            {
                                "targetVocab": "portion",
                                "prompt": "Hãy dùng từ 'portion' để viết một câu về lượng thức ăn phù hợp. Ví dụ: Buying the right portion of food helps you save money and reduce waste."
                            },
                            {
                                "targetVocab": "ripe",
                                "prompt": "Hãy dùng từ 'ripe' để viết một câu về cách chọn trái cây. Ví dụ: You can tell a mango is ripe by its color and how soft it feels."
                            },
                            {
                                "targetVocab": "spice",
                                "prompt": "Hãy dùng từ 'spice' để viết một câu về gia vị yêu thích của bạn. Ví dụ: My grandmother uses many different spices to make her soup taste amazing."
                            },
                            {
                                "targetVocab": "stall",
                                "prompt": "Hãy dùng từ 'stall' để viết một câu về quầy hàng yêu thích ở chợ. Ví dụ: The fruit stall at the corner always has the freshest mangoes."
                            },
                            {
                                "targetVocab": "weigh",
                                "prompt": "Hãy dùng từ 'weigh' để viết một câu về việc cân thực phẩm khi mua. Ví dụ: Always ask the vendor to weigh your food so you know the exact amount."
                            },
                            {
                                "targetVocab": "price",
                                "prompt": "Hãy dùng từ 'price' để viết một câu về giá cả ở chợ. Ví dụ: The price of fruit changes with the season — it is cheaper in summer."
                            },
                            {
                                "targetVocab": "basket",
                                "prompt": "Hãy dùng từ 'basket' để viết một câu về việc mang giỏ đi chợ. Ví dụ: Bringing your own basket to the market is better for the environment."
                            },
                            {
                                "targetVocab": "sample",
                                "prompt": "Hãy dùng từ 'sample' để viết một câu về việc thử đồ ăn trước khi mua. Ví dụ: I always sample the fruit at the market to make sure it is sweet."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc tổng hợp",
                    "description": "Giới thiệu bài đọc cuối cùng kết hợp câu chuyện của Hà và Tuấn ở chợ.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của Easy English: At the Market! Bạn đã đi một chặng đường tuyệt vời. Trong phần 1, bạn học về buổi đi chợ quen thuộc của Hà với 6 từ: vendor, bargain, fresh, ingredient, portion, ripe. Trong phần 2, bạn gặp Tuấn và lần đầu tiên anh ấy khám phá chợ với 6 từ: spice, stall, weigh, price, basket, sample. Trong phần ôn tập, bạn đã luyện lại tất cả 12 từ.\n\nBây giờ, bạn sẽ đọc một bài tổng hợp — Hà và Tuấn cùng nhau đi chợ vào một buổi sáng cuối tuần. Bài đọc này dùng tất cả 12 từ vựng bạn đã học. Hãy đọc chậm, chú ý từng từ, và thưởng thức câu chuyện nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Hà và Tuấn cùng đi chợ",
                    "description": "Hà and Tuấn go to the market together on a weekend morning.",
                    "data": {
                        "text": "It is Sunday morning. Hà and Tuấn walk to the market together. The sun is warm. The streets are busy. Tuấn carries a big basket this time. He learned his lesson.\n\n'What do we need today?' Tuấn asks.\n\n'We need ingredients for a big lunch,' Hà says. 'Mom and Dad are coming over. I want to make chicken soup and a mango salad.'\n\nThey walk past many stalls. The first stall sells vegetables. The vendor is an old woman with a kind face. Hà picks up some green onions and cilantro.\n\n'Are these fresh?' Tuấn asks. He touches the leaves. They are bright green and firm.\n\n'Very fresh,' the vendor says. 'I picked them this morning.'\n\nHà puts them in the basket. She pays without bargaining. 'Some vendors give you a fair price from the start,' she tells Tuấn. 'You do not always need to bargain.'\n\nNext, they go to the chicken stall. Hà asks for a medium portion. The vendor puts the chicken on a scale to weigh it. It is one and a half kilos.\n\n'What is the price?' Tuấn asks.\n\n'Eighty thousand,' the vendor says.\n\n'That is a good price,' Hà says. She pays and puts the chicken in the basket.\n\nThen they walk to the fruit stall. Tuấn picks up a mango. He presses it gently. It is soft. 'This one is ripe,' he says with a smile. He remembers what Hà taught him.\n\n'Good job!' Hà says. 'Pick four more. We need five for the salad.'\n\nTuấn picks four ripe mangoes. He is careful. He checks each one.\n\nBefore they leave, Hà stops at the spice stall. She buys pepper and dried chili. The vendor offers Tuấn a sample of lemongrass tea.\n\n'Try it,' the vendor says. Tuấn takes a small cup. It is warm and sweet.\n\n'This is delicious,' Tuấn says. 'How much is it?'\n\n'Twenty thousand for a bag,' the vendor says.\n\nTuấn looks at Hà. She nods. He buys one bag.\n\nOn the way home, the basket is full. Tuấn carries it with both hands.\n\n'You know,' Tuấn says, 'I used to think the market was just a place to buy food. But it is more than that. You talk to people. You learn about food. You smell the spices. You taste new things.'\n\nHà smiles. 'That is why I love the market,' she says. 'Every visit is a little adventure.'\n\nTuấn nods. 'Next Sunday, I will come again. And I will bring a bigger basket.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Hà và Tuấn cùng đi chợ",
                    "description": "Hà and Tuấn go to the market together on a weekend morning.",
                    "data": {
                        "text": "It is Sunday morning. Hà and Tuấn walk to the market together. The sun is warm. The streets are busy. Tuấn carries a big basket this time. He learned his lesson.\n\n'What do we need today?' Tuấn asks.\n\n'We need ingredients for a big lunch,' Hà says. 'Mom and Dad are coming over. I want to make chicken soup and a mango salad.'\n\nThey walk past many stalls. The first stall sells vegetables. The vendor is an old woman with a kind face. Hà picks up some green onions and cilantro.\n\n'Are these fresh?' Tuấn asks. He touches the leaves. They are bright green and firm.\n\n'Very fresh,' the vendor says. 'I picked them this morning.'\n\nHà puts them in the basket. She pays without bargaining. 'Some vendors give you a fair price from the start,' she tells Tuấn. 'You do not always need to bargain.'\n\nNext, they go to the chicken stall. Hà asks for a medium portion. The vendor puts the chicken on a scale to weigh it. It is one and a half kilos.\n\n'What is the price?' Tuấn asks.\n\n'Eighty thousand,' the vendor says.\n\n'That is a good price,' Hà says. She pays and puts the chicken in the basket.\n\nThen they walk to the fruit stall. Tuấn picks up a mango. He presses it gently. It is soft. 'This one is ripe,' he says with a smile. He remembers what Hà taught him.\n\n'Good job!' Hà says. 'Pick four more. We need five for the salad.'\n\nTuấn picks four ripe mangoes. He is careful. He checks each one.\n\nBefore they leave, Hà stops at the spice stall. She buys pepper and dried chili. The vendor offers Tuấn a sample of lemongrass tea.\n\n'Try it,' the vendor says. Tuấn takes a small cup. It is warm and sweet.\n\n'This is delicious,' Tuấn says. 'How much is it?'\n\n'Twenty thousand for a bag,' the vendor says.\n\nTuấn looks at Hà. She nods. He buys one bag.\n\nOn the way home, the basket is full. Tuấn carries it with both hands.\n\n'You know,' Tuấn says, 'I used to think the market was just a place to buy food. But it is more than that. You talk to people. You learn about food. You smell the spices. You taste new things.'\n\nHà smiles. 'That is why I love the market,' she says. 'Every visit is a little adventure.'\n\nTuấn nods. 'Next Sunday, I will come again. And I will bring a bigger basket.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Hà và Tuấn cùng đi chợ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "It is Sunday morning. Hà and Tuấn walk to the market together. The sun is warm. The streets are busy. Tuấn carries a big basket this time. He learned his lesson.\n\n'What do we need today?' Tuấn asks.\n\n'We need ingredients for a big lunch,' Hà says. 'Mom and Dad are coming over. I want to make chicken soup and a mango salad.'\n\nThey walk past many stalls. The first stall sells vegetables. The vendor is an old woman with a kind face. Hà picks up some green onions and cilantro.\n\n'Are these fresh?' Tuấn asks. He touches the leaves. They are bright green and firm.\n\n'Very fresh,' the vendor says. 'I picked them this morning.'\n\nHà puts them in the basket. She pays without bargaining. 'Some vendors give you a fair price from the start,' she tells Tuấn. 'You do not always need to bargain.'\n\nNext, they go to the chicken stall. Hà asks for a medium portion. The vendor puts the chicken on a scale to weigh it. It is one and a half kilos.\n\n'What is the price?' Tuấn asks.\n\n'Eighty thousand,' the vendor says.\n\n'That is a good price,' Hà says. She pays and puts the chicken in the basket.\n\nThen they walk to the fruit stall. Tuấn picks up a mango. He presses it gently. It is soft. 'This one is ripe,' he says with a smile. He remembers what Hà taught him.\n\n'Good job!' Hà says. 'Pick four more. We need five for the salad.'\n\nTuấn picks four ripe mangoes. He is careful. He checks each one.\n\nBefore they leave, Hà stops at the spice stall. She buys pepper and dried chili. The vendor offers Tuấn a sample of lemongrass tea.\n\n'Try it,' the vendor says. Tuấn takes a small cup. It is warm and sweet.\n\n'This is delicious,' Tuấn says. 'How much is it?'\n\n'Twenty thousand for a bag,' the vendor says.\n\nTuấn looks at Hà. She nods. He buys one bag.\n\nOn the way home, the basket is full. Tuấn carries it with both hands.\n\n'You know,' Tuấn says, 'I used to think the market was just a place to buy food. But it is more than that. You talk to people. You learn about food. You smell the spices. You taste new things.'\n\nHà smiles. 'That is why I love the market,' she says. 'Every visit is a little adventure.'\n\nTuấn nods. 'Next Sunday, I will come again. And I will bring a bigger basket.'"
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay — farewell tone: warm_accountability.",
                    "data": {
                        "text": "Bạn đã hoàn thành Easy English: At the Market. Và bây giờ, tôi muốn thử thách bạn một chút.\n\nBạn đã học 12 từ vựng. Bạn đã đọc về Hà và Tuấn. Bạn đã viết những câu của riêng mình. Nhưng từ vựng chỉ thực sự thuộc về bạn khi bạn dùng nó ngoài đời thật. Vì vậy, đây là thử thách của tôi dành cho bạn: lần tới bạn đi chợ, hãy thử nghĩ về những gì bạn thấy bằng tiếng Anh. Chỉ trong đầu thôi cũng được. Đó là cách bạn biến từ vựng thành kỹ năng thật sự.\n\nHãy cùng ôn lại 12 từ nhé — và lần này, tôi muốn bạn tự hỏi: mình đã dùng từ này trong câu của mình chưa?\n\nVendor — người bán hàng. Mỗi vendor ở chợ đều có một câu chuyện riêng. Câu mới: The best vendors remember their customers and always give them the freshest food.\n\nBargain — trả giá, món hời. Bargain là một kỹ năng — bạn cần lịch sự nhưng cũng cần tự tin. Câu mới: Learning to bargain is not just about saving money — it is about understanding the value of things.\n\nFresh — tươi. Fresh không chỉ là về thực phẩm — mà còn là về cách bạn bắt đầu mỗi ngày. Câu mới: Cooking with fresh ingredients from the market makes every meal taste like home.\n\nIngredient — nguyên liệu. Mỗi món ăn ngon bắt đầu từ những ingredient tốt. Câu mới: A great cook knows that the secret is not the recipe — it is the quality of each ingredient.\n\nPortion — khẩu phần. Mua đúng portion giúp bạn tiết kiệm và không lãng phí. Câu mới: Buying the right portion means you eat everything and throw nothing away.\n\nRipe — chín. Bạn đã biết cách chọn trái cây ripe chưa? Hãy thử lần tới đi chợ nhé. Câu mới: A perfectly ripe avocado is soft when you press it but not too mushy.\n\nBây giờ tôi hỏi bạn: tuần này, bạn có thể đi chợ và thử dùng ít nhất ba từ trong đầu không? Không cần nói to. Chỉ cần nghĩ: đây là vendor, quả này ripe, giá này là good price.\n\nSpice — gia vị. Spice làm cho cuộc sống thêm hương vị — cả trong bếp lẫn trong ngôn ngữ. Câu mới: Every country has its own favorite spices that make its food unique.\n\nStall — quầy hàng. Mỗi stall ở chợ là một thế giới nhỏ. Câu mới: Walking past the stalls in a morning market is like taking a tour of local food culture.\n\nWeigh — cân. Weigh giúp bạn biết chính xác mình mua bao nhiêu. Câu mới: It is a good habit to ask the vendor to weigh your food in front of you.\n\nPrice — giá. Biết price hợp lý giúp bạn mua sắm thông minh hơn. Câu mới: Comparing prices at different stalls can help you find the best deal.\n\nBasket — giỏ. Mang basket đi chợ là một thói quen nhỏ nhưng rất hữu ích. Câu mới: A reusable basket is better for the environment than plastic bags.\n\nSample — nếm thử. Đừng ngại sample — đó là cách tốt nhất để khám phá món mới. Câu mới: The joy of visiting a market is being able to sample foods you have never tried before.\n\nĐây là lời hứa của tôi với bạn: nếu bạn dùng những từ này trong cuộc sống thật — dù chỉ trong suy nghĩ — chúng sẽ ở lại với bạn mãi mãi. Đừng chỉ học từ vựng. Hãy sống với từ vựng.\n\nCảm ơn bạn đã học cùng tôi. Lần tới đi chợ, hãy nhớ mang theo basket — và nhớ mang theo cả 12 từ tiếng Anh này nhé! Hẹn gặp lại bạn trong bài học tiếp theo."
                    }
                }
            ]
        }
    ]
}

# ── Validate ──
print("Validating content...")
validate_balanced_skills_beginner(content)
print("  ✓ balanced_skills_beginner structure OK")
validate_content_type_tags(content)
print("  ✓ contentTypeTags OK")
validate_bilingual_prompts(content, "beginner")
print("  ✓ bilingual prompts OK")
print("All validations passed!\n")

# ── Upload ──
token = get_firebase_id_token(UID)
resp = requests.post(
    f"{API_BASE}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
resp.raise_for_status()
data = resp.json()
curriculum_id = data.get("id") or data.get("curriculum", {}).get("id")
print(f"Created curriculum: {curriculum_id}")
print(f"Title: {content['title']}")
print(f"Level: beginner | Skill: balanced_skills | Content: podcast")
print(f"Words: 12 (2 groups of 6)")
