"""
Create curriculum: Financial Statements – Báo Cáo Tài Chính
Series D — Kế Toán & Tài Chính Doanh Nghiệp (Accounting & Corporate Finance), curriculum #1
18 words | 5 sessions | surprising_fact tone | quiet awe farewell
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
W1 = ["asset", "liability", "equity", "revenue", "expense", "balance"]
W2 = ["income", "statement", "cash", "flow", "receivable", "payable"]
W3 = ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Financial Statements – Báo Cáo Tài Chính",
    "contentTypeTags": [],
    "description": (
        "MỘT DOANH NGHIỆP TRÊN SÀN CHỨNG KHOÁN VIỆT NAM PHẢI CÔNG BỐ BÁO CÁO TÀI CHÍNH MỖI QUÝ — VÀ 100% TÀI LIỆU GỐC ĐỀU VIẾT BẰNG THUẬT NGỮ KẾ TOÁN QUỐC TẾ.\n\n"
        "Bạn ngồi trong lớp kế toán, giảng viên chiếu bảng cân đối kế toán của Vinamilk lên màn hình. "
        "Bạn hiểu 'tài sản' và 'nợ phải trả' bằng tiếng Việt, nhưng khi đề thi yêu cầu phân tích "
        "asset, liability, equity trên báo cáo tiếng Anh — bạn đứng hình. "
        "Những từ này không khó về mặt logic, nhưng chúng là ngôn ngữ chung "
        "của mọi báo cáo tài chính trên thế giới.\n\n"
        "Hãy nghĩ về 18 từ vựng kế toán này như bộ chìa khóa vạn năng — "
        "một khi bạn nắm được chúng, mọi cánh cửa báo cáo tài chính tiếng Anh đều mở ra. "
        "Từ balance sheet đến income statement, từ cash flow đến disclosure — "
        "bạn sẽ đọc được 'ngôn ngữ' mà mọi doanh nghiệp trên thế giới dùng để kể câu chuyện tài chính.\n\n"
        "Sau khóa học, bạn sẽ tự tin đọc báo cáo tài chính tiếng Anh mà không cần tra từ điển mỗi dòng, "
        "phân tích financial statements trong bài tập nhóm, "
        "và viết nhận xét về tình hình tài chính doanh nghiệp bằng tiếng Anh chuyên ngành.\n\n"
        "18 từ vựng — từ asset đến disclosure — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kế toán tài chính, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về báo cáo tài chính — "
            "ngôn ngữ chung của mọi doanh nghiệp trên thế giới. "
            "Bạn sẽ học asset, liability, equity, revenue, expense, balance trong phần đầu tiên, "
            "nơi bài đọc giải thích cách đọc hiểu bảng cân đối kế toán. "
            "Tiếp theo là income, statement, cash, flow, receivable, payable — "
            "những từ giúp bạn hiểu báo cáo kết quả kinh doanh và lưu chuyển tiền tệ. "
            "Cuối cùng, accrual, depreciation, amortization, retained, comprehensive, disclosure "
            "đưa bạn vào thế giới nguyên tắc kế toán và công bố thông tin tài chính. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu báo cáo tài chính bằng tiếng Anh — "
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
                    "description": "Chào mừng bạn đến với bài học về báo cáo tài chính.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học đầu tiên trong chuỗi từ vựng Kế toán và Tài chính doanh nghiệp — "
                            "chủ đề hôm nay là Báo cáo tài chính, hay trong tiếng Anh là Financial Statements. "
                            "Mỗi doanh nghiệp, dù lớn hay nhỏ, đều phải kể câu chuyện tài chính của mình "
                            "qua một bộ báo cáo chuẩn hóa. Từ Vinamilk đến Samsung, từ startup đến tập đoàn đa quốc gia — "
                            "tất cả đều dùng cùng một ngôn ngữ kế toán quốc tế.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: asset, liability, equity, revenue, expense, và balance. "
                            "Đây là những từ nền tảng nhất — bạn sẽ gặp chúng trên mọi bảng cân đối kế toán.\n\n"
                            "Từ đầu tiên là asset — danh từ — nghĩa là tài sản, "
                            "bất kỳ nguồn lực nào mà doanh nghiệp sở hữu và có giá trị kinh tế. "
                            "Ví dụ: 'The company's total assets include cash, equipment, buildings, and intellectual property worth over two billion dollars.' "
                            "Trong bài đọc, asset xuất hiện ở phía bên trái của bảng cân đối kế toán — "
                            "nó cho biết doanh nghiệp đang nắm giữ những gì.\n\n"
                            "Từ thứ hai là liability — danh từ — nghĩa là nợ phải trả, "
                            "nghĩa vụ tài chính mà doanh nghiệp phải thanh toán cho bên khác. "
                            "Ví dụ: 'The firm's liabilities include bank loans, unpaid supplier invoices, and employee salaries that are due next month.' "
                            "Trong bài đọc, liability nằm ở phía bên phải của bảng cân đối kế toán — "
                            "nó cho biết doanh nghiệp đang nợ bao nhiêu.\n\n"
                            "Từ thứ ba là equity — danh từ — nghĩa là vốn chủ sở hữu, "
                            "phần giá trị còn lại sau khi trừ tất cả nợ phải trả khỏi tổng tài sản. "
                            "Ví dụ: 'Shareholders' equity represents the owners' claim on the company after all debts have been paid.' "
                            "Trong bài đọc, equity là phần cuối cùng của phương trình kế toán cơ bản: "
                            "Assets = Liabilities + Equity.\n\n"
                            "Từ thứ tư là revenue — danh từ — nghĩa là doanh thu, "
                            "tổng số tiền mà doanh nghiệp kiếm được từ hoạt động kinh doanh chính. "
                            "Ví dụ: 'The company reported revenue of fifteen million dollars from product sales in the third quarter.' "
                            "Trong bài đọc, revenue là dòng đầu tiên trên báo cáo kết quả kinh doanh — "
                            "nó cho biết doanh nghiệp đã bán được bao nhiêu.\n\n"
                            "Từ thứ năm là expense — danh từ — nghĩa là chi phí, "
                            "số tiền mà doanh nghiệp phải chi ra để vận hành và tạo ra doanh thu. "
                            "Ví dụ: 'Operating expenses such as rent, salaries, and utilities totaled eight million dollars for the year.' "
                            "Trong bài đọc, expense được trừ khỏi revenue để tính lợi nhuận — "
                            "chi phí càng cao, lợi nhuận càng thấp.\n\n"
                            "Từ cuối cùng là balance — danh từ — nghĩa là số dư hoặc cân đối, "
                            "trạng thái cân bằng giữa hai phía của một báo cáo tài chính. "
                            "Ví dụ: 'The balance sheet must always balance — total assets must equal the sum of liabilities and equity.' "
                            "Trong bài đọc, balance là nguyên tắc cốt lõi — "
                            "nếu hai bên không cân bằng, có lỗi trong sổ sách kế toán.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách đọc hiểu bảng cân đối kế toán nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tài sản, nợ và vốn chủ sở hữu",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {"vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tài sản, nợ và vốn chủ sở hữu",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {"vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tài sản, nợ và vốn chủ sở hữu",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {"vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tài sản, nợ và vốn chủ sở hữu",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {"vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Tài sản, nợ và vốn chủ sở hữu",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {"vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Bảng cân đối kế toán",
                    "description": "Every company tells its financial story through a set of standardized reports.",
                    "data": {
                        "text": (
                            "Every company tells its financial story through a set of standardized reports. "
                            "The most fundamental of these is the balance sheet — "
                            "a snapshot of what a company owns, what it owes, and what belongs to its owners "
                            "at a specific point in time.\n\n"
                            "The balance sheet is built on a simple equation: "
                            "Assets equal Liabilities plus Equity. "
                            "This equation must always hold true. "
                            "If a company has one hundred million dong in total assets, "
                            "and it owes sixty million dong to banks and suppliers, "
                            "then the remaining forty million dong is equity — "
                            "the portion that belongs to the owners or shareholders.\n\n"
                            "An asset is anything of value that a company controls. "
                            "Assets are divided into two categories: current and non-current. "
                            "Current assets include cash, inventory, and money that customers owe — "
                            "things that can be converted to cash within one year. "
                            "Non-current assets include buildings, machinery, and long-term investments — "
                            "resources that the company will use for more than one year.\n\n"
                            "On the other side of the balance sheet are liabilities. "
                            "A liability is a financial obligation — money the company must pay to someone else. "
                            "Like assets, liabilities are classified as current or non-current. "
                            "Current liabilities include short-term loans and bills due within a year. "
                            "Non-current liabilities include long-term bank loans and bonds that mature in several years.\n\n"
                            "Equity represents the owners' stake in the company. "
                            "For a publicly traded company in Vietnam, equity includes the money "
                            "that shareholders originally invested plus any profits the company has kept over the years. "
                            "When a company earns more revenue than it spends on expenses, "
                            "the profit increases equity. When expenses exceed revenue, "
                            "the loss reduces equity.\n\n"
                            "Revenue is the money a company earns from its main business activities. "
                            "A coffee shop's revenue comes from selling coffee. "
                            "A software company's revenue comes from selling licenses and subscriptions. "
                            "Revenue appears at the top of the income statement — "
                            "another key financial report that we will explore in the next session.\n\n"
                            "Expense is the cost of doing business. "
                            "Rent, salaries, raw materials, electricity — these are all expenses. "
                            "When revenue is greater than expenses, the company makes a profit. "
                            "When expenses are greater than revenue, the company reports a loss. "
                            "The relationship between revenue and expense determines "
                            "whether a company is growing or struggling.\n\n"
                            "The word balance in accounting has a precise meaning. "
                            "The balance sheet must always balance — "
                            "the left side (assets) must equal the right side (liabilities plus equity). "
                            "If the numbers do not balance, there is an error somewhere in the records. "
                            "This principle of balance is the foundation of double-entry bookkeeping, "
                            "a system that accountants have used for over five hundred years."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Bảng cân đối kế toán",
                    "description": "Every company tells its financial story through a set of standardized reports.",
                    "data": {
                        "text": (
                            "Every company tells its financial story through a set of standardized reports. "
                            "The most fundamental of these is the balance sheet — "
                            "a snapshot of what a company owns, what it owes, and what belongs to its owners "
                            "at a specific point in time.\n\n"
                            "The balance sheet is built on a simple equation: "
                            "Assets equal Liabilities plus Equity. "
                            "This equation must always hold true. "
                            "If a company has one hundred million dong in total assets, "
                            "and it owes sixty million dong to banks and suppliers, "
                            "then the remaining forty million dong is equity — "
                            "the portion that belongs to the owners or shareholders.\n\n"
                            "An asset is anything of value that a company controls. "
                            "Assets are divided into two categories: current and non-current. "
                            "Current assets include cash, inventory, and money that customers owe — "
                            "things that can be converted to cash within one year. "
                            "Non-current assets include buildings, machinery, and long-term investments — "
                            "resources that the company will use for more than one year.\n\n"
                            "On the other side of the balance sheet are liabilities. "
                            "A liability is a financial obligation — money the company must pay to someone else. "
                            "Like assets, liabilities are classified as current or non-current. "
                            "Current liabilities include short-term loans and bills due within a year. "
                            "Non-current liabilities include long-term bank loans and bonds that mature in several years.\n\n"
                            "Equity represents the owners' stake in the company. "
                            "For a publicly traded company in Vietnam, equity includes the money "
                            "that shareholders originally invested plus any profits the company has kept over the years. "
                            "When a company earns more revenue than it spends on expenses, "
                            "the profit increases equity. When expenses exceed revenue, "
                            "the loss reduces equity.\n\n"
                            "Revenue is the money a company earns from its main business activities. "
                            "A coffee shop's revenue comes from selling coffee. "
                            "A software company's revenue comes from selling licenses and subscriptions. "
                            "Revenue appears at the top of the income statement — "
                            "another key financial report that we will explore in the next session.\n\n"
                            "Expense is the cost of doing business. "
                            "Rent, salaries, raw materials, electricity — these are all expenses. "
                            "When revenue is greater than expenses, the company makes a profit. "
                            "When expenses are greater than revenue, the company reports a loss. "
                            "The relationship between revenue and expense determines "
                            "whether a company is growing or struggling.\n\n"
                            "The word balance in accounting has a precise meaning. "
                            "The balance sheet must always balance — "
                            "the left side (assets) must equal the right side (liabilities plus equity). "
                            "If the numbers do not balance, there is an error somewhere in the records. "
                            "This principle of balance is the foundation of double-entry bookkeeping, "
                            "a system that accountants have used for over five hundred years."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Bảng cân đối kế toán",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every company tells its financial story through a set of standardized reports. "
                            "The most fundamental of these is the balance sheet — "
                            "a snapshot of what a company owns, what it owes, and what belongs to its owners "
                            "at a specific point in time.\n\n"
                            "The balance sheet is built on a simple equation: "
                            "Assets equal Liabilities plus Equity. "
                            "This equation must always hold true. "
                            "If a company has one hundred million dong in total assets, "
                            "and it owes sixty million dong to banks and suppliers, "
                            "then the remaining forty million dong is equity — "
                            "the portion that belongs to the owners or shareholders.\n\n"
                            "An asset is anything of value that a company controls. "
                            "Assets are divided into two categories: current and non-current. "
                            "Current assets include cash, inventory, and money that customers owe — "
                            "things that can be converted to cash within one year. "
                            "Non-current assets include buildings, machinery, and long-term investments — "
                            "resources that the company will use for more than one year.\n\n"
                            "On the other side of the balance sheet are liabilities. "
                            "A liability is a financial obligation — money the company must pay to someone else. "
                            "Like assets, liabilities are classified as current or non-current. "
                            "Current liabilities include short-term loans and bills due within a year. "
                            "Non-current liabilities include long-term bank loans and bonds that mature in several years.\n\n"
                            "Equity represents the owners' stake in the company. "
                            "For a publicly traded company in Vietnam, equity includes the money "
                            "that shareholders originally invested plus any profits the company has kept over the years. "
                            "When a company earns more revenue than it spends on expenses, "
                            "the profit increases equity. When expenses exceed revenue, "
                            "the loss reduces equity.\n\n"
                            "Revenue is the money a company earns from its main business activities. "
                            "A coffee shop's revenue comes from selling coffee. "
                            "A software company's revenue comes from selling licenses and subscriptions. "
                            "Revenue appears at the top of the income statement — "
                            "another key financial report that we will explore in the next session.\n\n"
                            "Expense is the cost of doing business. "
                            "Rent, salaries, raw materials, electricity — these are all expenses. "
                            "When revenue is greater than expenses, the company makes a profit. "
                            "When expenses are greater than revenue, the company reports a loss. "
                            "The relationship between revenue and expense determines "
                            "whether a company is growing or struggling.\n\n"
                            "The word balance in accounting has a precise meaning. "
                            "The balance sheet must always balance — "
                            "the left side (assets) must equal the right side (liabilities plus equity). "
                            "If the numbers do not balance, there is an error somewhere in the records. "
                            "This principle of balance is the foundation of double-entry bookkeeping, "
                            "a system that accountants have used for over five hundred years."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tài sản, nợ và vốn chủ sở hữu",
                    "description": "Viết câu sử dụng 6 từ vựng về bảng cân đối kế toán.",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"],
                        "items": [
                            {
                                "targetVocab": "asset",
                                "prompt": "Dùng từ 'asset' để viết một câu về tài sản của một doanh nghiệp và cách chúng được phân loại trên bảng cân đối kế toán. Ví dụ: The company's largest asset is its factory in Binh Duong, which is valued at over fifty billion dong on the balance sheet."
                            },
                            {
                                "targetVocab": "liability",
                                "prompt": "Dùng từ 'liability' để viết một câu về nghĩa vụ tài chính mà doanh nghiệp phải thanh toán. Ví dụ: The firm's current liabilities increased sharply after it borrowed twenty billion dong from the bank to expand its production line."
                            },
                            {
                                "targetVocab": "equity",
                                "prompt": "Dùng từ 'equity' để viết một câu về vốn chủ sở hữu và mối quan hệ với tài sản và nợ. Ví dụ: After paying off all its debts, the company's equity stood at thirty billion dong, representing the true value belonging to shareholders."
                            },
                            {
                                "targetVocab": "revenue",
                                "prompt": "Dùng từ 'revenue' để viết một câu về doanh thu của một doanh nghiệp trong một kỳ báo cáo. Ví dụ: The coffee chain reported revenue of one hundred billion dong in the first half of the year, a twenty percent increase compared to the same period last year."
                            },
                            {
                                "targetVocab": "expense",
                                "prompt": "Dùng từ 'expense' để viết một câu về chi phí hoạt động và tác động đến lợi nhuận. Ví dụ: Rising raw material expenses forced the manufacturer to increase product prices by ten percent to maintain its profit margin."
                            },
                            {
                                "targetVocab": "balance",
                                "prompt": "Dùng từ 'balance' để viết một câu về nguyên tắc cân đối trong kế toán. Ví dụ: The accountant discovered that the balance sheet did not balance because a payment of five hundred million dong had been recorded twice in the system."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về báo cáo kết quả kinh doanh và lưu chuyển tiền tệ.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "asset — tài sản, liability — nợ phải trả, equity — vốn chủ sở hữu, "
                            "revenue — doanh thu, expense — chi phí, và balance — cân đối. "
                            "Bạn đã hiểu cách đọc bảng cân đối kế toán — bức ảnh chụp tài chính của doanh nghiệp. "
                            "Bây giờ, chúng ta sẽ đi vào hai báo cáo quan trọng tiếp theo: "
                            "báo cáo kết quả kinh doanh và báo cáo lưu chuyển tiền tệ.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: income, statement, cash, flow, receivable, và payable. "
                            "Đây là bộ từ vựng giúp bạn hiểu doanh nghiệp kiếm tiền và chi tiền như thế nào.\n\n"
                            "Từ đầu tiên là income — danh từ — nghĩa là thu nhập hoặc lợi nhuận, "
                            "số tiền còn lại sau khi trừ tất cả chi phí khỏi doanh thu. "
                            "Ví dụ: 'The company's net income for the year was three billion dong after deducting all operating costs and taxes.' "
                            "Trong bài đọc, income là con số cuối cùng trên báo cáo kết quả kinh doanh — "
                            "nó cho biết doanh nghiệp thực sự kiếm được bao nhiêu.\n\n"
                            "Từ thứ hai là statement — danh từ — nghĩa là báo cáo, "
                            "tài liệu chính thức trình bày thông tin tài chính của doanh nghiệp. "
                            "Ví dụ: 'The income statement shows how much revenue the company earned and how much it spent over a specific period.' "
                            "Trong bài đọc, statement kết hợp với các từ khác để tạo thành tên các báo cáo: "
                            "income statement, cash flow statement, financial statement.\n\n"
                            "Từ thứ ba là cash — danh từ — nghĩa là tiền mặt, "
                            "tiền thực tế mà doanh nghiệp có trong tay hoặc trong tài khoản ngân hàng. "
                            "Ví dụ: 'Despite reporting high profits, the company had very little cash in its bank account because most customers had not yet paid.' "
                            "Trong bài đọc, cash là yếu tố sống còn — "
                            "một doanh nghiệp có thể có lợi nhuận trên giấy nhưng vẫn phá sản nếu hết tiền mặt.\n\n"
                            "Từ thứ tư là flow — danh từ — nghĩa là dòng chảy, "
                            "sự di chuyển của tiền vào và ra khỏi doanh nghiệp. "
                            "Ví dụ: 'The cash flow statement tracks every dong that enters and leaves the business during the reporting period.' "
                            "Trong bài đọc, flow kết hợp với cash để tạo thành cash flow — "
                            "dòng tiền, một trong những chỉ số quan trọng nhất để đánh giá sức khỏe tài chính.\n\n"
                            "Từ thứ năm là receivable — tính từ/danh từ — nghĩa là phải thu, "
                            "số tiền mà khách hàng nợ doanh nghiệp nhưng chưa thanh toán. "
                            "Ví dụ: 'Accounts receivable increased to ten billion dong because the company allowed its biggest customers to pay within ninety days.' "
                            "Trong bài đọc, receivable là tài sản trên bảng cân đối kế toán — "
                            "tiền mà doanh nghiệp có quyền nhận nhưng chưa nhận được.\n\n"
                            "Từ cuối cùng là payable — tính từ/danh từ — nghĩa là phải trả, "
                            "số tiền mà doanh nghiệp nợ nhà cung cấp hoặc bên khác. "
                            "Ví dụ: 'The company's accounts payable rose sharply after it purchased raw materials on credit from three new suppliers.' "
                            "Trong bài đọc, payable là nợ phải trả ngắn hạn — "
                            "tiền mà doanh nghiệp phải thanh toán cho người khác trong tương lai gần.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về báo cáo kết quả kinh doanh và lưu chuyển tiền tệ nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Báo cáo kết quả kinh doanh và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {"vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Báo cáo kết quả kinh doanh và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {"vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Báo cáo kết quả kinh doanh và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {"vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Báo cáo kết quả kinh doanh và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {"vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Báo cáo kết quả kinh doanh và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {"vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Báo cáo kết quả kinh doanh và lưu chuyển tiền tệ",
                    "description": "While the balance sheet shows what a company owns and owes at a single moment, the income statement tells a different story.",
                    "data": {
                        "text": (
                            "While the balance sheet shows what a company owns and owes at a single moment, "
                            "the income statement tells a different story. "
                            "It answers a simple but crucial question: "
                            "did the company make money or lose money over a period of time?\n\n"
                            "The income statement starts with revenue at the top. "
                            "Revenue is the total amount of money the company earned from selling its products or services. "
                            "A Vietnamese garment manufacturer, for example, might report revenue "
                            "from exporting shirts and jackets to European retailers. "
                            "Revenue is sometimes called the top line because it appears first on the statement.\n\n"
                            "Below revenue, the statement lists various expenses — "
                            "the costs the company incurred to generate that revenue. "
                            "These include the cost of raw materials, employee salaries, rent, marketing, "
                            "and many other items. Each category of expense is listed separately "
                            "so that readers can see exactly where the money went.\n\n"
                            "After subtracting all expenses from revenue, the statement arrives at net income. "
                            "Net income is the company's profit — the money left over after everything has been paid. "
                            "If expenses exceed revenue, the result is a net loss instead of net income. "
                            "Investors pay close attention to income because it shows "
                            "whether the company's business model is actually working.\n\n"
                            "But income alone does not tell the whole story. "
                            "A company can report strong income on its statement "
                            "and still run out of cash. How is that possible? "
                            "The answer lies in the difference between profit and cash flow.\n\n"
                            "Cash flow measures the actual movement of money into and out of the business. "
                            "The cash flow statement is divided into three sections: "
                            "operating activities, investing activities, and financing activities. "
                            "Operating cash flow shows how much cash the company generated "
                            "from its day-to-day business. Investing cash flow tracks money spent on "
                            "buying or selling long-term assets. Financing cash flow records "
                            "transactions with lenders and shareholders.\n\n"
                            "One reason income and cash flow can differ is accounts receivable. "
                            "When a company sells goods on credit, it records the sale as revenue immediately, "
                            "even though the customer has not yet paid. "
                            "The unpaid amount appears as receivable on the balance sheet. "
                            "Until the customer actually pays, the company has revenue but no cash.\n\n"
                            "The opposite situation involves accounts payable. "
                            "When a company buys supplies on credit, it records the expense "
                            "but does not pay cash right away. "
                            "The amount owed appears as payable on the balance sheet. "
                            "This means the company has spent money on paper but still holds the cash. "
                            "Understanding the relationship between receivable and payable "
                            "is essential for reading financial statements accurately."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Báo cáo kết quả kinh doanh và lưu chuyển tiền tệ",
                    "description": "While the balance sheet shows what a company owns and owes at a single moment, the income statement tells a different story.",
                    "data": {
                        "text": (
                            "While the balance sheet shows what a company owns and owes at a single moment, "
                            "the income statement tells a different story. "
                            "It answers a simple but crucial question: "
                            "did the company make money or lose money over a period of time?\n\n"
                            "The income statement starts with revenue at the top. "
                            "Revenue is the total amount of money the company earned from selling its products or services. "
                            "A Vietnamese garment manufacturer, for example, might report revenue "
                            "from exporting shirts and jackets to European retailers. "
                            "Revenue is sometimes called the top line because it appears first on the statement.\n\n"
                            "Below revenue, the statement lists various expenses — "
                            "the costs the company incurred to generate that revenue. "
                            "These include the cost of raw materials, employee salaries, rent, marketing, "
                            "and many other items. Each category of expense is listed separately "
                            "so that readers can see exactly where the money went.\n\n"
                            "After subtracting all expenses from revenue, the statement arrives at net income. "
                            "Net income is the company's profit — the money left over after everything has been paid. "
                            "If expenses exceed revenue, the result is a net loss instead of net income. "
                            "Investors pay close attention to income because it shows "
                            "whether the company's business model is actually working.\n\n"
                            "But income alone does not tell the whole story. "
                            "A company can report strong income on its statement "
                            "and still run out of cash. How is that possible? "
                            "The answer lies in the difference between profit and cash flow.\n\n"
                            "Cash flow measures the actual movement of money into and out of the business. "
                            "The cash flow statement is divided into three sections: "
                            "operating activities, investing activities, and financing activities. "
                            "Operating cash flow shows how much cash the company generated "
                            "from its day-to-day business. Investing cash flow tracks money spent on "
                            "buying or selling long-term assets. Financing cash flow records "
                            "transactions with lenders and shareholders.\n\n"
                            "One reason income and cash flow can differ is accounts receivable. "
                            "When a company sells goods on credit, it records the sale as revenue immediately, "
                            "even though the customer has not yet paid. "
                            "The unpaid amount appears as receivable on the balance sheet. "
                            "Until the customer actually pays, the company has revenue but no cash.\n\n"
                            "The opposite situation involves accounts payable. "
                            "When a company buys supplies on credit, it records the expense "
                            "but does not pay cash right away. "
                            "The amount owed appears as payable on the balance sheet. "
                            "This means the company has spent money on paper but still holds the cash. "
                            "Understanding the relationship between receivable and payable "
                            "is essential for reading financial statements accurately."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Báo cáo kết quả kinh doanh và lưu chuyển tiền tệ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "While the balance sheet shows what a company owns and owes at a single moment, "
                            "the income statement tells a different story. "
                            "It answers a simple but crucial question: "
                            "did the company make money or lose money over a period of time?\n\n"
                            "The income statement starts with revenue at the top. "
                            "Revenue is the total amount of money the company earned from selling its products or services. "
                            "A Vietnamese garment manufacturer, for example, might report revenue "
                            "from exporting shirts and jackets to European retailers. "
                            "Revenue is sometimes called the top line because it appears first on the statement.\n\n"
                            "Below revenue, the statement lists various expenses — "
                            "the costs the company incurred to generate that revenue. "
                            "These include the cost of raw materials, employee salaries, rent, marketing, "
                            "and many other items. Each category of expense is listed separately "
                            "so that readers can see exactly where the money went.\n\n"
                            "After subtracting all expenses from revenue, the statement arrives at net income. "
                            "Net income is the company's profit — the money left over after everything has been paid. "
                            "If expenses exceed revenue, the result is a net loss instead of net income. "
                            "Investors pay close attention to income because it shows "
                            "whether the company's business model is actually working.\n\n"
                            "But income alone does not tell the whole story. "
                            "A company can report strong income on its statement "
                            "and still run out of cash. How is that possible? "
                            "The answer lies in the difference between profit and cash flow.\n\n"
                            "Cash flow measures the actual movement of money into and out of the business. "
                            "The cash flow statement is divided into three sections: "
                            "operating activities, investing activities, and financing activities. "
                            "Operating cash flow shows how much cash the company generated "
                            "from its day-to-day business. Investing cash flow tracks money spent on "
                            "buying or selling long-term assets. Financing cash flow records "
                            "transactions with lenders and shareholders.\n\n"
                            "One reason income and cash flow can differ is accounts receivable. "
                            "When a company sells goods on credit, it records the sale as revenue immediately, "
                            "even though the customer has not yet paid. "
                            "The unpaid amount appears as receivable on the balance sheet. "
                            "Until the customer actually pays, the company has revenue but no cash.\n\n"
                            "The opposite situation involves accounts payable. "
                            "When a company buys supplies on credit, it records the expense "
                            "but does not pay cash right away. "
                            "The amount owed appears as payable on the balance sheet. "
                            "This means the company has spent money on paper but still holds the cash. "
                            "Understanding the relationship between receivable and payable "
                            "is essential for reading financial statements accurately."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Báo cáo kết quả kinh doanh và dòng tiền",
                    "description": "Viết câu sử dụng 6 từ vựng về báo cáo kết quả kinh doanh và dòng tiền.",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"],
                        "items": [
                            {
                                "targetVocab": "income",
                                "prompt": "Dùng từ 'income' để viết một câu về lợi nhuận ròng của doanh nghiệp sau khi trừ chi phí. Ví dụ: The company's net income dropped by thirty percent this quarter because rising material costs ate into its profit margins."
                            },
                            {
                                "targetVocab": "statement",
                                "prompt": "Dùng từ 'statement' để viết một câu về một loại báo cáo tài chính và thông tin mà nó cung cấp. Ví dụ: The income statement revealed that the company spent more on marketing than on research and development for the first time in five years."
                            },
                            {
                                "targetVocab": "cash",
                                "prompt": "Dùng từ 'cash' để viết một câu về tầm quan trọng của tiền mặt đối với hoạt động doanh nghiệp. Ví dụ: Despite reporting record profits, the startup nearly collapsed because it did not have enough cash to pay its employees on time."
                            },
                            {
                                "targetVocab": "flow",
                                "prompt": "Dùng từ 'flow' để viết một câu về dòng tiền vào và ra của doanh nghiệp. Ví dụ: Positive operating cash flow indicates that the company is generating enough money from its core business to cover daily expenses without borrowing."
                            },
                            {
                                "targetVocab": "receivable",
                                "prompt": "Dùng từ 'receivable' để viết một câu về khoản phải thu từ khách hàng. Ví dụ: The company's accounts receivable grew to fifteen billion dong because it offered its retail partners a ninety-day payment window."
                            },
                            {
                                "targetVocab": "payable",
                                "prompt": "Dùng từ 'payable' để viết một câu về khoản phải trả cho nhà cung cấp. Ví dụ: By negotiating longer payment terms with suppliers, the company increased its accounts payable but improved its short-term cash position significantly."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về nguyên tắc kế toán và công bố thông tin.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: asset, liability, equity, revenue, expense, balance — "
                            "những khái niệm cốt lõi trên bảng cân đối kế toán. "
                            "Trong phần 2, bạn đã học thêm income, statement, cash, flow, receivable, payable — "
                            "bộ từ vựng về báo cáo kết quả kinh doanh và lưu chuyển tiền tệ.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh sâu hơn: "
                            "các nguyên tắc kế toán và nghĩa vụ công bố thông tin tài chính. "
                            "Bạn sẽ học 6 từ mới: accrual, depreciation, amortization, retained, comprehensive, và disclosure.\n\n"
                            "Từ đầu tiên là accrual — danh từ — nghĩa là dồn tích, "
                            "nguyên tắc kế toán ghi nhận doanh thu và chi phí khi chúng phát sinh, "
                            "không phải khi tiền thực sự được nhận hoặc chi trả. "
                            "Ví dụ: 'Under the accrual method, the company records revenue when it delivers the product, even if the customer pays thirty days later.' "
                            "Trong bài đọc, accrual giải thích vì sao lợi nhuận trên giấy "
                            "có thể khác xa số tiền thực tế trong tài khoản ngân hàng.\n\n"
                            "Từ thứ hai là depreciation — danh từ — nghĩa là khấu hao, "
                            "việc phân bổ chi phí của một tài sản hữu hình qua thời gian sử dụng. "
                            "Ví dụ: 'The factory equipment was purchased for ten billion dong and will be depreciated over ten years, reducing its book value by one billion dong each year.' "
                            "Trong bài đọc, depreciation là chi phí không dùng tiền mặt — "
                            "nó giảm giá trị tài sản trên sổ sách nhưng không có tiền thực sự rời khỏi công ty.\n\n"
                            "Từ thứ ba là amortization — danh từ — nghĩa là phân bổ, "
                            "tương tự depreciation nhưng áp dụng cho tài sản vô hình như bằng sáng chế hoặc bản quyền. "
                            "Ví dụ: 'The software license cost five billion dong and is subject to amortization over five years on the company's books.' "
                            "Trong bài đọc, amortization cho thấy rằng ngay cả tài sản vô hình "
                            "cũng mất giá trị theo thời gian và phải được ghi nhận trên báo cáo tài chính.\n\n"
                            "Từ thứ tư là retained — tính từ — nghĩa là giữ lại, "
                            "thường dùng trong cụm retained earnings — lợi nhuận giữ lại, "
                            "phần lợi nhuận mà doanh nghiệp không chia cho cổ đông mà giữ lại để tái đầu tư. "
                            "Ví dụ: 'The company's retained earnings grew to twenty billion dong because the board decided to reinvest profits rather than pay dividends.' "
                            "Trong bài đọc, retained earnings là một phần quan trọng của equity — "
                            "nó cho thấy doanh nghiệp đã tích lũy được bao nhiêu lợi nhuận qua các năm.\n\n"
                            "Từ thứ năm là comprehensive — tính từ — nghĩa là toàn diện, "
                            "thường dùng trong cụm comprehensive income — thu nhập toàn diện, "
                            "bao gồm cả lợi nhuận ròng và các khoản lãi lỗ chưa thực hiện. "
                            "Ví dụ: 'Comprehensive income includes not only net profit but also unrealized gains from foreign currency translation and investment revaluation.' "
                            "Trong bài đọc, comprehensive income cho bức tranh đầy đủ hơn net income — "
                            "nó bao gồm cả những thay đổi giá trị mà chưa được ghi nhận trên báo cáo kết quả kinh doanh.\n\n"
                            "Từ cuối cùng là disclosure — danh từ — nghĩa là công bố thông tin, "
                            "nghĩa vụ của doanh nghiệp phải cung cấp thông tin tài chính đầy đủ và trung thực. "
                            "Ví dụ: 'The company's disclosure notes revealed that it had a pending lawsuit that could cost up to fifty billion dong if the court ruled against it.' "
                            "Trong bài đọc, disclosure là phần thuyết minh báo cáo tài chính — "
                            "nơi doanh nghiệp giải thích chi tiết những con số trên các báo cáo chính.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về nguyên tắc kế toán và công bố thông tin nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nguyên tắc kế toán và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nguyên tắc kế toán và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nguyên tắc kế toán và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nguyên tắc kế toán và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nguyên tắc kế toán và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nguyên tắc kế toán và công bố thông tin tài chính",
                    "description": "Numbers on a financial statement do not appear by accident — they follow strict accounting rules.",
                    "data": {
                        "text": (
                            "Numbers on a financial statement do not appear by accident — "
                            "they follow strict accounting rules that determine when and how "
                            "transactions are recorded. Understanding these rules is essential "
                            "for anyone who wants to read financial reports with confidence.\n\n"
                            "The most important principle is accrual accounting. "
                            "Under the accrual method, revenue is recorded when it is earned, "
                            "not when cash is received. Similarly, an expense is recorded when it is incurred, "
                            "not when it is paid. For example, if a Vietnamese furniture company "
                            "delivers a shipment of tables to a hotel chain in December "
                            "but does not receive payment until February, "
                            "the revenue is recorded in December — the month the delivery happened. "
                            "This is why a company can show strong income on its statement "
                            "while having very little cash in the bank.\n\n"
                            "Another key concept is depreciation. "
                            "When a company buys a piece of equipment — say, a printing press for five billion dong — "
                            "it does not record the entire cost as an expense in the year of purchase. "
                            "Instead, the cost is spread over the useful life of the asset. "
                            "If the press is expected to last ten years, "
                            "the company records depreciation of five hundred million dong each year. "
                            "Depreciation reduces the book value of the asset on the balance sheet "
                            "and appears as an expense on the income statement, "
                            "even though no cash actually leaves the company.\n\n"
                            "Amortization works the same way but applies to intangible assets — "
                            "things you cannot touch, like patents, trademarks, and software licenses. "
                            "If a pharmaceutical company pays eight billion dong for a patent "
                            "that lasts twenty years, it records amortization of four hundred million dong annually. "
                            "Both depreciation and amortization are non-cash expenses, "
                            "meaning they reduce reported income without affecting cash flow directly.\n\n"
                            "After a company calculates its net income, "
                            "it must decide what to do with the profit. "
                            "Some of it may be distributed to shareholders as dividends. "
                            "The rest becomes retained earnings — profit that the company keeps "
                            "to reinvest in the business. Retained earnings accumulate over time "
                            "and appear in the equity section of the balance sheet. "
                            "A company with large retained earnings has been profitable for many years "
                            "and has chosen to reinvest rather than distribute its profits.\n\n"
                            "Beyond net income, accountants also calculate comprehensive income. "
                            "Comprehensive income includes net income plus other gains and losses "
                            "that are not part of regular business operations. "
                            "For example, if a Vietnamese company holds investments in foreign currencies, "
                            "changes in exchange rates can create unrealized gains or losses. "
                            "These appear in comprehensive income but not in net income. "
                            "The statement of comprehensive income gives investors a fuller picture "
                            "of all the changes in a company's financial position.\n\n"
                            "Finally, every set of financial statements includes disclosure notes. "
                            "Disclosure is the practice of providing additional information "
                            "that helps readers understand the numbers. "
                            "The notes might explain the company's accounting policies, "
                            "describe significant transactions, or reveal risks that are not obvious "
                            "from the main statements alone. "
                            "For example, a disclosure note might warn that the company "
                            "is involved in a lawsuit that could result in a large financial loss. "
                            "Without disclosure, investors would be making decisions based on incomplete information."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nguyên tắc kế toán và công bố thông tin tài chính",
                    "description": "Numbers on a financial statement do not appear by accident — they follow strict accounting rules.",
                    "data": {
                        "text": (
                            "Numbers on a financial statement do not appear by accident — "
                            "they follow strict accounting rules that determine when and how "
                            "transactions are recorded. Understanding these rules is essential "
                            "for anyone who wants to read financial reports with confidence.\n\n"
                            "The most important principle is accrual accounting. "
                            "Under the accrual method, revenue is recorded when it is earned, "
                            "not when cash is received. Similarly, an expense is recorded when it is incurred, "
                            "not when it is paid. For example, if a Vietnamese furniture company "
                            "delivers a shipment of tables to a hotel chain in December "
                            "but does not receive payment until February, "
                            "the revenue is recorded in December — the month the delivery happened. "
                            "This is why a company can show strong income on its statement "
                            "while having very little cash in the bank.\n\n"
                            "Another key concept is depreciation. "
                            "When a company buys a piece of equipment — say, a printing press for five billion dong — "
                            "it does not record the entire cost as an expense in the year of purchase. "
                            "Instead, the cost is spread over the useful life of the asset. "
                            "If the press is expected to last ten years, "
                            "the company records depreciation of five hundred million dong each year. "
                            "Depreciation reduces the book value of the asset on the balance sheet "
                            "and appears as an expense on the income statement, "
                            "even though no cash actually leaves the company.\n\n"
                            "Amortization works the same way but applies to intangible assets — "
                            "things you cannot touch, like patents, trademarks, and software licenses. "
                            "If a pharmaceutical company pays eight billion dong for a patent "
                            "that lasts twenty years, it records amortization of four hundred million dong annually. "
                            "Both depreciation and amortization are non-cash expenses, "
                            "meaning they reduce reported income without affecting cash flow directly.\n\n"
                            "After a company calculates its net income, "
                            "it must decide what to do with the profit. "
                            "Some of it may be distributed to shareholders as dividends. "
                            "The rest becomes retained earnings — profit that the company keeps "
                            "to reinvest in the business. Retained earnings accumulate over time "
                            "and appear in the equity section of the balance sheet. "
                            "A company with large retained earnings has been profitable for many years "
                            "and has chosen to reinvest rather than distribute its profits.\n\n"
                            "Beyond net income, accountants also calculate comprehensive income. "
                            "Comprehensive income includes net income plus other gains and losses "
                            "that are not part of regular business operations. "
                            "For example, if a Vietnamese company holds investments in foreign currencies, "
                            "changes in exchange rates can create unrealized gains or losses. "
                            "These appear in comprehensive income but not in net income. "
                            "The statement of comprehensive income gives investors a fuller picture "
                            "of all the changes in a company's financial position.\n\n"
                            "Finally, every set of financial statements includes disclosure notes. "
                            "Disclosure is the practice of providing additional information "
                            "that helps readers understand the numbers. "
                            "The notes might explain the company's accounting policies, "
                            "describe significant transactions, or reveal risks that are not obvious "
                            "from the main statements alone. "
                            "For example, a disclosure note might warn that the company "
                            "is involved in a lawsuit that could result in a large financial loss. "
                            "Without disclosure, investors would be making decisions based on incomplete information."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nguyên tắc kế toán và công bố thông tin tài chính",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Numbers on a financial statement do not appear by accident — "
                            "they follow strict accounting rules that determine when and how "
                            "transactions are recorded. Understanding these rules is essential "
                            "for anyone who wants to read financial reports with confidence.\n\n"
                            "The most important principle is accrual accounting. "
                            "Under the accrual method, revenue is recorded when it is earned, "
                            "not when cash is received. Similarly, an expense is recorded when it is incurred, "
                            "not when it is paid. For example, if a Vietnamese furniture company "
                            "delivers a shipment of tables to a hotel chain in December "
                            "but does not receive payment until February, "
                            "the revenue is recorded in December — the month the delivery happened. "
                            "This is why a company can show strong income on its statement "
                            "while having very little cash in the bank.\n\n"
                            "Another key concept is depreciation. "
                            "When a company buys a piece of equipment — say, a printing press for five billion dong — "
                            "it does not record the entire cost as an expense in the year of purchase. "
                            "Instead, the cost is spread over the useful life of the asset. "
                            "If the press is expected to last ten years, "
                            "the company records depreciation of five hundred million dong each year. "
                            "Depreciation reduces the book value of the asset on the balance sheet "
                            "and appears as an expense on the income statement, "
                            "even though no cash actually leaves the company.\n\n"
                            "Amortization works the same way but applies to intangible assets — "
                            "things you cannot touch, like patents, trademarks, and software licenses. "
                            "If a pharmaceutical company pays eight billion dong for a patent "
                            "that lasts twenty years, it records amortization of four hundred million dong annually. "
                            "Both depreciation and amortization are non-cash expenses, "
                            "meaning they reduce reported income without affecting cash flow directly.\n\n"
                            "After a company calculates its net income, "
                            "it must decide what to do with the profit. "
                            "Some of it may be distributed to shareholders as dividends. "
                            "The rest becomes retained earnings — profit that the company keeps "
                            "to reinvest in the business. Retained earnings accumulate over time "
                            "and appear in the equity section of the balance sheet. "
                            "A company with large retained earnings has been profitable for many years "
                            "and has chosen to reinvest rather than distribute its profits.\n\n"
                            "Beyond net income, accountants also calculate comprehensive income. "
                            "Comprehensive income includes net income plus other gains and losses "
                            "that are not part of regular business operations. "
                            "For example, if a Vietnamese company holds investments in foreign currencies, "
                            "changes in exchange rates can create unrealized gains or losses. "
                            "These appear in comprehensive income but not in net income. "
                            "The statement of comprehensive income gives investors a fuller picture "
                            "of all the changes in a company's financial position.\n\n"
                            "Finally, every set of financial statements includes disclosure notes. "
                            "Disclosure is the practice of providing additional information "
                            "that helps readers understand the numbers. "
                            "The notes might explain the company's accounting policies, "
                            "describe significant transactions, or reveal risks that are not obvious "
                            "from the main statements alone. "
                            "For example, a disclosure note might warn that the company "
                            "is involved in a lawsuit that could result in a large financial loss. "
                            "Without disclosure, investors would be making decisions based on incomplete information."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nguyên tắc kế toán và công bố thông tin",
                    "description": "Viết câu sử dụng 6 từ vựng về nguyên tắc kế toán.",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"],
                        "items": [
                            {
                                "targetVocab": "accrual",
                                "prompt": "Dùng từ 'accrual' để viết một câu về nguyên tắc kế toán dồn tích và cách nó ảnh hưởng đến ghi nhận doanh thu. Ví dụ: Under accrual accounting, the construction company recorded revenue of two billion dong in March even though the client did not pay until June."
                            },
                            {
                                "targetVocab": "depreciation",
                                "prompt": "Dùng từ 'depreciation' để viết một câu về việc khấu hao tài sản cố định trên báo cáo tài chính. Ví dụ: The annual depreciation of the delivery trucks reduced the company's reported profit by eight hundred million dong, even though no cash was actually spent."
                            },
                            {
                                "targetVocab": "amortization",
                                "prompt": "Dùng từ 'amortization' để viết một câu về việc phân bổ chi phí tài sản vô hình. Ví dụ: The technology firm recorded amortization of one billion dong per year on the software patent it acquired from a foreign developer."
                            },
                            {
                                "targetVocab": "retained",
                                "prompt": "Dùng từ 'retained' để viết một câu về lợi nhuận giữ lại và cách doanh nghiệp sử dụng nó. Ví dụ: The board voted to add this year's profit to retained earnings instead of paying dividends, using the funds to build a new factory in the south."
                            },
                            {
                                "targetVocab": "comprehensive",
                                "prompt": "Dùng từ 'comprehensive' để viết một câu về thu nhập toàn diện và sự khác biệt với lợi nhuận ròng. Ví dụ: The company's comprehensive income was higher than its net income because it included unrealized gains from the appreciation of its foreign currency holdings."
                            },
                            {
                                "targetVocab": "disclosure",
                                "prompt": "Dùng từ 'disclosure' để viết một câu về nghĩa vụ công bố thông tin tài chính của doanh nghiệp. Ví dụ: The disclosure notes in the annual report revealed that the company had guaranteed a loan of thirty billion dong for its subsidiary, creating a significant contingent liability."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Báo cáo tài chính. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "asset — tài sản, liability — nợ phải trả, equity — vốn chủ sở hữu, "
                            "revenue — doanh thu, expense — chi phí, và balance — cân đối. "
                            "Đây là bộ từ vựng cốt lõi trên bảng cân đối kế toán.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào báo cáo kết quả kinh doanh và dòng tiền: "
                            "income — thu nhập, statement — báo cáo, cash — tiền mặt, "
                            "flow — dòng chảy, receivable — phải thu, và payable — phải trả. "
                            "Những từ này giúp bạn hiểu doanh nghiệp kiếm tiền và chi tiền ra sao.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "accrual — dồn tích, depreciation — khấu hao, amortization — phân bổ, "
                            "retained — giữ lại, comprehensive — toàn diện, và disclosure — công bố thông tin. "
                            "Đây là những từ về nguyên tắc kế toán và nghĩa vụ minh bạch tài chính.\n\n"
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
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng báo cáo tài chính",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "asset",
                                "prompt": "Dùng từ 'asset' để viết một câu về cách phân loại tài sản trên bảng cân đối kế toán của một công ty niêm yết. Ví dụ: The technology company's most valuable asset is its portfolio of software patents, which are classified as intangible assets on the balance sheet."
                            },
                            {
                                "targetVocab": "liability",
                                "prompt": "Dùng từ 'liability' để viết một câu về tác động của nợ phải trả đối với sức khỏe tài chính doanh nghiệp. Ví dụ: The rapid increase in short-term liabilities raised concerns among investors about the company's ability to meet its financial obligations."
                            },
                            {
                                "targetVocab": "equity",
                                "prompt": "Dùng từ 'equity' để viết một câu về mối quan hệ giữa vốn chủ sở hữu và quyết định đầu tư. Ví dụ: Investors look at the return on equity ratio to determine how efficiently a company uses shareholders' money to generate profits."
                            },
                            {
                                "targetVocab": "revenue",
                                "prompt": "Dùng từ 'revenue' để viết một câu về nguồn doanh thu chính của một doanh nghiệp Việt Nam. Ví dụ: The dairy company's revenue comes primarily from domestic milk sales, which account for over seventy percent of its total income."
                            },
                            {
                                "targetVocab": "expense",
                                "prompt": "Dùng từ 'expense' để viết một câu về chiến lược cắt giảm chi phí của doanh nghiệp. Ví dụ: The new CEO reduced operating expenses by fifteen percent through automation, allowing the company to report its first profit in three years."
                            },
                            {
                                "targetVocab": "balance",
                                "prompt": "Dùng từ 'balance' để viết một câu về nguyên tắc cân đối kế toán và ý nghĩa của nó. Ví dụ: The auditor found that the balance sheet did not balance due to an unrecorded transaction of two billion dong in the accounts payable ledger."
                            },
                            {
                                "targetVocab": "income",
                                "prompt": "Dùng từ 'income' để viết một câu về xu hướng lợi nhuận của doanh nghiệp qua nhiều quý. Ví dụ: The company's net income has grown steadily for eight consecutive quarters, making it one of the most profitable firms on the Ho Chi Minh City stock exchange."
                            },
                            {
                                "targetVocab": "statement",
                                "prompt": "Dùng từ 'statement' để viết một câu về vai trò của báo cáo tài chính trong việc ra quyết định đầu tư. Ví dụ: Before investing, the analyst carefully reviewed the company's financial statements to assess its profitability, liquidity, and long-term growth potential."
                            },
                            {
                                "targetVocab": "cash",
                                "prompt": "Dùng từ 'cash' để viết một câu về tầm quan trọng của dự trữ tiền mặt trong thời kỳ khó khăn. Ví dụ: Companies with strong cash reserves were better able to survive the economic downturn because they could continue paying employees and suppliers without borrowing."
                            },
                            {
                                "targetVocab": "flow",
                                "prompt": "Dùng từ 'flow' để viết một câu về sự khác biệt giữa dòng tiền và lợi nhuận. Ví dụ: The company reported positive net income but negative operating cash flow, which meant it was earning profits on paper but not collecting enough money from customers."
                            },
                            {
                                "targetVocab": "receivable",
                                "prompt": "Dùng từ 'receivable' để viết một câu về rủi ro khi khoản phải thu quá lớn. Ví dụ: The sharp rise in accounts receivable worried the CFO because it meant customers were taking longer to pay, putting pressure on the company's cash position."
                            },
                            {
                                "targetVocab": "payable",
                                "prompt": "Dùng từ 'payable' để viết một câu về cách doanh nghiệp quản lý khoản phải trả. Ví dụ: The company extended its accounts payable cycle from thirty to sixty days, giving it more time to collect money from customers before paying suppliers."
                            },
                            {
                                "targetVocab": "accrual",
                                "prompt": "Dùng từ 'accrual' để viết một câu về sự khác biệt giữa kế toán dồn tích và kế toán tiền mặt. Ví dụ: The switch from cash-basis to accrual accounting changed the way the company reported revenue, making its financial statements more comparable to international standards."
                            },
                            {
                                "targetVocab": "depreciation",
                                "prompt": "Dùng từ 'depreciation' để viết một câu về tác động của khấu hao đối với giá trị tài sản trên sổ sách. Ví dụ: After five years of depreciation, the original factory equipment that cost ten billion dong was recorded at only half its purchase price on the balance sheet."
                            },
                            {
                                "targetVocab": "amortization",
                                "prompt": "Dùng từ 'amortization' để viết một câu về phân bổ chi phí tài sản vô hình trong ngành công nghệ. Ví dụ: The gaming company recorded amortization of three billion dong on the intellectual property rights it purchased from a Japanese studio two years ago."
                            },
                            {
                                "targetVocab": "retained",
                                "prompt": "Dùng từ 'retained' để viết một câu về quyết định giữ lại lợi nhuận thay vì chia cổ tức. Ví dụ: The startup's retained earnings reached fifty billion dong after five years of reinvesting all profits into product development and market expansion."
                            },
                            {
                                "targetVocab": "comprehensive",
                                "prompt": "Dùng từ 'comprehensive' để viết một câu về thu nhập toàn diện và các khoản lãi lỗ chưa thực hiện. Ví dụ: The bank's comprehensive income was significantly lower than its net income because of large unrealized losses on its bond portfolio caused by rising interest rates."
                            },
                            {
                                "targetVocab": "disclosure",
                                "prompt": "Dùng từ 'disclosure' để viết một câu về tầm quan trọng của công bố thông tin đối với nhà đầu tư. Ví dụ: The lack of adequate disclosure about the company's related-party transactions led the stock exchange to issue a formal warning and demand a detailed explanation."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về báo cáo tài chính.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về báo cáo tài chính — từ bảng cân đối kế toán, "
                            "báo cáo kết quả kinh doanh, đến dòng tiền và nguyên tắc kế toán.\n\n"
                            "Bạn sẽ gặp lại asset, liability, equity, revenue, expense, balance "
                            "trong phần mở đầu về nền tảng của hệ thống báo cáo tài chính. "
                            "Tiếp theo, income, statement, cash, flow, receivable, payable "
                            "sẽ giúp bạn hiểu cách đọc báo cáo kết quả kinh doanh và lưu chuyển tiền tệ. "
                            "Và cuối cùng, accrual, depreciation, amortization, retained, comprehensive, disclosure "
                            "sẽ đưa bạn vào thế giới nguyên tắc kế toán và minh bạch tài chính.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Báo cáo tài chính — Bức tranh toàn cảnh",
                    "description": "Imagine you are an investor considering whether to buy shares in a Vietnamese company listed on the Ho Chi Minh City stock exchange.",
                    "data": {
                        "text": (
                            "Imagine you are an investor considering whether to buy shares "
                            "in a Vietnamese company listed on the Ho Chi Minh City stock exchange. "
                            "The company makes consumer electronics and has been growing rapidly. "
                            "But before you invest a single dong, you need to understand "
                            "the company's financial health. The only way to do that "
                            "is to read its financial statements.\n\n"
                            "You start with the balance sheet. "
                            "The balance sheet is a snapshot of the company's financial position "
                            "at the end of the most recent quarter. "
                            "On the left side, you see the company's assets — "
                            "everything it owns that has economic value. "
                            "Current assets include cash in the bank, inventory in warehouses, "
                            "and accounts receivable from customers who have bought products on credit. "
                            "Non-current assets include the factory buildings, production equipment, "
                            "and patents on proprietary technology.\n\n"
                            "On the right side of the balance sheet are liabilities and equity. "
                            "A liability is money the company owes — "
                            "short-term loans from banks, accounts payable to suppliers, "
                            "and long-term bonds issued to raise capital. "
                            "Equity is what remains after subtracting all liabilities from total assets. "
                            "It represents the shareholders' ownership stake in the company. "
                            "The fundamental equation holds: assets equal liabilities plus equity. "
                            "If the numbers do not balance, something is wrong.\n\n"
                            "Next, you turn to the income statement. "
                            "This statement covers a period of time — usually a quarter or a full year — "
                            "and shows whether the company made money. "
                            "At the top is revenue, the total amount earned from selling electronics. "
                            "Below that are expenses: the cost of components, factory workers' salaries, "
                            "marketing campaigns, and administrative overhead. "
                            "After subtracting all expenses from revenue, you arrive at net income — "
                            "the company's bottom line. A positive income means profit; "
                            "a negative income means loss.\n\n"
                            "But you know that income can be misleading. "
                            "A company might report strong revenue and healthy income "
                            "while struggling with cash. "
                            "So you check the cash flow statement. "
                            "This statement tracks the actual flow of money "
                            "into and out of the business. "
                            "Operating cash flow tells you whether the company's core business "
                            "generates enough cash to sustain itself. "
                            "You notice that accounts receivable has grown significantly — "
                            "customers owe the company a lot of money that has not yet been collected. "
                            "At the same time, accounts payable is relatively low, "
                            "meaning the company is paying its suppliers quickly. "
                            "This combination explains why cash flow is weaker than income.\n\n"
                            "You also notice that the company uses accrual accounting, "
                            "as required by Vietnamese and international standards. "
                            "Under the accrual method, revenue is recorded when goods are delivered, "
                            "not when payment is received. "
                            "This means the income statement can show strong sales "
                            "even if much of the money is still sitting in receivable accounts.\n\n"
                            "Looking deeper, you find two significant non-cash expenses. "
                            "Depreciation of eight billion dong reflects the gradual wear "
                            "on the company's factory equipment over the year. "
                            "Amortization of two billion dong covers the declining value "
                            "of software licenses and patents. "
                            "Neither depreciation nor amortization involves actual cash leaving the company, "
                            "but both reduce reported income and the book value of assets.\n\n"
                            "In the equity section, you see retained earnings of sixty billion dong. "
                            "This tells you that over the years, the company has chosen to keep "
                            "a large portion of its profits rather than distribute them as dividends. "
                            "High retained earnings suggest that management is focused on growth "
                            "and reinvestment.\n\n"
                            "You also review the statement of comprehensive income. "
                            "Comprehensive income includes net income plus other items "
                            "that affect the company's value but are not part of regular operations. "
                            "This quarter, the company recorded an unrealized loss "
                            "on its foreign currency holdings because the dong strengthened against the dollar. "
                            "This loss appears in comprehensive income but not in net income.\n\n"
                            "Finally, you read the disclosure notes at the end of the report. "
                            "Disclosure is where the company explains the details behind the numbers. "
                            "One note reveals that the company is involved in a patent dispute "
                            "that could cost up to twenty billion dong if it loses. "
                            "Another note explains the depreciation method used for each category of asset. "
                            "Without these disclosures, you would be making investment decisions "
                            "based on incomplete information.\n\n"
                            "After reading all the statements, you have a clear picture. "
                            "The company is profitable, growing, and reinvesting in its future. "
                            "But its cash position needs watching, "
                            "and the pending lawsuit is a risk worth monitoring. "
                            "This is the power of financial statements — "
                            "they give you the language to understand any company's story, "
                            "no matter where in the world it operates."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Báo cáo tài chính — Bức tranh toàn cảnh",
                    "description": "Imagine you are an investor considering whether to buy shares in a Vietnamese company listed on the Ho Chi Minh City stock exchange.",
                    "data": {
                        "text": (
                            "Imagine you are an investor considering whether to buy shares "
                            "in a Vietnamese company listed on the Ho Chi Minh City stock exchange. "
                            "The company makes consumer electronics and has been growing rapidly. "
                            "But before you invest a single dong, you need to understand "
                            "the company's financial health. The only way to do that "
                            "is to read its financial statements.\n\n"
                            "You start with the balance sheet. "
                            "The balance sheet is a snapshot of the company's financial position "
                            "at the end of the most recent quarter. "
                            "On the left side, you see the company's assets — "
                            "everything it owns that has economic value. "
                            "Current assets include cash in the bank, inventory in warehouses, "
                            "and accounts receivable from customers who have bought products on credit. "
                            "Non-current assets include the factory buildings, production equipment, "
                            "and patents on proprietary technology.\n\n"
                            "On the right side of the balance sheet are liabilities and equity. "
                            "A liability is money the company owes — "
                            "short-term loans from banks, accounts payable to suppliers, "
                            "and long-term bonds issued to raise capital. "
                            "Equity is what remains after subtracting all liabilities from total assets. "
                            "It represents the shareholders' ownership stake in the company. "
                            "The fundamental equation holds: assets equal liabilities plus equity. "
                            "If the numbers do not balance, something is wrong.\n\n"
                            "Next, you turn to the income statement. "
                            "This statement covers a period of time — usually a quarter or a full year — "
                            "and shows whether the company made money. "
                            "At the top is revenue, the total amount earned from selling electronics. "
                            "Below that are expenses: the cost of components, factory workers' salaries, "
                            "marketing campaigns, and administrative overhead. "
                            "After subtracting all expenses from revenue, you arrive at net income — "
                            "the company's bottom line. A positive income means profit; "
                            "a negative income means loss.\n\n"
                            "But you know that income can be misleading. "
                            "A company might report strong revenue and healthy income "
                            "while struggling with cash. "
                            "So you check the cash flow statement. "
                            "This statement tracks the actual flow of money "
                            "into and out of the business. "
                            "Operating cash flow tells you whether the company's core business "
                            "generates enough cash to sustain itself. "
                            "You notice that accounts receivable has grown significantly — "
                            "customers owe the company a lot of money that has not yet been collected. "
                            "At the same time, accounts payable is relatively low, "
                            "meaning the company is paying its suppliers quickly. "
                            "This combination explains why cash flow is weaker than income.\n\n"
                            "You also notice that the company uses accrual accounting, "
                            "as required by Vietnamese and international standards. "
                            "Under the accrual method, revenue is recorded when goods are delivered, "
                            "not when payment is received. "
                            "This means the income statement can show strong sales "
                            "even if much of the money is still sitting in receivable accounts.\n\n"
                            "Looking deeper, you find two significant non-cash expenses. "
                            "Depreciation of eight billion dong reflects the gradual wear "
                            "on the company's factory equipment over the year. "
                            "Amortization of two billion dong covers the declining value "
                            "of software licenses and patents. "
                            "Neither depreciation nor amortization involves actual cash leaving the company, "
                            "but both reduce reported income and the book value of assets.\n\n"
                            "In the equity section, you see retained earnings of sixty billion dong. "
                            "This tells you that over the years, the company has chosen to keep "
                            "a large portion of its profits rather than distribute them as dividends. "
                            "High retained earnings suggest that management is focused on growth "
                            "and reinvestment.\n\n"
                            "You also review the statement of comprehensive income. "
                            "Comprehensive income includes net income plus other items "
                            "that affect the company's value but are not part of regular operations. "
                            "This quarter, the company recorded an unrealized loss "
                            "on its foreign currency holdings because the dong strengthened against the dollar. "
                            "This loss appears in comprehensive income but not in net income.\n\n"
                            "Finally, you read the disclosure notes at the end of the report. "
                            "Disclosure is where the company explains the details behind the numbers. "
                            "One note reveals that the company is involved in a patent dispute "
                            "that could cost up to twenty billion dong if it loses. "
                            "Another note explains the depreciation method used for each category of asset. "
                            "Without these disclosures, you would be making investment decisions "
                            "based on incomplete information.\n\n"
                            "After reading all the statements, you have a clear picture. "
                            "The company is profitable, growing, and reinvesting in its future. "
                            "But its cash position needs watching, "
                            "and the pending lawsuit is a risk worth monitoring. "
                            "This is the power of financial statements — "
                            "they give you the language to understand any company's story, "
                            "no matter where in the world it operates."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Báo cáo tài chính — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine you are an investor considering whether to buy shares "
                            "in a Vietnamese company listed on the Ho Chi Minh City stock exchange. "
                            "The company makes consumer electronics and has been growing rapidly. "
                            "But before you invest a single dong, you need to understand "
                            "the company's financial health. The only way to do that "
                            "is to read its financial statements.\n\n"
                            "You start with the balance sheet. "
                            "The balance sheet is a snapshot of the company's financial position "
                            "at the end of the most recent quarter. "
                            "On the left side, you see the company's assets — "
                            "everything it owns that has economic value. "
                            "Current assets include cash in the bank, inventory in warehouses, "
                            "and accounts receivable from customers who have bought products on credit. "
                            "Non-current assets include the factory buildings, production equipment, "
                            "and patents on proprietary technology.\n\n"
                            "On the right side of the balance sheet are liabilities and equity. "
                            "A liability is money the company owes — "
                            "short-term loans from banks, accounts payable to suppliers, "
                            "and long-term bonds issued to raise capital. "
                            "Equity is what remains after subtracting all liabilities from total assets. "
                            "It represents the shareholders' ownership stake in the company. "
                            "The fundamental equation holds: assets equal liabilities plus equity. "
                            "If the numbers do not balance, something is wrong.\n\n"
                            "Next, you turn to the income statement. "
                            "This statement covers a period of time — usually a quarter or a full year — "
                            "and shows whether the company made money. "
                            "At the top is revenue, the total amount earned from selling electronics. "
                            "Below that are expenses: the cost of components, factory workers' salaries, "
                            "marketing campaigns, and administrative overhead. "
                            "After subtracting all expenses from revenue, you arrive at net income — "
                            "the company's bottom line. A positive income means profit; "
                            "a negative income means loss.\n\n"
                            "But you know that income can be misleading. "
                            "A company might report strong revenue and healthy income "
                            "while struggling with cash. "
                            "So you check the cash flow statement. "
                            "This statement tracks the actual flow of money "
                            "into and out of the business. "
                            "Operating cash flow tells you whether the company's core business "
                            "generates enough cash to sustain itself. "
                            "You notice that accounts receivable has grown significantly — "
                            "customers owe the company a lot of money that has not yet been collected. "
                            "At the same time, accounts payable is relatively low, "
                            "meaning the company is paying its suppliers quickly. "
                            "This combination explains why cash flow is weaker than income.\n\n"
                            "You also notice that the company uses accrual accounting, "
                            "as required by Vietnamese and international standards. "
                            "Under the accrual method, revenue is recorded when goods are delivered, "
                            "not when payment is received. "
                            "This means the income statement can show strong sales "
                            "even if much of the money is still sitting in receivable accounts.\n\n"
                            "Looking deeper, you find two significant non-cash expenses. "
                            "Depreciation of eight billion dong reflects the gradual wear "
                            "on the company's factory equipment over the year. "
                            "Amortization of two billion dong covers the declining value "
                            "of software licenses and patents. "
                            "Neither depreciation nor amortization involves actual cash leaving the company, "
                            "but both reduce reported income and the book value of assets.\n\n"
                            "In the equity section, you see retained earnings of sixty billion dong. "
                            "This tells you that over the years, the company has chosen to keep "
                            "a large portion of its profits rather than distribute them as dividends. "
                            "High retained earnings suggest that management is focused on growth "
                            "and reinvestment.\n\n"
                            "You also review the statement of comprehensive income. "
                            "Comprehensive income includes net income plus other items "
                            "that affect the company's value but are not part of regular operations. "
                            "This quarter, the company recorded an unrealized loss "
                            "on its foreign currency holdings because the dong strengthened against the dollar. "
                            "This loss appears in comprehensive income but not in net income.\n\n"
                            "Finally, you read the disclosure notes at the end of the report. "
                            "Disclosure is where the company explains the details behind the numbers. "
                            "One note reveals that the company is involved in a patent dispute "
                            "that could cost up to twenty billion dong if it loses. "
                            "Another note explains the depreciation method used for each category of asset. "
                            "Without these disclosures, you would be making investment decisions "
                            "based on incomplete information.\n\n"
                            "After reading all the statements, you have a clear picture. "
                            "The company is profitable, growing, and reinvesting in its future. "
                            "But its cash position needs watching, "
                            "and the pending lawsuit is a risk worth monitoring. "
                            "This is the power of financial statements — "
                            "they give you the language to understand any company's story, "
                            "no matter where in the world it operates."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích báo cáo tài chính doanh nghiệp",
                    "description": "Viết đoạn văn tiếng Anh phân tích báo cáo tài chính sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của báo cáo tài chính doanh nghiệp. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích bảng cân đối kế toán của một công ty sản xuất Việt Nam. Giải thích mối quan hệ giữa asset, liability và equity, vai trò của depreciation trong việc giảm giá trị tài sản, và cách retained earnings phản ánh chiến lược tái đầu tư của doanh nghiệp.",
                            "Hãy giải thích vì sao một doanh nghiệp có thể báo cáo income cao nhưng lại thiếu cash. Phân tích vai trò của accrual accounting, tác động của receivable và payable đối với cash flow, và tầm quan trọng của disclosure trong việc giúp nhà đầu tư hiểu đúng tình hình tài chính."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần chiêm nghiệm.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Báo cáo tài chính. "
                            "Hãy dừng lại một chút và cảm nhận điều này: "
                            "bạn vừa học được ngôn ngữ mà mọi doanh nghiệp trên thế giới "
                            "dùng để kể câu chuyện tài chính của mình. "
                            "Đó không chỉ là 18 từ vựng — đó là một cách nhìn mới.\n\n"
                            "Equity — vốn chủ sở hữu. Từ này nghe đơn giản, "
                            "nhưng nó chứa đựng toàn bộ câu chuyện về quyền sở hữu trong doanh nghiệp. "
                            "Khi bạn nhìn vào equity trên bảng cân đối kế toán, "
                            "bạn đang nhìn vào phần giá trị thực sự thuộc về những người đã tin tưởng đầu tư. "
                            "Ví dụ mới: The company's equity doubled in five years "
                            "because management consistently reinvested profits into expanding production capacity "
                            "rather than paying large dividends.\n\n"
                            "Cash — tiền mặt. Trong kế toán, cash là sự thật không thể che giấu. "
                            "Lợi nhuận có thể được điều chỉnh, doanh thu có thể được ghi nhận sớm, "
                            "nhưng tiền mặt trong tài khoản ngân hàng thì không nói dối. "
                            "Ví dụ mới: The analyst warned that despite impressive revenue growth, "
                            "the company's cash position had deteriorated because it was extending "
                            "increasingly generous credit terms to attract new customers.\n\n"
                            "Depreciation — khấu hao. Đây là từ mà nhiều sinh viên kế toán "
                            "thấy trừu tượng lúc đầu, nhưng nó phản ánh một sự thật sâu sắc: "
                            "mọi thứ đều mất giá trị theo thời gian. Máy móc hao mòn, công nghệ lỗi thời, "
                            "tòa nhà xuống cấp — depreciation ghi nhận sự mất mát đó trên sổ sách. "
                            "Ví dụ mới: The airline recorded depreciation of over one trillion dong "
                            "on its fleet of aircraft, reflecting the reality that even the newest planes "
                            "lose value with every flight they make.\n\n"
                            "Accrual — dồn tích. Nguyên tắc này là trái tim của kế toán hiện đại. "
                            "Nó nói rằng: hãy ghi nhận sự thật kinh tế khi nó xảy ra, "
                            "không phải khi tiền đổi tay. Hiểu accrual, bạn hiểu vì sao "
                            "lợi nhuận và dòng tiền có thể kể hai câu chuyện khác nhau. "
                            "Ví dụ mới: Under accrual accounting, the construction firm recognized revenue "
                            "of twelve billion dong for work completed in December, "
                            "even though the client's payment would not arrive until March.\n\n"
                            "Disclosure — công bố thông tin. Đây có lẽ là từ quan trọng nhất "
                            "mà bạn học hôm nay, vì nó đại diện cho sự minh bạch — "
                            "giá trị cốt lõi của mọi hệ thống tài chính lành mạnh. "
                            "Không có disclosure, những con số trên báo cáo chỉ là vỏ bọc. "
                            "Với disclosure, chúng trở thành câu chuyện đầy đủ. "
                            "Ví dụ mới: The company's disclosure notes revealed that its CEO "
                            "had a personal financial interest in one of its major suppliers, "
                            "a fact that would have been invisible without proper reporting requirements.\n\n"
                            "Retained — giữ lại. Mỗi đồng lợi nhuận giữ lại "
                            "là một lời hứa về tương lai — rằng doanh nghiệp tin vào chính mình "
                            "đủ để tái đầu tư thay vì chia hết cho cổ đông. "
                            "Ví dụ mới: The tech startup's retained earnings of eighty billion dong "
                            "funded the development of three new product lines "
                            "without the company needing to borrow a single dong from the bank.\n\n"
                            "Bạn biết không, có một điều kỳ diệu về báo cáo tài chính: "
                            "chúng là ngôn ngữ chung của thế giới kinh doanh. "
                            "Một bảng cân đối kế toán ở Hà Nội tuân theo cùng logic "
                            "với một bảng cân đối kế toán ở New York hay Tokyo. "
                            "Và bây giờ, bạn đã có chìa khóa để đọc tất cả.\n\n"
                            "Hãy mang theo 18 từ vựng này như một bộ kính mới — "
                            "lần tới khi bạn mở báo cáo thường niên của một doanh nghiệp, "
                            "bạn sẽ thấy không chỉ những con số, mà cả câu chuyện đằng sau chúng. "
                            "Chúc bạn tiếp tục hành trình khám phá thế giới kế toán tài chính — "
                            "hẹn gặp lại ở bài học tiếp theo."
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Financial Statements – Báo Cáo Tài Chính' AND uid = '{UID}' ORDER BY created_at;")
