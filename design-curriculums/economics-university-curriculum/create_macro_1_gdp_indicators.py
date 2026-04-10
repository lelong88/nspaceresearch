"""
Create curriculum: GDP & Indicators – GDP và Chỉ Số Kinh Tế
Series B — Kinh Tế Vĩ Mô (Macroeconomics), curriculum #1
18 words | 5 sessions | bold_declaration tone | warm accountability farewell
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
W1 = ["gross", "domestic", "nominal", "real", "per capita", "output"]
W2 = ["indicator", "index", "inflation", "deflation", "growth", "contraction"]
W3 = ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "GDP & Indicators – GDP và Chỉ Số Kinh Tế",
    "contentTypeTags": [],
    "description": (
        "GDP KHÔNG CHỈ LÀ MỘT CON SỐ — NÓ LÀ NHỊP TIM CỦA CẢ NỀN KINH TẾ, VÀ BẠN CẦN ĐỌC ĐƯỢC NÓ BẰNG TIẾNG ANH.\n\n"
        "Mỗi quý, Tổng cục Thống kê công bố GDP, nhưng khi bạn mở báo cáo tiếng Anh từ World Bank hay IMF, "
        "bạn gặp ngay nominal GDP, real GDP, per capita output — và bạn không chắc mình hiểu đúng. "
        "Giảng viên chiếu biểu đồ growth rate, inflation index trên slide, "
        "bạn ghi chép nhưng không dám hỏi vì sợ lộ ra mình chưa nắm vững thuật ngữ.\n\n"
        "Hãy nghĩ về GDP như bản đồ sức khỏe của nền kinh tế — nếu bạn không đọc được bản đồ, "
        "bạn sẽ đi lạc giữa rừng số liệu. 18 từ vựng trong bài học này chính là la bàn "
        "giúp bạn định hướng trong mọi báo cáo kinh tế vĩ mô.\n\n"
        "Sau khóa học, bạn sẽ tự tin đọc báo cáo GDP bằng tiếng Anh, phân biệt được nominal và real, "
        "hiểu inflation với deflation tác động thế nào đến growth, "
        "và viết được những nhận định kinh tế sắc bén bằng ngôn ngữ chuyên ngành.\n\n"
        "18 từ — từ gross đến forecast — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kinh tế vĩ mô, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về GDP và các chỉ số kinh tế — "
            "nền tảng của mọi phân tích kinh tế vĩ mô. "
            "Bạn sẽ học gross, domestic, nominal, real, per capita, output trong phần đầu tiên, "
            "nơi bài đọc giải thích GDP là gì và tại sao nó quan trọng với mọi quốc gia. "
            "Tiếp theo là indicator, index, inflation, deflation, growth, contraction — "
            "những từ giúp bạn đọc hiểu các báo cáo kinh tế và biểu đồ tăng trưởng. "
            "Cuối cùng, aggregate, productivity, benchmark, quarterly, annual, forecast "
            "đưa bạn vào thế giới dự báo và đánh giá hiệu suất kinh tế. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu báo cáo kinh tế vĩ mô bằng tiếng Anh — "
            "từ bản tin World Bank đến slide giảng viên."
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
                    "description": "Chào mừng bạn đến với bài học về GDP — thước đo sức khỏe nền kinh tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học đầu tiên trong chuỗi từ vựng Kinh tế vĩ mô — "
                            "chủ đề hôm nay là GDP và các chỉ số kinh tế, hay trong tiếng Anh là "
                            "GDP and Economic Indicators. Nếu kinh tế vi mô nhìn vào từng thị trường riêng lẻ, "
                            "thì kinh tế vĩ mô nhìn vào bức tranh toàn cảnh: cả nền kinh tế đang khỏe mạnh hay ốm yếu? "
                            "Và GDP chính là nhiệt kế đo sức khỏe đó.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: gross, domestic, nominal, real, per capita, và output. "
                            "Đây là những từ bạn sẽ gặp ngay khi mở bất kỳ báo cáo kinh tế nào bằng tiếng Anh.\n\n"
                            "Từ đầu tiên là gross — tính từ — trong kinh tế nghĩa là tổng, toàn bộ, "
                            "chưa trừ đi bất kỳ khoản nào. "
                            "Ví dụ: 'Gross domestic product measures the total value of all goods and services produced in a country.' "
                            "Trong bài đọc, gross luôn đi kèm với domestic product — "
                            "tổng sản phẩm quốc nội, con số mà mọi quốc gia đều theo dõi.\n\n"
                            "Từ thứ hai là domestic — tính từ — nghĩa là trong nước, thuộc về quốc gia. "
                            "Ví dụ: 'Domestic production includes everything made within the country's borders, regardless of who owns the factory.' "
                            "Trong bài đọc, domestic nhấn mạnh rằng GDP chỉ tính những gì sản xuất trong lãnh thổ quốc gia — "
                            "không tính hàng nhập khẩu.\n\n"
                            "Từ thứ ba là nominal — tính từ — nghĩa là danh nghĩa, "
                            "giá trị tính theo giá hiện hành, chưa điều chỉnh lạm phát. "
                            "Ví dụ: 'Nominal GDP in Vietnam rose from 262 billion dollars in 2019 to over 400 billion in 2023, but part of that increase was due to rising prices.' "
                            "Trong bài đọc, nominal GDP là con số 'thô' — nó có thể tăng chỉ vì giá tăng, "
                            "không phải vì sản xuất thực sự nhiều hơn.\n\n"
                            "Từ thứ tư là real — tính từ — nghĩa là thực tế, "
                            "giá trị đã được điều chỉnh lạm phát để phản ánh sức mua thật. "
                            "Ví dụ: 'Real GDP gives a more accurate picture of economic growth because it removes the effect of price changes.' "
                            "Trong bài đọc, real GDP là con số mà các nhà kinh tế thực sự quan tâm — "
                            "nó cho biết nền kinh tế có thật sự sản xuất nhiều hơn hay không.\n\n"
                            "Từ thứ năm là per capita — tính từ/trạng từ — nghĩa là bình quân đầu người, "
                            "tổng giá trị chia cho dân số. "
                            "Ví dụ: 'Vietnam's GDP per capita reached approximately 4,300 dollars in 2023, reflecting steady improvement in living standards.' "
                            "Trong bài đọc, per capita giúp so sánh mức sống giữa các quốc gia — "
                            "một nước có GDP lớn nhưng dân số đông thì per capita có thể thấp.\n\n"
                            "Từ cuối cùng là output — danh từ — nghĩa là sản lượng, "
                            "tổng lượng hàng hóa và dịch vụ được sản xuất ra. "
                            "Ví dụ: 'The factory's output doubled after the company invested in new machinery and hired more workers.' "
                            "Trong bài đọc, output là thành phần cốt lõi của GDP — "
                            "GDP đo lường tổng output của cả nền kinh tế trong một khoảng thời gian.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về GDP để thấy các từ này trong ngữ cảnh thực tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: GDP cơ bản",
                    "description": "Học 6 từ: gross, domestic, nominal, real, per capita, output",
                    "data": {"vocabList": ["gross", "domestic", "nominal", "real", "per capita", "output"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: GDP cơ bản",
                    "description": "Học 6 từ: gross, domestic, nominal, real, per capita, output",
                    "data": {"vocabList": ["gross", "domestic", "nominal", "real", "per capita", "output"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: GDP cơ bản",
                    "description": "Học 6 từ: gross, domestic, nominal, real, per capita, output",
                    "data": {"vocabList": ["gross", "domestic", "nominal", "real", "per capita", "output"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: GDP cơ bản",
                    "description": "Học 6 từ: gross, domestic, nominal, real, per capita, output",
                    "data": {"vocabList": ["gross", "domestic", "nominal", "real", "per capita", "output"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: GDP cơ bản",
                    "description": "Học 6 từ: gross, domestic, nominal, real, per capita, output",
                    "data": {"vocabList": ["gross", "domestic", "nominal", "real", "per capita", "output"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: GDP là gì và tại sao nó quan trọng",
                    "description": "If you want to know whether a country's economy is doing well, the first number to check is its gross domestic product.",
                    "data": {
                        "text": (
                            "If you want to know whether a country's economy is doing well, "
                            "the first number to check is its gross domestic product, or GDP. "
                            "GDP measures the total value of all goods and services produced within a country's borders "
                            "during a specific period, usually one year. It is the single most important number "
                            "in macroeconomics.\n\n"
                            "The word gross means total, before any deductions. "
                            "The word domestic means within the country. "
                            "So gross domestic product is the total output of a nation's economy, "
                            "counting everything from the rice harvested by farmers to the software written by engineers "
                            "to the haircuts given by barbers. If it was produced inside the country, it counts.\n\n"
                            "But not all GDP numbers tell the same story. "
                            "Nominal GDP measures output using current prices — the prices people actually pay today. "
                            "If the price of a bowl of pho rises from thirty thousand dong to forty thousand dong, "
                            "nominal GDP goes up even if the same number of bowls were sold. "
                            "This can be misleading because it mixes real production changes with price changes.\n\n"
                            "That is why economists prefer real GDP. "
                            "Real GDP adjusts for price changes by using the prices from a fixed base year. "
                            "If real GDP rises, it means the economy truly produced more goods and services — "
                            "not just that prices went up. The difference between nominal and real GDP "
                            "is one of the most important distinctions in macroeconomics.\n\n"
                            "Another useful measure is GDP per capita, which divides the total GDP by the population. "
                            "A country like China has an enormous GDP, but because it has over one billion people, "
                            "its GDP per capita is much lower than that of a smaller, wealthier country like Singapore. "
                            "Per capita figures give a better sense of the average person's standard of living.\n\n"
                            "Output is at the heart of GDP. Every factory, farm, office, and shop contributes to output. "
                            "When output rises, the economy grows. When output falls, the economy shrinks. "
                            "Tracking output over time tells us whether a country is moving forward or falling behind."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: GDP là gì và tại sao nó quan trọng",
                    "description": "If you want to know whether a country's economy is doing well, the first number to check is its gross domestic product.",
                    "data": {
                        "text": (
                            "If you want to know whether a country's economy is doing well, "
                            "the first number to check is its gross domestic product, or GDP. "
                            "GDP measures the total value of all goods and services produced within a country's borders "
                            "during a specific period, usually one year. It is the single most important number "
                            "in macroeconomics.\n\n"
                            "The word gross means total, before any deductions. "
                            "The word domestic means within the country. "
                            "So gross domestic product is the total output of a nation's economy, "
                            "counting everything from the rice harvested by farmers to the software written by engineers "
                            "to the haircuts given by barbers. If it was produced inside the country, it counts.\n\n"
                            "But not all GDP numbers tell the same story. "
                            "Nominal GDP measures output using current prices — the prices people actually pay today. "
                            "If the price of a bowl of pho rises from thirty thousand dong to forty thousand dong, "
                            "nominal GDP goes up even if the same number of bowls were sold. "
                            "This can be misleading because it mixes real production changes with price changes.\n\n"
                            "That is why economists prefer real GDP. "
                            "Real GDP adjusts for price changes by using the prices from a fixed base year. "
                            "If real GDP rises, it means the economy truly produced more goods and services — "
                            "not just that prices went up. The difference between nominal and real GDP "
                            "is one of the most important distinctions in macroeconomics.\n\n"
                            "Another useful measure is GDP per capita, which divides the total GDP by the population. "
                            "A country like China has an enormous GDP, but because it has over one billion people, "
                            "its GDP per capita is much lower than that of a smaller, wealthier country like Singapore. "
                            "Per capita figures give a better sense of the average person's standard of living.\n\n"
                            "Output is at the heart of GDP. Every factory, farm, office, and shop contributes to output. "
                            "When output rises, the economy grows. When output falls, the economy shrinks. "
                            "Tracking output over time tells us whether a country is moving forward or falling behind."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: GDP là gì và tại sao nó quan trọng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "If you want to know whether a country's economy is doing well, "
                            "the first number to check is its gross domestic product, or GDP. "
                            "GDP measures the total value of all goods and services produced within a country's borders "
                            "during a specific period, usually one year. It is the single most important number "
                            "in macroeconomics.\n\n"
                            "The word gross means total, before any deductions. "
                            "The word domestic means within the country. "
                            "So gross domestic product is the total output of a nation's economy, "
                            "counting everything from the rice harvested by farmers to the software written by engineers "
                            "to the haircuts given by barbers. If it was produced inside the country, it counts.\n\n"
                            "But not all GDP numbers tell the same story. "
                            "Nominal GDP measures output using current prices — the prices people actually pay today. "
                            "If the price of a bowl of pho rises from thirty thousand dong to forty thousand dong, "
                            "nominal GDP goes up even if the same number of bowls were sold. "
                            "This can be misleading because it mixes real production changes with price changes.\n\n"
                            "That is why economists prefer real GDP. "
                            "Real GDP adjusts for price changes by using the prices from a fixed base year. "
                            "If real GDP rises, it means the economy truly produced more goods and services — "
                            "not just that prices went up. The difference between nominal and real GDP "
                            "is one of the most important distinctions in macroeconomics.\n\n"
                            "Another useful measure is GDP per capita, which divides the total GDP by the population. "
                            "A country like China has an enormous GDP, but because it has over one billion people, "
                            "its GDP per capita is much lower than that of a smaller, wealthier country like Singapore. "
                            "Per capita figures give a better sense of the average person's standard of living.\n\n"
                            "Output is at the heart of GDP. Every factory, farm, office, and shop contributes to output. "
                            "When output rises, the economy grows. When output falls, the economy shrinks. "
                            "Tracking output over time tells us whether a country is moving forward or falling behind."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: GDP cơ bản",
                    "description": "Viết câu sử dụng 6 từ vựng về GDP.",
                    "data": {
                        "vocabList": ["gross", "domestic", "nominal", "real", "per capita", "output"],
                        "items": [
                            {
                                "targetVocab": "gross",
                                "prompt": "Dùng từ 'gross' để viết một câu về tổng giá trị sản xuất của một quốc gia trước khi trừ các khoản khấu hao. Ví dụ: The gross value of Vietnam's manufacturing sector exceeded one hundred billion dollars last year, making it the largest contributor to the national economy."
                            },
                            {
                                "targetVocab": "domestic",
                                "prompt": "Dùng từ 'domestic' để viết một câu về sản xuất trong nước so với nhập khẩu. Ví dụ: The government launched a campaign to encourage consumers to buy domestic products instead of imported goods to support local businesses."
                            },
                            {
                                "targetVocab": "nominal",
                                "prompt": "Dùng từ 'nominal' để viết một câu về sự khác biệt giữa giá trị danh nghĩa và giá trị thực. Ví dụ: The nominal salary of a factory worker has doubled over the past decade, but after adjusting for inflation, the real increase is much smaller."
                            },
                            {
                                "targetVocab": "real",
                                "prompt": "Dùng từ 'real' để viết một câu về GDP thực tế sau khi điều chỉnh lạm phát. Ví dụ: Real GDP growth of six percent means the economy actually produced six percent more goods and services, not just that prices rose."
                            },
                            {
                                "targetVocab": "per capita",
                                "prompt": "Dùng từ 'per capita' để viết một câu so sánh mức sống bình quân đầu người giữa hai quốc gia. Ví dụ: Although Indonesia's total GDP is larger than Singapore's, Singapore's GDP per capita is nearly ten times higher because of its much smaller population."
                            },
                            {
                                "targetVocab": "output",
                                "prompt": "Dùng từ 'output' để viết một câu về sản lượng của một ngành kinh tế cụ thể. Ví dụ: The agricultural output of the Mekong Delta accounts for more than half of Vietnam's total rice production each year."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về chỉ số kinh tế và chu kỳ tăng trưởng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "gross — tổng, domestic — trong nước, nominal — danh nghĩa, "
                            "real — thực tế, per capita — bình quân đầu người, và output — sản lượng. "
                            "Bạn đã hiểu GDP là gì và tại sao nó là thước đo quan trọng nhất của nền kinh tế. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào các chỉ số đo lường sức khỏe kinh tế.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: indicator, index, inflation, deflation, growth, và contraction. "
                            "Những từ này giúp bạn đọc hiểu các bản tin kinh tế — "
                            "khi nào nền kinh tế đang tăng trưởng, khi nào đang suy thoái, "
                            "và giá cả đang biến động ra sao.\n\n"
                            "Từ đầu tiên là indicator — danh từ — nghĩa là chỉ số, chỉ báo, "
                            "một con số hoặc dữ liệu cho biết tình trạng của nền kinh tế. "
                            "Ví dụ: 'The unemployment rate is a key economic indicator that tells us how many people are looking for work but cannot find it.' "
                            "Trong bài đọc, indicator xuất hiện khi nói về các công cụ mà nhà kinh tế dùng "
                            "để chẩn đoán sức khỏe nền kinh tế — giống như bác sĩ dùng nhiệt kế và huyết áp.\n\n"
                            "Từ thứ hai là index — danh từ — nghĩa là chỉ số tổng hợp, "
                            "một con số được tính từ nhiều thành phần để đo lường xu hướng chung. "
                            "Ví dụ: 'The Consumer Price Index tracks the average change in prices paid by households for a basket of common goods and services.' "
                            "Trong bài đọc, index là cách các nhà thống kê gom nhiều dữ liệu "
                            "thành một con số duy nhất dễ theo dõi.\n\n"
                            "Từ thứ ba là inflation — danh từ — nghĩa là lạm phát, "
                            "sự tăng liên tục của mặt bằng giá cả trong nền kinh tế. "
                            "Ví dụ: 'When inflation is high, the money in your pocket buys less than it did last year.' "
                            "Trong bài đọc, inflation giải thích vì sao nominal GDP có thể tăng "
                            "mà đời sống người dân không thực sự cải thiện.\n\n"
                            "Từ thứ tư là deflation — danh từ — nghĩa là giảm phát, "
                            "sự giảm liên tục của mặt bằng giá cả — ngược lại với inflation. "
                            "Ví dụ: 'Japan experienced deflation for nearly two decades, which discouraged spending because consumers expected prices to keep falling.' "
                            "Trong bài đọc, deflation nghe có vẻ tốt nhưng thực ra rất nguy hiểm — "
                            "khi giá giảm, doanh nghiệp thu ít hơn, cắt giảm nhân sự, và nền kinh tế đi xuống.\n\n"
                            "Từ thứ năm là growth — danh từ — nghĩa là tăng trưởng, "
                            "sự gia tăng sản lượng hoặc giá trị kinh tế qua thời gian. "
                            "Ví dụ: 'Vietnam achieved an average GDP growth rate of about six percent per year over the past decade.' "
                            "Trong bài đọc, growth là mục tiêu mà mọi chính phủ theo đuổi — "
                            "nền kinh tế tăng trưởng nghĩa là có thêm việc làm, thu nhập, và cơ hội.\n\n"
                            "Từ cuối cùng là contraction — danh từ — nghĩa là suy giảm, co hẹp, "
                            "khi sản lượng kinh tế giảm xuống. "
                            "Ví dụ: 'The economy entered a contraction during the pandemic as factories closed and consumer spending dropped sharply.' "
                            "Trong bài đọc, contraction là mặt đối lập của growth — "
                            "khi GDP giảm hai quý liên tiếp, các nhà kinh tế gọi đó là suy thoái.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về các chỉ số kinh tế và chu kỳ tăng trưởng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Học 6 từ: indicator, index, inflation, deflation, growth, contraction",
                    "data": {"vocabList": ["indicator", "index", "inflation", "deflation", "growth", "contraction"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Học 6 từ: indicator, index, inflation, deflation, growth, contraction",
                    "data": {"vocabList": ["indicator", "index", "inflation", "deflation", "growth", "contraction"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Học 6 từ: indicator, index, inflation, deflation, growth, contraction",
                    "data": {"vocabList": ["indicator", "index", "inflation", "deflation", "growth", "contraction"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Học 6 từ: indicator, index, inflation, deflation, growth, contraction",
                    "data": {"vocabList": ["indicator", "index", "inflation", "deflation", "growth", "contraction"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Học 6 từ: indicator, index, inflation, deflation, growth, contraction",
                    "data": {"vocabList": ["indicator", "index", "inflation", "deflation", "growth", "contraction"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Economists do not rely on a single number to judge the health of an economy.",
                    "data": {
                        "text": (
                            "Economists do not rely on a single number to judge the health of an economy. "
                            "They use a collection of economic indicators — data points that reveal "
                            "whether the economy is expanding, slowing down, or heading into trouble.\n\n"
                            "One of the most widely watched indicators is the rate of economic growth. "
                            "Growth measures how much the total output of an economy increases over time. "
                            "When real GDP rises from one year to the next, the economy is growing. "
                            "More goods are being produced, more services are being delivered, "
                            "and generally more people have jobs. "
                            "Vietnam, for example, has been one of the fastest-growing economies in Southeast Asia, "
                            "with growth rates often exceeding six percent per year.\n\n"
                            "But economies do not grow forever in a straight line. "
                            "Sometimes output falls. When the total production of goods and services declines, "
                            "the economy enters a contraction. "
                            "During a contraction, businesses sell less, factories cut production, "
                            "and workers may lose their jobs. "
                            "If a contraction lasts for two consecutive quarters — six months — "
                            "economists call it a recession.\n\n"
                            "To track price changes across the economy, statisticians create an index. "
                            "The most famous is the Consumer Price Index, or CPI. "
                            "The CPI measures the average change in prices that households pay "
                            "for a standard basket of goods — food, housing, transportation, clothing, and more. "
                            "When the index rises over time, it signals inflation.\n\n"
                            "Inflation means that the general level of prices is going up. "
                            "A moderate rate of inflation — around two to three percent per year — "
                            "is considered normal and even healthy. "
                            "It encourages people to spend and invest rather than hold cash. "
                            "But when inflation climbs too high, it erodes purchasing power. "
                            "The money in your wallet buys fewer goods than it did last month.\n\n"
                            "The opposite of inflation is deflation — a sustained decrease in the general price level. "
                            "Deflation might sound like good news for shoppers, but it can be dangerous for the economy. "
                            "When prices fall, consumers delay purchases because they expect even lower prices tomorrow. "
                            "Businesses earn less revenue, cut costs, and lay off workers. "
                            "This downward spiral can turn a mild contraction into a deep recession.\n\n"
                            "Each of these indicators — growth rate, CPI, inflation rate — "
                            "tells a different part of the economic story. "
                            "Together, they give policymakers and business leaders the information they need "
                            "to make decisions that affect millions of people."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Economists do not rely on a single number to judge the health of an economy.",
                    "data": {
                        "text": (
                            "Economists do not rely on a single number to judge the health of an economy. "
                            "They use a collection of economic indicators — data points that reveal "
                            "whether the economy is expanding, slowing down, or heading into trouble.\n\n"
                            "One of the most widely watched indicators is the rate of economic growth. "
                            "Growth measures how much the total output of an economy increases over time. "
                            "When real GDP rises from one year to the next, the economy is growing. "
                            "More goods are being produced, more services are being delivered, "
                            "and generally more people have jobs. "
                            "Vietnam, for example, has been one of the fastest-growing economies in Southeast Asia, "
                            "with growth rates often exceeding six percent per year.\n\n"
                            "But economies do not grow forever in a straight line. "
                            "Sometimes output falls. When the total production of goods and services declines, "
                            "the economy enters a contraction. "
                            "During a contraction, businesses sell less, factories cut production, "
                            "and workers may lose their jobs. "
                            "If a contraction lasts for two consecutive quarters — six months — "
                            "economists call it a recession.\n\n"
                            "To track price changes across the economy, statisticians create an index. "
                            "The most famous is the Consumer Price Index, or CPI. "
                            "The CPI measures the average change in prices that households pay "
                            "for a standard basket of goods — food, housing, transportation, clothing, and more. "
                            "When the index rises over time, it signals inflation.\n\n"
                            "Inflation means that the general level of prices is going up. "
                            "A moderate rate of inflation — around two to three percent per year — "
                            "is considered normal and even healthy. "
                            "It encourages people to spend and invest rather than hold cash. "
                            "But when inflation climbs too high, it erodes purchasing power. "
                            "The money in your wallet buys fewer goods than it did last month.\n\n"
                            "The opposite of inflation is deflation — a sustained decrease in the general price level. "
                            "Deflation might sound like good news for shoppers, but it can be dangerous for the economy. "
                            "When prices fall, consumers delay purchases because they expect even lower prices tomorrow. "
                            "Businesses earn less revenue, cut costs, and lay off workers. "
                            "This downward spiral can turn a mild contraction into a deep recession.\n\n"
                            "Each of these indicators — growth rate, CPI, inflation rate — "
                            "tells a different part of the economic story. "
                            "Together, they give policymakers and business leaders the information they need "
                            "to make decisions that affect millions of people."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Economists do not rely on a single number to judge the health of an economy. "
                            "They use a collection of economic indicators — data points that reveal "
                            "whether the economy is expanding, slowing down, or heading into trouble.\n\n"
                            "One of the most widely watched indicators is the rate of economic growth. "
                            "Growth measures how much the total output of an economy increases over time. "
                            "When real GDP rises from one year to the next, the economy is growing. "
                            "More goods are being produced, more services are being delivered, "
                            "and generally more people have jobs. "
                            "Vietnam, for example, has been one of the fastest-growing economies in Southeast Asia, "
                            "with growth rates often exceeding six percent per year.\n\n"
                            "But economies do not grow forever in a straight line. "
                            "Sometimes output falls. When the total production of goods and services declines, "
                            "the economy enters a contraction. "
                            "During a contraction, businesses sell less, factories cut production, "
                            "and workers may lose their jobs. "
                            "If a contraction lasts for two consecutive quarters — six months — "
                            "economists call it a recession.\n\n"
                            "To track price changes across the economy, statisticians create an index. "
                            "The most famous is the Consumer Price Index, or CPI. "
                            "The CPI measures the average change in prices that households pay "
                            "for a standard basket of goods — food, housing, transportation, clothing, and more. "
                            "When the index rises over time, it signals inflation.\n\n"
                            "Inflation means that the general level of prices is going up. "
                            "A moderate rate of inflation — around two to three percent per year — "
                            "is considered normal and even healthy. "
                            "It encourages people to spend and invest rather than hold cash. "
                            "But when inflation climbs too high, it erodes purchasing power. "
                            "The money in your wallet buys fewer goods than it did last month.\n\n"
                            "The opposite of inflation is deflation — a sustained decrease in the general price level. "
                            "Deflation might sound like good news for shoppers, but it can be dangerous for the economy. "
                            "When prices fall, consumers delay purchases because they expect even lower prices tomorrow. "
                            "Businesses earn less revenue, cut costs, and lay off workers. "
                            "This downward spiral can turn a mild contraction into a deep recession.\n\n"
                            "Each of these indicators — growth rate, CPI, inflation rate — "
                            "tells a different part of the economic story. "
                            "Together, they give policymakers and business leaders the information they need "
                            "to make decisions that affect millions of people."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chỉ số kinh tế và chu kỳ tăng trưởng",
                    "description": "Viết câu sử dụng 6 từ vựng về chỉ số kinh tế.",
                    "data": {
                        "vocabList": ["indicator", "index", "inflation", "deflation", "growth", "contraction"],
                        "items": [
                            {
                                "targetVocab": "indicator",
                                "prompt": "Dùng từ 'indicator' để viết một câu về một chỉ số kinh tế mà chính phủ sử dụng để đánh giá tình hình kinh tế. Ví dụ: The unemployment rate is a lagging indicator because it tends to rise even after the economy has already started recovering."
                            },
                            {
                                "targetVocab": "index",
                                "prompt": "Dùng từ 'index' để viết một câu về chỉ số giá tiêu dùng hoặc một chỉ số tổng hợp khác. Ví dụ: The stock market index dropped by three percent in a single day after the central bank announced higher interest rates."
                            },
                            {
                                "targetVocab": "inflation",
                                "prompt": "Dùng từ 'inflation' để viết một câu về tác động của lạm phát đến đời sống người dân. Ví dụ: High inflation means that a family's monthly grocery bill keeps rising even though they are buying the same items as before."
                            },
                            {
                                "targetVocab": "deflation",
                                "prompt": "Dùng từ 'deflation' để viết một câu về nguy cơ của giảm phát đối với nền kinh tế. Ví dụ: During a period of deflation, businesses struggle to maintain profits because the prices of their products keep falling while their costs remain fixed."
                            },
                            {
                                "targetVocab": "growth",
                                "prompt": "Dùng từ 'growth' để viết một câu về tốc độ tăng trưởng kinh tế của một quốc gia. Ví dụ: Sustained economic growth over the past thirty years has lifted millions of Vietnamese people out of poverty and into the middle class."
                            },
                            {
                                "targetVocab": "contraction",
                                "prompt": "Dùng từ 'contraction' để viết một câu về giai đoạn suy giảm kinh tế và tác động của nó. Ví dụ: The sharp contraction in the tourism industry during the pandemic caused thousands of hotels and restaurants to close permanently."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về năng suất, chuẩn đo lường và dự báo kinh tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: gross, domestic, nominal, real, per capita, output — "
                            "những khái niệm cơ bản để hiểu GDP là gì. "
                            "Trong phần 2, bạn đã học thêm indicator, index, inflation, deflation, growth, contraction — "
                            "giúp bạn đọc hiểu các chỉ số kinh tế và nhận biết chu kỳ tăng trưởng.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào thế giới của dự báo và đánh giá hiệu suất kinh tế. "
                            "Bạn sẽ học 6 từ mới: aggregate, productivity, benchmark, quarterly, annual, và forecast.\n\n"
                            "Từ đầu tiên là aggregate — tính từ/danh từ — nghĩa là tổng hợp, gộp lại, "
                            "tổng cộng của nhiều thành phần riêng lẻ. "
                            "Ví dụ: 'Aggregate demand is the total demand for all goods and services in an economy at a given price level.' "
                            "Trong bài đọc, aggregate được dùng khi nói về toàn bộ nền kinh tế — "
                            "không phải một thị trường đơn lẻ mà là tổng hợp tất cả các thị trường.\n\n"
                            "Từ thứ hai là productivity — danh từ — nghĩa là năng suất, "
                            "lượng sản phẩm hoặc giá trị tạo ra trên mỗi đơn vị lao động hoặc nguồn lực. "
                            "Ví dụ: 'Labor productivity in Vietnam's technology sector has increased significantly thanks to better training and modern equipment.' "
                            "Trong bài đọc, productivity giải thích vì sao một số quốc gia giàu hơn — "
                            "không phải vì họ làm việc nhiều giờ hơn, mà vì mỗi giờ làm việc tạo ra nhiều giá trị hơn.\n\n"
                            "Từ thứ ba là benchmark — danh từ — nghĩa là chuẩn đo lường, mốc so sánh, "
                            "một tiêu chuẩn dùng để đánh giá hiệu suất. "
                            "Ví dụ: 'Many developing countries use Singapore's GDP per capita as a benchmark for their own economic development goals.' "
                            "Trong bài đọc, benchmark là điểm tham chiếu — "
                            "các nhà kinh tế so sánh số liệu hiện tại với benchmark để biết nền kinh tế đang tiến hay lùi.\n\n"
                            "Từ thứ tư là quarterly — tính từ/trạng từ — nghĩa là hàng quý, mỗi ba tháng một lần. "
                            "Ví dụ: 'The government releases quarterly GDP data so that economists can track economic performance throughout the year.' "
                            "Trong bài đọc, quarterly nhấn mạnh rằng GDP không chỉ được tính hàng năm — "
                            "dữ liệu hàng quý giúp phát hiện sớm các dấu hiệu suy thoái.\n\n"
                            "Từ thứ năm là annual — tính từ — nghĩa là hàng năm, tính theo năm. "
                            "Ví dụ: 'The annual report from the World Bank provides a comprehensive overview of global economic trends.' "
                            "Trong bài đọc, annual thường đi kèm với growth rate hoặc GDP — "
                            "tốc độ tăng trưởng hàng năm là con số được trích dẫn nhiều nhất trong báo cáo kinh tế.\n\n"
                            "Từ cuối cùng là forecast — danh từ/động từ — nghĩa là dự báo, "
                            "ước tính về tình hình kinh tế trong tương lai dựa trên dữ liệu hiện tại. "
                            "Ví dụ: 'The IMF's latest forecast predicts that Vietnam's economy will grow by six point five percent next year.' "
                            "Trong bài đọc, forecast là công cụ quan trọng — "
                            "chính phủ và doanh nghiệp dựa vào dự báo để lập kế hoạch ngân sách và đầu tư.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về năng suất, chuẩn đo lường và dự báo kinh tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Năng suất, chuẩn đo lường và dự báo",
                    "description": "Học 6 từ: aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Năng suất, chuẩn đo lường và dự báo",
                    "description": "Học 6 từ: aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Năng suất, chuẩn đo lường và dự báo",
                    "description": "Học 6 từ: aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Năng suất, chuẩn đo lường và dự báo",
                    "description": "Học 6 từ: aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Năng suất, chuẩn đo lường và dự báo",
                    "description": "Học 6 từ: aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Năng suất, chuẩn đo lường và dự báo kinh tế",
                    "description": "Knowing that an economy is growing is useful, but policymakers need to understand why it is growing and where it is headed.",
                    "data": {
                        "text": (
                            "Knowing that an economy is growing is useful, but policymakers need to understand "
                            "why it is growing and where it is headed. "
                            "That is where concepts like aggregate output, productivity, and economic forecasting come in.\n\n"
                            "Aggregate output refers to the total production of all goods and services in an economy. "
                            "When economists talk about aggregate demand or aggregate supply, "
                            "they are looking at the entire economy as a whole, not just one market. "
                            "Aggregate demand is the total spending by households, businesses, the government, "
                            "and foreign buyers. When aggregate demand rises, businesses produce more, "
                            "and the economy tends to grow.\n\n"
                            "But growth is not just about producing more — it is about producing more efficiently. "
                            "Productivity measures how much output is created per unit of input. "
                            "If a factory can make one hundred shirts per worker per day instead of eighty, "
                            "its productivity has increased by twenty-five percent. "
                            "Higher productivity is the main driver of long-term economic growth. "
                            "Countries with high productivity tend to have higher GDP per capita "
                            "and better living standards.\n\n"
                            "To evaluate economic performance, analysts often compare current data against a benchmark. "
                            "A benchmark is a standard point of reference. "
                            "For example, a country might use its own GDP growth rate from five years ago as a benchmark "
                            "to see whether the economy is speeding up or slowing down. "
                            "International organizations like the World Bank also set benchmarks — "
                            "such as the income threshold that separates low-income countries from middle-income ones.\n\n"
                            "Economic data is collected and reported at regular intervals. "
                            "Quarterly reports, published every three months, give a timely snapshot of the economy. "
                            "If quarterly GDP falls for two consecutive periods, "
                            "the economy is technically in a recession. "
                            "Annual data, covering a full twelve months, provides a broader view "
                            "and is often used for year-over-year comparisons.\n\n"
                            "Perhaps the most important use of economic data is forecasting. "
                            "A forecast is an estimate of future economic conditions based on current trends and models. "
                            "The International Monetary Fund, the World Bank, and national governments "
                            "all publish regular forecasts. "
                            "These forecasts influence everything from government budgets to business investment decisions. "
                            "If a forecast predicts strong growth, businesses may expand and hire more workers. "
                            "If it predicts a contraction, they may cut costs and delay new projects.\n\n"
                            "No forecast is perfect — the economy is shaped by millions of unpredictable decisions. "
                            "But by combining aggregate data, productivity trends, and benchmark comparisons, "
                            "economists can paint a reasonably accurate picture of where the economy is going."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Năng suất, chuẩn đo lường và dự báo kinh tế",
                    "description": "Knowing that an economy is growing is useful, but policymakers need to understand why it is growing and where it is headed.",
                    "data": {
                        "text": (
                            "Knowing that an economy is growing is useful, but policymakers need to understand "
                            "why it is growing and where it is headed. "
                            "That is where concepts like aggregate output, productivity, and economic forecasting come in.\n\n"
                            "Aggregate output refers to the total production of all goods and services in an economy. "
                            "When economists talk about aggregate demand or aggregate supply, "
                            "they are looking at the entire economy as a whole, not just one market. "
                            "Aggregate demand is the total spending by households, businesses, the government, "
                            "and foreign buyers. When aggregate demand rises, businesses produce more, "
                            "and the economy tends to grow.\n\n"
                            "But growth is not just about producing more — it is about producing more efficiently. "
                            "Productivity measures how much output is created per unit of input. "
                            "If a factory can make one hundred shirts per worker per day instead of eighty, "
                            "its productivity has increased by twenty-five percent. "
                            "Higher productivity is the main driver of long-term economic growth. "
                            "Countries with high productivity tend to have higher GDP per capita "
                            "and better living standards.\n\n"
                            "To evaluate economic performance, analysts often compare current data against a benchmark. "
                            "A benchmark is a standard point of reference. "
                            "For example, a country might use its own GDP growth rate from five years ago as a benchmark "
                            "to see whether the economy is speeding up or slowing down. "
                            "International organizations like the World Bank also set benchmarks — "
                            "such as the income threshold that separates low-income countries from middle-income ones.\n\n"
                            "Economic data is collected and reported at regular intervals. "
                            "Quarterly reports, published every three months, give a timely snapshot of the economy. "
                            "If quarterly GDP falls for two consecutive periods, "
                            "the economy is technically in a recession. "
                            "Annual data, covering a full twelve months, provides a broader view "
                            "and is often used for year-over-year comparisons.\n\n"
                            "Perhaps the most important use of economic data is forecasting. "
                            "A forecast is an estimate of future economic conditions based on current trends and models. "
                            "The International Monetary Fund, the World Bank, and national governments "
                            "all publish regular forecasts. "
                            "These forecasts influence everything from government budgets to business investment decisions. "
                            "If a forecast predicts strong growth, businesses may expand and hire more workers. "
                            "If it predicts a contraction, they may cut costs and delay new projects.\n\n"
                            "No forecast is perfect — the economy is shaped by millions of unpredictable decisions. "
                            "But by combining aggregate data, productivity trends, and benchmark comparisons, "
                            "economists can paint a reasonably accurate picture of where the economy is going."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Năng suất, chuẩn đo lường và dự báo kinh tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Knowing that an economy is growing is useful, but policymakers need to understand "
                            "why it is growing and where it is headed. "
                            "That is where concepts like aggregate output, productivity, and economic forecasting come in.\n\n"
                            "Aggregate output refers to the total production of all goods and services in an economy. "
                            "When economists talk about aggregate demand or aggregate supply, "
                            "they are looking at the entire economy as a whole, not just one market. "
                            "Aggregate demand is the total spending by households, businesses, the government, "
                            "and foreign buyers. When aggregate demand rises, businesses produce more, "
                            "and the economy tends to grow.\n\n"
                            "But growth is not just about producing more — it is about producing more efficiently. "
                            "Productivity measures how much output is created per unit of input. "
                            "If a factory can make one hundred shirts per worker per day instead of eighty, "
                            "its productivity has increased by twenty-five percent. "
                            "Higher productivity is the main driver of long-term economic growth. "
                            "Countries with high productivity tend to have higher GDP per capita "
                            "and better living standards.\n\n"
                            "To evaluate economic performance, analysts often compare current data against a benchmark. "
                            "A benchmark is a standard point of reference. "
                            "For example, a country might use its own GDP growth rate from five years ago as a benchmark "
                            "to see whether the economy is speeding up or slowing down. "
                            "International organizations like the World Bank also set benchmarks — "
                            "such as the income threshold that separates low-income countries from middle-income ones.\n\n"
                            "Economic data is collected and reported at regular intervals. "
                            "Quarterly reports, published every three months, give a timely snapshot of the economy. "
                            "If quarterly GDP falls for two consecutive periods, "
                            "the economy is technically in a recession. "
                            "Annual data, covering a full twelve months, provides a broader view "
                            "and is often used for year-over-year comparisons.\n\n"
                            "Perhaps the most important use of economic data is forecasting. "
                            "A forecast is an estimate of future economic conditions based on current trends and models. "
                            "The International Monetary Fund, the World Bank, and national governments "
                            "all publish regular forecasts. "
                            "These forecasts influence everything from government budgets to business investment decisions. "
                            "If a forecast predicts strong growth, businesses may expand and hire more workers. "
                            "If it predicts a contraction, they may cut costs and delay new projects.\n\n"
                            "No forecast is perfect — the economy is shaped by millions of unpredictable decisions. "
                            "But by combining aggregate data, productivity trends, and benchmark comparisons, "
                            "economists can paint a reasonably accurate picture of where the economy is going."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Năng suất, chuẩn đo lường và dự báo",
                    "description": "Viết câu sử dụng 6 từ vựng về năng suất và dự báo kinh tế.",
                    "data": {
                        "vocabList": ["aggregate", "productivity", "benchmark", "quarterly", "annual", "forecast"],
                        "items": [
                            {
                                "targetVocab": "aggregate",
                                "prompt": "Dùng từ 'aggregate' để viết một câu về tổng cầu hoặc tổng cung trong nền kinh tế. Ví dụ: When the government increases public spending, aggregate demand rises because more money flows into the economy through construction projects and public services."
                            },
                            {
                                "targetVocab": "productivity",
                                "prompt": "Dùng từ 'productivity' để viết một câu về năng suất lao động trong một ngành cụ thể. Ví dụ: The introduction of automated assembly lines boosted productivity at the electronics factory by forty percent, allowing the same number of workers to produce far more units."
                            },
                            {
                                "targetVocab": "benchmark",
                                "prompt": "Dùng từ 'benchmark' để viết một câu về việc sử dụng một tiêu chuẩn để đánh giá hiệu suất kinh tế. Ví dụ: The government uses the average GDP growth rate of ASEAN countries as a benchmark to evaluate whether Vietnam's economy is keeping pace with its regional peers."
                            },
                            {
                                "targetVocab": "quarterly",
                                "prompt": "Dùng từ 'quarterly' để viết một câu về báo cáo kinh tế được công bố mỗi ba tháng. Ví dụ: The quarterly GDP report showed that the economy grew by one point eight percent in the third quarter, slightly above the forecast."
                            },
                            {
                                "targetVocab": "annual",
                                "prompt": "Dùng từ 'annual' để viết một câu về dữ liệu hoặc báo cáo kinh tế hàng năm. Ví dụ: The company's annual revenue exceeded five billion dollars for the first time, reflecting strong demand for its products across Southeast Asia."
                            },
                            {
                                "targetVocab": "forecast",
                                "prompt": "Dùng từ 'forecast' để viết một câu về dự báo kinh tế từ một tổ chức quốc tế. Ví dụ: The Asian Development Bank revised its growth forecast for Vietnam upward after the country reported stronger-than-expected export numbers in the first half of the year."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về GDP và Chỉ Số Kinh Tế. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "gross — tổng, domestic — trong nước, nominal — danh nghĩa, "
                            "real — thực tế, per capita — bình quân đầu người, và output — sản lượng. "
                            "Đây là bộ khung cơ bản để hiểu GDP — thước đo quan trọng nhất của nền kinh tế.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "indicator — chỉ báo, index — chỉ số tổng hợp, inflation — lạm phát, "
                            "deflation — giảm phát, growth — tăng trưởng, và contraction — suy giảm. "
                            "Những từ này giúp bạn đọc hiểu các bản tin kinh tế và nhận biết chu kỳ kinh tế.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "aggregate — tổng hợp, productivity — năng suất, benchmark — chuẩn đo lường, "
                            "quarterly — hàng quý, annual — hàng năm, và forecast — dự báo. "
                            "Đây là những từ về phân tích và dự báo kinh tế vĩ mô.\n\n"
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
                    "description": "Học 18 từ: gross, domestic, nominal, real, per capita, output, indicator, index, inflation, deflation, growth, contraction, aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: gross, domestic, nominal, real, per capita, output, indicator, index, inflation, deflation, growth, contraction, aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: gross, domestic, nominal, real, per capita, output, indicator, index, inflation, deflation, growth, contraction, aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: gross, domestic, nominal, real, per capita, output, indicator, index, inflation, deflation, growth, contraction, aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: gross, domestic, nominal, real, per capita, output, indicator, index, inflation, deflation, growth, contraction, aggregate, productivity, benchmark, quarterly, annual, forecast",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng GDP và chỉ số kinh tế",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "gross",
                                "prompt": "Dùng từ 'gross' để viết một câu về tổng giá trị kinh tế của một quốc gia hoặc ngành. Ví dụ: The gross national income of Vietnam has been rising steadily, reflecting the country's transition from an agricultural economy to a manufacturing and services hub."
                            },
                            {
                                "targetVocab": "domestic",
                                "prompt": "Dùng từ 'domestic' để viết một câu về thị trường nội địa hoặc sản xuất trong nước. Ví dụ: Domestic consumption accounts for nearly seventy percent of the country's GDP, making it the primary engine of economic growth."
                            },
                            {
                                "targetVocab": "nominal",
                                "prompt": "Dùng từ 'nominal' để viết một câu so sánh giá trị danh nghĩa với giá trị thực. Ví dụ: The nominal interest rate offered by the bank is eight percent, but after subtracting the inflation rate of four percent, the real return on savings is only four percent."
                            },
                            {
                                "targetVocab": "real",
                                "prompt": "Dùng từ 'real' để viết một câu về tăng trưởng thực tế sau khi loại bỏ yếu tố lạm phát. Ví dụ: Real wages in the manufacturing sector have barely increased over the past five years because inflation has eaten into most of the nominal pay raises."
                            },
                            {
                                "targetVocab": "per capita",
                                "prompt": "Dùng từ 'per capita' để viết một câu về mức chi tiêu hoặc thu nhập bình quân đầu người. Ví dụ: Healthcare spending per capita in Vietnam is still much lower than in neighboring Thailand, which partly explains the gap in hospital infrastructure."
                            },
                            {
                                "targetVocab": "output",
                                "prompt": "Dùng từ 'output' để viết một câu về sản lượng của một ngành hoặc nền kinh tế. Ví dụ: The total industrial output of the northern provinces grew by nine percent last year, driven by new foreign-invested electronics factories."
                            },
                            {
                                "targetVocab": "indicator",
                                "prompt": "Dùng từ 'indicator' để viết một câu về một chỉ báo kinh tế cụ thể và ý nghĩa của nó. Ví dụ: Retail sales are a leading indicator of consumer confidence — when people spend more at shops, it usually means they feel optimistic about the economy."
                            },
                            {
                                "targetVocab": "index",
                                "prompt": "Dùng từ 'index' để viết một câu về một chỉ số tổng hợp được sử dụng trong phân tích kinh tế. Ví dụ: The Purchasing Managers' Index fell below fifty for the third consecutive month, signaling that the manufacturing sector is contracting."
                            },
                            {
                                "targetVocab": "inflation",
                                "prompt": "Dùng từ 'inflation' để viết một câu về tác động của lạm phát đến chính sách tiền tệ. Ví dụ: The central bank raised interest rates to combat inflation after the consumer price index showed prices rising at the fastest pace in a decade."
                            },
                            {
                                "targetVocab": "deflation",
                                "prompt": "Dùng từ 'deflation' để viết một câu về rủi ro của giảm phát đối với doanh nghiệp. Ví dụ: Prolonged deflation in the real estate market has left many property developers with unsold apartments and mounting debt."
                            },
                            {
                                "targetVocab": "growth",
                                "prompt": "Dùng từ 'growth' để viết một câu về mục tiêu tăng trưởng kinh tế của một quốc gia. Ví dụ: The government set an ambitious growth target of seven percent for the coming year, banking on strong exports and increased foreign investment."
                            },
                            {
                                "targetVocab": "contraction",
                                "prompt": "Dùng từ 'contraction' để viết một câu về sự suy giảm trong một lĩnh vực kinh tế cụ thể. Ví dụ: The contraction in global shipping demand led to a thirty percent drop in freight rates, hurting Vietnam's port operators and logistics companies."
                            },
                            {
                                "targetVocab": "aggregate",
                                "prompt": "Dùng từ 'aggregate' để viết một câu về tổng cầu hoặc tổng cung trong bối cảnh chính sách kinh tế. Ví dụ: The government's infrastructure spending program is designed to boost aggregate demand during a period when private investment has slowed."
                            },
                            {
                                "targetVocab": "productivity",
                                "prompt": "Dùng từ 'productivity' để viết một câu về mối quan hệ giữa năng suất và mức sống. Ví dụ: Improving labor productivity through better education and technology is the most sustainable way to raise living standards without causing inflation."
                            },
                            {
                                "targetVocab": "benchmark",
                                "prompt": "Dùng từ 'benchmark' để viết một câu về việc so sánh hiệu suất kinh tế với một tiêu chuẩn. Ví dụ: Analysts use the ten-year government bond yield as a benchmark for pricing corporate debt and evaluating investment risk."
                            },
                            {
                                "targetVocab": "quarterly",
                                "prompt": "Dùng từ 'quarterly' để viết một câu về tầm quan trọng của dữ liệu kinh tế hàng quý. Ví dụ: The quarterly employment survey revealed that the service sector added two hundred thousand new jobs, offsetting losses in manufacturing."
                            },
                            {
                                "targetVocab": "annual",
                                "prompt": "Dùng từ 'annual' để viết một câu về xu hướng kinh tế được đo lường hàng năm. Ví dụ: The annual inflation rate dropped to three percent, giving the central bank room to lower interest rates and stimulate borrowing."
                            },
                            {
                                "targetVocab": "forecast",
                                "prompt": "Dùng từ 'forecast' để viết một câu về dự báo kinh tế và tác động của nó đến quyết định kinh doanh. Ví dụ: Based on the optimistic growth forecast, the company decided to open three new factories in the southern provinces next year."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về GDP và chỉ số kinh tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về GDP và các chỉ số kinh tế — từ cách đo lường sản lượng quốc gia "
                            "đến dự báo tương lai nền kinh tế.\n\n"
                            "Bạn sẽ gặp lại gross, domestic, nominal, real, per capita, output "
                            "trong phần mở đầu về GDP và cách tính toán. "
                            "Tiếp theo, indicator, index, inflation, deflation, growth, contraction "
                            "sẽ giúp bạn hiểu sâu hơn về các chỉ số đo lường sức khỏe kinh tế. "
                            "Và cuối cùng, aggregate, productivity, benchmark, quarterly, annual, forecast "
                            "sẽ đưa bạn vào thế giới phân tích và dự báo kinh tế vĩ mô.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: GDP và chỉ số kinh tế — Bức tranh toàn cảnh",
                    "description": "Every quarter, governments around the world release a single number that captures the pulse of their entire economy: gross domestic product.",
                    "data": {
                        "text": (
                            "Every quarter, governments around the world release a single number "
                            "that captures the pulse of their entire economy: gross domestic product, or GDP. "
                            "This number represents the total value of all goods and services produced "
                            "within a country's borders during a specific period. "
                            "It is the most widely used measure of economic performance, "
                            "and understanding it is essential for anyone studying macroeconomics.\n\n"
                            "GDP is called gross because it counts total output before deducting "
                            "the wear and tear on machinery and equipment. "
                            "It is called domestic because it only includes production that happens "
                            "inside the country — a Vietnamese-owned factory in Cambodia does not count, "
                            "but a Korean-owned factory in Ho Chi Minh City does. "
                            "The output of every sector — agriculture, manufacturing, services — "
                            "is added together to arrive at the final number.\n\n"
                            "However, comparing GDP across years requires care. "
                            "Nominal GDP uses current prices, so it can rise simply because prices went up, "
                            "not because the economy actually produced more. "
                            "Real GDP solves this problem by adjusting for inflation, "
                            "using prices from a fixed base year. "
                            "If nominal GDP grew by eight percent but inflation was three percent, "
                            "then real GDP grew by roughly five percent. "
                            "Real GDP is the number that truly tells us whether an economy is expanding.\n\n"
                            "To compare living standards across countries, economists use GDP per capita — "
                            "total GDP divided by the population. "
                            "India's GDP is much larger than Norway's, "
                            "but Norway's GDP per capita is many times higher, "
                            "reflecting a much higher standard of living for the average citizen.\n\n"
                            "GDP is just one of many economic indicators that analysts track. "
                            "An indicator is any data point that reveals something about the state of the economy. "
                            "Some indicators, like new business registrations, signal future trends. "
                            "Others, like the unemployment rate, confirm what has already happened. "
                            "To make sense of many data points at once, statisticians combine them into an index — "
                            "a single number that summarizes a complex set of information. "
                            "The Consumer Price Index, for example, tracks the average change in prices "
                            "for a basket of everyday goods.\n\n"
                            "When the index rises steadily, the economy is experiencing inflation — "
                            "a general increase in the price level. "
                            "Moderate inflation is normal, but high inflation can hurt workers "
                            "whose wages do not keep up with rising prices. "
                            "The opposite, deflation, occurs when prices fall across the board. "
                            "While cheaper goods sound appealing, deflation can trigger a dangerous cycle: "
                            "consumers wait for lower prices, businesses earn less, "
                            "and the economy slides into contraction.\n\n"
                            "Growth and contraction are the two phases of the economic cycle. "
                            "During periods of growth, output rises, businesses hire, and incomes increase. "
                            "During a contraction, output falls, layoffs rise, and spending drops. "
                            "If a contraction lasts for two consecutive quarterly periods, "
                            "the economy is officially in a recession.\n\n"
                            "Looking at the economy as a whole, economists study aggregate demand and aggregate supply. "
                            "Aggregate demand is the total spending in the economy — "
                            "by households, businesses, the government, and foreign buyers. "
                            "When aggregate demand is strong, businesses produce more and the economy grows. "
                            "When it weakens, output falls.\n\n"
                            "Long-term growth depends heavily on productivity — "
                            "how efficiently an economy turns inputs into outputs. "
                            "A country that invests in education, technology, and infrastructure "
                            "tends to see rising productivity, which lifts GDP per capita over time. "
                            "Analysts compare current performance against a benchmark — "
                            "a reference point such as last year's growth rate or a regional average — "
                            "to judge whether the economy is on track.\n\n"
                            "Economic data is released on both quarterly and annual schedules. "
                            "Quarterly data provides a timely snapshot, "
                            "while annual figures offer a broader perspective for long-term planning. "
                            "Based on this data, organizations like the IMF and World Bank publish a forecast — "
                            "an estimate of where the economy is headed. "
                            "These forecasts shape government budgets, central bank policies, "
                            "and business investment decisions around the world.\n\n"
                            "From gross domestic product to economic forecasts, "
                            "the language of macroeconomics gives us the tools to understand "
                            "the forces that shape the wealth and well-being of nations."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: GDP và chỉ số kinh tế — Bức tranh toàn cảnh",
                    "description": "Every quarter, governments around the world release a single number that captures the pulse of their entire economy: gross domestic product.",
                    "data": {
                        "text": (
                            "Every quarter, governments around the world release a single number "
                            "that captures the pulse of their entire economy: gross domestic product, or GDP. "
                            "This number represents the total value of all goods and services produced "
                            "within a country's borders during a specific period. "
                            "It is the most widely used measure of economic performance, "
                            "and understanding it is essential for anyone studying macroeconomics.\n\n"
                            "GDP is called gross because it counts total output before deducting "
                            "the wear and tear on machinery and equipment. "
                            "It is called domestic because it only includes production that happens "
                            "inside the country — a Vietnamese-owned factory in Cambodia does not count, "
                            "but a Korean-owned factory in Ho Chi Minh City does. "
                            "The output of every sector — agriculture, manufacturing, services — "
                            "is added together to arrive at the final number.\n\n"
                            "However, comparing GDP across years requires care. "
                            "Nominal GDP uses current prices, so it can rise simply because prices went up, "
                            "not because the economy actually produced more. "
                            "Real GDP solves this problem by adjusting for inflation, "
                            "using prices from a fixed base year. "
                            "If nominal GDP grew by eight percent but inflation was three percent, "
                            "then real GDP grew by roughly five percent. "
                            "Real GDP is the number that truly tells us whether an economy is expanding.\n\n"
                            "To compare living standards across countries, economists use GDP per capita — "
                            "total GDP divided by the population. "
                            "India's GDP is much larger than Norway's, "
                            "but Norway's GDP per capita is many times higher, "
                            "reflecting a much higher standard of living for the average citizen.\n\n"
                            "GDP is just one of many economic indicators that analysts track. "
                            "An indicator is any data point that reveals something about the state of the economy. "
                            "Some indicators, like new business registrations, signal future trends. "
                            "Others, like the unemployment rate, confirm what has already happened. "
                            "To make sense of many data points at once, statisticians combine them into an index — "
                            "a single number that summarizes a complex set of information. "
                            "The Consumer Price Index, for example, tracks the average change in prices "
                            "for a basket of everyday goods.\n\n"
                            "When the index rises steadily, the economy is experiencing inflation — "
                            "a general increase in the price level. "
                            "Moderate inflation is normal, but high inflation can hurt workers "
                            "whose wages do not keep up with rising prices. "
                            "The opposite, deflation, occurs when prices fall across the board. "
                            "While cheaper goods sound appealing, deflation can trigger a dangerous cycle: "
                            "consumers wait for lower prices, businesses earn less, "
                            "and the economy slides into contraction.\n\n"
                            "Growth and contraction are the two phases of the economic cycle. "
                            "During periods of growth, output rises, businesses hire, and incomes increase. "
                            "During a contraction, output falls, layoffs rise, and spending drops. "
                            "If a contraction lasts for two consecutive quarterly periods, "
                            "the economy is officially in a recession.\n\n"
                            "Looking at the economy as a whole, economists study aggregate demand and aggregate supply. "
                            "Aggregate demand is the total spending in the economy — "
                            "by households, businesses, the government, and foreign buyers. "
                            "When aggregate demand is strong, businesses produce more and the economy grows. "
                            "When it weakens, output falls.\n\n"
                            "Long-term growth depends heavily on productivity — "
                            "how efficiently an economy turns inputs into outputs. "
                            "A country that invests in education, technology, and infrastructure "
                            "tends to see rising productivity, which lifts GDP per capita over time. "
                            "Analysts compare current performance against a benchmark — "
                            "a reference point such as last year's growth rate or a regional average — "
                            "to judge whether the economy is on track.\n\n"
                            "Economic data is released on both quarterly and annual schedules. "
                            "Quarterly data provides a timely snapshot, "
                            "while annual figures offer a broader perspective for long-term planning. "
                            "Based on this data, organizations like the IMF and World Bank publish a forecast — "
                            "an estimate of where the economy is headed. "
                            "These forecasts shape government budgets, central bank policies, "
                            "and business investment decisions around the world.\n\n"
                            "From gross domestic product to economic forecasts, "
                            "the language of macroeconomics gives us the tools to understand "
                            "the forces that shape the wealth and well-being of nations."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: GDP và chỉ số kinh tế — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every quarter, governments around the world release a single number "
                            "that captures the pulse of their entire economy: gross domestic product, or GDP. "
                            "This number represents the total value of all goods and services produced "
                            "within a country's borders during a specific period. "
                            "It is the most widely used measure of economic performance, "
                            "and understanding it is essential for anyone studying macroeconomics.\n\n"
                            "GDP is called gross because it counts total output before deducting "
                            "the wear and tear on machinery and equipment. "
                            "It is called domestic because it only includes production that happens "
                            "inside the country — a Vietnamese-owned factory in Cambodia does not count, "
                            "but a Korean-owned factory in Ho Chi Minh City does. "
                            "The output of every sector — agriculture, manufacturing, services — "
                            "is added together to arrive at the final number.\n\n"
                            "However, comparing GDP across years requires care. "
                            "Nominal GDP uses current prices, so it can rise simply because prices went up, "
                            "not because the economy actually produced more. "
                            "Real GDP solves this problem by adjusting for inflation, "
                            "using prices from a fixed base year. "
                            "If nominal GDP grew by eight percent but inflation was three percent, "
                            "then real GDP grew by roughly five percent. "
                            "Real GDP is the number that truly tells us whether an economy is expanding.\n\n"
                            "To compare living standards across countries, economists use GDP per capita — "
                            "total GDP divided by the population. "
                            "India's GDP is much larger than Norway's, "
                            "but Norway's GDP per capita is many times higher, "
                            "reflecting a much higher standard of living for the average citizen.\n\n"
                            "GDP is just one of many economic indicators that analysts track. "
                            "An indicator is any data point that reveals something about the state of the economy. "
                            "Some indicators, like new business registrations, signal future trends. "
                            "Others, like the unemployment rate, confirm what has already happened. "
                            "To make sense of many data points at once, statisticians combine them into an index — "
                            "a single number that summarizes a complex set of information. "
                            "The Consumer Price Index, for example, tracks the average change in prices "
                            "for a basket of everyday goods.\n\n"
                            "When the index rises steadily, the economy is experiencing inflation — "
                            "a general increase in the price level. "
                            "Moderate inflation is normal, but high inflation can hurt workers "
                            "whose wages do not keep up with rising prices. "
                            "The opposite, deflation, occurs when prices fall across the board. "
                            "While cheaper goods sound appealing, deflation can trigger a dangerous cycle: "
                            "consumers wait for lower prices, businesses earn less, "
                            "and the economy slides into contraction.\n\n"
                            "Growth and contraction are the two phases of the economic cycle. "
                            "During periods of growth, output rises, businesses hire, and incomes increase. "
                            "During a contraction, output falls, layoffs rise, and spending drops. "
                            "If a contraction lasts for two consecutive quarterly periods, "
                            "the economy is officially in a recession.\n\n"
                            "Looking at the economy as a whole, economists study aggregate demand and aggregate supply. "
                            "Aggregate demand is the total spending in the economy — "
                            "by households, businesses, the government, and foreign buyers. "
                            "When aggregate demand is strong, businesses produce more and the economy grows. "
                            "When it weakens, output falls.\n\n"
                            "Long-term growth depends heavily on productivity — "
                            "how efficiently an economy turns inputs into outputs. "
                            "A country that invests in education, technology, and infrastructure "
                            "tends to see rising productivity, which lifts GDP per capita over time. "
                            "Analysts compare current performance against a benchmark — "
                            "a reference point such as last year's growth rate or a regional average — "
                            "to judge whether the economy is on track.\n\n"
                            "Economic data is released on both quarterly and annual schedules. "
                            "Quarterly data provides a timely snapshot, "
                            "while annual figures offer a broader perspective for long-term planning. "
                            "Based on this data, organizations like the IMF and World Bank publish a forecast — "
                            "an estimate of where the economy is headed. "
                            "These forecasts shape government budgets, central bank policies, "
                            "and business investment decisions around the world.\n\n"
                            "From gross domestic product to economic forecasts, "
                            "the language of macroeconomics gives us the tools to understand "
                            "the forces that shape the wealth and well-being of nations."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích GDP và chỉ số kinh tế",
                    "description": "Viết đoạn văn tiếng Anh phân tích về GDP và chỉ số kinh tế sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống kinh tế vĩ mô thực tế liên quan đến GDP và các chỉ số kinh tế. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích sự khác biệt giữa nominal GDP và real GDP của Việt Nam trong thập kỷ qua. Giải thích tại sao inflation làm cho nominal GDP tăng nhanh hơn real GDP, và per capita output cho biết điều gì về mức sống thực tế của người dân.",
                            "Hãy mô tả cách các nhà kinh tế sử dụng indicators và index để forecast tình hình kinh tế. Giải thích điều gì xảy ra khi quarterly data cho thấy contraction, và productivity đóng vai trò gì trong việc duy trì growth bền vững."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần trách nhiệm ấm áp.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học về GDP và Chỉ Số Kinh Tế. "
                            "Đây không phải là kết thúc — đây là điểm bắt đầu. "
                            "Bây giờ bạn có trách nhiệm sử dụng những gì đã học.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất — và lần này, "
                            "tôi muốn bạn tự hỏi: mình sẽ dùng từ này ở đâu trong tuần tới?\n\n"
                            "Real — thực tế, đã điều chỉnh lạm phát. Đây là từ giúp bạn nhìn xuyên qua "
                            "những con số bề mặt. Lần tới khi ai đó nói 'GDP tăng 8 phần trăm', "
                            "bạn hãy hỏi: đó là nominal hay real? "
                            "Ví dụ mới: The real cost of living in Hanoi has risen faster than official statistics suggest "
                            "because the price of housing is not fully captured in the consumer price index.\n\n"
                            "Inflation — lạm phát. Từ này ảnh hưởng trực tiếp đến ví tiền của bạn. "
                            "Mỗi khi bạn thấy giá cà phê tăng, giá xăng tăng, giá phòng trọ tăng — "
                            "đó là inflation đang diễn ra. Hiểu inflation là hiểu vì sao tiền mất giá. "
                            "Ví dụ mới: Central banks around the world target an inflation rate of about two percent "
                            "because it keeps the economy growing without eroding people's savings too quickly.\n\n"
                            "Productivity — năng suất. Đây là chìa khóa của sự thịnh vượng dài hạn. "
                            "Không phải làm nhiều giờ hơn, mà là tạo ra nhiều giá trị hơn trong mỗi giờ. "
                            "Bạn — một sinh viên kinh tế — cũng có productivity cá nhân. "
                            "Ví dụ mới: Countries that invest heavily in education and research tend to see "
                            "the fastest gains in productivity, which translates directly into higher wages and better jobs.\n\n"
                            "Forecast — dự báo. Mọi quyết định kinh tế đều dựa trên dự báo — "
                            "từ chính phủ lập ngân sách đến doanh nghiệp quyết định mở rộng. "
                            "Bạn cũng đang forecast cho tương lai của mình khi chọn ngành học. "
                            "Ví dụ mới: The government revised its budget after the latest forecast showed "
                            "that tax revenue would fall short of expectations due to slower economic growth.\n\n"
                            "Growth — tăng trưởng. Mọi quốc gia đều theo đuổi growth, "
                            "nhưng growth bền vững mới là điều quan trọng. "
                            "Tăng trưởng nhanh mà không bền vững giống như chạy nước rút trong marathon — "
                            "bạn sẽ kiệt sức trước khi về đích. "
                            "Ví dụ mới: Sustainable growth requires a balance between expanding output today "
                            "and investing in the infrastructure and human capital needed for tomorrow.\n\n"
                            "Per capita — bình quân đầu người. Từ này nhắc bạn rằng "
                            "tổng GDP lớn không có nghĩa là mọi người đều giàu. "
                            "Khi đọc báo cáo kinh tế, luôn hỏi: per capita là bao nhiêu? "
                            "Ví dụ mới: Despite impressive GDP growth, the country's income per capita "
                            "remains below the regional average because the population has also grown rapidly.\n\n"
                            "Bạn biết không, 18 từ vựng này không chỉ để thi — "
                            "chúng là công cụ để bạn đọc báo cáo World Bank, "
                            "hiểu slide giảng viên, và tham gia thảo luận trong lớp bằng tiếng Anh. "
                            "Tuần này, hãy thử đọc một bài báo kinh tế tiếng Anh — "
                            "từ Bloomberg, Reuters, hay trang của IMF — và đếm xem bạn gặp bao nhiêu từ đã học.\n\n"
                            "Tôi tin bạn sẽ ngạc nhiên. Và tôi tin bạn sẽ tiếp tục.\n\n"
                            "Hẹn gặp lại bạn ở bài học tiếp theo — Thị Trường Lao Động. "
                            "Chúc bạn học tốt và luôn tò mò!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'GDP & Indicators – GDP và Chỉ Số Kinh Tế' AND uid = '{UID}' ORDER BY created_at;")
