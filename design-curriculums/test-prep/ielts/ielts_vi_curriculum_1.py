#!/usr/bin/env python3
"""
IELTS Academic Vocabulary — Curriculum 1: Education Systems Around the World
Series: Luyện Thi IELTS: Từ Vựng Học Thuật
vi-en | intermediate | 18 words | 5 sessions
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API = "https://helloapi.step.is"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
SERIES_ID = "__SERIES_ID__"  # Replace after running create_ielts_vi_series.py
DISPLAY_ORDER = 1

STRIP_KEYS = {"mp3Url","illustrationSet","chapterBookmarks","segments",
              "whiteboardItems","userReadingId","lessonUniqueId",
              "curriculumTags","taskId","imageId"}

def strip(obj):
    if isinstance(obj, dict):
        return {k: strip(v) for k, v in obj.items() if k not in STRIP_KEYS}
    if isinstance(obj, list):
        return [strip(i) for i in obj]
    return obj

def api(endpoint, body):
    token = get_firebase_id_token(UID)
    body["firebaseIdToken"] = token
    r = requests.post(f"{API}/{endpoint}", json=body)
    r.raise_for_status()
    return r.json()

# --- Vocabulary ---
W1 = ["curriculum", "assessment", "compulsory", "literacy", "enroll", "tuition"]
W2 = ["scholarship", "vocational", "discipline", "qualification", "semester", "lecture"]
W3 = ["graduate", "pedagogy", "dropout", "standardized", "extracurricular", "inclusive"]
ALL = W1 + W2 + W3

TITLE = "Education Systems – Hệ Thống Giáo Dục Toàn Cầu"

DESC = """TẠI SAO CÓ NƯỚC HỌC SINH GIỎI MÀ KHÔNG CẦN THI, CÒN NƯỚC KHÁC THI LIÊN TỤC MÀ VẪN TỤT HẬU?

Phần Lan không có bài kiểm tra chuẩn hóa cho đến năm 16 tuổi — nhưng luôn đứng đầu thế giới về giáo dục. Hàn Quốc thi cử khốc liệt — nhưng tỷ lệ stress học sinh thuộc hàng cao nhất.

Sự khác biệt không nằm ở việc học nhiều hay ít, mà ở cách mỗi quốc gia thiết kế hệ thống giáo dục: từ chương trình bắt buộc đến đánh giá, từ học phí đến học bổng.

Hiểu cách thế giới dạy và học sẽ thay đổi cách bạn nhìn nhận giáo dục — và mở ra cánh cửa cho bài thi IELTS Academic.

Học 18 từ vựng học thuật về giáo dục giúp bạn vừa mở rộng kiến thức, vừa nâng trình tiếng Anh một cách vượt bậc."""

PREVIEW = """Bạn có biết rằng ở Phần Lan, trẻ em không phải thi cho đến năm 16 tuổi — nhưng quốc gia này luôn nằm trong top giáo dục thế giới? Trong khi đó, nhiều nước châu Á có hệ thống thi cử khắc nghiệt nhưng tỷ lệ bỏ học (dropout) vẫn cao. Bài học này đưa bạn vào thế giới giáo dục toàn cầu qua 18 từ vựng thiết yếu cho IELTS Academic: từ 'curriculum' (chương trình học) và 'assessment' (đánh giá), đến 'compulsory' (bắt buộc) và 'literacy' (biết chữ), qua 'scholarship' (học bổng) và 'vocational' (dạy nghề), đến 'pedagogy' (phương pháp giảng dạy) và 'standardized' (chuẩn hóa). Qua ba bài đọc phong cách IELTS Academic, bạn sẽ hiểu tại sao mỗi quốc gia chọn con đường giáo dục khác nhau — và tự tin hơn khi gặp chủ đề này trong phòng thi."""

# --- Session 1: Foundations of Education ---
S1_WELCOME = """Chào bạn, chào mừng đến với bài học đầu tiên trong chuỗi Luyện Thi IELTS: Từ Vựng Học Thuật! Chủ đề hôm nay là hệ thống giáo dục — một trong những chủ đề phổ biến nhất trong bài thi IELTS Academic Reading. Bạn sẽ gặp chủ đề này trong cả phần Reading, Writing, và Speaking. Trong buổi đầu tiên, chúng ta sẽ học 6 từ vựng nền tảng về giáo dục: curriculum, assessment, compulsory, literacy, enroll, và tuition. Đây là những từ bạn sẽ gặp đi gặp lại trong các bài đọc học thuật. Cùng bắt đầu nhé!"""

S1_VOCAB = """Chúng ta sẽ học 6 từ vựng cực kỳ quan trọng cho IELTS nhé! Từ đầu tiên là 'curriculum' — 'chương trình học'. Đây là toàn bộ nội dung và kế hoạch giảng dạy của một khóa học hoặc trường học. Ví dụ: 'The national curriculum includes subjects like mathematics, science, and language arts.' — Chương trình học quốc gia bao gồm các môn như toán, khoa học, và ngữ văn. Tiếp theo là 'assessment' — 'sự đánh giá'. Quá trình đo lường kiến thức hoặc năng lực của học sinh. Ví dụ: 'Continuous assessment throughout the year gives a more accurate picture than a single final exam.' — Đánh giá liên tục trong năm cho bức tranh chính xác hơn một bài thi cuối kỳ duy nhất. 'Compulsory' — 'bắt buộc'. Điều mà bạn phải làm theo luật hoặc quy định. Ví dụ: 'In most countries, education is compulsory until the age of 16.' — Ở hầu hết các nước, giáo dục là bắt buộc đến 16 tuổi. 'Literacy' — 'biết chữ, khả năng đọc viết'. Khả năng đọc và viết ở mức cơ bản. Ví dụ: 'The government launched a campaign to improve literacy rates in rural areas.' — Chính phủ phát động chiến dịch cải thiện tỷ lệ biết chữ ở vùng nông thôn. 'Enroll' — 'ghi danh, đăng ký'. Đăng ký chính thức vào một trường học hoặc khóa học. Ví dụ: 'Over 500 students enrolled in the new online program within the first week.' — Hơn 500 sinh viên đăng ký chương trình trực tuyến mới trong tuần đầu tiên. Cuối cùng là 'tuition' — 'học phí'. Số tiền phải trả để được học. Ví dụ: 'University tuition in the United States has increased by over 200 percent in the last 30 years.' — Học phí đại học ở Mỹ đã tăng hơn 200 phần trăm trong 30 năm qua."""

S1_GRAMMAR = """Chào bạn, trước khi đọc đoạn văn, chúng mình cùng tìm hiểu một vài điểm quan trọng nhé. Điểm đầu tiên là 'curriculum'. Đây là danh từ đếm được. Số nhiều đặc biệt: 'curricula' (theo gốc Latin) hoặc 'curriculums'. Cụm từ phổ biến: 'national curriculum' — chương trình quốc gia, 'design a curriculum' — thiết kế chương trình. Ví dụ: 'Different countries design their curricula based on cultural values and economic needs.' — Các nước thiết kế chương trình học dựa trên giá trị văn hóa và nhu cầu kinh tế. Điểm thứ hai là 'compulsory'. Đây là tính từ, đối nghĩa với 'optional' hoặc 'elective'. Cụm từ: 'compulsory education' — giáo dục bắt buộc, 'compulsory subject' — môn bắt buộc. Ví dụ: 'Physical education is compulsory in primary school but optional in university.' — Thể dục là bắt buộc ở tiểu học nhưng tự chọn ở đại học. Điểm cuối cùng là 'enroll'. Động từ này thường đi với giới từ 'in': 'enroll in a course' — đăng ký một khóa học. Danh từ: 'enrollment'. Ví dụ: 'Enrollment in public schools has declined as more families choose homeschooling.' — Số lượng đăng ký trường công đã giảm khi nhiều gia đình chọn học tại nhà."""

S1_READING = """Education is one of the most important investments a society can make. Every country designs a curriculum that reflects its values, priorities, and economic goals. In Finland, the national curriculum emphasizes creativity, critical thinking, and student well-being over memorization and testing. In contrast, many Asian education systems focus heavily on assessment — using frequent exams to measure student progress and rank schools.

Most nations have made primary education compulsory, requiring children to attend school from around age six until at least age 15 or 16. This policy has dramatically improved global literacy rates over the past century. In 1900, only about 20 percent of the world's population could read and write. Today, that figure exceeds 85 percent.

However, access to education remains unequal. In many developing countries, families struggle to enroll their children in school due to distance, poverty, or cultural barriers. Even when schools are available, the cost of tuition — for uniforms, books, and fees — can be too high for low-income families. Free public education has helped close this gap, but millions of children worldwide still lack access to quality schooling."""

# --- Session 2: Structure and Opportunity ---
S2_WELCOME = """Chào mừng bạn quay lại! Ở buổi trước, chúng ta đã học về curriculum, assessment, compulsory, literacy, enroll, và tuition — những từ nền tảng về hệ thống giáo dục. Hôm nay, chúng ta sẽ đi sâu hơn vào cấu trúc giáo dục: từ scholarship giúp học sinh nghèo tiếp cận đại học, đến vocational training — con đường học nghề mà nhiều nước đang đầu tư mạnh. Bạn cũng sẽ học về discipline, qualification, semester, và lecture. Cùng khám phá nhé!"""

S2_VOCAB = """Chúng ta sẽ học 6 từ vựng mới trong buổi học hôm nay! Từ đầu tiên là 'scholarship' — 'học bổng'. Khoản tiền được trao cho học sinh giỏi hoặc có hoàn cảnh khó khăn để hỗ trợ việc học. Ví dụ: 'She received a full scholarship to study engineering at a top university.' — Cô ấy nhận được học bổng toàn phần để học kỹ thuật tại một trường đại học hàng đầu. Tiếp theo là 'vocational' — 'dạy nghề, hướng nghiệp'. Liên quan đến đào tạo kỹ năng thực tế cho một nghề cụ thể. Ví dụ: 'Germany's vocational training system is considered one of the best in the world.' — Hệ thống đào tạo nghề của Đức được coi là một trong những hệ thống tốt nhất thế giới. 'Discipline' — 'kỷ luật; lĩnh vực'. Từ này có hai nghĩa: (1) quy tắc hành vi, (2) một lĩnh vực học thuật. Ví dụ: 'Psychology is a discipline that combines science with the study of human behavior.' — Tâm lý học là một lĩnh vực kết hợp khoa học với nghiên cứu hành vi con người. 'Qualification' — 'bằng cấp, trình độ'. Chứng chỉ hoặc bằng cấp chứng minh bạn đã hoàn thành một khóa học. Ví dụ: 'Many employers require a university qualification for entry-level positions.' — Nhiều nhà tuyển dụng yêu cầu bằng đại học cho vị trí mới vào nghề. 'Semester' — 'học kỳ'. Một nửa năm học, thường kéo dài 4-5 tháng. Ví dụ: 'Students take five courses per semester and have exams at the end of each one.' — Sinh viên học 5 môn mỗi học kỳ và thi cuối mỗi kỳ. Cuối cùng là 'lecture' — 'bài giảng'. Buổi thuyết trình dài của giảng viên trước lớp đông sinh viên. Ví dụ: 'The professor's lecture on climate change lasted two hours and covered the latest research.' — Bài giảng của giáo sư về biến đổi khí hậu kéo dài hai giờ và bao gồm nghiên cứu mới nhất."""

S2_GRAMMAR = """Chào bạn, cùng tìm hiểu một vài điểm ngữ pháp trước khi đọc nhé. Điểm đầu tiên là 'discipline'. Từ này có hai nghĩa rất khác nhau: (1) 'kỷ luật' — rules of behavior, và (2) 'lĩnh vực học thuật' — a branch of knowledge. Trong ngữ cảnh giáo dục, nghĩa thứ hai phổ biến hơn. Ví dụ: 'Engineering and medicine are disciplines that require years of specialized training.' — Kỹ thuật và y khoa là những lĩnh vực đòi hỏi nhiều năm đào tạo chuyên sâu. Điểm thứ hai là 'qualification'. Danh từ đếm được, thường dùng ở số nhiều: 'qualifications'. Cụm từ: 'academic qualifications' — bằng cấp học thuật, 'professional qualifications' — chứng chỉ chuyên môn. Ví dụ: 'Her qualifications include a master's degree and three years of teaching experience.' — Bằng cấp của cô ấy bao gồm bằng thạc sĩ và ba năm kinh nghiệm giảng dạy. Điểm cuối cùng là 'vocational'. Tính từ, thường đi với: 'vocational training' — đào tạo nghề, 'vocational school' — trường nghề, 'vocational course' — khóa học nghề. Đối lập với 'academic'. Ví dụ: 'Some students prefer vocational training over academic study because it leads directly to employment.' — Một số sinh viên thích đào tạo nghề hơn học thuật vì nó dẫn trực tiếp đến việc làm."""

S2_READING = """The structure of higher education varies significantly across countries. In the United Kingdom, a typical undergraduate degree takes three years, while in the United States, it takes four. Students attend lectures, participate in seminars, and complete assignments throughout each semester. The academic calendar, the balance between theory and practice, and the methods of assessment all differ from one system to another.

One of the biggest debates in education today is the value of vocational training versus traditional academic study. Countries like Germany and Switzerland have strong vocational systems where students learn practical skills — such as plumbing, electrical work, or healthcare — alongside classroom instruction. Graduates of these programs earn recognized qualifications that lead directly to employment. In contrast, many countries still prioritize university degrees, even though not every discipline requires one.

Access to higher education often depends on financial resources. Scholarship programs help talented students from low-income families attend university, but demand far exceeds supply. Meanwhile, strict discipline in schools — particularly in East Asian countries — has produced impressive academic results, though critics argue it comes at the cost of creativity and mental health. The challenge for every education system is finding the right balance between structure and freedom, between academic knowledge and practical skills."""

# --- Session 3: Reform and the Future ---
S3_WELCOME = """Chào mừng bạn đến buổi học thứ ba! Ở hai buổi trước, bạn đã học 12 từ vựng về nền tảng và cấu trúc giáo dục. Hôm nay, chúng ta sẽ nói về cải cách giáo dục và tương lai: từ graduate — tốt nghiệp, đến pedagogy — phương pháp giảng dạy, dropout — bỏ học, standardized — chuẩn hóa, extracurricular — ngoại khóa, và inclusive — hòa nhập. Đây là những từ bạn sẽ gặp rất nhiều trong IELTS Academic Reading khi đọc về chính sách giáo dục. Cùng học nhé!"""

S3_VOCAB = """Chúng ta sẽ học 6 từ vựng cuối cùng của bài học này! Từ đầu tiên là 'graduate' — 'tốt nghiệp; người tốt nghiệp'. Từ này vừa là động từ vừa là danh từ. Ví dụ: 'She graduated from medical school in 2020 and is now a practicing doctor.' — Cô ấy tốt nghiệp trường y năm 2020 và hiện là bác sĩ. Tiếp theo là 'pedagogy' — 'phương pháp giảng dạy'. Nghệ thuật và khoa học của việc dạy học. Ví dụ: 'Modern pedagogy emphasizes active learning rather than passive listening.' — Phương pháp giảng dạy hiện đại nhấn mạnh học chủ động thay vì nghe thụ động. 'Dropout' — 'người bỏ học; sự bỏ học'. Người rời trường trước khi hoàn thành chương trình. Ví dụ: 'The dropout rate in rural schools is three times higher than in urban areas.' — Tỷ lệ bỏ học ở trường nông thôn cao gấp ba lần so với thành thị. 'Standardized' — 'chuẩn hóa'. Được thiết kế để mọi người làm cùng một bài theo cùng điều kiện. Ví dụ: 'Standardized tests like IELTS and TOEFL are used worldwide to measure English proficiency.' — Các bài thi chuẩn hóa như IELTS và TOEFL được sử dụng toàn cầu để đo trình độ tiếng Anh. 'Extracurricular' — 'ngoại khóa'. Hoạt động ngoài chương trình học chính thức. Ví dụ: 'Extracurricular activities like sports, music, and debate help students develop social skills.' — Hoạt động ngoại khóa như thể thao, âm nhạc, và tranh biện giúp học sinh phát triển kỹ năng xã hội. Cuối cùng là 'inclusive' — 'hòa nhập, bao trùm'. Đảm bảo mọi người đều được tham gia, không ai bị loại trừ. Ví dụ: 'An inclusive classroom welcomes students of all abilities, including those with disabilities.' — Lớp học hòa nhập chào đón học sinh mọi khả năng, bao gồm cả người khuyết tật."""

S3_GRAMMAR = """Chào bạn, cùng tìm hiểu ngữ pháp trước khi đọc nhé. Điểm đầu tiên là 'graduate'. Từ này vừa là động từ vừa là danh từ. Động từ: 'graduate from' + trường. Danh từ: 'a graduate' — người tốt nghiệp. Tính từ: 'graduate student' — nghiên cứu sinh. Ví dụ: 'After graduating from university, many graduates struggle to find jobs in their field.' — Sau khi tốt nghiệp đại học, nhiều người tốt nghiệp gặp khó khăn tìm việc đúng ngành. Điểm thứ hai là 'standardized'. Tính từ, thường đi với 'test', 'exam', 'assessment'. Động từ gốc: 'standardize' — chuẩn hóa. Danh từ: 'standardization'. Ví dụ: 'The standardization of testing has made it easier to compare students across different schools.' — Việc chuẩn hóa bài thi giúp so sánh học sinh giữa các trường dễ dàng hơn. Điểm cuối cùng là 'inclusive'. Tính từ, đối nghĩa: 'exclusive'. Danh từ: 'inclusion'. Cụm từ: 'inclusive education' — giáo dục hòa nhập, 'inclusive policy' — chính sách bao trùm. Ví dụ: 'Inclusive education policies ensure that children with special needs learn alongside their peers.' — Chính sách giáo dục hòa nhập đảm bảo trẻ có nhu cầu đặc biệt học cùng bạn bè."""

S3_READING = """Education reform is one of the most debated topics in public policy. At the heart of the debate is a simple question: what is the best way to prepare young people for the future? Traditional pedagogy — the teacher stands at the front and lectures while students listen — is being challenged by new approaches that emphasize collaboration, problem-solving, and technology.

One controversial area is standardized testing. Supporters argue that standardized exams provide an objective way to measure student achievement and hold schools accountable. Critics counter that these tests encourage teaching to the test, reduce creativity, and put enormous pressure on students. In some countries, the pressure is so intense that the dropout rate has become a serious concern. Students who fall behind or lose motivation simply leave school, often without any qualification.

Many educators now advocate for a more inclusive approach — one that recognizes different learning styles and provides support for students with disabilities, language barriers, or economic disadvantages. Extracurricular activities play an important role in this vision. Sports, arts, and community service help students develop skills that no exam can measure: teamwork, leadership, and resilience. The countries that graduate the most successful citizens are not necessarily those with the hardest exams, but those that create environments where every student has the opportunity to learn and grow."""

# --- Session 4: Review ---
S4_REVIEW_INTRO = """Chúc mừng bạn đã học xong toàn bộ 18 từ vựng! Từ curriculum và assessment — nền tảng của mọi hệ thống giáo dục, đến compulsory education và literacy — quyền cơ bản của mọi trẻ em, qua enroll và tuition — rào cản tiếp cận giáo dục, đến scholarship và vocational training — con đường mở rộng cơ hội, qua discipline và qualification — cấu trúc của giáo dục đại học, đến semester và lecture — nhịp sống đại học, và cuối cùng là graduate, pedagogy, dropout, standardized, extracurricular, và inclusive — những từ về cải cách và tương lai giáo dục. Hôm nay là buổi ôn tập. Bạn sẽ xem lại flashcards và làm bài tập cho toàn bộ 18 từ. Hãy chắc chắn bạn nhớ hết trước khi đọc bài đọc tổng hợp ở buổi cuối!"""

# --- Session 5: Full Reading & Farewell ---
FULL_READING = """Education is one of the most important investments a society can make. Every country designs a curriculum that reflects its values, priorities, and economic goals. In Finland, the national curriculum emphasizes creativity, critical thinking, and student well-being over memorization and testing. In contrast, many Asian education systems focus heavily on assessment — using frequent exams to measure student progress and rank schools.

Most nations have made primary education compulsory, requiring children to attend school from around age six until at least age 15 or 16. This policy has dramatically improved global literacy rates over the past century. In 1900, only about 20 percent of the world's population could read and write. Today, that figure exceeds 85 percent. However, access to education remains unequal. In many developing countries, families struggle to enroll their children in school due to distance, poverty, or cultural barriers. Even when schools are available, the cost of tuition — for uniforms, books, and fees — can be too high for low-income families.

The structure of higher education varies significantly across countries. Students attend lectures, participate in seminars, and complete assignments throughout each semester. One of the biggest debates in education today is the value of vocational training versus traditional academic study. Countries like Germany and Switzerland have strong vocational systems where students learn practical skills alongside classroom instruction. Graduates of these programs earn recognized qualifications that lead directly to employment. In contrast, many countries still prioritize university degrees, even though not every discipline requires one. Scholarship programs help talented students from low-income families attend university, but demand far exceeds supply. Meanwhile, strict discipline in schools has produced impressive academic results, though critics argue it comes at the cost of creativity.

Education reform is one of the most debated topics in public policy. Traditional pedagogy — the teacher stands at the front and lectures while students listen — is being challenged by new approaches that emphasize collaboration and technology. Standardized testing remains controversial: supporters say it provides objective measurement, while critics argue it encourages teaching to the test and increases the dropout rate. Many educators now advocate for a more inclusive approach that recognizes different learning styles. Extracurricular activities — sports, arts, and community service — help students develop skills that no exam can measure. The countries that graduate the most successful citizens are not necessarily those with the hardest exams, but those that create environments where every student has the opportunity to learn and grow."""

S5_INTRO = """Chào mừng bạn đến buổi học cuối cùng! Bạn đã học 18 từ vựng, ôn tập kỹ lưỡng, và đọc ba đoạn văn ngắn. Bây giờ là lúc đọc bài viết hoàn chỉnh — một bài đọc phong cách IELTS Academic về hệ thống giáo dục toàn cầu. Khi đọc, hãy chú ý cách mỗi từ vựng xuất hiện tự nhiên trong ngữ cảnh: curriculum, assessment, compulsory, literacy, enroll, tuition, scholarship, vocational, discipline, qualification, semester, lecture, graduate, pedagogy, dropout, standardized, extracurricular, và inclusive. Chúc bạn đọc vui!"""

FAREWELL = """Chúc mừng bạn đã hoàn thành bài học 'Education Systems — Hệ Thống Giáo Dục Toàn Cầu'! Trước khi chia tay, chúng ta cùng ôn lại 18 từ vựng nhé.

Từ thứ nhất: 'curriculum' — chương trình học. Ví dụ mới: 'The school updated its curriculum to include computer science and financial literacy.'

Từ thứ hai: 'assessment' — sự đánh giá. Ví dụ: 'Teachers use both written exams and project-based assessment to evaluate students.'

Từ thứ ba: 'compulsory' — bắt buộc. Ví dụ: 'Learning a second language is compulsory in many European schools from age eight.'

Từ thứ tư: 'literacy' — biết chữ. Ví dụ: 'Digital literacy is now considered as important as traditional reading and writing skills.'

Từ thứ năm: 'enroll' — ghi danh. Ví dụ: 'Parents must enroll their children in school before the September deadline.'

Từ thứ sáu: 'tuition' — học phí. Ví dụ: 'Some countries offer free tuition at public universities to encourage higher education.'

Từ thứ bảy: 'scholarship' — học bổng. Ví dụ: 'The scholarship covered not only tuition but also living expenses for four years.'

Từ thứ tám: 'vocational' — dạy nghề. Ví dụ: 'Vocational programs in healthcare train students to become nurses and medical technicians.'

Từ thứ chín: 'discipline' — kỷ luật; lĩnh vực. Ví dụ: 'Data science has emerged as one of the fastest-growing academic disciplines.'

Từ thứ mười: 'qualification' — bằng cấp. Ví dụ: 'Without the right qualifications, it is difficult to compete in today's job market.'

Từ thứ mười một: 'semester' — học kỳ. Ví dụ: 'She spent one semester studying abroad in Japan and it changed her perspective.'

Từ thứ mười hai: 'lecture' — bài giảng. Ví dụ: 'Online lectures have made university education accessible to people around the world.'

Từ thứ mười ba: 'graduate' — tốt nghiệp. Ví dụ: 'He graduated with honors and received three job offers before the ceremony.'

Từ thứ mười bốn: 'pedagogy' — phương pháp giảng dạy. Ví dụ: 'Research in pedagogy shows that students learn better when they are actively involved.'

Từ thứ mười lăm: 'dropout' — bỏ học. Ví dụ: 'Reducing the dropout rate requires addressing poverty, bullying, and lack of support.'

Từ thứ mười sáu: 'standardized' — chuẩn hóa. Ví dụ: 'Standardized testing is used in over 100 countries to assess student performance.'

Từ thứ mười bảy: 'extracurricular' — ngoại khóa. Ví dụ: 'Universities look at extracurricular activities as well as grades when selecting students.'

Từ thứ mười tám: 'inclusive' — hòa nhập. Ví dụ: 'An inclusive school ensures that every child, regardless of background, receives quality education.'

Và thế là xong! Bạn đã nắm vững 18 từ vựng học thuật về giáo dục — những từ bạn sẽ gặp lại trong bài thi IELTS Academic. Từ curriculum đến inclusive, mỗi từ đều là một công cụ giúp bạn đọc hiểu và viết tốt hơn. Cảm ơn bạn đã đồng hành, và chúc bạn thành công trên hành trình chinh phục IELTS!"""

# --- Writing sentence prompts ---
S1_WRITING_ITEMS = [
    {"targetVocab": "curriculum", "prompt": "Sử dụng từ 'curriculum' trong một câu về chương trình học ở trường. Example: The school redesigned its curriculum to focus more on practical skills and less on memorization."},
    {"targetVocab": "assessment", "prompt": "Sử dụng từ 'assessment' trong một câu về cách đánh giá học sinh. Example: Many teachers believe that continuous assessment is fairer than a single final exam."},
    {"targetVocab": "compulsory", "prompt": "Sử dụng từ 'compulsory' trong một câu về quy định giáo dục. Example: In Vietnam, nine years of education are compulsory for all children."},
    {"targetVocab": "literacy", "prompt": "Sử dụng từ 'literacy' trong một câu về khả năng đọc viết. Example: Improving literacy rates is essential for economic development in any country."},
    {"targetVocab": "enroll", "prompt": "Sử dụng từ 'enroll' trong một câu về đăng ký học. Example: She decided to enroll in an English course to prepare for the IELTS exam."},
    {"targetVocab": "tuition", "prompt": "Sử dụng từ 'tuition' trong một câu về chi phí học tập. Example: The high cost of tuition prevents many talented students from attending university."},
]

S2_WRITING_ITEMS = [
    {"targetVocab": "scholarship", "prompt": "Sử dụng từ 'scholarship' trong một câu về hỗ trợ tài chính cho học sinh. Example: Without the scholarship, he would not have been able to afford a university education."},
    {"targetVocab": "vocational", "prompt": "Sử dụng từ 'vocational' trong một câu về đào tạo nghề. Example: Vocational training programs help young people develop skills that employers actually need."},
    {"targetVocab": "discipline", "prompt": "Sử dụng từ 'discipline' trong một câu về lĩnh vực học thuật hoặc kỷ luật. Example: Economics is a discipline that helps us understand how societies allocate resources."},
    {"targetVocab": "qualification", "prompt": "Sử dụng từ 'qualification' trong một câu về bằng cấp. Example: A teaching qualification is required for anyone who wants to work in public schools."},
    {"targetVocab": "semester", "prompt": "Sử dụng từ 'semester' trong một câu về thời gian học. Example: The first semester covers basic theory, while the second focuses on practical application."},
    {"targetVocab": "lecture", "prompt": "Sử dụng từ 'lecture' trong một câu về giảng dạy đại học. Example: The lecture on global warming attracted over 300 students from different departments."},
]

S3_WRITING_ITEMS = [
    {"targetVocab": "graduate", "prompt": "Sử dụng từ 'graduate' trong một câu về tốt nghiệp. Example: Many students graduate from university without clear career plans."},
    {"targetVocab": "pedagogy", "prompt": "Sử dụng từ 'pedagogy' trong một câu về phương pháp giảng dạy. Example: Good pedagogy involves understanding how different students learn best."},
    {"targetVocab": "dropout", "prompt": "Sử dụng từ 'dropout' trong một câu về bỏ học. Example: The school introduced mentoring programs to reduce the dropout rate among at-risk students."},
    {"targetVocab": "standardized", "prompt": "Sử dụng từ 'standardized' trong một câu về bài thi chuẩn hóa. Example: Standardized tests may not accurately reflect a student's true abilities and potential."},
    {"targetVocab": "extracurricular", "prompt": "Sử dụng từ 'extracurricular' trong một câu về hoạt động ngoại khóa. Example: Participating in extracurricular activities teaches students time management and teamwork."},
    {"targetVocab": "inclusive", "prompt": "Sử dụng từ 'inclusive' trong một câu về giáo dục hòa nhập. Example: An inclusive education system benefits all students, not just those with special needs."},
]

# ============================================================
# BUILD CURRICULUM JSON
# ============================================================

def make_learning_session(title, words, welcome, vocab, grammar, reading, writing_items):
    return {
        "title": title,
        "activities": [
            {"activityType": "introAudio", "title": "Giới thiệu bài học",
             "description": f"Nghe giới thiệu về chủ đề buổi học",
             "practiceMinutes": "1",
             "data": {"text": welcome, "audioSpeed": 0.01}},
            {"activityType": "introAudio", "title": "Giới thiệu từ vựng",
             "description": "Nghe giới thiệu về các từ vựng trong bài và cách dùng",
             "practiceMinutes": "3",
             "data": {"text": vocab, "audioSpeed": 0.01}},
            {"activityType": "viewFlashcards", "title": f"Từ vựng: Education",
             "description": f"Học các từ: {', '.join(words)}",
             "practiceMinutes": "6",
             "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "speakFlashcards", "title": f"Tập nói từ vựng: Education",
             "description": f"Tập nói các từ: {', '.join(words)}",
             "practiceMinutes": "6",
             "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel1", "title": f"Bài tập nhận biết: Education",
             "description": "Chọn nghĩa đúng cho các từ vựng vừa học",
             "practiceMinutes": "10",
             "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel2", "title": f"Bài tập nhớ lại chủ động: Education",
             "description": "Điền từ thích hợp vào chỗ trống mà không có gợi ý",
             "practiceMinutes": "10",
             "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel3", "title": f"Bài tập hiểu sâu: Education",
             "description": "Kiểm tra khả năng hiểu và vận dụng từ vựng trong ngữ cảnh",
             "practiceMinutes": "10",
             "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "introAudio", "title": "Giải thích ngữ pháp",
             "description": "Nghe giải thích các điểm ngữ pháp và cách dùng từ trong ngữ cảnh",
             "practiceMinutes": "3",
             "data": {"text": grammar, "audioSpeed": 0.01}},
            {"activityType": "reading", "title": "Đọc ngắn: Education Systems",
             "description": reading[:80],
             "practiceMinutes": "5",
             "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "speakReading", "title": "Luyện nói theo: Education Systems",
             "description": "Tập phát âm đoạn văn bằng cách lặp lại",
             "practiceMinutes": "5",
             "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "readAlong", "title": "Nghe bài đọc: Education Systems",
             "description": "Nghe nội dung bài đọc ngắn",
             "practiceMinutes": "3",
             "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "writingSentence", "title": "Viết câu với từ vựng mục tiêu",
             "description": f"Viết câu tiếng Anh sử dụng từ vựng: {', '.join(words)}",
             "practiceMinutes": "10",
             "data": {"vocabList": words, "audioSpeed": 0.01,
                      "items": writing_items}},
        ]
    }

content = {
    "title": TITLE,
    "description": DESC,
    "preview": {"text": PREVIEW},
    "learningSessions": [
        make_learning_session("Buổi 1: Nền tảng giáo dục", W1, S1_WELCOME, S1_VOCAB, S1_GRAMMAR, S1_READING, S1_WRITING_ITEMS),
        make_learning_session("Buổi 2: Cấu trúc & Cơ hội", W2, S2_WELCOME, S2_VOCAB, S2_GRAMMAR, S2_READING, S2_WRITING_ITEMS),
        make_learning_session("Buổi 3: Cải cách & Tương lai", W3, S3_WELCOME, S3_VOCAB, S3_GRAMMAR, S3_READING, S3_WRITING_ITEMS),
        # Session 4: Review
        {
            "title": "Buổi 4: Ôn tập toàn bộ",
            "activities": [
                {"activityType": "introAudio", "title": "Dẫn nhập ôn tập",
                 "description": "Nghe hướng dẫn ôn tập lại toàn bộ từ vựng",
                 "practiceMinutes": "1",
                 "data": {"text": S4_REVIEW_INTRO, "audioSpeed": 0.01}},
                {"activityType": "viewFlashcards", "title": "Ôn tập tất cả từ vựng",
                 "description": "Xem lại flashcards cho 18 từ vựng của toàn bộ khóa học",
                 "practiceMinutes": "6",
                 "data": {"vocabList": ALL, "audioSpeed": -0.1}},
                {"activityType": "vocabLevel1", "title": "Kiểm tra nhanh: Nhận biết",
                 "description": "Bài tập trắc nghiệm nhanh cho toàn bộ 18 từ",
                 "practiceMinutes": "10",
                 "data": {"vocabList": ALL, "audioSpeed": -0.1}},
                {"activityType": "vocabLevel2", "title": "Kiểm tra sâu: Nhớ lại",
                 "description": "Ghi nhớ chủ động các từ vựng toàn bộ khóa học",
                 "practiceMinutes": "10",
                 "data": {"vocabList": ALL, "audioSpeed": -0.1}},
            ]
        },
        # Session 5: Full reading + farewell
        {
            "title": "Buổi 5: Đọc trọn vẹn",
            "activities": [
                {"activityType": "introAudio", "title": "Dẫn nhập bài đọc cuối",
                 "description": "Lời dẫn cho bài đọc tổng hợp",
                 "practiceMinutes": "1",
                 "data": {"text": S5_INTRO, "audioSpeed": 0.01}},
                {"activityType": "reading", "title": "Đọc hiểu: Hệ Thống Giáo Dục Toàn Cầu",
                 "description": "Đọc toàn bộ bài viết hoàn chỉnh có chứa 18 từ vựng đã học",
                 "practiceMinutes": "15",
                 "data": {"text": FULL_READING, "audioSpeed": -0.1}},
                {"activityType": "speakReading", "title": "Luyện nói theo: Hệ Thống Giáo Dục Toàn Cầu",
                 "description": "Phát âm toàn bộ bài viết hoàn chỉnh",
                 "practiceMinutes": "15",
                 "data": {"text": FULL_READING, "audioSpeed": -0.1}},
                {"activityType": "readAlong", "title": "Nghe bài đọc tổng hợp",
                 "description": "Nghe toàn bộ bài viết hoàn chỉnh",
                 "practiceMinutes": "3",
                 "data": {"text": FULL_READING, "audioSpeed": -0.1}},
                {"activityType": "introAudio", "title": "Tổng kết & Chúc mừng hoàn thành",
                 "description": "Ôn lại 18 từ vựng và lời chào tạm biệt",
                 "practiceMinutes": "4",
                 "data": {"text": FAREWELL, "audioSpeed": 0.01}},
            ]
        },
    ]
}

content = strip(content)

# --- Upload ---
if __name__ == "__main__":
    print(f"Creating: {TITLE}")
    result = api("curriculum/create", {
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    })
    cid = result["id"]
    print(f"Created curriculum: {cid}")

    # Add to series
    api("curriculum-series/addCurriculum", {
        "curriculumSeriesId": SERIES_ID,
        "curriculumId": cid,
    })
    print(f"Added to series {SERIES_ID}")

    # Set display order
    api("curriculum/setDisplayOrder", {
        "id": cid,
        "displayOrder": DISPLAY_ORDER,
    })
    print(f"Set displayOrder={DISPLAY_ORDER}")

    print(f"\nDone! Curriculum ID: {cid}")
