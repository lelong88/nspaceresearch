"""
Create curriculum: Production Costs – Chi Phí Sản Xuất
Series A — Kinh Tế Vi Mô (Microeconomics), curriculum #4
18 words | 5 sessions | empathetic_observation tone | quiet awe farewell
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
W1 = ["variable", "fixed", "marginal", "output", "revenue", "profit"]
W2 = ["economies", "diseconomies", "average", "total", "diminish", "scale"]
W3 = ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Production Costs – Chi Phí Sản Xuất",
    "contentTypeTags": [],
    "description": (
        "BẠN BIẾT DOANH NGHIỆP CẦN LỢI NHUẬN — NHƯNG BẠN CÓ THẬT SỰ HIỂU CHI PHÍ ĐANG ĂN MÒN NÓ NHƯ THẾ NÀO KHÔNG?\n\n"
        "Mỗi lần giảng viên chiếu bảng tính chi phí sản xuất bằng tiếng Anh — fixed cost, variable cost, marginal cost — "
        "bạn nhìn thấy những con số nhưng không nắm được logic đằng sau. "
        "Bạn hiểu 'chi phí cố định' và 'chi phí biến đổi' bằng tiếng Việt, "
        "nhưng khi đọc case study tiếng Anh về quyết định sản xuất của một nhà máy, bạn bị lạc ngay đoạn đầu.\n\n"
        "Chi phí sản xuất giống như dòng nước ngầm chảy dưới mỗi quyết định kinh doanh — "
        "bạn không nhìn thấy nó trên bề mặt, nhưng nếu không hiểu nó, mọi phân tích đều sụp đổ. "
        "18 từ vựng trong bài học này chính là chiếc kính lặn giúp bạn nhìn rõ dòng chảy ấy.\n\n"
        "Sau khóa học, bạn sẽ đọc được bảng phân tích chi phí bằng tiếng Anh, "
        "hiểu khi nào doanh nghiệp nên mở rộng sản xuất và khi nào nên dừng lại, "
        "và tự tin thảo luận về breakeven point hay economies of scale trong lớp học.\n\n"
        "18 từ — từ variable đến breakeven — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy phân tích chi phí, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về chi phí sản xuất — trái tim của mọi quyết định kinh doanh. "
            "Bạn sẽ bắt đầu với variable, fixed, marginal, output, revenue, profit — "
            "những từ giúp bạn hiểu cấu trúc chi phí cơ bản của một doanh nghiệp và cách tính lợi nhuận. "
            "Tiếp theo là economies, diseconomies, average, total, diminish, scale — "
            "bộ từ vựng về lợi thế và bất lợi khi mở rộng quy mô sản xuất. "
            "Cuối cùng, productivity, efficiency, overhead, depreciation, capacity, breakeven "
            "đưa bạn vào thế giới quản lý chi phí thực tế của nhà máy và doanh nghiệp. "
            "Qua 3 bài đọc tiếng Anh về quyết định sản xuất, 1 phần ôn tập toàn diện "
            "và 1 bài đọc tổng hợp, bạn sẽ tự tin phân tích chi phí sản xuất bằng tiếng Anh — "
            "từ giảng đường đến phòng họp doanh nghiệp."
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
                    "description": "Chào mừng bạn đến với bài học về chi phí sản xuất — nền tảng phân tích doanh nghiệp.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ tư trong chuỗi từ vựng Kinh tế vi mô — "
                            "chủ đề hôm nay là Chi phí sản xuất, hay trong tiếng Anh là Production Costs. "
                            "Nếu bạn muốn hiểu vì sao một nhà máy quyết định sản xuất thêm hay dừng lại, "
                            "vì sao giá thành sản phẩm thay đổi khi quy mô tăng, "
                            "thì tất cả bắt đầu từ việc hiểu chi phí.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: variable, fixed, marginal, output, revenue, và profit. "
                            "Đây là những từ xuất hiện trong mọi bài giảng về lý thuyết doanh nghiệp "
                            "và phân tích chi phí sản xuất.\n\n"
                            "Từ đầu tiên là variable — tính từ — nghĩa là biến đổi, thay đổi theo mức sản lượng. "
                            "Trong kinh tế, variable cost là chi phí biến đổi — chi phí tăng hoặc giảm "
                            "tùy thuộc vào số lượng sản phẩm được sản xuất. "
                            "Ví dụ: 'The variable cost of a bakery includes flour and sugar, which increase as more cakes are baked.' "
                            "Trong bài đọc, variable mô tả những khoản chi phí mà doanh nghiệp chỉ phải trả "
                            "khi thực sự sản xuất hàng hóa.\n\n"
                            "Từ thứ hai là fixed — tính từ — nghĩa là cố định, không thay đổi theo sản lượng. "
                            "Fixed cost là chi phí cố định — dù sản xuất nhiều hay ít, khoản chi này vẫn giữ nguyên. "
                            "Ví dụ: 'The fixed cost of renting a factory remains the same whether the company produces one unit or one thousand units.' "
                            "Trong bài đọc, fixed đối lập với variable — hai loại chi phí cơ bản "
                            "mà mọi doanh nghiệp phải quản lý.\n\n"
                            "Từ thứ ba là marginal — tính từ — nghĩa là biên, liên quan đến sự thay đổi "
                            "khi sản xuất thêm một đơn vị sản phẩm. "
                            "Marginal cost là chi phí biên — chi phí phát sinh khi sản xuất thêm một đơn vị. "
                            "Ví dụ: 'The marginal cost of producing the hundredth shirt is lower than the first because the factory is already running.' "
                            "Trong bài đọc, marginal là khái niệm then chốt — doanh nghiệp so sánh marginal cost "
                            "với marginal revenue để quyết định có nên sản xuất thêm hay không.\n\n"
                            "Từ thứ tư là output — danh từ — nghĩa là sản lượng, "
                            "tổng số hàng hóa hoặc dịch vụ mà doanh nghiệp sản xuất ra. "
                            "Ví dụ: 'The factory increased its output from five hundred to eight hundred units per day after installing new machines.' "
                            "Trong bài đọc, output là biến số trung tâm — mọi phân tích chi phí "
                            "đều xoay quanh câu hỏi: sản xuất bao nhiêu là tối ưu?\n\n"
                            "Từ thứ năm là revenue — danh từ — nghĩa là doanh thu, "
                            "tổng số tiền doanh nghiệp thu được từ việc bán hàng hóa hoặc dịch vụ. "
                            "Ví dụ: 'The company's revenue doubled after it expanded into the online market.' "
                            "Trong bài đọc, revenue là một nửa của bài toán lợi nhuận — "
                            "doanh nghiệp so sánh revenue với cost để biết mình có lãi hay không.\n\n"
                            "Từ cuối cùng là profit — danh từ — nghĩa là lợi nhuận, "
                            "phần chênh lệch giữa doanh thu và tổng chi phí. "
                            "Ví dụ: 'The small coffee shop made a profit of ten million dong in its first month of operation.' "
                            "Trong bài đọc, profit là mục tiêu cuối cùng của doanh nghiệp — "
                            "mọi quyết định về chi phí đều nhằm tối đa hóa profit.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cấu trúc chi phí sản xuất để thấy các từ này trong ngữ cảnh thực tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chi phí sản xuất cơ bản",
                    "description": "Học 6 từ: variable, fixed, marginal, output, revenue, profit",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chi phí sản xuất cơ bản",
                    "description": "Học 6 từ: variable, fixed, marginal, output, revenue, profit",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chi phí sản xuất cơ bản",
                    "description": "Học 6 từ: variable, fixed, marginal, output, revenue, profit",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chi phí sản xuất cơ bản",
                    "description": "Học 6 từ: variable, fixed, marginal, output, revenue, profit",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chi phí sản xuất cơ bản",
                    "description": "Học 6 từ: variable, fixed, marginal, output, revenue, profit",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cấu trúc chi phí sản xuất",
                    "description": "Every business, from a street-side pho shop to a multinational factory, faces the same fundamental question: how much does it cost to produce one more unit?",
                    "data": {
                        "text": (
                            "Every business, from a street-side pho shop to a multinational factory, faces the same fundamental question: "
                            "how much does it cost to produce one more unit? "
                            "To answer this, economists divide production costs into two categories: fixed costs and variable costs.\n\n"
                            "A fixed cost does not change with the level of output. "
                            "Whether a garment factory produces ten shirts or ten thousand, "
                            "the monthly rent for the building stays the same. "
                            "Insurance premiums, equipment leases, and the salaries of permanent managers are all fixed costs. "
                            "Even if the factory shuts down for a week, these costs continue.\n\n"
                            "A variable cost, on the other hand, rises and falls with output. "
                            "The more shirts the factory produces, the more fabric, thread, and electricity it uses. "
                            "If production doubles, variable costs roughly double as well. "
                            "Raw materials, hourly wages for production workers, and packaging are typical variable costs.\n\n"
                            "The total cost of production is simply the sum of fixed and variable costs. "
                            "But for decision-making, economists focus on a more powerful concept: marginal cost. "
                            "Marginal cost is the additional cost of producing one more unit of output. "
                            "If a bakery already makes one hundred loaves of bread per day and the cost of making the one-hundred-and-first loaf "
                            "is three thousand dong, then the marginal cost at that level of output is three thousand dong.\n\n"
                            "Why does marginal cost matter so much? Because firms compare it to marginal revenue — "
                            "the additional revenue earned from selling one more unit. "
                            "Revenue is the total income a firm receives from selling its products. "
                            "If the bakery sells each loaf for five thousand dong, the marginal revenue is five thousand dong. "
                            "Since the marginal revenue exceeds the marginal cost, the bakery should produce that extra loaf.\n\n"
                            "A firm maximizes its profit when marginal cost equals marginal revenue. "
                            "Profit is the difference between total revenue and total cost. "
                            "If a firm produces too little, it leaves money on the table. "
                            "If it produces too much, the cost of extra units exceeds what they bring in. "
                            "The sweet spot — where profit is greatest — is where the marginal cost curve crosses the marginal revenue line.\n\n"
                            "Understanding the relationship between fixed costs, variable costs, output, revenue, and profit "
                            "is the foundation of every production decision a firm makes."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cấu trúc chi phí sản xuất",
                    "description": "Every business, from a street-side pho shop to a multinational factory, faces the same fundamental question: how much does it cost to produce one more unit?",
                    "data": {
                        "text": (
                            "Every business, from a street-side pho shop to a multinational factory, faces the same fundamental question: "
                            "how much does it cost to produce one more unit? "
                            "To answer this, economists divide production costs into two categories: fixed costs and variable costs.\n\n"
                            "A fixed cost does not change with the level of output. "
                            "Whether a garment factory produces ten shirts or ten thousand, "
                            "the monthly rent for the building stays the same. "
                            "Insurance premiums, equipment leases, and the salaries of permanent managers are all fixed costs. "
                            "Even if the factory shuts down for a week, these costs continue.\n\n"
                            "A variable cost, on the other hand, rises and falls with output. "
                            "The more shirts the factory produces, the more fabric, thread, and electricity it uses. "
                            "If production doubles, variable costs roughly double as well. "
                            "Raw materials, hourly wages for production workers, and packaging are typical variable costs.\n\n"
                            "The total cost of production is simply the sum of fixed and variable costs. "
                            "But for decision-making, economists focus on a more powerful concept: marginal cost. "
                            "Marginal cost is the additional cost of producing one more unit of output. "
                            "If a bakery already makes one hundred loaves of bread per day and the cost of making the one-hundred-and-first loaf "
                            "is three thousand dong, then the marginal cost at that level of output is three thousand dong.\n\n"
                            "Why does marginal cost matter so much? Because firms compare it to marginal revenue — "
                            "the additional revenue earned from selling one more unit. "
                            "Revenue is the total income a firm receives from selling its products. "
                            "If the bakery sells each loaf for five thousand dong, the marginal revenue is five thousand dong. "
                            "Since the marginal revenue exceeds the marginal cost, the bakery should produce that extra loaf.\n\n"
                            "A firm maximizes its profit when marginal cost equals marginal revenue. "
                            "Profit is the difference between total revenue and total cost. "
                            "If a firm produces too little, it leaves money on the table. "
                            "If it produces too much, the cost of extra units exceeds what they bring in. "
                            "The sweet spot — where profit is greatest — is where the marginal cost curve crosses the marginal revenue line.\n\n"
                            "Understanding the relationship between fixed costs, variable costs, output, revenue, and profit "
                            "is the foundation of every production decision a firm makes."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cấu trúc chi phí sản xuất",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every business, from a street-side pho shop to a multinational factory, faces the same fundamental question: "
                            "how much does it cost to produce one more unit? "
                            "To answer this, economists divide production costs into two categories: fixed costs and variable costs.\n\n"
                            "A fixed cost does not change with the level of output. "
                            "Whether a garment factory produces ten shirts or ten thousand, "
                            "the monthly rent for the building stays the same. "
                            "Insurance premiums, equipment leases, and the salaries of permanent managers are all fixed costs. "
                            "Even if the factory shuts down for a week, these costs continue.\n\n"
                            "A variable cost, on the other hand, rises and falls with output. "
                            "The more shirts the factory produces, the more fabric, thread, and electricity it uses. "
                            "If production doubles, variable costs roughly double as well. "
                            "Raw materials, hourly wages for production workers, and packaging are typical variable costs.\n\n"
                            "The total cost of production is simply the sum of fixed and variable costs. "
                            "But for decision-making, economists focus on a more powerful concept: marginal cost. "
                            "Marginal cost is the additional cost of producing one more unit of output. "
                            "If a bakery already makes one hundred loaves of bread per day and the cost of making the one-hundred-and-first loaf "
                            "is three thousand dong, then the marginal cost at that level of output is three thousand dong.\n\n"
                            "Why does marginal cost matter so much? Because firms compare it to marginal revenue — "
                            "the additional revenue earned from selling one more unit. "
                            "Revenue is the total income a firm receives from selling its products. "
                            "If the bakery sells each loaf for five thousand dong, the marginal revenue is five thousand dong. "
                            "Since the marginal revenue exceeds the marginal cost, the bakery should produce that extra loaf.\n\n"
                            "A firm maximizes its profit when marginal cost equals marginal revenue. "
                            "Profit is the difference between total revenue and total cost. "
                            "If a firm produces too little, it leaves money on the table. "
                            "If it produces too much, the cost of extra units exceeds what they bring in. "
                            "The sweet spot — where profit is greatest — is where the marginal cost curve crosses the marginal revenue line.\n\n"
                            "Understanding the relationship between fixed costs, variable costs, output, revenue, and profit "
                            "is the foundation of every production decision a firm makes."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chi phí sản xuất cơ bản",
                    "description": "Viết câu sử dụng 6 từ vựng về chi phí sản xuất.",
                    "data": {
                        "vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit"],
                        "items": [
                            {
                                "targetVocab": "variable",
                                "prompt": "Dùng từ 'variable' để viết một câu về chi phí biến đổi của một doanh nghiệp khi sản lượng thay đổi. Ví dụ: The variable costs of the shoe factory rose sharply when it doubled its monthly output because it needed twice as much leather and rubber."
                            },
                            {
                                "targetVocab": "fixed",
                                "prompt": "Dùng từ 'fixed' để viết một câu về chi phí cố định mà doanh nghiệp phải trả bất kể sản xuất nhiều hay ít. Ví dụ: The fixed costs of running the restaurant include rent and insurance, which must be paid even during months when few customers visit."
                            },
                            {
                                "targetVocab": "marginal",
                                "prompt": "Dùng từ 'marginal' để viết một câu về chi phí biên khi sản xuất thêm một đơn vị sản phẩm. Ví dụ: The marginal cost of printing one additional textbook is very low because the printing press is already set up and running."
                            },
                            {
                                "targetVocab": "output",
                                "prompt": "Dùng từ 'output' để viết một câu về sản lượng của một nhà máy hoặc doanh nghiệp. Ví dụ: The ceramic factory increased its daily output from two hundred to three hundred vases after hiring ten more skilled workers."
                            },
                            {
                                "targetVocab": "revenue",
                                "prompt": "Dùng từ 'revenue' để viết một câu về doanh thu của một doanh nghiệp từ việc bán sản phẩm hoặc dịch vụ. Ví dụ: The online bookstore generated most of its revenue during the back-to-school season when parents bought textbooks for their children."
                            },
                            {
                                "targetVocab": "profit",
                                "prompt": "Dùng từ 'profit' để viết một câu về lợi nhuận và mối quan hệ giữa doanh thu và chi phí. Ví dụ: The new milk tea shop earned a healthy profit in its second quarter because its revenue grew faster than its costs."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về quy mô sản xuất và lợi thế kinh tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "variable — biến đổi, fixed — cố định, marginal — biên, "
                            "output — sản lượng, revenue — doanh thu, và profit — lợi nhuận. "
                            "Bạn đã hiểu cách doanh nghiệp phân tích chi phí để tối đa hóa lợi nhuận. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào câu hỏi: điều gì xảy ra khi doanh nghiệp mở rộng quy mô?\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: economies, diseconomies, average, total, diminish, và scale. "
                            "Những từ này giúp bạn hiểu vì sao một số công ty lớn hơn lại rẻ hơn, "
                            "trong khi những công ty khác lại gặp rắc rối khi phình to quá mức.\n\n"
                            "Từ đầu tiên là economies — danh từ — trong ngữ cảnh kinh tế, "
                            "economies of scale nghĩa là lợi thế kinh tế nhờ quy mô — "
                            "khi sản xuất nhiều hơn, chi phí trung bình trên mỗi đơn vị giảm xuống. "
                            "Ví dụ: 'The car manufacturer achieved economies of scale by producing one million vehicles per year, reducing the cost per car significantly.' "
                            "Trong bài đọc, economies mô tả lợi ích mà doanh nghiệp lớn có được "
                            "nhờ phân bổ chi phí cố định trên nhiều sản phẩm hơn.\n\n"
                            "Từ thứ hai là diseconomies — danh từ — nghĩa là bất lợi kinh tế nhờ quy mô, "
                            "khi doanh nghiệp quá lớn và chi phí trung bình bắt đầu tăng trở lại. "
                            "Ví dụ: 'The corporation experienced diseconomies of scale when its management structure became so complex that communication slowed down.' "
                            "Trong bài đọc, diseconomies là mặt trái của việc mở rộng — "
                            "khi tổ chức quá cồng kềnh, hiệu quả giảm và chi phí tăng.\n\n"
                            "Từ thứ ba là average — tính từ — nghĩa là trung bình. "
                            "Average cost là chi phí trung bình — tổng chi phí chia cho số lượng sản phẩm. "
                            "Ví dụ: 'The average cost of producing a pair of shoes dropped from eighty thousand to fifty thousand dong when the factory doubled its output.' "
                            "Trong bài đọc, average cost là thước đo quan trọng — "
                            "doanh nghiệp theo dõi nó để biết mình đang sản xuất hiệu quả hay không.\n\n"
                            "Từ thứ tư là total — tính từ — nghĩa là tổng cộng. "
                            "Total cost là tổng chi phí — bao gồm cả chi phí cố định và chi phí biến đổi. "
                            "Ví dụ: 'The total cost of running the restaurant last month was one hundred and fifty million dong, including rent, ingredients, and staff wages.' "
                            "Trong bài đọc, total cost là điểm xuất phát để tính lợi nhuận — "
                            "revenue trừ total cost bằng profit.\n\n"
                            "Từ thứ năm là diminish — động từ — nghĩa là giảm dần, suy giảm. "
                            "Trong kinh tế, diminishing returns nghĩa là hiệu suất giảm dần — "
                            "khi thêm ngày càng nhiều một yếu tố sản xuất, lợi ích bổ sung ngày càng nhỏ. "
                            "Ví dụ: 'Adding a fifth worker to the small kitchen did not help much — the returns began to diminish because there was not enough space for everyone.' "
                            "Trong bài đọc, diminish giải thích vì sao chi phí biên thường tăng "
                            "sau một mức sản lượng nhất định.\n\n"
                            "Từ cuối cùng là scale — danh từ — nghĩa là quy mô, kích thước hoạt động của doanh nghiệp. "
                            "Ví dụ: 'The startup grew rapidly and reached a scale where it could negotiate better prices with suppliers.' "
                            "Trong bài đọc, scale là yếu tố quyết định — "
                            "doanh nghiệp cần tìm quy mô tối ưu để tận dụng economies of scale "
                            "mà không rơi vào diseconomies.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về quy mô sản xuất và lợi thế kinh tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Quy mô sản xuất và lợi thế kinh tế",
                    "description": "Học 6 từ: economies, diseconomies, average, total, diminish, scale",
                    "data": {"vocabList": ["economies", "diseconomies", "average", "total", "diminish", "scale"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Quy mô sản xuất và lợi thế kinh tế",
                    "description": "Học 6 từ: economies, diseconomies, average, total, diminish, scale",
                    "data": {"vocabList": ["economies", "diseconomies", "average", "total", "diminish", "scale"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Quy mô sản xuất và lợi thế kinh tế",
                    "description": "Học 6 từ: economies, diseconomies, average, total, diminish, scale",
                    "data": {"vocabList": ["economies", "diseconomies", "average", "total", "diminish", "scale"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Quy mô sản xuất và lợi thế kinh tế",
                    "description": "Học 6 từ: economies, diseconomies, average, total, diminish, scale",
                    "data": {"vocabList": ["economies", "diseconomies", "average", "total", "diminish", "scale"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Quy mô sản xuất và lợi thế kinh tế",
                    "description": "Học 6 từ: economies, diseconomies, average, total, diminish, scale",
                    "data": {"vocabList": ["economies", "diseconomies", "average", "total", "diminish", "scale"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Quy mô sản xuất và hiệu suất giảm dần",
                    "description": "When a small coffee roaster in Da Nang first opened, the owner did everything alone — roasting, grinding, packaging, and delivering.",
                    "data": {
                        "text": (
                            "When a small coffee roaster in Da Nang first opened, the owner did everything alone — "
                            "roasting, grinding, packaging, and delivering. "
                            "As orders grew, she hired workers and bought a larger roasting machine. "
                            "Something interesting happened: the average cost per kilogram of coffee dropped. "
                            "This is the power of economies of scale.\n\n"
                            "Economies of scale occur when a firm increases its scale of production "
                            "and the average cost per unit falls. "
                            "There are several reasons this happens. "
                            "First, fixed costs like rent and equipment are spread over more units. "
                            "If a factory pays one hundred million dong per month in rent and produces ten thousand units, "
                            "the fixed cost per unit is ten thousand dong. "
                            "If it produces fifty thousand units, the fixed cost per unit drops to just two thousand dong.\n\n"
                            "Second, larger firms can buy raw materials in bulk at lower prices. "
                            "Third, they can invest in specialized machinery that smaller firms cannot afford. "
                            "The total cost still rises as output increases, but the average cost — "
                            "total cost divided by the number of units — falls.\n\n"
                            "However, growth does not always bring benefits. "
                            "When a firm becomes too large, it may experience diseconomies of scale. "
                            "Communication becomes slower as messages pass through many layers of management. "
                            "Workers may feel disconnected from the company's goals. "
                            "Coordination problems multiply, and the average cost per unit starts to rise again.\n\n"
                            "There is also a fundamental law that limits growth: diminishing returns. "
                            "Imagine a small workshop with five sewing machines. "
                            "Hiring a sixth worker increases output significantly because each machine now has a dedicated operator. "
                            "But hiring a seventh worker adds less, because that worker must wait for a free machine. "
                            "An eighth worker adds even less. The returns from each additional worker diminish.\n\n"
                            "Diminishing returns explain why the marginal cost curve eventually slopes upward. "
                            "At low levels of output, adding more workers or materials increases production efficiently. "
                            "But beyond a certain point, each additional unit of input produces less additional output, "
                            "and the cost of each extra unit rises.\n\n"
                            "The goal for every firm is to find the scale at which average cost is lowest — "
                            "large enough to enjoy economies of scale, but not so large that diseconomies set in. "
                            "This optimal scale varies by industry. "
                            "A steel mill needs massive scale to be efficient. "
                            "A local bakery may reach its optimal scale with just a handful of employees."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Quy mô sản xuất và hiệu suất giảm dần",
                    "description": "When a small coffee roaster in Da Nang first opened, the owner did everything alone — roasting, grinding, packaging, and delivering.",
                    "data": {
                        "text": (
                            "When a small coffee roaster in Da Nang first opened, the owner did everything alone — "
                            "roasting, grinding, packaging, and delivering. "
                            "As orders grew, she hired workers and bought a larger roasting machine. "
                            "Something interesting happened: the average cost per kilogram of coffee dropped. "
                            "This is the power of economies of scale.\n\n"
                            "Economies of scale occur when a firm increases its scale of production "
                            "and the average cost per unit falls. "
                            "There are several reasons this happens. "
                            "First, fixed costs like rent and equipment are spread over more units. "
                            "If a factory pays one hundred million dong per month in rent and produces ten thousand units, "
                            "the fixed cost per unit is ten thousand dong. "
                            "If it produces fifty thousand units, the fixed cost per unit drops to just two thousand dong.\n\n"
                            "Second, larger firms can buy raw materials in bulk at lower prices. "
                            "Third, they can invest in specialized machinery that smaller firms cannot afford. "
                            "The total cost still rises as output increases, but the average cost — "
                            "total cost divided by the number of units — falls.\n\n"
                            "However, growth does not always bring benefits. "
                            "When a firm becomes too large, it may experience diseconomies of scale. "
                            "Communication becomes slower as messages pass through many layers of management. "
                            "Workers may feel disconnected from the company's goals. "
                            "Coordination problems multiply, and the average cost per unit starts to rise again.\n\n"
                            "There is also a fundamental law that limits growth: diminishing returns. "
                            "Imagine a small workshop with five sewing machines. "
                            "Hiring a sixth worker increases output significantly because each machine now has a dedicated operator. "
                            "But hiring a seventh worker adds less, because that worker must wait for a free machine. "
                            "An eighth worker adds even less. The returns from each additional worker diminish.\n\n"
                            "Diminishing returns explain why the marginal cost curve eventually slopes upward. "
                            "At low levels of output, adding more workers or materials increases production efficiently. "
                            "But beyond a certain point, each additional unit of input produces less additional output, "
                            "and the cost of each extra unit rises.\n\n"
                            "The goal for every firm is to find the scale at which average cost is lowest — "
                            "large enough to enjoy economies of scale, but not so large that diseconomies set in. "
                            "This optimal scale varies by industry. "
                            "A steel mill needs massive scale to be efficient. "
                            "A local bakery may reach its optimal scale with just a handful of employees."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Quy mô sản xuất và hiệu suất giảm dần",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When a small coffee roaster in Da Nang first opened, the owner did everything alone — "
                            "roasting, grinding, packaging, and delivering. "
                            "As orders grew, she hired workers and bought a larger roasting machine. "
                            "Something interesting happened: the average cost per kilogram of coffee dropped. "
                            "This is the power of economies of scale.\n\n"
                            "Economies of scale occur when a firm increases its scale of production "
                            "and the average cost per unit falls. "
                            "There are several reasons this happens. "
                            "First, fixed costs like rent and equipment are spread over more units. "
                            "If a factory pays one hundred million dong per month in rent and produces ten thousand units, "
                            "the fixed cost per unit is ten thousand dong. "
                            "If it produces fifty thousand units, the fixed cost per unit drops to just two thousand dong.\n\n"
                            "Second, larger firms can buy raw materials in bulk at lower prices. "
                            "Third, they can invest in specialized machinery that smaller firms cannot afford. "
                            "The total cost still rises as output increases, but the average cost — "
                            "total cost divided by the number of units — falls.\n\n"
                            "However, growth does not always bring benefits. "
                            "When a firm becomes too large, it may experience diseconomies of scale. "
                            "Communication becomes slower as messages pass through many layers of management. "
                            "Workers may feel disconnected from the company's goals. "
                            "Coordination problems multiply, and the average cost per unit starts to rise again.\n\n"
                            "There is also a fundamental law that limits growth: diminishing returns. "
                            "Imagine a small workshop with five sewing machines. "
                            "Hiring a sixth worker increases output significantly because each machine now has a dedicated operator. "
                            "But hiring a seventh worker adds less, because that worker must wait for a free machine. "
                            "An eighth worker adds even less. The returns from each additional worker diminish.\n\n"
                            "Diminishing returns explain why the marginal cost curve eventually slopes upward. "
                            "At low levels of output, adding more workers or materials increases production efficiently. "
                            "But beyond a certain point, each additional unit of input produces less additional output, "
                            "and the cost of each extra unit rises.\n\n"
                            "The goal for every firm is to find the scale at which average cost is lowest — "
                            "large enough to enjoy economies of scale, but not so large that diseconomies set in. "
                            "This optimal scale varies by industry. "
                            "A steel mill needs massive scale to be efficient. "
                            "A local bakery may reach its optimal scale with just a handful of employees."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Quy mô sản xuất và lợi thế kinh tế",
                    "description": "Viết câu sử dụng 6 từ vựng về quy mô sản xuất.",
                    "data": {
                        "vocabList": ["economies", "diseconomies", "average", "total", "diminish", "scale"],
                        "items": [
                            {
                                "targetVocab": "economies",
                                "prompt": "Dùng từ 'economies' để viết một câu về lợi thế kinh tế nhờ quy mô khi doanh nghiệp mở rộng sản xuất. Ví dụ: The electronics company achieved economies of scale by building a second factory, which allowed it to cut the price of each unit by fifteen percent."
                            },
                            {
                                "targetVocab": "diseconomies",
                                "prompt": "Dùng từ 'diseconomies' để viết một câu về bất lợi khi doanh nghiệp phát triển quá lớn. Ví dụ: The multinational corporation suffered from diseconomies of scale when its headquarters could no longer coordinate effectively with dozens of overseas branches."
                            },
                            {
                                "targetVocab": "average",
                                "prompt": "Dùng từ 'average' để viết một câu về chi phí trung bình trên mỗi đơn vị sản phẩm. Ví dụ: The average cost of producing a bottle of fish sauce fell from eight thousand to five thousand dong after the company upgraded its bottling line."
                            },
                            {
                                "targetVocab": "total",
                                "prompt": "Dùng từ 'total' để viết một câu về tổng chi phí sản xuất bao gồm cả chi phí cố định và biến đổi. Ví dụ: The total cost of operating the textile mill last quarter included forty million dong in rent and one hundred and twenty million dong in raw materials."
                            },
                            {
                                "targetVocab": "diminish",
                                "prompt": "Dùng từ 'diminish' để viết một câu về hiện tượng hiệu suất giảm dần khi thêm yếu tố sản xuất. Ví dụ: The benefits of hiring additional tutors began to diminish after the tenth tutor, because there were not enough students to fill their schedules."
                            },
                            {
                                "targetVocab": "scale",
                                "prompt": "Dùng từ 'scale' để viết một câu về quy mô hoạt động của một doanh nghiệp và ảnh hưởng đến chi phí. Ví dụ: The startup needed to reach a larger scale of production before it could compete on price with established brands in the market."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về năng suất, hiệu quả và điểm hòa vốn.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: variable, fixed, marginal, output, revenue, profit — "
                            "những khái niệm cơ bản về cấu trúc chi phí và lợi nhuận. "
                            "Trong phần 2, bạn đã học thêm economies, diseconomies, average, total, diminish, scale — "
                            "giúp bạn hiểu điều gì xảy ra khi doanh nghiệp mở rộng hoặc thu hẹp quy mô.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào thế giới quản lý chi phí thực tế: "
                            "làm sao để đo lường hiệu quả, theo dõi chi phí ẩn, và biết khi nào doanh nghiệp bắt đầu có lãi? "
                            "Bạn sẽ học 6 từ mới: productivity, efficiency, overhead, depreciation, capacity, và breakeven.\n\n"
                            "Từ đầu tiên là productivity — danh từ — nghĩa là năng suất, "
                            "lượng sản phẩm được tạo ra trên mỗi đơn vị đầu vào (lao động, thời gian, vốn). "
                            "Ví dụ: 'The factory improved its productivity by training workers to use the new assembly line, producing thirty percent more units per hour.' "
                            "Trong bài đọc, productivity là thước đo hiệu quả sản xuất — "
                            "năng suất cao nghĩa là doanh nghiệp tạo ra nhiều hơn với ít hơn.\n\n"
                            "Từ thứ hai là efficiency — danh từ — nghĩa là hiệu quả, "
                            "khả năng đạt được kết quả tối đa với nguồn lực tối thiểu. "
                            "Ví dụ: 'The new software improved the efficiency of the accounting department by automating repetitive calculations.' "
                            "Trong bài đọc, efficiency liên quan chặt chẽ đến productivity — "
                            "một doanh nghiệp hiệu quả là doanh nghiệp không lãng phí nguồn lực.\n\n"
                            "Từ thứ ba là overhead — danh từ — nghĩa là chi phí chung, "
                            "những chi phí gián tiếp không liên quan trực tiếp đến sản xuất sản phẩm "
                            "nhưng cần thiết để doanh nghiệp vận hành. "
                            "Ví dụ: 'The company's overhead includes office rent, utility bills, and the salaries of administrative staff.' "
                            "Trong bài đọc, overhead là phần chi phí mà nhiều doanh nghiệp nhỏ thường bỏ qua "
                            "khi tính giá thành sản phẩm — dẫn đến định giá sai.\n\n"
                            "Từ thứ tư là depreciation — danh từ — nghĩa là khấu hao, "
                            "sự giảm giá trị của tài sản theo thời gian do sử dụng hoặc lỗi thời. "
                            "Ví dụ: 'The delivery trucks lose twenty percent of their value each year due to depreciation, which the company records as a cost.' "
                            "Trong bài đọc, depreciation là chi phí 'vô hình' — "
                            "bạn không trả tiền mặt mỗi tháng, nhưng giá trị máy móc vẫn giảm dần.\n\n"
                            "Từ thứ năm là capacity — danh từ — nghĩa là công suất, "
                            "mức sản lượng tối đa mà doanh nghiệp có thể đạt được với nguồn lực hiện có. "
                            "Ví dụ: 'The hotel is running at full capacity during the summer season, with every room booked weeks in advance.' "
                            "Trong bài đọc, capacity quyết định giới hạn sản xuất — "
                            "khi doanh nghiệp hoạt động gần hết capacity, chi phí biên thường tăng nhanh.\n\n"
                            "Từ cuối cùng là breakeven — danh từ và tính từ — nghĩa là hòa vốn, "
                            "điểm mà tại đó tổng doanh thu bằng tổng chi phí và doanh nghiệp không lãi cũng không lỗ. "
                            "Ví dụ: 'The new restaurant reached its breakeven point after six months, meaning it finally covered all its startup and operating costs.' "
                            "Trong bài đọc, breakeven là cột mốc quan trọng nhất cho mọi doanh nghiệp mới — "
                            "trước breakeven là lỗ, sau breakeven là lãi.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về năng suất, hiệu quả và điểm hòa vốn nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Năng suất, hiệu quả và điểm hòa vốn",
                    "description": "Học 6 từ: productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Năng suất, hiệu quả và điểm hòa vốn",
                    "description": "Học 6 từ: productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Năng suất, hiệu quả và điểm hòa vốn",
                    "description": "Học 6 từ: productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Năng suất, hiệu quả và điểm hòa vốn",
                    "description": "Học 6 từ: productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Năng suất, hiệu quả và điểm hòa vốn",
                    "description": "Học 6 từ: productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Năng suất, chi phí ẩn và điểm hòa vốn",
                    "description": "A young entrepreneur in Ho Chi Minh City opens a small workshop to produce handmade leather bags.",
                    "data": {
                        "text": (
                            "A young entrepreneur in Ho Chi Minh City opens a small workshop to produce handmade leather bags. "
                            "She invests in cutting tools, sewing machines, and a small team of three craftspeople. "
                            "Her first question is simple but critical: how many bags does she need to sell before she stops losing money? "
                            "The answer lies in understanding productivity, efficiency, overhead, depreciation, capacity, and the breakeven point.\n\n"
                            "Productivity measures how much output a worker or machine produces per unit of time. "
                            "If each craftsperson makes two bags per day, the workshop's productivity is six bags per day. "
                            "To increase productivity, the entrepreneur could invest in better tools, "
                            "provide training, or redesign the workflow so that each person specializes in one step.\n\n"
                            "Efficiency is closely related but broader. "
                            "A workshop is efficient when it uses the least amount of leather, time, and energy to produce each bag. "
                            "Waste — whether wasted material, wasted motion, or wasted hours — reduces efficiency. "
                            "High productivity with low waste means high efficiency.\n\n"
                            "But producing bags is not the only cost. "
                            "The entrepreneur also pays for overhead — the indirect costs of running the business. "
                            "Overhead includes rent for the workshop, electricity, internet, accounting fees, "
                            "and the salary of an assistant who handles orders and shipping. "
                            "These costs do not change much whether she makes six bags or sixty. "
                            "Many small business owners underestimate overhead and set prices too low as a result.\n\n"
                            "There is another hidden cost: depreciation. "
                            "The sewing machines she bought for fifty million dong will not last forever. "
                            "Each year, they lose value due to wear and tear. "
                            "If a machine lasts five years, its depreciation is ten million dong per year — "
                            "a cost that must be included in the price of each bag, even though no cash leaves the bank account each month.\n\n"
                            "The workshop also has a capacity limit. "
                            "With three workers and the current equipment, the maximum output is about twenty bags per day. "
                            "That is the workshop's capacity. "
                            "If demand grows beyond twenty bags, the entrepreneur must decide whether to hire more workers, "
                            "buy more machines, or turn away orders. "
                            "Operating near full capacity often increases costs because workers must rush, "
                            "overtime wages kick in, and mistakes become more frequent.\n\n"
                            "Now, the critical question: when does the business start making money? "
                            "The breakeven point is the level of sales at which total revenue equals total cost. "
                            "Below breakeven, the business loses money. Above it, every additional sale contributes to profit. "
                            "If the entrepreneur's total monthly costs — including variable costs, overhead, and depreciation — "
                            "are thirty million dong, and she sells each bag for five hundred thousand dong, "
                            "she needs to sell sixty bags per month just to break even.\n\n"
                            "Understanding these six concepts helps any business owner make smarter decisions: "
                            "invest in productivity improvements, control overhead, plan for depreciation, "
                            "respect capacity limits, and always know where the breakeven point is."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Năng suất, chi phí ẩn và điểm hòa vốn",
                    "description": "A young entrepreneur in Ho Chi Minh City opens a small workshop to produce handmade leather bags.",
                    "data": {
                        "text": (
                            "A young entrepreneur in Ho Chi Minh City opens a small workshop to produce handmade leather bags. "
                            "She invests in cutting tools, sewing machines, and a small team of three craftspeople. "
                            "Her first question is simple but critical: how many bags does she need to sell before she stops losing money? "
                            "The answer lies in understanding productivity, efficiency, overhead, depreciation, capacity, and the breakeven point.\n\n"
                            "Productivity measures how much output a worker or machine produces per unit of time. "
                            "If each craftsperson makes two bags per day, the workshop's productivity is six bags per day. "
                            "To increase productivity, the entrepreneur could invest in better tools, "
                            "provide training, or redesign the workflow so that each person specializes in one step.\n\n"
                            "Efficiency is closely related but broader. "
                            "A workshop is efficient when it uses the least amount of leather, time, and energy to produce each bag. "
                            "Waste — whether wasted material, wasted motion, or wasted hours — reduces efficiency. "
                            "High productivity with low waste means high efficiency.\n\n"
                            "But producing bags is not the only cost. "
                            "The entrepreneur also pays for overhead — the indirect costs of running the business. "
                            "Overhead includes rent for the workshop, electricity, internet, accounting fees, "
                            "and the salary of an assistant who handles orders and shipping. "
                            "These costs do not change much whether she makes six bags or sixty. "
                            "Many small business owners underestimate overhead and set prices too low as a result.\n\n"
                            "There is another hidden cost: depreciation. "
                            "The sewing machines she bought for fifty million dong will not last forever. "
                            "Each year, they lose value due to wear and tear. "
                            "If a machine lasts five years, its depreciation is ten million dong per year — "
                            "a cost that must be included in the price of each bag, even though no cash leaves the bank account each month.\n\n"
                            "The workshop also has a capacity limit. "
                            "With three workers and the current equipment, the maximum output is about twenty bags per day. "
                            "That is the workshop's capacity. "
                            "If demand grows beyond twenty bags, the entrepreneur must decide whether to hire more workers, "
                            "buy more machines, or turn away orders. "
                            "Operating near full capacity often increases costs because workers must rush, "
                            "overtime wages kick in, and mistakes become more frequent.\n\n"
                            "Now, the critical question: when does the business start making money? "
                            "The breakeven point is the level of sales at which total revenue equals total cost. "
                            "Below breakeven, the business loses money. Above it, every additional sale contributes to profit. "
                            "If the entrepreneur's total monthly costs — including variable costs, overhead, and depreciation — "
                            "are thirty million dong, and she sells each bag for five hundred thousand dong, "
                            "she needs to sell sixty bags per month just to break even.\n\n"
                            "Understanding these six concepts helps any business owner make smarter decisions: "
                            "invest in productivity improvements, control overhead, plan for depreciation, "
                            "respect capacity limits, and always know where the breakeven point is."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Năng suất, chi phí ẩn và điểm hòa vốn",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "A young entrepreneur in Ho Chi Minh City opens a small workshop to produce handmade leather bags. "
                            "She invests in cutting tools, sewing machines, and a small team of three craftspeople. "
                            "Her first question is simple but critical: how many bags does she need to sell before she stops losing money? "
                            "The answer lies in understanding productivity, efficiency, overhead, depreciation, capacity, and the breakeven point.\n\n"
                            "Productivity measures how much output a worker or machine produces per unit of time. "
                            "If each craftsperson makes two bags per day, the workshop's productivity is six bags per day. "
                            "To increase productivity, the entrepreneur could invest in better tools, "
                            "provide training, or redesign the workflow so that each person specializes in one step.\n\n"
                            "Efficiency is closely related but broader. "
                            "A workshop is efficient when it uses the least amount of leather, time, and energy to produce each bag. "
                            "Waste — whether wasted material, wasted motion, or wasted hours — reduces efficiency. "
                            "High productivity with low waste means high efficiency.\n\n"
                            "But producing bags is not the only cost. "
                            "The entrepreneur also pays for overhead — the indirect costs of running the business. "
                            "Overhead includes rent for the workshop, electricity, internet, accounting fees, "
                            "and the salary of an assistant who handles orders and shipping. "
                            "These costs do not change much whether she makes six bags or sixty. "
                            "Many small business owners underestimate overhead and set prices too low as a result.\n\n"
                            "There is another hidden cost: depreciation. "
                            "The sewing machines she bought for fifty million dong will not last forever. "
                            "Each year, they lose value due to wear and tear. "
                            "If a machine lasts five years, its depreciation is ten million dong per year — "
                            "a cost that must be included in the price of each bag, even though no cash leaves the bank account each month.\n\n"
                            "The workshop also has a capacity limit. "
                            "With three workers and the current equipment, the maximum output is about twenty bags per day. "
                            "That is the workshop's capacity. "
                            "If demand grows beyond twenty bags, the entrepreneur must decide whether to hire more workers, "
                            "buy more machines, or turn away orders. "
                            "Operating near full capacity often increases costs because workers must rush, "
                            "overtime wages kick in, and mistakes become more frequent.\n\n"
                            "Now, the critical question: when does the business start making money? "
                            "The breakeven point is the level of sales at which total revenue equals total cost. "
                            "Below breakeven, the business loses money. Above it, every additional sale contributes to profit. "
                            "If the entrepreneur's total monthly costs — including variable costs, overhead, and depreciation — "
                            "are thirty million dong, and she sells each bag for five hundred thousand dong, "
                            "she needs to sell sixty bags per month just to break even.\n\n"
                            "Understanding these six concepts helps any business owner make smarter decisions: "
                            "invest in productivity improvements, control overhead, plan for depreciation, "
                            "respect capacity limits, and always know where the breakeven point is."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Năng suất, hiệu quả và điểm hòa vốn",
                    "description": "Viết câu sử dụng 6 từ vựng về năng suất và quản lý chi phí.",
                    "data": {
                        "vocabList": ["productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"],
                        "items": [
                            {
                                "targetVocab": "productivity",
                                "prompt": "Dùng từ 'productivity' để viết một câu về năng suất lao động trong một nhà máy hoặc văn phòng. Ví dụ: The garment factory boosted its productivity by twenty percent after introducing an automated cutting machine that reduced manual labor."
                            },
                            {
                                "targetVocab": "efficiency",
                                "prompt": "Dùng từ 'efficiency' để viết một câu về hiệu quả sử dụng nguồn lực trong sản xuất. Ví dụ: The new layout of the warehouse improved efficiency by shortening the distance workers had to walk between the packing station and the loading dock."
                            },
                            {
                                "targetVocab": "overhead",
                                "prompt": "Dùng từ 'overhead' để viết một câu về chi phí chung mà doanh nghiệp phải gánh chịu ngoài chi phí sản xuất trực tiếp. Ví dụ: The startup kept its overhead low by working from a shared office space instead of renting a private building."
                            },
                            {
                                "targetVocab": "depreciation",
                                "prompt": "Dùng từ 'depreciation' để viết một câu về sự giảm giá trị của tài sản theo thời gian. Ví dụ: The company recorded five million dong in depreciation for its delivery van this year, reflecting the wear from daily use on rough roads."
                            },
                            {
                                "targetVocab": "capacity",
                                "prompt": "Dùng từ 'capacity' để viết một câu về công suất tối đa của một nhà máy hoặc cơ sở sản xuất. Ví dụ: The cement plant is operating at ninety percent of its capacity, and any further increase in orders would require building a new production line."
                            },
                            {
                                "targetVocab": "breakeven",
                                "prompt": "Dùng từ 'breakeven' để viết một câu về điểm hòa vốn của một doanh nghiệp mới. Ví dụ: The owner of the new gym calculated that she needs at least two hundred members to reach the breakeven point and start earning a profit."
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
                    "title": "Giới thiệu phần ôn tập",
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Hãy ôn tập toàn bộ.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã hoàn thành cả ba phần học từ vựng về chi phí sản xuất. "
                            "Hãy cùng nhìn lại hành trình.\n\n"
                            "Trong phần 1, bạn đã học variable, fixed, marginal, output, revenue, profit — "
                            "bộ từ vựng nền tảng về cấu trúc chi phí và cách doanh nghiệp tính lợi nhuận. "
                            "Bạn đã hiểu sự khác biệt giữa chi phí cố định và chi phí biến đổi, "
                            "và vì sao chi phí biên là chìa khóa cho mọi quyết định sản xuất.\n\n"
                            "Trong phần 2, bạn đã học economies, diseconomies, average, total, diminish, scale — "
                            "giúp bạn phân tích điều gì xảy ra khi doanh nghiệp thay đổi quy mô. "
                            "Bạn đã biết vì sao sản xuất lớn hơn có thể rẻ hơn, "
                            "nhưng cũng biết giới hạn của việc mở rộng.\n\n"
                            "Trong phần 3, bạn đã học productivity, efficiency, overhead, depreciation, capacity, breakeven — "
                            "bộ công cụ để đo lường hiệu quả và quản lý chi phí thực tế. "
                            "Bạn đã hiểu những chi phí ẩn như overhead và depreciation, "
                            "và biết cách tính điểm hòa vốn.\n\n"
                            "Bây giờ là lúc ôn tập toàn bộ 18 từ. "
                            "Bạn sẽ làm lại flashcard với tất cả các từ, "
                            "sau đó viết câu sử dụng từng từ trong ngữ cảnh mới. "
                            "Hãy tập trung và tận hưởng quá trình ôn tập nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: variable, fixed, marginal, output, revenue, profit, economies, diseconomies, average, total, diminish, scale, productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: variable, fixed, marginal, output, revenue, profit, economies, diseconomies, average, total, diminish, scale, productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: variable, fixed, marginal, output, revenue, profit, economies, diseconomies, average, total, diminish, scale, productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: variable, fixed, marginal, output, revenue, profit, economies, diseconomies, average, total, diminish, scale, productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: variable, fixed, marginal, output, revenue, profit, economies, diseconomies, average, total, diminish, scale, productivity, efficiency, overhead, depreciation, capacity, breakeven",
                    "data": {"vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng chi phí sản xuất",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"],
                        "items": [
                            {
                                "targetVocab": "variable",
                                "prompt": "Dùng từ 'variable' để viết một câu về chi phí biến đổi trong ngành nông nghiệp Việt Nam. Ví dụ: The variable costs of a rice farm include seeds, fertilizer, and seasonal labor, all of which increase when the farmer plants a larger area."
                            },
                            {
                                "targetVocab": "fixed",
                                "prompt": "Dùng từ 'fixed' để viết một câu về chi phí cố định của một cửa hàng bán lẻ. Ví dụ: The fixed costs of the clothing boutique remain at fifteen million dong per month regardless of whether sales are strong or weak."
                            },
                            {
                                "targetVocab": "marginal",
                                "prompt": "Dùng từ 'marginal' để viết một câu về quyết định sản xuất dựa trên chi phí biên. Ví dụ: The factory manager decided to accept the extra order because the marginal cost of producing five hundred more units was lower than the price the client offered."
                            },
                            {
                                "targetVocab": "output",
                                "prompt": "Dùng từ 'output' để viết một câu về sản lượng của một ngành công nghiệp tại Việt Nam. Ví dụ: Vietnam's total output of seafood has grown steadily over the past decade, making it one of the world's top exporters of shrimp and catfish."
                            },
                            {
                                "targetVocab": "revenue",
                                "prompt": "Dùng từ 'revenue' để viết một câu về doanh thu của một doanh nghiệp thương mại điện tử. Ví dụ: The e-commerce platform saw its revenue jump by forty percent during the year-end sale as millions of shoppers placed orders online."
                            },
                            {
                                "targetVocab": "profit",
                                "prompt": "Dùng từ 'profit' để viết một câu về lợi nhuận và chiến lược giảm chi phí. Ví dụ: The furniture company increased its profit not by raising prices but by negotiating cheaper wood supplies and reducing waste in the workshop."
                            },
                            {
                                "targetVocab": "economies",
                                "prompt": "Dùng từ 'economies' để viết một câu về lợi thế kinh tế nhờ quy mô trong ngành sản xuất. Ví dụ: The Vietnamese steel industry benefits from economies of scale because large mills can spread the cost of blast furnaces across millions of tons of output."
                            },
                            {
                                "targetVocab": "diseconomies",
                                "prompt": "Dùng từ 'diseconomies' để viết một câu về bất lợi khi một tổ chức trở nên quá lớn. Ví dụ: The state-owned enterprise faced diseconomies of scale as its bloated bureaucracy slowed decision-making and increased administrative costs."
                            },
                            {
                                "targetVocab": "average",
                                "prompt": "Dùng từ 'average' để viết một câu về chi phí trung bình và cách nó thay đổi theo sản lượng. Ví dụ: The average cost per cup of bubble tea dropped significantly after the chain opened its tenth store and centralized ingredient purchasing."
                            },
                            {
                                "targetVocab": "total",
                                "prompt": "Dùng từ 'total' để viết một câu về tổng chi phí vận hành một doanh nghiệp nhỏ. Ví dụ: The total cost of running the tutoring center includes teacher salaries, room rental, printed materials, and marketing expenses."
                            },
                            {
                                "targetVocab": "diminish",
                                "prompt": "Dùng từ 'diminish' để viết một câu về hiệu suất giảm dần trong một tình huống thực tế. Ví dụ: The effectiveness of additional advertising spending began to diminish after the brand had already reached most of its target audience."
                            },
                            {
                                "targetVocab": "scale",
                                "prompt": "Dùng từ 'scale' để viết một câu về quy mô sản xuất và tác động đến khả năng cạnh tranh. Ví dụ: The craft brewery struggled to compete on price because it lacked the scale to buy hops and barley at the same discount as large breweries."
                            },
                            {
                                "targetVocab": "productivity",
                                "prompt": "Dùng từ 'productivity' để viết một câu về cách công nghệ cải thiện năng suất lao động. Ví dụ: The introduction of barcode scanners at the warehouse tripled the productivity of the inventory team by eliminating manual counting."
                            },
                            {
                                "targetVocab": "efficiency",
                                "prompt": "Dùng từ 'efficiency' để viết một câu về hiệu quả sử dụng năng lượng trong sản xuất. Ví dụ: The solar panel factory improved its energy efficiency by recycling heat from the production process to warm the building in winter."
                            },
                            {
                                "targetVocab": "overhead",
                                "prompt": "Dùng từ 'overhead' để viết một câu về chi phí chung và cách doanh nghiệp cắt giảm chúng. Ví dụ: The consulting firm reduced its overhead by allowing employees to work from home three days a week, saving millions in office rent."
                            },
                            {
                                "targetVocab": "depreciation",
                                "prompt": "Dùng từ 'depreciation' để viết một câu về khấu hao tài sản và ảnh hưởng đến báo cáo tài chính. Ví dụ: The airline records significant depreciation on its fleet of aircraft each year, which reduces its reported profit even when ticket sales are strong."
                            },
                            {
                                "targetVocab": "capacity",
                                "prompt": "Dùng từ 'capacity' để viết một câu về công suất sản xuất và quyết định đầu tư mở rộng. Ví dụ: The chip manufacturer announced plans to build a new plant because its existing facilities were running at full capacity and could not meet growing demand."
                            },
                            {
                                "targetVocab": "breakeven",
                                "prompt": "Dùng từ 'breakeven' để viết một câu về điểm hòa vốn và kế hoạch kinh doanh. Ví dụ: The investor asked the startup founder how many months it would take to reach the breakeven point before committing any funding to the project."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về chi phí sản xuất.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về chi phí sản xuất — từ cấu trúc chi phí cơ bản "
                            "đến quyết định mở rộng quy mô và quản lý hiệu quả.\n\n"
                            "Bạn sẽ gặp lại variable, fixed, marginal, output, revenue, profit "
                            "trong phần mở đầu về cách doanh nghiệp phân tích chi phí. "
                            "Tiếp theo, economies, diseconomies, average, total, diminish, scale "
                            "sẽ giúp bạn hiểu sâu hơn về lợi thế và bất lợi của quy mô. "
                            "Và cuối cùng, productivity, efficiency, overhead, depreciation, capacity, breakeven "
                            "sẽ đưa bạn vào thế giới quản lý chi phí thực tế.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chi phí sản xuất — Bức tranh toàn cảnh",
                    "description": "Behind every product you buy — from a bowl of pho to a smartphone — lies a web of costs that the producer must manage.",
                    "data": {
                        "text": (
                            "Behind every product you buy — from a bowl of pho to a smartphone — "
                            "lies a web of costs that the producer must manage. "
                            "Understanding production costs is essential for anyone studying economics, "
                            "because costs determine prices, shape competition, and drive the decisions firms make every day.\n\n"
                            "Every firm faces two broad categories of cost. "
                            "Fixed costs do not change with the level of output. "
                            "Rent, insurance, and the salaries of permanent staff remain the same "
                            "whether the factory produces one unit or one million. "
                            "Variable costs, by contrast, rise and fall with production. "
                            "Raw materials, energy, and hourly wages are variable — "
                            "the more a firm produces, the more it spends on these inputs. "
                            "The total cost of production is the sum of fixed and variable costs.\n\n"
                            "For decision-making, the most important concept is marginal cost — "
                            "the additional cost of producing one more unit of output. "
                            "A rational firm compares marginal cost to marginal revenue, "
                            "the extra income from selling one more unit. "
                            "As long as marginal revenue exceeds marginal cost, the firm should keep producing. "
                            "The point where marginal cost equals marginal revenue is where profit is maximized. "
                            "Revenue is the total income from sales, and profit is what remains after subtracting total cost.\n\n"
                            "What happens when a firm grows? "
                            "At first, increasing the scale of production brings economies of scale. "
                            "The average cost per unit falls because fixed costs are spread over more output, "
                            "bulk purchasing lowers material prices, and specialized workers become more productive. "
                            "A small furniture workshop paying fifty million dong in monthly rent "
                            "has a high average fixed cost if it makes only one hundred chairs. "
                            "But if it scales up to one thousand chairs, the rent per chair drops tenfold.\n\n"
                            "However, there is a limit. "
                            "If the firm grows too large, it may encounter diseconomies of scale. "
                            "Management layers multiply, communication slows, and coordination becomes difficult. "
                            "The average cost per unit begins to rise again. "
                            "Meanwhile, the law of diminishing returns reminds us that adding more of one input — "
                            "say, more workers to a fixed number of machines — eventually yields less and less additional output. "
                            "The returns from each extra worker diminish, pushing marginal cost upward.\n\n"
                            "Beyond the textbook categories, real firms must also manage productivity, efficiency, and overhead. "
                            "Productivity measures how much output each worker or machine generates. "
                            "A factory that produces five hundred units per worker per day is more productive "
                            "than one that produces three hundred. "
                            "Efficiency goes further — it asks whether the firm is minimizing waste of materials, time, and energy. "
                            "High productivity with low waste equals high efficiency.\n\n"
                            "Overhead refers to the indirect costs of running a business — "
                            "office rent, utilities, administrative salaries, and software subscriptions. "
                            "These costs are real but easy to overlook when calculating the price of a product. "
                            "Similarly, depreciation captures the gradual loss of value in equipment and machinery. "
                            "A delivery truck that costs two hundred million dong and lasts ten years "
                            "loses twenty million dong in value each year. "
                            "This depreciation must be factored into the cost of each delivery.\n\n"
                            "Every firm also has a capacity — the maximum output it can achieve with its current resources. "
                            "Operating well below capacity means fixed costs are spread over too few units, raising average cost. "
                            "Operating at or above capacity strains workers and equipment, increasing marginal cost and error rates.\n\n"
                            "Finally, every business owner wants to know: when will I stop losing money? "
                            "The breakeven point is the level of output at which total revenue equals total cost. "
                            "Below breakeven, the firm operates at a loss. Above it, every additional unit sold contributes to profit. "
                            "Calculating the breakeven point requires knowing fixed costs, variable cost per unit, and the selling price.\n\n"
                            "From the street vendor calculating whether to buy a second cart "
                            "to the multinational deciding whether to build a new factory, "
                            "the logic of production costs is the same. "
                            "Fixed and variable, marginal and average, economies and diseconomies — "
                            "these concepts form the language of every business decision."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chi phí sản xuất — Bức tranh toàn cảnh",
                    "description": "Behind every product you buy — from a bowl of pho to a smartphone — lies a web of costs that the producer must manage.",
                    "data": {
                        "text": (
                            "Behind every product you buy — from a bowl of pho to a smartphone — "
                            "lies a web of costs that the producer must manage. "
                            "Understanding production costs is essential for anyone studying economics, "
                            "because costs determine prices, shape competition, and drive the decisions firms make every day.\n\n"
                            "Every firm faces two broad categories of cost. "
                            "Fixed costs do not change with the level of output. "
                            "Rent, insurance, and the salaries of permanent staff remain the same "
                            "whether the factory produces one unit or one million. "
                            "Variable costs, by contrast, rise and fall with production. "
                            "Raw materials, energy, and hourly wages are variable — "
                            "the more a firm produces, the more it spends on these inputs. "
                            "The total cost of production is the sum of fixed and variable costs.\n\n"
                            "For decision-making, the most important concept is marginal cost — "
                            "the additional cost of producing one more unit of output. "
                            "A rational firm compares marginal cost to marginal revenue, "
                            "the extra income from selling one more unit. "
                            "As long as marginal revenue exceeds marginal cost, the firm should keep producing. "
                            "The point where marginal cost equals marginal revenue is where profit is maximized. "
                            "Revenue is the total income from sales, and profit is what remains after subtracting total cost.\n\n"
                            "What happens when a firm grows? "
                            "At first, increasing the scale of production brings economies of scale. "
                            "The average cost per unit falls because fixed costs are spread over more output, "
                            "bulk purchasing lowers material prices, and specialized workers become more productive. "
                            "A small furniture workshop paying fifty million dong in monthly rent "
                            "has a high average fixed cost if it makes only one hundred chairs. "
                            "But if it scales up to one thousand chairs, the rent per chair drops tenfold.\n\n"
                            "However, there is a limit. "
                            "If the firm grows too large, it may encounter diseconomies of scale. "
                            "Management layers multiply, communication slows, and coordination becomes difficult. "
                            "The average cost per unit begins to rise again. "
                            "Meanwhile, the law of diminishing returns reminds us that adding more of one input — "
                            "say, more workers to a fixed number of machines — eventually yields less and less additional output. "
                            "The returns from each extra worker diminish, pushing marginal cost upward.\n\n"
                            "Beyond the textbook categories, real firms must also manage productivity, efficiency, and overhead. "
                            "Productivity measures how much output each worker or machine generates. "
                            "A factory that produces five hundred units per worker per day is more productive "
                            "than one that produces three hundred. "
                            "Efficiency goes further — it asks whether the firm is minimizing waste of materials, time, and energy. "
                            "High productivity with low waste equals high efficiency.\n\n"
                            "Overhead refers to the indirect costs of running a business — "
                            "office rent, utilities, administrative salaries, and software subscriptions. "
                            "These costs are real but easy to overlook when calculating the price of a product. "
                            "Similarly, depreciation captures the gradual loss of value in equipment and machinery. "
                            "A delivery truck that costs two hundred million dong and lasts ten years "
                            "loses twenty million dong in value each year. "
                            "This depreciation must be factored into the cost of each delivery.\n\n"
                            "Every firm also has a capacity — the maximum output it can achieve with its current resources. "
                            "Operating well below capacity means fixed costs are spread over too few units, raising average cost. "
                            "Operating at or above capacity strains workers and equipment, increasing marginal cost and error rates.\n\n"
                            "Finally, every business owner wants to know: when will I stop losing money? "
                            "The breakeven point is the level of output at which total revenue equals total cost. "
                            "Below breakeven, the firm operates at a loss. Above it, every additional unit sold contributes to profit. "
                            "Calculating the breakeven point requires knowing fixed costs, variable cost per unit, and the selling price.\n\n"
                            "From the street vendor calculating whether to buy a second cart "
                            "to the multinational deciding whether to build a new factory, "
                            "the logic of production costs is the same. "
                            "Fixed and variable, marginal and average, economies and diseconomies — "
                            "these concepts form the language of every business decision."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chi phí sản xuất — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Behind every product you buy — from a bowl of pho to a smartphone — "
                            "lies a web of costs that the producer must manage. "
                            "Understanding production costs is essential for anyone studying economics, "
                            "because costs determine prices, shape competition, and drive the decisions firms make every day.\n\n"
                            "Every firm faces two broad categories of cost. "
                            "Fixed costs do not change with the level of output. "
                            "Rent, insurance, and the salaries of permanent staff remain the same "
                            "whether the factory produces one unit or one million. "
                            "Variable costs, by contrast, rise and fall with production. "
                            "Raw materials, energy, and hourly wages are variable — "
                            "the more a firm produces, the more it spends on these inputs. "
                            "The total cost of production is the sum of fixed and variable costs.\n\n"
                            "For decision-making, the most important concept is marginal cost — "
                            "the additional cost of producing one more unit of output. "
                            "A rational firm compares marginal cost to marginal revenue, "
                            "the extra income from selling one more unit. "
                            "As long as marginal revenue exceeds marginal cost, the firm should keep producing. "
                            "The point where marginal cost equals marginal revenue is where profit is maximized. "
                            "Revenue is the total income from sales, and profit is what remains after subtracting total cost.\n\n"
                            "What happens when a firm grows? "
                            "At first, increasing the scale of production brings economies of scale. "
                            "The average cost per unit falls because fixed costs are spread over more output, "
                            "bulk purchasing lowers material prices, and specialized workers become more productive. "
                            "A small furniture workshop paying fifty million dong in monthly rent "
                            "has a high average fixed cost if it makes only one hundred chairs. "
                            "But if it scales up to one thousand chairs, the rent per chair drops tenfold.\n\n"
                            "However, there is a limit. "
                            "If the firm grows too large, it may encounter diseconomies of scale. "
                            "Management layers multiply, communication slows, and coordination becomes difficult. "
                            "The average cost per unit begins to rise again. "
                            "Meanwhile, the law of diminishing returns reminds us that adding more of one input — "
                            "say, more workers to a fixed number of machines — eventually yields less and less additional output. "
                            "The returns from each extra worker diminish, pushing marginal cost upward.\n\n"
                            "Beyond the textbook categories, real firms must also manage productivity, efficiency, and overhead. "
                            "Productivity measures how much output each worker or machine generates. "
                            "A factory that produces five hundred units per worker per day is more productive "
                            "than one that produces three hundred. "
                            "Efficiency goes further — it asks whether the firm is minimizing waste of materials, time, and energy. "
                            "High productivity with low waste equals high efficiency.\n\n"
                            "Overhead refers to the indirect costs of running a business — "
                            "office rent, utilities, administrative salaries, and software subscriptions. "
                            "These costs are real but easy to overlook when calculating the price of a product. "
                            "Similarly, depreciation captures the gradual loss of value in equipment and machinery. "
                            "A delivery truck that costs two hundred million dong and lasts ten years "
                            "loses twenty million dong in value each year. "
                            "This depreciation must be factored into the cost of each delivery.\n\n"
                            "Every firm also has a capacity — the maximum output it can achieve with its current resources. "
                            "Operating well below capacity means fixed costs are spread over too few units, raising average cost. "
                            "Operating at or above capacity strains workers and equipment, increasing marginal cost and error rates.\n\n"
                            "Finally, every business owner wants to know: when will I stop losing money? "
                            "The breakeven point is the level of output at which total revenue equals total cost. "
                            "Below breakeven, the firm operates at a loss. Above it, every additional unit sold contributes to profit. "
                            "Calculating the breakeven point requires knowing fixed costs, variable cost per unit, and the selling price.\n\n"
                            "From the street vendor calculating whether to buy a second cart "
                            "to the multinational deciding whether to build a new factory, "
                            "the logic of production costs is the same. "
                            "Fixed and variable, marginal and average, economies and diseconomies — "
                            "these concepts form the language of every business decision."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chi phí sản xuất",
                    "description": "Viết đoạn văn tiếng Anh phân tích về chi phí sản xuất sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["variable", "fixed", "marginal", "output", "revenue", "profit", "economies", "diseconomies", "average", "total", "diminish", "scale", "productivity", "efficiency", "overhead", "depreciation", "capacity", "breakeven"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống kinh tế thực tế liên quan đến chi phí sản xuất. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích quyết định mở rộng quy mô của một nhà máy sản xuất giày tại Việt Nam. Giải thích cách economies of scale giúp giảm average cost, nhưng cũng nêu rủi ro của diseconomies khi quy mô quá lớn. Doanh nghiệp cần xem xét những yếu tố nào về capacity, overhead, và depreciation trước khi quyết định đầu tư?",
                            "Hãy tưởng tượng bạn là chủ một quán cà phê mới mở. Phân tích cấu trúc chi phí của quán: đâu là fixed costs, đâu là variable costs? Bạn cần bán bao nhiêu ly cà phê mỗi tháng để đạt breakeven point? Làm thế nào để tăng productivity và efficiency nhằm tối đa hóa profit?"
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay đầy chiêm nghiệm.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành một hành trình đặc biệt. "
                            "Hãy dừng lại một chút — không phải để vội vàng sang bài tiếp theo, "
                            "mà để cảm nhận điều bạn vừa làm được.\n\n"
                            "Bạn đã đi từ những khái niệm tưởng chừng khô khan — chi phí cố định, chi phí biến đổi, "
                            "điểm hòa vốn — và biến chúng thành ngôn ngữ sống động bằng tiếng Anh. "
                            "Đó không phải là chuyện nhỏ. Đó là một bước tiến thật sự.\n\n"
                            "Hãy cùng nhìn lại một số từ đã đồng hành cùng bạn.\n\n"
                            "Marginal — biên. Có lẽ đây là từ đẹp nhất trong kinh tế học. "
                            "Nó nhắc bạn rằng mọi quyết định lớn đều bắt đầu từ một câu hỏi nhỏ: "
                            "'Nếu tôi làm thêm một đơn vị nữa, điều gì sẽ thay đổi?' "
                            "Ví dụ mới: The marginal cost of streaming one more song on a music platform is nearly zero, "
                            "which is why subscription services can offer millions of tracks for a flat monthly fee.\n\n"
                            "Economies — lợi thế kinh tế nhờ quy mô. "
                            "Từ này chứa đựng một sự thật kỳ diệu: đôi khi, làm nhiều hơn lại tốn ít hơn. "
                            "Khi bạn hiểu economies of scale, bạn hiểu vì sao những công ty lớn "
                            "có thể bán sản phẩm với giá mà doanh nghiệp nhỏ không thể cạnh tranh. "
                            "Ví dụ mới: The ride-hailing app achieved economies of scale by spreading its technology costs "
                            "across millions of daily trips in dozens of cities.\n\n"
                            "Breakeven — hòa vốn. Từ này mang trong mình cả hy vọng lẫn lo âu "
                            "của mọi người khởi nghiệp. Trước breakeven là những đêm mất ngủ, "
                            "sau breakeven là ánh sáng cuối đường hầm. "
                            "Ví dụ mới: The organic farm finally passed its breakeven point in the third year, "
                            "when loyal customers and word-of-mouth referrals pushed monthly sales above the cost of land, labor, and seeds.\n\n"
                            "Depreciation — khấu hao. Từ này dạy bạn một bài học sâu sắc: "
                            "mọi thứ đều mất giá trị theo thời gian — máy móc, xe cộ, công nghệ. "
                            "Nhưng kiến thức thì không. Những gì bạn học hôm nay sẽ không bị khấu hao. "
                            "Ví dụ mới: The hospital must account for the depreciation of its MRI scanner, "
                            "which loses about fifteen percent of its value each year as newer models enter the market.\n\n"
                            "Efficiency — hiệu quả. Trong một thế giới mà nguồn lực luôn có hạn, "
                            "efficiency không chỉ là mục tiêu kinh doanh — nó là triết lý sống. "
                            "Làm nhiều hơn với ít hơn. Không lãng phí. Tôn trọng từng giọt mồ hôi. "
                            "Ví dụ mới: The zero-waste restaurant achieved remarkable efficiency "
                            "by turning vegetable scraps into soup stock and coffee grounds into compost for its rooftop garden.\n\n"
                            "Profit — lợi nhuận. Đằng sau con số lợi nhuận là câu chuyện "
                            "về hàng trăm quyết định nhỏ — mua nguyên liệu ở đâu, thuê bao nhiêu người, "
                            "định giá sản phẩm ra sao. Profit không phải là điểm đến — nó là kết quả "
                            "của việc hiểu và quản lý tất cả những chi phí bạn vừa học. "
                            "Ví dụ mới: The family-owned noodle factory has maintained a steady profit for three generations "
                            "by keeping variable costs low and investing wisely in equipment that lasts.\n\n"
                            "Bạn biết không, có một điều kỳ lạ về chi phí sản xuất. "
                            "Khi bạn chưa hiểu nó, nó chỉ là những con số vô hồn trên bảng tính. "
                            "Nhưng khi bạn đã hiểu — khi bạn nhìn thấy fixed cost đằng sau tiền thuê nhà, "
                            "marginal cost đằng sau mỗi quyết định sản xuất, "
                            "depreciation đằng sau chiếc máy cũ trong xưởng — "
                            "thì mỗi con số bỗng kể một câu chuyện.\n\n"
                            "Và bạn, bây giờ, đã có thể đọc những câu chuyện ấy bằng tiếng Anh.\n\n"
                            "Hãy mang theo 18 từ vựng này vào giảng đường, vào phòng họp, "
                            "vào những cuốn sách kinh tế mà trước đây bạn ngại mở. "
                            "Chúc bạn luôn giữ được sự tò mò và niềm say mê khám phá. "
                            "Hẹn gặp lại bạn ở bài học tiếp theo."
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Production Costs – Chi Phí Sản Xuất' AND uid = '{UID}' ORDER BY created_at;")
