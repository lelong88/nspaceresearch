#!/usr/bin/env python3
"""
IELTS Academic Vocabulary — Curriculum 2: Urbanization & City Life
Series: Luyện Thi IELTS: Từ Vựng Học Thuật
vi-en | intermediate | 18 words | 5 sessions
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API = "https://helloapi.step.is"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
SERIES_ID = "__SERIES_ID__"  # Replace after running create_ielts_vi_series.py
DISPLAY_ORDER = 2

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

W1 = ["urbanization", "infrastructure", "congestion", "suburb", "population density", "migrate"]
W2 = ["affordable", "commute", "pollution", "zoning", "renovation", "municipal"]
W3 = ["sustainable", "gentrification", "pedestrian", "public transit", "slum", "metropolitan"]
ALL = W1 + W2 + W3

TITLE = "Urbanization & City Life – Đô Thị Hóa: Khi Thành Phố Không Ngừng Lớn"

DESC = """THÀNH PHỐ CỦA BẠN ĐANG "NUỐT CHỬNG" NÔNG THÔN — BẠN CÓ NHẬN RA KHÔNG?

Mỗi tuần, hơn 1 triệu người trên thế giới chuyển từ nông thôn ra thành phố. Đường phố tắc nghẽn, giá nhà tăng vọt, và không khí ngày càng ô nhiễm — nhưng dòng người vẫn đổ về.

Tại sao? Vì thành phố hứa hẹn cơ hội — việc làm, giáo dục, y tế. Nhưng cái giá phải trả là gì khi cơ sở hạ tầng không theo kịp tốc độ tăng dân số?

Khám phá hiện tượng đô thị hóa — từ khu ổ chuột đến khu phố sang trọng hóa — và tại sao hiểu về thành phố là hiểu về tương lai.

Học 18 từ vựng học thuật về đô thị giúp bạn vừa mở rộng kiến thức, vừa sẵn sàng cho bài thi IELTS Academic."""

PREVIEW = """Hơn một nửa dân số thế giới hiện sống ở thành phố — và con số này sẽ đạt 70 phần trăm vào năm 2050. Bài học này đưa bạn vào thế giới đô thị hóa qua 18 từ vựng thiết yếu cho IELTS Academic: từ 'urbanization' (đô thị hóa) và 'infrastructure' (cơ sở hạ tầng), đến 'congestion' (tắc nghẽn) và 'population density' (mật độ dân số), qua 'affordable' (giá cả phải chăng) và 'pollution' (ô nhiễm), đến 'sustainable' (bền vững) và 'gentrification' (sang trọng hóa khu phố). Qua ba bài đọc phong cách IELTS Academic, bạn sẽ hiểu tại sao thành phố vừa là giải pháp vừa là thách thức lớn nhất của thế kỷ 21."""

S1_WELCOME = """Chào bạn, chào mừng đến với bài học thứ hai trong chuỗi Luyện Thi IELTS! Chủ đề hôm nay là đô thị hóa và cuộc sống thành phố — một chủ đề cực kỳ phổ biến trong IELTS Academic. Bạn sẽ gặp chủ đề này trong Reading, Writing Task 2, và cả Speaking Part 3. Trong buổi đầu tiên, chúng ta sẽ học 6 từ vựng nền tảng: urbanization, infrastructure, congestion, suburb, population density, và migrate. Cùng bắt đầu nhé!"""

S1_VOCAB = """Từ đầu tiên là 'urbanization' — 'đô thị hóa'. Quá trình ngày càng nhiều người chuyển đến sống ở thành phố. Ví dụ: 'Rapid urbanization in developing countries has created both opportunities and challenges.' — Đô thị hóa nhanh chóng ở các nước đang phát triển đã tạo ra cả cơ hội lẫn thách thức. Tiếp theo là 'infrastructure' — 'cơ sở hạ tầng'. Hệ thống đường sá, cầu cống, điện nước, viễn thông phục vụ một khu vực. Ví dụ: 'The city needs to invest heavily in infrastructure to support its growing population.' — Thành phố cần đầu tư mạnh vào cơ sở hạ tầng để hỗ trợ dân số đang tăng. 'Congestion' — 'tắc nghẽn'. Tình trạng quá đông đúc, đặc biệt trên đường phố. Ví dụ: 'Traffic congestion costs the average commuter two hours per day in major cities.' — Tắc nghẽn giao thông khiến người đi làm trung bình mất hai giờ mỗi ngày ở các thành phố lớn. 'Suburb' — 'vùng ngoại ô'. Khu dân cư ở rìa thành phố, thường yên tĩnh hơn trung tâm. Ví dụ: 'Many families move to the suburbs to find larger homes and better schools.' — Nhiều gia đình chuyển ra ngoại ô để tìm nhà rộng hơn và trường tốt hơn. 'Population density' — 'mật độ dân số'. Số người sống trên mỗi đơn vị diện tích. Ví dụ: 'Tokyo has one of the highest population densities in the world.' — Tokyo có mật độ dân số cao nhất thế giới. Cuối cùng là 'migrate' — 'di cư'. Chuyển từ nơi này đến nơi khác để sống hoặc làm việc. Ví dụ: 'Millions of people migrate from rural areas to cities every year in search of better jobs.' — Hàng triệu người di cư từ nông thôn ra thành phố mỗi năm để tìm việc tốt hơn."""

S1_GRAMMAR = """Cùng tìm hiểu ngữ pháp nhé. Điểm đầu tiên là 'urbanization'. Danh từ không đếm được. Cụm từ: 'rapid urbanization' — đô thị hóa nhanh, 'rate of urbanization' — tốc độ đô thị hóa. Động từ gốc: 'urbanize'. Tính từ: 'urban' (đối lập: 'rural'). Ví dụ: 'The urbanization of coastal areas has increased flood risk.' — Đô thị hóa vùng ven biển đã tăng nguy cơ lũ lụt. Điểm thứ hai là 'infrastructure'. Danh từ không đếm được. Cụm từ: 'transport infrastructure' — hạ tầng giao thông, 'invest in infrastructure' — đầu tư vào hạ tầng. Ví dụ: 'Poor infrastructure makes it difficult for businesses to operate efficiently.' — Hạ tầng kém khiến doanh nghiệp khó hoạt động hiệu quả. Điểm cuối là 'migrate'. Động từ. Danh từ: 'migration' — sự di cư, 'migrant' — người di cư. Cụm từ: 'migrate to' + nơi đến, 'migrate from' + nơi đi. Ví dụ: 'Rural-to-urban migration is the main driver of city growth in Africa.' — Di cư từ nông thôn ra thành thị là động lực chính của tăng trưởng thành phố ở châu Phi."""

S1_READING = """More than half of the world's population now lives in cities, and this number continues to grow. Urbanization — the movement of people from rural areas to urban centers — is one of the defining trends of the 21st century. In 1950, only 30 percent of people lived in cities. By 2050, that figure is expected to reach 70 percent. People migrate to cities for many reasons: better jobs, higher wages, access to education, and improved healthcare. But rapid urbanization creates serious challenges.

As population density increases, cities struggle to provide adequate infrastructure — roads, water systems, electricity, and public services. Traffic congestion becomes a daily reality for millions of commuters. In cities like Jakarta, Manila, and São Paulo, workers spend three to four hours per day stuck in traffic. The suburbs expand outward as people search for affordable housing, but this sprawl creates new problems: longer commutes, loss of farmland, and increased energy consumption. The question facing every growing city is the same: how do you accommodate more people without sacrificing quality of life?"""

S2_WELCOME = """Chào mừng bạn quay lại! Ở buổi trước, chúng ta đã học về urbanization, infrastructure, congestion, suburb, population density, và migrate. Hôm nay, chúng ta sẽ tìm hiểu sâu hơn về cuộc sống đô thị: từ affordable housing — nhà ở giá phải chăng, đến pollution — ô nhiễm, và cách các thành phố quản lý phát triển qua zoning — quy hoạch phân vùng. Cùng học nhé!"""

S2_VOCAB = """Từ đầu tiên là 'affordable' — 'giá cả phải chăng'. Có giá mà người bình thường có thể chi trả được. Ví dụ: 'The lack of affordable housing is the biggest problem facing young people in major cities.' — Thiếu nhà ở giá phải chăng là vấn đề lớn nhất mà người trẻ đối mặt ở các thành phố lớn. Tiếp theo là 'commute' — 'đi lại hàng ngày (đi làm/đi học)'. Hành trình đi từ nhà đến nơi làm việc và ngược lại. Ví dụ: 'Her daily commute takes 90 minutes each way by bus and train.' — Hành trình đi làm hàng ngày của cô ấy mất 90 phút mỗi chiều bằng xe buýt và tàu. 'Pollution' — 'ô nhiễm'. Sự nhiễm bẩn môi trường bởi các chất có hại. Ví dụ: 'Air pollution in Delhi is so severe that schools sometimes close for days.' — Ô nhiễm không khí ở Delhi nghiêm trọng đến mức trường học đôi khi đóng cửa nhiều ngày. 'Zoning' — 'quy hoạch phân vùng'. Luật quy định khu vực nào được xây nhà ở, thương mại, hay công nghiệp. Ví dụ: 'Strict zoning laws prevent factories from being built near residential areas.' — Luật phân vùng nghiêm ngặt ngăn xây nhà máy gần khu dân cư. 'Renovation' — 'sự cải tạo, tu sửa'. Quá trình sửa chữa và nâng cấp tòa nhà cũ. Ví dụ: 'The renovation of the old train station transformed it into a modern shopping center.' — Việc cải tạo nhà ga cũ đã biến nó thành trung tâm mua sắm hiện đại. Cuối cùng là 'municipal' — 'thuộc thành phố, thuộc chính quyền địa phương'. Liên quan đến chính quyền hoặc dịch vụ của thành phố. Ví dụ: 'Municipal governments are responsible for waste collection, road maintenance, and public parks.' — Chính quyền thành phố chịu trách nhiệm thu gom rác, bảo trì đường, và công viên công cộng."""

S2_GRAMMAR = """Cùng tìm hiểu ngữ pháp nhé. Điểm đầu tiên là 'affordable'. Tính từ, đối nghĩa: 'unaffordable'. Cụm từ: 'affordable housing' — nhà ở giá phải chăng, 'affordable prices' — giá cả phải chăng. Danh từ: 'affordability'. Ví dụ: 'Housing affordability has become a political issue in almost every major city.' — Khả năng chi trả nhà ở đã trở thành vấn đề chính trị ở hầu hết thành phố lớn. Điểm thứ hai là 'commute'. Từ này vừa là danh từ vừa là động từ. Danh từ: 'a long commute' — hành trình dài. Động từ: 'commute to work' — đi làm. Người: 'commuter' — người đi làm hàng ngày. Ví dụ: 'Commuters in London spend an average of 74 minutes per day traveling to and from work.' — Người đi làm ở London trung bình mất 74 phút mỗi ngày di chuyển. Điểm cuối là 'municipal'. Tính từ, luôn đứng trước danh từ. Cụm từ: 'municipal government' — chính quyền thành phố, 'municipal services' — dịch vụ công. Danh từ: 'municipality' — đơn vị hành chính thành phố. Ví dụ: 'The municipality approved a new budget for public transportation improvements.' — Chính quyền thành phố phê duyệt ngân sách mới cho cải thiện giao thông công cộng."""

S2_READING = """Life in a modern city is shaped by decisions that most residents never think about. Zoning laws determine where homes, shops, and factories can be built. Municipal governments manage everything from garbage collection to street lighting. These invisible systems keep cities functioning, but they also create tensions.

The most pressing issue in many cities is affordable housing. As urban populations grow, demand for housing increases faster than supply. Rents rise, and low-income families are pushed to the edges of the city, where commute times are longer and public services are fewer. In some cities, the renovation of old neighborhoods attracts wealthier residents, driving up prices and displacing long-time communities.

Meanwhile, pollution remains a constant threat to urban health. Vehicle emissions, industrial waste, and construction dust combine to create air quality problems that affect millions. Cities like Beijing and New Delhi regularly exceed safe pollution levels, forcing residents to wear masks and limit outdoor activities. The challenge for municipal planners is clear: how to build cities that are both livable and affordable, where the commute is short, the air is clean, and every family can find a decent home."""

S3_WELCOME = """Chào mừng bạn đến buổi học thứ ba! Ở hai buổi trước, bạn đã học 12 từ vựng về đô thị hóa và cuộc sống thành phố. Hôm nay, chúng ta sẽ nói về tương lai đô thị: từ sustainable development — phát triển bền vững, đến gentrification — hiện tượng sang trọng hóa khu phố, và public transit — giao thông công cộng. Đây là những từ bạn sẽ gặp rất nhiều trong IELTS Writing Task 2. Cùng học nhé!"""

S3_VOCAB = """Từ đầu tiên là 'sustainable' — 'bền vững'. Có thể duy trì lâu dài mà không gây hại cho môi trường. Ví dụ: 'Sustainable city planning includes green spaces, bike lanes, and energy-efficient buildings.' — Quy hoạch thành phố bền vững bao gồm không gian xanh, làn xe đạp, và tòa nhà tiết kiệm năng lượng. Tiếp theo là 'gentrification' — 'sang trọng hóa khu phố'. Quá trình khu phố nghèo được cải tạo và trở nên đắt đỏ, đẩy cư dân cũ đi. Ví dụ: 'Gentrification has transformed the old warehouse district into a trendy area with expensive cafes and boutiques.' — Sang trọng hóa đã biến khu nhà kho cũ thành khu vực thời thượng với quán cà phê và cửa hàng đắt tiền. 'Pedestrian' — 'người đi bộ'. Người di chuyển bằng cách đi bộ. Ví dụ: 'The city center was redesigned as a pedestrian zone where cars are not allowed.' — Trung tâm thành phố được thiết kế lại thành khu vực dành cho người đi bộ, không cho xe hơi. 'Public transit' — 'giao thông công cộng'. Hệ thống xe buýt, tàu điện, metro phục vụ công chúng. Ví dụ: 'Investing in public transit reduces traffic congestion and air pollution.' — Đầu tư vào giao thông công cộng giảm tắc nghẽn và ô nhiễm không khí. 'Slum' — 'khu ổ chuột'. Khu dân cư nghèo, đông đúc, thiếu tiện nghi cơ bản. Ví dụ: 'Over one billion people worldwide live in slums without access to clean water or sanitation.' — Hơn một tỷ người trên thế giới sống trong khu ổ chuột không có nước sạch hay vệ sinh. Cuối cùng là 'metropolitan' — 'thuộc đô thị lớn'. Liên quan đến thành phố lớn và vùng xung quanh. Ví dụ: 'The Tokyo metropolitan area is home to over 37 million people.' — Vùng đô thị Tokyo có hơn 37 triệu dân."""

S3_GRAMMAR = """Cùng tìm hiểu ngữ pháp nhé. Điểm đầu tiên là 'sustainable'. Tính từ. Danh từ: 'sustainability'. Cụm từ: 'sustainable development' — phát triển bền vững, 'sustainable energy' — năng lượng bền vững. Đối nghĩa: 'unsustainable'. Ví dụ: 'The current rate of resource consumption is unsustainable and must change.' — Tốc độ tiêu thụ tài nguyên hiện tại là không bền vững và phải thay đổi. Điểm thứ hai là 'gentrification'. Danh từ không đếm được. Động từ: 'gentrify'. Cụm từ: 'urban gentrification' — sang trọng hóa đô thị. Đây là từ thường xuất hiện trong IELTS Writing Task 2 về housing và urban development. Ví dụ: 'Critics argue that gentrification benefits newcomers while harming existing residents.' — Người phê bình cho rằng sang trọng hóa có lợi cho người mới đến nhưng gây hại cho cư dân hiện tại. Điểm cuối là 'pedestrian'. Vừa là danh từ vừa là tính từ. Danh từ: 'a pedestrian' — người đi bộ. Tính từ: 'pedestrian zone' — khu vực đi bộ, 'pedestrian crossing' — vạch sang đường. Ví dụ: 'Pedestrian-friendly streets encourage walking and reduce dependence on cars.' — Đường phố thân thiện với người đi bộ khuyến khích đi bộ và giảm phụ thuộc vào xe hơi."""

S3_READING = """The future of cities depends on one word: sustainable. As urban populations grow, cities must find ways to provide housing, transportation, and services without destroying the environment. Some cities are leading the way. Copenhagen has invested heavily in bike lanes and public transit, making it possible for most residents to live without a car. Singapore has created vertical gardens and rooftop farms to bring nature into the metropolitan landscape.

But sustainability is not just about the environment — it is also about people. Gentrification is a growing concern in cities worldwide. When old neighborhoods are renovated and made attractive to wealthier residents, property values rise and long-time residents — often low-income families — are forced to move. Some end up in slums on the city's outskirts, where infrastructure is poor and opportunities are limited.

The most successful cities are those that balance growth with equity. They create pedestrian-friendly streets that encourage walking and cycling. They invest in public transit systems that connect suburbs to city centers quickly and affordably. They build mixed-income housing so that rich and poor live side by side. The metropolitan areas of the future will not be defined by their size, but by their ability to provide a good quality of life for everyone — not just those who can afford it."""

S4_REVIEW_INTRO = """Chúc mừng bạn đã học xong toàn bộ 18 từ vựng về đô thị hóa! Từ urbanization và infrastructure — nền tảng của mọi thành phố, đến congestion và population density — thách thức của tăng trưởng, qua suburb và migrate — dòng chảy dân số, đến affordable housing và commute — cuộc sống hàng ngày, qua pollution và zoning — quản lý đô thị, đến renovation và municipal — chính quyền địa phương, và cuối cùng là sustainable, gentrification, pedestrian, public transit, slum, và metropolitan — tương lai đô thị. Hôm nay là buổi ôn tập toàn bộ!"""

FULL_READING = """More than half of the world's population now lives in cities, and this number continues to grow. Urbanization — the movement of people from rural areas to urban centers — is one of the defining trends of the 21st century. In 1950, only 30 percent of people lived in cities. By 2050, that figure is expected to reach 70 percent. People migrate to cities for many reasons: better jobs, higher wages, access to education, and improved healthcare. But rapid urbanization creates serious challenges. As population density increases, cities struggle to provide adequate infrastructure — roads, water systems, electricity, and public services. Traffic congestion becomes a daily reality for millions of commuters. The suburbs expand outward as people search for affordable housing, but this sprawl creates new problems: longer commutes, loss of farmland, and increased energy consumption.

Life in a modern city is shaped by decisions that most residents never think about. Zoning laws determine where homes, shops, and factories can be built. Municipal governments manage everything from garbage collection to street lighting. The most pressing issue in many cities is affordable housing. As urban populations grow, demand for housing increases faster than supply. Rents rise, and low-income families are pushed to the edges of the city, where commute times are longer. The renovation of old neighborhoods attracts wealthier residents, driving up prices. Meanwhile, pollution remains a constant threat to urban health — vehicle emissions, industrial waste, and construction dust combine to create air quality problems that affect millions.

The future of cities depends on sustainability. Copenhagen has invested heavily in bike lanes and public transit, making it possible for most residents to live without a car. But gentrification is a growing concern: when old neighborhoods are renovated and made attractive to wealthier residents, long-time residents are forced to move, sometimes ending up in slums on the city's outskirts. The most successful cities create pedestrian-friendly streets, invest in public transit systems that connect suburbs to city centers, and build mixed-income housing. The metropolitan areas of the future will not be defined by their size, but by their ability to provide a good quality of life for everyone."""

S5_INTRO = """Chào mừng bạn đến buổi học cuối cùng! Bạn đã học 18 từ vựng, ôn tập kỹ lưỡng, và đọc ba đoạn văn ngắn. Bây giờ là lúc đọc bài viết hoàn chỉnh — một bài đọc phong cách IELTS Academic về đô thị hóa và cuộc sống thành phố. Khi đọc, hãy chú ý cách 18 từ vựng xuất hiện tự nhiên trong ngữ cảnh. Chúc bạn đọc vui!"""

FAREWELL = """Chúc mừng bạn đã hoàn thành bài học 'Urbanization & City Life — Đô Thị Hóa: Khi Thành Phố Không Ngừng Lớn'! Cùng ôn lại 18 từ vựng nhé.

'Urbanization' — đô thị hóa. Ví dụ: 'Urbanization has accelerated in Africa, with Lagos growing from 1 million to over 15 million people in 50 years.'

'Infrastructure' — cơ sở hạ tầng. Ví dụ: 'Aging infrastructure in many American cities needs billions of dollars in repairs.'

'Congestion' — tắc nghẽn. Ví dụ: 'London introduced a congestion charge to reduce the number of cars entering the city center.'

'Suburb' — ngoại ô. Ví dụ: 'The suburbs offer more space but less access to cultural events and nightlife.'

'Population density' — mật độ dân số. Ví dụ: 'Hong Kong's population density is among the highest in the world at over 6,000 people per square kilometer.'

'Migrate' — di cư. Ví dụ: 'Young professionals migrate to capital cities where salaries are higher and opportunities are greater.'

'Affordable' — giá phải chăng. Ví dụ: 'Building affordable apartments near public transit stations helps low-income workers.'

'Commute' — đi lại hàng ngày. Ví dụ: 'Remote work has eliminated the commute for millions of office workers.'

'Pollution' — ô nhiễm. Ví dụ: 'Switching to electric buses has significantly reduced air pollution in Shenzhen.'

'Zoning' — quy hoạch phân vùng. Ví dụ: 'Mixed-use zoning allows shops and apartments to exist in the same building.'

'Renovation' — cải tạo. Ví dụ: 'The renovation of the waterfront area attracted tourists and created new jobs.'

'Municipal' — thuộc thành phố. Ví dụ: 'Municipal bonds help cities raise money for schools and hospitals.'

'Sustainable' — bền vững. Ví dụ: 'Sustainable architecture uses natural light and recycled materials to reduce energy consumption.'

'Gentrification' — sang trọng hóa. Ví dụ: 'Gentrification often starts with artists moving into cheap neighborhoods, followed by developers.'

'Pedestrian' — người đi bộ. Ví dụ: 'The new pedestrian bridge connects the park to the shopping district safely.'

'Public transit' — giao thông công cộng. Ví dụ: 'Tokyo's public transit system carries over 8 million passengers daily with remarkable punctuality.'

'Slum' — khu ổ chuột. Ví dụ: 'Improving conditions in slums requires investment in water, sanitation, and electricity.'

'Metropolitan' — thuộc đô thị lớn. Ví dụ: 'The Seoul metropolitan area generates nearly half of South Korea's total economic output.'

Bạn đã nắm vững 18 từ vựng học thuật về đô thị hóa — chủ đề bạn sẽ gặp lại nhiều lần trong IELTS Academic. Cảm ơn bạn đã đồng hành, và hẹn gặp lại ở bài học tiếp theo!"""

S1_WRITING_ITEMS = [
    {"targetVocab": "urbanization", "prompt": "Sử dụng từ 'urbanization' trong một câu về sự phát triển thành phố. Example: Urbanization has brought economic growth but also created problems like overcrowding and pollution."},
    {"targetVocab": "infrastructure", "prompt": "Sử dụng từ 'infrastructure' trong một câu về cơ sở hạ tầng. Example: The government plans to spend $50 billion on infrastructure projects including roads, bridges, and railways."},
    {"targetVocab": "congestion", "prompt": "Sử dụng từ 'congestion' trong một câu về giao thông. Example: Traffic congestion during rush hour makes it nearly impossible to cross the city in less than two hours."},
    {"targetVocab": "suburb", "prompt": "Sử dụng từ 'suburb' trong một câu về ngoại ô. Example: The suburb has grown rapidly as young families seek affordable homes with gardens."},
    {"targetVocab": "population density", "prompt": "Sử dụng từ 'population density' trong một câu về dân số. Example: Areas with high population density require more schools, hospitals, and public services."},
    {"targetVocab": "migrate", "prompt": "Sử dụng từ 'migrate' trong một câu về di cư. Example: Many young people migrate to the capital city because there are more job opportunities there."},
]

S2_WRITING_ITEMS = [
    {"targetVocab": "affordable", "prompt": "Sử dụng từ 'affordable' trong một câu về giá cả. Example: The city needs to build more affordable housing so that teachers and nurses can live near their workplaces."},
    {"targetVocab": "commute", "prompt": "Sử dụng từ 'commute' trong một câu về đi lại. Example: A shorter commute gives people more time to spend with their families and on hobbies."},
    {"targetVocab": "pollution", "prompt": "Sử dụng từ 'pollution' trong một câu về ô nhiễm. Example: Water pollution from factories has made the river unsafe for swimming or fishing."},
    {"targetVocab": "zoning", "prompt": "Sử dụng từ 'zoning' trong một câu về quy hoạch. Example: New zoning regulations allow developers to build taller apartment buildings near train stations."},
    {"targetVocab": "renovation", "prompt": "Sử dụng từ 'renovation' trong một câu về cải tạo. Example: The renovation of the historic market brought new life to the neighborhood."},
    {"targetVocab": "municipal", "prompt": "Sử dụng từ 'municipal' trong một câu về chính quyền thành phố. Example: Municipal authorities are responsible for keeping the streets clean and safe."},
]

S3_WRITING_ITEMS = [
    {"targetVocab": "sustainable", "prompt": "Sử dụng từ 'sustainable' trong một câu về phát triển bền vững. Example: Sustainable transportation options like cycling and electric buses help reduce carbon emissions."},
    {"targetVocab": "gentrification", "prompt": "Sử dụng từ 'gentrification' trong một câu về biến đổi khu phố. Example: Gentrification has made the neighborhood more attractive but also more expensive for original residents."},
    {"targetVocab": "pedestrian", "prompt": "Sử dụng từ 'pedestrian' trong một câu về người đi bộ. Example: The city closed the main street to cars and turned it into a pedestrian-only zone."},
    {"targetVocab": "public transit", "prompt": "Sử dụng từ 'public transit' trong một câu về giao thông công cộng. Example: Reliable public transit reduces the need for private cars and helps the environment."},
    {"targetVocab": "slum", "prompt": "Sử dụng từ 'slum' trong một câu về khu ổ chuột. Example: The government launched a program to replace slums with proper housing and clean water systems."},
    {"targetVocab": "metropolitan", "prompt": "Sử dụng từ 'metropolitan' trong một câu về vùng đô thị. Example: The metropolitan area includes the city center and all surrounding towns within a 50-kilometer radius."},
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
            {"activityType": "viewFlashcards", "title": f"Từ vựng: Urbanization",
             "description": f"Học các từ: {', '.join(words)}",
             "practiceMinutes": "6", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "speakFlashcards", "title": f"Tập nói từ vựng: Urbanization",
             "description": f"Tập nói các từ: {', '.join(words)}",
             "practiceMinutes": "6", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel1", "title": f"Bài tập nhận biết: Urbanization",
             "description": "Chọn nghĩa đúng cho các từ vựng vừa học",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel2", "title": f"Bài tập nhớ lại chủ động: Urbanization",
             "description": "Điền từ thích hợp vào chỗ trống mà không có gợi ý",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "vocabLevel3", "title": f"Bài tập hiểu sâu: Urbanization",
             "description": "Kiểm tra khả năng hiểu và vận dụng từ vựng trong ngữ cảnh",
             "practiceMinutes": "10", "data": {"vocabList": words, "audioSpeed": -0.1}},
            {"activityType": "introAudio", "title": "Giải thích ngữ pháp",
             "description": "Nghe giải thích các điểm ngữ pháp và cách dùng từ trong ngữ cảnh",
             "practiceMinutes": "3", "data": {"text": grammar, "audioSpeed": 0.01}},
            {"activityType": "reading", "title": "Đọc ngắn: Urbanization",
             "description": reading[:80],
             "practiceMinutes": "5", "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "speakReading", "title": "Luyện nói theo: Urbanization",
             "description": "Tập phát âm đoạn văn bằng cách lặp lại",
             "practiceMinutes": "5", "data": {"text": reading, "audioSpeed": -0.1}},
            {"activityType": "readAlong", "title": "Nghe bài đọc: Urbanization",
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
        make_learning_session("Buổi 1: Sự bùng nổ đô thị", W1, S1_WELCOME, S1_VOCAB, S1_GRAMMAR, S1_READING, S1_WRITING_ITEMS),
        make_learning_session("Buổi 2: Cuộc sống đô thị", W2, S2_WELCOME, S2_VOCAB, S2_GRAMMAR, S2_READING, S2_WRITING_ITEMS),
        make_learning_session("Buổi 3: Tương lai bền vững", W3, S3_WELCOME, S3_VOCAB, S3_GRAMMAR, S3_READING, S3_WRITING_ITEMS),
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
            {"activityType": "reading", "title": "Đọc hiểu: Đô Thị Hóa Toàn Cầu",
             "description": "Đọc toàn bộ bài viết hoàn chỉnh có chứa 18 từ vựng đã học",
             "practiceMinutes": "15", "data": {"text": FULL_READING, "audioSpeed": -0.1}},
            {"activityType": "speakReading", "title": "Luyện nói theo: Đô Thị Hóa Toàn Cầu",
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
