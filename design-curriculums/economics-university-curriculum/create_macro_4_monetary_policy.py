"""
Create curriculum: Monetary Policy – Chính Sách Tiền Tệ
Series B — Kinh Tế Vĩ Mô (Macroeconomics), curriculum #4
18 words | 5 sessions | vivid_scenario tone | introspective guide farewell
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
W1 = ["monetary", "interest", "central", "reserve", "liquidity", "credit"]
W2 = ["inflation", "target", "tighten", "ease", "transmission", "benchmark"]
W3 = ["quantitative", "yield", "maturity", "deposit", "lending", "overnight"]
ALL_WORDS = W1 + W2 + W3

# ── Session 1 reading text (reused across reading/speakReading/readAlong) ──
S1_READING = (
    "Every modern economy has a central bank — an institution responsible for managing the country's money supply "
    "and setting the direction of monetary policy. In Vietnam, this role belongs to the State Bank of Vietnam. "
    "In the United States, it is the Federal Reserve. In Europe, it is the European Central Bank. "
    "Though their names differ, their core mission is the same: to keep the economy stable.\n\n"
    "The most powerful tool a central bank has is the interest rate. "
    "The interest rate is the cost of borrowing money, expressed as a percentage. "
    "When the central bank lowers the interest rate, borrowing becomes cheaper. "
    "Businesses find it easier to take out loans to build factories, buy equipment, or hire workers. "
    "Consumers are more willing to borrow for homes, cars, and education. "
    "This increase in spending stimulates the economy.\n\n"
    "When the central bank raises the interest rate, the opposite happens. "
    "Borrowing becomes more expensive, so businesses and consumers cut back on spending. "
    "This slows down economic activity, which can help prevent the economy from overheating.\n\n"
    "But interest rates alone do not tell the whole story. "
    "Central banks also manage the reserve requirement — the percentage of deposits that commercial banks must hold "
    "and cannot lend out. If the central bank raises the reserve requirement, banks have less money available to lend. "
    "If it lowers the requirement, banks can lend more, increasing the flow of credit in the economy.\n\n"
    "Credit is the lifeblood of a modern economy. "
    "When a small business owner borrows money to open a new shop, that is credit at work. "
    "When a family takes out a mortgage to buy a house, that is credit too. "
    "The total amount of credit flowing through the economy depends heavily on the monetary policy decisions "
    "made by the central bank.\n\n"
    "Liquidity refers to how easily money flows through the financial system. "
    "When liquidity is high, banks lend freely, businesses invest, and the economy grows. "
    "When liquidity is low — as it was during the 2008 financial crisis — banks hoard cash, "
    "lending freezes, and economic activity grinds to a halt. "
    "One of the central bank's most important jobs is to ensure that the financial system "
    "always has enough liquidity to function smoothly."
)

S2_READING = (
    "Central banks do not change interest rates randomly. "
    "Every decision is guided by a clear goal: keeping inflation under control. "
    "Inflation is the general rise in prices over time. "
    "A small amount of inflation — around two to three percent per year — is considered healthy. "
    "It means the economy is growing and people are spending. "
    "But when inflation rises too fast, it erodes the purchasing power of money. "
    "The salary you earn today buys less tomorrow.\n\n"
    "Most central banks set an inflation target — a specific rate they aim to achieve. "
    "The Federal Reserve, for example, targets two percent inflation. "
    "The State Bank of Vietnam typically aims to keep inflation below four percent. "
    "This target gives businesses and consumers a clear signal about where prices are heading, "
    "which helps them plan for the future.\n\n"
    "When inflation rises above the target, the central bank may decide to tighten monetary policy. "
    "To tighten means to make borrowing more expensive and reduce the amount of money in circulation. "
    "The most common way to tighten is to raise the benchmark interest rate. "
    "The benchmark rate is the reference rate that influences all other interest rates in the economy — "
    "from mortgage rates to business loan rates to credit card rates.\n\n"
    "When inflation falls too low or the economy slows down, the central bank may choose to ease monetary policy. "
    "To ease means to make borrowing cheaper and increase the money supply. "
    "Lowering the benchmark rate is the primary tool for easing. "
    "When rates drop, businesses and consumers are encouraged to borrow and spend, "
    "which pushes economic activity upward.\n\n"
    "But how does a change in the benchmark rate affect the entire economy? "
    "This process is called transmission — the mechanism through which monetary policy decisions "
    "travel from the central bank to commercial banks, then to businesses and households, "
    "and finally to prices and employment. "
    "The transmission mechanism has several channels: the interest rate channel, the credit channel, "
    "the exchange rate channel, and the expectations channel. "
    "Understanding transmission is key to understanding why monetary policy sometimes works quickly "
    "and sometimes takes months to show results."
)

S3_READING = (
    "Sometimes, lowering the benchmark interest rate to zero is not enough to revive a struggling economy. "
    "This is what happened in the United States after the 2008 financial crisis "
    "and again during the COVID-19 pandemic. "
    "When traditional tools run out, central banks turn to unconventional measures — "
    "the most famous of which is quantitative easing.\n\n"
    "Quantitative easing, often shortened to QE, is a policy where the central bank buys large amounts "
    "of government bonds and other financial assets from the market. "
    "By purchasing these assets, the central bank injects money directly into the financial system, "
    "increasing liquidity and pushing down long-term interest rates. "
    "The word quantitative refers to the large quantity of money created through this process.\n\n"
    "When the central bank buys bonds, it affects the yield on those bonds. "
    "Yield is the return an investor earns from holding a bond. "
    "When bond prices go up — because the central bank is buying them — yields go down. "
    "Lower yields on government bonds push investors to look for higher returns elsewhere, "
    "such as in corporate bonds or the stock market. "
    "This is how quantitative easing stimulates the broader economy.\n\n"
    "Bonds also have a maturity — the date when the borrower must repay the full amount. "
    "Short-term bonds might mature in three months or one year. "
    "Long-term bonds might mature in ten or thirty years. "
    "Central banks pay close attention to the relationship between short-term and long-term yields, "
    "known as the yield curve, because it signals how investors feel about the future.\n\n"
    "At the foundation of the banking system are two basic activities: taking deposits and lending money. "
    "A deposit is money that a customer places in a bank account. "
    "The bank pays the customer a small interest rate on the deposit "
    "and then lends that money to borrowers at a higher rate. "
    "The difference between the lending rate and the deposit rate is how banks earn profit.\n\n"
    "Lending is the act of providing money to borrowers with the expectation that it will be repaid with interest. "
    "The central bank influences lending by setting the cost at which commercial banks can borrow from each other. "
    "This is called the overnight rate — the interest rate banks charge each other for very short-term loans, "
    "usually just one night. "
    "The overnight rate is the most immediate reflection of the central bank's monetary policy stance. "
    "When the overnight rate rises, all other lending rates tend to follow."
)

S5_READING = (
    "Money makes the modern world turn, but it does not manage itself. "
    "Behind every loan, every mortgage, every credit card transaction, "
    "there is an invisible hand guiding the flow of money through the economy. "
    "That hand belongs to the central bank, and its primary instrument is monetary policy.\n\n"
    "Monetary policy is the set of decisions a central bank makes about interest rates "
    "and the money supply to achieve economic stability. "
    "The central bank sits at the heart of the financial system. "
    "It does not lend directly to consumers or businesses. "
    "Instead, it sets the conditions under which commercial banks operate — "
    "and those conditions ripple outward to affect every corner of the economy.\n\n"
    "The most visible tool is the interest rate. "
    "When the central bank lowers the interest rate, credit becomes cheaper. "
    "Businesses borrow to expand, consumers borrow to spend, and the economy accelerates. "
    "When the central bank raises the rate, credit becomes expensive, spending slows, "
    "and the economy cools down. This push and pull is the essence of monetary policy.\n\n"
    "The central bank also controls the reserve requirement — "
    "the share of deposits that commercial banks must keep on hand rather than lend out. "
    "A higher reserve requirement means less money available for lending. "
    "A lower requirement means more liquidity flows into the economy. "
    "Liquidity is the oxygen of the financial system: without it, banks cannot lend, "
    "businesses cannot invest, and growth stalls.\n\n"
    "Every monetary policy decision is guided by a target — most commonly, an inflation target. "
    "Inflation is the gradual rise in prices that erodes the value of money over time. "
    "A moderate level of inflation signals a healthy, growing economy. "
    "But when inflation climbs too high, the central bank must tighten policy "
    "by raising the benchmark interest rate. "
    "When inflation falls too low or the economy weakens, the central bank will ease policy "
    "by cutting rates and encouraging borrowing.\n\n"
    "The benchmark rate is the reference point for all other rates in the economy. "
    "When it changes, the effects travel through the transmission mechanism — "
    "from the central bank to commercial banks, then to businesses and households. "
    "Mortgage rates, car loan rates, and deposit rates all adjust in response. "
    "This transmission process can take weeks or months, "
    "which is why central banks must act with foresight, not just react to current conditions.\n\n"
    "When conventional tools are not enough — when interest rates are already near zero — "
    "central banks may turn to quantitative easing. "
    "By buying large quantities of government bonds, the central bank pushes bond prices up "
    "and yields down, flooding the financial system with liquidity. "
    "The yield on a bond is the return an investor earns, "
    "and it moves inversely with the bond's price. "
    "Lower yields on safe government bonds push investors toward riskier assets, "
    "stimulating investment across the economy.\n\n"
    "Bonds come with a maturity date — the point at which the borrower repays the principal. "
    "Short-term bonds mature quickly; long-term bonds lock up money for years. "
    "The relationship between yields at different maturities tells a story about market expectations. "
    "A normal yield curve — where long-term yields are higher than short-term ones — "
    "suggests confidence in future growth.\n\n"
    "At the base of the entire system are two simple activities: "
    "banks accept deposits from savers and make lending decisions to borrowers. "
    "The deposit rate is what banks pay savers; the lending rate is what they charge borrowers. "
    "The gap between these two rates is the bank's profit margin. "
    "The overnight rate — the rate at which banks lend to each other for just one night — "
    "is the most sensitive indicator of the central bank's current policy stance.\n\n"
    "Understanding monetary policy is understanding the heartbeat of the economy. "
    "Every time you read that the central bank has raised or lowered rates, "
    "you are reading about a decision that will touch the lives of millions — "
    "from the factory worker whose company may hire or lay off staff, "
    "to the student deciding whether to take out a loan for graduate school. "
    "The language of monetary policy is the language of modern economics, "
    "and now you have the vocabulary to read it."
)

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Monetary Policy – Chính Sách Tiền Tệ",
    "contentTypeTags": [],
    "description": (
        "HÃY TƯỞNG TƯỢNG BẠN ĐANG NGỒI TRONG PHÒNG HỌP CỦA NGÂN HÀNG TRUNG ƯƠNG — VÀ QUYẾT ĐỊNH LÃI SUẤT CỦA BẠN SẼ ẢNH HƯỞNG ĐẾN 100 TRIỆU NGƯỜI.\n\n"
        "Mỗi tháng, Ngân hàng Nhà nước Việt Nam họp và đưa ra quyết định mà ít ai để ý — "
        "nhưng nó ảnh hưởng trực tiếp đến tiền thuê nhà bạn trả, lãi suất vay mua xe, "
        "và thậm chí giá ly cà phê sáng. Bạn đọc tin 'Ngân hàng trung ương tăng lãi suất' "
        "nhưng không hiểu vì sao điều đó khiến cổ phiếu lao dốc và doanh nghiệp ngừng tuyển dụng.\n\n"
        "Chính sách tiền tệ giống như hệ thống tuần hoàn máu của nền kinh tế — "
        "bạn không nhìn thấy nó hoạt động, nhưng nếu nó ngừng chảy, mọi thứ sụp đổ. "
        "Lãi suất là nhịp tim, thanh khoản là dòng máu, và ngân hàng trung ương là trái tim "
        "bơm tiền đi khắp cơ thể kinh tế.\n\n"
        "Sau bài học này, bạn sẽ đọc được bản tin của Bloomberg hay Reuters về quyết định lãi suất "
        "mà không cần dừng lại tra từ, hiểu được vì sao Fed tăng interest rate lại ảnh hưởng đến Việt Nam, "
        "và tự tin thảo luận về monetary policy trong lớp kinh tế vĩ mô.\n\n"
        "18 từ vựng — từ monetary đến overnight — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kinh tế vĩ mô, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về chính sách tiền tệ — "
            "công cụ mạnh nhất mà ngân hàng trung ương sử dụng để điều hành nền kinh tế. "
            "Bạn sẽ học monetary, interest, central, reserve, liquidity, credit trong phần đầu tiên, "
            "nơi bài đọc giải thích cách ngân hàng trung ương kiểm soát dòng tiền trong nền kinh tế. "
            "Tiếp theo là inflation, target, tighten, ease, transmission, benchmark — "
            "những từ giúp bạn hiểu vì sao ngân hàng trung ương tăng hoặc giảm lãi suất "
            "và quyết định đó lan tỏa ra toàn bộ nền kinh tế như thế nào. "
            "Cuối cùng, quantitative, yield, maturity, deposit, lending, overnight "
            "đưa bạn vào thế giới của các công cụ tiền tệ hiện đại và thị trường liên ngân hàng. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tin tức tài chính quốc tế về chính sách tiền tệ — "
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
                    "description": "Chào mừng bạn đến với bài học về chính sách tiền tệ và ngân hàng trung ương.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ tư trong chuỗi từ vựng Kinh tế vĩ mô — "
                            "chủ đề hôm nay là Chính sách tiền tệ, hay trong tiếng Anh là Monetary Policy. "
                            "Đây là một trong những công cụ quan trọng nhất mà chính phủ sử dụng "
                            "để điều hành nền kinh tế. Nếu chính sách tài khóa là về thuế và chi tiêu, "
                            "thì chính sách tiền tệ là về lãi suất và lượng tiền trong lưu thông.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: monetary, interest, central, reserve, liquidity, và credit. "
                            "Đây là những từ bạn sẽ gặp mỗi khi đọc tin tức về ngân hàng trung ương "
                            "hay quyết định lãi suất.\n\n"
                            "Từ đầu tiên là monetary — tính từ — nghĩa là thuộc về tiền tệ, "
                            "liên quan đến tiền và hệ thống tiền tệ của một quốc gia. "
                            "Ví dụ: 'The central bank uses monetary tools to control the amount of money circulating in the economy.' "
                            "Trong bài đọc, monetary xuất hiện khi nói về chính sách tiền tệ — "
                            "tập hợp các quyết định của ngân hàng trung ương nhằm ổn định giá cả và thúc đẩy tăng trưởng.\n\n"
                            "Từ thứ hai là interest — danh từ — nghĩa là lãi suất, "
                            "số tiền mà người vay phải trả thêm cho người cho vay, tính theo tỷ lệ phần trăm. "
                            "Ví dụ: 'When the central bank raises the interest rate, borrowing becomes more expensive for businesses and consumers.' "
                            "Trong bài đọc, interest là biến số trung tâm — "
                            "ngân hàng trung ương điều chỉnh lãi suất để tác động đến toàn bộ nền kinh tế.\n\n"
                            "Từ thứ ba là central — tính từ — trong ngữ cảnh kinh tế nghĩa là trung ương, "
                            "thường đi kèm với 'bank' để chỉ ngân hàng trung ương. "
                            "Ví dụ: 'The central bank of Vietnam is called the State Bank of Vietnam, and it manages the country's monetary policy.' "
                            "Trong bài đọc, central bank là tổ chức chịu trách nhiệm "
                            "kiểm soát lượng tiền và lãi suất trong nền kinh tế.\n\n"
                            "Từ thứ tư là reserve — danh từ — nghĩa là dự trữ, "
                            "lượng tiền mà các ngân hàng thương mại phải giữ lại và không được cho vay. "
                            "Ví dụ: 'Banks must keep a certain percentage of deposits as reserves to ensure they can meet withdrawal demands.' "
                            "Trong bài đọc, reserve là một công cụ chính sách — "
                            "khi ngân hàng trung ương tăng tỷ lệ dự trữ bắt buộc, ngân hàng thương mại có ít tiền hơn để cho vay.\n\n"
                            "Từ thứ năm là liquidity — danh từ — nghĩa là thanh khoản, "
                            "khả năng chuyển đổi tài sản thành tiền mặt một cách nhanh chóng. "
                            "Ví dụ: 'During a financial crisis, liquidity dries up because banks become afraid to lend to each other.' "
                            "Trong bài đọc, liquidity mô tả dòng tiền chảy trong hệ thống ngân hàng — "
                            "khi thanh khoản dồi dào, doanh nghiệp dễ vay vốn; khi thanh khoản cạn kiệt, nền kinh tế đóng băng.\n\n"
                            "Từ cuối cùng là credit — danh từ — nghĩa là tín dụng, "
                            "khả năng vay tiền dựa trên cam kết sẽ trả lại trong tương lai. "
                            "Ví dụ: 'Small businesses depend on credit from banks to buy inventory and pay employees before they earn revenue.' "
                            "Trong bài đọc, credit là mạch máu của nền kinh tế — "
                            "khi tín dụng mở rộng, doanh nghiệp đầu tư và tuyển dụng; khi tín dụng thu hẹp, kinh tế chậm lại.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về ngân hàng trung ương và chính sách tiền tệ nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ngân hàng trung ương và tiền tệ",
                    "description": "Học 6 từ: monetary, interest, central, reserve, liquidity, credit",
                    "data": {"vocabList": ["monetary", "interest", "central", "reserve", "liquidity", "credit"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ngân hàng trung ương và tiền tệ",
                    "description": "Học 6 từ: monetary, interest, central, reserve, liquidity, credit",
                    "data": {"vocabList": ["monetary", "interest", "central", "reserve", "liquidity", "credit"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ngân hàng trung ương và tiền tệ",
                    "description": "Học 6 từ: monetary, interest, central, reserve, liquidity, credit",
                    "data": {"vocabList": ["monetary", "interest", "central", "reserve", "liquidity", "credit"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ngân hàng trung ương và tiền tệ",
                    "description": "Học 6 từ: monetary, interest, central, reserve, liquidity, credit",
                    "data": {"vocabList": ["monetary", "interest", "central", "reserve", "liquidity", "credit"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ngân hàng trung ương và tiền tệ",
                    "description": "Học 6 từ: monetary, interest, central, reserve, liquidity, credit",
                    "data": {"vocabList": ["monetary", "interest", "central", "reserve", "liquidity", "credit"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Ngân hàng trung ương và dòng tiền",
                    "description": "Every modern economy has a central bank — an institution responsible for managing the country's money supply.",
                    "data": {"text": S1_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Ngân hàng trung ương và dòng tiền",
                    "description": "Every modern economy has a central bank — an institution responsible for managing the country's money supply.",
                    "data": {"text": S1_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ngân hàng trung ương và dòng tiền",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": S1_READING}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ngân hàng trung ương và tiền tệ",
                    "description": "Viết câu sử dụng 6 từ vựng về ngân hàng trung ương và chính sách tiền tệ.",
                    "data": {
                        "vocabList": W1,
                        "items": [
                            {
                                "targetVocab": "monetary",
                                "prompt": "Dùng từ 'monetary' để viết một câu về chính sách tiền tệ của một quốc gia và tác động của nó đến nền kinh tế. Ví dụ: The government's monetary policy focuses on keeping inflation low while supporting economic growth through careful management of the money supply."
                            },
                            {
                                "targetVocab": "interest",
                                "prompt": "Dùng từ 'interest' để viết một câu về tác động của lãi suất đến quyết định vay vốn của doanh nghiệp hoặc người tiêu dùng. Ví dụ: The sharp rise in interest rates made many young couples postpone their plans to buy a first home."
                            },
                            {
                                "targetVocab": "central",
                                "prompt": "Dùng từ 'central' để viết một câu về vai trò của ngân hàng trung ương trong việc điều hành nền kinh tế. Ví dụ: The central bank held an emergency meeting to address the sudden drop in the national currency's value."
                            },
                            {
                                "targetVocab": "reserve",
                                "prompt": "Dùng từ 'reserve' để viết một câu về tỷ lệ dự trữ bắt buộc và ảnh hưởng của nó đến khả năng cho vay của ngân hàng. Ví dụ: By lowering the reserve requirement from eight to six percent, the central bank freed up billions of dong for commercial banks to lend."
                            },
                            {
                                "targetVocab": "liquidity",
                                "prompt": "Dùng từ 'liquidity' để viết một câu về tình trạng thanh khoản trong hệ thống ngân hàng và tác động đến doanh nghiệp. Ví dụ: The lack of liquidity in the banking system during the crisis forced many small businesses to close because they could not access short-term loans."
                            },
                            {
                                "targetVocab": "credit",
                                "prompt": "Dùng từ 'credit' để viết một câu về vai trò của tín dụng trong việc hỗ trợ tăng trưởng kinh tế. Ví dụ: Easy access to credit allowed thousands of Vietnamese farmers to invest in modern equipment and double their rice production."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về lạm phát và cơ chế truyền dẫn chính sách.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "monetary — thuộc về tiền tệ, interest — lãi suất, central — trung ương, "
                            "reserve — dự trữ, liquidity — thanh khoản, và credit — tín dụng. "
                            "Bạn đã hiểu cách ngân hàng trung ương kiểm soát dòng tiền trong nền kinh tế. "
                            "Bây giờ, chúng ta sẽ tìm hiểu vì sao ngân hàng trung ương đưa ra những quyết định đó.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: inflation, target, tighten, ease, transmission, và benchmark. "
                            "Những từ này giúp bạn hiểu mục tiêu và cơ chế hoạt động của chính sách tiền tệ — "
                            "không chỉ biết ngân hàng trung ương làm gì, mà còn hiểu tại sao và bằng cách nào.\n\n"
                            "Từ đầu tiên là inflation — danh từ — nghĩa là lạm phát, "
                            "sự tăng giá chung và liên tục của hàng hóa và dịch vụ theo thời gian. "
                            "Ví dụ: 'When inflation reaches double digits, the money in your savings account loses value faster than it earns interest.' "
                            "Trong bài đọc, inflation là kẻ thù số một mà ngân hàng trung ương phải kiểm soát — "
                            "lạm phát vừa phải là dấu hiệu kinh tế khỏe mạnh, nhưng lạm phát quá cao sẽ phá hủy sức mua.\n\n"
                            "Từ thứ hai là target — danh từ và động từ — nghĩa là mục tiêu, "
                            "mức cụ thể mà ngân hàng trung ương đặt ra để hướng tới. "
                            "Ví dụ: 'The Federal Reserve has set an inflation target of two percent, meaning it adjusts policy to keep price increases near that level.' "
                            "Trong bài đọc, target cho thấy chính sách tiền tệ không phải là phản ứng ngẫu nhiên — "
                            "mà là hành động có mục tiêu rõ ràng.\n\n"
                            "Từ thứ ba là tighten — động từ — nghĩa là thắt chặt, "
                            "làm cho chính sách tiền tệ trở nên nghiêm ngặt hơn bằng cách tăng lãi suất hoặc giảm cung tiền. "
                            "Ví dụ: 'The central bank decided to tighten monetary policy after inflation rose above five percent for three consecutive months.' "
                            "Trong bài đọc, tighten là hành động ngân hàng trung ương thực hiện khi nền kinh tế nóng quá mức.\n\n"
                            "Từ thứ tư là ease — động từ — nghĩa là nới lỏng, "
                            "làm cho chính sách tiền tệ trở nên linh hoạt hơn bằng cách giảm lãi suất hoặc tăng cung tiền. "
                            "Ví dụ: 'To fight the recession, the central bank chose to ease monetary policy by cutting the benchmark rate to a historic low.' "
                            "Trong bài đọc, ease là mặt đối lập của tighten — "
                            "ngân hàng trung ương nới lỏng khi nền kinh tế cần được kích thích.\n\n"
                            "Từ thứ năm là transmission — danh từ — nghĩa là sự truyền dẫn, "
                            "cơ chế mà qua đó quyết định chính sách tiền tệ lan tỏa từ ngân hàng trung ương "
                            "đến ngân hàng thương mại, doanh nghiệp và hộ gia đình. "
                            "Ví dụ: 'The transmission of monetary policy to the real economy can take six to twelve months, which is why central banks must plan ahead.' "
                            "Trong bài đọc, transmission giải thích vì sao khi ngân hàng trung ương thay đổi lãi suất, "
                            "bạn không thấy tác động ngay lập tức — cần thời gian để quyết định đó lan tỏa.\n\n"
                            "Từ cuối cùng là benchmark — danh từ — nghĩa là mốc chuẩn, "
                            "lãi suất tham chiếu mà tất cả các lãi suất khác trong nền kinh tế dựa vào. "
                            "Ví dụ: 'The benchmark interest rate set by the central bank influences everything from mortgage rates to the cost of business loans.' "
                            "Trong bài đọc, benchmark là điểm neo — khi lãi suất chuẩn thay đổi, "
                            "mọi lãi suất khác trong nền kinh tế đều điều chỉnh theo.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về lạm phát và cơ chế truyền dẫn chính sách tiền tệ nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Lạm phát và truyền dẫn chính sách",
                    "description": "Học 6 từ: inflation, target, tighten, ease, transmission, benchmark",
                    "data": {"vocabList": ["inflation", "target", "tighten", "ease", "transmission", "benchmark"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Lạm phát và truyền dẫn chính sách",
                    "description": "Học 6 từ: inflation, target, tighten, ease, transmission, benchmark",
                    "data": {"vocabList": ["inflation", "target", "tighten", "ease", "transmission", "benchmark"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Lạm phát và truyền dẫn chính sách",
                    "description": "Học 6 từ: inflation, target, tighten, ease, transmission, benchmark",
                    "data": {"vocabList": ["inflation", "target", "tighten", "ease", "transmission", "benchmark"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Lạm phát và truyền dẫn chính sách",
                    "description": "Học 6 từ: inflation, target, tighten, ease, transmission, benchmark",
                    "data": {"vocabList": ["inflation", "target", "tighten", "ease", "transmission", "benchmark"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Lạm phát và truyền dẫn chính sách",
                    "description": "Học 6 từ: inflation, target, tighten, ease, transmission, benchmark",
                    "data": {"vocabList": ["inflation", "target", "tighten", "ease", "transmission", "benchmark"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Lạm phát và cơ chế truyền dẫn",
                    "description": "Central banks do not change interest rates randomly.",
                    "data": {"text": S2_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lạm phát và cơ chế truyền dẫn",
                    "description": "Central banks do not change interest rates randomly.",
                    "data": {"text": S2_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lạm phát và cơ chế truyền dẫn",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": S2_READING}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Lạm phát và truyền dẫn chính sách",
                    "description": "Viết câu sử dụng 6 từ vựng về lạm phát và cơ chế chính sách tiền tệ.",
                    "data": {
                        "vocabList": W2,
                        "items": [
                            {
                                "targetVocab": "inflation",
                                "prompt": "Dùng từ 'inflation' để viết một câu về tác động của lạm phát đến đời sống hàng ngày của người dân. Ví dụ: Rising inflation means that the same basket of groceries that cost five hundred thousand dong last year now costs nearly six hundred thousand."
                            },
                            {
                                "targetVocab": "target",
                                "prompt": "Dùng từ 'target' để viết một câu về mục tiêu lạm phát mà ngân hàng trung ương đặt ra. Ví dụ: The State Bank of Vietnam set an inflation target of four percent for the year, signaling its commitment to price stability."
                            },
                            {
                                "targetVocab": "tighten",
                                "prompt": "Dùng từ 'tighten' để viết một câu về việc ngân hàng trung ương thắt chặt chính sách tiền tệ khi lạm phát tăng cao. Ví dụ: The central bank had to tighten monetary policy aggressively after food and energy prices pushed inflation above seven percent."
                            },
                            {
                                "targetVocab": "ease",
                                "prompt": "Dùng từ 'ease' để viết một câu về việc nới lỏng chính sách tiền tệ để hỗ trợ nền kinh tế trong thời kỳ suy thoái. Ví dụ: To help the economy recover from the pandemic, the central bank decided to ease policy by cutting rates three times in six months."
                            },
                            {
                                "targetVocab": "transmission",
                                "prompt": "Dùng từ 'transmission' để viết một câu về cách quyết định lãi suất của ngân hàng trung ương ảnh hưởng đến nền kinh tế thực. Ví dụ: The transmission of the rate cut to mortgage markets took several months, but eventually home loan rates dropped by a full percentage point."
                            },
                            {
                                "targetVocab": "benchmark",
                                "prompt": "Dùng từ 'benchmark' để viết một câu về lãi suất chuẩn và vai trò của nó trong hệ thống tài chính. Ví dụ: All commercial banks in the country adjust their lending rates based on the benchmark rate announced by the central bank each quarter."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về công cụ tiền tệ hiện đại và thị trường liên ngân hàng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: monetary, interest, central, reserve, liquidity, credit — "
                            "những khái niệm cơ bản về ngân hàng trung ương và dòng tiền trong nền kinh tế. "
                            "Trong phần 2, bạn đã học thêm inflation, target, tighten, ease, transmission, benchmark — "
                            "giúp bạn hiểu vì sao và bằng cách nào ngân hàng trung ương điều chỉnh chính sách.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào thế giới của các công cụ tiền tệ hiện đại "
                            "và thị trường liên ngân hàng — nơi mà những quyết định chính sách trở thành hành động thực tế. "
                            "Bạn sẽ học 6 từ mới: quantitative, yield, maturity, deposit, lending, và overnight.\n\n"
                            "Từ đầu tiên là quantitative — tính từ — nghĩa là định lượng, "
                            "liên quan đến số lượng hoặc quy mô. Trong kinh tế, từ này thường đi kèm với 'easing' "
                            "để chỉ chính sách nới lỏng định lượng — khi ngân hàng trung ương bơm tiền vào nền kinh tế "
                            "bằng cách mua trái phiếu với số lượng lớn. "
                            "Ví dụ: 'The Federal Reserve launched a massive quantitative easing program, buying trillions of dollars in bonds to stimulate the economy.' "
                            "Trong bài đọc, quantitative mô tả quy mô khổng lồ của các chương trình mua tài sản "
                            "mà ngân hàng trung ương thực hiện khi lãi suất đã giảm về gần không.\n\n"
                            "Từ thứ hai là yield — danh từ — nghĩa là lợi suất, "
                            "tỷ lệ lợi nhuận mà nhà đầu tư nhận được khi nắm giữ trái phiếu. "
                            "Ví dụ: 'When the central bank buys government bonds, the increased demand pushes bond prices up and yields down.' "
                            "Trong bài đọc, yield là chỉ số quan trọng — "
                            "lợi suất trái phiếu phản ánh kỳ vọng của thị trường về lãi suất và lạm phát trong tương lai.\n\n"
                            "Từ thứ ba là maturity — danh từ — nghĩa là kỳ hạn, "
                            "thời điểm mà người vay phải hoàn trả toàn bộ số tiền gốc của trái phiếu. "
                            "Ví dụ: 'A ten-year government bond reaches maturity in 2034, at which point the government repays the full face value to the bondholder.' "
                            "Trong bài đọc, maturity giúp phân biệt giữa trái phiếu ngắn hạn và dài hạn — "
                            "mỗi loại có mức lợi suất và rủi ro khác nhau.\n\n"
                            "Từ thứ tư là deposit — danh từ — nghĩa là tiền gửi, "
                            "số tiền mà khách hàng đặt vào tài khoản ngân hàng. "
                            "Ví dụ: 'Vietnamese households keep most of their savings in bank deposits because they consider it the safest form of investment.' "
                            "Trong bài đọc, deposit là nguồn vốn chính của ngân hàng — "
                            "ngân hàng nhận tiền gửi từ người tiết kiệm và cho vay lại với lãi suất cao hơn.\n\n"
                            "Từ thứ năm là lending — danh từ — nghĩa là hoạt động cho vay, "
                            "việc cung cấp tiền cho người vay với kỳ vọng sẽ được hoàn trả kèm lãi suất. "
                            "Ví dụ: 'Bank lending to small and medium enterprises increased by fifteen percent after the central bank cut the benchmark rate.' "
                            "Trong bài đọc, lending là cầu nối giữa chính sách tiền tệ và nền kinh tế thực — "
                            "khi ngân hàng cho vay nhiều hơn, doanh nghiệp có vốn để mở rộng.\n\n"
                            "Từ cuối cùng là overnight — tính từ — nghĩa là qua đêm, "
                            "mô tả các khoản vay rất ngắn hạn giữa các ngân hàng, thường chỉ kéo dài một đêm. "
                            "Ví dụ: 'The overnight lending rate between banks jumped sharply, signaling that liquidity in the financial system was tightening.' "
                            "Trong bài đọc, overnight rate là chỉ báo nhạy nhất về lập trường chính sách tiền tệ — "
                            "khi lãi suất qua đêm tăng, tất cả các lãi suất khác đều có xu hướng tăng theo.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về công cụ tiền tệ hiện đại nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Công cụ tiền tệ và thị trường liên ngân hàng",
                    "description": "Học 6 từ: quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ["quantitative", "yield", "maturity", "deposit", "lending", "overnight"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Công cụ tiền tệ và thị trường liên ngân hàng",
                    "description": "Học 6 từ: quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ["quantitative", "yield", "maturity", "deposit", "lending", "overnight"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Công cụ tiền tệ và thị trường liên ngân hàng",
                    "description": "Học 6 từ: quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ["quantitative", "yield", "maturity", "deposit", "lending", "overnight"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Công cụ tiền tệ và thị trường liên ngân hàng",
                    "description": "Học 6 từ: quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ["quantitative", "yield", "maturity", "deposit", "lending", "overnight"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Công cụ tiền tệ và thị trường liên ngân hàng",
                    "description": "Học 6 từ: quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ["quantitative", "yield", "maturity", "deposit", "lending", "overnight"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nới lỏng định lượng và thị trường trái phiếu",
                    "description": "Sometimes, lowering the benchmark interest rate to zero is not enough to revive a struggling economy.",
                    "data": {"text": S3_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nới lỏng định lượng và thị trường trái phiếu",
                    "description": "Sometimes, lowering the benchmark interest rate to zero is not enough to revive a struggling economy.",
                    "data": {"text": S3_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nới lỏng định lượng và thị trường trái phiếu",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": S3_READING}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Công cụ tiền tệ và thị trường liên ngân hàng",
                    "description": "Viết câu sử dụng 6 từ vựng về công cụ tiền tệ hiện đại.",
                    "data": {
                        "vocabList": W3,
                        "items": [
                            {
                                "targetVocab": "quantitative",
                                "prompt": "Dùng từ 'quantitative' để viết một câu về chương trình nới lỏng định lượng của ngân hàng trung ương và tác động của nó. Ví dụ: The Bank of Japan's quantitative easing program was so large that the central bank ended up owning more government bonds than any other investor in the country."
                            },
                            {
                                "targetVocab": "yield",
                                "prompt": "Dùng từ 'yield' để viết một câu về lợi suất trái phiếu và mối quan hệ với giá trái phiếu. Ví dụ: The yield on ten-year government bonds fell to a record low after investors rushed to buy safe assets during the stock market crash."
                            },
                            {
                                "targetVocab": "maturity",
                                "prompt": "Dùng từ 'maturity' để viết một câu về kỳ hạn trái phiếu và chiến lược đầu tư. Ví dụ: Investors who buy bonds with a thirty-year maturity accept more risk but typically earn higher returns than those who choose short-term bonds."
                            },
                            {
                                "targetVocab": "deposit",
                                "prompt": "Dùng từ 'deposit' để viết một câu về tiền gửi ngân hàng và vai trò của nó trong hệ thống tài chính. Ví dụ: The total value of household deposits in Vietnamese banks exceeded five thousand trillion dong, providing a stable source of funding for the banking system."
                            },
                            {
                                "targetVocab": "lending",
                                "prompt": "Dùng từ 'lending' để viết một câu về hoạt động cho vay của ngân hàng và tác động đến tăng trưởng kinh tế. Ví dụ: Aggressive lending by commercial banks fueled a construction boom, but it also raised concerns about the quality of loans on their books."
                            },
                            {
                                "targetVocab": "overnight",
                                "prompt": "Dùng từ 'overnight' để viết một câu về lãi suất qua đêm trên thị trường liên ngân hàng. Ví dụ: The overnight rate spiked to nine percent at the end of the quarter as banks scrambled to meet their reserve requirements before the deadline."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Chính sách tiền tệ. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "monetary — thuộc về tiền tệ, interest — lãi suất, central — trung ương, "
                            "reserve — dự trữ, liquidity — thanh khoản, và credit — tín dụng. "
                            "Đây là bộ khung cơ bản để hiểu cách ngân hàng trung ương vận hành.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "inflation — lạm phát, target — mục tiêu, tighten — thắt chặt, "
                            "ease — nới lỏng, transmission — truyền dẫn, và benchmark — mốc chuẩn. "
                            "Những từ này giúp bạn hiểu vì sao ngân hàng trung ương hành động "
                            "và quyết định đó lan tỏa ra nền kinh tế như thế nào.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "quantitative — định lượng, yield — lợi suất, maturity — kỳ hạn, "
                            "deposit — tiền gửi, lending — cho vay, và overnight — qua đêm. "
                            "Đây là những từ về công cụ tiền tệ hiện đại và thị trường liên ngân hàng.\n\n"
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
                    "description": "Học 18 từ: monetary, interest, central, reserve, liquidity, credit, inflation, target, tighten, ease, transmission, benchmark, quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monetary, interest, central, reserve, liquidity, credit, inflation, target, tighten, ease, transmission, benchmark, quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monetary, interest, central, reserve, liquidity, credit, inflation, target, tighten, ease, transmission, benchmark, quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monetary, interest, central, reserve, liquidity, credit, inflation, target, tighten, ease, transmission, benchmark, quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monetary, interest, central, reserve, liquidity, credit, inflation, target, tighten, ease, transmission, benchmark, quantitative, yield, maturity, deposit, lending, overnight",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng chính sách tiền tệ",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "monetary",
                                "prompt": "Dùng từ 'monetary' để viết một câu về sự phối hợp giữa chính sách tiền tệ và chính sách tài khóa. Ví dụ: Effective monetary policy requires coordination with fiscal policy — the central bank controls interest rates while the government manages taxes and spending."
                            },
                            {
                                "targetVocab": "interest",
                                "prompt": "Dùng từ 'interest' để viết một câu về ảnh hưởng của lãi suất đến thị trường bất động sản. Ví dụ: The record-low interest rate environment encouraged a wave of home buying, pushing property prices in major Vietnamese cities to all-time highs."
                            },
                            {
                                "targetVocab": "central",
                                "prompt": "Dùng từ 'central' để viết một câu về sự độc lập của ngân hàng trung ương trong việc ra quyết định. Ví dụ: A truly independent central bank makes decisions based on economic data rather than political pressure, which helps maintain public trust in the currency."
                            },
                            {
                                "targetVocab": "reserve",
                                "prompt": "Dùng từ 'reserve' để viết một câu về dự trữ ngoại hối và vai trò bảo vệ nền kinh tế. Ví dụ: Vietnam's foreign exchange reserves have grown steadily over the past decade, giving the central bank more firepower to defend the dong during currency crises."
                            },
                            {
                                "targetVocab": "liquidity",
                                "prompt": "Dùng từ 'liquidity' để viết một câu về thanh khoản trên thị trường chứng khoán. Ví dụ: Trading volume on the Ho Chi Minh Stock Exchange surged, indicating strong liquidity that attracted both domestic and foreign investors."
                            },
                            {
                                "targetVocab": "credit",
                                "prompt": "Dùng từ 'credit' để viết một câu về tăng trưởng tín dụng và rủi ro nợ xấu. Ví dụ: Rapid credit growth of over twenty percent per year raised alarm bells at the central bank, which feared that too many risky loans could lead to a banking crisis."
                            },
                            {
                                "targetVocab": "inflation",
                                "prompt": "Dùng từ 'inflation' để viết một câu so sánh lạm phát ở hai thời kỳ khác nhau. Ví dụ: Vietnam experienced double-digit inflation in 2008 and 2011, but careful monetary management has kept inflation below four percent in recent years."
                            },
                            {
                                "targetVocab": "target",
                                "prompt": "Dùng từ 'target' để viết một câu về cách mục tiêu lạm phát giúp ổn định kỳ vọng của thị trường. Ví dụ: By publicly announcing its inflation target, the central bank helps businesses and consumers plan their spending and investment decisions with greater confidence."
                            },
                            {
                                "targetVocab": "tighten",
                                "prompt": "Dùng từ 'tighten' để viết một câu về hậu quả của việc thắt chặt chính sách tiền tệ quá nhanh. Ví dụ: When the central bank chose to tighten policy too quickly, the sudden rise in borrowing costs pushed several overleveraged real estate developers into bankruptcy."
                            },
                            {
                                "targetVocab": "ease",
                                "prompt": "Dùng từ 'ease' để viết một câu về tác động tích cực của việc nới lỏng chính sách đến doanh nghiệp nhỏ. Ví dụ: The decision to ease monetary policy gave small business owners access to cheaper loans, helping them survive the economic downturn and retain their employees."
                            },
                            {
                                "targetVocab": "transmission",
                                "prompt": "Dùng từ 'transmission' để viết một câu về độ trễ trong cơ chế truyền dẫn chính sách tiền tệ. Ví dụ: The slow transmission of rate cuts to the real economy frustrated policymakers, who expected businesses to start borrowing and investing much sooner."
                            },
                            {
                                "targetVocab": "benchmark",
                                "prompt": "Dùng từ 'benchmark' để viết một câu về sự thay đổi lãi suất chuẩn và phản ứng của thị trường tài chính. Ví dụ: The unexpected increase in the benchmark rate sent shockwaves through the bond market, causing prices to drop and yields to spike within hours."
                            },
                            {
                                "targetVocab": "quantitative",
                                "prompt": "Dùng từ 'quantitative' để viết một câu về tranh luận xung quanh hiệu quả của nới lỏng định lượng. Ví dụ: Critics argue that quantitative easing mainly benefits wealthy investors who own stocks and bonds, while doing little to help ordinary workers struggling with stagnant wages."
                            },
                            {
                                "targetVocab": "yield",
                                "prompt": "Dùng từ 'yield' để viết một câu về đường cong lợi suất và tín hiệu kinh tế. Ví dụ: An inverted yield curve — where short-term yields exceed long-term ones — has historically been a reliable predictor of economic recession."
                            },
                            {
                                "targetVocab": "maturity",
                                "prompt": "Dùng từ 'maturity' để viết một câu về chiến lược quản lý danh mục trái phiếu. Ví dụ: The pension fund diversified its portfolio by holding bonds with maturities ranging from two years to thirty years, balancing risk and return."
                            },
                            {
                                "targetVocab": "deposit",
                                "prompt": "Dùng từ 'deposit' để viết một câu về cạnh tranh lãi suất tiền gửi giữa các ngân hàng. Ví dụ: Several commercial banks raised their deposit rates to attract more savings from households, intensifying competition for funding in the banking sector."
                            },
                            {
                                "targetVocab": "lending",
                                "prompt": "Dùng từ 'lending' để viết một câu về tiêu chuẩn cho vay và rủi ro hệ thống. Ví dụ: Loose lending standards in the years before the crisis meant that many borrowers received loans they could never repay, eventually triggering a wave of defaults."
                            },
                            {
                                "targetVocab": "overnight",
                                "prompt": "Dùng từ 'overnight' để viết một câu về biến động lãi suất qua đêm và tác động đến hệ thống ngân hàng. Ví dụ: The central bank injected emergency liquidity into the system after the overnight rate surged to fifteen percent, threatening the stability of smaller banks."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về chính sách tiền tệ.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về chính sách tiền tệ — từ vai trò của ngân hàng trung ương "
                            "đến các công cụ hiện đại như nới lỏng định lượng.\n\n"
                            "Bạn sẽ gặp lại monetary, interest, central, reserve, liquidity, credit "
                            "trong phần mở đầu về cơ chế hoạt động của ngân hàng trung ương. "
                            "Tiếp theo, inflation, target, tighten, ease, transmission, benchmark "
                            "sẽ giúp bạn hiểu sâu hơn về mục tiêu và cách thức điều hành chính sách. "
                            "Và cuối cùng, quantitative, yield, maturity, deposit, lending, overnight "
                            "sẽ đưa bạn vào thế giới thị trường trái phiếu và liên ngân hàng.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chính sách tiền tệ — Bức tranh toàn cảnh",
                    "description": "Money makes the modern world turn, but it does not manage itself.",
                    "data": {"text": S5_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chính sách tiền tệ — Bức tranh toàn cảnh",
                    "description": "Money makes the modern world turn, but it does not manage itself.",
                    "data": {"text": S5_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chính sách tiền tệ — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": S5_READING}
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chính sách tiền tệ",
                    "description": "Viết đoạn văn tiếng Anh phân tích về chính sách tiền tệ sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống kinh tế thực tế liên quan đến chính sách tiền tệ. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích điều gì xảy ra khi ngân hàng trung ương quyết định tighten monetary policy bằng cách tăng benchmark interest rate. Giải thích cơ chế transmission từ quyết định lãi suất đến hoạt động lending của ngân hàng thương mại, và tác động cuối cùng đến inflation và credit trong nền kinh tế.",
                            "Hãy giải thích vì sao một số ngân hàng trung ương phải sử dụng quantitative easing khi lãi suất đã giảm về gần không. Phân tích cách chương trình mua trái phiếu ảnh hưởng đến yield, liquidity trong hệ thống tài chính, và deposit cùng lending rates mà người dân và doanh nghiệp phải đối mặt."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay sâu lắng.",
                    "data": {
                        "text": (
                            "Bạn đã đi đến cuối hành trình rồi. Hãy dừng lại một chút — "
                            "không phải để vội vàng sang bài tiếp theo, mà để thật sự cảm nhận "
                            "quãng đường bạn vừa đi qua.\n\n"
                            "Khi bắt đầu bài học này, có thể bạn chỉ biết 'lãi suất' và 'ngân hàng trung ương' "
                            "như những cụm từ xuất hiện trên bản tin tối — xa xôi và trừu tượng. "
                            "Nhưng bây giờ, bạn đã có một bộ ngôn ngữ để đọc, hiểu và suy ngẫm "
                            "về cách tiền tệ vận hành trong thế giới thực.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất — lần này, "
                            "tôi muốn bạn không chỉ nhớ định nghĩa, mà còn tự hỏi: "
                            "từ này nói gì về cách thế giới vận hành?\n\n"
                            "Monetary — thuộc về tiền tệ. Mọi thứ bạn học hôm nay đều xoay quanh từ này. "
                            "Monetary policy không chỉ là thuật ngữ trong sách giáo khoa — "
                            "nó là tập hợp những quyết định ảnh hưởng đến cuộc sống của hàng triệu người mỗi ngày. "
                            "Ví dụ mới: The debate over monetary policy dominated the economics conference, "
                            "with some experts calling for aggressive rate cuts and others warning about the risks of inflation.\n\n"
                            "Transmission — sự truyền dẫn. Đây là từ khiến tôi suy nghĩ nhiều nhất. "
                            "Một quyết định được đưa ra trong phòng họp kín của ngân hàng trung ương, "
                            "và vài tháng sau, nó thay đổi cuộc sống của một người nông dân ở đồng bằng sông Cửu Long "
                            "hay một sinh viên đang cân nhắc vay tiền học đại học. "
                            "Ví dụ mới: The transmission of the rate hike was felt most acutely by first-time homebuyers, "
                            "whose monthly mortgage payments increased by nearly twenty percent.\n\n"
                            "Liquidity — thanh khoản. Từ này nghe có vẻ kỹ thuật, "
                            "nhưng bản chất nó rất đơn giản: tiền có chảy không? "
                            "Khi liquidity dồi dào, nền kinh tế sống động. Khi nó cạn kiệt, mọi thứ đóng băng. "
                            "Ví dụ mới: The startup ecosystem in Ho Chi Minh City thrives partly because "
                            "there is strong liquidity in the venture capital market, with investors eager to fund promising ideas.\n\n"
                            "Yield — lợi suất. Mỗi khi bạn đọc tin về thị trường trái phiếu, "
                            "yield sẽ là từ bạn gặp đầu tiên. Nó cho bạn biết nhà đầu tư kỳ vọng gì "
                            "về tương lai của nền kinh tế. "
                            "Ví dụ mới: When the yield on government bonds drops below the inflation rate, "
                            "savers effectively lose money by holding bonds — pushing them toward riskier investments.\n\n"
                            "Overnight — qua đêm. Từ này nhỏ bé nhưng mang sức nặng lớn. "
                            "Lãi suất overnight là nhiệt kế chính xác nhất đo sức khỏe của hệ thống ngân hàng. "
                            "Khi nó tăng đột biến, đó là dấu hiệu có gì đó không ổn. "
                            "Ví dụ mới: Analysts closely watch the overnight rate because sudden spikes often signal "
                            "that banks are struggling to find enough cash to meet their daily obligations.\n\n"
                            "Benchmark — mốc chuẩn. Trong một thế giới đầy biến động, "
                            "benchmark là điểm neo giúp mọi người định hướng. "
                            "Khi ngân hàng trung ương thay đổi benchmark rate, "
                            "nó gửi tín hiệu đến toàn bộ nền kinh tế về hướng đi phía trước. "
                            "Ví dụ mới: The central bank's decision to hold the benchmark rate steady "
                            "reassured markets that policymakers were confident about the economic recovery.\n\n"
                            "Bạn biết không, điều tôi muốn bạn mang theo sau bài học này "
                            "không chỉ là 18 từ vựng. Tôi muốn bạn mang theo một cách nhìn mới. "
                            "Lần tới khi bạn đọc tin 'Ngân hàng Nhà nước giữ nguyên lãi suất', "
                            "bạn sẽ không chỉ lướt qua — bạn sẽ hiểu quyết định đó có nghĩa gì "
                            "cho doanh nghiệp, cho người vay mua nhà, cho cả nền kinh tế.\n\n"
                            "Tiếng Anh kinh tế không phải là rào cản — nó là cánh cửa dẫn đến hiểu biết sâu hơn. "
                            "Và bạn vừa bước qua cánh cửa đó.\n\n"
                            "Hãy tiếp tục đọc, tiếp tục hỏi, tiếp tục suy ngẫm. "
                            "Hẹn gặp lại bạn ở bài học tiếp theo nhé."
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Monetary Policy – Chính Sách Tiền Tệ' AND uid = '{UID}' ORDER BY created_at;")
