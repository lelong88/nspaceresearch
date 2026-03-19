#!/usr/bin/env python3
"""
IELTS Academic Vocabulary — Curriculum 3: Health & Medicine
Series: Luyện Thi IELTS: Từ Vựng Học Thuật
vi-en | intermediate | 18 words | 5 sessions
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API = "https://helloapi.step.is"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
SERIES_ID = "__SERIES_ID__"  # Replace after running create_ielts_vi_series.py
DISPLAY_ORDER = 3

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

W1 = ["symptom", "diagnosis", "treatment", "chronic", "immune system", "vaccine"]
W2 = ["prescription", "surgery", "epidemic", "nutrition", "mental health", "prevention"]
W3 = ["life expectancy", "healthcare", "obesity", "antibiotic", "rehabilitation", "well-being"]
ALL = W1 + W2 + W3

TITLE = "Health & Medicine – Sức Khỏe: Hiểu Cơ Thể, Hiểu Cuộc Sống"

DESC = """CƠ THỂ BẠN ĐANG GỬI TÍN HIỆU CẦU CỨU — BẠN CÓ NGHE THẤY KHÔNG?

Mỗi ngày, cơ thể bạn chiến đấu với hàng nghìn mầm bệnh mà bạn không hề hay biết. Hệ miễn dịch làm việc không ngừng, nhưng khi nó kiệt sức — từ một cơn cảm cúm đến những căn bệnh mãn tính — bạn mới nhận ra sức khỏe quý giá đến nhường nào.

Tại sao có người sống khỏe đến 90 tuổi, trong khi người khác phải vật lộn với bệnh tật từ năm 40? Câu trả lời không chỉ nằm ở gen di truyền — mà ở cách bạn hiểu và chăm sóc cơ thể mình. Nếu không hiểu "triệu chứng" cơ thể đang nói gì, bạn sẽ mãi như người lái xe mà không nhìn đồng hồ cảnh báo.

Khám phá thế giới y học — từ vaccine cứu hàng triệu mạng người đến cuộc chiến chống béo phì toàn cầu — và tại sao hiểu về sức khỏe là khoản đầu tư sinh lời nhất cuộc đời.

Học 18 từ vựng học thuật về y tế giúp bạn vừa nâng cấp kiến thức sức khỏe, vừa sẵn sàng chinh phục bài thi IELTS Academic."""

PREVIEW = """Sức khỏe là tài sản quý giá nhất — nhưng bạn có thực sự hiểu cơ thể mình đang nói gì? Bài học này đưa bạn vào thế giới y tế qua 18 từ vựng thiết yếu cho IELTS Academic: từ 'symptom' (triệu chứng) và 'diagnosis' (chẩn đoán), đến 'treatment' (điều trị) và 'chronic' (mãn tính), qua 'immune system' (hệ miễn dịch) và 'vaccine' (vắc-xin), đến 'prescription' (đơn thuốc) và 'surgery' (phẫu thuật), qua 'epidemic' (dịch bệnh) và 'prevention' (phòng ngừa), đến 'life expectancy' (tuổi thọ) và 'obesity' (béo phì). Qua ba bài đọc phong cách IELTS Academic, bạn sẽ hiểu tại sao y tế vừa là khoa học vừa là trách nhiệm của mỗi người trong thế kỷ 21."""

S1_WELCOME = """Chào bạn, chào mừng đến với bài học thứ ba trong chuỗi Luyện Thi IELTS! Chủ đề hôm nay là sức khỏe và y tế — một chủ đề xuất hiện rất thường xuyên trong IELTS Academic. Bạn sẽ gặp chủ đề này trong Reading, Writing Task 2, và cả Speaking Part 3. Trong buổi đầu tiên, chúng ta sẽ học 6 từ vựng nền tảng: symptom, diagnosis, treatment, chronic, immune system, và vaccine. Cùng bắt đầu nhé!"""

S1_VOCAB = """Từ đầu tiên là 'symptom' — 'triệu chứng'. Dấu hiệu cho thấy cơ thể đang có vấn đề về sức khỏe. Ví dụ: 'Common symptoms of the flu include fever, headache, and muscle pain.' — Các triệu chứng phổ biến của cúm bao gồm sốt, đau đầu, và đau cơ. Tiếp theo là 'diagnosis' — 'chẩn đoán'. Quá trình xác định bệnh dựa trên triệu chứng và xét nghiệm. Ví dụ: 'Early diagnosis of cancer significantly increases the chances of successful treatment.' — Chẩn đoán sớm ung thư tăng đáng kể cơ hội điều trị thành công. 'Treatment' — 'điều trị'. Phương pháp y tế được sử dụng để chữa bệnh hoặc giảm triệu chứng. Ví dụ: 'The treatment for malaria involves a combination of antimalarial drugs taken over several days.' — Điều trị sốt rét bao gồm kết hợp thuốc chống sốt rét uống trong nhiều ngày. 'Chronic' — 'mãn tính'. Kéo dài trong thời gian dài, thường là vĩnh viễn. Ví dụ: 'Chronic diseases like diabetes and heart disease account for 70 percent of all deaths worldwide.' — Bệnh mãn tính như tiểu đường và bệnh tim chiếm 70 phần trăm tổng số ca tử vong trên thế giới. 'Immune system' — 'hệ miễn dịch'. Hệ thống phòng thủ tự nhiên của cơ thể chống lại bệnh tật. Ví dụ: 'A healthy immune system can fight off most common infections without medical intervention.' — Hệ miễn dịch khỏe mạnh có thể chống lại hầu hết các bệnh nhiễm trùng thông thường mà không cần can thiệp y tế. Cuối cùng là 'vaccine' — 'vắc-xin'. Chế phẩm sinh học giúp cơ thể tạo miễn dịch chống lại bệnh cụ thể. Ví dụ: 'The development of vaccines has saved millions of lives by preventing diseases like polio and measles.' — Sự phát triển của vắc-xin đã cứu hàng triệu mạng người bằng cách ngăn ngừa các bệnh như bại liệt và sởi."""

S1_GRAMMAR = """Cùng tìm hiểu ngữ pháp nhé. Điểm đầu tiên là 'symptom'. Danh từ đếm được, số nhiều: 'symptoms'. Cụm từ: 'show symptoms' — biểu hiện triệu chứng, 'symptom of' — triệu chứng của. Tính từ: 'symptomatic' (có triệu chứng), đối lập: 'asymptomatic' (không triệu chứng). Ví dụ: 'Some patients remain asymptomatic for weeks, making the disease harder to detect.' — Một số bệnh nhân không có triệu chứng trong nhiều tuần, khiến bệnh khó phát hiện hơn. Điểm thứ hai là 'diagnosis'. Danh từ đếm được, số nhiều: 'diagnoses'. Động từ: 'diagnose'. Cụm từ: 'make a diagnosis' — đưa ra chẩn đoán, 'be diagnosed with' — được chẩn đoán mắc. Ví dụ: 'She was diagnosed with diabetes at the age of 35 after experiencing extreme fatigue.' — Cô ấy được chẩn đoán mắc tiểu đường năm 35 tuổi sau khi bị mệt mỏi cực độ. Điểm cuối là 'chronic'. Tính từ, đối nghĩa: 'acute' (cấp tính). Cụm từ: 'chronic disease' — bệnh mãn tính, 'chronic pain' — đau mãn tính. Trạng từ: 'chronically'. Ví dụ: 'Chronically ill patients often require lifelong medication and regular medical check-ups.' — Bệnh nhân mãn tính thường cần dùng thuốc suốt đời và khám sức khỏe định kỳ."""

S1_READING = """Every year, millions of people visit their doctors because of symptoms they cannot explain — persistent headaches, unusual fatigue, or sudden weight loss. These symptoms are the body's way of signaling that something is wrong. The process of diagnosis begins when a doctor listens to the patient, examines the body, and orders tests such as blood work or imaging scans. An accurate diagnosis is essential because it determines the treatment plan.

For many conditions, treatment is straightforward: antibiotics for bacterial infections, rest for mild injuries, or medication for high blood pressure. But chronic diseases — conditions that last for months or years — present a much greater challenge. Diabetes, asthma, and heart disease require ongoing management rather than a simple cure. The immune system plays a central role in how the body responds to illness. When it functions well, it destroys harmful bacteria and viruses before they cause serious damage. Vaccines work by training the immune system to recognize specific threats, allowing the body to respond quickly if exposed to the real disease. The development of vaccines against smallpox, polio, and measles has saved hundreds of millions of lives over the past century."""

S2_WELCOME = """Chào mừng bạn quay lại! Ở buổi trước, chúng ta đã học về symptom, diagnosis, treatment, chronic, immune system, và vaccine. Hôm nay, chúng ta sẽ tìm hiểu sâu hơn về hệ thống y tế: từ prescription — đơn thuốc, đến surgery — phẫu thuật, và cách phòng ngừa dịch bệnh qua prevention — phòng ngừa. Cùng học nhé!"""

S2_VOCAB = """Từ đầu tiên là 'prescription' — 'đơn thuốc'. Giấy chỉ định của bác sĩ về loại thuốc và liều lượng bệnh nhân cần dùng. Ví dụ: 'The doctor wrote a prescription for antibiotics and advised the patient to complete the full course.' — Bác sĩ kê đơn thuốc kháng sinh và khuyên bệnh nhân uống hết liệu trình. Tiếp theo là 'surgery' — 'phẫu thuật'. Thủ thuật y tế cắt mở cơ thể để sửa chữa hoặc loại bỏ phần bị tổn thương. Ví dụ: 'Heart surgery has become much safer thanks to advances in medical technology.' — Phẫu thuật tim đã trở nên an toàn hơn nhiều nhờ tiến bộ công nghệ y tế. 'Epidemic' — 'dịch bệnh'. Sự bùng phát nhanh chóng của bệnh truyền nhiễm trong một khu vực. Ví dụ: 'The Ebola epidemic in West Africa killed over 11,000 people between 2014 and 2016.' — Dịch Ebola ở Tây Phi đã giết hơn 11.000 người từ 2014 đến 2016. 'Nutrition' — 'dinh dưỡng'. Quá trình cung cấp chất dinh dưỡng cần thiết cho cơ thể qua thức ăn. Ví dụ: 'Good nutrition during childhood is essential for healthy brain development and strong bones.' — Dinh dưỡng tốt trong thời thơ ấu rất cần thiết cho phát triển não và xương chắc khỏe. 'Mental health' — 'sức khỏe tâm thần'. Trạng thái tâm lý và cảm xúc ảnh hưởng đến cách suy nghĩ, cảm nhận và hành xử. Ví dụ: 'The pandemic had a devastating impact on mental health, with rates of anxiety and depression doubling worldwide.' — Đại dịch có tác động tàn khốc đến sức khỏe tâm thần, tỷ lệ lo âu và trầm cảm tăng gấp đôi trên toàn thế giới. Cuối cùng là 'prevention' — 'phòng ngừa'. Hành động ngăn chặn bệnh tật trước khi nó xảy ra. Ví dụ: 'Disease prevention through vaccination and hygiene is far more cost-effective than treatment.' — Phòng ngừa bệnh qua tiêm chủng và vệ sinh hiệu quả về chi phí hơn nhiều so với điều trị."""

S2_GRAMMAR = """Cùng tìm hiểu ngữ pháp nhé. Điểm đầu tiên là 'prescription'. Danh từ đếm được. Cụm từ: 'write a prescription' — kê đơn thuốc, 'prescription drug' — thuốc kê đơn (đối lập: 'over-the-counter drug' — thuốc không kê đơn). Động từ: 'prescribe'. Ví dụ: 'Doctors prescribe painkillers only when other treatments have failed.' — Bác sĩ kê thuốc giảm đau chỉ khi các phương pháp điều trị khác thất bại. Điểm thứ hai là 'surgery'. Danh từ, có thể đếm được hoặc không đếm được. Cụm từ: 'undergo surgery' — trải qua phẫu thuật, 'perform surgery' — thực hiện phẫu thuật. Người: 'surgeon' — bác sĩ phẫu thuật. Tính từ: 'surgical'. Ví dụ: 'Surgical techniques have improved dramatically, allowing patients to recover in days rather than weeks.' — Kỹ thuật phẫu thuật đã cải thiện đáng kể, cho phép bệnh nhân hồi phục trong vài ngày thay vì vài tuần. Điểm cuối là 'prevention'. Danh từ không đếm được. Cụm từ: 'disease prevention' — phòng ngừa bệnh, 'prevention is better than cure' — phòng bệnh hơn chữa bệnh. Tính từ: 'preventive' hoặc 'preventative'. Động từ: 'prevent'. Ví dụ: 'Preventive healthcare measures such as regular screening can detect diseases before symptoms appear.' — Các biện pháp y tế phòng ngừa như khám sàng lọc định kỳ có thể phát hiện bệnh trước khi triệu chứng xuất hiện."""

S2_READING = """Modern medicine offers two paths: treatment after illness strikes, or prevention before it begins. Most healthcare systems spend the majority of their budgets on treatment — hospitals, surgery, and prescription drugs — while investing far less in prevention. Yet research consistently shows that prevention saves both lives and money.

Consider nutrition. Poor diet is now the leading risk factor for death globally, contributing to heart disease, diabetes, and certain cancers. A balanced diet rich in fruits, vegetables, and whole grains can prevent many chronic conditions. Similarly, mental health — long ignored by healthcare systems — is now recognized as equally important as physical health. Depression and anxiety affect over 300 million people worldwide, reducing productivity and quality of life.

When prevention fails, epidemics can spread with terrifying speed. The COVID-19 pandemic demonstrated how quickly an epidemic can overwhelm hospitals and disrupt entire societies. Governments that invested in early detection, public health education, and rapid vaccine development fared better than those that relied solely on treatment after infection. The lesson is clear: a healthcare system built on prevention rather than reaction is stronger, cheaper, and saves more lives."""

S3_WELCOME = """Chào mừng bạn đến buổi học thứ ba! Ở hai buổi trước, bạn đã học 12 từ vựng về triệu chứng, chẩn đoán, điều trị và phòng ngừa. Hôm nay, chúng ta sẽ nói về sức khỏe cộng đồng: từ life expectancy — tuổi thọ, đến obesity — béo phì, và well-being — sức khỏe toàn diện. Đây là những từ bạn sẽ gặp rất nhiều trong IELTS Writing Task 2. Cùng học nhé!"""

S3_VOCAB = """Từ đầu tiên là 'life expectancy' — 'tuổi thọ trung bình'. Số năm mà một người được kỳ vọng sẽ sống. Ví dụ: 'Life expectancy in Japan is over 84 years, one of the highest in the world.' — Tuổi thọ trung bình ở Nhật Bản là hơn 84 tuổi, một trong những mức cao nhất thế giới. Tiếp theo là 'healthcare' — 'chăm sóc sức khỏe'. Hệ thống dịch vụ y tế phục vụ cộng đồng. Ví dụ: 'Universal healthcare ensures that every citizen can see a doctor regardless of their income.' — Chăm sóc sức khỏe toàn dân đảm bảo mọi công dân đều có thể khám bác sĩ bất kể thu nhập. 'Obesity' — 'béo phì'. Tình trạng thừa cân nghiêm trọng gây nguy hiểm cho sức khỏe. Ví dụ: 'Childhood obesity has tripled in the past 40 years, largely due to processed food and lack of exercise.' — Béo phì trẻ em đã tăng gấp ba trong 40 năm qua, chủ yếu do thực phẩm chế biến sẵn và thiếu vận động. 'Antibiotic' — 'kháng sinh'. Thuốc dùng để tiêu diệt hoặc ngăn chặn vi khuẩn gây bệnh. Ví dụ: 'The overuse of antibiotics has led to the emergence of drug-resistant bacteria, a major global health threat.' — Lạm dụng kháng sinh đã dẫn đến sự xuất hiện của vi khuẩn kháng thuốc, một mối đe dọa sức khỏe toàn cầu lớn. 'Rehabilitation' — 'phục hồi chức năng'. Quá trình giúp bệnh nhân lấy lại sức khỏe và khả năng sau chấn thương hoặc bệnh tật. Ví dụ: 'After his knee surgery, he spent three months in rehabilitation to regain full mobility.' — Sau phẫu thuật đầu gối, anh ấy dành ba tháng phục hồi chức năng để lấy lại khả năng vận động. Cuối cùng là 'well-being' — 'sức khỏe toàn diện, hạnh phúc'. Trạng thái khỏe mạnh, thoải mái và hài lòng về thể chất lẫn tinh thần. Ví dụ: 'Employers are increasingly investing in programs that support the well-being of their workers.' — Nhà tuyển dụng ngày càng đầu tư vào các chương trình hỗ trợ sức khỏe toàn diện của nhân viên."""

S3_GRAMMAR = """Cùng tìm hiểu ngữ pháp nhé. Điểm đầu tiên là 'life expectancy'. Cụm danh từ không đếm được. Cụm từ: 'average life expectancy' — tuổi thọ trung bình, 'increase life expectancy' — tăng tuổi thọ. Ví dụ: 'Advances in medicine have increased life expectancy by over 30 years since 1900.' — Tiến bộ y học đã tăng tuổi thọ hơn 30 năm kể từ năm 1900. Điểm thứ hai là 'obesity'. Danh từ không đếm được. Tính từ: 'obese'. Cụm từ: 'childhood obesity' — béo phì trẻ em, 'obesity rate' — tỷ lệ béo phì. Lưu ý: 'obese' mạnh hơn 'overweight' — 'overweight' là thừa cân, 'obese' là béo phì nghiêm trọng. Ví dụ: 'The obesity rate in the United States has risen from 15 percent in 1980 to over 40 percent today.' — Tỷ lệ béo phì ở Mỹ đã tăng từ 15 phần trăm năm 1980 lên hơn 40 phần trăm hiện nay. Điểm cuối là 'well-being'. Danh từ không đếm được, luôn viết có gạch nối. Cụm từ: 'physical well-being' — sức khỏe thể chất, 'emotional well-being' — sức khỏe cảm xúc, 'sense of well-being' — cảm giác khỏe mạnh. Ví dụ: 'Regular exercise improves both physical fitness and psychological well-being.' — Tập thể dục đều đặn cải thiện cả thể lực lẫn sức khỏe tâm lý."""

S3_READING = """The health of a nation is measured not just by the quality of its hospitals, but by the well-being of its entire population. Life expectancy — the average number of years a person is expected to live — varies dramatically around the world. In Japan and Switzerland, people live past 84 on average. In parts of sub-Saharan Africa, life expectancy remains below 60. The gap is driven largely by differences in healthcare access, nutrition, and disease prevention.

One of the greatest public health challenges of the 21st century is obesity. Globally, over 650 million adults are classified as obese, and the number continues to rise. Obesity increases the risk of diabetes, heart disease, and certain cancers. At the same time, the overuse of antibiotics has created a new crisis: drug-resistant bacteria that no longer respond to standard treatment. The World Health Organization warns that antibiotic resistance could cause 10 million deaths per year by 2050.

On a more hopeful note, rehabilitation programs are helping millions of people recover from injuries, strokes, and surgeries. Physical therapy, occupational therapy, and psychological support work together to restore patients' independence and quality of life. The most effective healthcare systems recognize that well-being is not simply the absence of disease — it is a state of complete physical, mental, and social health that allows people to live full and productive lives."""

S4_REVIEW_INTRO = """Chúc mừng bạn đã học xong toàn bộ 18 từ vựng về sức khỏe và y tế! Từ symptom và diagnosis — nhận biết bệnh tật, đến treatment và chronic — điều trị và bệnh mãn tính, qua immune system và vaccine — hệ thống phòng thủ của cơ thể, đến prescription và surgery — can thiệp y tế, qua epidemic và nutrition — dịch bệnh và dinh dưỡng, đến mental health và prevention — sức khỏe tâm thần và phòng ngừa, và cuối cùng là life expectancy, healthcare, obesity, antibiotic, rehabilitation, và well-being — sức khỏe cộng đồng. Hôm nay là buổi ôn tập toàn bộ!"""

FULL_READING = """Every year, millions of people visit their doctors because of symptoms they cannot explain — persistent headaches, unusual fatigue, or sudden weight loss. These symptoms are the body's way of signaling that something is wrong. The process of diagnosis begins when a doctor listens to the patient, examines the body, and orders tests. An accurate diagnosis is essential because it determines the treatment plan. For many conditions, treatment is straightforward. But chronic diseases — conditions that last for months or years — present a much greater challenge. Diabetes, asthma, and heart disease require ongoing management rather than a simple cure. The immune system plays a central role in how the body responds to illness, destroying harmful bacteria and viruses before they cause serious damage. Vaccines work by training the immune system to recognize specific threats, and their development against smallpox, polio, and measles has saved hundreds of millions of lives.

Modern medicine offers two paths: treatment after illness strikes, or prevention before it begins. Most healthcare systems spend the majority of their budgets on hospitals, surgery, and prescription drugs, while investing far less in prevention. Yet research consistently shows that prevention saves both lives and money. Poor nutrition is now the leading risk factor for death globally, contributing to heart disease, diabetes, and certain cancers. Mental health — long ignored by healthcare systems — is now recognized as equally important as physical health, with depression and anxiety affecting over 300 million people worldwide. When prevention fails, epidemics can spread with terrifying speed, as the COVID-19 pandemic demonstrated. Governments that invested in early detection and rapid vaccine development fared better than those that relied solely on treatment after infection.

The health of a nation is measured not just by the quality of its hospitals, but by the well-being of its entire population. Life expectancy varies dramatically around the world — over 84 years in Japan, below 60 in parts of sub-Saharan Africa — driven largely by differences in healthcare access and disease prevention. One of the greatest public health challenges is obesity, with over 650 million adults classified as obese globally. At the same time, the overuse of antibiotics has created drug-resistant bacteria that no longer respond to standard treatment. On a more hopeful note, rehabilitation programs are helping millions recover from injuries and surgeries through physical therapy and psychological support. The most effective healthcare systems recognize that well-being is not simply the absence of disease — it is a state of complete physical, mental, and social health that allows people to live full and productive lives."""

S5_INTRO = """Chào mừng bạn đến buổi học cuối cùng! Bạn đã học 18 từ vựng, ôn tập kỹ lưỡng, và đọc ba đoạn văn ngắn. Bây giờ là lúc đọc bài viết hoàn chỉnh — một bài đọc phong cách IELTS Academic về sức khỏe và y tế toàn cầu. Khi đọc, hãy chú ý cách 18 từ vựng xuất hiện tự nhiên trong ngữ cảnh. Chúc bạn đọc vui!"""

FAREWELL = """Chúc mừng bạn đã hoàn thành bài học 'Health & Medicine — Sức Khỏe: Hiểu Cơ Thể, Hiểu Cuộc Sống'! Cùng ôn lại 18 từ vựng nhé.

'Symptom' — triệu chứng. Ví dụ: 'Recognizing early symptoms of a stroke — sudden numbness, confusion, difficulty speaking — can save a person's life.'

'Diagnosis' — chẩn đoán. Ví dụ: 'A correct diagnosis depends on honest communication between the patient and the doctor.'

'Treatment' — điều trị. Ví dụ: 'New cancer treatments using immunotherapy have shown remarkable results in clinical trials.'

'Chronic' — mãn tính. Ví dụ: 'Managing chronic pain requires a combination of medication, physical therapy, and lifestyle changes.'

'Immune system' — hệ miễn dịch. Ví dụ: 'Stress and lack of sleep can weaken the immune system, making you more vulnerable to infections.'

'Vaccine' — vắc-xin. Ví dụ: 'The measles vaccine alone prevents an estimated 2.6 million deaths every year worldwide.'

'Prescription' — đơn thuốc. Ví dụ: 'In many countries, antibiotics require a prescription to prevent misuse and resistance.'

'Surgery' — phẫu thuật. Ví dụ: 'Minimally invasive surgery allows patients to leave the hospital the same day.'

'Epidemic' — dịch bệnh. Ví dụ: 'The cholera epidemic spread rapidly through communities without access to clean drinking water.'

'Nutrition' — dinh dưỡng. Ví dụ: 'School nutrition programs ensure that children from low-income families receive at least one healthy meal per day.'

'Mental health' — sức khỏe tâm thần. Ví dụ: 'Talking openly about mental health reduces stigma and encourages people to seek help.'

'Prevention' — phòng ngừa. Ví dụ: 'Handwashing is one of the simplest and most effective forms of disease prevention.'

'Life expectancy' — tuổi thọ trung bình. Ví dụ: 'Access to clean water and basic healthcare has doubled life expectancy in many developing countries over the past century.'

'Healthcare' — chăm sóc sức khỏe. Ví dụ: 'Countries that spend more on primary healthcare tend to have healthier populations and lower hospital costs.'

'Obesity' — béo phì. Ví dụ: 'Taxing sugary drinks has been shown to reduce obesity rates in countries like Mexico and the UK.'

'Antibiotic' — kháng sinh. Ví dụ: 'Taking antibiotics for a viral infection like the common cold is ineffective and contributes to resistance.'

'Rehabilitation' — phục hồi chức năng. Ví dụ: 'Cardiac rehabilitation programs help heart attack survivors regain strength and confidence.'

'Well-being' — sức khỏe toàn diện. Ví dụ: 'A sense of community and belonging is essential for emotional well-being.'

Bạn đã nắm vững 18 từ vựng học thuật về sức khỏe và y tế — chủ đề bạn sẽ gặp lại nhiều lần trong IELTS Academic. Cảm ơn bạn đã đồng hành, và hẹn gặp lại ở bài học tiếp theo!"""

S1_WRITING_ITEMS = [
    {"targetVocab": "symptom", "prompt": "Sử dụng từ 'symptom' trong một câu về dấu hiệu bệnh tật. Example: The most common symptoms of COVID-19 include cough, fever, and loss of taste or smell."},
    {"targetVocab": "diagnosis", "prompt": "Sử dụng từ 'diagnosis' trong một câu về chẩn đoán bệnh. Example: Advances in technology have made the diagnosis of rare diseases faster and more accurate."},
    {"targetVocab": "treatment", "prompt": "Sử dụng từ 'treatment' trong một câu về điều trị. Example: The treatment for depression often combines medication with cognitive behavioral therapy."},
    {"targetVocab": "chronic", "prompt": "Sử dụng từ 'chronic' trong một câu về bệnh mãn tính. Example: Chronic stress can lead to serious health problems including high blood pressure and weakened immunity."},
    {"targetVocab": "immune system", "prompt": "Sử dụng từ 'immune system' trong một câu về hệ miễn dịch. Example: Eating a balanced diet with plenty of vitamins helps strengthen the immune system."},
    {"targetVocab": "vaccine", "prompt": "Sử dụng từ 'vaccine' trong một câu về vắc-xin. Example: Scientists developed an effective vaccine against COVID-19 in less than one year, a historic achievement."},
]

S2_WRITING_ITEMS = [
    {"targetVocab": "prescription", "prompt": "Sử dụng từ 'prescription' trong một câu về đơn thuốc. Example: The pharmacist refused to fill the prescription because it had expired three months ago."},
    {"targetVocab": "surgery", "prompt": "Sử dụng từ 'surgery' trong một câu về phẫu thuật. Example: Robotic surgery allows doctors to perform complex operations with greater precision and smaller incisions."},
    {"targetVocab": "epidemic", "prompt": "Sử dụng từ 'epidemic' trong một câu về dịch bệnh. Example: Health officials declared an epidemic after the number of flu cases doubled in just two weeks."},
    {"targetVocab": "nutrition", "prompt": "Sử dụng từ 'nutrition' trong một câu về dinh dưỡng. Example: Proper nutrition during pregnancy is critical for the healthy development of the baby."},
    {"targetVocab": "mental health", "prompt": "Sử dụng từ 'mental health' trong một câu về sức khỏe tâm thần. Example: Many universities now offer free mental health counseling to help students cope with academic pressure."},
    {"targetVocab": "prevention", "prompt": "Sử dụng từ 'prevention' trong một câu về phòng ngừa bệnh. Example: Investing in disease prevention through public education campaigns is more effective than treating patients after they become ill."},
]

S3_WRITING_ITEMS = [
    {"targetVocab": "life expectancy", "prompt": "Sử dụng từ 'life expectancy' trong một câu về tuổi thọ. Example: Improvements in sanitation and nutrition have raised life expectancy in developing countries by over 20 years."},
    {"targetVocab": "healthcare", "prompt": "Sử dụng từ 'healthcare' trong một câu về hệ thống y tế. Example: Many people in rural areas lack access to basic healthcare services such as clinics and trained doctors."},
    {"targetVocab": "obesity", "prompt": "Sử dụng từ 'obesity' trong một câu về béo phì. Example: The government launched a campaign to fight childhood obesity by promoting healthy school lunches and daily exercise."},
    {"targetVocab": "antibiotic", "prompt": "Sử dụng từ 'antibiotic' trong một câu về kháng sinh. Example: Doctors warn that prescribing antibiotics unnecessarily is creating dangerous drug-resistant bacteria."},
    {"targetVocab": "rehabilitation", "prompt": "Sử dụng từ 'rehabilitation' trong một câu về phục hồi chức năng. Example: The rehabilitation center provides physical therapy and emotional support for patients recovering from serious accidents."},
    {"targetVocab": "well-being", "prompt": "Sử dụng từ 'well-being' trong một câu về sức khỏe toàn diện. Example: Companies that prioritize employee well-being through flexible hours and wellness programs see higher productivity."},
]

# ============================================================
# BUILD CURRICULUM JSON (same structure as curriculum 1)
# ============================================================

def make_learning_session(title, words, welcome, vocab, grammar, reading, writing_items):
    return {
        "title": title,
        "activities": [
            {"activityType": "introAudio", "title": "Giới thiệu bài học",
             "description": "Nghe giới thiệu về chủ đề buổi học",
             "practiceMinutes": "1", "data": {"text": welcome, "audioSpeed": 0.01}},
            {"activityType": "introAudio", "title": "Giới thiệu từ vựng",
             "description": "Nghe giới thiệu về các từ vựng trong bài và cách dùng",
             "practiceMinutes": "3", "data": {"text": vocab, "audioSpeed": 0.01}},
            {"activityType": "viewFlashcards", "title": f"Từ vựng: Health",
             "description": f"Học các từ: {', '.join(words)}",
             "practiceMinutes": "6", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "speakFlashcards", "title": f"Tập nói từ vựng: Health",
             "description": f"Tập nói các từ: {', '.join(words)}",
             "practiceMinutes": "6", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel1", "title": f"Bài tập nhận biết: Health",
             "description": "Chọn nghĩa đúng cho các từ vựng vừa học",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel2", "title": f"Bài tập nhớ lại chủ động: Health",
             "description": "Điền từ thích hợp vào chỗ trống mà không có gợi ý",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel3", "title": f"Bài tập hiểu sâu: Health",
             "description": "Kiểm tra khả năng hiểu và vận dụng từ vựng trong ngữ cảnh",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "introAudio", "title": "Giải thích ngữ pháp",
             "description": "Nghe giải thích các điểm ngữ pháp và cách dùng từ trong ngữ cảnh",
             "practiceMinutes": "3", "data": {"text": grammar, "audioSpeed": 0.01}},
            {"activityType": "reading", "title": "Đọc ngắn: Health",
             "description": reading[:80],
             "practiceMinutes": "5", "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "speakReading", "title": "Luyện nói theo: Health",
             "description": "Tập phát âm đoạn văn bằng cách lặp lại",
             "practiceMinutes": "5", "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "readAlong", "title": "Nghe bài đọc: Health",
             "description": "Nghe nội dung bài đọc ngắn",
             "practiceMinutes": "3", "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "writingSentence", "title": "Viết câu với từ vựng mục tiêu",
             "description": f"Viết câu tiếng Anh sử dụng từ vựng: {', '.join(words)}",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": 0.01, "items": writing_items}},
        ]
    }

content = {
    "title": TITLE,
    "description": DESC,
    "preview": {"text": PREVIEW},
    "learningSessions": [
        make_learning_session("Buổi 1: Triệu chứng & Chẩn đoán", W1, S1_WELCOME, S1_VOCAB, S1_GRAMMAR, S1_READING, S1_WRITING_ITEMS),
        make_learning_session("Buổi 2: Điều trị & Phòng ngừa", W2, S2_WELCOME, S2_VOCAB, S2_GRAMMAR, S2_READING, S2_WRITING_ITEMS),
        make_learning_session("Buổi 3: Sức khỏe cộng đồng", W3, S3_WELCOME, S3_VOCAB, S3_GRAMMAR, S3_READING, S3_WRITING_ITEMS),
        {"title": "Buổi 4: Ôn tập toàn bộ", "activities": [
            {"activityType": "introAudio", "title": "Dẫn nhập ôn tập",
             "description": "Nghe hướng dẫn ôn tập lại toàn bộ từ vựng",
             "practiceMinutes": "1", "data": {"text": S4_REVIEW_INTRO, "audioSpeed": 0.01}},
            {"activityType": "viewFlashcards", "title": "Ôn tập tất cả từ vựng",
             "description": "Xem lại flashcards cho 18 từ vựng",
             "practiceMinutes": "6", "data": {"vocabList": ALL, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel1", "title": "Kiểm tra nhanh: Nhận biết",
             "description": "Bài tập trắc nghiệm nhanh cho toàn bộ 18 từ",
             "practiceMinutes": "10", "data": {"vocabList": ALL, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel2", "title": "Kiểm tra sâu: Nhớ lại",
             "description": "Ghi nhớ chủ động các từ vựng toàn bộ khóa học",
             "practiceMinutes": "10", "data": {"vocabList": ALL, "audioSpeed": -0.1}},
        ]},
        {"title": "Buổi 5: Đọc trọn vẹn", "activities": [
            {"activityType": "introAudio", "title": "Dẫn nhập bài đọc cuối",
             "description": "Lời dẫn cho bài đọc tổng hợp",
             "practiceMinutes": "1", "data": {"text": S5_INTRO, "audioSpeed": 0.01}},
            {"activityType": "reading", "title": "Đọc hiểu: Sức Khỏe Toàn Cầu",
             "description": "Đọc toàn bộ bài viết hoàn chỉnh có chứa 18 từ vựng đã học",
             "practiceMinutes": "15", "data": {"text": FULL_READING, "audioSpeed": -0.1}},
            {"activityType": "speakReading", "title": "Luyện nói theo: Sức Khỏe Toàn Cầu",
             "description": "Phát âm toàn bộ bài viết hoàn chỉnh",
             "practiceMinutes": "15", "data": {"text": FULL_READING, "audioSpeed": -0.1}},
            {"activityType": "readAlong", "title": "Nghe bài đọc tổng hợp",
             "description": "Nghe toàn bộ bài viết hoàn chỉnh",
             "practiceMinutes": "3", "data": {"text": FULL_READING, "audioSpeed": -0.1}},
            {"activityType": "introAudio", "title": "Tổng kết & Chúc mừng hoàn thành",
             "description": "Ôn lại 18 từ vựng và lời chào tạm biệt",
             "practiceMinutes": "4", "data": {"text": FAREWELL, "audioSpeed": 0.01}},
        ]},
    ]
}

content = strip(content)

if __name__ == "__main__":
    print(f"Creating: {TITLE}")
    result = api("curriculum/create", {
        "language": "en", "userLanguage": "vi",
        "content": json.dumps(content),
    })
    cid = result["id"]
    print(f"Created curriculum: {cid}")
    api("curriculum-series/addCurriculum", {"curriculumSeriesId": SERIES_ID, "curriculumId": cid})
    print(f"Added to series {SERIES_ID}")
    api("curriculum/setDisplayOrder", {"id": cid, "displayOrder": DISPLAY_ORDER})
    print(f"Set displayOrder={DISPLAY_ORDER}")
    print(f"\nDone! Curriculum ID: {cid}")
