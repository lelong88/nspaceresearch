"""
Create curriculum: Trade Barriers – Rào Cản Thương Mại
Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa (International Trade), curriculum #2
18 words | 5 sessions | provocative_question tone | introspective guide farewell
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
W1 = ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"]
W2 = ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"]
W3 = ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Trade Barriers – Rào Cản Thương Mại",
    "contentTypeTags": [],
    "description": (
        "AI ĐÃ QUYẾT ĐỊNH GIÁ CHIẾC ÁO BẠN MẶC HÔM NAY — VÀ ĐÓ KHÔNG PHẢI NHÀ SẢN XUẤT?\n\n"
        "Mỗi lần bạn mua một chiếc áo 'made in Bangladesh' với giá 200 nghìn đồng, "
        "bạn có biết rằng chính phủ đã cộng thêm bao nhiêu phần trăm thuế nhập khẩu vào giá gốc không? "
        "Tariff, quota, embargo — những từ tưởng chỉ xuất hiện trong sách giáo khoa "
        "nhưng thực ra đang quyết định giá cả mọi thứ bạn mua mỗi ngày.\n\n"
        "Hãy nghĩ về rào cản thương mại như một bức tường vô hình giữa các quốc gia — "
        "bạn không nhìn thấy nó, nhưng nó quyết định hàng hóa nào được vào, "
        "hàng nào bị chặn, và ai phải trả giá cao hơn. "
        "Nếu không hiểu bức tường này, bạn sẽ mãi đọc tin kinh tế quốc tế mà không hiểu vì sao "
        "một cuộc chiến thương mại lại ảnh hưởng đến giá xăng ở Việt Nam.\n\n"
        "Sau khóa học này, bạn sẽ đọc được bài phân tích về tariff và quota bằng tiếng Anh "
        "mà không cần dừng lại tra từ, tự tin giải thích vì sao một quốc gia áp dụng sanction "
        "hay anti-dumping duty, và viết được những câu phân tích sắc bén về chính sách thương mại.\n\n"
        "18 từ vựng — từ tariff đến compliance — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy về thương mại quốc tế, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về rào cản thương mại — "
            "những công cụ mà các quốc gia sử dụng để kiểm soát dòng chảy hàng hóa qua biên giới. "
            "Bạn sẽ học tariff, quota, embargo, sanction, dumping, countervailing trong phần đầu tiên, "
            "nơi bài đọc giải thích cách thuế quan và hạn ngạch ảnh hưởng đến giá cả hàng nhập khẩu. "
            "Tiếp theo là barrier, non-tariff, standard, certification, licensing, restriction — "
            "những rào cản phi thuế quan tinh vi mà nhiều quốc gia sử dụng để bảo hộ sản xuất trong nước. "
            "Cuối cùng, retaliation, safeguard, anti-dumping, preferential, exemption, compliance "
            "đưa bạn vào thế giới của các biện pháp phòng vệ thương mại và hiệp định ưu đãi. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu các bài phân tích về chính sách thương mại quốc tế bằng tiếng Anh — "
            "không cần tra từ điển mỗi dòng."
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
                    "description": "Chào mừng bạn đến với bài học về rào cản thương mại — thuế quan, hạn ngạch và trừng phạt.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ hai trong chuỗi từ vựng Thương mại quốc tế — "
                            "chủ đề hôm nay là Rào cản thương mại, hay trong tiếng Anh là Trade Barriers. "
                            "Nếu bài trước bạn đã học về lý thuyết thương mại và lợi thế so sánh, "
                            "thì bài này sẽ cho bạn thấy thực tế phức tạp hơn nhiều — "
                            "các quốc gia không phải lúc nào cũng để hàng hóa tự do qua biên giới.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: tariff, quota, embargo, sanction, dumping, và countervailing. "
                            "Đây là những công cụ trực tiếp nhất mà chính phủ sử dụng để kiểm soát thương mại quốc tế.\n\n"
                            "Từ đầu tiên là tariff — danh từ — nghĩa là thuế quan, "
                            "khoản thuế mà chính phủ đánh vào hàng hóa nhập khẩu khi chúng đi qua biên giới. "
                            "Ví dụ: 'The government imposed a twenty-five percent tariff on imported steel to protect domestic manufacturers.' "
                            "Trong bài đọc, bạn sẽ thấy tariff là công cụ phổ biến nhất — "
                            "nó làm tăng giá hàng nhập khẩu, khiến hàng nội địa trở nên cạnh tranh hơn.\n\n"
                            "Từ thứ hai là quota — danh từ — nghĩa là hạn ngạch, "
                            "giới hạn về số lượng hàng hóa được phép nhập khẩu trong một khoảng thời gian. "
                            "Ví dụ: 'The country set a quota allowing only fifty thousand tons of sugar to be imported each year.' "
                            "Trong bài đọc, quota khác với tariff ở chỗ nó giới hạn trực tiếp số lượng "
                            "thay vì tăng giá.\n\n"
                            "Từ thứ ba là embargo — danh từ — nghĩa là lệnh cấm vận, "
                            "lệnh cấm hoàn toàn việc giao thương với một quốc gia hoặc một loại hàng hóa cụ thể. "
                            "Ví dụ: 'The United Nations imposed an embargo on arms sales to the conflict zone.' "
                            "Trong bài đọc, embargo là biện pháp mạnh nhất — "
                            "không phải giới hạn hay đánh thuế, mà là cấm hoàn toàn.\n\n"
                            "Từ thứ tư là sanction — danh từ — nghĩa là biện pháp trừng phạt kinh tế, "
                            "hạn chế thương mại hoặc tài chính mà một quốc gia áp đặt lên quốc gia khác "
                            "vì lý do chính trị hoặc an ninh. "
                            "Ví dụ: 'Economic sanctions against the country included freezing bank accounts and banning oil exports.' "
                            "Trong bài đọc, sanction thường đi kèm với embargo — "
                            "cả hai đều là công cụ ngoại giao sử dụng thương mại làm đòn bẩy.\n\n"
                            "Từ thứ năm là dumping — danh từ — nghĩa là bán phá giá, "
                            "khi một công ty xuất khẩu hàng hóa sang nước khác với giá thấp hơn giá thành sản xuất "
                            "hoặc thấp hơn giá bán tại thị trường nội địa. "
                            "Ví dụ: 'The steel industry accused foreign producers of dumping cheap steel on the domestic market.' "
                            "Trong bài đọc, dumping được coi là hành vi cạnh tranh không lành mạnh — "
                            "nó có thể phá hủy ngành sản xuất nội địa.\n\n"
                            "Từ cuối cùng là countervailing — tính từ — nghĩa là đối kháng hoặc bù trừ, "
                            "thường dùng trong cụm 'countervailing duty' — thuế chống trợ cấp, "
                            "loại thuế đánh vào hàng nhập khẩu được chính phủ nước xuất khẩu trợ cấp. "
                            "Ví dụ: 'The trade commission imposed countervailing duties on subsidized solar panels from abroad.' "
                            "Trong bài đọc, countervailing duty là phản ứng của quốc gia nhập khẩu "
                            "khi phát hiện hàng hóa được trợ cấp không công bằng.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về thuế quan và hạn ngạch để thấy các từ này trong ngữ cảnh thực tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thuế quan, hạn ngạch và trừng phạt",
                    "description": "Học 6 từ: tariff, quota, embargo, sanction, dumping, countervailing",
                    "data": {"vocabList": ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thuế quan, hạn ngạch và trừng phạt",
                    "description": "Học 6 từ: tariff, quota, embargo, sanction, dumping, countervailing",
                    "data": {"vocabList": ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thuế quan, hạn ngạch và trừng phạt",
                    "description": "Học 6 từ: tariff, quota, embargo, sanction, dumping, countervailing",
                    "data": {"vocabList": ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thuế quan, hạn ngạch và trừng phạt",
                    "description": "Học 6 từ: tariff, quota, embargo, sanction, dumping, countervailing",
                    "data": {"vocabList": ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Thuế quan, hạn ngạch và trừng phạt",
                    "description": "Học 6 từ: tariff, quota, embargo, sanction, dumping, countervailing",
                    "data": {"vocabList": ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thuế quan và hạn ngạch trong thương mại quốc tế",
                    "description": "When goods cross international borders, they rarely travel freely.",
                    "data": {
                        "text": (
                            "When goods cross international borders, they rarely travel freely. "
                            "Governments around the world use a variety of tools to control what comes in and what goes out. "
                            "The most common of these tools is the tariff — a tax placed on imported goods.\n\n"
                            "A tariff works by raising the price of foreign products. "
                            "Suppose a Vietnamese shoe factory sells a pair of shoes for two hundred thousand dong. "
                            "A foreign competitor can produce the same shoes for one hundred and fifty thousand dong. "
                            "Without any tariff, consumers would choose the cheaper foreign shoes. "
                            "But if the government places a thirty percent tariff on imported footwear, "
                            "the foreign shoes now cost nearly two hundred thousand dong — "
                            "making the domestic product competitive again. "
                            "Tariffs protect local industries, but they also mean consumers pay higher prices.\n\n"
                            "Another tool is the quota — a limit on the quantity of a good that can be imported. "
                            "Unlike a tariff, which raises prices, a quota directly restricts the amount. "
                            "For example, a country might set a quota of ten thousand tons of imported rice per year. "
                            "Once that limit is reached, no more rice can enter the country until the next year. "
                            "Quotas give domestic producers a guaranteed share of the market.\n\n"
                            "In extreme cases, a government may impose an embargo — "
                            "a complete ban on trade with a particular country or on a specific product. "
                            "An embargo is the strongest form of trade restriction. "
                            "It is often used for political or security reasons rather than economic ones. "
                            "When one country threatens another's interests, "
                            "an embargo can cut off all commercial ties.\n\n"
                            "Closely related to embargoes are sanctions — "
                            "economic penalties imposed on a country to pressure it into changing its behavior. "
                            "A sanction might freeze bank accounts, ban certain exports, "
                            "or prohibit companies from doing business with the targeted nation. "
                            "Sanctions are a tool of foreign policy that uses trade as leverage.\n\n"
                            "Sometimes trade disputes arise not from government policy but from company behavior. "
                            "Dumping occurs when a foreign company sells goods in another country "
                            "at a price below its production cost or below the price it charges at home. "
                            "Dumping can destroy local industries because domestic firms cannot compete "
                            "with artificially low prices. "
                            "To fight back, the importing country may impose a countervailing duty — "
                            "an extra tax designed to offset the unfair price advantage. "
                            "Countervailing duties level the playing field "
                            "by raising the price of dumped or subsidized goods back to a fair level."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thuế quan và hạn ngạch trong thương mại quốc tế",
                    "description": "When goods cross international borders, they rarely travel freely.",
                    "data": {
                        "text": (
                            "When goods cross international borders, they rarely travel freely. "
                            "Governments around the world use a variety of tools to control what comes in and what goes out. "
                            "The most common of these tools is the tariff — a tax placed on imported goods.\n\n"
                            "A tariff works by raising the price of foreign products. "
                            "Suppose a Vietnamese shoe factory sells a pair of shoes for two hundred thousand dong. "
                            "A foreign competitor can produce the same shoes for one hundred and fifty thousand dong. "
                            "Without any tariff, consumers would choose the cheaper foreign shoes. "
                            "But if the government places a thirty percent tariff on imported footwear, "
                            "the foreign shoes now cost nearly two hundred thousand dong — "
                            "making the domestic product competitive again. "
                            "Tariffs protect local industries, but they also mean consumers pay higher prices.\n\n"
                            "Another tool is the quota — a limit on the quantity of a good that can be imported. "
                            "Unlike a tariff, which raises prices, a quota directly restricts the amount. "
                            "For example, a country might set a quota of ten thousand tons of imported rice per year. "
                            "Once that limit is reached, no more rice can enter the country until the next year. "
                            "Quotas give domestic producers a guaranteed share of the market.\n\n"
                            "In extreme cases, a government may impose an embargo — "
                            "a complete ban on trade with a particular country or on a specific product. "
                            "An embargo is the strongest form of trade restriction. "
                            "It is often used for political or security reasons rather than economic ones. "
                            "When one country threatens another's interests, "
                            "an embargo can cut off all commercial ties.\n\n"
                            "Closely related to embargoes are sanctions — "
                            "economic penalties imposed on a country to pressure it into changing its behavior. "
                            "A sanction might freeze bank accounts, ban certain exports, "
                            "or prohibit companies from doing business with the targeted nation. "
                            "Sanctions are a tool of foreign policy that uses trade as leverage.\n\n"
                            "Sometimes trade disputes arise not from government policy but from company behavior. "
                            "Dumping occurs when a foreign company sells goods in another country "
                            "at a price below its production cost or below the price it charges at home. "
                            "Dumping can destroy local industries because domestic firms cannot compete "
                            "with artificially low prices. "
                            "To fight back, the importing country may impose a countervailing duty — "
                            "an extra tax designed to offset the unfair price advantage. "
                            "Countervailing duties level the playing field "
                            "by raising the price of dumped or subsidized goods back to a fair level."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thuế quan và hạn ngạch trong thương mại quốc tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When goods cross international borders, they rarely travel freely. "
                            "Governments around the world use a variety of tools to control what comes in and what goes out. "
                            "The most common of these tools is the tariff — a tax placed on imported goods.\n\n"
                            "A tariff works by raising the price of foreign products. "
                            "Suppose a Vietnamese shoe factory sells a pair of shoes for two hundred thousand dong. "
                            "A foreign competitor can produce the same shoes for one hundred and fifty thousand dong. "
                            "Without any tariff, consumers would choose the cheaper foreign shoes. "
                            "But if the government places a thirty percent tariff on imported footwear, "
                            "the foreign shoes now cost nearly two hundred thousand dong — "
                            "making the domestic product competitive again. "
                            "Tariffs protect local industries, but they also mean consumers pay higher prices.\n\n"
                            "Another tool is the quota — a limit on the quantity of a good that can be imported. "
                            "Unlike a tariff, which raises prices, a quota directly restricts the amount. "
                            "For example, a country might set a quota of ten thousand tons of imported rice per year. "
                            "Once that limit is reached, no more rice can enter the country until the next year. "
                            "Quotas give domestic producers a guaranteed share of the market.\n\n"
                            "In extreme cases, a government may impose an embargo — "
                            "a complete ban on trade with a particular country or on a specific product. "
                            "An embargo is the strongest form of trade restriction. "
                            "It is often used for political or security reasons rather than economic ones. "
                            "When one country threatens another's interests, "
                            "an embargo can cut off all commercial ties.\n\n"
                            "Closely related to embargoes are sanctions — "
                            "economic penalties imposed on a country to pressure it into changing its behavior. "
                            "A sanction might freeze bank accounts, ban certain exports, "
                            "or prohibit companies from doing business with the targeted nation. "
                            "Sanctions are a tool of foreign policy that uses trade as leverage.\n\n"
                            "Sometimes trade disputes arise not from government policy but from company behavior. "
                            "Dumping occurs when a foreign company sells goods in another country "
                            "at a price below its production cost or below the price it charges at home. "
                            "Dumping can destroy local industries because domestic firms cannot compete "
                            "with artificially low prices. "
                            "To fight back, the importing country may impose a countervailing duty — "
                            "an extra tax designed to offset the unfair price advantage. "
                            "Countervailing duties level the playing field "
                            "by raising the price of dumped or subsidized goods back to a fair level."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thuế quan, hạn ngạch và trừng phạt",
                    "description": "Viết câu sử dụng 6 từ vựng về thuế quan và rào cản thương mại trực tiếp.",
                    "data": {
                        "vocabList": ["tariff", "quota", "embargo", "sanction", "dumping", "countervailing"],
                        "items": [
                            {
                                "targetVocab": "tariff",
                                "prompt": "Dùng từ 'tariff' để viết một câu về tác động của thuế quan đến giá hàng nhập khẩu mà người tiêu dùng phải trả. Ví dụ: The new tariff on imported electronics raised the price of smartphones by fifteen percent, making domestic brands more attractive to budget-conscious buyers."
                            },
                            {
                                "targetVocab": "quota",
                                "prompt": "Dùng từ 'quota' để viết một câu về việc chính phủ giới hạn số lượng hàng hóa nhập khẩu để bảo vệ ngành sản xuất trong nước. Ví dụ: The government set a strict quota on imported sugar, allowing only thirty thousand tons per year to enter the country."
                            },
                            {
                                "targetVocab": "embargo",
                                "prompt": "Dùng từ 'embargo' để viết một câu về lệnh cấm vận thương mại giữa hai quốc gia vì lý do chính trị. Ví dụ: The trade embargo prevented any commercial ships from delivering goods to the sanctioned nation for over a decade."
                            },
                            {
                                "targetVocab": "sanction",
                                "prompt": "Dùng từ 'sanction' để viết một câu về biện pháp trừng phạt kinh tế mà cộng đồng quốc tế áp dụng. Ví dụ: International sanctions froze the country's overseas bank accounts and banned its airlines from landing at foreign airports."
                            },
                            {
                                "targetVocab": "dumping",
                                "prompt": "Dùng từ 'dumping' để viết một câu về hành vi bán phá giá của doanh nghiệp nước ngoài trên thị trường nội địa. Ví dụ: Local textile manufacturers filed a complaint alleging that foreign competitors were dumping cheap fabric at prices far below production cost."
                            },
                            {
                                "targetVocab": "countervailing",
                                "prompt": "Dùng từ 'countervailing' để viết một câu về thuế chống trợ cấp mà chính phủ áp dụng để bảo vệ ngành sản xuất nội địa. Ví dụ: The trade ministry imposed countervailing duties on subsidized fertilizer imports after an investigation confirmed unfair government support."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về rào cản phi thuế quan.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng về các công cụ "
                            "trực tiếp nhất trong thương mại quốc tế: "
                            "tariff — thuế quan, quota — hạn ngạch, embargo — lệnh cấm vận, "
                            "sanction — biện pháp trừng phạt, dumping — bán phá giá, "
                            "và countervailing — đối kháng, thường dùng trong 'countervailing duty'. "
                            "Đó là những rào cản mà bạn có thể nhìn thấy rõ ràng — "
                            "thuế, hạn ngạch, lệnh cấm.\n\n"
                            "Nhưng trong thương mại quốc tế hiện đại, nhiều rào cản tinh vi hơn nhiều. "
                            "Trong phần 2, bạn sẽ học 6 từ mới: barrier, non-tariff, standard, certification, "
                            "licensing, và restriction. Đây là những rào cản 'ẩn' — "
                            "không phải thuế, không phải hạn ngạch, nhưng vẫn ngăn hàng hóa vào thị trường.\n\n"
                            "Từ đầu tiên là barrier — danh từ — nghĩa là rào cản, "
                            "bất kỳ trở ngại nào ngăn cản hoặc hạn chế dòng chảy thương mại giữa các quốc gia. "
                            "Ví dụ: 'Trade barriers between the two countries have made it difficult for small businesses to export their products.' "
                            "Trong bài đọc, barrier là thuật ngữ chung bao gồm cả thuế quan lẫn phi thuế quan.\n\n"
                            "Từ thứ hai là non-tariff — tính từ — nghĩa là phi thuế quan, "
                            "mô tả các rào cản thương mại không phải là thuế nhập khẩu. "
                            "Ví dụ: 'Non-tariff barriers such as safety regulations and labeling requirements can be just as effective as tariffs in limiting imports.' "
                            "Trong bài đọc, non-tariff barriers là trọng tâm — "
                            "chúng ngày càng phổ biến hơn khi các hiệp định thương mại cắt giảm thuế quan.\n\n"
                            "Từ thứ ba là standard — danh từ — nghĩa là tiêu chuẩn, "
                            "yêu cầu kỹ thuật mà sản phẩm phải đáp ứng để được bán tại một thị trường. "
                            "Ví dụ: 'European food safety standards require all imported meat to pass strict quality tests before it can be sold.' "
                            "Trong bài đọc, standard có thể vừa là biện pháp bảo vệ người tiêu dùng chính đáng, "
                            "vừa là rào cản thương mại trá hình.\n\n"
                            "Từ thứ tư là certification — danh từ — nghĩa là chứng nhận, "
                            "quy trình xác nhận rằng sản phẩm hoặc doanh nghiệp đáp ứng các tiêu chuẩn nhất định. "
                            "Ví dụ: 'Obtaining organic certification for exported coffee requires months of inspections and paperwork.' "
                            "Trong bài đọc, certification là một bước bắt buộc — "
                            "nếu không có chứng nhận phù hợp, hàng hóa không thể vào thị trường.\n\n"
                            "Từ thứ năm là licensing — danh từ — nghĩa là cấp phép, "
                            "yêu cầu doanh nghiệp phải có giấy phép từ chính phủ để nhập khẩu hoặc xuất khẩu hàng hóa. "
                            "Ví dụ: 'The licensing process for importing pharmaceutical products can take up to six months in some countries.' "
                            "Trong bài đọc, licensing là một rào cản hành chính — "
                            "nó không cấm hàng hóa, nhưng làm chậm và tốn kém quá trình nhập khẩu.\n\n"
                            "Từ cuối cùng là restriction — danh từ — nghĩa là hạn chế, "
                            "bất kỳ quy định nào giới hạn hoạt động thương mại. "
                            "Ví dụ: 'Export restrictions on rare earth minerals have created supply shortages in the global electronics industry.' "
                            "Trong bài đọc, restriction là thuật ngữ rộng — "
                            "bao gồm mọi hình thức giới hạn từ quota đến licensing.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về rào cản phi thuế quan nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Rào cản phi thuế quan",
                    "description": "Học 6 từ: barrier, non-tariff, standard, certification, licensing, restriction",
                    "data": {"vocabList": ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Rào cản phi thuế quan",
                    "description": "Học 6 từ: barrier, non-tariff, standard, certification, licensing, restriction",
                    "data": {"vocabList": ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Rào cản phi thuế quan",
                    "description": "Học 6 từ: barrier, non-tariff, standard, certification, licensing, restriction",
                    "data": {"vocabList": ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Rào cản phi thuế quan",
                    "description": "Học 6 từ: barrier, non-tariff, standard, certification, licensing, restriction",
                    "data": {"vocabList": ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Rào cản phi thuế quan",
                    "description": "Học 6 từ: barrier, non-tariff, standard, certification, licensing, restriction",
                    "data": {"vocabList": ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Rào cản phi thuế quan — Bức tường vô hình",
                    "description": "As global trade agreements have reduced tariffs over the past decades, a different kind of trade barrier has grown in importance.",
                    "data": {
                        "text": (
                            "As global trade agreements have reduced tariffs over the past decades, "
                            "a different kind of trade barrier has grown in importance. "
                            "These are called non-tariff barriers, and they can be just as powerful as any tax.\n\n"
                            "A non-tariff barrier is any restriction on trade that does not take the form of a tariff. "
                            "While tariffs are transparent — everyone can see the tax rate — "
                            "non-tariff barriers are often hidden in regulations, paperwork, and technical requirements. "
                            "They create a barrier that foreign companies must overcome before their products "
                            "can reach consumers in another country.\n\n"
                            "One of the most common non-tariff barriers is the technical standard. "
                            "Every country has its own standards for product safety, quality, and labeling. "
                            "A Vietnamese seafood exporter, for example, must meet strict food safety standards "
                            "set by the European Union before selling shrimp in Europe. "
                            "These standards require specific testing methods, temperature controls during shipping, "
                            "and detailed labeling in the local language. "
                            "Meeting these standards costs time and money.\n\n"
                            "Closely related to standards is certification. "
                            "Certification is the process of proving that a product meets the required standards. "
                            "A coffee producer who wants to sell organic coffee in Japan "
                            "must obtain certification from an approved agency. "
                            "The certification process involves inspections, documentation, and fees. "
                            "For small producers, the cost of certification alone can be a significant barrier to entry.\n\n"
                            "Another form of non-tariff barrier is licensing. "
                            "Some countries require importers to obtain a license before they can bring in certain goods. "
                            "The licensing process may involve applications, waiting periods, and government approval. "
                            "In some cases, the number of licenses is limited, "
                            "effectively creating a quota without calling it one. "
                            "Licensing requirements can delay shipments by weeks or even months.\n\n"
                            "All of these measures fall under the broad category of trade restrictions. "
                            "A restriction is any rule or regulation that limits the free flow of goods across borders. "
                            "Some restrictions are genuinely designed to protect public health and safety. "
                            "Others are used strategically to protect domestic industries from foreign competition. "
                            "The challenge for trade negotiators is telling the difference between "
                            "a legitimate safety standard and a disguised barrier to trade."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Rào cản phi thuế quan — Bức tường vô hình",
                    "description": "As global trade agreements have reduced tariffs over the past decades, a different kind of trade barrier has grown in importance.",
                    "data": {
                        "text": (
                            "As global trade agreements have reduced tariffs over the past decades, "
                            "a different kind of trade barrier has grown in importance. "
                            "These are called non-tariff barriers, and they can be just as powerful as any tax.\n\n"
                            "A non-tariff barrier is any restriction on trade that does not take the form of a tariff. "
                            "While tariffs are transparent — everyone can see the tax rate — "
                            "non-tariff barriers are often hidden in regulations, paperwork, and technical requirements. "
                            "They create a barrier that foreign companies must overcome before their products "
                            "can reach consumers in another country.\n\n"
                            "One of the most common non-tariff barriers is the technical standard. "
                            "Every country has its own standards for product safety, quality, and labeling. "
                            "A Vietnamese seafood exporter, for example, must meet strict food safety standards "
                            "set by the European Union before selling shrimp in Europe. "
                            "These standards require specific testing methods, temperature controls during shipping, "
                            "and detailed labeling in the local language. "
                            "Meeting these standards costs time and money.\n\n"
                            "Closely related to standards is certification. "
                            "Certification is the process of proving that a product meets the required standards. "
                            "A coffee producer who wants to sell organic coffee in Japan "
                            "must obtain certification from an approved agency. "
                            "The certification process involves inspections, documentation, and fees. "
                            "For small producers, the cost of certification alone can be a significant barrier to entry.\n\n"
                            "Another form of non-tariff barrier is licensing. "
                            "Some countries require importers to obtain a license before they can bring in certain goods. "
                            "The licensing process may involve applications, waiting periods, and government approval. "
                            "In some cases, the number of licenses is limited, "
                            "effectively creating a quota without calling it one. "
                            "Licensing requirements can delay shipments by weeks or even months.\n\n"
                            "All of these measures fall under the broad category of trade restrictions. "
                            "A restriction is any rule or regulation that limits the free flow of goods across borders. "
                            "Some restrictions are genuinely designed to protect public health and safety. "
                            "Others are used strategically to protect domestic industries from foreign competition. "
                            "The challenge for trade negotiators is telling the difference between "
                            "a legitimate safety standard and a disguised barrier to trade."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Rào cản phi thuế quan — Bức tường vô hình",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "As global trade agreements have reduced tariffs over the past decades, "
                            "a different kind of trade barrier has grown in importance. "
                            "These are called non-tariff barriers, and they can be just as powerful as any tax.\n\n"
                            "A non-tariff barrier is any restriction on trade that does not take the form of a tariff. "
                            "While tariffs are transparent — everyone can see the tax rate — "
                            "non-tariff barriers are often hidden in regulations, paperwork, and technical requirements. "
                            "They create a barrier that foreign companies must overcome before their products "
                            "can reach consumers in another country.\n\n"
                            "One of the most common non-tariff barriers is the technical standard. "
                            "Every country has its own standards for product safety, quality, and labeling. "
                            "A Vietnamese seafood exporter, for example, must meet strict food safety standards "
                            "set by the European Union before selling shrimp in Europe. "
                            "These standards require specific testing methods, temperature controls during shipping, "
                            "and detailed labeling in the local language. "
                            "Meeting these standards costs time and money.\n\n"
                            "Closely related to standards is certification. "
                            "Certification is the process of proving that a product meets the required standards. "
                            "A coffee producer who wants to sell organic coffee in Japan "
                            "must obtain certification from an approved agency. "
                            "The certification process involves inspections, documentation, and fees. "
                            "For small producers, the cost of certification alone can be a significant barrier to entry.\n\n"
                            "Another form of non-tariff barrier is licensing. "
                            "Some countries require importers to obtain a license before they can bring in certain goods. "
                            "The licensing process may involve applications, waiting periods, and government approval. "
                            "In some cases, the number of licenses is limited, "
                            "effectively creating a quota without calling it one. "
                            "Licensing requirements can delay shipments by weeks or even months.\n\n"
                            "All of these measures fall under the broad category of trade restrictions. "
                            "A restriction is any rule or regulation that limits the free flow of goods across borders. "
                            "Some restrictions are genuinely designed to protect public health and safety. "
                            "Others are used strategically to protect domestic industries from foreign competition. "
                            "The challenge for trade negotiators is telling the difference between "
                            "a legitimate safety standard and a disguised barrier to trade."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Rào cản phi thuế quan",
                    "description": "Viết câu sử dụng 6 từ vựng về rào cản phi thuế quan.",
                    "data": {
                        "vocabList": ["barrier", "non-tariff", "standard", "certification", "licensing", "restriction"],
                        "items": [
                            {
                                "targetVocab": "barrier",
                                "prompt": "Dùng từ 'barrier' để viết một câu về trở ngại mà doanh nghiệp xuất khẩu gặp phải khi tiếp cận thị trường nước ngoài. Ví dụ: Language differences and complex customs procedures create significant barriers for Vietnamese small businesses trying to export to European markets."
                            },
                            {
                                "targetVocab": "non-tariff",
                                "prompt": "Dùng từ 'non-tariff' để viết một câu về rào cản phi thuế quan ảnh hưởng đến thương mại quốc tế. Ví dụ: Non-tariff barriers such as packaging regulations and health inspections have replaced traditional tariffs as the main obstacle to free trade."
                            },
                            {
                                "targetVocab": "standard",
                                "prompt": "Dùng từ 'standard' để viết một câu về tiêu chuẩn kỹ thuật mà sản phẩm xuất khẩu phải đáp ứng. Ví dụ: Vietnamese shrimp exporters must comply with strict hygiene standards set by the Japanese government before their products can enter the market."
                            },
                            {
                                "targetVocab": "certification",
                                "prompt": "Dùng từ 'certification' để viết một câu về quy trình chứng nhận sản phẩm để đáp ứng yêu cầu thị trường quốc tế. Ví dụ: The organic certification process requires farmers to document every step of production, from planting to packaging."
                            },
                            {
                                "targetVocab": "licensing",
                                "prompt": "Dùng từ 'licensing' để viết một câu về yêu cầu cấp phép nhập khẩu mà doanh nghiệp phải tuân thủ. Ví dụ: The licensing requirement for importing medical equipment adds three months to the delivery timeline and increases costs for hospitals."
                            },
                            {
                                "targetVocab": "restriction",
                                "prompt": "Dùng từ 'restriction' để viết một câu về hạn chế thương mại ảnh hưởng đến chuỗi cung ứng toàn cầu. Ví dụ: Export restrictions on semiconductor chips have disrupted the global supply chain for smartphones and laptops."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về phòng vệ thương mại và tuân thủ.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 công cụ trực tiếp nhất: "
                            "tariff — thuế quan, quota — hạn ngạch, embargo — lệnh cấm vận, "
                            "sanction — biện pháp trừng phạt, dumping — bán phá giá, "
                            "và countervailing — đối kháng. "
                            "Trong phần 2, bạn đã học về rào cản phi thuế quan: "
                            "barrier — rào cản, non-tariff — phi thuế quan, standard — tiêu chuẩn, "
                            "certification — chứng nhận, licensing — cấp phép, và restriction — hạn chế.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào khía cạnh phức tạp nhất: "
                            "khi các quốc gia phản ứng lại rào cản thương mại, và khi luật chơi quốc tế "
                            "tạo ra cả ngoại lệ lẫn nghĩa vụ. "
                            "Bạn sẽ học 6 từ mới: retaliation, safeguard, anti-dumping, preferential, "
                            "exemption, và compliance.\n\n"
                            "Từ đầu tiên là retaliation — danh từ — nghĩa là trả đũa, "
                            "hành động đáp trả khi một quốc gia bị áp đặt rào cản thương mại bất công. "
                            "Ví dụ: 'In retaliation for the new tariffs on steel, the trading partner imposed tariffs on agricultural products.' "
                            "Trong bài đọc, retaliation là phản ứng dây chuyền — "
                            "khi một nước tăng thuế, nước kia đáp trả, và cuộc chiến thương mại bắt đầu.\n\n"
                            "Từ thứ hai là safeguard — danh từ — nghĩa là biện pháp tự vệ, "
                            "biện pháp tạm thời mà một quốc gia áp dụng để bảo vệ ngành sản xuất nội địa "
                            "khỏi sự gia tăng đột biến của hàng nhập khẩu. "
                            "Ví dụ: 'The government activated safeguard measures after imports of cheap textiles surged by two hundred percent in one year.' "
                            "Trong bài đọc, safeguard khác với tariff thông thường — "
                            "nó là biện pháp khẩn cấp, tạm thời, và phải tuân theo quy tắc quốc tế.\n\n"
                            "Từ thứ ba là anti-dumping — tính từ — nghĩa là chống bán phá giá, "
                            "mô tả các biện pháp nhằm ngăn chặn hành vi bán hàng dưới giá thành. "
                            "Ví dụ: 'The anti-dumping investigation found that imported tires were being sold at forty percent below their fair market value.' "
                            "Trong bài đọc, anti-dumping duty là phản ứng pháp lý — "
                            "quốc gia nhập khẩu điều tra và áp thuế bổ sung nếu phát hiện dumping.\n\n"
                            "Từ thứ tư là preferential — tính từ — nghĩa là ưu đãi, "
                            "mô tả điều kiện thương mại thuận lợi hơn dành cho một số đối tác nhất định. "
                            "Ví dụ: 'Under the free trade agreement, member countries enjoy preferential tariff rates that are much lower than standard rates.' "
                            "Trong bài đọc, preferential treatment là phần thưởng cho các quốc gia "
                            "tham gia hiệp định thương mại — họ được hưởng thuế thấp hơn.\n\n"
                            "Từ thứ năm là exemption — danh từ — nghĩa là miễn trừ, "
                            "quyền được miễn khỏi một quy định hoặc nghĩa vụ thương mại. "
                            "Ví dụ: 'Developing countries often receive exemptions from certain trade rules to give their industries time to grow.' "
                            "Trong bài đọc, exemption là ngoại lệ trong luật chơi — "
                            "không phải ai cũng phải tuân theo cùng một quy tắc.\n\n"
                            "Từ cuối cùng là compliance — danh từ — nghĩa là sự tuân thủ, "
                            "việc thực hiện đúng các quy định, tiêu chuẩn hoặc nghĩa vụ thương mại. "
                            "Ví dụ: 'Companies that fail to maintain compliance with international trade regulations face heavy fines and loss of export privileges.' "
                            "Trong bài đọc, compliance là yêu cầu bắt buộc — "
                            "dù bạn được ưu đãi hay miễn trừ, bạn vẫn phải tuân thủ các quy tắc cơ bản.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về phòng vệ thương mại và tuân thủ quốc tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phòng vệ thương mại và tuân thủ",
                    "description": "Học 6 từ: retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phòng vệ thương mại và tuân thủ",
                    "description": "Học 6 từ: retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phòng vệ thương mại và tuân thủ",
                    "description": "Học 6 từ: retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phòng vệ thương mại và tuân thủ",
                    "description": "Học 6 từ: retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phòng vệ thương mại và tuân thủ",
                    "description": "Học 6 từ: retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phòng vệ thương mại và luật chơi quốc tế",
                    "description": "International trade is governed by rules, but those rules also allow countries to defend themselves.",
                    "data": {
                        "text": (
                            "International trade is governed by rules, but those rules also allow countries "
                            "to defend themselves when trade becomes unfair. "
                            "The tools they use — safeguards, anti-dumping duties, and retaliation — "
                            "shape the landscape of global commerce.\n\n"
                            "When a country discovers that foreign companies are dumping goods — "
                            "selling them below cost to capture market share — it can launch an anti-dumping investigation. "
                            "If the investigation confirms that dumping is occurring and harming domestic producers, "
                            "the government can impose an anti-dumping duty. "
                            "This extra tax raises the price of the dumped goods to a fair level. "
                            "Anti-dumping measures are among the most frequently used trade defense tools in the world.\n\n"
                            "Sometimes the threat comes not from unfair pricing but from a sudden surge in imports. "
                            "A safeguard measure allows a country to temporarily restrict imports "
                            "when a domestic industry faces serious injury from an unexpected increase in foreign goods. "
                            "Unlike anti-dumping duties, safeguards do not require proof of unfair behavior — "
                            "they simply protect an industry that is overwhelmed by the volume of imports. "
                            "However, safeguard measures must be temporary and are subject to review.\n\n"
                            "Trade disputes often escalate through retaliation. "
                            "When one country imposes new tariffs or barriers, the affected country may respond in kind. "
                            "Retaliation can take many forms: higher tariffs on the first country's exports, "
                            "new restrictions on services, or even sanctions on specific companies. "
                            "A cycle of retaliation can quickly turn into a trade war, "
                            "where both sides suffer from higher prices and reduced trade.\n\n"
                            "Not all trade relationships are adversarial. "
                            "Many countries sign agreements that grant each other preferential treatment. "
                            "Preferential trade agreements reduce or eliminate tariffs between member countries, "
                            "giving their exporters an advantage over competitors from non-member nations. "
                            "Vietnam, for example, benefits from preferential tariff rates under agreements "
                            "with ASEAN, the European Union, and several other trading partners.\n\n"
                            "Within these agreements, some countries receive special exemptions. "
                            "An exemption frees a country from a particular obligation — "
                            "for instance, a developing nation might be exempt from reducing tariffs "
                            "on agricultural products for a certain number of years. "
                            "Exemptions recognize that not all countries start from the same position.\n\n"
                            "Whether a country enjoys preferential treatment or faces anti-dumping duties, "
                            "one requirement remains constant: compliance. "
                            "Compliance means following the rules — meeting standards, filing reports, "
                            "and honoring commitments made in trade agreements. "
                            "Countries and companies that fail to maintain compliance "
                            "risk losing their trade privileges, facing penalties, "
                            "or being taken to dispute resolution at the World Trade Organization."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phòng vệ thương mại và luật chơi quốc tế",
                    "description": "International trade is governed by rules, but those rules also allow countries to defend themselves.",
                    "data": {
                        "text": (
                            "International trade is governed by rules, but those rules also allow countries "
                            "to defend themselves when trade becomes unfair. "
                            "The tools they use — safeguards, anti-dumping duties, and retaliation — "
                            "shape the landscape of global commerce.\n\n"
                            "When a country discovers that foreign companies are dumping goods — "
                            "selling them below cost to capture market share — it can launch an anti-dumping investigation. "
                            "If the investigation confirms that dumping is occurring and harming domestic producers, "
                            "the government can impose an anti-dumping duty. "
                            "This extra tax raises the price of the dumped goods to a fair level. "
                            "Anti-dumping measures are among the most frequently used trade defense tools in the world.\n\n"
                            "Sometimes the threat comes not from unfair pricing but from a sudden surge in imports. "
                            "A safeguard measure allows a country to temporarily restrict imports "
                            "when a domestic industry faces serious injury from an unexpected increase in foreign goods. "
                            "Unlike anti-dumping duties, safeguards do not require proof of unfair behavior — "
                            "they simply protect an industry that is overwhelmed by the volume of imports. "
                            "However, safeguard measures must be temporary and are subject to review.\n\n"
                            "Trade disputes often escalate through retaliation. "
                            "When one country imposes new tariffs or barriers, the affected country may respond in kind. "
                            "Retaliation can take many forms: higher tariffs on the first country's exports, "
                            "new restrictions on services, or even sanctions on specific companies. "
                            "A cycle of retaliation can quickly turn into a trade war, "
                            "where both sides suffer from higher prices and reduced trade.\n\n"
                            "Not all trade relationships are adversarial. "
                            "Many countries sign agreements that grant each other preferential treatment. "
                            "Preferential trade agreements reduce or eliminate tariffs between member countries, "
                            "giving their exporters an advantage over competitors from non-member nations. "
                            "Vietnam, for example, benefits from preferential tariff rates under agreements "
                            "with ASEAN, the European Union, and several other trading partners.\n\n"
                            "Within these agreements, some countries receive special exemptions. "
                            "An exemption frees a country from a particular obligation — "
                            "for instance, a developing nation might be exempt from reducing tariffs "
                            "on agricultural products for a certain number of years. "
                            "Exemptions recognize that not all countries start from the same position.\n\n"
                            "Whether a country enjoys preferential treatment or faces anti-dumping duties, "
                            "one requirement remains constant: compliance. "
                            "Compliance means following the rules — meeting standards, filing reports, "
                            "and honoring commitments made in trade agreements. "
                            "Countries and companies that fail to maintain compliance "
                            "risk losing their trade privileges, facing penalties, "
                            "or being taken to dispute resolution at the World Trade Organization."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phòng vệ thương mại và luật chơi quốc tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "International trade is governed by rules, but those rules also allow countries "
                            "to defend themselves when trade becomes unfair. "
                            "The tools they use — safeguards, anti-dumping duties, and retaliation — "
                            "shape the landscape of global commerce.\n\n"
                            "When a country discovers that foreign companies are dumping goods — "
                            "selling them below cost to capture market share — it can launch an anti-dumping investigation. "
                            "If the investigation confirms that dumping is occurring and harming domestic producers, "
                            "the government can impose an anti-dumping duty. "
                            "This extra tax raises the price of the dumped goods to a fair level. "
                            "Anti-dumping measures are among the most frequently used trade defense tools in the world.\n\n"
                            "Sometimes the threat comes not from unfair pricing but from a sudden surge in imports. "
                            "A safeguard measure allows a country to temporarily restrict imports "
                            "when a domestic industry faces serious injury from an unexpected increase in foreign goods. "
                            "Unlike anti-dumping duties, safeguards do not require proof of unfair behavior — "
                            "they simply protect an industry that is overwhelmed by the volume of imports. "
                            "However, safeguard measures must be temporary and are subject to review.\n\n"
                            "Trade disputes often escalate through retaliation. "
                            "When one country imposes new tariffs or barriers, the affected country may respond in kind. "
                            "Retaliation can take many forms: higher tariffs on the first country's exports, "
                            "new restrictions on services, or even sanctions on specific companies. "
                            "A cycle of retaliation can quickly turn into a trade war, "
                            "where both sides suffer from higher prices and reduced trade.\n\n"
                            "Not all trade relationships are adversarial. "
                            "Many countries sign agreements that grant each other preferential treatment. "
                            "Preferential trade agreements reduce or eliminate tariffs between member countries, "
                            "giving their exporters an advantage over competitors from non-member nations. "
                            "Vietnam, for example, benefits from preferential tariff rates under agreements "
                            "with ASEAN, the European Union, and several other trading partners.\n\n"
                            "Within these agreements, some countries receive special exemptions. "
                            "An exemption frees a country from a particular obligation — "
                            "for instance, a developing nation might be exempt from reducing tariffs "
                            "on agricultural products for a certain number of years. "
                            "Exemptions recognize that not all countries start from the same position.\n\n"
                            "Whether a country enjoys preferential treatment or faces anti-dumping duties, "
                            "one requirement remains constant: compliance. "
                            "Compliance means following the rules — meeting standards, filing reports, "
                            "and honoring commitments made in trade agreements. "
                            "Countries and companies that fail to maintain compliance "
                            "risk losing their trade privileges, facing penalties, "
                            "or being taken to dispute resolution at the World Trade Organization."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phòng vệ thương mại và tuân thủ",
                    "description": "Viết câu sử dụng 6 từ vựng về phòng vệ thương mại.",
                    "data": {
                        "vocabList": ["retaliation", "safeguard", "anti-dumping", "preferential", "exemption", "compliance"],
                        "items": [
                            {
                                "targetVocab": "retaliation",
                                "prompt": "Dùng từ 'retaliation' để viết một câu về phản ứng trả đũa thương mại giữa hai quốc gia. Ví dụ: In retaliation for the increased tariffs on automobiles, the affected country raised import duties on agricultural products by twenty-five percent."
                            },
                            {
                                "targetVocab": "safeguard",
                                "prompt": "Dùng từ 'safeguard' để viết một câu về biện pháp tự vệ thương mại khi hàng nhập khẩu tăng đột biến. Ví dụ: The government imposed safeguard measures on imported steel after domestic factories reported a fifty percent drop in orders within six months."
                            },
                            {
                                "targetVocab": "anti-dumping",
                                "prompt": "Dùng từ 'anti-dumping' để viết một câu về cuộc điều tra chống bán phá giá đối với hàng nhập khẩu. Ví dụ: The anti-dumping investigation revealed that imported ceramic tiles were being sold at prices thirty percent below their production cost."
                            },
                            {
                                "targetVocab": "preferential",
                                "prompt": "Dùng từ 'preferential' để viết một câu về ưu đãi thuế quan trong hiệp định thương mại tự do. Ví dụ: Vietnamese coffee exporters enjoy preferential tariff rates in the European market thanks to the free trade agreement signed in 2020."
                            },
                            {
                                "targetVocab": "exemption",
                                "prompt": "Dùng từ 'exemption' để viết một câu về quyền miễn trừ mà các nước đang phát triển được hưởng trong thương mại quốc tế. Ví dụ: The trade agreement grants developing nations a five-year exemption from reducing tariffs on essential food products."
                            },
                            {
                                "targetVocab": "compliance",
                                "prompt": "Dùng từ 'compliance' để viết một câu về yêu cầu tuân thủ quy định thương mại quốc tế. Ví dụ: The company hired a dedicated team to ensure full compliance with the new export regulations before shipping goods overseas."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Rào cản thương mại. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những công cụ trực tiếp nhất: "
                            "tariff — thuế quan, quota — hạn ngạch, embargo — lệnh cấm vận, "
                            "sanction — biện pháp trừng phạt, dumping — bán phá giá, "
                            "và countervailing — đối kháng. "
                            "Đây là những vũ khí rõ ràng nhất trong kho công cụ thương mại.\n\n"
                            "Trong phần 2, bạn đã khám phá thế giới tinh vi hơn: "
                            "barrier — rào cản, non-tariff — phi thuế quan, standard — tiêu chuẩn, "
                            "certification — chứng nhận, licensing — cấp phép, và restriction — hạn chế. "
                            "Những rào cản này ẩn trong quy định và thủ tục hành chính.\n\n"
                            "Trong phần 3, bạn đã học về phản ứng và luật chơi: "
                            "retaliation — trả đũa, safeguard — biện pháp tự vệ, "
                            "anti-dumping — chống bán phá giá, preferential — ưu đãi, "
                            "exemption — miễn trừ, và compliance — tuân thủ. "
                            "Đây là cách các quốc gia vừa bảo vệ mình vừa hợp tác với nhau.\n\n"
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
                    "description": "Học 18 từ: tariff, quota, embargo, sanction, dumping, countervailing, barrier, non-tariff, standard, certification, licensing, restriction, retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: tariff, quota, embargo, sanction, dumping, countervailing, barrier, non-tariff, standard, certification, licensing, restriction, retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: tariff, quota, embargo, sanction, dumping, countervailing, barrier, non-tariff, standard, certification, licensing, restriction, retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: tariff, quota, embargo, sanction, dumping, countervailing, barrier, non-tariff, standard, certification, licensing, restriction, retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: tariff, quota, embargo, sanction, dumping, countervailing, barrier, non-tariff, standard, certification, licensing, restriction, retaliation, safeguard, anti-dumping, preferential, exemption, compliance",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng rào cản thương mại",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "tariff",
                                "prompt": "Dùng từ 'tariff' để viết một câu về thuế quan ảnh hưởng đến giá hàng tiêu dùng nhập khẩu tại Việt Nam. Ví dụ: The tariff on imported wine makes a bottle that costs ten dollars in France sell for nearly twenty dollars in Vietnamese stores."
                            },
                            {
                                "targetVocab": "quota",
                                "prompt": "Dùng từ 'quota' để viết một câu về hạn ngạch nhập khẩu ảnh hưởng đến nguồn cung trên thị trường nội địa. Ví dụ: Once the annual quota for imported automobiles is reached, car dealers must wait until January to place new orders from overseas."
                            },
                            {
                                "targetVocab": "embargo",
                                "prompt": "Dùng từ 'embargo' để viết một câu về tác động của lệnh cấm vận đến nền kinh tế của quốc gia bị trừng phạt. Ví dụ: The decades-long trade embargo severely limited the country's access to modern technology and medical equipment."
                            },
                            {
                                "targetVocab": "sanction",
                                "prompt": "Dùng từ 'sanction' để viết một câu về biện pháp trừng phạt kinh tế và tác động đến doanh nghiệp quốc tế. Ví dụ: International sanctions forced multinational companies to withdraw their operations from the targeted country within ninety days."
                            },
                            {
                                "targetVocab": "dumping",
                                "prompt": "Dùng từ 'dumping' để viết một câu về hành vi bán phá giá ảnh hưởng đến ngành sản xuất nội địa Việt Nam. Ví dụ: Vietnamese steel producers accused foreign competitors of dumping low-quality steel at prices that made it impossible for local factories to compete."
                            },
                            {
                                "targetVocab": "countervailing",
                                "prompt": "Dùng từ 'countervailing' để viết một câu về thuế chống trợ cấp áp dụng cho hàng nhập khẩu được chính phủ nước ngoài hỗ trợ. Ví dụ: The trade commission imposed countervailing duties of eighteen percent on imported paper products after confirming they received government subsidies."
                            },
                            {
                                "targetVocab": "barrier",
                                "prompt": "Dùng từ 'barrier' để viết một câu về rào cản thương mại ảnh hưởng đến doanh nghiệp nhỏ muốn xuất khẩu. Ví dụ: High shipping costs and complex customs paperwork create significant barriers for small Vietnamese craft businesses trying to sell products in Europe."
                            },
                            {
                                "targetVocab": "non-tariff",
                                "prompt": "Dùng từ 'non-tariff' để viết một câu so sánh rào cản phi thuế quan với thuế quan truyền thống. Ví dụ: While tariffs have decreased under free trade agreements, non-tariff barriers such as technical regulations have actually increased in many countries."
                            },
                            {
                                "targetVocab": "standard",
                                "prompt": "Dùng từ 'standard' để viết một câu về tiêu chuẩn chất lượng mà hàng xuất khẩu Việt Nam phải đáp ứng. Ví dụ: Vietnamese pepper exporters must meet strict pesticide residue standards set by the European Union before their products can be sold in EU supermarkets."
                            },
                            {
                                "targetVocab": "certification",
                                "prompt": "Dùng từ 'certification' để viết một câu về chi phí và thời gian cần thiết để đạt chứng nhận quốc tế. Ví dụ: Obtaining fair-trade certification for a coffee cooperative requires at least one year of documentation and multiple on-site inspections."
                            },
                            {
                                "targetVocab": "licensing",
                                "prompt": "Dùng từ 'licensing' để viết một câu về yêu cầu cấp phép nhập khẩu gây khó khăn cho doanh nghiệp. Ví dụ: The complex licensing process for importing medical devices has delayed the arrival of critical hospital equipment by several months."
                            },
                            {
                                "targetVocab": "restriction",
                                "prompt": "Dùng từ 'restriction' để viết một câu về hạn chế xuất khẩu ảnh hưởng đến chuỗi cung ứng toàn cầu. Ví dụ: Export restrictions on rare minerals have forced electronics manufacturers to find alternative materials or new suppliers in other countries."
                            },
                            {
                                "targetVocab": "retaliation",
                                "prompt": "Dùng từ 'retaliation' để viết một câu về vòng xoáy trả đũa thương mại giữa hai nền kinh tế lớn. Ví dụ: The cycle of retaliation between the two largest economies raised prices for consumers on both sides and disrupted global supply chains."
                            },
                            {
                                "targetVocab": "safeguard",
                                "prompt": "Dùng từ 'safeguard' để viết một câu về biện pháp tự vệ thương mại bảo vệ ngành sản xuất nội địa. Ví dụ: The government activated safeguard measures on imported dairy products after local farmers reported a sharp decline in milk prices."
                            },
                            {
                                "targetVocab": "anti-dumping",
                                "prompt": "Dùng từ 'anti-dumping' để viết một câu về thuế chống bán phá giá áp dụng cho một sản phẩm cụ thể. Ví dụ: The anti-dumping duty of thirty-five percent on imported plywood helped Vietnamese wood manufacturers recover their market share."
                            },
                            {
                                "targetVocab": "preferential",
                                "prompt": "Dùng từ 'preferential' để viết một câu về lợi ích mà doanh nghiệp Việt Nam được hưởng từ hiệp định thương mại. Ví dụ: Thanks to preferential trade terms under the CPTPP agreement, Vietnamese garment exports to Canada now face zero tariffs on most product categories."
                            },
                            {
                                "targetVocab": "exemption",
                                "prompt": "Dùng từ 'exemption' để viết một câu về quyền miễn trừ thuế quan cho các nước đang phát triển. Ví dụ: The exemption from import duties on educational materials allows schools in developing countries to access textbooks at affordable prices."
                            },
                            {
                                "targetVocab": "compliance",
                                "prompt": "Dùng từ 'compliance' để viết một câu về tầm quan trọng của việc tuân thủ quy định thương mại quốc tế. Ví dụ: Maintaining compliance with international food safety regulations is essential for Vietnamese seafood companies that want to keep their export licenses."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về rào cản thương mại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về rào cản thương mại — từ thuế quan và hạn ngạch "
                            "đến rào cản phi thuế quan và phòng vệ thương mại.\n\n"
                            "Bạn sẽ gặp lại tariff, quota, embargo, sanction, dumping, countervailing "
                            "trong phần mở đầu về các công cụ kiểm soát thương mại. "
                            "Tiếp theo, barrier, non-tariff, standard, certification, licensing, restriction "
                            "sẽ cho bạn thấy những rào cản ẩn trong quy định và thủ tục. "
                            "Và cuối cùng, retaliation, safeguard, anti-dumping, preferential, exemption, compliance "
                            "sẽ đưa bạn vào thế giới phòng vệ thương mại và hợp tác quốc tế.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Rào cản thương mại — Bức tranh toàn cảnh",
                    "description": "No country in the world trades completely freely.",
                    "data": {
                        "text": (
                            "No country in the world trades completely freely. "
                            "Even the most open economies maintain some form of barrier "
                            "to control the flow of goods across their borders. "
                            "Understanding these barriers — why they exist, how they work, "
                            "and what happens when countries fight over them — "
                            "is essential for anyone studying international trade.\n\n"
                            "The most visible barrier is the tariff. "
                            "A tariff is a tax on imported goods, and it serves two purposes: "
                            "it raises revenue for the government, and it protects domestic producers "
                            "by making foreign products more expensive. "
                            "When a country places a tariff on imported clothing, for example, "
                            "local textile factories gain an advantage because consumers now find "
                            "domestic products relatively cheaper.\n\n"
                            "Governments also use quotas to limit the quantity of imports. "
                            "A quota sets a maximum amount of a product that can enter the country. "
                            "Once the quota is filled, no more of that product can be imported "
                            "until the next period begins. "
                            "In the most extreme cases, a government may impose an embargo — "
                            "a total ban on trade with a specific country. "
                            "Embargoes are often accompanied by broader sanctions, "
                            "which may include freezing financial assets, banning travel, "
                            "and cutting off diplomatic relations. "
                            "A sanction uses economic pressure to achieve political goals.\n\n"
                            "Not all unfair trade practices come from governments. "
                            "Sometimes foreign companies engage in dumping — "
                            "selling goods in another country at prices below their cost of production. "
                            "Dumping can devastate local industries that cannot match the artificially low prices. "
                            "To counter this, importing countries may impose a countervailing duty — "
                            "an additional tax that offsets the unfair price advantage "
                            "created by dumping or foreign government subsidies.\n\n"
                            "As international agreements have lowered tariffs around the world, "
                            "non-tariff barriers have become increasingly important. "
                            "These include technical standards that products must meet, "
                            "certification requirements that exporters must obtain, "
                            "and licensing procedures that importers must complete. "
                            "A Vietnamese furniture maker who wants to sell tables in Australia, for instance, "
                            "must ensure the wood meets Australian environmental standards, "
                            "obtain the proper certification from an approved testing laboratory, "
                            "and navigate the licensing process required by Australian customs. "
                            "Each of these steps adds cost and time, creating a restriction "
                            "that functions much like a tariff — even though no tax is involved.\n\n"
                            "When one country feels that another's trade barriers are unfair, "
                            "it may respond with retaliation. "
                            "Retaliation typically means imposing new tariffs or restrictions "
                            "on the offending country's exports. "
                            "A cycle of retaliation can escalate into a full trade war, "
                            "where both countries raise barriers higher and higher, "
                            "hurting consumers and businesses on both sides.\n\n"
                            "International trade law provides tools to manage these conflicts. "
                            "A country can invoke safeguard measures to temporarily protect "
                            "a domestic industry that is being overwhelmed by a surge in imports. "
                            "It can also launch an anti-dumping investigation "
                            "to determine whether foreign goods are being sold below fair value. "
                            "If the investigation confirms dumping, the country can impose anti-dumping duties "
                            "to restore fair competition.\n\n"
                            "Trade agreements create a framework for cooperation. "
                            "Countries that sign free trade agreements grant each other preferential treatment — "
                            "lower tariffs, simplified customs procedures, and mutual recognition of standards. "
                            "Within these agreements, developing countries often receive exemptions "
                            "that allow them more time to open their markets. "
                            "An exemption acknowledges that poorer nations need extra support "
                            "to compete on the global stage.\n\n"
                            "But preferential treatment and exemptions come with obligations. "
                            "Every member of a trade agreement must maintain compliance "
                            "with the rules they have agreed to follow. "
                            "Compliance means meeting standards, honoring commitments, "
                            "and submitting to dispute resolution when disagreements arise. "
                            "A country that fails to comply risks losing its preferential access "
                            "and facing penalties from its trading partners.\n\n"
                            "The world of trade barriers is complex, but it comes down to a fundamental tension: "
                            "every country wants the benefits of free trade — lower prices, more choices, "
                            "and access to global markets — but every country also wants to protect "
                            "its own workers, industries, and strategic interests. "
                            "The tools of trade policy — tariffs, quotas, standards, safeguards, "
                            "and the agreements that govern them — are how nations navigate this tension."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Rào cản thương mại — Bức tranh toàn cảnh",
                    "description": "No country in the world trades completely freely.",
                    "data": {
                        "text": (
                            "No country in the world trades completely freely. "
                            "Even the most open economies maintain some form of barrier "
                            "to control the flow of goods across their borders. "
                            "Understanding these barriers — why they exist, how they work, "
                            "and what happens when countries fight over them — "
                            "is essential for anyone studying international trade.\n\n"
                            "The most visible barrier is the tariff. "
                            "A tariff is a tax on imported goods, and it serves two purposes: "
                            "it raises revenue for the government, and it protects domestic producers "
                            "by making foreign products more expensive. "
                            "When a country places a tariff on imported clothing, for example, "
                            "local textile factories gain an advantage because consumers now find "
                            "domestic products relatively cheaper.\n\n"
                            "Governments also use quotas to limit the quantity of imports. "
                            "A quota sets a maximum amount of a product that can enter the country. "
                            "Once the quota is filled, no more of that product can be imported "
                            "until the next period begins. "
                            "In the most extreme cases, a government may impose an embargo — "
                            "a total ban on trade with a specific country. "
                            "Embargoes are often accompanied by broader sanctions, "
                            "which may include freezing financial assets, banning travel, "
                            "and cutting off diplomatic relations. "
                            "A sanction uses economic pressure to achieve political goals.\n\n"
                            "Not all unfair trade practices come from governments. "
                            "Sometimes foreign companies engage in dumping — "
                            "selling goods in another country at prices below their cost of production. "
                            "Dumping can devastate local industries that cannot match the artificially low prices. "
                            "To counter this, importing countries may impose a countervailing duty — "
                            "an additional tax that offsets the unfair price advantage "
                            "created by dumping or foreign government subsidies.\n\n"
                            "As international agreements have lowered tariffs around the world, "
                            "non-tariff barriers have become increasingly important. "
                            "These include technical standards that products must meet, "
                            "certification requirements that exporters must obtain, "
                            "and licensing procedures that importers must complete. "
                            "A Vietnamese furniture maker who wants to sell tables in Australia, for instance, "
                            "must ensure the wood meets Australian environmental standards, "
                            "obtain the proper certification from an approved testing laboratory, "
                            "and navigate the licensing process required by Australian customs. "
                            "Each of these steps adds cost and time, creating a restriction "
                            "that functions much like a tariff — even though no tax is involved.\n\n"
                            "When one country feels that another's trade barriers are unfair, "
                            "it may respond with retaliation. "
                            "Retaliation typically means imposing new tariffs or restrictions "
                            "on the offending country's exports. "
                            "A cycle of retaliation can escalate into a full trade war, "
                            "where both countries raise barriers higher and higher, "
                            "hurting consumers and businesses on both sides.\n\n"
                            "International trade law provides tools to manage these conflicts. "
                            "A country can invoke safeguard measures to temporarily protect "
                            "a domestic industry that is being overwhelmed by a surge in imports. "
                            "It can also launch an anti-dumping investigation "
                            "to determine whether foreign goods are being sold below fair value. "
                            "If the investigation confirms dumping, the country can impose anti-dumping duties "
                            "to restore fair competition.\n\n"
                            "Trade agreements create a framework for cooperation. "
                            "Countries that sign free trade agreements grant each other preferential treatment — "
                            "lower tariffs, simplified customs procedures, and mutual recognition of standards. "
                            "Within these agreements, developing countries often receive exemptions "
                            "that allow them more time to open their markets. "
                            "An exemption acknowledges that poorer nations need extra support "
                            "to compete on the global stage.\n\n"
                            "But preferential treatment and exemptions come with obligations. "
                            "Every member of a trade agreement must maintain compliance "
                            "with the rules they have agreed to follow. "
                            "Compliance means meeting standards, honoring commitments, "
                            "and submitting to dispute resolution when disagreements arise. "
                            "A country that fails to comply risks losing its preferential access "
                            "and facing penalties from its trading partners.\n\n"
                            "The world of trade barriers is complex, but it comes down to a fundamental tension: "
                            "every country wants the benefits of free trade — lower prices, more choices, "
                            "and access to global markets — but every country also wants to protect "
                            "its own workers, industries, and strategic interests. "
                            "The tools of trade policy — tariffs, quotas, standards, safeguards, "
                            "and the agreements that govern them — are how nations navigate this tension."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Rào cản thương mại — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "No country in the world trades completely freely. "
                            "Even the most open economies maintain some form of barrier "
                            "to control the flow of goods across their borders. "
                            "Understanding these barriers — why they exist, how they work, "
                            "and what happens when countries fight over them — "
                            "is essential for anyone studying international trade.\n\n"
                            "The most visible barrier is the tariff. "
                            "A tariff is a tax on imported goods, and it serves two purposes: "
                            "it raises revenue for the government, and it protects domestic producers "
                            "by making foreign products more expensive. "
                            "When a country places a tariff on imported clothing, for example, "
                            "local textile factories gain an advantage because consumers now find "
                            "domestic products relatively cheaper.\n\n"
                            "Governments also use quotas to limit the quantity of imports. "
                            "A quota sets a maximum amount of a product that can enter the country. "
                            "Once the quota is filled, no more of that product can be imported "
                            "until the next period begins. "
                            "In the most extreme cases, a government may impose an embargo — "
                            "a total ban on trade with a specific country. "
                            "Embargoes are often accompanied by broader sanctions, "
                            "which may include freezing financial assets, banning travel, "
                            "and cutting off diplomatic relations. "
                            "A sanction uses economic pressure to achieve political goals.\n\n"
                            "Not all unfair trade practices come from governments. "
                            "Sometimes foreign companies engage in dumping — "
                            "selling goods in another country at prices below their cost of production. "
                            "Dumping can devastate local industries that cannot match the artificially low prices. "
                            "To counter this, importing countries may impose a countervailing duty — "
                            "an additional tax that offsets the unfair price advantage "
                            "created by dumping or foreign government subsidies.\n\n"
                            "As international agreements have lowered tariffs around the world, "
                            "non-tariff barriers have become increasingly important. "
                            "These include technical standards that products must meet, "
                            "certification requirements that exporters must obtain, "
                            "and licensing procedures that importers must complete. "
                            "A Vietnamese furniture maker who wants to sell tables in Australia, for instance, "
                            "must ensure the wood meets Australian environmental standards, "
                            "obtain the proper certification from an approved testing laboratory, "
                            "and navigate the licensing process required by Australian customs. "
                            "Each of these steps adds cost and time, creating a restriction "
                            "that functions much like a tariff — even though no tax is involved.\n\n"
                            "When one country feels that another's trade barriers are unfair, "
                            "it may respond with retaliation. "
                            "Retaliation typically means imposing new tariffs or restrictions "
                            "on the offending country's exports. "
                            "A cycle of retaliation can escalate into a full trade war, "
                            "where both countries raise barriers higher and higher, "
                            "hurting consumers and businesses on both sides.\n\n"
                            "International trade law provides tools to manage these conflicts. "
                            "A country can invoke safeguard measures to temporarily protect "
                            "a domestic industry that is being overwhelmed by a surge in imports. "
                            "It can also launch an anti-dumping investigation "
                            "to determine whether foreign goods are being sold below fair value. "
                            "If the investigation confirms dumping, the country can impose anti-dumping duties "
                            "to restore fair competition.\n\n"
                            "Trade agreements create a framework for cooperation. "
                            "Countries that sign free trade agreements grant each other preferential treatment — "
                            "lower tariffs, simplified customs procedures, and mutual recognition of standards. "
                            "Within these agreements, developing countries often receive exemptions "
                            "that allow them more time to open their markets. "
                            "An exemption acknowledges that poorer nations need extra support "
                            "to compete on the global stage.\n\n"
                            "But preferential treatment and exemptions come with obligations. "
                            "Every member of a trade agreement must maintain compliance "
                            "with the rules they have agreed to follow. "
                            "Compliance means meeting standards, honoring commitments, "
                            "and submitting to dispute resolution when disagreements arise. "
                            "A country that fails to comply risks losing its preferential access "
                            "and facing penalties from its trading partners.\n\n"
                            "The world of trade barriers is complex, but it comes down to a fundamental tension: "
                            "every country wants the benefits of free trade — lower prices, more choices, "
                            "and access to global markets — but every country also wants to protect "
                            "its own workers, industries, and strategic interests. "
                            "The tools of trade policy — tariffs, quotas, standards, safeguards, "
                            "and the agreements that govern them — are how nations navigate this tension."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích rào cản thương mại",
                    "description": "Viết đoạn văn tiếng Anh phân tích về rào cản thương mại sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến rào cản thương mại. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích tác động của một cuộc chiến thương mại giữa hai nền kinh tế lớn. Giải thích cách tariff và retaliation leo thang, vai trò của anti-dumping duty và safeguard measure, và tại sao compliance với luật thương mại quốc tế lại quan trọng để ngăn chặn xung đột.",
                            "Hãy chọn một sản phẩm xuất khẩu của Việt Nam (ví dụ: tôm, cà phê, gỗ) và phân tích những barrier mà doanh nghiệp Việt Nam phải vượt qua để tiếp cận thị trường quốc tế. Giải thích vai trò của standard, certification, licensing, và cách preferential trade agreement giúp giảm restriction."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay sâu lắng.",
                    "data": {
                        "text": (
                            "Bạn đã đi đến cuối hành trình rồi. Hãy dừng lại một chút, "
                            "hít thở sâu, và nhìn lại quãng đường bạn vừa đi qua.\n\n"
                            "Khi bắt đầu bài học này, có thể bạn chỉ biết 'thuế quan' và 'hạn ngạch' "
                            "như hai khái niệm khô khan trong sách giáo khoa. "
                            "Nhưng bây giờ, bạn đã có một bộ công cụ ngôn ngữ để đọc, hiểu và phân tích "
                            "chính sách thương mại quốc tế bằng tiếng Anh. "
                            "Và quan trọng hơn, bạn đã bắt đầu nhìn thế giới khác đi.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất — "
                            "nhưng lần này, tôi muốn bạn không chỉ nhớ định nghĩa, "
                            "mà hãy tự hỏi: từ này nói gì về cách thế giới vận hành?\n\n"
                            "Tariff — thuế quan. Mỗi khi bạn mua một sản phẩm nhập khẩu, "
                            "có một phần giá bạn trả không đến tay nhà sản xuất — "
                            "nó đi vào ngân sách chính phủ. Tariff là lựa chọn: "
                            "bảo vệ người sản xuất trong nước, nhưng người tiêu dùng phải trả giá cao hơn. "
                            "Ví dụ mới: The tariff on imported dairy products means Vietnamese consumers pay "
                            "nearly double the international price for a block of cheese.\n\n"
                            "Embargo — lệnh cấm vận. Đây là khi thương mại trở thành vũ khí. "
                            "Một quốc gia nói: 'Chúng tôi sẽ không mua, không bán, không giao dịch với bạn.' "
                            "Embargo nhắc nhở chúng ta rằng thương mại không chỉ là kinh tế — "
                            "nó là chính trị, là quyền lực, là quan hệ giữa các quốc gia. "
                            "Ví dụ mới: The oil embargo forced the targeted country to develop "
                            "its own renewable energy sources faster than anyone expected.\n\n"
                            "Non-tariff — phi thuế quan. Đây là bài học về sự tinh vi. "
                            "Khi thuế quan bị cắt giảm bởi hiệp định thương mại, "
                            "các quốc gia tìm cách khác để bảo hộ — qua tiêu chuẩn, chứng nhận, giấy phép. "
                            "Non-tariff barriers dạy bạn rằng rào cản không phải lúc nào cũng nhìn thấy được. "
                            "Ví dụ mới: The non-tariff barriers in the form of complex labeling requirements "
                            "have prevented many small Asian food producers from entering the European market.\n\n"
                            "Compliance — tuân thủ. Trong thương mại quốc tế, tự do không có nghĩa là vô luật. "
                            "Mọi ưu đãi, mọi miễn trừ đều đi kèm với nghĩa vụ. "
                            "Compliance là lời nhắc rằng quyền lợi và trách nhiệm luôn song hành. "
                            "Ví dụ mới: The exporter lost its preferential tariff rate after failing "
                            "to maintain compliance with the agreement's rules of origin requirements.\n\n"
                            "Safeguard — biện pháp tự vệ. Không phải mọi sự bảo hộ đều xấu. "
                            "Đôi khi một ngành sản xuất cần thời gian để thích nghi, "
                            "và safeguard cho họ khoảng thở đó. "
                            "Câu hỏi không phải là 'có nên bảo hộ không?' mà là 'bảo hộ bao lâu và bằng cách nào?' "
                            "Ví dụ mới: The temporary safeguard on imported textiles gave local weavers "
                            "three years to modernize their equipment and improve product quality.\n\n"
                            "Retaliation — trả đũa. Đây là từ nhắc nhở bạn rằng "
                            "mọi hành động trong thương mại quốc tế đều có phản ứng. "
                            "Khi một nước tăng thuế, nước kia đáp trả. "
                            "Vòng xoáy retaliation cho thấy tại sao đối thoại và hợp tác "
                            "luôn tốt hơn đối đầu. "
                            "Ví dụ mới: The threat of retaliation from major trading partners "
                            "convinced the government to reconsider its plan to raise tariffs on imported machinery.\n\n"
                            "Bạn biết không, học từ vựng thương mại quốc tế không chỉ là ghi nhớ thuật ngữ. "
                            "Mỗi từ bạn học là một cửa sổ nhìn vào cách các quốc gia tương tác với nhau. "
                            "Khi bạn đọc tin về cuộc chiến thương mại, bạn sẽ hiểu vì sao nó xảy ra. "
                            "Khi bạn nghe về hiệp định thương mại mới, bạn sẽ biết nó ảnh hưởng đến ai.\n\n"
                            "Thương mại quốc tế là câu chuyện về sự kết nối — "
                            "giữa các quốc gia, giữa người sản xuất và người tiêu dùng, "
                            "giữa chính sách và đời sống hàng ngày. "
                            "Và bạn vừa có thêm 18 từ vựng để đọc, hiểu và kể câu chuyện đó bằng tiếng Anh.\n\n"
                            "Hãy mang những từ này theo bạn — không chỉ vào phòng thi, "
                            "mà vào mỗi lần bạn đọc tin kinh tế, mỗi lần bạn suy nghĩ về thế giới. "
                            "Chúc bạn tiếp tục hành trình học tập thật sâu sắc và ý nghĩa. "
                            "Hẹn gặp lại bạn ở bài học tiếp theo nhé!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Trade Barriers – Rào Cản Thương Mại' AND uid = '{UID}' ORDER BY created_at;")
