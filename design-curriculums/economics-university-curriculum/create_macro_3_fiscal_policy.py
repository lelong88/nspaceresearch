"""
Create curriculum: Fiscal Policy – Chính Sách Tài Khóa
Series B — Kinh Tế Vĩ Mô (Macroeconomics), curriculum #3
18 words | 5 sessions | surprising_fact tone | practical momentum farewell
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
W1 = ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"]
W2 = ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"]
W3 = ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Fiscal Policy – Chính Sách Tài Khóa",
    "contentTypeTags": [],
    "description": (
        "CHÍNH PHỦ MỸ CHI TIÊU HƠN 6 NGHÌN TỶ ĐÔ MỖI NĂM — NHƯNG VẪN NỢ CHỒNG NỢ. VÌ SAO?\n\n"
        "Bạn đọc tin tức về ngân sách quốc gia, thâm hụt tài khóa, gói kích thích kinh tế — "
        "nhưng khi gặp những từ như fiscal deficit, discretionary spending hay appropriation bill "
        "trong bài giảng tiếng Anh, bạn chỉ biết nhìn slide và đoán mò. "
        "Giảng viên hỏi về sự khác biệt giữa progressive và regressive taxation, "
        "bạn hiểu bằng tiếng Việt nhưng không thể diễn đạt bằng tiếng Anh.\n\n"
        "Chính sách tài khóa giống như tay lái của một chiếc xe tải khổng lồ — "
        "chính phủ dùng nó để điều hướng cả nền kinh tế, nhưng nếu bạn không đọc được bảng chỉ dẫn "
        "bằng tiếng Anh, bạn sẽ không bao giờ hiểu xe đang đi đâu.\n\n"
        "Sau khóa học này, bạn sẽ đọc được báo cáo ngân sách bằng tiếng Anh, "
        "phân biệt được mandatory và discretionary spending trong một câu, "
        "và tự tin thảo luận về fiscal stimulus hay austerity measures trong lớp học.\n\n"
        "18 từ vựng — từ fiscal đến appropriation — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy về chính sách công, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về chính sách tài khóa — "
            "công cụ mạnh nhất mà chính phủ dùng để điều hành nền kinh tế. "
            "Bạn sẽ bắt đầu với fiscal, budget, deficit, surplus, expenditure, revenue — "
            "những từ nền tảng giúp bạn đọc hiểu bất kỳ báo cáo ngân sách nào. "
            "Tiếp theo là taxation, progressive, regressive, stimulus, austerity, debt — "
            "bộ từ vựng về thuế và các chính sách can thiệp kinh tế vĩ mô. "
            "Cuối cùng, bond, treasury, allocation, discretionary, mandatory, appropriation "
            "đưa bạn vào thế giới trái phiếu chính phủ và quy trình phân bổ ngân sách. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tài liệu kinh tế vĩ mô về chính sách tài khóa — "
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
                    "description": "Chào mừng bạn đến với bài học về chính sách tài khóa — nền tảng kinh tế vĩ mô.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ ba trong chuỗi từ vựng Kinh tế vĩ mô — "
                            "chủ đề hôm nay là Chính sách tài khóa, hay trong tiếng Anh là Fiscal Policy. "
                            "Đây là cách chính phủ sử dụng thuế và chi tiêu công để tác động đến nền kinh tế. "
                            "Mỗi khi bạn nghe tin về ngân sách nhà nước, gói kích thích kinh tế, "
                            "hay chính sách thắt lưng buộc bụng, đó đều là chính sách tài khóa.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: fiscal, budget, deficit, surplus, expenditure, và revenue. "
                            "Đây là những từ bạn sẽ gặp ngay từ những bài giảng đầu tiên về kinh tế vĩ mô.\n\n"
                            "Từ đầu tiên là fiscal — tính từ — nghĩa là thuộc về tài khóa, "
                            "liên quan đến thu chi và ngân sách của chính phủ. "
                            "Ví dụ: 'The government announced a new fiscal policy to boost economic growth after the recession.' "
                            "Trong bài đọc, fiscal xuất hiện khi nói về các quyết định tài chính của chính phủ — "
                            "từ việc tăng thuế đến cắt giảm chi tiêu.\n\n"
                            "Từ thứ hai là budget — danh từ — nghĩa là ngân sách, "
                            "kế hoạch chi tiết về thu nhập và chi tiêu của chính phủ trong một khoảng thời gian. "
                            "Ví dụ: 'The national budget for this year allocates more money to education and healthcare.' "
                            "Trong bài đọc, budget là tài liệu trung tâm — "
                            "nó cho thấy chính phủ dự định thu bao nhiêu và chi bao nhiêu.\n\n"
                            "Từ thứ ba là deficit — danh từ — nghĩa là thâm hụt, "
                            "tình trạng khi chi tiêu của chính phủ vượt quá thu nhập. "
                            "Ví dụ: 'The country ran a budget deficit of fifty billion dollars because it spent more than it collected in taxes.' "
                            "Trong bài đọc, deficit mô tả khoảng cách giữa những gì chính phủ chi "
                            "và những gì chính phủ thu được — khi chi nhiều hơn thu, đó là deficit.\n\n"
                            "Từ thứ tư là surplus — danh từ — nghĩa là thặng dư, "
                            "tình trạng khi thu nhập của chính phủ vượt quá chi tiêu. "
                            "Ví dụ: 'Norway often runs a budget surplus thanks to its enormous oil revenue.' "
                            "Trong bài đọc, surplus là mặt đối lập của deficit — "
                            "khi chính phủ thu được nhiều hơn chi, phần dư ra có thể dùng để trả nợ hoặc đầu tư.\n\n"
                            "Từ thứ năm là expenditure — danh từ — nghĩa là chi tiêu, "
                            "tổng số tiền mà chính phủ chi ra cho các chương trình và dịch vụ công. "
                            "Ví dụ: 'Government expenditure on infrastructure projects creates jobs and stimulates the economy.' "
                            "Trong bài đọc, expenditure bao gồm mọi khoản chi — "
                            "từ lương công chức đến xây dựng đường cao tốc.\n\n"
                            "Từ cuối cùng là revenue — danh từ — nghĩa là doanh thu, thu nhập, "
                            "tổng số tiền mà chính phủ thu được, chủ yếu từ thuế. "
                            "Ví dụ: 'Tax revenue accounts for about ninety percent of the government's total income.' "
                            "Trong bài đọc, revenue là nguồn tiền mà chính phủ dùng để trang trải expenditure — "
                            "khi revenue thấp hơn expenditure, deficit xuất hiện.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về ngân sách và tài khóa để thấy các từ này trong ngữ cảnh thực tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ngân sách và tài khóa cơ bản",
                    "description": "Học 6 từ: fiscal, budget, deficit, surplus, expenditure, revenue",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ngân sách và tài khóa cơ bản",
                    "description": "Học 6 từ: fiscal, budget, deficit, surplus, expenditure, revenue",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ngân sách và tài khóa cơ bản",
                    "description": "Học 6 từ: fiscal, budget, deficit, surplus, expenditure, revenue",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ngân sách và tài khóa cơ bản",
                    "description": "Học 6 từ: fiscal, budget, deficit, surplus, expenditure, revenue",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ngân sách và tài khóa cơ bản",
                    "description": "Học 6 từ: fiscal, budget, deficit, surplus, expenditure, revenue",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Ngân sách và tài khóa cơ bản",
                    "description": "Every year, governments around the world face the same fundamental question: how much should we spend, and how will we pay for it?",
                    "data": {
                        "text": (
                            "Every year, governments around the world face the same fundamental question: "
                            "how much should we spend, and how will we pay for it? "
                            "The answer lies in fiscal policy — the use of government spending and taxation "
                            "to influence the economy.\n\n"
                            "At the heart of fiscal policy is the budget. "
                            "A government budget is a detailed plan that lists all expected revenue "
                            "and all planned expenditure for a given period, usually one year. "
                            "Revenue is the money the government collects, mostly through taxes. "
                            "Expenditure is the money the government spends on public services, "
                            "infrastructure, defense, education, and social programs.\n\n"
                            "When the government's revenue equals its expenditure, the budget is balanced. "
                            "But balanced budgets are rare. In most years, governments spend more than they collect. "
                            "When expenditure exceeds revenue, the result is a budget deficit. "
                            "The government must borrow money to cover the gap. "
                            "For example, if a country collects one hundred billion dollars in taxes "
                            "but spends one hundred and twenty billion, it runs a deficit of twenty billion.\n\n"
                            "On the other hand, when revenue exceeds expenditure, the government has a budget surplus. "
                            "A surplus means the government has extra money that it can use to pay down existing debt "
                            "or save for future needs. Countries like Norway have run surpluses for years "
                            "thanks to their oil revenue, building large national savings funds.\n\n"
                            "Fiscal policy is not just about numbers on a spreadsheet. "
                            "It shapes the daily lives of millions of people. "
                            "When the government increases expenditure on hospitals, more patients receive care. "
                            "When it raises taxes, workers take home less pay. "
                            "Every fiscal decision involves trade-offs — spending more in one area "
                            "often means spending less in another, or borrowing more to cover the difference.\n\n"
                            "Understanding the relationship between revenue, expenditure, deficit, and surplus "
                            "is the first step toward reading any government budget report in English. "
                            "These four concepts form the foundation of all fiscal policy analysis."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Ngân sách và tài khóa cơ bản",
                    "description": "Every year, governments around the world face the same fundamental question: how much should we spend, and how will we pay for it?",
                    "data": {
                        "text": (
                            "Every year, governments around the world face the same fundamental question: "
                            "how much should we spend, and how will we pay for it? "
                            "The answer lies in fiscal policy — the use of government spending and taxation "
                            "to influence the economy.\n\n"
                            "At the heart of fiscal policy is the budget. "
                            "A government budget is a detailed plan that lists all expected revenue "
                            "and all planned expenditure for a given period, usually one year. "
                            "Revenue is the money the government collects, mostly through taxes. "
                            "Expenditure is the money the government spends on public services, "
                            "infrastructure, defense, education, and social programs.\n\n"
                            "When the government's revenue equals its expenditure, the budget is balanced. "
                            "But balanced budgets are rare. In most years, governments spend more than they collect. "
                            "When expenditure exceeds revenue, the result is a budget deficit. "
                            "The government must borrow money to cover the gap. "
                            "For example, if a country collects one hundred billion dollars in taxes "
                            "but spends one hundred and twenty billion, it runs a deficit of twenty billion.\n\n"
                            "On the other hand, when revenue exceeds expenditure, the government has a budget surplus. "
                            "A surplus means the government has extra money that it can use to pay down existing debt "
                            "or save for future needs. Countries like Norway have run surpluses for years "
                            "thanks to their oil revenue, building large national savings funds.\n\n"
                            "Fiscal policy is not just about numbers on a spreadsheet. "
                            "It shapes the daily lives of millions of people. "
                            "When the government increases expenditure on hospitals, more patients receive care. "
                            "When it raises taxes, workers take home less pay. "
                            "Every fiscal decision involves trade-offs — spending more in one area "
                            "often means spending less in another, or borrowing more to cover the difference.\n\n"
                            "Understanding the relationship between revenue, expenditure, deficit, and surplus "
                            "is the first step toward reading any government budget report in English. "
                            "These four concepts form the foundation of all fiscal policy analysis."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ngân sách và tài khóa cơ bản",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every year, governments around the world face the same fundamental question: "
                            "how much should we spend, and how will we pay for it? "
                            "The answer lies in fiscal policy — the use of government spending and taxation "
                            "to influence the economy.\n\n"
                            "At the heart of fiscal policy is the budget. "
                            "A government budget is a detailed plan that lists all expected revenue "
                            "and all planned expenditure for a given period, usually one year. "
                            "Revenue is the money the government collects, mostly through taxes. "
                            "Expenditure is the money the government spends on public services, "
                            "infrastructure, defense, education, and social programs.\n\n"
                            "When the government's revenue equals its expenditure, the budget is balanced. "
                            "But balanced budgets are rare. In most years, governments spend more than they collect. "
                            "When expenditure exceeds revenue, the result is a budget deficit. "
                            "The government must borrow money to cover the gap. "
                            "For example, if a country collects one hundred billion dollars in taxes "
                            "but spends one hundred and twenty billion, it runs a deficit of twenty billion.\n\n"
                            "On the other hand, when revenue exceeds expenditure, the government has a budget surplus. "
                            "A surplus means the government has extra money that it can use to pay down existing debt "
                            "or save for future needs. Countries like Norway have run surpluses for years "
                            "thanks to their oil revenue, building large national savings funds.\n\n"
                            "Fiscal policy is not just about numbers on a spreadsheet. "
                            "It shapes the daily lives of millions of people. "
                            "When the government increases expenditure on hospitals, more patients receive care. "
                            "When it raises taxes, workers take home less pay. "
                            "Every fiscal decision involves trade-offs — spending more in one area "
                            "often means spending less in another, or borrowing more to cover the difference.\n\n"
                            "Understanding the relationship between revenue, expenditure, deficit, and surplus "
                            "is the first step toward reading any government budget report in English. "
                            "These four concepts form the foundation of all fiscal policy analysis."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ngân sách và tài khóa cơ bản",
                    "description": "Viết câu sử dụng 6 từ vựng về ngân sách và tài khóa.",
                    "data": {
                        "vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue"],
                        "items": [
                            {
                                "targetVocab": "fiscal",
                                "prompt": "Dùng từ 'fiscal' để viết một câu về chính sách tài khóa của chính phủ nhằm ổn định nền kinh tế. Ví dụ: The government adopted an expansionary fiscal policy by increasing public spending to create jobs during the economic downturn."
                            },
                            {
                                "targetVocab": "budget",
                                "prompt": "Dùng từ 'budget' để viết một câu về ngân sách quốc gia và cách nó phản ánh ưu tiên của chính phủ. Ví dụ: The annual budget revealed that the government plans to spend thirty percent of its funds on education and healthcare."
                            },
                            {
                                "targetVocab": "deficit",
                                "prompt": "Dùng từ 'deficit' để viết một câu về tình trạng thâm hụt ngân sách và hậu quả của nó. Ví dụ: The growing budget deficit forced the government to borrow heavily from international lenders, raising concerns about long-term debt."
                            },
                            {
                                "targetVocab": "surplus",
                                "prompt": "Dùng từ 'surplus' để viết một câu về thặng dư ngân sách và cách chính phủ sử dụng phần dư. Ví dụ: The budget surplus allowed the government to invest in a new high-speed rail project without taking on additional debt."
                            },
                            {
                                "targetVocab": "expenditure",
                                "prompt": "Dùng từ 'expenditure' để viết một câu về chi tiêu công cho một lĩnh vực cụ thể. Ví dụ: Military expenditure accounts for a significant portion of the national budget in countries facing security threats."
                            },
                            {
                                "targetVocab": "revenue",
                                "prompt": "Dùng từ 'revenue' để viết một câu về nguồn thu nhập chính của chính phủ. Ví dụ: The government's revenue from corporate taxes declined sharply after several multinational companies relocated their headquarters overseas."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về thuế và chính sách can thiệp kinh tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "fiscal — thuộc về tài khóa, budget — ngân sách, deficit — thâm hụt, "
                            "surplus — thặng dư, expenditure — chi tiêu, và revenue — thu nhập. "
                            "Bạn đã hiểu cách chính phủ lập ngân sách và điều gì xảy ra khi chi nhiều hơn thu. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào các công cụ mà chính phủ sử dụng.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: taxation, progressive, regressive, stimulus, austerity, và debt. "
                            "Những từ này giúp bạn hiểu cách chính phủ thu thuế, kích thích kinh tế, "
                            "và đối phó với khủng hoảng tài chính.\n\n"
                            "Từ đầu tiên là taxation — danh từ — nghĩa là thuế khóa, hệ thống thuế, "
                            "quá trình chính phủ thu thuế từ cá nhân và doanh nghiệp. "
                            "Ví dụ: 'Taxation is the primary source of government revenue in most countries around the world.' "
                            "Trong bài đọc, taxation là nền tảng của mọi chính sách tài khóa — "
                            "không có thuế, chính phủ không có tiền để chi tiêu.\n\n"
                            "Từ thứ hai là progressive — tính từ — nghĩa là lũy tiến, "
                            "hệ thống thuế mà người thu nhập cao trả tỷ lệ thuế cao hơn. "
                            "Ví dụ: 'Under a progressive tax system, a worker earning ten million dong per month pays a lower rate than a manager earning fifty million.' "
                            "Trong bài đọc, progressive mô tả triết lý thuế phổ biến nhất — "
                            "ai kiếm nhiều hơn thì đóng góp nhiều hơn.\n\n"
                            "Từ thứ ba là regressive — tính từ — nghĩa là lũy thoái, "
                            "hệ thống thuế mà người thu nhập thấp chịu gánh nặng thuế lớn hơn theo tỷ lệ. "
                            "Ví dụ: 'Sales taxes are considered regressive because low-income families spend a larger share of their earnings on taxed goods.' "
                            "Trong bài đọc, regressive là mặt đối lập của progressive — "
                            "thuế tiêu dùng thường mang tính regressive vì ảnh hưởng đến người nghèo nhiều hơn.\n\n"
                            "Từ thứ tư là stimulus — danh từ — nghĩa là kích thích, "
                            "gói chi tiêu hoặc cắt giảm thuế nhằm thúc đẩy tăng trưởng kinh tế. "
                            "Ví dụ: 'The government launched a massive stimulus package to help businesses survive the pandemic.' "
                            "Trong bài đọc, stimulus xuất hiện khi nền kinh tế suy thoái — "
                            "chính phủ bơm tiền vào nền kinh tế để tạo việc làm và tăng chi tiêu.\n\n"
                            "Từ thứ năm là austerity — danh từ — nghĩa là thắt lưng buộc bụng, "
                            "chính sách cắt giảm chi tiêu công và tăng thuế để giảm thâm hụt. "
                            "Ví dụ: 'Greece implemented strict austerity measures after the debt crisis, cutting public salaries and pensions.' "
                            "Trong bài đọc, austerity là mặt đối lập của stimulus — "
                            "khi nợ quá cao, chính phủ phải siết chặt chi tiêu.\n\n"
                            "Từ cuối cùng là debt — danh từ — nghĩa là nợ, "
                            "tổng số tiền mà chính phủ đã vay và chưa trả. "
                            "Ví dụ: 'The national debt has reached record levels as the government continues to borrow to fund its programs.' "
                            "Trong bài đọc, debt là hậu quả tích lũy của nhiều năm deficit — "
                            "mỗi năm chính phủ chi nhiều hơn thu, nợ lại tăng thêm.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về thuế và chính sách can thiệp kinh tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thuế và chính sách can thiệp",
                    "description": "Học 6 từ: taxation, progressive, regressive, stimulus, austerity, debt",
                    "data": {"vocabList": ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thuế và chính sách can thiệp",
                    "description": "Học 6 từ: taxation, progressive, regressive, stimulus, austerity, debt",
                    "data": {"vocabList": ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thuế và chính sách can thiệp",
                    "description": "Học 6 từ: taxation, progressive, regressive, stimulus, austerity, debt",
                    "data": {"vocabList": ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thuế và chính sách can thiệp",
                    "description": "Học 6 từ: taxation, progressive, regressive, stimulus, austerity, debt",
                    "data": {"vocabList": ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Thuế và chính sách can thiệp",
                    "description": "Học 6 từ: taxation, progressive, regressive, stimulus, austerity, debt",
                    "data": {"vocabList": ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thuế và chính sách can thiệp kinh tế",
                    "description": "Taxation is the engine that powers government spending, but not all tax systems work the same way.",
                    "data": {
                        "text": (
                            "Taxation is the engine that powers government spending, "
                            "but not all tax systems work the same way. "
                            "How a government designs its taxation system reveals a great deal "
                            "about its values and priorities.\n\n"
                            "Most modern economies use a progressive tax system for personal income. "
                            "Under a progressive system, people who earn more pay a higher percentage of their income in taxes. "
                            "For example, a worker earning twenty million dong per month might pay ten percent, "
                            "while a manager earning one hundred million pays twenty-five percent. "
                            "The idea behind progressive taxation is fairness: "
                            "those who can afford to contribute more should do so.\n\n"
                            "However, not all taxes are progressive. "
                            "Sales taxes and value-added taxes are often regressive. "
                            "A regressive tax takes a larger share of income from low-income earners "
                            "than from high-income earners. Consider a ten-percent sales tax on food. "
                            "A family earning five million dong per month spends most of its income on food, "
                            "so the tax hits them hard. A wealthy family earning fifty million "
                            "spends a much smaller share on food, so the same tax barely affects them.\n\n"
                            "Governments use fiscal policy not only to collect revenue but also to manage the economy. "
                            "When the economy slows down — when businesses close and workers lose jobs — "
                            "the government may introduce a stimulus. "
                            "A fiscal stimulus typically involves increasing government spending, "
                            "cutting taxes, or both. The goal is to put more money into the hands of consumers and businesses "
                            "so they spend more, which creates demand and helps the economy recover.\n\n"
                            "But stimulus spending often increases the deficit, which adds to the national debt. "
                            "Debt is the total amount of money the government owes to lenders — "
                            "both domestic investors and foreign governments. "
                            "When debt grows too large, lenders may demand higher interest rates, "
                            "making it even more expensive for the government to borrow.\n\n"
                            "To bring debt under control, some governments turn to austerity. "
                            "Austerity means cutting government spending and raising taxes "
                            "to reduce the deficit and slow the growth of debt. "
                            "Austerity can be painful: public services shrink, government workers lose jobs, "
                            "and citizens pay more in taxes. But supporters argue that it is necessary "
                            "to restore confidence in the government's finances.\n\n"
                            "The debate between stimulus and austerity is one of the most important "
                            "in macroeconomics. There is no simple answer — the right choice depends "
                            "on the state of the economy, the level of debt, "
                            "and the government's ability to borrow at reasonable rates."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thuế và chính sách can thiệp kinh tế",
                    "description": "Taxation is the engine that powers government spending, but not all tax systems work the same way.",
                    "data": {
                        "text": (
                            "Taxation is the engine that powers government spending, "
                            "but not all tax systems work the same way. "
                            "How a government designs its taxation system reveals a great deal "
                            "about its values and priorities.\n\n"
                            "Most modern economies use a progressive tax system for personal income. "
                            "Under a progressive system, people who earn more pay a higher percentage of their income in taxes. "
                            "For example, a worker earning twenty million dong per month might pay ten percent, "
                            "while a manager earning one hundred million pays twenty-five percent. "
                            "The idea behind progressive taxation is fairness: "
                            "those who can afford to contribute more should do so.\n\n"
                            "However, not all taxes are progressive. "
                            "Sales taxes and value-added taxes are often regressive. "
                            "A regressive tax takes a larger share of income from low-income earners "
                            "than from high-income earners. Consider a ten-percent sales tax on food. "
                            "A family earning five million dong per month spends most of its income on food, "
                            "so the tax hits them hard. A wealthy family earning fifty million "
                            "spends a much smaller share on food, so the same tax barely affects them.\n\n"
                            "Governments use fiscal policy not only to collect revenue but also to manage the economy. "
                            "When the economy slows down — when businesses close and workers lose jobs — "
                            "the government may introduce a stimulus. "
                            "A fiscal stimulus typically involves increasing government spending, "
                            "cutting taxes, or both. The goal is to put more money into the hands of consumers and businesses "
                            "so they spend more, which creates demand and helps the economy recover.\n\n"
                            "But stimulus spending often increases the deficit, which adds to the national debt. "
                            "Debt is the total amount of money the government owes to lenders — "
                            "both domestic investors and foreign governments. "
                            "When debt grows too large, lenders may demand higher interest rates, "
                            "making it even more expensive for the government to borrow.\n\n"
                            "To bring debt under control, some governments turn to austerity. "
                            "Austerity means cutting government spending and raising taxes "
                            "to reduce the deficit and slow the growth of debt. "
                            "Austerity can be painful: public services shrink, government workers lose jobs, "
                            "and citizens pay more in taxes. But supporters argue that it is necessary "
                            "to restore confidence in the government's finances.\n\n"
                            "The debate between stimulus and austerity is one of the most important "
                            "in macroeconomics. There is no simple answer — the right choice depends "
                            "on the state of the economy, the level of debt, "
                            "and the government's ability to borrow at reasonable rates."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thuế và chính sách can thiệp kinh tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Taxation is the engine that powers government spending, "
                            "but not all tax systems work the same way. "
                            "How a government designs its taxation system reveals a great deal "
                            "about its values and priorities.\n\n"
                            "Most modern economies use a progressive tax system for personal income. "
                            "Under a progressive system, people who earn more pay a higher percentage of their income in taxes. "
                            "For example, a worker earning twenty million dong per month might pay ten percent, "
                            "while a manager earning one hundred million pays twenty-five percent. "
                            "The idea behind progressive taxation is fairness: "
                            "those who can afford to contribute more should do so.\n\n"
                            "However, not all taxes are progressive. "
                            "Sales taxes and value-added taxes are often regressive. "
                            "A regressive tax takes a larger share of income from low-income earners "
                            "than from high-income earners. Consider a ten-percent sales tax on food. "
                            "A family earning five million dong per month spends most of its income on food, "
                            "so the tax hits them hard. A wealthy family earning fifty million "
                            "spends a much smaller share on food, so the same tax barely affects them.\n\n"
                            "Governments use fiscal policy not only to collect revenue but also to manage the economy. "
                            "When the economy slows down — when businesses close and workers lose jobs — "
                            "the government may introduce a stimulus. "
                            "A fiscal stimulus typically involves increasing government spending, "
                            "cutting taxes, or both. The goal is to put more money into the hands of consumers and businesses "
                            "so they spend more, which creates demand and helps the economy recover.\n\n"
                            "But stimulus spending often increases the deficit, which adds to the national debt. "
                            "Debt is the total amount of money the government owes to lenders — "
                            "both domestic investors and foreign governments. "
                            "When debt grows too large, lenders may demand higher interest rates, "
                            "making it even more expensive for the government to borrow.\n\n"
                            "To bring debt under control, some governments turn to austerity. "
                            "Austerity means cutting government spending and raising taxes "
                            "to reduce the deficit and slow the growth of debt. "
                            "Austerity can be painful: public services shrink, government workers lose jobs, "
                            "and citizens pay more in taxes. But supporters argue that it is necessary "
                            "to restore confidence in the government's finances.\n\n"
                            "The debate between stimulus and austerity is one of the most important "
                            "in macroeconomics. There is no simple answer — the right choice depends "
                            "on the state of the economy, the level of debt, "
                            "and the government's ability to borrow at reasonable rates."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thuế và chính sách can thiệp kinh tế",
                    "description": "Viết câu sử dụng 6 từ vựng về thuế và chính sách kinh tế.",
                    "data": {
                        "vocabList": ["taxation", "progressive", "regressive", "stimulus", "austerity", "debt"],
                        "items": [
                            {
                                "targetVocab": "taxation",
                                "prompt": "Dùng từ 'taxation' để viết một câu về vai trò của hệ thống thuế trong việc tài trợ cho dịch vụ công. Ví dụ: Without effective taxation, the government cannot fund public schools, hospitals, or the police force that citizens depend on every day."
                            },
                            {
                                "targetVocab": "progressive",
                                "prompt": "Dùng từ 'progressive' để viết một câu về hệ thống thuế lũy tiến và tác động đến các nhóm thu nhập khác nhau. Ví dụ: Vietnam uses a progressive income tax with rates ranging from five percent for the lowest bracket to thirty-five percent for the highest earners."
                            },
                            {
                                "targetVocab": "regressive",
                                "prompt": "Dùng từ 'regressive' để viết một câu về loại thuế mang tính lũy thoái và ảnh hưởng đến người thu nhập thấp. Ví dụ: Critics argue that the value-added tax is regressive because it takes a bigger bite out of the budgets of low-income households."
                            },
                            {
                                "targetVocab": "stimulus",
                                "prompt": "Dùng từ 'stimulus' để viết một câu về gói kích thích kinh tế trong thời kỳ suy thoái. Ví dụ: The government's stimulus package included direct cash payments to families and low-interest loans for small businesses struggling to survive."
                            },
                            {
                                "targetVocab": "austerity",
                                "prompt": "Dùng từ 'austerity' để viết một câu về chính sách thắt lưng buộc bụng và phản ứng của người dân. Ví dụ: The austerity measures sparked widespread protests as citizens faced cuts to healthcare, education, and public transportation."
                            },
                            {
                                "targetVocab": "debt",
                                "prompt": "Dùng từ 'debt' để viết một câu về nợ quốc gia và mối lo ngại về tính bền vững. Ví dụ: Economists warn that the country's debt has reached a level where interest payments alone consume fifteen percent of the annual budget."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về trái phiếu chính phủ và phân bổ ngân sách.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: fiscal, budget, deficit, surplus, expenditure, revenue — "
                            "những khái niệm cơ bản về ngân sách và tài khóa. "
                            "Trong phần 2, bạn đã học thêm taxation, progressive, regressive, stimulus, austerity, debt — "
                            "giúp bạn hiểu cách chính phủ thu thuế và can thiệp vào nền kinh tế.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh quan trọng khác: "
                            "chính phủ vay tiền bằng cách nào, và ngân sách được phân bổ ra sao? "
                            "Bạn sẽ học 6 từ mới: bond, treasury, allocation, discretionary, mandatory, và appropriation.\n\n"
                            "Từ đầu tiên là bond — danh từ — nghĩa là trái phiếu, "
                            "một loại giấy nợ mà chính phủ phát hành để vay tiền từ nhà đầu tư. "
                            "Ví dụ: 'The government issued ten-year bonds to raise money for rebuilding roads and bridges after the flood.' "
                            "Trong bài đọc, bond là công cụ chính mà chính phủ dùng để tài trợ cho deficit — "
                            "thay vì in tiền, chính phủ bán bond cho nhà đầu tư và hứa trả lại kèm lãi suất.\n\n"
                            "Từ thứ hai là treasury — danh từ — nghĩa là kho bạc, bộ tài chính, "
                            "cơ quan quản lý tài chính quốc gia và phát hành trái phiếu chính phủ. "
                            "Ví dụ: 'The Treasury Department announced that it would sell fifty billion dollars in new bonds this quarter.' "
                            "Trong bài đọc, treasury xuất hiện khi nói về cơ quan chịu trách nhiệm "
                            "quản lý tiền của quốc gia và phát hành trái phiếu.\n\n"
                            "Từ thứ ba là allocation — danh từ — nghĩa là sự phân bổ, "
                            "cách chia nguồn lực hoặc ngân sách cho các mục đích khác nhau. "
                            "Ví dụ: 'The allocation of funds between defense and education is always a politically sensitive decision.' "
                            "Trong bài đọc, allocation mô tả quá trình quyết định mỗi lĩnh vực "
                            "nhận được bao nhiêu tiền từ ngân sách.\n\n"
                            "Từ thứ tư là discretionary — tính từ — nghĩa là tùy ý, không bắt buộc, "
                            "khoản chi tiêu mà chính phủ có thể tăng hoặc giảm mỗi năm. "
                            "Ví dụ: 'Discretionary spending on scientific research can be cut when the government needs to reduce the deficit.' "
                            "Trong bài đọc, discretionary mô tả phần ngân sách mà quốc hội "
                            "có quyền điều chỉnh hàng năm — khác với chi tiêu bắt buộc.\n\n"
                            "Từ thứ năm là mandatory — tính từ — nghĩa là bắt buộc, "
                            "khoản chi tiêu mà chính phủ phải thực hiện theo luật định. "
                            "Ví dụ: 'Mandatory spending on social security and healthcare makes up more than sixty percent of the total budget.' "
                            "Trong bài đọc, mandatory là mặt đối lập của discretionary — "
                            "những khoản chi này được luật quy định và không thể cắt giảm dễ dàng.\n\n"
                            "Từ cuối cùng là appropriation — danh từ — nghĩa là sự cấp phát ngân sách, "
                            "quyết định chính thức của quốc hội về việc chi tiền cho một mục đích cụ thể. "
                            "Ví dụ: 'Congress passed an appropriation bill that set aside two billion dollars for disaster relief.' "
                            "Trong bài đọc, appropriation là bước cuối cùng trong quy trình ngân sách — "
                            "khi quốc hội chính thức phê duyệt việc chi tiền.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về trái phiếu và phân bổ ngân sách nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Trái phiếu và phân bổ ngân sách",
                    "description": "Học 6 từ: bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Trái phiếu và phân bổ ngân sách",
                    "description": "Học 6 từ: bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Trái phiếu và phân bổ ngân sách",
                    "description": "Học 6 từ: bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Trái phiếu và phân bổ ngân sách",
                    "description": "Học 6 từ: bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Trái phiếu và phân bổ ngân sách",
                    "description": "Học 6 từ: bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Trái phiếu chính phủ và quy trình ngân sách",
                    "description": "When a government spends more than it collects in taxes, it needs to borrow the difference.",
                    "data": {
                        "text": (
                            "When a government spends more than it collects in taxes, it needs to borrow the difference. "
                            "The most common way governments borrow is by issuing bonds. "
                            "A bond is essentially a promise: the government takes your money today "
                            "and agrees to pay it back with interest on a future date.\n\n"
                            "In many countries, the treasury is the government agency responsible for managing public finances. "
                            "The treasury collects taxes, pays the government's bills, and issues bonds "
                            "when the government needs to borrow. In the United States, "
                            "Treasury bonds are considered one of the safest investments in the world "
                            "because the government has never failed to repay its debts.\n\n"
                            "But borrowing is only part of the story. "
                            "The real challenge of fiscal policy lies in how the government decides to spend its money. "
                            "This process is called budget allocation — the division of available funds "
                            "among competing priorities like defense, education, healthcare, and infrastructure.\n\n"
                            "Government spending falls into two broad categories. "
                            "Mandatory spending is required by existing laws. "
                            "Social security payments, government pensions, and interest on the national debt "
                            "are all mandatory — the government must pay them regardless of the economic situation. "
                            "In many countries, mandatory spending accounts for more than half of the total budget.\n\n"
                            "Discretionary spending, on the other hand, is the portion of the budget "
                            "that lawmakers can adjust each year. "
                            "Funding for scientific research, national parks, foreign aid, "
                            "and military equipment all fall under discretionary spending. "
                            "When governments face pressure to reduce the deficit, "
                            "discretionary programs are usually the first to face cuts.\n\n"
                            "The formal process of approving government spending is called appropriation. "
                            "In a democratic system, the legislature — such as a parliament or congress — "
                            "must pass an appropriation bill before any money can be spent. "
                            "This process ensures that elected representatives, not just government officials, "
                            "have a say in how public money is used.\n\n"
                            "The allocation of a national budget reflects a society's priorities. "
                            "A country that spends heavily on education signals that it values human capital. "
                            "A country that increases military spending may be responding to security threats. "
                            "Every appropriation decision is a statement about what a nation considers most important."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Trái phiếu chính phủ và quy trình ngân sách",
                    "description": "When a government spends more than it collects in taxes, it needs to borrow the difference.",
                    "data": {
                        "text": (
                            "When a government spends more than it collects in taxes, it needs to borrow the difference. "
                            "The most common way governments borrow is by issuing bonds. "
                            "A bond is essentially a promise: the government takes your money today "
                            "and agrees to pay it back with interest on a future date.\n\n"
                            "In many countries, the treasury is the government agency responsible for managing public finances. "
                            "The treasury collects taxes, pays the government's bills, and issues bonds "
                            "when the government needs to borrow. In the United States, "
                            "Treasury bonds are considered one of the safest investments in the world "
                            "because the government has never failed to repay its debts.\n\n"
                            "But borrowing is only part of the story. "
                            "The real challenge of fiscal policy lies in how the government decides to spend its money. "
                            "This process is called budget allocation — the division of available funds "
                            "among competing priorities like defense, education, healthcare, and infrastructure.\n\n"
                            "Government spending falls into two broad categories. "
                            "Mandatory spending is required by existing laws. "
                            "Social security payments, government pensions, and interest on the national debt "
                            "are all mandatory — the government must pay them regardless of the economic situation. "
                            "In many countries, mandatory spending accounts for more than half of the total budget.\n\n"
                            "Discretionary spending, on the other hand, is the portion of the budget "
                            "that lawmakers can adjust each year. "
                            "Funding for scientific research, national parks, foreign aid, "
                            "and military equipment all fall under discretionary spending. "
                            "When governments face pressure to reduce the deficit, "
                            "discretionary programs are usually the first to face cuts.\n\n"
                            "The formal process of approving government spending is called appropriation. "
                            "In a democratic system, the legislature — such as a parliament or congress — "
                            "must pass an appropriation bill before any money can be spent. "
                            "This process ensures that elected representatives, not just government officials, "
                            "have a say in how public money is used.\n\n"
                            "The allocation of a national budget reflects a society's priorities. "
                            "A country that spends heavily on education signals that it values human capital. "
                            "A country that increases military spending may be responding to security threats. "
                            "Every appropriation decision is a statement about what a nation considers most important."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Trái phiếu chính phủ và quy trình ngân sách",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When a government spends more than it collects in taxes, it needs to borrow the difference. "
                            "The most common way governments borrow is by issuing bonds. "
                            "A bond is essentially a promise: the government takes your money today "
                            "and agrees to pay it back with interest on a future date.\n\n"
                            "In many countries, the treasury is the government agency responsible for managing public finances. "
                            "The treasury collects taxes, pays the government's bills, and issues bonds "
                            "when the government needs to borrow. In the United States, "
                            "Treasury bonds are considered one of the safest investments in the world "
                            "because the government has never failed to repay its debts.\n\n"
                            "But borrowing is only part of the story. "
                            "The real challenge of fiscal policy lies in how the government decides to spend its money. "
                            "This process is called budget allocation — the division of available funds "
                            "among competing priorities like defense, education, healthcare, and infrastructure.\n\n"
                            "Government spending falls into two broad categories. "
                            "Mandatory spending is required by existing laws. "
                            "Social security payments, government pensions, and interest on the national debt "
                            "are all mandatory — the government must pay them regardless of the economic situation. "
                            "In many countries, mandatory spending accounts for more than half of the total budget.\n\n"
                            "Discretionary spending, on the other hand, is the portion of the budget "
                            "that lawmakers can adjust each year. "
                            "Funding for scientific research, national parks, foreign aid, "
                            "and military equipment all fall under discretionary spending. "
                            "When governments face pressure to reduce the deficit, "
                            "discretionary programs are usually the first to face cuts.\n\n"
                            "The formal process of approving government spending is called appropriation. "
                            "In a democratic system, the legislature — such as a parliament or congress — "
                            "must pass an appropriation bill before any money can be spent. "
                            "This process ensures that elected representatives, not just government officials, "
                            "have a say in how public money is used.\n\n"
                            "The allocation of a national budget reflects a society's priorities. "
                            "A country that spends heavily on education signals that it values human capital. "
                            "A country that increases military spending may be responding to security threats. "
                            "Every appropriation decision is a statement about what a nation considers most important."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Trái phiếu và phân bổ ngân sách",
                    "description": "Viết câu sử dụng 6 từ vựng về trái phiếu và ngân sách.",
                    "data": {
                        "vocabList": ["bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"],
                        "items": [
                            {
                                "targetVocab": "bond",
                                "prompt": "Dùng từ 'bond' để viết một câu về cách chính phủ phát hành trái phiếu để huy động vốn. Ví dụ: The government sold five-year bonds with a three-percent interest rate to finance the construction of a new international airport."
                            },
                            {
                                "targetVocab": "treasury",
                                "prompt": "Dùng từ 'treasury' để viết một câu về vai trò của kho bạc trong quản lý tài chính quốc gia. Ví dụ: The treasury reported that tax collections exceeded expectations this quarter, reducing the need to issue additional bonds."
                            },
                            {
                                "targetVocab": "allocation",
                                "prompt": "Dùng từ 'allocation' để viết một câu về cách ngân sách được phân bổ giữa các lĩnh vực khác nhau. Ví dụ: The allocation of twenty percent of the national budget to education reflects the government's commitment to building human capital."
                            },
                            {
                                "targetVocab": "discretionary",
                                "prompt": "Dùng từ 'discretionary' để viết một câu về khoản chi tiêu tùy ý mà chính phủ có thể điều chỉnh. Ví dụ: Discretionary funding for space exploration was reduced by half when the government shifted its priorities to pandemic response."
                            },
                            {
                                "targetVocab": "mandatory",
                                "prompt": "Dùng từ 'mandatory' để viết một câu về khoản chi tiêu bắt buộc theo luật định. Ví dụ: Mandatory spending on pension payments continues to grow each year as the population ages and more workers reach retirement."
                            },
                            {
                                "targetVocab": "appropriation",
                                "prompt": "Dùng từ 'appropriation' để viết một câu về quy trình phê duyệt ngân sách của quốc hội. Ví dụ: The appropriation bill for the new fiscal year was delayed by three months due to disagreements between political parties over defense spending."
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
                    "description": "Ôn lại toàn bộ 18 từ vựng về chính sách tài khóa.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Chính sách tài khóa. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "fiscal — thuộc về tài khóa, budget — ngân sách, deficit — thâm hụt, "
                            "surplus — thặng dư, expenditure — chi tiêu, và revenue — thu nhập. "
                            "Đây là bộ khung cơ bản để hiểu bất kỳ báo cáo ngân sách nào.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "taxation — thuế khóa, progressive — lũy tiến, regressive — lũy thoái, "
                            "stimulus — kích thích kinh tế, austerity — thắt lưng buộc bụng, và debt — nợ. "
                            "Những từ này giúp bạn phân tích cách chính phủ thu thuế và can thiệp vào nền kinh tế.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "bond — trái phiếu, treasury — kho bạc, allocation — phân bổ, "
                            "discretionary — tùy ý, mandatory — bắt buộc, và appropriation — cấp phát ngân sách. "
                            "Đây là những từ về cách chính phủ vay tiền và phân bổ ngân sách.\n\n"
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
                    "description": "Học 18 từ: fiscal, budget, deficit, surplus, expenditure, revenue, taxation, progressive, regressive, stimulus, austerity, debt, bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: fiscal, budget, deficit, surplus, expenditure, revenue, taxation, progressive, regressive, stimulus, austerity, debt, bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: fiscal, budget, deficit, surplus, expenditure, revenue, taxation, progressive, regressive, stimulus, austerity, debt, bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: fiscal, budget, deficit, surplus, expenditure, revenue, taxation, progressive, regressive, stimulus, austerity, debt, bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: fiscal, budget, deficit, surplus, expenditure, revenue, taxation, progressive, regressive, stimulus, austerity, debt, bond, treasury, allocation, discretionary, mandatory, appropriation",
                    "data": {"vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng chính sách tài khóa",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"],
                        "items": [
                            {
                                "targetVocab": "fiscal",
                                "prompt": "Dùng từ 'fiscal' để viết một câu về năm tài khóa và chu kỳ ngân sách của chính phủ. Ví dụ: The fiscal year in Vietnam runs from January to December, and the government must submit its budget plan to the National Assembly before it begins."
                            },
                            {
                                "targetVocab": "budget",
                                "prompt": "Dùng từ 'budget' để viết một câu về quá trình lập ngân sách và các bên tham gia. Ví dụ: The budget proposal went through months of debate in parliament before lawmakers finally agreed on how to divide funds among ministries."
                            },
                            {
                                "targetVocab": "deficit",
                                "prompt": "Dùng từ 'deficit' để viết một câu về nguyên nhân dẫn đến thâm hụt ngân sách. Ví dụ: The deficit widened dramatically during the pandemic because tax revenue fell while government spending on healthcare and relief programs soared."
                            },
                            {
                                "targetVocab": "surplus",
                                "prompt": "Dùng từ 'surplus' để viết một câu về cách một quốc gia đạt được thặng dư ngân sách. Ví dụ: Singapore has maintained a budget surplus for decades by keeping government expenditure low and attracting foreign investment that generates strong tax revenue."
                            },
                            {
                                "targetVocab": "expenditure",
                                "prompt": "Dùng từ 'expenditure' để viết một câu so sánh chi tiêu công giữa hai lĩnh vực. Ví dụ: Government expenditure on infrastructure in developing countries often exceeds spending on social welfare because roads and ports are seen as essential for economic growth."
                            },
                            {
                                "targetVocab": "revenue",
                                "prompt": "Dùng từ 'revenue' để viết một câu về nguồn thu nhập đa dạng của chính phủ. Ví dụ: Beyond income taxes, the government collects revenue from import duties, property taxes, and fees for public services like vehicle registration."
                            },
                            {
                                "targetVocab": "taxation",
                                "prompt": "Dùng từ 'taxation' để viết một câu về cải cách thuế và tác động đến doanh nghiệp. Ví dụ: The new taxation reform simplified the corporate tax code, reducing the number of tax brackets from seven to three and lowering compliance costs for small businesses."
                            },
                            {
                                "targetVocab": "progressive",
                                "prompt": "Dùng từ 'progressive' để viết một câu về lý do ủng hộ hệ thống thuế lũy tiến. Ví dụ: Supporters of progressive taxation argue that wealthy individuals benefit more from public infrastructure and should therefore contribute a larger share of their income."
                            },
                            {
                                "targetVocab": "regressive",
                                "prompt": "Dùng từ 'regressive' để viết một câu về tác động của thuế lũy thoái đến người thu nhập thấp. Ví dụ: The government introduced food vouchers to offset the regressive impact of the new sales tax on families living below the poverty line."
                            },
                            {
                                "targetVocab": "stimulus",
                                "prompt": "Dùng từ 'stimulus' để viết một câu về hiệu quả của gói kích thích kinh tế. Ví dụ: The stimulus program created over two hundred thousand jobs in the construction sector by funding new highway and bridge projects across the country."
                            },
                            {
                                "targetVocab": "austerity",
                                "prompt": "Dùng từ 'austerity' để viết một câu về hậu quả xã hội của chính sách thắt lưng buộc bụng. Ví dụ: Years of austerity left public hospitals understaffed and underfunded, leading to longer wait times and declining quality of care."
                            },
                            {
                                "targetVocab": "debt",
                                "prompt": "Dùng từ 'debt' để viết một câu về mối quan hệ giữa nợ quốc gia và tăng trưởng kinh tế. Ví dụ: Some economists argue that moderate levels of government debt can actually support growth by funding productive investments in education and technology."
                            },
                            {
                                "targetVocab": "bond",
                                "prompt": "Dùng từ 'bond' để viết một câu về nhà đầu tư mua trái phiếu chính phủ. Ví dụ: Pension funds and insurance companies are among the largest buyers of government bonds because they need safe, predictable returns over long periods."
                            },
                            {
                                "targetVocab": "treasury",
                                "prompt": "Dùng từ 'treasury' để viết một câu về hoạt động phát hành trái phiếu của kho bạc. Ví dụ: The treasury held its quarterly bond auction and received bids worth three times the amount offered, signaling strong investor confidence."
                            },
                            {
                                "targetVocab": "allocation",
                                "prompt": "Dùng từ 'allocation' để viết một câu về tranh luận chính trị xung quanh phân bổ ngân sách. Ví dụ: The allocation of emergency funds became a heated political debate, with some lawmakers demanding more money for flood relief and others prioritizing economic recovery."
                            },
                            {
                                "targetVocab": "discretionary",
                                "prompt": "Dùng từ 'discretionary' để viết một câu về khoản chi tiêu tùy ý bị cắt giảm trong thời kỳ khó khăn. Ví dụ: Discretionary spending on arts and cultural programs was the first casualty when the government announced budget cuts to reduce the growing deficit."
                            },
                            {
                                "targetVocab": "mandatory",
                                "prompt": "Dùng từ 'mandatory' để viết một câu về thách thức của chi tiêu bắt buộc ngày càng tăng. Ví dụ: As the population ages, mandatory spending on healthcare and pensions is projected to consume seventy percent of the budget within the next decade."
                            },
                            {
                                "targetVocab": "appropriation",
                                "prompt": "Dùng từ 'appropriation' để viết một câu về quy trình phê duyệt ngân sách trong hệ thống dân chủ. Ví dụ: The appropriation process requires each government department to justify its spending requests before a legislative committee that reviews every line item."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về chính sách tài khóa.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về chính sách tài khóa — từ ngân sách cơ bản "
                            "đến trái phiếu chính phủ và quy trình phân bổ ngân sách.\n\n"
                            "Bạn sẽ gặp lại fiscal, budget, deficit, surplus, expenditure, revenue "
                            "trong phần mở đầu về cơ chế ngân sách. "
                            "Tiếp theo, taxation, progressive, regressive, stimulus, austerity, debt "
                            "sẽ giúp bạn hiểu sâu hơn về cách chính phủ can thiệp vào nền kinh tế. "
                            "Và cuối cùng, bond, treasury, allocation, discretionary, mandatory, appropriation "
                            "sẽ đưa bạn vào thế giới tài chính công và quy trình lập pháp.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chính sách tài khóa — Bức tranh toàn cảnh",
                    "description": "Fiscal policy is one of the most powerful tools a government has to shape the economy.",
                    "data": {
                        "text": (
                            "Fiscal policy is one of the most powerful tools a government has to shape the economy. "
                            "Through decisions about taxation and expenditure, governments influence employment, "
                            "growth, and the distribution of wealth across society. "
                            "Understanding how fiscal policy works requires knowing how governments raise money, "
                            "how they spend it, and what happens when the two do not match.\n\n"
                            "Every fiscal year, the government prepares a budget — "
                            "a comprehensive plan that estimates how much revenue it expects to collect "
                            "and how much expenditure it plans to make. "
                            "Revenue comes primarily from taxation: income taxes paid by workers, "
                            "corporate taxes paid by businesses, and consumption taxes paid by shoppers. "
                            "Most developed countries use a progressive income tax system, "
                            "where higher earners pay a larger percentage of their income. "
                            "This is designed to distribute the tax burden fairly. "
                            "However, consumption taxes like the value-added tax tend to be regressive, "
                            "taking a proportionally larger bite from the budgets of lower-income families.\n\n"
                            "On the spending side, the budget is divided into two main categories. "
                            "Mandatory spending covers programs required by law — "
                            "social security, government pensions, and interest payments on the national debt. "
                            "These obligations cannot be easily changed without new legislation. "
                            "Discretionary spending covers everything else: defense, education, "
                            "scientific research, infrastructure, and foreign aid. "
                            "Lawmakers debate the allocation of discretionary funds every year, "
                            "deciding which programs deserve more money and which should be cut.\n\n"
                            "The formal process of approving spending is called appropriation. "
                            "In democratic systems, the legislature must pass appropriation bills "
                            "that authorize the government to spend money on specific programs. "
                            "Without an appropriation, no government agency can legally spend a single dollar. "
                            "This process gives elected representatives control over public finances "
                            "and ensures accountability.\n\n"
                            "When the government's expenditure exceeds its revenue, the result is a deficit. "
                            "To cover the gap, the treasury issues bonds — "
                            "financial instruments that allow the government to borrow from investors. "
                            "A bond is a promise to repay the borrowed amount plus interest on a future date. "
                            "Investors buy bonds because they are considered safe, "
                            "especially those issued by stable governments. "
                            "The accumulated total of all past deficits becomes the national debt.\n\n"
                            "When the economy enters a recession, governments often respond with a fiscal stimulus. "
                            "A stimulus package may include increased spending on public works, "
                            "tax cuts for businesses and consumers, or direct payments to households. "
                            "The goal is to inject money into the economy, create jobs, "
                            "and encourage spending. During the global financial crisis and the pandemic, "
                            "many governments launched massive stimulus programs "
                            "that added trillions of dollars to their national debt.\n\n"
                            "When debt reaches levels that worry investors and policymakers, "
                            "governments may shift to austerity. "
                            "Austerity involves cutting expenditure and raising taxes "
                            "to reduce the deficit and slow the growth of debt. "
                            "While austerity can restore fiscal discipline, "
                            "it often comes at a social cost: reduced public services, "
                            "higher unemployment, and slower economic growth.\n\n"
                            "The tension between stimulus and austerity defines much of modern fiscal debate. "
                            "Should the government spend more to help the economy grow, "
                            "even if it means higher debt? Or should it cut spending to keep finances sustainable, "
                            "even if it means short-term pain? "
                            "The answer depends on the allocation of priorities, "
                            "the level of existing debt, and the willingness of investors "
                            "to keep buying government bonds.\n\n"
                            "In the rare case when revenue exceeds expenditure, "
                            "the government enjoys a budget surplus. "
                            "A surplus can be used to pay down debt, build reserve funds, "
                            "or invest in long-term projects. "
                            "But surpluses are uncommon — most governments operate with some level of deficit, "
                            "relying on the bond market and the treasury to manage their borrowing needs.\n\n"
                            "Fiscal policy is not just an abstract concept studied in textbooks. "
                            "Every appropriation bill, every tax reform, every decision about mandatory "
                            "versus discretionary spending affects real people — "
                            "the teacher whose salary depends on the education budget, "
                            "the retiree whose pension is a mandatory obligation, "
                            "the entrepreneur whose business benefits from a stimulus tax cut. "
                            "Understanding fiscal policy means understanding how governments "
                            "make the choices that shape our daily lives."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chính sách tài khóa — Bức tranh toàn cảnh",
                    "description": "Fiscal policy is one of the most powerful tools a government has to shape the economy.",
                    "data": {
                        "text": (
                            "Fiscal policy is one of the most powerful tools a government has to shape the economy. "
                            "Through decisions about taxation and expenditure, governments influence employment, "
                            "growth, and the distribution of wealth across society. "
                            "Understanding how fiscal policy works requires knowing how governments raise money, "
                            "how they spend it, and what happens when the two do not match.\n\n"
                            "Every fiscal year, the government prepares a budget — "
                            "a comprehensive plan that estimates how much revenue it expects to collect "
                            "and how much expenditure it plans to make. "
                            "Revenue comes primarily from taxation: income taxes paid by workers, "
                            "corporate taxes paid by businesses, and consumption taxes paid by shoppers. "
                            "Most developed countries use a progressive income tax system, "
                            "where higher earners pay a larger percentage of their income. "
                            "This is designed to distribute the tax burden fairly. "
                            "However, consumption taxes like the value-added tax tend to be regressive, "
                            "taking a proportionally larger bite from the budgets of lower-income families.\n\n"
                            "On the spending side, the budget is divided into two main categories. "
                            "Mandatory spending covers programs required by law — "
                            "social security, government pensions, and interest payments on the national debt. "
                            "These obligations cannot be easily changed without new legislation. "
                            "Discretionary spending covers everything else: defense, education, "
                            "scientific research, infrastructure, and foreign aid. "
                            "Lawmakers debate the allocation of discretionary funds every year, "
                            "deciding which programs deserve more money and which should be cut.\n\n"
                            "The formal process of approving spending is called appropriation. "
                            "In democratic systems, the legislature must pass appropriation bills "
                            "that authorize the government to spend money on specific programs. "
                            "Without an appropriation, no government agency can legally spend a single dollar. "
                            "This process gives elected representatives control over public finances "
                            "and ensures accountability.\n\n"
                            "When the government's expenditure exceeds its revenue, the result is a deficit. "
                            "To cover the gap, the treasury issues bonds — "
                            "financial instruments that allow the government to borrow from investors. "
                            "A bond is a promise to repay the borrowed amount plus interest on a future date. "
                            "Investors buy bonds because they are considered safe, "
                            "especially those issued by stable governments. "
                            "The accumulated total of all past deficits becomes the national debt.\n\n"
                            "When the economy enters a recession, governments often respond with a fiscal stimulus. "
                            "A stimulus package may include increased spending on public works, "
                            "tax cuts for businesses and consumers, or direct payments to households. "
                            "The goal is to inject money into the economy, create jobs, "
                            "and encourage spending. During the global financial crisis and the pandemic, "
                            "many governments launched massive stimulus programs "
                            "that added trillions of dollars to their national debt.\n\n"
                            "When debt reaches levels that worry investors and policymakers, "
                            "governments may shift to austerity. "
                            "Austerity involves cutting expenditure and raising taxes "
                            "to reduce the deficit and slow the growth of debt. "
                            "While austerity can restore fiscal discipline, "
                            "it often comes at a social cost: reduced public services, "
                            "higher unemployment, and slower economic growth.\n\n"
                            "The tension between stimulus and austerity defines much of modern fiscal debate. "
                            "Should the government spend more to help the economy grow, "
                            "even if it means higher debt? Or should it cut spending to keep finances sustainable, "
                            "even if it means short-term pain? "
                            "The answer depends on the allocation of priorities, "
                            "the level of existing debt, and the willingness of investors "
                            "to keep buying government bonds.\n\n"
                            "In the rare case when revenue exceeds expenditure, "
                            "the government enjoys a budget surplus. "
                            "A surplus can be used to pay down debt, build reserve funds, "
                            "or invest in long-term projects. "
                            "But surpluses are uncommon — most governments operate with some level of deficit, "
                            "relying on the bond market and the treasury to manage their borrowing needs.\n\n"
                            "Fiscal policy is not just an abstract concept studied in textbooks. "
                            "Every appropriation bill, every tax reform, every decision about mandatory "
                            "versus discretionary spending affects real people — "
                            "the teacher whose salary depends on the education budget, "
                            "the retiree whose pension is a mandatory obligation, "
                            "the entrepreneur whose business benefits from a stimulus tax cut. "
                            "Understanding fiscal policy means understanding how governments "
                            "make the choices that shape our daily lives."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chính sách tài khóa — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Fiscal policy is one of the most powerful tools a government has to shape the economy. "
                            "Through decisions about taxation and expenditure, governments influence employment, "
                            "growth, and the distribution of wealth across society. "
                            "Understanding how fiscal policy works requires knowing how governments raise money, "
                            "how they spend it, and what happens when the two do not match.\n\n"
                            "Every fiscal year, the government prepares a budget — "
                            "a comprehensive plan that estimates how much revenue it expects to collect "
                            "and how much expenditure it plans to make. "
                            "Revenue comes primarily from taxation: income taxes paid by workers, "
                            "corporate taxes paid by businesses, and consumption taxes paid by shoppers. "
                            "Most developed countries use a progressive income tax system, "
                            "where higher earners pay a larger percentage of their income. "
                            "This is designed to distribute the tax burden fairly. "
                            "However, consumption taxes like the value-added tax tend to be regressive, "
                            "taking a proportionally larger bite from the budgets of lower-income families.\n\n"
                            "On the spending side, the budget is divided into two main categories. "
                            "Mandatory spending covers programs required by law — "
                            "social security, government pensions, and interest payments on the national debt. "
                            "These obligations cannot be easily changed without new legislation. "
                            "Discretionary spending covers everything else: defense, education, "
                            "scientific research, infrastructure, and foreign aid. "
                            "Lawmakers debate the allocation of discretionary funds every year, "
                            "deciding which programs deserve more money and which should be cut.\n\n"
                            "The formal process of approving spending is called appropriation. "
                            "In democratic systems, the legislature must pass appropriation bills "
                            "that authorize the government to spend money on specific programs. "
                            "Without an appropriation, no government agency can legally spend a single dollar. "
                            "This process gives elected representatives control over public finances "
                            "and ensures accountability.\n\n"
                            "When the government's expenditure exceeds its revenue, the result is a deficit. "
                            "To cover the gap, the treasury issues bonds — "
                            "financial instruments that allow the government to borrow from investors. "
                            "A bond is a promise to repay the borrowed amount plus interest on a future date. "
                            "Investors buy bonds because they are considered safe, "
                            "especially those issued by stable governments. "
                            "The accumulated total of all past deficits becomes the national debt.\n\n"
                            "When the economy enters a recession, governments often respond with a fiscal stimulus. "
                            "A stimulus package may include increased spending on public works, "
                            "tax cuts for businesses and consumers, or direct payments to households. "
                            "The goal is to inject money into the economy, create jobs, "
                            "and encourage spending. During the global financial crisis and the pandemic, "
                            "many governments launched massive stimulus programs "
                            "that added trillions of dollars to their national debt.\n\n"
                            "When debt reaches levels that worry investors and policymakers, "
                            "governments may shift to austerity. "
                            "Austerity involves cutting expenditure and raising taxes "
                            "to reduce the deficit and slow the growth of debt. "
                            "While austerity can restore fiscal discipline, "
                            "it often comes at a social cost: reduced public services, "
                            "higher unemployment, and slower economic growth.\n\n"
                            "The tension between stimulus and austerity defines much of modern fiscal debate. "
                            "Should the government spend more to help the economy grow, "
                            "even if it means higher debt? Or should it cut spending to keep finances sustainable, "
                            "even if it means short-term pain? "
                            "The answer depends on the allocation of priorities, "
                            "the level of existing debt, and the willingness of investors "
                            "to keep buying government bonds.\n\n"
                            "In the rare case when revenue exceeds expenditure, "
                            "the government enjoys a budget surplus. "
                            "A surplus can be used to pay down debt, build reserve funds, "
                            "or invest in long-term projects. "
                            "But surpluses are uncommon — most governments operate with some level of deficit, "
                            "relying on the bond market and the treasury to manage their borrowing needs.\n\n"
                            "Fiscal policy is not just an abstract concept studied in textbooks. "
                            "Every appropriation bill, every tax reform, every decision about mandatory "
                            "versus discretionary spending affects real people — "
                            "the teacher whose salary depends on the education budget, "
                            "the retiree whose pension is a mandatory obligation, "
                            "the entrepreneur whose business benefits from a stimulus tax cut. "
                            "Understanding fiscal policy means understanding how governments "
                            "make the choices that shape our daily lives."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chính sách tài khóa",
                    "description": "Viết đoạn văn tiếng Anh phân tích về chính sách tài khóa sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["fiscal", "budget", "deficit", "surplus", "expenditure", "revenue", "taxation", "progressive", "regressive", "stimulus", "austerity", "debt", "bond", "treasury", "allocation", "discretionary", "mandatory", "appropriation"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến chính sách tài khóa. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích tình huống khi một quốc gia đang đối mặt với suy thoái kinh tế. Chính phủ nên chọn stimulus hay austerity? Giải thích cách mỗi lựa chọn ảnh hưởng đến deficit, debt, và expenditure, và vai trò của bond trong việc tài trợ cho chính sách.",
                            "Hãy so sánh hệ thống thuế progressive và regressive, và phân tích cách mỗi hệ thống ảnh hưởng đến revenue của chính phủ. Giải thích cách allocation ngân sách giữa mandatory và discretionary spending phản ánh ưu tiên của một quốc gia."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết và ôn tập từ vựng",
                    "description": "Ôn lại từ vựng quan trọng và lời khuyên thực tế để tiếp tục học.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành toàn bộ bài học về Chính sách tài khóa — Fiscal Policy! "
                            "Hãy cùng ôn lại những từ vựng quan trọng nhất, "
                            "và mình sẽ cho bạn một vài gợi ý cụ thể để áp dụng ngay vào thực tế.\n\n"
                            "Fiscal — thuộc về tài khóa. Đây là từ bạn sẽ gặp mỗi khi đọc về chính sách kinh tế. "
                            "Ví dụ mới: The prime minister promised a responsible fiscal strategy "
                            "that balances growth with debt reduction over the next five years.\n\n"
                            "Deficit — thâm hụt. Khi chính phủ chi nhiều hơn thu, đó là deficit. "
                            "Ví dụ mới: The country's deficit reached eight percent of GDP last year, "
                            "the highest level since the financial crisis a decade ago.\n\n"
                            "Taxation — thuế khóa. Hệ thống thuế quyết định ai đóng bao nhiêu. "
                            "Ví dụ mới: The debate over taxation reform dominated the election campaign, "
                            "with one party proposing higher corporate taxes and the other pushing for lower rates.\n\n"
                            "Stimulus — kích thích kinh tế. Khi nền kinh tế cần một cú hích, "
                            "chính phủ tung ra stimulus. "
                            "Ví dụ mới: The stimulus checks sent directly to households helped millions of families "
                            "pay rent and buy groceries during the worst months of the economic shutdown.\n\n"
                            "Bond — trái phiếu. Đây là cách chính phủ vay tiền từ nhà đầu tư. "
                            "Ví dụ mới: When interest rates fell to near zero, demand for government bonds surged "
                            "as investors searched for safe places to park their money.\n\n"
                            "Appropriation — cấp phát ngân sách. Không có appropriation, "
                            "không có tiền nào được chi. "
                            "Ví dụ mới: The emergency appropriation bill passed in just forty-eight hours, "
                            "releasing funds for earthquake relief before the end of the week.\n\n"
                            "Bây giờ, đây là bước tiếp theo bạn có thể làm ngay hôm nay. "
                            "Hãy mở trang web của một tờ báo kinh tế tiếng Anh — "
                            "Financial Times, The Economist, hoặc Bloomberg — "
                            "và tìm một bài viết có chứa từ 'fiscal' hoặc 'budget'. "
                            "Đọc đoạn đầu tiên và đánh dấu những từ bạn vừa học. "
                            "Bạn sẽ ngạc nhiên khi thấy mình hiểu được bao nhiêu.\n\n"
                            "Nếu bạn muốn đi xa hơn, hãy thử viết một đoạn tóm tắt ngắn "
                            "bằng tiếng Anh về bài báo đó — chỉ cần 3-4 câu, "
                            "sử dụng ít nhất 3 từ vựng bạn đã học. "
                            "Đây là cách nhanh nhất để biến từ vựng thụ động thành từ vựng chủ động.\n\n"
                            "Chính sách tài khóa không phải là chủ đề xa vời — "
                            "nó ảnh hưởng đến lương của bạn, giá cả bạn trả, "
                            "và cơ hội việc làm bạn có. "
                            "Giờ bạn đã có ngôn ngữ để hiểu và thảo luận về nó bằng tiếng Anh.\n\n"
                            "Chúc bạn tiếp tục hành trình học tập thật hiệu quả. "
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Fiscal Policy – Chính Sách Tài Khóa' AND uid = '{UID}' ORDER BY created_at;")
