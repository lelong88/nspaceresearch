"""
Create vi-en Grit podcast curriculum.
Angela Duckworth's "Grit: The Power of Passion and Perseverance" TED Talk.
Language: vi-en (Vietnamese speakers learning English vocabulary)
Description tone: vivid_scenario
Farewell tone: team-building energy
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
BASE_URL = "https://helloapi.step.is"

# --- Vocabulary (same 18 words as en-en version — Property 10: vocab parity) ---
# Group 1 (Session 1): perseverance, stamina, tenacity, resilience, diligence, fortitude
# Group 2 (Session 2): passion, aptitude, deliberate, consistency, endurance, determination
# Group 3 (Session 3): grit, predictor, achievement, talent, potential, mindset

VOCAB_GROUP_1 = ["perseverance", "stamina", "tenacity", "resilience", "diligence", "fortitude"]
VOCAB_GROUP_2 = ["passion", "aptitude", "deliberate", "consistency", "endurance", "determination"]
VOCAB_GROUP_3 = ["grit", "predictor", "achievement", "talent", "potential", "mindset"]
ALL_VOCAB = VOCAB_GROUP_1 + VOCAB_GROUP_2 + VOCAB_GROUP_3

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId", "curriculumTags",
    "taskId", "imageId", "practiceMinutes", "practiceTime",
    "difficultyTags", "skillFocusTags"
}


def strip_keys(obj):
    if isinstance(obj, dict):
        return {k: strip_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
    elif isinstance(obj, list):
        return [strip_keys(item) for item in obj]
    return obj


def build_content():
    # ---- Session 1: Group 1 vocabulary ----
    s1_intro_topic = {
        "type": "introAudio",
        "title": "Giới thiệu về Grit",
        "description": "Tổng quan về nghiên cứu của Angela Duckworth và lý do đam mê kết hợp kiên trì quan trọng hơn tài năng.",
        "data": {
            "text": "Chào mừng bạn đến với khóa học Grit: Sức Mạnh Của Đam Mê Và Kiên Trì. Trong khóa học này, bạn sẽ khám phá một trong những ý tưởng quan trọng nhất của tâm lý học hiện đại — khái niệm grit. Angela Duckworth, một nhà tâm lý học và cựu giáo viên, đã dành nhiều năm nghiên cứu điều gì tạo nên sự khác biệt giữa những người thành công xuất sắc và những người còn lại. Kết luận của bà vừa bất ngờ vừa mạnh mẽ: không phải tài năng, không phải chỉ số IQ, không phải trí thông minh xã hội mới dự đoán thành công. Chính là grit — sự kết hợp giữa đam mê và kiên trì hướng tới những mục tiêu dài hạn. Duckworth phát hiện ra mô hình này ở khắp nơi bà nghiên cứu. Tại Học viện Quân sự West Point, những học viên sống sót qua mùa hè huấn luyện khắc nghiệt đầu tiên không phải là những người khỏe nhất hay thông minh nhất. Họ là những người có grit cao nhất. Trong cuộc thi đánh vần quốc gia, những đứa trẻ vào được vòng chung kết không nhất thiết là những em có chỉ số IQ ngôn ngữ cao nhất. Họ là những em luyện tập chăm chỉ nhất và lâu nhất. Trong bài TED Talk của mình, Duckworth chia sẻ hành trình từ tư vấn quản lý đến dạy toán lớp bảy tại các trường công lập New York. Bà nhận ra rằng những học sinh giỏi nhất không phải lúc nào cũng là những em có khả năng tự nhiên nhất. Những học sinh thành công là những em chăm chỉ, cam kết, và không bỏ cuộc khi mọi thứ trở nên khó khăn. Quan sát này đã đưa bà vào sự nghiệp nghiên cứu tâm lý học về thành tựu. Trong năm phần tiếp theo, bạn sẽ học 18 từ vựng tiếng Anh nắm bắt bản chất nghiên cứu của Duckworth. Những từ này sẽ giúp bạn nói về nỗ lực, sự kiên trì, và những phẩm chất thúc đẩy thành công lâu dài. Hôm nay, trong Phần Một, chúng ta sẽ tập trung vào sáu từ mô tả những phẩm chất bên trong của người có grit: perseverance, stamina, tenacity, resilience, diligence, và fortitude. Hãy bắt đầu nào."
        }
    }

    s1_intro_vocab = {
        "type": "introAudio",
        "title": "Từ vựng: Những phẩm chất bên trong của Grit",
        "description": "Học 6 từ mô tả phẩm chất bên trong của người kiên trì: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "data": {
            "text": "Trong phần này, bạn sẽ học sáu từ tiếng Anh mô tả phẩm chất bên trong của người có grit. Đây là những đặc điểm Duckworth tìm thấy ở người thành công — không phải sự thông minh hay may mắn, mà là phẩm chất cá nhân duy trì nỗ lực theo thời gian. Hãy tìm hiểu từng từ. Từ đầu tiên là perseverance. Perseverance là danh từ, nghĩa là sự kiên trì — nỗ lực liên tục bất chấp khó khăn hay thất bại. Khi Duckworth nghiên cứu học viên tại West Point, bà thấy perseverance là yếu tố dự đoán tốt nhất ai sẽ vượt qua mùa hè huấn luyện tàn khốc gọi là Beast Barracks. Những người vượt qua không phải nhanh nhất hay khỏe nhất — họ là người tiếp tục tiến bước khi muốn bỏ cuộc. Perseverance là sự từ chối dừng lại. Từ thứ hai là stamina. Stamina là danh từ, nghĩa là sức bền — sức mạnh thể chất hoặc tinh thần để duy trì nỗ lực kéo dài. Grit không phải cuộc chạy nước rút mà là marathon. Bạn cần stamina để theo đuổi mục tiêu nhiều năm. Những nhà vô địch đánh vần luyện tập hàng tháng, xây dựng stamina chịu đựng hàng nghìn giờ học. Stamina giữ bạn đứng vững khi công việc kéo dài hơn mong đợi. Từ thứ ba là tenacity. Tenacity là danh từ, nghĩa là sự bám trụ — phẩm chất nắm chắc mục đích hay hướng hành động. Tenacity là điều bạn thấy ở học sinh trượt bài kiểm tra, học chăm hơn, trượt lần nữa, và vẫn quay lại. Duckworth mô tả người có grit giữ chặt mục tiêu với tenacity mà người khác thấy gần như phi lý. Từ thứ tư là resilience. Resilience là danh từ, nghĩa là khả năng phục hồi — hồi phục nhanh từ thất bại hay khó khăn. Resilience không phải tránh thất bại mà là bật dậy từ nó. Người có grit coi thất bại là tình trạng tạm thời, không phải bản sắc vĩnh viễn. Người có resilience ngã xuống và đứng dậy, coi kết quả tệ là thông tin về điều cần làm khác. Từ thứ năm là diligence. Diligence là danh từ, nghĩa là sự cần cù — nỗ lực cẩn thận và chăm chỉ. Trong khi perseverance nhấn mạnh không bỏ cuộc, diligence nhấn mạnh chất lượng nỗ lực. Học sinh cần cù không chỉ bỏ nhiều giờ — họ bỏ giờ tập trung, có suy nghĩ. Người có grit kiên trì có chủ đích, tìm phản hồi và cải thiện cách tiếp cận. Diligence là perseverance với sự chính xác. Từ cuối cùng là fortitude. Fortitude là danh từ, nghĩa là sự dũng cảm — lòng can đảm trước đau đớn hay nghịch cảnh. Fortitude là xương sống cảm xúc của grit, cho phép chịu đựng không chỉ khó khăn thể chất mà còn tinh thần — sự cô đơn, thất vọng của tiến bộ chậm, nỗi sợ nỗ lực không được đền đáp. Fortitude phân biệt người mơ lớn với người đạt được điều lớn lao. Hãy ôn lại: perseverance, từ chối dừng lại; stamina, sức mạnh duy trì nỗ lực; tenacity, nắm chắc mục tiêu; resilience, bật dậy từ thất bại; diligence, nỗ lực cẩn thận; fortitude, can đảm trước nghịch cảnh. Bạn sẽ gặp sáu từ này trong bài đọc tiếp theo."
        }
    }

    s1_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Thẻ từ vựng: Phẩm chất bên trong của Grit",
        "description": "Học 6 từ: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Thẻ từ vựng: Luyện phát âm",
        "description": "Học 6 từ: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Thẻ từ vựng: Kiểm tra cấp 1",
        "description": "Học 6 từ: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Thẻ từ vựng: Kiểm tra cấp 2",
        "description": "Học 6 từ: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_reading_text = "Most people assume that the highest achievers in any field are the most naturally gifted. Angela Duckworth spent years proving them wrong. Before she became a psychologist, Duckworth worked as a management consultant at McKinsey. The job paid well and the work was intellectually stimulating, but something felt incomplete. She left to teach seventh-grade math in a low-income neighborhood in New York City, and what she saw in that classroom changed everything.\n\nThe students who earned the highest grades were not always the ones who grasped concepts the fastest. Some of the quickest learners grew bored and disengaged when the material became challenging. Meanwhile, other students — the ones who struggled at first, who asked the same question three times, who stayed after class for extra help — gradually pulled ahead. Their secret was perseverance. They did not interpret confusion as a sign that they were not smart enough. They interpreted it as a normal part of learning and kept pushing forward.\n\nThis pattern followed Duckworth into her research at the University of Pennsylvania. At West Point Military Academy, she studied incoming cadets during Beast Barracks — a brutal six-week initiation designed to break down even the toughest recruits. Every year, a significant percentage of cadets dropped out. The military had tried using SAT scores, physical fitness tests, and leadership evaluations to predict who would survive. None of these measures worked well. What did work was a simple questionnaire measuring stamina and tenacity — the willingness to keep going when the body aches and the mind screams for relief.\n\nDuckworth found the same dynamic in the National Spelling Bee. The finalists were not necessarily the children with the largest natural vocabularies. They were the children who demonstrated extraordinary resilience after misspelling a word on stage. Instead of crumbling under the pressure, they went home, studied with even greater diligence, and returned the following year stronger than before. Their practice was not casual or haphazard. It was focused, repetitive, and often uncomfortable — the kind of work that requires real fortitude to sustain over months and years.\n\nWhat fascinated Duckworth most was the emotional core of these high achievers. Physical toughness alone did not explain their success. Many of them described moments of deep doubt, loneliness, and frustration. The difference was that they possessed a kind of fortitude that allowed them to sit with discomfort rather than flee from it. They could tolerate the slow pace of improvement, the absence of immediate rewards, and the uncertainty of whether their efforts would ever pay off. This emotional fortitude, Duckworth concluded, was the invisible foundation beneath every other quality she had studied."

    s1_reading = {
        "type": "reading",
        "title": "Đọc: Hành trình khám phá Grit",
        "description": "Most people assume that the highest achievers in any field are the most naturally gifted. Angela...",
        "data": {"text": s1_reading_text}
    }

    s1_speak_reading = {
        "type": "speakReading",
        "title": "Đọc: Đọc to bài văn",
        "description": "Most people assume that the highest achievers in any field are the most naturally gifted. Angela...",
        "data": {"text": s1_reading_text}
    }

    s1_read_along = {
        "type": "readAlong",
        "title": "Nghe: Hành trình khám phá Grit",
        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
        "data": {"text": s1_reading_text}
    }

    s1_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Viết: Sử dụng từ 'perseverance'",
        "description": "Viết một câu sử dụng từ perseverance.",
        "data": {
            "prompt": "Hãy sử dụng từ 'perseverance' để viết một câu về việc không bỏ cuộc trước khó khăn. Ví dụ: Her perseverance through years of rejection finally led to a breakthrough that changed her career.",
            "vocabWord": "perseverance"
        }
    }

    s1_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Viết: Sử dụng từ 'resilience'",
        "description": "Viết một câu sử dụng từ resilience.",
        "data": {
            "prompt": "Hãy sử dụng từ 'resilience' để viết một câu về việc phục hồi sau thất bại. Ví dụ: The athlete's resilience after a devastating injury inspired her entire team to train harder than ever before.",
            "vocabWord": "resilience"
        }
    }

    s1_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Viết: Suy ngẫm về sức mạnh nội tại",
        "description": "Viết một đoạn văn về những phẩm chất giúp con người vượt qua thử thách.",
        "data": {
            "prompt": "Hãy nghĩ về một lần bạn hoặc ai đó bạn biết phải đối mặt với thử thách lớn đòi hỏi nỗ lực liên tục trong nhiều tuần hoặc nhiều tháng. Viết một đoạn văn tiếng Anh mô tả trải nghiệm đó, sử dụng ít nhất bốn trong số các từ sau: perseverance, stamina, tenacity, resilience, diligence, fortitude. Giải thích điều gì khiến thử thách đó khó khăn và phẩm chất nào đã giúp người đó vượt qua.",
            "vocabList": VOCAB_GROUP_1
        }
    }

    session_1 = {
        "title": "Phần 1: Những phẩm chất bên trong của Grit",
        "activities": [
            s1_intro_topic, s1_intro_vocab, s1_view_flashcards, s1_speak_flashcards,
            s1_vocab_level1, s1_vocab_level2, s1_reading, s1_speak_reading,
            s1_read_along, s1_writing_sentence_1, s1_writing_sentence_2, s1_writing_paragraph
        ]
    }

    # ---- Session 2: Group 2 vocabulary ----
    s2_intro_topic = {
        "type": "introAudio",
        "title": "Động lực đằng sau Grit",
        "description": "Khám phá cách đam mê, luyện tập có chủ đích và quyết tâm thúc đẩy thành tựu lâu dài.",
        "data": {
            "text": "Chào mừng bạn trở lại. Trong Phần Một, bạn đã học sáu từ mô tả những phẩm chất bên trong của người có grit — perseverance, stamina, tenacity, resilience, diligence, và fortitude. Đây là những đặc điểm giữ cho ai đó tiếp tục khi công việc trở nên khó khăn. Nhưng nghiên cứu của Duckworth tiết lộ điều quan trọng không kém: grit không chỉ là sự cứng rắn. Nó còn là về hướng đi. Những người có grit cao nhất mà bà nghiên cứu không chỉ kiên trì — họ còn đam mê. Họ đã tìm thấy điều gì đó có ý nghĩa sâu sắc với mình, và họ theo đuổi nó với sự nhất quán kéo dài nhiều năm, đôi khi nhiều thập kỷ. Trong phần này, bạn sẽ học sáu từ mới nắm bắt động lực đằng sau grit: passion, aptitude, deliberate, consistency, endurance, và determination. Những từ này mô tả không chỉ nỗ lực, mà còn mục đích và chiến lược đằng sau nó. Hãy bắt đầu nào."
        }
    }

    s2_intro_vocab = {
        "type": "introAudio",
        "title": "Từ vựng: Động lực đằng sau Grit",
        "description": "Học 6 từ về động lực của grit: passion, aptitude, deliberate, consistency, endurance, determination.",
        "data": {
            "text": "Trong Phần Một, bạn đã học về phẩm chất bên trong duy trì người có grit — perseverance, stamina, tenacity, resilience, diligence, và fortitude. Bây giờ, trong Phần Hai, chúng ta chuyển sang lực lượng thúc đẩy grit tiến về phía trước. Sáu từ này mô tả mục đích, chiến lược, và năng lượng bền vững đằng sau thành tựu lâu dài. Từ đầu tiên là passion. Passion là danh từ, nghĩa là đam mê — cảm xúc mãnh liệt hoặc sự nhiệt tình sâu sắc dành cho điều gì đó. Duckworth sử dụng passion theo cách cụ thể — không phải hứng thú thoáng qua mà là cam kết sâu sắc, bền bỉ với một mục tiêu. Người có grit cao nhất tìm thấy passion sớm và gắn bó nhiều năm. Một nhạc sĩ đam mê tổ chức toàn bộ cuộc sống xung quanh việc trở nên giỏi hơn. Passion là la bàn cho grit hướng đi. Từ thứ hai là aptitude. Aptitude là danh từ, nghĩa là năng khiếu — khả năng tự nhiên để học điều gì đó. Nghiên cứu của Duckworth thách thức niềm tin rằng aptitude là yếu tố quan trọng nhất. Người có aptitude cao nhưng grit thấp thường kém hơn người có aptitude trung bình nhưng grit cao. Aptitude mở cánh cửa, nhưng nỗ lực mới đưa bạn bước qua. Từ thứ ba là deliberate. Deliberate là tính từ, nghĩa là có chủ đích — được thực hiện có ý thức với suy nghĩ cẩn thận. Duckworth nhấn mạnh deliberate practice — luyện tập có chủ đích — nỗ lực tập trung nhằm cải thiện điểm yếu cụ thể. Người học deliberate xác định điều chưa hiểu, tìm phản hồi, và luyện phần khó nhất. Nỗ lực deliberate phân biệt luyện tập hiệu quả với lặp lại vô nghĩa. Từ thứ tư là consistency. Consistency là danh từ, nghĩa là sự nhất quán — phẩm chất luôn thực hiện theo cách tương tự. Consistency của nỗ lực theo thời gian là dấu hiệu mạnh nhất của grit. Không phải về một ngày tuyệt vời mà là xuất hiện mỗi ngày, ngay cả khi động lực thấp. Vận động viên nhất quán tập cả ngày muốn nằm trên giường. Consistency là xương sống thầm lặng của mọi thành tựu. Từ thứ năm là endurance. Endurance là danh từ, nghĩa là sức chịu đựng — khả năng chịu khó khăn trong thời gian dài. Trong khi stamina đề cập đến năng lượng, endurance nhấn mạnh khả năng kéo dài qua khó khăn. Người có grit duy trì nỗ lực qua nhiều năm tiến bộ chậm và bất định. Endurance giữ nghiên cứu sinh làm luận văn năm năm, hay doanh nhân xây dựng lại sau thất bại. Từ cuối cùng là determination. Determination là danh từ, nghĩa là sự quyết tâm — sự vững vàng về mục đích. Determination nhấn mạnh quyết định theo đuổi mục tiêu, trong khi perseverance nhấn mạnh hành động tiếp tục. Người có determination đã lựa chọn có ý thức và cam kết theo đuổi. Duckworth mô tả determination là khoảnh khắc grit kết tinh — khi người ta ngừng thử nghiệm và bắt đầu cam kết. Hãy ôn lại: passion, cam kết sâu sắc cho hướng đi; aptitude, khả năng tự nhiên là điểm khởi đầu; deliberate, cách tiếp cận có chủ ý; consistency, xuất hiện ngày qua ngày; endurance, chịu đựng khó khăn kéo dài; determination, vững vàng về mục đích. Bạn sẽ thấy sáu từ này trong bài đọc phía trước."
        }
    }

    s2_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Thẻ từ vựng: Động lực đằng sau Grit",
        "description": "Học 6 từ: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Thẻ từ vựng: Luyện phát âm",
        "description": "Học 6 từ: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Thẻ từ vựng: Kiểm tra cấp 1",
        "description": "Học 6 từ: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Thẻ từ vựng: Kiểm tra cấp 2",
        "description": "Học 6 từ: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_reading_text = "Angela Duckworth likes to tell the story of a swimming coach she once interviewed. The coach had trained dozens of Olympic hopefuls over a thirty-year career. When asked what separated the athletes who made it to the Games from those who did not, his answer was immediate: it was never about aptitude. The most physically gifted swimmers in his program were not always the ones who stood on the podium. The ones who made it were the ones who showed up at five in the morning, every single day, for years. They had passion for the sport that went beyond the thrill of competition. They loved the process — the monotonous laps, the aching muscles, the tiny incremental improvements that nobody else could see.\n\nThis story captures something essential about Duckworth's framework. She argues that effort counts twice in the equation of success. Talent multiplied by effort produces skill. Skill multiplied by effort produces achievement. The math is elegant, but the implications are radical. It means that a swimmer with moderate aptitude but extraordinary consistency will eventually surpass a swimmer with extraordinary aptitude but inconsistent effort. The gap between talent and achievement is filled entirely by effort — and the quality of that effort matters enormously.\n\nDuckworth draws heavily on the work of psychologist Anders Ericsson, who spent decades studying expert performers in fields ranging from chess to surgery. Ericsson found that what distinguished world-class performers from merely good ones was not innate ability but the quantity and quality of their practice. Specifically, the best performers engaged in what Ericsson called deliberate practice — structured, focused work aimed at improving specific weaknesses. A deliberate pianist does not simply play through her favorite pieces for an hour. She identifies the three measures where her timing falters, isolates them, and repeats them fifty times until the problem disappears.\n\nThis kind of practice demands extraordinary endurance. It is inherently uncomfortable because you are spending your time on the things you are worst at, not the things that come easily. Most people avoid this discomfort. They practice what they already know, which feels productive but produces little improvement. Gritty people, Duckworth found, embrace the discomfort. They understand that deliberate practice is the price of genuine improvement, and they are willing to pay it day after day, month after month.\n\nThe fuel for this sustained effort is determination — a firm, conscious decision about what matters and a refusal to be distracted from it. Duckworth distinguishes between people who dabble and people who commit. Dabblers try many things but stick with nothing. Committed people have made a determination about their direction and organize their lives around it. This determination is not rigid or blind. Gritty people adjust their tactics constantly. But they rarely abandon their ultimate goal. The combination of deep passion, deliberate practice, daily consistency, and unwavering determination is what Duckworth calls the engine of long-term achievement."

    s2_reading = {
        "type": "reading",
        "title": "Đọc: Công thức của nỗ lực",
        "description": "Angela Duckworth likes to tell the story of a swimming coach she once interviewed. The coach had...",
        "data": {"text": s2_reading_text}
    }

    s2_speak_reading = {
        "type": "speakReading",
        "title": "Đọc: Đọc to bài văn",
        "description": "Angela Duckworth likes to tell the story of a swimming coach she once interviewed. The coach had...",
        "data": {"text": s2_reading_text}
    }

    s2_read_along = {
        "type": "readAlong",
        "title": "Nghe: Công thức của nỗ lực",
        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
        "data": {"text": s2_reading_text}
    }

    s2_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Viết: Sử dụng từ 'deliberate'",
        "description": "Viết một câu sử dụng từ deliberate.",
        "data": {
            "prompt": "Hãy sử dụng từ 'deliberate' để viết một câu về việc luyện tập hoặc học tập có chủ đích. Ví dụ: His deliberate focus on the weakest parts of his presentation transformed him from a nervous speaker into a confident one.",
            "vocabWord": "deliberate"
        }
    }

    s2_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Viết: Sử dụng từ 'consistency'",
        "description": "Viết một câu sử dụng từ consistency.",
        "data": {
            "prompt": "Hãy sử dụng từ 'consistency' để viết một câu về tầm quan trọng của nỗ lực đều đặn. Ví dụ: The consistency of her daily writing habit — even just five hundred words before breakfast — produced three novels in four years.",
            "vocabWord": "consistency"
        }
    }

    s2_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Viết: Suy ngẫm về nỗ lực và hướng đi",
        "description": "Viết một đoạn văn về cách đam mê và nỗ lực có chủ đích thúc đẩy thành tựu.",
        "data": {
            "prompt": "Duckworth lập luận rằng nỗ lực đếm hai lần: tài năng nhân nỗ lực bằng kỹ năng, và kỹ năng nhân nỗ lực bằng thành tựu. Hãy nghĩ về một kỹ năng bạn đã phát triển theo thời gian — có thể là học thuật, thể thao, nghệ thuật, hoặc nghề nghiệp. Viết một đoạn văn tiếng Anh mô tả cách passion, deliberate practice, consistency, hoặc determination đã đóng vai trò trong sự phát triển của bạn. Sử dụng ít nhất bốn từ vựng của phần này.",
            "vocabList": VOCAB_GROUP_2
        }
    }

    session_2 = {
        "title": "Phần 2: Động lực đằng sau Grit",
        "activities": [
            s2_intro_topic, s2_intro_vocab, s2_view_flashcards, s2_speak_flashcards,
            s2_vocab_level1, s2_vocab_level2, s2_reading, s2_speak_reading,
            s2_read_along, s2_writing_sentence_1, s2_writing_sentence_2, s2_writing_paragraph
        ]
    }

    # ---- Session 3: Group 3 vocabulary ----
    s3_intro_topic = {
        "type": "introAudio",
        "title": "Grit, tài năng và tư duy phát triển",
        "description": "Khám phá mối quan hệ giữa grit, tài năng, thành tựu và tư duy giúp thành công lâu dài.",
        "data": {
            "text": "Chào mừng bạn đến Phần Ba. Qua hai phần trước, bạn đã xây dựng một vốn từ vựng mạnh mẽ để nói về grit. Trong Phần Một, bạn học về những phẩm chất bên trong — perseverance, stamina, tenacity, resilience, diligence, và fortitude. Trong Phần Hai, bạn khám phá những động lực — passion, aptitude, deliberate practice, consistency, endurance, và determination. Bây giờ, trong phần dạy cuối cùng này, chúng ta kết nối tất cả lại. Bạn sẽ học sáu từ nắm bắt bức tranh toàn cảnh nghiên cứu của Duckworth: bản thân grit, khái niệm predictor, bản chất của achievement, vai trò của talent, ý tưởng về potential, và sức mạnh của mindset. Những từ này sẽ giúp bạn thảo luận không chỉ grit là gì, mà tại sao nó quan trọng — và cách nó kết nối với khoa học rộng hơn về hiệu suất con người. Hãy bắt đầu nào."
        }
    }

    s3_intro_vocab = {
        "type": "introAudio",
        "title": "Từ vựng: Bức tranh toàn cảnh của Grit",
        "description": "Học 6 từ về khung lý thuyết rộng hơn của grit: grit, predictor, achievement, talent, potential, mindset.",
        "data": {
            "text": "Bạn đã học mười hai từ qua hai phần. Phần Một: perseverance, stamina, tenacity, resilience, diligence, fortitude. Phần Hai: passion, aptitude, deliberate, consistency, endurance, determination. Bây giờ, Phần Ba, bạn sẽ học sáu từ tạo nên bức tranh toàn cảnh nghiên cứu của Duckworth. Từ đầu tiên là grit. Grit là danh từ, nghĩa là sự kiên cường — sự kết hợp giữa đam mê và kiên trì hướng tới mục tiêu dài hạn. Duckworth định nghĩa grit là xu hướng duy trì sự quan tâm và nỗ lực hướng tới mục tiêu rất dài hạn. Không phải cứng rắn trong một khoảnh khắc mà cứng rắn qua nhiều năm. Grit giữ sinh viên y khoa tiếp tục qua một thập kỷ đào tạo, giữ doanh nhân xây dựng lại sau nhiều lần thất bại. Trong khung lý thuyết của Duckworth, grit là phẩm chất chủ đạo bao trùm tất cả. Từ thứ hai là predictor. Predictor là danh từ, nghĩa là yếu tố dự đoán — yếu tố dùng để dự báo kết quả tương lai. Grit nổi lên như predictor mạnh nhất của thành công trong hầu hết mọi lĩnh vực Duckworth nghiên cứu. Tại West Point, grit là predictor tốt hơn điểm SAT. Trong cuộc thi đánh vần, tốt hơn chỉ số IQ. Phát hiện này gợi ý rằng yếu tố dự đoán quan trọng nhất nằm trong tầm kiểm soát của chúng ta. Từ thứ ba là achievement. Achievement là danh từ, nghĩa là thành tựu — điều đạt được qua nỗ lực hoặc kỹ năng. Duckworth phân biệt talent và achievement. Talent là nơi bắt đầu, achievement là nơi kết thúc. Khoảng cách được lấp đầy bởi nỗ lực. Công thức: talent nhân effort bằng skill, skill nhân effort bằng achievement. Effort đếm hai lần. Từ thứ tư là talent. Talent là danh từ, nghĩa là tài năng — khả năng tự nhiên trong một lĩnh vực. Duckworth thách thức sự tôn sùng talent. Bà không nói talent không quan trọng, nhưng chúng ta đánh giá quá cao talent và quá thấp effort. Khi tôn vinh talent hơn nỗ lực, chúng ta gửi thông điệp rằng nếu điều gì không đến dễ dàng, bạn không phù hợp. Thông điệp này là kẻ thù của grit. Từ thứ năm là potential. Potential là danh từ, nghĩa là tiềm năng — phẩm chất có thể phát triển dẫn đến thành công tương lai. Duckworth tin hầu hết mọi người có nhiều potential hơn họ nhận ra. Rào cản chính không phải thiếu talent mà thiếu nỗ lực bền vững. Potential không cố định — nó mở rộng với mỗi giờ luyện tập có chủ đích, mỗi thất bại được phục hồi. Từ cuối cùng là mindset. Mindset là danh từ, nghĩa là tư duy — cách suy nghĩ về khả năng của chính mình. Duckworth kết nối với nghiên cứu của Carol Dweck về growth mindset. Người tin khả năng phát triển được — growth mindset — đón nhận thử thách, kiên trì qua thất bại, đạt được nhiều hơn người có fixed mindset. Growth mindset là nền tảng tâm lý của grit. Nếu tin potential cố định, không có lý do vượt qua khó khăn. Nếu tin potential mở rộng với nỗ lực, mọi trở ngại thành cơ hội phát triển. Hãy ôn lại: grit, kết hợp passion và perseverance; predictor, yếu tố dự đoán kết quả; achievement, điều đạt được qua nỗ lực; talent, khả năng tự nhiên là điểm khởi đầu; potential, khả năng chờ phát triển; mindset, cách suy nghĩ định hình mọi thứ. Bạn sẽ gặp sáu từ trong bài đọc tiếp theo."
        }
    }

    s3_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Thẻ từ vựng: Bức tranh toàn cảnh của Grit",
        "description": "Học 6 từ: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Thẻ từ vựng: Luyện phát âm",
        "description": "Học 6 từ: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Thẻ từ vựng: Kiểm tra cấp 1",
        "description": "Học 6 từ: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Thẻ từ vựng: Kiểm tra cấp 2",
        "description": "Học 6 từ: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_reading_text = "There is a question that has haunted educators, coaches, and parents for generations: why do some people with extraordinary talent never reach their potential, while others with modest abilities achieve remarkable things? Angela Duckworth believes she has found the answer, and it comes down to a single word: grit.\n\nDuckworth's research began with a puzzle. As a math teacher, she watched students with obvious talent coast through easy assignments and then collapse when the material became difficult. These students had the aptitude to excel, but they lacked something crucial — the willingness to struggle. Meanwhile, students with less natural ability but greater determination steadily improved. They did not see difficulty as a threat. They saw it as the normal cost of learning something worthwhile.\n\nWhen Duckworth moved into academic research, she set out to identify the strongest predictor of success across different domains. She studied military cadets, spelling bee contestants, first-year teachers in tough urban schools, and salespeople at major corporations. In every setting, the pattern was the same. The traditional predictors — IQ, standardized test scores, physical fitness, even measures of talent — were weaker than expected. The strongest predictor, consistently, was grit.\n\nThis finding challenged a deeply held cultural belief. Western societies, in particular, have long celebrated talent as the primary driver of achievement. We build entire industries around identifying talented children early and placing them on accelerated tracks. But Duckworth's data suggests that this approach may be fundamentally misguided. By focusing on talent, we risk overlooking the qualities that actually matter most: the perseverance to keep working when progress is invisible, the resilience to recover from failure, and the mindset that treats ability as something that grows rather than something you are born with.\n\nDuckworth's connection to Carol Dweck's work on mindset is central to her argument. Dweck demonstrated that people who hold a growth mindset — the belief that intelligence and ability can be developed through effort — respond to challenges very differently from people with a fixed mindset. Growth-minded individuals see failure as feedback, not as a verdict on their potential. They are more likely to seek out difficult tasks, persist through frustration, and ultimately achieve at higher levels. Duckworth argues that this growth mindset is the psychological soil in which grit takes root. Without it, perseverance becomes mere stubbornness. With it, perseverance becomes a pathway to genuine achievement.\n\nThe implications of this research are both hopeful and demanding. Hopeful because it means that achievement is not reserved for the genetically fortunate. Anyone who cultivates passion, practices with deliberate intention, maintains consistency over time, and develops the endurance to weather setbacks can close the gap between where they are and where they want to be. Demanding because it means there are no shortcuts. The path to meaningful achievement runs through years of sustained, uncomfortable effort — and the only way to walk that path is with grit."

    s3_reading = {
        "type": "reading",
        "title": "Đọc: Tại sao Grit quan trọng hơn tài năng",
        "description": "There is a question that has haunted educators, coaches, and parents for generations: why do some...",
        "data": {"text": s3_reading_text}
    }

    s3_speak_reading = {
        "type": "speakReading",
        "title": "Đọc: Đọc to bài văn",
        "description": "There is a question that has haunted educators, coaches, and parents for generations: why do some...",
        "data": {"text": s3_reading_text}
    }

    s3_read_along = {
        "type": "readAlong",
        "title": "Nghe: Tại sao Grit quan trọng hơn tài năng",
        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
        "data": {"text": s3_reading_text}
    }

    s3_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Viết: Sử dụng từ 'mindset'",
        "description": "Viết một câu sử dụng từ mindset.",
        "data": {
            "prompt": "Hãy sử dụng từ 'mindset' để viết một câu về cách niềm tin của một người ảnh hưởng đến khả năng học hỏi hoặc phát triển. Ví dụ: Shifting from a fixed mindset to a growth mindset helped him see every mistake as a learning opportunity rather than a personal failure.",
            "vocabWord": "mindset"
        }
    }

    s3_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Viết: Sử dụng từ 'achievement'",
        "description": "Viết một câu sử dụng từ achievement.",
        "data": {
            "prompt": "Hãy sử dụng từ 'achievement' để viết một câu về điều gì đó đạt được nhờ nỗ lực bền bỉ thay vì tài năng bẩm sinh. Ví dụ: Her greatest achievement was not the medal itself, but the four years of early mornings and grueling training that made it possible.",
            "vocabWord": "achievement"
        }
    }

    s3_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Viết: Suy ngẫm về tài năng và nỗ lực",
        "description": "Viết một đoạn văn về mối quan hệ giữa tài năng, nỗ lực và thành tựu.",
        "data": {
            "prompt": "Duckworth lập luận rằng văn hóa của chúng ta đánh giá quá cao tài năng và đánh giá quá thấp nỗ lực. Bạn có đồng ý không? Hãy nghĩ về một lĩnh vực trong cuộc sống mà bạn đã thấy ai đó có ít tài năng tự nhiên hơn vượt qua người có nhiều tài năng hơn nhờ nỗ lực và kiên trì. Viết một đoạn văn tiếng Anh khám phá ý tưởng này, sử dụng ít nhất bốn trong số các từ sau: grit, predictor, achievement, talent, potential, mindset.",
            "vocabList": VOCAB_GROUP_3
        }
    }

    session_3 = {
        "title": "Phần 3: Grit, tài năng và tư duy phát triển",
        "activities": [
            s3_intro_topic, s3_intro_vocab, s3_view_flashcards, s3_speak_flashcards,
            s3_vocab_level1, s3_vocab_level2, s3_reading, s3_speak_reading,
            s3_read_along, s3_writing_sentence_1, s3_writing_sentence_2, s3_writing_paragraph
        ]
    }

    # ---- Session 4: Review (full article) ----
    s4_reading_text = "On a spring afternoon in 2013, Angela Duckworth walked onto the TED stage and delivered a six-minute talk that would eventually be viewed more than thirty million times. Her message was deceptively simple: the quality that best predicts success is not talent, not intelligence, not good looks or physical health. It is grit — the combination of passion and perseverance for very long-term goals.\n\nDuckworth arrived at this conclusion through an unusual path. She had been a successful management consultant, but the work left her feeling hollow. She wanted to understand something deeper about human performance. So she quit her job and became a seventh-grade math teacher in a public school serving low-income families. In that classroom, she made an observation that would define her career: the students who learned the most were not the ones with the greatest natural aptitude. They were the ones who worked with the most diligence and tenacity. They asked questions when they were confused. They redid problems they had gotten wrong. They stayed focused when their classmates had given up.\n\nThis observation led Duckworth to graduate school at the University of Pennsylvania, where she began systematically studying the predictors of achievement. Her research took her to West Point Military Academy, where she measured incoming cadets on a grit scale she had developed. The results were striking. Grit was a far better predictor of who would complete the brutal first summer of training than SAT scores, class rank, leadership potential, or physical fitness. The cadets who survived Beast Barracks were not necessarily the strongest or the smartest. They were the ones with the stamina to endure six weeks of relentless physical and psychological pressure, and the fortitude to keep going when every instinct told them to quit.\n\nShe found the same pattern in the National Spelling Bee. The children who advanced to the final rounds were distinguished not by their verbal IQ but by their resilience and the consistency of their preparation. They practiced for hours every day, targeting their weakest areas with deliberate focus. When they misspelled a word in competition, they did not spiral into self-doubt. They went home, studied the word, and came back stronger. Their endurance through months of monotonous preparation was remarkable.\n\nDuckworth's research also revealed something important about the relationship between talent and effort. She developed a simple formula: talent times effort equals skill, and skill times effort equals achievement. The key insight is that effort appears twice. A person with moderate talent who applies extraordinary effort will develop greater skill and achieve more than a person with extraordinary talent who applies only moderate effort. This formula explains why aptitude alone is such a poor predictor of long-term success. Talent determines your starting point, but determination — the conscious decision to keep working toward your goal — determines your trajectory.\n\nPerhaps the most influential aspect of Duckworth's work is her connection to Carol Dweck's research on mindset. Dweck showed that people who believe their abilities are fixed — a fixed mindset — tend to avoid challenges, give up easily, and see effort as pointless. People who believe their abilities can grow — a growth mindset — embrace challenges, persist through setbacks, and see effort as the path to mastery. Duckworth argues that a growth mindset is the foundation of grit. Without the belief that you can improve, there is no reason to persevere. With that belief, every failure becomes a lesson, every setback becomes a setup for a comeback, and every hour of deliberate practice becomes an investment in your own potential.\n\nDuckworth closes her TED Talk with a confession: she does not yet fully understand how to build grit. But she believes the best idea she has heard is Carol Dweck's concept of growth mindset — the belief that the ability to learn is not fixed, that it can change with your effort. This humility is part of what makes Duckworth's message so compelling. She is not selling a formula for guaranteed success. She is sharing a finding that is both simple and profound: the people who achieve the most are not the most talented. They are the ones who combine passion with perseverance, who show up with consistency, who practice with deliberate intention, and who possess the endurance and fortitude to keep going long after everyone else has stopped."

    s4_intro = {
        "type": "introAudio",
        "title": "Ôn tập: Bức tranh hoàn chỉnh về Grit",
        "description": "Phần ôn tập kết hợp tất cả 18 từ vựng trong một bài viết toàn diện về grit.",
        "data": {
            "text": "Chào mừng bạn đến Phần Bốn. Qua ba phần trước, bạn đã học mười tám từ vựng nắm bắt khoa học về grit. Trong Phần Một, bạn khám phá những phẩm chất bên trong: perseverance, stamina, tenacity, resilience, diligence, và fortitude. Trong Phần Hai, bạn nghiên cứu những động lực: passion, aptitude, deliberate, consistency, endurance, và determination. Trong Phần Ba, bạn xem xét bức tranh toàn cảnh: grit, predictor, achievement, talent, potential, và mindset. Bây giờ là lúc thấy tất cả mười tám từ hoạt động cùng nhau trong một bài viết toàn diện duy nhất về nghiên cứu của Angela Duckworth. Bài viết này kết nối mọi thứ bạn đã học. Khi đọc, hãy chú ý cách các từ liên kết với nhau và với các chủ đề rộng hơn của bài TED Talk của Duckworth. Hãy bắt đầu nào."
        }
    }

    s4_reading = {
        "type": "reading",
        "title": "Đọc: Khoa học về Grit — Tổng quan toàn diện",
        "description": "On a spring afternoon in 2013, Angela Duckworth walked onto the TED stage and delivered a six-min...",
        "data": {"text": s4_reading_text}
    }

    s4_speak_reading = {
        "type": "speakReading",
        "title": "Đọc: Đọc to toàn bộ bài viết",
        "description": "On a spring afternoon in 2013, Angela Duckworth walked onto the TED stage and delivered a six-min...",
        "data": {"text": s4_reading_text}
    }

    s4_read_along = {
        "type": "readAlong",
        "title": "Nghe: Khoa học về Grit — Tổng quan toàn diện",
        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
        "data": {"text": s4_reading_text}
    }

    session_4 = {
        "title": "Phần 4: Ôn tập — Bức tranh hoàn chỉnh",
        "activities": [s4_intro, s4_reading, s4_speak_reading, s4_read_along]
    }

    # ---- Session 5: Final reading + farewell ----
    s5_reading_text = "What happens after a TED Talk goes viral? For Angela Duckworth, the answer was both gratifying and complicated. Her six-minute presentation on grit resonated with millions of viewers around the world. Teachers shared it in staff meetings. Parents discussed it at dinner tables. Corporate trainers built workshops around it. But the widespread enthusiasm also brought scrutiny, and some of the criticism raised important questions about the limits and applications of grit research.\n\nOne common critique is that emphasizing grit places too much responsibility on individuals while ignoring the structural barriers that prevent many people from succeeding. A child growing up in poverty, for example, faces obstacles that no amount of perseverance alone can overcome — inadequate schools, food insecurity, unstable housing. Duckworth has acknowledged this concern. She does not argue that grit is a substitute for systemic change. Rather, she argues that within any given set of circumstances, the people who demonstrate the most grit tend to achieve the most. Grit is not a magic solution to inequality, but it is a powerful predictor of who will make the most of the opportunities they have.\n\nAnother critique focuses on measurement. Duckworth's Grit Scale — a self-report questionnaire — has been questioned by researchers who argue that self-reported perseverance and passion may not accurately capture the construct. People tend to overestimate their own tenacity and consistency. Despite these methodological debates, the core finding has been replicated across dozens of studies: sustained effort toward long-term goals is one of the strongest predictors of achievement in education, athletics, business, and the military.\n\nPerhaps the most productive line of inquiry emerging from Duckworth's work is the question of how grit can be developed. She identifies four psychological assets that contribute to grit over time. The first is interest — finding something that genuinely fascinates you. Passion does not arrive fully formed. It develops through exploration, experimentation, and the gradual discovery of what holds your attention. The second is practice — specifically, the kind of deliberate practice that targets weaknesses and pushes you beyond your comfort zone. The third is purpose — the belief that your work matters to people beyond yourself. And the fourth is hope — not wishful thinking, but the deep conviction that your own efforts can improve your future. This kind of hope is closely linked to Dweck's concept of growth mindset.\n\nThe practical implications are significant. If grit can be cultivated, then educators can design learning environments that build it. This means creating classrooms where struggle is normalized, where failure is treated as feedback rather than a verdict, and where students develop the stamina and endurance to work through difficult material rather than giving up at the first sign of confusion. It means coaching athletes to value diligence and consistency over raw talent, and helping them develop the fortitude to endure the long, unglamorous middle phase of skill development where progress is slow and invisible.\n\nIn the workplace, understanding grit can transform how organizations hire, train, and promote. Instead of selecting primarily for aptitude and credentials, companies can look for evidence of sustained commitment, resilience in the face of setbacks, and the determination to pursue difficult goals over extended periods. The research suggests that these qualities are better predictors of long-term performance than traditional measures of talent or intelligence.\n\nDuckworth herself remains cautious about overpromising. She freely admits that the science of grit is still young and that many questions remain unanswered. But she is firm on one point: the potential for human growth is far greater than most people believe. The gap between who we are and who we could become is not primarily a gap of talent. It is a gap of effort — effort sustained over time, guided by passion, sharpened by deliberate practice, and supported by a mindset that refuses to accept fixed limits on what is possible."

    s5_intro = {
        "type": "introAudio",
        "title": "Bài đọc cuối: Grit ngoài bài TED Talk",
        "description": "Giới thiệu bài đọc cuối cùng khám phá ý nghĩa rộng hơn và cuộc tranh luận xung quanh grit.",
        "data": {
            "text": "Chào mừng bạn đến Phần Năm — phần cuối cùng của bạn. Bạn đã đi một chặng đường dài. Bạn đã học mười tám từ nắm bắt khoa học về grit, đọc ba bài văn khám phá các khía cạnh khác nhau của nghiên cứu Duckworth, và luyện tập sử dụng những từ này trong bài viết của riêng bạn. Trong phần này, bạn sẽ đọc thêm một bài viết nữa — bài này nhìn vào ý nghĩa rộng hơn của nghiên cứu grit, bao gồm tác động của nó đến giáo dục, nơi làm việc, và phát triển cá nhân. Bạn sẽ gặp tất cả mười tám từ vựng trong ngữ cảnh. Sau bài đọc, chúng ta sẽ kết thúc với lời chia tay ôn lại những từ quan trọng nhất. Hãy bắt đầu nào."
        }
    }

    s5_reading = {
        "type": "reading",
        "title": "Đọc: Grit ngoài bài TED Talk",
        "description": "What happens after a TED Talk goes viral? For Angela Duckworth, the answer was both gratifying an...",
        "data": {"text": s5_reading_text}
    }

    s5_speak_reading = {
        "type": "speakReading",
        "title": "Đọc: Đọc to bài viết cuối cùng",
        "description": "What happens after a TED Talk goes viral? For Angela Duckworth, the answer was both gratifying an...",
        "data": {"text": s5_reading_text}
    }

    s5_read_along = {
        "type": "readAlong",
        "title": "Nghe: Grit ngoài bài TED Talk",
        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
        "data": {"text": s5_reading_text}
    }

    s5_farewell = {
        "type": "introAudio",
        "title": "Lời chia tay: Vốn từ vựng Grit của bạn",
        "description": "Lời chia tay đầy năng lượng ôn lại các từ vựng quan trọng và khích lệ bạn áp dụng những gì đã học.",
        "data": {
            "text": "Bạn đã hoàn thành rồi! Năm phần, mười tám từ, và một hành trình sâu vào một trong những ý tưởng quan trọng nhất của tâm lý học hiện đại. Chúng ta đã cùng nhau đi qua chặng đường này, và trước khi chia tay, hãy cùng ôn lại những từ quan trọng nhất — không chỉ như từ vựng, mà như công cụ để bạn mang theo vào cuộc sống hàng ngày.\n\nGrit có nghĩa là sự kết hợp giữa đam mê và kiên trì hướng tới mục tiêu dài hạn. Đây là một ví dụ mới: The startup founder faced three years of rejection from investors, but her grit kept her refining her product until she finally secured funding that transformed her company. Grit không phải là phẩm chất của một khoảnh khắc — mà là phẩm chất của cả một hành trình.\n\nPerseverance có nghĩa là nỗ lực liên tục bất chấp khó khăn. Hãy nghĩ thế này: The immigrant doctor showed extraordinary perseverance, studying for medical licensing exams in a new language while working two jobs to support his family. Perseverance là thứ biến giấc mơ thành hiện thực khi mọi thứ xung quanh bạn nói rằng hãy bỏ cuộc.\n\nDeliberate có nghĩa là có chủ đích, được thực hiện với sự tập trung và ý định rõ ràng. A deliberate student does not just reread her notes before an exam — she tests herself on the hardest concepts, identifies gaps in her understanding, and fills them one by one. Lần tới bạn ngồi xuống học tiếng Anh, hãy tự hỏi: mình đang học có chủ đích, hay chỉ đang bỏ thời gian?\n\nResilience có nghĩa là khả năng phục hồi từ thất bại. After losing his first three chess tournaments, the young player showed remarkable resilience — he analyzed every game he lost, identified his patterns of weakness, and returned to competition as a fundamentally stronger player. Resilience không phải là tránh thất bại. Mà là biến thất bại thành nhiên liệu.\n\nDetermination có nghĩa là sự vững vàng về mục đích. The researcher's determination to find a cure kept her working in the laboratory for twelve years, long after her colleagues had moved on to other projects. Determination là khoảnh khắc bạn ngừng do dự và bắt đầu cam kết.\n\nMindset có nghĩa là cách bạn suy nghĩ về khả năng của chính mình. Bạn tin mình có thể phát triển, hay bạn tin khả năng của mình là cố định? Câu trả lời cho câu hỏi đó định hình mọi thứ — cách bạn phản ứng với phê bình, cách bạn xử lý thất bại, và liệu bạn có kiên trì khi công việc trở nên khó khăn. Hãy chọn growth mindset. Đó là quyết định quan trọng nhất bạn có thể đưa ra cho sự phát triển của chính mình.\n\nBây giờ, đây là thử thách của chúng ta — vâng, của chúng ta, vì chúng ta là một đội. Đừng để những từ này nằm yên trên thẻ từ vựng. Hãy mang chúng vào cuộc sống. Lần tới bạn đối mặt với dự án khó khăn, hãy nhớ rằng bạn có fortitude để vượt qua. Lần tới bạn muốn bỏ cuộc, hãy nhớ rằng tenacity là sự nắm giữ không chịu buông. Lần tới ai đó nói bạn không đủ tài năng, hãy nhớ công thức của Duckworth: effort đếm hai lần. Talent là nơi bạn bắt đầu. Effort quyết định nơi bạn kết thúc.\n\nBạn đã có vốn từ vựng. Bạn đã có khung tư duy. Và quan trọng nhất, bạn đã chứng minh rằng bạn có stamina và endurance để hoàn thành khóa học này. Nếu bạn mang cùng sự diligence và consistency vào mục tiêu của mình mà bạn đã mang vào việc hoàn thành khóa học này, tôi không nghi ngờ gì bạn sẽ tự làm mình ngạc nhiên.\n\nCảm ơn bạn đã học cùng tôi. Chúng ta đã làm được điều tuyệt vời cùng nhau. Bây giờ hãy ra ngoài và sống với grit — cùng nhau, từng bước một."
        }
    }

    session_5 = {
        "title": "Phần 5: Bài đọc cuối và lời chia tay",
        "activities": [s5_intro, s5_reading, s5_speak_reading, s5_read_along, s5_farewell]
    }

    # ---- Assemble content ----
    content = {
        "title": "Grit: Sức Mạnh Của Đam Mê Và Kiên Trì",
        "description": "HÃY TƯỞNG TƯỢNG BẠN ĐANG ĐỨNG TRƯỚC MỘT CON DỐC DÀI — KHÔNG THẤY ĐỈNH, KHÔNG CÓ AI CỔ VŨ, CHỈ CÓ BẠN VÀ TỪNG BƯỚC CHÂN.\n\nBạn đã từng thấy điều này chưa? Người đồng nghiệp lặng lẽ làm việc mỗi ngày trong ba năm rồi bất ngờ được thăng chức. Đứa trẻ hàng xóm thi trượt hai lần nhưng lần thứ ba đỗ đầu. Người bạn không có nền tảng thể thao nhưng hoàn thành marathon đầu tiên chỉ bằng sự kiên trì thuần túy.\n\nĐiều họ có không phải bí mật. Đó là grit — sự kết hợp mãnh liệt giữa đam mê và kiên trì mà Angela Duckworth xác định là yếu tố dự đoán thành công mạnh nhất trong mọi lĩnh vực bà nghiên cứu. Grit giống như rễ cây đại thụ — bạn không nhìn thấy nó, nhưng nó là thứ giữ cho cả thân cây đứng vững giữa bão.\n\nHãy tưởng tượng bạn hiểu chính xác tại sao một số người kiên trì trong khi người khác bỏ cuộc. Hãy tưởng tượng bạn có vốn từ vựng để mô tả cơ chế bên trong của thành tựu dài hạn — không phải bằng những lời động viên mơ hồ, mà với sự chính xác của một nhà tâm lý học.\n\nHọc 18 từ vựng tiếng Anh đắt giá từ bài TED Talk đột phá của Duckworth. Từ perseverance và resilience đến mindset và deliberate practice, những từ này sẽ giúp bạn vừa nâng cấp tư duy về thành công, vừa nâng trình tiếng Anh một cách vượt bậc.",
        "preview": {
            "text": "Điều gì sẽ xảy ra nếu phẩm chất quan trọng nhất cho thành công không phải là tài năng, trí thông minh, hay may mắn — mà là thứ gì đó kiên cường hơn nhiều? Nghiên cứu của Angela Duckworth tiết lộ rằng sự kết hợp giữa đam mê và kiên trì dự đoán thành tựu tốt hơn bất kỳ yếu tố nào khác. Trong khóa học này, bạn sẽ làm chủ 18 từ vựng tiếng Anh trung cấp — perseverance, stamina, tenacity, resilience, diligence, fortitude, passion, aptitude, deliberate, consistency, endurance, determination, grit, predictor, achievement, talent, potential, và mindset — qua năm phần học sâu được xây dựng xung quanh bài TED Talk nổi tiếng của Duckworth. Bạn sẽ đọc các bài văn gốc khám phá khoa học về grit, luyện nói và viết với sự chính xác, và xây dựng vốn từ vựng cho phép bạn thảo luận về nỗ lực, kiên trì, và tiềm năng con người với sự tự tin của người thực sự hiểu nghiên cứu."
        },
        "contentTypeTags": ["podcast"],
        "youtubeUrl": "https://www.youtube.com/watch?v=H14bBuluwB8",
        "sessions": [session_1, session_2, session_3, session_4, session_5]
    }

    return content


def validate(content):
    """Validate all correctness properties applicable to a single curriculum."""

    # Property 1: Vocabulary count and grouping — 18 unique words across 3 groups of 6
    all_words = []
    for i in range(3):
        session = content["sessions"][i]
        vocab_activities = [a for a in session["activities"]
                           if a["type"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2")]
        assert len(vocab_activities) == 4, f"Session {i+1} should have 4 vocab activities, got {len(vocab_activities)}"
        words = vocab_activities[0]["vocabList"]
        assert len(words) == 6, f"Session {i+1} vocabList has {len(words)} words, expected 6"
        for va in vocab_activities:
            assert va["vocabList"] == words, f"Session {i+1} vocab activities have mismatched vocabLists"
        all_words.extend(words)
    assert len(all_words) == 18, f"Expected 18 total vocab words, got {len(all_words)}"
    assert len(set(all_words)) == 18, f"Expected 18 unique vocab words, got {len(set(all_words))} unique"

    # Property 2: Session and activity counts — 5 sessions with [12, 12, 12, 4, 5]
    assert len(content["sessions"]) == 5, f"Expected 5 sessions, got {len(content['sessions'])}"
    expected_counts = [12, 12, 12, 4, 5]
    for i, session in enumerate(content["sessions"]):
        actual = len(session["activities"])
        assert actual == expected_counts[i], f"Session {i+1} has {actual} activities, expected {expected_counts[i]}"

    # Property 3: Activity type sequences
    s123_types = ["introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
                  "vocabLevel1", "vocabLevel2", "reading", "speakReading",
                  "readAlong", "writingSentence", "writingSentence", "writingParagraph"]
    s4_types = ["introAudio", "reading", "speakReading", "readAlong"]
    s5_types = ["introAudio", "reading", "speakReading", "readAlong", "introAudio"]

    for i in range(3):
        actual = [a["type"] for a in content["sessions"][i]["activities"]]
        assert actual == s123_types, f"Session {i+1} activity types mismatch: {actual}"
    actual_s4 = [a["type"] for a in content["sessions"][3]["activities"]]
    assert actual_s4 == s4_types, f"Session 4 activity types mismatch: {actual_s4}"
    actual_s5 = [a["type"] for a in content["sessions"][4]["activities"]]
    assert actual_s5 == s5_types, f"Session 5 activity types mismatch: {actual_s5}"

    # Property 4: Podcast content type tags — youtubeUrl present, contentTypeTags == ["podcast"]
    assert "youtubeUrl" in content, "Missing youtubeUrl for podcast curriculum"
    assert content["youtubeUrl"] == "https://www.youtube.com/watch?v=H14bBuluwB8", "Wrong youtubeUrl"
    assert content["contentTypeTags"] == ["podcast"], f"contentTypeTags should be ['podcast'], got {content['contentTypeTags']}"

    # Property 5: vocabList correctness on vocab activities
    vocab_types = {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"}
    for si, session in enumerate(content["sessions"]):
        for ai, a in enumerate(session["activities"]):
            if a["type"] in vocab_types:
                assert "vocabList" in a, f"Session {si+1} activity {ai} ({a['type']}) missing vocabList"
                assert "words" not in a, f"Session {si+1} activity {ai} ({a['type']}) has 'words' key — should be 'vocabList'"
                assert len(a["vocabList"]) == 6, f"Session {si+1} activity {ai} vocabList has {len(a['vocabList'])} items, expected 6"
                assert all(isinstance(w, str) and w == w.lower() for w in a["vocabList"]), \
                    f"Session {si+1} activity {ai} vocabList contains non-lowercase or non-string items"

    # Property 6: Activity and session metadata completeness
    for si, session in enumerate(content["sessions"]):
        assert "title" in session and isinstance(session["title"], str) and session["title"].strip(), \
            f"Session {si+1} missing or empty title"
        for ai, a in enumerate(session["activities"]):
            assert "title" in a and isinstance(a["title"], str) and a["title"].strip(), \
                f"Session {si+1} activity {ai} missing or empty title"
            assert "description" in a and isinstance(a["description"], str) and a["description"].strip(), \
                f"Session {si+1} activity {ai} missing or empty description"

    # Property 7: Strip keys absence
    def check_no_strip_keys(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                assert k not in STRIP_KEYS, f"Strip key '{k}' found at {path}.{k}"
                check_no_strip_keys(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                check_no_strip_keys(item, f"{path}[{i}]")
    check_no_strip_keys(content)

    # Property 8: Vocab teaching script word count (500-800 words) — index 1 in sessions 1-3
    for i in range(3):
        text = content["sessions"][i]["activities"][1]["data"]["text"]
        word_count = len(text.split())
        assert 500 <= word_count <= 800, \
            f"Session {i+1} vocab teaching introAudio has {word_count} words, expected 500-800"

    print("All validations passed.")


def create():
    """Build content, validate, and create curriculum via API."""
    token = get_firebase_id_token(UID)
    content = build_content()
    content = strip_keys(content)
    validate(content)

    response = requests.post(f"{BASE_URL}/curriculum/create", json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content)
    })
    response.raise_for_status()
    result = response.json()
    curriculum_id = result["id"]
    print(f"Created curriculum: {curriculum_id}")
    print(f"\n-- Duplicate check SQL:")
    print(f"SELECT id, content->>'title' as title, created_at FROM curriculum")
    print(f"WHERE content->>'title' = 'Grit: Sức Mạnh Của Đam Mê Và Kiên Trì'")
    print(f"  AND uid = '{UID}' ORDER BY created_at;")
    return curriculum_id


if __name__ == "__main__":
    create()
