"""
Create curriculum: Cost Accounting – Kế Toán Chi Phí
Series D — Kế Toán & Tài Chính Doanh Nghiệp (Accounting & Corporate Finance), curriculum #2
18 words | 5 sessions | metaphor_led tone | practical momentum farewell
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
W1 = ["cost", "budget", "variance", "overhead", "allocation", "direct"]
W2 = ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]
W3 = ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Cost Accounting – Kế Toán Chi Phí",
    "contentTypeTags": [],
    "description": (
        "KẾ TOÁN CHI PHÍ GIỐNG NHƯ TẤM BẢN ĐỒ NHIỆT CỦA DOANH NGHIỆP — NƠI NÀO ĐANG 'NÓNG' VÌ CHI TIÊU QUÁ MỨC, NƠI NÀO ĐANG 'LẠNH' VÌ THIẾU ĐẦU TƯ.\n\n"
        "Bạn ngồi trong phòng họp, giám đốc tài chính chiếu bảng phân tích chi phí sản xuất lên màn hình. "
        "Bạn hiểu 'chi phí trực tiếp' và 'chi phí gián tiếp' bằng tiếng Việt, "
        "nhưng khi đối tác Nhật Bản hỏi về variance analysis và absorption costing — "
        "bạn chỉ biết gật đầu mà không thể phản hồi. "
        "Những thuật ngữ này không phức tạp về logic, "
        "nhưng chúng là ngôn ngữ chung của mọi hệ thống quản trị chi phí trên thế giới.\n\n"
        "Hãy nghĩ về 18 từ vựng kế toán chi phí này như bộ cảm biến tài chính — "
        "một khi bạn gắn chúng vào tư duy, bạn sẽ 'đọc' được sức khỏe chi phí "
        "của bất kỳ doanh nghiệp nào chỉ qua một bảng báo cáo. "
        "Từ budget đến breakeven, từ overhead đến benchmark — "
        "bạn sẽ nắm được 'nhịp thở' tài chính mà mọi nhà quản lý cần hiểu.\n\n"
        "Sau khóa học, bạn sẽ tự tin phân tích báo cáo chi phí bằng tiếng Anh, "
        "thảo luận về variance analysis trong buổi họp đa quốc gia, "
        "và viết nhận xét về hiệu quả chi phí doanh nghiệp bằng ngôn ngữ chuyên ngành.\n\n"
        "18 từ vựng — từ cost đến uncontrollable — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy quản trị chi phí, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về kế toán chi phí — "
            "ngôn ngữ mà mọi nhà quản lý dùng để kiểm soát và tối ưu hóa chi tiêu doanh nghiệp. "
            "Bạn sẽ học cost, budget, variance, overhead, allocation, direct trong phần đầu tiên, "
            "nơi bài đọc giải thích cách doanh nghiệp phân loại và theo dõi chi phí sản xuất. "
            "Tiếp theo là indirect, standard, actual, absorption, marginal, contribution — "
            "những từ giúp bạn hiểu các phương pháp tính giá thành sản phẩm. "
            "Cuối cùng, breakeven, forecast, performance, benchmark, controllable, uncontrollable "
            "đưa bạn vào thế giới phân tích hòa vốn và đánh giá hiệu quả chi phí. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu báo cáo chi phí bằng tiếng Anh — "
            "không cần dừng lại tra từ điển mỗi dòng."
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
                    "description": "Chào mừng bạn đến với bài học về kế toán chi phí.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ hai trong chuỗi từ vựng Kế toán và Tài chính doanh nghiệp — "
                            "chủ đề hôm nay là Kế toán chi phí, hay trong tiếng Anh là Cost Accounting. "
                            "Nếu báo cáo tài chính cho bạn bức tranh tổng thể về doanh nghiệp, "
                            "thì kế toán chi phí đi sâu vào bên trong — phân tích từng đồng chi tiêu, "
                            "từ nguyên vật liệu đến tiền lương, từ chi phí nhà xưởng đến quảng cáo.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: cost, budget, variance, overhead, allocation, và direct. "
                            "Đây là những từ nền tảng nhất trong kế toán chi phí — "
                            "bạn sẽ gặp chúng trong mọi báo cáo quản trị.\n\n"
                            "Từ đầu tiên là cost — danh từ — nghĩa là chi phí, "
                            "tổng số tiền mà doanh nghiệp phải bỏ ra để sản xuất hàng hóa hoặc cung cấp dịch vụ. "
                            "Ví dụ: 'The total cost of producing one thousand units includes raw materials, labor, and factory maintenance.' "
                            "Trong bài đọc, cost là khái niệm trung tâm — "
                            "mọi quyết định quản trị đều xoay quanh việc kiểm soát và tối ưu hóa chi phí.\n\n"
                            "Từ thứ hai là budget — danh từ — nghĩa là ngân sách, "
                            "kế hoạch tài chính dự kiến cho một khoảng thời gian nhất định. "
                            "Ví dụ: 'The marketing department submitted a budget of five billion dong for the next quarter, covering advertising, events, and digital campaigns.' "
                            "Trong bài đọc, budget là công cụ kiểm soát — "
                            "nó đặt ra giới hạn chi tiêu và mục tiêu tài chính cho từng bộ phận.\n\n"
                            "Từ thứ ba là variance — danh từ — nghĩa là chênh lệch, "
                            "sự khác biệt giữa con số dự kiến trong ngân sách và con số thực tế. "
                            "Ví dụ: 'The production department reported a favorable variance of two hundred million dong because raw material prices dropped unexpectedly.' "
                            "Trong bài đọc, variance là tín hiệu cảnh báo — "
                            "nó cho biết bộ phận nào đang chi tiêu đúng kế hoạch và bộ phận nào đang vượt ngân sách.\n\n"
                            "Từ thứ tư là overhead — danh từ — nghĩa là chi phí chung, "
                            "những chi phí không liên quan trực tiếp đến sản xuất nhưng cần thiết để vận hành doanh nghiệp. "
                            "Ví dụ: 'Factory overhead includes electricity, equipment maintenance, and the salaries of supervisors who do not work directly on the production line.' "
                            "Trong bài đọc, overhead là phần chi phí khó kiểm soát nhất — "
                            "nó không gắn trực tiếp với sản phẩm nhưng ảnh hưởng lớn đến giá thành.\n\n"
                            "Từ thứ năm là allocation — danh từ — nghĩa là phân bổ, "
                            "quá trình chia chi phí chung cho các sản phẩm, bộ phận hoặc dự án khác nhau. "
                            "Ví dụ: 'The accountant used machine hours as the basis for allocation of factory overhead to each product line.' "
                            "Trong bài đọc, allocation là nghệ thuật — "
                            "cách bạn phân bổ chi phí ảnh hưởng trực tiếp đến giá thành sản phẩm.\n\n"
                            "Từ cuối cùng là direct — tính từ — nghĩa là trực tiếp, "
                            "mô tả chi phí có thể gắn trực tiếp với một sản phẩm hoặc dịch vụ cụ thể. "
                            "Ví dụ: 'Direct costs for the furniture factory include the wood, fabric, and wages of workers who assemble each piece by hand.' "
                            "Trong bài đọc, direct costs là phần dễ theo dõi nhất — "
                            "bạn biết chính xác bao nhiêu tiền đã chi cho từng sản phẩm.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách doanh nghiệp phân loại và kiểm soát chi phí nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chi phí, ngân sách và phân bổ",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {"vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chi phí, ngân sách và phân bổ",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {"vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chi phí, ngân sách và phân bổ",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {"vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chi phí, ngân sách và phân bổ",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {"vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chi phí, ngân sách và phân bổ",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {"vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phân loại và kiểm soát chi phí",
                    "description": "Every business, whether it makes shoes or software, needs to understand where its money goes.",
                    "data": {
                        "text": (
                            "Every business, whether it makes shoes or software, "
                            "needs to understand where its money goes. "
                            "Cost accounting is the branch of accounting that tracks, classifies, "
                            "and analyzes every dong a company spends. "
                            "Without it, managers would be making decisions in the dark.\n\n"
                            "The most basic concept is cost itself. "
                            "In accounting, a cost is any expenditure incurred to produce goods or deliver services. "
                            "A Vietnamese garment factory, for example, has many types of costs: "
                            "the fabric it buys, the wages it pays to sewing workers, "
                            "the electricity that powers the machines, and the rent for the factory building. "
                            "Some of these costs are easy to trace to a specific product. "
                            "Others are shared across the entire operation.\n\n"
                            "Costs that can be traced directly to a product are called direct costs. "
                            "In the garment factory, the fabric used to make a shirt is a direct cost — "
                            "you can measure exactly how many meters of fabric go into each shirt "
                            "and calculate the cost precisely. "
                            "The wages of the worker who sews that shirt are also a direct cost. "
                            "Direct costs are straightforward to track "
                            "because they have a clear, measurable link to the product.\n\n"
                            "But not all costs are so easy to assign. "
                            "The factory's electricity bill, the salary of the quality control manager, "
                            "and the cost of maintaining the sewing machines — "
                            "these are overhead costs. "
                            "Overhead refers to expenses that support the production process "
                            "but cannot be traced to a single product. "
                            "A factory might produce ten different styles of clothing, "
                            "and the electricity powers all of them equally.\n\n"
                            "This is where allocation becomes important. "
                            "Allocation is the process of distributing overhead costs "
                            "across different products or departments. "
                            "The accountant must choose a fair basis for allocation. "
                            "For example, if Product A uses sixty percent of the machine hours "
                            "and Product B uses forty percent, "
                            "the factory might allocate sixty percent of the electricity cost to Product A "
                            "and forty percent to Product B. "
                            "The choice of allocation method can significantly affect "
                            "the reported cost of each product.\n\n"
                            "To keep costs under control, companies create a budget. "
                            "A budget is a financial plan that sets spending limits "
                            "for each department and each category of cost. "
                            "At the beginning of the year, the production manager might receive "
                            "a budget of eight billion dong for raw materials. "
                            "The marketing team might get three billion dong for advertising. "
                            "The budget serves as a roadmap — "
                            "it tells everyone how much they can spend and what results are expected.\n\n"
                            "At the end of each month or quarter, accountants compare "
                            "actual spending to the budget. "
                            "The difference between what was planned and what actually happened "
                            "is called a variance. "
                            "If the production department spent seven billion dong on materials "
                            "instead of the budgeted eight billion, "
                            "there is a favorable variance of one billion dong — "
                            "the department spent less than expected. "
                            "If it spent nine billion, there is an unfavorable variance — "
                            "the department exceeded its budget. "
                            "Variance analysis helps managers identify problems early "
                            "and take corrective action before costs spiral out of control."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phân loại và kiểm soát chi phí",
                    "description": "Every business, whether it makes shoes or software, needs to understand where its money goes.",
                    "data": {
                        "text": (
                            "Every business, whether it makes shoes or software, "
                            "needs to understand where its money goes. "
                            "Cost accounting is the branch of accounting that tracks, classifies, "
                            "and analyzes every dong a company spends. "
                            "Without it, managers would be making decisions in the dark.\n\n"
                            "The most basic concept is cost itself. "
                            "In accounting, a cost is any expenditure incurred to produce goods or deliver services. "
                            "A Vietnamese garment factory, for example, has many types of costs: "
                            "the fabric it buys, the wages it pays to sewing workers, "
                            "the electricity that powers the machines, and the rent for the factory building. "
                            "Some of these costs are easy to trace to a specific product. "
                            "Others are shared across the entire operation.\n\n"
                            "Costs that can be traced directly to a product are called direct costs. "
                            "In the garment factory, the fabric used to make a shirt is a direct cost — "
                            "you can measure exactly how many meters of fabric go into each shirt "
                            "and calculate the cost precisely. "
                            "The wages of the worker who sews that shirt are also a direct cost. "
                            "Direct costs are straightforward to track "
                            "because they have a clear, measurable link to the product.\n\n"
                            "But not all costs are so easy to assign. "
                            "The factory's electricity bill, the salary of the quality control manager, "
                            "and the cost of maintaining the sewing machines — "
                            "these are overhead costs. "
                            "Overhead refers to expenses that support the production process "
                            "but cannot be traced to a single product. "
                            "A factory might produce ten different styles of clothing, "
                            "and the electricity powers all of them equally.\n\n"
                            "This is where allocation becomes important. "
                            "Allocation is the process of distributing overhead costs "
                            "across different products or departments. "
                            "The accountant must choose a fair basis for allocation. "
                            "For example, if Product A uses sixty percent of the machine hours "
                            "and Product B uses forty percent, "
                            "the factory might allocate sixty percent of the electricity cost to Product A "
                            "and forty percent to Product B. "
                            "The choice of allocation method can significantly affect "
                            "the reported cost of each product.\n\n"
                            "To keep costs under control, companies create a budget. "
                            "A budget is a financial plan that sets spending limits "
                            "for each department and each category of cost. "
                            "At the beginning of the year, the production manager might receive "
                            "a budget of eight billion dong for raw materials. "
                            "The marketing team might get three billion dong for advertising. "
                            "The budget serves as a roadmap — "
                            "it tells everyone how much they can spend and what results are expected.\n\n"
                            "At the end of each month or quarter, accountants compare "
                            "actual spending to the budget. "
                            "The difference between what was planned and what actually happened "
                            "is called a variance. "
                            "If the production department spent seven billion dong on materials "
                            "instead of the budgeted eight billion, "
                            "there is a favorable variance of one billion dong — "
                            "the department spent less than expected. "
                            "If it spent nine billion, there is an unfavorable variance — "
                            "the department exceeded its budget. "
                            "Variance analysis helps managers identify problems early "
                            "and take corrective action before costs spiral out of control."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phân loại và kiểm soát chi phí",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every business, whether it makes shoes or software, "
                            "needs to understand where its money goes. "
                            "Cost accounting is the branch of accounting that tracks, classifies, "
                            "and analyzes every dong a company spends. "
                            "Without it, managers would be making decisions in the dark.\n\n"
                            "The most basic concept is cost itself. "
                            "In accounting, a cost is any expenditure incurred to produce goods or deliver services. "
                            "A Vietnamese garment factory, for example, has many types of costs: "
                            "the fabric it buys, the wages it pays to sewing workers, "
                            "the electricity that powers the machines, and the rent for the factory building. "
                            "Some of these costs are easy to trace to a specific product. "
                            "Others are shared across the entire operation.\n\n"
                            "Costs that can be traced directly to a product are called direct costs. "
                            "In the garment factory, the fabric used to make a shirt is a direct cost — "
                            "you can measure exactly how many meters of fabric go into each shirt "
                            "and calculate the cost precisely. "
                            "The wages of the worker who sews that shirt are also a direct cost. "
                            "Direct costs are straightforward to track "
                            "because they have a clear, measurable link to the product.\n\n"
                            "But not all costs are so easy to assign. "
                            "The factory's electricity bill, the salary of the quality control manager, "
                            "and the cost of maintaining the sewing machines — "
                            "these are overhead costs. "
                            "Overhead refers to expenses that support the production process "
                            "but cannot be traced to a single product. "
                            "A factory might produce ten different styles of clothing, "
                            "and the electricity powers all of them equally.\n\n"
                            "This is where allocation becomes important. "
                            "Allocation is the process of distributing overhead costs "
                            "across different products or departments. "
                            "The accountant must choose a fair basis for allocation. "
                            "For example, if Product A uses sixty percent of the machine hours "
                            "and Product B uses forty percent, "
                            "the factory might allocate sixty percent of the electricity cost to Product A "
                            "and forty percent to Product B. "
                            "The choice of allocation method can significantly affect "
                            "the reported cost of each product.\n\n"
                            "To keep costs under control, companies create a budget. "
                            "A budget is a financial plan that sets spending limits "
                            "for each department and each category of cost. "
                            "At the beginning of the year, the production manager might receive "
                            "a budget of eight billion dong for raw materials. "
                            "The marketing team might get three billion dong for advertising. "
                            "The budget serves as a roadmap — "
                            "it tells everyone how much they can spend and what results are expected.\n\n"
                            "At the end of each month or quarter, accountants compare "
                            "actual spending to the budget. "
                            "The difference between what was planned and what actually happened "
                            "is called a variance. "
                            "If the production department spent seven billion dong on materials "
                            "instead of the budgeted eight billion, "
                            "there is a favorable variance of one billion dong — "
                            "the department spent less than expected. "
                            "If it spent nine billion, there is an unfavorable variance — "
                            "the department exceeded its budget. "
                            "Variance analysis helps managers identify problems early "
                            "and take corrective action before costs spiral out of control."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chi phí, ngân sách và phân bổ",
                    "description": "Viết câu sử dụng 6 từ vựng về phân loại và kiểm soát chi phí.",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"],
                        "items": [
                            {
                                "targetVocab": "cost",
                                "prompt": "Dùng từ 'cost' để viết một câu về tổng chi phí sản xuất của một doanh nghiệp và các yếu tố cấu thành. Ví dụ: The total cost of manufacturing one bicycle includes the metal frame, rubber tires, labor wages, and a share of the factory's electricity bill."
                            },
                            {
                                "targetVocab": "budget",
                                "prompt": "Dùng từ 'budget' để viết một câu về cách một bộ phận lập kế hoạch chi tiêu cho quý tới. Ví dụ: The production manager prepared a quarterly budget of six billion dong, allocating four billion for raw materials and two billion for temporary workers during peak season."
                            },
                            {
                                "targetVocab": "variance",
                                "prompt": "Dùng từ 'variance' để viết một câu về sự chênh lệch giữa chi phí dự kiến và chi phí thực tế. Ví dụ: The unfavorable variance of eight hundred million dong in the logistics department was caused by a sudden increase in fuel prices during the monsoon season."
                            },
                            {
                                "targetVocab": "overhead",
                                "prompt": "Dùng từ 'overhead' để viết một câu về chi phí chung của nhà máy và cách chúng ảnh hưởng đến giá thành. Ví dụ: Rising overhead costs, including factory rent and insurance premiums, forced the company to raise the selling price of its products by five percent."
                            },
                            {
                                "targetVocab": "allocation",
                                "prompt": "Dùng từ 'allocation' để viết một câu về cách phân bổ chi phí chung cho các sản phẩm khác nhau. Ví dụ: The new allocation method based on machine hours gave a more accurate picture of each product's true cost than the old method based on direct labor hours."
                            },
                            {
                                "targetVocab": "direct",
                                "prompt": "Dùng từ 'direct' để viết một câu về chi phí trực tiếp trong sản xuất và cách theo dõi chúng. Ví dụ: Direct costs such as wood and varnish accounted for sixty percent of the total production cost of each handmade table at the furniture workshop."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về phương pháp tính giá thành sản phẩm.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "cost — chi phí, budget — ngân sách, variance — chênh lệch, "
                            "overhead — chi phí chung, allocation — phân bổ, và direct — trực tiếp. "
                            "Bạn đã hiểu cách doanh nghiệp phân loại chi phí và kiểm soát ngân sách. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào các phương pháp tính giá thành sản phẩm — "
                            "cách kế toán viên quyết định mỗi sản phẩm 'gánh' bao nhiêu chi phí.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: indirect, standard, actual, absorption, marginal, và contribution. "
                            "Đây là bộ từ vựng giúp bạn hiểu các hệ thống tính giá thành khác nhau.\n\n"
                            "Từ đầu tiên là indirect — tính từ — nghĩa là gián tiếp, "
                            "mô tả chi phí không thể gắn trực tiếp với một sản phẩm cụ thể. "
                            "Ví dụ: 'Indirect costs such as factory security, cleaning services, and equipment depreciation are shared across all products manufactured in the plant.' "
                            "Trong bài đọc, indirect costs là đối lập của direct costs — "
                            "chúng cần được phân bổ vì không thể đo lường chính xác cho từng sản phẩm.\n\n"
                            "Từ thứ hai là standard — tính từ/danh từ — nghĩa là tiêu chuẩn, "
                            "mức chi phí dự kiến được thiết lập trước cho mỗi đơn vị sản phẩm. "
                            "Ví dụ: 'The standard cost for producing one pair of shoes was set at one hundred and fifty thousand dong, based on expected material prices and labor efficiency.' "
                            "Trong bài đọc, standard cost là thước đo — "
                            "nó cho phép so sánh chi phí thực tế với kỳ vọng.\n\n"
                            "Từ thứ ba là actual — tính từ — nghĩa là thực tế, "
                            "chi phí thực sự phát sinh trong quá trình sản xuất. "
                            "Ví dụ: 'The actual cost of production was higher than expected because the price of imported leather increased by twenty percent during the quarter.' "
                            "Trong bài đọc, actual cost được so sánh với standard cost "
                            "để tính variance — chênh lệch giữa kế hoạch và thực tế.\n\n"
                            "Từ thứ tư là absorption — danh từ — nghĩa là hấp thụ, "
                            "phương pháp tính giá thành trong đó mỗi sản phẩm 'hấp thụ' "
                            "cả chi phí trực tiếp lẫn một phần chi phí chung. "
                            "Ví dụ: 'Under absorption costing, each unit of output carries a share of fixed overhead, so the cost per unit changes when production volume increases or decreases.' "
                            "Trong bài đọc, absorption costing là phương pháp phổ biến nhất — "
                            "nó đảm bảo mọi chi phí đều được phản ánh trong giá thành sản phẩm.\n\n"
                            "Từ thứ năm là marginal — tính từ — nghĩa là biên, "
                            "chi phí phát sinh thêm khi sản xuất thêm một đơn vị sản phẩm. "
                            "Ví dụ: 'The marginal cost of producing one additional smartphone was only eighty thousand dong because the factory already had spare capacity and raw materials in stock.' "
                            "Trong bài đọc, marginal costing chỉ tính chi phí biến đổi vào giá thành — "
                            "chi phí cố định được xem là chi phí của kỳ, không phải của sản phẩm.\n\n"
                            "Từ cuối cùng là contribution — danh từ — nghĩa là đóng góp biên, "
                            "phần doanh thu còn lại sau khi trừ chi phí biến đổi. "
                            "Ví dụ: 'Each unit sold generates a contribution of fifty thousand dong, which goes toward covering the company's fixed costs and eventually generating profit.' "
                            "Trong bài đọc, contribution là chỉ số quan trọng — "
                            "nó cho biết mỗi sản phẩm đóng góp bao nhiêu vào việc bù đắp chi phí cố định.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về các phương pháp tính giá thành sản phẩm nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {"vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {"vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {"vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {"vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {"vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phương pháp tính giá thành sản phẩm",
                    "description": "Once a company has classified its costs into direct and indirect categories, the next question is how to calculate the total cost of each product.",
                    "data": {
                        "text": (
                            "Once a company has classified its costs into direct and indirect categories, "
                            "the next question is how to calculate the total cost of each product. "
                            "This is where costing methods come in — "
                            "and the method a company chooses can change the numbers dramatically.\n\n"
                            "The most widely used approach is absorption costing. "
                            "Under this method, every product absorbs a share of all production costs — "
                            "both direct costs like materials and labor, "
                            "and indirect costs like factory rent and equipment maintenance. "
                            "If a Vietnamese ceramics factory produces ten thousand vases in a month "
                            "and the total overhead is two billion dong, "
                            "each vase absorbs two hundred thousand dong of overhead "
                            "on top of its direct material and labor costs. "
                            "Absorption costing gives a complete picture of what each product truly costs to make.\n\n"
                            "However, absorption costing has a limitation. "
                            "Because fixed overhead is spread across all units produced, "
                            "the cost per unit changes when production volume changes. "
                            "If the factory makes twenty thousand vases instead of ten thousand, "
                            "each vase absorbs only one hundred thousand dong of overhead — "
                            "making it appear cheaper to produce, even though total overhead has not changed.\n\n"
                            "An alternative approach is marginal costing. "
                            "Under marginal costing, only variable costs are included in the product cost. "
                            "Fixed overhead is treated as a period expense — "
                            "a cost of running the business for that time period, "
                            "not a cost of making any specific product. "
                            "The marginal cost of producing one additional vase "
                            "includes only the clay, glaze, and the labor to shape and fire it. "
                            "This approach is useful for short-term decisions "
                            "like whether to accept a special order at a lower price.\n\n"
                            "A key concept in marginal costing is contribution. "
                            "Contribution is the amount left over after subtracting variable costs from revenue. "
                            "If a vase sells for five hundred thousand dong "
                            "and its variable costs are three hundred thousand dong, "
                            "the contribution is two hundred thousand dong per unit. "
                            "This contribution goes toward covering the factory's fixed costs. "
                            "Once enough units are sold to cover all fixed costs, "
                            "every additional contribution becomes pure profit.\n\n"
                            "To set realistic targets, companies establish standard costs. "
                            "A standard cost is a predetermined estimate of what a product should cost "
                            "under normal operating conditions. "
                            "The standard might specify that each vase should use "
                            "two kilograms of clay at fifty thousand dong per kilogram "
                            "and require thirty minutes of labor at one hundred thousand dong per hour. "
                            "The total standard cost would then be one hundred and fifty thousand dong.\n\n"
                            "At the end of the period, accountants compare the standard cost "
                            "to the actual cost — what the company really spent. "
                            "If the actual cost of clay was higher because prices rose, "
                            "or if workers took longer than expected, "
                            "the actual cost will exceed the standard. "
                            "The difference is a variance, and managers investigate "
                            "whether it was caused by price changes, efficiency problems, "
                            "or changes in production volume.\n\n"
                            "Understanding the difference between indirect and direct costs, "
                            "between absorption and marginal approaches, "
                            "and between standard and actual figures "
                            "is essential for anyone who wants to manage costs effectively. "
                            "These concepts form the foundation of cost accounting "
                            "and appear in every management report around the world."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phương pháp tính giá thành sản phẩm",
                    "description": "Once a company has classified its costs into direct and indirect categories, the next question is how to calculate the total cost of each product.",
                    "data": {
                        "text": (
                            "Once a company has classified its costs into direct and indirect categories, "
                            "the next question is how to calculate the total cost of each product. "
                            "This is where costing methods come in — "
                            "and the method a company chooses can change the numbers dramatically.\n\n"
                            "The most widely used approach is absorption costing. "
                            "Under this method, every product absorbs a share of all production costs — "
                            "both direct costs like materials and labor, "
                            "and indirect costs like factory rent and equipment maintenance. "
                            "If a Vietnamese ceramics factory produces ten thousand vases in a month "
                            "and the total overhead is two billion dong, "
                            "each vase absorbs two hundred thousand dong of overhead "
                            "on top of its direct material and labor costs. "
                            "Absorption costing gives a complete picture of what each product truly costs to make.\n\n"
                            "However, absorption costing has a limitation. "
                            "Because fixed overhead is spread across all units produced, "
                            "the cost per unit changes when production volume changes. "
                            "If the factory makes twenty thousand vases instead of ten thousand, "
                            "each vase absorbs only one hundred thousand dong of overhead — "
                            "making it appear cheaper to produce, even though total overhead has not changed.\n\n"
                            "An alternative approach is marginal costing. "
                            "Under marginal costing, only variable costs are included in the product cost. "
                            "Fixed overhead is treated as a period expense — "
                            "a cost of running the business for that time period, "
                            "not a cost of making any specific product. "
                            "The marginal cost of producing one additional vase "
                            "includes only the clay, glaze, and the labor to shape and fire it. "
                            "This approach is useful for short-term decisions "
                            "like whether to accept a special order at a lower price.\n\n"
                            "A key concept in marginal costing is contribution. "
                            "Contribution is the amount left over after subtracting variable costs from revenue. "
                            "If a vase sells for five hundred thousand dong "
                            "and its variable costs are three hundred thousand dong, "
                            "the contribution is two hundred thousand dong per unit. "
                            "This contribution goes toward covering the factory's fixed costs. "
                            "Once enough units are sold to cover all fixed costs, "
                            "every additional contribution becomes pure profit.\n\n"
                            "To set realistic targets, companies establish standard costs. "
                            "A standard cost is a predetermined estimate of what a product should cost "
                            "under normal operating conditions. "
                            "The standard might specify that each vase should use "
                            "two kilograms of clay at fifty thousand dong per kilogram "
                            "and require thirty minutes of labor at one hundred thousand dong per hour. "
                            "The total standard cost would then be one hundred and fifty thousand dong.\n\n"
                            "At the end of the period, accountants compare the standard cost "
                            "to the actual cost — what the company really spent. "
                            "If the actual cost of clay was higher because prices rose, "
                            "or if workers took longer than expected, "
                            "the actual cost will exceed the standard. "
                            "The difference is a variance, and managers investigate "
                            "whether it was caused by price changes, efficiency problems, "
                            "or changes in production volume.\n\n"
                            "Understanding the difference between indirect and direct costs, "
                            "between absorption and marginal approaches, "
                            "and between standard and actual figures "
                            "is essential for anyone who wants to manage costs effectively. "
                            "These concepts form the foundation of cost accounting "
                            "and appear in every management report around the world."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phương pháp tính giá thành sản phẩm",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Once a company has classified its costs into direct and indirect categories, "
                            "the next question is how to calculate the total cost of each product. "
                            "This is where costing methods come in — "
                            "and the method a company chooses can change the numbers dramatically.\n\n"
                            "The most widely used approach is absorption costing. "
                            "Under this method, every product absorbs a share of all production costs — "
                            "both direct costs like materials and labor, "
                            "and indirect costs like factory rent and equipment maintenance. "
                            "If a Vietnamese ceramics factory produces ten thousand vases in a month "
                            "and the total overhead is two billion dong, "
                            "each vase absorbs two hundred thousand dong of overhead "
                            "on top of its direct material and labor costs. "
                            "Absorption costing gives a complete picture of what each product truly costs to make.\n\n"
                            "However, absorption costing has a limitation. "
                            "Because fixed overhead is spread across all units produced, "
                            "the cost per unit changes when production volume changes. "
                            "If the factory makes twenty thousand vases instead of ten thousand, "
                            "each vase absorbs only one hundred thousand dong of overhead — "
                            "making it appear cheaper to produce, even though total overhead has not changed.\n\n"
                            "An alternative approach is marginal costing. "
                            "Under marginal costing, only variable costs are included in the product cost. "
                            "Fixed overhead is treated as a period expense — "
                            "a cost of running the business for that time period, "
                            "not a cost of making any specific product. "
                            "The marginal cost of producing one additional vase "
                            "includes only the clay, glaze, and the labor to shape and fire it. "
                            "This approach is useful for short-term decisions "
                            "like whether to accept a special order at a lower price.\n\n"
                            "A key concept in marginal costing is contribution. "
                            "Contribution is the amount left over after subtracting variable costs from revenue. "
                            "If a vase sells for five hundred thousand dong "
                            "and its variable costs are three hundred thousand dong, "
                            "the contribution is two hundred thousand dong per unit. "
                            "This contribution goes toward covering the factory's fixed costs. "
                            "Once enough units are sold to cover all fixed costs, "
                            "every additional contribution becomes pure profit.\n\n"
                            "To set realistic targets, companies establish standard costs. "
                            "A standard cost is a predetermined estimate of what a product should cost "
                            "under normal operating conditions. "
                            "The standard might specify that each vase should use "
                            "two kilograms of clay at fifty thousand dong per kilogram "
                            "and require thirty minutes of labor at one hundred thousand dong per hour. "
                            "The total standard cost would then be one hundred and fifty thousand dong.\n\n"
                            "At the end of the period, accountants compare the standard cost "
                            "to the actual cost — what the company really spent. "
                            "If the actual cost of clay was higher because prices rose, "
                            "or if workers took longer than expected, "
                            "the actual cost will exceed the standard. "
                            "The difference is a variance, and managers investigate "
                            "whether it was caused by price changes, efficiency problems, "
                            "or changes in production volume.\n\n"
                            "Understanding the difference between indirect and direct costs, "
                            "between absorption and marginal approaches, "
                            "and between standard and actual figures "
                            "is essential for anyone who wants to manage costs effectively. "
                            "These concepts form the foundation of cost accounting "
                            "and appear in every management report around the world."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phương pháp tính giá thành",
                    "description": "Viết câu sử dụng 6 từ vựng về phương pháp tính giá thành sản phẩm.",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"],
                        "items": [
                            {
                                "targetVocab": "indirect",
                                "prompt": "Dùng từ 'indirect' để viết một câu về chi phí gián tiếp trong nhà máy và cách chúng được xử lý. Ví dụ: Indirect costs such as factory insurance and the plant manager's salary were distributed equally among the three product lines manufactured at the facility."
                            },
                            {
                                "targetVocab": "standard",
                                "prompt": "Dùng từ 'standard' để viết một câu về chi phí tiêu chuẩn và vai trò của nó trong kiểm soát chi phí. Ví dụ: The company set a standard cost of two hundred thousand dong per unit, which served as the target for the production team to measure their efficiency against."
                            },
                            {
                                "targetVocab": "actual",
                                "prompt": "Dùng từ 'actual' để viết một câu về chi phí thực tế và sự khác biệt với chi phí dự kiến. Ví dụ: The actual cost of producing the batch was fifteen percent higher than planned because a key supplier raised prices without warning in the middle of the quarter."
                            },
                            {
                                "targetVocab": "absorption",
                                "prompt": "Dùng từ 'absorption' để viết một câu về phương pháp tính giá thành hấp thụ toàn bộ. Ví dụ: Under absorption costing, the factory allocated its entire monthly overhead of three billion dong across all units produced, increasing the reported cost per unit significantly."
                            },
                            {
                                "targetVocab": "marginal",
                                "prompt": "Dùng từ 'marginal' để viết một câu về chi phí biên và ứng dụng trong quyết định kinh doanh. Ví dụ: The marginal cost of adding one more passenger to the tour bus was almost zero, so the travel company offered last-minute discounts to fill empty seats."
                            },
                            {
                                "targetVocab": "contribution",
                                "prompt": "Dùng từ 'contribution' để viết một câu về đóng góp biên của sản phẩm vào việc bù đắp chi phí cố định. Ví dụ: Each cup of coffee sold at the campus cafe generates a contribution of thirty thousand dong, which helps cover the monthly rent and staff salaries."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về phân tích hòa vốn và đánh giá hiệu quả.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: cost, budget, variance, overhead, allocation, direct — "
                            "những khái niệm cốt lõi về phân loại và kiểm soát chi phí. "
                            "Trong phần 2, bạn đã học thêm indirect, standard, actual, absorption, marginal, contribution — "
                            "bộ từ vựng về các phương pháp tính giá thành sản phẩm.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh thực tiễn hơn: "
                            "phân tích hòa vốn, dự báo chi phí, và đánh giá hiệu quả hoạt động. "
                            "Bạn sẽ học 6 từ mới: breakeven, forecast, performance, benchmark, controllable, và uncontrollable.\n\n"
                            "Từ đầu tiên là breakeven — danh từ/tính từ — nghĩa là hòa vốn, "
                            "điểm mà tại đó tổng doanh thu bằng tổng chi phí — doanh nghiệp không lãi cũng không lỗ. "
                            "Ví dụ: 'The new restaurant needs to sell at least three hundred meals per day to reach its breakeven point and start generating profit.' "
                            "Trong bài đọc, breakeven là mục tiêu tối thiểu — "
                            "nếu doanh nghiệp chưa đạt breakeven, mỗi ngày hoạt động là một ngày lỗ.\n\n"
                            "Từ thứ hai là forecast — danh từ/động từ — nghĩa là dự báo, "
                            "ước tính về chi phí, doanh thu hoặc nhu cầu trong tương lai. "
                            "Ví dụ: 'The finance team prepared a cost forecast for the next fiscal year, predicting a ten percent increase in raw material prices due to global supply chain disruptions.' "
                            "Trong bài đọc, forecast là công cụ lập kế hoạch — "
                            "nó giúp doanh nghiệp chuẩn bị ngân sách và đưa ra quyết định trước khi chi phí thực tế phát sinh.\n\n"
                            "Từ thứ ba là performance — danh từ — nghĩa là hiệu quả hoạt động, "
                            "mức độ mà một bộ phận hoặc doanh nghiệp đạt được so với mục tiêu đề ra. "
                            "Ví dụ: 'The production department's performance exceeded expectations this quarter, with output increasing by twelve percent while costs remained within budget.' "
                            "Trong bài đọc, performance được đo lường bằng nhiều chỉ số — "
                            "từ chi phí trên mỗi đơn vị đến tỷ lệ sản phẩm lỗi.\n\n"
                            "Từ thứ tư là benchmark — danh từ/động từ — nghĩa là chuẩn đối sánh, "
                            "tiêu chuẩn hoặc điểm tham chiếu dùng để so sánh hiệu quả. "
                            "Ví dụ: 'The company uses industry benchmarks to evaluate whether its production costs are competitive compared to other manufacturers in the region.' "
                            "Trong bài đọc, benchmark giúp doanh nghiệp biết mình đang ở đâu — "
                            "tốt hơn hay kém hơn so với đối thủ và tiêu chuẩn ngành.\n\n"
                            "Từ thứ năm là controllable — tính từ — nghĩa là có thể kiểm soát, "
                            "mô tả chi phí mà nhà quản lý có quyền và khả năng tác động. "
                            "Ví dụ: 'The factory manager focused on reducing controllable costs such as overtime wages and material waste, which were within her authority to change.' "
                            "Trong bài đọc, controllable costs là trọng tâm đánh giá — "
                            "nhà quản lý chỉ nên chịu trách nhiệm về những chi phí mà họ có thể kiểm soát.\n\n"
                            "Từ cuối cùng là uncontrollable — tính từ — nghĩa là không thể kiểm soát, "
                            "mô tả chi phí nằm ngoài tầm ảnh hưởng của nhà quản lý cấp bộ phận. "
                            "Ví dụ: 'The increase in electricity tariffs was an uncontrollable cost for the plant manager, as it was determined by the national energy regulator.' "
                            "Trong bài đọc, uncontrollable costs vẫn ảnh hưởng đến kết quả — "
                            "nhưng chúng không nên được dùng để đánh giá hiệu quả của nhà quản lý.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về phân tích hòa vốn và đánh giá hiệu quả nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phân tích hòa vốn và đánh giá hiệu quả chi phí",
                    "description": "Every manager wants to know one thing: how many units do we need to sell before we start making money?",
                    "data": {
                        "text": (
                            "Every manager wants to know one thing: "
                            "how many units do we need to sell before we start making money? "
                            "The answer comes from breakeven analysis — "
                            "one of the most practical tools in cost accounting.\n\n"
                            "The breakeven point is where total revenue equals total costs. "
                            "Below this point, the company loses money. Above it, the company earns profit. "
                            "To calculate the breakeven point, you need to know three things: "
                            "the selling price per unit, the variable cost per unit, "
                            "and the total fixed costs for the period. "
                            "For example, a Vietnamese bakery sells each cake for one hundred thousand dong. "
                            "The variable cost — flour, eggs, sugar, and packaging — is sixty thousand dong per cake. "
                            "The contribution per cake is forty thousand dong. "
                            "If the bakery's fixed costs — rent, equipment, and salaries — total "
                            "twenty million dong per month, "
                            "the breakeven point is five hundred cakes per month. "
                            "Sell fewer than five hundred, and the bakery loses money. "
                            "Sell more, and every additional cake adds forty thousand dong of pure profit.\n\n"
                            "But breakeven analysis looks backward at current costs. "
                            "To plan for the future, companies need a forecast. "
                            "A cost forecast estimates what expenses will look like "
                            "in the coming months or years. "
                            "The finance team might forecast that raw material prices will rise "
                            "by eight percent next year based on commodity market trends. "
                            "They might also forecast that labor costs will increase "
                            "as the government raises the minimum wage. "
                            "A good forecast helps the company adjust its budget in advance "
                            "rather than reacting to surprises after they happen.\n\n"
                            "Once the budget is set and the period ends, "
                            "managers need to evaluate performance. "
                            "Performance measurement in cost accounting means comparing "
                            "what actually happened to what was planned. "
                            "Did the production department stay within its budget? "
                            "Did the sales team generate enough revenue to cover costs? "
                            "Performance reports break down results by department, product line, "
                            "and cost category so that managers can see exactly where things went well "
                            "and where they went wrong.\n\n"
                            "To make performance evaluation meaningful, "
                            "companies use benchmarks. "
                            "A benchmark is a standard of comparison — "
                            "it could be the company's own historical performance, "
                            "an industry average, or the results of a leading competitor. "
                            "If the average production cost in the Vietnamese textile industry "
                            "is eighty thousand dong per meter of fabric, "
                            "and your factory's cost is ninety thousand dong, "
                            "the benchmark tells you that there is room for improvement. "
                            "Without benchmarks, a company might think it is doing well "
                            "simply because it is better than last year — "
                            "even if competitors are doing much better.\n\n"
                            "A fair performance evaluation must also distinguish "
                            "between controllable and uncontrollable costs. "
                            "A controllable cost is one that a manager can influence through decisions. "
                            "The factory manager can control overtime hours, material usage, "
                            "and the number of temporary workers hired. "
                            "These are controllable costs, and the manager should be held accountable for them.\n\n"
                            "An uncontrollable cost, on the other hand, "
                            "is determined by forces outside the manager's authority. "
                            "The price of imported steel, changes in tax rates, "
                            "and government-mandated wage increases are all uncontrollable "
                            "from the factory manager's perspective. "
                            "It would be unfair to blame a manager for cost increases "
                            "that were caused by external factors beyond their control. "
                            "Good cost accounting systems separate controllable from uncontrollable costs "
                            "so that each manager is evaluated only on what they can actually influence."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phân tích hòa vốn và đánh giá hiệu quả chi phí",
                    "description": "Every manager wants to know one thing: how many units do we need to sell before we start making money?",
                    "data": {
                        "text": (
                            "Every manager wants to know one thing: "
                            "how many units do we need to sell before we start making money? "
                            "The answer comes from breakeven analysis — "
                            "one of the most practical tools in cost accounting.\n\n"
                            "The breakeven point is where total revenue equals total costs. "
                            "Below this point, the company loses money. Above it, the company earns profit. "
                            "To calculate the breakeven point, you need to know three things: "
                            "the selling price per unit, the variable cost per unit, "
                            "and the total fixed costs for the period. "
                            "For example, a Vietnamese bakery sells each cake for one hundred thousand dong. "
                            "The variable cost — flour, eggs, sugar, and packaging — is sixty thousand dong per cake. "
                            "The contribution per cake is forty thousand dong. "
                            "If the bakery's fixed costs — rent, equipment, and salaries — total "
                            "twenty million dong per month, "
                            "the breakeven point is five hundred cakes per month. "
                            "Sell fewer than five hundred, and the bakery loses money. "
                            "Sell more, and every additional cake adds forty thousand dong of pure profit.\n\n"
                            "But breakeven analysis looks backward at current costs. "
                            "To plan for the future, companies need a forecast. "
                            "A cost forecast estimates what expenses will look like "
                            "in the coming months or years. "
                            "The finance team might forecast that raw material prices will rise "
                            "by eight percent next year based on commodity market trends. "
                            "They might also forecast that labor costs will increase "
                            "as the government raises the minimum wage. "
                            "A good forecast helps the company adjust its budget in advance "
                            "rather than reacting to surprises after they happen.\n\n"
                            "Once the budget is set and the period ends, "
                            "managers need to evaluate performance. "
                            "Performance measurement in cost accounting means comparing "
                            "what actually happened to what was planned. "
                            "Did the production department stay within its budget? "
                            "Did the sales team generate enough revenue to cover costs? "
                            "Performance reports break down results by department, product line, "
                            "and cost category so that managers can see exactly where things went well "
                            "and where they went wrong.\n\n"
                            "To make performance evaluation meaningful, "
                            "companies use benchmarks. "
                            "A benchmark is a standard of comparison — "
                            "it could be the company's own historical performance, "
                            "an industry average, or the results of a leading competitor. "
                            "If the average production cost in the Vietnamese textile industry "
                            "is eighty thousand dong per meter of fabric, "
                            "and your factory's cost is ninety thousand dong, "
                            "the benchmark tells you that there is room for improvement. "
                            "Without benchmarks, a company might think it is doing well "
                            "simply because it is better than last year — "
                            "even if competitors are doing much better.\n\n"
                            "A fair performance evaluation must also distinguish "
                            "between controllable and uncontrollable costs. "
                            "A controllable cost is one that a manager can influence through decisions. "
                            "The factory manager can control overtime hours, material usage, "
                            "and the number of temporary workers hired. "
                            "These are controllable costs, and the manager should be held accountable for them.\n\n"
                            "An uncontrollable cost, on the other hand, "
                            "is determined by forces outside the manager's authority. "
                            "The price of imported steel, changes in tax rates, "
                            "and government-mandated wage increases are all uncontrollable "
                            "from the factory manager's perspective. "
                            "It would be unfair to blame a manager for cost increases "
                            "that were caused by external factors beyond their control. "
                            "Good cost accounting systems separate controllable from uncontrollable costs "
                            "so that each manager is evaluated only on what they can actually influence."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phân tích hòa vốn và đánh giá hiệu quả chi phí",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every manager wants to know one thing: "
                            "how many units do we need to sell before we start making money? "
                            "The answer comes from breakeven analysis — "
                            "one of the most practical tools in cost accounting.\n\n"
                            "The breakeven point is where total revenue equals total costs. "
                            "Below this point, the company loses money. Above it, the company earns profit. "
                            "To calculate the breakeven point, you need to know three things: "
                            "the selling price per unit, the variable cost per unit, "
                            "and the total fixed costs for the period. "
                            "For example, a Vietnamese bakery sells each cake for one hundred thousand dong. "
                            "The variable cost — flour, eggs, sugar, and packaging — is sixty thousand dong per cake. "
                            "The contribution per cake is forty thousand dong. "
                            "If the bakery's fixed costs — rent, equipment, and salaries — total "
                            "twenty million dong per month, "
                            "the breakeven point is five hundred cakes per month. "
                            "Sell fewer than five hundred, and the bakery loses money. "
                            "Sell more, and every additional cake adds forty thousand dong of pure profit.\n\n"
                            "But breakeven analysis looks backward at current costs. "
                            "To plan for the future, companies need a forecast. "
                            "A cost forecast estimates what expenses will look like "
                            "in the coming months or years. "
                            "The finance team might forecast that raw material prices will rise "
                            "by eight percent next year based on commodity market trends. "
                            "They might also forecast that labor costs will increase "
                            "as the government raises the minimum wage. "
                            "A good forecast helps the company adjust its budget in advance "
                            "rather than reacting to surprises after they happen.\n\n"
                            "Once the budget is set and the period ends, "
                            "managers need to evaluate performance. "
                            "Performance measurement in cost accounting means comparing "
                            "what actually happened to what was planned. "
                            "Did the production department stay within its budget? "
                            "Did the sales team generate enough revenue to cover costs? "
                            "Performance reports break down results by department, product line, "
                            "and cost category so that managers can see exactly where things went well "
                            "and where they went wrong.\n\n"
                            "To make performance evaluation meaningful, "
                            "companies use benchmarks. "
                            "A benchmark is a standard of comparison — "
                            "it could be the company's own historical performance, "
                            "an industry average, or the results of a leading competitor. "
                            "If the average production cost in the Vietnamese textile industry "
                            "is eighty thousand dong per meter of fabric, "
                            "and your factory's cost is ninety thousand dong, "
                            "the benchmark tells you that there is room for improvement. "
                            "Without benchmarks, a company might think it is doing well "
                            "simply because it is better than last year — "
                            "even if competitors are doing much better.\n\n"
                            "A fair performance evaluation must also distinguish "
                            "between controllable and uncontrollable costs. "
                            "A controllable cost is one that a manager can influence through decisions. "
                            "The factory manager can control overtime hours, material usage, "
                            "and the number of temporary workers hired. "
                            "These are controllable costs, and the manager should be held accountable for them.\n\n"
                            "An uncontrollable cost, on the other hand, "
                            "is determined by forces outside the manager's authority. "
                            "The price of imported steel, changes in tax rates, "
                            "and government-mandated wage increases are all uncontrollable "
                            "from the factory manager's perspective. "
                            "It would be unfair to blame a manager for cost increases "
                            "that were caused by external factors beyond their control. "
                            "Good cost accounting systems separate controllable from uncontrollable costs "
                            "so that each manager is evaluated only on what they can actually influence."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Hòa vốn và đánh giá hiệu quả",
                    "description": "Viết câu sử dụng 6 từ vựng về phân tích hòa vốn và đánh giá hiệu quả.",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"],
                        "items": [
                            {
                                "targetVocab": "breakeven",
                                "prompt": "Dùng từ 'breakeven' để viết một câu về điểm hòa vốn của một doanh nghiệp mới. Ví dụ: The startup calculated that it needed to sell at least two thousand subscriptions per month to reach its breakeven point and stop burning through investor capital."
                            },
                            {
                                "targetVocab": "forecast",
                                "prompt": "Dùng từ 'forecast' để viết một câu về dự báo chi phí cho năm tài chính tiếp theo. Ví dụ: The finance department's forecast predicted that energy costs would rise by twelve percent next year, prompting the company to invest in solar panels for the factory roof."
                            },
                            {
                                "targetVocab": "performance",
                                "prompt": "Dùng từ 'performance' để viết một câu về đánh giá hiệu quả hoạt động của một bộ phận. Ví dụ: The quarterly performance report showed that the logistics department reduced delivery costs by eighteen percent while maintaining the same level of customer satisfaction."
                            },
                            {
                                "targetVocab": "benchmark",
                                "prompt": "Dùng từ 'benchmark' để viết một câu về việc so sánh hiệu quả với tiêu chuẩn ngành. Ví dụ: The company benchmarked its production costs against five leading competitors in Southeast Asia and discovered that its labor efficiency was twenty percent below the regional average."
                            },
                            {
                                "targetVocab": "controllable",
                                "prompt": "Dùng từ 'controllable' để viết một câu về chi phí mà nhà quản lý có thể tác động. Ví dụ: The plant manager reduced controllable costs by renegotiating contracts with local suppliers and implementing a strict policy on overtime hours for production workers."
                            },
                            {
                                "targetVocab": "uncontrollable",
                                "prompt": "Dùng từ 'uncontrollable' để viết một câu về chi phí nằm ngoài tầm kiểm soát của nhà quản lý. Ví dụ: The sharp increase in import duties was an uncontrollable cost that affected every manufacturer in the industry, regardless of how efficiently they managed their internal operations."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Kế toán chi phí. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "cost — chi phí, budget — ngân sách, variance — chênh lệch, "
                            "overhead — chi phí chung, allocation — phân bổ, và direct — trực tiếp. "
                            "Đây là bộ từ vựng cốt lõi về phân loại và kiểm soát chi phí.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào các phương pháp tính giá thành: "
                            "indirect — gián tiếp, standard — tiêu chuẩn, actual — thực tế, "
                            "absorption — hấp thụ, marginal — biên, và contribution — đóng góp biên. "
                            "Những từ này giúp bạn hiểu cách doanh nghiệp tính chi phí cho từng sản phẩm.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "breakeven — hòa vốn, forecast — dự báo, performance — hiệu quả, "
                            "benchmark — chuẩn đối sánh, controllable — có thể kiểm soát, "
                            "và uncontrollable — không thể kiểm soát. "
                            "Đây là những từ về phân tích hòa vốn và đánh giá hiệu quả chi phí.\n\n"
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
                    "description": "Học 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng kế toán chi phí",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "cost",
                                "prompt": "Dùng từ 'cost' để viết một câu về cách doanh nghiệp phân tích cấu trúc chi phí để tìm cơ hội tiết kiệm. Ví dụ: A detailed cost analysis revealed that packaging materials accounted for fifteen percent of the total production cost, prompting the company to switch to a cheaper but equally durable supplier."
                            },
                            {
                                "targetVocab": "budget",
                                "prompt": "Dùng từ 'budget' để viết một câu về quy trình lập ngân sách hàng năm của doanh nghiệp. Ví dụ: The annual budget meeting lasted three days as each department head presented their spending plans and negotiated for additional resources to meet next year's growth targets."
                            },
                            {
                                "targetVocab": "variance",
                                "prompt": "Dùng từ 'variance' để viết một câu về cách nhà quản lý phản ứng khi phát hiện chênh lệch chi phí. Ví dụ: When the monthly report showed an unfavorable variance of one billion dong in the raw materials category, the procurement team immediately investigated whether suppliers had raised prices without notice."
                            },
                            {
                                "targetVocab": "overhead",
                                "prompt": "Dùng từ 'overhead' để viết một câu về tác động của chi phí chung đến khả năng cạnh tranh. Ví dụ: The company relocated its factory from central Ho Chi Minh City to an industrial zone in Long An province to reduce overhead costs, saving two billion dong per year in rent alone."
                            },
                            {
                                "targetVocab": "allocation",
                                "prompt": "Dùng từ 'allocation' để viết một câu về tranh luận nội bộ về phương pháp phân bổ chi phí. Ví dụ: The two product managers disagreed about the allocation of shared marketing expenses, with each arguing that the other's product line should bear a larger share of the cost."
                            },
                            {
                                "targetVocab": "direct",
                                "prompt": "Dùng từ 'direct' để viết một câu về tỷ trọng chi phí trực tiếp trong tổng giá thành sản phẩm. Ví dụ: In the electronics assembly plant, direct costs including imported components and assembly labor represented over seventy percent of the total cost per unit."
                            },
                            {
                                "targetVocab": "indirect",
                                "prompt": "Dùng từ 'indirect' để viết một câu về thách thức trong việc theo dõi chi phí gián tiếp. Ví dụ: Tracking indirect costs proved challenging because the shared warehouse served four different product divisions, making it difficult to determine how much space each division actually used."
                            },
                            {
                                "targetVocab": "standard",
                                "prompt": "Dùng từ 'standard' để viết một câu về cách thiết lập chi phí tiêu chuẩn cho sản phẩm mới. Ví dụ: The engineering team worked with the accounting department to establish a standard cost for the new product, estimating material usage, labor time, and machine hours based on prototype testing."
                            },
                            {
                                "targetVocab": "actual",
                                "prompt": "Dùng từ 'actual' để viết một câu về sự khác biệt giữa chi phí thực tế và dự kiến trong dự án. Ví dụ: The actual cost of the construction project exceeded the original estimate by thirty percent because of unexpected soil conditions that required additional foundation work."
                            },
                            {
                                "targetVocab": "absorption",
                                "prompt": "Dùng từ 'absorption' để viết một câu về ảnh hưởng của sản lượng đến giá thành theo phương pháp hấp thụ. Ví dụ: Under absorption costing, the cost per unit dropped significantly when the factory increased production from five thousand to eight thousand units because fixed overhead was spread across more products."
                            },
                            {
                                "targetVocab": "marginal",
                                "prompt": "Dùng từ 'marginal' để viết một câu về quyết định nhận đơn hàng đặc biệt dựa trên chi phí biên. Ví dụ: The export manager accepted the special order at a lower price because the marginal cost of producing the extra units was well below the offered price, generating additional contribution."
                            },
                            {
                                "targetVocab": "contribution",
                                "prompt": "Dùng từ 'contribution' để viết một câu về cách sử dụng đóng góp biên để đánh giá sản phẩm. Ví dụ: Although Product B had lower revenue than Product A, its contribution margin was higher because it used cheaper materials and required less labor per unit."
                            },
                            {
                                "targetVocab": "breakeven",
                                "prompt": "Dùng từ 'breakeven' để viết một câu về cách thay đổi giá bán ảnh hưởng đến điểm hòa vốn. Ví dụ: Raising the selling price by ten percent lowered the breakeven point from eight hundred to six hundred units per month, giving the company a larger margin of safety."
                            },
                            {
                                "targetVocab": "forecast",
                                "prompt": "Dùng từ 'forecast' để viết một câu về tầm quan trọng của dự báo chính xác trong lập ngân sách. Ví dụ: The inaccurate sales forecast led to overproduction and excess inventory, costing the company three billion dong in storage fees and product markdowns."
                            },
                            {
                                "targetVocab": "performance",
                                "prompt": "Dùng từ 'performance' để viết một câu về hệ thống đánh giá hiệu quả theo bộ phận. Ví dụ: The new performance evaluation system linked each department manager's bonus to their ability to control costs within budget while maintaining product quality standards."
                            },
                            {
                                "targetVocab": "benchmark",
                                "prompt": "Dùng từ 'benchmark' để viết một câu về việc sử dụng chuẩn đối sánh quốc tế. Ví dụ: After benchmarking against Japanese manufacturers, the Vietnamese auto parts company realized its defect rate was three times higher than the industry standard and launched a quality improvement program."
                            },
                            {
                                "targetVocab": "controllable",
                                "prompt": "Dùng từ 'controllable' để viết một câu về trách nhiệm của nhà quản lý đối với chi phí kiểm soát được. Ví dụ: The performance review focused exclusively on controllable costs, recognizing that the department head had no influence over the corporate-level decisions that increased insurance premiums."
                            },
                            {
                                "targetVocab": "uncontrollable",
                                "prompt": "Dùng từ 'uncontrollable' để viết một câu về cách doanh nghiệp ứng phó với chi phí không kiểm soát được. Ví dụ: To mitigate the impact of uncontrollable costs like fluctuating exchange rates, the company signed forward contracts to lock in the price of imported raw materials for six months."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về kế toán chi phí.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về kế toán chi phí — từ phân loại chi phí, "
                            "phương pháp tính giá thành, đến phân tích hòa vốn và đánh giá hiệu quả.\n\n"
                            "Bạn sẽ gặp lại cost, budget, variance, overhead, allocation, direct "
                            "trong phần mở đầu về cách doanh nghiệp theo dõi và kiểm soát chi phí. "
                            "Tiếp theo, indirect, standard, actual, absorption, marginal, contribution "
                            "sẽ giúp bạn hiểu cách tính giá thành sản phẩm bằng các phương pháp khác nhau. "
                            "Và cuối cùng, breakeven, forecast, performance, benchmark, controllable, uncontrollable "
                            "sẽ đưa bạn vào thế giới phân tích và đánh giá hiệu quả chi phí.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Kế toán chi phí — Từ phân loại đến quyết định",
                    "description": "A medium-sized Vietnamese furniture company has just won a contract to supply office desks to a multinational corporation.",
                    "data": {
                        "text": (
                            "A medium-sized Vietnamese furniture company has just won a contract "
                            "to supply office desks to a multinational corporation. "
                            "The order is large — five thousand desks over six months — "
                            "and the management team needs to make sure the deal is profitable. "
                            "To do that, they turn to cost accounting.\n\n"
                            "The first step is to identify all the costs involved in producing the desks. "
                            "The cost accountant separates them into two categories. "
                            "Direct costs are those that can be traced to each desk: "
                            "the wood, the metal legs, the screws, and the wages of the carpenters "
                            "who cut, assemble, and sand each piece. "
                            "These costs are straightforward — "
                            "the company knows exactly how much material and labor goes into one desk.\n\n"
                            "Then there are indirect costs — expenses that support production "
                            "but cannot be linked to a single desk. "
                            "The factory's electricity bill, the salary of the quality inspector, "
                            "the cost of maintaining the cutting machines, "
                            "and the rent for the warehouse where finished desks are stored — "
                            "all of these are overhead. "
                            "The challenge is figuring out how much overhead each desk should carry.\n\n"
                            "This is where allocation comes in. "
                            "The accountant decides to allocate overhead based on machine hours. "
                            "If the total monthly overhead is one billion dong "
                            "and the factory runs its machines for ten thousand hours, "
                            "the allocation rate is one hundred thousand dong per machine hour. "
                            "Each desk takes two machine hours to produce, "
                            "so each desk is allocated two hundred thousand dong of overhead.\n\n"
                            "Using absorption costing, the accountant calculates the full cost per desk. "
                            "Direct materials cost three hundred thousand dong. "
                            "Direct labor costs one hundred and fifty thousand dong. "
                            "Allocated overhead adds two hundred thousand dong. "
                            "The total absorption cost is six hundred and fifty thousand dong per desk. "
                            "This method ensures that every cost — both direct and indirect — "
                            "is reflected in the product's price.\n\n"
                            "But the sales manager wants a different perspective. "
                            "She asks: what is the marginal cost of producing one more desk? "
                            "Under marginal costing, only variable costs count. "
                            "The wood, metal, screws, and carpenter wages total four hundred and fifty thousand dong. "
                            "Fixed overhead is excluded because it does not change "
                            "whether the factory makes one more desk or one fewer. "
                            "The contribution per desk — selling price minus variable cost — "
                            "is three hundred and fifty thousand dong if the desk sells for eight hundred thousand. "
                            "This contribution goes toward covering fixed costs and generating profit.\n\n"
                            "Before signing the contract, the finance director runs a breakeven analysis. "
                            "The company's total fixed costs for the six-month period are three billion dong. "
                            "With a contribution of three hundred and fifty thousand dong per desk, "
                            "the breakeven point is approximately eight thousand five hundred and seventy-one desks. "
                            "Since the contract is for only five thousand desks, "
                            "the company needs additional orders to reach breakeven. "
                            "The director checks the sales forecast, "
                            "which predicts total demand of twelve thousand desks across all customers. "
                            "If the forecast is accurate, the company will comfortably pass breakeven "
                            "and earn a healthy profit.\n\n"
                            "To prepare for the project, the accounting team sets standard costs. "
                            "The standard cost for wood is based on current supplier prices "
                            "plus a small buffer for price fluctuations. "
                            "The standard labor time is ninety minutes per desk, "
                            "based on time studies conducted on the factory floor. "
                            "These standards become the budget targets for the production team.\n\n"
                            "Three months into the contract, the accountant compares "
                            "actual costs to the standards. "
                            "The actual cost of wood has risen by eight percent "
                            "because a typhoon damaged timber plantations in the central region. "
                            "This creates an unfavorable material price variance. "
                            "However, the carpenters have become more efficient with practice, "
                            "completing each desk in eighty minutes instead of ninety. "
                            "This creates a favorable labor efficiency variance. "
                            "The net effect is a small overall variance — "
                            "the savings in labor nearly offset the increase in material costs.\n\n"
                            "The management team reviews the performance report. "
                            "The production department's performance is strong — "
                            "output is on schedule, quality defects are below two percent, "
                            "and controllable costs are within budget. "
                            "The factory manager has done an excellent job managing overtime, "
                            "reducing material waste, and negotiating with local suppliers. "
                            "These are all controllable costs that she can directly influence.\n\n"
                            "The increase in wood prices, however, is an uncontrollable cost. "
                            "The factory manager had no way to prevent the typhoon "
                            "or the resulting spike in timber prices. "
                            "The performance evaluation system recognizes this distinction — "
                            "the manager is praised for her controllable cost management "
                            "and not penalized for the uncontrollable price increase.\n\n"
                            "Finally, the finance director compares the company's cost structure "
                            "to industry benchmarks. "
                            "The benchmark data shows that the average furniture manufacturer in Vietnam "
                            "spends thirty-five percent of revenue on direct materials "
                            "and twenty percent on overhead. "
                            "The company's numbers are close to the benchmark — "
                            "thirty-three percent on materials and twenty-two percent on overhead. "
                            "The slightly higher overhead is explained by the company's investment "
                            "in modern CNC machines, which increase overhead "
                            "but improve quality and reduce labor costs.\n\n"
                            "By the end of the six-month contract, the company has delivered "
                            "all five thousand desks on time and within budget. "
                            "The cost accounting system — from allocation to variance analysis, "
                            "from breakeven calculations to performance benchmarks — "
                            "gave managers the information they needed to make smart decisions "
                            "at every stage of the project."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Kế toán chi phí — Từ phân loại đến quyết định",
                    "description": "A medium-sized Vietnamese furniture company has just won a contract to supply office desks to a multinational corporation.",
                    "data": {
                        "text": (
                            "A medium-sized Vietnamese furniture company has just won a contract "
                            "to supply office desks to a multinational corporation. "
                            "The order is large — five thousand desks over six months — "
                            "and the management team needs to make sure the deal is profitable. "
                            "To do that, they turn to cost accounting.\n\n"
                            "The first step is to identify all the costs involved in producing the desks. "
                            "The cost accountant separates them into two categories. "
                            "Direct costs are those that can be traced to each desk: "
                            "the wood, the metal legs, the screws, and the wages of the carpenters "
                            "who cut, assemble, and sand each piece. "
                            "These costs are straightforward — "
                            "the company knows exactly how much material and labor goes into one desk.\n\n"
                            "Then there are indirect costs — expenses that support production "
                            "but cannot be linked to a single desk. "
                            "The factory's electricity bill, the salary of the quality inspector, "
                            "the cost of maintaining the cutting machines, "
                            "and the rent for the warehouse where finished desks are stored — "
                            "all of these are overhead. "
                            "The challenge is figuring out how much overhead each desk should carry.\n\n"
                            "This is where allocation comes in. "
                            "The accountant decides to allocate overhead based on machine hours. "
                            "If the total monthly overhead is one billion dong "
                            "and the factory runs its machines for ten thousand hours, "
                            "the allocation rate is one hundred thousand dong per machine hour. "
                            "Each desk takes two machine hours to produce, "
                            "so each desk is allocated two hundred thousand dong of overhead.\n\n"
                            "Using absorption costing, the accountant calculates the full cost per desk. "
                            "Direct materials cost three hundred thousand dong. "
                            "Direct labor costs one hundred and fifty thousand dong. "
                            "Allocated overhead adds two hundred thousand dong. "
                            "The total absorption cost is six hundred and fifty thousand dong per desk. "
                            "This method ensures that every cost — both direct and indirect — "
                            "is reflected in the product's price.\n\n"
                            "But the sales manager wants a different perspective. "
                            "She asks: what is the marginal cost of producing one more desk? "
                            "Under marginal costing, only variable costs count. "
                            "The wood, metal, screws, and carpenter wages total four hundred and fifty thousand dong. "
                            "Fixed overhead is excluded because it does not change "
                            "whether the factory makes one more desk or one fewer. "
                            "The contribution per desk — selling price minus variable cost — "
                            "is three hundred and fifty thousand dong if the desk sells for eight hundred thousand. "
                            "This contribution goes toward covering fixed costs and generating profit.\n\n"
                            "Before signing the contract, the finance director runs a breakeven analysis. "
                            "The company's total fixed costs for the six-month period are three billion dong. "
                            "With a contribution of three hundred and fifty thousand dong per desk, "
                            "the breakeven point is approximately eight thousand five hundred and seventy-one desks. "
                            "Since the contract is for only five thousand desks, "
                            "the company needs additional orders to reach breakeven. "
                            "The director checks the sales forecast, "
                            "which predicts total demand of twelve thousand desks across all customers. "
                            "If the forecast is accurate, the company will comfortably pass breakeven "
                            "and earn a healthy profit.\n\n"
                            "To prepare for the project, the accounting team sets standard costs. "
                            "The standard cost for wood is based on current supplier prices "
                            "plus a small buffer for price fluctuations. "
                            "The standard labor time is ninety minutes per desk, "
                            "based on time studies conducted on the factory floor. "
                            "These standards become the budget targets for the production team.\n\n"
                            "Three months into the contract, the accountant compares "
                            "actual costs to the standards. "
                            "The actual cost of wood has risen by eight percent "
                            "because a typhoon damaged timber plantations in the central region. "
                            "This creates an unfavorable material price variance. "
                            "However, the carpenters have become more efficient with practice, "
                            "completing each desk in eighty minutes instead of ninety. "
                            "This creates a favorable labor efficiency variance. "
                            "The net effect is a small overall variance — "
                            "the savings in labor nearly offset the increase in material costs.\n\n"
                            "The management team reviews the performance report. "
                            "The production department's performance is strong — "
                            "output is on schedule, quality defects are below two percent, "
                            "and controllable costs are within budget. "
                            "The factory manager has done an excellent job managing overtime, "
                            "reducing material waste, and negotiating with local suppliers. "
                            "These are all controllable costs that she can directly influence.\n\n"
                            "The increase in wood prices, however, is an uncontrollable cost. "
                            "The factory manager had no way to prevent the typhoon "
                            "or the resulting spike in timber prices. "
                            "The performance evaluation system recognizes this distinction — "
                            "the manager is praised for her controllable cost management "
                            "and not penalized for the uncontrollable price increase.\n\n"
                            "Finally, the finance director compares the company's cost structure "
                            "to industry benchmarks. "
                            "The benchmark data shows that the average furniture manufacturer in Vietnam "
                            "spends thirty-five percent of revenue on direct materials "
                            "and twenty percent on overhead. "
                            "The company's numbers are close to the benchmark — "
                            "thirty-three percent on materials and twenty-two percent on overhead. "
                            "The slightly higher overhead is explained by the company's investment "
                            "in modern CNC machines, which increase overhead "
                            "but improve quality and reduce labor costs.\n\n"
                            "By the end of the six-month contract, the company has delivered "
                            "all five thousand desks on time and within budget. "
                            "The cost accounting system — from allocation to variance analysis, "
                            "from breakeven calculations to performance benchmarks — "
                            "gave managers the information they needed to make smart decisions "
                            "at every stage of the project."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Kế toán chi phí — Từ phân loại đến quyết định",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "A medium-sized Vietnamese furniture company has just won a contract "
                            "to supply office desks to a multinational corporation. "
                            "The order is large — five thousand desks over six months — "
                            "and the management team needs to make sure the deal is profitable. "
                            "To do that, they turn to cost accounting.\n\n"
                            "The first step is to identify all the costs involved in producing the desks. "
                            "The cost accountant separates them into two categories. "
                            "Direct costs are those that can be traced to each desk: "
                            "the wood, the metal legs, the screws, and the wages of the carpenters "
                            "who cut, assemble, and sand each piece. "
                            "These costs are straightforward — "
                            "the company knows exactly how much material and labor goes into one desk.\n\n"
                            "Then there are indirect costs — expenses that support production "
                            "but cannot be linked to a single desk. "
                            "The factory's electricity bill, the salary of the quality inspector, "
                            "the cost of maintaining the cutting machines, "
                            "and the rent for the warehouse where finished desks are stored — "
                            "all of these are overhead. "
                            "The challenge is figuring out how much overhead each desk should carry.\n\n"
                            "This is where allocation comes in. "
                            "The accountant decides to allocate overhead based on machine hours. "
                            "If the total monthly overhead is one billion dong "
                            "and the factory runs its machines for ten thousand hours, "
                            "the allocation rate is one hundred thousand dong per machine hour. "
                            "Each desk takes two machine hours to produce, "
                            "so each desk is allocated two hundred thousand dong of overhead.\n\n"
                            "Using absorption costing, the accountant calculates the full cost per desk. "
                            "Direct materials cost three hundred thousand dong. "
                            "Direct labor costs one hundred and fifty thousand dong. "
                            "Allocated overhead adds two hundred thousand dong. "
                            "The total absorption cost is six hundred and fifty thousand dong per desk. "
                            "This method ensures that every cost — both direct and indirect — "
                            "is reflected in the product's price.\n\n"
                            "But the sales manager wants a different perspective. "
                            "She asks: what is the marginal cost of producing one more desk? "
                            "Under marginal costing, only variable costs count. "
                            "The wood, metal, screws, and carpenter wages total four hundred and fifty thousand dong. "
                            "Fixed overhead is excluded because it does not change "
                            "whether the factory makes one more desk or one fewer. "
                            "The contribution per desk — selling price minus variable cost — "
                            "is three hundred and fifty thousand dong if the desk sells for eight hundred thousand. "
                            "This contribution goes toward covering fixed costs and generating profit.\n\n"
                            "Before signing the contract, the finance director runs a breakeven analysis. "
                            "The company's total fixed costs for the six-month period are three billion dong. "
                            "With a contribution of three hundred and fifty thousand dong per desk, "
                            "the breakeven point is approximately eight thousand five hundred and seventy-one desks. "
                            "Since the contract is for only five thousand desks, "
                            "the company needs additional orders to reach breakeven. "
                            "The director checks the sales forecast, "
                            "which predicts total demand of twelve thousand desks across all customers. "
                            "If the forecast is accurate, the company will comfortably pass breakeven "
                            "and earn a healthy profit.\n\n"
                            "To prepare for the project, the accounting team sets standard costs. "
                            "The standard cost for wood is based on current supplier prices "
                            "plus a small buffer for price fluctuations. "
                            "The standard labor time is ninety minutes per desk, "
                            "based on time studies conducted on the factory floor. "
                            "These standards become the budget targets for the production team.\n\n"
                            "Three months into the contract, the accountant compares "
                            "actual costs to the standards. "
                            "The actual cost of wood has risen by eight percent "
                            "because a typhoon damaged timber plantations in the central region. "
                            "This creates an unfavorable material price variance. "
                            "However, the carpenters have become more efficient with practice, "
                            "completing each desk in eighty minutes instead of ninety. "
                            "This creates a favorable labor efficiency variance. "
                            "The net effect is a small overall variance — "
                            "the savings in labor nearly offset the increase in material costs.\n\n"
                            "The management team reviews the performance report. "
                            "The production department's performance is strong — "
                            "output is on schedule, quality defects are below two percent, "
                            "and controllable costs are within budget. "
                            "The factory manager has done an excellent job managing overtime, "
                            "reducing material waste, and negotiating with local suppliers. "
                            "These are all controllable costs that she can directly influence.\n\n"
                            "The increase in wood prices, however, is an uncontrollable cost. "
                            "The factory manager had no way to prevent the typhoon "
                            "or the resulting spike in timber prices. "
                            "The performance evaluation system recognizes this distinction — "
                            "the manager is praised for her controllable cost management "
                            "and not penalized for the uncontrollable price increase.\n\n"
                            "Finally, the finance director compares the company's cost structure "
                            "to industry benchmarks. "
                            "The benchmark data shows that the average furniture manufacturer in Vietnam "
                            "spends thirty-five percent of revenue on direct materials "
                            "and twenty percent on overhead. "
                            "The company's numbers are close to the benchmark — "
                            "thirty-three percent on materials and twenty-two percent on overhead. "
                            "The slightly higher overhead is explained by the company's investment "
                            "in modern CNC machines, which increase overhead "
                            "but improve quality and reduce labor costs.\n\n"
                            "By the end of the six-month contract, the company has delivered "
                            "all five thousand desks on time and within budget. "
                            "The cost accounting system — from allocation to variance analysis, "
                            "from breakeven calculations to performance benchmarks — "
                            "gave managers the information they needed to make smart decisions "
                            "at every stage of the project."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chi phí sản xuất doanh nghiệp",
                    "description": "Viết đoạn văn tiếng Anh phân tích chi phí sản xuất sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của kế toán chi phí trong doanh nghiệp. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích cách một nhà máy sản xuất Việt Nam sử dụng absorption costing và marginal costing để đưa ra quyết định khác nhau. Giải thích vai trò của direct costs, indirect costs, overhead allocation, và contribution trong việc tính giá thành sản phẩm.",
                            "Hãy giải thích cách một doanh nghiệp sử dụng variance analysis và performance benchmarks để đánh giá hiệu quả chi phí. Phân tích sự khác biệt giữa standard costs và actual costs, vai trò của forecast trong lập budget, và tầm quan trọng của việc phân biệt controllable và uncontrollable costs."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần hành động thực tiễn.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Kế toán chi phí. "
                            "18 từ vựng này không chỉ là kiến thức — chúng là công cụ. "
                            "Và công cụ chỉ có giá trị khi bạn sử dụng chúng. "
                            "Vậy hãy cùng ôn lại 6 từ quan trọng nhất "
                            "và nghĩ xem bạn sẽ dùng chúng ở đâu ngay tuần này.\n\n"
                            "Variance — chênh lệch. Đây là từ mà mọi nhà quản lý cần biết, "
                            "vì nó là tín hiệu sớm nhất cho thấy kế hoạch đang đi đúng hướng hay chệch hướng. "
                            "Lần tới khi bạn đọc một báo cáo quản trị bằng tiếng Anh, "
                            "hãy tìm cột variance — nó sẽ cho bạn biết câu chuyện thật. "
                            "Ví dụ mới: The monthly variance report revealed that the packaging department "
                            "had saved four hundred million dong by switching to a domestic supplier, "
                            "creating a favorable material price variance that offset higher labor costs.\n\n"
                            "Contribution — đóng góp biên. Từ này thay đổi cách bạn nhìn mỗi sản phẩm. "
                            "Thay vì hỏi 'sản phẩm này lãi bao nhiêu?', bạn hỏi "
                            "'sản phẩm này đóng góp bao nhiêu vào việc bù đắp chi phí cố định?' "
                            "Đó là tư duy marginal costing — và nó cực kỳ hữu ích cho quyết định ngắn hạn. "
                            "Ví dụ mới: The sales team used contribution analysis to decide which products "
                            "to promote during the holiday season, focusing on items with the highest "
                            "contribution margin rather than the highest selling price.\n\n"
                            "Breakeven — hòa vốn. Mỗi doanh nghiệp, mỗi dự án, mỗi sản phẩm mới "
                            "đều có một con số breakeven. Biết con số đó, bạn biết mình cần bán bao nhiêu "
                            "trước khi bắt đầu kiếm lời. Đó là điểm xuất phát của mọi kế hoạch kinh doanh. "
                            "Ví dụ mới: Before launching the new product line, the team calculated "
                            "that the breakeven point was three thousand units per month — "
                            "a target they believed was achievable based on pre-order data from distributors.\n\n"
                            "Benchmark — chuẩn đối sánh. Bạn không thể cải thiện "
                            "nếu bạn không biết mình đang ở đâu so với người khác. "
                            "Benchmark cho bạn điểm tham chiếu — và từ đó, bạn biết cần làm gì tiếp theo. "
                            "Ví dụ mới: After benchmarking against three competitors in the same industrial zone, "
                            "the company discovered that its energy cost per unit was thirty percent higher "
                            "and immediately began auditing its electricity usage patterns.\n\n"
                            "Allocation — phân bổ. Cách bạn phân bổ chi phí chung "
                            "quyết định giá thành sản phẩm — và giá thành quyết định giá bán. "
                            "Một phương pháp allocation sai có thể khiến bạn định giá quá cao "
                            "cho sản phẩm này và quá thấp cho sản phẩm kia. "
                            "Ví dụ mới: The company switched from allocating overhead based on direct labor hours "
                            "to machine hours, which more accurately reflected how each product line "
                            "actually consumed factory resources.\n\n"
                            "Forecast — dự báo. Ngân sách tốt bắt đầu từ dự báo tốt. "
                            "Nếu bạn dự báo sai, ngân sách sẽ sai, và variance sẽ lớn. "
                            "Forecast không cần hoàn hảo — nhưng nó cần dựa trên dữ liệu thực tế, "
                            "không phải ước đoán cảm tính. "
                            "Ví dụ mới: The finance team improved its cost forecast accuracy by twenty percent "
                            "after incorporating real-time commodity price data and historical seasonal patterns "
                            "into their budgeting model.\n\n"
                            "Đây là điều tôi muốn bạn làm ngay sau bài học này: "
                            "mở một báo cáo quản trị bằng tiếng Anh — có thể là báo cáo chi phí, "
                            "báo cáo ngân sách, hoặc báo cáo hiệu quả bộ phận — "
                            "và tìm xem bao nhiêu trong 18 từ vựng hôm nay xuất hiện trong đó. "
                            "Bạn sẽ ngạc nhiên khi thấy chúng ở khắp nơi.\n\n"
                            "Kế toán chi phí không phải lý thuyết trên giấy — "
                            "nó là ngôn ngữ mà mọi nhà quản lý dùng mỗi ngày để ra quyết định. "
                            "Và bây giờ, bạn đã nói được ngôn ngữ đó. "
                            "Hãy dùng nó. Chúc bạn thành công — hẹn gặp lại ở bài học tiếp theo!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Cost Accounting – Kế Toán Chi Phí' AND uid = '{UID}' ORDER BY created_at;")
