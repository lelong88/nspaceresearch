"""
Create curriculum: Consumer Choice – Lựa Chọn Người Tiêu Dùng
Series A — Kinh Tế Vi Mô (Microeconomics), curriculum #3
18 words | 5 sessions | bold_declaration tone | team-building energy farewell
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
W1 = ["utility", "preference", "budget", "constraint", "marginal", "rational"]
W2 = ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"]
W3 = ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Consumer Choice – Lựa Chọn Người Tiêu Dùng",
    "contentTypeTags": [],
    "description": (
        "MỌI QUYẾT ĐỊNH MUA SẮM CỦA BẠN ĐỀU TUÂN THEO MỘT CÔNG THỨC — BẠN CHỈ CHƯA BIẾT NÓ THÔI.\n\n"
        "Mỗi sáng bạn chọn uống cà phê hay trà sữa, mỗi tháng bạn cân nhắc trả tiền thuê nhà hay mua quần áo mới — "
        "tất cả đều là lựa chọn tiêu dùng. Bạn nghĩ mình chọn theo cảm tính, nhưng thực ra "
        "đằng sau mỗi quyết định là một hệ thống logic mà kinh tế học gọi là lý thuyết lựa chọn người tiêu dùng.\n\n"
        "Hãy hình dung ngân sách của bạn như một sợi dây thừng — bạn kéo về phía này thì phải buông phía kia. "
        "Mỗi đồng chi tiêu đều có chi phí cơ hội, mỗi sự hài lòng đều tuân theo quy luật giảm dần. "
        "Nếu không hiểu cơ chế này, bạn sẽ mãi chi tiêu mà không biết mình đang đánh đổi điều gì.\n\n"
        "Sau khóa học này, bạn sẽ đọc được những phân tích về utility, indifference curve và budget constraint "
        "trong giáo trình tiếng Anh mà không cần dừng lại tra từ. Bạn sẽ tự tin giải thích "
        "vì sao người tiêu dùng hành xử theo cách họ làm — bằng ngôn ngữ chuyên ngành chuẩn xác.\n\n"
        "18 từ vựng — từ utility đến threshold — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kinh tế, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về lựa chọn người tiêu dùng — trái tim của kinh tế vi mô. "
            "Bạn sẽ bắt đầu với utility, preference, budget, constraint, marginal, rational — "
            "những từ giúp bạn hiểu cách người tiêu dùng đưa ra quyết định dựa trên sở thích và giới hạn ngân sách. "
            "Tiếp theo là indifference, diminishing, maximize, consumption, satisfaction, income — "
            "bộ từ vựng về đường bàng quan, quy luật lợi ích giảm dần và tối ưu hóa tiêu dùng. "
            "Cuối cùng, opportunity, trade-off, optimal, welfare, expenditure, threshold "
            "đưa bạn vào thế giới chi phí cơ hội và phúc lợi người tiêu dùng. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin phân tích hành vi tiêu dùng bằng tiếng Anh chuyên ngành — "
            "sẵn sàng cho mọi bài giảng và giáo trình đại học."
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
                    "description": "Chào mừng bạn đến với bài học về lựa chọn người tiêu dùng — nền tảng phân tích hành vi mua sắm.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học về Lựa chọn Người tiêu dùng — "
                            "hay trong tiếng Anh là Consumer Choice. Đây là một trong những chủ đề quan trọng nhất "
                            "của kinh tế vi mô, vì nó giải thích tại sao bạn mua những gì bạn mua, "
                            "và làm thế nào để đưa ra quyết định tiêu dùng thông minh nhất với số tiền có hạn.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: utility, preference, budget, constraint, marginal, và rational. "
                            "Đây là những từ nền tảng mà bạn sẽ gặp ngay từ chương đầu tiên khi đọc về hành vi người tiêu dùng.\n\n"
                            "Từ đầu tiên là utility — danh từ — nghĩa là lợi ích, mức độ hài lòng hoặc thỏa mãn "
                            "mà người tiêu dùng nhận được khi sử dụng một hàng hóa hoặc dịch vụ. "
                            "Ví dụ: 'The utility a student gets from the first cup of coffee in the morning is much higher than from the third cup.' "
                            "Trong bài đọc, utility là khái niệm trung tâm — mọi quyết định tiêu dùng đều nhằm tối đa hóa utility.\n\n"
                            "Từ thứ hai là preference — danh từ — nghĩa là sở thích, thứ tự ưu tiên "
                            "mà người tiêu dùng đặt cho các lựa chọn khác nhau. "
                            "Ví dụ: 'Her preference for organic food means she is willing to pay more at the supermarket.' "
                            "Trong bài đọc, preference giải thích vì sao hai người có cùng thu nhập "
                            "nhưng lại chi tiêu hoàn toàn khác nhau.\n\n"
                            "Từ thứ ba là budget — danh từ — nghĩa là ngân sách, "
                            "tổng số tiền mà người tiêu dùng có thể chi tiêu trong một khoảng thời gian. "
                            "Ví dụ: 'A university student with a monthly budget of three million dong must choose carefully between food, transport, and entertainment.' "
                            "Trong bài đọc, budget là giới hạn thực tế mà mọi người tiêu dùng phải đối mặt.\n\n"
                            "Từ thứ tư là constraint — danh từ — nghĩa là ràng buộc, "
                            "giới hạn ngăn cản người tiêu dùng mua tất cả những gì họ muốn. "
                            "Ví dụ: 'The budget constraint forces consumers to make trade-offs between different goods.' "
                            "Trong bài đọc, constraint thường đi kèm với budget — "
                            "budget constraint là đường giới hạn ngân sách trên đồ thị kinh tế.\n\n"
                            "Từ thứ năm là marginal — tính từ — nghĩa là biên, cận biên, "
                            "liên quan đến sự thay đổi khi thêm một đơn vị nữa. "
                            "Ví dụ: 'The marginal utility of eating one more slice of pizza decreases as you get fuller.' "
                            "Trong bài đọc, marginal là từ bạn sẽ gặp rất nhiều — "
                            "marginal utility, marginal cost, marginal benefit đều là khái niệm cốt lõi.\n\n"
                            "Từ cuối cùng là rational — tính từ — nghĩa là hợp lý, lý trí, "
                            "mô tả người tiêu dùng đưa ra quyết định dựa trên logic và tính toán lợi ích. "
                            "Ví dụ: 'A rational consumer compares the price and quality of different brands before making a purchase.' "
                            "Trong bài đọc, rational là giả định cơ bản của kinh tế học — "
                            "rằng người tiêu dùng luôn cố gắng tối đa hóa lợi ích với nguồn lực có hạn.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về nền tảng lựa chọn người tiêu dùng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng lựa chọn tiêu dùng",
                    "description": "Học 6 từ: utility, preference, budget, constraint, marginal, rational",
                    "data": {"vocabList": ["utility", "preference", "budget", "constraint", "marginal", "rational"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng lựa chọn tiêu dùng",
                    "description": "Học 6 từ: utility, preference, budget, constraint, marginal, rational",
                    "data": {"vocabList": ["utility", "preference", "budget", "constraint", "marginal", "rational"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng lựa chọn tiêu dùng",
                    "description": "Học 6 từ: utility, preference, budget, constraint, marginal, rational",
                    "data": {"vocabList": ["utility", "preference", "budget", "constraint", "marginal", "rational"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng lựa chọn tiêu dùng",
                    "description": "Học 6 từ: utility, preference, budget, constraint, marginal, rational",
                    "data": {"vocabList": ["utility", "preference", "budget", "constraint", "marginal", "rational"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nền tảng lựa chọn tiêu dùng",
                    "description": "Học 6 từ: utility, preference, budget, constraint, marginal, rational",
                    "data": {"vocabList": ["utility", "preference", "budget", "constraint", "marginal", "rational"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nền tảng lựa chọn người tiêu dùng",
                    "description": "Every time you walk into a store or open a shopping app, you face a decision.",
                    "data": {
                        "text": (
                            "Every time you walk into a store or open a shopping app, you face a decision. "
                            "You want many things, but your wallet has limits. "
                            "Economists call this the problem of consumer choice, "
                            "and it is one of the oldest questions in microeconomics.\n\n"
                            "At the heart of consumer choice is the concept of utility. "
                            "Utility is the satisfaction or benefit a person gets from consuming a good or service. "
                            "When you drink a cold glass of lemonade on a hot day, the pleasure you feel is utility. "
                            "Economists do not measure utility in exact numbers, "
                            "but they assume that consumers can rank their options — "
                            "they know whether they prefer one thing over another.\n\n"
                            "This ranking is called a preference. "
                            "A preference tells us which combination of goods a consumer likes more. "
                            "For example, a student might prefer spending money on books rather than on snacks, "
                            "while another student has the opposite preference. "
                            "Neither choice is wrong — preferences are personal.\n\n"
                            "However, no one can buy everything they want. "
                            "Every consumer has a budget — a limited amount of money available for spending. "
                            "This budget creates a constraint, a boundary that limits the set of choices available. "
                            "If you have one hundred thousand dong for lunch, "
                            "you cannot order a meal that costs one hundred and fifty thousand. "
                            "The budget constraint is a line on a graph that shows all the combinations of two goods "
                            "a consumer can afford at current prices.\n\n"
                            "Within this constraint, a rational consumer tries to get the most utility possible. "
                            "A rational person does not waste money on things that bring little satisfaction. "
                            "Instead, they compare options and choose the combination that makes them happiest. "
                            "This does not mean every decision is perfect — "
                            "it means the consumer uses the information they have to make the best choice they can.\n\n"
                            "One important tool in this analysis is the idea of marginal utility. "
                            "Marginal utility is the extra satisfaction gained from consuming one more unit of a good. "
                            "The first bowl of pho at lunch brings great satisfaction. "
                            "The second bowl still tastes good, but the pleasure is less. "
                            "By the third bowl, you might not want any more at all. "
                            "This pattern — where each additional unit brings less utility — "
                            "is a key principle that shapes how rational consumers allocate their budgets."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nền tảng lựa chọn người tiêu dùng",
                    "description": "Every time you walk into a store or open a shopping app, you face a decision.",
                    "data": {
                        "text": (
                            "Every time you walk into a store or open a shopping app, you face a decision. "
                            "You want many things, but your wallet has limits. "
                            "Economists call this the problem of consumer choice, "
                            "and it is one of the oldest questions in microeconomics.\n\n"
                            "At the heart of consumer choice is the concept of utility. "
                            "Utility is the satisfaction or benefit a person gets from consuming a good or service. "
                            "When you drink a cold glass of lemonade on a hot day, the pleasure you feel is utility. "
                            "Economists do not measure utility in exact numbers, "
                            "but they assume that consumers can rank their options — "
                            "they know whether they prefer one thing over another.\n\n"
                            "This ranking is called a preference. "
                            "A preference tells us which combination of goods a consumer likes more. "
                            "For example, a student might prefer spending money on books rather than on snacks, "
                            "while another student has the opposite preference. "
                            "Neither choice is wrong — preferences are personal.\n\n"
                            "However, no one can buy everything they want. "
                            "Every consumer has a budget — a limited amount of money available for spending. "
                            "This budget creates a constraint, a boundary that limits the set of choices available. "
                            "If you have one hundred thousand dong for lunch, "
                            "you cannot order a meal that costs one hundred and fifty thousand. "
                            "The budget constraint is a line on a graph that shows all the combinations of two goods "
                            "a consumer can afford at current prices.\n\n"
                            "Within this constraint, a rational consumer tries to get the most utility possible. "
                            "A rational person does not waste money on things that bring little satisfaction. "
                            "Instead, they compare options and choose the combination that makes them happiest. "
                            "This does not mean every decision is perfect — "
                            "it means the consumer uses the information they have to make the best choice they can.\n\n"
                            "One important tool in this analysis is the idea of marginal utility. "
                            "Marginal utility is the extra satisfaction gained from consuming one more unit of a good. "
                            "The first bowl of pho at lunch brings great satisfaction. "
                            "The second bowl still tastes good, but the pleasure is less. "
                            "By the third bowl, you might not want any more at all. "
                            "This pattern — where each additional unit brings less utility — "
                            "is a key principle that shapes how rational consumers allocate their budgets."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nền tảng lựa chọn người tiêu dùng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every time you walk into a store or open a shopping app, you face a decision. "
                            "You want many things, but your wallet has limits. "
                            "Economists call this the problem of consumer choice, "
                            "and it is one of the oldest questions in microeconomics.\n\n"
                            "At the heart of consumer choice is the concept of utility. "
                            "Utility is the satisfaction or benefit a person gets from consuming a good or service. "
                            "When you drink a cold glass of lemonade on a hot day, the pleasure you feel is utility. "
                            "Economists do not measure utility in exact numbers, "
                            "but they assume that consumers can rank their options — "
                            "they know whether they prefer one thing over another.\n\n"
                            "This ranking is called a preference. "
                            "A preference tells us which combination of goods a consumer likes more. "
                            "For example, a student might prefer spending money on books rather than on snacks, "
                            "while another student has the opposite preference. "
                            "Neither choice is wrong — preferences are personal.\n\n"
                            "However, no one can buy everything they want. "
                            "Every consumer has a budget — a limited amount of money available for spending. "
                            "This budget creates a constraint, a boundary that limits the set of choices available. "
                            "If you have one hundred thousand dong for lunch, "
                            "you cannot order a meal that costs one hundred and fifty thousand. "
                            "The budget constraint is a line on a graph that shows all the combinations of two goods "
                            "a consumer can afford at current prices.\n\n"
                            "Within this constraint, a rational consumer tries to get the most utility possible. "
                            "A rational person does not waste money on things that bring little satisfaction. "
                            "Instead, they compare options and choose the combination that makes them happiest. "
                            "This does not mean every decision is perfect — "
                            "it means the consumer uses the information they have to make the best choice they can.\n\n"
                            "One important tool in this analysis is the idea of marginal utility. "
                            "Marginal utility is the extra satisfaction gained from consuming one more unit of a good. "
                            "The first bowl of pho at lunch brings great satisfaction. "
                            "The second bowl still tastes good, but the pleasure is less. "
                            "By the third bowl, you might not want any more at all. "
                            "This pattern — where each additional unit brings less utility — "
                            "is a key principle that shapes how rational consumers allocate their budgets."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng lựa chọn tiêu dùng",
                    "description": "Viết câu sử dụng 6 từ vựng về lựa chọn người tiêu dùng.",
                    "data": {
                        "vocabList": ["utility", "preference", "budget", "constraint", "marginal", "rational"],
                        "items": [
                            {
                                "targetVocab": "utility",
                                "prompt": "Dùng từ 'utility' để viết một câu về mức độ hài lòng mà người tiêu dùng nhận được từ một sản phẩm hoặc dịch vụ. Ví dụ: The utility of owning a bicycle is especially high for students who live far from campus and cannot afford daily taxi rides."
                            },
                            {
                                "targetVocab": "preference",
                                "prompt": "Dùng từ 'preference' để viết một câu về sở thích tiêu dùng khác nhau giữa các nhóm người. Ví dụ: Young professionals in Ho Chi Minh City show a strong preference for co-working spaces over traditional offices because of the flexible atmosphere."
                            },
                            {
                                "targetVocab": "budget",
                                "prompt": "Dùng từ 'budget' để viết một câu về giới hạn ngân sách ảnh hưởng đến quyết định mua sắm. Ví dụ: With a tight monthly budget, many university students choose street food over restaurant meals to save money for textbooks."
                            },
                            {
                                "targetVocab": "constraint",
                                "prompt": "Dùng từ 'constraint' để viết một câu về ràng buộc ngăn cản người tiêu dùng mua tất cả những gì họ muốn. Ví dụ: The budget constraint means that a family earning five million dong per month cannot afford both a new phone and a weekend vacation."
                            },
                            {
                                "targetVocab": "marginal",
                                "prompt": "Dùng từ 'marginal' để viết một câu về lợi ích cận biên khi tiêu dùng thêm một đơn vị hàng hóa. Ví dụ: The marginal benefit of studying one more hour decreases late at night when your concentration starts to fade."
                            },
                            {
                                "targetVocab": "rational",
                                "prompt": "Dùng từ 'rational' để viết một câu về hành vi hợp lý của người tiêu dùng khi đưa ra quyết định mua sắm. Ví dụ: A rational shopper compares prices at three different stores before buying a laptop to make sure she gets the best deal."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về đường bàng quan và tối ưu hóa tiêu dùng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "utility — lợi ích, preference — sở thích, budget — ngân sách, "
                            "constraint — ràng buộc, marginal — cận biên, và rational — hợp lý. "
                            "Bạn đã hiểu cách người tiêu dùng đưa ra quyết định dựa trên sở thích "
                            "và giới hạn ngân sách. Bây giờ, chúng ta sẽ đi sâu hơn vào lý thuyết.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: indifference, diminishing, maximize, consumption, satisfaction, và income. "
                            "Những từ này giúp bạn hiểu các công cụ phân tích mà nhà kinh tế sử dụng "
                            "để mô hình hóa hành vi tiêu dùng.\n\n"
                            "Từ đầu tiên là indifference — danh từ — nghĩa là sự bàng quan, "
                            "trạng thái khi người tiêu dùng cảm thấy hài lòng như nhau giữa hai lựa chọn. "
                            "Ví dụ: 'An indifference curve shows all the combinations of two goods that give a consumer the same level of satisfaction.' "
                            "Trong bài đọc, indifference curve là công cụ đồ thị quan trọng — "
                            "nó cho thấy người tiêu dùng sẵn sàng đánh đổi bao nhiêu hàng hóa này để lấy hàng hóa kia.\n\n"
                            "Từ thứ hai là diminishing — tính từ — nghĩa là giảm dần, "
                            "mô tả xu hướng lợi ích giảm khi tiêu dùng thêm. "
                            "Ví dụ: 'The law of diminishing marginal utility explains why the fifth piece of chocolate is less enjoyable than the first.' "
                            "Trong bài đọc, diminishing đi kèm với marginal utility — "
                            "quy luật lợi ích cận biên giảm dần là nền tảng của lý thuyết tiêu dùng.\n\n"
                            "Từ thứ ba là maximize — động từ — nghĩa là tối đa hóa, "
                            "đạt được mức cao nhất có thể. "
                            "Ví dụ: 'Consumers try to maximize their utility by choosing the best combination of goods within their budget.' "
                            "Trong bài đọc, maximize là mục tiêu của mọi người tiêu dùng hợp lý — "
                            "họ muốn đạt được sự hài lòng cao nhất với số tiền có hạn.\n\n"
                            "Từ thứ tư là consumption — danh từ — nghĩa là sự tiêu dùng, "
                            "hành vi sử dụng hàng hóa và dịch vụ để thỏa mãn nhu cầu. "
                            "Ví dụ: 'The consumption of fast food among young people has increased significantly in the last decade.' "
                            "Trong bài đọc, consumption là hoạt động trung tâm — "
                            "mọi phân tích đều xoay quanh cách người tiêu dùng phân bổ consumption giữa các hàng hóa.\n\n"
                            "Từ thứ năm là satisfaction — danh từ — nghĩa là sự hài lòng, thỏa mãn, "
                            "cảm giác tích cực khi nhu cầu được đáp ứng. "
                            "Ví dụ: 'Customer satisfaction surveys help companies understand whether their products meet consumer expectations.' "
                            "Trong bài đọc, satisfaction thường được dùng thay thế cho utility — "
                            "cả hai đều chỉ mức độ hài lòng mà người tiêu dùng nhận được.\n\n"
                            "Từ cuối cùng là income — danh từ — nghĩa là thu nhập, "
                            "tổng số tiền mà một cá nhân hoặc hộ gia đình kiếm được. "
                            "Ví dụ: 'When income rises, consumers can afford to buy more goods, shifting their budget constraint outward.' "
                            "Trong bài đọc, income là yếu tố quyết định kích thước ngân sách — "
                            "thu nhập cao hơn nghĩa là nhiều lựa chọn hơn.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về lý thuyết lợi ích và tối ưu hóa tiêu dùng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Lý thuyết lợi ích và tối ưu hóa",
                    "description": "Học 6 từ: indifference, diminishing, maximize, consumption, satisfaction, income",
                    "data": {"vocabList": ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Lý thuyết lợi ích và tối ưu hóa",
                    "description": "Học 6 từ: indifference, diminishing, maximize, consumption, satisfaction, income",
                    "data": {"vocabList": ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Lý thuyết lợi ích và tối ưu hóa",
                    "description": "Học 6 từ: indifference, diminishing, maximize, consumption, satisfaction, income",
                    "data": {"vocabList": ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Lý thuyết lợi ích và tối ưu hóa",
                    "description": "Học 6 từ: indifference, diminishing, maximize, consumption, satisfaction, income",
                    "data": {"vocabList": ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Lý thuyết lợi ích và tối ưu hóa",
                    "description": "Học 6 từ: indifference, diminishing, maximize, consumption, satisfaction, income",
                    "data": {"vocabList": ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Lý thuyết lợi ích và tối ưu hóa tiêu dùng",
                    "description": "Imagine you have a fixed amount of money each month and must decide how to split it between two things you enjoy.",
                    "data": {
                        "text": (
                            "Imagine you have a fixed amount of money each month and must decide how to split it "
                            "between two things you enjoy: eating out and watching movies. "
                            "How do you find the best combination? "
                            "Economists use a set of tools to answer this question.\n\n"
                            "The starting point is the idea that consumption brings satisfaction. "
                            "Every time you eat a meal or watch a film, you gain some level of satisfaction — "
                            "what economists call utility. "
                            "But not all units of consumption are equal. "
                            "The first movie of the week is exciting. The second is still enjoyable. "
                            "By the fifth, you might feel bored. "
                            "This pattern is known as diminishing marginal utility: "
                            "each additional unit of a good provides less extra satisfaction than the one before.\n\n"
                            "To visualize consumer preferences, economists draw indifference curves. "
                            "An indifference curve connects all the combinations of two goods "
                            "that give a consumer the same total satisfaction. "
                            "For example, you might be equally happy with three restaurant meals and two movies, "
                            "or with one restaurant meal and four movies. "
                            "Both points sit on the same indifference curve because your total satisfaction is identical.\n\n"
                            "Higher indifference curves represent higher levels of satisfaction. "
                            "A consumer always wants to reach the highest possible curve. "
                            "But there is a limit: income. "
                            "Your income determines how much you can spend. "
                            "If your monthly income for entertainment is five hundred thousand dong, "
                            "and a restaurant meal costs one hundred thousand while a movie ticket costs fifty thousand, "
                            "your budget constraint is a straight line showing every affordable combination.\n\n"
                            "The goal of a rational consumer is to maximize utility — "
                            "to reach the highest indifference curve that still touches the budget constraint. "
                            "This point of contact is called the optimal choice. "
                            "At this point, the consumer cannot do better without spending more money.\n\n"
                            "What happens when income changes? "
                            "If your income increases, the budget constraint shifts outward. "
                            "You can now afford combinations that were previously out of reach. "
                            "Your consumption of both goods may rise, and you move to a higher indifference curve. "
                            "This is why rising income generally leads to greater satisfaction — "
                            "more resources mean more freedom to choose."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lý thuyết lợi ích và tối ưu hóa tiêu dùng",
                    "description": "Imagine you have a fixed amount of money each month and must decide how to split it between two things you enjoy.",
                    "data": {
                        "text": (
                            "Imagine you have a fixed amount of money each month and must decide how to split it "
                            "between two things you enjoy: eating out and watching movies. "
                            "How do you find the best combination? "
                            "Economists use a set of tools to answer this question.\n\n"
                            "The starting point is the idea that consumption brings satisfaction. "
                            "Every time you eat a meal or watch a film, you gain some level of satisfaction — "
                            "what economists call utility. "
                            "But not all units of consumption are equal. "
                            "The first movie of the week is exciting. The second is still enjoyable. "
                            "By the fifth, you might feel bored. "
                            "This pattern is known as diminishing marginal utility: "
                            "each additional unit of a good provides less extra satisfaction than the one before.\n\n"
                            "To visualize consumer preferences, economists draw indifference curves. "
                            "An indifference curve connects all the combinations of two goods "
                            "that give a consumer the same total satisfaction. "
                            "For example, you might be equally happy with three restaurant meals and two movies, "
                            "or with one restaurant meal and four movies. "
                            "Both points sit on the same indifference curve because your total satisfaction is identical.\n\n"
                            "Higher indifference curves represent higher levels of satisfaction. "
                            "A consumer always wants to reach the highest possible curve. "
                            "But there is a limit: income. "
                            "Your income determines how much you can spend. "
                            "If your monthly income for entertainment is five hundred thousand dong, "
                            "and a restaurant meal costs one hundred thousand while a movie ticket costs fifty thousand, "
                            "your budget constraint is a straight line showing every affordable combination.\n\n"
                            "The goal of a rational consumer is to maximize utility — "
                            "to reach the highest indifference curve that still touches the budget constraint. "
                            "This point of contact is called the optimal choice. "
                            "At this point, the consumer cannot do better without spending more money.\n\n"
                            "What happens when income changes? "
                            "If your income increases, the budget constraint shifts outward. "
                            "You can now afford combinations that were previously out of reach. "
                            "Your consumption of both goods may rise, and you move to a higher indifference curve. "
                            "This is why rising income generally leads to greater satisfaction — "
                            "more resources mean more freedom to choose."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lý thuyết lợi ích và tối ưu hóa tiêu dùng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine you have a fixed amount of money each month and must decide how to split it "
                            "between two things you enjoy: eating out and watching movies. "
                            "How do you find the best combination? "
                            "Economists use a set of tools to answer this question.\n\n"
                            "The starting point is the idea that consumption brings satisfaction. "
                            "Every time you eat a meal or watch a film, you gain some level of satisfaction — "
                            "what economists call utility. "
                            "But not all units of consumption are equal. "
                            "The first movie of the week is exciting. The second is still enjoyable. "
                            "By the fifth, you might feel bored. "
                            "This pattern is known as diminishing marginal utility: "
                            "each additional unit of a good provides less extra satisfaction than the one before.\n\n"
                            "To visualize consumer preferences, economists draw indifference curves. "
                            "An indifference curve connects all the combinations of two goods "
                            "that give a consumer the same total satisfaction. "
                            "For example, you might be equally happy with three restaurant meals and two movies, "
                            "or with one restaurant meal and four movies. "
                            "Both points sit on the same indifference curve because your total satisfaction is identical.\n\n"
                            "Higher indifference curves represent higher levels of satisfaction. "
                            "A consumer always wants to reach the highest possible curve. "
                            "But there is a limit: income. "
                            "Your income determines how much you can spend. "
                            "If your monthly income for entertainment is five hundred thousand dong, "
                            "and a restaurant meal costs one hundred thousand while a movie ticket costs fifty thousand, "
                            "your budget constraint is a straight line showing every affordable combination.\n\n"
                            "The goal of a rational consumer is to maximize utility — "
                            "to reach the highest indifference curve that still touches the budget constraint. "
                            "This point of contact is called the optimal choice. "
                            "At this point, the consumer cannot do better without spending more money.\n\n"
                            "What happens when income changes? "
                            "If your income increases, the budget constraint shifts outward. "
                            "You can now afford combinations that were previously out of reach. "
                            "Your consumption of both goods may rise, and you move to a higher indifference curve. "
                            "This is why rising income generally leads to greater satisfaction — "
                            "more resources mean more freedom to choose."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Lý thuyết lợi ích và tối ưu hóa",
                    "description": "Viết câu sử dụng 6 từ vựng về lợi ích và tối ưu hóa tiêu dùng.",
                    "data": {
                        "vocabList": ["indifference", "diminishing", "maximize", "consumption", "satisfaction", "income"],
                        "items": [
                            {
                                "targetVocab": "indifference",
                                "prompt": "Dùng từ 'indifference' để viết một câu về đường bàng quan trong phân tích lựa chọn tiêu dùng. Ví dụ: Each point on an indifference curve represents a different mix of goods that gives the consumer exactly the same level of happiness."
                            },
                            {
                                "targetVocab": "diminishing",
                                "prompt": "Dùng từ 'diminishing' để viết một câu về quy luật lợi ích cận biên giảm dần khi tiêu dùng thêm. Ví dụ: The diminishing returns from overtime work explain why employees become less productive after ten hours on the job."
                            },
                            {
                                "targetVocab": "maximize",
                                "prompt": "Dùng từ 'maximize' để viết một câu về mục tiêu tối đa hóa lợi ích của người tiêu dùng. Ví dụ: To maximize her savings, Lan compares prices online before buying any item that costs more than two hundred thousand dong."
                            },
                            {
                                "targetVocab": "consumption",
                                "prompt": "Dùng từ 'consumption' để viết một câu về thói quen tiêu dùng thay đổi theo thu nhập hoặc xu hướng xã hội. Ví dụ: The consumption of plant-based milk in Vietnam has grown rapidly as more young people adopt healthier eating habits."
                            },
                            {
                                "targetVocab": "satisfaction",
                                "prompt": "Dùng từ 'satisfaction' để viết một câu về mức độ hài lòng của người tiêu dùng với một sản phẩm hoặc dịch vụ. Ví dụ: Customer satisfaction with the new delivery app increased after the company reduced average wait times from forty minutes to twenty."
                            },
                            {
                                "targetVocab": "income",
                                "prompt": "Dùng từ 'income' để viết một câu về ảnh hưởng của thu nhập đến khả năng chi tiêu và lựa chọn tiêu dùng. Ví dụ: A rise in household income allows families to spend more on education and healthcare instead of just basic necessities."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về chi phí cơ hội và phúc lợi người tiêu dùng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: utility, preference, budget, constraint, marginal, rational — "
                            "những khái niệm cơ bản về cách người tiêu dùng đưa ra quyết định. "
                            "Trong phần 2, bạn đã học thêm indifference, diminishing, maximize, consumption, satisfaction, income — "
                            "giúp bạn hiểu đường bàng quan, quy luật lợi ích giảm dần và tối ưu hóa tiêu dùng.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh thực tế hơn: "
                            "chi phí cơ hội, sự đánh đổi, và phúc lợi người tiêu dùng. "
                            "Bạn sẽ học 6 từ mới: opportunity, trade-off, optimal, welfare, expenditure, và threshold.\n\n"
                            "Từ đầu tiên là opportunity — danh từ — nghĩa là cơ hội, "
                            "và trong kinh tế học thường đi kèm với cost thành opportunity cost — chi phí cơ hội, "
                            "giá trị của lựa chọn tốt nhất mà bạn phải từ bỏ khi chọn một thứ khác. "
                            "Ví dụ: 'The opportunity cost of attending a four-year university includes not only tuition fees but also the salary you could have earned by working full-time.' "
                            "Trong bài đọc, opportunity cost là khái niệm giúp bạn nhìn thấy cái giá thật sự của mỗi quyết định.\n\n"
                            "Từ thứ hai là trade-off — danh từ — nghĩa là sự đánh đổi, "
                            "tình huống khi bạn phải chấp nhận mất một thứ để có được thứ khác. "
                            "Ví dụ: 'There is always a trade-off between spending time studying and spending time with friends.' "
                            "Trong bài đọc, trade-off xuất hiện ở mọi quyết định tiêu dùng — "
                            "mua thêm hàng hóa này nghĩa là phải giảm hàng hóa kia.\n\n"
                            "Từ thứ ba là optimal — tính từ — nghĩa là tối ưu, "
                            "lựa chọn tốt nhất có thể trong điều kiện ràng buộc. "
                            "Ví dụ: 'The optimal combination of food and clothing depends on both the consumer's preferences and their budget.' "
                            "Trong bài đọc, optimal là điểm mà người tiêu dùng đạt được sự hài lòng cao nhất "
                            "mà ngân sách cho phép.\n\n"
                            "Từ thứ tư là welfare — danh từ — nghĩa là phúc lợi, "
                            "mức độ hạnh phúc hoặc lợi ích tổng thể của người tiêu dùng hoặc xã hội. "
                            "Ví dụ: 'Government policies that reduce the price of basic goods can improve consumer welfare, especially for low-income families.' "
                            "Trong bài đọc, welfare được dùng để đánh giá tác động của chính sách "
                            "lên đời sống người tiêu dùng.\n\n"
                            "Từ thứ năm là expenditure — danh từ — nghĩa là chi tiêu, "
                            "tổng số tiền mà người tiêu dùng bỏ ra để mua hàng hóa và dịch vụ. "
                            "Ví dụ: 'Household expenditure on food accounts for about thirty-five percent of total spending in many Vietnamese families.' "
                            "Trong bài đọc, expenditure là thước đo cụ thể cho hành vi tiêu dùng — "
                            "nó cho thấy người ta thực sự chi tiền vào đâu.\n\n"
                            "Từ cuối cùng là threshold — danh từ — nghĩa là ngưỡng, "
                            "mức giới hạn mà khi vượt qua sẽ tạo ra sự thay đổi trong hành vi. "
                            "Ví dụ: 'Many consumers have a price threshold — once the price of a product crosses that point, they stop buying it entirely.' "
                            "Trong bài đọc, threshold giải thích vì sao người tiêu dùng đột ngột thay đổi hành vi "
                            "khi giá hoặc thu nhập đạt đến một mức nhất định.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về chi phí cơ hội và phúc lợi người tiêu dùng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chi phí cơ hội và phúc lợi",
                    "description": "Học 6 từ: opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chi phí cơ hội và phúc lợi",
                    "description": "Học 6 từ: opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chi phí cơ hội và phúc lợi",
                    "description": "Học 6 từ: opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chi phí cơ hội và phúc lợi",
                    "description": "Học 6 từ: opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chi phí cơ hội và phúc lợi",
                    "description": "Học 6 từ: opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chi phí cơ hội và phúc lợi người tiêu dùng",
                    "description": "Every choice has a hidden price. When you decide to spend your Saturday studying for an exam, you give up the chance to earn money at a part-time job.",
                    "data": {
                        "text": (
                            "Every choice has a hidden price. "
                            "When you decide to spend your Saturday studying for an exam, "
                            "you give up the chance to earn money at a part-time job. "
                            "When you buy a new phone, you give up the vacation you could have taken with the same money. "
                            "Economists call this hidden price the opportunity cost — "
                            "the value of the best alternative you did not choose.\n\n"
                            "Opportunity cost is everywhere in consumer decisions. "
                            "A student who spends two hundred thousand dong on a concert ticket "
                            "faces an opportunity cost equal to whatever else that money could have bought — "
                            "perhaps ten meals at the campus cafeteria. "
                            "Understanding opportunity cost helps consumers make more thoughtful choices "
                            "because it forces them to consider what they are truly giving up.\n\n"
                            "Closely related is the idea of a trade-off. "
                            "A trade-off occurs whenever you must accept less of one thing to get more of another. "
                            "If you have a fixed budget and the price of food rises, "
                            "you face a trade-off: spend more on food and less on entertainment, "
                            "or keep your entertainment spending and eat cheaper meals. "
                            "Trade-offs are unavoidable because resources are limited.\n\n"
                            "Given these trade-offs, how does a consumer find the best possible outcome? "
                            "Economists say the answer is the optimal choice — "
                            "the combination of goods that gives the highest satisfaction within the budget constraint. "
                            "At the optimal point, the consumer cannot increase satisfaction "
                            "by shifting expenditure from one good to another. "
                            "Every dong is allocated in the way that produces the most utility.\n\n"
                            "Expenditure patterns reveal a lot about consumer behavior. "
                            "When economists study how households divide their expenditure "
                            "among food, housing, transport, and education, "
                            "they can measure changes in welfare. "
                            "Welfare, in economics, refers to the overall well-being of consumers. "
                            "If a policy reduces the price of rice, consumer welfare improves "
                            "because families can buy the same amount of rice for less money "
                            "and use the savings on other goods.\n\n"
                            "Finally, consumers often have a threshold — a tipping point "
                            "that triggers a change in behavior. "
                            "For example, a commuter might take the bus every day, "
                            "but if the bus fare crosses a certain threshold, "
                            "she switches to a motorbike. "
                            "A coffee drinker might accept small price increases, "
                            "but once the price passes his personal threshold, "
                            "he stops buying and makes coffee at home instead. "
                            "Thresholds help explain why consumer demand sometimes changes suddenly "
                            "rather than gradually — small price movements have little effect, "
                            "but crossing the threshold triggers a sharp shift in behavior."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chi phí cơ hội và phúc lợi người tiêu dùng",
                    "description": "Every choice has a hidden price. When you decide to spend your Saturday studying for an exam, you give up the chance to earn money at a part-time job.",
                    "data": {
                        "text": (
                            "Every choice has a hidden price. "
                            "When you decide to spend your Saturday studying for an exam, "
                            "you give up the chance to earn money at a part-time job. "
                            "When you buy a new phone, you give up the vacation you could have taken with the same money. "
                            "Economists call this hidden price the opportunity cost — "
                            "the value of the best alternative you did not choose.\n\n"
                            "Opportunity cost is everywhere in consumer decisions. "
                            "A student who spends two hundred thousand dong on a concert ticket "
                            "faces an opportunity cost equal to whatever else that money could have bought — "
                            "perhaps ten meals at the campus cafeteria. "
                            "Understanding opportunity cost helps consumers make more thoughtful choices "
                            "because it forces them to consider what they are truly giving up.\n\n"
                            "Closely related is the idea of a trade-off. "
                            "A trade-off occurs whenever you must accept less of one thing to get more of another. "
                            "If you have a fixed budget and the price of food rises, "
                            "you face a trade-off: spend more on food and less on entertainment, "
                            "or keep your entertainment spending and eat cheaper meals. "
                            "Trade-offs are unavoidable because resources are limited.\n\n"
                            "Given these trade-offs, how does a consumer find the best possible outcome? "
                            "Economists say the answer is the optimal choice — "
                            "the combination of goods that gives the highest satisfaction within the budget constraint. "
                            "At the optimal point, the consumer cannot increase satisfaction "
                            "by shifting expenditure from one good to another. "
                            "Every dong is allocated in the way that produces the most utility.\n\n"
                            "Expenditure patterns reveal a lot about consumer behavior. "
                            "When economists study how households divide their expenditure "
                            "among food, housing, transport, and education, "
                            "they can measure changes in welfare. "
                            "Welfare, in economics, refers to the overall well-being of consumers. "
                            "If a policy reduces the price of rice, consumer welfare improves "
                            "because families can buy the same amount of rice for less money "
                            "and use the savings on other goods.\n\n"
                            "Finally, consumers often have a threshold — a tipping point "
                            "that triggers a change in behavior. "
                            "For example, a commuter might take the bus every day, "
                            "but if the bus fare crosses a certain threshold, "
                            "she switches to a motorbike. "
                            "A coffee drinker might accept small price increases, "
                            "but once the price passes his personal threshold, "
                            "he stops buying and makes coffee at home instead. "
                            "Thresholds help explain why consumer demand sometimes changes suddenly "
                            "rather than gradually — small price movements have little effect, "
                            "but crossing the threshold triggers a sharp shift in behavior."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chi phí cơ hội và phúc lợi người tiêu dùng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every choice has a hidden price. "
                            "When you decide to spend your Saturday studying for an exam, "
                            "you give up the chance to earn money at a part-time job. "
                            "When you buy a new phone, you give up the vacation you could have taken with the same money. "
                            "Economists call this hidden price the opportunity cost — "
                            "the value of the best alternative you did not choose.\n\n"
                            "Opportunity cost is everywhere in consumer decisions. "
                            "A student who spends two hundred thousand dong on a concert ticket "
                            "faces an opportunity cost equal to whatever else that money could have bought — "
                            "perhaps ten meals at the campus cafeteria. "
                            "Understanding opportunity cost helps consumers make more thoughtful choices "
                            "because it forces them to consider what they are truly giving up.\n\n"
                            "Closely related is the idea of a trade-off. "
                            "A trade-off occurs whenever you must accept less of one thing to get more of another. "
                            "If you have a fixed budget and the price of food rises, "
                            "you face a trade-off: spend more on food and less on entertainment, "
                            "or keep your entertainment spending and eat cheaper meals. "
                            "Trade-offs are unavoidable because resources are limited.\n\n"
                            "Given these trade-offs, how does a consumer find the best possible outcome? "
                            "Economists say the answer is the optimal choice — "
                            "the combination of goods that gives the highest satisfaction within the budget constraint. "
                            "At the optimal point, the consumer cannot increase satisfaction "
                            "by shifting expenditure from one good to another. "
                            "Every dong is allocated in the way that produces the most utility.\n\n"
                            "Expenditure patterns reveal a lot about consumer behavior. "
                            "When economists study how households divide their expenditure "
                            "among food, housing, transport, and education, "
                            "they can measure changes in welfare. "
                            "Welfare, in economics, refers to the overall well-being of consumers. "
                            "If a policy reduces the price of rice, consumer welfare improves "
                            "because families can buy the same amount of rice for less money "
                            "and use the savings on other goods.\n\n"
                            "Finally, consumers often have a threshold — a tipping point "
                            "that triggers a change in behavior. "
                            "For example, a commuter might take the bus every day, "
                            "but if the bus fare crosses a certain threshold, "
                            "she switches to a motorbike. "
                            "A coffee drinker might accept small price increases, "
                            "but once the price passes his personal threshold, "
                            "he stops buying and makes coffee at home instead. "
                            "Thresholds help explain why consumer demand sometimes changes suddenly "
                            "rather than gradually — small price movements have little effect, "
                            "but crossing the threshold triggers a sharp shift in behavior."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chi phí cơ hội và phúc lợi",
                    "description": "Viết câu sử dụng 6 từ vựng về chi phí cơ hội và phúc lợi.",
                    "data": {
                        "vocabList": ["opportunity", "trade-off", "optimal", "welfare", "expenditure", "threshold"],
                        "items": [
                            {
                                "targetVocab": "opportunity",
                                "prompt": "Dùng từ 'opportunity' để viết một câu về chi phí cơ hội khi đưa ra một quyết định trong cuộc sống. Ví dụ: The opportunity cost of taking a gap year after high school is the income and work experience you could have gained by starting a job immediately."
                            },
                            {
                                "targetVocab": "trade-off",
                                "prompt": "Dùng từ 'trade-off' để viết một câu về sự đánh đổi mà người tiêu dùng phải chấp nhận khi ngân sách có hạn. Ví dụ: Choosing to live in a smaller apartment closer to work involves a trade-off between living space and commuting time."
                            },
                            {
                                "targetVocab": "optimal",
                                "prompt": "Dùng từ 'optimal' để viết một câu về lựa chọn tối ưu trong điều kiện ràng buộc ngân sách. Ví dụ: The optimal study schedule balances enough review time for each subject without sacrificing sleep or exercise."
                            },
                            {
                                "targetVocab": "welfare",
                                "prompt": "Dùng từ 'welfare' để viết một câu về tác động của chính sách kinh tế lên phúc lợi người tiêu dùng. Ví dụ: Reducing import taxes on essential medicines improves consumer welfare by making healthcare more affordable for low-income families."
                            },
                            {
                                "targetVocab": "expenditure",
                                "prompt": "Dùng từ 'expenditure' để viết một câu về cách hộ gia đình phân bổ chi tiêu cho các nhu cầu khác nhau. Ví dụ: As household income grows, the share of expenditure on food typically decreases while spending on education and leisure increases."
                            },
                            {
                                "targetVocab": "threshold",
                                "prompt": "Dùng từ 'threshold' để viết một câu về ngưỡng giá mà khi vượt qua sẽ thay đổi hành vi tiêu dùng. Ví dụ: Once the price of a ride-hailing service crosses the threshold of fifty thousand dong, many commuters switch back to public buses."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Lựa chọn Người tiêu dùng. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "utility — lợi ích, preference — sở thích, budget — ngân sách, "
                            "constraint — ràng buộc, marginal — cận biên, và rational — hợp lý. "
                            "Đây là bộ khung cơ bản để hiểu cách người tiêu dùng đưa ra quyết định.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "indifference — sự bàng quan, diminishing — giảm dần, maximize — tối đa hóa, "
                            "consumption — tiêu dùng, satisfaction — sự hài lòng, và income — thu nhập. "
                            "Những từ này giúp bạn phân tích đường bàng quan và tối ưu hóa tiêu dùng.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "opportunity — cơ hội, trade-off — sự đánh đổi, optimal — tối ưu, "
                            "welfare — phúc lợi, expenditure — chi tiêu, và threshold — ngưỡng. "
                            "Đây là những từ về chi phí cơ hội và phúc lợi người tiêu dùng.\n\n"
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
                    "description": "Học 18 từ: utility, preference, budget, constraint, marginal, rational, indifference, diminishing, maximize, consumption, satisfaction, income, opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: utility, preference, budget, constraint, marginal, rational, indifference, diminishing, maximize, consumption, satisfaction, income, opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: utility, preference, budget, constraint, marginal, rational, indifference, diminishing, maximize, consumption, satisfaction, income, opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: utility, preference, budget, constraint, marginal, rational, indifference, diminishing, maximize, consumption, satisfaction, income, opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: utility, preference, budget, constraint, marginal, rational, indifference, diminishing, maximize, consumption, satisfaction, income, opportunity, trade-off, optimal, welfare, expenditure, threshold",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng lựa chọn tiêu dùng",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "utility",
                                "prompt": "Dùng từ 'utility' để viết một câu về lợi ích mà sinh viên nhận được từ việc sử dụng thư viện trường. Ví dụ: The utility of a university library goes beyond borrowing books — it provides a quiet space for focused study and access to online research databases."
                            },
                            {
                                "targetVocab": "preference",
                                "prompt": "Dùng từ 'preference' để viết một câu về sở thích tiêu dùng thay đổi theo thế hệ. Ví dụ: Generation Z shows a clear preference for digital entertainment over traditional television, spending most of their leisure time on streaming platforms and social media."
                            },
                            {
                                "targetVocab": "budget",
                                "prompt": "Dùng từ 'budget' để viết một câu về cách lập ngân sách giúp sinh viên quản lý tài chính cá nhân. Ví dụ: Creating a monthly budget helped Minh realize he was spending nearly half his allowance on bubble tea and delivery food."
                            },
                            {
                                "targetVocab": "constraint",
                                "prompt": "Dùng từ 'constraint' để viết một câu về ràng buộc thời gian ảnh hưởng đến quyết định tiêu dùng. Ví dụ: Time is a constraint just as real as money — a busy professional may pay more for convenience foods because she has no time to cook."
                            },
                            {
                                "targetVocab": "marginal",
                                "prompt": "Dùng từ 'marginal' để viết một câu so sánh lợi ích cận biên của hai hoạt động khác nhau. Ví dụ: The marginal value of an extra hour of sleep is much higher when you have only slept four hours than when you have already slept eight."
                            },
                            {
                                "targetVocab": "rational",
                                "prompt": "Dùng từ 'rational' để viết một câu về giả định hành vi hợp lý trong kinh tế học và thực tế. Ví dụ: While economic models assume consumers are rational, real people often make impulsive purchases driven by emotions rather than careful calculation."
                            },
                            {
                                "targetVocab": "indifference",
                                "prompt": "Dùng từ 'indifference' để viết một câu về cách đường bàng quan giúp phân tích sở thích tiêu dùng. Ví dụ: An indifference map with many closely spaced curves suggests that the consumer is very sensitive to small changes in the mix of goods."
                            },
                            {
                                "targetVocab": "diminishing",
                                "prompt": "Dùng từ 'diminishing' để viết một câu về quy luật giảm dần áp dụng vào một tình huống hàng ngày. Ví dụ: The diminishing enjoyment from scrolling social media explains why people feel less entertained after the first thirty minutes but keep scrolling anyway."
                            },
                            {
                                "targetVocab": "maximize",
                                "prompt": "Dùng từ 'maximize' để viết một câu về chiến lược tối đa hóa giá trị khi mua sắm. Ví dụ: Savvy shoppers maximize the value of their money by waiting for seasonal sales and using discount codes before placing online orders."
                            },
                            {
                                "targetVocab": "consumption",
                                "prompt": "Dùng từ 'consumption' để viết một câu về xu hướng tiêu dùng thay đổi trong xã hội hiện đại. Ví dụ: The consumption of single-use plastics in Vietnam has become a growing environmental concern as convenience culture spreads to smaller cities."
                            },
                            {
                                "targetVocab": "satisfaction",
                                "prompt": "Dùng từ 'satisfaction' để viết một câu về mối quan hệ giữa kỳ vọng và sự hài lòng của người tiêu dùng. Ví dụ: Customer satisfaction drops sharply when the actual product quality falls below the expectations set by advertising."
                            },
                            {
                                "targetVocab": "income",
                                "prompt": "Dùng từ 'income' để viết một câu về ảnh hưởng của thu nhập đến cơ cấu chi tiêu hộ gia đình. Ví dụ: As average income in Vietnam rises, families spend a smaller share on food and a larger share on education, travel, and healthcare."
                            },
                            {
                                "targetVocab": "opportunity",
                                "prompt": "Dùng từ 'opportunity' để viết một câu về chi phí cơ hội của một quyết định đầu tư cá nhân. Ví dụ: The opportunity cost of investing in a master's degree includes two years of salary that could have been earned by working full-time."
                            },
                            {
                                "targetVocab": "trade-off",
                                "prompt": "Dùng từ 'trade-off' để viết một câu về sự đánh đổi giữa chất lượng và giá cả khi mua sắm. Ví dụ: Buying a cheaper laptop involves a trade-off — you save money now but may face slower performance and a shorter lifespan."
                            },
                            {
                                "targetVocab": "optimal",
                                "prompt": "Dùng từ 'optimal' để viết một câu về điểm tối ưu trong phân bổ thời gian học tập. Ví dụ: Research suggests the optimal study session lasts about fifty minutes followed by a ten-minute break to maintain concentration and retention."
                            },
                            {
                                "targetVocab": "welfare",
                                "prompt": "Dùng từ 'welfare' để viết một câu về chính sách cải thiện phúc lợi cho nhóm người có thu nhập thấp. Ví dụ: Free school lunch programs improve child welfare by ensuring that students from low-income families receive at least one nutritious meal per day."
                            },
                            {
                                "targetVocab": "expenditure",
                                "prompt": "Dùng từ 'expenditure' để viết một câu về xu hướng chi tiêu của người tiêu dùng trẻ tại Việt Nam. Ví dụ: A recent survey found that monthly expenditure on online subscriptions among Vietnamese millennials has doubled in the past three years."
                            },
                            {
                                "targetVocab": "threshold",
                                "prompt": "Dùng từ 'threshold' để viết một câu về ngưỡng tâm lý ảnh hưởng đến quyết định mua hàng. Ví dụ: Many online shoppers have a free-shipping threshold in mind — they add extra items to their cart just to avoid paying delivery fees."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về lựa chọn người tiêu dùng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về lựa chọn người tiêu dùng — từ khái niệm lợi ích "
                            "đến chi phí cơ hội và phúc lợi xã hội.\n\n"
                            "Bạn sẽ gặp lại utility, preference, budget, constraint, marginal, rational "
                            "trong phần mở đầu về nền tảng hành vi tiêu dùng. "
                            "Tiếp theo, indifference, diminishing, maximize, consumption, satisfaction, income "
                            "sẽ giúp bạn hiểu sâu hơn về cách phân tích tối ưu hóa. "
                            "Và cuối cùng, opportunity, trade-off, optimal, welfare, expenditure, threshold "
                            "sẽ đưa bạn vào thế giới chi phí cơ hội và phúc lợi.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Lựa chọn người tiêu dùng — Bức tranh toàn cảnh",
                    "description": "Every morning, before you even leave your house, you have already made dozens of economic decisions.",
                    "data": {
                        "text": (
                            "Every morning, before you even leave your house, you have already made dozens of economic decisions. "
                            "You chose what to eat for breakfast, what to wear, and how to get to school or work. "
                            "Each of these choices reflects your preferences, your budget, and the trade-offs you are willing to accept. "
                            "This is the world of consumer choice — and understanding it is one of the most practical skills economics can offer.\n\n"
                            "The foundation of consumer choice theory is utility — "
                            "the satisfaction or benefit a person receives from consuming a good or service. "
                            "Economists assume that every consumer has a set of preferences — "
                            "a personal ranking of different goods and combinations. "
                            "One student might prefer spending money on books, while another prefers concerts. "
                            "Neither is wrong; preferences are subjective. "
                            "What matters is that a rational consumer — one who thinks logically — "
                            "uses these preferences to make the best possible choice.\n\n"
                            "But even the most rational consumer faces limits. "
                            "The most important limit is the budget constraint — "
                            "the boundary set by how much money is available. "
                            "If your monthly budget for food and entertainment is two million dong, "
                            "you cannot spend three million. "
                            "The budget constraint is a line on a graph showing every combination of two goods you can afford. "
                            "Anything beyond that line is out of reach.\n\n"
                            "Within the budget constraint, the consumer seeks to maximize utility. "
                            "Economists use indifference curves to map out preferences. "
                            "An indifference curve shows all the combinations of two goods "
                            "that give the consumer the same level of satisfaction. "
                            "Higher curves mean more satisfaction. "
                            "The optimal choice is where the highest reachable indifference curve "
                            "just touches the budget constraint. "
                            "At this point, the consumer gets the most satisfaction possible from their income.\n\n"
                            "A key principle behind this analysis is diminishing marginal utility. "
                            "The marginal utility of a good is the extra satisfaction from consuming one more unit. "
                            "The first cup of coffee in the morning brings great pleasure. "
                            "The second is still nice. By the fourth, you might feel jittery rather than satisfied. "
                            "Because of this diminishing pattern, rational consumers spread their expenditure "
                            "across different goods rather than spending everything on just one.\n\n"
                            "Every consumption decision involves a trade-off. "
                            "Buying more of one good means buying less of another. "
                            "The opportunity cost of choosing a restaurant dinner "
                            "is the movie tickets or the new book you could have bought instead. "
                            "Consumers who understand opportunity cost make more deliberate choices — "
                            "they weigh not just what they gain, but what they give up.\n\n"
                            "Income plays a central role. "
                            "When income rises, the budget constraint shifts outward, "
                            "and the consumer can reach higher indifference curves. "
                            "Consumption of most goods increases. "
                            "When income falls, the constraint tightens, and consumers must make harder trade-offs. "
                            "Expenditure patterns — how households divide their spending among food, housing, "
                            "education, and leisure — shift as income changes.\n\n"
                            "Economists also study consumer welfare — "
                            "the overall well-being that consumers derive from their choices. "
                            "Policies that lower the price of essential goods improve welfare "
                            "because consumers can buy the same amount for less and use the savings elsewhere. "
                            "Policies that raise prices or limit choices can reduce welfare.\n\n"
                            "Finally, real consumers often behave in ways that are not perfectly smooth. "
                            "Many people have a threshold — a price point or income level "
                            "that triggers a sudden change in behavior. "
                            "A commuter might tolerate small fare increases for months, "
                            "but once the fare crosses a personal threshold, she buys a motorbike instead. "
                            "Thresholds remind us that consumer behavior is not always gradual — "
                            "sometimes a small change in conditions produces a big shift in choices.\n\n"
                            "Consumer choice theory ties together preferences, constraints, and trade-offs "
                            "into a framework that explains how people allocate their limited resources. "
                            "It is not a perfect description of every decision — "
                            "people are sometimes impulsive, emotional, or poorly informed. "
                            "But as a model of how rational consumers navigate scarcity, "
                            "it remains one of the most useful tools in economics."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lựa chọn người tiêu dùng — Bức tranh toàn cảnh",
                    "description": "Every morning, before you even leave your house, you have already made dozens of economic decisions.",
                    "data": {
                        "text": (
                            "Every morning, before you even leave your house, you have already made dozens of economic decisions. "
                            "You chose what to eat for breakfast, what to wear, and how to get to school or work. "
                            "Each of these choices reflects your preferences, your budget, and the trade-offs you are willing to accept. "
                            "This is the world of consumer choice — and understanding it is one of the most practical skills economics can offer.\n\n"
                            "The foundation of consumer choice theory is utility — "
                            "the satisfaction or benefit a person receives from consuming a good or service. "
                            "Economists assume that every consumer has a set of preferences — "
                            "a personal ranking of different goods and combinations. "
                            "One student might prefer spending money on books, while another prefers concerts. "
                            "Neither is wrong; preferences are subjective. "
                            "What matters is that a rational consumer — one who thinks logically — "
                            "uses these preferences to make the best possible choice.\n\n"
                            "But even the most rational consumer faces limits. "
                            "The most important limit is the budget constraint — "
                            "the boundary set by how much money is available. "
                            "If your monthly budget for food and entertainment is two million dong, "
                            "you cannot spend three million. "
                            "The budget constraint is a line on a graph showing every combination of two goods you can afford. "
                            "Anything beyond that line is out of reach.\n\n"
                            "Within the budget constraint, the consumer seeks to maximize utility. "
                            "Economists use indifference curves to map out preferences. "
                            "An indifference curve shows all the combinations of two goods "
                            "that give the consumer the same level of satisfaction. "
                            "Higher curves mean more satisfaction. "
                            "The optimal choice is where the highest reachable indifference curve "
                            "just touches the budget constraint. "
                            "At this point, the consumer gets the most satisfaction possible from their income.\n\n"
                            "A key principle behind this analysis is diminishing marginal utility. "
                            "The marginal utility of a good is the extra satisfaction from consuming one more unit. "
                            "The first cup of coffee in the morning brings great pleasure. "
                            "The second is still nice. By the fourth, you might feel jittery rather than satisfied. "
                            "Because of this diminishing pattern, rational consumers spread their expenditure "
                            "across different goods rather than spending everything on just one.\n\n"
                            "Every consumption decision involves a trade-off. "
                            "Buying more of one good means buying less of another. "
                            "The opportunity cost of choosing a restaurant dinner "
                            "is the movie tickets or the new book you could have bought instead. "
                            "Consumers who understand opportunity cost make more deliberate choices — "
                            "they weigh not just what they gain, but what they give up.\n\n"
                            "Income plays a central role. "
                            "When income rises, the budget constraint shifts outward, "
                            "and the consumer can reach higher indifference curves. "
                            "Consumption of most goods increases. "
                            "When income falls, the constraint tightens, and consumers must make harder trade-offs. "
                            "Expenditure patterns — how households divide their spending among food, housing, "
                            "education, and leisure — shift as income changes.\n\n"
                            "Economists also study consumer welfare — "
                            "the overall well-being that consumers derive from their choices. "
                            "Policies that lower the price of essential goods improve welfare "
                            "because consumers can buy the same amount for less and use the savings elsewhere. "
                            "Policies that raise prices or limit choices can reduce welfare.\n\n"
                            "Finally, real consumers often behave in ways that are not perfectly smooth. "
                            "Many people have a threshold — a price point or income level "
                            "that triggers a sudden change in behavior. "
                            "A commuter might tolerate small fare increases for months, "
                            "but once the fare crosses a personal threshold, she buys a motorbike instead. "
                            "Thresholds remind us that consumer behavior is not always gradual — "
                            "sometimes a small change in conditions produces a big shift in choices.\n\n"
                            "Consumer choice theory ties together preferences, constraints, and trade-offs "
                            "into a framework that explains how people allocate their limited resources. "
                            "It is not a perfect description of every decision — "
                            "people are sometimes impulsive, emotional, or poorly informed. "
                            "But as a model of how rational consumers navigate scarcity, "
                            "it remains one of the most useful tools in economics."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lựa chọn người tiêu dùng — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every morning, before you even leave your house, you have already made dozens of economic decisions. "
                            "You chose what to eat for breakfast, what to wear, and how to get to school or work. "
                            "Each of these choices reflects your preferences, your budget, and the trade-offs you are willing to accept. "
                            "This is the world of consumer choice — and understanding it is one of the most practical skills economics can offer.\n\n"
                            "The foundation of consumer choice theory is utility — "
                            "the satisfaction or benefit a person receives from consuming a good or service. "
                            "Economists assume that every consumer has a set of preferences — "
                            "a personal ranking of different goods and combinations. "
                            "One student might prefer spending money on books, while another prefers concerts. "
                            "Neither is wrong; preferences are subjective. "
                            "What matters is that a rational consumer — one who thinks logically — "
                            "uses these preferences to make the best possible choice.\n\n"
                            "But even the most rational consumer faces limits. "
                            "The most important limit is the budget constraint — "
                            "the boundary set by how much money is available. "
                            "If your monthly budget for food and entertainment is two million dong, "
                            "you cannot spend three million. "
                            "The budget constraint is a line on a graph showing every combination of two goods you can afford. "
                            "Anything beyond that line is out of reach.\n\n"
                            "Within the budget constraint, the consumer seeks to maximize utility. "
                            "Economists use indifference curves to map out preferences. "
                            "An indifference curve shows all the combinations of two goods "
                            "that give the consumer the same level of satisfaction. "
                            "Higher curves mean more satisfaction. "
                            "The optimal choice is where the highest reachable indifference curve "
                            "just touches the budget constraint. "
                            "At this point, the consumer gets the most satisfaction possible from their income.\n\n"
                            "A key principle behind this analysis is diminishing marginal utility. "
                            "The marginal utility of a good is the extra satisfaction from consuming one more unit. "
                            "The first cup of coffee in the morning brings great pleasure. "
                            "The second is still nice. By the fourth, you might feel jittery rather than satisfied. "
                            "Because of this diminishing pattern, rational consumers spread their expenditure "
                            "across different goods rather than spending everything on just one.\n\n"
                            "Every consumption decision involves a trade-off. "
                            "Buying more of one good means buying less of another. "
                            "The opportunity cost of choosing a restaurant dinner "
                            "is the movie tickets or the new book you could have bought instead. "
                            "Consumers who understand opportunity cost make more deliberate choices — "
                            "they weigh not just what they gain, but what they give up.\n\n"
                            "Income plays a central role. "
                            "When income rises, the budget constraint shifts outward, "
                            "and the consumer can reach higher indifference curves. "
                            "Consumption of most goods increases. "
                            "When income falls, the constraint tightens, and consumers must make harder trade-offs. "
                            "Expenditure patterns — how households divide their spending among food, housing, "
                            "education, and leisure — shift as income changes.\n\n"
                            "Economists also study consumer welfare — "
                            "the overall well-being that consumers derive from their choices. "
                            "Policies that lower the price of essential goods improve welfare "
                            "because consumers can buy the same amount for less and use the savings elsewhere. "
                            "Policies that raise prices or limit choices can reduce welfare.\n\n"
                            "Finally, real consumers often behave in ways that are not perfectly smooth. "
                            "Many people have a threshold — a price point or income level "
                            "that triggers a sudden change in behavior. "
                            "A commuter might tolerate small fare increases for months, "
                            "but once the fare crosses a personal threshold, she buys a motorbike instead. "
                            "Thresholds remind us that consumer behavior is not always gradual — "
                            "sometimes a small change in conditions produces a big shift in choices.\n\n"
                            "Consumer choice theory ties together preferences, constraints, and trade-offs "
                            "into a framework that explains how people allocate their limited resources. "
                            "It is not a perfect description of every decision — "
                            "people are sometimes impulsive, emotional, or poorly informed. "
                            "But as a model of how rational consumers navigate scarcity, "
                            "it remains one of the most useful tools in economics."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích lựa chọn người tiêu dùng",
                    "description": "Viết đoạn văn tiếng Anh phân tích về lựa chọn tiêu dùng sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống kinh tế thực tế liên quan đến lựa chọn người tiêu dùng. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích cách một sinh viên đại học với ngân sách hạn chế đưa ra quyết định tiêu dùng hàng tháng. Giải thích budget constraint ảnh hưởng đến lựa chọn như thế nào, trade-off giữa các nhu cầu ra sao, và tại sao diminishing marginal utility khiến sinh viên phân bổ chi tiêu thay vì dồn hết vào một thứ.",
                            "Hãy chọn một sản phẩm hoặc dịch vụ phổ biến ở Việt Nam (ví dụ: trà sữa, xe máy, dịch vụ streaming) và phân tích hành vi tiêu dùng xung quanh sản phẩm đó. Giải thích utility mà người tiêu dùng nhận được, threshold giá mà tại đó họ thay đổi hành vi, và opportunity cost của việc chi tiêu cho sản phẩm đó thay vì lựa chọn khác."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay đầy năng lượng.",
                    "data": {
                        "text": (
                            "Bạn ơi, bạn vừa hoàn thành một hành trình tuyệt vời! "
                            "Hãy tự hào về bản thân mình — không phải ai cũng kiên trì đi hết 5 phần học "
                            "và nắm vững 18 từ vựng chuyên ngành kinh tế bằng tiếng Anh. "
                            "Bạn đã làm được, và chúng ta đã làm được cùng nhau!\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất — lần này, "
                            "hãy nghĩ về chúng như những công cụ mà bạn sẽ mang theo "
                            "vào mọi bài giảng và giáo trình kinh tế từ bây giờ.\n\n"
                            "Utility — lợi ích. Đây là từ bạn sẽ gặp nhiều nhất trong kinh tế vi mô. "
                            "Mỗi khi bạn mua một ly cà phê, xem một bộ phim, hay đọc một cuốn sách, "
                            "bạn đang nhận utility. Và bây giờ bạn biết cách nói về nó bằng tiếng Anh. "
                            "Ví dụ mới: The utility of learning a new language extends far beyond the classroom — "
                            "it opens doors to careers, friendships, and ways of thinking you never imagined.\n\n"
                            "Budget constraint — ràng buộc ngân sách. Hai từ này đi cùng nhau "
                            "như một cặp đôi không thể tách rời trong kinh tế học. "
                            "Ngân sách có hạn, nhưng mong muốn thì không — và đó chính là lý do "
                            "chúng ta cần kinh tế học. "
                            "Ví dụ mới: Even billionaires face a budget constraint on their time — "
                            "there are only twenty-four hours in a day, and every hour spent on one project "
                            "is an hour not spent on another.\n\n"
                            "Diminishing marginal utility — lợi ích cận biên giảm dần. "
                            "Đây là quy luật giải thích vì sao bạn không ăn phở ba bữa một ngày, "
                            "dù bạn rất thích phở. Mỗi đơn vị thêm vào mang lại ít hài lòng hơn. "
                            "Ví dụ mới: The diminishing marginal utility of checking your phone explains "
                            "why the hundredth notification of the day feels annoying rather than exciting.\n\n"
                            "Trade-off — sự đánh đổi. Mỗi quyết định đều có cái giá. "
                            "Khi bạn chọn A, bạn đang từ bỏ B. Hiểu trade-off giúp bạn "
                            "đưa ra quyết định sáng suốt hơn — không chỉ trong kinh tế, mà trong cuộc sống. "
                            "Ví dụ mới: The trade-off between working part-time and studying full-time "
                            "is one of the most common dilemmas facing university students in Vietnam.\n\n"
                            "Welfare — phúc lợi. Từ này nhắc nhở chúng ta rằng kinh tế học "
                            "không chỉ về tiền bạc — mà về chất lượng cuộc sống. "
                            "Mọi chính sách, mọi quyết định thị trường đều ảnh hưởng đến welfare của ai đó. "
                            "Ví dụ mới: Community libraries improve social welfare by giving everyone — "
                            "regardless of income — free access to knowledge and a quiet place to learn.\n\n"
                            "Threshold — ngưỡng. Từ này giải thích những khoảnh khắc bất ngờ "
                            "khi hành vi tiêu dùng thay đổi đột ngột. Không phải lúc nào thay đổi cũng từ từ — "
                            "đôi khi chỉ cần vượt qua một ngưỡng nhỏ là mọi thứ khác đi hoàn toàn. "
                            "Ví dụ mới: The threshold for switching from a free app to a paid subscription "
                            "is often lower than people expect — once they see the value, "
                            "they are willing to pay without hesitation.\n\n"
                            "Bạn biết không, bạn không chỉ học từ vựng — bạn đang xây dựng "
                            "một cách nhìn mới về thế giới. Mỗi lần bạn đi siêu thị, "
                            "bạn sẽ thấy utility và trade-off ở khắp nơi. "
                            "Mỗi lần đọc tin tức kinh tế, bạn sẽ hiểu sâu hơn vì sao "
                            "người tiêu dùng hành xử theo cách họ làm.\n\n"
                            "Và điều tuyệt vời nhất? Bạn không đi một mình. "
                            "Hàng nghìn sinh viên kinh tế khác cũng đang trên cùng hành trình này — "
                            "cùng học, cùng tiến bộ, cùng nâng cấp tiếng Anh chuyên ngành. "
                            "Hãy nghĩ về cộng đồng đó mỗi khi bạn cảm thấy khó khăn. "
                            "Bạn là một phần của đội ngũ, và đội ngũ này đang ngày càng mạnh hơn.\n\n"
                            "Chúc mừng bạn một lần nữa! Hẹn gặp lại ở bài học tiếp theo — "
                            "chúng ta sẽ tiếp tục chinh phục những đỉnh cao mới cùng nhau nhé!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Consumer Choice – Lựa Chọn Người Tiêu Dùng' AND uid = '{UID}' ORDER BY created_at;")
