"""
Create curriculum: Market Research – Nghiên Cứu Thị Trường
Series E — Marketing & Quản Trị (Marketing & Management), curriculum #1, displayOrder 0
18 words | 5 sessions | vivid_scenario tone | practical momentum farewell
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
W1 = ["research", "survey", "sample", "demographic", "segment", "target"]
W2 = ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"]
W3 = ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Market Research – Nghiên Cứu Thị Trường",
    "contentTypeTags": [],
    "description": (
        "HÃY TƯỞNG TƯỢNG BẠN ĐANG NGỒI TRONG PHÒNG HỌP CỦA MỘT CÔNG TY FMCG — "
        "TRƯỚC MẶT BẠN LÀ 500 TRANG DỮ LIỆU KHẢO SÁT NGƯỜI TIÊU DÙNG, "
        "VÀ SẾP YÊU CẦU BẠN TÓM TẮT BẰNG TIẾNG ANH TRONG 10 PHÚT.\n\n"
        "Bạn biết rõ thị trường Việt Nam — biết rằng giới trẻ Gen Z ở Sài Gòn "
        "mua sắm khác hẳn phụ huynh họ ở Đà Nẵng. Bạn hiểu demographic, "
        "hiểu segment, hiểu target audience bằng tiếng Việt. "
        "Nhưng khi đối tác Singapore hỏi 'What does your qualitative research suggest about this segment?' — "
        "bạn chỉ biết im lặng.\n\n"
        "Nghiên cứu thị trường là la bàn của mọi quyết định kinh doanh — "
        "không có nó, bạn đang bắn tên trong bóng tối. "
        "Và ngôn ngữ của nghiên cứu thị trường quốc tế là tiếng Anh. "
        "Từ survey design đến sampling methodology, từ focus group đến trend forecast — "
        "tất cả đều được viết, trình bày và thảo luận bằng tiếng Anh.\n\n"
        "18 từ vựng trong bài học này sẽ biến bạn từ người đọc báo cáo thụ động "
        "thành người phân tích chủ động — người có thể đặt câu hỏi đúng, "
        "phát hiện bias trong dữ liệu, và trình bày insight bằng ngôn ngữ chuyên nghiệp.\n\n"
        "Học qua bài đọc, flashcard, luyện nói và viết — "
        "bạn vừa nâng cấp tư duy nghiên cứu thị trường, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về nghiên cứu thị trường — "
            "ngôn ngữ chung của mọi bộ phận marketing trên thế giới. "
            "Bạn sẽ bắt đầu với research, survey, sample, demographic, segment, target — "
            "những từ nền tảng giúp bạn hiểu cách doanh nghiệp thu thập và phân loại dữ liệu khách hàng. "
            "Tiếp theo là qualitative, quantitative, focus, panel, respondent, bias — "
            "bộ từ vựng về phương pháp nghiên cứu, từ phỏng vấn sâu đến khảo sát quy mô lớn. "
            "Cuối cùng, insight, trend, forecast, correlation, hypothesis, methodology "
            "đưa bạn vào thế giới phân tích dữ liệu và dự báo xu hướng tiêu dùng. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu báo cáo nghiên cứu thị trường bằng tiếng Anh — "
            "và trình bày kết quả trước đối tác quốc tế mà không cần dừng lại tìm từ."
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
                    "description": "Chào mừng bạn đến với bài học về nghiên cứu thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học đầu tiên trong chuỗi từ vựng Marketing và Quản trị — "
                            "chủ đề hôm nay là Nghiên cứu thị trường, hay trong tiếng Anh là Market Research. "
                            "Trước khi một doanh nghiệp tung ra sản phẩm mới, trước khi chạy quảng cáo, "
                            "trước khi quyết định mở rộng sang thị trường mới — họ phải hiểu khách hàng. "
                            "Và cách duy nhất để hiểu khách hàng một cách có hệ thống là nghiên cứu thị trường.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: research, survey, sample, demographic, segment, và target. "
                            "Đây là những từ nền tảng nhất — bạn sẽ gặp chúng trong mọi báo cáo nghiên cứu thị trường.\n\n"
                            "Từ đầu tiên là research — danh từ/động từ — nghĩa là nghiên cứu, "
                            "quá trình thu thập và phân tích thông tin một cách có hệ thống để hiểu một vấn đề. "
                            "Ví dụ: 'The company invested two billion dong in market research before launching its new line of organic skincare products in Vietnam.' "
                            "Trong bài đọc, research là bước đầu tiên và quan trọng nhất — "
                            "không có research, mọi quyết định marketing đều dựa trên phỏng đoán.\n\n"
                            "Từ thứ hai là survey — danh từ/động từ — nghĩa là khảo sát, "
                            "phương pháp thu thập dữ liệu bằng cách đặt câu hỏi cho một nhóm người. "
                            "Ví dụ: 'The marketing team designed an online survey with twenty questions to understand why customers were switching to a competitor brand.' "
                            "Trong bài đọc, survey là công cụ phổ biến nhất trong nghiên cứu thị trường — "
                            "từ khảo sát trực tuyến đến phỏng vấn trực tiếp.\n\n"
                            "Từ thứ ba là sample — danh từ — nghĩa là mẫu, "
                            "một nhóm nhỏ được chọn từ tổng thể để đại diện cho toàn bộ dân số mục tiêu. "
                            "Ví dụ: 'The researchers selected a sample of one thousand consumers across five major cities to ensure the results reflected national buying patterns.' "
                            "Trong bài đọc, sample quyết định độ tin cậy của nghiên cứu — "
                            "mẫu quá nhỏ hoặc không đại diện sẽ cho kết quả sai lệch.\n\n"
                            "Từ thứ tư là demographic — danh từ/tính từ — nghĩa là nhân khẩu học, "
                            "đặc điểm dân số như tuổi, giới tính, thu nhập, trình độ học vấn. "
                            "Ví dụ: 'The demographic data showed that seventy percent of the brand's customers were women aged twenty-five to thirty-five with above-average household income.' "
                            "Trong bài đọc, demographic giúp doanh nghiệp hiểu khách hàng là ai — "
                            "không phải họ nghĩ gì, mà họ thuộc nhóm nào.\n\n"
                            "Từ thứ năm là segment — danh từ/động từ — nghĩa là phân khúc, "
                            "một nhóm khách hàng có đặc điểm hoặc nhu cầu tương tự nhau. "
                            "Ví dụ: 'The company identified three distinct market segments: budget-conscious students, young professionals seeking convenience, and premium buyers who prioritize quality.' "
                            "Trong bài đọc, segment là kết quả của việc phân tích dữ liệu — "
                            "khi bạn chia thị trường thành các nhóm nhỏ hơn để phục vụ tốt hơn.\n\n"
                            "Từ cuối cùng là target — danh từ/động từ/tính từ — nghĩa là mục tiêu, "
                            "nhóm khách hàng cụ thể mà doanh nghiệp chọn để tập trung phục vụ. "
                            "Ví dụ: 'After analyzing the research data, the team decided to target young urban professionals aged twenty-two to thirty who use social media daily.' "
                            "Trong bài đọc, target là bước cuối cùng sau khi phân khúc — "
                            "bạn chọn segment nào để tập trung nguồn lực marketing.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách doanh nghiệp thu thập dữ liệu khách hàng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng nghiên cứu thị trường",
                    "description": "Học 6 từ: research, survey, sample, demographic, segment, target",
                    "data": {"vocabList": ["research", "survey", "sample", "demographic", "segment", "target"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng nghiên cứu thị trường",
                    "description": "Học 6 từ: research, survey, sample, demographic, segment, target",
                    "data": {"vocabList": ["research", "survey", "sample", "demographic", "segment", "target"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng nghiên cứu thị trường",
                    "description": "Học 6 từ: research, survey, sample, demographic, segment, target",
                    "data": {"vocabList": ["research", "survey", "sample", "demographic", "segment", "target"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng nghiên cứu thị trường",
                    "description": "Học 6 từ: research, survey, sample, demographic, segment, target",
                    "data": {"vocabList": ["research", "survey", "sample", "demographic", "segment", "target"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nền tảng nghiên cứu thị trường",
                    "description": "Học 6 từ: research, survey, sample, demographic, segment, target",
                    "data": {"vocabList": ["research", "survey", "sample", "demographic", "segment", "target"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thu thập dữ liệu khách hàng",
                    "description": "Every successful product begins not in a factory or a design studio, but in the mind of the customer.",
                    "data": {
                        "text": (
                            "Every successful product begins not in a factory or a design studio, "
                            "but in the mind of the customer. The challenge for any business "
                            "is to understand what customers think, want, and need — "
                            "and that is exactly what market research does.\n\n"
                            "Market research is the systematic process of gathering, recording, "
                            "and analyzing information about customers, competitors, and the market itself. "
                            "A Vietnamese coffee chain planning to open stores in a new city, "
                            "for example, would conduct research to understand local drinking habits, "
                            "price sensitivity, and the competitive landscape. "
                            "Without research, the company would be guessing — "
                            "and in business, guessing is expensive.\n\n"
                            "One of the most common tools in market research is the survey. "
                            "A survey is a structured set of questions designed to collect data "
                            "from a group of people. Surveys can be conducted online, by phone, "
                            "in person, or through mobile apps. "
                            "A well-designed survey asks clear, unbiased questions "
                            "and gives respondents enough options to express their true opinions. "
                            "A poorly designed survey leads to unreliable data.\n\n"
                            "But a survey is only as good as the people who answer it. "
                            "This is where the concept of a sample becomes critical. "
                            "A sample is a smaller group selected from the larger population "
                            "that the researcher wants to study. "
                            "If a company wants to understand the preferences of all Vietnamese women "
                            "aged eighteen to thirty-five, it cannot interview every single one. "
                            "Instead, it selects a representative sample — perhaps one thousand women "
                            "from different cities, income levels, and educational backgrounds. "
                            "The quality of the sample determines whether the findings "
                            "can be generalized to the entire population.\n\n"
                            "To build a good sample, researchers rely on demographic data. "
                            "A demographic is a statistical characteristic of a population — "
                            "age, gender, income, education, occupation, marital status, and location. "
                            "Demographic information helps researchers ensure that their sample "
                            "mirrors the real population. If sixty percent of a city's consumers "
                            "are under thirty, then roughly sixty percent of the sample "
                            "should also be under thirty.\n\n"
                            "Once the data is collected, the next step is segmentation. "
                            "To segment a market means to divide it into distinct groups "
                            "based on shared characteristics or behaviors. "
                            "A smartphone company might segment its market by income level: "
                            "budget buyers, mid-range buyers, and premium buyers. "
                            "Each segment has different needs, different price expectations, "
                            "and different reasons for choosing a product.\n\n"
                            "After identifying segments, the company must decide which one to target. "
                            "Targeting means selecting the specific segment or segments "
                            "that the company will focus its marketing efforts on. "
                            "A small Vietnamese tea brand might target health-conscious professionals "
                            "in Ho Chi Minh City rather than trying to sell to everyone in the country. "
                            "By choosing a clear target, the company can craft messages, "
                            "design products, and set prices that resonate with that specific group."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thu thập dữ liệu khách hàng",
                    "description": "Every successful product begins not in a factory or a design studio, but in the mind of the customer.",
                    "data": {
                        "text": (
                            "Every successful product begins not in a factory or a design studio, "
                            "but in the mind of the customer. The challenge for any business "
                            "is to understand what customers think, want, and need — "
                            "and that is exactly what market research does.\n\n"
                            "Market research is the systematic process of gathering, recording, "
                            "and analyzing information about customers, competitors, and the market itself. "
                            "A Vietnamese coffee chain planning to open stores in a new city, "
                            "for example, would conduct research to understand local drinking habits, "
                            "price sensitivity, and the competitive landscape. "
                            "Without research, the company would be guessing — "
                            "and in business, guessing is expensive.\n\n"
                            "One of the most common tools in market research is the survey. "
                            "A survey is a structured set of questions designed to collect data "
                            "from a group of people. Surveys can be conducted online, by phone, "
                            "in person, or through mobile apps. "
                            "A well-designed survey asks clear, unbiased questions "
                            "and gives respondents enough options to express their true opinions. "
                            "A poorly designed survey leads to unreliable data.\n\n"
                            "But a survey is only as good as the people who answer it. "
                            "This is where the concept of a sample becomes critical. "
                            "A sample is a smaller group selected from the larger population "
                            "that the researcher wants to study. "
                            "If a company wants to understand the preferences of all Vietnamese women "
                            "aged eighteen to thirty-five, it cannot interview every single one. "
                            "Instead, it selects a representative sample — perhaps one thousand women "
                            "from different cities, income levels, and educational backgrounds. "
                            "The quality of the sample determines whether the findings "
                            "can be generalized to the entire population.\n\n"
                            "To build a good sample, researchers rely on demographic data. "
                            "A demographic is a statistical characteristic of a population — "
                            "age, gender, income, education, occupation, marital status, and location. "
                            "Demographic information helps researchers ensure that their sample "
                            "mirrors the real population. If sixty percent of a city's consumers "
                            "are under thirty, then roughly sixty percent of the sample "
                            "should also be under thirty.\n\n"
                            "Once the data is collected, the next step is segmentation. "
                            "To segment a market means to divide it into distinct groups "
                            "based on shared characteristics or behaviors. "
                            "A smartphone company might segment its market by income level: "
                            "budget buyers, mid-range buyers, and premium buyers. "
                            "Each segment has different needs, different price expectations, "
                            "and different reasons for choosing a product.\n\n"
                            "After identifying segments, the company must decide which one to target. "
                            "Targeting means selecting the specific segment or segments "
                            "that the company will focus its marketing efforts on. "
                            "A small Vietnamese tea brand might target health-conscious professionals "
                            "in Ho Chi Minh City rather than trying to sell to everyone in the country. "
                            "By choosing a clear target, the company can craft messages, "
                            "design products, and set prices that resonate with that specific group."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thu thập dữ liệu khách hàng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every successful product begins not in a factory or a design studio, "
                            "but in the mind of the customer. The challenge for any business "
                            "is to understand what customers think, want, and need — "
                            "and that is exactly what market research does.\n\n"
                            "Market research is the systematic process of gathering, recording, "
                            "and analyzing information about customers, competitors, and the market itself. "
                            "A Vietnamese coffee chain planning to open stores in a new city, "
                            "for example, would conduct research to understand local drinking habits, "
                            "price sensitivity, and the competitive landscape. "
                            "Without research, the company would be guessing — "
                            "and in business, guessing is expensive.\n\n"
                            "One of the most common tools in market research is the survey. "
                            "A survey is a structured set of questions designed to collect data "
                            "from a group of people. Surveys can be conducted online, by phone, "
                            "in person, or through mobile apps. "
                            "A well-designed survey asks clear, unbiased questions "
                            "and gives respondents enough options to express their true opinions. "
                            "A poorly designed survey leads to unreliable data.\n\n"
                            "But a survey is only as good as the people who answer it. "
                            "This is where the concept of a sample becomes critical. "
                            "A sample is a smaller group selected from the larger population "
                            "that the researcher wants to study. "
                            "If a company wants to understand the preferences of all Vietnamese women "
                            "aged eighteen to thirty-five, it cannot interview every single one. "
                            "Instead, it selects a representative sample — perhaps one thousand women "
                            "from different cities, income levels, and educational backgrounds. "
                            "The quality of the sample determines whether the findings "
                            "can be generalized to the entire population.\n\n"
                            "To build a good sample, researchers rely on demographic data. "
                            "A demographic is a statistical characteristic of a population — "
                            "age, gender, income, education, occupation, marital status, and location. "
                            "Demographic information helps researchers ensure that their sample "
                            "mirrors the real population. If sixty percent of a city's consumers "
                            "are under thirty, then roughly sixty percent of the sample "
                            "should also be under thirty.\n\n"
                            "Once the data is collected, the next step is segmentation. "
                            "To segment a market means to divide it into distinct groups "
                            "based on shared characteristics or behaviors. "
                            "A smartphone company might segment its market by income level: "
                            "budget buyers, mid-range buyers, and premium buyers. "
                            "Each segment has different needs, different price expectations, "
                            "and different reasons for choosing a product.\n\n"
                            "After identifying segments, the company must decide which one to target. "
                            "Targeting means selecting the specific segment or segments "
                            "that the company will focus its marketing efforts on. "
                            "A small Vietnamese tea brand might target health-conscious professionals "
                            "in Ho Chi Minh City rather than trying to sell to everyone in the country. "
                            "By choosing a clear target, the company can craft messages, "
                            "design products, and set prices that resonate with that specific group."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng nghiên cứu thị trường",
                    "description": "Viết câu sử dụng 6 từ vựng về thu thập dữ liệu khách hàng.",
                    "data": {
                        "vocabList": ["research", "survey", "sample", "demographic", "segment", "target"],
                        "items": [
                            {
                                "targetVocab": "research",
                                "prompt": "Dùng từ 'research' để viết một câu về vai trò của nghiên cứu thị trường trước khi ra mắt sản phẩm mới. Ví dụ: The cosmetics company spent six months conducting market research in three Vietnamese cities before deciding on the packaging design and price point for its new sunscreen line."
                            },
                            {
                                "targetVocab": "survey",
                                "prompt": "Dùng từ 'survey' để viết một câu về cách thiết kế khảo sát để thu thập ý kiến khách hàng. Ví dụ: The online survey received over five thousand responses in just two weeks, giving the marketing team a clear picture of customer satisfaction levels across all age groups."
                            },
                            {
                                "targetVocab": "sample",
                                "prompt": "Dùng từ 'sample' để viết một câu về tầm quan trọng của việc chọn mẫu đại diện trong nghiên cứu. Ví dụ: The research firm selected a sample of eight hundred households across rural and urban areas to ensure the findings accurately represented the entire Vietnamese consumer market."
                            },
                            {
                                "targetVocab": "demographic",
                                "prompt": "Dùng từ 'demographic' để viết một câu về cách dữ liệu nhân khẩu học giúp doanh nghiệp hiểu khách hàng. Ví dụ: The demographic analysis revealed that the brand's core customers were university-educated women aged twenty-five to forty living in cities with populations over one million."
                            },
                            {
                                "targetVocab": "segment",
                                "prompt": "Dùng từ 'segment' để viết một câu về cách phân khúc thị trường theo hành vi hoặc đặc điểm khách hàng. Ví dụ: The company identified a fast-growing segment of environmentally conscious consumers who were willing to pay up to thirty percent more for products with sustainable packaging."
                            },
                            {
                                "targetVocab": "target",
                                "prompt": "Dùng từ 'target' để viết một câu về việc chọn nhóm khách hàng mục tiêu cho chiến dịch marketing. Ví dụ: After reviewing the research data, the team decided to target young professionals in Ho Chi Minh City who commute by motorbike and buy coffee at least three times a week."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về phương pháp nghiên cứu thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "research — nghiên cứu, survey — khảo sát, sample — mẫu, "
                            "demographic — nhân khẩu học, segment — phân khúc, và target — mục tiêu. "
                            "Bạn đã hiểu cách doanh nghiệp thu thập dữ liệu và phân loại khách hàng. "
                            "Bây giờ, chúng ta sẽ đi sâu vào phương pháp nghiên cứu — "
                            "cách các nhà nghiên cứu thực sự tiến hành thu thập và đánh giá dữ liệu.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: qualitative, quantitative, focus, panel, respondent, và bias. "
                            "Đây là bộ từ vựng giúp bạn hiểu sự khác biệt giữa các phương pháp nghiên cứu.\n\n"
                            "Từ đầu tiên là qualitative — tính từ — nghĩa là định tính, "
                            "liên quan đến nghiên cứu tập trung vào chất lượng, ý nghĩa và trải nghiệm "
                            "thay vì con số. "
                            "Ví dụ: 'The qualitative study involved in-depth interviews with thirty mothers to understand their emotional connection to the baby food brand.' "
                            "Trong bài đọc, qualitative research giúp trả lời câu hỏi 'tại sao' và 'như thế nào' — "
                            "những điều mà con số không thể giải thích.\n\n"
                            "Từ thứ hai là quantitative — tính từ — nghĩa là định lượng, "
                            "liên quan đến nghiên cứu dựa trên số liệu, thống kê và đo lường. "
                            "Ví dụ: 'The quantitative survey of five thousand consumers showed that sixty-two percent preferred the new packaging design over the old one.' "
                            "Trong bài đọc, quantitative research trả lời câu hỏi 'bao nhiêu' và 'mức độ nào' — "
                            "nó cho bạn con số cụ thể để ra quyết định.\n\n"
                            "Từ thứ ba là focus — danh từ/động từ — trong ngữ cảnh marketing thường dùng trong cụm focus group, "
                            "nghĩa là nhóm thảo luận tập trung — một nhóm nhỏ người được mời thảo luận về sản phẩm hoặc ý tưởng. "
                            "Ví dụ: 'The company organized three focus groups in Hanoi to test consumer reactions to the new advertisement before launching it nationally.' "
                            "Trong bài đọc, focus group là công cụ qualitative phổ biến nhất — "
                            "nơi nhà nghiên cứu quan sát cách người tiêu dùng phản ứng trong thời gian thực.\n\n"
                            "Từ thứ tư là panel — danh từ — nghĩa là hội đồng hoặc nhóm cố định, "
                            "một nhóm người được chọn sẵn để tham gia nhiều đợt nghiên cứu theo thời gian. "
                            "Ví dụ: 'The research agency maintained a consumer panel of two thousand households that reported their grocery purchases every month for three years.' "
                            "Trong bài đọc, panel cho phép theo dõi sự thay đổi hành vi tiêu dùng theo thời gian — "
                            "không chỉ chụp một bức ảnh mà quay cả bộ phim.\n\n"
                            "Từ thứ năm là respondent — danh từ — nghĩa là người trả lời, "
                            "người tham gia trả lời câu hỏi trong một cuộc khảo sát hoặc nghiên cứu. "
                            "Ví dụ: 'Only forty percent of respondents completed the entire survey, which raised concerns about whether the remaining data was representative.' "
                            "Trong bài đọc, respondent là nguồn dữ liệu sống — "
                            "chất lượng nghiên cứu phụ thuộc vào việc respondent có trả lời trung thực hay không.\n\n"
                            "Từ cuối cùng là bias — danh từ — nghĩa là thiên lệch hoặc sai lệch, "
                            "bất kỳ yếu tố nào khiến kết quả nghiên cứu không phản ánh đúng thực tế. "
                            "Ví dụ: 'The survey suffered from selection bias because it was only distributed through social media, excluding older consumers who rarely use the internet.' "
                            "Trong bài đọc, bias là kẻ thù lớn nhất của nghiên cứu — "
                            "nó có thể ẩn trong cách đặt câu hỏi, cách chọn mẫu, hoặc cách phân tích dữ liệu.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về phương pháp nghiên cứu định tính và định lượng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phương pháp nghiên cứu thị trường",
                    "description": "Học 6 từ: qualitative, quantitative, focus, panel, respondent, bias",
                    "data": {"vocabList": ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phương pháp nghiên cứu thị trường",
                    "description": "Học 6 từ: qualitative, quantitative, focus, panel, respondent, bias",
                    "data": {"vocabList": ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phương pháp nghiên cứu thị trường",
                    "description": "Học 6 từ: qualitative, quantitative, focus, panel, respondent, bias",
                    "data": {"vocabList": ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phương pháp nghiên cứu thị trường",
                    "description": "Học 6 từ: qualitative, quantitative, focus, panel, respondent, bias",
                    "data": {"vocabList": ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phương pháp nghiên cứu thị trường",
                    "description": "Học 6 từ: qualitative, quantitative, focus, panel, respondent, bias",
                    "data": {"vocabList": ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phương pháp nghiên cứu định tính và định lượng",
                    "description": "There are two fundamental approaches to market research, and every marketing professional must understand both.",
                    "data": {
                        "text": (
                            "There are two fundamental approaches to market research, "
                            "and every marketing professional must understand both. "
                            "They are qualitative research and quantitative research. "
                            "Each answers different questions, uses different tools, "
                            "and produces different kinds of knowledge.\n\n"
                            "Quantitative research deals with numbers. "
                            "It measures how many, how much, and how often. "
                            "A quantitative survey might ask one thousand consumers "
                            "to rate a product on a scale from one to ten, "
                            "or to choose between three packaging designs. "
                            "The results can be expressed as percentages, averages, and statistical patterns. "
                            "Quantitative data is powerful because it is objective and scalable — "
                            "you can survey ten thousand people and summarize the results in a single chart.\n\n"
                            "Qualitative research, on the other hand, explores depth rather than breadth. "
                            "It seeks to understand why people behave the way they do, "
                            "what emotions drive their choices, and how they experience a product or brand. "
                            "Qualitative methods include in-depth interviews, observation, "
                            "and the most popular tool of all — the focus group.\n\n"
                            "A focus group typically consists of six to ten people "
                            "who are brought together to discuss a specific topic "
                            "under the guidance of a trained moderator. "
                            "The moderator asks open-ended questions and encourages participants "
                            "to share their honest opinions. "
                            "A Vietnamese snack company, for example, might run a focus group "
                            "with university students to understand how they feel about a new flavor. "
                            "The moderator watches not just what participants say, "
                            "but how they say it — their facial expressions, their hesitations, "
                            "their enthusiasm or indifference.\n\n"
                            "For longer-term studies, companies often use a panel. "
                            "A consumer panel is a group of people who agree to participate "
                            "in research over an extended period — weeks, months, or even years. "
                            "Panel members might record their daily purchases, "
                            "complete monthly surveys, or test new products before they launch. "
                            "Because the same people are tracked over time, "
                            "a panel can reveal how consumer behavior changes — "
                            "something that a one-time survey cannot capture.\n\n"
                            "In any research study, the people who provide data are called respondents. "
                            "A respondent is anyone who answers questions in a survey, interview, "
                            "or focus group. The quality of research depends heavily "
                            "on whether respondents are honest and engaged. "
                            "If respondents rush through a survey without reading the questions, "
                            "or if they give answers they think the researcher wants to hear, "
                            "the data becomes unreliable.\n\n"
                            "This brings us to one of the most important concepts in research: bias. "
                            "Bias is any systematic error that distorts the results of a study. "
                            "It can appear at every stage of the research process. "
                            "Selection bias occurs when the sample does not represent the population — "
                            "for example, surveying only people in shopping malls "
                            "excludes those who shop online. "
                            "Question bias occurs when the wording of a question "
                            "pushes respondents toward a particular answer. "
                            "Confirmation bias occurs when researchers interpret data "
                            "in a way that supports their existing beliefs. "
                            "Recognizing and minimizing bias is what separates "
                            "reliable research from misleading research."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phương pháp nghiên cứu định tính và định lượng",
                    "description": "There are two fundamental approaches to market research, and every marketing professional must understand both.",
                    "data": {
                        "text": (
                            "There are two fundamental approaches to market research, "
                            "and every marketing professional must understand both. "
                            "They are qualitative research and quantitative research. "
                            "Each answers different questions, uses different tools, "
                            "and produces different kinds of knowledge.\n\n"
                            "Quantitative research deals with numbers. "
                            "It measures how many, how much, and how often. "
                            "A quantitative survey might ask one thousand consumers "
                            "to rate a product on a scale from one to ten, "
                            "or to choose between three packaging designs. "
                            "The results can be expressed as percentages, averages, and statistical patterns. "
                            "Quantitative data is powerful because it is objective and scalable — "
                            "you can survey ten thousand people and summarize the results in a single chart.\n\n"
                            "Qualitative research, on the other hand, explores depth rather than breadth. "
                            "It seeks to understand why people behave the way they do, "
                            "what emotions drive their choices, and how they experience a product or brand. "
                            "Qualitative methods include in-depth interviews, observation, "
                            "and the most popular tool of all — the focus group.\n\n"
                            "A focus group typically consists of six to ten people "
                            "who are brought together to discuss a specific topic "
                            "under the guidance of a trained moderator. "
                            "The moderator asks open-ended questions and encourages participants "
                            "to share their honest opinions. "
                            "A Vietnamese snack company, for example, might run a focus group "
                            "with university students to understand how they feel about a new flavor. "
                            "The moderator watches not just what participants say, "
                            "but how they say it — their facial expressions, their hesitations, "
                            "their enthusiasm or indifference.\n\n"
                            "For longer-term studies, companies often use a panel. "
                            "A consumer panel is a group of people who agree to participate "
                            "in research over an extended period — weeks, months, or even years. "
                            "Panel members might record their daily purchases, "
                            "complete monthly surveys, or test new products before they launch. "
                            "Because the same people are tracked over time, "
                            "a panel can reveal how consumer behavior changes — "
                            "something that a one-time survey cannot capture.\n\n"
                            "In any research study, the people who provide data are called respondents. "
                            "A respondent is anyone who answers questions in a survey, interview, "
                            "or focus group. The quality of research depends heavily "
                            "on whether respondents are honest and engaged. "
                            "If respondents rush through a survey without reading the questions, "
                            "or if they give answers they think the researcher wants to hear, "
                            "the data becomes unreliable.\n\n"
                            "This brings us to one of the most important concepts in research: bias. "
                            "Bias is any systematic error that distorts the results of a study. "
                            "It can appear at every stage of the research process. "
                            "Selection bias occurs when the sample does not represent the population — "
                            "for example, surveying only people in shopping malls "
                            "excludes those who shop online. "
                            "Question bias occurs when the wording of a question "
                            "pushes respondents toward a particular answer. "
                            "Confirmation bias occurs when researchers interpret data "
                            "in a way that supports their existing beliefs. "
                            "Recognizing and minimizing bias is what separates "
                            "reliable research from misleading research."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phương pháp nghiên cứu định tính và định lượng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "There are two fundamental approaches to market research, "
                            "and every marketing professional must understand both. "
                            "They are qualitative research and quantitative research. "
                            "Each answers different questions, uses different tools, "
                            "and produces different kinds of knowledge.\n\n"
                            "Quantitative research deals with numbers. "
                            "It measures how many, how much, and how often. "
                            "A quantitative survey might ask one thousand consumers "
                            "to rate a product on a scale from one to ten, "
                            "or to choose between three packaging designs. "
                            "The results can be expressed as percentages, averages, and statistical patterns. "
                            "Quantitative data is powerful because it is objective and scalable — "
                            "you can survey ten thousand people and summarize the results in a single chart.\n\n"
                            "Qualitative research, on the other hand, explores depth rather than breadth. "
                            "It seeks to understand why people behave the way they do, "
                            "what emotions drive their choices, and how they experience a product or brand. "
                            "Qualitative methods include in-depth interviews, observation, "
                            "and the most popular tool of all — the focus group.\n\n"
                            "A focus group typically consists of six to ten people "
                            "who are brought together to discuss a specific topic "
                            "under the guidance of a trained moderator. "
                            "The moderator asks open-ended questions and encourages participants "
                            "to share their honest opinions. "
                            "A Vietnamese snack company, for example, might run a focus group "
                            "with university students to understand how they feel about a new flavor. "
                            "The moderator watches not just what participants say, "
                            "but how they say it — their facial expressions, their hesitations, "
                            "their enthusiasm or indifference.\n\n"
                            "For longer-term studies, companies often use a panel. "
                            "A consumer panel is a group of people who agree to participate "
                            "in research over an extended period — weeks, months, or even years. "
                            "Panel members might record their daily purchases, "
                            "complete monthly surveys, or test new products before they launch. "
                            "Because the same people are tracked over time, "
                            "a panel can reveal how consumer behavior changes — "
                            "something that a one-time survey cannot capture.\n\n"
                            "In any research study, the people who provide data are called respondents. "
                            "A respondent is anyone who answers questions in a survey, interview, "
                            "or focus group. The quality of research depends heavily "
                            "on whether respondents are honest and engaged. "
                            "If respondents rush through a survey without reading the questions, "
                            "or if they give answers they think the researcher wants to hear, "
                            "the data becomes unreliable.\n\n"
                            "This brings us to one of the most important concepts in research: bias. "
                            "Bias is any systematic error that distorts the results of a study. "
                            "It can appear at every stage of the research process. "
                            "Selection bias occurs when the sample does not represent the population — "
                            "for example, surveying only people in shopping malls "
                            "excludes those who shop online. "
                            "Question bias occurs when the wording of a question "
                            "pushes respondents toward a particular answer. "
                            "Confirmation bias occurs when researchers interpret data "
                            "in a way that supports their existing beliefs. "
                            "Recognizing and minimizing bias is what separates "
                            "reliable research from misleading research."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phương pháp nghiên cứu thị trường",
                    "description": "Viết câu sử dụng 6 từ vựng về phương pháp nghiên cứu.",
                    "data": {
                        "vocabList": ["qualitative", "quantitative", "focus", "panel", "respondent", "bias"],
                        "items": [
                            {
                                "targetVocab": "qualitative",
                                "prompt": "Dùng từ 'qualitative' để viết một câu về nghiên cứu định tính và cách nó giúp hiểu cảm xúc khách hàng. Ví dụ: The qualitative interviews revealed that customers chose the brand not because of price but because of an emotional attachment to its Vietnamese heritage story."
                            },
                            {
                                "targetVocab": "quantitative",
                                "prompt": "Dùng từ 'quantitative' để viết một câu về nghiên cứu định lượng và dữ liệu số. Ví dụ: The quantitative analysis of ten thousand survey responses confirmed that product quality ranked as the number one purchase driver across all age groups."
                            },
                            {
                                "targetVocab": "focus",
                                "prompt": "Dùng từ 'focus' để viết một câu về nhóm thảo luận tập trung trong nghiên cứu thị trường. Ví dụ: The focus group of eight university students in Da Nang provided unexpected feedback — they wanted smaller portion sizes at lower prices rather than the premium large packs the company had planned."
                            },
                            {
                                "targetVocab": "panel",
                                "prompt": "Dùng từ 'panel' để viết một câu về nhóm người tiêu dùng cố định tham gia nghiên cứu dài hạn. Ví dụ: The consumer panel tracked the grocery spending of fifteen hundred households over two years, revealing a steady shift from traditional markets to online delivery platforms."
                            },
                            {
                                "targetVocab": "respondent",
                                "prompt": "Dùng từ 'respondent' để viết một câu về người tham gia trả lời khảo sát và chất lượng dữ liệu. Ví dụ: Nearly thirty percent of respondents abandoned the survey halfway through, forcing the research team to extend the data collection period by two additional weeks."
                            },
                            {
                                "targetVocab": "bias",
                                "prompt": "Dùng từ 'bias' để viết một câu về sai lệch trong nghiên cứu và cách nó ảnh hưởng đến kết quả. Ví dụ: The marketing director discovered a significant bias in the customer satisfaction survey because it was only sent to customers who had made repeat purchases, excluding dissatisfied one-time buyers."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về phân tích dữ liệu và dự báo xu hướng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: research, survey, sample, demographic, segment, target — "
                            "những khái niệm cốt lõi về thu thập dữ liệu và phân loại khách hàng. "
                            "Trong phần 2, bạn đã học thêm qualitative, quantitative, focus, panel, respondent, bias — "
                            "bộ từ vựng về phương pháp nghiên cứu và các nguồn sai lệch.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào giai đoạn quan trọng nhất: "
                            "phân tích dữ liệu và dự báo xu hướng. "
                            "Bạn sẽ học 6 từ mới: insight, trend, forecast, correlation, hypothesis, và methodology.\n\n"
                            "Từ đầu tiên là insight — danh từ — nghĩa là hiểu biết sâu sắc, "
                            "một phát hiện có giá trị rút ra từ việc phân tích dữ liệu nghiên cứu. "
                            "Ví dụ: 'The key insight from the research was that Vietnamese consumers trusted recommendations from friends and family far more than celebrity endorsements.' "
                            "Trong bài đọc, insight là mục tiêu cuối cùng của mọi nghiên cứu — "
                            "không phải dữ liệu thô, mà là ý nghĩa ẩn sau dữ liệu.\n\n"
                            "Từ thứ hai là trend — danh từ — nghĩa là xu hướng, "
                            "hướng đi chung hoặc sự thay đổi dần dần trong hành vi, thị hiếu hoặc thị trường. "
                            "Ví dụ: 'The data revealed a clear trend: spending on health and wellness products among young Vietnamese consumers had doubled in just three years.' "
                            "Trong bài đọc, trend giúp doanh nghiệp nhìn xa hơn hiện tại — "
                            "nếu bạn thấy xu hướng sớm, bạn có lợi thế cạnh tranh.\n\n"
                            "Từ thứ ba là forecast — danh từ/động từ — nghĩa là dự báo, "
                            "ước tính về những gì sẽ xảy ra trong tương lai dựa trên dữ liệu hiện tại. "
                            "Ví dụ: 'The market forecast predicted that online grocery sales in Vietnam would grow by twenty-five percent annually over the next five years.' "
                            "Trong bài đọc, forecast biến dữ liệu quá khứ thành kế hoạch tương lai — "
                            "nó giúp doanh nghiệp chuẩn bị thay vì phản ứng.\n\n"
                            "Từ thứ tư là correlation — danh từ — nghĩa là tương quan, "
                            "mối quan hệ thống kê giữa hai biến số — khi một biến thay đổi, biến kia cũng thay đổi. "
                            "Ví dụ: 'The research found a strong correlation between social media usage and brand awareness among consumers aged eighteen to twenty-four.' "
                            "Trong bài đọc, correlation giúp phát hiện mối liên hệ — "
                            "nhưng nhớ rằng tương quan không có nghĩa là nhân quả.\n\n"
                            "Từ thứ năm là hypothesis — danh từ — nghĩa là giả thuyết, "
                            "một phát biểu có thể kiểm chứng mà nhà nghiên cứu đặt ra trước khi thu thập dữ liệu. "
                            "Ví dụ: 'The team's hypothesis was that lowering the price by ten percent would increase sales volume by at least twenty percent, but the data showed only a five percent increase.' "
                            "Trong bài đọc, hypothesis là điểm khởi đầu của mọi nghiên cứu khoa học — "
                            "bạn đặt giả thuyết, rồi dùng dữ liệu để xác nhận hoặc bác bỏ nó.\n\n"
                            "Từ cuối cùng là methodology — danh từ — nghĩa là phương pháp luận, "
                            "hệ thống các phương pháp và nguyên tắc được sử dụng trong một nghiên cứu. "
                            "Ví dụ: 'The research methodology combined an online quantitative survey of three thousand respondents with qualitative focus groups in five cities across Vietnam.' "
                            "Trong bài đọc, methodology là bản thiết kế của nghiên cứu — "
                            "nó quyết định liệu kết quả có đáng tin cậy hay không.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về phân tích dữ liệu và dự báo xu hướng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phân tích dữ liệu và dự báo",
                    "description": "Học 6 từ: insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phân tích dữ liệu và dự báo",
                    "description": "Học 6 từ: insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phân tích dữ liệu và dự báo",
                    "description": "Học 6 từ: insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phân tích dữ liệu và dự báo",
                    "description": "Học 6 từ: insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phân tích dữ liệu và dự báo",
                    "description": "Học 6 từ: insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phân tích dữ liệu và dự báo xu hướng tiêu dùng",
                    "description": "Collecting data is only half the job — the real value of market research lies in what you do with the data after it is gathered.",
                    "data": {
                        "text": (
                            "Collecting data is only half the job — "
                            "the real value of market research lies in what you do with the data "
                            "after it is gathered. The goal is not to produce charts and tables, "
                            "but to extract insights that drive better business decisions.\n\n"
                            "An insight is a deep understanding that emerges from analyzing data. "
                            "It goes beyond surface-level observations. "
                            "Saying that sixty percent of customers prefer product A over product B "
                            "is a finding. Discovering that they prefer it because the packaging "
                            "reminds them of a trusted local brand from their childhood — that is an insight. "
                            "Good insights are specific, actionable, and often surprising. "
                            "They tell the company something it did not already know "
                            "and suggest a clear course of action.\n\n"
                            "To find insights, researchers look for trends in the data. "
                            "A trend is a general direction of change over time. "
                            "If sales of plant-based milk in Vietnam have increased "
                            "by fifteen percent every year for the past four years, "
                            "that is a trend. Trends help companies understand "
                            "where the market is heading, not just where it is today. "
                            "A company that spots a trend early can develop products "
                            "and marketing strategies before competitors react.\n\n"
                            "Trends also form the basis of forecasting. "
                            "A forecast is a prediction about future market conditions "
                            "based on current and historical data. "
                            "If the trend in online shopping continues at its current rate, "
                            "a forecast might predict that fifty percent of all retail sales "
                            "in major Vietnamese cities will happen online within five years. "
                            "Forecasts are never perfectly accurate, "
                            "but they give companies a framework for planning budgets, "
                            "setting targets, and allocating resources.\n\n"
                            "When analyzing data, researchers often look for correlations. "
                            "A correlation is a statistical relationship between two variables. "
                            "For example, research might show a correlation "
                            "between the amount a company spends on social media advertising "
                            "and the number of new customers it acquires each month. "
                            "When one variable increases and the other also increases, "
                            "that is a positive correlation. "
                            "However, correlation does not prove causation. "
                            "Just because two things move together does not mean one causes the other. "
                            "A researcher must investigate further to determine "
                            "whether the relationship is truly cause and effect.\n\n"
                            "Before collecting any data, good researchers start with a hypothesis. "
                            "A hypothesis is a testable statement about what the researcher expects to find. "
                            "For example: 'Customers who receive a personalized email offer "
                            "are twice as likely to make a purchase within seven days "
                            "compared to customers who receive a generic promotion.' "
                            "The research is then designed to test this hypothesis. "
                            "If the data supports it, the hypothesis is confirmed. "
                            "If not, the researcher must revise the hypothesis "
                            "and consider alternative explanations.\n\n"
                            "All of these elements — insights, trends, forecasts, "
                            "correlations, and hypotheses — depend on the research methodology. "
                            "Methodology refers to the overall design and approach of a study. "
                            "It includes decisions about what type of research to conduct, "
                            "how to select the sample, what questions to ask, "
                            "how to collect and analyze the data, and how to report the findings. "
                            "A strong methodology produces results that are reliable and repeatable. "
                            "A weak methodology — one with a biased sample, "
                            "poorly worded questions, or inappropriate analysis techniques — "
                            "produces results that no one should trust."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phân tích dữ liệu và dự báo xu hướng tiêu dùng",
                    "description": "Collecting data is only half the job — the real value of market research lies in what you do with the data after it is gathered.",
                    "data": {
                        "text": (
                            "Collecting data is only half the job — "
                            "the real value of market research lies in what you do with the data "
                            "after it is gathered. The goal is not to produce charts and tables, "
                            "but to extract insights that drive better business decisions.\n\n"
                            "An insight is a deep understanding that emerges from analyzing data. "
                            "It goes beyond surface-level observations. "
                            "Saying that sixty percent of customers prefer product A over product B "
                            "is a finding. Discovering that they prefer it because the packaging "
                            "reminds them of a trusted local brand from their childhood — that is an insight. "
                            "Good insights are specific, actionable, and often surprising. "
                            "They tell the company something it did not already know "
                            "and suggest a clear course of action.\n\n"
                            "To find insights, researchers look for trends in the data. "
                            "A trend is a general direction of change over time. "
                            "If sales of plant-based milk in Vietnam have increased "
                            "by fifteen percent every year for the past four years, "
                            "that is a trend. Trends help companies understand "
                            "where the market is heading, not just where it is today. "
                            "A company that spots a trend early can develop products "
                            "and marketing strategies before competitors react.\n\n"
                            "Trends also form the basis of forecasting. "
                            "A forecast is a prediction about future market conditions "
                            "based on current and historical data. "
                            "If the trend in online shopping continues at its current rate, "
                            "a forecast might predict that fifty percent of all retail sales "
                            "in major Vietnamese cities will happen online within five years. "
                            "Forecasts are never perfectly accurate, "
                            "but they give companies a framework for planning budgets, "
                            "setting targets, and allocating resources.\n\n"
                            "When analyzing data, researchers often look for correlations. "
                            "A correlation is a statistical relationship between two variables. "
                            "For example, research might show a correlation "
                            "between the amount a company spends on social media advertising "
                            "and the number of new customers it acquires each month. "
                            "When one variable increases and the other also increases, "
                            "that is a positive correlation. "
                            "However, correlation does not prove causation. "
                            "Just because two things move together does not mean one causes the other. "
                            "A researcher must investigate further to determine "
                            "whether the relationship is truly cause and effect.\n\n"
                            "Before collecting any data, good researchers start with a hypothesis. "
                            "A hypothesis is a testable statement about what the researcher expects to find. "
                            "For example: 'Customers who receive a personalized email offer "
                            "are twice as likely to make a purchase within seven days "
                            "compared to customers who receive a generic promotion.' "
                            "The research is then designed to test this hypothesis. "
                            "If the data supports it, the hypothesis is confirmed. "
                            "If not, the researcher must revise the hypothesis "
                            "and consider alternative explanations.\n\n"
                            "All of these elements — insights, trends, forecasts, "
                            "correlations, and hypotheses — depend on the research methodology. "
                            "Methodology refers to the overall design and approach of a study. "
                            "It includes decisions about what type of research to conduct, "
                            "how to select the sample, what questions to ask, "
                            "how to collect and analyze the data, and how to report the findings. "
                            "A strong methodology produces results that are reliable and repeatable. "
                            "A weak methodology — one with a biased sample, "
                            "poorly worded questions, or inappropriate analysis techniques — "
                            "produces results that no one should trust."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phân tích dữ liệu và dự báo xu hướng tiêu dùng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Collecting data is only half the job — "
                            "the real value of market research lies in what you do with the data "
                            "after it is gathered. The goal is not to produce charts and tables, "
                            "but to extract insights that drive better business decisions.\n\n"
                            "An insight is a deep understanding that emerges from analyzing data. "
                            "It goes beyond surface-level observations. "
                            "Saying that sixty percent of customers prefer product A over product B "
                            "is a finding. Discovering that they prefer it because the packaging "
                            "reminds them of a trusted local brand from their childhood — that is an insight. "
                            "Good insights are specific, actionable, and often surprising. "
                            "They tell the company something it did not already know "
                            "and suggest a clear course of action.\n\n"
                            "To find insights, researchers look for trends in the data. "
                            "A trend is a general direction of change over time. "
                            "If sales of plant-based milk in Vietnam have increased "
                            "by fifteen percent every year for the past four years, "
                            "that is a trend. Trends help companies understand "
                            "where the market is heading, not just where it is today. "
                            "A company that spots a trend early can develop products "
                            "and marketing strategies before competitors react.\n\n"
                            "Trends also form the basis of forecasting. "
                            "A forecast is a prediction about future market conditions "
                            "based on current and historical data. "
                            "If the trend in online shopping continues at its current rate, "
                            "a forecast might predict that fifty percent of all retail sales "
                            "in major Vietnamese cities will happen online within five years. "
                            "Forecasts are never perfectly accurate, "
                            "but they give companies a framework for planning budgets, "
                            "setting targets, and allocating resources.\n\n"
                            "When analyzing data, researchers often look for correlations. "
                            "A correlation is a statistical relationship between two variables. "
                            "For example, research might show a correlation "
                            "between the amount a company spends on social media advertising "
                            "and the number of new customers it acquires each month. "
                            "When one variable increases and the other also increases, "
                            "that is a positive correlation. "
                            "However, correlation does not prove causation. "
                            "Just because two things move together does not mean one causes the other. "
                            "A researcher must investigate further to determine "
                            "whether the relationship is truly cause and effect.\n\n"
                            "Before collecting any data, good researchers start with a hypothesis. "
                            "A hypothesis is a testable statement about what the researcher expects to find. "
                            "For example: 'Customers who receive a personalized email offer "
                            "are twice as likely to make a purchase within seven days "
                            "compared to customers who receive a generic promotion.' "
                            "The research is then designed to test this hypothesis. "
                            "If the data supports it, the hypothesis is confirmed. "
                            "If not, the researcher must revise the hypothesis "
                            "and consider alternative explanations.\n\n"
                            "All of these elements — insights, trends, forecasts, "
                            "correlations, and hypotheses — depend on the research methodology. "
                            "Methodology refers to the overall design and approach of a study. "
                            "It includes decisions about what type of research to conduct, "
                            "how to select the sample, what questions to ask, "
                            "how to collect and analyze the data, and how to report the findings. "
                            "A strong methodology produces results that are reliable and repeatable. "
                            "A weak methodology — one with a biased sample, "
                            "poorly worded questions, or inappropriate analysis techniques — "
                            "produces results that no one should trust."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phân tích dữ liệu và dự báo",
                    "description": "Viết câu sử dụng 6 từ vựng về phân tích dữ liệu và dự báo xu hướng.",
                    "data": {
                        "vocabList": ["insight", "trend", "forecast", "correlation", "hypothesis", "methodology"],
                        "items": [
                            {
                                "targetVocab": "insight",
                                "prompt": "Dùng từ 'insight' để viết một câu về phát hiện quan trọng từ nghiên cứu thị trường. Ví dụ: The most valuable insight from the consumer study was that price was not the main barrier to purchase — customers simply did not understand how to use the product."
                            },
                            {
                                "targetVocab": "trend",
                                "prompt": "Dùng từ 'trend' để viết một câu về xu hướng tiêu dùng đang thay đổi tại Việt Nam. Ví dụ: The research identified a growing trend of Vietnamese millennials choosing experiences over material goods, spending more on travel and dining than on clothing and electronics."
                            },
                            {
                                "targetVocab": "forecast",
                                "prompt": "Dùng từ 'forecast' để viết một câu về dự báo thị trường dựa trên dữ liệu nghiên cứu. Ví dụ: Based on current growth rates, the market forecast predicted that the Vietnamese organic food market would reach ten trillion dong in annual revenue by the end of the decade."
                            },
                            {
                                "targetVocab": "correlation",
                                "prompt": "Dùng từ 'correlation' để viết một câu về mối tương quan giữa hai yếu tố trong nghiên cứu marketing. Ví dụ: The data showed a strong positive correlation between the number of product reviews on the website and the conversion rate, suggesting that social proof significantly influenced buying decisions."
                            },
                            {
                                "targetVocab": "hypothesis",
                                "prompt": "Dùng từ 'hypothesis' để viết một câu về giả thuyết nghiên cứu và cách kiểm chứng nó. Ví dụ: The marketing team's hypothesis that free shipping would increase average order value was disproven by the data — customers ordered more frequently but spent less per transaction."
                            },
                            {
                                "targetVocab": "methodology",
                                "prompt": "Dùng từ 'methodology' để viết một câu về phương pháp luận nghiên cứu và độ tin cậy của kết quả. Ví dụ: The competitor's research methodology was criticized because it relied entirely on self-reported data from a small, non-representative sample of loyal customers."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Nghiên cứu thị trường. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "research — nghiên cứu, survey — khảo sát, sample — mẫu, "
                            "demographic — nhân khẩu học, segment — phân khúc, và target — mục tiêu. "
                            "Đây là bộ từ vựng cốt lõi về thu thập dữ liệu và phân loại khách hàng.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào phương pháp nghiên cứu: "
                            "qualitative — định tính, quantitative — định lượng, focus — tập trung, "
                            "panel — nhóm cố định, respondent — người trả lời, và bias — thiên lệch. "
                            "Những từ này giúp bạn hiểu cách thu thập dữ liệu đáng tin cậy.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "insight — hiểu biết sâu sắc, trend — xu hướng, forecast — dự báo, "
                            "correlation — tương quan, hypothesis — giả thuyết, và methodology — phương pháp luận. "
                            "Đây là những từ về phân tích dữ liệu và biến thông tin thành hành động.\n\n"
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
                    "description": "Học 18 từ: research, survey, sample, demographic, segment, target, qualitative, quantitative, focus, panel, respondent, bias, insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: research, survey, sample, demographic, segment, target, qualitative, quantitative, focus, panel, respondent, bias, insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: research, survey, sample, demographic, segment, target, qualitative, quantitative, focus, panel, respondent, bias, insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: research, survey, sample, demographic, segment, target, qualitative, quantitative, focus, panel, respondent, bias, insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: research, survey, sample, demographic, segment, target, qualitative, quantitative, focus, panel, respondent, bias, insight, trend, forecast, correlation, hypothesis, methodology",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng nghiên cứu thị trường",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "research",
                                "prompt": "Dùng từ 'research' để viết một câu về cách nghiên cứu thị trường giúp doanh nghiệp giảm rủi ro khi ra mắt sản phẩm. Ví dụ: The company's decision to invest in thorough market research before the product launch saved it from a costly mistake — the original concept had no appeal to its core customer base."
                            },
                            {
                                "targetVocab": "survey",
                                "prompt": "Dùng từ 'survey' để viết một câu về thiết kế khảo sát hiệu quả. Ví dụ: The redesigned survey used simple language and took only five minutes to complete, which tripled the response rate compared to the previous version that had been too long and confusing."
                            },
                            {
                                "targetVocab": "sample",
                                "prompt": "Dùng từ 'sample' để viết một câu về cách chọn mẫu ảnh hưởng đến kết quả nghiên cứu. Ví dụ: The research team expanded its sample to include consumers from rural provinces after realizing that the initial urban-only sample had missed a significant portion of the target market."
                            },
                            {
                                "targetVocab": "demographic",
                                "prompt": "Dùng từ 'demographic' để viết một câu về cách phân tích nhân khẩu học giúp cá nhân hóa chiến lược marketing. Ví dụ: The demographic breakdown of the survey data revealed that the product was unexpectedly popular among men over fifty, a group the company had never considered targeting."
                            },
                            {
                                "targetVocab": "segment",
                                "prompt": "Dùng từ 'segment' để viết một câu về phân khúc thị trường và chiến lược tiếp cận khác nhau. Ví dụ: The premium segment accounted for only fifteen percent of total customers but generated forty percent of the company's revenue, making it the most profitable group to serve."
                            },
                            {
                                "targetVocab": "target",
                                "prompt": "Dùng từ 'target' để viết một câu về việc thay đổi nhóm khách hàng mục tiêu dựa trên dữ liệu mới. Ví dụ: After the research revealed that its original target audience had low purchase intent, the brand shifted its focus to a younger, more digitally active consumer group."
                            },
                            {
                                "targetVocab": "qualitative",
                                "prompt": "Dùng từ 'qualitative' để viết một câu về giá trị của nghiên cứu định tính trong việc hiểu động cơ khách hàng. Ví dụ: The qualitative phase of the study uncovered a powerful emotional driver — customers associated the brand with memories of family meals during Tet holiday celebrations."
                            },
                            {
                                "targetVocab": "quantitative",
                                "prompt": "Dùng từ 'quantitative' để viết một câu về cách dữ liệu định lượng hỗ trợ ra quyết định. Ví dụ: The quantitative results were clear — seventy-eight percent of respondents said they would switch brands if a competitor offered the same quality at a ten percent lower price."
                            },
                            {
                                "targetVocab": "focus",
                                "prompt": "Dùng từ 'focus' để viết một câu về phát hiện bất ngờ từ nhóm thảo luận tập trung. Ví dụ: During the focus group session, participants revealed that they found the product's instructions confusing, a problem that had never appeared in the quantitative survey data."
                            },
                            {
                                "targetVocab": "panel",
                                "prompt": "Dùng từ 'panel' để viết một câu về lợi ích của nghiên cứu panel dài hạn. Ví dụ: The three-year consumer panel study showed that brand loyalty among Vietnamese coffee drinkers was declining steadily as new international chains entered the market."
                            },
                            {
                                "targetVocab": "respondent",
                                "prompt": "Dùng từ 'respondent' để viết một câu về chất lượng phản hồi và độ tin cậy dữ liệu. Ví dụ: The research team removed two hundred respondents from the dataset after detecting patterns suggesting they had answered randomly without reading the questions."
                            },
                            {
                                "targetVocab": "bias",
                                "prompt": "Dùng từ 'bias' để viết một câu về cách phát hiện và giảm thiểu sai lệch trong nghiên cứu. Ví dụ: To reduce confirmation bias, the company hired an independent research firm to analyze the data instead of relying on its own marketing team, which had a vested interest in positive results."
                            },
                            {
                                "targetVocab": "insight",
                                "prompt": "Dùng từ 'insight' để viết một câu về cách insight từ nghiên cứu dẫn đến thay đổi chiến lược. Ví dụ: The consumer insight that convenience mattered more than price led the company to invest heavily in a same-day delivery service, which became its strongest competitive advantage."
                            },
                            {
                                "targetVocab": "trend",
                                "prompt": "Dùng từ 'trend' để viết một câu về cách phát hiện xu hướng sớm tạo lợi thế cạnh tranh. Ví dụ: The company was among the first to identify the trend toward sugar-free beverages in Vietnam, launching its zero-sugar line two years before major competitors entered the category."
                            },
                            {
                                "targetVocab": "forecast",
                                "prompt": "Dùng từ 'forecast' để viết một câu về dự báo thị trường và lập kế hoạch kinh doanh. Ví dụ: The five-year market forecast projected that demand for electric scooters in Vietnamese cities would triple, prompting the company to begin building a nationwide charging network."
                            },
                            {
                                "targetVocab": "correlation",
                                "prompt": "Dùng từ 'correlation' để viết một câu về mối tương quan trong dữ liệu marketing và cách diễn giải nó. Ví dụ: Although the data showed a correlation between television advertising and sales growth, further analysis revealed that seasonal demand — not the ads — was the true driver of the increase."
                            },
                            {
                                "targetVocab": "hypothesis",
                                "prompt": "Dùng từ 'hypothesis' để viết một câu về quá trình đặt và kiểm chứng giả thuyết trong marketing. Ví dụ: The team tested the hypothesis that a loyalty program would reduce customer churn by twenty percent, but after six months the data showed only a marginal improvement of three percent."
                            },
                            {
                                "targetVocab": "methodology",
                                "prompt": "Dùng từ 'methodology' để viết một câu về cách phương pháp luận ảnh hưởng đến chất lượng nghiên cứu. Ví dụ: The research agency's methodology was praised for combining large-scale quantitative surveys with in-depth qualitative interviews, giving the client both statistical confidence and rich consumer stories."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về nghiên cứu thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về nghiên cứu thị trường — từ thiết kế nghiên cứu, "
                            "thu thập dữ liệu, đến phân tích và dự báo xu hướng.\n\n"
                            "Bạn sẽ gặp lại research, survey, sample, demographic, segment, target "
                            "trong phần mở đầu về cách một công ty Việt Nam bắt đầu dự án nghiên cứu. "
                            "Tiếp theo, qualitative, quantitative, focus, panel, respondent, bias "
                            "sẽ xuất hiện khi bài viết mô tả các phương pháp thu thập dữ liệu. "
                            "Và cuối cùng, insight, trend, forecast, correlation, hypothesis, methodology "
                            "sẽ đưa bạn vào giai đoạn phân tích và ra quyết định.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nghiên cứu thị trường — Từ dữ liệu đến quyết định",
                    "description": "A Vietnamese beverage company is preparing to launch a new line of ready-to-drink iced tea targeting young consumers in major cities.",
                    "data": {
                        "text": (
                            "A Vietnamese beverage company is preparing to launch a new line "
                            "of ready-to-drink iced tea targeting young consumers in major cities. "
                            "The product development team has created three flavor options, "
                            "but before investing billions of dong in production and marketing, "
                            "the company needs answers. Which flavor will sell best? "
                            "What price are consumers willing to pay? "
                            "Where should the company distribute first? "
                            "To answer these questions, the company turns to market research.\n\n"
                            "The research team begins by defining the methodology. "
                            "They decide on a mixed-method approach — "
                            "combining quantitative surveys for statistical data "
                            "with qualitative focus groups for deeper understanding. "
                            "This methodology will give them both the numbers they need "
                            "to make confident decisions and the stories behind those numbers.\n\n"
                            "The first step is the quantitative phase. "
                            "The team designs an online survey with thirty questions "
                            "covering taste preferences, price sensitivity, brand awareness, "
                            "and purchasing habits. To ensure reliable results, "
                            "they need a representative sample. "
                            "They select three thousand respondents across Ho Chi Minh City, "
                            "Hanoi, and Da Nang, carefully matching the demographic profile "
                            "of each city — age, gender, income level, and education. "
                            "The sample must mirror the actual population of young urban consumers "
                            "so that the findings can be generalized.\n\n"
                            "As the survey responses come in, the team watches for potential bias. "
                            "They notice that eighty percent of respondents are women, "
                            "even though the target market is roughly equal between men and women. "
                            "This gender bias could skew the results. "
                            "To correct it, they extend the survey period "
                            "and adjust their recruitment strategy to reach more male respondents. "
                            "They also review the survey questions for wording bias — "
                            "making sure no question subtly pushes respondents toward a particular answer.\n\n"
                            "While the quantitative survey runs, the team launches the qualitative phase. "
                            "They organize four focus groups — two in Ho Chi Minh City and two in Hanoi. "
                            "Each focus group consists of eight young consumers "
                            "who are asked to taste all three flavors, discuss their reactions, "
                            "and explain what they look for when choosing a bottled tea. "
                            "The moderator probes deeper: Why do you prefer this flavor? "
                            "What does this packaging make you feel? "
                            "Would you buy this if you saw it in a convenience store?\n\n"
                            "The company also maintains a consumer panel — "
                            "a group of five hundred regular tea drinkers "
                            "who have agreed to report their beverage purchases monthly. "
                            "The panel data reveals how often these consumers buy iced tea, "
                            "which brands they currently prefer, and how their habits change with the seasons. "
                            "Unlike a one-time survey, the panel tracks behavior over time, "
                            "providing a moving picture rather than a single snapshot.\n\n"
                            "After six weeks, the data collection is complete. "
                            "Now comes the most important part: analysis. "
                            "The team starts by testing their hypothesis. "
                            "Before the research began, they predicted that the lemon-honey flavor "
                            "would be the most popular among consumers aged eighteen to twenty-five. "
                            "The quantitative data confirms this hypothesis — "
                            "sixty-one percent of respondents in that age group chose lemon-honey "
                            "as their top preference.\n\n"
                            "But the qualitative data adds nuance. "
                            "In the focus groups, several respondents mentioned "
                            "that they liked the lemon-honey flavor but found the sweetness level too high. "
                            "This insight — that the flavor concept is right but the execution needs adjustment — "
                            "would never have appeared in the quantitative survey alone. "
                            "It is exactly the kind of deep understanding "
                            "that makes qualitative research invaluable.\n\n"
                            "The team also discovers an interesting correlation in the data. "
                            "Respondents who exercise regularly are significantly more likely "
                            "to prefer the unsweetened green tea option. "
                            "This correlation suggests a potential segment — "
                            "health-conscious fitness enthusiasts — "
                            "that the company had not originally considered as a primary target.\n\n"
                            "Looking at the panel data and broader market statistics, "
                            "the team identifies a clear trend: "
                            "demand for low-sugar and sugar-free beverages in Vietnam "
                            "has been growing by eighteen percent annually for three consecutive years. "
                            "Based on this trend, the team builds a forecast "
                            "predicting that the low-sugar segment will account for thirty percent "
                            "of the total iced tea market within four years.\n\n"
                            "Armed with these findings, the research team presents its recommendations. "
                            "Launch the lemon-honey flavor first, but reduce the sugar content by fifteen percent. "
                            "Target young urban professionals aged twenty to thirty "
                            "in Ho Chi Minh City and Hanoi as the primary segment. "
                            "Develop the unsweetened green tea as a secondary product "
                            "for the health-conscious demographic. "
                            "And invest in building brand awareness through social media, "
                            "where the correlation between digital engagement and purchase intent is strongest.\n\n"
                            "This is the power of market research. "
                            "It transforms guesswork into evidence, opinions into insights, "
                            "and hunches into forecasts. "
                            "Every decision — from the flavor on the shelf to the ad on the screen — "
                            "is stronger when it is built on a foundation of rigorous, "
                            "well-designed research."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nghiên cứu thị trường — Từ dữ liệu đến quyết định",
                    "description": "A Vietnamese beverage company is preparing to launch a new line of ready-to-drink iced tea targeting young consumers in major cities.",
                    "data": {
                        "text": (
                            "A Vietnamese beverage company is preparing to launch a new line "
                            "of ready-to-drink iced tea targeting young consumers in major cities. "
                            "The product development team has created three flavor options, "
                            "but before investing billions of dong in production and marketing, "
                            "the company needs answers. Which flavor will sell best? "
                            "What price are consumers willing to pay? "
                            "Where should the company distribute first? "
                            "To answer these questions, the company turns to market research.\n\n"
                            "The research team begins by defining the methodology. "
                            "They decide on a mixed-method approach — "
                            "combining quantitative surveys for statistical data "
                            "with qualitative focus groups for deeper understanding. "
                            "This methodology will give them both the numbers they need "
                            "to make confident decisions and the stories behind those numbers.\n\n"
                            "The first step is the quantitative phase. "
                            "The team designs an online survey with thirty questions "
                            "covering taste preferences, price sensitivity, brand awareness, "
                            "and purchasing habits. To ensure reliable results, "
                            "they need a representative sample. "
                            "They select three thousand respondents across Ho Chi Minh City, "
                            "Hanoi, and Da Nang, carefully matching the demographic profile "
                            "of each city — age, gender, income level, and education. "
                            "The sample must mirror the actual population of young urban consumers "
                            "so that the findings can be generalized.\n\n"
                            "As the survey responses come in, the team watches for potential bias. "
                            "They notice that eighty percent of respondents are women, "
                            "even though the target market is roughly equal between men and women. "
                            "This gender bias could skew the results. "
                            "To correct it, they extend the survey period "
                            "and adjust their recruitment strategy to reach more male respondents. "
                            "They also review the survey questions for wording bias — "
                            "making sure no question subtly pushes respondents toward a particular answer.\n\n"
                            "While the quantitative survey runs, the team launches the qualitative phase. "
                            "They organize four focus groups — two in Ho Chi Minh City and two in Hanoi. "
                            "Each focus group consists of eight young consumers "
                            "who are asked to taste all three flavors, discuss their reactions, "
                            "and explain what they look for when choosing a bottled tea. "
                            "The moderator probes deeper: Why do you prefer this flavor? "
                            "What does this packaging make you feel? "
                            "Would you buy this if you saw it in a convenience store?\n\n"
                            "The company also maintains a consumer panel — "
                            "a group of five hundred regular tea drinkers "
                            "who have agreed to report their beverage purchases monthly. "
                            "The panel data reveals how often these consumers buy iced tea, "
                            "which brands they currently prefer, and how their habits change with the seasons. "
                            "Unlike a one-time survey, the panel tracks behavior over time, "
                            "providing a moving picture rather than a single snapshot.\n\n"
                            "After six weeks, the data collection is complete. "
                            "Now comes the most important part: analysis. "
                            "The team starts by testing their hypothesis. "
                            "Before the research began, they predicted that the lemon-honey flavor "
                            "would be the most popular among consumers aged eighteen to twenty-five. "
                            "The quantitative data confirms this hypothesis — "
                            "sixty-one percent of respondents in that age group chose lemon-honey "
                            "as their top preference.\n\n"
                            "But the qualitative data adds nuance. "
                            "In the focus groups, several respondents mentioned "
                            "that they liked the lemon-honey flavor but found the sweetness level too high. "
                            "This insight — that the flavor concept is right but the execution needs adjustment — "
                            "would never have appeared in the quantitative survey alone. "
                            "It is exactly the kind of deep understanding "
                            "that makes qualitative research invaluable.\n\n"
                            "The team also discovers an interesting correlation in the data. "
                            "Respondents who exercise regularly are significantly more likely "
                            "to prefer the unsweetened green tea option. "
                            "This correlation suggests a potential segment — "
                            "health-conscious fitness enthusiasts — "
                            "that the company had not originally considered as a primary target.\n\n"
                            "Looking at the panel data and broader market statistics, "
                            "the team identifies a clear trend: "
                            "demand for low-sugar and sugar-free beverages in Vietnam "
                            "has been growing by eighteen percent annually for three consecutive years. "
                            "Based on this trend, the team builds a forecast "
                            "predicting that the low-sugar segment will account for thirty percent "
                            "of the total iced tea market within four years.\n\n"
                            "Armed with these findings, the research team presents its recommendations. "
                            "Launch the lemon-honey flavor first, but reduce the sugar content by fifteen percent. "
                            "Target young urban professionals aged twenty to thirty "
                            "in Ho Chi Minh City and Hanoi as the primary segment. "
                            "Develop the unsweetened green tea as a secondary product "
                            "for the health-conscious demographic. "
                            "And invest in building brand awareness through social media, "
                            "where the correlation between digital engagement and purchase intent is strongest.\n\n"
                            "This is the power of market research. "
                            "It transforms guesswork into evidence, opinions into insights, "
                            "and hunches into forecasts. "
                            "Every decision — from the flavor on the shelf to the ad on the screen — "
                            "is stronger when it is built on a foundation of rigorous, "
                            "well-designed research."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nghiên cứu thị trường — Từ dữ liệu đến quyết định",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "A Vietnamese beverage company is preparing to launch a new line "
                            "of ready-to-drink iced tea targeting young consumers in major cities. "
                            "The product development team has created three flavor options, "
                            "but before investing billions of dong in production and marketing, "
                            "the company needs answers. Which flavor will sell best? "
                            "What price are consumers willing to pay? "
                            "Where should the company distribute first? "
                            "To answer these questions, the company turns to market research.\n\n"
                            "The research team begins by defining the methodology. "
                            "They decide on a mixed-method approach — "
                            "combining quantitative surveys for statistical data "
                            "with qualitative focus groups for deeper understanding. "
                            "This methodology will give them both the numbers they need "
                            "to make confident decisions and the stories behind those numbers.\n\n"
                            "The first step is the quantitative phase. "
                            "The team designs an online survey with thirty questions "
                            "covering taste preferences, price sensitivity, brand awareness, "
                            "and purchasing habits. To ensure reliable results, "
                            "they need a representative sample. "
                            "They select three thousand respondents across Ho Chi Minh City, "
                            "Hanoi, and Da Nang, carefully matching the demographic profile "
                            "of each city — age, gender, income level, and education. "
                            "The sample must mirror the actual population of young urban consumers "
                            "so that the findings can be generalized.\n\n"
                            "As the survey responses come in, the team watches for potential bias. "
                            "They notice that eighty percent of respondents are women, "
                            "even though the target market is roughly equal between men and women. "
                            "This gender bias could skew the results. "
                            "To correct it, they extend the survey period "
                            "and adjust their recruitment strategy to reach more male respondents. "
                            "They also review the survey questions for wording bias — "
                            "making sure no question subtly pushes respondents toward a particular answer.\n\n"
                            "While the quantitative survey runs, the team launches the qualitative phase. "
                            "They organize four focus groups — two in Ho Chi Minh City and two in Hanoi. "
                            "Each focus group consists of eight young consumers "
                            "who are asked to taste all three flavors, discuss their reactions, "
                            "and explain what they look for when choosing a bottled tea. "
                            "The moderator probes deeper: Why do you prefer this flavor? "
                            "What does this packaging make you feel? "
                            "Would you buy this if you saw it in a convenience store?\n\n"
                            "The company also maintains a consumer panel — "
                            "a group of five hundred regular tea drinkers "
                            "who have agreed to report their beverage purchases monthly. "
                            "The panel data reveals how often these consumers buy iced tea, "
                            "which brands they currently prefer, and how their habits change with the seasons. "
                            "Unlike a one-time survey, the panel tracks behavior over time, "
                            "providing a moving picture rather than a single snapshot.\n\n"
                            "After six weeks, the data collection is complete. "
                            "Now comes the most important part: analysis. "
                            "The team starts by testing their hypothesis. "
                            "Before the research began, they predicted that the lemon-honey flavor "
                            "would be the most popular among consumers aged eighteen to twenty-five. "
                            "The quantitative data confirms this hypothesis — "
                            "sixty-one percent of respondents in that age group chose lemon-honey "
                            "as their top preference.\n\n"
                            "But the qualitative data adds nuance. "
                            "In the focus groups, several respondents mentioned "
                            "that they liked the lemon-honey flavor but found the sweetness level too high. "
                            "This insight — that the flavor concept is right but the execution needs adjustment — "
                            "would never have appeared in the quantitative survey alone. "
                            "It is exactly the kind of deep understanding "
                            "that makes qualitative research invaluable.\n\n"
                            "The team also discovers an interesting correlation in the data. "
                            "Respondents who exercise regularly are significantly more likely "
                            "to prefer the unsweetened green tea option. "
                            "This correlation suggests a potential segment — "
                            "health-conscious fitness enthusiasts — "
                            "that the company had not originally considered as a primary target.\n\n"
                            "Looking at the panel data and broader market statistics, "
                            "the team identifies a clear trend: "
                            "demand for low-sugar and sugar-free beverages in Vietnam "
                            "has been growing by eighteen percent annually for three consecutive years. "
                            "Based on this trend, the team builds a forecast "
                            "predicting that the low-sugar segment will account for thirty percent "
                            "of the total iced tea market within four years.\n\n"
                            "Armed with these findings, the research team presents its recommendations. "
                            "Launch the lemon-honey flavor first, but reduce the sugar content by fifteen percent. "
                            "Target young urban professionals aged twenty to thirty "
                            "in Ho Chi Minh City and Hanoi as the primary segment. "
                            "Develop the unsweetened green tea as a secondary product "
                            "for the health-conscious demographic. "
                            "And invest in building brand awareness through social media, "
                            "where the correlation between digital engagement and purchase intent is strongest.\n\n"
                            "This is the power of market research. "
                            "It transforms guesswork into evidence, opinions into insights, "
                            "and hunches into forecasts. "
                            "Every decision — from the flavor on the shelf to the ad on the screen — "
                            "is stronger when it is built on a foundation of rigorous, "
                            "well-designed research."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích dự án nghiên cứu thị trường",
                    "description": "Viết đoạn văn tiếng Anh phân tích nghiên cứu thị trường sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của nghiên cứu thị trường. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy mô tả cách bạn sẽ thiết kế một dự án nghiên cứu thị trường cho một sản phẩm mới tại Việt Nam. Giải thích methodology bạn chọn, cách xây dựng sample đại diện, phương pháp thu thập dữ liệu (survey, focus group, panel), và cách bạn sẽ giảm thiểu bias trong quá trình nghiên cứu.",
                            "Hãy phân tích cách một doanh nghiệp có thể sử dụng kết quả nghiên cứu thị trường để ra quyết định. Giải thích vai trò của insight, trend và forecast trong việc xác định target segment, và tầm quan trọng của việc kiểm chứng hypothesis bằng cả dữ liệu qualitative và quantitative."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần hành động thực tế.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Nghiên cứu thị trường — "
                            "và bây giờ là lúc biến kiến thức thành hành động.\n\n"
                            "Research — nghiên cứu. Đây là nền tảng của mọi quyết định marketing thông minh. "
                            "Lần tới khi ai đó trong nhóm nói 'Mình nghĩ khách hàng muốn thế này,' "
                            "bạn hãy hỏi lại: 'Dữ liệu research nói gì?' "
                            "Ví dụ mới: The startup's decision to pivot its business model "
                            "was entirely driven by market research showing that its original target audience "
                            "had no interest in the product category.\n\n"
                            "Bias — thiên lệch. Đây là từ mà bạn nên giữ trong đầu "
                            "mỗi khi đọc bất kỳ báo cáo nghiên cứu nào. "
                            "Hãy luôn hỏi: Ai trả lời khảo sát này? Câu hỏi có dẫn dắt không? "
                            "Mẫu có đại diện không? Phát hiện bias là kỹ năng quan trọng nhất "
                            "của một nhà phân tích thị trường. "
                            "Ví dụ mới: The CEO dismissed the positive survey results "
                            "after learning that the sample had a significant age bias — "
                            "ninety percent of respondents were under twenty-five, "
                            "while the actual customer base was much older.\n\n"
                            "Insight — hiểu biết sâu sắc. Dữ liệu thô là nguyên liệu, "
                            "nhưng insight là món ăn thành phẩm. "
                            "Bất kỳ ai cũng có thể đọc biểu đồ, "
                            "nhưng người giỏi là người nhìn ra ý nghĩa ẩn sau con số. "
                            "Ví dụ mới: The most powerful insight from the six-month study "
                            "was that customers did not leave because of price — "
                            "they left because the brand had stopped communicating with them.\n\n"
                            "Methodology — phương pháp luận. Khi bạn đọc một báo cáo nghiên cứu, "
                            "hãy đọc phần methodology trước. Nếu phương pháp yếu, "
                            "kết quả không đáng tin — dù con số có đẹp đến đâu. "
                            "Ví dụ mới: The investor asked to review the research methodology "
                            "before accepting the market size estimates, "
                            "knowing that flawed methods could produce dangerously optimistic forecasts.\n\n"
                            "Forecast — dự báo. Trong kinh doanh, "
                            "người nhìn xa hơn hiện tại là người có lợi thế. "
                            "Forecast không phải tiên tri — nó là ước tính có cơ sở dữ liệu. "
                            "Và bạn bây giờ đã có từ vựng để đọc, hiểu và thảo luận về forecast "
                            "bằng tiếng Anh chuyên nghiệp. "
                            "Ví dụ mới: The company's five-year forecast for the Vietnamese market "
                            "projected annual growth of twelve percent, "
                            "based on demographic trends and rising disposable income among urban millennials.\n\n"
                            "Correlation — tương quan. Nhớ rằng correlation không phải causation. "
                            "Hai thứ có thể di chuyển cùng nhau mà không có quan hệ nhân quả. "
                            "Kỹ năng phân biệt tương quan và nhân quả "
                            "sẽ giúp bạn tránh những kết luận sai lầm tốn kém. "
                            "Ví dụ mới: The marketing manager initially believed "
                            "that the correlation between social media followers and sales "
                            "meant more followers caused more sales, "
                            "but deeper analysis showed that a third factor — seasonal promotions — "
                            "was driving both metrics simultaneously.\n\n"
                            "Đây là bước đầu tiên trong hành trình Marketing và Quản trị. "
                            "Bạn đã có 18 từ vựng — bây giờ hãy dùng chúng. "
                            "Tuần này, hãy thử đọc một bài báo tiếng Anh về nghiên cứu thị trường "
                            "trên Harvard Business Review, McKinsey, hoặc Nielsen. "
                            "Bạn sẽ ngạc nhiên khi thấy mình hiểu được bao nhiêu. "
                            "Hẹn gặp lại ở bài học tiếp theo — Chiến lược thương hiệu!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Market Research – Nghiên Cứu Thị Trường' AND uid = '{UID}' ORDER BY created_at;")
