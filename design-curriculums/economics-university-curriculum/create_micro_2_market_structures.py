"""
Create curriculum: Market Structures – Cấu Trúc Thị Trường
Series A — Kinh Tế Vi Mô (Microeconomics), curriculum #2
18 words | 5 sessions | vivid_scenario tone | warm accountability farewell
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
W1 = ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"]
W2 = ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"]
W3 = ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Market Structures – Cấu Trúc Thị Trường",
    "contentTypeTags": [],
    "description": (
        "HÃY TƯỞNG TƯỢNG BẠN BƯỚC VÀO SIÊU THỊ — CHỈ CÓ MỘT HÃNG SỮA DUY NHẤT TRÊN KỆ, VÀ GIÁ DO HỌ QUYẾT ĐỊNH.\n\n"
        "Bạn mua xăng mỗi ngày nhưng chỉ có vài công ty bán — họ tăng giá cùng lúc, "
        "giảm giá cùng lúc, và bạn không có lựa chọn nào khác. "
        "Bạn mở quán cà phê nhưng đối thủ khổng lồ chiếm hết mặt bằng đẹp — "
        "rào cản gia nhập thị trường cao đến mức bạn chưa bắt đầu đã muốn bỏ cuộc.\n\n"
        "Thị trường không phải lúc nào cũng công bằng — nó giống như một sân chơi mà kẻ đến trước "
        "đã xây tường bao quanh, và bạn phải tìm cách leo qua hoặc đào hầm bên dưới. "
        "Hiểu cấu trúc thị trường chính là hiểu luật chơi — ai có quyền lực, ai bị kìm hãm, "
        "và vì sao một số ngành chỉ có một ông lớn trong khi ngành khác có hàng nghìn đối thủ.\n\n"
        "Sau khóa học này, bạn sẽ đọc được bài phân tích về monopoly, oligopoly, và antitrust bằng tiếng Anh "
        "mà không cần dừng lại tra từ — tự tin thảo luận về merger, regulation, và cartel "
        "trong lớp kinh tế vi mô như thể đó là ngôn ngữ mẹ đẻ.\n\n"
        "18 từ vựng — từ monopoly đến deregulation — được dạy qua bài đọc chuyên sâu, flashcard, "
        "luyện nói và viết. Bạn vừa nâng cấp tư duy phân tích thị trường, "
        "vừa nâng trình tiếng Anh chuyên ngành kinh tế một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về cấu trúc thị trường — "
            "từ độc quyền đến cạnh tranh hoàn hảo, từ sáp nhập đến luật chống độc quyền. "
            "Bạn sẽ bắt đầu với monopoly, oligopoly, competition, barrier, market, industry — "
            "những từ nền tảng giúp bạn phân biệt các loại thị trường khác nhau. "
            "Tiếp theo là differentiation, homogeneous, concentration, merger, antitrust, regulation — "
            "bộ từ vựng về cách doanh nghiệp cạnh tranh và chính phủ kiểm soát quyền lực thị trường. "
            "Cuối cùng, cartel, collusion, duopoly, contestable, dominance, deregulation "
            "đưa bạn vào thế giới của thỏa thuận ngầm và tự do hóa thị trường. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin phân tích cấu trúc thị trường bằng tiếng Anh chuyên ngành — "
            "sẵn sàng cho mọi bài giảng và bài thi kinh tế vi mô."
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
                    "description": "Chào mừng bạn đến với bài học về cấu trúc thị trường — các loại hình thị trường trong kinh tế vi mô.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ hai trong chuỗi từ vựng Kinh tế vi mô — "
                            "chủ đề hôm nay là Cấu trúc thị trường, hay trong tiếng Anh là Market Structures. "
                            "Nếu bài trước bạn đã học về cung và cầu — cách thị trường hoạt động ở mức cơ bản nhất — "
                            "thì bài này sẽ đưa bạn lên một tầng cao hơn: không phải mọi thị trường đều giống nhau. "
                            "Có thị trường chỉ một người bán, có thị trường hàng nghìn người bán, "
                            "và cách thị trường vận hành phụ thuộc rất nhiều vào cấu trúc của nó.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: monopoly, oligopoly, competition, barrier, market, và industry. "
                            "Đây là những từ bạn sẽ gặp ngay khi mở chương về cấu trúc thị trường trong bất kỳ giáo trình nào.\n\n"
                            "Từ đầu tiên là monopoly — danh từ — nghĩa là độc quyền, "
                            "tình trạng khi chỉ có một doanh nghiệp duy nhất cung cấp sản phẩm hoặc dịch vụ trên thị trường, "
                            "không có đối thủ cạnh tranh. "
                            "Ví dụ: 'The national railway company operates as a monopoly because no other firm is allowed to run trains on the same routes.' "
                            "Trong bài đọc, monopoly được dùng để mô tả thị trường mà một công ty kiểm soát toàn bộ nguồn cung "
                            "và có quyền định giá mà không lo bị cạnh tranh.\n\n"
                            "Từ thứ hai là oligopoly — danh từ — nghĩa là thị trường thiểu số, "
                            "tình trạng khi chỉ có một vài doanh nghiệp lớn chi phối thị trường. "
                            "Ví dụ: 'The smartphone industry is an oligopoly dominated by a handful of companies like Apple, Samsung, and Xiaomi.' "
                            "Trong bài đọc, oligopoly xuất hiện khi phân tích những ngành mà vài ông lớn "
                            "kiểm soát phần lớn thị phần và quyết định của một hãng ảnh hưởng trực tiếp đến các hãng còn lại.\n\n"
                            "Từ thứ ba là competition — danh từ — nghĩa là cạnh tranh, "
                            "quá trình các doanh nghiệp tranh giành khách hàng bằng giá cả, chất lượng, hoặc sáng tạo. "
                            "Ví dụ: 'Intense competition among coffee shops in the city center keeps prices low and quality high.' "
                            "Trong bài đọc, competition là lực lượng đối lập với monopoly — "
                            "càng nhiều cạnh tranh, người tiêu dùng càng được lợi.\n\n"
                            "Từ thứ tư là barrier — danh từ — nghĩa là rào cản, "
                            "yếu tố ngăn cản doanh nghiệp mới gia nhập thị trường. "
                            "Ví dụ: 'High startup costs are a major barrier to entry in the airline industry.' "
                            "Trong bài đọc, barrier giải thích vì sao một số thị trường chỉ có ít người chơi — "
                            "rào cản càng cao, càng ít doanh nghiệp mới có thể tham gia.\n\n"
                            "Từ thứ năm là market — danh từ — nghĩa là thị trường, "
                            "nơi người mua và người bán gặp nhau để trao đổi hàng hóa hoặc dịch vụ. "
                            "Ví dụ: 'The market for organic food has grown rapidly as consumers become more health-conscious.' "
                            "Trong bài đọc, market không chỉ là một địa điểm vật lý — "
                            "nó là toàn bộ hệ thống mua bán cho một loại sản phẩm cụ thể.\n\n"
                            "Từ cuối cùng là industry — danh từ — nghĩa là ngành công nghiệp, "
                            "tập hợp các doanh nghiệp sản xuất cùng loại sản phẩm hoặc dịch vụ. "
                            "Ví dụ: 'The Vietnamese textile industry employs millions of workers and exports to markets worldwide.' "
                            "Trong bài đọc, industry được dùng để chỉ nhóm các công ty hoạt động trong cùng lĩnh vực — "
                            "phân tích cấu trúc thị trường luôn bắt đầu bằng việc xác định industry.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về các loại cấu trúc thị trường nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Các loại cấu trúc thị trường",
                    "description": "Học 6 từ: monopoly, oligopoly, competition, barrier, market, industry",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Các loại cấu trúc thị trường",
                    "description": "Học 6 từ: monopoly, oligopoly, competition, barrier, market, industry",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Các loại cấu trúc thị trường",
                    "description": "Học 6 từ: monopoly, oligopoly, competition, barrier, market, industry",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Các loại cấu trúc thị trường",
                    "description": "Học 6 từ: monopoly, oligopoly, competition, barrier, market, industry",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Các loại cấu trúc thị trường",
                    "description": "Học 6 từ: monopoly, oligopoly, competition, barrier, market, industry",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Các loại cấu trúc thị trường",
                    "description": "Not all markets look the same. Walk into a local wet market in Vietnam and you will see dozens of vendors selling similar vegetables.",
                    "data": {
                        "text": (
                            "Not all markets look the same. Walk into a local wet market in Vietnam and you will see "
                            "dozens of vendors selling similar vegetables, each competing for your attention with lower prices "
                            "or fresher produce. Now think about your electricity bill — there is only one company that supplies "
                            "power to your home, and you cannot choose another. These two situations represent very different "
                            "market structures, and understanding them is essential to microeconomics.\n\n"
                            "At one extreme is perfect competition. In a perfectly competitive market, many small firms "
                            "sell identical products. No single seller can influence the price because buyers can always "
                            "go to someone else. The vegetable market is close to this model. Competition keeps prices low "
                            "and pushes sellers to be efficient. If one vendor charges too much, customers simply walk "
                            "to the next stall.\n\n"
                            "At the other extreme is a monopoly. A monopoly exists when a single firm controls the entire "
                            "market for a product or service. Because there are no competitors, the monopolist can set "
                            "prices higher than they would be under competition. Utility companies — electricity, water, "
                            "natural gas — are classic examples. The industry has room for only one provider because "
                            "building a second set of power lines or water pipes would be wasteful.\n\n"
                            "Between these two extremes lies the oligopoly. An oligopoly is a market dominated by a few "
                            "large firms. The mobile phone network in Vietnam is a good example — a handful of companies "
                            "control most of the market. In an oligopoly, each firm watches its rivals closely. "
                            "If one company lowers its price, the others must decide whether to follow or risk losing customers.\n\n"
                            "What determines which structure a market takes? A key factor is the barrier to entry. "
                            "A barrier is anything that makes it difficult for new firms to enter an industry. "
                            "High startup costs, government licenses, patents, and control of essential resources "
                            "are all barriers. When barriers are high, fewer firms can enter, and the market tends "
                            "toward monopoly or oligopoly. When barriers are low, many firms can compete, "
                            "and the market moves toward perfect competition.\n\n"
                            "The structure of a market matters because it affects prices, quality, and innovation. "
                            "In competitive markets, firms must constantly improve to survive. "
                            "In monopolies, the lack of competition can lead to higher prices and less motivation to innovate. "
                            "Economists study market structures to understand how different industries work "
                            "and to recommend policies that promote fair competition."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Các loại cấu trúc thị trường",
                    "description": "Not all markets look the same. Walk into a local wet market in Vietnam and you will see dozens of vendors selling similar vegetables.",
                    "data": {
                        "text": (
                            "Not all markets look the same. Walk into a local wet market in Vietnam and you will see "
                            "dozens of vendors selling similar vegetables, each competing for your attention with lower prices "
                            "or fresher produce. Now think about your electricity bill — there is only one company that supplies "
                            "power to your home, and you cannot choose another. These two situations represent very different "
                            "market structures, and understanding them is essential to microeconomics.\n\n"
                            "At one extreme is perfect competition. In a perfectly competitive market, many small firms "
                            "sell identical products. No single seller can influence the price because buyers can always "
                            "go to someone else. The vegetable market is close to this model. Competition keeps prices low "
                            "and pushes sellers to be efficient. If one vendor charges too much, customers simply walk "
                            "to the next stall.\n\n"
                            "At the other extreme is a monopoly. A monopoly exists when a single firm controls the entire "
                            "market for a product or service. Because there are no competitors, the monopolist can set "
                            "prices higher than they would be under competition. Utility companies — electricity, water, "
                            "natural gas — are classic examples. The industry has room for only one provider because "
                            "building a second set of power lines or water pipes would be wasteful.\n\n"
                            "Between these two extremes lies the oligopoly. An oligopoly is a market dominated by a few "
                            "large firms. The mobile phone network in Vietnam is a good example — a handful of companies "
                            "control most of the market. In an oligopoly, each firm watches its rivals closely. "
                            "If one company lowers its price, the others must decide whether to follow or risk losing customers.\n\n"
                            "What determines which structure a market takes? A key factor is the barrier to entry. "
                            "A barrier is anything that makes it difficult for new firms to enter an industry. "
                            "High startup costs, government licenses, patents, and control of essential resources "
                            "are all barriers. When barriers are high, fewer firms can enter, and the market tends "
                            "toward monopoly or oligopoly. When barriers are low, many firms can compete, "
                            "and the market moves toward perfect competition.\n\n"
                            "The structure of a market matters because it affects prices, quality, and innovation. "
                            "In competitive markets, firms must constantly improve to survive. "
                            "In monopolies, the lack of competition can lead to higher prices and less motivation to innovate. "
                            "Economists study market structures to understand how different industries work "
                            "and to recommend policies that promote fair competition."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Các loại cấu trúc thị trường",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Not all markets look the same. Walk into a local wet market in Vietnam and you will see "
                            "dozens of vendors selling similar vegetables, each competing for your attention with lower prices "
                            "or fresher produce. Now think about your electricity bill — there is only one company that supplies "
                            "power to your home, and you cannot choose another. These two situations represent very different "
                            "market structures, and understanding them is essential to microeconomics.\n\n"
                            "At one extreme is perfect competition. In a perfectly competitive market, many small firms "
                            "sell identical products. No single seller can influence the price because buyers can always "
                            "go to someone else. The vegetable market is close to this model. Competition keeps prices low "
                            "and pushes sellers to be efficient. If one vendor charges too much, customers simply walk "
                            "to the next stall.\n\n"
                            "At the other extreme is a monopoly. A monopoly exists when a single firm controls the entire "
                            "market for a product or service. Because there are no competitors, the monopolist can set "
                            "prices higher than they would be under competition. Utility companies — electricity, water, "
                            "natural gas — are classic examples. The industry has room for only one provider because "
                            "building a second set of power lines or water pipes would be wasteful.\n\n"
                            "Between these two extremes lies the oligopoly. An oligopoly is a market dominated by a few "
                            "large firms. The mobile phone network in Vietnam is a good example — a handful of companies "
                            "control most of the market. In an oligopoly, each firm watches its rivals closely. "
                            "If one company lowers its price, the others must decide whether to follow or risk losing customers.\n\n"
                            "What determines which structure a market takes? A key factor is the barrier to entry. "
                            "A barrier is anything that makes it difficult for new firms to enter an industry. "
                            "High startup costs, government licenses, patents, and control of essential resources "
                            "are all barriers. When barriers are high, fewer firms can enter, and the market tends "
                            "toward monopoly or oligopoly. When barriers are low, many firms can compete, "
                            "and the market moves toward perfect competition.\n\n"
                            "The structure of a market matters because it affects prices, quality, and innovation. "
                            "In competitive markets, firms must constantly improve to survive. "
                            "In monopolies, the lack of competition can lead to higher prices and less motivation to innovate. "
                            "Economists study market structures to understand how different industries work "
                            "and to recommend policies that promote fair competition."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Các loại cấu trúc thị trường",
                    "description": "Viết câu sử dụng 6 từ vựng về cấu trúc thị trường.",
                    "data": {
                        "vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry"],
                        "items": [
                            {
                                "targetVocab": "monopoly",
                                "prompt": "Dùng từ 'monopoly' để viết một câu về một công ty kiểm soát toàn bộ thị trường cho một sản phẩm hoặc dịch vụ. Ví dụ: The water utility company holds a monopoly in the province because no other firm has the infrastructure to deliver clean water to households."
                            },
                            {
                                "targetVocab": "oligopoly",
                                "prompt": "Dùng từ 'oligopoly' để viết một câu về một ngành chỉ có vài công ty lớn chi phối. Ví dụ: The Vietnamese cement industry is an oligopoly where three major producers control over seventy percent of total output."
                            },
                            {
                                "targetVocab": "competition",
                                "prompt": "Dùng từ 'competition' để viết một câu về cách cạnh tranh giữa các doanh nghiệp mang lại lợi ích cho người tiêu dùng. Ví dụ: Fierce competition among ride-hailing apps in Ho Chi Minh City has driven down fares and improved service quality for passengers."
                            },
                            {
                                "targetVocab": "barrier",
                                "prompt": "Dùng từ 'barrier' để viết một câu về rào cản ngăn doanh nghiệp mới gia nhập một ngành cụ thể. Ví dụ: The enormous cost of building a semiconductor factory is a barrier that prevents most companies from entering the chip-making industry."
                            },
                            {
                                "targetVocab": "market",
                                "prompt": "Dùng từ 'market' để viết một câu về một thị trường cụ thể và đặc điểm của nó. Ví dụ: The market for electric scooters in Vietnam is expanding rapidly as young urban commuters look for affordable and eco-friendly transportation."
                            },
                            {
                                "targetVocab": "industry",
                                "prompt": "Dùng từ 'industry' để viết một câu về một ngành công nghiệp và vai trò của nó trong nền kinh tế. Ví dụ: The tourism industry accounts for a significant share of Vietnam's GDP and provides employment for millions of workers across the country."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về cạnh tranh, sáp nhập và luật chống độc quyền.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "monopoly — độc quyền, oligopoly — thị trường thiểu số, competition — cạnh tranh, "
                            "barrier — rào cản, market — thị trường, và industry — ngành công nghiệp. "
                            "Bạn đã hiểu các loại cấu trúc thị trường cơ bản và vì sao rào cản gia nhập "
                            "quyết định số lượng doanh nghiệp trong một ngành.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: differentiation, homogeneous, concentration, "
                            "merger, antitrust, và regulation. Những từ này đưa bạn sâu hơn vào cách doanh nghiệp "
                            "cạnh tranh và cách chính phủ kiểm soát quyền lực thị trường.\n\n"
                            "Từ đầu tiên là differentiation — danh từ — nghĩa là sự khác biệt hóa, "
                            "chiến lược mà doanh nghiệp tạo ra sản phẩm khác biệt so với đối thủ "
                            "để thu hút khách hàng. "
                            "Ví dụ: 'Apple uses product differentiation to charge premium prices — its design, ecosystem, and brand image set it apart from competitors.' "
                            "Trong bài đọc, differentiation giải thích vì sao trong cùng một ngành, "
                            "có công ty bán giá cao mà vẫn đông khách — vì sản phẩm của họ không giống ai.\n\n"
                            "Từ thứ hai là homogeneous — tính từ — nghĩa là đồng nhất, "
                            "khi các sản phẩm trên thị trường giống hệt nhau và không có sự khác biệt. "
                            "Ví dụ: 'In a perfectly competitive market, products are homogeneous — one kilogram of white rice from any farmer is essentially the same.' "
                            "Trong bài đọc, homogeneous là đặc điểm của thị trường cạnh tranh hoàn hảo — "
                            "nơi sản phẩm không có gì khác biệt nên giá là yếu tố quyết định duy nhất.\n\n"
                            "Từ thứ ba là concentration — danh từ — nghĩa là mức độ tập trung, "
                            "tỷ lệ thị phần mà một vài doanh nghiệp lớn nhất nắm giữ trong một ngành. "
                            "Ví dụ: 'Market concentration in the banking sector is high — the top five banks hold over sixty percent of all deposits.' "
                            "Trong bài đọc, concentration là thước đo để xác định thị trường đang gần monopoly "
                            "hay gần cạnh tranh hoàn hảo.\n\n"
                            "Từ thứ tư là merger — danh từ — nghĩa là sáp nhập, "
                            "khi hai hoặc nhiều công ty hợp nhất thành một công ty duy nhất. "
                            "Ví dụ: 'The merger between the two largest airlines created a company that controls nearly half of all domestic flights.' "
                            "Trong bài đọc, merger là một trong những cách mà concentration tăng lên — "
                            "khi các công ty sáp nhập, số lượng đối thủ giảm và quyền lực thị trường tập trung hơn.\n\n"
                            "Từ thứ năm là antitrust — tính từ — nghĩa là chống độc quyền, "
                            "liên quan đến luật pháp và chính sách ngăn chặn doanh nghiệp lạm dụng quyền lực thị trường. "
                            "Ví dụ: 'The government filed an antitrust lawsuit against the tech giant for using its dominance to crush smaller competitors.' "
                            "Trong bài đọc, antitrust là công cụ pháp lý mà chính phủ sử dụng "
                            "để bảo vệ cạnh tranh và ngăn monopoly gây hại cho người tiêu dùng.\n\n"
                            "Từ cuối cùng là regulation — danh từ — nghĩa là quy định, "
                            "các luật lệ và quy tắc mà chính phủ đặt ra để kiểm soát hoạt động của doanh nghiệp. "
                            "Ví dụ: 'Strict environmental regulation forces factories to invest in cleaner technology, even if it raises production costs.' "
                            "Trong bài đọc, regulation là cách chính phủ can thiệp vào thị trường — "
                            "đặc biệt quan trọng trong các ngành có monopoly hoặc oligopoly.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về cạnh tranh và quy định thị trường nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cạnh tranh và quy định thị trường",
                    "description": "Học 6 từ: differentiation, homogeneous, concentration, merger, antitrust, regulation",
                    "data": {"vocabList": ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cạnh tranh và quy định thị trường",
                    "description": "Học 6 từ: differentiation, homogeneous, concentration, merger, antitrust, regulation",
                    "data": {"vocabList": ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cạnh tranh và quy định thị trường",
                    "description": "Học 6 từ: differentiation, homogeneous, concentration, merger, antitrust, regulation",
                    "data": {"vocabList": ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cạnh tranh và quy định thị trường",
                    "description": "Học 6 từ: differentiation, homogeneous, concentration, merger, antitrust, regulation",
                    "data": {"vocabList": ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Cạnh tranh và quy định thị trường",
                    "description": "Học 6 từ: differentiation, homogeneous, concentration, merger, antitrust, regulation",
                    "data": {"vocabList": ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cạnh tranh và quy định thị trường",
                    "description": "How do firms compete when they cannot simply lower prices? In many industries, the answer is differentiation.",
                    "data": {
                        "text": (
                            "How do firms compete when they cannot simply lower prices? "
                            "In many industries, the answer is differentiation. "
                            "Differentiation means making your product stand out from the rest — "
                            "through design, quality, branding, or customer service. "
                            "When products are differentiated, consumers see them as unique, "
                            "and firms can charge higher prices without losing all their customers.\n\n"
                            "In contrast, some markets sell homogeneous products — goods that are essentially identical "
                            "no matter who produces them. Commodities like raw sugar, steel, or unprocessed rice "
                            "are homogeneous. In these markets, buyers care only about price "
                            "because one seller's product is the same as another's. "
                            "Competition in homogeneous markets is fierce and margins are thin.\n\n"
                            "Economists measure how much power a few firms hold using a concept called market concentration. "
                            "Concentration tells us what share of total sales belongs to the largest companies in an industry. "
                            "A market where the top four firms control ninety percent of sales has high concentration — "
                            "it is likely an oligopoly or close to a monopoly. "
                            "A market where no single firm holds more than two percent has low concentration — "
                            "it is closer to perfect competition.\n\n"
                            "One way concentration increases is through mergers. "
                            "A merger happens when two companies combine into one. "
                            "Sometimes mergers create efficiency — the combined firm can produce at lower cost. "
                            "But mergers can also reduce competition. "
                            "If the two largest firms in an industry merge, the remaining competitors may be too small "
                            "to challenge the new giant, and consumers may face higher prices.\n\n"
                            "This is where antitrust policy comes in. "
                            "Antitrust laws are designed to prevent firms from gaining too much market power. "
                            "Governments use antitrust regulation to block mergers that would harm competition, "
                            "to break up monopolies, and to punish companies that engage in unfair practices. "
                            "In the United States, the Sherman Act and the Clayton Act are landmark antitrust laws. "
                            "In Vietnam, the Competition Law serves a similar purpose.\n\n"
                            "Regulation goes beyond antitrust. Governments regulate industries for many reasons — "
                            "to protect consumers, to ensure safety, to preserve the environment, "
                            "and to prevent firms from exploiting their market power. "
                            "In industries with natural monopolies, such as electricity or water supply, "
                            "regulation often sets the prices that the monopolist can charge. "
                            "The goal is to balance the efficiency of having one provider "
                            "with the need to protect consumers from unfair pricing.\n\n"
                            "The interplay between competition, concentration, and regulation "
                            "shapes every industry you can think of — from the coffee shop on your street corner "
                            "to the global technology giants that dominate the internet."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cạnh tranh và quy định thị trường",
                    "description": "How do firms compete when they cannot simply lower prices? In many industries, the answer is differentiation.",
                    "data": {
                        "text": (
                            "How do firms compete when they cannot simply lower prices? "
                            "In many industries, the answer is differentiation. "
                            "Differentiation means making your product stand out from the rest — "
                            "through design, quality, branding, or customer service. "
                            "When products are differentiated, consumers see them as unique, "
                            "and firms can charge higher prices without losing all their customers.\n\n"
                            "In contrast, some markets sell homogeneous products — goods that are essentially identical "
                            "no matter who produces them. Commodities like raw sugar, steel, or unprocessed rice "
                            "are homogeneous. In these markets, buyers care only about price "
                            "because one seller's product is the same as another's. "
                            "Competition in homogeneous markets is fierce and margins are thin.\n\n"
                            "Economists measure how much power a few firms hold using a concept called market concentration. "
                            "Concentration tells us what share of total sales belongs to the largest companies in an industry. "
                            "A market where the top four firms control ninety percent of sales has high concentration — "
                            "it is likely an oligopoly or close to a monopoly. "
                            "A market where no single firm holds more than two percent has low concentration — "
                            "it is closer to perfect competition.\n\n"
                            "One way concentration increases is through mergers. "
                            "A merger happens when two companies combine into one. "
                            "Sometimes mergers create efficiency — the combined firm can produce at lower cost. "
                            "But mergers can also reduce competition. "
                            "If the two largest firms in an industry merge, the remaining competitors may be too small "
                            "to challenge the new giant, and consumers may face higher prices.\n\n"
                            "This is where antitrust policy comes in. "
                            "Antitrust laws are designed to prevent firms from gaining too much market power. "
                            "Governments use antitrust regulation to block mergers that would harm competition, "
                            "to break up monopolies, and to punish companies that engage in unfair practices. "
                            "In the United States, the Sherman Act and the Clayton Act are landmark antitrust laws. "
                            "In Vietnam, the Competition Law serves a similar purpose.\n\n"
                            "Regulation goes beyond antitrust. Governments regulate industries for many reasons — "
                            "to protect consumers, to ensure safety, to preserve the environment, "
                            "and to prevent firms from exploiting their market power. "
                            "In industries with natural monopolies, such as electricity or water supply, "
                            "regulation often sets the prices that the monopolist can charge. "
                            "The goal is to balance the efficiency of having one provider "
                            "with the need to protect consumers from unfair pricing.\n\n"
                            "The interplay between competition, concentration, and regulation "
                            "shapes every industry you can think of — from the coffee shop on your street corner "
                            "to the global technology giants that dominate the internet."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cạnh tranh và quy định thị trường",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "How do firms compete when they cannot simply lower prices? "
                            "In many industries, the answer is differentiation. "
                            "Differentiation means making your product stand out from the rest — "
                            "through design, quality, branding, or customer service. "
                            "When products are differentiated, consumers see them as unique, "
                            "and firms can charge higher prices without losing all their customers.\n\n"
                            "In contrast, some markets sell homogeneous products — goods that are essentially identical "
                            "no matter who produces them. Commodities like raw sugar, steel, or unprocessed rice "
                            "are homogeneous. In these markets, buyers care only about price "
                            "because one seller's product is the same as another's. "
                            "Competition in homogeneous markets is fierce and margins are thin.\n\n"
                            "Economists measure how much power a few firms hold using a concept called market concentration. "
                            "Concentration tells us what share of total sales belongs to the largest companies in an industry. "
                            "A market where the top four firms control ninety percent of sales has high concentration — "
                            "it is likely an oligopoly or close to a monopoly. "
                            "A market where no single firm holds more than two percent has low concentration — "
                            "it is closer to perfect competition.\n\n"
                            "One way concentration increases is through mergers. "
                            "A merger happens when two companies combine into one. "
                            "Sometimes mergers create efficiency — the combined firm can produce at lower cost. "
                            "But mergers can also reduce competition. "
                            "If the two largest firms in an industry merge, the remaining competitors may be too small "
                            "to challenge the new giant, and consumers may face higher prices.\n\n"
                            "This is where antitrust policy comes in. "
                            "Antitrust laws are designed to prevent firms from gaining too much market power. "
                            "Governments use antitrust regulation to block mergers that would harm competition, "
                            "to break up monopolies, and to punish companies that engage in unfair practices. "
                            "In the United States, the Sherman Act and the Clayton Act are landmark antitrust laws. "
                            "In Vietnam, the Competition Law serves a similar purpose.\n\n"
                            "Regulation goes beyond antitrust. Governments regulate industries for many reasons — "
                            "to protect consumers, to ensure safety, to preserve the environment, "
                            "and to prevent firms from exploiting their market power. "
                            "In industries with natural monopolies, such as electricity or water supply, "
                            "regulation often sets the prices that the monopolist can charge. "
                            "The goal is to balance the efficiency of having one provider "
                            "with the need to protect consumers from unfair pricing.\n\n"
                            "The interplay between competition, concentration, and regulation "
                            "shapes every industry you can think of — from the coffee shop on your street corner "
                            "to the global technology giants that dominate the internet."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cạnh tranh và quy định thị trường",
                    "description": "Viết câu sử dụng 6 từ vựng về cạnh tranh và quy định.",
                    "data": {
                        "vocabList": ["differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation"],
                        "items": [
                            {
                                "targetVocab": "differentiation",
                                "prompt": "Dùng từ 'differentiation' để viết một câu về cách một doanh nghiệp tạo sự khác biệt cho sản phẩm của mình so với đối thủ. Ví dụ: The coffee chain achieved differentiation by roasting its own beans in-store, giving customers a freshness that competitors could not match."
                            },
                            {
                                "targetVocab": "homogeneous",
                                "prompt": "Dùng từ 'homogeneous' để viết một câu về một thị trường nơi các sản phẩm giống hệt nhau. Ví dụ: The market for table salt is nearly homogeneous because consumers cannot tell the difference between one brand and another."
                            },
                            {
                                "targetVocab": "concentration",
                                "prompt": "Dùng từ 'concentration' để viết một câu về mức độ tập trung thị phần trong một ngành cụ thể. Ví dụ: The high concentration in the domestic beer market means that two companies account for almost eighty percent of all sales."
                            },
                            {
                                "targetVocab": "merger",
                                "prompt": "Dùng từ 'merger' để viết một câu về việc hai công ty sáp nhập và tác động đến thị trường. Ví dụ: The merger between the two largest supermarket chains raised concerns that reduced competition would lead to higher grocery prices."
                            },
                            {
                                "targetVocab": "antitrust",
                                "prompt": "Dùng từ 'antitrust' để viết một câu về luật chống độc quyền và vai trò bảo vệ cạnh tranh. Ví dụ: European antitrust authorities fined the technology company billions of euros for abusing its dominant position in the search engine market."
                            },
                            {
                                "targetVocab": "regulation",
                                "prompt": "Dùng từ 'regulation' để viết một câu về quy định của chính phủ đối với một ngành kinh tế. Ví dụ: New regulation on data privacy requires all social media platforms to obtain clear consent before collecting personal information from users."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về cartel, thông đồng và tự do hóa thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng về cấu trúc thị trường! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học.\n\n"
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: "
                            "monopoly — độc quyền, oligopoly — thị trường thiểu số, competition — cạnh tranh, "
                            "barrier — rào cản, market — thị trường, và industry — ngành công nghiệp. "
                            "Đây là bộ khung để phân biệt các loại cấu trúc thị trường.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "differentiation — sự khác biệt hóa, homogeneous — đồng nhất, "
                            "concentration — mức độ tập trung, merger — sáp nhập, "
                            "antitrust — chống độc quyền, và regulation — quy định. "
                            "Những từ này giúp bạn hiểu cách doanh nghiệp cạnh tranh và chính phủ kiểm soát.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào mặt tối của thị trường: "
                            "khi các doanh nghiệp không cạnh tranh mà lại bắt tay nhau để kiểm soát giá. "
                            "Bạn sẽ học 6 từ mới: cartel, collusion, duopoly, contestable, dominance, và deregulation.\n\n"
                            "Từ đầu tiên là cartel — danh từ — nghĩa là tổ chức liên minh giá, "
                            "nhóm các doanh nghiệp thỏa thuận với nhau để kiểm soát giá hoặc sản lượng "
                            "thay vì cạnh tranh. "
                            "Ví dụ: 'OPEC is often described as a cartel because its member countries coordinate oil production to influence global prices.' "
                            "Trong bài đọc, cartel là ví dụ điển hình về cách các doanh nghiệp "
                            "phá vỡ cạnh tranh để tối đa hóa lợi nhuận chung.\n\n"
                            "Từ thứ hai là collusion — danh từ — nghĩa là sự thông đồng, "
                            "thỏa thuận bí mật giữa các doanh nghiệp để cùng tăng giá hoặc chia thị trường. "
                            "Ví dụ: 'The construction companies were caught in collusion — they secretly agreed to take turns winning government contracts at inflated prices.' "
                            "Trong bài đọc, collusion là hành vi bất hợp pháp mà luật antitrust nhắm vào — "
                            "khi các đối thủ giả vờ cạnh tranh nhưng thực chất đã thỏa thuận ngầm.\n\n"
                            "Từ thứ ba là duopoly — danh từ — nghĩa là thị trường song quyền, "
                            "dạng đặc biệt của oligopoly khi chỉ có đúng hai doanh nghiệp chi phối thị trường. "
                            "Ví dụ: 'The commercial aircraft industry is essentially a duopoly, with Boeing and Airbus controlling nearly all large plane orders worldwide.' "
                            "Trong bài đọc, duopoly cho thấy khi thị trường chỉ có hai người chơi, "
                            "mỗi quyết định của một bên đều ảnh hưởng trực tiếp đến bên kia.\n\n"
                            "Từ thứ tư là contestable — tính từ — nghĩa là có thể bị thách thức, "
                            "mô tả thị trường mà dù chỉ có ít doanh nghiệp, đối thủ mới vẫn có thể dễ dàng gia nhập. "
                            "Ví dụ: 'The budget airline market is highly contestable because new carriers can lease planes and start flying routes with relatively low investment.' "
                            "Trong bài đọc, contestable là khái niệm quan trọng — "
                            "một thị trường không cần nhiều đối thủ để có cạnh tranh, "
                            "chỉ cần mối đe dọa rằng đối thủ mới có thể xuất hiện bất cứ lúc nào.\n\n"
                            "Từ thứ năm là dominance — danh từ — nghĩa là sự thống trị, "
                            "vị thế mà một doanh nghiệp kiểm soát phần lớn thị trường và có khả năng "
                            "ảnh hưởng đến giá cả hoặc loại bỏ đối thủ. "
                            "Ví dụ: 'The company's dominance in the search engine market allows it to set advertising rates that smaller rivals cannot compete with.' "
                            "Trong bài đọc, dominance là trạng thái mà luật antitrust cố gắng ngăn chặn — "
                            "khi một công ty quá mạnh, cạnh tranh bị bóp nghẹt.\n\n"
                            "Từ cuối cùng là deregulation — danh từ — nghĩa là tự do hóa, "
                            "quá trình chính phủ gỡ bỏ hoặc giảm bớt các quy định kiểm soát một ngành. "
                            "Ví dụ: 'The deregulation of the telecommunications industry in the 1990s led to lower phone bills and more choices for consumers.' "
                            "Trong bài đọc, deregulation là mặt đối lập của regulation — "
                            "khi chính phủ tin rằng thị trường tự do sẽ hoạt động hiệu quả hơn.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về cartel và quyền lực thị trường nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cartel và quyền lực thị trường",
                    "description": "Học 6 từ: cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cartel và quyền lực thị trường",
                    "description": "Học 6 từ: cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cartel và quyền lực thị trường",
                    "description": "Học 6 từ: cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cartel và quyền lực thị trường",
                    "description": "Học 6 từ: cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Cartel và quyền lực thị trường",
                    "description": "Học 6 từ: cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cartel, thông đồng và quyền lực thị trường",
                    "description": "When a few powerful firms control an industry, they face a temptation that goes against the spirit of free markets.",
                    "data": {
                        "text": (
                            "When a few powerful firms control an industry, they face a temptation "
                            "that goes against the spirit of free markets: instead of competing, they can cooperate. "
                            "If rival companies secretly agree to fix prices or divide territories, "
                            "they can earn higher profits than they would in a competitive market. "
                            "This secret agreement is called collusion, and the group that forms it is called a cartel.\n\n"
                            "The most famous cartel in the world is OPEC — the Organization of the Petroleum Exporting Countries. "
                            "OPEC members agree on how much oil each country will produce. "
                            "By limiting total output, they keep oil prices higher than they would be "
                            "if every country pumped as much as it could. "
                            "Cartels are effective when there are few members and the product is homogeneous — "
                            "oil from Saudi Arabia is essentially the same as oil from Nigeria.\n\n"
                            "However, cartels are inherently unstable. Each member has an incentive to cheat — "
                            "to secretly produce more than its agreed share and sell at the high cartel price. "
                            "If too many members cheat, the cartel collapses and prices fall. "
                            "This tension between cooperation and self-interest is one of the central puzzles of oligopoly theory.\n\n"
                            "In most countries, collusion among private companies is illegal. "
                            "Antitrust authorities investigate suspected cartels and impose heavy fines. "
                            "But proving collusion is difficult because the agreements are secret. "
                            "Sometimes firms engage in tacit collusion — they do not communicate directly "
                            "but follow each other's pricing signals. "
                            "When one airline raises its fare, others quickly match the increase. "
                            "Is this collusion or simply rational behavior in an oligopoly? The line is often blurry.\n\n"
                            "A special case of oligopoly is the duopoly — a market with exactly two dominant firms. "
                            "The commercial aircraft industry is a classic duopoly. "
                            "Boeing and Airbus together fill nearly every order for large passenger planes. "
                            "In a duopoly, each firm's strategy depends entirely on what the other does. "
                            "If Boeing offers a discount to an airline, Airbus must decide whether to match it or lose the sale.\n\n"
                            "Not all concentrated markets behave like monopolies, however. "
                            "Economists use the concept of a contestable market to describe situations "
                            "where even a single firm or a duopoly cannot exploit its dominance "
                            "because new competitors could enter easily. "
                            "If barriers to entry are low, the threat of new entrants keeps prices in check. "
                            "A market does not need many firms to be competitive — "
                            "it just needs the possibility that new firms could appear.\n\n"
                            "When a firm achieves dominance — controlling a large share of the market — "
                            "regulators pay close attention. Dominance itself is not illegal, "
                            "but abusing it is. A dominant firm that uses its power to block competitors, "
                            "force suppliers into exclusive deals, or undercut rivals below cost "
                            "may face antitrust action.\n\n"
                            "On the other side of the policy spectrum is deregulation — "
                            "the process of removing government controls from an industry. "
                            "In the 1980s and 1990s, many countries deregulated airlines, telecommunications, "
                            "and energy markets. The idea was that reducing regulation would lower barriers, "
                            "increase competition, and benefit consumers through lower prices and more choices. "
                            "Deregulation has produced mixed results — in some industries it worked well, "
                            "while in others it led to instability or new forms of market dominance."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cartel, thông đồng và quyền lực thị trường",
                    "description": "When a few powerful firms control an industry, they face a temptation that goes against the spirit of free markets.",
                    "data": {
                        "text": (
                            "When a few powerful firms control an industry, they face a temptation "
                            "that goes against the spirit of free markets: instead of competing, they can cooperate. "
                            "If rival companies secretly agree to fix prices or divide territories, "
                            "they can earn higher profits than they would in a competitive market. "
                            "This secret agreement is called collusion, and the group that forms it is called a cartel.\n\n"
                            "The most famous cartel in the world is OPEC — the Organization of the Petroleum Exporting Countries. "
                            "OPEC members agree on how much oil each country will produce. "
                            "By limiting total output, they keep oil prices higher than they would be "
                            "if every country pumped as much as it could. "
                            "Cartels are effective when there are few members and the product is homogeneous — "
                            "oil from Saudi Arabia is essentially the same as oil from Nigeria.\n\n"
                            "However, cartels are inherently unstable. Each member has an incentive to cheat — "
                            "to secretly produce more than its agreed share and sell at the high cartel price. "
                            "If too many members cheat, the cartel collapses and prices fall. "
                            "This tension between cooperation and self-interest is one of the central puzzles of oligopoly theory.\n\n"
                            "In most countries, collusion among private companies is illegal. "
                            "Antitrust authorities investigate suspected cartels and impose heavy fines. "
                            "But proving collusion is difficult because the agreements are secret. "
                            "Sometimes firms engage in tacit collusion — they do not communicate directly "
                            "but follow each other's pricing signals. "
                            "When one airline raises its fare, others quickly match the increase. "
                            "Is this collusion or simply rational behavior in an oligopoly? The line is often blurry.\n\n"
                            "A special case of oligopoly is the duopoly — a market with exactly two dominant firms. "
                            "The commercial aircraft industry is a classic duopoly. "
                            "Boeing and Airbus together fill nearly every order for large passenger planes. "
                            "In a duopoly, each firm's strategy depends entirely on what the other does. "
                            "If Boeing offers a discount to an airline, Airbus must decide whether to match it or lose the sale.\n\n"
                            "Not all concentrated markets behave like monopolies, however. "
                            "Economists use the concept of a contestable market to describe situations "
                            "where even a single firm or a duopoly cannot exploit its dominance "
                            "because new competitors could enter easily. "
                            "If barriers to entry are low, the threat of new entrants keeps prices in check. "
                            "A market does not need many firms to be competitive — "
                            "it just needs the possibility that new firms could appear.\n\n"
                            "When a firm achieves dominance — controlling a large share of the market — "
                            "regulators pay close attention. Dominance itself is not illegal, "
                            "but abusing it is. A dominant firm that uses its power to block competitors, "
                            "force suppliers into exclusive deals, or undercut rivals below cost "
                            "may face antitrust action.\n\n"
                            "On the other side of the policy spectrum is deregulation — "
                            "the process of removing government controls from an industry. "
                            "In the 1980s and 1990s, many countries deregulated airlines, telecommunications, "
                            "and energy markets. The idea was that reducing regulation would lower barriers, "
                            "increase competition, and benefit consumers through lower prices and more choices. "
                            "Deregulation has produced mixed results — in some industries it worked well, "
                            "while in others it led to instability or new forms of market dominance."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cartel, thông đồng và quyền lực thị trường",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When a few powerful firms control an industry, they face a temptation "
                            "that goes against the spirit of free markets: instead of competing, they can cooperate. "
                            "If rival companies secretly agree to fix prices or divide territories, "
                            "they can earn higher profits than they would in a competitive market. "
                            "This secret agreement is called collusion, and the group that forms it is called a cartel.\n\n"
                            "The most famous cartel in the world is OPEC — the Organization of the Petroleum Exporting Countries. "
                            "OPEC members agree on how much oil each country will produce. "
                            "By limiting total output, they keep oil prices higher than they would be "
                            "if every country pumped as much as it could. "
                            "Cartels are effective when there are few members and the product is homogeneous — "
                            "oil from Saudi Arabia is essentially the same as oil from Nigeria.\n\n"
                            "However, cartels are inherently unstable. Each member has an incentive to cheat — "
                            "to secretly produce more than its agreed share and sell at the high cartel price. "
                            "If too many members cheat, the cartel collapses and prices fall. "
                            "This tension between cooperation and self-interest is one of the central puzzles of oligopoly theory.\n\n"
                            "In most countries, collusion among private companies is illegal. "
                            "Antitrust authorities investigate suspected cartels and impose heavy fines. "
                            "But proving collusion is difficult because the agreements are secret. "
                            "Sometimes firms engage in tacit collusion — they do not communicate directly "
                            "but follow each other's pricing signals. "
                            "When one airline raises its fare, others quickly match the increase. "
                            "Is this collusion or simply rational behavior in an oligopoly? The line is often blurry.\n\n"
                            "A special case of oligopoly is the duopoly — a market with exactly two dominant firms. "
                            "The commercial aircraft industry is a classic duopoly. "
                            "Boeing and Airbus together fill nearly every order for large passenger planes. "
                            "In a duopoly, each firm's strategy depends entirely on what the other does. "
                            "If Boeing offers a discount to an airline, Airbus must decide whether to match it or lose the sale.\n\n"
                            "Not all concentrated markets behave like monopolies, however. "
                            "Economists use the concept of a contestable market to describe situations "
                            "where even a single firm or a duopoly cannot exploit its dominance "
                            "because new competitors could enter easily. "
                            "If barriers to entry are low, the threat of new entrants keeps prices in check. "
                            "A market does not need many firms to be competitive — "
                            "it just needs the possibility that new firms could appear.\n\n"
                            "When a firm achieves dominance — controlling a large share of the market — "
                            "regulators pay close attention. Dominance itself is not illegal, "
                            "but abusing it is. A dominant firm that uses its power to block competitors, "
                            "force suppliers into exclusive deals, or undercut rivals below cost "
                            "may face antitrust action.\n\n"
                            "On the other side of the policy spectrum is deregulation — "
                            "the process of removing government controls from an industry. "
                            "In the 1980s and 1990s, many countries deregulated airlines, telecommunications, "
                            "and energy markets. The idea was that reducing regulation would lower barriers, "
                            "increase competition, and benefit consumers through lower prices and more choices. "
                            "Deregulation has produced mixed results — in some industries it worked well, "
                            "while in others it led to instability or new forms of market dominance."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cartel và quyền lực thị trường",
                    "description": "Viết câu sử dụng 6 từ vựng về cartel và quyền lực thị trường.",
                    "data": {
                        "vocabList": ["cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"],
                        "items": [
                            {
                                "targetVocab": "cartel",
                                "prompt": "Dùng từ 'cartel' để viết một câu về nhóm doanh nghiệp thỏa thuận kiểm soát giá hoặc sản lượng. Ví dụ: The cement cartel was exposed when investigators discovered that the three largest producers had been secretly fixing prices for over a decade."
                            },
                            {
                                "targetVocab": "collusion",
                                "prompt": "Dùng từ 'collusion' để viết một câu về hành vi thông đồng bí mật giữa các doanh nghiệp. Ví dụ: Evidence of collusion emerged when emails showed that rival pharmaceutical companies had agreed to keep generic drug prices artificially high."
                            },
                            {
                                "targetVocab": "duopoly",
                                "prompt": "Dùng từ 'duopoly' để viết một câu về thị trường chỉ có hai doanh nghiệp chi phối. Ví dụ: The operating system market for smartphones is a duopoly — Android and iOS together power over ninety-nine percent of all devices sold worldwide."
                            },
                            {
                                "targetVocab": "contestable",
                                "prompt": "Dùng từ 'contestable' để viết một câu về thị trường mà đối thủ mới có thể dễ dàng gia nhập. Ví dụ: The food delivery market remains contestable because any startup with a good app and a network of drivers can begin competing almost immediately."
                            },
                            {
                                "targetVocab": "dominance",
                                "prompt": "Dùng từ 'dominance' để viết một câu về vị thế thống trị của một doanh nghiệp trên thị trường. Ví dụ: The company's dominance in the e-commerce sector gives it the power to negotiate lower shipping rates that smaller online stores cannot obtain."
                            },
                            {
                                "targetVocab": "deregulation",
                                "prompt": "Dùng từ 'deregulation' để viết một câu về quá trình chính phủ gỡ bỏ quy định kiểm soát một ngành. Ví dụ: The deregulation of the banking sector allowed new fintech companies to offer savings accounts and loans without the overhead costs of traditional banks."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Cấu trúc thị trường. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "monopoly — độc quyền, oligopoly — thị trường thiểu số, competition — cạnh tranh, "
                            "barrier — rào cản, market — thị trường, và industry — ngành công nghiệp. "
                            "Đây là bộ khung để phân biệt các loại thị trường khác nhau.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "differentiation — sự khác biệt hóa, homogeneous — đồng nhất, "
                            "concentration — mức độ tập trung, merger — sáp nhập, "
                            "antitrust — chống độc quyền, và regulation — quy định. "
                            "Những từ này giúp bạn hiểu cách doanh nghiệp cạnh tranh và chính phủ kiểm soát quyền lực thị trường.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "cartel — liên minh giá, collusion — thông đồng, duopoly — thị trường song quyền, "
                            "contestable — có thể bị thách thức, dominance — sự thống trị, "
                            "và deregulation — tự do hóa. "
                            "Đây là những từ về mặt tối và mặt sáng của quyền lực thị trường.\n\n"
                            "Bây giờ, phần ôn tập này sẽ giúp bạn củng cố toàn bộ 18 từ vựng. "
                            "Bạn sẽ xem lại flashcard, luyện phát âm, và viết câu với tất cả các từ. "
                            "Sau phần ôn tập, bạn sẽ sẵn sàng cho bài đọc tổng hợp — "
                            "một bài viết dài hơn sử dụng cả 18 từ trong một câu chuyện liền mạch "
                            "về cấu trúc thị trường. Hãy bắt đầu nào!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monopoly, oligopoly, competition, barrier, market, industry, differentiation, homogeneous, concentration, merger, antitrust, regulation, cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monopoly, oligopoly, competition, barrier, market, industry, differentiation, homogeneous, concentration, merger, antitrust, regulation, cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monopoly, oligopoly, competition, barrier, market, industry, differentiation, homogeneous, concentration, merger, antitrust, regulation, cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monopoly, oligopoly, competition, barrier, market, industry, differentiation, homogeneous, concentration, merger, antitrust, regulation, cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: monopoly, oligopoly, competition, barrier, market, industry, differentiation, homogeneous, concentration, merger, antitrust, regulation, cartel, collusion, duopoly, contestable, dominance, deregulation",
                    "data": {"vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng cấu trúc thị trường",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"],
                        "items": [
                            {
                                "targetVocab": "monopoly",
                                "prompt": "Dùng từ 'monopoly' để viết một câu về tác động của độc quyền đến giá cả và người tiêu dùng. Ví dụ: The state-owned postal service held a monopoly on letter delivery for decades, but the rise of email and private couriers has eroded its market power."
                            },
                            {
                                "targetVocab": "oligopoly",
                                "prompt": "Dùng từ 'oligopoly' để viết một câu về hành vi của các doanh nghiệp trong thị trường thiểu số. Ví dụ: In the Vietnamese mobile network oligopoly, when one carrier launches a new data plan, the others release similar packages within days."
                            },
                            {
                                "targetVocab": "competition",
                                "prompt": "Dùng từ 'competition' để viết một câu về lợi ích của cạnh tranh đối với đổi mới sáng tạo. Ví dụ: Healthy competition in the electric vehicle market has accelerated innovation, pushing companies to develop longer-lasting batteries and faster charging technology."
                            },
                            {
                                "targetVocab": "barrier",
                                "prompt": "Dùng từ 'barrier' để viết một câu về rào cản gia nhập trong ngành dược phẩm. Ví dụ: Patent protection creates a significant barrier to entry in the pharmaceutical industry, preventing generic manufacturers from copying new drugs for twenty years."
                            },
                            {
                                "targetVocab": "market",
                                "prompt": "Dùng từ 'market' để viết một câu về sự phát triển của một thị trường mới nổi. Ví dụ: The market for plant-based meat alternatives has expanded from a niche segment to a mainstream category found in every major supermarket chain."
                            },
                            {
                                "targetVocab": "industry",
                                "prompt": "Dùng từ 'industry' để viết một câu về sự chuyển đổi của một ngành công nghiệp truyền thống. Ví dụ: The publishing industry has undergone a dramatic transformation as digital books and audiobooks now account for nearly forty percent of total revenue."
                            },
                            {
                                "targetVocab": "differentiation",
                                "prompt": "Dùng từ 'differentiation' để viết một câu về chiến lược khác biệt hóa trong ngành thời trang. Ví dụ: Vietnamese fashion brands use differentiation through traditional fabric patterns and sustainable materials to stand out in a market flooded with fast fashion imports."
                            },
                            {
                                "targetVocab": "homogeneous",
                                "prompt": "Dùng từ 'homogeneous' để viết một câu về thị trường hàng hóa đồng nhất và cách cạnh tranh. Ví dụ: Because gasoline is a homogeneous product, petrol stations compete almost entirely on location and price rather than on the quality of the fuel itself."
                            },
                            {
                                "targetVocab": "concentration",
                                "prompt": "Dùng từ 'concentration' để viết một câu về xu hướng tập trung thị phần trong ngành công nghệ. Ví dụ: The increasing concentration in the social media industry means that three platforms now capture over eighty percent of all digital advertising revenue."
                            },
                            {
                                "targetVocab": "merger",
                                "prompt": "Dùng từ 'merger' để viết một câu về một vụ sáp nhập và phản ứng của cơ quan quản lý. Ví dụ: The proposed merger between the two largest ride-hailing companies was blocked by regulators who feared it would eliminate competition and raise fares for passengers."
                            },
                            {
                                "targetVocab": "antitrust",
                                "prompt": "Dùng từ 'antitrust' để viết một câu về một vụ kiện chống độc quyền nổi tiếng. Ví dụ: The landmark antitrust case against the software giant resulted in the company being forced to share its operating system code with competitors."
                            },
                            {
                                "targetVocab": "regulation",
                                "prompt": "Dùng từ 'regulation' để viết một câu về tác động của quy định đến hoạt động kinh doanh. Ví dụ: Tighter regulation on food labeling has forced manufacturers to clearly list all ingredients and allergens on their packaging."
                            },
                            {
                                "targetVocab": "cartel",
                                "prompt": "Dùng từ 'cartel' để viết một câu về hậu quả khi một cartel bị phát hiện. Ví dụ: When the shipping cartel was uncovered, the participating companies were fined a combined total of over one billion dollars for fixing freight rates."
                            },
                            {
                                "targetVocab": "collusion",
                                "prompt": "Dùng từ 'collusion' để viết một câu về cách phát hiện hành vi thông đồng giữa các doanh nghiệp. Ví dụ: Investigators discovered collusion among the bidding companies when they noticed that the losing bids were always exactly five percent higher than the winning one."
                            },
                            {
                                "targetVocab": "duopoly",
                                "prompt": "Dùng từ 'duopoly' để viết một câu về cách hai doanh nghiệp chi phối một thị trường cụ thể. Ví dụ: The credit card processing market is largely a duopoly, with Visa and Mastercard handling the vast majority of electronic payment transactions globally."
                            },
                            {
                                "targetVocab": "contestable",
                                "prompt": "Dùng từ 'contestable' để viết một câu về thị trường mà đối thủ mới có thể dễ dàng gia nhập. Ví dụ: The online tutoring market is highly contestable because any qualified teacher with a laptop and internet connection can start offering lessons immediately."
                            },
                            {
                                "targetVocab": "dominance",
                                "prompt": "Dùng từ 'dominance' để viết một câu về cách một doanh nghiệp duy trì vị thế thống trị. Ví dụ: The company maintains its dominance in the streaming market by investing billions of dollars each year in original content that competitors cannot match."
                            },
                            {
                                "targetVocab": "deregulation",
                                "prompt": "Dùng từ 'deregulation' để viết một câu về tác động của tự do hóa đến một ngành cụ thể. Ví dụ: The deregulation of the airline industry in Vietnam opened the door for budget carriers, giving millions of travelers access to affordable domestic flights for the first time."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về cấu trúc thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về cấu trúc thị trường — từ cạnh tranh hoàn hảo "
                            "đến độc quyền, từ sáp nhập đến tự do hóa.\n\n"
                            "Bạn sẽ gặp lại monopoly, oligopoly, competition, barrier, market, industry "
                            "trong phần mở đầu về các loại cấu trúc thị trường. "
                            "Tiếp theo, differentiation, homogeneous, concentration, merger, antitrust, regulation "
                            "sẽ giúp bạn hiểu cách doanh nghiệp cạnh tranh và chính phủ kiểm soát. "
                            "Và cuối cùng, cartel, collusion, duopoly, contestable, dominance, deregulation "
                            "sẽ đưa bạn vào thế giới của quyền lực thị trường và chính sách cạnh tranh.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cấu trúc thị trường — Bức tranh toàn cảnh",
                    "description": "Imagine walking down a busy street in any Vietnamese city. On one side, you see dozens of small pho restaurants.",
                    "data": {
                        "text": (
                            "Imagine walking down a busy street in any Vietnamese city. "
                            "On one side, you see dozens of small pho restaurants, each trying to attract customers "
                            "with slightly different recipes, lower prices, or friendlier service. "
                            "On the other side, there is a single electricity company — "
                            "you have no choice but to buy power from them. "
                            "These two scenes capture the essence of market structures: "
                            "the way an industry is organized determines how firms behave, "
                            "how prices are set, and how much choice consumers have.\n\n"
                            "Economists classify markets into several structures based on the number of firms, "
                            "the type of product, and the ease of entry. "
                            "At one end of the spectrum is perfect competition — a market with many sellers "
                            "offering homogeneous products. In such a market, no single firm has the power to set prices. "
                            "Agricultural commodities like unprocessed rice come close to this model. "
                            "Competition is intense, and firms survive only by being efficient.\n\n"
                            "At the opposite end is a monopoly — a single firm that controls the entire market. "
                            "Monopolies arise when barriers to entry are so high that no other firm can compete. "
                            "These barriers may include enormous startup costs, exclusive access to raw materials, "
                            "or government-granted licenses. The electricity industry in many countries "
                            "is a natural monopoly because building duplicate power grids would be wasteful.\n\n"
                            "Between these extremes lies the oligopoly, where a small number of large firms dominate. "
                            "The global smartphone market is a clear example — a handful of companies "
                            "account for the vast majority of sales. In an oligopoly, firms are interdependent: "
                            "each company's pricing and production decisions depend on what its rivals do. "
                            "A special case is the duopoly, where exactly two firms share the market. "
                            "Boeing and Airbus in commercial aviation illustrate this structure perfectly.\n\n"
                            "How firms compete within these structures varies widely. "
                            "In markets with homogeneous products, price is the only weapon. "
                            "But in markets where differentiation is possible, firms invest heavily "
                            "in branding, design, and customer experience to make their products stand out. "
                            "A coffee chain that roasts its own beans and creates a unique atmosphere "
                            "can charge more than a street vendor selling the same basic drink.\n\n"
                            "The level of concentration in a market — how much of total sales "
                            "the largest firms control — is a key indicator of market power. "
                            "High concentration often means less competition and higher prices for consumers. "
                            "One way concentration increases is through mergers. "
                            "When two large firms in the same industry combine, "
                            "the number of competitors shrinks and the merged company gains greater market power.\n\n"
                            "This is why governments enforce antitrust laws. "
                            "Antitrust regulation aims to prevent any single firm from achieving "
                            "unchecked dominance over a market. Regulators review proposed mergers, "
                            "investigate anti-competitive practices, and can break up companies "
                            "that abuse their market position. "
                            "The goal is not to punish success but to ensure that competition remains alive.\n\n"
                            "Sometimes, firms try to avoid competition altogether through collusion. "
                            "When rival companies secretly agree to fix prices or divide markets, "
                            "they form a cartel. Cartels harm consumers by keeping prices artificially high. "
                            "Although cartels are illegal in most countries, they still emerge — "
                            "particularly in industries with few players and homogeneous products "
                            "where the temptation to cooperate is strong.\n\n"
                            "Yet not all concentrated markets are harmful. "
                            "The theory of contestable markets shows that even a market with one or two firms "
                            "can behave competitively if barriers to entry are low. "
                            "When potential competitors can enter quickly and cheaply, "
                            "existing firms dare not raise prices too high for fear of attracting new rivals. "
                            "The threat of entry, not just actual competition, disciplines the market.\n\n"
                            "Government policy plays a crucial role in shaping market structures. "
                            "Regulation can protect consumers from monopoly abuse, "
                            "ensure product safety, and maintain fair competition. "
                            "But too much regulation can also stifle innovation and raise costs. "
                            "This is why some governments pursue deregulation — "
                            "removing rules that are no longer necessary to let markets operate more freely. "
                            "The deregulation of airlines in many countries led to the rise of budget carriers "
                            "and dramatically lower ticket prices.\n\n"
                            "Understanding market structures is not just an academic exercise. "
                            "Every time you choose between brands, every time a government approves or blocks a merger, "
                            "every time a new startup challenges an established giant — "
                            "the forces of competition, concentration, and regulation are at work. "
                            "These 18 words give you the vocabulary to read, analyze, and discuss "
                            "how industries are organized and why it matters for everyone."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cấu trúc thị trường — Bức tranh toàn cảnh",
                    "description": "Imagine walking down a busy street in any Vietnamese city. On one side, you see dozens of small pho restaurants.",
                    "data": {
                        "text": (
                            "Imagine walking down a busy street in any Vietnamese city. "
                            "On one side, you see dozens of small pho restaurants, each trying to attract customers "
                            "with slightly different recipes, lower prices, or friendlier service. "
                            "On the other side, there is a single electricity company — "
                            "you have no choice but to buy power from them. "
                            "These two scenes capture the essence of market structures: "
                            "the way an industry is organized determines how firms behave, "
                            "how prices are set, and how much choice consumers have.\n\n"
                            "Economists classify markets into several structures based on the number of firms, "
                            "the type of product, and the ease of entry. "
                            "At one end of the spectrum is perfect competition — a market with many sellers "
                            "offering homogeneous products. In such a market, no single firm has the power to set prices. "
                            "Agricultural commodities like unprocessed rice come close to this model. "
                            "Competition is intense, and firms survive only by being efficient.\n\n"
                            "At the opposite end is a monopoly — a single firm that controls the entire market. "
                            "Monopolies arise when barriers to entry are so high that no other firm can compete. "
                            "These barriers may include enormous startup costs, exclusive access to raw materials, "
                            "or government-granted licenses. The electricity industry in many countries "
                            "is a natural monopoly because building duplicate power grids would be wasteful.\n\n"
                            "Between these extremes lies the oligopoly, where a small number of large firms dominate. "
                            "The global smartphone market is a clear example — a handful of companies "
                            "account for the vast majority of sales. In an oligopoly, firms are interdependent: "
                            "each company's pricing and production decisions depend on what its rivals do. "
                            "A special case is the duopoly, where exactly two firms share the market. "
                            "Boeing and Airbus in commercial aviation illustrate this structure perfectly.\n\n"
                            "How firms compete within these structures varies widely. "
                            "In markets with homogeneous products, price is the only weapon. "
                            "But in markets where differentiation is possible, firms invest heavily "
                            "in branding, design, and customer experience to make their products stand out. "
                            "A coffee chain that roasts its own beans and creates a unique atmosphere "
                            "can charge more than a street vendor selling the same basic drink.\n\n"
                            "The level of concentration in a market — how much of total sales "
                            "the largest firms control — is a key indicator of market power. "
                            "High concentration often means less competition and higher prices for consumers. "
                            "One way concentration increases is through mergers. "
                            "When two large firms in the same industry combine, "
                            "the number of competitors shrinks and the merged company gains greater market power.\n\n"
                            "This is why governments enforce antitrust laws. "
                            "Antitrust regulation aims to prevent any single firm from achieving "
                            "unchecked dominance over a market. Regulators review proposed mergers, "
                            "investigate anti-competitive practices, and can break up companies "
                            "that abuse their market position. "
                            "The goal is not to punish success but to ensure that competition remains alive.\n\n"
                            "Sometimes, firms try to avoid competition altogether through collusion. "
                            "When rival companies secretly agree to fix prices or divide markets, "
                            "they form a cartel. Cartels harm consumers by keeping prices artificially high. "
                            "Although cartels are illegal in most countries, they still emerge — "
                            "particularly in industries with few players and homogeneous products "
                            "where the temptation to cooperate is strong.\n\n"
                            "Yet not all concentrated markets are harmful. "
                            "The theory of contestable markets shows that even a market with one or two firms "
                            "can behave competitively if barriers to entry are low. "
                            "When potential competitors can enter quickly and cheaply, "
                            "existing firms dare not raise prices too high for fear of attracting new rivals. "
                            "The threat of entry, not just actual competition, disciplines the market.\n\n"
                            "Government policy plays a crucial role in shaping market structures. "
                            "Regulation can protect consumers from monopoly abuse, "
                            "ensure product safety, and maintain fair competition. "
                            "But too much regulation can also stifle innovation and raise costs. "
                            "This is why some governments pursue deregulation — "
                            "removing rules that are no longer necessary to let markets operate more freely. "
                            "The deregulation of airlines in many countries led to the rise of budget carriers "
                            "and dramatically lower ticket prices.\n\n"
                            "Understanding market structures is not just an academic exercise. "
                            "Every time you choose between brands, every time a government approves or blocks a merger, "
                            "every time a new startup challenges an established giant — "
                            "the forces of competition, concentration, and regulation are at work. "
                            "These 18 words give you the vocabulary to read, analyze, and discuss "
                            "how industries are organized and why it matters for everyone."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cấu trúc thị trường — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine walking down a busy street in any Vietnamese city. "
                            "On one side, you see dozens of small pho restaurants, each trying to attract customers "
                            "with slightly different recipes, lower prices, or friendlier service. "
                            "On the other side, there is a single electricity company — "
                            "you have no choice but to buy power from them. "
                            "These two scenes capture the essence of market structures: "
                            "the way an industry is organized determines how firms behave, "
                            "how prices are set, and how much choice consumers have.\n\n"
                            "Economists classify markets into several structures based on the number of firms, "
                            "the type of product, and the ease of entry. "
                            "At one end of the spectrum is perfect competition — a market with many sellers "
                            "offering homogeneous products. In such a market, no single firm has the power to set prices. "
                            "Agricultural commodities like unprocessed rice come close to this model. "
                            "Competition is intense, and firms survive only by being efficient.\n\n"
                            "At the opposite end is a monopoly — a single firm that controls the entire market. "
                            "Monopolies arise when barriers to entry are so high that no other firm can compete. "
                            "These barriers may include enormous startup costs, exclusive access to raw materials, "
                            "or government-granted licenses. The electricity industry in many countries "
                            "is a natural monopoly because building duplicate power grids would be wasteful.\n\n"
                            "Between these extremes lies the oligopoly, where a small number of large firms dominate. "
                            "The global smartphone market is a clear example — a handful of companies "
                            "account for the vast majority of sales. In an oligopoly, firms are interdependent: "
                            "each company's pricing and production decisions depend on what its rivals do. "
                            "A special case is the duopoly, where exactly two firms share the market. "
                            "Boeing and Airbus in commercial aviation illustrate this structure perfectly.\n\n"
                            "How firms compete within these structures varies widely. "
                            "In markets with homogeneous products, price is the only weapon. "
                            "But in markets where differentiation is possible, firms invest heavily "
                            "in branding, design, and customer experience to make their products stand out. "
                            "A coffee chain that roasts its own beans and creates a unique atmosphere "
                            "can charge more than a street vendor selling the same basic drink.\n\n"
                            "The level of concentration in a market — how much of total sales "
                            "the largest firms control — is a key indicator of market power. "
                            "High concentration often means less competition and higher prices for consumers. "
                            "One way concentration increases is through mergers. "
                            "When two large firms in the same industry combine, "
                            "the number of competitors shrinks and the merged company gains greater market power.\n\n"
                            "This is why governments enforce antitrust laws. "
                            "Antitrust regulation aims to prevent any single firm from achieving "
                            "unchecked dominance over a market. Regulators review proposed mergers, "
                            "investigate anti-competitive practices, and can break up companies "
                            "that abuse their market position. "
                            "The goal is not to punish success but to ensure that competition remains alive.\n\n"
                            "Sometimes, firms try to avoid competition altogether through collusion. "
                            "When rival companies secretly agree to fix prices or divide markets, "
                            "they form a cartel. Cartels harm consumers by keeping prices artificially high. "
                            "Although cartels are illegal in most countries, they still emerge — "
                            "particularly in industries with few players and homogeneous products "
                            "where the temptation to cooperate is strong.\n\n"
                            "Yet not all concentrated markets are harmful. "
                            "The theory of contestable markets shows that even a market with one or two firms "
                            "can behave competitively if barriers to entry are low. "
                            "When potential competitors can enter quickly and cheaply, "
                            "existing firms dare not raise prices too high for fear of attracting new rivals. "
                            "The threat of entry, not just actual competition, disciplines the market.\n\n"
                            "Government policy plays a crucial role in shaping market structures. "
                            "Regulation can protect consumers from monopoly abuse, "
                            "ensure product safety, and maintain fair competition. "
                            "But too much regulation can also stifle innovation and raise costs. "
                            "This is why some governments pursue deregulation — "
                            "removing rules that are no longer necessary to let markets operate more freely. "
                            "The deregulation of airlines in many countries led to the rise of budget carriers "
                            "and dramatically lower ticket prices.\n\n"
                            "Understanding market structures is not just an academic exercise. "
                            "Every time you choose between brands, every time a government approves or blocks a merger, "
                            "every time a new startup challenges an established giant — "
                            "the forces of competition, concentration, and regulation are at work. "
                            "These 18 words give you the vocabulary to read, analyze, and discuss "
                            "how industries are organized and why it matters for everyone."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích cấu trúc thị trường",
                    "description": "Viết đoạn văn tiếng Anh phân tích về cấu trúc thị trường sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["monopoly", "oligopoly", "competition", "barrier", "market", "industry", "differentiation", "homogeneous", "concentration", "merger", "antitrust", "regulation", "cartel", "collusion", "duopoly", "contestable", "dominance", "deregulation"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích cấu trúc của một ngành kinh tế cụ thể. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích cấu trúc thị trường của ngành viễn thông tại Việt Nam. Đây là monopoly, oligopoly, hay thị trường cạnh tranh? Giải thích các barrier to entry, mức độ concentration, và vai trò của regulation trong việc kiểm soát quyền lực thị trường của các nhà mạng lớn.",
                            "Hãy so sánh hai ngành: ngành hàng không (airline industry) và ngành quán cà phê (coffee shop industry). Ngành nào có concentration cao hơn? Ngành nào contestable hơn? Giải thích vì sao merger trong ngành hàng không thường bị antitrust authorities xem xét kỹ hơn so với ngành cà phê."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần trách nhiệm ấm áp.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học về Cấu trúc thị trường. "
                            "Nhưng đừng vội đóng sách lại — hãy tự hỏi: bạn sẽ làm gì với những gì vừa học?\n\n"
                            "Kiến thức chỉ có giá trị khi bạn sử dụng nó. "
                            "Và 18 từ vựng bạn vừa học không phải để ghi nhớ rồi quên — "
                            "chúng là công cụ để bạn đọc, phân tích, và tranh luận về thế giới kinh tế xung quanh. "
                            "Hãy cùng ôn lại một số từ quan trọng nhất, "
                            "và lần này, hãy nghĩ xem bạn sẽ dùng chúng ở đâu trong tuần tới.\n\n"
                            "Oligopoly — thị trường thiểu số. Lần tới khi bạn đổ xăng và thấy giá ở mọi cây xăng "
                            "gần như giống nhau, hãy tự hỏi: đây có phải là oligopoly không? "
                            "Các công ty xăng dầu có đang theo dõi nhau để định giá không? "
                            "Ví dụ mới: The Vietnamese banking sector operates as an oligopoly "
                            "where the four largest state-owned banks control over fifty percent of total deposits.\n\n"
                            "Barrier — rào cản. Nếu bạn từng nghĩ đến việc khởi nghiệp, "
                            "bạn đã gặp barrier rồi đấy — vốn, giấy phép, mối quan hệ, công nghệ. "
                            "Hiểu barrier giúp bạn biết ngành nào dễ gia nhập và ngành nào cần chuẩn bị kỹ. "
                            "Ví dụ mới: The high cost of research and development creates a formidable barrier "
                            "that keeps small startups out of the biotechnology industry.\n\n"
                            "Antitrust — chống độc quyền. Mỗi khi đọc tin về một vụ sáp nhập lớn bị chặn, "
                            "bạn sẽ biết đó là antitrust đang hoạt động. "
                            "Luật chống độc quyền tồn tại để bảo vệ bạn — người tiêu dùng. "
                            "Ví dụ mới: The antitrust investigation revealed that the dominant platform "
                            "had been secretly favoring its own products in search results over those of independent sellers.\n\n"
                            "Collusion — thông đồng. Đây là từ bạn sẽ gặp trong tin tức kinh tế quốc tế. "
                            "Khi các công ty bắt tay nhau thay vì cạnh tranh, người thiệt thòi là bạn. "
                            "Ví dụ mới: The court found evidence of collusion when internal documents showed "
                            "that the three largest suppliers had coordinated their price increases on the same dates.\n\n"
                            "Contestable — có thể bị thách thức. Đây là từ mang lại hy vọng. "
                            "Ngay cả khi thị trường chỉ có một vài ông lớn, "
                            "nếu đối thủ mới có thể gia nhập dễ dàng, cạnh tranh vẫn tồn tại. "
                            "Ví dụ mới: The cloud computing market remains contestable "
                            "because new providers can scale up quickly using leased infrastructure "
                            "without building their own data centers.\n\n"
                            "Deregulation — tự do hóa. Khi chính phủ gỡ bỏ quy định, "
                            "thị trường có thể trở nên sôi động hơn — nhưng cũng rủi ro hơn. "
                            "Hiểu deregulation giúp bạn đánh giá chính sách kinh tế một cách có chiều sâu. "
                            "Ví dụ mới: The deregulation of electricity markets in several European countries "
                            "allowed consumers to choose their energy provider for the first time, "
                            "driving prices down through increased competition.\n\n"
                            "Bây giờ, đây là thử thách dành cho bạn. "
                            "Trong tuần tới, hãy đọc một bài báo tiếng Anh về kinh tế — "
                            "có thể là về một vụ sáp nhập, một cuộc điều tra chống độc quyền, "
                            "hoặc một ngành đang được tự do hóa. "
                            "Đếm xem bạn nhận ra bao nhiêu từ trong 18 từ đã học. "
                            "Nếu bạn nhận ra được 5 từ trở lên, bạn đã thực sự nắm vững bài học này.\n\n"
                            "Học từ vựng không phải là đích đến — nó là điểm khởi đầu. "
                            "Bạn đã có công cụ. Bây giờ hãy dùng nó.\n\n"
                            "Chúc bạn tiếp tục hành trình học tập đầy quyết tâm. "
                            "Hẹn gặp lại bạn ở bài học tiếp theo!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Market Structures – Cấu Trúc Thị Trường' AND uid = '{UID}' ORDER BY created_at;")
