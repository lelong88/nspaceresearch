"""
Create curriculum: Economic Growth – Tăng Trưởng Kinh Tế
Series B — Kinh Tế Vĩ Mô (Macroeconomics), curriculum #5
18 words | 5 sessions | provocative_question tone | team-building energy farewell
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
W1 = ["growth", "development", "investment", "capital", "infrastructure", "innovation"]
W2 = ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"]
W3 = ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Economic Growth – Tăng Trưởng Kinh Tế",
    "contentTypeTags": [],
    "description": (
        "TẠI SAO CÓ NƯỚC GIÀU LÊN THẦN TỐC, CÒN NƯỚC KHÁC MÃI GIẬM CHÂN TẠI CHỖ?\n\n"
        "Việt Nam tăng trưởng GDP trung bình 6-7% mỗi năm suốt hai thập kỷ — nhưng bạn có thật sự hiểu "
        "điều gì đang kéo nền kinh tế đi lên? Là investment đổ vào nhà máy, là infrastructure kết nối "
        "thành thị với nông thôn, hay là innovation từ những startup công nghệ? "
        "Và tại sao có quốc gia cùng xuất phát điểm lại rơi vào stagnation?\n\n"
        "Hãy hình dung nền kinh tế như một chiếc xe đua — capital là động cơ, human capital là tay lái, "
        "và institutional reform là đường đua. Thiếu một trong ba, chiếc xe không thể về đích. "
        "Bạn cần đọc được bản đồ tăng trưởng bằng tiếng Anh để hiểu cuộc đua này.\n\n"
        "Sau khóa học, bạn sẽ tự tin đọc báo cáo World Bank về emerging economies, "
        "phân tích convergence và divergence giữa các quốc gia, "
        "và viết được những đoạn phân tích sắc bén về sustainable development bằng tiếng Anh chuyên ngành.\n\n"
        "18 từ vựng — từ growth đến stagnation — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kinh tế vĩ mô, vừa nâng trình tiếng Anh học thuật một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về tăng trưởng và phát triển kinh tế — "
            "chủ đề trung tâm của kinh tế vĩ mô hiện đại. "
            "Bạn sẽ bắt đầu với growth, development, investment, capital, infrastructure, innovation — "
            "những động lực chính đưa một quốc gia từ nghèo đến giàu. "
            "Tiếp theo là convergence, divergence, sustainable, emerging, industrialization, urbanization — "
            "những từ giúp bạn so sánh quỹ đạo phát triển giữa các nền kinh tế. "
            "Cuối cùng, productivity, human, institutional, reform, liberalization, stagnation "
            "đưa bạn vào thế giới chính sách và thể chế — nơi quyết định một quốc gia thịnh vượng hay trì trệ. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tài liệu về economic growth bằng tiếng Anh — "
            "từ giáo trình đại học đến báo cáo của World Bank."
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
                    "description": "Chào mừng bạn đến với bài học về tăng trưởng kinh tế — động lực phát triển quốc gia.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học cuối cùng trong chuỗi Kinh tế vĩ mô — "
                            "chủ đề hôm nay là Tăng trưởng kinh tế, hay trong tiếng Anh là Economic Growth. "
                            "Đây là câu hỏi lớn nhất của kinh tế học: tại sao có quốc gia giàu và có quốc gia nghèo? "
                            "Điều gì khiến một nền kinh tế tăng trưởng bền vững qua nhiều thập kỷ?\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: growth, development, investment, capital, "
                            "infrastructure, và innovation. Đây là những từ bạn sẽ gặp trong mọi cuộc thảo luận "
                            "về phát triển kinh tế — từ giáo trình đại học đến báo cáo của World Bank.\n\n"
                            "Từ đầu tiên là growth — danh từ — nghĩa là tăng trưởng, "
                            "sự gia tăng sản lượng hàng hóa và dịch vụ của một nền kinh tế theo thời gian. "
                            "Ví dụ: 'Vietnam has achieved impressive economic growth over the past two decades, "
                            "averaging around six to seven percent per year.' "
                            "Trong bài đọc, growth được dùng để mô tả tốc độ mở rộng của nền kinh tế — "
                            "thường đo bằng tỷ lệ tăng GDP.\n\n"
                            "Từ thứ hai là development — danh từ — nghĩa là phát triển, "
                            "quá trình cải thiện toàn diện đời sống kinh tế, xã hội và con người của một quốc gia. "
                            "Ví dụ: 'Economic development includes not only higher incomes but also better education, "
                            "healthcare, and living standards for all citizens.' "
                            "Trong bài đọc, development rộng hơn growth — growth chỉ đo sản lượng, "
                            "còn development bao gồm cả chất lượng cuộc sống.\n\n"
                            "Từ thứ ba là investment — danh từ — nghĩa là đầu tư, "
                            "việc bỏ tiền vào máy móc, nhà xưởng, công nghệ hoặc giáo dục để tạo ra giá trị trong tương lai. "
                            "Ví dụ: 'Foreign direct investment in Vietnam's manufacturing sector has created millions of jobs "
                            "and boosted export revenues.' "
                            "Trong bài đọc, investment là động lực chính của tăng trưởng — "
                            "không có đầu tư, nền kinh tế không thể mở rộng năng lực sản xuất.\n\n"
                            "Từ thứ tư là capital — danh từ — nghĩa là vốn, "
                            "tài sản được sử dụng để sản xuất hàng hóa và dịch vụ, bao gồm máy móc, nhà xưởng và tiền. "
                            "Ví dụ: 'A country needs both physical capital like factories and human capital like skilled workers "
                            "to sustain long-term growth.' "
                            "Trong bài đọc, capital xuất hiện ở nhiều dạng — physical capital là máy móc, "
                            "human capital là kỹ năng và kiến thức của người lao động.\n\n"
                            "Từ thứ năm là infrastructure — danh từ — nghĩa là cơ sở hạ tầng, "
                            "hệ thống đường sá, cầu cống, điện, nước, viễn thông phục vụ nền kinh tế. "
                            "Ví dụ: 'Investing in infrastructure such as highways and ports helps reduce transportation costs "
                            "and connect rural areas to urban markets.' "
                            "Trong bài đọc, infrastructure là nền tảng vật chất cho tăng trưởng — "
                            "không có đường tốt, hàng hóa không thể lưu thông.\n\n"
                            "Từ cuối cùng là innovation — danh từ — nghĩa là đổi mới sáng tạo, "
                            "việc tạo ra sản phẩm, quy trình hoặc công nghệ mới giúp nâng cao năng suất. "
                            "Ví dụ: 'Innovation in mobile banking has allowed millions of people in developing countries "
                            "to access financial services for the first time.' "
                            "Trong bài đọc, innovation là yếu tố phân biệt giữa tăng trưởng ngắn hạn "
                            "và tăng trưởng bền vững dài hạn.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về các động lực tăng trưởng kinh tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Động lực tăng trưởng kinh tế",
                    "description": "Học 6 từ: growth, development, investment, capital, infrastructure, innovation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Động lực tăng trưởng kinh tế",
                    "description": "Học 6 từ: growth, development, investment, capital, infrastructure, innovation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Động lực tăng trưởng kinh tế",
                    "description": "Học 6 từ: growth, development, investment, capital, infrastructure, innovation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Động lực tăng trưởng kinh tế",
                    "description": "Học 6 từ: growth, development, investment, capital, infrastructure, innovation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Động lực tăng trưởng kinh tế",
                    "description": "Học 6 từ: growth, development, investment, capital, infrastructure, innovation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Động lực tăng trưởng kinh tế",
                    "description": "Why do some countries grow rich while others remain poor?",
                    "data": {
                        "text": (
                            "Why do some countries grow rich while others remain poor? "
                            "This is one of the most important questions in economics. "
                            "The answer lies in understanding the forces that drive economic growth.\n\n"
                            "Growth refers to the increase in a country's total output of goods and services over time. "
                            "Economists usually measure growth by looking at changes in gross domestic product. "
                            "When GDP rises year after year, the economy is growing. "
                            "But growth alone does not tell the whole story. "
                            "Development is a broader concept that includes improvements in education, health, "
                            "and the overall quality of life. A country can have high growth rates "
                            "but still lag behind in development if the benefits do not reach all citizens.\n\n"
                            "One of the most powerful engines of growth is investment. "
                            "When businesses invest in new factories, machines, and technology, "
                            "they increase the economy's capacity to produce goods. "
                            "Foreign direct investment has played a major role in Vietnam's transformation. "
                            "Companies from South Korea, Japan, and other countries have built manufacturing plants "
                            "that employ hundreds of thousands of workers and generate billions in exports.\n\n"
                            "Investment creates capital — the tools, equipment, and structures used in production. "
                            "Physical capital includes everything from assembly lines in factories to computers in offices. "
                            "The more capital an economy has, the more it can produce per worker. "
                            "But capital alone is not enough. Workers need skills and knowledge to use it effectively.\n\n"
                            "Infrastructure is another critical ingredient. "
                            "Roads, bridges, ports, power plants, and internet networks form the backbone of a modern economy. "
                            "Without reliable infrastructure, businesses cannot move goods to market, "
                            "factories cannot operate efficiently, and rural communities remain isolated. "
                            "Vietnam has invested heavily in infrastructure over the past two decades, "
                            "building expressways, expanding airports, and improving electricity access across the country.\n\n"
                            "Finally, innovation is what separates countries that grow steadily from those that leap ahead. "
                            "Innovation means creating new products, new processes, or new ways of organizing work. "
                            "It is the reason why a smartphone today is more powerful than a room-sized computer from fifty years ago. "
                            "Countries that invest in research and development, support entrepreneurs, "
                            "and protect intellectual property tend to innovate more — and grow faster as a result."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Động lực tăng trưởng kinh tế",
                    "description": "Why do some countries grow rich while others remain poor?",
                    "data": {
                        "text": (
                            "Why do some countries grow rich while others remain poor? "
                            "This is one of the most important questions in economics. "
                            "The answer lies in understanding the forces that drive economic growth.\n\n"
                            "Growth refers to the increase in a country's total output of goods and services over time. "
                            "Economists usually measure growth by looking at changes in gross domestic product. "
                            "When GDP rises year after year, the economy is growing. "
                            "But growth alone does not tell the whole story. "
                            "Development is a broader concept that includes improvements in education, health, "
                            "and the overall quality of life. A country can have high growth rates "
                            "but still lag behind in development if the benefits do not reach all citizens.\n\n"
                            "One of the most powerful engines of growth is investment. "
                            "When businesses invest in new factories, machines, and technology, "
                            "they increase the economy's capacity to produce goods. "
                            "Foreign direct investment has played a major role in Vietnam's transformation. "
                            "Companies from South Korea, Japan, and other countries have built manufacturing plants "
                            "that employ hundreds of thousands of workers and generate billions in exports.\n\n"
                            "Investment creates capital — the tools, equipment, and structures used in production. "
                            "Physical capital includes everything from assembly lines in factories to computers in offices. "
                            "The more capital an economy has, the more it can produce per worker. "
                            "But capital alone is not enough. Workers need skills and knowledge to use it effectively.\n\n"
                            "Infrastructure is another critical ingredient. "
                            "Roads, bridges, ports, power plants, and internet networks form the backbone of a modern economy. "
                            "Without reliable infrastructure, businesses cannot move goods to market, "
                            "factories cannot operate efficiently, and rural communities remain isolated. "
                            "Vietnam has invested heavily in infrastructure over the past two decades, "
                            "building expressways, expanding airports, and improving electricity access across the country.\n\n"
                            "Finally, innovation is what separates countries that grow steadily from those that leap ahead. "
                            "Innovation means creating new products, new processes, or new ways of organizing work. "
                            "It is the reason why a smartphone today is more powerful than a room-sized computer from fifty years ago. "
                            "Countries that invest in research and development, support entrepreneurs, "
                            "and protect intellectual property tend to innovate more — and grow faster as a result."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Động lực tăng trưởng kinh tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Why do some countries grow rich while others remain poor? "
                            "This is one of the most important questions in economics. "
                            "The answer lies in understanding the forces that drive economic growth.\n\n"
                            "Growth refers to the increase in a country's total output of goods and services over time. "
                            "Economists usually measure growth by looking at changes in gross domestic product. "
                            "When GDP rises year after year, the economy is growing. "
                            "But growth alone does not tell the whole story. "
                            "Development is a broader concept that includes improvements in education, health, "
                            "and the overall quality of life. A country can have high growth rates "
                            "but still lag behind in development if the benefits do not reach all citizens.\n\n"
                            "One of the most powerful engines of growth is investment. "
                            "When businesses invest in new factories, machines, and technology, "
                            "they increase the economy's capacity to produce goods. "
                            "Foreign direct investment has played a major role in Vietnam's transformation. "
                            "Companies from South Korea, Japan, and other countries have built manufacturing plants "
                            "that employ hundreds of thousands of workers and generate billions in exports.\n\n"
                            "Investment creates capital — the tools, equipment, and structures used in production. "
                            "Physical capital includes everything from assembly lines in factories to computers in offices. "
                            "The more capital an economy has, the more it can produce per worker. "
                            "But capital alone is not enough. Workers need skills and knowledge to use it effectively.\n\n"
                            "Infrastructure is another critical ingredient. "
                            "Roads, bridges, ports, power plants, and internet networks form the backbone of a modern economy. "
                            "Without reliable infrastructure, businesses cannot move goods to market, "
                            "factories cannot operate efficiently, and rural communities remain isolated. "
                            "Vietnam has invested heavily in infrastructure over the past two decades, "
                            "building expressways, expanding airports, and improving electricity access across the country.\n\n"
                            "Finally, innovation is what separates countries that grow steadily from those that leap ahead. "
                            "Innovation means creating new products, new processes, or new ways of organizing work. "
                            "It is the reason why a smartphone today is more powerful than a room-sized computer from fifty years ago. "
                            "Countries that invest in research and development, support entrepreneurs, "
                            "and protect intellectual property tend to innovate more — and grow faster as a result."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Động lực tăng trưởng kinh tế",
                    "description": "Viết câu sử dụng 6 từ vựng về tăng trưởng kinh tế.",
                    "data": {
                        "vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation"],
                        "items": [
                            {
                                "targetVocab": "growth",
                                "prompt": "Dùng từ 'growth' để viết một câu về tốc độ tăng trưởng kinh tế của một quốc gia trong khu vực Đông Nam Á. Ví dụ: Vietnam's economic growth has averaged over six percent annually, making it one of the fastest-growing economies in Southeast Asia."
                            },
                            {
                                "targetVocab": "development",
                                "prompt": "Dùng từ 'development' để viết một câu về sự khác biệt giữa tăng trưởng kinh tế và phát triển toàn diện. Ví dụ: True economic development requires not just rising GDP but also improvements in healthcare, education, and environmental protection."
                            },
                            {
                                "targetVocab": "investment",
                                "prompt": "Dùng từ 'investment' để viết một câu về vai trò của đầu tư nước ngoài trong việc tạo việc làm. Ví dụ: Foreign investment in the electronics sector has created thousands of well-paying jobs in industrial zones across northern Vietnam."
                            },
                            {
                                "targetVocab": "capital",
                                "prompt": "Dùng từ 'capital' để viết một câu về tầm quan trọng của vốn trong quá trình sản xuất. Ví dụ: Small businesses often struggle to grow because they lack the capital needed to purchase modern equipment and expand their operations."
                            },
                            {
                                "targetVocab": "infrastructure",
                                "prompt": "Dùng từ 'infrastructure' để viết một câu về tác động của cơ sở hạ tầng đến phát triển kinh tế vùng nông thôn. Ví dụ: Building better infrastructure in rural areas, such as paved roads and reliable electricity, helps farmers bring their products to market more efficiently."
                            },
                            {
                                "targetVocab": "innovation",
                                "prompt": "Dùng từ 'innovation' để viết một câu về vai trò của đổi mới sáng tạo trong nền kinh tế số. Ví dụ: Innovation in financial technology has enabled millions of Vietnamese consumers to make cashless payments using just their smartphones."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về hội tụ, phân kỳ và quá trình công nghiệp hóa.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "growth — tăng trưởng, development — phát triển, investment — đầu tư, "
                            "capital — vốn, infrastructure — cơ sở hạ tầng, và innovation — đổi mới sáng tạo. "
                            "Bạn đã hiểu những động lực chính đưa một nền kinh tế đi lên. "
                            "Bây giờ, chúng ta sẽ nhìn rộng hơn — so sánh các quốc gia với nhau.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: convergence, divergence, sustainable, emerging, "
                            "industrialization, và urbanization. Những từ này giúp bạn phân tích quỹ đạo phát triển "
                            "của các nền kinh tế — ai đang đuổi kịp, ai đang tụt lại, và quá trình chuyển đổi "
                            "từ nông nghiệp sang công nghiệp diễn ra như thế nào.\n\n"
                            "Từ đầu tiên là convergence — danh từ — nghĩa là hội tụ, "
                            "xu hướng các nước nghèo tăng trưởng nhanh hơn các nước giàu và dần thu hẹp khoảng cách. "
                            "Ví dụ: 'The convergence between China's GDP per capita and that of developed nations "
                            "has been one of the most remarkable economic stories of the twenty-first century.' "
                            "Trong bài đọc, convergence mô tả hiện tượng các nước đang phát triển "
                            "bắt kịp các nước phát triển về mức sống.\n\n"
                            "Từ thứ hai là divergence — danh từ — nghĩa là phân kỳ, "
                            "xu hướng khoảng cách giữa các nước giàu và nghèo ngày càng rộng ra. "
                            "Ví dụ: 'The divergence between sub-Saharan Africa and East Asia over the past fifty years "
                            "shows that geography and policy both matter for growth.' "
                            "Trong bài đọc, divergence là mặt đối lập của convergence — "
                            "khi một số nước phát triển nhanh trong khi những nước khác bị bỏ lại phía sau.\n\n"
                            "Từ thứ ba là sustainable — tính từ — nghĩa là bền vững, "
                            "có thể duy trì được trong dài hạn mà không làm cạn kiệt tài nguyên hoặc gây hại môi trường. "
                            "Ví dụ: 'Sustainable growth requires balancing economic expansion with environmental protection "
                            "so that future generations can also prosper.' "
                            "Trong bài đọc, sustainable nhấn mạnh rằng tăng trưởng chỉ có ý nghĩa "
                            "khi nó không phá hủy nền tảng cho tương lai.\n\n"
                            "Từ thứ tư là emerging — tính từ — nghĩa là mới nổi, "
                            "dùng để chỉ các nền kinh tế đang trong giai đoạn chuyển đổi từ thu nhập thấp sang trung bình. "
                            "Ví dụ: 'Vietnam, Indonesia, and the Philippines are considered emerging economies "
                            "because they are growing rapidly and attracting increasing foreign investment.' "
                            "Trong bài đọc, emerging mô tả nhóm quốc gia đang trên đà phát triển mạnh "
                            "nhưng chưa đạt mức thu nhập cao.\n\n"
                            "Từ thứ năm là industrialization — danh từ — nghĩa là công nghiệp hóa, "
                            "quá trình chuyển đổi nền kinh tế từ nông nghiệp sang sản xuất công nghiệp. "
                            "Ví dụ: 'Industrialization in South Korea during the nineteen sixties and seventies "
                            "transformed the country from one of the poorest in Asia to a global manufacturing powerhouse.' "
                            "Trong bài đọc, industrialization là bước ngoặt lịch sử — "
                            "khi lao động chuyển từ đồng ruộng vào nhà máy.\n\n"
                            "Từ cuối cùng là urbanization — danh từ — nghĩa là đô thị hóa, "
                            "quá trình dân cư di chuyển từ nông thôn ra thành phố. "
                            "Ví dụ: 'Rapid urbanization in Ho Chi Minh City has created both economic opportunities "
                            "and challenges such as traffic congestion and housing shortages.' "
                            "Trong bài đọc, urbanization đi đôi với industrialization — "
                            "khi nhà máy mọc lên ở thành phố, người lao động đổ về đó để tìm việc.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về hội tụ, phân kỳ và quá trình chuyển đổi kinh tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Học 6 từ: convergence, divergence, sustainable, emerging, industrialization, urbanization",
                    "data": {"vocabList": ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Học 6 từ: convergence, divergence, sustainable, emerging, industrialization, urbanization",
                    "data": {"vocabList": ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Học 6 từ: convergence, divergence, sustainable, emerging, industrialization, urbanization",
                    "data": {"vocabList": ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Học 6 từ: convergence, divergence, sustainable, emerging, industrialization, urbanization",
                    "data": {"vocabList": ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Học 6 từ: convergence, divergence, sustainable, emerging, industrialization, urbanization",
                    "data": {"vocabList": ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "In the nineteen sixties, South Korea and many countries in sub-Saharan Africa had similar levels of income per person.",
                    "data": {
                        "text": (
                            "In the nineteen sixties, South Korea and many countries in sub-Saharan Africa "
                            "had similar levels of income per person. "
                            "Today, South Korea is one of the richest nations in the world, "
                            "while many African countries still struggle with poverty. "
                            "This dramatic difference illustrates two opposing trends in the global economy: "
                            "convergence and divergence.\n\n"
                            "Convergence occurs when poorer countries grow faster than richer ones, "
                            "gradually closing the income gap. "
                            "East Asia provides the strongest evidence of convergence. "
                            "Countries like China, Vietnam, and Indonesia have grown at rates far above the global average, "
                            "lifting hundreds of millions of people out of poverty. "
                            "These emerging economies have attracted foreign investment, built modern infrastructure, "
                            "and expanded their manufacturing sectors at remarkable speed.\n\n"
                            "Divergence, on the other hand, happens when the gap between rich and poor countries widens. "
                            "Some nations in Africa and parts of South Asia have experienced slow or negative growth "
                            "for decades, falling further behind the developed world. "
                            "Conflict, weak institutions, and lack of investment are common reasons for divergence.\n\n"
                            "A key process in the growth story is industrialization — "
                            "the shift from an economy based on farming to one based on manufacturing. "
                            "When a country industrializes, workers move from low-productivity agriculture "
                            "to higher-productivity factory jobs. "
                            "Output per worker rises, wages increase, and the economy grows. "
                            "Britain was the first country to industrialize in the late seventeen hundreds. "
                            "Japan followed in the late eighteen hundreds, and South Korea in the nineteen sixties.\n\n"
                            "Industrialization almost always brings urbanization — "
                            "the movement of people from rural areas to cities. "
                            "Factories are built near ports and transportation hubs, "
                            "and workers migrate to be close to jobs. "
                            "In Vietnam, urbanization has accelerated rapidly. "
                            "Ho Chi Minh City and Hanoi have grown into major economic centers, "
                            "drawing millions of workers from the countryside.\n\n"
                            "But growth must be sustainable to last. "
                            "Sustainable growth means expanding the economy without depleting natural resources "
                            "or causing environmental damage that harms future generations. "
                            "Many emerging economies face a difficult balance: "
                            "they need rapid industrialization to reduce poverty, "
                            "but they also need to protect their rivers, forests, and air quality. "
                            "Finding this balance is one of the greatest challenges of modern development."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "In the nineteen sixties, South Korea and many countries in sub-Saharan Africa had similar levels of income per person.",
                    "data": {
                        "text": (
                            "In the nineteen sixties, South Korea and many countries in sub-Saharan Africa "
                            "had similar levels of income per person. "
                            "Today, South Korea is one of the richest nations in the world, "
                            "while many African countries still struggle with poverty. "
                            "This dramatic difference illustrates two opposing trends in the global economy: "
                            "convergence and divergence.\n\n"
                            "Convergence occurs when poorer countries grow faster than richer ones, "
                            "gradually closing the income gap. "
                            "East Asia provides the strongest evidence of convergence. "
                            "Countries like China, Vietnam, and Indonesia have grown at rates far above the global average, "
                            "lifting hundreds of millions of people out of poverty. "
                            "These emerging economies have attracted foreign investment, built modern infrastructure, "
                            "and expanded their manufacturing sectors at remarkable speed.\n\n"
                            "Divergence, on the other hand, happens when the gap between rich and poor countries widens. "
                            "Some nations in Africa and parts of South Asia have experienced slow or negative growth "
                            "for decades, falling further behind the developed world. "
                            "Conflict, weak institutions, and lack of investment are common reasons for divergence.\n\n"
                            "A key process in the growth story is industrialization — "
                            "the shift from an economy based on farming to one based on manufacturing. "
                            "When a country industrializes, workers move from low-productivity agriculture "
                            "to higher-productivity factory jobs. "
                            "Output per worker rises, wages increase, and the economy grows. "
                            "Britain was the first country to industrialize in the late seventeen hundreds. "
                            "Japan followed in the late eighteen hundreds, and South Korea in the nineteen sixties.\n\n"
                            "Industrialization almost always brings urbanization — "
                            "the movement of people from rural areas to cities. "
                            "Factories are built near ports and transportation hubs, "
                            "and workers migrate to be close to jobs. "
                            "In Vietnam, urbanization has accelerated rapidly. "
                            "Ho Chi Minh City and Hanoi have grown into major economic centers, "
                            "drawing millions of workers from the countryside.\n\n"
                            "But growth must be sustainable to last. "
                            "Sustainable growth means expanding the economy without depleting natural resources "
                            "or causing environmental damage that harms future generations. "
                            "Many emerging economies face a difficult balance: "
                            "they need rapid industrialization to reduce poverty, "
                            "but they also need to protect their rivers, forests, and air quality. "
                            "Finding this balance is one of the greatest challenges of modern development."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "In the nineteen sixties, South Korea and many countries in sub-Saharan Africa "
                            "had similar levels of income per person. "
                            "Today, South Korea is one of the richest nations in the world, "
                            "while many African countries still struggle with poverty. "
                            "This dramatic difference illustrates two opposing trends in the global economy: "
                            "convergence and divergence.\n\n"
                            "Convergence occurs when poorer countries grow faster than richer ones, "
                            "gradually closing the income gap. "
                            "East Asia provides the strongest evidence of convergence. "
                            "Countries like China, Vietnam, and Indonesia have grown at rates far above the global average, "
                            "lifting hundreds of millions of people out of poverty. "
                            "These emerging economies have attracted foreign investment, built modern infrastructure, "
                            "and expanded their manufacturing sectors at remarkable speed.\n\n"
                            "Divergence, on the other hand, happens when the gap between rich and poor countries widens. "
                            "Some nations in Africa and parts of South Asia have experienced slow or negative growth "
                            "for decades, falling further behind the developed world. "
                            "Conflict, weak institutions, and lack of investment are common reasons for divergence.\n\n"
                            "A key process in the growth story is industrialization — "
                            "the shift from an economy based on farming to one based on manufacturing. "
                            "When a country industrializes, workers move from low-productivity agriculture "
                            "to higher-productivity factory jobs. "
                            "Output per worker rises, wages increase, and the economy grows. "
                            "Britain was the first country to industrialize in the late seventeen hundreds. "
                            "Japan followed in the late eighteen hundreds, and South Korea in the nineteen sixties.\n\n"
                            "Industrialization almost always brings urbanization — "
                            "the movement of people from rural areas to cities. "
                            "Factories are built near ports and transportation hubs, "
                            "and workers migrate to be close to jobs. "
                            "In Vietnam, urbanization has accelerated rapidly. "
                            "Ho Chi Minh City and Hanoi have grown into major economic centers, "
                            "drawing millions of workers from the countryside.\n\n"
                            "But growth must be sustainable to last. "
                            "Sustainable growth means expanding the economy without depleting natural resources "
                            "or causing environmental damage that harms future generations. "
                            "Many emerging economies face a difficult balance: "
                            "they need rapid industrialization to reduce poverty, "
                            "but they also need to protect their rivers, forests, and air quality. "
                            "Finding this balance is one of the greatest challenges of modern development."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Hội tụ, phân kỳ và chuyển đổi kinh tế",
                    "description": "Viết câu sử dụng 6 từ vựng về hội tụ và chuyển đổi kinh tế.",
                    "data": {
                        "vocabList": ["convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization"],
                        "items": [
                            {
                                "targetVocab": "convergence",
                                "prompt": "Dùng từ 'convergence' để viết một câu về xu hướng các nước đang phát triển thu hẹp khoảng cách với các nước giàu. Ví dụ: The convergence between Vietnam's living standards and those of middle-income countries has accelerated since the country joined the World Trade Organization."
                            },
                            {
                                "targetVocab": "divergence",
                                "prompt": "Dùng từ 'divergence' để viết một câu về khoảng cách ngày càng lớn giữa hai nhóm quốc gia. Ví dụ: The divergence in economic performance between oil-rich nations that diversified their economies and those that did not has become increasingly clear."
                            },
                            {
                                "targetVocab": "sustainable",
                                "prompt": "Dùng từ 'sustainable' để viết một câu về tăng trưởng bền vững và bảo vệ môi trường. Ví dụ: The government has set a target for sustainable development that includes reducing carbon emissions while maintaining economic growth above five percent."
                            },
                            {
                                "targetVocab": "emerging",
                                "prompt": "Dùng từ 'emerging' để viết một câu về đặc điểm của các nền kinh tế mới nổi. Ví dụ: Emerging economies in Southeast Asia are attracting global attention because of their young populations, growing middle classes, and improving business environments."
                            },
                            {
                                "targetVocab": "industrialization",
                                "prompt": "Dùng từ 'industrialization' để viết một câu về quá trình công nghiệp hóa và tác động đến cơ cấu lao động. Ví dụ: Industrialization shifted millions of Vietnamese workers from rice paddies to factory floors, dramatically increasing their productivity and income."
                            },
                            {
                                "targetVocab": "urbanization",
                                "prompt": "Dùng từ 'urbanization' để viết một câu về quá trình đô thị hóa và những thách thức đi kèm. Ví dụ: Rapid urbanization in Hanoi has led to severe traffic congestion and air pollution, prompting the city to invest in a new metro system."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về năng suất, thể chế và cải cách.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: growth, development, investment, "
                            "capital, infrastructure, innovation — những động lực chính của tăng trưởng kinh tế. "
                            "Trong phần 2, bạn đã học thêm convergence, divergence, sustainable, emerging, "
                            "industrialization, urbanization — giúp bạn so sánh quỹ đạo phát triển giữa các quốc gia.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ đi vào câu hỏi sâu hơn: "
                            "điều gì quyết định một quốc gia tăng trưởng bền vững hay rơi vào trì trệ? "
                            "Bạn sẽ học 6 từ mới: productivity, human, institutional, reform, liberalization, và stagnation.\n\n"
                            "Từ đầu tiên là productivity — danh từ — nghĩa là năng suất, "
                            "lượng sản phẩm hoặc giá trị mà một đơn vị lao động hoặc vốn tạo ra. "
                            "Ví dụ: 'Improving labor productivity is essential for Vietnam to move from a middle-income "
                            "to a high-income economy.' "
                            "Trong bài đọc, productivity là thước đo quan trọng nhất — "
                            "một quốc gia chỉ có thể giàu lên bền vững khi mỗi người lao động tạo ra nhiều giá trị hơn.\n\n"
                            "Từ thứ hai là human — tính từ — trong ngữ cảnh kinh tế, thường đi với capital "
                            "thành human capital, nghĩa là vốn con người — kiến thức, kỹ năng và sức khỏe của người lao động. "
                            "Ví dụ: 'Countries that invest in human capital through education and healthcare "
                            "tend to achieve higher and more sustained economic growth.' "
                            "Trong bài đọc, human capital là yếu tố then chốt — "
                            "máy móc hiện đại vô dụng nếu không có người đủ kỹ năng vận hành.\n\n"
                            "Từ thứ ba là institutional — tính từ — nghĩa là thuộc về thể chế, "
                            "liên quan đến hệ thống luật pháp, quy tắc và tổ chức quản lý nền kinh tế. "
                            "Ví dụ: 'Institutional quality — including rule of law, property rights, and low corruption — "
                            "is a strong predictor of long-term economic success.' "
                            "Trong bài đọc, institutional nhấn mạnh rằng thể chế tốt tạo ra môi trường "
                            "thuận lợi cho đầu tư và đổi mới.\n\n"
                            "Từ thứ tư là reform — danh từ và động từ — nghĩa là cải cách, "
                            "thay đổi có hệ thống trong chính sách hoặc thể chế để cải thiện hiệu quả kinh tế. "
                            "Ví dụ: 'Vietnam's Doi Moi reform in nineteen eighty-six transformed the country "
                            "from a centrally planned economy to a market-oriented one.' "
                            "Trong bài đọc, reform là bước ngoặt — khi chính phủ quyết định thay đổi "
                            "cách vận hành nền kinh tế để thúc đẩy tăng trưởng.\n\n"
                            "Từ thứ năm là liberalization — danh từ — nghĩa là tự do hóa, "
                            "quá trình giảm bớt sự kiểm soát của nhà nước đối với thương mại, đầu tư và thị trường. "
                            "Ví dụ: 'Trade liberalization allowed Vietnamese businesses to access global markets "
                            "and compete with international companies.' "
                            "Trong bài đọc, liberalization là một phần quan trọng của reform — "
                            "mở cửa thị trường để thu hút đầu tư và thúc đẩy cạnh tranh.\n\n"
                            "Từ cuối cùng là stagnation — danh từ — nghĩa là trì trệ, "
                            "tình trạng nền kinh tế không tăng trưởng hoặc tăng trưởng rất chậm trong thời gian dài. "
                            "Ví dụ: 'Japan experienced economic stagnation throughout the nineteen nineties, "
                            "a period often called the Lost Decade.' "
                            "Trong bài đọc, stagnation là kết quả khi một quốc gia thiếu reform, "
                            "thiếu innovation, hoặc gặp vấn đề về thể chế.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về năng suất, thể chế và cải cách nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Năng suất, thể chế và cải cách",
                    "description": "Học 6 từ: productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Năng suất, thể chế và cải cách",
                    "description": "Học 6 từ: productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Năng suất, thể chế và cải cách",
                    "description": "Học 6 từ: productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Năng suất, thể chế và cải cách",
                    "description": "Học 6 từ: productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Năng suất, thể chế và cải cách",
                    "description": "Học 6 từ: productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Năng suất, thể chế và con đường cải cách",
                    "description": "In the long run, the wealth of a nation depends on one thing above all else: how much each worker can produce.",
                    "data": {
                        "text": (
                            "In the long run, the wealth of a nation depends on one thing above all else: "
                            "how much each worker can produce. "
                            "This is the concept of productivity — the amount of output generated per unit of labor or capital. "
                            "Countries with high productivity are rich. Countries with low productivity are poor. "
                            "Almost everything else in economics follows from this simple fact.\n\n"
                            "What determines productivity? One of the most important factors is human capital. "
                            "Human capital refers to the knowledge, skills, and health of the workforce. "
                            "A factory worker who has completed secondary school and received technical training "
                            "can operate complex machinery and solve problems on the production line. "
                            "A worker without education may only be able to perform simple manual tasks. "
                            "Countries that invest heavily in education and healthcare — "
                            "building schools, training teachers, and providing basic medical services — "
                            "tend to see their productivity rise over time.\n\n"
                            "But human capital alone is not enough. "
                            "The institutional environment matters just as much. "
                            "Institutional quality refers to the rules, laws, and organizations that govern economic activity. "
                            "When property rights are protected, contracts are enforced, and corruption is low, "
                            "businesses feel confident investing and innovating. "
                            "When institutions are weak — when courts are unreliable, regulations are unpredictable, "
                            "or officials demand bribes — businesses hold back, and growth suffers.\n\n"
                            "Many countries have discovered that the path to sustained growth requires reform. "
                            "Reform means making deliberate changes to policies and institutions "
                            "to create a better environment for economic activity. "
                            "Vietnam's Doi Moi reform in nineteen eighty-six is a powerful example. "
                            "Before Doi Moi, the economy was centrally planned — "
                            "the government decided what to produce, how much to charge, and where to sell. "
                            "After the reform, markets were allowed to function, private businesses were permitted, "
                            "and foreign investors were welcomed.\n\n"
                            "A key part of many reform programs is liberalization — "
                            "reducing government control over trade, investment, and prices. "
                            "Trade liberalization means lowering tariffs and removing barriers "
                            "so that domestic companies can sell abroad and foreign goods can enter the market. "
                            "Financial liberalization means allowing banks and investors to operate with fewer restrictions. "
                            "When done carefully, liberalization can boost competition, attract capital, "
                            "and accelerate growth.\n\n"
                            "But not every country succeeds. "
                            "Some economies fall into stagnation — a prolonged period of little or no growth. "
                            "Japan's Lost Decade in the nineteen nineties is a well-known case. "
                            "After decades of rapid expansion, the Japanese economy stopped growing. "
                            "Asset prices collapsed, banks were burdened with bad loans, "
                            "and the government struggled to find policies that would restart growth. "
                            "Stagnation can also result from resistance to reform, "
                            "over-reliance on a single industry, or failure to invest in human capital and innovation."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Năng suất, thể chế và con đường cải cách",
                    "description": "In the long run, the wealth of a nation depends on one thing above all else: how much each worker can produce.",
                    "data": {
                        "text": (
                            "In the long run, the wealth of a nation depends on one thing above all else: "
                            "how much each worker can produce. "
                            "This is the concept of productivity — the amount of output generated per unit of labor or capital. "
                            "Countries with high productivity are rich. Countries with low productivity are poor. "
                            "Almost everything else in economics follows from this simple fact.\n\n"
                            "What determines productivity? One of the most important factors is human capital. "
                            "Human capital refers to the knowledge, skills, and health of the workforce. "
                            "A factory worker who has completed secondary school and received technical training "
                            "can operate complex machinery and solve problems on the production line. "
                            "A worker without education may only be able to perform simple manual tasks. "
                            "Countries that invest heavily in education and healthcare — "
                            "building schools, training teachers, and providing basic medical services — "
                            "tend to see their productivity rise over time.\n\n"
                            "But human capital alone is not enough. "
                            "The institutional environment matters just as much. "
                            "Institutional quality refers to the rules, laws, and organizations that govern economic activity. "
                            "When property rights are protected, contracts are enforced, and corruption is low, "
                            "businesses feel confident investing and innovating. "
                            "When institutions are weak — when courts are unreliable, regulations are unpredictable, "
                            "or officials demand bribes — businesses hold back, and growth suffers.\n\n"
                            "Many countries have discovered that the path to sustained growth requires reform. "
                            "Reform means making deliberate changes to policies and institutions "
                            "to create a better environment for economic activity. "
                            "Vietnam's Doi Moi reform in nineteen eighty-six is a powerful example. "
                            "Before Doi Moi, the economy was centrally planned — "
                            "the government decided what to produce, how much to charge, and where to sell. "
                            "After the reform, markets were allowed to function, private businesses were permitted, "
                            "and foreign investors were welcomed.\n\n"
                            "A key part of many reform programs is liberalization — "
                            "reducing government control over trade, investment, and prices. "
                            "Trade liberalization means lowering tariffs and removing barriers "
                            "so that domestic companies can sell abroad and foreign goods can enter the market. "
                            "Financial liberalization means allowing banks and investors to operate with fewer restrictions. "
                            "When done carefully, liberalization can boost competition, attract capital, "
                            "and accelerate growth.\n\n"
                            "But not every country succeeds. "
                            "Some economies fall into stagnation — a prolonged period of little or no growth. "
                            "Japan's Lost Decade in the nineteen nineties is a well-known case. "
                            "After decades of rapid expansion, the Japanese economy stopped growing. "
                            "Asset prices collapsed, banks were burdened with bad loans, "
                            "and the government struggled to find policies that would restart growth. "
                            "Stagnation can also result from resistance to reform, "
                            "over-reliance on a single industry, or failure to invest in human capital and innovation."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Năng suất, thể chế và con đường cải cách",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "In the long run, the wealth of a nation depends on one thing above all else: "
                            "how much each worker can produce. "
                            "This is the concept of productivity — the amount of output generated per unit of labor or capital. "
                            "Countries with high productivity are rich. Countries with low productivity are poor. "
                            "Almost everything else in economics follows from this simple fact.\n\n"
                            "What determines productivity? One of the most important factors is human capital. "
                            "Human capital refers to the knowledge, skills, and health of the workforce. "
                            "A factory worker who has completed secondary school and received technical training "
                            "can operate complex machinery and solve problems on the production line. "
                            "A worker without education may only be able to perform simple manual tasks. "
                            "Countries that invest heavily in education and healthcare — "
                            "building schools, training teachers, and providing basic medical services — "
                            "tend to see their productivity rise over time.\n\n"
                            "But human capital alone is not enough. "
                            "The institutional environment matters just as much. "
                            "Institutional quality refers to the rules, laws, and organizations that govern economic activity. "
                            "When property rights are protected, contracts are enforced, and corruption is low, "
                            "businesses feel confident investing and innovating. "
                            "When institutions are weak — when courts are unreliable, regulations are unpredictable, "
                            "or officials demand bribes — businesses hold back, and growth suffers.\n\n"
                            "Many countries have discovered that the path to sustained growth requires reform. "
                            "Reform means making deliberate changes to policies and institutions "
                            "to create a better environment for economic activity. "
                            "Vietnam's Doi Moi reform in nineteen eighty-six is a powerful example. "
                            "Before Doi Moi, the economy was centrally planned — "
                            "the government decided what to produce, how much to charge, and where to sell. "
                            "After the reform, markets were allowed to function, private businesses were permitted, "
                            "and foreign investors were welcomed.\n\n"
                            "A key part of many reform programs is liberalization — "
                            "reducing government control over trade, investment, and prices. "
                            "Trade liberalization means lowering tariffs and removing barriers "
                            "so that domestic companies can sell abroad and foreign goods can enter the market. "
                            "Financial liberalization means allowing banks and investors to operate with fewer restrictions. "
                            "When done carefully, liberalization can boost competition, attract capital, "
                            "and accelerate growth.\n\n"
                            "But not every country succeeds. "
                            "Some economies fall into stagnation — a prolonged period of little or no growth. "
                            "Japan's Lost Decade in the nineteen nineties is a well-known case. "
                            "After decades of rapid expansion, the Japanese economy stopped growing. "
                            "Asset prices collapsed, banks were burdened with bad loans, "
                            "and the government struggled to find policies that would restart growth. "
                            "Stagnation can also result from resistance to reform, "
                            "over-reliance on a single industry, or failure to invest in human capital and innovation."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Năng suất, thể chế và cải cách",
                    "description": "Viết câu sử dụng 6 từ vựng về năng suất và cải cách.",
                    "data": {
                        "vocabList": ["productivity", "human", "institutional", "reform", "liberalization", "stagnation"],
                        "items": [
                            {
                                "targetVocab": "productivity",
                                "prompt": "Dùng từ 'productivity' để viết một câu về mối quan hệ giữa năng suất lao động và mức sống. Ví dụ: Raising labor productivity through better training and modern technology is the most reliable way for a developing country to increase wages and living standards."
                            },
                            {
                                "targetVocab": "human",
                                "prompt": "Dùng từ 'human' (trong cụm human capital) để viết một câu về vai trò của giáo dục trong phát triển kinh tế. Ví dụ: Vietnam's investment in human capital — especially universal primary education and expanding university access — has been a key driver of its economic transformation."
                            },
                            {
                                "targetVocab": "institutional",
                                "prompt": "Dùng từ 'institutional' để viết một câu về tầm quan trọng của chất lượng thể chế đối với tăng trưởng. Ví dụ: Institutional reforms that strengthen the rule of law and reduce corruption can attract more foreign investment than any tax incentive."
                            },
                            {
                                "targetVocab": "reform",
                                "prompt": "Dùng từ 'reform' để viết một câu về một cuộc cải cách kinh tế cụ thể và tác động của nó. Ví dụ: The Doi Moi reform allowed private enterprise to flourish in Vietnam, leading to three decades of rapid economic growth and poverty reduction."
                            },
                            {
                                "targetVocab": "liberalization",
                                "prompt": "Dùng từ 'liberalization' để viết một câu về quá trình tự do hóa thương mại và tác động đến doanh nghiệp trong nước. Ví dụ: Trade liberalization forced Vietnamese manufacturers to improve quality and efficiency in order to compete with cheaper imports from China."
                            },
                            {
                                "targetVocab": "stagnation",
                                "prompt": "Dùng từ 'stagnation' để viết một câu về nguyên nhân và hậu quả của trì trệ kinh tế. Ví dụ: Economic stagnation in Venezuela resulted from over-dependence on oil revenues and a failure to diversify the economy when prices were high."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Tăng trưởng kinh tế. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "growth — tăng trưởng, development — phát triển, investment — đầu tư, "
                            "capital — vốn, infrastructure — cơ sở hạ tầng, và innovation — đổi mới sáng tạo. "
                            "Đây là những động lực chính đưa một nền kinh tế đi lên.\n\n"
                            "Trong phần 2, bạn đã mở rộng tầm nhìn với: "
                            "convergence — hội tụ, divergence — phân kỳ, sustainable — bền vững, "
                            "emerging — mới nổi, industrialization — công nghiệp hóa, và urbanization — đô thị hóa. "
                            "Những từ này giúp bạn so sánh và phân tích quỹ đạo phát triển giữa các quốc gia.\n\n"
                            "Trong phần 3, bạn đã đi sâu vào: "
                            "productivity — năng suất, human — vốn con người, institutional — thể chế, "
                            "reform — cải cách, liberalization — tự do hóa, và stagnation — trì trệ. "
                            "Đây là những từ về chính sách và thể chế — yếu tố quyết định thành bại của một nền kinh tế.\n\n"
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
                    "description": "Học 18 từ: growth, development, investment, capital, infrastructure, innovation, convergence, divergence, sustainable, emerging, industrialization, urbanization, productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: growth, development, investment, capital, infrastructure, innovation, convergence, divergence, sustainable, emerging, industrialization, urbanization, productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: growth, development, investment, capital, infrastructure, innovation, convergence, divergence, sustainable, emerging, industrialization, urbanization, productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: growth, development, investment, capital, infrastructure, innovation, convergence, divergence, sustainable, emerging, industrialization, urbanization, productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: growth, development, investment, capital, infrastructure, innovation, convergence, divergence, sustainable, emerging, industrialization, urbanization, productivity, human, institutional, reform, liberalization, stagnation",
                    "data": {"vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng tăng trưởng kinh tế",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"],
                        "items": [
                            {
                                "targetVocab": "growth",
                                "prompt": "Dùng từ 'growth' để viết một câu so sánh tốc độ tăng trưởng giữa hai giai đoạn lịch sử của Việt Nam. Ví dụ: Vietnam's growth rate jumped from under four percent in the early nineteen eighties to over eight percent in the mid-nineteen nineties after the Doi Moi reforms took effect."
                            },
                            {
                                "targetVocab": "development",
                                "prompt": "Dùng từ 'development' để viết một câu về chỉ số phát triển con người (HDI) và ý nghĩa của nó. Ví dụ: The Human Development Index measures development by combining data on life expectancy, education, and income per capita into a single score."
                            },
                            {
                                "targetVocab": "investment",
                                "prompt": "Dùng từ 'investment' để viết một câu về tác động của đầu tư vào giáo dục đối với tăng trưởng dài hạn. Ví dụ: Investment in early childhood education yields some of the highest returns of any public spending because it builds the foundation for lifelong productivity."
                            },
                            {
                                "targetVocab": "capital",
                                "prompt": "Dùng từ 'capital' để viết một câu phân biệt giữa physical capital và human capital. Ví dụ: While physical capital like machinery can be purchased quickly, building human capital through education and training takes years of sustained effort."
                            },
                            {
                                "targetVocab": "infrastructure",
                                "prompt": "Dùng từ 'infrastructure' để viết một câu về dự án cơ sở hạ tầng lớn và tác động kinh tế của nó. Ví dụ: The new expressway connecting Hanoi to Hai Phong has improved infrastructure in the region and cut transportation time for goods by more than half."
                            },
                            {
                                "targetVocab": "innovation",
                                "prompt": "Dùng từ 'innovation' để viết một câu về vai trò của đổi mới sáng tạo trong việc thoát bẫy thu nhập trung bình. Ví dụ: Without sustained innovation in technology and business processes, many emerging economies risk getting stuck in the middle-income trap."
                            },
                            {
                                "targetVocab": "convergence",
                                "prompt": "Dùng từ 'convergence' để viết một câu về xu hướng hội tụ kinh tế trong khu vực ASEAN. Ví dụ: Economic convergence among ASEAN nations has been uneven — while Vietnam and Cambodia have grown rapidly, Myanmar's progress has been slowed by political instability."
                            },
                            {
                                "targetVocab": "divergence",
                                "prompt": "Dùng từ 'divergence' để viết một câu về sự phân kỳ giữa thành thị và nông thôn trong cùng một quốc gia. Ví dụ: The divergence in income between urban and rural areas in Vietnam has widened as cities attract more investment and higher-paying jobs."
                            },
                            {
                                "targetVocab": "sustainable",
                                "prompt": "Dùng từ 'sustainable' để viết một câu về thách thức của tăng trưởng bền vững trong bối cảnh biến đổi khí hậu. Ví dụ: Achieving sustainable growth in the Mekong Delta requires adapting agriculture to rising sea levels while maintaining the region's role as Vietnam's rice bowl."
                            },
                            {
                                "targetVocab": "emerging",
                                "prompt": "Dùng từ 'emerging' để viết một câu về cơ hội đầu tư tại các thị trường mới nổi. Ví dụ: Global fund managers are increasingly allocating capital to emerging markets in Southeast Asia because of their strong demographic trends and improving governance."
                            },
                            {
                                "targetVocab": "industrialization",
                                "prompt": "Dùng từ 'industrialization' để viết một câu về bài học từ quá trình công nghiệp hóa của một quốc gia châu Á. Ví dụ: South Korea's rapid industrialization was driven by government-directed investment in heavy industries like steel and shipbuilding during the nineteen seventies."
                            },
                            {
                                "targetVocab": "urbanization",
                                "prompt": "Dùng từ 'urbanization' để viết một câu về mối quan hệ giữa đô thị hóa và dịch vụ công. Ví dụ: Urbanization puts enormous pressure on public services — cities must build more schools, hospitals, and water treatment plants to keep up with population growth."
                            },
                            {
                                "targetVocab": "productivity",
                                "prompt": "Dùng từ 'productivity' để viết một câu về cách công nghệ nâng cao năng suất trong nông nghiệp. Ví dụ: The introduction of high-yield rice varieties and modern irrigation systems has dramatically increased agricultural productivity in the Mekong Delta."
                            },
                            {
                                "targetVocab": "human",
                                "prompt": "Dùng từ 'human' (trong cụm human capital) để viết một câu về chính sách đào tạo nghề và tác động kinh tế. Ví dụ: Germany's dual education system, which combines classroom learning with on-the-job training, is widely regarded as one of the best models for building human capital."
                            },
                            {
                                "targetVocab": "institutional",
                                "prompt": "Dùng từ 'institutional' để viết một câu về mối quan hệ giữa chất lượng thể chế và thu hút đầu tư. Ví dụ: Countries with strong institutional frameworks — transparent regulations, independent courts, and low corruption — consistently attract more foreign direct investment."
                            },
                            {
                                "targetVocab": "reform",
                                "prompt": "Dùng từ 'reform' để viết một câu về một cuộc cải cách kinh tế đang diễn ra và mục tiêu của nó. Ví dụ: Vietnam's ongoing reform of state-owned enterprises aims to improve efficiency and reduce the burden on the national budget."
                            },
                            {
                                "targetVocab": "liberalization",
                                "prompt": "Dùng từ 'liberalization' để viết một câu về tác động của tự do hóa tài chính đối với hệ thống ngân hàng. Ví dụ: Financial liberalization in the early two thousands allowed foreign banks to enter Vietnam's market, increasing competition and improving the quality of banking services."
                            },
                            {
                                "targetVocab": "stagnation",
                                "prompt": "Dùng từ 'stagnation' để viết một câu về rủi ro trì trệ kinh tế khi thiếu đổi mới. Ví dụ: Without continuous investment in research and innovation, even successful economies can fall into stagnation as their industries lose competitiveness to newer rivals."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về tăng trưởng kinh tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về tăng trưởng kinh tế — từ những động lực cơ bản "
                            "đến thể chế và cải cách.\n\n"
                            "Bạn sẽ gặp lại growth, development, investment, capital, infrastructure, innovation "
                            "trong phần mở đầu về các yếu tố thúc đẩy tăng trưởng. "
                            "Tiếp theo, convergence, divergence, sustainable, emerging, industrialization, urbanization "
                            "sẽ giúp bạn hiểu quỹ đạo phát triển của các quốc gia. "
                            "Và cuối cùng, productivity, human, institutional, reform, liberalization, stagnation "
                            "sẽ đưa bạn vào thế giới chính sách và thể chế.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tăng trưởng kinh tế — Bức tranh toàn cảnh",
                    "description": "Two hundred years ago, almost every person on Earth lived in poverty.",
                    "data": {
                        "text": (
                            "Two hundred years ago, almost every person on Earth lived in poverty. "
                            "Today, billions enjoy standards of living that would have been unimaginable to their ancestors. "
                            "What changed? The answer is economic growth — "
                            "the sustained increase in a nation's output of goods and services over time.\n\n"
                            "Growth begins with investment. "
                            "When a country channels resources into building factories, purchasing machinery, "
                            "and developing new technologies, it accumulates capital. "
                            "Physical capital — the tools and structures used in production — "
                            "allows workers to produce more with less effort. "
                            "A farmer with a tractor can cultivate ten times the land of a farmer with a hoe. "
                            "A factory with modern robots can assemble products faster and more precisely than one relying on manual labor.\n\n"
                            "But capital is only part of the story. "
                            "Infrastructure — roads, ports, power grids, and communication networks — "
                            "connects producers to markets and enables the flow of goods and information. "
                            "Vietnam's investment in infrastructure over the past three decades "
                            "has been a cornerstone of its growth strategy. "
                            "New highways link industrial zones to seaports, "
                            "and expanded internet access has opened doors for digital businesses.\n\n"
                            "Innovation pushes the frontier further. "
                            "It is not enough to simply build more factories; "
                            "countries must also find smarter ways to produce. "
                            "Innovation — whether in technology, management, or business models — "
                            "is what allows economies to grow even after they have accumulated large amounts of capital. "
                            "Without innovation, growth eventually slows as the returns from adding more capital diminish.\n\n"
                            "The distinction between growth and development matters. "
                            "Growth measures the size of the economic pie. "
                            "Development asks whether the pie is being shared fairly "
                            "and whether people's lives are actually improving. "
                            "A country can post impressive growth numbers while millions remain in poverty, "
                            "lack access to healthcare, or breathe polluted air. "
                            "True development requires that growth be inclusive and sustainable — "
                            "benefiting all citizens without destroying the environment for future generations.\n\n"
                            "Looking across the globe, we see two patterns. "
                            "Convergence describes the hopeful trend of poorer countries catching up with richer ones. "
                            "Many emerging economies in East and Southeast Asia have experienced convergence, "
                            "growing at rates far above the world average. "
                            "Vietnam, once among the poorest countries in the region, "
                            "has narrowed the gap with its wealthier neighbors through decades of sustained effort.\n\n"
                            "Divergence tells the opposite story. "
                            "Some countries have fallen further behind, "
                            "trapped by conflict, corruption, or poor policy choices. "
                            "The divergence between East Asia and parts of sub-Saharan Africa "
                            "over the past half-century is one of the starkest examples in modern economics.\n\n"
                            "The process of industrialization has been central to nearly every growth success story. "
                            "When workers move from subsistence farming to manufacturing, "
                            "productivity rises dramatically. "
                            "Industrialization also drives urbanization, "
                            "as people migrate to cities where factories and service jobs are concentrated. "
                            "Vietnam's rapid urbanization — with millions moving to Ho Chi Minh City, "
                            "Hanoi, and Da Nang — reflects this global pattern.\n\n"
                            "Productivity is the ultimate source of wealth. "
                            "A country becomes rich not by working more hours, "
                            "but by producing more value per hour worked. "
                            "Raising productivity requires investing in human capital — "
                            "the education, skills, and health of the workforce. "
                            "A well-educated population can adopt new technologies, "
                            "manage complex organizations, and drive innovation.\n\n"
                            "The institutional environment shapes everything. "
                            "Countries with strong institutional frameworks — "
                            "clear property rights, fair courts, transparent regulations — "
                            "create an environment where businesses are willing to invest and take risks. "
                            "Countries with weak institutions often see capital flee, talent emigrate, "
                            "and growth stall.\n\n"
                            "Reform is the bridge between a struggling economy and a thriving one. "
                            "Vietnam's Doi Moi reform opened the door to private enterprise and foreign investment, "
                            "setting the stage for three decades of rapid growth. "
                            "China's market reforms in the late nineteen seventies had a similar transformative effect. "
                            "Liberalization — reducing barriers to trade, investment, and competition — "
                            "has been a common thread in successful reform programs around the world.\n\n"
                            "Not every story has a happy ending. "
                            "Stagnation — prolonged periods of little or no growth — "
                            "can strike even once-successful economies. "
                            "Japan's Lost Decade, Argentina's repeated crises, "
                            "and the slow growth of many resource-rich nations "
                            "all show that past success does not guarantee future prosperity.\n\n"
                            "The study of economic growth is ultimately the study of human potential. "
                            "Every road built, every child educated, every reform enacted "
                            "is a step toward a future where more people can live with dignity and opportunity. "
                            "Understanding the vocabulary of growth is the first step "
                            "toward participating in this conversation — in any language."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tăng trưởng kinh tế — Bức tranh toàn cảnh",
                    "description": "Two hundred years ago, almost every person on Earth lived in poverty.",
                    "data": {
                        "text": (
                            "Two hundred years ago, almost every person on Earth lived in poverty. "
                            "Today, billions enjoy standards of living that would have been unimaginable to their ancestors. "
                            "What changed? The answer is economic growth — "
                            "the sustained increase in a nation's output of goods and services over time.\n\n"
                            "Growth begins with investment. "
                            "When a country channels resources into building factories, purchasing machinery, "
                            "and developing new technologies, it accumulates capital. "
                            "Physical capital — the tools and structures used in production — "
                            "allows workers to produce more with less effort. "
                            "A farmer with a tractor can cultivate ten times the land of a farmer with a hoe. "
                            "A factory with modern robots can assemble products faster and more precisely than one relying on manual labor.\n\n"
                            "But capital is only part of the story. "
                            "Infrastructure — roads, ports, power grids, and communication networks — "
                            "connects producers to markets and enables the flow of goods and information. "
                            "Vietnam's investment in infrastructure over the past three decades "
                            "has been a cornerstone of its growth strategy. "
                            "New highways link industrial zones to seaports, "
                            "and expanded internet access has opened doors for digital businesses.\n\n"
                            "Innovation pushes the frontier further. "
                            "It is not enough to simply build more factories; "
                            "countries must also find smarter ways to produce. "
                            "Innovation — whether in technology, management, or business models — "
                            "is what allows economies to grow even after they have accumulated large amounts of capital. "
                            "Without innovation, growth eventually slows as the returns from adding more capital diminish.\n\n"
                            "The distinction between growth and development matters. "
                            "Growth measures the size of the economic pie. "
                            "Development asks whether the pie is being shared fairly "
                            "and whether people's lives are actually improving. "
                            "A country can post impressive growth numbers while millions remain in poverty, "
                            "lack access to healthcare, or breathe polluted air. "
                            "True development requires that growth be inclusive and sustainable — "
                            "benefiting all citizens without destroying the environment for future generations.\n\n"
                            "Looking across the globe, we see two patterns. "
                            "Convergence describes the hopeful trend of poorer countries catching up with richer ones. "
                            "Many emerging economies in East and Southeast Asia have experienced convergence, "
                            "growing at rates far above the world average. "
                            "Vietnam, once among the poorest countries in the region, "
                            "has narrowed the gap with its wealthier neighbors through decades of sustained effort.\n\n"
                            "Divergence tells the opposite story. "
                            "Some countries have fallen further behind, "
                            "trapped by conflict, corruption, or poor policy choices. "
                            "The divergence between East Asia and parts of sub-Saharan Africa "
                            "over the past half-century is one of the starkest examples in modern economics.\n\n"
                            "The process of industrialization has been central to nearly every growth success story. "
                            "When workers move from subsistence farming to manufacturing, "
                            "productivity rises dramatically. "
                            "Industrialization also drives urbanization, "
                            "as people migrate to cities where factories and service jobs are concentrated. "
                            "Vietnam's rapid urbanization — with millions moving to Ho Chi Minh City, "
                            "Hanoi, and Da Nang — reflects this global pattern.\n\n"
                            "Productivity is the ultimate source of wealth. "
                            "A country becomes rich not by working more hours, "
                            "but by producing more value per hour worked. "
                            "Raising productivity requires investing in human capital — "
                            "the education, skills, and health of the workforce. "
                            "A well-educated population can adopt new technologies, "
                            "manage complex organizations, and drive innovation.\n\n"
                            "The institutional environment shapes everything. "
                            "Countries with strong institutional frameworks — "
                            "clear property rights, fair courts, transparent regulations — "
                            "create an environment where businesses are willing to invest and take risks. "
                            "Countries with weak institutions often see capital flee, talent emigrate, "
                            "and growth stall.\n\n"
                            "Reform is the bridge between a struggling economy and a thriving one. "
                            "Vietnam's Doi Moi reform opened the door to private enterprise and foreign investment, "
                            "setting the stage for three decades of rapid growth. "
                            "China's market reforms in the late nineteen seventies had a similar transformative effect. "
                            "Liberalization — reducing barriers to trade, investment, and competition — "
                            "has been a common thread in successful reform programs around the world.\n\n"
                            "Not every story has a happy ending. "
                            "Stagnation — prolonged periods of little or no growth — "
                            "can strike even once-successful economies. "
                            "Japan's Lost Decade, Argentina's repeated crises, "
                            "and the slow growth of many resource-rich nations "
                            "all show that past success does not guarantee future prosperity.\n\n"
                            "The study of economic growth is ultimately the study of human potential. "
                            "Every road built, every child educated, every reform enacted "
                            "is a step toward a future where more people can live with dignity and opportunity. "
                            "Understanding the vocabulary of growth is the first step "
                            "toward participating in this conversation — in any language."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tăng trưởng kinh tế — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Two hundred years ago, almost every person on Earth lived in poverty. "
                            "Today, billions enjoy standards of living that would have been unimaginable to their ancestors. "
                            "What changed? The answer is economic growth — "
                            "the sustained increase in a nation's output of goods and services over time.\n\n"
                            "Growth begins with investment. "
                            "When a country channels resources into building factories, purchasing machinery, "
                            "and developing new technologies, it accumulates capital. "
                            "Physical capital — the tools and structures used in production — "
                            "allows workers to produce more with less effort. "
                            "A farmer with a tractor can cultivate ten times the land of a farmer with a hoe. "
                            "A factory with modern robots can assemble products faster and more precisely than one relying on manual labor.\n\n"
                            "But capital is only part of the story. "
                            "Infrastructure — roads, ports, power grids, and communication networks — "
                            "connects producers to markets and enables the flow of goods and information. "
                            "Vietnam's investment in infrastructure over the past three decades "
                            "has been a cornerstone of its growth strategy. "
                            "New highways link industrial zones to seaports, "
                            "and expanded internet access has opened doors for digital businesses.\n\n"
                            "Innovation pushes the frontier further. "
                            "It is not enough to simply build more factories; "
                            "countries must also find smarter ways to produce. "
                            "Innovation — whether in technology, management, or business models — "
                            "is what allows economies to grow even after they have accumulated large amounts of capital. "
                            "Without innovation, growth eventually slows as the returns from adding more capital diminish.\n\n"
                            "The distinction between growth and development matters. "
                            "Growth measures the size of the economic pie. "
                            "Development asks whether the pie is being shared fairly "
                            "and whether people's lives are actually improving. "
                            "A country can post impressive growth numbers while millions remain in poverty, "
                            "lack access to healthcare, or breathe polluted air. "
                            "True development requires that growth be inclusive and sustainable — "
                            "benefiting all citizens without destroying the environment for future generations.\n\n"
                            "Looking across the globe, we see two patterns. "
                            "Convergence describes the hopeful trend of poorer countries catching up with richer ones. "
                            "Many emerging economies in East and Southeast Asia have experienced convergence, "
                            "growing at rates far above the world average. "
                            "Vietnam, once among the poorest countries in the region, "
                            "has narrowed the gap with its wealthier neighbors through decades of sustained effort.\n\n"
                            "Divergence tells the opposite story. "
                            "Some countries have fallen further behind, "
                            "trapped by conflict, corruption, or poor policy choices. "
                            "The divergence between East Asia and parts of sub-Saharan Africa "
                            "over the past half-century is one of the starkest examples in modern economics.\n\n"
                            "The process of industrialization has been central to nearly every growth success story. "
                            "When workers move from subsistence farming to manufacturing, "
                            "productivity rises dramatically. "
                            "Industrialization also drives urbanization, "
                            "as people migrate to cities where factories and service jobs are concentrated. "
                            "Vietnam's rapid urbanization — with millions moving to Ho Chi Minh City, "
                            "Hanoi, and Da Nang — reflects this global pattern.\n\n"
                            "Productivity is the ultimate source of wealth. "
                            "A country becomes rich not by working more hours, "
                            "but by producing more value per hour worked. "
                            "Raising productivity requires investing in human capital — "
                            "the education, skills, and health of the workforce. "
                            "A well-educated population can adopt new technologies, "
                            "manage complex organizations, and drive innovation.\n\n"
                            "The institutional environment shapes everything. "
                            "Countries with strong institutional frameworks — "
                            "clear property rights, fair courts, transparent regulations — "
                            "create an environment where businesses are willing to invest and take risks. "
                            "Countries with weak institutions often see capital flee, talent emigrate, "
                            "and growth stall.\n\n"
                            "Reform is the bridge between a struggling economy and a thriving one. "
                            "Vietnam's Doi Moi reform opened the door to private enterprise and foreign investment, "
                            "setting the stage for three decades of rapid growth. "
                            "China's market reforms in the late nineteen seventies had a similar transformative effect. "
                            "Liberalization — reducing barriers to trade, investment, and competition — "
                            "has been a common thread in successful reform programs around the world.\n\n"
                            "Not every story has a happy ending. "
                            "Stagnation — prolonged periods of little or no growth — "
                            "can strike even once-successful economies. "
                            "Japan's Lost Decade, Argentina's repeated crises, "
                            "and the slow growth of many resource-rich nations "
                            "all show that past success does not guarantee future prosperity.\n\n"
                            "The study of economic growth is ultimately the study of human potential. "
                            "Every road built, every child educated, every reform enacted "
                            "is a step toward a future where more people can live with dignity and opportunity. "
                            "Understanding the vocabulary of growth is the first step "
                            "toward participating in this conversation — in any language."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích tăng trưởng kinh tế",
                    "description": "Viết đoạn văn phân tích về tăng trưởng kinh tế sử dụng từ vựng đã học.",
                    "data": {
                        "vocabList": ["growth", "development", "investment", "capital", "infrastructure", "innovation", "convergence", "divergence", "sustainable", "emerging", "industrialization", "urbanization", "productivity", "human", "institutional", "reform", "liberalization", "stagnation"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của tăng trưởng kinh tế. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích quá trình tăng trưởng kinh tế của Việt Nam từ Đổi Mới đến nay. Giải thích vai trò của reform và liberalization trong việc thu hút investment, xây dựng infrastructure, và thúc đẩy industrialization. Liệu Việt Nam có đang trên đà convergence với các nước thu nhập cao, hay có nguy cơ rơi vào stagnation?",
                            "Hãy so sánh quỹ đạo phát triển của hai quốc gia hoặc khu vực — một bên đạt được sustainable growth và một bên rơi vào stagnation hoặc divergence. Phân tích vai trò của human capital, institutional quality, và innovation trong việc tạo ra sự khác biệt giữa hai con đường phát triển."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay đầy năng lượng.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học cuối cùng trong chuỗi Kinh tế vĩ mô — "
                            "và đây không phải là kết thúc, mà là khởi đầu cho một chặng đường mới!\n\n"
                            "Hãy cùng ôn lại những từ vựng quan trọng nhất — "
                            "những từ mà bạn sẽ mang theo vào mọi cuộc thảo luận về kinh tế từ bây giờ.\n\n"
                            "Growth — tăng trưởng. Đây là từ bạn sẽ gặp nhiều nhất khi đọc bất kỳ tài liệu kinh tế nào. "
                            "Tăng trưởng không chỉ là con số — nó là câu chuyện về cách một quốc gia "
                            "biến nguồn lực thành cơ hội cho người dân. "
                            "Ví dụ mới: The government's new five-year plan targets annual growth of six point five percent "
                            "through increased investment in technology and green energy.\n\n"
                            "Innovation — đổi mới sáng tạo. Trong thế kỷ 21, innovation là vũ khí bí mật "
                            "của những nền kinh tế vươn lên hàng đầu. Không phải ai có nhiều tài nguyên nhất sẽ thắng, "
                            "mà ai sáng tạo nhất sẽ dẫn đầu. "
                            "Ví dụ mới: Innovation in renewable energy has made solar power cheaper than coal "
                            "in many emerging economies, opening a new path to sustainable industrialization.\n\n"
                            "Convergence — hội tụ. Từ này mang theo hy vọng — hy vọng rằng các nước nghèo "
                            "có thể bắt kịp các nước giàu nếu đi đúng hướng. "
                            "Ví dụ mới: The convergence between Vietnam's per capita income and the ASEAN average "
                            "has accelerated since the country deepened its integration into global supply chains.\n\n"
                            "Reform — cải cách. Mỗi bước ngoặt trong lịch sử kinh tế đều bắt đầu bằng reform. "
                            "Đổi Mới 1986 là minh chứng sống động nhất cho sức mạnh của cải cách. "
                            "Ví dụ mới: The latest round of administrative reform has cut the time needed "
                            "to register a new business in Vietnam from thirty days to just three.\n\n"
                            "Human capital — vốn con người. Máy móc có thể mua, nhà xưởng có thể xây, "
                            "nhưng human capital phải được vun đắp qua nhiều năm giáo dục và đào tạo. "
                            "Đây là tài sản quý giá nhất của bất kỳ quốc gia nào. "
                            "Ví dụ mới: Countries that prioritize human capital development — "
                            "investing in schools, universities, and vocational training — "
                            "consistently outperform those that focus only on physical infrastructure.\n\n"
                            "Stagnation — trì trệ. Đây là từ cảnh báo — nhắc nhở rằng không có quốc gia nào "
                            "được đảm bảo tăng trưởng mãi mãi. Thiếu reform, thiếu innovation, "
                            "thiếu đầu tư vào con người — và stagnation sẽ gõ cửa. "
                            "Ví dụ mới: The risk of stagnation increases when an economy becomes complacent "
                            "and stops investing in the institutional reforms needed to stay competitive.\n\n"
                            "Bạn biết không, bạn không học một mình. Hàng triệu sinh viên kinh tế trên khắp thế giới "
                            "cũng đang đọc những tài liệu này, cũng đang vật lộn với những từ vựng này. "
                            "Nhưng bạn có một lợi thế — bạn đã bắt đầu. Bạn đã dành thời gian, "
                            "đã đọc, đã luyện, đã viết. Và mỗi từ bạn học hôm nay "
                            "là một viên gạch xây nên nền tảng cho sự nghiệp của bạn.\n\n"
                            "Hãy mang 18 từ vựng này vào lớp học, vào phòng thảo luận, "
                            "vào những buổi đọc báo cáo World Bank hay IMF. "
                            "Hãy dùng chúng khi viết bài luận, khi thuyết trình, khi tranh luận với bạn bè. "
                            "Tiếng Anh kinh tế không phải là rào cản — nó là cầu nối "
                            "đưa bạn đến với cộng đồng kinh tế toàn cầu.\n\n"
                            "Chúng tôi rất tự hào về bạn. Hẹn gặp lại ở những bài học tiếp theo — "
                            "cùng nhau, chúng ta sẽ đi xa hơn nữa!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Economic Growth – Tăng Trưởng Kinh Tế' AND uid = '{UID}' ORDER BY created_at;")
