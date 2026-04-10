"""
Create curriculum: Capital Structure – Cấu Trúc Vốn
Series D — Kế Toán & Tài Chính Doanh Nghiệp (Accounting & Corporate Finance), curriculum #4
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
W1 = ["capital", "debt", "equity", "leverage", "ratio", "valuation"]
W2 = ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"]
W3 = ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Capital Structure – Cấu Trúc Vốn",
    "contentTypeTags": [],
    "description": (
        "MỌI DOANH NGHIỆP LỚN TRÊN THẾ GIỚI ĐỀU PHẢI TRẢ LỜI MỘT CÂU HỎI SỐNG CÒN: VAY NỢ HAY GỌI VỐN CỔ ĐÔNG?\n\n"
        "Bạn đang ngồi trong lớp tài chính doanh nghiệp, giảng viên chiếu cấu trúc vốn của Vingroup lên màn hình. "
        "Bạn hiểu 'nợ vay' và 'vốn cổ phần' bằng tiếng Việt, nhưng khi bài tập yêu cầu phân tích "
        "debt-to-equity ratio, weighted average cost of capital, hay bond yield — bạn chững lại. "
        "Những thuật ngữ này không phải kiến thức xa vời — chúng là ngôn ngữ hàng ngày "
        "của mọi giám đốc tài chính trên thế giới.\n\n"
        "Hãy nghĩ về 18 từ vựng này như bản đồ dẫn đường qua mê cung tài chính doanh nghiệp — "
        "từ quyết định vay nợ hay phát hành cổ phiếu, đến chính sách cổ tức, "
        "từ định giá trái phiếu đến tái cấu trúc vốn. "
        "Một khi bạn nắm được bản đồ, mọi quyết định tài chính đều trở nên rõ ràng.\n\n"
        "Sau khóa học, bạn sẽ tự tin đọc báo cáo phân tích cấu trúc vốn bằng tiếng Anh, "
        "thảo luận về leverage và valuation trong bài tập nhóm, "
        "và viết nhận xét về chính sách tài chính doanh nghiệp bằng ngôn ngữ chuyên ngành quốc tế.\n\n"
        "18 từ vựng — từ capital đến buyback — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy tài chính doanh nghiệp, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về cấu trúc vốn doanh nghiệp — "
            "ngôn ngữ mà mọi giám đốc tài chính trên thế giới sử dụng mỗi ngày. "
            "Bạn sẽ học capital, debt, equity, leverage, ratio, valuation trong phần đầu tiên, "
            "nơi bài đọc giải thích cách doanh nghiệp quyết định giữa vay nợ và gọi vốn cổ đông. "
            "Tiếp theo là dividend, shareholder, bond, yield, maturity, coupon — "
            "những từ giúp bạn hiểu thị trường trái phiếu và chính sách cổ tức. "
            "Cuối cùng, weighted, optimal, restructuring, refinancing, dilution, buyback "
            "đưa bạn vào thế giới tối ưu hóa cấu trúc vốn và các quyết định tài chính chiến lược. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin phân tích cấu trúc vốn doanh nghiệp bằng tiếng Anh — "
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
                    "description": "Chào mừng bạn đến với bài học về cấu trúc vốn doanh nghiệp.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ tư trong chuỗi từ vựng Kế toán và Tài chính doanh nghiệp — "
                            "chủ đề hôm nay là Cấu trúc vốn, hay trong tiếng Anh là Capital Structure. "
                            "Mỗi doanh nghiệp, từ startup công nghệ đến tập đoàn đa quốc gia, "
                            "đều phải đối mặt với một câu hỏi then chốt: lấy tiền ở đâu để phát triển? "
                            "Vay ngân hàng? Phát hành trái phiếu? Hay gọi vốn từ cổ đông? "
                            "Câu trả lời nằm trong cấu trúc vốn — và bạn sắp học ngôn ngữ để hiểu nó.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: capital, debt, equity, leverage, ratio, và valuation. "
                            "Đây là những từ nền tảng nhất — bạn sẽ gặp chúng trong mọi bài phân tích tài chính doanh nghiệp.\n\n"
                            "Từ đầu tiên là capital — danh từ — nghĩa là vốn, "
                            "tổng nguồn lực tài chính mà doanh nghiệp huy động để hoạt động và phát triển. "
                            "Ví dụ: 'The company raised five hundred billion dong in capital through a combination of bank loans and a new share offering to fund its expansion into Southeast Asia.' "
                            "Trong bài đọc, capital là khái niệm trung tâm — "
                            "mọi quyết định tài chính đều xoay quanh việc huy động và sử dụng vốn hiệu quả.\n\n"
                            "Từ thứ hai là debt — danh từ — nghĩa là nợ vay, "
                            "số tiền mà doanh nghiệp vay từ ngân hàng, trái chủ, hoặc các tổ chức tài chính khác. "
                            "Ví dụ: 'The firm's total debt reached two trillion dong after it borrowed heavily to build three new factories in the Mekong Delta region.' "
                            "Trong bài đọc, debt là một trong hai nguồn vốn chính — "
                            "nó mang lại tiền nhanh nhưng đi kèm nghĩa vụ trả lãi và gốc.\n\n"
                            "Từ thứ ba là equity — danh từ — nghĩa là vốn cổ phần, "
                            "phần vốn mà cổ đông đóng góp hoặc lợi nhuận giữ lại trong doanh nghiệp. "
                            "Ví dụ: 'The startup raised equity of one hundred billion dong from venture capital firms in exchange for a thirty percent ownership stake.' "
                            "Trong bài đọc, equity là nguồn vốn thứ hai — "
                            "không cần trả lãi nhưng cổ đông sẽ chia sẻ quyền sở hữu và lợi nhuận.\n\n"
                            "Từ thứ tư là leverage — danh từ — nghĩa là đòn bẩy tài chính, "
                            "mức độ sử dụng nợ vay so với vốn cổ phần trong cấu trúc vốn. "
                            "Ví dụ: 'High leverage can amplify profits when business is good, but it also magnifies losses during economic downturns because interest payments remain fixed.' "
                            "Trong bài đọc, leverage là con dao hai lưỡi — "
                            "dùng đúng thì tăng lợi nhuận, dùng sai thì đẩy doanh nghiệp vào khủng hoảng.\n\n"
                            "Từ thứ năm là ratio — danh từ — nghĩa là tỷ số hoặc tỷ lệ, "
                            "công cụ đo lường mối quan hệ giữa hai chỉ số tài chính. "
                            "Ví dụ: 'The debt-to-equity ratio of the company is one point five, meaning it has borrowed one and a half dong for every dong of shareholder equity.' "
                            "Trong bài đọc, ratio là ngôn ngữ so sánh — "
                            "nhà phân tích dùng các tỷ số để đánh giá sức khỏe tài chính nhanh chóng.\n\n"
                            "Từ cuối cùng là valuation — danh từ — nghĩa là định giá, "
                            "quá trình xác định giá trị kinh tế của một doanh nghiệp hoặc tài sản. "
                            "Ví dụ: 'The investment bank estimated the company's valuation at ten trillion dong based on its projected cash flows over the next ten years.' "
                            "Trong bài đọc, valuation là kết quả cuối cùng — "
                            "cấu trúc vốn ảnh hưởng trực tiếp đến cách thị trường định giá doanh nghiệp.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách doanh nghiệp quyết định cấu trúc vốn nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Vốn, nợ và đòn bẩy tài chính",
                    "description": "Học 6 từ: capital, debt, equity, leverage, ratio, valuation",
                    "data": {"vocabList": ["capital", "debt", "equity", "leverage", "ratio", "valuation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Vốn, nợ và đòn bẩy tài chính",
                    "description": "Học 6 từ: capital, debt, equity, leverage, ratio, valuation",
                    "data": {"vocabList": ["capital", "debt", "equity", "leverage", "ratio", "valuation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Vốn, nợ và đòn bẩy tài chính",
                    "description": "Học 6 từ: capital, debt, equity, leverage, ratio, valuation",
                    "data": {"vocabList": ["capital", "debt", "equity", "leverage", "ratio", "valuation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Vốn, nợ và đòn bẩy tài chính",
                    "description": "Học 6 từ: capital, debt, equity, leverage, ratio, valuation",
                    "data": {"vocabList": ["capital", "debt", "equity", "leverage", "ratio", "valuation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Vốn, nợ và đòn bẩy tài chính",
                    "description": "Học 6 từ: capital, debt, equity, leverage, ratio, valuation",
                    "data": {"vocabList": ["capital", "debt", "equity", "leverage", "ratio", "valuation"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Quyết định cấu trúc vốn",
                    "description": "Every company needs money to grow, and the way it raises that money defines its capital structure.",
                    "data": {
                        "text": (
                            "Every company needs money to grow, and the way it raises that money "
                            "defines its capital structure. Capital structure is the mix of debt and equity "
                            "that a company uses to finance its operations and expansion. "
                            "Getting this mix right is one of the most important decisions "
                            "a chief financial officer will ever make.\n\n"
                            "Capital comes in two basic forms. The first is debt — money borrowed "
                            "from banks, bondholders, or other lenders. Debt must be repaid with interest, "
                            "regardless of whether the company is profitable. "
                            "A Vietnamese real estate developer, for example, might borrow "
                            "three trillion dong from a consortium of banks to build a new residential complex. "
                            "The developer must make regular interest payments and eventually return the principal, "
                            "even if apartment sales are slower than expected.\n\n"
                            "The second form of capital is equity — money contributed by shareholders "
                            "who become part owners of the company. Unlike debt, equity does not require "
                            "fixed repayments. Shareholders earn returns through dividends and rising share prices. "
                            "However, issuing new equity means sharing ownership and future profits "
                            "with more people.\n\n"
                            "The balance between debt and equity creates leverage. "
                            "Leverage measures how much a company relies on borrowed money. "
                            "A company with high leverage has a large proportion of debt relative to equity. "
                            "Leverage works like a magnifying glass — it amplifies both gains and losses. "
                            "When a highly leveraged company earns strong profits, "
                            "the returns to shareholders are magnified because the profits are spread "
                            "over a smaller equity base. But when profits fall, "
                            "the fixed interest payments on debt can quickly turn a small decline "
                            "into a serious financial problem.\n\n"
                            "Financial analysts use ratios to measure and compare capital structures. "
                            "The most common is the debt-to-equity ratio, which divides total debt "
                            "by total equity. A ratio of two means the company has borrowed "
                            "two dong for every dong of shareholder equity. "
                            "Different industries have different norms — "
                            "banks and utilities typically operate with higher ratios "
                            "than technology companies or consumer goods firms.\n\n"
                            "Ultimately, capital structure affects valuation — "
                            "how much the market thinks a company is worth. "
                            "A company that uses debt wisely can lower its overall cost of capital "
                            "and increase its valuation. But too much debt raises the risk of default, "
                            "which drives the valuation down. "
                            "Finding the right balance between debt and equity "
                            "is the central challenge of corporate finance."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Quyết định cấu trúc vốn",
                    "description": "Every company needs money to grow, and the way it raises that money defines its capital structure.",
                    "data": {
                        "text": (
                            "Every company needs money to grow, and the way it raises that money "
                            "defines its capital structure. Capital structure is the mix of debt and equity "
                            "that a company uses to finance its operations and expansion. "
                            "Getting this mix right is one of the most important decisions "
                            "a chief financial officer will ever make.\n\n"
                            "Capital comes in two basic forms. The first is debt — money borrowed "
                            "from banks, bondholders, or other lenders. Debt must be repaid with interest, "
                            "regardless of whether the company is profitable. "
                            "A Vietnamese real estate developer, for example, might borrow "
                            "three trillion dong from a consortium of banks to build a new residential complex. "
                            "The developer must make regular interest payments and eventually return the principal, "
                            "even if apartment sales are slower than expected.\n\n"
                            "The second form of capital is equity — money contributed by shareholders "
                            "who become part owners of the company. Unlike debt, equity does not require "
                            "fixed repayments. Shareholders earn returns through dividends and rising share prices. "
                            "However, issuing new equity means sharing ownership and future profits "
                            "with more people.\n\n"
                            "The balance between debt and equity creates leverage. "
                            "Leverage measures how much a company relies on borrowed money. "
                            "A company with high leverage has a large proportion of debt relative to equity. "
                            "Leverage works like a magnifying glass — it amplifies both gains and losses. "
                            "When a highly leveraged company earns strong profits, "
                            "the returns to shareholders are magnified because the profits are spread "
                            "over a smaller equity base. But when profits fall, "
                            "the fixed interest payments on debt can quickly turn a small decline "
                            "into a serious financial problem.\n\n"
                            "Financial analysts use ratios to measure and compare capital structures. "
                            "The most common is the debt-to-equity ratio, which divides total debt "
                            "by total equity. A ratio of two means the company has borrowed "
                            "two dong for every dong of shareholder equity. "
                            "Different industries have different norms — "
                            "banks and utilities typically operate with higher ratios "
                            "than technology companies or consumer goods firms.\n\n"
                            "Ultimately, capital structure affects valuation — "
                            "how much the market thinks a company is worth. "
                            "A company that uses debt wisely can lower its overall cost of capital "
                            "and increase its valuation. But too much debt raises the risk of default, "
                            "which drives the valuation down. "
                            "Finding the right balance between debt and equity "
                            "is the central challenge of corporate finance."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Quyết định cấu trúc vốn",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every company needs money to grow, and the way it raises that money "
                            "defines its capital structure. Capital structure is the mix of debt and equity "
                            "that a company uses to finance its operations and expansion. "
                            "Getting this mix right is one of the most important decisions "
                            "a chief financial officer will ever make.\n\n"
                            "Capital comes in two basic forms. The first is debt — money borrowed "
                            "from banks, bondholders, or other lenders. Debt must be repaid with interest, "
                            "regardless of whether the company is profitable. "
                            "A Vietnamese real estate developer, for example, might borrow "
                            "three trillion dong from a consortium of banks to build a new residential complex. "
                            "The developer must make regular interest payments and eventually return the principal, "
                            "even if apartment sales are slower than expected.\n\n"
                            "The second form of capital is equity — money contributed by shareholders "
                            "who become part owners of the company. Unlike debt, equity does not require "
                            "fixed repayments. Shareholders earn returns through dividends and rising share prices. "
                            "However, issuing new equity means sharing ownership and future profits "
                            "with more people.\n\n"
                            "The balance between debt and equity creates leverage. "
                            "Leverage measures how much a company relies on borrowed money. "
                            "A company with high leverage has a large proportion of debt relative to equity. "
                            "Leverage works like a magnifying glass — it amplifies both gains and losses. "
                            "When a highly leveraged company earns strong profits, "
                            "the returns to shareholders are magnified because the profits are spread "
                            "over a smaller equity base. But when profits fall, "
                            "the fixed interest payments on debt can quickly turn a small decline "
                            "into a serious financial problem.\n\n"
                            "Financial analysts use ratios to measure and compare capital structures. "
                            "The most common is the debt-to-equity ratio, which divides total debt "
                            "by total equity. A ratio of two means the company has borrowed "
                            "two dong for every dong of shareholder equity. "
                            "Different industries have different norms — "
                            "banks and utilities typically operate with higher ratios "
                            "than technology companies or consumer goods firms.\n\n"
                            "Ultimately, capital structure affects valuation — "
                            "how much the market thinks a company is worth. "
                            "A company that uses debt wisely can lower its overall cost of capital "
                            "and increase its valuation. But too much debt raises the risk of default, "
                            "which drives the valuation down. "
                            "Finding the right balance between debt and equity "
                            "is the central challenge of corporate finance."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Vốn, nợ và đòn bẩy tài chính",
                    "description": "Viết câu sử dụng 6 từ vựng về cấu trúc vốn cơ bản.",
                    "data": {
                        "vocabList": ["capital", "debt", "equity", "leverage", "ratio", "valuation"],
                        "items": [
                            {
                                "targetVocab": "capital",
                                "prompt": "Dùng từ 'capital' để viết một câu về cách doanh nghiệp huy động vốn để mở rộng hoạt động. Ví dụ: The logistics company raised three hundred billion dong in capital through a combination of bank loans and a private equity investment to build a new distribution center in Da Nang."
                            },
                            {
                                "targetVocab": "debt",
                                "prompt": "Dùng từ 'debt' để viết một câu về tác động của nợ vay đối với doanh nghiệp. Ví dụ: The airline's total debt exceeded five trillion dong after it borrowed heavily to purchase ten new aircraft, putting significant pressure on its quarterly interest payments."
                            },
                            {
                                "targetVocab": "equity",
                                "prompt": "Dùng từ 'equity' để viết một câu về vốn cổ phần và quyền sở hữu trong doanh nghiệp. Ví dụ: The founders diluted their equity from eighty percent to fifty-five percent after the company issued new shares to raise capital for international expansion."
                            },
                            {
                                "targetVocab": "leverage",
                                "prompt": "Dùng từ 'leverage' để viết một câu về đòn bẩy tài chính và rủi ro đi kèm. Ví dụ: The property developer's high leverage made it extremely vulnerable when interest rates rose sharply, turning what had been manageable debt payments into a cash flow crisis."
                            },
                            {
                                "targetVocab": "ratio",
                                "prompt": "Dùng từ 'ratio' để viết một câu về cách sử dụng tỷ số tài chính để đánh giá doanh nghiệp. Ví dụ: The analyst flagged the company's debt-to-equity ratio of three point two as dangerously high compared to the industry average of one point five."
                            },
                            {
                                "targetVocab": "valuation",
                                "prompt": "Dùng từ 'valuation' để viết một câu về quá trình định giá doanh nghiệp. Ví dụ: The investment bank estimated the startup's valuation at eight trillion dong based on its rapid revenue growth and dominant market position in the Vietnamese e-commerce sector."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về cổ tức, trái phiếu và thị trường vốn.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "capital — vốn, debt — nợ vay, equity — vốn cổ phần, "
                            "leverage — đòn bẩy tài chính, ratio — tỷ số, và valuation — định giá. "
                            "Bạn đã hiểu cách doanh nghiệp quyết định giữa vay nợ và gọi vốn cổ đông. "
                            "Bây giờ, chúng ta sẽ đi sâu vào hai chủ đề quan trọng: "
                            "chính sách cổ tức và thị trường trái phiếu.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: dividend, shareholder, bond, yield, maturity, và coupon. "
                            "Đây là bộ từ vựng giúp bạn hiểu cách doanh nghiệp trả lại giá trị cho nhà đầu tư "
                            "và cách thị trường trái phiếu hoạt động.\n\n"
                            "Từ đầu tiên là dividend — danh từ — nghĩa là cổ tức, "
                            "phần lợi nhuận mà doanh nghiệp chia cho cổ đông. "
                            "Ví dụ: 'The board of directors approved a dividend of two thousand dong per share, distributing a total of fifty billion dong to shareholders from the company's annual profits.' "
                            "Trong bài đọc, dividend là cách doanh nghiệp nói với cổ đông: "
                            "chúng tôi đã kiếm được tiền và muốn chia sẻ với bạn.\n\n"
                            "Từ thứ hai là shareholder — danh từ — nghĩa là cổ đông, "
                            "người sở hữu cổ phần trong doanh nghiệp. "
                            "Ví dụ: 'The company's largest shareholder owns fifteen percent of all outstanding shares and has a seat on the board of directors.' "
                            "Trong bài đọc, shareholder là người có quyền biểu quyết "
                            "và nhận cổ tức — họ là chủ sở hữu thực sự của doanh nghiệp.\n\n"
                            "Từ thứ ba là bond — danh từ — nghĩa là trái phiếu, "
                            "chứng khoán nợ mà doanh nghiệp hoặc chính phủ phát hành để vay tiền từ nhà đầu tư. "
                            "Ví dụ: 'The corporation issued bonds worth one trillion dong with a ten-year term to finance the construction of a new semiconductor factory.' "
                            "Trong bài đọc, bond là công cụ nợ phổ biến nhất — "
                            "nhà đầu tư cho doanh nghiệp vay tiền và nhận lãi định kỳ.\n\n"
                            "Từ thứ tư là yield — danh từ — nghĩa là lợi suất, "
                            "tỷ lệ lợi nhuận mà nhà đầu tư nhận được từ một khoản đầu tư. "
                            "Ví dụ: 'The bond offers a yield of eight percent per year, which is attractive compared to the five percent interest rate on bank savings accounts.' "
                            "Trong bài đọc, yield là thước đo quan trọng nhất — "
                            "nó cho nhà đầu tư biết họ sẽ kiếm được bao nhiêu từ trái phiếu.\n\n"
                            "Từ thứ năm là maturity — danh từ — nghĩa là ngày đáo hạn, "
                            "thời điểm mà trái phiếu hết hạn và doanh nghiệp phải trả lại toàn bộ vốn gốc. "
                            "Ví dụ: 'The company's bonds have a maturity of seven years, meaning investors will receive their principal back in full at the end of the seventh year.' "
                            "Trong bài đọc, maturity quyết định thời gian nhà đầu tư phải chờ — "
                            "trái phiếu dài hạn thường có lợi suất cao hơn để bù đắp rủi ro.\n\n"
                            "Từ cuối cùng là coupon — danh từ — nghĩa là lãi suất coupon, "
                            "khoản lãi cố định mà doanh nghiệp trả cho trái chủ định kỳ. "
                            "Ví dụ: 'The bond has a coupon rate of six percent, which means the issuer pays sixty billion dong in interest each year on the one trillion dong bond issue.' "
                            "Trong bài đọc, coupon là thu nhập đều đặn mà trái chủ nhận được — "
                            "giống như tiền lãi ngân hàng nhưng từ doanh nghiệp.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về cổ tức và thị trường trái phiếu nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cổ tức, cổ đông và trái phiếu",
                    "description": "Học 6 từ: dividend, shareholder, bond, yield, maturity, coupon",
                    "data": {"vocabList": ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cổ tức, cổ đông và trái phiếu",
                    "description": "Học 6 từ: dividend, shareholder, bond, yield, maturity, coupon",
                    "data": {"vocabList": ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cổ tức, cổ đông và trái phiếu",
                    "description": "Học 6 từ: dividend, shareholder, bond, yield, maturity, coupon",
                    "data": {"vocabList": ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cổ tức, cổ đông và trái phiếu",
                    "description": "Học 6 từ: dividend, shareholder, bond, yield, maturity, coupon",
                    "data": {"vocabList": ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Cổ tức, cổ đông và trái phiếu",
                    "description": "Học 6 từ: dividend, shareholder, bond, yield, maturity, coupon",
                    "data": {"vocabList": ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cổ tức và thị trường trái phiếu",
                    "description": "When a company earns a profit, its board of directors faces a fundamental choice: keep the money or give it back to shareholders.",
                    "data": {
                        "text": (
                            "When a company earns a profit, its board of directors faces "
                            "a fundamental choice: keep the money or give it back to shareholders. "
                            "The money returned to shareholders is called a dividend. "
                            "Dividend policy is one of the most debated topics in corporate finance "
                            "because it directly affects how shareholders perceive the company's value.\n\n"
                            "A shareholder is anyone who owns shares in a company. "
                            "Shareholders have two ways to earn returns on their investment. "
                            "The first is through dividends — regular cash payments "
                            "that the company distributes from its profits. "
                            "The second is through capital gains — the increase in share price over time. "
                            "Some shareholders prefer steady dividends because they provide predictable income. "
                            "Others prefer the company to reinvest all profits "
                            "to drive growth and higher share prices.\n\n"
                            "A Vietnamese bank, for example, might pay a dividend of one thousand five hundred dong "
                            "per share each year. If a shareholder owns one million shares, "
                            "they receive one and a half billion dong annually — "
                            "a significant income stream that does not require selling any shares. "
                            "But if the bank had reinvested that money instead, "
                            "it might have grown faster and pushed the share price higher.\n\n"
                            "On the debt side of capital structure, bonds are the most common instrument. "
                            "A bond is essentially a loan that investors make to a company or government. "
                            "When a corporation issues a bond, it promises to pay investors "
                            "a fixed amount of interest at regular intervals "
                            "and return the full principal at the end of the bond's life.\n\n"
                            "The interest rate printed on the bond is called the coupon rate. "
                            "If a company issues a bond with a face value of one billion dong "
                            "and a coupon rate of seven percent, it pays seventy million dong "
                            "in interest each year. The coupon payment is fixed — "
                            "it does not change regardless of market conditions or the company's performance.\n\n"
                            "The date when the bond expires and the principal is returned "
                            "is called the maturity date. Bonds can have maturities "
                            "ranging from one year to thirty years or more. "
                            "Generally, longer maturity means higher risk for the investor "
                            "because more things can go wrong over a longer period. "
                            "To compensate for this risk, longer-term bonds usually offer higher coupon rates.\n\n"
                            "Yield is the actual return an investor earns on a bond. "
                            "If an investor buys a bond at its face value, "
                            "the yield equals the coupon rate. "
                            "But bonds are traded on the market, and their prices fluctuate. "
                            "When a bond's price falls below face value, its yield rises above the coupon rate. "
                            "When the price rises above face value, the yield falls below the coupon rate. "
                            "Understanding the relationship between bond prices and yield "
                            "is essential for anyone working in corporate finance."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cổ tức và thị trường trái phiếu",
                    "description": "When a company earns a profit, its board of directors faces a fundamental choice: keep the money or give it back to shareholders.",
                    "data": {
                        "text": (
                            "When a company earns a profit, its board of directors faces "
                            "a fundamental choice: keep the money or give it back to shareholders. "
                            "The money returned to shareholders is called a dividend. "
                            "Dividend policy is one of the most debated topics in corporate finance "
                            "because it directly affects how shareholders perceive the company's value.\n\n"
                            "A shareholder is anyone who owns shares in a company. "
                            "Shareholders have two ways to earn returns on their investment. "
                            "The first is through dividends — regular cash payments "
                            "that the company distributes from its profits. "
                            "The second is through capital gains — the increase in share price over time. "
                            "Some shareholders prefer steady dividends because they provide predictable income. "
                            "Others prefer the company to reinvest all profits "
                            "to drive growth and higher share prices.\n\n"
                            "A Vietnamese bank, for example, might pay a dividend of one thousand five hundred dong "
                            "per share each year. If a shareholder owns one million shares, "
                            "they receive one and a half billion dong annually — "
                            "a significant income stream that does not require selling any shares. "
                            "But if the bank had reinvested that money instead, "
                            "it might have grown faster and pushed the share price higher.\n\n"
                            "On the debt side of capital structure, bonds are the most common instrument. "
                            "A bond is essentially a loan that investors make to a company or government. "
                            "When a corporation issues a bond, it promises to pay investors "
                            "a fixed amount of interest at regular intervals "
                            "and return the full principal at the end of the bond's life.\n\n"
                            "The interest rate printed on the bond is called the coupon rate. "
                            "If a company issues a bond with a face value of one billion dong "
                            "and a coupon rate of seven percent, it pays seventy million dong "
                            "in interest each year. The coupon payment is fixed — "
                            "it does not change regardless of market conditions or the company's performance.\n\n"
                            "The date when the bond expires and the principal is returned "
                            "is called the maturity date. Bonds can have maturities "
                            "ranging from one year to thirty years or more. "
                            "Generally, longer maturity means higher risk for the investor "
                            "because more things can go wrong over a longer period. "
                            "To compensate for this risk, longer-term bonds usually offer higher coupon rates.\n\n"
                            "Yield is the actual return an investor earns on a bond. "
                            "If an investor buys a bond at its face value, "
                            "the yield equals the coupon rate. "
                            "But bonds are traded on the market, and their prices fluctuate. "
                            "When a bond's price falls below face value, its yield rises above the coupon rate. "
                            "When the price rises above face value, the yield falls below the coupon rate. "
                            "Understanding the relationship between bond prices and yield "
                            "is essential for anyone working in corporate finance."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cổ tức và thị trường trái phiếu",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When a company earns a profit, its board of directors faces "
                            "a fundamental choice: keep the money or give it back to shareholders. "
                            "The money returned to shareholders is called a dividend. "
                            "Dividend policy is one of the most debated topics in corporate finance "
                            "because it directly affects how shareholders perceive the company's value.\n\n"
                            "A shareholder is anyone who owns shares in a company. "
                            "Shareholders have two ways to earn returns on their investment. "
                            "The first is through dividends — regular cash payments "
                            "that the company distributes from its profits. "
                            "The second is through capital gains — the increase in share price over time. "
                            "Some shareholders prefer steady dividends because they provide predictable income. "
                            "Others prefer the company to reinvest all profits "
                            "to drive growth and higher share prices.\n\n"
                            "A Vietnamese bank, for example, might pay a dividend of one thousand five hundred dong "
                            "per share each year. If a shareholder owns one million shares, "
                            "they receive one and a half billion dong annually — "
                            "a significant income stream that does not require selling any shares. "
                            "But if the bank had reinvested that money instead, "
                            "it might have grown faster and pushed the share price higher.\n\n"
                            "On the debt side of capital structure, bonds are the most common instrument. "
                            "A bond is essentially a loan that investors make to a company or government. "
                            "When a corporation issues a bond, it promises to pay investors "
                            "a fixed amount of interest at regular intervals "
                            "and return the full principal at the end of the bond's life.\n\n"
                            "The interest rate printed on the bond is called the coupon rate. "
                            "If a company issues a bond with a face value of one billion dong "
                            "and a coupon rate of seven percent, it pays seventy million dong "
                            "in interest each year. The coupon payment is fixed — "
                            "it does not change regardless of market conditions or the company's performance.\n\n"
                            "The date when the bond expires and the principal is returned "
                            "is called the maturity date. Bonds can have maturities "
                            "ranging from one year to thirty years or more. "
                            "Generally, longer maturity means higher risk for the investor "
                            "because more things can go wrong over a longer period. "
                            "To compensate for this risk, longer-term bonds usually offer higher coupon rates.\n\n"
                            "Yield is the actual return an investor earns on a bond. "
                            "If an investor buys a bond at its face value, "
                            "the yield equals the coupon rate. "
                            "But bonds are traded on the market, and their prices fluctuate. "
                            "When a bond's price falls below face value, its yield rises above the coupon rate. "
                            "When the price rises above face value, the yield falls below the coupon rate. "
                            "Understanding the relationship between bond prices and yield "
                            "is essential for anyone working in corporate finance."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cổ tức, cổ đông và trái phiếu",
                    "description": "Viết câu sử dụng 6 từ vựng về cổ tức và thị trường trái phiếu.",
                    "data": {
                        "vocabList": ["dividend", "shareholder", "bond", "yield", "maturity", "coupon"],
                        "items": [
                            {
                                "targetVocab": "dividend",
                                "prompt": "Dùng từ 'dividend' để viết một câu về chính sách chia cổ tức của một doanh nghiệp. Ví dụ: The company increased its annual dividend to three thousand dong per share after reporting record profits, rewarding loyal shareholders who had held their stock through the difficult years."
                            },
                            {
                                "targetVocab": "shareholder",
                                "prompt": "Dùng từ 'shareholder' để viết một câu về quyền và vai trò của cổ đông trong doanh nghiệp. Ví dụ: The largest shareholder demanded a seat on the board of directors after acquiring twenty percent of the company's outstanding shares through open market purchases."
                            },
                            {
                                "targetVocab": "bond",
                                "prompt": "Dùng từ 'bond' để viết một câu về việc phát hành trái phiếu để huy động vốn. Ví dụ: The energy company issued bonds worth two trillion dong to finance the construction of a wind farm in Ninh Thuan province, attracting both domestic and foreign investors."
                            },
                            {
                                "targetVocab": "yield",
                                "prompt": "Dùng từ 'yield' để viết một câu về lợi suất trái phiếu và mối quan hệ với giá. Ví dụ: When the central bank raised interest rates, the yield on existing corporate bonds rose sharply because their market prices fell to make them competitive with new higher-rate offerings."
                            },
                            {
                                "targetVocab": "maturity",
                                "prompt": "Dùng từ 'maturity' để viết một câu về ngày đáo hạn trái phiếu và chiến lược đầu tư. Ví dụ: The pension fund prefers bonds with a maturity of twenty years or more because its obligations to retirees extend far into the future and require long-term stable income."
                            },
                            {
                                "targetVocab": "coupon",
                                "prompt": "Dùng từ 'coupon' để viết một câu về lãi suất coupon và thu nhập từ trái phiếu. Ví dụ: The government bond offers a coupon rate of five point five percent, paying investors fifty-five billion dong in interest annually on the one trillion dong issue."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về tối ưu hóa và tái cấu trúc vốn.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: capital, debt, equity, leverage, ratio, valuation — "
                            "những khái niệm cốt lõi về cấu trúc vốn doanh nghiệp. "
                            "Trong phần 2, bạn đã học thêm dividend, shareholder, bond, yield, maturity, coupon — "
                            "bộ từ vựng về cổ tức, cổ đông và thị trường trái phiếu.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào khía cạnh chiến lược nhất: "
                            "tối ưu hóa cấu trúc vốn và các quyết định tài chính lớn. "
                            "Bạn sẽ học 6 từ mới: weighted, optimal, restructuring, refinancing, dilution, và buyback.\n\n"
                            "Từ đầu tiên là weighted — tính từ — nghĩa là có trọng số, "
                            "thường dùng trong cụm weighted average cost of capital (WACC) — "
                            "chi phí vốn bình quân gia quyền, chỉ số đo lường chi phí trung bình "
                            "mà doanh nghiệp phải trả cho tất cả các nguồn vốn. "
                            "Ví dụ: 'The company's weighted average cost of capital is nine percent, meaning every project it undertakes must earn at least nine percent to create value for shareholders.' "
                            "Trong bài đọc, weighted cho thấy rằng chi phí vốn không đơn giản là một con số — "
                            "nó phụ thuộc vào tỷ trọng nợ và vốn cổ phần trong cấu trúc vốn.\n\n"
                            "Từ thứ hai là optimal — tính từ — nghĩa là tối ưu, "
                            "cấu trúc vốn lý tưởng nhất giúp tối thiểu hóa chi phí vốn và tối đa hóa giá trị doanh nghiệp. "
                            "Ví dụ: 'The CFO spent months analyzing different scenarios to find the optimal capital structure that would minimize the cost of funding while maintaining a strong credit rating.' "
                            "Trong bài đọc, optimal là mục tiêu mà mọi giám đốc tài chính theo đuổi — "
                            "nhưng nó thay đổi theo điều kiện thị trường và đặc thù ngành.\n\n"
                            "Từ thứ ba là restructuring — danh từ — nghĩa là tái cấu trúc, "
                            "quá trình thay đổi căn bản cấu trúc vốn hoặc tổ chức của doanh nghiệp. "
                            "Ví dụ: 'The struggling airline underwent a major restructuring that involved converting two trillion dong of debt into equity, giving creditors ownership stakes in exchange for forgiving their loans.' "
                            "Trong bài đọc, restructuring thường xảy ra khi doanh nghiệp gặp khó khăn tài chính — "
                            "đó là cách viết lại hợp đồng giữa doanh nghiệp và các chủ nợ.\n\n"
                            "Từ thứ tư là refinancing — danh từ — nghĩa là tái cấp vốn, "
                            "việc thay thế khoản nợ cũ bằng khoản nợ mới với điều kiện tốt hơn. "
                            "Ví dụ: 'The company saved fifty billion dong per year in interest costs by refinancing its old high-rate bonds with new bonds at a lower coupon rate.' "
                            "Trong bài đọc, refinancing là chiến thuật phổ biến — "
                            "khi lãi suất giảm, doanh nghiệp vay mới để trả nợ cũ và tiết kiệm chi phí.\n\n"
                            "Từ thứ năm là dilution — danh từ — nghĩa là pha loãng, "
                            "sự giảm tỷ lệ sở hữu của cổ đông hiện tại khi doanh nghiệp phát hành thêm cổ phiếu mới. "
                            "Ví dụ: 'Existing shareholders opposed the new share issue because it would cause dilution of their ownership from twenty percent to just twelve percent of the company.' "
                            "Trong bài đọc, dilution là cái giá của việc gọi vốn cổ phần — "
                            "doanh nghiệp có thêm tiền nhưng mỗi cổ đông sở hữu ít hơn.\n\n"
                            "Từ cuối cùng là buyback — danh từ — nghĩa là mua lại cổ phiếu, "
                            "khi doanh nghiệp dùng tiền mặt để mua lại chính cổ phiếu của mình trên thị trường. "
                            "Ví dụ: 'The technology giant announced a share buyback program worth five trillion dong, signaling to the market that management believes the stock is undervalued.' "
                            "Trong bài đọc, buyback là ngược lại với dilution — "
                            "nó giảm số cổ phiếu lưu hành và tăng giá trị cho cổ đông còn lại.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về tối ưu hóa cấu trúc vốn nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tối ưu hóa và tái cấu trúc vốn",
                    "description": "Học 6 từ: weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tối ưu hóa và tái cấu trúc vốn",
                    "description": "Học 6 từ: weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tối ưu hóa và tái cấu trúc vốn",
                    "description": "Học 6 từ: weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tối ưu hóa và tái cấu trúc vốn",
                    "description": "Học 6 từ: weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Tối ưu hóa và tái cấu trúc vốn",
                    "description": "Học 6 từ: weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tối ưu hóa cấu trúc vốn và quyết định tài chính chiến lược",
                    "description": "Every chief financial officer dreams of finding the perfect capital structure — the ideal mix of debt and equity.",
                    "data": {
                        "text": (
                            "Every chief financial officer dreams of finding the perfect capital structure — "
                            "the ideal mix of debt and equity that minimizes the company's cost of funding "
                            "and maximizes its value. This search for the optimal structure "
                            "is at the heart of modern corporate finance.\n\n"
                            "The key tool for measuring the cost of capital is the weighted average cost of capital, "
                            "commonly known as WACC. The weighted average takes into account "
                            "both the cost of debt and the cost of equity, "
                            "adjusted by the proportion of each in the company's capital structure. "
                            "If a company is funded sixty percent by debt at a cost of seven percent "
                            "and forty percent by equity at a cost of twelve percent, "
                            "the weighted average cost of capital is roughly nine percent. "
                            "Every investment the company makes must earn more than nine percent "
                            "to create value.\n\n"
                            "Finding the optimal capital structure means finding the mix "
                            "that produces the lowest possible WACC. "
                            "In theory, adding more debt lowers the WACC "
                            "because interest payments are tax-deductible, "
                            "making debt cheaper than equity. "
                            "But beyond a certain point, the risk of financial distress rises, "
                            "and both lenders and shareholders demand higher returns. "
                            "The optimal point is where the tax benefit of debt "
                            "is exactly balanced by the increased risk.\n\n"
                            "When a company's capital structure becomes unsustainable, "
                            "it may undergo restructuring. "
                            "Restructuring can take many forms — "
                            "converting debt into equity, selling assets to pay down loans, "
                            "or negotiating new terms with creditors. "
                            "A Vietnamese steel manufacturer that borrowed too heavily during a boom, "
                            "for example, might restructure by offering its banks "
                            "an ownership stake in exchange for forgiving part of the debt. "
                            "Restructuring is painful but sometimes necessary to save a company from bankruptcy.\n\n"
                            "A less dramatic strategy is refinancing. "
                            "Refinancing means replacing existing debt with new debt "
                            "that has better terms — typically a lower interest rate or longer maturity. "
                            "When market interest rates fall, companies rush to refinance "
                            "their outstanding bonds and loans. "
                            "A company that issued bonds at nine percent five years ago "
                            "might refinance them at six percent today, "
                            "saving billions of dong in annual interest costs.\n\n"
                            "On the equity side, companies face the challenge of dilution. "
                            "When a company issues new shares to raise capital, "
                            "the ownership percentage of existing shareholders decreases. "
                            "If a shareholder owned ten percent of a company with one million shares, "
                            "and the company issues another five hundred thousand shares, "
                            "that shareholder's stake drops to six point seven percent. "
                            "Dilution is the price shareholders pay when a company chooses equity over debt.\n\n"
                            "The opposite of dilution is a share buyback. "
                            "In a buyback, the company uses its own cash to purchase shares "
                            "from the open market, reducing the total number of shares outstanding. "
                            "This increases each remaining shareholder's ownership percentage "
                            "and often pushes the share price higher. "
                            "Buybacks have become one of the most popular ways "
                            "for profitable companies to return value to shareholders "
                            "without committing to regular dividend payments."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tối ưu hóa cấu trúc vốn và quyết định tài chính chiến lược",
                    "description": "Every chief financial officer dreams of finding the perfect capital structure — the ideal mix of debt and equity.",
                    "data": {
                        "text": (
                            "Every chief financial officer dreams of finding the perfect capital structure — "
                            "the ideal mix of debt and equity that minimizes the company's cost of funding "
                            "and maximizes its value. This search for the optimal structure "
                            "is at the heart of modern corporate finance.\n\n"
                            "The key tool for measuring the cost of capital is the weighted average cost of capital, "
                            "commonly known as WACC. The weighted average takes into account "
                            "both the cost of debt and the cost of equity, "
                            "adjusted by the proportion of each in the company's capital structure. "
                            "If a company is funded sixty percent by debt at a cost of seven percent "
                            "and forty percent by equity at a cost of twelve percent, "
                            "the weighted average cost of capital is roughly nine percent. "
                            "Every investment the company makes must earn more than nine percent "
                            "to create value.\n\n"
                            "Finding the optimal capital structure means finding the mix "
                            "that produces the lowest possible WACC. "
                            "In theory, adding more debt lowers the WACC "
                            "because interest payments are tax-deductible, "
                            "making debt cheaper than equity. "
                            "But beyond a certain point, the risk of financial distress rises, "
                            "and both lenders and shareholders demand higher returns. "
                            "The optimal point is where the tax benefit of debt "
                            "is exactly balanced by the increased risk.\n\n"
                            "When a company's capital structure becomes unsustainable, "
                            "it may undergo restructuring. "
                            "Restructuring can take many forms — "
                            "converting debt into equity, selling assets to pay down loans, "
                            "or negotiating new terms with creditors. "
                            "A Vietnamese steel manufacturer that borrowed too heavily during a boom, "
                            "for example, might restructure by offering its banks "
                            "an ownership stake in exchange for forgiving part of the debt. "
                            "Restructuring is painful but sometimes necessary to save a company from bankruptcy.\n\n"
                            "A less dramatic strategy is refinancing. "
                            "Refinancing means replacing existing debt with new debt "
                            "that has better terms — typically a lower interest rate or longer maturity. "
                            "When market interest rates fall, companies rush to refinance "
                            "their outstanding bonds and loans. "
                            "A company that issued bonds at nine percent five years ago "
                            "might refinance them at six percent today, "
                            "saving billions of dong in annual interest costs.\n\n"
                            "On the equity side, companies face the challenge of dilution. "
                            "When a company issues new shares to raise capital, "
                            "the ownership percentage of existing shareholders decreases. "
                            "If a shareholder owned ten percent of a company with one million shares, "
                            "and the company issues another five hundred thousand shares, "
                            "that shareholder's stake drops to six point seven percent. "
                            "Dilution is the price shareholders pay when a company chooses equity over debt.\n\n"
                            "The opposite of dilution is a share buyback. "
                            "In a buyback, the company uses its own cash to purchase shares "
                            "from the open market, reducing the total number of shares outstanding. "
                            "This increases each remaining shareholder's ownership percentage "
                            "and often pushes the share price higher. "
                            "Buybacks have become one of the most popular ways "
                            "for profitable companies to return value to shareholders "
                            "without committing to regular dividend payments."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tối ưu hóa cấu trúc vốn và quyết định tài chính chiến lược",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every chief financial officer dreams of finding the perfect capital structure — "
                            "the ideal mix of debt and equity that minimizes the company's cost of funding "
                            "and maximizes its value. This search for the optimal structure "
                            "is at the heart of modern corporate finance.\n\n"
                            "The key tool for measuring the cost of capital is the weighted average cost of capital, "
                            "commonly known as WACC. The weighted average takes into account "
                            "both the cost of debt and the cost of equity, "
                            "adjusted by the proportion of each in the company's capital structure. "
                            "If a company is funded sixty percent by debt at a cost of seven percent "
                            "and forty percent by equity at a cost of twelve percent, "
                            "the weighted average cost of capital is roughly nine percent. "
                            "Every investment the company makes must earn more than nine percent "
                            "to create value.\n\n"
                            "Finding the optimal capital structure means finding the mix "
                            "that produces the lowest possible WACC. "
                            "In theory, adding more debt lowers the WACC "
                            "because interest payments are tax-deductible, "
                            "making debt cheaper than equity. "
                            "But beyond a certain point, the risk of financial distress rises, "
                            "and both lenders and shareholders demand higher returns. "
                            "The optimal point is where the tax benefit of debt "
                            "is exactly balanced by the increased risk.\n\n"
                            "When a company's capital structure becomes unsustainable, "
                            "it may undergo restructuring. "
                            "Restructuring can take many forms — "
                            "converting debt into equity, selling assets to pay down loans, "
                            "or negotiating new terms with creditors. "
                            "A Vietnamese steel manufacturer that borrowed too heavily during a boom, "
                            "for example, might restructure by offering its banks "
                            "an ownership stake in exchange for forgiving part of the debt. "
                            "Restructuring is painful but sometimes necessary to save a company from bankruptcy.\n\n"
                            "A less dramatic strategy is refinancing. "
                            "Refinancing means replacing existing debt with new debt "
                            "that has better terms — typically a lower interest rate or longer maturity. "
                            "When market interest rates fall, companies rush to refinance "
                            "their outstanding bonds and loans. "
                            "A company that issued bonds at nine percent five years ago "
                            "might refinance them at six percent today, "
                            "saving billions of dong in annual interest costs.\n\n"
                            "On the equity side, companies face the challenge of dilution. "
                            "When a company issues new shares to raise capital, "
                            "the ownership percentage of existing shareholders decreases. "
                            "If a shareholder owned ten percent of a company with one million shares, "
                            "and the company issues another five hundred thousand shares, "
                            "that shareholder's stake drops to six point seven percent. "
                            "Dilution is the price shareholders pay when a company chooses equity over debt.\n\n"
                            "The opposite of dilution is a share buyback. "
                            "In a buyback, the company uses its own cash to purchase shares "
                            "from the open market, reducing the total number of shares outstanding. "
                            "This increases each remaining shareholder's ownership percentage "
                            "and often pushes the share price higher. "
                            "Buybacks have become one of the most popular ways "
                            "for profitable companies to return value to shareholders "
                            "without committing to regular dividend payments."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tối ưu hóa và tái cấu trúc vốn",
                    "description": "Viết câu sử dụng 6 từ vựng về tối ưu hóa cấu trúc vốn.",
                    "data": {
                        "vocabList": ["weighted", "optimal", "restructuring", "refinancing", "dilution", "buyback"],
                        "items": [
                            {
                                "targetVocab": "weighted",
                                "prompt": "Dùng từ 'weighted' để viết một câu về chi phí vốn bình quân gia quyền và vai trò của nó trong quyết định đầu tư. Ví dụ: The company rejected the new factory project because its expected return of seven percent was below the weighted average cost of capital of eight point five percent."
                            },
                            {
                                "targetVocab": "optimal",
                                "prompt": "Dùng từ 'optimal' để viết một câu về việc tìm kiếm cấu trúc vốn tối ưu cho doanh nghiệp. Ví dụ: After extensive analysis, the CFO concluded that the optimal capital structure for the company was forty percent debt and sixty percent equity, balancing tax benefits against financial risk."
                            },
                            {
                                "targetVocab": "restructuring",
                                "prompt": "Dùng từ 'restructuring' để viết một câu về quá trình tái cấu trúc vốn của doanh nghiệp gặp khó khăn. Ví dụ: The hotel chain's restructuring plan involved converting three trillion dong of bank debt into equity shares, giving the lenders a forty percent ownership stake in the company."
                            },
                            {
                                "targetVocab": "refinancing",
                                "prompt": "Dùng từ 'refinancing' để viết một câu về chiến lược tái cấp vốn để giảm chi phí lãi vay. Ví dụ: The corporation completed a successful refinancing of its outstanding bonds, replacing the old nine percent coupon with a new issue at six percent and saving over two hundred billion dong annually."
                            },
                            {
                                "targetVocab": "dilution",
                                "prompt": "Dùng từ 'dilution' để viết một câu về tác động của việc phát hành cổ phiếu mới đối với cổ đông hiện tại. Ví dụ: The venture capital round caused significant dilution for the founders, reducing their combined ownership from seventy percent to just forty-five percent of the company."
                            },
                            {
                                "targetVocab": "buyback",
                                "prompt": "Dùng từ 'buyback' để viết một câu về chương trình mua lại cổ phiếu và tác động đến giá cổ phiếu. Ví dụ: The board approved a share buyback program of two trillion dong, which reduced the number of outstanding shares by eight percent and boosted earnings per share significantly."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Cấu trúc vốn. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "capital — vốn, debt — nợ vay, equity — vốn cổ phần, "
                            "leverage — đòn bẩy tài chính, ratio — tỷ số, và valuation — định giá. "
                            "Đây là bộ từ vựng cốt lõi về cấu trúc vốn doanh nghiệp.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào cổ tức và thị trường trái phiếu: "
                            "dividend — cổ tức, shareholder — cổ đông, bond — trái phiếu, "
                            "yield — lợi suất, maturity — đáo hạn, và coupon — lãi suất coupon. "
                            "Những từ này giúp bạn hiểu cách doanh nghiệp trả lại giá trị cho nhà đầu tư.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "weighted — có trọng số, optimal — tối ưu, restructuring — tái cấu trúc, "
                            "refinancing — tái cấp vốn, dilution — pha loãng, và buyback — mua lại cổ phiếu. "
                            "Đây là những từ về chiến lược tối ưu hóa cấu trúc vốn.\n\n"
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
                    "description": "Học 18 từ: capital, debt, equity, leverage, ratio, valuation, dividend, shareholder, bond, yield, maturity, coupon, weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: capital, debt, equity, leverage, ratio, valuation, dividend, shareholder, bond, yield, maturity, coupon, weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: capital, debt, equity, leverage, ratio, valuation, dividend, shareholder, bond, yield, maturity, coupon, weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: capital, debt, equity, leverage, ratio, valuation, dividend, shareholder, bond, yield, maturity, coupon, weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: capital, debt, equity, leverage, ratio, valuation, dividend, shareholder, bond, yield, maturity, coupon, weighted, optimal, restructuring, refinancing, dilution, buyback",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng cấu trúc vốn",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "capital",
                                "prompt": "Dùng từ 'capital' để viết một câu về chiến lược huy động vốn của một tập đoàn lớn. Ví dụ: The conglomerate raised ten trillion dong in capital through a combination of bond issuance and a secondary share offering to fund its acquisition of three regional competitors."
                            },
                            {
                                "targetVocab": "debt",
                                "prompt": "Dùng từ 'debt' để viết một câu về rủi ro khi doanh nghiệp vay nợ quá nhiều. Ví dụ: The retail chain's excessive debt of four trillion dong became unsustainable when consumer spending dropped sharply during the economic slowdown."
                            },
                            {
                                "targetVocab": "equity",
                                "prompt": "Dùng từ 'equity' để viết một câu về lợi ích và chi phí của việc huy động vốn cổ phần. Ví dụ: Raising equity allowed the company to expand without taking on debt, but the founders had to accept a significant reduction in their ownership percentage."
                            },
                            {
                                "targetVocab": "leverage",
                                "prompt": "Dùng từ 'leverage' để viết một câu về tác động của đòn bẩy tài chính trong thời kỳ suy thoái. Ví dụ: Companies with high leverage suffered the most during the recession because their fixed interest payments consumed an ever-larger share of their shrinking revenues."
                            },
                            {
                                "targetVocab": "ratio",
                                "prompt": "Dùng từ 'ratio' để viết một câu về cách nhà phân tích sử dụng tỷ số tài chính để so sánh doanh nghiệp. Ví dụ: The analyst compared the debt-to-equity ratios of five Vietnamese banks and found that the state-owned bank had the highest ratio at three point eight."
                            },
                            {
                                "targetVocab": "valuation",
                                "prompt": "Dùng từ 'valuation' để viết một câu về cách cấu trúc vốn ảnh hưởng đến định giá doanh nghiệp. Ví dụ: The company's valuation dropped by twenty percent after it announced plans to take on massive debt to fund an aggressive expansion that investors considered too risky."
                            },
                            {
                                "targetVocab": "dividend",
                                "prompt": "Dùng từ 'dividend' để viết một câu về quyết định tăng hoặc cắt cổ tức và phản ứng của thị trường. Ví dụ: The board's decision to cut the dividend by fifty percent sent the stock price tumbling as income-focused investors sold their shares in disappointment."
                            },
                            {
                                "targetVocab": "shareholder",
                                "prompt": "Dùng từ 'shareholder' để viết một câu về xung đột lợi ích giữa các nhóm cổ đông. Ví dụ: The minority shareholders filed a lawsuit against the controlling shareholder for approving a related-party transaction that benefited the parent company at the expense of the listed subsidiary."
                            },
                            {
                                "targetVocab": "bond",
                                "prompt": "Dùng từ 'bond' để viết một câu về thị trường trái phiếu doanh nghiệp tại Việt Nam. Ví dụ: The Vietnamese corporate bond market has grown rapidly in recent years, with total outstanding bonds exceeding one hundred trillion dong as companies seek alternatives to bank lending."
                            },
                            {
                                "targetVocab": "yield",
                                "prompt": "Dùng từ 'yield' để viết một câu về mối quan hệ giữa lợi suất và rủi ro tín dụng. Ví dụ: The bond's yield jumped to twelve percent after the credit rating agency downgraded the issuer, reflecting the market's increased concern about the company's ability to repay."
                            },
                            {
                                "targetVocab": "maturity",
                                "prompt": "Dùng từ 'maturity' để viết một câu về chiến lược quản lý kỳ hạn nợ của doanh nghiệp. Ví dụ: The treasurer staggered the maturity dates of the company's bonds across five, seven, and ten years to avoid having all the debt come due at the same time."
                            },
                            {
                                "targetVocab": "coupon",
                                "prompt": "Dùng từ 'coupon' để viết một câu về so sánh lãi suất coupon giữa các loại trái phiếu. Ví dụ: The new bond issue carries a coupon of seven percent, which is two percentage points higher than government bonds of the same maturity, reflecting the additional credit risk."
                            },
                            {
                                "targetVocab": "weighted",
                                "prompt": "Dùng từ 'weighted' để viết một câu về cách tính chi phí vốn bình quân gia quyền. Ví dụ: The company's weighted average cost of capital decreased from ten percent to eight percent after it replaced expensive equity with cheaper long-term debt."
                            },
                            {
                                "targetVocab": "optimal",
                                "prompt": "Dùng từ 'optimal' để viết một câu về sự thay đổi cấu trúc vốn tối ưu theo điều kiện thị trường. Ví dụ: The optimal capital structure shifted toward more equity after interest rates rose sharply, making debt financing significantly more expensive than it had been the previous year."
                            },
                            {
                                "targetVocab": "restructuring",
                                "prompt": "Dùng từ 'restructuring' để viết một câu về kết quả của quá trình tái cấu trúc vốn. Ví dụ: After two years of restructuring, the shipping company emerged with a healthier balance sheet — its debt had been reduced by sixty percent and its equity base had doubled."
                            },
                            {
                                "targetVocab": "refinancing",
                                "prompt": "Dùng từ 'refinancing' để viết một câu về cơ hội tái cấp vốn khi lãi suất thay đổi. Ví dụ: The central bank's decision to lower the benchmark rate created a wave of refinancing activity as companies rushed to replace their high-interest loans with cheaper alternatives."
                            },
                            {
                                "targetVocab": "dilution",
                                "prompt": "Dùng từ 'dilution' để viết một câu về cách doanh nghiệp cân nhắc giữa huy động vốn và pha loãng cổ phần. Ví dụ: The CEO chose to issue convertible bonds instead of new shares to raise capital, delaying potential dilution until the bonds are converted at a higher share price in the future."
                            },
                            {
                                "targetVocab": "buyback",
                                "prompt": "Dùng từ 'buyback' để viết một câu về tác động của chương trình mua lại cổ phiếu đối với chỉ số tài chính. Ví dụ: The company's aggressive buyback program reduced outstanding shares by fifteen percent over three years, boosting earnings per share even though total net income remained flat."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về cấu trúc vốn.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về cấu trúc vốn — từ quyết định vay nợ hay gọi vốn, "
                            "đến thị trường trái phiếu, chính sách cổ tức, và tái cấu trúc doanh nghiệp.\n\n"
                            "Bạn sẽ gặp lại capital, debt, equity, leverage, ratio, valuation "
                            "trong phần mở đầu về nền tảng cấu trúc vốn. "
                            "Tiếp theo, dividend, shareholder, bond, yield, maturity, coupon "
                            "sẽ giúp bạn hiểu cách doanh nghiệp tương tác với nhà đầu tư. "
                            "Và cuối cùng, weighted, optimal, restructuring, refinancing, dilution, buyback "
                            "sẽ đưa bạn vào thế giới chiến lược tài chính cấp cao.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cấu trúc vốn — Nghệ thuật cân bằng tài chính",
                    "description": "Imagine you are a financial analyst at a securities firm in Ho Chi Minh City, and your team has been asked to evaluate the capital structure of a fast-growing Vietnamese technology company.",
                    "data": {
                        "text": (
                            "Imagine you are a financial analyst at a securities firm in Ho Chi Minh City, "
                            "and your team has been asked to evaluate the capital structure "
                            "of a fast-growing Vietnamese technology company. "
                            "The company has doubled its revenue in three years "
                            "and now needs to raise a massive amount of capital "
                            "to fund its next phase of expansion. "
                            "Your job is to analyze how the company should finance this growth.\n\n"
                            "You begin by examining the company's current capital structure. "
                            "Total capital stands at eight trillion dong, "
                            "split roughly evenly between debt and equity. "
                            "The company's debt includes bank loans and two outstanding bond issues. "
                            "Its equity comes from the original investment by founders, "
                            "subsequent share offerings, and retained profits accumulated over the years. "
                            "The debt-to-equity ratio is approximately one, "
                            "which is moderate for a technology company.\n\n"
                            "You calculate the company's leverage and find that it is manageable "
                            "but approaching the upper limit for its industry. "
                            "High leverage amplifies returns when the business is growing, "
                            "but it also means the company must make substantial interest payments "
                            "regardless of how well it performs. "
                            "If revenue growth slows, the fixed debt payments "
                            "could squeeze the company's cash flow.\n\n"
                            "Next, you look at the bond details. "
                            "The company's first bond issue has a face value of one trillion dong, "
                            "a coupon rate of eight percent, and a maturity of five years. "
                            "The second bond has a coupon of seven percent and matures in eight years. "
                            "On the open market, the first bond is trading below face value, "
                            "which means its yield has risen above the coupon rate — "
                            "a sign that investors see increased risk in the company's ability to repay.\n\n"
                            "You also review the company's dividend policy. "
                            "For the past three years, the board has paid a modest dividend "
                            "of five hundred dong per share. "
                            "Some shareholders are happy with the steady income, "
                            "but others argue that the company should stop paying dividends entirely "
                            "and reinvest every dong into growth. "
                            "The shareholder base is divided — "
                            "institutional investors want dividends for their portfolios, "
                            "while the founders prefer to reinvest.\n\n"
                            "Your team runs a valuation model using discounted cash flows. "
                            "The valuation depends heavily on the weighted average cost of capital. "
                            "You calculate the weighted cost by combining the after-tax cost of debt "
                            "at five point five percent with the cost of equity at thirteen percent, "
                            "weighted by their proportions in the capital structure. "
                            "The result is a WACC of approximately nine percent. "
                            "Any new project must earn more than nine percent to create value.\n\n"
                            "Now comes the critical question: "
                            "how should the company raise the additional capital it needs? "
                            "Option one is to issue more debt — perhaps a new bond offering. "
                            "This would increase leverage but keep ownership concentrated. "
                            "Option two is to issue new equity through a share offering. "
                            "This would strengthen the balance sheet but cause dilution "
                            "for existing shareholders, reducing their ownership percentage.\n\n"
                            "Your analysis suggests that the optimal approach is a combination. "
                            "The company should issue two trillion dong in new bonds "
                            "at a competitive coupon rate, taking advantage of its still-decent credit rating. "
                            "At the same time, it should raise one trillion dong in equity "
                            "to keep the debt-to-equity ratio below one point five. "
                            "This balanced approach minimizes the weighted cost of capital "
                            "while keeping leverage at a safe level.\n\n"
                            "You also recommend that the company consider refinancing "
                            "its first bond issue, which carries the higher coupon of eight percent. "
                            "If the company can issue new bonds at six point five percent, "
                            "refinancing would save over fifteen billion dong per year in interest costs. "
                            "The maturity of the new bonds should be extended to ten years "
                            "to reduce the pressure of near-term repayments.\n\n"
                            "Regarding the dividend, your team suggests maintaining the current payout "
                            "but supplementing it with a share buyback program. "
                            "A buyback of five hundred billion dong would reduce the number of outstanding shares, "
                            "partially offsetting the dilution from the new equity issue. "
                            "This sends a positive signal to the market — "
                            "management believes the stock is undervalued and is willing to invest in it.\n\n"
                            "Finally, you note that if the expansion does not go as planned, "
                            "the company should have a restructuring contingency. "
                            "Restructuring options could include converting some debt to equity, "
                            "selling non-core assets, or renegotiating loan terms with banks. "
                            "Having a plan in place before problems arise "
                            "is a sign of strong financial management.\n\n"
                            "Your report concludes that the company's capital structure is sound "
                            "but needs careful adjustment to support the next phase of growth. "
                            "The right combination of debt, equity, dividends, and buybacks "
                            "can maximize the company's valuation while keeping risk under control. "
                            "This is the art of capital structure — "
                            "balancing ambition with prudence, growth with stability, "
                            "and the interests of shareholders with the long-term health of the business."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cấu trúc vốn — Nghệ thuật cân bằng tài chính",
                    "description": "Imagine you are a financial analyst at a securities firm in Ho Chi Minh City, and your team has been asked to evaluate the capital structure of a fast-growing Vietnamese technology company.",
                    "data": {
                        "text": (
                            "Imagine you are a financial analyst at a securities firm in Ho Chi Minh City, "
                            "and your team has been asked to evaluate the capital structure "
                            "of a fast-growing Vietnamese technology company. "
                            "The company has doubled its revenue in three years "
                            "and now needs to raise a massive amount of capital "
                            "to fund its next phase of expansion. "
                            "Your job is to analyze how the company should finance this growth.\n\n"
                            "You begin by examining the company's current capital structure. "
                            "Total capital stands at eight trillion dong, "
                            "split roughly evenly between debt and equity. "
                            "The company's debt includes bank loans and two outstanding bond issues. "
                            "Its equity comes from the original investment by founders, "
                            "subsequent share offerings, and retained profits accumulated over the years. "
                            "The debt-to-equity ratio is approximately one, "
                            "which is moderate for a technology company.\n\n"
                            "You calculate the company's leverage and find that it is manageable "
                            "but approaching the upper limit for its industry. "
                            "High leverage amplifies returns when the business is growing, "
                            "but it also means the company must make substantial interest payments "
                            "regardless of how well it performs. "
                            "If revenue growth slows, the fixed debt payments "
                            "could squeeze the company's cash flow.\n\n"
                            "Next, you look at the bond details. "
                            "The company's first bond issue has a face value of one trillion dong, "
                            "a coupon rate of eight percent, and a maturity of five years. "
                            "The second bond has a coupon of seven percent and matures in eight years. "
                            "On the open market, the first bond is trading below face value, "
                            "which means its yield has risen above the coupon rate — "
                            "a sign that investors see increased risk in the company's ability to repay.\n\n"
                            "You also review the company's dividend policy. "
                            "For the past three years, the board has paid a modest dividend "
                            "of five hundred dong per share. "
                            "Some shareholders are happy with the steady income, "
                            "but others argue that the company should stop paying dividends entirely "
                            "and reinvest every dong into growth. "
                            "The shareholder base is divided — "
                            "institutional investors want dividends for their portfolios, "
                            "while the founders prefer to reinvest.\n\n"
                            "Your team runs a valuation model using discounted cash flows. "
                            "The valuation depends heavily on the weighted average cost of capital. "
                            "You calculate the weighted cost by combining the after-tax cost of debt "
                            "at five point five percent with the cost of equity at thirteen percent, "
                            "weighted by their proportions in the capital structure. "
                            "The result is a WACC of approximately nine percent. "
                            "Any new project must earn more than nine percent to create value.\n\n"
                            "Now comes the critical question: "
                            "how should the company raise the additional capital it needs? "
                            "Option one is to issue more debt — perhaps a new bond offering. "
                            "This would increase leverage but keep ownership concentrated. "
                            "Option two is to issue new equity through a share offering. "
                            "This would strengthen the balance sheet but cause dilution "
                            "for existing shareholders, reducing their ownership percentage.\n\n"
                            "Your analysis suggests that the optimal approach is a combination. "
                            "The company should issue two trillion dong in new bonds "
                            "at a competitive coupon rate, taking advantage of its still-decent credit rating. "
                            "At the same time, it should raise one trillion dong in equity "
                            "to keep the debt-to-equity ratio below one point five. "
                            "This balanced approach minimizes the weighted cost of capital "
                            "while keeping leverage at a safe level.\n\n"
                            "You also recommend that the company consider refinancing "
                            "its first bond issue, which carries the higher coupon of eight percent. "
                            "If the company can issue new bonds at six point five percent, "
                            "refinancing would save over fifteen billion dong per year in interest costs. "
                            "The maturity of the new bonds should be extended to ten years "
                            "to reduce the pressure of near-term repayments.\n\n"
                            "Regarding the dividend, your team suggests maintaining the current payout "
                            "but supplementing it with a share buyback program. "
                            "A buyback of five hundred billion dong would reduce the number of outstanding shares, "
                            "partially offsetting the dilution from the new equity issue. "
                            "This sends a positive signal to the market — "
                            "management believes the stock is undervalued and is willing to invest in it.\n\n"
                            "Finally, you note that if the expansion does not go as planned, "
                            "the company should have a restructuring contingency. "
                            "Restructuring options could include converting some debt to equity, "
                            "selling non-core assets, or renegotiating loan terms with banks. "
                            "Having a plan in place before problems arise "
                            "is a sign of strong financial management.\n\n"
                            "Your report concludes that the company's capital structure is sound "
                            "but needs careful adjustment to support the next phase of growth. "
                            "The right combination of debt, equity, dividends, and buybacks "
                            "can maximize the company's valuation while keeping risk under control. "
                            "This is the art of capital structure — "
                            "balancing ambition with prudence, growth with stability, "
                            "and the interests of shareholders with the long-term health of the business."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cấu trúc vốn — Nghệ thuật cân bằng tài chính",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine you are a financial analyst at a securities firm in Ho Chi Minh City, "
                            "and your team has been asked to evaluate the capital structure "
                            "of a fast-growing Vietnamese technology company. "
                            "The company has doubled its revenue in three years "
                            "and now needs to raise a massive amount of capital "
                            "to fund its next phase of expansion. "
                            "Your job is to analyze how the company should finance this growth.\n\n"
                            "You begin by examining the company's current capital structure. "
                            "Total capital stands at eight trillion dong, "
                            "split roughly evenly between debt and equity. "
                            "The company's debt includes bank loans and two outstanding bond issues. "
                            "Its equity comes from the original investment by founders, "
                            "subsequent share offerings, and retained profits accumulated over the years. "
                            "The debt-to-equity ratio is approximately one, "
                            "which is moderate for a technology company.\n\n"
                            "You calculate the company's leverage and find that it is manageable "
                            "but approaching the upper limit for its industry. "
                            "High leverage amplifies returns when the business is growing, "
                            "but it also means the company must make substantial interest payments "
                            "regardless of how well it performs. "
                            "If revenue growth slows, the fixed debt payments "
                            "could squeeze the company's cash flow.\n\n"
                            "Next, you look at the bond details. "
                            "The company's first bond issue has a face value of one trillion dong, "
                            "a coupon rate of eight percent, and a maturity of five years. "
                            "The second bond has a coupon of seven percent and matures in eight years. "
                            "On the open market, the first bond is trading below face value, "
                            "which means its yield has risen above the coupon rate — "
                            "a sign that investors see increased risk in the company's ability to repay.\n\n"
                            "You also review the company's dividend policy. "
                            "For the past three years, the board has paid a modest dividend "
                            "of five hundred dong per share. "
                            "Some shareholders are happy with the steady income, "
                            "but others argue that the company should stop paying dividends entirely "
                            "and reinvest every dong into growth. "
                            "The shareholder base is divided — "
                            "institutional investors want dividends for their portfolios, "
                            "while the founders prefer to reinvest.\n\n"
                            "Your team runs a valuation model using discounted cash flows. "
                            "The valuation depends heavily on the weighted average cost of capital. "
                            "You calculate the weighted cost by combining the after-tax cost of debt "
                            "at five point five percent with the cost of equity at thirteen percent, "
                            "weighted by their proportions in the capital structure. "
                            "The result is a WACC of approximately nine percent. "
                            "Any new project must earn more than nine percent to create value.\n\n"
                            "Now comes the critical question: "
                            "how should the company raise the additional capital it needs? "
                            "Option one is to issue more debt — perhaps a new bond offering. "
                            "This would increase leverage but keep ownership concentrated. "
                            "Option two is to issue new equity through a share offering. "
                            "This would strengthen the balance sheet but cause dilution "
                            "for existing shareholders, reducing their ownership percentage.\n\n"
                            "Your analysis suggests that the optimal approach is a combination. "
                            "The company should issue two trillion dong in new bonds "
                            "at a competitive coupon rate, taking advantage of its still-decent credit rating. "
                            "At the same time, it should raise one trillion dong in equity "
                            "to keep the debt-to-equity ratio below one point five. "
                            "This balanced approach minimizes the weighted cost of capital "
                            "while keeping leverage at a safe level.\n\n"
                            "You also recommend that the company consider refinancing "
                            "its first bond issue, which carries the higher coupon of eight percent. "
                            "If the company can issue new bonds at six point five percent, "
                            "refinancing would save over fifteen billion dong per year in interest costs. "
                            "The maturity of the new bonds should be extended to ten years "
                            "to reduce the pressure of near-term repayments.\n\n"
                            "Regarding the dividend, your team suggests maintaining the current payout "
                            "but supplementing it with a share buyback program. "
                            "A buyback of five hundred billion dong would reduce the number of outstanding shares, "
                            "partially offsetting the dilution from the new equity issue. "
                            "This sends a positive signal to the market — "
                            "management believes the stock is undervalued and is willing to invest in it.\n\n"
                            "Finally, you note that if the expansion does not go as planned, "
                            "the company should have a restructuring contingency. "
                            "Restructuring options could include converting some debt to equity, "
                            "selling non-core assets, or renegotiating loan terms with banks. "
                            "Having a plan in place before problems arise "
                            "is a sign of strong financial management.\n\n"
                            "Your report concludes that the company's capital structure is sound "
                            "but needs careful adjustment to support the next phase of growth. "
                            "The right combination of debt, equity, dividends, and buybacks "
                            "can maximize the company's valuation while keeping risk under control. "
                            "This is the art of capital structure — "
                            "balancing ambition with prudence, growth with stability, "
                            "and the interests of shareholders with the long-term health of the business."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích cấu trúc vốn doanh nghiệp",
                    "description": "Viết đoạn văn tiếng Anh phân tích cấu trúc vốn sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của cấu trúc vốn doanh nghiệp. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích cấu trúc vốn của một công ty bất động sản Việt Nam đang sử dụng đòn bẩy tài chính cao. Giải thích mối quan hệ giữa debt, equity và leverage, vai trò của ratio trong đánh giá rủi ro, và cách weighted average cost of capital ảnh hưởng đến valuation của doanh nghiệp.",
                            "Hãy giải thích chiến lược tài chính của một doanh nghiệp công nghệ đang cân nhắc giữa phát hành bond mới và gọi thêm vốn equity. Phân tích tác động của dilution đối với shareholder hiện tại, vai trò của dividend và buyback trong việc trả lại giá trị, và khi nào doanh nghiệp nên xem xét refinancing hoặc restructuring."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần đội nhóm.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Cấu trúc vốn — "
                            "và mình muốn nói thẳng: bạn vừa chinh phục một trong những chủ đề "
                            "khó nhất trong tài chính doanh nghiệp. Không phải ai cũng đi được đến đây. "
                            "Nhưng bạn đã làm được, và đó là điều đáng tự hào.\n\n"
                            "Hãy cùng ôn lại những từ vựng quan trọng nhất — "
                            "không chỉ để nhớ, mà để sẵn sàng dùng chúng trong bài tập, "
                            "trong thảo luận nhóm, và trong sự nghiệp tài chính của bạn.\n\n"
                            "Leverage — đòn bẩy tài chính. Đây là từ mà mọi giám đốc tài chính "
                            "phải cân nhắc mỗi ngày. Leverage giống như tốc độ trên đường cao tốc — "
                            "nó giúp bạn đến đích nhanh hơn, nhưng nếu mất kiểm soát, hậu quả rất nặng nề. "
                            "Ví dụ mới: The private equity firm used aggressive leverage "
                            "to acquire the retail chain, borrowing four dong for every dong of equity, "
                            "a strategy that paid off handsomely when the chain's profits doubled in two years.\n\n"
                            "Bond — trái phiếu. Trong thế giới tài chính, bond là cầu nối "
                            "giữa doanh nghiệp cần vốn và nhà đầu tư tìm kiếm thu nhập ổn định. "
                            "Hiểu bond là hiểu một nửa thị trường vốn. "
                            "Ví dụ mới: The Vietnamese government issued a ten-year bond "
                            "with a coupon of four point five percent to fund infrastructure projects, "
                            "and the issue was oversubscribed by three times within the first day.\n\n"
                            "Weighted — có trọng số. Từ này nghe kỹ thuật, "
                            "nhưng ý tưởng đằng sau nó rất trực quan: "
                            "không phải mọi nguồn vốn đều có chi phí như nhau, "
                            "và bạn phải tính trung bình có trọng số để biết chi phí thực sự. "
                            "Ví dụ mới: After the company shifted its capital structure toward more debt, "
                            "its weighted average cost of capital dropped from eleven percent to eight percent, "
                            "making previously unprofitable projects suddenly viable.\n\n"
                            "Dilution — pha loãng. Mỗi khi doanh nghiệp phát hành cổ phiếu mới, "
                            "miếng bánh sở hữu được chia nhỏ hơn. "
                            "Hiểu dilution giúp bạn đánh giá đúng tác động của mỗi đợt gọi vốn. "
                            "Ví dụ mới: The Series C funding round caused thirty percent dilution "
                            "for early investors, but the company's valuation tripled, "
                            "so their smaller slice was worth far more than before.\n\n"
                            "Buyback — mua lại cổ phiếu. Đây là cách doanh nghiệp nói với thị trường: "
                            "chúng tôi tin vào giá trị của chính mình. "
                            "Buyback giảm số cổ phiếu lưu hành và tăng giá trị cho cổ đông còn lại. "
                            "Ví dụ mới: The board authorized a buyback of three trillion dong "
                            "after the stock price fell thirty percent, "
                            "believing the market had significantly undervalued the company's long-term prospects.\n\n"
                            "Restructuring — tái cấu trúc. Không phải mọi câu chuyện tài chính "
                            "đều có kết thúc đẹp, nhưng restructuring cho doanh nghiệp cơ hội viết lại. "
                            "Đó là sự can đảm để thừa nhận vấn đề và hành động quyết liệt. "
                            "Ví dụ mới: The airline's restructuring transformed it from a company "
                            "on the brink of bankruptcy into a lean, profitable carrier "
                            "by converting half its debt into equity and renegotiating every supplier contract.\n\n"
                            "Bạn biết không, điều tuyệt vời nhất về cấu trúc vốn "
                            "là nó không phải bài toán có một đáp án duy nhất. "
                            "Mỗi doanh nghiệp, mỗi ngành, mỗi giai đoạn phát triển "
                            "đều cần một cấu trúc vốn khác nhau. "
                            "Và bây giờ, bạn đã có ngôn ngữ để tham gia vào cuộc thảo luận đó.\n\n"
                            "Hãy mang 18 từ vựng này vào lớp học, vào nhóm làm bài tập, "
                            "vào buổi thuyết trình tiếp theo. "
                            "Khi bạn nói về leverage, yield, hay optimal capital structure bằng tiếng Anh, "
                            "bạn không chỉ đang nói đúng — bạn đang nói như một chuyên gia tài chính thực thụ. "
                            "Cả nhóm sẽ nhìn bạn khác đi. Và bạn xứng đáng với điều đó.\n\n"
                            "Chúc mừng bạn đã hoàn thành! Hẹn gặp lại ở bài học tiếp theo — "
                            "chúng ta sẽ cùng nhau chinh phục thêm nhiều đỉnh cao nữa."
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Capital Structure – Cấu Trúc Vốn' AND uid = '{UID}' ORDER BY created_at;")
