import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Series D, Curriculum 1: Financial Statements – Báo Cáo Tài Chính
# Description tone: surprising_fact
# Farewell tone: quiet awe
# W1: asset, liability, equity, revenue, expense, balance
# W2: income, statement, cash, flow, receivable, payable
# W3: accrual, depreciation, amortization, retained, comprehensive, disclosure

content = {
    "title": "Financial Statements – Báo Cáo Tài Chính",
    "contentTypeTags": [],
    "description": "93% DOANH NGHIỆP VIỆT NAM GỌI VỐN NƯỚC NGOÀI THẤT BẠI — VÌ KHÔNG ĐỌC ĐƯỢC BÁO CÁO TÀI CHÍNH BẰNG TIẾNG ANH.\n\nBạn học kế toán bằng tiếng Việt, bạn hiểu bảng cân đối kế toán, báo cáo kết quả kinh doanh, báo cáo lưu chuyển tiền tệ. Nhưng khi một quỹ đầu tư Singapore gửi cho bạn bản financial statements và hỏi 'What's your retained earnings trend?' — bạn đứng hình. Không phải vì bạn không biết kế toán, mà vì bạn không biết nói kế toán bằng tiếng Anh.\n\nHãy nghĩ về báo cáo tài chính như tấm gương phản chiếu sức khỏe doanh nghiệp — mỗi con số là một nhịp tim, mỗi dòng là một mạch máu. Nếu bạn không đọc được tấm gương đó bằng ngôn ngữ quốc tế, bạn sẽ mãi là người đứng ngoài cuộc chơi tài chính toàn cầu.\n\n18 từ vựng trong bài học này — từ asset đến disclosure — sẽ giúp bạn tự tin đọc hiểu báo cáo tài chính bằng tiếng Anh, thảo luận với đối tác quốc tế, và mở ra cánh cửa sự nghiệp mà trước đây bạn chỉ nhìn qua khe hở.\n\nTừ balance sheet đến comprehensive income — bạn vừa nâng cấp tư duy tài chính, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc.",
    "preview": {
        "text": "Khám phá 18 từ vựng tiếng Anh cốt lõi về báo cáo tài chính — ngôn ngữ mà mọi kế toán viên, nhà phân tích và nhà đầu tư trên thế giới đều sử dụng. Bạn sẽ bắt đầu với asset, liability, equity, revenue, expense, balance — bộ từ nền tảng giúp bạn đọc hiểu bảng cân đối kế toán và báo cáo kết quả kinh doanh. Tiếp theo là income, statement, cash, flow, receivable, payable — những từ giúp bạn hiểu dòng tiền ra vào doanh nghiệp và các khoản phải thu, phải trả. Cuối cùng, accrual, depreciation, amortization, retained, comprehensive, disclosure đưa bạn vào thế giới kế toán dồn tích, khấu hao tài sản, và công bố thông tin tài chính. Qua 3 bài đọc tiếng Anh về báo cáo tài chính thực tế, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, bạn sẽ tự tin đọc hiểu financial statements bằng tiếng Anh mà không cần dừng lại tra từ."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Chào mừng bạn đến với bài học về báo cáo tài chính — ngôn ngữ chung của thế giới tài chính.",
                    "data": {
                        "text": "Chào mừng bạn đến với bài học đầu tiên trong chuỗi từ vựng Kế toán và Tài chính doanh nghiệp — chủ đề hôm nay là Báo cáo tài chính, hay trong tiếng Anh là Financial Statements. Nếu bạn đang học kế toán hoặc tài chính tại trường đại học, bạn đã biết rằng báo cáo tài chính là tấm gương phản chiếu toàn bộ sức khỏe của một doanh nghiệp. Nhưng khi bạn bước ra thế giới — khi đối tác là người Singapore, khi nhà đầu tư là người Mỹ, khi báo cáo kiểm toán viết bằng tiếng Anh — bạn cần nắm vững ngôn ngữ tài chính quốc tế.\n\nTrong phần này, bạn sẽ học 6 từ vựng: asset, liability, equity, revenue, expense, và balance. Đây là những từ xuất hiện trên mọi bảng cân đối kế toán và báo cáo kết quả kinh doanh trên thế giới.\n\nTừ đầu tiên là asset — danh từ — nghĩa là tài sản. Asset là bất kỳ nguồn lực nào mà doanh nghiệp sở hữu và có giá trị kinh tế — từ tiền mặt, nhà xưởng, máy móc đến bằng sáng chế và thương hiệu. Ví dụ: 'The company's total assets grew by twelve percent last year, driven by new factory investments and increased cash reserves.' Trong bài đọc, asset là điểm khởi đầu của bảng cân đối kế toán — mọi thứ doanh nghiệp có đều nằm ở đây.\n\nTừ thứ hai là liability — danh từ — nghĩa là nợ phải trả, nghĩa vụ tài chính. Liability là tất cả những gì doanh nghiệp nợ — từ khoản vay ngân hàng, tiền lương chưa trả đến thuế phải nộp. Ví dụ: 'Short-term liabilities such as accounts payable and accrued wages must be settled within one year.' Trong bài đọc, liability đứng đối diện với asset trên bảng cân đối kế toán — tổng tài sản luôn bằng tổng nợ cộng vốn chủ sở hữu.\n\nTừ thứ ba là equity — danh từ — nghĩa là vốn chủ sở hữu. Equity là phần giá trị còn lại của doanh nghiệp sau khi trừ đi tất cả các khoản nợ. Nói đơn giản: Equity = Assets - Liabilities. Ví dụ: 'Shareholders' equity represents the owners' residual claim on the company's assets after all debts have been paid.' Trong bài đọc, equity là thước đo giá trị thực sự mà cổ đông sở hữu trong doanh nghiệp.\n\nTừ thứ tư là revenue — danh từ — nghĩa là doanh thu. Revenue là tổng số tiền doanh nghiệp kiếm được từ hoạt động kinh doanh chính — bán hàng, cung cấp dịch vụ — trước khi trừ bất kỳ chi phí nào. Ví dụ: 'Apple reported quarterly revenue of over ninety billion dollars, with iPhone sales accounting for more than half of the total.' Trong bài đọc, revenue là dòng đầu tiên trên báo cáo kết quả kinh doanh — vì thế người ta gọi nó là 'top line.'\n\nTừ thứ năm là expense — danh từ — nghĩa là chi phí. Expense là tất cả các khoản chi mà doanh nghiệp phải bỏ ra để vận hành — từ tiền thuê mặt bằng, lương nhân viên đến chi phí nguyên vật liệu. Ví dụ: 'Operating expenses include rent, salaries, utilities, and marketing costs — everything the company spends to keep the business running.' Trong bài đọc, expense là đối trọng của revenue — doanh thu trừ chi phí cho ra lợi nhuận.\n\nTừ cuối cùng là balance — danh từ — nghĩa là số dư, cân đối. Trong kế toán, balance sheet là bảng cân đối kế toán — báo cáo cho thấy tài sản, nợ và vốn chủ sở hữu tại một thời điểm cụ thể. Ví dụ: 'The balance sheet must always balance — total assets on one side must equal total liabilities plus equity on the other.' Trong bài đọc, balance nhấn mạnh nguyên tắc cốt lõi của kế toán: mọi thứ phải cân đối.\n\nBạn đã có 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, sau đó đọc bài viết về cách đọc hiểu bảng cân đối kế toán và báo cáo kết quả kinh doanh nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng báo cáo tài chính",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng báo cáo tài chính",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng báo cáo tài chính",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng báo cáo tài chính",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nền tảng báo cáo tài chính",
                    "description": "Học 6 từ: asset, liability, equity, revenue, expense, balance",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Bảng cân đối kế toán và báo cáo kết quả kinh doanh",
                    "description": "If you want to understand a company, start with its financial statements.",
                    "data": {
                        "text": "If you want to understand a company, start with its financial statements. These documents tell the story of a business — how much it owns, how much it owes, how much it earns, and how much it spends. For investors, lenders, and managers, financial statements are the most important source of information about a company's health.\n\nThe most fundamental financial statement is the balance sheet. It provides a snapshot of a company's financial position at a specific point in time. The balance sheet is built on a simple equation: Assets = Liabilities + Equity. This equation must always hold true. If a company has one hundred million dollars in assets, and it owes sixty million in liabilities, then its equity — the value belonging to the owners — is forty million.\n\nAn asset is anything of value that a company owns or controls. Assets are divided into two categories. Current assets are things that can be converted to cash within one year, such as cash itself, inventory, and money owed by customers. Non-current assets are long-term resources like buildings, machinery, and patents. A manufacturing company might have factories and equipment as its largest assets, while a technology company might list intellectual property and software.\n\nA liability is a financial obligation — something the company owes to others. Like assets, liabilities are classified as current or non-current. Current liabilities include short-term debts, wages owed to employees, and taxes due within the year. Non-current liabilities include long-term bank loans and bonds that mature in five or ten years. A company with too many liabilities relative to its assets may struggle to pay its debts.\n\nEquity represents the owners' stake in the company. It is what remains after subtracting all liabilities from all assets. For a publicly traded company, equity belongs to the shareholders. When a company earns profits and keeps them instead of paying dividends, those retained profits increase equity over time.\n\nThe second major financial statement is the income statement, also called the profit and loss statement. While the balance sheet shows a snapshot at one moment, the income statement shows performance over a period — usually a quarter or a year. It starts with revenue at the top and subtracts expenses to arrive at net income at the bottom.\n\nRevenue is the total amount of money a company earns from its core business activities. A retail company earns revenue from selling products. A consulting firm earns revenue from providing services. Revenue is sometimes called the top line because it appears at the top of the income statement.\n\nExpense is the cost of doing business. Operating expenses include rent, salaries, utilities, raw materials, and marketing. There are also non-operating expenses like interest payments on loans. The difference between revenue and total expenses determines whether the company made a profit or a loss.\n\nThe balance between assets and liabilities, between revenue and expenses — this is the language of accounting. Every business decision ultimately shows up in these numbers. Learning to read them in English opens the door to understanding companies anywhere in the world."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Bảng cân đối kế toán và báo cáo kết quả kinh doanh",
                    "description": "If you want to understand a company, start with its financial statements.",
                    "data": {
                        "text": "If you want to understand a company, start with its financial statements. These documents tell the story of a business — how much it owns, how much it owes, how much it earns, and how much it spends. For investors, lenders, and managers, financial statements are the most important source of information about a company's health.\n\nThe most fundamental financial statement is the balance sheet. It provides a snapshot of a company's financial position at a specific point in time. The balance sheet is built on a simple equation: Assets = Liabilities + Equity. This equation must always hold true. If a company has one hundred million dollars in assets, and it owes sixty million in liabilities, then its equity — the value belonging to the owners — is forty million.\n\nAn asset is anything of value that a company owns or controls. Assets are divided into two categories. Current assets are things that can be converted to cash within one year, such as cash itself, inventory, and money owed by customers. Non-current assets are long-term resources like buildings, machinery, and patents. A manufacturing company might have factories and equipment as its largest assets, while a technology company might list intellectual property and software.\n\nA liability is a financial obligation — something the company owes to others. Like assets, liabilities are classified as current or non-current. Current liabilities include short-term debts, wages owed to employees, and taxes due within the year. Non-current liabilities include long-term bank loans and bonds that mature in five or ten years. A company with too many liabilities relative to its assets may struggle to pay its debts.\n\nEquity represents the owners' stake in the company. It is what remains after subtracting all liabilities from all assets. For a publicly traded company, equity belongs to the shareholders. When a company earns profits and keeps them instead of paying dividends, those retained profits increase equity over time.\n\nThe second major financial statement is the income statement, also called the profit and loss statement. While the balance sheet shows a snapshot at one moment, the income statement shows performance over a period — usually a quarter or a year. It starts with revenue at the top and subtracts expenses to arrive at net income at the bottom.\n\nRevenue is the total amount of money a company earns from its core business activities. A retail company earns revenue from selling products. A consulting firm earns revenue from providing services. Revenue is sometimes called the top line because it appears at the top of the income statement.\n\nExpense is the cost of doing business. Operating expenses include rent, salaries, utilities, raw materials, and marketing. There are also non-operating expenses like interest payments on loans. The difference between revenue and total expenses determines whether the company made a profit or a loss.\n\nThe balance between assets and liabilities, between revenue and expenses — this is the language of accounting. Every business decision ultimately shows up in these numbers. Learning to read them in English opens the door to understanding companies anywhere in the world."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Bảng cân đối kế toán và báo cáo kết quả kinh doanh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "If you want to understand a company, start with its financial statements. These documents tell the story of a business — how much it owns, how much it owes, how much it earns, and how much it spends. For investors, lenders, and managers, financial statements are the most important source of information about a company's health.\n\nThe most fundamental financial statement is the balance sheet. It provides a snapshot of a company's financial position at a specific point in time. The balance sheet is built on a simple equation: Assets = Liabilities + Equity. This equation must always hold true. If a company has one hundred million dollars in assets, and it owes sixty million in liabilities, then its equity — the value belonging to the owners — is forty million.\n\nAn asset is anything of value that a company owns or controls. Assets are divided into two categories. Current assets are things that can be converted to cash within one year, such as cash itself, inventory, and money owed by customers. Non-current assets are long-term resources like buildings, machinery, and patents. A manufacturing company might have factories and equipment as its largest assets, while a technology company might list intellectual property and software.\n\nA liability is a financial obligation — something the company owes to others. Like assets, liabilities are classified as current or non-current. Current liabilities include short-term debts, wages owed to employees, and taxes due within the year. Non-current liabilities include long-term bank loans and bonds that mature in five or ten years. A company with too many liabilities relative to its assets may struggle to pay its debts.\n\nEquity represents the owners' stake in the company. It is what remains after subtracting all liabilities from all assets. For a publicly traded company, equity belongs to the shareholders. When a company earns profits and keeps them instead of paying dividends, those retained profits increase equity over time.\n\nThe second major financial statement is the income statement, also called the profit and loss statement. While the balance sheet shows a snapshot at one moment, the income statement shows performance over a period — usually a quarter or a year. It starts with revenue at the top and subtracts expenses to arrive at net income at the bottom.\n\nRevenue is the total amount of money a company earns from its core business activities. A retail company earns revenue from selling products. A consulting firm earns revenue from providing services. Revenue is sometimes called the top line because it appears at the top of the income statement.\n\nExpense is the cost of doing business. Operating expenses include rent, salaries, utilities, raw materials, and marketing. There are also non-operating expenses like interest payments on loans. The difference between revenue and total expenses determines whether the company made a profit or a loss.\n\nThe balance between assets and liabilities, between revenue and expenses — this is the language of accounting. Every business decision ultimately shows up in these numbers. Learning to read them in English opens the door to understanding companies anywhere in the world."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng báo cáo tài chính",
                    "description": "Viết câu sử dụng 6 từ vựng về nền tảng báo cáo tài chính.",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'asset' để viết một câu về tài sản của doanh nghiệp và cách phân loại chúng. Ví dụ: The company classified its new headquarters as a non-current asset on the balance sheet because the building would serve the business for at least twenty years.",
                                "targetVocab": "asset"
                            },
                            {
                                "prompt": "Dùng từ 'liability' để viết một câu về nghĩa vụ tài chính mà doanh nghiệp phải thanh toán. Ví dụ: The bank loan of five million dollars appeared as a long-term liability on the company's balance sheet, with repayment scheduled over the next ten years.",
                                "targetVocab": "liability"
                            },
                            {
                                "prompt": "Dùng từ 'equity' để viết một câu về vốn chủ sở hữu và mối quan hệ với tài sản và nợ. Ví dụ: After paying off all its debts, the startup's equity stood at two million dollars, reflecting the true value that belonged to the founders and early investors.",
                                "targetVocab": "equity"
                            },
                            {
                                "prompt": "Dùng từ 'revenue' để viết một câu về doanh thu của một công ty và nguồn gốc của nó. Ví dụ: The restaurant chain reported a fifteen percent increase in revenue after expanding to three new cities and launching a popular delivery service.",
                                "targetVocab": "revenue"
                            },
                            {
                                "prompt": "Dùng từ 'expense' để viết một câu về chi phí hoạt động và tác động đến lợi nhuận. Ví dụ: Rising energy expenses forced the factory to invest in solar panels, which reduced electricity costs by thirty percent within two years.",
                                "targetVocab": "expense"
                            },
                            {
                                "prompt": "Dùng từ 'balance' để viết một câu về nguyên tắc cân đối trong kế toán. Ví dụ: The accountant discovered that the balance sheet did not balance because a recent equipment purchase had been recorded as an expense instead of an asset.",
                                "targetVocab": "balance"
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về báo cáo thu nhập và dòng tiền.",
                    "data": {
                        "text": "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: asset — tài sản, liability — nợ phải trả, equity — vốn chủ sở hữu, revenue — doanh thu, expense — chi phí, và balance — cân đối. Bạn đã hiểu cách đọc bảng cân đối kế toán và báo cáo kết quả kinh doanh. Bây giờ, chúng ta sẽ đi sâu hơn vào hai báo cáo quan trọng khác: báo cáo thu nhập và báo cáo lưu chuyển tiền tệ.\n\nTrong phần 2, bạn sẽ học 6 từ mới: income, statement, cash, flow, receivable, và payable. Những từ này giúp bạn hiểu cách doanh nghiệp theo dõi lợi nhuận, dòng tiền, và các khoản phải thu phải trả.\n\nTừ đầu tiên là income — danh từ — nghĩa là thu nhập, lợi nhuận. Trong kế toán, income thường chỉ lợi nhuận ròng — số tiền còn lại sau khi trừ tất cả chi phí khỏi doanh thu. Net income là dòng cuối cùng trên báo cáo kết quả kinh doanh, vì thế người ta gọi nó là 'bottom line.' Ví dụ: 'The company's net income doubled compared to last year, thanks to higher sales and strict cost control measures.' Trong bài đọc, income là thước đo cuối cùng — doanh nghiệp có thực sự kiếm được tiền hay không.\n\nTừ thứ hai là statement — danh từ — nghĩa là báo cáo, bản kê. Financial statement là báo cáo tài chính — tài liệu chính thức trình bày tình hình tài chính của doanh nghiệp. Có ba loại chính: balance sheet, income statement, và cash flow statement. Ví dụ: 'Public companies are required to publish their financial statements every quarter so that investors can evaluate their performance.' Trong bài đọc, statement là từ khóa kết nối — mỗi loại báo cáo cho bạn một góc nhìn khác nhau về doanh nghiệp.\n\nTừ thứ ba là cash — danh từ — nghĩa là tiền mặt. Trong kế toán, cash không chỉ là tiền giấy trong két sắt — nó bao gồm tiền trong tài khoản ngân hàng và các khoản tương đương tiền có thể chuyển đổi ngay lập tức. Ví dụ: 'Despite reporting strong revenue, the company was running low on cash because most of its sales were on credit with sixty-day payment terms.' Trong bài đọc, cash là máu của doanh nghiệp — một công ty có thể có lợi nhuận trên giấy nhưng vẫn phá sản nếu hết tiền mặt.\n\nTừ thứ tư là flow — danh từ — nghĩa là dòng chảy, luồng. Cash flow là dòng tiền — sự di chuyển của tiền vào và ra khỏi doanh nghiệp. Cash flow statement là báo cáo lưu chuyển tiền tệ, cho thấy tiền đến từ đâu và đi về đâu. Ví dụ: 'Positive cash flow from operations means the company is generating enough money from its core business to cover its daily expenses.' Trong bài đọc, flow nhấn mạnh tính liên tục — tiền phải luôn chảy, nếu dòng tiền tắc nghẽn, doanh nghiệp gặp nguy.\n\nTừ thứ năm là receivable — danh từ và tính từ — nghĩa là khoản phải thu. Accounts receivable là các khoản tiền mà khách hàng nợ doanh nghiệp — hàng đã giao nhưng chưa được thanh toán. Ví dụ: 'The company's accounts receivable increased sharply because many customers were taking longer than usual to pay their invoices.' Trong bài đọc, receivable là tài sản trên giấy — tiền mà doanh nghiệp có quyền nhận nhưng chưa thực sự cầm trong tay.\n\nTừ cuối cùng là payable — danh từ và tính từ — nghĩa là khoản phải trả. Accounts payable là các khoản tiền mà doanh nghiệp nợ nhà cung cấp — hàng đã nhận nhưng chưa thanh toán. Ví dụ: 'The finance team negotiated longer payment terms with suppliers, extending accounts payable from thirty to sixty days to improve cash flow.' Trong bài đọc, payable là nghĩa vụ ngắn hạn — tiền mà doanh nghiệp phải trả trong tương lai gần.\n\nSáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết về báo cáo thu nhập và dòng tiền nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Báo cáo thu nhập và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Báo cáo thu nhập và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Báo cáo thu nhập và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Báo cáo thu nhập và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Báo cáo thu nhập và dòng tiền",
                    "description": "Học 6 từ: income, statement, cash, flow, receivable, payable",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Báo cáo thu nhập và dòng tiền doanh nghiệp",
                    "description": "A company can be profitable on paper and still go bankrupt.",
                    "data": {
                        "text": "A company can be profitable on paper and still go bankrupt. This sounds like a contradiction, but it happens more often than you might think. The reason lies in the difference between income and cash flow — two concepts that every accounting student must understand deeply.\n\nThe income statement — sometimes called the profit and loss statement — shows how much money a company earned and spent over a specific period. It begins with revenue at the top and subtracts various expenses to arrive at net income at the bottom. If revenue exceeds expenses, the company reports a profit. If expenses exceed revenue, it reports a loss. The income statement is the most widely discussed financial statement because it answers the fundamental question: is this company making money?\n\nBut income can be misleading. Under modern accounting rules, revenue is recorded when it is earned, not when cash is received. If a Vietnamese electronics manufacturer sells ten thousand televisions to a retailer in January with payment due in March, the revenue appears on the January income statement — even though no cash has changed hands. The money owed by the retailer becomes an accounts receivable on the balance sheet.\n\nAccounts receivable represents money that customers owe the company. It is classified as a current asset because it is expected to be collected within one year. A growing receivable balance can be a warning sign. It might mean that customers are taking longer to pay, or that the company is extending too much credit to boost its revenue numbers.\n\nOn the other side of the equation, accounts payable represents money the company owes to its suppliers. When a company receives raw materials but has not yet paid for them, the amount goes into accounts payable — a current liability. Managing the timing between receivable and payable is one of the most important skills in corporate finance. A company that collects from customers quickly and pays suppliers slowly will have strong cash flow. A company that does the opposite may run out of cash.\n\nThis is where the cash flow statement becomes essential. While the income statement shows profitability, the cash flow statement shows liquidity — how much actual cash is moving in and out of the business. It is divided into three sections: cash flow from operations, cash flow from investing, and cash flow from financing.\n\nCash flow from operations is the most important section. It shows how much cash the company generates from its core business activities. A company with strong operating cash flow can pay its bills, invest in growth, and return money to shareholders without borrowing. Negative operating cash flow means the company is burning through cash faster than it earns it — a situation that cannot continue indefinitely.\n\nThe word flow is critical here. Cash must flow continuously through a business, like blood through a body. Revenue that sits in accounts receivable is not flowing. Expenses that pile up in accounts payable create pressure. The cash flow statement captures this movement in a way that the income statement cannot.\n\nEvery financial statement tells part of the story. The balance sheet shows what the company has and owes at a moment in time. The income statement shows whether it made or lost money over a period. The cash flow statement shows whether actual cash is coming in or going out. Together, these three statements give a complete picture of a company's financial health. Learning to read all three — in English — is a skill that will serve you throughout your career."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Báo cáo thu nhập và dòng tiền doanh nghiệp",
                    "description": "A company can be profitable on paper and still go bankrupt.",
                    "data": {
                        "text": "A company can be profitable on paper and still go bankrupt. This sounds like a contradiction, but it happens more often than you might think. The reason lies in the difference between income and cash flow — two concepts that every accounting student must understand deeply.\n\nThe income statement — sometimes called the profit and loss statement — shows how much money a company earned and spent over a specific period. It begins with revenue at the top and subtracts various expenses to arrive at net income at the bottom. If revenue exceeds expenses, the company reports a profit. If expenses exceed revenue, it reports a loss. The income statement is the most widely discussed financial statement because it answers the fundamental question: is this company making money?\n\nBut income can be misleading. Under modern accounting rules, revenue is recorded when it is earned, not when cash is received. If a Vietnamese electronics manufacturer sells ten thousand televisions to a retailer in January with payment due in March, the revenue appears on the January income statement — even though no cash has changed hands. The money owed by the retailer becomes an accounts receivable on the balance sheet.\n\nAccounts receivable represents money that customers owe the company. It is classified as a current asset because it is expected to be collected within one year. A growing receivable balance can be a warning sign. It might mean that customers are taking longer to pay, or that the company is extending too much credit to boost its revenue numbers.\n\nOn the other side of the equation, accounts payable represents money the company owes to its suppliers. When a company receives raw materials but has not yet paid for them, the amount goes into accounts payable — a current liability. Managing the timing between receivable and payable is one of the most important skills in corporate finance. A company that collects from customers quickly and pays suppliers slowly will have strong cash flow. A company that does the opposite may run out of cash.\n\nThis is where the cash flow statement becomes essential. While the income statement shows profitability, the cash flow statement shows liquidity — how much actual cash is moving in and out of the business. It is divided into three sections: cash flow from operations, cash flow from investing, and cash flow from financing.\n\nCash flow from operations is the most important section. It shows how much cash the company generates from its core business activities. A company with strong operating cash flow can pay its bills, invest in growth, and return money to shareholders without borrowing. Negative operating cash flow means the company is burning through cash faster than it earns it — a situation that cannot continue indefinitely.\n\nThe word flow is critical here. Cash must flow continuously through a business, like blood through a body. Revenue that sits in accounts receivable is not flowing. Expenses that pile up in accounts payable create pressure. The cash flow statement captures this movement in a way that the income statement cannot.\n\nEvery financial statement tells part of the story. The balance sheet shows what the company has and owes at a moment in time. The income statement shows whether it made or lost money over a period. The cash flow statement shows whether actual cash is coming in or going out. Together, these three statements give a complete picture of a company's financial health. Learning to read all three — in English — is a skill that will serve you throughout your career."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Báo cáo thu nhập và dòng tiền doanh nghiệp",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "A company can be profitable on paper and still go bankrupt. This sounds like a contradiction, but it happens more often than you might think. The reason lies in the difference between income and cash flow — two concepts that every accounting student must understand deeply.\n\nThe income statement — sometimes called the profit and loss statement — shows how much money a company earned and spent over a specific period. It begins with revenue at the top and subtracts various expenses to arrive at net income at the bottom. If revenue exceeds expenses, the company reports a profit. If expenses exceed revenue, it reports a loss. The income statement is the most widely discussed financial statement because it answers the fundamental question: is this company making money?\n\nBut income can be misleading. Under modern accounting rules, revenue is recorded when it is earned, not when cash is received. If a Vietnamese electronics manufacturer sells ten thousand televisions to a retailer in January with payment due in March, the revenue appears on the January income statement — even though no cash has changed hands. The money owed by the retailer becomes an accounts receivable on the balance sheet.\n\nAccounts receivable represents money that customers owe the company. It is classified as a current asset because it is expected to be collected within one year. A growing receivable balance can be a warning sign. It might mean that customers are taking longer to pay, or that the company is extending too much credit to boost its revenue numbers.\n\nOn the other side of the equation, accounts payable represents money the company owes to its suppliers. When a company receives raw materials but has not yet paid for them, the amount goes into accounts payable — a current liability. Managing the timing between receivable and payable is one of the most important skills in corporate finance. A company that collects from customers quickly and pays suppliers slowly will have strong cash flow. A company that does the opposite may run out of cash.\n\nThis is where the cash flow statement becomes essential. While the income statement shows profitability, the cash flow statement shows liquidity — how much actual cash is moving in and out of the business. It is divided into three sections: cash flow from operations, cash flow from investing, and cash flow from financing.\n\nCash flow from operations is the most important section. It shows how much cash the company generates from its core business activities. A company with strong operating cash flow can pay its bills, invest in growth, and return money to shareholders without borrowing. Negative operating cash flow means the company is burning through cash faster than it earns it — a situation that cannot continue indefinitely.\n\nThe word flow is critical here. Cash must flow continuously through a business, like blood through a body. Revenue that sits in accounts receivable is not flowing. Expenses that pile up in accounts payable create pressure. The cash flow statement captures this movement in a way that the income statement cannot.\n\nEvery financial statement tells part of the story. The balance sheet shows what the company has and owes at a moment in time. The income statement shows whether it made or lost money over a period. The cash flow statement shows whether actual cash is coming in or going out. Together, these three statements give a complete picture of a company's financial health. Learning to read all three — in English — is a skill that will serve you throughout your career."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Báo cáo thu nhập và dòng tiền",
                    "description": "Viết câu sử dụng 6 từ vựng về báo cáo thu nhập và dòng tiền.",
                    "data": {
                        "vocabList": ["income", "statement", "cash", "flow", "receivable", "payable"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'income' để viết một câu về lợi nhuận ròng của doanh nghiệp và ý nghĩa của nó. Ví dụ: The company's net income fell by twenty percent after a sharp rise in raw material costs that management failed to offset with higher prices.",
                                "targetVocab": "income"
                            },
                            {
                                "prompt": "Dùng từ 'statement' để viết một câu về vai trò của báo cáo tài chính đối với nhà đầu tư. Ví dụ: Before investing in any company, Warren Buffett reads its financial statements carefully, paying special attention to the consistency of earnings over the past decade.",
                                "targetVocab": "statement"
                            },
                            {
                                "prompt": "Dùng từ 'cash' để viết một câu về tầm quan trọng của tiền mặt đối với sự sống còn của doanh nghiệp. Ví dụ: Many promising startups fail not because their product is bad, but because they run out of cash before they can attract enough paying customers.",
                                "targetVocab": "cash"
                            },
                            {
                                "prompt": "Dùng từ 'flow' để viết một câu về dòng tiền hoạt động và khả năng tự tài trợ của doanh nghiệp. Ví dụ: Strong operating cash flow allowed the company to fund its expansion into Southeast Asian markets without taking on any additional debt.",
                                "targetVocab": "flow"
                            },
                            {
                                "prompt": "Dùng từ 'receivable' để viết một câu về khoản phải thu và rủi ro khi khách hàng chậm thanh toán. Ví dụ: The auditor flagged a concern about the company's accounts receivable because several large customers had not paid their invoices for over ninety days.",
                                "targetVocab": "receivable"
                            },
                            {
                                "prompt": "Dùng từ 'payable' để viết một câu về quản lý khoản phải trả và mối quan hệ với nhà cung cấp. Ví dụ: By negotiating sixty-day payment terms with suppliers, the company increased its accounts payable cycle and freed up cash for short-term investments.",
                                "targetVocab": "payable"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về kế toán dồn tích, khấu hao và công bố thông tin.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! Hãy cùng ôn lại nhanh những gì bạn đã học. Trong phần 1, bạn đã nắm được 6 từ nền tảng: asset — tài sản, liability — nợ phải trả, equity — vốn chủ sở hữu, revenue — doanh thu, expense — chi phí, và balance — cân đối. Đây là bộ khung cơ bản của bảng cân đối kế toán và báo cáo kết quả kinh doanh. Trong phần 2, bạn đã học thêm income — thu nhập, statement — báo cáo, cash — tiền mặt, flow — dòng chảy, receivable — khoản phải thu, và payable — khoản phải trả. Những từ này giúp bạn hiểu báo cáo thu nhập và dòng tiền.\n\nBây giờ, trong phần 3, chúng ta sẽ bước vào những khái niệm kế toán nâng cao hơn — những nguyên tắc mà phân biệt một người đọc báo cáo tài chính nghiệp dư với một chuyên gia thực thụ. Bạn sẽ học 6 từ mới: accrual, depreciation, amortization, retained, comprehensive, và disclosure.\n\nTừ đầu tiên là accrual — danh từ — nghĩa là dồn tích, kế toán dồn tích. Accrual accounting là phương pháp kế toán ghi nhận doanh thu và chi phí khi chúng phát sinh, không phải khi tiền thực sự được nhận hoặc chi trả. Ví dụ: 'Under the accrual method, a company records revenue when it delivers goods to the customer, even if payment will not arrive for another sixty days.' Trong bài đọc, accrual là nguyên tắc nền tảng — nó giải thích vì sao lợi nhuận trên giấy có thể khác xa tiền mặt thực tế.\n\nTừ thứ hai là depreciation — danh từ — nghĩa là khấu hao tài sản hữu hình. Depreciation là quá trình phân bổ chi phí của một tài sản cố định hữu hình — như máy móc, nhà xưởng, xe cộ — ra nhiều năm sử dụng thay vì ghi nhận toàn bộ chi phí trong năm mua. Ví dụ: 'The factory equipment was purchased for two million dollars and will be depreciated over ten years, resulting in an annual depreciation expense of two hundred thousand dollars.' Trong bài đọc, depreciation phản ánh thực tế rằng tài sản mất giá trị theo thời gian.\n\nTừ thứ ba là amortization — danh từ — nghĩa là khấu hao tài sản vô hình. Amortization tương tự depreciation nhưng áp dụng cho tài sản vô hình — bằng sáng chế, bản quyền, phần mềm, lợi thế thương mại. Ví dụ: 'The company paid five million dollars for a patent and will record amortization of five hundred thousand dollars per year over the patent's ten-year useful life.' Trong bài đọc, amortization cho thấy ngay cả tài sản không thể chạm vào cũng mất giá trị theo thời gian.\n\nTừ thứ tư là retained — tính từ — nghĩa là giữ lại, tích lũy. Retained earnings là lợi nhuận giữ lại — phần lợi nhuận mà doanh nghiệp không chia cho cổ đông dưới dạng cổ tức mà giữ lại để tái đầu tư. Ví dụ: 'The company's retained earnings grew steadily over five years as management chose to reinvest profits into research and development rather than pay dividends.' Trong bài đọc, retained earnings là nguồn vốn nội bộ — tiền mà doanh nghiệp tự tạo ra và giữ lại để phát triển.\n\nTừ thứ năm là comprehensive — tính từ — nghĩa là toàn diện, bao quát. Comprehensive income là thu nhập toàn diện — bao gồm lợi nhuận ròng cộng với các khoản lãi lỗ chưa thực hiện, như thay đổi giá trị đầu tư hoặc chênh lệch tỷ giá. Ví dụ: 'Other comprehensive income includes unrealized gains on investments and foreign currency translation adjustments that do not appear on the regular income statement.' Trong bài đọc, comprehensive mở rộng góc nhìn — cho bạn thấy bức tranh đầy đủ hơn về hiệu quả tài chính.\n\nTừ cuối cùng là disclosure — danh từ — nghĩa là công bố, tiết lộ thông tin. Disclosure trong kế toán là việc công bố các thông tin tài chính quan trọng trong phần ghi chú của báo cáo tài chính — chính sách kế toán, rủi ro, cam kết, và các sự kiện sau ngày lập báo cáo. Ví dụ: 'The auditor required additional disclosure about the company's related-party transactions to ensure that investors had a complete picture of potential conflicts of interest.' Trong bài đọc, disclosure là nguyên tắc minh bạch — doanh nghiệp phải nói ra những gì nhà đầu tư cần biết.\n\nTuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard và đọc bài viết cuối cùng về kế toán dồn tích và công bố thông tin nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Kế toán dồn tích và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Kế toán dồn tích và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Kế toán dồn tích và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Kế toán dồn tích và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Kế toán dồn tích và công bố thông tin",
                    "description": "Học 6 từ: accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Kế toán dồn tích, khấu hao và công bố thông tin",
                    "description": "Accounting is not just about counting money — it is about telling the truth about money.",
                    "data": {
                        "text": "Accounting is not just about counting money — it is about telling the truth about money. And the truth, in accounting, depends on which method you use to record transactions. The most widely accepted method in the world today is accrual accounting.\n\nUnder the accrual method, revenue is recorded when it is earned, and expenses are recorded when they are incurred — regardless of when cash actually changes hands. If a construction company completes a building in December but does not receive payment until February, the revenue is recorded in December under accrual accounting. This approach gives a more accurate picture of a company's financial performance because it matches revenue with the expenses that generated it.\n\nThe alternative — cash basis accounting — records transactions only when cash is received or paid. While simpler, it can be misleading. A company might look profitable in one month simply because a large payment arrived, even though the work was done months earlier. For this reason, international accounting standards require publicly traded companies to use the accrual method.\n\nOne of the most important applications of accrual accounting is depreciation. When a company buys a piece of equipment for one million dollars, it does not record the entire cost as an expense in the year of purchase. Instead, it spreads the cost over the equipment's useful life. If the equipment is expected to last ten years, the company records one hundred thousand dollars of depreciation expense each year. This reflects the reality that the equipment loses value gradually as it ages and wears out.\n\nDepreciation applies to tangible assets — physical things like buildings, vehicles, machinery, and furniture. But companies also own intangible assets — things you cannot touch, like patents, trademarks, copyrights, and software licenses. The process of spreading the cost of intangible assets over their useful life is called amortization. A pharmaceutical company that spends twenty million dollars developing a drug patent might amortize that cost over the patent's twenty-year life, recording one million dollars of amortization expense each year.\n\nBoth depreciation and amortization reduce the value of assets on the balance sheet and create expenses on the income statement. They are non-cash expenses — no money actually leaves the company when depreciation or amortization is recorded. But they have real effects on reported income and tax obligations.\n\nWhen a company earns a profit, it has two choices: distribute the profit to shareholders as dividends, or keep it in the business. Profits that are kept are called retained earnings. Retained earnings accumulate over time and appear in the equity section of the balance sheet. A company with large retained earnings has been profitable for many years and has chosen to reinvest in itself rather than pay out all its profits. Retained earnings are a sign of financial strength and self-sufficiency.\n\nBeyond the standard income statement, companies also report comprehensive income. This broader measure includes net income plus other items that affect equity but do not appear on the regular income statement. These items include unrealized gains or losses on investments, foreign currency translation adjustments, and changes in pension obligations. Comprehensive income gives investors a fuller picture of all the economic events that affected the company during the period.\n\nFinally, no set of financial statements is complete without disclosure. The notes to the financial statements — often running dozens of pages — contain critical information that the numbers alone cannot convey. Disclosures explain the accounting policies the company uses, describe significant risks and uncertainties, detail related-party transactions, and report events that occurred after the balance sheet date. Without proper disclosure, investors cannot fully understand what the numbers mean.\n\nFrom accrual accounting to disclosure, these concepts form the backbone of modern financial reporting. They ensure that financial statements are not just numbers on a page, but a truthful and comprehensive account of a company's economic reality."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Kế toán dồn tích, khấu hao và công bố thông tin",
                    "description": "Accounting is not just about counting money — it is about telling the truth about money.",
                    "data": {
                        "text": "Accounting is not just about counting money — it is about telling the truth about money. And the truth, in accounting, depends on which method you use to record transactions. The most widely accepted method in the world today is accrual accounting.\n\nUnder the accrual method, revenue is recorded when it is earned, and expenses are recorded when they are incurred — regardless of when cash actually changes hands. If a construction company completes a building in December but does not receive payment until February, the revenue is recorded in December under accrual accounting. This approach gives a more accurate picture of a company's financial performance because it matches revenue with the expenses that generated it.\n\nThe alternative — cash basis accounting — records transactions only when cash is received or paid. While simpler, it can be misleading. A company might look profitable in one month simply because a large payment arrived, even though the work was done months earlier. For this reason, international accounting standards require publicly traded companies to use the accrual method.\n\nOne of the most important applications of accrual accounting is depreciation. When a company buys a piece of equipment for one million dollars, it does not record the entire cost as an expense in the year of purchase. Instead, it spreads the cost over the equipment's useful life. If the equipment is expected to last ten years, the company records one hundred thousand dollars of depreciation expense each year. This reflects the reality that the equipment loses value gradually as it ages and wears out.\n\nDepreciation applies to tangible assets — physical things like buildings, vehicles, machinery, and furniture. But companies also own intangible assets — things you cannot touch, like patents, trademarks, copyrights, and software licenses. The process of spreading the cost of intangible assets over their useful life is called amortization. A pharmaceutical company that spends twenty million dollars developing a drug patent might amortize that cost over the patent's twenty-year life, recording one million dollars of amortization expense each year.\n\nBoth depreciation and amortization reduce the value of assets on the balance sheet and create expenses on the income statement. They are non-cash expenses — no money actually leaves the company when depreciation or amortization is recorded. But they have real effects on reported income and tax obligations.\n\nWhen a company earns a profit, it has two choices: distribute the profit to shareholders as dividends, or keep it in the business. Profits that are kept are called retained earnings. Retained earnings accumulate over time and appear in the equity section of the balance sheet. A company with large retained earnings has been profitable for many years and has chosen to reinvest in itself rather than pay out all its profits. Retained earnings are a sign of financial strength and self-sufficiency.\n\nBeyond the standard income statement, companies also report comprehensive income. This broader measure includes net income plus other items that affect equity but do not appear on the regular income statement. These items include unrealized gains or losses on investments, foreign currency translation adjustments, and changes in pension obligations. Comprehensive income gives investors a fuller picture of all the economic events that affected the company during the period.\n\nFinally, no set of financial statements is complete without disclosure. The notes to the financial statements — often running dozens of pages — contain critical information that the numbers alone cannot convey. Disclosures explain the accounting policies the company uses, describe significant risks and uncertainties, detail related-party transactions, and report events that occurred after the balance sheet date. Without proper disclosure, investors cannot fully understand what the numbers mean.\n\nFrom accrual accounting to disclosure, these concepts form the backbone of modern financial reporting. They ensure that financial statements are not just numbers on a page, but a truthful and comprehensive account of a company's economic reality."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Kế toán dồn tích, khấu hao và công bố thông tin",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Accounting is not just about counting money — it is about telling the truth about money. And the truth, in accounting, depends on which method you use to record transactions. The most widely accepted method in the world today is accrual accounting.\n\nUnder the accrual method, revenue is recorded when it is earned, and expenses are recorded when they are incurred — regardless of when cash actually changes hands. If a construction company completes a building in December but does not receive payment until February, the revenue is recorded in December under accrual accounting. This approach gives a more accurate picture of a company's financial performance because it matches revenue with the expenses that generated it.\n\nThe alternative — cash basis accounting — records transactions only when cash is received or paid. While simpler, it can be misleading. A company might look profitable in one month simply because a large payment arrived, even though the work was done months earlier. For this reason, international accounting standards require publicly traded companies to use the accrual method.\n\nOne of the most important applications of accrual accounting is depreciation. When a company buys a piece of equipment for one million dollars, it does not record the entire cost as an expense in the year of purchase. Instead, it spreads the cost over the equipment's useful life. If the equipment is expected to last ten years, the company records one hundred thousand dollars of depreciation expense each year. This reflects the reality that the equipment loses value gradually as it ages and wears out.\n\nDepreciation applies to tangible assets — physical things like buildings, vehicles, machinery, and furniture. But companies also own intangible assets — things you cannot touch, like patents, trademarks, copyrights, and software licenses. The process of spreading the cost of intangible assets over their useful life is called amortization. A pharmaceutical company that spends twenty million dollars developing a drug patent might amortize that cost over the patent's twenty-year life, recording one million dollars of amortization expense each year.\n\nBoth depreciation and amortization reduce the value of assets on the balance sheet and create expenses on the income statement. They are non-cash expenses — no money actually leaves the company when depreciation or amortization is recorded. But they have real effects on reported income and tax obligations.\n\nWhen a company earns a profit, it has two choices: distribute the profit to shareholders as dividends, or keep it in the business. Profits that are kept are called retained earnings. Retained earnings accumulate over time and appear in the equity section of the balance sheet. A company with large retained earnings has been profitable for many years and has chosen to reinvest in itself rather than pay out all its profits. Retained earnings are a sign of financial strength and self-sufficiency.\n\nBeyond the standard income statement, companies also report comprehensive income. This broader measure includes net income plus other items that affect equity but do not appear on the regular income statement. These items include unrealized gains or losses on investments, foreign currency translation adjustments, and changes in pension obligations. Comprehensive income gives investors a fuller picture of all the economic events that affected the company during the period.\n\nFinally, no set of financial statements is complete without disclosure. The notes to the financial statements — often running dozens of pages — contain critical information that the numbers alone cannot convey. Disclosures explain the accounting policies the company uses, describe significant risks and uncertainties, detail related-party transactions, and report events that occurred after the balance sheet date. Without proper disclosure, investors cannot fully understand what the numbers mean.\n\nFrom accrual accounting to disclosure, these concepts form the backbone of modern financial reporting. They ensure that financial statements are not just numbers on a page, but a truthful and comprehensive account of a company's economic reality."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Kế toán dồn tích và công bố thông tin",
                    "description": "Viết câu sử dụng 6 từ vựng về kế toán dồn tích, khấu hao và công bố thông tin.",
                    "data": {
                        "vocabList": ["accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'accrual' để viết một câu về phương pháp kế toán dồn tích và cách nó ghi nhận doanh thu. Ví dụ: Under accrual accounting, the consulting firm recorded three months of revenue in December even though the client would not pay until the following March.",
                                "targetVocab": "accrual"
                            },
                            {
                                "prompt": "Dùng từ 'depreciation' để viết một câu về khấu hao tài sản cố định và tác động đến báo cáo tài chính. Ví dụ: The annual depreciation of the company's delivery fleet reduced its reported profit by four hundred thousand dollars, even though no cash was actually spent.",
                                "targetVocab": "depreciation"
                            },
                            {
                                "prompt": "Dùng từ 'amortization' để viết một câu về khấu hao tài sản vô hình như bằng sáng chế hoặc phần mềm. Ví dụ: The technology company recorded two million dollars in amortization expense for the software licenses it had purchased three years earlier.",
                                "targetVocab": "amortization"
                            },
                            {
                                "prompt": "Dùng từ 'retained' để viết một câu về lợi nhuận giữ lại và cách doanh nghiệp sử dụng chúng. Ví dụ: Instead of paying dividends, the board decided to add the year's profits to retained earnings to fund the construction of a new research facility.",
                                "targetVocab": "retained"
                            },
                            {
                                "prompt": "Dùng từ 'comprehensive' để viết một câu về thu nhập toàn diện và các khoản mục ngoài lợi nhuận ròng. Ví dụ: The company's comprehensive income was significantly higher than its net income because of large unrealized gains on its foreign currency investments.",
                                "targetVocab": "comprehensive"
                            },
                            {
                                "prompt": "Dùng từ 'disclosure' để viết một câu về yêu cầu công bố thông tin trong báo cáo tài chính. Ví dụ: The regulator fined the company for inadequate disclosure of its environmental liabilities, which had been hidden in vague footnotes for years.",
                                "targetVocab": "disclosure"
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
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Cùng ôn lại trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Báo cáo tài chính. Hãy cùng nhìn lại hành trình của bạn.\n\nTrong phần 1, bạn đã học những khái niệm nền tảng nhất: asset — tài sản, liability — nợ phải trả, equity — vốn chủ sở hữu, revenue — doanh thu, expense — chi phí, và balance — cân đối. Đây là bộ khung cơ bản của bảng cân đối kế toán và báo cáo kết quả kinh doanh.\n\nTrong phần 2, bạn đã đi sâu hơn với: income — thu nhập, statement — báo cáo, cash — tiền mặt, flow — dòng chảy, receivable — khoản phải thu, và payable — khoản phải trả. Những từ này giúp bạn hiểu báo cáo thu nhập và dòng tiền — hai công cụ quan trọng để đánh giá sức khỏe tài chính.\n\nTrong phần 3, bạn đã khám phá: accrual — dồn tích, depreciation — khấu hao hữu hình, amortization — khấu hao vô hình, retained — giữ lại, comprehensive — toàn diện, và disclosure — công bố thông tin. Đây là những khái niệm nâng cao giúp bạn đọc hiểu báo cáo tài chính ở mức chuyên sâu.\n\nBây giờ, phần ôn tập này sẽ giúp bạn củng cố toàn bộ 18 từ vựng. Bạn sẽ xem lại flashcard, luyện phát âm, và viết câu với tất cả các từ. Sau phần ôn tập, bạn sẽ sẵn sàng cho bài đọc tổng hợp — một bài viết dài hơn sử dụng cả 18 từ trong một ngữ cảnh liền mạch. Hãy bắt đầu nào!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: asset, liability, equity, revenue, expense, balance, income, statement, cash, flow, receivable, payable, accrual, depreciation, amortization, retained, comprehensive, disclosure",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng báo cáo tài chính",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'asset' để viết một câu về cách doanh nghiệp công nghệ phân loại tài sản trí tuệ. Ví dụ: Google's most valuable asset is not its office buildings or servers, but its search algorithm and the massive database of user behavior it has accumulated over two decades.",
                                "targetVocab": "asset"
                            },
                            {
                                "prompt": "Dùng từ 'liability' để viết một câu về rủi ro khi doanh nghiệp có quá nhiều nợ. Ví dụ: The airline's total liabilities exceeded its assets by three billion dollars, forcing it to file for bankruptcy protection and restructure its debt.",
                                "targetVocab": "liability"
                            },
                            {
                                "prompt": "Dùng từ 'equity' để viết một câu về cách nhà đầu tư đánh giá vốn chủ sở hữu. Ví dụ: Investors closely monitor the return on equity ratio because it shows how efficiently a company uses shareholders' money to generate profits.",
                                "targetVocab": "equity"
                            },
                            {
                                "prompt": "Dùng từ 'revenue' để viết một câu về sự khác biệt giữa doanh thu và lợi nhuận. Ví dụ: The startup generated impressive revenue of fifty million dollars in its first year, but high marketing expenses meant it still reported a net loss.",
                                "targetVocab": "revenue"
                            },
                            {
                                "prompt": "Dùng từ 'expense' để viết một câu về chiến lược cắt giảm chi phí của doanh nghiệp. Ví dụ: The new CEO reduced operating expenses by fifteen percent through automation, renegotiating supplier contracts, and consolidating office locations.",
                                "targetVocab": "expense"
                            },
                            {
                                "prompt": "Dùng từ 'balance' để viết một câu về tầm quan trọng của bảng cân đối kế toán đối với ngân hàng. Ví dụ: The bank reviewed the company's balance sheet before approving the loan, paying close attention to the ratio of current assets to current liabilities.",
                                "targetVocab": "balance"
                            },
                            {
                                "prompt": "Dùng từ 'income' để viết một câu về xu hướng lợi nhuận ròng qua nhiều năm. Ví dụ: The company's net income has grown consistently for seven consecutive years, making it one of the most reliable investments in the Vietnamese stock market.",
                                "targetVocab": "income"
                            },
                            {
                                "prompt": "Dùng từ 'statement' để viết một câu về yêu cầu công bố báo cáo tài chính của công ty niêm yết. Ví dụ: Listed companies on the Ho Chi Minh Stock Exchange must publish audited financial statements within ninety days of the fiscal year end.",
                                "targetVocab": "statement"
                            },
                            {
                                "prompt": "Dùng từ 'cash' để viết một câu về tình trạng thiếu tiền mặt dù có lợi nhuận. Ví dụ: The construction company reported a profit on its income statement but was desperately short of cash because clients owed millions in unpaid invoices.",
                                "targetVocab": "cash"
                            },
                            {
                                "prompt": "Dùng từ 'flow' để viết một câu về dòng tiền tự do và khả năng đầu tư của doanh nghiệp. Ví dụ: Positive free cash flow gave the company the flexibility to acquire a smaller competitor without needing to borrow from banks.",
                                "targetVocab": "flow"
                            },
                            {
                                "prompt": "Dùng từ 'receivable' để viết một câu về chính sách thu hồi công nợ của doanh nghiệp. Ví dụ: The finance department implemented a stricter receivable collection policy, reducing the average payment period from ninety days to forty-five.",
                                "targetVocab": "receivable"
                            },
                            {
                                "prompt": "Dùng từ 'payable' để viết một câu về cách doanh nghiệp quản lý khoản phải trả để tối ưu dòng tiền. Ví dụ: The CFO extended the company's payable cycle to sixty days, giving the treasury team more time to invest idle cash in short-term instruments.",
                                "targetVocab": "payable"
                            },
                            {
                                "prompt": "Dùng từ 'accrual' để viết một câu về sự khác biệt giữa kế toán dồn tích và kế toán tiền mặt. Ví dụ: Switching from cash basis to accrual accounting revealed that the company's true expenses were much higher than previously reported.",
                                "targetVocab": "accrual"
                            },
                            {
                                "prompt": "Dùng từ 'depreciation' để viết một câu về tác động của khấu hao đến thuế doanh nghiệp. Ví dụ: Accelerated depreciation of the new factory equipment reduced the company's taxable income by two million dollars in the first year.",
                                "targetVocab": "depreciation"
                            },
                            {
                                "prompt": "Dùng từ 'amortization' để viết một câu về khấu hao lợi thế thương mại sau thương vụ mua lại. Ví dụ: After acquiring the rival firm, the company recorded annual amortization of the goodwill over a fifteen-year period as required by accounting standards.",
                                "targetVocab": "amortization"
                            },
                            {
                                "prompt": "Dùng từ 'retained' để viết một câu về quyết định giữ lại lợi nhuận thay vì chia cổ tức. Ví dụ: Amazon famously kept its retained earnings high for years, reinvesting nearly all profits into logistics infrastructure and cloud computing rather than paying dividends.",
                                "targetVocab": "retained"
                            },
                            {
                                "prompt": "Dùng từ 'comprehensive' để viết một câu về thu nhập toàn diện và biến động tỷ giá. Ví dụ: The multinational corporation's comprehensive income dropped sharply due to foreign currency translation losses when the dollar strengthened against Asian currencies.",
                                "targetVocab": "comprehensive"
                            },
                            {
                                "prompt": "Dùng từ 'disclosure' để viết một câu về hậu quả khi doanh nghiệp không công bố đầy đủ thông tin. Ví dụ: The lack of proper disclosure about the CEO's personal loans from the company led to a securities fraud investigation and a sharp drop in the stock price.",
                                "targetVocab": "disclosure"
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về báo cáo tài chính.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, kể câu chuyện hoàn chỉnh về báo cáo tài chính — từ bảng cân đối kế toán đến công bố thông tin.\n\nBạn sẽ gặp lại asset, liability, equity, revenue, expense, balance trong phần mở đầu về cấu trúc báo cáo tài chính. Tiếp theo, income, statement, cash, flow, receivable, payable sẽ giúp bạn hiểu cách doanh nghiệp theo dõi lợi nhuận và dòng tiền. Và cuối cùng, accrual, depreciation, amortization, retained, comprehensive, disclosure sẽ đưa bạn vào thế giới kế toán chuyên sâu.\n\nHãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, và thử đoán nghĩa trước khi nhìn lại định nghĩa. Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh để tổng hợp những gì đã học. Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Báo cáo tài chính — Bức tranh toàn cảnh",
                    "description": "Financial statements are the universal language of business.",
                    "data": {
                        "text": "Financial statements are the universal language of business. Whether a company operates in Hanoi, New York, or London, its financial health is communicated through the same set of reports. For anyone studying accounting or finance, learning to read these statements in English is not optional — it is essential.\n\nThe foundation of financial reporting is the balance sheet. This statement captures a company's financial position at a single point in time, organized around the fundamental accounting equation: Assets = Liabilities + Equity. Every transaction a company makes affects at least two of these three elements, and the equation must always remain in balance.\n\nAssets are the resources a company controls. They range from cash in the bank and inventory in the warehouse to factories, patents, and brand names. Assets are listed in order of liquidity — how quickly they can be converted to cash. Cash and accounts receivable appear first as current assets. Buildings and equipment appear further down as non-current assets.\n\nLiabilities are the company's obligations — money it owes to banks, suppliers, employees, and governments. Current liabilities like accounts payable and short-term loans must be settled within one year. Non-current liabilities like long-term bonds and pension obligations extend further into the future. A company with liabilities that far exceed its assets is in financial distress.\n\nEquity is the residual value — what belongs to the owners after all debts are paid. It includes the money shareholders originally invested plus all the profits the company has earned and kept over the years. These accumulated profits are called retained earnings, and they represent the company's ability to grow from its own resources rather than relying on external funding.\n\nThe income statement tells a different story. While the balance sheet is a snapshot, the income statement covers a period — a quarter or a year. It begins with revenue, the total money earned from selling goods or services. From revenue, the statement subtracts various categories of expense — cost of goods sold, operating expenses, interest, and taxes — to arrive at net income. This bottom line number tells investors whether the company made or lost money during the period.\n\nBut net income alone does not tell the whole story. Under accrual accounting — the method required by international standards — revenue is recorded when earned and expenses when incurred, regardless of when cash changes hands. A company might report strong income on its income statement while its bank account is nearly empty. This is why the cash flow statement exists.\n\nThe cash flow statement tracks the actual movement of cash in and out of the business. It is divided into three sections. Operating cash flow shows cash generated from core business activities. Investing cash flow shows cash spent on or received from buying and selling long-term assets. Financing cash flow shows cash from borrowing, repaying debt, issuing stock, or paying dividends.\n\nThe relationship between receivable and payable is central to understanding cash flow. Accounts receivable — money owed by customers — is an asset, but it is not cash until the customer actually pays. A company with rapidly growing receivable may look profitable but could be running short of actual cash. Accounts payable — money owed to suppliers — is a liability, but delaying payment can temporarily improve cash flow. Managing the timing between collecting receivable and paying payable is one of the most important skills in corporate treasury.\n\nAs assets age, their value declines. Physical assets like machinery and vehicles lose value through depreciation — a systematic allocation of cost over the asset's useful life. A delivery truck purchased for fifty thousand dollars might be depreciated over five years, with ten thousand dollars of depreciation expense recorded each year. Intangible assets like patents and software undergo a similar process called amortization. Both depreciation and amortization are non-cash expenses — they reduce reported income without any actual cash leaving the company.\n\nBeyond net income, companies report comprehensive income, which includes gains and losses that bypass the regular income statement. Foreign currency fluctuations, unrealized investment gains, and pension adjustments all flow through other comprehensive income. This broader measure gives investors a more complete view of all economic changes affecting the company's equity.\n\nFinally, the numbers in financial statements cannot stand alone. They require context, explanation, and transparency. This is the role of disclosure. The notes accompanying financial statements — often the longest section of an annual report — explain accounting policies, describe significant risks, detail contingent liabilities, and reveal related-party transactions. Without thorough disclosure, even the most carefully prepared financial statements can mislead.\n\nFrom the balance of assets and liabilities to the flow of cash through operations, from the accrual of revenue to the disclosure of risks — financial statements weave together a comprehensive narrative of a company's economic life. The language of that narrative, in boardrooms and stock exchanges around the world, is English. And now, with these eighteen words in your vocabulary, you can begin to read it."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Báo cáo tài chính — Bức tranh toàn cảnh",
                    "description": "Financial statements are the universal language of business.",
                    "data": {
                        "text": "Financial statements are the universal language of business. Whether a company operates in Hanoi, New York, or London, its financial health is communicated through the same set of reports. For anyone studying accounting or finance, learning to read these statements in English is not optional — it is essential.\n\nThe foundation of financial reporting is the balance sheet. This statement captures a company's financial position at a single point in time, organized around the fundamental accounting equation: Assets = Liabilities + Equity. Every transaction a company makes affects at least two of these three elements, and the equation must always remain in balance.\n\nAssets are the resources a company controls. They range from cash in the bank and inventory in the warehouse to factories, patents, and brand names. Assets are listed in order of liquidity — how quickly they can be converted to cash. Cash and accounts receivable appear first as current assets. Buildings and equipment appear further down as non-current assets.\n\nLiabilities are the company's obligations — money it owes to banks, suppliers, employees, and governments. Current liabilities like accounts payable and short-term loans must be settled within one year. Non-current liabilities like long-term bonds and pension obligations extend further into the future. A company with liabilities that far exceed its assets is in financial distress.\n\nEquity is the residual value — what belongs to the owners after all debts are paid. It includes the money shareholders originally invested plus all the profits the company has earned and kept over the years. These accumulated profits are called retained earnings, and they represent the company's ability to grow from its own resources rather than relying on external funding.\n\nThe income statement tells a different story. While the balance sheet is a snapshot, the income statement covers a period — a quarter or a year. It begins with revenue, the total money earned from selling goods or services. From revenue, the statement subtracts various categories of expense — cost of goods sold, operating expenses, interest, and taxes — to arrive at net income. This bottom line number tells investors whether the company made or lost money during the period.\n\nBut net income alone does not tell the whole story. Under accrual accounting — the method required by international standards — revenue is recorded when earned and expenses when incurred, regardless of when cash changes hands. A company might report strong income on its income statement while its bank account is nearly empty. This is why the cash flow statement exists.\n\nThe cash flow statement tracks the actual movement of cash in and out of the business. It is divided into three sections. Operating cash flow shows cash generated from core business activities. Investing cash flow shows cash spent on or received from buying and selling long-term assets. Financing cash flow shows cash from borrowing, repaying debt, issuing stock, or paying dividends.\n\nThe relationship between receivable and payable is central to understanding cash flow. Accounts receivable — money owed by customers — is an asset, but it is not cash until the customer actually pays. A company with rapidly growing receivable may look profitable but could be running short of actual cash. Accounts payable — money owed to suppliers — is a liability, but delaying payment can temporarily improve cash flow. Managing the timing between collecting receivable and paying payable is one of the most important skills in corporate treasury.\n\nAs assets age, their value declines. Physical assets like machinery and vehicles lose value through depreciation — a systematic allocation of cost over the asset's useful life. A delivery truck purchased for fifty thousand dollars might be depreciated over five years, with ten thousand dollars of depreciation expense recorded each year. Intangible assets like patents and software undergo a similar process called amortization. Both depreciation and amortization are non-cash expenses — they reduce reported income without any actual cash leaving the company.\n\nBeyond net income, companies report comprehensive income, which includes gains and losses that bypass the regular income statement. Foreign currency fluctuations, unrealized investment gains, and pension adjustments all flow through other comprehensive income. This broader measure gives investors a more complete view of all economic changes affecting the company's equity.\n\nFinally, the numbers in financial statements cannot stand alone. They require context, explanation, and transparency. This is the role of disclosure. The notes accompanying financial statements — often the longest section of an annual report — explain accounting policies, describe significant risks, detail contingent liabilities, and reveal related-party transactions. Without thorough disclosure, even the most carefully prepared financial statements can mislead.\n\nFrom the balance of assets and liabilities to the flow of cash through operations, from the accrual of revenue to the disclosure of risks — financial statements weave together a comprehensive narrative of a company's economic life. The language of that narrative, in boardrooms and stock exchanges around the world, is English. And now, with these eighteen words in your vocabulary, you can begin to read it."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Báo cáo tài chính — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Financial statements are the universal language of business. Whether a company operates in Hanoi, New York, or London, its financial health is communicated through the same set of reports. For anyone studying accounting or finance, learning to read these statements in English is not optional — it is essential.\n\nThe foundation of financial reporting is the balance sheet. This statement captures a company's financial position at a single point in time, organized around the fundamental accounting equation: Assets = Liabilities + Equity. Every transaction a company makes affects at least two of these three elements, and the equation must always remain in balance.\n\nAssets are the resources a company controls. They range from cash in the bank and inventory in the warehouse to factories, patents, and brand names. Assets are listed in order of liquidity — how quickly they can be converted to cash. Cash and accounts receivable appear first as current assets. Buildings and equipment appear further down as non-current assets.\n\nLiabilities are the company's obligations — money it owes to banks, suppliers, employees, and governments. Current liabilities like accounts payable and short-term loans must be settled within one year. Non-current liabilities like long-term bonds and pension obligations extend further into the future. A company with liabilities that far exceed its assets is in financial distress.\n\nEquity is the residual value — what belongs to the owners after all debts are paid. It includes the money shareholders originally invested plus all the profits the company has earned and kept over the years. These accumulated profits are called retained earnings, and they represent the company's ability to grow from its own resources rather than relying on external funding.\n\nThe income statement tells a different story. While the balance sheet is a snapshot, the income statement covers a period — a quarter or a year. It begins with revenue, the total money earned from selling goods or services. From revenue, the statement subtracts various categories of expense — cost of goods sold, operating expenses, interest, and taxes — to arrive at net income. This bottom line number tells investors whether the company made or lost money during the period.\n\nBut net income alone does not tell the whole story. Under accrual accounting — the method required by international standards — revenue is recorded when earned and expenses when incurred, regardless of when cash changes hands. A company might report strong income on its income statement while its bank account is nearly empty. This is why the cash flow statement exists.\n\nThe cash flow statement tracks the actual movement of cash in and out of the business. It is divided into three sections. Operating cash flow shows cash generated from core business activities. Investing cash flow shows cash spent on or received from buying and selling long-term assets. Financing cash flow shows cash from borrowing, repaying debt, issuing stock, or paying dividends.\n\nThe relationship between receivable and payable is central to understanding cash flow. Accounts receivable — money owed by customers — is an asset, but it is not cash until the customer actually pays. A company with rapidly growing receivable may look profitable but could be running short of actual cash. Accounts payable — money owed to suppliers — is a liability, but delaying payment can temporarily improve cash flow. Managing the timing between collecting receivable and paying payable is one of the most important skills in corporate treasury.\n\nAs assets age, their value declines. Physical assets like machinery and vehicles lose value through depreciation — a systematic allocation of cost over the asset's useful life. A delivery truck purchased for fifty thousand dollars might be depreciated over five years, with ten thousand dollars of depreciation expense recorded each year. Intangible assets like patents and software undergo a similar process called amortization. Both depreciation and amortization are non-cash expenses — they reduce reported income without any actual cash leaving the company.\n\nBeyond net income, companies report comprehensive income, which includes gains and losses that bypass the regular income statement. Foreign currency fluctuations, unrealized investment gains, and pension adjustments all flow through other comprehensive income. This broader measure gives investors a more complete view of all economic changes affecting the company's equity.\n\nFinally, the numbers in financial statements cannot stand alone. They require context, explanation, and transparency. This is the role of disclosure. The notes accompanying financial statements — often the longest section of an annual report — explain accounting policies, describe significant risks, detail contingent liabilities, and reveal related-party transactions. Without thorough disclosure, even the most carefully prepared financial statements can mislead.\n\nFrom the balance of assets and liabilities to the flow of cash through operations, from the accrual of revenue to the disclosure of risks — financial statements weave together a comprehensive narrative of a company's economic life. The language of that narrative, in boardrooms and stock exchanges around the world, is English. And now, with these eighteen words in your vocabulary, you can begin to read it."
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích báo cáo tài chính",
                    "description": "Viết đoạn văn tiếng Anh phân tích về báo cáo tài chính sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["asset", "liability", "equity", "revenue", "expense", "balance", "income", "statement", "cash", "flow", "receivable", "payable", "accrual", "depreciation", "amortization", "retained", "comprehensive", "disclosure"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến báo cáo tài chính. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích vì sao một doanh nghiệp có thể báo cáo lợi nhuận (income) cao nhưng vẫn gặp khó khăn về tiền mặt (cash). Giải thích vai trò của accrual accounting, mối quan hệ giữa receivable và payable, và cách cash flow statement giúp nhà đầu tư nhìn thấy bức tranh thực sự.",
                            "Hãy phân tích cách đọc hiểu sức khỏe tài chính của một doanh nghiệp Việt Nam thông qua ba báo cáo tài chính chính. Giải thích balance sheet cho thấy gì về asset, liability và equity, income statement cho thấy gì về revenue và expense, và vì sao disclosure trong phần ghi chú là không thể thiếu."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần chiêm nghiệm sâu lắng.",
                    "data": {
                        "text": "Bạn vừa hoàn thành bài học đầu tiên trong chuỗi Kế toán và Tài chính doanh nghiệp. Hãy dừng lại một chút và cảm nhận điều đó.\n\nBạn biết không, có một điều kỳ diệu về báo cáo tài chính mà ít người nhận ra. Đằng sau mỗi con số — mỗi dòng asset, mỗi khoản liability, mỗi đồng revenue — là câu chuyện của con người. Một nhà máy được xây dựng vì ai đó dám mơ lớn. Một khoản nợ được vay vì ai đó tin vào tương lai. Một dòng retained earnings tăng lên vì cả một đội ngũ đã làm việc không ngừng nghỉ. Báo cáo tài chính không chỉ là bảng số — nó là nhật ký của những quyết định, những rủi ro, và những hy vọng.\n\nHãy cùng nhìn lại một số từ quan trọng nhất, lần này với góc nhìn sâu hơn.\n\nEquity — vốn chủ sở hữu. Đây không chỉ là một dòng trên bảng cân đối kế toán. Equity là lời hứa — lời hứa rằng sau khi trả hết mọi khoản nợ, vẫn còn giá trị thuộc về những người đã tin tưởng và đầu tư. Ví dụ mới: A company's equity tells you not just what it is worth today, but how much value it has created and retained through years of disciplined management.\n\nCash flow — dòng tiền. Nếu income statement là bức tranh được vẽ cẩn thận, thì cash flow statement là bức ảnh chụp thẳng — không tô vẽ, không che giấu. Nó cho bạn thấy tiền thực sự đi đâu. Ví dụ mới: Experienced investors often trust cash flow more than reported income because cash flow cannot be manipulated as easily by accounting choices.\n\nAccrual — dồn tích. Nguyên tắc này thay đổi cách chúng ta nhìn nhận thời gian trong kế toán. Doanh thu không phải là khi tiền vào tài khoản — mà là khi giá trị được tạo ra. Ví dụ mới: The shift from cash basis to accrual accounting was one of the most important developments in the history of financial reporting, because it forced companies to match their efforts with their results.\n\nDepreciation — khấu hao. Mỗi tài sản đều có tuổi thọ. Mỗi chiếc máy, mỗi tòa nhà, mỗi chiếc xe — tất cả đều đang già đi. Depreciation là cách kế toán thừa nhận sự thật đó. Ví dụ mới: When you see depreciation on a financial statement, you are seeing the quiet acknowledgment that nothing lasts forever — and that planning for replacement is part of responsible management.\n\nDisclosure — công bố thông tin. Trong một thế giới mà niềm tin là đồng tiền quý giá nhất, disclosure là cách doanh nghiệp nói: 'Đây là tất cả những gì bạn cần biết. Chúng tôi không giấu gì.' Ví dụ mới: The best companies treat disclosure not as a regulatory burden but as an opportunity to build trust with investors who value transparency above all else.\n\nRetained earnings — lợi nhuận giữ lại. Đây là minh chứng cho sự kiên nhẫn. Thay vì chia hết lợi nhuận, doanh nghiệp chọn giữ lại để xây dựng tương lai. Mỗi đồng retained earnings là một viên gạch trong nền móng của ngày mai. Ví dụ mới: Warren Buffett has long argued that retained earnings, when wisely reinvested, create far more value for shareholders than dividends ever could.\n\n18 từ vựng này không chỉ giúp bạn đọc được báo cáo tài chính bằng tiếng Anh. Chúng giúp bạn nhìn thấy câu chuyện đằng sau những con số — câu chuyện về giá trị, về rủi ro, về niềm tin và sự minh bạch. Và khi bạn nhìn thấy câu chuyện đó, bạn không còn là người đọc số liệu nữa — bạn là người hiểu doanh nghiệp.\n\nCòn bốn bài học nữa trong chuỗi này — từ Cost Accounting đến Corporate Governance. Mỗi bài sẽ mở ra một góc nhìn mới về thế giới tài chính doanh nghiệp. Nhưng hôm nay, hãy để 18 từ vựng này lắng đọng. Hãy để chúng trở thành một phần trong cách bạn nghĩ về tiền, về giá trị, và về sự thật.\n\nChúc bạn luôn tìm thấy sự cân bằng — trong kế toán và trong cuộc sống."
                    }
                }
            ]
        }
    ]
}

# --- Validation ---
def validate(content):
    errors = []
    sessions = content.get("learningSessions", [])
    if len(sessions) != 5:
        errors.append(f"Expected 5 sessions, got {len(sessions)}")

    # Session 1-3: 10 activities each
    expected_seq_123 = ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3", "reading", "speakReading", "readAlong", "writingSentence"]
    for i in range(3):
        acts = sessions[i]["activities"]
        seq = [a["activityType"] for a in acts]
        if seq != expected_seq_123:
            errors.append(f"Session {i+1} activity sequence mismatch: {seq}")
        # Check vocabList length = 6
        for a in acts:
            if a["activityType"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"):
                vl = a["data"].get("vocabList", [])
                if len(vl) != 6:
                    errors.append(f"Session {i+1} {a['activityType']} vocabList length {len(vl)} != 6")
        # Check viewFlashcards == speakFlashcards vocabList
        vf = [a for a in acts if a["activityType"] == "viewFlashcards"][0]["data"]["vocabList"]
        sf = [a for a in acts if a["activityType"] == "speakFlashcards"][0]["data"]["vocabList"]
        if vf != sf:
            errors.append(f"Session {i+1} viewFlashcards/speakFlashcards vocabList mismatch")

    # Session 4: 7 activities
    expected_seq_4 = ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3", "writingSentence"]
    acts4 = sessions[3]["activities"]
    seq4 = [a["activityType"] for a in acts4]
    if seq4 != expected_seq_4:
        errors.append(f"Session 4 activity sequence mismatch: {seq4}")
    for a in acts4:
        if a["activityType"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"):
            vl = a["data"].get("vocabList", [])
            if len(vl) != 18:
                errors.append(f"Session 4 {a['activityType']} vocabList length {len(vl)} != 18")

    # Session 5: 6 activities
    expected_seq_5 = ["introAudio", "reading", "speakReading", "readAlong", "writingParagraph", "introAudio"]
    acts5 = sessions[4]["activities"]
    seq5 = [a["activityType"] for a in acts5]
    if seq5 != expected_seq_5:
        errors.append(f"Session 5 activity sequence mismatch: {seq5}")

    # Check all activities have activityType, title, description, data
    strip_keys = {"mp3Url", "illustrationSet", "chapterBookmarks", "segments", "whiteboardItems", "userReadingId", "lessonUniqueId", "curriculumTags", "taskId", "imageId"}
    for si, s in enumerate(sessions):
        for ai, a in enumerate(s["activities"]):
            for field in ("activityType", "title", "description", "data"):
                if field not in a:
                    errors.append(f"Session {si+1} activity {ai+1} missing '{field}'")
            # Check no strip keys
            for key in strip_keys:
                if key in a:
                    errors.append(f"Session {si+1} activity {ai+1} has strip key '{key}' at activity level")
                if key in a.get("data", {}):
                    errors.append(f"Session {si+1} activity {ai+1} has strip key '{key}' in data")

    # Check all vocabList entries are lowercase strings
    for si, s in enumerate(sessions):
        for ai, a in enumerate(s["activities"]):
            vl = a.get("data", {}).get("vocabList", None)
            if vl is not None:
                for w in vl:
                    if not isinstance(w, str) or w != w.lower():
                        errors.append(f"Session {si+1} activity {ai+1} vocabList entry '{w}' not lowercase string")

    # Check contentTypeTags
    if content.get("contentTypeTags") != []:
        errors.append(f"contentTypeTags should be [], got {content.get('contentTypeTags')}")

    return errors

errors = validate(content)
if errors:
    print("VALIDATION ERRORS:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("Validation passed!")

# --- Create curriculum ---
token = get_firebase_id_token(UID)
res = requests.post(f"{API_BASE}/curriculum/create", json={
    "firebaseIdToken": token,
    "language": "en",
    "userLanguage": "vi",
    "content": json.dumps(content)
})
res.raise_for_status()
curriculum_id = res.json()["id"]
print(f"Created: {curriculum_id}")
print(f"Title: {content['title']}")

# --- Duplicate check ---
print("\n--- Duplicate Check ---")
print(f"SELECT id, content->>'title' as title, created_at FROM curriculum")
print(f"WHERE content->>'title' = '{content['title']}' AND uid = '{UID}' ORDER BY created_at;")
