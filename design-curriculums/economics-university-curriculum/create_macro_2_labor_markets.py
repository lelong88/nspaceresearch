"""
Create curriculum: Labor Markets – Thị Trường Lao Động
Series B — Kinh Tế Vĩ Mô (Macroeconomics), curriculum #2
18 words | 5 sessions | empathetic_observation tone | quiet awe farewell
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
W1 = ["unemployment", "labor", "workforce", "participation", "wage", "hiring"]
W2 = ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"]
W3 = ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Labor Markets – Thị Trường Lao Động",
    "contentTypeTags": [],
    "description": (
        "BẠN ĐỌC BÁO CÁO VIỆC LÀM BẰNG TIẾNG ANH MÀ KHÔNG HIỂU UNEMPLOYMENT RATE KHÁC GÌ UNDEREMPLOYMENT — CẢM GIÁC ĐÓ RẤT CÔ ĐƠN, ĐÚNG KHÔNG?\n\n"
        "Mỗi kỳ thi, giảng viên chiếu biểu đồ labor market bằng tiếng Anh — "
        "structural unemployment, cyclical unemployment, frictional unemployment — "
        "bạn biết đại khái chúng liên quan đến thất nghiệp, nhưng khi phải phân tích bằng tiếng Anh "
        "thì đầu óc trống rỗng. Bạn không thiếu kiến thức kinh tế, bạn thiếu ngôn ngữ để diễn đạt nó.\n\n"
        "Hãy nghĩ về vốn từ tiếng Anh kinh tế của bạn như một tấm bản đồ bị mờ — "
        "bạn biết đích đến ở đâu đó phía trước, nhưng không đọc được tên đường. "
        "18 từ vựng trong bài học này sẽ làm rõ từng con đường trên tấm bản đồ ấy.\n\n"
        "Sau khóa học, bạn sẽ tự tin đọc báo cáo thị trường lao động quốc tế, "
        "phân biệt được các loại thất nghiệp, và viết được đoạn phân tích sắc bén "
        "về hiring, layoff, automation bằng tiếng Anh chuyên ngành.\n\n"
        "18 từ — từ unemployment đến retraining — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kinh tế vĩ mô, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về thị trường lao động — "
            "một trong những chủ đề quan trọng nhất của kinh tế vĩ mô. "
            "Bạn sẽ học unemployment, labor, workforce, participation, wage, hiring trong phần đầu tiên, "
            "nơi bài đọc giải thích cách đo lường sức khỏe của thị trường việc làm. "
            "Tiếp theo là structural, cyclical, frictional, seasonal, underemployment, layoff — "
            "những từ giúp bạn phân loại các dạng thất nghiệp và hiểu nguyên nhân sâu xa của chúng. "
            "Cuối cùng, vacancy, turnover, mobility, outsource, automation, retraining "
            "đưa bạn vào thế giới biến động của lực lượng lao động hiện đại. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu báo cáo việc làm và phân tích thị trường lao động bằng tiếng Anh — "
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
                    "description": "Chào mừng bạn đến với bài học về thị trường lao động — trụ cột của kinh tế vĩ mô.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học về Thị trường Lao động — "
                            "hay trong tiếng Anh là Labor Markets. "
                            "Đây là một trong những chủ đề trung tâm của kinh tế vĩ mô, "
                            "bởi vì sức khỏe của nền kinh tế được phản ánh rõ nhất qua việc làm: "
                            "bao nhiêu người có việc, bao nhiêu người đang tìm việc, "
                            "và mức lương họ nhận được.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: unemployment, labor, workforce, "
                            "participation, wage, và hiring. "
                            "Đây là những từ bạn sẽ gặp trong bất kỳ báo cáo kinh tế nào "
                            "khi nói về tình hình việc làm của một quốc gia.\n\n"
                            "Từ đầu tiên là unemployment — danh từ — nghĩa là thất nghiệp, "
                            "tình trạng khi người lao động muốn làm việc nhưng không tìm được việc làm. "
                            "Ví dụ: 'Unemployment rose sharply during the economic recession as companies cut thousands of jobs.' "
                            "Trong bài đọc, unemployment là chỉ số quan trọng nhất để đánh giá "
                            "sức khỏe của thị trường lao động.\n\n"
                            "Từ thứ hai là labor — danh từ — nghĩa là lao động, "
                            "sức lao động của con người được sử dụng để sản xuất hàng hóa và dịch vụ. "
                            "Ví dụ: 'The cost of labor in Vietnam is lower than in Japan, which attracts foreign manufacturers.' "
                            "Trong bài đọc, labor được dùng để nói về lực lượng lao động "
                            "như một yếu tố sản xuất cơ bản của nền kinh tế.\n\n"
                            "Từ thứ ba là workforce — danh từ — nghĩa là lực lượng lao động, "
                            "tổng số người đang làm việc hoặc đang tìm việc trong một nền kinh tế. "
                            "Ví dụ: 'Vietnam has a young workforce, with over half the population under the age of thirty-five.' "
                            "Trong bài đọc, workforce bao gồm cả người đang có việc "
                            "và người đang tích cực tìm kiếm việc làm.\n\n"
                            "Từ thứ tư là participation — danh từ — nghĩa là sự tham gia, "
                            "tỷ lệ người trong độ tuổi lao động thực sự tham gia vào thị trường việc làm. "
                            "Ví dụ: 'The labor force participation rate for women has increased significantly over the past two decades.' "
                            "Trong bài đọc, participation rate cho biết bao nhiêu phần trăm dân số "
                            "đang làm việc hoặc đang tìm việc — không phải ai trong độ tuổi lao động "
                            "cũng tham gia thị trường.\n\n"
                            "Từ thứ năm là wage — danh từ — nghĩa là tiền lương, "
                            "số tiền người lao động nhận được cho công việc của mình. "
                            "Ví dụ: 'The minimum wage in Vietnam varies by region, with higher rates in major cities like Hanoi and Ho Chi Minh City.' "
                            "Trong bài đọc, wage phản ánh giá cả của lao động trên thị trường — "
                            "khi cầu lao động tăng, wage có xu hướng tăng theo.\n\n"
                            "Từ cuối cùng là hiring — danh từ và động từ — nghĩa là tuyển dụng, "
                            "quá trình doanh nghiệp tìm và nhận người lao động mới. "
                            "Ví dụ: 'Tech companies are hiring aggressively to fill positions in artificial intelligence and data science.' "
                            "Trong bài đọc, hiring là tín hiệu tích cực của thị trường lao động — "
                            "khi doanh nghiệp tuyển nhiều, nền kinh tế đang phát triển.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về thị trường lao động để thấy các từ này trong ngữ cảnh thực tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thị trường lao động cơ bản",
                    "description": "Học 6 từ: unemployment, labor, workforce, participation, wage, hiring",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thị trường lao động cơ bản",
                    "description": "Học 6 từ: unemployment, labor, workforce, participation, wage, hiring",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thị trường lao động cơ bản",
                    "description": "Học 6 từ: unemployment, labor, workforce, participation, wage, hiring",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thị trường lao động cơ bản",
                    "description": "Học 6 từ: unemployment, labor, workforce, participation, wage, hiring",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Thị trường lao động cơ bản",
                    "description": "Học 6 từ: unemployment, labor, workforce, participation, wage, hiring",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thị trường lao động cơ bản",
                    "description": "When economists talk about the health of an economy, one of the first things they look at is the labor market.",
                    "data": {
                        "text": (
                            "When economists talk about the health of an economy, one of the first things they look at is the labor market. "
                            "The labor market is where workers offer their skills and time, and employers offer jobs and wages. "
                            "Just like any other market, the labor market is shaped by supply and demand — "
                            "but here, the product being traded is human labor.\n\n"
                            "The total number of people who are either working or actively looking for work is called the workforce. "
                            "Not everyone in a country is part of the workforce. "
                            "Students, retirees, and people who have chosen not to seek employment are not counted. "
                            "The share of the working-age population that is in the workforce is measured by the participation rate. "
                            "A high participation rate means that most adults are engaged in the economy, "
                            "either by holding a job or by searching for one.\n\n"
                            "Unemployment is the condition of being without a job while actively seeking work. "
                            "The unemployment rate is one of the most closely watched economic indicators in any country. "
                            "When unemployment is low, it usually means the economy is growing and businesses are confident. "
                            "When unemployment is high, it signals trouble — fewer people are earning income, "
                            "consumer spending drops, and the government may need to step in with support programs.\n\n"
                            "The wage that workers earn is determined by the interaction of labor supply and labor demand. "
                            "When many companies are competing to hire workers in a particular field, wages tend to rise. "
                            "For example, the rapid growth of the technology sector in Vietnam has pushed up wages "
                            "for software developers because the demand for their skills exceeds the supply.\n\n"
                            "Hiring is the process by which companies bring new workers on board. "
                            "When hiring is strong across many industries, it is a sign that the economy is expanding. "
                            "Companies hire when they expect future demand for their products to grow. "
                            "On the other hand, when hiring slows down, it often means businesses are uncertain about the future.\n\n"
                            "Understanding the labor market helps us see beyond the headline numbers. "
                            "A low unemployment rate sounds good, but if the participation rate is also low, "
                            "it may mean that many people have simply given up looking for work. "
                            "The labor market tells a story about opportunity, confidence, and the real state of the economy."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thị trường lao động cơ bản",
                    "description": "When economists talk about the health of an economy, one of the first things they look at is the labor market.",
                    "data": {
                        "text": (
                            "When economists talk about the health of an economy, one of the first things they look at is the labor market. "
                            "The labor market is where workers offer their skills and time, and employers offer jobs and wages. "
                            "Just like any other market, the labor market is shaped by supply and demand — "
                            "but here, the product being traded is human labor.\n\n"
                            "The total number of people who are either working or actively looking for work is called the workforce. "
                            "Not everyone in a country is part of the workforce. "
                            "Students, retirees, and people who have chosen not to seek employment are not counted. "
                            "The share of the working-age population that is in the workforce is measured by the participation rate. "
                            "A high participation rate means that most adults are engaged in the economy, "
                            "either by holding a job or by searching for one.\n\n"
                            "Unemployment is the condition of being without a job while actively seeking work. "
                            "The unemployment rate is one of the most closely watched economic indicators in any country. "
                            "When unemployment is low, it usually means the economy is growing and businesses are confident. "
                            "When unemployment is high, it signals trouble — fewer people are earning income, "
                            "consumer spending drops, and the government may need to step in with support programs.\n\n"
                            "The wage that workers earn is determined by the interaction of labor supply and labor demand. "
                            "When many companies are competing to hire workers in a particular field, wages tend to rise. "
                            "For example, the rapid growth of the technology sector in Vietnam has pushed up wages "
                            "for software developers because the demand for their skills exceeds the supply.\n\n"
                            "Hiring is the process by which companies bring new workers on board. "
                            "When hiring is strong across many industries, it is a sign that the economy is expanding. "
                            "Companies hire when they expect future demand for their products to grow. "
                            "On the other hand, when hiring slows down, it often means businesses are uncertain about the future.\n\n"
                            "Understanding the labor market helps us see beyond the headline numbers. "
                            "A low unemployment rate sounds good, but if the participation rate is also low, "
                            "it may mean that many people have simply given up looking for work. "
                            "The labor market tells a story about opportunity, confidence, and the real state of the economy."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thị trường lao động cơ bản",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When economists talk about the health of an economy, one of the first things they look at is the labor market. "
                            "The labor market is where workers offer their skills and time, and employers offer jobs and wages. "
                            "Just like any other market, the labor market is shaped by supply and demand — "
                            "but here, the product being traded is human labor.\n\n"
                            "The total number of people who are either working or actively looking for work is called the workforce. "
                            "Not everyone in a country is part of the workforce. "
                            "Students, retirees, and people who have chosen not to seek employment are not counted. "
                            "The share of the working-age population that is in the workforce is measured by the participation rate. "
                            "A high participation rate means that most adults are engaged in the economy, "
                            "either by holding a job or by searching for one.\n\n"
                            "Unemployment is the condition of being without a job while actively seeking work. "
                            "The unemployment rate is one of the most closely watched economic indicators in any country. "
                            "When unemployment is low, it usually means the economy is growing and businesses are confident. "
                            "When unemployment is high, it signals trouble — fewer people are earning income, "
                            "consumer spending drops, and the government may need to step in with support programs.\n\n"
                            "The wage that workers earn is determined by the interaction of labor supply and labor demand. "
                            "When many companies are competing to hire workers in a particular field, wages tend to rise. "
                            "For example, the rapid growth of the technology sector in Vietnam has pushed up wages "
                            "for software developers because the demand for their skills exceeds the supply.\n\n"
                            "Hiring is the process by which companies bring new workers on board. "
                            "When hiring is strong across many industries, it is a sign that the economy is expanding. "
                            "Companies hire when they expect future demand for their products to grow. "
                            "On the other hand, when hiring slows down, it often means businesses are uncertain about the future.\n\n"
                            "Understanding the labor market helps us see beyond the headline numbers. "
                            "A low unemployment rate sounds good, but if the participation rate is also low, "
                            "it may mean that many people have simply given up looking for work. "
                            "The labor market tells a story about opportunity, confidence, and the real state of the economy."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thị trường lao động cơ bản",
                    "description": "Viết câu sử dụng 6 từ vựng về thị trường lao động.",
                    "data": {
                        "vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring"],
                        "items": [
                            {
                                "targetVocab": "unemployment",
                                "prompt": "Dùng từ 'unemployment' để viết một câu về tình trạng thất nghiệp tăng cao trong thời kỳ suy thoái kinh tế. Ví dụ: Unemployment in the manufacturing sector doubled during the recession as factories reduced production and let go of thousands of workers."
                            },
                            {
                                "targetVocab": "labor",
                                "prompt": "Dùng từ 'labor' để viết một câu về vai trò của lao động như một yếu tố sản xuất trong nền kinh tế. Ví dụ: The cost of labor is one of the biggest expenses for garment factories in Vietnam, accounting for nearly forty percent of total production costs."
                            },
                            {
                                "targetVocab": "workforce",
                                "prompt": "Dùng từ 'workforce' để viết một câu về đặc điểm của lực lượng lao động ở một quốc gia hoặc ngành cụ thể. Ví dụ: The healthcare workforce in rural areas is much smaller than in cities, which creates unequal access to medical services."
                            },
                            {
                                "targetVocab": "participation",
                                "prompt": "Dùng từ 'participation' để viết một câu về tỷ lệ tham gia lực lượng lao động và ý nghĩa kinh tế của nó. Ví dụ: The government launched a childcare program to increase female labor force participation, which had been declining for five years."
                            },
                            {
                                "targetVocab": "wage",
                                "prompt": "Dùng từ 'wage' để viết một câu về mối quan hệ giữa tiền lương và cung cầu lao động. Ví dụ: The average wage for construction workers rose by fifteen percent this year because there were not enough skilled builders to meet the demand."
                            },
                            {
                                "targetVocab": "hiring",
                                "prompt": "Dùng từ 'hiring' để viết một câu về xu hướng tuyển dụng trong một ngành đang phát triển. Ví dụ: Hiring in the renewable energy sector has surged as the government pushes companies to reduce their carbon emissions."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về các loại thất nghiệp.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "unemployment — thất nghiệp, labor — lao động, workforce — lực lượng lao động, "
                            "participation — sự tham gia, wage — tiền lương, và hiring — tuyển dụng. "
                            "Bạn đã hiểu cách thị trường lao động vận hành ở mức cơ bản nhất. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào câu hỏi: tại sao người ta thất nghiệp?\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: structural, cyclical, frictional, seasonal, "
                            "underemployment, và layoff. "
                            "Những từ này giúp bạn phân loại thất nghiệp — không phải mọi người mất việc "
                            "đều vì cùng một lý do, và hiểu sự khác biệt là chìa khóa để phân tích chính sách.\n\n"
                            "Từ đầu tiên là structural — tính từ — nghĩa là mang tính cấu trúc, "
                            "liên quan đến sự thay đổi lâu dài trong cơ cấu nền kinh tế. "
                            "Ví dụ: 'Structural unemployment occurs when workers' skills no longer match the jobs available in the economy.' "
                            "Trong bài đọc, structural unemployment mô tả tình trạng khi ngành công nghiệp thay đổi "
                            "và người lao động cần kỹ năng mới mà họ chưa có.\n\n"
                            "Từ thứ hai là cyclical — tính từ — nghĩa là theo chu kỳ, "
                            "liên quan đến sự lên xuống tự nhiên của nền kinh tế. "
                            "Ví dụ: 'Cyclical unemployment rises during recessions and falls during periods of economic growth.' "
                            "Trong bài đọc, cyclical unemployment gắn liền với chu kỳ kinh doanh — "
                            "khi nền kinh tế suy thoái, doanh nghiệp cắt giảm nhân sự.\n\n"
                            "Từ thứ ba là frictional — tính từ — nghĩa là ma sát, "
                            "liên quan đến khoảng thời gian chuyển đổi giữa các công việc. "
                            "Ví dụ: 'Frictional unemployment is normal and even healthy — it means people are searching for better jobs.' "
                            "Trong bài đọc, frictional unemployment là loại thất nghiệp tạm thời "
                            "khi người lao động đang tìm việc mới phù hợp hơn.\n\n"
                            "Từ thứ tư là seasonal — tính từ — nghĩa là theo mùa, "
                            "liên quan đến sự thay đổi nhu cầu lao động theo thời điểm trong năm. "
                            "Ví dụ: 'Seasonal unemployment affects tourism workers who lose their jobs when the holiday season ends.' "
                            "Trong bài đọc, seasonal unemployment xảy ra ở những ngành phụ thuộc vào mùa vụ "
                            "như nông nghiệp, du lịch, và bán lẻ.\n\n"
                            "Từ thứ năm là underemployment — danh từ — nghĩa là thiếu việc làm, "
                            "tình trạng khi người lao động có việc nhưng không được sử dụng hết năng lực. "
                            "Ví dụ: 'A university graduate working as a part-time cashier is an example of underemployment.' "
                            "Trong bài đọc, underemployment cho thấy rằng tỷ lệ thất nghiệp thấp "
                            "không phải lúc nào cũng có nghĩa là thị trường lao động khỏe mạnh.\n\n"
                            "Từ cuối cùng là layoff — danh từ — nghĩa là sa thải, "
                            "việc doanh nghiệp cho người lao động nghỉ việc vì lý do kinh tế. "
                            "Ví dụ: 'The company announced a layoff of five hundred employees after losing its biggest client.' "
                            "Trong bài đọc, layoff khác với việc bị đuổi vì lỗi cá nhân — "
                            "layoff xảy ra khi doanh nghiệp cần cắt giảm chi phí hoặc thu hẹp quy mô.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về các loại thất nghiệp nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Các loại thất nghiệp",
                    "description": "Học 6 từ: structural, cyclical, frictional, seasonal, underemployment, layoff",
                    "data": {"vocabList": ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Các loại thất nghiệp",
                    "description": "Học 6 từ: structural, cyclical, frictional, seasonal, underemployment, layoff",
                    "data": {"vocabList": ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Các loại thất nghiệp",
                    "description": "Học 6 từ: structural, cyclical, frictional, seasonal, underemployment, layoff",
                    "data": {"vocabList": ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Các loại thất nghiệp",
                    "description": "Học 6 từ: structural, cyclical, frictional, seasonal, underemployment, layoff",
                    "data": {"vocabList": ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Các loại thất nghiệp",
                    "description": "Học 6 từ: structural, cyclical, frictional, seasonal, underemployment, layoff",
                    "data": {"vocabList": ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Các loại thất nghiệp",
                    "description": "Not all unemployment is the same. Economists divide unemployment into several types based on its cause.",
                    "data": {
                        "text": (
                            "Not all unemployment is the same. "
                            "Economists divide unemployment into several types based on its cause, "
                            "and understanding these differences is essential for designing the right policy response.\n\n"
                            "The most common type during economic downturns is cyclical unemployment. "
                            "Cyclical unemployment rises when the economy slows down and falls when the economy recovers. "
                            "During a recession, consumers spend less, businesses earn less revenue, "
                            "and companies respond by reducing their workforce. "
                            "Layoffs spread across industries — from manufacturing to retail to hospitality. "
                            "A layoff happens when a company lets workers go not because of poor performance, "
                            "but because there is simply not enough work to justify keeping them.\n\n"
                            "Structural unemployment has a different cause. "
                            "It occurs when the skills that workers have do not match the skills that employers need. "
                            "This often happens when technology changes an industry. "
                            "For example, when factories in Vietnam began using automated assembly lines, "
                            "many manual workers found that their skills were no longer in demand. "
                            "Structural unemployment tends to last longer than cyclical unemployment "
                            "because workers need time to learn new skills or move to new industries.\n\n"
                            "Frictional unemployment is the most natural type. "
                            "It occurs when workers are between jobs — perhaps they quit to find something better, "
                            "or they just graduated from university and are searching for their first position. "
                            "Frictional unemployment exists even in a healthy economy. "
                            "In fact, some level of frictional unemployment is considered a sign "
                            "that workers have the freedom to look for jobs that match their abilities and preferences.\n\n"
                            "Seasonal unemployment follows a predictable pattern tied to the time of year. "
                            "Agricultural workers may be unemployed after the harvest season ends. "
                            "Hotel staff in beach towns may lose their jobs when tourists stop coming in the winter. "
                            "Seasonal unemployment is temporary, but it can create real hardship "
                            "for workers who depend on income from seasonal industries.\n\n"
                            "Beyond these categories, economists also pay attention to underemployment. "
                            "Underemployment describes a situation where workers have jobs, "
                            "but those jobs do not fully use their skills or provide enough hours. "
                            "A trained engineer working as a delivery driver is underemployed. "
                            "A teacher who can only find part-time work when she wants full-time hours is underemployed. "
                            "The official unemployment rate does not capture underemployment, "
                            "which is why economists look at broader measures to understand the true state of the labor market.\n\n"
                            "Each type of unemployment calls for a different solution. "
                            "Cyclical unemployment may respond to government spending that boosts demand. "
                            "Structural unemployment requires education and training programs. "
                            "Frictional unemployment can be reduced by better job-matching services. "
                            "And seasonal unemployment may be softened by diversifying local economies. "
                            "Knowing which type you are dealing with is the first step toward finding the right answer."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Các loại thất nghiệp",
                    "description": "Not all unemployment is the same. Economists divide unemployment into several types based on its cause.",
                    "data": {
                        "text": (
                            "Not all unemployment is the same. "
                            "Economists divide unemployment into several types based on its cause, "
                            "and understanding these differences is essential for designing the right policy response.\n\n"
                            "The most common type during economic downturns is cyclical unemployment. "
                            "Cyclical unemployment rises when the economy slows down and falls when the economy recovers. "
                            "During a recession, consumers spend less, businesses earn less revenue, "
                            "and companies respond by reducing their workforce. "
                            "Layoffs spread across industries — from manufacturing to retail to hospitality. "
                            "A layoff happens when a company lets workers go not because of poor performance, "
                            "but because there is simply not enough work to justify keeping them.\n\n"
                            "Structural unemployment has a different cause. "
                            "It occurs when the skills that workers have do not match the skills that employers need. "
                            "This often happens when technology changes an industry. "
                            "For example, when factories in Vietnam began using automated assembly lines, "
                            "many manual workers found that their skills were no longer in demand. "
                            "Structural unemployment tends to last longer than cyclical unemployment "
                            "because workers need time to learn new skills or move to new industries.\n\n"
                            "Frictional unemployment is the most natural type. "
                            "It occurs when workers are between jobs — perhaps they quit to find something better, "
                            "or they just graduated from university and are searching for their first position. "
                            "Frictional unemployment exists even in a healthy economy. "
                            "In fact, some level of frictional unemployment is considered a sign "
                            "that workers have the freedom to look for jobs that match their abilities and preferences.\n\n"
                            "Seasonal unemployment follows a predictable pattern tied to the time of year. "
                            "Agricultural workers may be unemployed after the harvest season ends. "
                            "Hotel staff in beach towns may lose their jobs when tourists stop coming in the winter. "
                            "Seasonal unemployment is temporary, but it can create real hardship "
                            "for workers who depend on income from seasonal industries.\n\n"
                            "Beyond these categories, economists also pay attention to underemployment. "
                            "Underemployment describes a situation where workers have jobs, "
                            "but those jobs do not fully use their skills or provide enough hours. "
                            "A trained engineer working as a delivery driver is underemployed. "
                            "A teacher who can only find part-time work when she wants full-time hours is underemployed. "
                            "The official unemployment rate does not capture underemployment, "
                            "which is why economists look at broader measures to understand the true state of the labor market.\n\n"
                            "Each type of unemployment calls for a different solution. "
                            "Cyclical unemployment may respond to government spending that boosts demand. "
                            "Structural unemployment requires education and training programs. "
                            "Frictional unemployment can be reduced by better job-matching services. "
                            "And seasonal unemployment may be softened by diversifying local economies. "
                            "Knowing which type you are dealing with is the first step toward finding the right answer."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Các loại thất nghiệp",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Not all unemployment is the same. "
                            "Economists divide unemployment into several types based on its cause, "
                            "and understanding these differences is essential for designing the right policy response.\n\n"
                            "The most common type during economic downturns is cyclical unemployment. "
                            "Cyclical unemployment rises when the economy slows down and falls when the economy recovers. "
                            "During a recession, consumers spend less, businesses earn less revenue, "
                            "and companies respond by reducing their workforce. "
                            "Layoffs spread across industries — from manufacturing to retail to hospitality. "
                            "A layoff happens when a company lets workers go not because of poor performance, "
                            "but because there is simply not enough work to justify keeping them.\n\n"
                            "Structural unemployment has a different cause. "
                            "It occurs when the skills that workers have do not match the skills that employers need. "
                            "This often happens when technology changes an industry. "
                            "For example, when factories in Vietnam began using automated assembly lines, "
                            "many manual workers found that their skills were no longer in demand. "
                            "Structural unemployment tends to last longer than cyclical unemployment "
                            "because workers need time to learn new skills or move to new industries.\n\n"
                            "Frictional unemployment is the most natural type. "
                            "It occurs when workers are between jobs — perhaps they quit to find something better, "
                            "or they just graduated from university and are searching for their first position. "
                            "Frictional unemployment exists even in a healthy economy. "
                            "In fact, some level of frictional unemployment is considered a sign "
                            "that workers have the freedom to look for jobs that match their abilities and preferences.\n\n"
                            "Seasonal unemployment follows a predictable pattern tied to the time of year. "
                            "Agricultural workers may be unemployed after the harvest season ends. "
                            "Hotel staff in beach towns may lose their jobs when tourists stop coming in the winter. "
                            "Seasonal unemployment is temporary, but it can create real hardship "
                            "for workers who depend on income from seasonal industries.\n\n"
                            "Beyond these categories, economists also pay attention to underemployment. "
                            "Underemployment describes a situation where workers have jobs, "
                            "but those jobs do not fully use their skills or provide enough hours. "
                            "A trained engineer working as a delivery driver is underemployed. "
                            "A teacher who can only find part-time work when she wants full-time hours is underemployed. "
                            "The official unemployment rate does not capture underemployment, "
                            "which is why economists look at broader measures to understand the true state of the labor market.\n\n"
                            "Each type of unemployment calls for a different solution. "
                            "Cyclical unemployment may respond to government spending that boosts demand. "
                            "Structural unemployment requires education and training programs. "
                            "Frictional unemployment can be reduced by better job-matching services. "
                            "And seasonal unemployment may be softened by diversifying local economies. "
                            "Knowing which type you are dealing with is the first step toward finding the right answer."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Các loại thất nghiệp",
                    "description": "Viết câu sử dụng 6 từ vựng về các loại thất nghiệp.",
                    "data": {
                        "vocabList": ["structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff"],
                        "items": [
                            {
                                "targetVocab": "structural",
                                "prompt": "Dùng từ 'structural' để viết một câu về thất nghiệp cấu trúc khi kỹ năng của người lao động không còn phù hợp với nhu cầu thị trường. Ví dụ: Structural unemployment in the coal mining regions increased as the country shifted toward renewable energy sources."
                            },
                            {
                                "targetVocab": "cyclical",
                                "prompt": "Dùng từ 'cyclical' để viết một câu về thất nghiệp theo chu kỳ kinh tế khi nền kinh tế suy thoái. Ví dụ: Cyclical unemployment peaked during the financial crisis when consumer spending collapsed and businesses across all sectors cut their workforce."
                            },
                            {
                                "targetVocab": "frictional",
                                "prompt": "Dùng từ 'frictional' để viết một câu về thất nghiệp ma sát khi người lao động đang chuyển đổi giữa các công việc. Ví dụ: Frictional unemployment among recent graduates is expected because it takes time to find a job that matches their degree and career goals."
                            },
                            {
                                "targetVocab": "seasonal",
                                "prompt": "Dùng từ 'seasonal' để viết một câu về thất nghiệp theo mùa trong một ngành phụ thuộc vào thời tiết hoặc lịch. Ví dụ: Seasonal unemployment rises in Vietnam's central coast after the summer tourist season ends and hotels reduce their staff."
                            },
                            {
                                "targetVocab": "underemployment",
                                "prompt": "Dùng từ 'underemployment' để viết một câu về tình trạng thiếu việc làm khi người lao động không được sử dụng hết năng lực. Ví dụ: Underemployment is a hidden problem — many workers have jobs but earn far less than their qualifications would suggest."
                            },
                            {
                                "targetVocab": "layoff",
                                "prompt": "Dùng từ 'layoff' để viết một câu về việc sa thải nhân viên do doanh nghiệp cắt giảm chi phí. Ví dụ: The airline announced a massive layoff of two thousand cabin crew members after international travel demand dropped by seventy percent."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về biến động lực lượng lao động hiện đại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: "
                            "unemployment — thất nghiệp, labor — lao động, workforce — lực lượng lao động, "
                            "participation — sự tham gia, wage — tiền lương, và hiring — tuyển dụng. "
                            "Trong phần 2, bạn đã học thêm: "
                            "structural — cấu trúc, cyclical — theo chu kỳ, frictional — ma sát, "
                            "seasonal — theo mùa, underemployment — thiếu việc làm, và layoff — sa thải. "
                            "Bạn đã hiểu các loại thất nghiệp khác nhau và nguyên nhân của chúng.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh rất thời sự: "
                            "thị trường lao động đang thay đổi như thế nào trong thế kỷ 21? "
                            "Bạn sẽ học 6 từ mới: vacancy, turnover, mobility, outsource, automation, và retraining.\n\n"
                            "Từ đầu tiên là vacancy — danh từ — nghĩa là vị trí tuyển dụng còn trống, "
                            "công việc mà doanh nghiệp đang cần người nhưng chưa tìm được. "
                            "Ví dụ: 'The number of job vacancies in the IT sector has reached a record high as companies struggle to find qualified programmers.' "
                            "Trong bài đọc, vacancy là chỉ số quan trọng — "
                            "khi số vacancy cao, thị trường lao động đang thiếu người.\n\n"
                            "Từ thứ hai là turnover — danh từ — nghĩa là tỷ lệ thay đổi nhân sự, "
                            "tốc độ người lao động rời đi và được thay thế trong một tổ chức. "
                            "Ví dụ: 'High employee turnover costs companies money because they must constantly recruit and train new workers.' "
                            "Trong bài đọc, turnover phản ánh sự ổn định của lực lượng lao động — "
                            "turnover cao có thể là dấu hiệu của môi trường làm việc không tốt.\n\n"
                            "Từ thứ ba là mobility — danh từ — nghĩa là tính di động, "
                            "khả năng người lao động chuyển đổi giữa các công việc, ngành nghề, hoặc địa điểm. "
                            "Ví dụ: 'Labor mobility between provinces in Vietnam has increased as young workers move to industrial zones for better wages.' "
                            "Trong bài đọc, mobility cho thấy thị trường lao động linh hoạt đến mức nào — "
                            "mobility cao giúp giảm thất nghiệp cấu trúc.\n\n"
                            "Từ thứ tư là outsource — động từ — nghĩa là thuê ngoài, "
                            "chuyển một phần công việc cho công ty hoặc quốc gia khác thực hiện. "
                            "Ví dụ: 'Many American companies outsource their customer service operations to Vietnam and the Philippines to reduce labor costs.' "
                            "Trong bài đọc, outsource là xu hướng toàn cầu hóa — "
                            "doanh nghiệp tìm kiếm lao động rẻ hơn ở nơi khác.\n\n"
                            "Từ thứ năm là automation — danh từ — nghĩa là tự động hóa, "
                            "việc sử dụng máy móc và công nghệ để thay thế lao động con người. "
                            "Ví dụ: 'Automation in garment factories has replaced many sewing jobs with robotic machines that work faster and cheaper.' "
                            "Trong bài đọc, automation là một trong những nguyên nhân chính "
                            "gây ra structural unemployment trong thế kỷ 21.\n\n"
                            "Từ cuối cùng là retraining — danh từ — nghĩa là đào tạo lại, "
                            "quá trình dạy người lao động những kỹ năng mới để họ có thể làm công việc khác. "
                            "Ví dụ: 'The government invested in retraining programs to help factory workers learn digital skills for the new economy.' "
                            "Trong bài đọc, retraining là giải pháp quan trọng nhất "
                            "cho structural unemployment — giúp người lao động thích nghi với thay đổi.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về biến động lực lượng lao động hiện đại nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Biến động lao động hiện đại",
                    "description": "Học 6 từ: vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Biến động lao động hiện đại",
                    "description": "Học 6 từ: vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Biến động lao động hiện đại",
                    "description": "Học 6 từ: vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Biến động lao động hiện đại",
                    "description": "Học 6 từ: vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Biến động lao động hiện đại",
                    "description": "Học 6 từ: vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Biến động lực lượng lao động hiện đại",
                    "description": "The labor market of the twenty-first century looks very different from the one our parents knew.",
                    "data": {
                        "text": (
                            "The labor market of the twenty-first century looks very different from the one our parents knew. "
                            "Three powerful forces — automation, outsourcing, and changing worker expectations — "
                            "are reshaping how people find work, keep work, and move between jobs.\n\n"
                            "Automation is perhaps the most visible force. "
                            "When machines and software can perform tasks that humans once did, "
                            "companies often choose the cheaper and faster option. "
                            "In Vietnam, automation has transformed the electronics manufacturing sector. "
                            "Robots now handle assembly tasks that once required hundreds of workers on a factory floor. "
                            "The result is higher productivity but fewer jobs for low-skilled workers. "
                            "This is a major driver of structural unemployment — "
                            "the workers who lose their jobs to machines often lack the skills needed for the new positions that automation creates.\n\n"
                            "The solution that economists most often recommend is retraining. "
                            "Retraining programs teach displaced workers new skills so they can move into growing industries. "
                            "For example, a garment worker who learns basic coding or data entry "
                            "may find a new career in the digital economy. "
                            "However, retraining takes time and money, and not all programs are equally effective. "
                            "The best programs combine technical skills with soft skills like communication and teamwork.\n\n"
                            "Outsourcing is another force that changes the labor landscape. "
                            "When a company decides to outsource a function — say, customer support or accounting — "
                            "it moves those jobs to another company or another country where labor costs are lower. "
                            "Vietnam has benefited from this trend: many multinational firms outsource "
                            "software development and manufacturing to Vietnamese companies. "
                            "But outsourcing also means that jobs can leave just as quickly as they arrive, "
                            "depending on where the next low-cost labor market emerges.\n\n"
                            "Within companies, two important indicators reveal the health of the internal labor market: "
                            "vacancy rates and turnover rates. "
                            "A vacancy is an open position that a company is trying to fill. "
                            "When vacancy rates are high, it means employers are struggling to find the right workers. "
                            "This can happen when the economy is booming or when there is a skills mismatch. "
                            "Turnover measures how often employees leave and are replaced. "
                            "High turnover is costly — each time a worker leaves, "
                            "the company must spend time and money on hiring and training a replacement.\n\n"
                            "Labor mobility ties all of these trends together. "
                            "Mobility refers to the ability of workers to move between jobs, industries, or locations. "
                            "In a labor market with high mobility, workers can quickly shift from declining sectors to growing ones. "
                            "Geographic mobility — moving from one city or province to another for work — "
                            "is especially important in countries like Vietnam, "
                            "where industrial zones in the south attract millions of workers from rural areas in the north and center.\n\n"
                            "The modern labor market rewards adaptability. "
                            "Workers who invest in continuous learning, who are willing to move, "
                            "and who can navigate the shifting landscape of automation and outsourcing "
                            "are the ones most likely to thrive. "
                            "For policymakers, the challenge is to support this adaptability "
                            "through education, retraining, and social safety nets that help workers during transitions."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Biến động lực lượng lao động hiện đại",
                    "description": "The labor market of the twenty-first century looks very different from the one our parents knew.",
                    "data": {
                        "text": (
                            "The labor market of the twenty-first century looks very different from the one our parents knew. "
                            "Three powerful forces — automation, outsourcing, and changing worker expectations — "
                            "are reshaping how people find work, keep work, and move between jobs.\n\n"
                            "Automation is perhaps the most visible force. "
                            "When machines and software can perform tasks that humans once did, "
                            "companies often choose the cheaper and faster option. "
                            "In Vietnam, automation has transformed the electronics manufacturing sector. "
                            "Robots now handle assembly tasks that once required hundreds of workers on a factory floor. "
                            "The result is higher productivity but fewer jobs for low-skilled workers. "
                            "This is a major driver of structural unemployment — "
                            "the workers who lose their jobs to machines often lack the skills needed for the new positions that automation creates.\n\n"
                            "The solution that economists most often recommend is retraining. "
                            "Retraining programs teach displaced workers new skills so they can move into growing industries. "
                            "For example, a garment worker who learns basic coding or data entry "
                            "may find a new career in the digital economy. "
                            "However, retraining takes time and money, and not all programs are equally effective. "
                            "The best programs combine technical skills with soft skills like communication and teamwork.\n\n"
                            "Outsourcing is another force that changes the labor landscape. "
                            "When a company decides to outsource a function — say, customer support or accounting — "
                            "it moves those jobs to another company or another country where labor costs are lower. "
                            "Vietnam has benefited from this trend: many multinational firms outsource "
                            "software development and manufacturing to Vietnamese companies. "
                            "But outsourcing also means that jobs can leave just as quickly as they arrive, "
                            "depending on where the next low-cost labor market emerges.\n\n"
                            "Within companies, two important indicators reveal the health of the internal labor market: "
                            "vacancy rates and turnover rates. "
                            "A vacancy is an open position that a company is trying to fill. "
                            "When vacancy rates are high, it means employers are struggling to find the right workers. "
                            "This can happen when the economy is booming or when there is a skills mismatch. "
                            "Turnover measures how often employees leave and are replaced. "
                            "High turnover is costly — each time a worker leaves, "
                            "the company must spend time and money on hiring and training a replacement.\n\n"
                            "Labor mobility ties all of these trends together. "
                            "Mobility refers to the ability of workers to move between jobs, industries, or locations. "
                            "In a labor market with high mobility, workers can quickly shift from declining sectors to growing ones. "
                            "Geographic mobility — moving from one city or province to another for work — "
                            "is especially important in countries like Vietnam, "
                            "where industrial zones in the south attract millions of workers from rural areas in the north and center.\n\n"
                            "The modern labor market rewards adaptability. "
                            "Workers who invest in continuous learning, who are willing to move, "
                            "and who can navigate the shifting landscape of automation and outsourcing "
                            "are the ones most likely to thrive. "
                            "For policymakers, the challenge is to support this adaptability "
                            "through education, retraining, and social safety nets that help workers during transitions."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Biến động lực lượng lao động hiện đại",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "The labor market of the twenty-first century looks very different from the one our parents knew. "
                            "Three powerful forces — automation, outsourcing, and changing worker expectations — "
                            "are reshaping how people find work, keep work, and move between jobs.\n\n"
                            "Automation is perhaps the most visible force. "
                            "When machines and software can perform tasks that humans once did, "
                            "companies often choose the cheaper and faster option. "
                            "In Vietnam, automation has transformed the electronics manufacturing sector. "
                            "Robots now handle assembly tasks that once required hundreds of workers on a factory floor. "
                            "The result is higher productivity but fewer jobs for low-skilled workers. "
                            "This is a major driver of structural unemployment — "
                            "the workers who lose their jobs to machines often lack the skills needed for the new positions that automation creates.\n\n"
                            "The solution that economists most often recommend is retraining. "
                            "Retraining programs teach displaced workers new skills so they can move into growing industries. "
                            "For example, a garment worker who learns basic coding or data entry "
                            "may find a new career in the digital economy. "
                            "However, retraining takes time and money, and not all programs are equally effective. "
                            "The best programs combine technical skills with soft skills like communication and teamwork.\n\n"
                            "Outsourcing is another force that changes the labor landscape. "
                            "When a company decides to outsource a function — say, customer support or accounting — "
                            "it moves those jobs to another company or another country where labor costs are lower. "
                            "Vietnam has benefited from this trend: many multinational firms outsource "
                            "software development and manufacturing to Vietnamese companies. "
                            "But outsourcing also means that jobs can leave just as quickly as they arrive, "
                            "depending on where the next low-cost labor market emerges.\n\n"
                            "Within companies, two important indicators reveal the health of the internal labor market: "
                            "vacancy rates and turnover rates. "
                            "A vacancy is an open position that a company is trying to fill. "
                            "When vacancy rates are high, it means employers are struggling to find the right workers. "
                            "This can happen when the economy is booming or when there is a skills mismatch. "
                            "Turnover measures how often employees leave and are replaced. "
                            "High turnover is costly — each time a worker leaves, "
                            "the company must spend time and money on hiring and training a replacement.\n\n"
                            "Labor mobility ties all of these trends together. "
                            "Mobility refers to the ability of workers to move between jobs, industries, or locations. "
                            "In a labor market with high mobility, workers can quickly shift from declining sectors to growing ones. "
                            "Geographic mobility — moving from one city or province to another for work — "
                            "is especially important in countries like Vietnam, "
                            "where industrial zones in the south attract millions of workers from rural areas in the north and center.\n\n"
                            "The modern labor market rewards adaptability. "
                            "Workers who invest in continuous learning, who are willing to move, "
                            "and who can navigate the shifting landscape of automation and outsourcing "
                            "are the ones most likely to thrive. "
                            "For policymakers, the challenge is to support this adaptability "
                            "through education, retraining, and social safety nets that help workers during transitions."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Biến động lao động hiện đại",
                    "description": "Viết câu sử dụng 6 từ vựng về biến động lực lượng lao động.",
                    "data": {
                        "vocabList": ["vacancy", "turnover", "mobility", "outsource", "automation", "retraining"],
                        "items": [
                            {
                                "targetVocab": "vacancy",
                                "prompt": "Dùng từ 'vacancy' để viết một câu về số lượng vị trí tuyển dụng còn trống trong một ngành đang thiếu nhân lực. Ví dụ: The hospital has had a vacancy for a senior surgeon for over six months because very few doctors want to work in rural areas."
                            },
                            {
                                "targetVocab": "turnover",
                                "prompt": "Dùng từ 'turnover' để viết một câu về tỷ lệ thay đổi nhân sự cao và tác động của nó đến doanh nghiệp. Ví dụ: The high turnover rate at the call center costs the company millions of dong each year in recruitment and training expenses."
                            },
                            {
                                "targetVocab": "mobility",
                                "prompt": "Dùng từ 'mobility' để viết một câu về khả năng di chuyển của người lao động giữa các ngành nghề hoặc địa điểm. Ví dụ: Greater labor mobility between provinces would help reduce unemployment in areas where factories have closed down."
                            },
                            {
                                "targetVocab": "outsource",
                                "prompt": "Dùng từ 'outsource' để viết một câu về xu hướng doanh nghiệp thuê ngoài một phần công việc để giảm chi phí. Ví dụ: The Japanese electronics company decided to outsource its assembly operations to Vietnam, creating thousands of new jobs in Bac Ninh province."
                            },
                            {
                                "targetVocab": "automation",
                                "prompt": "Dùng từ 'automation' để viết một câu về tác động của tự động hóa đến việc làm trong một ngành cụ thể. Ví dụ: Automation in the banking sector has reduced the need for tellers, but it has also created new positions in cybersecurity and data analysis."
                            },
                            {
                                "targetVocab": "retraining",
                                "prompt": "Dùng từ 'retraining' để viết một câu về chương trình đào tạo lại giúp người lao động thích nghi với thay đổi công nghệ. Ví dụ: The government launched a retraining program for textile workers, teaching them how to operate computerized sewing machines and quality control systems."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Thị trường Lao động. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "unemployment — thất nghiệp, labor — lao động, workforce — lực lượng lao động, "
                            "participation — sự tham gia, wage — tiền lương, và hiring — tuyển dụng. "
                            "Đây là bộ khung cơ bản để hiểu thị trường việc làm.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "structural — cấu trúc, cyclical — theo chu kỳ, frictional — ma sát, "
                            "seasonal — theo mùa, underemployment — thiếu việc làm, và layoff — sa thải. "
                            "Những từ này giúp bạn phân loại và phân tích các dạng thất nghiệp khác nhau.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "vacancy — vị trí tuyển dụng trống, turnover — tỷ lệ thay đổi nhân sự, "
                            "mobility — tính di động, outsource — thuê ngoài, "
                            "automation — tự động hóa, và retraining — đào tạo lại. "
                            "Đây là những từ về xu hướng biến động của thị trường lao động hiện đại.\n\n"
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
                    "description": "Học 18 từ: unemployment, labor, workforce, participation, wage, hiring, structural, cyclical, frictional, seasonal, underemployment, layoff, vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: unemployment, labor, workforce, participation, wage, hiring, structural, cyclical, frictional, seasonal, underemployment, layoff, vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: unemployment, labor, workforce, participation, wage, hiring, structural, cyclical, frictional, seasonal, underemployment, layoff, vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: unemployment, labor, workforce, participation, wage, hiring, structural, cyclical, frictional, seasonal, underemployment, layoff, vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: unemployment, labor, workforce, participation, wage, hiring, structural, cyclical, frictional, seasonal, underemployment, layoff, vacancy, turnover, mobility, outsource, automation, retraining",
                    "data": {"vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng thị trường lao động",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"],
                        "items": [
                            {
                                "targetVocab": "unemployment",
                                "prompt": "Dùng từ 'unemployment' để viết một câu về tác động của thất nghiệp đến đời sống xã hội ở Việt Nam. Ví dụ: Rising unemployment among young graduates has become a major social concern in Vietnam, as many struggle to find jobs that match their education."
                            },
                            {
                                "targetVocab": "labor",
                                "prompt": "Dùng từ 'labor' để viết một câu về chi phí lao động ảnh hưởng đến quyết định đầu tư của doanh nghiệp nước ngoài. Ví dụ: The relatively low cost of labor in Vietnam continues to attract foreign direct investment from South Korea, Japan, and Taiwan."
                            },
                            {
                                "targetVocab": "workforce",
                                "prompt": "Dùng từ 'workforce' để viết một câu về sự thay đổi cơ cấu lực lượng lao động theo thời gian. Ví dụ: The Vietnamese workforce is gradually shifting from agriculture to manufacturing and services as the economy modernizes."
                            },
                            {
                                "targetVocab": "participation",
                                "prompt": "Dùng từ 'participation' để viết một câu về tỷ lệ tham gia lao động của phụ nữ và ý nghĩa kinh tế. Ví dụ: Increasing female participation in the workforce could add billions of dollars to Vietnam's GDP over the next decade."
                            },
                            {
                                "targetVocab": "wage",
                                "prompt": "Dùng từ 'wage' để viết một câu về sự chênh lệch tiền lương giữa các ngành hoặc khu vực. Ví dụ: The wage gap between technology workers and factory workers has widened significantly as demand for digital skills continues to grow."
                            },
                            {
                                "targetVocab": "hiring",
                                "prompt": "Dùng từ 'hiring' để viết một câu về xu hướng tuyển dụng phản ánh tình hình kinh tế. Ví dụ: A freeze in hiring across the banking sector signals that financial institutions are preparing for a period of slower economic growth."
                            },
                            {
                                "targetVocab": "structural",
                                "prompt": "Dùng từ 'structural' để viết một câu về thất nghiệp cấu trúc do thay đổi công nghệ gây ra. Ví dụ: Structural unemployment in the textile industry is rising as automated looms replace workers who have spent decades operating manual machines."
                            },
                            {
                                "targetVocab": "cyclical",
                                "prompt": "Dùng từ 'cyclical' để viết một câu về mối quan hệ giữa thất nghiệp theo chu kỳ và chính sách kinh tế. Ví dụ: The government increased public spending on infrastructure projects to reduce cyclical unemployment during the economic downturn."
                            },
                            {
                                "targetVocab": "frictional",
                                "prompt": "Dùng từ 'frictional' để viết một câu về thất nghiệp ma sát như một phần tự nhiên của thị trường lao động. Ví dụ: Online job platforms have helped reduce frictional unemployment by making it easier for workers and employers to find each other quickly."
                            },
                            {
                                "targetVocab": "seasonal",
                                "prompt": "Dùng từ 'seasonal' để viết một câu về thất nghiệp theo mùa trong ngành nông nghiệp hoặc du lịch. Ví dụ: Seasonal unemployment in the Mekong Delta peaks after the rice harvest when farm laborers have no crops to tend until the next planting season."
                            },
                            {
                                "targetVocab": "underemployment",
                                "prompt": "Dùng từ 'underemployment' để viết một câu về tình trạng thiếu việc làm ẩn sau con số thất nghiệp chính thức. Ví dụ: The official unemployment rate looks low, but underemployment remains high as many workers can only find part-time or informal jobs."
                            },
                            {
                                "targetVocab": "layoff",
                                "prompt": "Dùng từ 'layoff' để viết một câu về đợt sa thải lớn và tác động đến cộng đồng địa phương. Ví dụ: The factory layoff affected the entire town because most families depended on the plant for their income."
                            },
                            {
                                "targetVocab": "vacancy",
                                "prompt": "Dùng từ 'vacancy' để viết một câu về mối quan hệ giữa số vị trí tuyển dụng trống và tình trạng thiếu kỹ năng. Ví dụ: Despite high unemployment, thousands of vacancies in the cybersecurity field remain unfilled because few workers have the required technical certifications."
                            },
                            {
                                "targetVocab": "turnover",
                                "prompt": "Dùng từ 'turnover' để viết một câu về nguyên nhân và hậu quả của tỷ lệ thay đổi nhân sự cao. Ví dụ: The restaurant chain reduced its turnover rate by offering better wages and a clear path for career advancement to its kitchen staff."
                            },
                            {
                                "targetVocab": "mobility",
                                "prompt": "Dùng từ 'mobility' để viết một câu về tính di động lao động giúp giảm thất nghiệp ở một khu vực. Ví dụ: Improved transportation links between rural provinces and industrial cities have increased labor mobility and reduced regional unemployment."
                            },
                            {
                                "targetVocab": "outsource",
                                "prompt": "Dùng từ 'outsource' để viết một câu về tác động hai mặt của việc thuê ngoài đối với thị trường lao động. Ví dụ: When the American firm decided to outsource its accounting department to India, it saved money but eliminated three hundred domestic jobs."
                            },
                            {
                                "targetVocab": "automation",
                                "prompt": "Dùng từ 'automation' để viết một câu về cách tự động hóa vừa tạo ra vừa xóa bỏ việc làm. Ví dụ: Automation in the logistics industry has eliminated many warehouse packing jobs but created new roles for technicians who maintain and program the robots."
                            },
                            {
                                "targetVocab": "retraining",
                                "prompt": "Dùng từ 'retraining' để viết một câu về tầm quan trọng của đào tạo lại trong nền kinh tế đang thay đổi nhanh. Ví dụ: The success of the retraining program was measured by how many former coal miners found stable employment in the solar energy industry within two years."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về thị trường lao động.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về thị trường lao động — từ những khái niệm cơ bản "
                            "đến những xu hướng biến động của thế kỷ 21.\n\n"
                            "Bạn sẽ gặp lại unemployment, labor, workforce, participation, wage, hiring "
                            "trong phần mở đầu về cơ chế thị trường việc làm. "
                            "Tiếp theo, structural, cyclical, frictional, seasonal, underemployment, layoff "
                            "sẽ giúp bạn hiểu sâu hơn về các dạng thất nghiệp. "
                            "Và cuối cùng, vacancy, turnover, mobility, outsource, automation, retraining "
                            "sẽ đưa bạn vào thế giới lao động hiện đại.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thị trường lao động — Bức tranh toàn cảnh",
                    "description": "Behind every economic statistic is a human story — and nowhere is this more true than in the labor market.",
                    "data": {
                        "text": (
                            "Behind every economic statistic is a human story — "
                            "and nowhere is this more true than in the labor market. "
                            "The labor market is where people offer their time, skills, and energy in exchange for wages, "
                            "and where businesses search for the workers they need to produce goods and services. "
                            "Understanding how this market works is essential for anyone studying macroeconomics.\n\n"
                            "The workforce of a country includes everyone who is either employed or actively seeking employment. "
                            "Not all adults are part of the workforce — students, retirees, and those who have stopped looking for work are excluded. "
                            "The participation rate measures what share of the working-age population is engaged in the labor market. "
                            "A falling participation rate can be a warning sign: "
                            "it may mean that people are discouraged and have given up the search for jobs.\n\n"
                            "Unemployment is the most visible indicator of labor market health. "
                            "But not all unemployment is alike. "
                            "Cyclical unemployment rises and falls with the business cycle. "
                            "During a recession, companies face lower demand for their products, "
                            "so they reduce costs by announcing layoffs. "
                            "A layoff is not a reflection of a worker's ability — "
                            "it is a business decision driven by economic conditions. "
                            "When the economy recovers, hiring picks up and cyclical unemployment falls.\n\n"
                            "Structural unemployment is harder to fix. "
                            "It happens when the skills workers have no longer match what employers need. "
                            "Automation is a major cause: when factories install robots to do assembly work, "
                            "the workers who once did those tasks may find themselves without marketable skills. "
                            "The gap between what workers can do and what the economy demands "
                            "creates long-term unemployment that does not disappear simply because the economy grows.\n\n"
                            "Frictional unemployment is the healthiest kind. "
                            "It exists because workers need time to search for the right job, "
                            "and employers need time to find the right candidate. "
                            "A recent graduate exploring career options or a professional switching industries "
                            "both contribute to frictional unemployment. "
                            "This type is temporary and reflects a dynamic, functioning labor market.\n\n"
                            "Seasonal unemployment follows the calendar. "
                            "Tourism workers in coastal cities, farm laborers after the harvest, "
                            "and retail staff after the holiday shopping season all experience seasonal job loss. "
                            "It is predictable, but for the workers affected, the income gap between seasons can be painful.\n\n"
                            "Even when the unemployment rate looks low, the picture may not be as bright as it seems. "
                            "Underemployment captures the workers who have jobs but are not fully utilized — "
                            "a university-trained accountant driving a taxi, "
                            "or a nurse working only ten hours a week when she wants forty. "
                            "Underemployment is invisible in the headline numbers but very real in people's lives.\n\n"
                            "Inside companies, two metrics reveal how well the internal labor market is functioning. "
                            "The vacancy rate shows how many positions remain unfilled. "
                            "High vacancy rates can signal a skills shortage — "
                            "there are jobs available, but not enough qualified workers to fill them. "
                            "The turnover rate measures how frequently employees leave and must be replaced. "
                            "High turnover drives up costs for hiring and training, "
                            "and it can damage team morale and productivity.\n\n"
                            "Labor mobility — the ability of workers to move between jobs, industries, and regions — "
                            "is what keeps the market flexible. "
                            "When workers can relocate from a province with few opportunities "
                            "to an industrial zone with many vacancies, unemployment falls and wages adjust. "
                            "Mobility also means career mobility: a worker who retrains from manufacturing to information technology "
                            "is exercising mobility across industries.\n\n"
                            "Two global trends are reshaping labor markets everywhere. "
                            "Companies increasingly outsource tasks to countries where labor is cheaper, "
                            "moving call centers, software development, and even accounting across borders. "
                            "At the same time, automation continues to replace routine tasks with machines and algorithms. "
                            "Both trends create winners and losers. "
                            "The workers who lose out need retraining — "
                            "programs that teach them new skills so they can re-enter the workforce in a different role.\n\n"
                            "The story of the labor market is ultimately a story about people: "
                            "their search for meaningful work, their resilience when jobs disappear, "
                            "and their willingness to learn and adapt. "
                            "Every wage negotiation, every hiring decision, every layoff, "
                            "and every retraining program reflects the constant push and pull "
                            "between what the economy needs and what workers can offer. "
                            "Learning to read this story in English gives you a powerful lens "
                            "for understanding not just economics, but the world around you."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thị trường lao động — Bức tranh toàn cảnh",
                    "description": "Behind every economic statistic is a human story — and nowhere is this more true than in the labor market.",
                    "data": {
                        "text": (
                            "Behind every economic statistic is a human story — "
                            "and nowhere is this more true than in the labor market. "
                            "The labor market is where people offer their time, skills, and energy in exchange for wages, "
                            "and where businesses search for the workers they need to produce goods and services. "
                            "Understanding how this market works is essential for anyone studying macroeconomics.\n\n"
                            "The workforce of a country includes everyone who is either employed or actively seeking employment. "
                            "Not all adults are part of the workforce — students, retirees, and those who have stopped looking for work are excluded. "
                            "The participation rate measures what share of the working-age population is engaged in the labor market. "
                            "A falling participation rate can be a warning sign: "
                            "it may mean that people are discouraged and have given up the search for jobs.\n\n"
                            "Unemployment is the most visible indicator of labor market health. "
                            "But not all unemployment is alike. "
                            "Cyclical unemployment rises and falls with the business cycle. "
                            "During a recession, companies face lower demand for their products, "
                            "so they reduce costs by announcing layoffs. "
                            "A layoff is not a reflection of a worker's ability — "
                            "it is a business decision driven by economic conditions. "
                            "When the economy recovers, hiring picks up and cyclical unemployment falls.\n\n"
                            "Structural unemployment is harder to fix. "
                            "It happens when the skills workers have no longer match what employers need. "
                            "Automation is a major cause: when factories install robots to do assembly work, "
                            "the workers who once did those tasks may find themselves without marketable skills. "
                            "The gap between what workers can do and what the economy demands "
                            "creates long-term unemployment that does not disappear simply because the economy grows.\n\n"
                            "Frictional unemployment is the healthiest kind. "
                            "It exists because workers need time to search for the right job, "
                            "and employers need time to find the right candidate. "
                            "A recent graduate exploring career options or a professional switching industries "
                            "both contribute to frictional unemployment. "
                            "This type is temporary and reflects a dynamic, functioning labor market.\n\n"
                            "Seasonal unemployment follows the calendar. "
                            "Tourism workers in coastal cities, farm laborers after the harvest, "
                            "and retail staff after the holiday shopping season all experience seasonal job loss. "
                            "It is predictable, but for the workers affected, the income gap between seasons can be painful.\n\n"
                            "Even when the unemployment rate looks low, the picture may not be as bright as it seems. "
                            "Underemployment captures the workers who have jobs but are not fully utilized — "
                            "a university-trained accountant driving a taxi, "
                            "or a nurse working only ten hours a week when she wants forty. "
                            "Underemployment is invisible in the headline numbers but very real in people's lives.\n\n"
                            "Inside companies, two metrics reveal how well the internal labor market is functioning. "
                            "The vacancy rate shows how many positions remain unfilled. "
                            "High vacancy rates can signal a skills shortage — "
                            "there are jobs available, but not enough qualified workers to fill them. "
                            "The turnover rate measures how frequently employees leave and must be replaced. "
                            "High turnover drives up costs for hiring and training, "
                            "and it can damage team morale and productivity.\n\n"
                            "Labor mobility — the ability of workers to move between jobs, industries, and regions — "
                            "is what keeps the market flexible. "
                            "When workers can relocate from a province with few opportunities "
                            "to an industrial zone with many vacancies, unemployment falls and wages adjust. "
                            "Mobility also means career mobility: a worker who retrains from manufacturing to information technology "
                            "is exercising mobility across industries.\n\n"
                            "Two global trends are reshaping labor markets everywhere. "
                            "Companies increasingly outsource tasks to countries where labor is cheaper, "
                            "moving call centers, software development, and even accounting across borders. "
                            "At the same time, automation continues to replace routine tasks with machines and algorithms. "
                            "Both trends create winners and losers. "
                            "The workers who lose out need retraining — "
                            "programs that teach them new skills so they can re-enter the workforce in a different role.\n\n"
                            "The story of the labor market is ultimately a story about people: "
                            "their search for meaningful work, their resilience when jobs disappear, "
                            "and their willingness to learn and adapt. "
                            "Every wage negotiation, every hiring decision, every layoff, "
                            "and every retraining program reflects the constant push and pull "
                            "between what the economy needs and what workers can offer. "
                            "Learning to read this story in English gives you a powerful lens "
                            "for understanding not just economics, but the world around you."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thị trường lao động — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Behind every economic statistic is a human story — "
                            "and nowhere is this more true than in the labor market. "
                            "The labor market is where people offer their time, skills, and energy in exchange for wages, "
                            "and where businesses search for the workers they need to produce goods and services. "
                            "Understanding how this market works is essential for anyone studying macroeconomics.\n\n"
                            "The workforce of a country includes everyone who is either employed or actively seeking employment. "
                            "Not all adults are part of the workforce — students, retirees, and those who have stopped looking for work are excluded. "
                            "The participation rate measures what share of the working-age population is engaged in the labor market. "
                            "A falling participation rate can be a warning sign: "
                            "it may mean that people are discouraged and have given up the search for jobs.\n\n"
                            "Unemployment is the most visible indicator of labor market health. "
                            "But not all unemployment is alike. "
                            "Cyclical unemployment rises and falls with the business cycle. "
                            "During a recession, companies face lower demand for their products, "
                            "so they reduce costs by announcing layoffs. "
                            "A layoff is not a reflection of a worker's ability — "
                            "it is a business decision driven by economic conditions. "
                            "When the economy recovers, hiring picks up and cyclical unemployment falls.\n\n"
                            "Structural unemployment is harder to fix. "
                            "It happens when the skills workers have no longer match what employers need. "
                            "Automation is a major cause: when factories install robots to do assembly work, "
                            "the workers who once did those tasks may find themselves without marketable skills. "
                            "The gap between what workers can do and what the economy demands "
                            "creates long-term unemployment that does not disappear simply because the economy grows.\n\n"
                            "Frictional unemployment is the healthiest kind. "
                            "It exists because workers need time to search for the right job, "
                            "and employers need time to find the right candidate. "
                            "A recent graduate exploring career options or a professional switching industries "
                            "both contribute to frictional unemployment. "
                            "This type is temporary and reflects a dynamic, functioning labor market.\n\n"
                            "Seasonal unemployment follows the calendar. "
                            "Tourism workers in coastal cities, farm laborers after the harvest, "
                            "and retail staff after the holiday shopping season all experience seasonal job loss. "
                            "It is predictable, but for the workers affected, the income gap between seasons can be painful.\n\n"
                            "Even when the unemployment rate looks low, the picture may not be as bright as it seems. "
                            "Underemployment captures the workers who have jobs but are not fully utilized — "
                            "a university-trained accountant driving a taxi, "
                            "or a nurse working only ten hours a week when she wants forty. "
                            "Underemployment is invisible in the headline numbers but very real in people's lives.\n\n"
                            "Inside companies, two metrics reveal how well the internal labor market is functioning. "
                            "The vacancy rate shows how many positions remain unfilled. "
                            "High vacancy rates can signal a skills shortage — "
                            "there are jobs available, but not enough qualified workers to fill them. "
                            "The turnover rate measures how frequently employees leave and must be replaced. "
                            "High turnover drives up costs for hiring and training, "
                            "and it can damage team morale and productivity.\n\n"
                            "Labor mobility — the ability of workers to move between jobs, industries, and regions — "
                            "is what keeps the market flexible. "
                            "When workers can relocate from a province with few opportunities "
                            "to an industrial zone with many vacancies, unemployment falls and wages adjust. "
                            "Mobility also means career mobility: a worker who retrains from manufacturing to information technology "
                            "is exercising mobility across industries.\n\n"
                            "Two global trends are reshaping labor markets everywhere. "
                            "Companies increasingly outsource tasks to countries where labor is cheaper, "
                            "moving call centers, software development, and even accounting across borders. "
                            "At the same time, automation continues to replace routine tasks with machines and algorithms. "
                            "Both trends create winners and losers. "
                            "The workers who lose out need retraining — "
                            "programs that teach them new skills so they can re-enter the workforce in a different role.\n\n"
                            "The story of the labor market is ultimately a story about people: "
                            "their search for meaningful work, their resilience when jobs disappear, "
                            "and their willingness to learn and adapt. "
                            "Every wage negotiation, every hiring decision, every layoff, "
                            "and every retraining program reflects the constant push and pull "
                            "between what the economy needs and what workers can offer. "
                            "Learning to read this story in English gives you a powerful lens "
                            "for understanding not just economics, but the world around you."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích thị trường lao động",
                    "description": "Viết đoạn văn tiếng Anh phân tích về thị trường lao động sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["unemployment", "labor", "workforce", "participation", "wage", "hiring", "structural", "cyclical", "frictional", "seasonal", "underemployment", "layoff", "vacancy", "turnover", "mobility", "outsource", "automation", "retraining"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến thị trường lao động. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích tác động của automation đến thị trường lao động Việt Nam. Giải thích loại unemployment nào tăng lên (structural hay cyclical), tại sao retraining là giải pháp quan trọng, và mobility giúp người lao động thích nghi như thế nào.",
                            "Hãy chọn một ngành ở Việt Nam (ví dụ: du lịch, công nghệ, nông nghiệp) và phân tích tình hình hiring, wage, và vacancy trong ngành đó. Giải thích ngành đó có bị ảnh hưởng bởi seasonal unemployment không, và turnover rate cao hay thấp vì lý do gì."
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
                            "Có điều gì đó rất đẹp trong việc học ngôn ngữ kinh tế. "
                            "Mỗi từ bạn vừa học không chỉ là một định nghĩa trong sách giáo khoa — "
                            "nó là một cánh cửa nhỏ mở ra một góc nhìn mới về cuộc sống con người.\n\n"
                            "Hãy cùng nhìn lại một số từ quan trọng nhất.\n\n"
                            "Unemployment — thất nghiệp. Đằng sau con số phần trăm khô khan ấy "
                            "là hàng triệu câu chuyện cá nhân — người cha mất việc không biết nói gì với con, "
                            "cô sinh viên tốt nghiệp gửi hàng trăm đơn xin việc mà không nhận được hồi âm. "
                            "Ví dụ mới: Youth unemployment in many developing countries exceeds twenty percent, "
                            "meaning one in five young people who want to work cannot find a job.\n\n"
                            "Structural — mang tính cấu trúc. Từ này nhắc chúng ta rằng "
                            "thế giới không đứng yên. Khi nền kinh tế thay đổi, "
                            "những kỹ năng từng có giá trị có thể trở nên lỗi thời. "
                            "Ví dụ mới: Structural changes in the energy sector mean that workers in coal plants "
                            "must learn entirely new skills to find employment in solar or wind energy.\n\n"
                            "Automation — tự động hóa. Có lẽ không có từ nào trong bài học này "
                            "gợi lên nhiều cảm xúc phức tạp hơn. Automation vừa là lời hứa về tiến bộ, "
                            "vừa là nỗi lo về tương lai. Nó tạo ra sự giàu có, "
                            "nhưng cũng để lại những người lao động đứng bên lề. "
                            "Ví dụ mới: The automation of customer service through chatbots has improved efficiency "
                            "but left many call center workers searching for new careers.\n\n"
                            "Retraining — đào tạo lại. Đây là từ mang nhiều hy vọng nhất. "
                            "Nó nói rằng: dù thế giới thay đổi, con người có khả năng thích nghi. "
                            "Một người thợ may có thể học lập trình. Một công nhân nhà máy có thể trở thành kỹ thuật viên. "
                            "Ví dụ mới: A successful retraining initiative in South Korea helped thousands of shipyard workers "
                            "transition into the semiconductor industry when global demand for ships declined.\n\n"
                            "Mobility — tính di động. Từ này nhẹ nhàng nhưng sâu sắc. "
                            "Nó nói về khả năng con người di chuyển — không chỉ về mặt địa lý, "
                            "mà còn về mặt nghề nghiệp và tư duy. "
                            "Ví dụ mới: Career mobility has become more important than job security "
                            "in an economy where the average worker changes careers three to five times in a lifetime.\n\n"
                            "Wage — tiền lương. Đằng sau mỗi con số lương là một cuộc thương lượng "
                            "giữa giá trị mà người lao động tạo ra và giá trị mà thị trường sẵn sàng trả. "
                            "Ví dụ mới: The debate over a living wage asks a profound question: "
                            "should the market alone decide how much a worker's time is worth?\n\n"
                            "Bạn biết không, khi bạn đọc tin tức về một nhà máy đóng cửa, "
                            "bạn sẽ không chỉ thấy con số — bạn sẽ thấy layoff, structural unemployment, "
                            "và nhu cầu retraining. Khi bạn nghe về một khu công nghiệp mới mở, "
                            "bạn sẽ nghĩ đến hiring, vacancy, và labor mobility. "
                            "Ngôn ngữ không chỉ giúp bạn đọc — nó giúp bạn nhìn.\n\n"
                            "Có một điều kỳ diệu trong việc học: "
                            "mỗi từ mới không chỉ thêm vào vốn từ vựng của bạn — "
                            "nó thêm vào cách bạn hiểu thế giới. "
                            "Và thế giới của thị trường lao động, với tất cả sự phức tạp và nhân văn của nó, "
                            "giờ đây đã gần hơn với bạn một chút.\n\n"
                            "Cảm ơn bạn đã đi cùng bài học này. "
                            "Hẹn gặp lại bạn ở hành trình tiếp theo."
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Labor Markets – Thị Trường Lao Động' AND uid = '{UID}' ORDER BY created_at;")
