"""
Create curriculum: Exchange Markets – Thị Trường Ngoại Hối
Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa (International Trade), curriculum #3
18 words | 5 sessions | vivid_scenario tone | quiet awe farewell
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
W1 = ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"]
W2 = ["forex", "spot", "forward", "hedge", "speculation", "volatility"]
W3 = ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Exchange Markets – Thị Trường Ngoại Hối",
    "contentTypeTags": [],
    "description": (
        "HÃY TƯỞNG TƯỢNG BẠN ĐANG NGỒI TRƯỚC MÀN HÌNH BLOOMBERG LÚC 5 GIỜ SÁNG, "
        "NHÌN ĐỒNG YÊN NHẬT LẠO DỐC VÀ ĐỒNG DOLLAR TĂNG VỌT — BẠN CÓ HIỂU CHUYỆN GÌ ĐANG XẢY RA KHÔNG?\n\n"
        "Mỗi ngày, hơn 7.500 tỷ đô la Mỹ được giao dịch trên thị trường ngoại hối — "
        "lớn hơn GDP cả năm của hầu hết các quốc gia. Khi bạn đọc tin 'VND depreciation against USD', "
        "bạn biết đồng Việt Nam yếu đi, nhưng bạn có giải thích được vì sao, "
        "và điều đó ảnh hưởng thế nào đến giá xăng bạn đổ mỗi tuần không?\n\n"
        "Thị trường ngoại hối giống như đại dương — bề mặt có vẻ phẳng lặng, "
        "nhưng bên dưới là những dòng chảy khổng lồ của tiền tệ, đầu cơ và chính sách ngân hàng trung ương. "
        "Nếu không có từ vựng để đọc bản đồ dòng chảy đó, bạn sẽ mãi chỉ đứng trên bờ nhìn ra.\n\n"
        "Sau khóa học này, bạn sẽ đọc được báo cáo forex bằng tiếng Anh mà không cần dừng lại tra từ, "
        "hiểu được tại sao ngân hàng trung ương can thiệp vào tỷ giá, "
        "và tự tin thảo luận về floating rate hay pegged regime trong lớp học.\n\n"
        "18 từ vựng — từ exchange đến intervention — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy tài chính quốc tế, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về thị trường ngoại hối — "
            "nơi hàng nghìn tỷ đô la được giao dịch mỗi ngày và tỷ giá ảnh hưởng đến mọi nền kinh tế. "
            "Bạn sẽ học exchange, currency, appreciation, depreciation, floating, pegged trong phần đầu tiên, "
            "nơi bài đọc giải thích cách tỷ giá hối đoái được xác định và vì sao đồng tiền tăng giảm. "
            "Tiếp theo là forex, spot, forward, hedge, speculation, volatility — "
            "những từ đưa bạn vào thế giới giao dịch ngoại hối thực tế, nơi các ngân hàng và quỹ đầu tư "
            "mua bán tiền tệ để phòng ngừa rủi ro hoặc kiếm lời. "
            "Cuối cùng, arbitrage, devaluation, revaluation, convertible, reserve, intervention "
            "giúp bạn hiểu vai trò của ngân hàng trung ương và chính sách tiền tệ quốc tế. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tin tức tài chính quốc tế bằng tiếng Anh — "
            "không còn bỡ ngỡ trước những biến động tỷ giá."
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
                    "description": "Chào mừng bạn đến với bài học về thị trường ngoại hối — nền tảng tài chính quốc tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học về Thị trường Ngoại hối — "
                            "hay trong tiếng Anh là Exchange Markets. "
                            "Đây là thị trường tài chính lớn nhất thế giới, nơi các đồng tiền được mua bán "
                            "liên tục 24 giờ mỗi ngày, từ Tokyo đến London đến New York.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: exchange, currency, appreciation, "
                            "depreciation, floating, và pegged. "
                            "Đây là những từ nền tảng giúp bạn hiểu cách tỷ giá hối đoái hoạt động.\n\n"
                            "Từ đầu tiên là exchange — danh từ và động từ — nghĩa là trao đổi, hối đoái. "
                            "Trong ngữ cảnh tài chính, exchange rate là tỷ giá hối đoái — "
                            "giá của một đồng tiền tính bằng đồng tiền khác. "
                            "Ví dụ: 'The exchange rate between the Vietnamese dong and the US dollar "
                            "affects the price of imported goods in Vietnam.' "
                            "Trong bài đọc, exchange được dùng để mô tả quá trình chuyển đổi tiền tệ "
                            "khi các quốc gia giao thương với nhau.\n\n"
                            "Từ thứ hai là currency — danh từ — nghĩa là tiền tệ, đồng tiền của một quốc gia. "
                            "Ví dụ: 'The Vietnamese dong is the official currency of Vietnam, "
                            "while the euro is used by nineteen countries in Europe.' "
                            "Trong bài đọc, currency xuất hiện khi nói về các đồng tiền khác nhau "
                            "được giao dịch trên thị trường quốc tế.\n\n"
                            "Từ thứ ba là appreciation — danh từ — trong tài chính nghĩa là sự tăng giá "
                            "của một đồng tiền so với đồng tiền khác. "
                            "Ví dụ: 'The appreciation of the Japanese yen makes Japanese exports more expensive "
                            "for foreign buyers.' "
                            "Trong bài đọc, appreciation mô tả khi một đồng tiền trở nên mạnh hơn — "
                            "bạn cần ít đồng tiền đó hơn để mua cùng một lượng ngoại tệ.\n\n"
                            "Từ thứ tư là depreciation — danh từ — nghĩa là sự mất giá, "
                            "khi một đồng tiền yếu đi so với đồng tiền khác. "
                            "Ví dụ: 'The depreciation of the Turkish lira in recent years has made imports "
                            "much more expensive for Turkish consumers.' "
                            "Trong bài đọc, depreciation là mặt đối lập của appreciation — "
                            "khi đồng tiền mất giá, hàng nhập khẩu đắt hơn nhưng hàng xuất khẩu rẻ hơn.\n\n"
                            "Từ thứ năm là floating — tính từ — nghĩa là thả nổi, "
                            "mô tả chế độ tỷ giá mà giá trị đồng tiền được quyết định bởi thị trường. "
                            "Ví dụ: 'Most major economies use a floating exchange rate system "
                            "where currency values change based on supply and demand.' "
                            "Trong bài đọc, floating mô tả hệ thống mà đồng tiền tự do tăng giảm "
                            "theo cung cầu trên thị trường.\n\n"
                            "Từ cuối cùng là pegged — tính từ — nghĩa là neo cố định, "
                            "khi chính phủ giữ tỷ giá đồng tiền ở một mức cố định so với đồng tiền khác. "
                            "Ví dụ: 'Hong Kong has pegged its dollar to the US dollar since 1983 "
                            "to maintain stability in international trade.' "
                            "Trong bài đọc, pegged là chế độ đối lập với floating — "
                            "ngân hàng trung ương phải can thiệp liên tục để giữ tỷ giá ổn định.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về tỷ giá hối đoái và các chế độ tiền tệ nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tỷ giá và chế độ tiền tệ",
                    "description": "Học 6 từ: exchange, currency, appreciation, depreciation, floating, pegged",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tỷ giá và chế độ tiền tệ",
                    "description": "Học 6 từ: exchange, currency, appreciation, depreciation, floating, pegged",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tỷ giá và chế độ tiền tệ",
                    "description": "Học 6 từ: exchange, currency, appreciation, depreciation, floating, pegged",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tỷ giá và chế độ tiền tệ",
                    "description": "Học 6 từ: exchange, currency, appreciation, depreciation, floating, pegged",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Tỷ giá và chế độ tiền tệ",
                    "description": "Học 6 từ: exchange, currency, appreciation, depreciation, floating, pegged",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tỷ giá hối đoái và chế độ tiền tệ",
                    "description": "When a Vietnamese company imports machinery from Germany, it must pay in euros, not dong.",
                    "data": {
                        "text": (
                            "When a Vietnamese company imports machinery from Germany, it must pay in euros, not dong. "
                            "To get euros, the company goes to a bank and exchanges its Vietnamese currency for European currency. "
                            "The price it pays — how many dong for one euro — is the exchange rate.\n\n"
                            "An exchange rate is simply the price of one currency expressed in terms of another. "
                            "If one US dollar costs twenty-five thousand dong, the exchange rate is 25,000 VND per USD. "
                            "Exchange rates matter because they affect the cost of everything that crosses a border — "
                            "imports, exports, foreign investment, and even tourism.\n\n"
                            "When a currency becomes stronger, economists say it experiences appreciation. "
                            "If the dong appreciates against the dollar, Vietnamese importers benefit "
                            "because they need fewer dong to buy the same amount of American goods. "
                            "However, Vietnamese exporters suffer because their products become more expensive "
                            "for foreign buyers.\n\n"
                            "The opposite is depreciation. When a currency loses value relative to another, "
                            "imports become more expensive but exports become cheaper. "
                            "If the dong depreciates, a Vietnamese shoe factory can sell its products "
                            "at a lower price in dollars, making them more competitive in the American market. "
                            "But the same factory will pay more for imported leather and rubber.\n\n"
                            "How are exchange rates determined? It depends on the system a country uses. "
                            "In a floating exchange rate system, the value of a currency is set by market forces — "
                            "the supply of and demand for that currency in the foreign exchange market. "
                            "If many investors want to buy Japanese yen, the yen appreciates. "
                            "If investors sell yen and buy dollars instead, the yen depreciates. "
                            "Most major economies, including the United States, Japan, and the eurozone, "
                            "use floating rates.\n\n"
                            "Some countries, however, choose a pegged exchange rate. "
                            "Under a pegged system, the government fixes the value of its currency "
                            "to another currency — usually the US dollar. "
                            "Saudi Arabia, for example, has pegged its riyal to the dollar for decades. "
                            "A pegged rate provides stability and predictability for businesses, "
                            "but it requires the central bank to hold large amounts of foreign currency "
                            "and to intervene in the market whenever the rate drifts from the target.\n\n"
                            "Vietnam uses a managed float — a system between pure floating and a hard peg. "
                            "The State Bank of Vietnam sets a reference rate each day "
                            "and allows the dong to move within a narrow band around it. "
                            "This gives the market some flexibility while keeping the currency relatively stable."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tỷ giá hối đoái và chế độ tiền tệ",
                    "description": "When a Vietnamese company imports machinery from Germany, it must pay in euros, not dong.",
                    "data": {
                        "text": (
                            "When a Vietnamese company imports machinery from Germany, it must pay in euros, not dong. "
                            "To get euros, the company goes to a bank and exchanges its Vietnamese currency for European currency. "
                            "The price it pays — how many dong for one euro — is the exchange rate.\n\n"
                            "An exchange rate is simply the price of one currency expressed in terms of another. "
                            "If one US dollar costs twenty-five thousand dong, the exchange rate is 25,000 VND per USD. "
                            "Exchange rates matter because they affect the cost of everything that crosses a border — "
                            "imports, exports, foreign investment, and even tourism.\n\n"
                            "When a currency becomes stronger, economists say it experiences appreciation. "
                            "If the dong appreciates against the dollar, Vietnamese importers benefit "
                            "because they need fewer dong to buy the same amount of American goods. "
                            "However, Vietnamese exporters suffer because their products become more expensive "
                            "for foreign buyers.\n\n"
                            "The opposite is depreciation. When a currency loses value relative to another, "
                            "imports become more expensive but exports become cheaper. "
                            "If the dong depreciates, a Vietnamese shoe factory can sell its products "
                            "at a lower price in dollars, making them more competitive in the American market. "
                            "But the same factory will pay more for imported leather and rubber.\n\n"
                            "How are exchange rates determined? It depends on the system a country uses. "
                            "In a floating exchange rate system, the value of a currency is set by market forces — "
                            "the supply of and demand for that currency in the foreign exchange market. "
                            "If many investors want to buy Japanese yen, the yen appreciates. "
                            "If investors sell yen and buy dollars instead, the yen depreciates. "
                            "Most major economies, including the United States, Japan, and the eurozone, "
                            "use floating rates.\n\n"
                            "Some countries, however, choose a pegged exchange rate. "
                            "Under a pegged system, the government fixes the value of its currency "
                            "to another currency — usually the US dollar. "
                            "Saudi Arabia, for example, has pegged its riyal to the dollar for decades. "
                            "A pegged rate provides stability and predictability for businesses, "
                            "but it requires the central bank to hold large amounts of foreign currency "
                            "and to intervene in the market whenever the rate drifts from the target.\n\n"
                            "Vietnam uses a managed float — a system between pure floating and a hard peg. "
                            "The State Bank of Vietnam sets a reference rate each day "
                            "and allows the dong to move within a narrow band around it. "
                            "This gives the market some flexibility while keeping the currency relatively stable."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tỷ giá hối đoái và chế độ tiền tệ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When a Vietnamese company imports machinery from Germany, it must pay in euros, not dong. "
                            "To get euros, the company goes to a bank and exchanges its Vietnamese currency for European currency. "
                            "The price it pays — how many dong for one euro — is the exchange rate.\n\n"
                            "An exchange rate is simply the price of one currency expressed in terms of another. "
                            "If one US dollar costs twenty-five thousand dong, the exchange rate is 25,000 VND per USD. "
                            "Exchange rates matter because they affect the cost of everything that crosses a border — "
                            "imports, exports, foreign investment, and even tourism.\n\n"
                            "When a currency becomes stronger, economists say it experiences appreciation. "
                            "If the dong appreciates against the dollar, Vietnamese importers benefit "
                            "because they need fewer dong to buy the same amount of American goods. "
                            "However, Vietnamese exporters suffer because their products become more expensive "
                            "for foreign buyers.\n\n"
                            "The opposite is depreciation. When a currency loses value relative to another, "
                            "imports become more expensive but exports become cheaper. "
                            "If the dong depreciates, a Vietnamese shoe factory can sell its products "
                            "at a lower price in dollars, making them more competitive in the American market. "
                            "But the same factory will pay more for imported leather and rubber.\n\n"
                            "How are exchange rates determined? It depends on the system a country uses. "
                            "In a floating exchange rate system, the value of a currency is set by market forces — "
                            "the supply of and demand for that currency in the foreign exchange market. "
                            "If many investors want to buy Japanese yen, the yen appreciates. "
                            "If investors sell yen and buy dollars instead, the yen depreciates. "
                            "Most major economies, including the United States, Japan, and the eurozone, "
                            "use floating rates.\n\n"
                            "Some countries, however, choose a pegged exchange rate. "
                            "Under a pegged system, the government fixes the value of its currency "
                            "to another currency — usually the US dollar. "
                            "Saudi Arabia, for example, has pegged its riyal to the dollar for decades. "
                            "A pegged rate provides stability and predictability for businesses, "
                            "but it requires the central bank to hold large amounts of foreign currency "
                            "and to intervene in the market whenever the rate drifts from the target.\n\n"
                            "Vietnam uses a managed float — a system between pure floating and a hard peg. "
                            "The State Bank of Vietnam sets a reference rate each day "
                            "and allows the dong to move within a narrow band around it. "
                            "This gives the market some flexibility while keeping the currency relatively stable."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tỷ giá và chế độ tiền tệ",
                    "description": "Viết câu sử dụng 6 từ vựng về tỷ giá hối đoái.",
                    "data": {
                        "vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged"],
                        "items": [
                            {
                                "targetVocab": "exchange",
                                "prompt": "Dùng từ 'exchange' để viết một câu về tỷ giá hối đoái và tác động của nó đến thương mại quốc tế. Ví dụ: The exchange rate between the dong and the dollar determines how much Vietnamese coffee exporters earn when they sell to American buyers."
                            },
                            {
                                "targetVocab": "currency",
                                "prompt": "Dùng từ 'currency' để viết một câu về vai trò của đồng tiền quốc gia trong nền kinh tế. Ví dụ: A stable currency gives foreign investors confidence to put their money into a country's stock market and real estate."
                            },
                            {
                                "targetVocab": "appreciation",
                                "prompt": "Dùng từ 'appreciation' để viết một câu về tác động khi đồng tiền tăng giá đối với nhà xuất khẩu. Ví dụ: The appreciation of the Chinese yuan made Chinese-made electronics more expensive in Southeast Asian markets."
                            },
                            {
                                "targetVocab": "depreciation",
                                "prompt": "Dùng từ 'depreciation' để viết một câu về hậu quả khi đồng tiền mất giá đối với người tiêu dùng trong nước. Ví dụ: The sharp depreciation of the Argentine peso doubled the price of imported medicine within just a few months."
                            },
                            {
                                "targetVocab": "floating",
                                "prompt": "Dùng từ 'floating' để viết một câu về chế độ tỷ giá thả nổi và cách nó phản ứng với thị trường. Ví dụ: Under a floating exchange rate system, the British pound fell sharply after the Brexit referendum because investors feared economic uncertainty."
                            },
                            {
                                "targetVocab": "pegged",
                                "prompt": "Dùng từ 'pegged' để viết một câu về quốc gia sử dụng chế độ tỷ giá neo cố định và lý do. Ví dụ: The United Arab Emirates has pegged its dirham to the US dollar to provide a stable environment for its oil-based trade."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về giao dịch ngoại hối và rủi ro.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "exchange — hối đoái, currency — tiền tệ, appreciation — sự tăng giá, "
                            "depreciation — sự mất giá, floating — thả nổi, và pegged — neo cố định. "
                            "Bạn đã hiểu cách tỷ giá hối đoái được xác định và hai chế độ tiền tệ chính. "
                            "Bây giờ, chúng ta sẽ đi vào thế giới giao dịch ngoại hối thực tế.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: forex, spot, forward, hedge, speculation, và volatility. "
                            "Những từ này đưa bạn từ lý thuyết vào thực hành — "
                            "cách các ngân hàng, doanh nghiệp và nhà đầu tư thực sự mua bán tiền tệ mỗi ngày.\n\n"
                            "Từ đầu tiên là forex — danh từ — viết tắt của foreign exchange, "
                            "nghĩa là thị trường ngoại hối, nơi các đồng tiền được mua bán. "
                            "Ví dụ: 'The forex market operates twenty-four hours a day, five days a week, "
                            "making it the most liquid financial market in the world.' "
                            "Trong bài đọc, forex mô tả thị trường khổng lồ nơi hàng nghìn tỷ đô la "
                            "được giao dịch mỗi ngày.\n\n"
                            "Từ thứ hai là spot — tính từ và danh từ — trong tài chính nghĩa là giao ngay, "
                            "giao dịch mua bán tiền tệ với giá hiện tại và thanh toán ngay lập tức. "
                            "Ví dụ: 'The company bought euros on the spot market to pay its German supplier today.' "
                            "Trong bài đọc, spot mô tả loại giao dịch phổ biến nhất — "
                            "bạn mua tiền tệ ngay bây giờ với giá hiện tại.\n\n"
                            "Từ thứ ba là forward — tính từ và danh từ — nghĩa là kỳ hạn, "
                            "giao dịch mua bán tiền tệ với giá thỏa thuận hôm nay nhưng thanh toán trong tương lai. "
                            "Ví dụ: 'The exporter signed a forward contract to sell dollars at a fixed rate "
                            "three months from now, protecting against currency risk.' "
                            "Trong bài đọc, forward là công cụ giúp doanh nghiệp biết trước chi phí "
                            "dù tỷ giá có thay đổi.\n\n"
                            "Từ thứ tư là hedge — động từ và danh từ — nghĩa là phòng ngừa rủi ro, "
                            "hành động bảo vệ mình khỏi tổn thất do biến động tỷ giá. "
                            "Ví dụ: 'Airlines often hedge against fuel price increases by locking in prices "
                            "through forward contracts.' "
                            "Trong bài đọc, hedge mô tả chiến lược mà doanh nghiệp dùng "
                            "để giảm thiểu rủi ro từ biến động tiền tệ.\n\n"
                            "Từ thứ năm là speculation — danh từ — nghĩa là đầu cơ, "
                            "hành động mua bán tiền tệ với mục đích kiếm lời từ biến động giá. "
                            "Ví dụ: 'Currency speculation can generate huge profits, "
                            "but it can also destabilize small economies when large amounts of money move quickly.' "
                            "Trong bài đọc, speculation là mặt đối lập của hedge — "
                            "thay vì giảm rủi ro, nhà đầu cơ chủ động chấp nhận rủi ro để kiếm lời.\n\n"
                            "Từ cuối cùng là volatility — danh từ — nghĩa là sự biến động, "
                            "mức độ dao động mạnh và nhanh của tỷ giá hoặc giá tài sản. "
                            "Ví dụ: 'The volatility of the Brazilian real increased sharply during the political crisis, "
                            "making it difficult for businesses to plan ahead.' "
                            "Trong bài đọc, volatility mô tả tình trạng bất ổn trên thị trường — "
                            "khi tỷ giá thay đổi nhanh và khó dự đoán.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về giao dịch ngoại hối và quản lý rủi ro nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Giao dịch ngoại hối và rủi ro",
                    "description": "Học 6 từ: forex, spot, forward, hedge, speculation, volatility",
                    "data": {"vocabList": ["forex", "spot", "forward", "hedge", "speculation", "volatility"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Giao dịch ngoại hối và rủi ro",
                    "description": "Học 6 từ: forex, spot, forward, hedge, speculation, volatility",
                    "data": {"vocabList": ["forex", "spot", "forward", "hedge", "speculation", "volatility"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Giao dịch ngoại hối và rủi ro",
                    "description": "Học 6 từ: forex, spot, forward, hedge, speculation, volatility",
                    "data": {"vocabList": ["forex", "spot", "forward", "hedge", "speculation", "volatility"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Giao dịch ngoại hối và rủi ro",
                    "description": "Học 6 từ: forex, spot, forward, hedge, speculation, volatility",
                    "data": {"vocabList": ["forex", "spot", "forward", "hedge", "speculation", "volatility"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Giao dịch ngoại hối và rủi ro",
                    "description": "Học 6 từ: forex, spot, forward, hedge, speculation, volatility",
                    "data": {"vocabList": ["forex", "spot", "forward", "hedge", "speculation", "volatility"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Giao dịch ngoại hối và quản lý rủi ro",
                    "description": "The foreign exchange market — known as forex — is the largest financial market on Earth.",
                    "data": {
                        "text": (
                            "The foreign exchange market — known as forex — is the largest financial market on Earth. "
                            "Every day, banks, corporations, governments, and individual traders buy and sell currencies "
                            "worth more than seven trillion US dollars. Unlike stock markets, "
                            "the forex market has no central building or exchange. "
                            "It operates electronically, around the clock, across time zones.\n\n"
                            "The most common type of forex transaction is a spot trade. "
                            "In a spot trade, two parties agree to exchange currencies at the current market price, "
                            "with settlement typically occurring within two business days. "
                            "When a Vietnamese tourist arrives in Bangkok and exchanges dong for Thai baht at the airport, "
                            "that is essentially a spot transaction — the exchange happens immediately at today's rate.\n\n"
                            "But businesses that trade internationally often need more certainty about future costs. "
                            "A Vietnamese seafood exporter that will receive payment in US dollars three months from now "
                            "faces a risk: what if the dollar depreciates against the dong before the payment arrives? "
                            "To manage this risk, the exporter can use a forward contract. "
                            "A forward contract locks in an exchange rate for a future date. "
                            "The exporter agrees today to sell dollars at a specific rate in three months, "
                            "regardless of what the spot rate will be at that time.\n\n"
                            "This practice of protecting against currency risk is called hedging. "
                            "To hedge means to take a position that offsets potential losses from exchange rate movements. "
                            "Companies that import raw materials, pay foreign suppliers, or earn revenue in other currencies "
                            "all use hedging strategies to reduce uncertainty. "
                            "A well-designed hedge does not eliminate all risk, but it makes the future more predictable.\n\n"
                            "Not everyone in the forex market is trying to reduce risk. "
                            "Some participants engage in speculation — buying or selling currencies "
                            "with the goal of profiting from price changes. "
                            "A speculator might buy Japanese yen because she believes the yen will appreciate next month. "
                            "If she is right, she sells the yen at a higher price and keeps the profit. "
                            "If she is wrong, she takes a loss. "
                            "Speculation adds liquidity to the market, but it can also increase volatility.\n\n"
                            "Volatility refers to how much and how quickly exchange rates change. "
                            "High volatility means rates swing widely in short periods, "
                            "making it harder for businesses to plan and for investors to predict returns. "
                            "Political events, economic data releases, and central bank announcements "
                            "can all trigger sudden spikes in volatility. "
                            "During the Asian financial crisis of 1997, the volatility of several Southeast Asian currencies "
                            "reached extreme levels as investors rushed to sell.\n\n"
                            "Understanding the difference between hedging and speculation is essential "
                            "for anyone working in international business. "
                            "Hedgers use the forex market as insurance; speculators use it as an opportunity. "
                            "Both play important roles in keeping the market liquid and efficient."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Giao dịch ngoại hối và quản lý rủi ro",
                    "description": "The foreign exchange market — known as forex — is the largest financial market on Earth.",
                    "data": {
                        "text": (
                            "The foreign exchange market — known as forex — is the largest financial market on Earth. "
                            "Every day, banks, corporations, governments, and individual traders buy and sell currencies "
                            "worth more than seven trillion US dollars. Unlike stock markets, "
                            "the forex market has no central building or exchange. "
                            "It operates electronically, around the clock, across time zones.\n\n"
                            "The most common type of forex transaction is a spot trade. "
                            "In a spot trade, two parties agree to exchange currencies at the current market price, "
                            "with settlement typically occurring within two business days. "
                            "When a Vietnamese tourist arrives in Bangkok and exchanges dong for Thai baht at the airport, "
                            "that is essentially a spot transaction — the exchange happens immediately at today's rate.\n\n"
                            "But businesses that trade internationally often need more certainty about future costs. "
                            "A Vietnamese seafood exporter that will receive payment in US dollars three months from now "
                            "faces a risk: what if the dollar depreciates against the dong before the payment arrives? "
                            "To manage this risk, the exporter can use a forward contract. "
                            "A forward contract locks in an exchange rate for a future date. "
                            "The exporter agrees today to sell dollars at a specific rate in three months, "
                            "regardless of what the spot rate will be at that time.\n\n"
                            "This practice of protecting against currency risk is called hedging. "
                            "To hedge means to take a position that offsets potential losses from exchange rate movements. "
                            "Companies that import raw materials, pay foreign suppliers, or earn revenue in other currencies "
                            "all use hedging strategies to reduce uncertainty. "
                            "A well-designed hedge does not eliminate all risk, but it makes the future more predictable.\n\n"
                            "Not everyone in the forex market is trying to reduce risk. "
                            "Some participants engage in speculation — buying or selling currencies "
                            "with the goal of profiting from price changes. "
                            "A speculator might buy Japanese yen because she believes the yen will appreciate next month. "
                            "If she is right, she sells the yen at a higher price and keeps the profit. "
                            "If she is wrong, she takes a loss. "
                            "Speculation adds liquidity to the market, but it can also increase volatility.\n\n"
                            "Volatility refers to how much and how quickly exchange rates change. "
                            "High volatility means rates swing widely in short periods, "
                            "making it harder for businesses to plan and for investors to predict returns. "
                            "Political events, economic data releases, and central bank announcements "
                            "can all trigger sudden spikes in volatility. "
                            "During the Asian financial crisis of 1997, the volatility of several Southeast Asian currencies "
                            "reached extreme levels as investors rushed to sell.\n\n"
                            "Understanding the difference between hedging and speculation is essential "
                            "for anyone working in international business. "
                            "Hedgers use the forex market as insurance; speculators use it as an opportunity. "
                            "Both play important roles in keeping the market liquid and efficient."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Giao dịch ngoại hối và quản lý rủi ro",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "The foreign exchange market — known as forex — is the largest financial market on Earth. "
                            "Every day, banks, corporations, governments, and individual traders buy and sell currencies "
                            "worth more than seven trillion US dollars. Unlike stock markets, "
                            "the forex market has no central building or exchange. "
                            "It operates electronically, around the clock, across time zones.\n\n"
                            "The most common type of forex transaction is a spot trade. "
                            "In a spot trade, two parties agree to exchange currencies at the current market price, "
                            "with settlement typically occurring within two business days. "
                            "When a Vietnamese tourist arrives in Bangkok and exchanges dong for Thai baht at the airport, "
                            "that is essentially a spot transaction — the exchange happens immediately at today's rate.\n\n"
                            "But businesses that trade internationally often need more certainty about future costs. "
                            "A Vietnamese seafood exporter that will receive payment in US dollars three months from now "
                            "faces a risk: what if the dollar depreciates against the dong before the payment arrives? "
                            "To manage this risk, the exporter can use a forward contract. "
                            "A forward contract locks in an exchange rate for a future date. "
                            "The exporter agrees today to sell dollars at a specific rate in three months, "
                            "regardless of what the spot rate will be at that time.\n\n"
                            "This practice of protecting against currency risk is called hedging. "
                            "To hedge means to take a position that offsets potential losses from exchange rate movements. "
                            "Companies that import raw materials, pay foreign suppliers, or earn revenue in other currencies "
                            "all use hedging strategies to reduce uncertainty. "
                            "A well-designed hedge does not eliminate all risk, but it makes the future more predictable.\n\n"
                            "Not everyone in the forex market is trying to reduce risk. "
                            "Some participants engage in speculation — buying or selling currencies "
                            "with the goal of profiting from price changes. "
                            "A speculator might buy Japanese yen because she believes the yen will appreciate next month. "
                            "If she is right, she sells the yen at a higher price and keeps the profit. "
                            "If she is wrong, she takes a loss. "
                            "Speculation adds liquidity to the market, but it can also increase volatility.\n\n"
                            "Volatility refers to how much and how quickly exchange rates change. "
                            "High volatility means rates swing widely in short periods, "
                            "making it harder for businesses to plan and for investors to predict returns. "
                            "Political events, economic data releases, and central bank announcements "
                            "can all trigger sudden spikes in volatility. "
                            "During the Asian financial crisis of 1997, the volatility of several Southeast Asian currencies "
                            "reached extreme levels as investors rushed to sell.\n\n"
                            "Understanding the difference between hedging and speculation is essential "
                            "for anyone working in international business. "
                            "Hedgers use the forex market as insurance; speculators use it as an opportunity. "
                            "Both play important roles in keeping the market liquid and efficient."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Giao dịch ngoại hối và rủi ro",
                    "description": "Viết câu sử dụng 6 từ vựng về giao dịch forex.",
                    "data": {
                        "vocabList": ["forex", "spot", "forward", "hedge", "speculation", "volatility"],
                        "items": [
                            {
                                "targetVocab": "forex",
                                "prompt": "Dùng từ 'forex' để viết một câu về quy mô và đặc điểm của thị trường ngoại hối. Ví dụ: The forex market trades over seven trillion dollars daily, dwarfing the combined volume of all the world's stock exchanges."
                            },
                            {
                                "targetVocab": "spot",
                                "prompt": "Dùng từ 'spot' để viết một câu về giao dịch mua bán tiền tệ ngay lập tức với giá hiện tại. Ví dụ: The importer purchased Japanese yen on the spot market to pay for a shipment of electronics arriving this week."
                            },
                            {
                                "targetVocab": "forward",
                                "prompt": "Dùng từ 'forward' để viết một câu về hợp đồng kỳ hạn giúp doanh nghiệp cố định tỷ giá trong tương lai. Ví dụ: The coffee exporter signed a forward contract to sell dollars at a guaranteed rate in six months, removing the uncertainty of future exchange rate movements."
                            },
                            {
                                "targetVocab": "hedge",
                                "prompt": "Dùng từ 'hedge' để viết một câu về chiến lược phòng ngừa rủi ro tỷ giá của doanh nghiệp. Ví dụ: The airline decided to hedge its fuel costs by entering into forward contracts for crude oil priced in US dollars."
                            },
                            {
                                "targetVocab": "speculation",
                                "prompt": "Dùng từ 'speculation' để viết một câu về hoạt động đầu cơ tiền tệ và rủi ro đi kèm. Ví dụ: Reckless speculation on the Thai baht by international hedge funds contributed to the Asian financial crisis in 1997."
                            },
                            {
                                "targetVocab": "volatility",
                                "prompt": "Dùng từ 'volatility' để viết một câu về sự biến động tỷ giá và tác động đến doanh nghiệp. Ví dụ: The high volatility of the Russian ruble forced many foreign companies to delay their investment plans in Moscow."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về chính sách tiền tệ quốc tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: "
                            "exchange — hối đoái, currency — tiền tệ, appreciation — sự tăng giá, "
                            "depreciation — sự mất giá, floating — thả nổi, và pegged — neo cố định. "
                            "Đây là bộ khung cơ bản để hiểu tỷ giá hối đoái.\n\n"
                            "Trong phần 2, bạn đã đi vào thế giới giao dịch thực tế với: "
                            "forex — thị trường ngoại hối, spot — giao ngay, forward — kỳ hạn, "
                            "hedge — phòng ngừa rủi ro, speculation — đầu cơ, và volatility — sự biến động. "
                            "Những từ này giúp bạn hiểu cách tiền tệ được mua bán và rủi ro được quản lý.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào khía cạnh chính sách: "
                            "khi ngân hàng trung ương và chính phủ can thiệp vào thị trường ngoại hối. "
                            "Bạn sẽ học 6 từ mới: arbitrage, devaluation, revaluation, convertible, reserve, và intervention.\n\n"
                            "Từ đầu tiên là arbitrage — danh từ — nghĩa là kinh doanh chênh lệch giá, "
                            "hành động mua tiền tệ ở thị trường giá thấp và bán ở thị trường giá cao "
                            "để kiếm lời từ sự chênh lệch. "
                            "Ví dụ: 'Currency arbitrage becomes possible when the exchange rate for the euro "
                            "differs between the London and Tokyo markets by even a fraction of a cent.' "
                            "Trong bài đọc, arbitrage mô tả cách các nhà giao dịch tận dụng "
                            "sự khác biệt giá giữa các thị trường.\n\n"
                            "Từ thứ hai là devaluation — danh từ — nghĩa là phá giá, "
                            "hành động chính thức của chính phủ giảm giá trị đồng tiền so với đồng tiền khác. "
                            "Ví dụ: 'China's devaluation of the yuan in 2015 sent shockwaves through global markets "
                            "as investors feared a currency war.' "
                            "Trong bài đọc, devaluation khác với depreciation — "
                            "depreciation xảy ra tự nhiên trên thị trường, còn devaluation là quyết định có chủ đích.\n\n"
                            "Từ thứ ba là revaluation — danh từ — nghĩa là nâng giá, "
                            "hành động chính thức tăng giá trị đồng tiền. "
                            "Ví dụ: 'Germany's revaluation of the Deutsche Mark in the 1960s "
                            "reflected the country's growing economic strength after the war.' "
                            "Trong bài đọc, revaluation là mặt đối lập của devaluation — "
                            "chính phủ chủ động nâng giá đồng tiền.\n\n"
                            "Từ thứ tư là convertible — tính từ — nghĩa là có thể chuyển đổi tự do, "
                            "mô tả đồng tiền có thể được đổi sang đồng tiền khác mà không bị hạn chế. "
                            "Ví dụ: 'The US dollar is a fully convertible currency — "
                            "anyone can exchange it for another currency without government permission.' "
                            "Trong bài đọc, convertible mô tả mức độ tự do của một đồng tiền "
                            "trên thị trường quốc tế.\n\n"
                            "Từ thứ năm là reserve — danh từ — nghĩa là dự trữ ngoại hối, "
                            "lượng ngoại tệ và vàng mà ngân hàng trung ương nắm giữ. "
                            "Ví dụ: 'China holds the world's largest foreign exchange reserves, "
                            "worth over three trillion US dollars.' "
                            "Trong bài đọc, reserve là công cụ quan trọng nhất "
                            "để ngân hàng trung ương bảo vệ giá trị đồng tiền.\n\n"
                            "Từ cuối cùng là intervention — danh từ — nghĩa là sự can thiệp, "
                            "hành động của ngân hàng trung ương mua hoặc bán ngoại tệ "
                            "để ảnh hưởng đến tỷ giá hối đoái. "
                            "Ví dụ: 'The Bank of Japan's intervention in the forex market "
                            "temporarily stopped the yen from falling further against the dollar.' "
                            "Trong bài đọc, intervention mô tả cách ngân hàng trung ương "
                            "sử dụng dự trữ ngoại hối để ổn định tỷ giá.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về chính sách tiền tệ quốc tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chính sách tiền tệ quốc tế",
                    "description": "Học 6 từ: arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chính sách tiền tệ quốc tế",
                    "description": "Học 6 từ: arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chính sách tiền tệ quốc tế",
                    "description": "Học 6 từ: arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chính sách tiền tệ quốc tế",
                    "description": "Học 6 từ: arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chính sách tiền tệ quốc tế",
                    "description": "Học 6 từ: arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Ngân hàng trung ương và chính sách tỷ giá",
                    "description": "Not all exchange rate movements are driven by market forces alone.",
                    "data": {
                        "text": (
                            "Not all exchange rate movements are driven by market forces alone. "
                            "Governments and central banks play an active role in shaping the value of their currencies. "
                            "The tools they use — and the reasons behind their decisions — "
                            "are central to understanding international finance.\n\n"
                            "One of the most powerful tools is intervention. "
                            "When a central bank intervenes in the forex market, "
                            "it buys or sells large amounts of foreign currency to influence the exchange rate. "
                            "For example, if the Vietnamese dong is depreciating too quickly, "
                            "the State Bank of Vietnam might sell US dollars from its reserves and buy dong. "
                            "This increases demand for the dong and slows its decline.\n\n"
                            "To carry out intervention, a central bank needs foreign exchange reserves — "
                            "stockpiles of foreign currencies, gold, and other assets held for emergencies. "
                            "Countries with large reserves, like China and Japan, "
                            "have more firepower to defend their currencies. "
                            "Countries with small reserves may find it difficult to sustain intervention "
                            "if market pressure is strong.\n\n"
                            "Sometimes a government makes a deliberate decision to lower the official value "
                            "of its currency. This is called devaluation. "
                            "Unlike depreciation, which happens naturally through market forces, "
                            "devaluation is a policy choice — typically made by countries with pegged exchange rates. "
                            "A government might devalue its currency to make exports cheaper "
                            "and boost the competitiveness of domestic industries. "
                            "However, devaluation also makes imports more expensive "
                            "and can trigger inflation.\n\n"
                            "The opposite action is revaluation — officially increasing the value of a currency. "
                            "Revaluation is less common because it makes a country's exports more expensive. "
                            "But it can help control inflation by making imports cheaper. "
                            "In the 1970s, several European countries revalued their currencies "
                            "as their economies grew stronger relative to the US dollar.\n\n"
                            "Whether a country can freely adjust its currency also depends on convertibility. "
                            "A fully convertible currency can be exchanged for any other currency "
                            "without restrictions. The US dollar, the euro, and the Japanese yen are all convertible. "
                            "Some countries, however, impose capital controls that limit convertibility. "
                            "The Chinese yuan, for instance, is only partially convertible — "
                            "the government restricts how much money can flow in and out of the country.\n\n"
                            "Finally, the forex market creates opportunities for arbitrage. "
                            "Arbitrage occurs when a trader exploits price differences between markets. "
                            "If the euro is slightly cheaper in London than in New York, "
                            "a trader can buy euros in London and sell them in New York for a small profit. "
                            "In practice, arbitrage opportunities disappear very quickly "
                            "because thousands of traders are watching for them. "
                            "This constant search for arbitrage helps keep exchange rates consistent across markets.\n\n"
                            "Together, these concepts — intervention, reserves, devaluation, revaluation, "
                            "convertibility, and arbitrage — form the policy toolkit "
                            "that shapes how currencies behave in the global economy."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Ngân hàng trung ương và chính sách tỷ giá",
                    "description": "Not all exchange rate movements are driven by market forces alone.",
                    "data": {
                        "text": (
                            "Not all exchange rate movements are driven by market forces alone. "
                            "Governments and central banks play an active role in shaping the value of their currencies. "
                            "The tools they use — and the reasons behind their decisions — "
                            "are central to understanding international finance.\n\n"
                            "One of the most powerful tools is intervention. "
                            "When a central bank intervenes in the forex market, "
                            "it buys or sells large amounts of foreign currency to influence the exchange rate. "
                            "For example, if the Vietnamese dong is depreciating too quickly, "
                            "the State Bank of Vietnam might sell US dollars from its reserves and buy dong. "
                            "This increases demand for the dong and slows its decline.\n\n"
                            "To carry out intervention, a central bank needs foreign exchange reserves — "
                            "stockpiles of foreign currencies, gold, and other assets held for emergencies. "
                            "Countries with large reserves, like China and Japan, "
                            "have more firepower to defend their currencies. "
                            "Countries with small reserves may find it difficult to sustain intervention "
                            "if market pressure is strong.\n\n"
                            "Sometimes a government makes a deliberate decision to lower the official value "
                            "of its currency. This is called devaluation. "
                            "Unlike depreciation, which happens naturally through market forces, "
                            "devaluation is a policy choice — typically made by countries with pegged exchange rates. "
                            "A government might devalue its currency to make exports cheaper "
                            "and boost the competitiveness of domestic industries. "
                            "However, devaluation also makes imports more expensive "
                            "and can trigger inflation.\n\n"
                            "The opposite action is revaluation — officially increasing the value of a currency. "
                            "Revaluation is less common because it makes a country's exports more expensive. "
                            "But it can help control inflation by making imports cheaper. "
                            "In the 1970s, several European countries revalued their currencies "
                            "as their economies grew stronger relative to the US dollar.\n\n"
                            "Whether a country can freely adjust its currency also depends on convertibility. "
                            "A fully convertible currency can be exchanged for any other currency "
                            "without restrictions. The US dollar, the euro, and the Japanese yen are all convertible. "
                            "Some countries, however, impose capital controls that limit convertibility. "
                            "The Chinese yuan, for instance, is only partially convertible — "
                            "the government restricts how much money can flow in and out of the country.\n\n"
                            "Finally, the forex market creates opportunities for arbitrage. "
                            "Arbitrage occurs when a trader exploits price differences between markets. "
                            "If the euro is slightly cheaper in London than in New York, "
                            "a trader can buy euros in London and sell them in New York for a small profit. "
                            "In practice, arbitrage opportunities disappear very quickly "
                            "because thousands of traders are watching for them. "
                            "This constant search for arbitrage helps keep exchange rates consistent across markets.\n\n"
                            "Together, these concepts — intervention, reserves, devaluation, revaluation, "
                            "convertibility, and arbitrage — form the policy toolkit "
                            "that shapes how currencies behave in the global economy."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ngân hàng trung ương và chính sách tỷ giá",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Not all exchange rate movements are driven by market forces alone. "
                            "Governments and central banks play an active role in shaping the value of their currencies. "
                            "The tools they use — and the reasons behind their decisions — "
                            "are central to understanding international finance.\n\n"
                            "One of the most powerful tools is intervention. "
                            "When a central bank intervenes in the forex market, "
                            "it buys or sells large amounts of foreign currency to influence the exchange rate. "
                            "For example, if the Vietnamese dong is depreciating too quickly, "
                            "the State Bank of Vietnam might sell US dollars from its reserves and buy dong. "
                            "This increases demand for the dong and slows its decline.\n\n"
                            "To carry out intervention, a central bank needs foreign exchange reserves — "
                            "stockpiles of foreign currencies, gold, and other assets held for emergencies. "
                            "Countries with large reserves, like China and Japan, "
                            "have more firepower to defend their currencies. "
                            "Countries with small reserves may find it difficult to sustain intervention "
                            "if market pressure is strong.\n\n"
                            "Sometimes a government makes a deliberate decision to lower the official value "
                            "of its currency. This is called devaluation. "
                            "Unlike depreciation, which happens naturally through market forces, "
                            "devaluation is a policy choice — typically made by countries with pegged exchange rates. "
                            "A government might devalue its currency to make exports cheaper "
                            "and boost the competitiveness of domestic industries. "
                            "However, devaluation also makes imports more expensive "
                            "and can trigger inflation.\n\n"
                            "The opposite action is revaluation — officially increasing the value of a currency. "
                            "Revaluation is less common because it makes a country's exports more expensive. "
                            "But it can help control inflation by making imports cheaper. "
                            "In the 1970s, several European countries revalued their currencies "
                            "as their economies grew stronger relative to the US dollar.\n\n"
                            "Whether a country can freely adjust its currency also depends on convertibility. "
                            "A fully convertible currency can be exchanged for any other currency "
                            "without restrictions. The US dollar, the euro, and the Japanese yen are all convertible. "
                            "Some countries, however, impose capital controls that limit convertibility. "
                            "The Chinese yuan, for instance, is only partially convertible — "
                            "the government restricts how much money can flow in and out of the country.\n\n"
                            "Finally, the forex market creates opportunities for arbitrage. "
                            "Arbitrage occurs when a trader exploits price differences between markets. "
                            "If the euro is slightly cheaper in London than in New York, "
                            "a trader can buy euros in London and sell them in New York for a small profit. "
                            "In practice, arbitrage opportunities disappear very quickly "
                            "because thousands of traders are watching for them. "
                            "This constant search for arbitrage helps keep exchange rates consistent across markets.\n\n"
                            "Together, these concepts — intervention, reserves, devaluation, revaluation, "
                            "convertibility, and arbitrage — form the policy toolkit "
                            "that shapes how currencies behave in the global economy."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chính sách tiền tệ quốc tế",
                    "description": "Viết câu sử dụng 6 từ vựng về chính sách tỷ giá.",
                    "data": {
                        "vocabList": ["arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"],
                        "items": [
                            {
                                "targetVocab": "arbitrage",
                                "prompt": "Dùng từ 'arbitrage' để viết một câu về cách nhà giao dịch kiếm lời từ chênh lệch giá giữa các thị trường. Ví dụ: High-frequency traders use computer algorithms to detect arbitrage opportunities between currency markets in milliseconds."
                            },
                            {
                                "targetVocab": "devaluation",
                                "prompt": "Dùng từ 'devaluation' để viết một câu về quyết định phá giá đồng tiền của chính phủ và tác động kinh tế. Ví dụ: Egypt's devaluation of the pound in 2016 was a condition set by the International Monetary Fund in exchange for a twelve-billion-dollar loan."
                            },
                            {
                                "targetVocab": "revaluation",
                                "prompt": "Dùng từ 'revaluation' để viết một câu về việc nâng giá đồng tiền và ảnh hưởng đến thương mại. Ví dụ: The revaluation of the Swiss franc in 2015 caught many traders off guard and caused billions of dollars in losses overnight."
                            },
                            {
                                "targetVocab": "convertible",
                                "prompt": "Dùng từ 'convertible' để viết một câu về mức độ tự do chuyển đổi của một đồng tiền trên thị trường quốc tế. Ví dụ: India has been gradually making the rupee more convertible to attract foreign investment and integrate deeper into global financial markets."
                            },
                            {
                                "targetVocab": "reserve",
                                "prompt": "Dùng từ 'reserve' để viết một câu về vai trò của dự trữ ngoại hối trong việc bảo vệ đồng tiền quốc gia. Ví dụ: Vietnam's foreign exchange reserves have grown steadily over the past decade, giving the central bank more power to stabilize the dong."
                            },
                            {
                                "targetVocab": "intervention",
                                "prompt": "Dùng từ 'intervention' để viết một câu về hành động can thiệp của ngân hàng trung ương vào thị trường ngoại hối. Ví dụ: The Bank of Japan spent over sixty billion dollars in a single month on currency intervention to prevent the yen from weakening further."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Thị trường Ngoại hối. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "exchange — hối đoái, currency — tiền tệ, appreciation — sự tăng giá, "
                            "depreciation — sự mất giá, floating — thả nổi, và pegged — neo cố định. "
                            "Đây là bộ khung cơ bản để hiểu tỷ giá hối đoái hoạt động như thế nào.\n\n"
                            "Trong phần 2, bạn đã đi vào thế giới giao dịch thực tế với: "
                            "forex — thị trường ngoại hối, spot — giao ngay, forward — kỳ hạn, "
                            "hedge — phòng ngừa rủi ro, speculation — đầu cơ, và volatility — sự biến động. "
                            "Những từ này giúp bạn hiểu cách tiền tệ được mua bán hàng ngày.\n\n"
                            "Trong phần 3, bạn đã khám phá khía cạnh chính sách: "
                            "arbitrage — kinh doanh chênh lệch giá, devaluation — phá giá, "
                            "revaluation — nâng giá, convertible — có thể chuyển đổi, "
                            "reserve — dự trữ ngoại hối, và intervention — sự can thiệp. "
                            "Đây là những từ về vai trò của ngân hàng trung ương trên thị trường tiền tệ.\n\n"
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
                    "description": "Học 18 từ: exchange, currency, appreciation, depreciation, floating, pegged, forex, spot, forward, hedge, speculation, volatility, arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: exchange, currency, appreciation, depreciation, floating, pegged, forex, spot, forward, hedge, speculation, volatility, arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: exchange, currency, appreciation, depreciation, floating, pegged, forex, spot, forward, hedge, speculation, volatility, arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: exchange, currency, appreciation, depreciation, floating, pegged, forex, spot, forward, hedge, speculation, volatility, arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: exchange, currency, appreciation, depreciation, floating, pegged, forex, spot, forward, hedge, speculation, volatility, arbitrage, devaluation, revaluation, convertible, reserve, intervention",
                    "data": {"vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng ngoại hối",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"],
                        "items": [
                            {
                                "targetVocab": "exchange",
                                "prompt": "Dùng từ 'exchange' để viết một câu về tác động của tỷ giá hối đoái đến du lịch quốc tế. Ví dụ: A favorable exchange rate makes Thailand an even more attractive destination for Vietnamese tourists who want to stretch their travel budget."
                            },
                            {
                                "targetVocab": "currency",
                                "prompt": "Dùng từ 'currency' để viết một câu về đồng tiền chung của một khu vực kinh tế. Ví dụ: The euro became the shared currency of the eurozone in 1999, replacing national currencies like the French franc and the German mark."
                            },
                            {
                                "targetVocab": "appreciation",
                                "prompt": "Dùng từ 'appreciation' để viết một câu về tác động tích cực của đồng tiền tăng giá đối với người tiêu dùng. Ví dụ: The appreciation of the dong against the dollar last quarter made imported laptops and smartphones slightly cheaper for Vietnamese students."
                            },
                            {
                                "targetVocab": "depreciation",
                                "prompt": "Dùng từ 'depreciation' để viết một câu về tác động của đồng tiền mất giá đối với ngành xuất khẩu. Ví dụ: The depreciation of the Indonesian rupiah boosted the country's textile exports because foreign buyers could purchase more goods for the same amount of dollars."
                            },
                            {
                                "targetVocab": "floating",
                                "prompt": "Dùng từ 'floating' để viết một câu so sánh ưu và nhược điểm của chế độ tỷ giá thả nổi. Ví dụ: A floating exchange rate allows a country's currency to adjust naturally to economic shocks, but it also exposes businesses to unpredictable swings."
                            },
                            {
                                "targetVocab": "pegged",
                                "prompt": "Dùng từ 'pegged' để viết một câu về thách thức của việc duy trì tỷ giá neo cố định. Ví dụ: Argentina pegged its peso to the US dollar in the 1990s, but the policy collapsed in 2002 when the country ran out of reserves to defend the rate."
                            },
                            {
                                "targetVocab": "forex",
                                "prompt": "Dùng từ 'forex' để viết một câu về vai trò của thị trường ngoại hối trong nền kinh tế toàn cầu. Ví dụ: The forex market connects economies around the world by enabling the exchange of currencies needed for international trade and investment."
                            },
                            {
                                "targetVocab": "spot",
                                "prompt": "Dùng từ 'spot' để viết một câu về giao dịch giao ngay trong tình huống thực tế. Ví dụ: The tourist exchanged her euros for dong at the spot rate posted at the airport counter, receiving twenty-seven thousand dong per euro."
                            },
                            {
                                "targetVocab": "forward",
                                "prompt": "Dùng từ 'forward' để viết một câu về cách doanh nghiệp sử dụng hợp đồng kỳ hạn để lập kế hoạch tài chính. Ví dụ: The Vietnamese garment manufacturer used a forward contract to lock in the dollar-dong rate for its next quarter's export revenue."
                            },
                            {
                                "targetVocab": "hedge",
                                "prompt": "Dùng từ 'hedge' để viết một câu về chiến lược phòng ngừa rủi ro của một công ty đa quốc gia. Ví dụ: Samsung hedges its currency exposure in dozens of countries to ensure that exchange rate swings do not wipe out its overseas profits."
                            },
                            {
                                "targetVocab": "speculation",
                                "prompt": "Dùng từ 'speculation' để viết một câu về tác động tiêu cực của đầu cơ tiền tệ đối với nền kinh tế nhỏ. Ví dụ: Massive speculation against the Malaysian ringgit in 1997 forced the government to impose capital controls to stop the currency from collapsing."
                            },
                            {
                                "targetVocab": "volatility",
                                "prompt": "Dùng từ 'volatility' để viết một câu về cách biến động tỷ giá ảnh hưởng đến quyết định đầu tư. Ví dụ: High currency volatility in emerging markets discourages long-term foreign investment because companies cannot predict their future costs and revenues."
                            },
                            {
                                "targetVocab": "arbitrage",
                                "prompt": "Dùng từ 'arbitrage' để viết một câu về vai trò của kinh doanh chênh lệch giá trong việc duy trì hiệu quả thị trường. Ví dụ: Currency arbitrage ensures that exchange rates remain consistent across global markets because any price gap is quickly exploited and closed."
                            },
                            {
                                "targetVocab": "devaluation",
                                "prompt": "Dùng từ 'devaluation' để viết một câu về hậu quả xã hội của việc phá giá đồng tiền. Ví dụ: The sudden devaluation of the Nigerian naira made imported food and medicine unaffordable for millions of low-income families."
                            },
                            {
                                "targetVocab": "revaluation",
                                "prompt": "Dùng từ 'revaluation' để viết một câu về áp lực quốc tế đòi một quốc gia nâng giá đồng tiền. Ví dụ: The United States has repeatedly urged China to allow a revaluation of the yuan, arguing that an undervalued currency gives Chinese exporters an unfair advantage."
                            },
                            {
                                "targetVocab": "convertible",
                                "prompt": "Dùng từ 'convertible' để viết một câu về lợi ích của việc có đồng tiền chuyển đổi tự do. Ví dụ: Making the rupee fully convertible would allow Indian businesses to move money across borders more easily, but it also increases the risk of capital flight during crises."
                            },
                            {
                                "targetVocab": "reserve",
                                "prompt": "Dùng từ 'reserve' để viết một câu về tầm quan trọng của dự trữ ngoại hối đối với sự ổn định kinh tế. Ví dụ: Building up foreign exchange reserves gives a developing country a safety net to weather economic storms and maintain confidence among international investors."
                            },
                            {
                                "targetVocab": "intervention",
                                "prompt": "Dùng từ 'intervention' để viết một câu về tranh luận xung quanh việc ngân hàng trung ương can thiệp vào thị trường tiền tệ. Ví dụ: Critics argue that repeated intervention by the central bank only delays necessary market adjustments and depletes valuable foreign exchange reserves."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về thị trường ngoại hối.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về thị trường ngoại hối — từ cơ chế tỷ giá "
                            "đến giao dịch thực tế và chính sách can thiệp của ngân hàng trung ương.\n\n"
                            "Bạn sẽ gặp lại exchange, currency, appreciation, depreciation, floating, pegged "
                            "trong phần mở đầu về cách tỷ giá hoạt động. "
                            "Tiếp theo, forex, spot, forward, hedge, speculation, volatility "
                            "sẽ đưa bạn vào thế giới giao dịch tiền tệ. "
                            "Và cuối cùng, arbitrage, devaluation, revaluation, convertible, reserve, intervention "
                            "sẽ cho bạn thấy vai trò của chính phủ và ngân hàng trung ương.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thị trường ngoại hối — Bức tranh toàn cảnh",
                    "description": "Every time you check the price of a dollar in dong, you are looking at the foreign exchange market at work.",
                    "data": {
                        "text": (
                            "Every time you check the price of a dollar in dong, "
                            "you are looking at the foreign exchange market at work. "
                            "The exchange rate — the price of one currency in terms of another — "
                            "is one of the most important numbers in any open economy. "
                            "It determines how much a country pays for imports, "
                            "how much it earns from exports, and how attractive it is to foreign investors.\n\n"
                            "The world's currencies are traded on the forex market, "
                            "a decentralized network of banks, brokers, and electronic platforms "
                            "that operates twenty-four hours a day. "
                            "With daily trading volumes exceeding seven trillion dollars, "
                            "forex dwarfs every other financial market. "
                            "The most traded currency pair is the euro against the US dollar, "
                            "followed by the dollar against the Japanese yen.\n\n"
                            "Countries choose different systems to manage their currency values. "
                            "In a floating system, the exchange rate moves freely based on supply and demand. "
                            "When investors are optimistic about an economy, they buy its currency, "
                            "causing appreciation — the currency becomes stronger. "
                            "When confidence falls, investors sell, leading to depreciation — "
                            "the currency weakens. Most advanced economies let their currencies float.\n\n"
                            "Other countries prefer a pegged system, fixing their currency to a major one like the dollar. "
                            "A peg provides stability for trade and investment, "
                            "but it requires the central bank to hold large foreign exchange reserves "
                            "and to conduct intervention — buying or selling currencies — "
                            "whenever the market rate drifts from the target.\n\n"
                            "In the forex market, the simplest transaction is a spot trade: "
                            "two parties exchange currencies at today's rate with immediate settlement. "
                            "But many businesses need to plan ahead. "
                            "A Vietnamese furniture exporter expecting payment in dollars six months from now "
                            "can sign a forward contract, locking in today's rate for a future date. "
                            "This is a form of hedging — using financial instruments to hedge against "
                            "the risk that the exchange rate will move unfavorably.\n\n"
                            "Not all market participants seek to reduce risk. "
                            "Speculation drives a large share of forex trading. "
                            "Speculators bet on which direction a currency will move, "
                            "hoping to buy low and sell high. "
                            "Their activity adds liquidity but can also amplify volatility — "
                            "the rapid, unpredictable swings in exchange rates "
                            "that make planning difficult for businesses and governments alike.\n\n"
                            "When volatility threatens economic stability, central banks may step in. "
                            "Intervention can take many forms: selling reserves to prop up a weakening currency, "
                            "or buying foreign currency to prevent excessive appreciation. "
                            "The effectiveness of intervention depends on the size of a country's reserves "
                            "and the credibility of its central bank.\n\n"
                            "Governments with pegged rates sometimes make dramatic policy shifts. "
                            "A devaluation — an official reduction in the currency's value — "
                            "can make exports cheaper and boost growth, "
                            "but it also raises the cost of imports and can fuel inflation. "
                            "The reverse, a revaluation, strengthens the currency "
                            "and helps control inflation but hurts exporters.\n\n"
                            "The degree to which a currency can be freely traded matters too. "
                            "A fully convertible currency, like the dollar or the euro, "
                            "can be exchanged without restrictions anywhere in the world. "
                            "Currencies with limited convertibility, like the Chinese yuan, "
                            "face government controls on how much money can cross borders.\n\n"
                            "Finally, the forex market's efficiency is maintained in part by arbitrage. "
                            "When the same currency is priced differently in two markets, "
                            "traders buy where it is cheap and sell where it is expensive, "
                            "quickly eliminating the gap. "
                            "This constant process of arbitrage ensures that exchange rates "
                            "stay consistent across the globe.\n\n"
                            "From the tourist exchanging cash at an airport booth "
                            "to the central banker defending a currency peg with billions in reserves, "
                            "the foreign exchange market connects every economy on Earth. "
                            "Understanding its vocabulary is the first step "
                            "toward reading the financial world in English."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thị trường ngoại hối — Bức tranh toàn cảnh",
                    "description": "Every time you check the price of a dollar in dong, you are looking at the foreign exchange market at work.",
                    "data": {
                        "text": (
                            "Every time you check the price of a dollar in dong, "
                            "you are looking at the foreign exchange market at work. "
                            "The exchange rate — the price of one currency in terms of another — "
                            "is one of the most important numbers in any open economy. "
                            "It determines how much a country pays for imports, "
                            "how much it earns from exports, and how attractive it is to foreign investors.\n\n"
                            "The world's currencies are traded on the forex market, "
                            "a decentralized network of banks, brokers, and electronic platforms "
                            "that operates twenty-four hours a day. "
                            "With daily trading volumes exceeding seven trillion dollars, "
                            "forex dwarfs every other financial market. "
                            "The most traded currency pair is the euro against the US dollar, "
                            "followed by the dollar against the Japanese yen.\n\n"
                            "Countries choose different systems to manage their currency values. "
                            "In a floating system, the exchange rate moves freely based on supply and demand. "
                            "When investors are optimistic about an economy, they buy its currency, "
                            "causing appreciation — the currency becomes stronger. "
                            "When confidence falls, investors sell, leading to depreciation — "
                            "the currency weakens. Most advanced economies let their currencies float.\n\n"
                            "Other countries prefer a pegged system, fixing their currency to a major one like the dollar. "
                            "A peg provides stability for trade and investment, "
                            "but it requires the central bank to hold large foreign exchange reserves "
                            "and to conduct intervention — buying or selling currencies — "
                            "whenever the market rate drifts from the target.\n\n"
                            "In the forex market, the simplest transaction is a spot trade: "
                            "two parties exchange currencies at today's rate with immediate settlement. "
                            "But many businesses need to plan ahead. "
                            "A Vietnamese furniture exporter expecting payment in dollars six months from now "
                            "can sign a forward contract, locking in today's rate for a future date. "
                            "This is a form of hedging — using financial instruments to hedge against "
                            "the risk that the exchange rate will move unfavorably.\n\n"
                            "Not all market participants seek to reduce risk. "
                            "Speculation drives a large share of forex trading. "
                            "Speculators bet on which direction a currency will move, "
                            "hoping to buy low and sell high. "
                            "Their activity adds liquidity but can also amplify volatility — "
                            "the rapid, unpredictable swings in exchange rates "
                            "that make planning difficult for businesses and governments alike.\n\n"
                            "When volatility threatens economic stability, central banks may step in. "
                            "Intervention can take many forms: selling reserves to prop up a weakening currency, "
                            "or buying foreign currency to prevent excessive appreciation. "
                            "The effectiveness of intervention depends on the size of a country's reserves "
                            "and the credibility of its central bank.\n\n"
                            "Governments with pegged rates sometimes make dramatic policy shifts. "
                            "A devaluation — an official reduction in the currency's value — "
                            "can make exports cheaper and boost growth, "
                            "but it also raises the cost of imports and can fuel inflation. "
                            "The reverse, a revaluation, strengthens the currency "
                            "and helps control inflation but hurts exporters.\n\n"
                            "The degree to which a currency can be freely traded matters too. "
                            "A fully convertible currency, like the dollar or the euro, "
                            "can be exchanged without restrictions anywhere in the world. "
                            "Currencies with limited convertibility, like the Chinese yuan, "
                            "face government controls on how much money can cross borders.\n\n"
                            "Finally, the forex market's efficiency is maintained in part by arbitrage. "
                            "When the same currency is priced differently in two markets, "
                            "traders buy where it is cheap and sell where it is expensive, "
                            "quickly eliminating the gap. "
                            "This constant process of arbitrage ensures that exchange rates "
                            "stay consistent across the globe.\n\n"
                            "From the tourist exchanging cash at an airport booth "
                            "to the central banker defending a currency peg with billions in reserves, "
                            "the foreign exchange market connects every economy on Earth. "
                            "Understanding its vocabulary is the first step "
                            "toward reading the financial world in English."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thị trường ngoại hối — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every time you check the price of a dollar in dong, "
                            "you are looking at the foreign exchange market at work. "
                            "The exchange rate — the price of one currency in terms of another — "
                            "is one of the most important numbers in any open economy. "
                            "It determines how much a country pays for imports, "
                            "how much it earns from exports, and how attractive it is to foreign investors.\n\n"
                            "The world's currencies are traded on the forex market, "
                            "a decentralized network of banks, brokers, and electronic platforms "
                            "that operates twenty-four hours a day. "
                            "With daily trading volumes exceeding seven trillion dollars, "
                            "forex dwarfs every other financial market. "
                            "The most traded currency pair is the euro against the US dollar, "
                            "followed by the dollar against the Japanese yen.\n\n"
                            "Countries choose different systems to manage their currency values. "
                            "In a floating system, the exchange rate moves freely based on supply and demand. "
                            "When investors are optimistic about an economy, they buy its currency, "
                            "causing appreciation — the currency becomes stronger. "
                            "When confidence falls, investors sell, leading to depreciation — "
                            "the currency weakens. Most advanced economies let their currencies float.\n\n"
                            "Other countries prefer a pegged system, fixing their currency to a major one like the dollar. "
                            "A peg provides stability for trade and investment, "
                            "but it requires the central bank to hold large foreign exchange reserves "
                            "and to conduct intervention — buying or selling currencies — "
                            "whenever the market rate drifts from the target.\n\n"
                            "In the forex market, the simplest transaction is a spot trade: "
                            "two parties exchange currencies at today's rate with immediate settlement. "
                            "But many businesses need to plan ahead. "
                            "A Vietnamese furniture exporter expecting payment in dollars six months from now "
                            "can sign a forward contract, locking in today's rate for a future date. "
                            "This is a form of hedging — using financial instruments to hedge against "
                            "the risk that the exchange rate will move unfavorably.\n\n"
                            "Not all market participants seek to reduce risk. "
                            "Speculation drives a large share of forex trading. "
                            "Speculators bet on which direction a currency will move, "
                            "hoping to buy low and sell high. "
                            "Their activity adds liquidity but can also amplify volatility — "
                            "the rapid, unpredictable swings in exchange rates "
                            "that make planning difficult for businesses and governments alike.\n\n"
                            "When volatility threatens economic stability, central banks may step in. "
                            "Intervention can take many forms: selling reserves to prop up a weakening currency, "
                            "or buying foreign currency to prevent excessive appreciation. "
                            "The effectiveness of intervention depends on the size of a country's reserves "
                            "and the credibility of its central bank.\n\n"
                            "Governments with pegged rates sometimes make dramatic policy shifts. "
                            "A devaluation — an official reduction in the currency's value — "
                            "can make exports cheaper and boost growth, "
                            "but it also raises the cost of imports and can fuel inflation. "
                            "The reverse, a revaluation, strengthens the currency "
                            "and helps control inflation but hurts exporters.\n\n"
                            "The degree to which a currency can be freely traded matters too. "
                            "A fully convertible currency, like the dollar or the euro, "
                            "can be exchanged without restrictions anywhere in the world. "
                            "Currencies with limited convertibility, like the Chinese yuan, "
                            "face government controls on how much money can cross borders.\n\n"
                            "Finally, the forex market's efficiency is maintained in part by arbitrage. "
                            "When the same currency is priced differently in two markets, "
                            "traders buy where it is cheap and sell where it is expensive, "
                            "quickly eliminating the gap. "
                            "This constant process of arbitrage ensures that exchange rates "
                            "stay consistent across the globe.\n\n"
                            "From the tourist exchanging cash at an airport booth "
                            "to the central banker defending a currency peg with billions in reserves, "
                            "the foreign exchange market connects every economy on Earth. "
                            "Understanding its vocabulary is the first step "
                            "toward reading the financial world in English."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích thị trường ngoại hối",
                    "description": "Viết đoạn văn tiếng Anh phân tích về thị trường ngoại hối sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["exchange", "currency", "appreciation", "depreciation", "floating", "pegged", "forex", "spot", "forward", "hedge", "speculation", "volatility", "arbitrage", "devaluation", "revaluation", "convertible", "reserve", "intervention"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến thị trường ngoại hối. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích điều gì xảy ra khi ngân hàng trung ương của một quốc gia nhỏ quyết định từ bỏ chế độ pegged và chuyển sang floating. Giải thích tại sao quyết định này có thể gây ra volatility, và doanh nghiệp xuất nhập khẩu có thể dùng forward contract để hedge rủi ro như thế nào.",
                            "Hãy chọn một cuộc khủng hoảng tiền tệ (ví dụ: khủng hoảng châu Á 1997, khủng hoảng Argentina 2002) và phân tích vai trò của speculation, intervention, và reserve trong diễn biến sự kiện. Giải thích tại sao devaluation đôi khi là lựa chọn cuối cùng của chính phủ."
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
                            "mà để cảm nhận quãng đường bạn đã đi.\n\n"
                            "Có một điều kỳ diệu trong việc học ngôn ngữ chuyên ngành: "
                            "mỗi từ mới không chỉ là một nhãn dán — nó là một cánh cửa nhỏ "
                            "mở ra một cách nhìn hoàn toàn mới về thế giới. "
                            "Trước bài học này, có thể bạn chỉ thấy con số tỷ giá trên bảng điện tử "
                            "ở quầy đổi tiền sân bay. Bây giờ, bạn nhìn thấy cả một hệ sinh thái "
                            "đang vận hành phía sau con số đó.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất.\n\n"
                            "Forex — thị trường ngoại hối. Đây là thị trường tài chính lớn nhất hành tinh, "
                            "nơi hơn 7.000 tỷ đô la được giao dịch mỗi ngày. "
                            "Khi bạn nghe tin 'forex traders react to Fed announcement', "
                            "bạn biết đó là hàng triệu người đang đồng loạt phản ứng với một quyết định chính sách. "
                            "Ví dụ mới: The forex market reacted instantly when the European Central Bank "
                            "announced an unexpected interest rate cut, sending the euro down two percent in minutes.\n\n"
                            "Volatility — sự biến động. Từ này nắm bắt được bản chất bất định "
                            "của thị trường tài chính. Không ai biết chắc ngày mai tỷ giá sẽ ra sao — "
                            "và chính sự không chắc chắn đó tạo ra cả cơ hội lẫn rủi ro. "
                            "Ví dụ mới: The volatility of cryptocurrency markets makes traditional forex swings "
                            "look calm by comparison, yet both require careful risk management.\n\n"
                            "Reserve — dự trữ ngoại hối. Hãy nghĩ về reserve như chiếc phao cứu sinh "
                            "của một quốc gia. Khi sóng gió ập đến — khủng hoảng tài chính, "
                            "dòng vốn tháo chạy — dự trữ ngoại hối là thứ giữ cho con tàu không chìm. "
                            "Ví dụ mới: After the 1997 crisis, most Southeast Asian nations dramatically increased "
                            "their foreign exchange reserves as insurance against future currency attacks.\n\n"
                            "Hedge — phòng ngừa rủi ro. Trong một thế giới đầy biến động, "
                            "hedge là nghệ thuật của sự thận trọng. Không phải ai cũng muốn đánh bạc với tỷ giá — "
                            "những doanh nghiệp khôn ngoan chọn cách bảo vệ mình trước khi bão đến. "
                            "Ví dụ mới: A small Vietnamese coffee cooperative learned to hedge its dollar earnings "
                            "after losing twenty percent of its revenue to an unexpected dong appreciation.\n\n"
                            "Depreciation — sự mất giá. Khi đồng tiền của bạn yếu đi, "
                            "mọi thứ nhập khẩu đều đắt hơn — từ chiếc iPhone đến thùng dầu. "
                            "Nhưng đồng thời, hàng xuất khẩu của bạn lại rẻ hơn trong mắt thế giới. "
                            "Ví dụ mới: The gradual depreciation of the Indian rupee over the past decade "
                            "has been a double-edged sword — boosting IT exports while raising the cost of imported energy.\n\n"
                            "Intervention — sự can thiệp. Đây là khoảnh khắc ngân hàng trung ương "
                            "bước ra khỏi hậu trường và trở thành người chơi chính trên thị trường. "
                            "Mỗi lần can thiệp là một thông điệp: 'Chúng tôi sẽ không để đồng tiền rơi tự do.' "
                            "Ví dụ mới: Switzerland's surprise intervention in 2011, "
                            "when it set a floor for the euro-franc rate, "
                            "showed that even small countries can reshape forex markets with bold action.\n\n"
                            "Bạn biết không, thị trường ngoại hối là nơi mà kinh tế học gặp địa chính trị, "
                            "nơi mà quyết định của một ngân hàng trung ương ở Washington "
                            "có thể thay đổi giá gạo ở Hà Nội. "
                            "Mỗi từ bạn học hôm nay là một sợi dây nối bạn với mạng lưới tài chính toàn cầu đó.\n\n"
                            "Có lẽ điều đẹp nhất trong hành trình này không phải là 18 từ vựng bạn đã thuộc, "
                            "mà là cách bạn bắt đầu nhìn thế giới khác đi. "
                            "Lần tới khi bạn đọc tin về đồng yen Nhật hay đồng euro, "
                            "bạn sẽ không chỉ thấy con số — bạn sẽ thấy câu chuyện phía sau.\n\n"
                            "Cảm ơn bạn đã đi cùng bài học này. "
                            "Hẹn gặp lại ở bài tiếp theo nhé."
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Exchange Markets – Thị Trường Ngoại Hối' AND uid = '{UID}' ORDER BY created_at;")
