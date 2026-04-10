"""
Create curriculum: Supply & Demand – Cung và Cầu
Series A — Kinh Tế Vi Mô (Microeconomics), curriculum #1
18 words | 5 sessions | provocative_question tone | introspective guide farewell
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/economics-university-curriculum")
from validate_curriculum import validate_all

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Word groups ──────────────────────────────────────────────
W1 = ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]
W2 = ["elasticity", "substitute", "complement", "shift", "curve", "price"]
W3 = ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Supply & Demand – Cung và Cầu",
    "contentTypeTags": [],
    "description": (
        "BẠN ĐỌC SÁCH KINH TẾ TIẾNG ANH MÀ CỨ PHẢI TRA TỪ ĐIỂN MỖI TRANG — BAO GIỜ MỚI THOÁT?\n\n"
        "Mỗi lần mở giáo trình Microeconomics, bạn gặp ngay supply, demand, equilibrium — "
        "những từ tưởng đơn giản nhưng khi ghép vào câu phân tích thì bạn đọc ba lần vẫn chưa hiểu. "
        "Bạn biết cung cầu là gì bằng tiếng Việt, nhưng khi giảng viên chiếu slide tiếng Anh, "
        "bạn chỉ biết gật đầu và hy vọng không bị gọi trả lời.\n\n"
        "Hãy tưởng tượng vốn từ tiếng Anh kinh tế của bạn như một chiếc chìa khóa gỉ sét — "
        "cánh cửa tri thức ở ngay trước mặt nhưng bạn không mở nổi. "
        "Chỉ cần đánh bóng lại 18 từ vựng cốt lõi, chiếc chìa khóa ấy sẽ vừa khít ổ khóa.\n\n"
        "Sau khóa học này, bạn sẽ đọc được đoạn phân tích cung cầu bằng tiếng Anh mà không cần dừng lại tra từ, "
        "tự tin phát biểu trong lớp khi thảo luận về equilibrium hay price ceiling, "
        "và viết được những câu phân tích sắc bén bằng ngôn ngữ chuyên ngành.\n\n"
        "18 từ vựng — từ supply đến scarcity — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kinh tế, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về cung và cầu — nền tảng của mọi phân tích kinh tế vi mô. "
            "Bạn sẽ học supply, demand, equilibrium, surplus, shortage, quantity trong phần đầu tiên, "
            "nơi bài đọc kể về cách thị trường tự điều chỉnh khi cung gặp cầu. "
            "Tiếp theo là elasticity, substitute, complement, shift, curve, price — "
            "những từ giúp bạn hiểu vì sao giá cả thay đổi và thị trường phản ứng ra sao. "
            "Cuối cùng, allocate, ration, ceiling, floor, incentive, scarcity đưa bạn vào thế giới "
            "của chính sách giá và phân bổ nguồn lực. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu giáo trình kinh tế vi mô bằng tiếng Anh — "
            "không cần tra từ điển mỗi dòng."
        )
    },
    "learningSessions": [
        # ── SESSION 1: Words 1-6 ─────────────────────────────
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Chào mừng bạn đến với bài học về cung và cầu — nền tảng kinh tế vi mô.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học đầu tiên trong chuỗi từ vựng Kinh tế vi mô — "
                            "chủ đề hôm nay là Cung và Cầu, hay trong tiếng Anh là Supply and Demand. "
                            "Đây là nền tảng của mọi phân tích kinh tế. Dù bạn đang học về thị trường cà phê "
                            "hay thị trường bất động sản, tất cả đều bắt đầu từ hai lực cơ bản: cung và cầu.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: supply, demand, equilibrium, surplus, shortage, và quantity. "
                            "Đây là những từ bạn sẽ gặp ngay từ chương đầu tiên của bất kỳ giáo trình kinh tế vi mô nào.\n\n"
                            "Từ đầu tiên là supply — danh từ — nghĩa là nguồn cung, lượng hàng hóa hoặc dịch vụ "
                            "mà người bán sẵn sàng cung cấp ở một mức giá nhất định. "
                            "Ví dụ: 'When the price of rice increases, the supply from farmers also increases.' "
                            "Trong bài đọc, bạn sẽ thấy supply được dùng để mô tả lượng hàng mà các nhà sản xuất "
                            "đưa ra thị trường khi giá thay đổi.\n\n"
                            "Từ thứ hai là demand — danh từ — nghĩa là nhu cầu, lượng hàng hóa hoặc dịch vụ "
                            "mà người mua muốn mua ở một mức giá nhất định. "
                            "Ví dụ: 'The demand for smartphones rises every year as technology improves.' "
                            "Trong bài đọc, demand xuất hiện khi nói về hành vi của người tiêu dùng — "
                            "họ muốn mua bao nhiêu sản phẩm ở các mức giá khác nhau.\n\n"
                            "Từ thứ ba là equilibrium — danh từ — nghĩa là trạng thái cân bằng, "
                            "điểm mà tại đó lượng cung bằng lượng cầu và giá cả ổn định. "
                            "Ví dụ: 'The market reaches equilibrium when the amount buyers want equals the amount sellers offer.' "
                            "Đây là khái niệm trung tâm trong bài đọc — khi thị trường tìm được điểm cân bằng, "
                            "không có áp lực để giá tăng hay giảm.\n\n"
                            "Từ thứ tư là surplus — danh từ — nghĩa là thặng dư, tình trạng khi lượng cung "
                            "vượt quá lượng cầu. "
                            "Ví dụ: 'A surplus of unsold goods forces companies to lower their prices.' "
                            "Trong bài đọc, surplus mô tả điều gì xảy ra khi giá quá cao — "
                            "người bán có nhiều hàng hơn người mua muốn mua.\n\n"
                            "Từ thứ năm là shortage — danh từ — nghĩa là thiếu hụt, tình trạng khi lượng cầu "
                            "vượt quá lượng cung. "
                            "Ví dụ: 'During the pandemic, there was a shortage of medical masks worldwide.' "
                            "Trong bài đọc, shortage là mặt đối lập của surplus — khi giá quá thấp, "
                            "người mua muốn nhiều hơn những gì người bán có thể cung cấp.\n\n"
                            "Từ cuối cùng là quantity — danh từ — nghĩa là số lượng, lượng cụ thể của hàng hóa "
                            "hoặc dịch vụ được mua hoặc bán. "
                            "Ví dụ: 'The quantity of coffee sold depends on both the price and the season.' "
                            "Trong bài đọc, quantity luôn đi kèm với supply hoặc demand — "
                            "quantity supplied là lượng cung, quantity demanded là lượng cầu.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cung và cầu để thấy các từ này trong ngữ cảnh thực tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cung và cầu cơ bản",
                    "description": "Học 6 từ: supply, demand, equilibrium, surplus, shortage, quantity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cung và cầu cơ bản",
                    "description": "Học 6 từ: supply, demand, equilibrium, surplus, shortage, quantity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cung và cầu cơ bản",
                    "description": "Học 6 từ: supply, demand, equilibrium, surplus, shortage, quantity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cung và cầu cơ bản",
                    "description": "Học 6 từ: supply, demand, equilibrium, surplus, shortage, quantity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Cung và cầu cơ bản",
                    "description": "Học 6 từ: supply, demand, equilibrium, surplus, shortage, quantity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cung và cầu cơ bản",
                    "description": "Every day, millions of buyers and sellers make decisions that shape the prices we see in markets.",
                    "data": {
                        "text": (
                            "Every day, millions of buyers and sellers make decisions that shape the prices we see in markets. "
                            "To understand how prices are set, economists study two basic forces: supply and demand.\n\n"
                            "Demand is the quantity of a good or service that consumers are willing to buy at a given price. "
                            "When the price of a product goes down, people usually want to buy more of it. "
                            "For example, if the price of a cup of coffee drops from fifty thousand dong to thirty thousand dong, "
                            "many students will buy coffee more often. This is the law of demand: "
                            "as price falls, the quantity demanded rises.\n\n"
                            "Supply is the quantity of a good or service that producers are willing to sell at a given price. "
                            "When the price goes up, producers want to sell more because they can earn higher profits. "
                            "If coffee shops can charge fifty thousand dong per cup instead of thirty thousand, "
                            "more shops will open and existing ones will make more coffee. "
                            "This is the law of supply: as price rises, the quantity supplied rises.\n\n"
                            "The market finds its equilibrium where the supply curve meets the demand curve. "
                            "At this point, the quantity that buyers want to purchase equals the quantity that sellers want to sell. "
                            "The price at equilibrium is called the market-clearing price. "
                            "No one is left wanting to buy more, and no seller is stuck with unsold goods.\n\n"
                            "But what happens when the price is not at equilibrium? "
                            "If the price is too high, sellers offer more than buyers want. "
                            "This creates a surplus — extra goods sit on shelves and sellers must lower prices to attract buyers. "
                            "On the other hand, if the price is too low, buyers want more than sellers can provide. "
                            "This creates a shortage — people line up, shelves go empty, and sellers may raise prices.\n\n"
                            "In both cases, the market pushes the price back toward equilibrium. "
                            "A surplus puts downward pressure on prices, while a shortage puts upward pressure. "
                            "Over time, the quantity bought and sold adjusts until supply equals demand once again. "
                            "This self-correcting process is one of the most powerful ideas in economics."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cung và cầu cơ bản",
                    "description": "Every day, millions of buyers and sellers make decisions that shape the prices we see in markets.",
                    "data": {
                        "text": (
                            "Every day, millions of buyers and sellers make decisions that shape the prices we see in markets. "
                            "To understand how prices are set, economists study two basic forces: supply and demand.\n\n"
                            "Demand is the quantity of a good or service that consumers are willing to buy at a given price. "
                            "When the price of a product goes down, people usually want to buy more of it. "
                            "For example, if the price of a cup of coffee drops from fifty thousand dong to thirty thousand dong, "
                            "many students will buy coffee more often. This is the law of demand: "
                            "as price falls, the quantity demanded rises.\n\n"
                            "Supply is the quantity of a good or service that producers are willing to sell at a given price. "
                            "When the price goes up, producers want to sell more because they can earn higher profits. "
                            "If coffee shops can charge fifty thousand dong per cup instead of thirty thousand, "
                            "more shops will open and existing ones will make more coffee. "
                            "This is the law of supply: as price rises, the quantity supplied rises.\n\n"
                            "The market finds its equilibrium where the supply curve meets the demand curve. "
                            "At this point, the quantity that buyers want to purchase equals the quantity that sellers want to sell. "
                            "The price at equilibrium is called the market-clearing price. "
                            "No one is left wanting to buy more, and no seller is stuck with unsold goods.\n\n"
                            "But what happens when the price is not at equilibrium? "
                            "If the price is too high, sellers offer more than buyers want. "
                            "This creates a surplus — extra goods sit on shelves and sellers must lower prices to attract buyers. "
                            "On the other hand, if the price is too low, buyers want more than sellers can provide. "
                            "This creates a shortage — people line up, shelves go empty, and sellers may raise prices.\n\n"
                            "In both cases, the market pushes the price back toward equilibrium. "
                            "A surplus puts downward pressure on prices, while a shortage puts upward pressure. "
                            "Over time, the quantity bought and sold adjusts until supply equals demand once again. "
                            "This self-correcting process is one of the most powerful ideas in economics."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cung và cầu cơ bản",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every day, millions of buyers and sellers make decisions that shape the prices we see in markets. "
                            "To understand how prices are set, economists study two basic forces: supply and demand.\n\n"
                            "Demand is the quantity of a good or service that consumers are willing to buy at a given price. "
                            "When the price of a product goes down, people usually want to buy more of it. "
                            "For example, if the price of a cup of coffee drops from fifty thousand dong to thirty thousand dong, "
                            "many students will buy coffee more often. This is the law of demand: "
                            "as price falls, the quantity demanded rises.\n\n"
                            "Supply is the quantity of a good or service that producers are willing to sell at a given price. "
                            "When the price goes up, producers want to sell more because they can earn higher profits. "
                            "If coffee shops can charge fifty thousand dong per cup instead of thirty thousand, "
                            "more shops will open and existing ones will make more coffee. "
                            "This is the law of supply: as price rises, the quantity supplied rises.\n\n"
                            "The market finds its equilibrium where the supply curve meets the demand curve. "
                            "At this point, the quantity that buyers want to purchase equals the quantity that sellers want to sell. "
                            "The price at equilibrium is called the market-clearing price. "
                            "No one is left wanting to buy more, and no seller is stuck with unsold goods.\n\n"
                            "But what happens when the price is not at equilibrium? "
                            "If the price is too high, sellers offer more than buyers want. "
                            "This creates a surplus — extra goods sit on shelves and sellers must lower prices to attract buyers. "
                            "On the other hand, if the price is too low, buyers want more than sellers can provide. "
                            "This creates a shortage — people line up, shelves go empty, and sellers may raise prices.\n\n"
                            "In both cases, the market pushes the price back toward equilibrium. "
                            "A surplus puts downward pressure on prices, while a shortage puts upward pressure. "
                            "Over time, the quantity bought and sold adjusts until supply equals demand once again. "
                            "This self-correcting process is one of the most powerful ideas in economics."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cung và cầu cơ bản",
                    "description": "Viết câu sử dụng 6 từ vựng về cung và cầu.",
                    "data": {
                        "vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"],
                        "items": [
                            {
                                "targetVocab": "supply",
                                "prompt": "Dùng từ 'supply' để viết một câu về lượng hàng hóa mà người bán cung cấp ra thị trường khi giá thay đổi. Ví dụ: The supply of fresh vegetables increases during the harvest season because farmers bring more produce to the market."
                            },
                            {
                                "targetVocab": "demand",
                                "prompt": "Dùng từ 'demand' để viết một câu về nhu cầu mua hàng của người tiêu dùng khi giá giảm. Ví dụ: The demand for air conditioners rises sharply during the summer months as temperatures climb above thirty-five degrees."
                            },
                            {
                                "targetVocab": "equilibrium",
                                "prompt": "Dùng từ 'equilibrium' để viết một câu về trạng thái cân bằng của thị trường khi cung gặp cầu. Ví dụ: The rice market reached equilibrium at a price where farmers were happy to sell and consumers were willing to buy."
                            },
                            {
                                "targetVocab": "surplus",
                                "prompt": "Dùng từ 'surplus' để viết một câu về tình trạng thặng dư khi hàng hóa dư thừa trên thị trường. Ví dụ: The surplus of unsold motorbikes forced dealers to offer large discounts at the end of the year."
                            },
                            {
                                "targetVocab": "shortage",
                                "prompt": "Dùng từ 'shortage' để viết một câu về tình trạng thiếu hụt hàng hóa khi nhu cầu vượt quá nguồn cung. Ví dụ: A shortage of affordable housing in the city has pushed many young workers to rent rooms far from their offices."
                            },
                            {
                                "targetVocab": "quantity",
                                "prompt": "Dùng từ 'quantity' để viết một câu về số lượng hàng hóa được mua hoặc bán tại một mức giá cụ thể. Ví dụ: The quantity of coffee sold at the campus shop doubles during exam week when students need extra energy."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 2: Words 7-12 ─────────────────────────────
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Ôn lại phần 1 và học 6 từ mới về độ co giãn và động lực thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "supply — nguồn cung, demand — nhu cầu, equilibrium — trạng thái cân bằng, "
                            "surplus — thặng dư, shortage — thiếu hụt, và quantity — số lượng. "
                            "Bạn đã hiểu cách thị trường tự điều chỉnh khi cung gặp cầu. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào cơ chế thị trường.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: elasticity, substitute, complement, shift, curve, và price. "
                            "Những từ này giúp bạn phân tích thị trường ở mức độ tinh vi hơn — "
                            "không chỉ biết cung cầu gặp nhau ở đâu, mà còn hiểu thị trường phản ứng mạnh hay yếu "
                            "khi điều kiện thay đổi.\n\n"
                            "Từ đầu tiên là elasticity — danh từ — nghĩa là độ co giãn, "
                            "mức độ phản ứng của lượng cầu hoặc lượng cung khi giá thay đổi. "
                            "Ví dụ: 'The elasticity of demand for luxury goods is high because people can easily stop buying them when prices rise.' "
                            "Trong bài đọc, elasticity giúp giải thích vì sao một số sản phẩm nhạy cảm với giá hơn những sản phẩm khác.\n\n"
                            "Từ thứ hai là substitute — danh từ — nghĩa là hàng thay thế, "
                            "sản phẩm có thể được dùng thay cho sản phẩm khác. "
                            "Ví dụ: 'Tea is a common substitute for coffee — when coffee prices go up, many people switch to tea.' "
                            "Trong bài đọc, substitute xuất hiện khi phân tích cách người tiêu dùng chuyển đổi giữa các sản phẩm.\n\n"
                            "Từ thứ ba là complement — danh từ — nghĩa là hàng bổ sung, "
                            "sản phẩm thường được mua cùng với sản phẩm khác. "
                            "Ví dụ: 'Printers and ink cartridges are complements — if printer prices drop, ink sales often rise.' "
                            "Trong bài đọc, complement cho thấy mối quan hệ giữa các sản phẩm liên quan trên thị trường.\n\n"
                            "Từ thứ tư là shift — danh từ và động từ — nghĩa là sự dịch chuyển, "
                            "khi toàn bộ đường cung hoặc đường cầu di chuyển sang trái hoặc phải. "
                            "Ví dụ: 'A shift in demand occurs when consumer preferences change, not just when prices change.' "
                            "Trong bài đọc, shift mô tả những thay đổi lớn trên thị trường — "
                            "khác với việc di chuyển dọc theo đường cung cầu.\n\n"
                            "Từ thứ năm là curve — danh từ — nghĩa là đường cong, "
                            "đường biểu diễn mối quan hệ giữa giá và lượng trên đồ thị. "
                            "Ví dụ: 'The demand curve slopes downward because people buy less when prices are higher.' "
                            "Trong bài đọc, curve là công cụ trực quan giúp bạn hình dung cung cầu trên đồ thị.\n\n"
                            "Từ cuối cùng là price — danh từ — nghĩa là giá cả, "
                            "số tiền mà người mua trả và người bán nhận cho một đơn vị hàng hóa. "
                            "Ví dụ: 'The price of gasoline affects almost every other product because transportation costs change.' "
                            "Trong bài đọc, price là biến số trung tâm — mọi phân tích cung cầu đều xoay quanh giá.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về độ co giãn và động lực thị trường nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Độ co giãn và động lực thị trường",
                    "description": "Học 6 từ: elasticity, substitute, complement, shift, curve, price",
                    "data": {"vocabList": ["elasticity", "substitute", "complement", "shift", "curve", "price"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Độ co giãn và động lực thị trường",
                    "description": "Học 6 từ: elasticity, substitute, complement, shift, curve, price",
                    "data": {"vocabList": ["elasticity", "substitute", "complement", "shift", "curve", "price"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Độ co giãn và động lực thị trường",
                    "description": "Học 6 từ: elasticity, substitute, complement, shift, curve, price",
                    "data": {"vocabList": ["elasticity", "substitute", "complement", "shift", "curve", "price"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Độ co giãn và động lực thị trường",
                    "description": "Học 6 từ: elasticity, substitute, complement, shift, curve, price",
                    "data": {"vocabList": ["elasticity", "substitute", "complement", "shift", "curve", "price"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Độ co giãn và động lực thị trường",
                    "description": "Học 6 từ: elasticity, substitute, complement, shift, curve, price",
                    "data": {"vocabList": ["elasticity", "substitute", "complement", "shift", "curve", "price"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Độ co giãn và phản ứng thị trường",
                    "description": "Understanding how markets respond to change requires more than knowing where supply meets demand.",
                    "data": {
                        "text": (
                            "Understanding how markets respond to change requires more than knowing where supply meets demand. "
                            "Economists use a concept called elasticity to measure how sensitive buyers and sellers are to price changes.\n\n"
                            "Elasticity tells us how much the quantity demanded or supplied changes when the price goes up or down. "
                            "Some goods have high elasticity — a small change in price leads to a big change in quantity. "
                            "Luxury items like designer bags are a good example. "
                            "If the price rises by ten percent, many buyers will simply stop purchasing. "
                            "Other goods have low elasticity. Rice, for instance, is a daily necessity in Vietnam. "
                            "Even if the price increases, people still need to buy it.\n\n"
                            "Elasticity also depends on whether a good has a close substitute. "
                            "A substitute is a product that can replace another. "
                            "If the price of Coca-Cola rises, many consumers will switch to Pepsi because it serves the same purpose. "
                            "The more substitutes a product has, the more elastic its demand tends to be.\n\n"
                            "Some products are complements — they are used together. "
                            "A complement is a good that people buy alongside another good. "
                            "Motorbikes and gasoline are complements in Vietnam. "
                            "When gasoline prices rise, people may ride their motorbikes less, "
                            "which can reduce the demand for motorbike accessories too.\n\n"
                            "Markets do not stay still. When something other than price changes — "
                            "like consumer income, tastes, or technology — the entire demand or supply curve can shift. "
                            "A shift means the whole curve moves to the left or right on the graph. "
                            "For example, if a new health study says that drinking green tea prevents disease, "
                            "the demand curve for green tea shifts to the right. "
                            "At every price level, consumers now want to buy more.\n\n"
                            "The supply curve and the demand curve are the two most important tools in microeconomics. "
                            "The demand curve slopes downward — as price falls, quantity demanded rises. "
                            "The supply curve slopes upward — as price rises, quantity supplied rises. "
                            "Where the two curves cross, the market finds its price.\n\n"
                            "Price is the signal that coordinates millions of decisions. "
                            "When the price of a product rises, it tells producers to make more and consumers to buy less. "
                            "When the price falls, it tells producers to cut back and consumers to buy more. "
                            "This constant adjustment through price is what keeps markets moving toward balance."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Độ co giãn và phản ứng thị trường",
                    "description": "Understanding how markets respond to change requires more than knowing where supply meets demand.",
                    "data": {
                        "text": (
                            "Understanding how markets respond to change requires more than knowing where supply meets demand. "
                            "Economists use a concept called elasticity to measure how sensitive buyers and sellers are to price changes.\n\n"
                            "Elasticity tells us how much the quantity demanded or supplied changes when the price goes up or down. "
                            "Some goods have high elasticity — a small change in price leads to a big change in quantity. "
                            "Luxury items like designer bags are a good example. "
                            "If the price rises by ten percent, many buyers will simply stop purchasing. "
                            "Other goods have low elasticity. Rice, for instance, is a daily necessity in Vietnam. "
                            "Even if the price increases, people still need to buy it.\n\n"
                            "Elasticity also depends on whether a good has a close substitute. "
                            "A substitute is a product that can replace another. "
                            "If the price of Coca-Cola rises, many consumers will switch to Pepsi because it serves the same purpose. "
                            "The more substitutes a product has, the more elastic its demand tends to be.\n\n"
                            "Some products are complements — they are used together. "
                            "A complement is a good that people buy alongside another good. "
                            "Motorbikes and gasoline are complements in Vietnam. "
                            "When gasoline prices rise, people may ride their motorbikes less, "
                            "which can reduce the demand for motorbike accessories too.\n\n"
                            "Markets do not stay still. When something other than price changes — "
                            "like consumer income, tastes, or technology — the entire demand or supply curve can shift. "
                            "A shift means the whole curve moves to the left or right on the graph. "
                            "For example, if a new health study says that drinking green tea prevents disease, "
                            "the demand curve for green tea shifts to the right. "
                            "At every price level, consumers now want to buy more.\n\n"
                            "The supply curve and the demand curve are the two most important tools in microeconomics. "
                            "The demand curve slopes downward — as price falls, quantity demanded rises. "
                            "The supply curve slopes upward — as price rises, quantity supplied rises. "
                            "Where the two curves cross, the market finds its price.\n\n"
                            "Price is the signal that coordinates millions of decisions. "
                            "When the price of a product rises, it tells producers to make more and consumers to buy less. "
                            "When the price falls, it tells producers to cut back and consumers to buy more. "
                            "This constant adjustment through price is what keeps markets moving toward balance."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Độ co giãn và phản ứng thị trường",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Understanding how markets respond to change requires more than knowing where supply meets demand. "
                            "Economists use a concept called elasticity to measure how sensitive buyers and sellers are to price changes.\n\n"
                            "Elasticity tells us how much the quantity demanded or supplied changes when the price goes up or down. "
                            "Some goods have high elasticity — a small change in price leads to a big change in quantity. "
                            "Luxury items like designer bags are a good example. "
                            "If the price rises by ten percent, many buyers will simply stop purchasing. "
                            "Other goods have low elasticity. Rice, for instance, is a daily necessity in Vietnam. "
                            "Even if the price increases, people still need to buy it.\n\n"
                            "Elasticity also depends on whether a good has a close substitute. "
                            "A substitute is a product that can replace another. "
                            "If the price of Coca-Cola rises, many consumers will switch to Pepsi because it serves the same purpose. "
                            "The more substitutes a product has, the more elastic its demand tends to be.\n\n"
                            "Some products are complements — they are used together. "
                            "A complement is a good that people buy alongside another good. "
                            "Motorbikes and gasoline are complements in Vietnam. "
                            "When gasoline prices rise, people may ride their motorbikes less, "
                            "which can reduce the demand for motorbike accessories too.\n\n"
                            "Markets do not stay still. When something other than price changes — "
                            "like consumer income, tastes, or technology — the entire demand or supply curve can shift. "
                            "A shift means the whole curve moves to the left or right on the graph. "
                            "For example, if a new health study says that drinking green tea prevents disease, "
                            "the demand curve for green tea shifts to the right. "
                            "At every price level, consumers now want to buy more.\n\n"
                            "The supply curve and the demand curve are the two most important tools in microeconomics. "
                            "The demand curve slopes downward — as price falls, quantity demanded rises. "
                            "The supply curve slopes upward — as price rises, quantity supplied rises. "
                            "Where the two curves cross, the market finds its price.\n\n"
                            "Price is the signal that coordinates millions of decisions. "
                            "When the price of a product rises, it tells producers to make more and consumers to buy less. "
                            "When the price falls, it tells producers to cut back and consumers to buy more. "
                            "This constant adjustment through price is what keeps markets moving toward balance."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Độ co giãn và động lực thị trường",
                    "description": "Viết câu sử dụng 6 từ vựng về độ co giãn và thị trường.",
                    "data": {
                        "vocabList": ["elasticity", "substitute", "complement", "shift", "curve", "price"],
                        "items": [
                            {
                                "targetVocab": "elasticity",
                                "prompt": "Dùng từ 'elasticity' để viết một câu về mức độ nhạy cảm của người tiêu dùng với sự thay đổi giá của một sản phẩm. Ví dụ: The elasticity of demand for bottled water is low because people need water regardless of how much it costs."
                            },
                            {
                                "targetVocab": "substitute",
                                "prompt": "Dùng từ 'substitute' để viết một câu về việc người tiêu dùng chuyển sang sản phẩm thay thế khi giá tăng. Ví dụ: When the price of beef rises, chicken becomes a popular substitute for families on a tight budget."
                            },
                            {
                                "targetVocab": "complement",
                                "prompt": "Dùng từ 'complement' để viết một câu về hai sản phẩm thường được mua cùng nhau. Ví dụ: Smartphones and phone cases are complements — when a new phone model launches, case sales increase immediately."
                            },
                            {
                                "targetVocab": "shift",
                                "prompt": "Dùng từ 'shift' để viết một câu về sự dịch chuyển của đường cung hoặc đường cầu khi có yếu tố ngoài giá thay đổi. Ví dụ: The growing popularity of electric vehicles caused a shift in the demand curve for gasoline to the left."
                            },
                            {
                                "targetVocab": "curve",
                                "prompt": "Dùng từ 'curve' để viết một câu về đường cung hoặc đường cầu trên đồ thị kinh tế. Ví dụ: The supply curve for handmade goods slopes upward steeply because production cannot increase quickly."
                            },
                            {
                                "targetVocab": "price",
                                "prompt": "Dùng từ 'price' để viết một câu về vai trò của giá cả trong việc điều phối quyết định mua bán trên thị trường. Ví dụ: The price of organic vegetables is higher than regular ones, but many health-conscious consumers are willing to pay the difference."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 3: Words 13-18 ────────────────────────────
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về phân bổ nguồn lực và chính sách giá.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: supply, demand, equilibrium, surplus, shortage, quantity — "
                            "những khái niệm cơ bản về cách thị trường hoạt động. "
                            "Trong phần 2, bạn đã học thêm elasticity, substitute, complement, shift, curve, price — "
                            "giúp bạn hiểu thị trường phản ứng như thế nào khi điều kiện thay đổi.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh quan trọng khác: "
                            "khi thị trường không thể tự giải quyết vấn đề, chính phủ can thiệp như thế nào? "
                            "Bạn sẽ học 6 từ mới: allocate, ration, ceiling, floor, incentive, và scarcity.\n\n"
                            "Từ đầu tiên là allocate — động từ — nghĩa là phân bổ, "
                            "chia nguồn lực cho các mục đích hoặc đối tượng khác nhau. "
                            "Ví dụ: 'The government must allocate limited vaccine doses to the groups that need them most.' "
                            "Trong bài đọc, allocate được dùng khi nói về cách xã hội quyết định ai nhận được gì "
                            "khi nguồn lực có hạn.\n\n"
                            "Từ thứ hai là ration — động từ — nghĩa là phân phối theo định mức, "
                            "giới hạn lượng hàng hóa mỗi người được mua hoặc nhận. "
                            "Ví dụ: 'During the oil crisis, the government had to ration gasoline so that everyone could get a fair share.' "
                            "Trong bài đọc, ration xuất hiện khi mô tả biện pháp kiểm soát phân phối "
                            "trong thời kỳ khan hiếm.\n\n"
                            "Từ thứ ba là ceiling — danh từ — trong kinh tế nghĩa là giá trần, "
                            "mức giá tối đa mà chính phủ cho phép. "
                            "Ví dụ: 'The city set a rent ceiling to prevent landlords from charging too much during the housing crisis.' "
                            "Trong bài đọc, ceiling là một công cụ chính sách — "
                            "chính phủ đặt giá trần để bảo vệ người tiêu dùng, nhưng điều này có thể gây ra shortage.\n\n"
                            "Từ thứ tư là floor — danh từ — trong kinh tế nghĩa là giá sàn, "
                            "mức giá tối thiểu mà chính phủ quy định. "
                            "Ví dụ: 'The government set a price floor for rice to protect farmers from earning too little.' "
                            "Trong bài đọc, floor là mặt đối lập của ceiling — "
                            "giá sàn bảo vệ người sản xuất nhưng có thể tạo ra surplus.\n\n"
                            "Từ thứ năm là incentive — danh từ — nghĩa là động lực, "
                            "yếu tố thúc đẩy người ta hành động theo một hướng nhất định. "
                            "Ví dụ: 'Tax breaks serve as an incentive for companies to invest in renewable energy.' "
                            "Trong bài đọc, incentive giải thích vì sao người mua và người bán "
                            "phản ứng với sự thay đổi giá — giá chính là incentive mạnh nhất trên thị trường.\n\n"
                            "Từ cuối cùng là scarcity — danh từ — nghĩa là sự khan hiếm, "
                            "tình trạng khi nguồn lực có hạn nhưng nhu cầu thì không. "
                            "Ví dụ: 'Scarcity is the fundamental problem of economics — there are never enough resources to satisfy all human wants.' "
                            "Trong bài đọc, scarcity là lý do tại sao chúng ta cần kinh tế học — "
                            "vì nguồn lực luôn có giới hạn, xã hội phải đưa ra lựa chọn.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về phân bổ nguồn lực và chính sách giá nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phân bổ nguồn lực và chính sách giá",
                    "description": "Học 6 từ: allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phân bổ nguồn lực và chính sách giá",
                    "description": "Học 6 từ: allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phân bổ nguồn lực và chính sách giá",
                    "description": "Học 6 từ: allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phân bổ nguồn lực và chính sách giá",
                    "description": "Học 6 từ: allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phân bổ nguồn lực và chính sách giá",
                    "description": "Học 6 từ: allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phân bổ nguồn lực và kiểm soát giá",
                    "description": "Every society faces a basic problem: there are not enough resources to give everyone everything they want.",
                    "data": {
                        "text": (
                            "Every society faces a basic problem: there are not enough resources to give everyone everything they want. "
                            "This condition is called scarcity, and it is the reason economics exists as a field of study. "
                            "Because of scarcity, societies must decide how to allocate their limited resources.\n\n"
                            "In a free market, prices do most of the work of allocation. "
                            "When a product becomes scarce, its price rises. "
                            "The higher price creates an incentive for producers to make more and for consumers to use less. "
                            "Over time, the market moves toward a new equilibrium. "
                            "This is the invisible hand at work — no central planner is needed.\n\n"
                            "But sometimes governments decide that the market price is unfair. "
                            "They may set a price ceiling — a maximum price that sellers can charge. "
                            "Rent control is a common example. In many cities, the government sets a ceiling on how much landlords can charge for apartments. "
                            "The goal is to keep housing affordable for low-income families.\n\n"
                            "However, a price ceiling set below the equilibrium price creates problems. "
                            "At the lower price, more people want to rent apartments, but fewer landlords want to offer them. "
                            "The result is a shortage. Long waiting lists form, and some people cannot find housing at all. "
                            "The ceiling helps those who get an apartment, but it hurts those who are left out.\n\n"
                            "Governments can also set a price floor — a minimum price that buyers must pay. "
                            "The minimum wage is a well-known price floor. "
                            "It ensures that workers earn at least a certain amount per hour. "
                            "But if the floor is set above the equilibrium wage, some employers will hire fewer workers, "
                            "creating a surplus of labor — in other words, unemployment.\n\n"
                            "When price controls cause shortages, governments sometimes step in to ration goods directly. "
                            "To ration means to limit how much each person can buy. "
                            "During wartime or natural disasters, governments may issue ration cards "
                            "so that everyone gets a fair share of food, fuel, or medicine.\n\n"
                            "Each of these tools — ceilings, floors, rationing — tries to solve a problem caused by scarcity. "
                            "But each also creates new trade-offs. "
                            "The incentive structure changes when prices are controlled: "
                            "producers may have less reason to increase supply, and consumers may have less reason to conserve. "
                            "Understanding these trade-offs is at the heart of microeconomic analysis."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phân bổ nguồn lực và kiểm soát giá",
                    "description": "Every society faces a basic problem: there are not enough resources to give everyone everything they want.",
                    "data": {
                        "text": (
                            "Every society faces a basic problem: there are not enough resources to give everyone everything they want. "
                            "This condition is called scarcity, and it is the reason economics exists as a field of study. "
                            "Because of scarcity, societies must decide how to allocate their limited resources.\n\n"
                            "In a free market, prices do most of the work of allocation. "
                            "When a product becomes scarce, its price rises. "
                            "The higher price creates an incentive for producers to make more and for consumers to use less. "
                            "Over time, the market moves toward a new equilibrium. "
                            "This is the invisible hand at work — no central planner is needed.\n\n"
                            "But sometimes governments decide that the market price is unfair. "
                            "They may set a price ceiling — a maximum price that sellers can charge. "
                            "Rent control is a common example. In many cities, the government sets a ceiling on how much landlords can charge for apartments. "
                            "The goal is to keep housing affordable for low-income families.\n\n"
                            "However, a price ceiling set below the equilibrium price creates problems. "
                            "At the lower price, more people want to rent apartments, but fewer landlords want to offer them. "
                            "The result is a shortage. Long waiting lists form, and some people cannot find housing at all. "
                            "The ceiling helps those who get an apartment, but it hurts those who are left out.\n\n"
                            "Governments can also set a price floor — a minimum price that buyers must pay. "
                            "The minimum wage is a well-known price floor. "
                            "It ensures that workers earn at least a certain amount per hour. "
                            "But if the floor is set above the equilibrium wage, some employers will hire fewer workers, "
                            "creating a surplus of labor — in other words, unemployment.\n\n"
                            "When price controls cause shortages, governments sometimes step in to ration goods directly. "
                            "To ration means to limit how much each person can buy. "
                            "During wartime or natural disasters, governments may issue ration cards "
                            "so that everyone gets a fair share of food, fuel, or medicine.\n\n"
                            "Each of these tools — ceilings, floors, rationing — tries to solve a problem caused by scarcity. "
                            "But each also creates new trade-offs. "
                            "The incentive structure changes when prices are controlled: "
                            "producers may have less reason to increase supply, and consumers may have less reason to conserve. "
                            "Understanding these trade-offs is at the heart of microeconomic analysis."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phân bổ nguồn lực và kiểm soát giá",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every society faces a basic problem: there are not enough resources to give everyone everything they want. "
                            "This condition is called scarcity, and it is the reason economics exists as a field of study. "
                            "Because of scarcity, societies must decide how to allocate their limited resources.\n\n"
                            "In a free market, prices do most of the work of allocation. "
                            "When a product becomes scarce, its price rises. "
                            "The higher price creates an incentive for producers to make more and for consumers to use less. "
                            "Over time, the market moves toward a new equilibrium. "
                            "This is the invisible hand at work — no central planner is needed.\n\n"
                            "But sometimes governments decide that the market price is unfair. "
                            "They may set a price ceiling — a maximum price that sellers can charge. "
                            "Rent control is a common example. In many cities, the government sets a ceiling on how much landlords can charge for apartments. "
                            "The goal is to keep housing affordable for low-income families.\n\n"
                            "However, a price ceiling set below the equilibrium price creates problems. "
                            "At the lower price, more people want to rent apartments, but fewer landlords want to offer them. "
                            "The result is a shortage. Long waiting lists form, and some people cannot find housing at all. "
                            "The ceiling helps those who get an apartment, but it hurts those who are left out.\n\n"
                            "Governments can also set a price floor — a minimum price that buyers must pay. "
                            "The minimum wage is a well-known price floor. "
                            "It ensures that workers earn at least a certain amount per hour. "
                            "But if the floor is set above the equilibrium wage, some employers will hire fewer workers, "
                            "creating a surplus of labor — in other words, unemployment.\n\n"
                            "When price controls cause shortages, governments sometimes step in to ration goods directly. "
                            "To ration means to limit how much each person can buy. "
                            "During wartime or natural disasters, governments may issue ration cards "
                            "so that everyone gets a fair share of food, fuel, or medicine.\n\n"
                            "Each of these tools — ceilings, floors, rationing — tries to solve a problem caused by scarcity. "
                            "But each also creates new trade-offs. "
                            "The incentive structure changes when prices are controlled: "
                            "producers may have less reason to increase supply, and consumers may have less reason to conserve. "
                            "Understanding these trade-offs is at the heart of microeconomic analysis."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phân bổ nguồn lực và chính sách giá",
                    "description": "Viết câu sử dụng 6 từ vựng về phân bổ nguồn lực.",
                    "data": {
                        "vocabList": ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"],
                        "items": [
                            {
                                "targetVocab": "allocate",
                                "prompt": "Dùng từ 'allocate' để viết một câu về cách chính phủ hoặc tổ chức phân bổ nguồn lực có hạn cho các mục đích khác nhau. Ví dụ: The university must allocate its limited scholarship funds to students who demonstrate both financial need and academic excellence."
                            },
                            {
                                "targetVocab": "ration",
                                "prompt": "Dùng từ 'ration' để viết một câu về việc giới hạn lượng hàng hóa mỗi người được mua trong thời kỳ khan hiếm. Ví dụ: During the severe drought, the local government had to ration clean water to ensure every household received at least fifty liters per day."
                            },
                            {
                                "targetVocab": "ceiling",
                                "prompt": "Dùng từ 'ceiling' để viết một câu về chính sách giá trần mà chính phủ áp dụng để bảo vệ người tiêu dùng. Ví dụ: The government imposed a ceiling on the price of cooking oil to prevent stores from overcharging during the food shortage."
                            },
                            {
                                "targetVocab": "floor",
                                "prompt": "Dùng từ 'floor' để viết một câu về chính sách giá sàn nhằm bảo vệ người sản xuất hoặc người lao động. Ví dụ: Setting a floor on the price of coffee beans helps small farmers earn enough income to cover their production costs."
                            },
                            {
                                "targetVocab": "incentive",
                                "prompt": "Dùng từ 'incentive' để viết một câu về yếu tố thúc đẩy hành vi kinh tế của người mua hoặc người bán. Ví dụ: The tax reduction on electric cars serves as a strong incentive for consumers to switch from gasoline-powered vehicles."
                            },
                            {
                                "targetVocab": "scarcity",
                                "prompt": "Dùng từ 'scarcity' để viết một câu về tình trạng khan hiếm nguồn lực và tác động của nó đến quyết định kinh tế. Ví dụ: The scarcity of clean water in many developing countries forces communities to make difficult choices about how to use every drop."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 4: Review (all 18 words) ─────────────────
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Cùng ôn lại trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Cung và Cầu. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "supply — nguồn cung, demand — nhu cầu, equilibrium — cân bằng thị trường, "
                            "surplus — thặng dư, shortage — thiếu hụt, và quantity — số lượng. "
                            "Đây là bộ khung cơ bản để hiểu bất kỳ thị trường nào.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "elasticity — độ co giãn, substitute — hàng thay thế, complement — hàng bổ sung, "
                            "shift — sự dịch chuyển, curve — đường cong, và price — giá cả. "
                            "Những từ này giúp bạn phân tích cách thị trường phản ứng với thay đổi.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "allocate — phân bổ, ration — phân phối theo định mức, ceiling — giá trần, "
                            "floor — giá sàn, incentive — động lực, và scarcity — sự khan hiếm. "
                            "Đây là những từ về chính sách và can thiệp của chính phủ vào thị trường.\n\n"
                            "Bây giờ, phần ôn tập này sẽ giúp bạn củng cố toàn bộ 18 từ vựng. "
                            "Bạn sẽ xem lại flashcard, luyện phát âm, và viết câu với tất cả các từ. "
                            "Sau phần ôn tập, bạn sẽ sẵn sàng cho bài đọc tổng hợp — "
                            "một bài viết dài hơn sử dụng cả 18 từ trong một ngữ cảnh liền mạch. "
                            "Hãy bắt đầu nào!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: supply, demand, equilibrium, surplus, shortage, quantity, elasticity, substitute, complement, shift, curve, price, allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: supply, demand, equilibrium, surplus, shortage, quantity, elasticity, substitute, complement, shift, curve, price, allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: supply, demand, equilibrium, surplus, shortage, quantity, elasticity, substitute, complement, shift, curve, price, allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: supply, demand, equilibrium, surplus, shortage, quantity, elasticity, substitute, complement, shift, curve, price, allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: supply, demand, equilibrium, surplus, shortage, quantity, elasticity, substitute, complement, shift, curve, price, allocate, ration, ceiling, floor, incentive, scarcity",
                    "data": {"vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng cung và cầu",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"],
                        "items": [
                            {
                                "targetVocab": "supply",
                                "prompt": "Dùng từ 'supply' để viết một câu về nguồn cung hàng hóa trên thị trường nông sản Việt Nam. Ví dụ: The supply of dragon fruit from the Mekong Delta has grown rapidly as more farmers switch from rice to fruit cultivation."
                            },
                            {
                                "targetVocab": "demand",
                                "prompt": "Dùng từ 'demand' để viết một câu về nhu cầu tiêu dùng thay đổi theo mùa. Ví dụ: The demand for warm clothing in northern Vietnam peaks in December and January when temperatures drop below ten degrees."
                            },
                            {
                                "targetVocab": "equilibrium",
                                "prompt": "Dùng từ 'equilibrium' để viết một câu về điểm cân bằng giá trên thị trường bất động sản. Ví dụ: The housing market in Ho Chi Minh City has not yet reached equilibrium because demand continues to outpace the supply of affordable apartments."
                            },
                            {
                                "targetVocab": "surplus",
                                "prompt": "Dùng từ 'surplus' để viết một câu về tình trạng dư thừa sản phẩm và cách doanh nghiệp xử lý. Ví dụ: The electronics store offered deep discounts to clear the surplus of last year's smartphone models before the new ones arrived."
                            },
                            {
                                "targetVocab": "shortage",
                                "prompt": "Dùng từ 'shortage' để viết một câu về tình trạng thiếu hụt nguồn nhân lực trong một ngành cụ thể. Ví dụ: Vietnam faces a shortage of skilled software engineers, which has driven up salaries in the technology sector."
                            },
                            {
                                "targetVocab": "quantity",
                                "prompt": "Dùng từ 'quantity' để viết một câu về mối quan hệ giữa số lượng hàng bán được và mức giá. Ví dụ: The quantity of organic milk sold at the supermarket tripled after the store reduced the price by twenty percent."
                            },
                            {
                                "targetVocab": "elasticity",
                                "prompt": "Dùng từ 'elasticity' để viết một câu so sánh độ co giãn của hai loại hàng hóa khác nhau. Ví dụ: The elasticity of demand for luxury handbags is much higher than for rice, because people can easily live without expensive bags but not without food."
                            },
                            {
                                "targetVocab": "substitute",
                                "prompt": "Dùng từ 'substitute' để viết một câu về sản phẩm thay thế trong ngành đồ uống. Ví dụ: Soy milk has become a popular substitute for dairy milk among Vietnamese consumers who are lactose intolerant."
                            },
                            {
                                "targetVocab": "complement",
                                "prompt": "Dùng từ 'complement' để viết một câu về hai sản phẩm bổ sung cho nhau trong đời sống hàng ngày. Ví dụ: Instant noodles and eggs are complements in many Vietnamese households — when noodle prices drop, egg sales often increase too."
                            },
                            {
                                "targetVocab": "shift",
                                "prompt": "Dùng từ 'shift' để viết một câu về sự dịch chuyển đường cầu do thay đổi thị hiếu người tiêu dùng. Ví dụ: The growing awareness of health risks from sugary drinks caused a shift in the demand curve for bottled water to the right."
                            },
                            {
                                "targetVocab": "curve",
                                "prompt": "Dùng từ 'curve' để viết một câu mô tả hình dạng của đường cung hoặc đường cầu trên đồ thị. Ví dụ: The supply curve for seasonal fruits is nearly vertical in the short run because farmers cannot instantly grow more mangoes."
                            },
                            {
                                "targetVocab": "price",
                                "prompt": "Dùng từ 'price' để viết một câu về vai trò của giá cả như tín hiệu trên thị trường. Ví dụ: A rising price for computer chips signals to manufacturers that they should invest in building new factories to increase production."
                            },
                            {
                                "targetVocab": "allocate",
                                "prompt": "Dùng từ 'allocate' để viết một câu về cách một tổ chức phân bổ ngân sách cho các dự án khác nhau. Ví dụ: The company decided to allocate sixty percent of its annual budget to research and development to stay competitive."
                            },
                            {
                                "targetVocab": "ration",
                                "prompt": "Dùng từ 'ration' để viết một câu về việc phân phối hàng hóa theo định mức trong tình huống khẩn cấp. Ví dụ: After the typhoon destroyed the water treatment plant, authorities had to ration bottled water to two liters per person per day."
                            },
                            {
                                "targetVocab": "ceiling",
                                "prompt": "Dùng từ 'ceiling' để viết một câu về chính sách giá trần và tác động của nó đến thị trường. Ví dụ: The government placed a ceiling on the price of face masks during the pandemic, but the policy led to long lines at pharmacies."
                            },
                            {
                                "targetVocab": "floor",
                                "prompt": "Dùng từ 'floor' để viết một câu về chính sách giá sàn và ảnh hưởng đến người sản xuất. Ví dụ: The price floor on domestic sugar protects local farmers but makes Vietnamese candy more expensive than imported alternatives."
                            },
                            {
                                "targetVocab": "incentive",
                                "prompt": "Dùng từ 'incentive' để viết một câu về chính sách khuyến khích đầu tư vào năng lượng sạch. Ví dụ: The government offers tax incentives to companies that install solar panels on their factory rooftops."
                            },
                            {
                                "targetVocab": "scarcity",
                                "prompt": "Dùng từ 'scarcity' để viết một câu về sự khan hiếm tài nguyên thiên nhiên và tác động kinh tế. Ví dụ: The scarcity of rare earth minerals used in smartphone batteries has pushed technology companies to invest in recycling programs."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 5: Full reading + farewell ────────────────
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc tổng hợp",
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về cung và cầu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về cung và cầu — từ những nguyên lý cơ bản "
                            "đến chính sách can thiệp của chính phủ.\n\n"
                            "Bạn sẽ gặp lại supply, demand, equilibrium, surplus, shortage, quantity "
                            "trong phần mở đầu về cơ chế thị trường. "
                            "Tiếp theo, elasticity, substitute, complement, shift, curve, price "
                            "sẽ giúp bạn hiểu sâu hơn về cách thị trường phản ứng. "
                            "Và cuối cùng, allocate, ration, ceiling, floor, incentive, scarcity "
                            "sẽ đưa bạn vào thế giới chính sách kinh tế.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cung và cầu — Bức tranh toàn cảnh",
                    "description": "Economics begins with a simple observation: people have unlimited wants, but the world has limited resources.",
                    "data": {
                        "text": (
                            "Economics begins with a simple observation: people have unlimited wants, but the world has limited resources. "
                            "This fundamental condition — scarcity — forces every society to make choices. "
                            "How should we allocate land, labor, and capital? "
                            "Who gets what, and how much? "
                            "The study of supply and demand gives us a framework to answer these questions.\n\n"
                            "In any market, two forces interact. "
                            "Demand represents the quantity of a good that consumers are willing and able to buy at each price level. "
                            "Supply represents the quantity that producers are willing and able to sell. "
                            "When we draw these relationships on a graph, we get two curves. "
                            "The demand curve slopes downward: as the price falls, consumers want more. "
                            "The supply curve slopes upward: as the price rises, producers want to sell more.\n\n"
                            "Where the two curves cross, the market reaches equilibrium. "
                            "At this point, the quantity demanded equals the quantity supplied, "
                            "and there is no pressure for the price to change. "
                            "But markets rarely stay at equilibrium for long. "
                            "Changes in income, tastes, technology, or the cost of production can cause the entire curve to shift. "
                            "A shift in the demand curve to the right means consumers want more at every price. "
                            "A shift in the supply curve to the left means producers offer less.\n\n"
                            "How strongly buyers and sellers respond to price changes depends on elasticity. "
                            "If demand is elastic, a small price increase causes a large drop in quantity demanded. "
                            "Goods with many substitutes tend to have elastic demand. "
                            "A substitute is a product that serves a similar purpose — "
                            "if the price of one brand of coffee rises, consumers can easily switch to another. "
                            "In contrast, goods that are complements — products used together, "
                            "like cars and gasoline — show linked demand patterns. "
                            "When the price of gasoline rises, the demand for large cars may fall.\n\n"
                            "When the market price is above equilibrium, a surplus appears. "
                            "Sellers have more goods than buyers want, so they lower prices to clear their shelves. "
                            "When the price is below equilibrium, a shortage develops. "
                            "Buyers want more than sellers can provide, and prices tend to rise. "
                            "In both cases, the incentive created by changing prices pushes the market back toward balance.\n\n"
                            "Sometimes, however, governments decide that the market outcome is not acceptable. "
                            "They may impose a price ceiling — a legal maximum price — to protect consumers. "
                            "Rent control is a classic example: the government sets a ceiling on apartment rents "
                            "to keep housing affordable. But if the ceiling is below the equilibrium price, "
                            "landlords have less incentive to offer apartments, and a shortage results.\n\n"
                            "Governments may also set a price floor — a legal minimum price — to protect producers. "
                            "Agricultural price supports and minimum wage laws are common examples. "
                            "A floor above the equilibrium price can create a surplus: "
                            "more workers want jobs at the higher wage, but fewer employers are willing to hire.\n\n"
                            "When shortages become severe, governments sometimes ration goods directly, "
                            "limiting the quantity each person can buy. "
                            "Rationing ensures a more equal distribution, "
                            "but it also removes the price signal that normally guides allocation.\n\n"
                            "The story of supply and demand is, at its core, a story about scarcity and choice. "
                            "Every price, every surplus, every shortage reflects the tension between what people want "
                            "and what is available. Understanding these forces — and the trade-offs that come with "
                            "every policy intervention — is the first step toward thinking like an economist."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cung và cầu — Bức tranh toàn cảnh",
                    "description": "Economics begins with a simple observation: people have unlimited wants, but the world has limited resources.",
                    "data": {
                        "text": (
                            "Economics begins with a simple observation: people have unlimited wants, but the world has limited resources. "
                            "This fundamental condition — scarcity — forces every society to make choices. "
                            "How should we allocate land, labor, and capital? "
                            "Who gets what, and how much? "
                            "The study of supply and demand gives us a framework to answer these questions.\n\n"
                            "In any market, two forces interact. "
                            "Demand represents the quantity of a good that consumers are willing and able to buy at each price level. "
                            "Supply represents the quantity that producers are willing and able to sell. "
                            "When we draw these relationships on a graph, we get two curves. "
                            "The demand curve slopes downward: as the price falls, consumers want more. "
                            "The supply curve slopes upward: as the price rises, producers want to sell more.\n\n"
                            "Where the two curves cross, the market reaches equilibrium. "
                            "At this point, the quantity demanded equals the quantity supplied, "
                            "and there is no pressure for the price to change. "
                            "But markets rarely stay at equilibrium for long. "
                            "Changes in income, tastes, technology, or the cost of production can cause the entire curve to shift. "
                            "A shift in the demand curve to the right means consumers want more at every price. "
                            "A shift in the supply curve to the left means producers offer less.\n\n"
                            "How strongly buyers and sellers respond to price changes depends on elasticity. "
                            "If demand is elastic, a small price increase causes a large drop in quantity demanded. "
                            "Goods with many substitutes tend to have elastic demand. "
                            "A substitute is a product that serves a similar purpose — "
                            "if the price of one brand of coffee rises, consumers can easily switch to another. "
                            "In contrast, goods that are complements — products used together, "
                            "like cars and gasoline — show linked demand patterns. "
                            "When the price of gasoline rises, the demand for large cars may fall.\n\n"
                            "When the market price is above equilibrium, a surplus appears. "
                            "Sellers have more goods than buyers want, so they lower prices to clear their shelves. "
                            "When the price is below equilibrium, a shortage develops. "
                            "Buyers want more than sellers can provide, and prices tend to rise. "
                            "In both cases, the incentive created by changing prices pushes the market back toward balance.\n\n"
                            "Sometimes, however, governments decide that the market outcome is not acceptable. "
                            "They may impose a price ceiling — a legal maximum price — to protect consumers. "
                            "Rent control is a classic example: the government sets a ceiling on apartment rents "
                            "to keep housing affordable. But if the ceiling is below the equilibrium price, "
                            "landlords have less incentive to offer apartments, and a shortage results.\n\n"
                            "Governments may also set a price floor — a legal minimum price — to protect producers. "
                            "Agricultural price supports and minimum wage laws are common examples. "
                            "A floor above the equilibrium price can create a surplus: "
                            "more workers want jobs at the higher wage, but fewer employers are willing to hire.\n\n"
                            "When shortages become severe, governments sometimes ration goods directly, "
                            "limiting the quantity each person can buy. "
                            "Rationing ensures a more equal distribution, "
                            "but it also removes the price signal that normally guides allocation.\n\n"
                            "The story of supply and demand is, at its core, a story about scarcity and choice. "
                            "Every price, every surplus, every shortage reflects the tension between what people want "
                            "and what is available. Understanding these forces — and the trade-offs that come with "
                            "every policy intervention — is the first step toward thinking like an economist."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cung và cầu — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Economics begins with a simple observation: people have unlimited wants, but the world has limited resources. "
                            "This fundamental condition — scarcity — forces every society to make choices. "
                            "How should we allocate land, labor, and capital? "
                            "Who gets what, and how much? "
                            "The study of supply and demand gives us a framework to answer these questions.\n\n"
                            "In any market, two forces interact. "
                            "Demand represents the quantity of a good that consumers are willing and able to buy at each price level. "
                            "Supply represents the quantity that producers are willing and able to sell. "
                            "When we draw these relationships on a graph, we get two curves. "
                            "The demand curve slopes downward: as the price falls, consumers want more. "
                            "The supply curve slopes upward: as the price rises, producers want to sell more.\n\n"
                            "Where the two curves cross, the market reaches equilibrium. "
                            "At this point, the quantity demanded equals the quantity supplied, "
                            "and there is no pressure for the price to change. "
                            "But markets rarely stay at equilibrium for long. "
                            "Changes in income, tastes, technology, or the cost of production can cause the entire curve to shift. "
                            "A shift in the demand curve to the right means consumers want more at every price. "
                            "A shift in the supply curve to the left means producers offer less.\n\n"
                            "How strongly buyers and sellers respond to price changes depends on elasticity. "
                            "If demand is elastic, a small price increase causes a large drop in quantity demanded. "
                            "Goods with many substitutes tend to have elastic demand. "
                            "A substitute is a product that serves a similar purpose — "
                            "if the price of one brand of coffee rises, consumers can easily switch to another. "
                            "In contrast, goods that are complements — products used together, "
                            "like cars and gasoline — show linked demand patterns. "
                            "When the price of gasoline rises, the demand for large cars may fall.\n\n"
                            "When the market price is above equilibrium, a surplus appears. "
                            "Sellers have more goods than buyers want, so they lower prices to clear their shelves. "
                            "When the price is below equilibrium, a shortage develops. "
                            "Buyers want more than sellers can provide, and prices tend to rise. "
                            "In both cases, the incentive created by changing prices pushes the market back toward balance.\n\n"
                            "Sometimes, however, governments decide that the market outcome is not acceptable. "
                            "They may impose a price ceiling — a legal maximum price — to protect consumers. "
                            "Rent control is a classic example: the government sets a ceiling on apartment rents "
                            "to keep housing affordable. But if the ceiling is below the equilibrium price, "
                            "landlords have less incentive to offer apartments, and a shortage results.\n\n"
                            "Governments may also set a price floor — a legal minimum price — to protect producers. "
                            "Agricultural price supports and minimum wage laws are common examples. "
                            "A floor above the equilibrium price can create a surplus: "
                            "more workers want jobs at the higher wage, but fewer employers are willing to hire.\n\n"
                            "When shortages become severe, governments sometimes ration goods directly, "
                            "limiting the quantity each person can buy. "
                            "Rationing ensures a more equal distribution, "
                            "but it also removes the price signal that normally guides allocation.\n\n"
                            "The story of supply and demand is, at its core, a story about scarcity and choice. "
                            "Every price, every surplus, every shortage reflects the tension between what people want "
                            "and what is available. Understanding these forces — and the trade-offs that come with "
                            "every policy intervention — is the first step toward thinking like an economist."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích cung và cầu",
                    "description": "Viết đoạn văn tiếng Anh phân tích về cung và cầu sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity", "elasticity", "substitute", "complement", "shift", "curve", "price", "allocate", "ration", "ceiling", "floor", "incentive", "scarcity"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống kinh tế thực tế liên quan đến cung và cầu. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích điều gì xảy ra trên thị trường nhà ở khi chính phủ áp dụng giá trần (price ceiling) cho tiền thuê nhà. Giải thích tại sao chính sách này có thể tạo ra shortage, và người thuê nhà cũng như chủ nhà phản ứng như thế nào với incentive mới.",
                            "Hãy chọn một sản phẩm quen thuộc ở Việt Nam (ví dụ: cà phê, gạo, xăng) và phân tích elasticity của demand cho sản phẩm đó. Giải thích sản phẩm đó có substitute không, điều gì có thể gây ra shift trong đường cung hoặc đường cầu, và scarcity ảnh hưởng đến price như thế nào."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay ấm áp.",
                    "data": {
                        "text": (
                            "Bạn đã đi đến cuối hành trình rồi. Hãy dừng lại một chút và nhìn lại "
                            "quãng đường bạn vừa đi qua.\n\n"
                            "Khi bắt đầu bài học này, có thể bạn chỉ biết 'cung' và 'cầu' như hai khái niệm "
                            "mơ hồ trong sách giáo khoa. Nhưng bây giờ, bạn đã có một bộ công cụ ngôn ngữ "
                            "để đọc, hiểu và phân tích thị trường bằng tiếng Anh.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất.\n\n"
                            "Equilibrium — trạng thái cân bằng. Đây là điểm mà mọi thị trường hướng tới. "
                            "Hãy nghĩ về nó như thế này: khi bạn đổ nước vào một cái bình, nước sẽ tự tìm "
                            "mặt phẳng — thị trường cũng vậy, giá cả tự tìm đến equilibrium. "
                            "Ví dụ mới: After the holiday season ends, the price of airline tickets returns to equilibrium "
                            "as both demand from travelers and supply of seats normalize.\n\n"
                            "Elasticity — độ co giãn. Từ này cho bạn biết thị trường nhạy cảm đến mức nào. "
                            "Không phải mọi sản phẩm đều phản ứng giống nhau khi giá thay đổi. "
                            "Ví dụ mới: The elasticity of demand for university textbooks is very low because students "
                            "must buy them regardless of the price — there is no real alternative.\n\n"
                            "Scarcity — sự khan hiếm. Đây là từ nền tảng nhất trong kinh tế học. "
                            "Mọi thứ bạn học — từ cung cầu đến chính sách giá — đều bắt nguồn từ một sự thật đơn giản: "
                            "nguồn lực có hạn, nhưng mong muốn của con người thì không. "
                            "Ví dụ mới: The scarcity of time is something every student understands — "
                            "you cannot study for every subject and also enjoy a full social life.\n\n"
                            "Incentive — động lực. Kinh tế học, ở cốt lõi, là nghiên cứu về incentive. "
                            "Tại sao người ta làm những gì họ làm? Vì có động lực — có thể là tiền, "
                            "có thể là sự tiện lợi, có thể là nỗi sợ mất mát. "
                            "Ví dụ mới: Free parking at the shopping mall creates an incentive for people "
                            "to drive instead of taking public transportation.\n\n"
                            "Ceiling — giá trần. Khi chính phủ nói 'giá không được vượt quá mức này', "
                            "đó là ceiling. Nó bảo vệ người mua, nhưng cũng có thể tạo ra hậu quả không mong muốn. "
                            "Ví dụ mới: Some countries set a ceiling on the interest rate that banks can charge "
                            "on personal loans to protect borrowers from predatory lending.\n\n"
                            "Surplus — thặng dư. Khi có quá nhiều hàng mà không đủ người mua, "
                            "đó là surplus. Nó là tín hiệu để thị trường tự điều chỉnh. "
                            "Ví dụ mới: The surplus of fresh flowers after Valentine's Day forces florists "
                            "to sell bouquets at half price to avoid waste.\n\n"
                            "Bạn biết không, học từ vựng kinh tế không chỉ là ghi nhớ định nghĩa. "
                            "Mỗi từ bạn học là một cách nhìn mới về thế giới. "
                            "Khi bạn đi chợ và thấy giá rau tăng, bạn sẽ nghĩ đến supply và demand. "
                            "Khi đọc tin tức về chính phủ kiểm soát giá xăng, bạn sẽ nghĩ đến ceiling và shortage. "
                            "Khi chọn giữa hai sản phẩm, bạn sẽ nghĩ đến substitute và complement.\n\n"
                            "Tiếng Anh kinh tế không phải là rào cản — nó là cánh cửa. "
                            "Và bạn vừa mở cánh cửa đầu tiên.\n\n"
                            "Chúc bạn tiếp tục hành trình học tập thật vui và hiệu quả. "
                            "Hẹn gặp lại bạn ở bài học tiếp theo nhé!"
                        )
                    }
                }
            ]
        }
    ]
}

# ── Validate before upload ───────────────────────────────────
print("Validating content...")
validate_all(content)
print("Validation passed!")

# ── Upload ───────────────────────────────────────────────────
token = get_firebase_id_token(UID)
res = requests.post(
    f"{API_BASE}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
res.raise_for_status()
curriculum_id = res.json()["id"]
print(f"Created curriculum: {curriculum_id}")
print(f"Title: {content['title']}")

# ── Duplicate check SQL ──────────────────────────────────────
print("\n-- Duplicate check SQL (run manually): --")
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Supply & Demand – Cung và Cầu' AND uid = '{UID}' ORDER BY created_at;")
