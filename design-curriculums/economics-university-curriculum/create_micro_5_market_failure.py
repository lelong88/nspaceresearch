"""
Create curriculum: Market Failure – Thất Bại Thị Trường
Series A — Kinh Tế Vi Mô (Microeconomics), curriculum #5
18 words | 5 sessions | surprising_fact tone | practical momentum farewell
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
W1 = ["externality", "subsidy", "public", "free-rider", "commons", "pollution"]
W2 = ["intervention", "tax", "quota", "welfare", "deadweight", "loss"]
W3 = ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Market Failure – Thất Bại Thị Trường",
    "contentTypeTags": [],
    "description": (
        "MỖI NĂM, Ô NHIỄM KHÔNG KHÍ GIẾT CHẾT 7 TRIỆU NGƯỜI TRÊN THẾ GIỚI — VÀ THỊ TRƯỜNG TỰ DO KHÔNG THỂ NGĂN ĐIỀU ĐÓ.\n\n"
        "Bạn đã học về cung cầu, cân bằng thị trường, và bàn tay vô hình. "
        "Nhưng có một sự thật mà sách giáo khoa thường giấu ở chương sau: "
        "thị trường không phải lúc nào cũng hoạt động hoàn hảo. "
        "Khi nhà máy xả khói độc mà không phải trả giá, khi người dân hưởng lợi từ đèn đường "
        "mà không ai chịu đóng tiền, khi công ty bảo hiểm không biết ai đang nói dối — "
        "đó là lúc thị trường thất bại.\n\n"
        "Hãy tưởng tượng thị trường như một chiếc đồng hồ tinh xảo — "
        "phần lớn thời gian nó chạy chính xác, nhưng có những bánh răng bị kẹt "
        "mà chỉ khi bạn hiểu cơ chế bên trong, bạn mới sửa được. "
        "18 từ vựng trong bài học này chính là bộ dụng cụ để bạn mở nắp chiếc đồng hồ ấy.\n\n"
        "Sau khóa học, bạn sẽ đọc được bài phân tích về externality và public goods bằng tiếng Anh, "
        "hiểu vì sao chính phủ đánh thuế ô nhiễm hay trợ cấp giáo dục, "
        "và tự tin tranh luận về market failure trong lớp kinh tế vi mô.\n\n"
        "18 từ — từ externality đến spillover — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy phân tích chính sách, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về thất bại thị trường — "
            "chương quan trọng nhất mà nhiều sinh viên kinh tế bỏ qua. "
            "Bạn sẽ bắt đầu với externality, subsidy, public, free-rider, commons, pollution — "
            "những từ giúp bạn hiểu vì sao thị trường tự do đôi khi gây hại cho xã hội. "
            "Tiếp theo là intervention, tax, quota, welfare, deadweight, loss — "
            "bộ công cụ chính sách mà chính phủ dùng để sửa chữa thất bại thị trường. "
            "Cuối cùng, asymmetry, moral, adverse, regulation, corrective, spillover "
            "đưa bạn vào thế giới thông tin bất cân xứng và hiệu ứng lan tỏa. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu và thảo luận về market failure bằng tiếng Anh — "
            "không cần dừng lại tra từ điển mỗi câu."
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
                    "description": "Chào mừng bạn đến với bài học về thất bại thị trường và ngoại tác.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học cuối cùng trong chuỗi Kinh tế vi mô — "
                            "chủ đề hôm nay là Thất bại thị trường, hay Market Failure trong tiếng Anh. "
                            "Đây là một trong những chương quan trọng nhất vì nó cho thấy giới hạn "
                            "của bàn tay vô hình — khi thị trường tự do không thể phân bổ nguồn lực hiệu quả.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: externality, subsidy, public, free-rider, commons, và pollution. "
                            "Đây là những từ bạn sẽ gặp ngay khi mở chương về market failure trong bất kỳ giáo trình nào.\n\n"
                            "Từ đầu tiên là externality — danh từ — nghĩa là ngoại tác, "
                            "tác động phụ của một hoạt động kinh tế lên bên thứ ba không tham gia giao dịch. "
                            "Ví dụ: 'A factory that dumps waste into a river creates a negative externality "
                            "for the fishing communities downstream.' "
                            "Trong bài đọc, externality là khái niệm trung tâm — "
                            "khi chi phí hoặc lợi ích của một giao dịch rơi vào người ngoài cuộc, "
                            "thị trường không thể tự điều chỉnh.\n\n"
                            "Từ thứ hai là subsidy — danh từ — nghĩa là trợ cấp, "
                            "khoản tiền chính phủ hỗ trợ cho người sản xuất hoặc người tiêu dùng "
                            "để khuyến khích một hoạt động kinh tế. "
                            "Ví dụ: 'The government provides a subsidy for solar panel installation "
                            "to encourage households to switch to clean energy.' "
                            "Trong bài đọc, subsidy là công cụ chính phủ dùng để khắc phục ngoại tác tích cực — "
                            "khi thị trường sản xuất quá ít một thứ có lợi cho xã hội.\n\n"
                            "Từ thứ ba là public — tính từ — trong kinh tế nghĩa là công cộng, "
                            "thuộc về hoặc phục vụ cho toàn bộ cộng đồng. "
                            "Ví dụ: 'National defense is a classic public good because everyone benefits "
                            "from it regardless of whether they pay taxes.' "
                            "Trong bài đọc, public xuất hiện trong cụm public good — "
                            "hàng hóa mà ai cũng được hưởng và không ai bị loại trừ.\n\n"
                            "Từ thứ tư là free-rider — danh từ — nghĩa là người hưởng lợi miễn phí, "
                            "người được hưởng lợi từ hàng hóa hoặc dịch vụ mà không đóng góp chi phí. "
                            "Ví dụ: 'Some residents become free-riders by enjoying the neighborhood park "
                            "without contributing to its maintenance fund.' "
                            "Trong bài đọc, free-rider là vấn đề cốt lõi của hàng hóa công cộng — "
                            "khi mọi người đều muốn hưởng lợi mà không ai muốn trả tiền.\n\n"
                            "Từ thứ năm là commons — danh từ — nghĩa là tài nguyên chung, "
                            "nguồn lực mà ai cũng có quyền sử dụng nhưng không ai sở hữu riêng. "
                            "Ví dụ: 'Overfishing in the ocean is a tragedy of the commons — "
                            "each fisherman takes as much as possible because no one owns the fish.' "
                            "Trong bài đọc, commons mô tả tình huống khi tài nguyên chung bị khai thác quá mức "
                            "vì không có ai chịu trách nhiệm bảo vệ.\n\n"
                            "Từ cuối cùng là pollution — danh từ — nghĩa là ô nhiễm, "
                            "sự làm bẩn môi trường bởi các chất độc hại từ hoạt động kinh tế. "
                            "Ví dụ: 'Air pollution from coal-fired power plants causes respiratory diseases "
                            "in communities living nearby.' "
                            "Trong bài đọc, pollution là ví dụ điển hình nhất của negative externality — "
                            "nhà máy sản xuất hàng hóa nhưng xã hội phải gánh chịu chi phí ô nhiễm.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về ngoại tác và hàng hóa công cộng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ngoại tác và hàng hóa công cộng",
                    "description": "Học 6 từ: externality, subsidy, public, free-rider, commons, pollution",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ngoại tác và hàng hóa công cộng",
                    "description": "Học 6 từ: externality, subsidy, public, free-rider, commons, pollution",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ngoại tác và hàng hóa công cộng",
                    "description": "Học 6 từ: externality, subsidy, public, free-rider, commons, pollution",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ngoại tác và hàng hóa công cộng",
                    "description": "Học 6 từ: externality, subsidy, public, free-rider, commons, pollution",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ngoại tác và hàng hóa công cộng",
                    "description": "Học 6 từ: externality, subsidy, public, free-rider, commons, pollution",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Ngoại tác và hàng hóa công cộng",
                    "description": "Markets are powerful tools for organizing economic activity, but they do not always produce the best outcome for society.",
                    "data": {
                        "text": (
                            "Markets are powerful tools for organizing economic activity, "
                            "but they do not always produce the best outcome for society. "
                            "When a transaction between a buyer and a seller affects a third party "
                            "who is not involved in the deal, economists call this an externality.\n\n"
                            "A negative externality imposes costs on outsiders. "
                            "Pollution is the most common example. "
                            "When a factory produces steel, it also produces smoke and wastewater. "
                            "The factory and its customers benefit from the steel, "
                            "but nearby residents suffer from the pollution without receiving any compensation. "
                            "Because the factory does not pay for the environmental damage it causes, "
                            "it produces more steel than is socially optimal. "
                            "The market price of steel is too low because it does not include the cost of pollution.\n\n"
                            "A positive externality creates benefits for outsiders. "
                            "Education is a good example. When a person gets a university degree, "
                            "they earn a higher salary — that is a private benefit. "
                            "But society also benefits: educated citizens pay more taxes, commit fewer crimes, "
                            "and contribute to innovation. Because these social benefits are not captured "
                            "by the market price of education, the market produces less education than society needs. "
                            "This is why governments often provide a subsidy for education — "
                            "financial support that lowers the cost for students and encourages more people to study.\n\n"
                            "Some goods are so difficult for markets to provide that they are called public goods. "
                            "A public good has two special features: it is non-excludable, meaning you cannot stop "
                            "anyone from using it, and it is non-rivalrous, meaning one person's use does not "
                            "reduce the amount available for others. Street lighting is a classic example. "
                            "Once a street lamp is installed, everyone on the street benefits, "
                            "whether they helped pay for it or not.\n\n"
                            "This creates the free-rider problem. "
                            "A free-rider is someone who enjoys the benefits of a good without paying for it. "
                            "If everyone waits for someone else to pay for the street lamp, "
                            "no one will pay, and the lamp will never be built. "
                            "This is why public goods are usually provided by the government, funded through taxes.\n\n"
                            "A related problem involves the commons — shared resources that anyone can use "
                            "but no one owns. Fisheries, forests, and clean air are examples of the commons. "
                            "Because no single person owns the ocean, each fisherman has an incentive "
                            "to catch as many fish as possible before others do. "
                            "Over time, the resource is depleted. "
                            "This pattern, known as the tragedy of the commons, "
                            "shows how individual self-interest can destroy shared resources "
                            "when there are no rules to limit use."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Ngoại tác và hàng hóa công cộng",
                    "description": "Markets are powerful tools for organizing economic activity, but they do not always produce the best outcome for society.",
                    "data": {
                        "text": (
                            "Markets are powerful tools for organizing economic activity, "
                            "but they do not always produce the best outcome for society. "
                            "When a transaction between a buyer and a seller affects a third party "
                            "who is not involved in the deal, economists call this an externality.\n\n"
                            "A negative externality imposes costs on outsiders. "
                            "Pollution is the most common example. "
                            "When a factory produces steel, it also produces smoke and wastewater. "
                            "The factory and its customers benefit from the steel, "
                            "but nearby residents suffer from the pollution without receiving any compensation. "
                            "Because the factory does not pay for the environmental damage it causes, "
                            "it produces more steel than is socially optimal. "
                            "The market price of steel is too low because it does not include the cost of pollution.\n\n"
                            "A positive externality creates benefits for outsiders. "
                            "Education is a good example. When a person gets a university degree, "
                            "they earn a higher salary — that is a private benefit. "
                            "But society also benefits: educated citizens pay more taxes, commit fewer crimes, "
                            "and contribute to innovation. Because these social benefits are not captured "
                            "by the market price of education, the market produces less education than society needs. "
                            "This is why governments often provide a subsidy for education — "
                            "financial support that lowers the cost for students and encourages more people to study.\n\n"
                            "Some goods are so difficult for markets to provide that they are called public goods. "
                            "A public good has two special features: it is non-excludable, meaning you cannot stop "
                            "anyone from using it, and it is non-rivalrous, meaning one person's use does not "
                            "reduce the amount available for others. Street lighting is a classic example. "
                            "Once a street lamp is installed, everyone on the street benefits, "
                            "whether they helped pay for it or not.\n\n"
                            "This creates the free-rider problem. "
                            "A free-rider is someone who enjoys the benefits of a good without paying for it. "
                            "If everyone waits for someone else to pay for the street lamp, "
                            "no one will pay, and the lamp will never be built. "
                            "This is why public goods are usually provided by the government, funded through taxes.\n\n"
                            "A related problem involves the commons — shared resources that anyone can use "
                            "but no one owns. Fisheries, forests, and clean air are examples of the commons. "
                            "Because no single person owns the ocean, each fisherman has an incentive "
                            "to catch as many fish as possible before others do. "
                            "Over time, the resource is depleted. "
                            "This pattern, known as the tragedy of the commons, "
                            "shows how individual self-interest can destroy shared resources "
                            "when there are no rules to limit use."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ngoại tác và hàng hóa công cộng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Markets are powerful tools for organizing economic activity, "
                            "but they do not always produce the best outcome for society. "
                            "When a transaction between a buyer and a seller affects a third party "
                            "who is not involved in the deal, economists call this an externality.\n\n"
                            "A negative externality imposes costs on outsiders. "
                            "Pollution is the most common example. "
                            "When a factory produces steel, it also produces smoke and wastewater. "
                            "The factory and its customers benefit from the steel, "
                            "but nearby residents suffer from the pollution without receiving any compensation. "
                            "Because the factory does not pay for the environmental damage it causes, "
                            "it produces more steel than is socially optimal. "
                            "The market price of steel is too low because it does not include the cost of pollution.\n\n"
                            "A positive externality creates benefits for outsiders. "
                            "Education is a good example. When a person gets a university degree, "
                            "they earn a higher salary — that is a private benefit. "
                            "But society also benefits: educated citizens pay more taxes, commit fewer crimes, "
                            "and contribute to innovation. Because these social benefits are not captured "
                            "by the market price of education, the market produces less education than society needs. "
                            "This is why governments often provide a subsidy for education — "
                            "financial support that lowers the cost for students and encourages more people to study.\n\n"
                            "Some goods are so difficult for markets to provide that they are called public goods. "
                            "A public good has two special features: it is non-excludable, meaning you cannot stop "
                            "anyone from using it, and it is non-rivalrous, meaning one person's use does not "
                            "reduce the amount available for others. Street lighting is a classic example. "
                            "Once a street lamp is installed, everyone on the street benefits, "
                            "whether they helped pay for it or not.\n\n"
                            "This creates the free-rider problem. "
                            "A free-rider is someone who enjoys the benefits of a good without paying for it. "
                            "If everyone waits for someone else to pay for the street lamp, "
                            "no one will pay, and the lamp will never be built. "
                            "This is why public goods are usually provided by the government, funded through taxes.\n\n"
                            "A related problem involves the commons — shared resources that anyone can use "
                            "but no one owns. Fisheries, forests, and clean air are examples of the commons. "
                            "Because no single person owns the ocean, each fisherman has an incentive "
                            "to catch as many fish as possible before others do. "
                            "Over time, the resource is depleted. "
                            "This pattern, known as the tragedy of the commons, "
                            "shows how individual self-interest can destroy shared resources "
                            "when there are no rules to limit use."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ngoại tác và hàng hóa công cộng",
                    "description": "Viết câu sử dụng 6 từ vựng về ngoại tác và hàng hóa công cộng.",
                    "data": {
                        "vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution"],
                        "items": [
                            {
                                "targetVocab": "externality",
                                "prompt": "Dùng từ 'externality' để viết một câu về tác động phụ của một hoạt động kinh tế lên người ngoài cuộc. Ví dụ: The construction of a new highway creates a negative externality for nearby homeowners whose property values drop due to increased noise and traffic."
                            },
                            {
                                "targetVocab": "subsidy",
                                "prompt": "Dùng từ 'subsidy' để viết một câu về khoản trợ cấp của chính phủ nhằm khuyến khích một hoạt động có lợi cho xã hội. Ví dụ: The government offers a subsidy to farmers who switch from chemical fertilizers to organic methods, reducing soil pollution in the long run."
                            },
                            {
                                "targetVocab": "public",
                                "prompt": "Dùng từ 'public' để viết một câu về hàng hóa công cộng mà mọi người đều được hưởng lợi. Ví dụ: Public parks in Ho Chi Minh City provide green space for millions of residents, but funding their maintenance remains a constant challenge."
                            },
                            {
                                "targetVocab": "free-rider",
                                "prompt": "Dùng từ 'free-rider' để viết một câu về người hưởng lợi từ dịch vụ mà không đóng góp chi phí. Ví dụ: In group projects at university, there is always a risk that one member becomes a free-rider, benefiting from the team's work without contributing their fair share."
                            },
                            {
                                "targetVocab": "commons",
                                "prompt": "Dùng từ 'commons' để viết một câu về tài nguyên chung bị khai thác quá mức. Ví dụ: The groundwater beneath the Mekong Delta is a commons that farmers share, but excessive pumping has caused the water table to drop dangerously low."
                            },
                            {
                                "targetVocab": "pollution",
                                "prompt": "Dùng từ 'pollution' để viết một câu về ô nhiễm môi trường do hoạt động sản xuất gây ra. Ví dụ: Industrial pollution from textile factories along the river has made the water unsafe for drinking and destroyed the livelihoods of local fishermen."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về can thiệp chính phủ và tổn thất phúc lợi.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "externality — ngoại tác, subsidy — trợ cấp, public — công cộng, "
                            "free-rider — người hưởng lợi miễn phí, commons — tài nguyên chung, "
                            "và pollution — ô nhiễm. "
                            "Bạn đã hiểu vì sao thị trường đôi khi thất bại trong việc phân bổ nguồn lực. "
                            "Bây giờ, chúng ta sẽ tìm hiểu chính phủ can thiệp như thế nào.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: intervention, tax, quota, welfare, deadweight, và loss. "
                            "Những từ này giúp bạn phân tích các công cụ chính sách — "
                            "từ thuế và hạn ngạch đến phúc lợi xã hội — và hiểu cái giá phải trả "
                            "khi chính phủ can thiệp vào thị trường.\n\n"
                            "Từ đầu tiên là intervention — danh từ — nghĩa là sự can thiệp, "
                            "hành động của chính phủ nhằm thay đổi kết quả thị trường. "
                            "Ví dụ: 'Government intervention in the housing market includes rent controls, "
                            "building subsidies, and zoning regulations.' "
                            "Trong bài đọc, intervention là chủ đề trung tâm — "
                            "khi thị trường thất bại, chính phủ phải quyết định có nên can thiệp hay không.\n\n"
                            "Từ thứ hai là tax — danh từ và động từ — nghĩa là thuế, "
                            "khoản tiền bắt buộc mà cá nhân hoặc doanh nghiệp phải nộp cho chính phủ. "
                            "Ví dụ: 'A carbon tax makes companies pay for each ton of carbon dioxide they emit, "
                            "giving them an incentive to reduce pollution.' "
                            "Trong bài đọc, tax là công cụ phổ biến nhất để chính phủ sửa chữa ngoại tác tiêu cực — "
                            "buộc người gây ô nhiễm phải trả chi phí xã hội.\n\n"
                            "Từ thứ ba là quota — danh từ — nghĩa là hạn ngạch, "
                            "giới hạn số lượng tối đa mà chính phủ cho phép sản xuất hoặc tiêu thụ. "
                            "Ví dụ: 'The fishing quota limits each boat to five hundred kilograms per trip "
                            "to prevent overfishing in the South China Sea.' "
                            "Trong bài đọc, quota là biện pháp trực tiếp — "
                            "thay vì dùng giá để điều chỉnh, chính phủ đặt giới hạn cứng.\n\n"
                            "Từ thứ tư là welfare — danh từ — nghĩa là phúc lợi, "
                            "mức độ hạnh phúc và thịnh vượng của cá nhân hoặc xã hội. "
                            "Ví dụ: 'Economists measure social welfare by looking at both consumer surplus "
                            "and producer surplus in a market.' "
                            "Trong bài đọc, welfare là thước đo để đánh giá chính sách — "
                            "một chính sách tốt là chính sách tăng tổng phúc lợi xã hội.\n\n"
                            "Từ thứ năm là deadweight — tính từ — nghĩa là vô ích, không tạo ra giá trị, "
                            "thường đi kèm với loss để tạo thành deadweight loss — tổn thất vô ích. "
                            "Ví dụ: 'The tariff on imported shoes created a deadweight loss "
                            "because some trades that would have benefited both buyers and sellers no longer happen.' "
                            "Trong bài đọc, deadweight mô tả phần giá trị bị mất đi vĩnh viễn "
                            "khi chính sách ngăn cản các giao dịch có lợi.\n\n"
                            "Từ cuối cùng là loss — danh từ — nghĩa là tổn thất, sự mất mát, "
                            "phần giá trị kinh tế bị giảm đi. "
                            "Ví dụ: 'The loss of economic efficiency from the price control "
                            "was greater than the benefit it provided to low-income consumers.' "
                            "Trong bài đọc, loss thường đi cùng deadweight — "
                            "deadweight loss là tổn thất mà không ai được hưởng, nó đơn giản biến mất.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về can thiệp chính phủ và tổn thất phúc lợi nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Học 6 từ: intervention, tax, quota, welfare, deadweight, loss",
                    "data": {"vocabList": ["intervention", "tax", "quota", "welfare", "deadweight", "loss"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Học 6 từ: intervention, tax, quota, welfare, deadweight, loss",
                    "data": {"vocabList": ["intervention", "tax", "quota", "welfare", "deadweight", "loss"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Học 6 từ: intervention, tax, quota, welfare, deadweight, loss",
                    "data": {"vocabList": ["intervention", "tax", "quota", "welfare", "deadweight", "loss"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Học 6 từ: intervention, tax, quota, welfare, deadweight, loss",
                    "data": {"vocabList": ["intervention", "tax", "quota", "welfare", "deadweight", "loss"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Học 6 từ: intervention, tax, quota, welfare, deadweight, loss",
                    "data": {"vocabList": ["intervention", "tax", "quota", "welfare", "deadweight", "loss"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "When markets fail, governments face a difficult choice: intervene and risk creating new problems, or stand back and accept the damage.",
                    "data": {
                        "text": (
                            "When markets fail, governments face a difficult choice: "
                            "intervene and risk creating new problems, or stand back and accept the damage. "
                            "Government intervention takes many forms, and each comes with trade-offs.\n\n"
                            "One of the most common tools is a tax. "
                            "When a factory creates pollution, the market price of its product does not reflect "
                            "the true cost to society. A tax on pollution — sometimes called a Pigouvian tax — "
                            "forces the factory to pay for the damage it causes. "
                            "If the tax is set at the right level, it raises the price of the product "
                            "just enough to account for the externality. "
                            "Consumers buy less, the factory produces less, and pollution falls. "
                            "The tax revenue can then be used to clean up the environment "
                            "or compensate those who were harmed.\n\n"
                            "Another tool is a quota — a direct limit on how much of something can be produced or consumed. "
                            "Fishing quotas, for example, set a maximum catch for each season. "
                            "Unlike a tax, which works through prices, a quota works through quantity. "
                            "The government decides the total amount allowed and divides it among producers. "
                            "Quotas are effective when the government knows exactly how much pollution or resource use "
                            "is acceptable, but they can be difficult to enforce.\n\n"
                            "Both taxes and quotas are forms of government intervention — "
                            "deliberate actions to change market outcomes. "
                            "The goal of intervention is usually to improve social welfare — "
                            "the overall well-being of society. "
                            "Welfare in economics is measured by adding up consumer surplus "
                            "(the benefit buyers get from paying less than they would be willing to) "
                            "and producer surplus (the benefit sellers get from receiving more than their minimum price). "
                            "When the market works well, total welfare is maximized.\n\n"
                            "But intervention can also reduce welfare. "
                            "When a tax or quota prevents trades that would have made both buyers and sellers better off, "
                            "the result is a deadweight loss. "
                            "A deadweight loss is a loss of economic value that no one receives — "
                            "it simply disappears. "
                            "For example, if a tax on sugary drinks is set too high, "
                            "some consumers who would have happily paid the original price stop buying. "
                            "The producer loses a sale, the consumer loses a product they wanted, "
                            "and the government does not collect tax on that transaction. "
                            "That lost value is the deadweight loss.\n\n"
                            "The challenge for policymakers is to design interventions "
                            "that correct market failures without creating large deadweight losses. "
                            "A well-designed tax can improve welfare by reducing pollution, "
                            "but a poorly designed one can make society worse off. "
                            "The key is to set the tax or quota at a level "
                            "where the benefit of reducing the externality outweighs the loss from reduced trade."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "When markets fail, governments face a difficult choice: intervene and risk creating new problems, or stand back and accept the damage.",
                    "data": {
                        "text": (
                            "When markets fail, governments face a difficult choice: "
                            "intervene and risk creating new problems, or stand back and accept the damage. "
                            "Government intervention takes many forms, and each comes with trade-offs.\n\n"
                            "One of the most common tools is a tax. "
                            "When a factory creates pollution, the market price of its product does not reflect "
                            "the true cost to society. A tax on pollution — sometimes called a Pigouvian tax — "
                            "forces the factory to pay for the damage it causes. "
                            "If the tax is set at the right level, it raises the price of the product "
                            "just enough to account for the externality. "
                            "Consumers buy less, the factory produces less, and pollution falls. "
                            "The tax revenue can then be used to clean up the environment "
                            "or compensate those who were harmed.\n\n"
                            "Another tool is a quota — a direct limit on how much of something can be produced or consumed. "
                            "Fishing quotas, for example, set a maximum catch for each season. "
                            "Unlike a tax, which works through prices, a quota works through quantity. "
                            "The government decides the total amount allowed and divides it among producers. "
                            "Quotas are effective when the government knows exactly how much pollution or resource use "
                            "is acceptable, but they can be difficult to enforce.\n\n"
                            "Both taxes and quotas are forms of government intervention — "
                            "deliberate actions to change market outcomes. "
                            "The goal of intervention is usually to improve social welfare — "
                            "the overall well-being of society. "
                            "Welfare in economics is measured by adding up consumer surplus "
                            "(the benefit buyers get from paying less than they would be willing to) "
                            "and producer surplus (the benefit sellers get from receiving more than their minimum price). "
                            "When the market works well, total welfare is maximized.\n\n"
                            "But intervention can also reduce welfare. "
                            "When a tax or quota prevents trades that would have made both buyers and sellers better off, "
                            "the result is a deadweight loss. "
                            "A deadweight loss is a loss of economic value that no one receives — "
                            "it simply disappears. "
                            "For example, if a tax on sugary drinks is set too high, "
                            "some consumers who would have happily paid the original price stop buying. "
                            "The producer loses a sale, the consumer loses a product they wanted, "
                            "and the government does not collect tax on that transaction. "
                            "That lost value is the deadweight loss.\n\n"
                            "The challenge for policymakers is to design interventions "
                            "that correct market failures without creating large deadweight losses. "
                            "A well-designed tax can improve welfare by reducing pollution, "
                            "but a poorly designed one can make society worse off. "
                            "The key is to set the tax or quota at a level "
                            "where the benefit of reducing the externality outweighs the loss from reduced trade."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When markets fail, governments face a difficult choice: "
                            "intervene and risk creating new problems, or stand back and accept the damage. "
                            "Government intervention takes many forms, and each comes with trade-offs.\n\n"
                            "One of the most common tools is a tax. "
                            "When a factory creates pollution, the market price of its product does not reflect "
                            "the true cost to society. A tax on pollution — sometimes called a Pigouvian tax — "
                            "forces the factory to pay for the damage it causes. "
                            "If the tax is set at the right level, it raises the price of the product "
                            "just enough to account for the externality. "
                            "Consumers buy less, the factory produces less, and pollution falls. "
                            "The tax revenue can then be used to clean up the environment "
                            "or compensate those who were harmed.\n\n"
                            "Another tool is a quota — a direct limit on how much of something can be produced or consumed. "
                            "Fishing quotas, for example, set a maximum catch for each season. "
                            "Unlike a tax, which works through prices, a quota works through quantity. "
                            "The government decides the total amount allowed and divides it among producers. "
                            "Quotas are effective when the government knows exactly how much pollution or resource use "
                            "is acceptable, but they can be difficult to enforce.\n\n"
                            "Both taxes and quotas are forms of government intervention — "
                            "deliberate actions to change market outcomes. "
                            "The goal of intervention is usually to improve social welfare — "
                            "the overall well-being of society. "
                            "Welfare in economics is measured by adding up consumer surplus "
                            "(the benefit buyers get from paying less than they would be willing to) "
                            "and producer surplus (the benefit sellers get from receiving more than their minimum price). "
                            "When the market works well, total welfare is maximized.\n\n"
                            "But intervention can also reduce welfare. "
                            "When a tax or quota prevents trades that would have made both buyers and sellers better off, "
                            "the result is a deadweight loss. "
                            "A deadweight loss is a loss of economic value that no one receives — "
                            "it simply disappears. "
                            "For example, if a tax on sugary drinks is set too high, "
                            "some consumers who would have happily paid the original price stop buying. "
                            "The producer loses a sale, the consumer loses a product they wanted, "
                            "and the government does not collect tax on that transaction. "
                            "That lost value is the deadweight loss.\n\n"
                            "The challenge for policymakers is to design interventions "
                            "that correct market failures without creating large deadweight losses. "
                            "A well-designed tax can improve welfare by reducing pollution, "
                            "but a poorly designed one can make society worse off. "
                            "The key is to set the tax or quota at a level "
                            "where the benefit of reducing the externality outweighs the loss from reduced trade."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Can thiệp chính phủ và tổn thất phúc lợi",
                    "description": "Viết câu sử dụng 6 từ vựng về can thiệp chính phủ.",
                    "data": {
                        "vocabList": ["intervention", "tax", "quota", "welfare", "deadweight", "loss"],
                        "items": [
                            {
                                "targetVocab": "intervention",
                                "prompt": "Dùng từ 'intervention' để viết một câu về hành động can thiệp của chính phủ vào thị trường khi xảy ra thất bại. Ví dụ: Government intervention in the pharmaceutical market ensures that essential medicines remain affordable for patients who cannot pay market prices."
                            },
                            {
                                "targetVocab": "tax",
                                "prompt": "Dùng từ 'tax' để viết một câu về việc đánh thuế nhằm giảm thiểu ngoại tác tiêu cực. Ví dụ: Vietnam introduced a higher tax on plastic bags to discourage single-use plastics and reduce the amount of waste entering rivers and oceans."
                            },
                            {
                                "targetVocab": "quota",
                                "prompt": "Dùng từ 'quota' để viết một câu về hạn ngạch mà chính phủ áp dụng để bảo vệ tài nguyên. Ví dụ: The fishing quota in the Gulf of Thailand limits each vessel to a specific catch size to allow fish populations to recover."
                            },
                            {
                                "targetVocab": "welfare",
                                "prompt": "Dùng từ 'welfare' để viết một câu về phúc lợi xã hội và cách chính sách kinh tế ảnh hưởng đến nó. Ví dụ: The new public transportation system improved social welfare by reducing commute times and giving low-income workers better access to jobs across the city."
                            },
                            {
                                "targetVocab": "deadweight",
                                "prompt": "Dùng từ 'deadweight' để viết một câu về tổn thất vô ích khi chính sách ngăn cản giao dịch có lợi. Ví dụ: The import ban on used cars created a deadweight loss because many buyers who wanted affordable vehicles could no longer find them in the market."
                            },
                            {
                                "targetVocab": "loss",
                                "prompt": "Dùng từ 'loss' để viết một câu về tổn thất kinh tế do chính sách can thiệp gây ra. Ví dụ: The loss of trade between the two countries after the tariff increase was estimated at over two billion dollars per year."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về thông tin bất cân xứng và quy định.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: "
                            "externality — ngoại tác, subsidy — trợ cấp, public — công cộng, "
                            "free-rider — người hưởng lợi miễn phí, commons — tài nguyên chung, "
                            "và pollution — ô nhiễm. "
                            "Bạn đã hiểu vì sao thị trường đôi khi không thể tự giải quyết vấn đề.\n\n"
                            "Trong phần 2, bạn đã học thêm: "
                            "intervention — can thiệp, tax — thuế, quota — hạn ngạch, "
                            "welfare — phúc lợi, deadweight — vô ích, và loss — tổn thất. "
                            "Bạn đã biết chính phủ dùng những công cụ nào để sửa chữa thất bại thị trường "
                            "và cái giá phải trả khi can thiệp không đúng cách.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ khám phá một loại thất bại thị trường khác — "
                            "khi thông tin không được chia sẻ đều giữa các bên giao dịch. "
                            "Bạn sẽ học 6 từ mới: asymmetry, moral, adverse, regulation, corrective, và spillover.\n\n"
                            "Từ đầu tiên là asymmetry — danh từ — nghĩa là sự bất cân xứng, "
                            "tình trạng khi một bên có nhiều thông tin hơn bên kia trong giao dịch. "
                            "Ví dụ: 'Information asymmetry in the used car market means that sellers know "
                            "more about the car's condition than buyers do.' "
                            "Trong bài đọc, asymmetry là nguyên nhân gốc rễ của nhiều thất bại thị trường — "
                            "khi người mua không biết chất lượng thật sự của sản phẩm.\n\n"
                            "Từ thứ hai là moral — tính từ — trong kinh tế thường đi với hazard "
                            "để tạo thành moral hazard — rủi ro đạo đức, "
                            "khi một bên thay đổi hành vi vì biết rằng bên kia gánh chịu rủi ro. "
                            "Ví dụ: 'Moral hazard occurs when people with health insurance "
                            "take fewer precautions because they know the insurer will pay for treatment.' "
                            "Trong bài đọc, moral mô tả vấn đề khi bảo hiểm hoặc bảo lãnh "
                            "khiến người ta hành động thiếu trách nhiệm.\n\n"
                            "Từ thứ ba là adverse — tính từ — nghĩa là bất lợi, tiêu cực, "
                            "thường đi với selection để tạo thành adverse selection — lựa chọn ngược. "
                            "Ví dụ: 'Adverse selection in the insurance market means that people "
                            "who are most likely to get sick are also the most likely to buy insurance.' "
                            "Trong bài đọc, adverse mô tả hiện tượng khi thông tin bất cân xứng "
                            "khiến thị trường thu hút sai đối tượng.\n\n"
                            "Từ thứ tư là regulation — danh từ — nghĩa là quy định, "
                            "luật lệ mà chính phủ ban hành để kiểm soát hành vi kinh tế. "
                            "Ví dụ: 'Environmental regulation requires factories to install filters "
                            "that reduce the amount of harmful chemicals released into the air.' "
                            "Trong bài đọc, regulation là công cụ chính phủ dùng để giải quyết "
                            "cả ngoại tác lẫn thông tin bất cân xứng.\n\n"
                            "Từ thứ năm là corrective — tính từ — nghĩa là mang tính sửa chữa, điều chỉnh, "
                            "thường dùng trong cụm corrective tax hoặc corrective policy. "
                            "Ví dụ: 'A corrective tax on carbon emissions aims to align the private cost "
                            "of production with the true social cost.' "
                            "Trong bài đọc, corrective mô tả các chính sách được thiết kế "
                            "để đưa thị trường trở lại trạng thái hiệu quả.\n\n"
                            "Từ cuối cùng là spillover — danh từ — nghĩa là hiệu ứng lan tỏa, "
                            "tác động của một hoạt động kinh tế lan sang các lĩnh vực hoặc khu vực khác. "
                            "Ví dụ: 'The technology spillover from multinational companies "
                            "helps local firms in Vietnam improve their production methods.' "
                            "Trong bài đọc, spillover là cách nói khác của externality — "
                            "nhưng nhấn mạnh vào sự lan tỏa, đặc biệt là lan tỏa tích cực.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về thông tin bất cân xứng và quy định nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thông tin bất cân xứng và quy định",
                    "description": "Học 6 từ: asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thông tin bất cân xứng và quy định",
                    "description": "Học 6 từ: asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thông tin bất cân xứng và quy định",
                    "description": "Học 6 từ: asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thông tin bất cân xứng và quy định",
                    "description": "Học 6 từ: asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Thông tin bất cân xứng và quy định",
                    "description": "Học 6 từ: asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thông tin bất cân xứng và hiệu ứng lan tỏa",
                    "description": "Not all market failures come from pollution or public goods. Some of the most damaging failures happen because of information.",
                    "data": {
                        "text": (
                            "Not all market failures come from pollution or public goods. "
                            "Some of the most damaging failures happen because of information. "
                            "When one side of a transaction knows more than the other, "
                            "economists call this information asymmetry, and it can cause markets to break down.\n\n"
                            "Consider the market for used cars. "
                            "The seller knows whether the car has hidden problems, but the buyer does not. "
                            "This asymmetry creates a problem called adverse selection. "
                            "Because buyers cannot tell good cars from bad ones, "
                            "they are only willing to pay an average price. "
                            "Owners of high-quality cars refuse to sell at that low price and leave the market. "
                            "Over time, only low-quality cars — lemons — remain for sale. "
                            "The market fails because good products are driven out by bad ones.\n\n"
                            "A related problem is moral hazard. "
                            "Moral hazard occurs when someone changes their behavior "
                            "because they do not bear the full consequences of their actions. "
                            "Health insurance is a common example. "
                            "A person with full insurance coverage may visit the doctor more often "
                            "or take fewer steps to stay healthy, because the insurance company pays the bills. "
                            "The insurer cannot easily observe the patient's daily habits, "
                            "so the asymmetry of information leads to higher costs for everyone.\n\n"
                            "Governments use regulation to address these problems. "
                            "Regulation is a set of rules that controls how businesses and individuals behave. "
                            "In the used car market, regulations may require sellers to disclose known defects. "
                            "In the insurance market, regulations may require minimum coverage levels "
                            "or limit how much insurers can charge based on health status. "
                            "The goal is to reduce the information gap and make markets work more fairly.\n\n"
                            "When externalities are the problem, governments can use corrective measures. "
                            "A corrective tax — also known as a Pigouvian tax — is designed to make polluters "
                            "pay the full social cost of their actions. "
                            "A corrective subsidy does the opposite: it rewards activities that create positive spillovers. "
                            "Education, vaccination, and research all generate spillover effects — "
                            "benefits that spread beyond the person who pays for them. "
                            "When a scientist discovers a new technology, the spillover reaches other companies "
                            "and even other countries, boosting productivity far beyond the original investment.\n\n"
                            "Market failure is not a reason to abandon markets. "
                            "It is a reason to understand their limits. "
                            "With the right combination of regulation, corrective taxes, and subsidies, "
                            "governments can help markets work better — "
                            "reducing pollution, protecting consumers from adverse selection, "
                            "and encouraging the positive spillovers that drive economic progress."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thông tin bất cân xứng và hiệu ứng lan tỏa",
                    "description": "Not all market failures come from pollution or public goods. Some of the most damaging failures happen because of information.",
                    "data": {
                        "text": (
                            "Not all market failures come from pollution or public goods. "
                            "Some of the most damaging failures happen because of information. "
                            "When one side of a transaction knows more than the other, "
                            "economists call this information asymmetry, and it can cause markets to break down.\n\n"
                            "Consider the market for used cars. "
                            "The seller knows whether the car has hidden problems, but the buyer does not. "
                            "This asymmetry creates a problem called adverse selection. "
                            "Because buyers cannot tell good cars from bad ones, "
                            "they are only willing to pay an average price. "
                            "Owners of high-quality cars refuse to sell at that low price and leave the market. "
                            "Over time, only low-quality cars — lemons — remain for sale. "
                            "The market fails because good products are driven out by bad ones.\n\n"
                            "A related problem is moral hazard. "
                            "Moral hazard occurs when someone changes their behavior "
                            "because they do not bear the full consequences of their actions. "
                            "Health insurance is a common example. "
                            "A person with full insurance coverage may visit the doctor more often "
                            "or take fewer steps to stay healthy, because the insurance company pays the bills. "
                            "The insurer cannot easily observe the patient's daily habits, "
                            "so the asymmetry of information leads to higher costs for everyone.\n\n"
                            "Governments use regulation to address these problems. "
                            "Regulation is a set of rules that controls how businesses and individuals behave. "
                            "In the used car market, regulations may require sellers to disclose known defects. "
                            "In the insurance market, regulations may require minimum coverage levels "
                            "or limit how much insurers can charge based on health status. "
                            "The goal is to reduce the information gap and make markets work more fairly.\n\n"
                            "When externalities are the problem, governments can use corrective measures. "
                            "A corrective tax — also known as a Pigouvian tax — is designed to make polluters "
                            "pay the full social cost of their actions. "
                            "A corrective subsidy does the opposite: it rewards activities that create positive spillovers. "
                            "Education, vaccination, and research all generate spillover effects — "
                            "benefits that spread beyond the person who pays for them. "
                            "When a scientist discovers a new technology, the spillover reaches other companies "
                            "and even other countries, boosting productivity far beyond the original investment.\n\n"
                            "Market failure is not a reason to abandon markets. "
                            "It is a reason to understand their limits. "
                            "With the right combination of regulation, corrective taxes, and subsidies, "
                            "governments can help markets work better — "
                            "reducing pollution, protecting consumers from adverse selection, "
                            "and encouraging the positive spillovers that drive economic progress."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thông tin bất cân xứng và hiệu ứng lan tỏa",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Not all market failures come from pollution or public goods. "
                            "Some of the most damaging failures happen because of information. "
                            "When one side of a transaction knows more than the other, "
                            "economists call this information asymmetry, and it can cause markets to break down.\n\n"
                            "Consider the market for used cars. "
                            "The seller knows whether the car has hidden problems, but the buyer does not. "
                            "This asymmetry creates a problem called adverse selection. "
                            "Because buyers cannot tell good cars from bad ones, "
                            "they are only willing to pay an average price. "
                            "Owners of high-quality cars refuse to sell at that low price and leave the market. "
                            "Over time, only low-quality cars — lemons — remain for sale. "
                            "The market fails because good products are driven out by bad ones.\n\n"
                            "A related problem is moral hazard. "
                            "Moral hazard occurs when someone changes their behavior "
                            "because they do not bear the full consequences of their actions. "
                            "Health insurance is a common example. "
                            "A person with full insurance coverage may visit the doctor more often "
                            "or take fewer steps to stay healthy, because the insurance company pays the bills. "
                            "The insurer cannot easily observe the patient's daily habits, "
                            "so the asymmetry of information leads to higher costs for everyone.\n\n"
                            "Governments use regulation to address these problems. "
                            "Regulation is a set of rules that controls how businesses and individuals behave. "
                            "In the used car market, regulations may require sellers to disclose known defects. "
                            "In the insurance market, regulations may require minimum coverage levels "
                            "or limit how much insurers can charge based on health status. "
                            "The goal is to reduce the information gap and make markets work more fairly.\n\n"
                            "When externalities are the problem, governments can use corrective measures. "
                            "A corrective tax — also known as a Pigouvian tax — is designed to make polluters "
                            "pay the full social cost of their actions. "
                            "A corrective subsidy does the opposite: it rewards activities that create positive spillovers. "
                            "Education, vaccination, and research all generate spillover effects — "
                            "benefits that spread beyond the person who pays for them. "
                            "When a scientist discovers a new technology, the spillover reaches other companies "
                            "and even other countries, boosting productivity far beyond the original investment.\n\n"
                            "Market failure is not a reason to abandon markets. "
                            "It is a reason to understand their limits. "
                            "With the right combination of regulation, corrective taxes, and subsidies, "
                            "governments can help markets work better — "
                            "reducing pollution, protecting consumers from adverse selection, "
                            "and encouraging the positive spillovers that drive economic progress."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thông tin bất cân xứng và quy định",
                    "description": "Viết câu sử dụng 6 từ vựng về thông tin bất cân xứng.",
                    "data": {
                        "vocabList": ["asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"],
                        "items": [
                            {
                                "targetVocab": "asymmetry",
                                "prompt": "Dùng từ 'asymmetry' để viết một câu về tình trạng thông tin bất cân xứng giữa người mua và người bán. Ví dụ: The information asymmetry between doctors and patients means that patients often cannot judge whether a recommended treatment is truly necessary."
                            },
                            {
                                "targetVocab": "moral",
                                "prompt": "Dùng từ 'moral' để viết một câu về rủi ro đạo đức khi một bên không chịu hậu quả hành động của mình. Ví dụ: The bank bailout during the financial crisis raised concerns about moral hazard, as banks learned they could take excessive risks without facing bankruptcy."
                            },
                            {
                                "targetVocab": "adverse",
                                "prompt": "Dùng từ 'adverse' để viết một câu về lựa chọn ngược trong thị trường bảo hiểm hoặc tín dụng. Ví dụ: Adverse selection in the health insurance market means that people with chronic illnesses are more likely to purchase comprehensive coverage, driving up premiums for everyone."
                            },
                            {
                                "targetVocab": "regulation",
                                "prompt": "Dùng từ 'regulation' để viết một câu về quy định của chính phủ nhằm bảo vệ người tiêu dùng hoặc môi trường. Ví dụ: Stricter regulation on food labeling in Vietnam now requires manufacturers to list all ingredients and allergens clearly on the packaging."
                            },
                            {
                                "targetVocab": "corrective",
                                "prompt": "Dùng từ 'corrective' để viết một câu về chính sách điều chỉnh nhằm sửa chữa thất bại thị trường. Ví dụ: The corrective tax on sugary beverages in several countries has successfully reduced consumption and improved public health outcomes."
                            },
                            {
                                "targetVocab": "spillover",
                                "prompt": "Dùng từ 'spillover' để viết một câu về hiệu ứng lan tỏa tích cực hoặc tiêu cực từ một hoạt động kinh tế. Ví dụ: The technology spillover from Samsung's factory in Thai Nguyen has helped dozens of local Vietnamese suppliers upgrade their manufacturing processes."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Thất bại thị trường. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng: "
                            "externality — ngoại tác, subsidy — trợ cấp, public — công cộng, "
                            "free-rider — người hưởng lợi miễn phí, commons — tài nguyên chung, "
                            "và pollution — ô nhiễm. "
                            "Đây là bộ khung để hiểu vì sao thị trường đôi khi thất bại.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "intervention — can thiệp, tax — thuế, quota — hạn ngạch, "
                            "welfare — phúc lợi, deadweight — vô ích, và loss — tổn thất. "
                            "Những từ này giúp bạn phân tích công cụ chính sách và cái giá của can thiệp.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "asymmetry — bất cân xứng, moral — đạo đức, adverse — bất lợi, "
                            "regulation — quy định, corrective — điều chỉnh, và spillover — lan tỏa. "
                            "Đây là những từ về thông tin bất cân xứng và hiệu ứng lan tỏa trong kinh tế.\n\n"
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
                    "description": "Học 18 từ: externality, subsidy, public, free-rider, commons, pollution, intervention, tax, quota, welfare, deadweight, loss, asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: externality, subsidy, public, free-rider, commons, pollution, intervention, tax, quota, welfare, deadweight, loss, asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: externality, subsidy, public, free-rider, commons, pollution, intervention, tax, quota, welfare, deadweight, loss, asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: externality, subsidy, public, free-rider, commons, pollution, intervention, tax, quota, welfare, deadweight, loss, asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: externality, subsidy, public, free-rider, commons, pollution, intervention, tax, quota, welfare, deadweight, loss, asymmetry, moral, adverse, regulation, corrective, spillover",
                    "data": {"vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng thất bại thị trường",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"],
                        "items": [
                            {
                                "targetVocab": "externality",
                                "prompt": "Dùng từ 'externality' để viết một câu về tác động ngoại tác trong ngành giao thông ở Việt Nam. Ví dụ: Traffic congestion in Hanoi is a negative externality of rapid motorbike ownership growth — every new rider slows down the commute for everyone else."
                            },
                            {
                                "targetVocab": "subsidy",
                                "prompt": "Dùng từ 'subsidy' để viết một câu về chính sách trợ cấp cho năng lượng tái tạo. Ví dụ: The government subsidy for rooftop solar panels has made clean energy affordable for thousands of Vietnamese households in rural areas."
                            },
                            {
                                "targetVocab": "public",
                                "prompt": "Dùng từ 'public' để viết một câu về một hàng hóa công cộng cụ thể và thách thức trong việc cung cấp nó. Ví dụ: Clean air is a public good that no private company has an incentive to provide, which is why governments must step in with environmental regulations."
                            },
                            {
                                "targetVocab": "free-rider",
                                "prompt": "Dùng từ 'free-rider' để viết một câu về vấn đề hưởng lợi miễn phí trong một tình huống thực tế. Ví dụ: Residents who refuse to pay the neighborhood security fee but still benefit from the guard's presence are classic free-riders."
                            },
                            {
                                "targetVocab": "commons",
                                "prompt": "Dùng từ 'commons' để viết một câu về tài nguyên chung đang bị đe dọa ở Việt Nam hoặc trên thế giới. Ví dụ: The coral reefs off the coast of Nha Trang are a commons threatened by both tourism and fishing — without protection, they will disappear within decades."
                            },
                            {
                                "targetVocab": "pollution",
                                "prompt": "Dùng từ 'pollution' để viết một câu về chi phí xã hội của ô nhiễm mà thị trường không phản ánh. Ví dụ: The true cost of cheap plastic products is hidden because the pollution they cause in rivers and oceans is not included in their market price."
                            },
                            {
                                "targetVocab": "intervention",
                                "prompt": "Dùng từ 'intervention' để viết một câu về một trường hợp can thiệp chính phủ thành công hoặc gây tranh cãi. Ví dụ: Government intervention to ban single-use plastic straws was initially controversial but has significantly reduced plastic waste in Vietnamese cities."
                            },
                            {
                                "targetVocab": "tax",
                                "prompt": "Dùng từ 'tax' để viết một câu về thuế môi trường và tác động của nó đến hành vi doanh nghiệp. Ví dụ: The environmental tax on coal has encouraged several power companies in Vietnam to invest in natural gas and solar alternatives."
                            },
                            {
                                "targetVocab": "quota",
                                "prompt": "Dùng từ 'quota' để viết một câu về hạn ngạch trong ngành khai thác tài nguyên. Ví dụ: The government set a strict quota on sand mining along the Mekong River after years of uncontrolled extraction caused severe riverbank erosion."
                            },
                            {
                                "targetVocab": "welfare",
                                "prompt": "Dùng từ 'welfare' để viết một câu so sánh phúc lợi xã hội trước và sau một chính sách cụ thể. Ví dụ: The universal health insurance program has improved social welfare in Vietnam by giving millions of low-income citizens access to medical care they could not previously afford."
                            },
                            {
                                "targetVocab": "deadweight",
                                "prompt": "Dùng từ 'deadweight' để viết một câu về tổn thất vô ích do một chính sách thuế hoặc hạn ngạch gây ra. Ví dụ: The high import tariff on foreign books creates a deadweight loss because many students who would benefit from affordable textbooks can no longer access them."
                            },
                            {
                                "targetVocab": "loss",
                                "prompt": "Dùng từ 'loss' để viết một câu về tổn thất kinh tế khi thị trường không hoạt động hiệu quả. Ví dụ: The economic loss from air pollution in major Vietnamese cities is estimated at billions of dollars per year in healthcare costs and reduced worker productivity."
                            },
                            {
                                "targetVocab": "asymmetry",
                                "prompt": "Dùng từ 'asymmetry' để viết một câu về thông tin bất cân xứng trong thị trường bất động sản. Ví dụ: The information asymmetry in Vietnam's real estate market means that developers often know about zoning changes months before ordinary buyers, giving them an unfair advantage."
                            },
                            {
                                "targetVocab": "moral",
                                "prompt": "Dùng từ 'moral' để viết một câu về rủi ro đạo đức trong ngành tài chính hoặc bảo hiểm. Ví dụ: The moral hazard problem in crop insurance means that some farmers may take fewer precautions against flooding because they know the insurance will cover their losses."
                            },
                            {
                                "targetVocab": "adverse",
                                "prompt": "Dùng từ 'adverse' để viết một câu về lựa chọn ngược trong thị trường lao động hoặc bảo hiểm. Ví dụ: Adverse selection in the job market occurs when companies offering low salaries attract only less-qualified candidates, while top talent goes to competitors."
                            },
                            {
                                "targetVocab": "regulation",
                                "prompt": "Dùng từ 'regulation' để viết một câu về quy định bảo vệ người tiêu dùng trong thương mại điện tử. Ví dụ: New regulation on e-commerce platforms in Vietnam requires sellers to provide accurate product descriptions and accept returns within seven days of delivery."
                            },
                            {
                                "targetVocab": "corrective",
                                "prompt": "Dùng từ 'corrective' để viết một câu về biện pháp điều chỉnh nhằm giảm ngoại tác tiêu cực. Ví dụ: The corrective measure of requiring all new buildings to include green spaces has helped reduce the urban heat island effect in Ho Chi Minh City."
                            },
                            {
                                "targetVocab": "spillover",
                                "prompt": "Dùng từ 'spillover' để viết một câu về hiệu ứng lan tỏa từ đầu tư nước ngoài vào Việt Nam. Ví dụ: The knowledge spillover from foreign-invested technology companies has helped Vietnamese startups develop competitive software products for the global market."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về thất bại thị trường.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về thất bại thị trường — từ ngoại tác và hàng hóa công cộng "
                            "đến can thiệp chính phủ và thông tin bất cân xứng.\n\n"
                            "Bạn sẽ gặp lại externality, subsidy, public, free-rider, commons, pollution "
                            "trong phần mở đầu về các loại thất bại thị trường. "
                            "Tiếp theo, intervention, tax, quota, welfare, deadweight, loss "
                            "sẽ giúp bạn hiểu cách chính phủ phản ứng và cái giá phải trả. "
                            "Và cuối cùng, asymmetry, moral, adverse, regulation, corrective, spillover "
                            "sẽ đưa bạn vào thế giới thông tin bất cân xứng và chính sách điều chỉnh.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thất bại thị trường — Bức tranh toàn cảnh",
                    "description": "The free market is a remarkable system, but it has blind spots.",
                    "data": {
                        "text": (
                            "The free market is a remarkable system, but it has blind spots. "
                            "When buyers and sellers make decisions based only on their own costs and benefits, "
                            "they sometimes ignore the effects on everyone else. "
                            "Economists call these situations market failures, "
                            "and understanding them is essential for anyone studying microeconomics.\n\n"
                            "The most visible type of market failure involves externalities. "
                            "An externality is a cost or benefit that falls on someone outside the transaction. "
                            "Pollution is the textbook example of a negative externality. "
                            "A cement factory produces building materials that society needs, "
                            "but it also releases dust and chemicals into the air. "
                            "The people living near the factory bear the health costs, "
                            "yet they receive none of the profits. "
                            "Because the factory does not pay for the pollution it creates, "
                            "it produces more cement than is socially efficient.\n\n"
                            "Positive externalities work in the opposite direction. "
                            "When a farmer plants trees along a riverbank to prevent erosion, "
                            "the spillover benefits reach neighboring farms and even downstream communities. "
                            "The farmer captures only a fraction of the total benefit, "
                            "so without help, fewer trees get planted than society would like. "
                            "A government subsidy — a payment to encourage the activity — "
                            "can close this gap by making tree planting financially worthwhile for the farmer.\n\n"
                            "Public goods present another challenge. "
                            "A public good is one that everyone can use without reducing its availability to others. "
                            "National defense, street lighting, and flood control systems are all public goods. "
                            "The problem is the free-rider. "
                            "A free-rider enjoys the benefit without contributing to the cost. "
                            "If enough people become free-riders, no one pays, and the good is never provided. "
                            "This is why governments fund public goods through taxes "
                            "rather than leaving them to the market.\n\n"
                            "The commons — shared resources like fisheries, groundwater, and clean air — "
                            "face a similar threat. "
                            "Because no one owns the commons, each user has an incentive to take as much as possible. "
                            "Overfishing, deforestation, and water depletion are all examples "
                            "of the tragedy of the commons. "
                            "Governments respond with quotas — limits on how much each person can extract — "
                            "and with regulation that sets rules for sustainable use.\n\n"
                            "Government intervention is not free. "
                            "Every tax, quota, or regulation changes the incentives in a market, "
                            "and some of those changes reduce welfare. "
                            "A tax on pollution, for instance, raises the price of goods "
                            "and causes some consumers to stop buying. "
                            "The trades that no longer happen represent a deadweight loss — "
                            "economic value that simply vanishes. "
                            "The loss is not transferred to anyone; it is gone. "
                            "Good policy aims to keep the deadweight loss smaller than the benefit "
                            "of correcting the market failure.\n\n"
                            "A corrective tax — also called a Pigouvian tax — is designed to do exactly this. "
                            "By setting the tax equal to the external cost, "
                            "the government forces producers to face the true social cost of their actions. "
                            "The result is less pollution, higher welfare, and a market that works more efficiently.\n\n"
                            "Not all market failures involve externalities. "
                            "Information asymmetry — when one party knows more than the other — "
                            "can be equally destructive. "
                            "In the insurance market, adverse selection occurs "
                            "when the people most likely to file claims are also the most eager to buy coverage. "
                            "Insurers cannot easily tell high-risk customers from low-risk ones, "
                            "so they charge everyone a higher premium. "
                            "Healthy people drop out, the pool becomes riskier, and premiums rise further. "
                            "Left unchecked, the market can collapse entirely.\n\n"
                            "Moral hazard is a related problem. "
                            "When people are protected from the consequences of their actions, "
                            "they may behave more recklessly. "
                            "A driver with full insurance coverage might take fewer precautions on the road. "
                            "A company that expects a government bailout might take on excessive debt. "
                            "Regulation — mandatory disclosure, minimum standards, and oversight — "
                            "helps reduce both adverse selection and moral hazard "
                            "by narrowing the information gap between parties.\n\n"
                            "Market failure is not an argument against markets. "
                            "It is a call for smarter markets. "
                            "With the right mix of corrective taxes, subsidies, quotas, and regulation, "
                            "governments can reduce pollution, protect the commons, fund public goods, "
                            "and ensure that information flows more evenly between buyers and sellers. "
                            "The spillover from getting these policies right extends far beyond any single market — "
                            "it shapes the welfare of entire societies."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thất bại thị trường — Bức tranh toàn cảnh",
                    "description": "The free market is a remarkable system, but it has blind spots.",
                    "data": {
                        "text": (
                            "The free market is a remarkable system, but it has blind spots. "
                            "When buyers and sellers make decisions based only on their own costs and benefits, "
                            "they sometimes ignore the effects on everyone else. "
                            "Economists call these situations market failures, "
                            "and understanding them is essential for anyone studying microeconomics.\n\n"
                            "The most visible type of market failure involves externalities. "
                            "An externality is a cost or benefit that falls on someone outside the transaction. "
                            "Pollution is the textbook example of a negative externality. "
                            "A cement factory produces building materials that society needs, "
                            "but it also releases dust and chemicals into the air. "
                            "The people living near the factory bear the health costs, "
                            "yet they receive none of the profits. "
                            "Because the factory does not pay for the pollution it creates, "
                            "it produces more cement than is socially efficient.\n\n"
                            "Positive externalities work in the opposite direction. "
                            "When a farmer plants trees along a riverbank to prevent erosion, "
                            "the spillover benefits reach neighboring farms and even downstream communities. "
                            "The farmer captures only a fraction of the total benefit, "
                            "so without help, fewer trees get planted than society would like. "
                            "A government subsidy — a payment to encourage the activity — "
                            "can close this gap by making tree planting financially worthwhile for the farmer.\n\n"
                            "Public goods present another challenge. "
                            "A public good is one that everyone can use without reducing its availability to others. "
                            "National defense, street lighting, and flood control systems are all public goods. "
                            "The problem is the free-rider. "
                            "A free-rider enjoys the benefit without contributing to the cost. "
                            "If enough people become free-riders, no one pays, and the good is never provided. "
                            "This is why governments fund public goods through taxes "
                            "rather than leaving them to the market.\n\n"
                            "The commons — shared resources like fisheries, groundwater, and clean air — "
                            "face a similar threat. "
                            "Because no one owns the commons, each user has an incentive to take as much as possible. "
                            "Overfishing, deforestation, and water depletion are all examples "
                            "of the tragedy of the commons. "
                            "Governments respond with quotas — limits on how much each person can extract — "
                            "and with regulation that sets rules for sustainable use.\n\n"
                            "Government intervention is not free. "
                            "Every tax, quota, or regulation changes the incentives in a market, "
                            "and some of those changes reduce welfare. "
                            "A tax on pollution, for instance, raises the price of goods "
                            "and causes some consumers to stop buying. "
                            "The trades that no longer happen represent a deadweight loss — "
                            "economic value that simply vanishes. "
                            "The loss is not transferred to anyone; it is gone. "
                            "Good policy aims to keep the deadweight loss smaller than the benefit "
                            "of correcting the market failure.\n\n"
                            "A corrective tax — also called a Pigouvian tax — is designed to do exactly this. "
                            "By setting the tax equal to the external cost, "
                            "the government forces producers to face the true social cost of their actions. "
                            "The result is less pollution, higher welfare, and a market that works more efficiently.\n\n"
                            "Not all market failures involve externalities. "
                            "Information asymmetry — when one party knows more than the other — "
                            "can be equally destructive. "
                            "In the insurance market, adverse selection occurs "
                            "when the people most likely to file claims are also the most eager to buy coverage. "
                            "Insurers cannot easily tell high-risk customers from low-risk ones, "
                            "so they charge everyone a higher premium. "
                            "Healthy people drop out, the pool becomes riskier, and premiums rise further. "
                            "Left unchecked, the market can collapse entirely.\n\n"
                            "Moral hazard is a related problem. "
                            "When people are protected from the consequences of their actions, "
                            "they may behave more recklessly. "
                            "A driver with full insurance coverage might take fewer precautions on the road. "
                            "A company that expects a government bailout might take on excessive debt. "
                            "Regulation — mandatory disclosure, minimum standards, and oversight — "
                            "helps reduce both adverse selection and moral hazard "
                            "by narrowing the information gap between parties.\n\n"
                            "Market failure is not an argument against markets. "
                            "It is a call for smarter markets. "
                            "With the right mix of corrective taxes, subsidies, quotas, and regulation, "
                            "governments can reduce pollution, protect the commons, fund public goods, "
                            "and ensure that information flows more evenly between buyers and sellers. "
                            "The spillover from getting these policies right extends far beyond any single market — "
                            "it shapes the welfare of entire societies."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thất bại thị trường — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "The free market is a remarkable system, but it has blind spots. "
                            "When buyers and sellers make decisions based only on their own costs and benefits, "
                            "they sometimes ignore the effects on everyone else. "
                            "Economists call these situations market failures, "
                            "and understanding them is essential for anyone studying microeconomics.\n\n"
                            "The most visible type of market failure involves externalities. "
                            "An externality is a cost or benefit that falls on someone outside the transaction. "
                            "Pollution is the textbook example of a negative externality. "
                            "A cement factory produces building materials that society needs, "
                            "but it also releases dust and chemicals into the air. "
                            "The people living near the factory bear the health costs, "
                            "yet they receive none of the profits. "
                            "Because the factory does not pay for the pollution it creates, "
                            "it produces more cement than is socially efficient.\n\n"
                            "Positive externalities work in the opposite direction. "
                            "When a farmer plants trees along a riverbank to prevent erosion, "
                            "the spillover benefits reach neighboring farms and even downstream communities. "
                            "The farmer captures only a fraction of the total benefit, "
                            "so without help, fewer trees get planted than society would like. "
                            "A government subsidy — a payment to encourage the activity — "
                            "can close this gap by making tree planting financially worthwhile for the farmer.\n\n"
                            "Public goods present another challenge. "
                            "A public good is one that everyone can use without reducing its availability to others. "
                            "National defense, street lighting, and flood control systems are all public goods. "
                            "The problem is the free-rider. "
                            "A free-rider enjoys the benefit without contributing to the cost. "
                            "If enough people become free-riders, no one pays, and the good is never provided. "
                            "This is why governments fund public goods through taxes "
                            "rather than leaving them to the market.\n\n"
                            "The commons — shared resources like fisheries, groundwater, and clean air — "
                            "face a similar threat. "
                            "Because no one owns the commons, each user has an incentive to take as much as possible. "
                            "Overfishing, deforestation, and water depletion are all examples "
                            "of the tragedy of the commons. "
                            "Governments respond with quotas — limits on how much each person can extract — "
                            "and with regulation that sets rules for sustainable use.\n\n"
                            "Government intervention is not free. "
                            "Every tax, quota, or regulation changes the incentives in a market, "
                            "and some of those changes reduce welfare. "
                            "A tax on pollution, for instance, raises the price of goods "
                            "and causes some consumers to stop buying. "
                            "The trades that no longer happen represent a deadweight loss — "
                            "economic value that simply vanishes. "
                            "The loss is not transferred to anyone; it is gone. "
                            "Good policy aims to keep the deadweight loss smaller than the benefit "
                            "of correcting the market failure.\n\n"
                            "A corrective tax — also called a Pigouvian tax — is designed to do exactly this. "
                            "By setting the tax equal to the external cost, "
                            "the government forces producers to face the true social cost of their actions. "
                            "The result is less pollution, higher welfare, and a market that works more efficiently.\n\n"
                            "Not all market failures involve externalities. "
                            "Information asymmetry — when one party knows more than the other — "
                            "can be equally destructive. "
                            "In the insurance market, adverse selection occurs "
                            "when the people most likely to file claims are also the most eager to buy coverage. "
                            "Insurers cannot easily tell high-risk customers from low-risk ones, "
                            "so they charge everyone a higher premium. "
                            "Healthy people drop out, the pool becomes riskier, and premiums rise further. "
                            "Left unchecked, the market can collapse entirely.\n\n"
                            "Moral hazard is a related problem. "
                            "When people are protected from the consequences of their actions, "
                            "they may behave more recklessly. "
                            "A driver with full insurance coverage might take fewer precautions on the road. "
                            "A company that expects a government bailout might take on excessive debt. "
                            "Regulation — mandatory disclosure, minimum standards, and oversight — "
                            "helps reduce both adverse selection and moral hazard "
                            "by narrowing the information gap between parties.\n\n"
                            "Market failure is not an argument against markets. "
                            "It is a call for smarter markets. "
                            "With the right mix of corrective taxes, subsidies, quotas, and regulation, "
                            "governments can reduce pollution, protect the commons, fund public goods, "
                            "and ensure that information flows more evenly between buyers and sellers. "
                            "The spillover from getting these policies right extends far beyond any single market — "
                            "it shapes the welfare of entire societies."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích thất bại thị trường",
                    "description": "Viết đoạn văn tiếng Anh phân tích về thất bại thị trường sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["externality", "subsidy", "public", "free-rider", "commons", "pollution", "intervention", "tax", "quota", "welfare", "deadweight", "loss", "asymmetry", "moral", "adverse", "regulation", "corrective", "spillover"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thất bại thị trường thực tế. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích vấn đề ô nhiễm không khí ở các thành phố lớn của Việt Nam như một trường hợp market failure. Giải thích externality tiêu cực từ giao thông và công nghiệp, tại sao thị trường tự do không giải quyết được pollution, và chính phủ có thể dùng corrective tax hoặc regulation nào để cải thiện welfare xã hội.",
                            "Hãy chọn một thị trường có vấn đề thông tin bất cân xứng (ví dụ: bảo hiểm y tế, xe cũ, hoặc thương mại điện tử) và phân tích cách asymmetry dẫn đến adverse selection hoặc moral hazard. Giải thích regulation nào có thể giúp giảm deadweight loss và cải thiện welfare cho cả người mua lẫn người bán."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với động lực hành động.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học cuối cùng trong chuỗi Kinh tế vi mô. "
                            "Đây không chỉ là kết thúc — đây là bước nhảy để bạn bắt đầu hành động.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất, "
                            "và lần này, mình sẽ gợi ý cho bạn cách dùng chúng ngay trong tuần tới.\n\n"
                            "Externality — ngoại tác. Mỗi khi bạn đọc tin tức về ô nhiễm, tắc đường, "
                            "hay tiếng ồn từ công trình xây dựng, hãy tự hỏi: ai đang chịu chi phí "
                            "mà không được bồi thường? Đó chính là externality. "
                            "Ví dụ mới: The positive externality of a well-maintained garden "
                            "is that it increases property values for the entire neighborhood.\n\n"
                            "Deadweight loss — tổn thất vô ích. Đây là khái niệm mà nhiều sinh viên "
                            "thấy trừu tượng, nhưng nó rất thực tế. Mỗi khi một chính sách ngăn cản "
                            "một giao dịch mà cả hai bên đều muốn, giá trị bị mất đi — không ai nhận được. "
                            "Ví dụ mới: The deadweight loss from the luxury goods tax was significant "
                            "because many middle-class consumers stopped buying products "
                            "that they previously enjoyed and could afford.\n\n"
                            "Asymmetry — bất cân xứng. Lần tới khi bạn mua hàng online "
                            "và không chắc chắn về chất lượng sản phẩm, hãy nhớ: "
                            "đó là information asymmetry đang hoạt động. "
                            "Ví dụ mới: The asymmetry between what food delivery apps know about restaurant hygiene "
                            "and what customers can see creates a trust problem in the market.\n\n"
                            "Regulation — quy định. Không phải mọi quy định đều tốt, "
                            "nhưng không có quy định nào cũng không ổn. "
                            "Bí quyết là tìm điểm cân bằng — đủ để bảo vệ, không quá nhiều để cản trở. "
                            "Ví dụ mới: The new regulation requiring ride-hailing drivers to pass safety inspections "
                            "has reduced accident rates without significantly increasing fares.\n\n"
                            "Spillover — hiệu ứng lan tỏa. Đây là từ lạc quan nhất trong bài học. "
                            "Mỗi khi bạn học một điều mới và chia sẻ với bạn bè, "
                            "bạn đang tạo ra positive spillover. "
                            "Ví dụ mới: The spillover from Vietnam's investment in public education "
                            "is visible in the country's rapidly growing technology sector.\n\n"
                            "Corrective — điều chỉnh. Khi bạn thấy một vấn đề trong thị trường, "
                            "đừng chỉ phàn nàn — hãy nghĩ xem corrective measure nào có thể giúp. "
                            "Đó là cách tư duy của một nhà kinh tế. "
                            "Ví dụ mới: The corrective policy of offering free public Wi-Fi in libraries "
                            "helps bridge the digital divide for students from low-income families.\n\n"
                            "Bạn biết không, bạn vừa hoàn thành toàn bộ 5 bài học Kinh tế vi mô — "
                            "từ cung cầu, cấu trúc thị trường, lựa chọn người tiêu dùng, chi phí sản xuất, "
                            "đến thất bại thị trường. Đó là 90 từ vựng tiếng Anh chuyên ngành.\n\n"
                            "Đây là bước tiếp theo mình gợi ý cho bạn: "
                            "tuần này, hãy mở một bài báo tiếng Anh về kinh tế trên The Economist hoặc BBC, "
                            "đọc một đoạn, và đánh dấu mỗi từ vựng bạn nhận ra. "
                            "Bạn sẽ ngạc nhiên khi thấy mình hiểu được bao nhiêu.\n\n"
                            "Tiếng Anh kinh tế không còn là rào cản — nó đã trở thành công cụ của bạn. "
                            "Hãy dùng nó. Chúc bạn thành công trên hành trình học tập!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Market Failure – Thất Bại Thị Trường' AND uid = '{UID}' ORDER BY created_at;")
