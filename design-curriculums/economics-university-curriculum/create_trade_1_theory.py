"""
Create curriculum: Trade Theory – Lý Thuyết Thương Mại
Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa (International Trade), curriculum #1
18 words | 5 sessions | empathetic_observation tone | team-building energy farewell
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
W1 = ["comparative", "absolute", "advantage", "specialization", "export", "import"]
W2 = ["trade", "surplus", "deficit", "balance", "terms", "gains"]
W3 = ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Trade Theory – Lý Thuyết Thương Mại",
    "contentTypeTags": [],
    "description": (
        "BẠN HỌC THƯƠNG MẠI QUỐC TẾ BẰNG TIẾNG VIỆT RẤT GIỎI — NHƯNG KHI ĐỌC BÁO CÁO WTO BẰNG TIẾNG ANH THÌ SAO?\n\n"
        "Bạn biết lợi thế so sánh là gì, hiểu vì sao Việt Nam xuất khẩu gạo và nhập khẩu máy móc. "
        "Nhưng khi giảng viên chiếu slide về comparative advantage hay terms of trade, "
        "bạn phải đọc đi đọc lại mà vẫn không chắc mình hiểu đúng. "
        "Cảm giác đó — biết kiến thức nhưng thiếu ngôn ngữ — thật sự bực bội.\n\n"
        "Hãy nghĩ về vốn từ tiếng Anh thương mại như tấm hộ chiếu ngôn ngữ — "
        "bạn có kiến thức để đi khắp thế giới học thuật, nhưng thiếu tấm hộ chiếu này thì cửa nào cũng đóng. "
        "18 từ vựng trong bài học này chính là con dấu đầu tiên trên tấm hộ chiếu ấy.\n\n"
        "Sau bài học, bạn sẽ đọc được đoạn phân tích về lợi thế so sánh và cán cân thương mại bằng tiếng Anh "
        "mà không cần dừng lại tra từ, tự tin thảo luận về trade surplus hay protectionism trong lớp, "
        "và viết được những câu phân tích chính xác bằng ngôn ngữ chuyên ngành.\n\n"
        "18 từ — từ comparative đến multilateral — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy thương mại quốc tế, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về lý thuyết thương mại quốc tế — "
            "nền tảng để hiểu vì sao các quốc gia giao thương với nhau. "
            "Bạn sẽ học comparative, absolute, advantage, specialization, export, import trong phần đầu tiên, "
            "nơi bài đọc giải thích lý thuyết lợi thế so sánh của David Ricardo và vì sao chuyên môn hóa tạo ra giá trị. "
            "Tiếp theo là trade, surplus, deficit, balance, terms, gains — "
            "những từ giúp bạn đọc hiểu cán cân thương mại và phân tích lợi ích từ giao thương. "
            "Cuối cùng, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral "
            "đưa bạn vào thế giới chính sách thương mại — từ tự cung tự cấp đến hội nhập toàn cầu. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tài liệu thương mại quốc tế bằng tiếng Anh — "
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
                    "description": "Chào mừng bạn đến với bài học về lý thuyết thương mại — nền tảng thương mại quốc tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học đầu tiên trong chuỗi từ vựng Thương mại quốc tế — "
                            "chủ đề hôm nay là Lý thuyết thương mại, hay trong tiếng Anh là Trade Theory. "
                            "Đây là nền tảng để hiểu vì sao các quốc gia giao thương với nhau "
                            "thay vì tự sản xuất mọi thứ. Từ chiếc áo bạn mặc đến chiếc điện thoại bạn cầm — "
                            "tất cả đều là sản phẩm của thương mại quốc tế.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: comparative, absolute, advantage, specialization, export, và import. "
                            "Đây là những từ bạn sẽ gặp ngay từ chương đầu tiên của bất kỳ giáo trình thương mại quốc tế nào.\n\n"
                            "Từ đầu tiên là comparative — tính từ — nghĩa là so sánh, tương đối. "
                            "Trong kinh tế, comparative thường đi với advantage để tạo thành comparative advantage — "
                            "lợi thế so sánh, khái niệm trung tâm của lý thuyết thương mại. "
                            "Ví dụ: 'Vietnam has a comparative advantage in rice production because its climate and labor costs make rice farming relatively cheaper.' "
                            "Trong bài đọc, comparative được dùng để giải thích vì sao một quốc gia nên tập trung vào "
                            "sản phẩm mà họ sản xuất hiệu quả hơn tương đối so với quốc gia khác.\n\n"
                            "Từ thứ hai là absolute — tính từ — nghĩa là tuyệt đối. "
                            "Absolute advantage là lợi thế tuyệt đối — khi một quốc gia có thể sản xuất "
                            "một sản phẩm với ít nguồn lực hơn bất kỳ quốc gia nào khác. "
                            "Ví dụ: 'Saudi Arabia has an absolute advantage in oil production because of its vast natural reserves.' "
                            "Trong bài đọc, absolute được so sánh với comparative — "
                            "Adam Smith nói về absolute advantage, nhưng David Ricardo chứng minh rằng "
                            "comparative advantage mới là lý do thực sự các nước giao thương.\n\n"
                            "Từ thứ ba là advantage — danh từ — nghĩa là lợi thế, ưu thế. "
                            "Trong thương mại quốc tế, advantage là khả năng sản xuất hàng hóa "
                            "hiệu quả hơn hoặc với chi phí cơ hội thấp hơn. "
                            "Ví dụ: 'A country's advantage in a particular industry often comes from its natural resources, skilled labor, or technology.' "
                            "Trong bài đọc, advantage xuất hiện xuyên suốt — "
                            "đây là từ khóa kết nối mọi lý thuyết về thương mại.\n\n"
                            "Từ thứ tư là specialization — danh từ — nghĩa là chuyên môn hóa, "
                            "việc một quốc gia tập trung sản xuất những hàng hóa mà họ có lợi thế. "
                            "Ví dụ: 'Through specialization, each country focuses on what it does best and trades for the rest.' "
                            "Trong bài đọc, specialization là kết quả tự nhiên của comparative advantage — "
                            "khi mỗi nước chuyên môn hóa, tổng sản lượng toàn cầu tăng lên.\n\n"
                            "Từ thứ năm là export — danh từ và động từ — nghĩa là xuất khẩu, "
                            "hàng hóa hoặc dịch vụ được bán ra nước ngoài. "
                            "Ví dụ: 'Vietnam's top exports include electronics, textiles, and seafood.' "
                            "Trong bài đọc, export mô tả hàng hóa mà một quốc gia bán cho thế giới — "
                            "thường là những sản phẩm mà họ có lợi thế so sánh.\n\n"
                            "Từ cuối cùng là import — danh từ và động từ — nghĩa là nhập khẩu, "
                            "hàng hóa hoặc dịch vụ được mua từ nước ngoài. "
                            "Ví dụ: 'Japan imports most of its energy because it has very few domestic oil reserves.' "
                            "Trong bài đọc, import là mặt đối lập của export — "
                            "quốc gia nhập khẩu những sản phẩm mà nước khác sản xuất hiệu quả hơn.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về lợi thế so sánh và thương mại quốc tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Lợi thế so sánh và thương mại",
                    "description": "Học 6 từ: comparative, absolute, advantage, specialization, export, import",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Lợi thế so sánh và thương mại",
                    "description": "Học 6 từ: comparative, absolute, advantage, specialization, export, import",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Lợi thế so sánh và thương mại",
                    "description": "Học 6 từ: comparative, absolute, advantage, specialization, export, import",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Lợi thế so sánh và thương mại",
                    "description": "Học 6 từ: comparative, absolute, advantage, specialization, export, import",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Lợi thế so sánh và thương mại",
                    "description": "Học 6 từ: comparative, absolute, advantage, specialization, export, import",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Lợi thế so sánh và chuyên môn hóa",
                    "description": "Why do countries trade with each other instead of producing everything on their own?",
                    "data": {
                        "text": (
                            "Why do countries trade with each other instead of producing everything on their own? "
                            "This is one of the oldest questions in economics, and the answer lies in a powerful idea: "
                            "comparative advantage.\n\n"
                            "In the late eighteenth century, the economist Adam Smith argued that countries should "
                            "focus on goods they can produce more efficiently than anyone else. "
                            "He called this absolute advantage. If Vietnam can grow rice using fewer resources "
                            "than Germany, then Vietnam has an absolute advantage in rice production. "
                            "If Germany can build cars using fewer resources than Vietnam, "
                            "then Germany has an absolute advantage in car manufacturing.\n\n"
                            "But what if one country is better at producing everything? "
                            "David Ricardo answered this question in 1817 with the theory of comparative advantage. "
                            "Even if one nation has an absolute advantage in all goods, "
                            "both countries still benefit from trade. The key is opportunity cost. "
                            "A country has a comparative advantage in a good if it can produce that good "
                            "at a lower opportunity cost than its trading partner.\n\n"
                            "Consider a simple example. Suppose Vietnam can produce either ten tons of rice "
                            "or two computers with the same amount of labor. "
                            "Japan, meanwhile, can produce either eight tons of rice or eight computers. "
                            "Japan is better at both, so it has an absolute advantage in both goods. "
                            "But Vietnam gives up only one-fifth of a computer for each ton of rice, "
                            "while Japan gives up one computer for each ton of rice. "
                            "Vietnam has a comparative advantage in rice because its opportunity cost is lower.\n\n"
                            "When each country pursues specialization — focusing on the good where it has "
                            "a comparative advantage — total world output increases. "
                            "Vietnam specializes in rice and exports the surplus to Japan. "
                            "Japan specializes in computers and exports them to Vietnam. "
                            "Both countries end up with more rice and more computers than they could produce alone.\n\n"
                            "This is the magic of trade. Export what you do relatively well, "
                            "and import what others do relatively better. "
                            "Specialization and exchange make both sides richer, "
                            "even when one side is more productive in every single industry."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lợi thế so sánh và chuyên môn hóa",
                    "description": "Why do countries trade with each other instead of producing everything on their own?",
                    "data": {
                        "text": (
                            "Why do countries trade with each other instead of producing everything on their own? "
                            "This is one of the oldest questions in economics, and the answer lies in a powerful idea: "
                            "comparative advantage.\n\n"
                            "In the late eighteenth century, the economist Adam Smith argued that countries should "
                            "focus on goods they can produce more efficiently than anyone else. "
                            "He called this absolute advantage. If Vietnam can grow rice using fewer resources "
                            "than Germany, then Vietnam has an absolute advantage in rice production. "
                            "If Germany can build cars using fewer resources than Vietnam, "
                            "then Germany has an absolute advantage in car manufacturing.\n\n"
                            "But what if one country is better at producing everything? "
                            "David Ricardo answered this question in 1817 with the theory of comparative advantage. "
                            "Even if one nation has an absolute advantage in all goods, "
                            "both countries still benefit from trade. The key is opportunity cost. "
                            "A country has a comparative advantage in a good if it can produce that good "
                            "at a lower opportunity cost than its trading partner.\n\n"
                            "Consider a simple example. Suppose Vietnam can produce either ten tons of rice "
                            "or two computers with the same amount of labor. "
                            "Japan, meanwhile, can produce either eight tons of rice or eight computers. "
                            "Japan is better at both, so it has an absolute advantage in both goods. "
                            "But Vietnam gives up only one-fifth of a computer for each ton of rice, "
                            "while Japan gives up one computer for each ton of rice. "
                            "Vietnam has a comparative advantage in rice because its opportunity cost is lower.\n\n"
                            "When each country pursues specialization — focusing on the good where it has "
                            "a comparative advantage — total world output increases. "
                            "Vietnam specializes in rice and exports the surplus to Japan. "
                            "Japan specializes in computers and exports them to Vietnam. "
                            "Both countries end up with more rice and more computers than they could produce alone.\n\n"
                            "This is the magic of trade. Export what you do relatively well, "
                            "and import what others do relatively better. "
                            "Specialization and exchange make both sides richer, "
                            "even when one side is more productive in every single industry."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lợi thế so sánh và chuyên môn hóa",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Why do countries trade with each other instead of producing everything on their own? "
                            "This is one of the oldest questions in economics, and the answer lies in a powerful idea: "
                            "comparative advantage.\n\n"
                            "In the late eighteenth century, the economist Adam Smith argued that countries should "
                            "focus on goods they can produce more efficiently than anyone else. "
                            "He called this absolute advantage. If Vietnam can grow rice using fewer resources "
                            "than Germany, then Vietnam has an absolute advantage in rice production. "
                            "If Germany can build cars using fewer resources than Vietnam, "
                            "then Germany has an absolute advantage in car manufacturing.\n\n"
                            "But what if one country is better at producing everything? "
                            "David Ricardo answered this question in 1817 with the theory of comparative advantage. "
                            "Even if one nation has an absolute advantage in all goods, "
                            "both countries still benefit from trade. The key is opportunity cost. "
                            "A country has a comparative advantage in a good if it can produce that good "
                            "at a lower opportunity cost than its trading partner.\n\n"
                            "Consider a simple example. Suppose Vietnam can produce either ten tons of rice "
                            "or two computers with the same amount of labor. "
                            "Japan, meanwhile, can produce either eight tons of rice or eight computers. "
                            "Japan is better at both, so it has an absolute advantage in both goods. "
                            "But Vietnam gives up only one-fifth of a computer for each ton of rice, "
                            "while Japan gives up one computer for each ton of rice. "
                            "Vietnam has a comparative advantage in rice because its opportunity cost is lower.\n\n"
                            "When each country pursues specialization — focusing on the good where it has "
                            "a comparative advantage — total world output increases. "
                            "Vietnam specializes in rice and exports the surplus to Japan. "
                            "Japan specializes in computers and exports them to Vietnam. "
                            "Both countries end up with more rice and more computers than they could produce alone.\n\n"
                            "This is the magic of trade. Export what you do relatively well, "
                            "and import what others do relatively better. "
                            "Specialization and exchange make both sides richer, "
                            "even when one side is more productive in every single industry."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Lợi thế so sánh và thương mại",
                    "description": "Viết câu sử dụng 6 từ vựng về lợi thế so sánh.",
                    "data": {
                        "vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import"],
                        "items": [
                            {
                                "targetVocab": "comparative",
                                "prompt": "Dùng từ 'comparative' để viết một câu về lợi thế so sánh của một quốc gia trong sản xuất một loại hàng hóa. Ví dụ: Vietnam has a comparative advantage in textile manufacturing because its labor costs are lower relative to many other industries."
                            },
                            {
                                "targetVocab": "absolute",
                                "prompt": "Dùng từ 'absolute' để viết một câu về lợi thế tuyệt đối của một quốc gia nhờ tài nguyên thiên nhiên hoặc công nghệ. Ví dụ: Brazil holds an absolute advantage in coffee production thanks to its ideal climate and vast farmland in the highlands."
                            },
                            {
                                "targetVocab": "advantage",
                                "prompt": "Dùng từ 'advantage' để viết một câu về lợi thế cạnh tranh của một quốc gia trên thị trường quốc tế. Ví dụ: South Korea's advantage in semiconductor manufacturing comes from decades of investment in research and a highly skilled workforce."
                            },
                            {
                                "targetVocab": "specialization",
                                "prompt": "Dùng từ 'specialization' để viết một câu về việc một quốc gia tập trung sản xuất hàng hóa mà họ làm tốt nhất. Ví dụ: Through specialization in electronics assembly, Vietnam has become one of the largest exporters of smartphones in Southeast Asia."
                            },
                            {
                                "targetVocab": "export",
                                "prompt": "Dùng từ 'export' để viết một câu về hàng hóa mà một quốc gia bán ra thị trường quốc tế. Ví dụ: Thailand's export of rice generates billions of dollars in revenue each year and supports millions of farming families."
                            },
                            {
                                "targetVocab": "import",
                                "prompt": "Dùng từ 'import' để viết một câu về hàng hóa mà một quốc gia mua từ nước ngoài vì không tự sản xuất hiệu quả. Ví dụ: Vietnam must import most of its crude oil refining equipment because domestic manufacturers cannot yet produce it at competitive quality."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về cán cân thương mại và lợi ích giao thương.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "comparative — so sánh, tương đối, absolute — tuyệt đối, advantage — lợi thế, "
                            "specialization — chuyên môn hóa, export — xuất khẩu, và import — nhập khẩu. "
                            "Bạn đã hiểu vì sao các quốc gia giao thương dựa trên lợi thế so sánh. "
                            "Bây giờ, chúng ta sẽ tìm hiểu kết quả của thương mại — ai được lợi, ai chịu thiệt, "
                            "và cán cân thương mại hoạt động ra sao.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: trade, surplus, deficit, balance, terms, và gains. "
                            "Những từ này giúp bạn đọc hiểu các báo cáo kinh tế về xuất nhập khẩu "
                            "và phân tích mối quan hệ thương mại giữa các quốc gia.\n\n"
                            "Từ đầu tiên là trade — danh từ và động từ — nghĩa là thương mại, giao thương. "
                            "Trade là hoạt động mua bán hàng hóa và dịch vụ giữa các quốc gia. "
                            "Ví dụ: 'International trade allows countries to access goods they cannot produce efficiently on their own.' "
                            "Trong bài đọc, trade là từ khóa trung tâm — mọi phân tích đều xoay quanh "
                            "dòng chảy hàng hóa giữa các nền kinh tế.\n\n"
                            "Từ thứ hai là surplus — danh từ — trong thương mại nghĩa là thặng dư, "
                            "khi giá trị xuất khẩu lớn hơn giá trị nhập khẩu. "
                            "Ví dụ: 'China has maintained a large trade surplus with the United States for many years, exporting far more than it imports.' "
                            "Trong bài đọc, surplus mô tả tình trạng một quốc gia bán ra nhiều hơn mua vào.\n\n"
                            "Từ thứ ba là deficit — danh từ — nghĩa là thâm hụt, "
                            "khi giá trị nhập khẩu lớn hơn giá trị xuất khẩu. "
                            "Ví dụ: 'The United States runs a trade deficit because it imports more consumer goods than it exports.' "
                            "Trong bài đọc, deficit là mặt đối lập của surplus — "
                            "một quốc gia mua từ thế giới nhiều hơn những gì nó bán ra.\n\n"
                            "Từ thứ tư là balance — danh từ — nghĩa là cán cân, sự cân bằng. "
                            "Balance of trade là cán cân thương mại — chênh lệch giữa xuất khẩu và nhập khẩu. "
                            "Ví dụ: 'A country's balance of trade is calculated by subtracting the value of imports from the value of exports.' "
                            "Trong bài đọc, balance giúp bạn hiểu bức tranh tổng thể "
                            "về mối quan hệ thương mại của một quốc gia với thế giới.\n\n"
                            "Từ thứ năm là terms — danh từ — trong thương mại, terms of trade nghĩa là "
                            "điều kiện thương mại, tỷ lệ giữa giá xuất khẩu và giá nhập khẩu. "
                            "Ví dụ: 'When a country's terms of trade improve, it can buy more imports for each unit of exports it sells.' "
                            "Trong bài đọc, terms cho thấy liệu thương mại có thực sự có lợi cho một quốc gia hay không.\n\n"
                            "Từ cuối cùng là gains — danh từ — nghĩa là lợi ích, phần được. "
                            "Gains from trade là lợi ích từ thương mại — phần giá trị tăng thêm "
                            "mà mỗi quốc gia nhận được nhờ giao thương. "
                            "Ví dụ: 'The gains from trade are not always shared equally — some industries benefit while others may suffer.' "
                            "Trong bài đọc, gains giải thích vì sao thương mại tự do "
                            "làm tăng tổng phúc lợi, dù không phải ai cũng được lợi như nhau.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về cán cân thương mại và lợi ích giao thương nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cán cân thương mại và lợi ích",
                    "description": "Học 6 từ: trade, surplus, deficit, balance, terms, gains",
                    "data": {"vocabList": ["trade", "surplus", "deficit", "balance", "terms", "gains"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cán cân thương mại và lợi ích",
                    "description": "Học 6 từ: trade, surplus, deficit, balance, terms, gains",
                    "data": {"vocabList": ["trade", "surplus", "deficit", "balance", "terms", "gains"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cán cân thương mại và lợi ích",
                    "description": "Học 6 từ: trade, surplus, deficit, balance, terms, gains",
                    "data": {"vocabList": ["trade", "surplus", "deficit", "balance", "terms", "gains"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cán cân thương mại và lợi ích",
                    "description": "Học 6 từ: trade, surplus, deficit, balance, terms, gains",
                    "data": {"vocabList": ["trade", "surplus", "deficit", "balance", "terms", "gains"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Cán cân thương mại và lợi ích",
                    "description": "Học 6 từ: trade, surplus, deficit, balance, terms, gains",
                    "data": {"vocabList": ["trade", "surplus", "deficit", "balance", "terms", "gains"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cán cân thương mại và lợi ích từ giao thương",
                    "description": "When two countries trade, both sides expect to gain something they did not have before.",
                    "data": {
                        "text": (
                            "When two countries trade, both sides expect to gain something they did not have before. "
                            "But how do we measure whether trade is actually helping a nation? "
                            "Economists use several tools to answer this question, "
                            "starting with the balance of trade.\n\n"
                            "The balance of trade is the difference between the value of a country's exports "
                            "and the value of its imports over a given period. "
                            "If a country exports more than it imports, it has a trade surplus. "
                            "If it imports more than it exports, it has a trade deficit. "
                            "Vietnam, for example, has shifted from running persistent deficits in the early 2000s "
                            "to achieving a trade surplus in recent years, "
                            "largely thanks to the growth of electronics and textile exports.\n\n"
                            "A surplus is not always good, and a deficit is not always bad. "
                            "The United States has run a trade deficit for decades, "
                            "yet it remains one of the wealthiest nations in the world. "
                            "A deficit can mean that consumers have access to a wide variety of affordable imported goods. "
                            "A surplus can mean that domestic consumers are not buying enough, "
                            "or that the country is saving more than it invests at home.\n\n"
                            "To understand whether trade is truly beneficial, economists look at the terms of trade. "
                            "The terms of trade measure the ratio of export prices to import prices. "
                            "If a country's export prices rise faster than its import prices, "
                            "its terms of trade improve. This means the country can buy more imports "
                            "for each unit of goods it sells abroad. "
                            "Developing countries that export raw materials often face declining terms of trade "
                            "because commodity prices tend to be volatile and fall over time "
                            "relative to manufactured goods.\n\n"
                            "The gains from trade are the additional output and consumption "
                            "that countries enjoy because they specialize and exchange. "
                            "Without trade, each country would have to produce everything it needs on its own. "
                            "With trade, countries can focus on what they do best and enjoy a wider range of products "
                            "at lower prices. The gains are real, but they are not always distributed evenly. "
                            "Some industries grow and create jobs, while others shrink and workers lose employment.\n\n"
                            "This is why trade policy is always a balancing act. "
                            "The total gains from trade are positive, but the challenge is ensuring "
                            "that the benefits reach everyone, not just the industries that export."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cán cân thương mại và lợi ích từ giao thương",
                    "description": "When two countries trade, both sides expect to gain something they did not have before.",
                    "data": {
                        "text": (
                            "When two countries trade, both sides expect to gain something they did not have before. "
                            "But how do we measure whether trade is actually helping a nation? "
                            "Economists use several tools to answer this question, "
                            "starting with the balance of trade.\n\n"
                            "The balance of trade is the difference between the value of a country's exports "
                            "and the value of its imports over a given period. "
                            "If a country exports more than it imports, it has a trade surplus. "
                            "If it imports more than it exports, it has a trade deficit. "
                            "Vietnam, for example, has shifted from running persistent deficits in the early 2000s "
                            "to achieving a trade surplus in recent years, "
                            "largely thanks to the growth of electronics and textile exports.\n\n"
                            "A surplus is not always good, and a deficit is not always bad. "
                            "The United States has run a trade deficit for decades, "
                            "yet it remains one of the wealthiest nations in the world. "
                            "A deficit can mean that consumers have access to a wide variety of affordable imported goods. "
                            "A surplus can mean that domestic consumers are not buying enough, "
                            "or that the country is saving more than it invests at home.\n\n"
                            "To understand whether trade is truly beneficial, economists look at the terms of trade. "
                            "The terms of trade measure the ratio of export prices to import prices. "
                            "If a country's export prices rise faster than its import prices, "
                            "its terms of trade improve. This means the country can buy more imports "
                            "for each unit of goods it sells abroad. "
                            "Developing countries that export raw materials often face declining terms of trade "
                            "because commodity prices tend to be volatile and fall over time "
                            "relative to manufactured goods.\n\n"
                            "The gains from trade are the additional output and consumption "
                            "that countries enjoy because they specialize and exchange. "
                            "Without trade, each country would have to produce everything it needs on its own. "
                            "With trade, countries can focus on what they do best and enjoy a wider range of products "
                            "at lower prices. The gains are real, but they are not always distributed evenly. "
                            "Some industries grow and create jobs, while others shrink and workers lose employment.\n\n"
                            "This is why trade policy is always a balancing act. "
                            "The total gains from trade are positive, but the challenge is ensuring "
                            "that the benefits reach everyone, not just the industries that export."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cán cân thương mại và lợi ích từ giao thương",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When two countries trade, both sides expect to gain something they did not have before. "
                            "But how do we measure whether trade is actually helping a nation? "
                            "Economists use several tools to answer this question, "
                            "starting with the balance of trade.\n\n"
                            "The balance of trade is the difference between the value of a country's exports "
                            "and the value of its imports over a given period. "
                            "If a country exports more than it imports, it has a trade surplus. "
                            "If it imports more than it exports, it has a trade deficit. "
                            "Vietnam, for example, has shifted from running persistent deficits in the early 2000s "
                            "to achieving a trade surplus in recent years, "
                            "largely thanks to the growth of electronics and textile exports.\n\n"
                            "A surplus is not always good, and a deficit is not always bad. "
                            "The United States has run a trade deficit for decades, "
                            "yet it remains one of the wealthiest nations in the world. "
                            "A deficit can mean that consumers have access to a wide variety of affordable imported goods. "
                            "A surplus can mean that domestic consumers are not buying enough, "
                            "or that the country is saving more than it invests at home.\n\n"
                            "To understand whether trade is truly beneficial, economists look at the terms of trade. "
                            "The terms of trade measure the ratio of export prices to import prices. "
                            "If a country's export prices rise faster than its import prices, "
                            "its terms of trade improve. This means the country can buy more imports "
                            "for each unit of goods it sells abroad. "
                            "Developing countries that export raw materials often face declining terms of trade "
                            "because commodity prices tend to be volatile and fall over time "
                            "relative to manufactured goods.\n\n"
                            "The gains from trade are the additional output and consumption "
                            "that countries enjoy because they specialize and exchange. "
                            "Without trade, each country would have to produce everything it needs on its own. "
                            "With trade, countries can focus on what they do best and enjoy a wider range of products "
                            "at lower prices. The gains are real, but they are not always distributed evenly. "
                            "Some industries grow and create jobs, while others shrink and workers lose employment.\n\n"
                            "This is why trade policy is always a balancing act. "
                            "The total gains from trade are positive, but the challenge is ensuring "
                            "that the benefits reach everyone, not just the industries that export."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cán cân thương mại và lợi ích",
                    "description": "Viết câu sử dụng 6 từ vựng về cán cân thương mại.",
                    "data": {
                        "vocabList": ["trade", "surplus", "deficit", "balance", "terms", "gains"],
                        "items": [
                            {
                                "targetVocab": "trade",
                                "prompt": "Dùng từ 'trade' để viết một câu về hoạt động giao thương giữa hai quốc gia. Ví dụ: Trade between Vietnam and South Korea has expanded rapidly since the two countries signed a free trade agreement in 2015."
                            },
                            {
                                "targetVocab": "surplus",
                                "prompt": "Dùng từ 'surplus' để viết một câu về tình trạng thặng dư thương mại của một quốc gia. Ví dụ: Germany's trade surplus reflects its strong manufacturing sector, which exports cars, machinery, and chemicals to markets around the world."
                            },
                            {
                                "targetVocab": "deficit",
                                "prompt": "Dùng từ 'deficit' để viết một câu về tình trạng thâm hụt thương mại và nguyên nhân của nó. Ví dụ: India's trade deficit with China has grown because Indian consumers buy large quantities of Chinese electronics and machinery."
                            },
                            {
                                "targetVocab": "balance",
                                "prompt": "Dùng từ 'balance' để viết một câu về cán cân thương mại và cách tính toán nó. Ví dụ: The balance of trade turned positive for Vietnam in 2020 as exports of electronics and textiles exceeded the value of imported goods."
                            },
                            {
                                "targetVocab": "terms",
                                "prompt": "Dùng từ 'terms' để viết một câu về điều kiện thương mại và tác động đến nền kinh tế. Ví dụ: When oil prices fall, the terms of trade for oil-exporting countries like Nigeria worsen because they earn less for each barrel they sell abroad."
                            },
                            {
                                "targetVocab": "gains",
                                "prompt": "Dùng từ 'gains' để viết một câu về lợi ích mà các quốc gia nhận được từ thương mại tự do. Ví dụ: The gains from trade allowed Vietnamese consumers to buy affordable smartphones manufactured in South Korea and China."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về chính sách thương mại và hội nhập.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: comparative, absolute, advantage, specialization, export, import — "
                            "những khái niệm cơ bản về lý thuyết lợi thế so sánh và vì sao các nước giao thương. "
                            "Trong phần 2, bạn đã học thêm trade, surplus, deficit, balance, terms, gains — "
                            "giúp bạn hiểu cán cân thương mại và lợi ích từ giao thương quốc tế.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh quan trọng khác: "
                            "chính sách thương mại. Một quốc gia nên mở cửa hoàn toàn hay bảo hộ nền kinh tế? "
                            "Nên đàm phán song phương hay đa phương? "
                            "Bạn sẽ học 6 từ mới: autarky, protectionism, liberalization, reciprocal, bilateral, và multilateral.\n\n"
                            "Từ đầu tiên là autarky — danh từ — nghĩa là tự cung tự cấp, "
                            "tình trạng một quốc gia không giao thương với bên ngoài mà tự sản xuất mọi thứ. "
                            "Ví dụ: 'North Korea's policy of autarky has isolated its economy from the rest of the world.' "
                            "Trong bài đọc, autarky là điểm xuất phát — trước khi có thương mại, "
                            "mỗi quốc gia phải tự lo liệu mọi nhu cầu, và điều đó rất tốn kém.\n\n"
                            "Từ thứ hai là protectionism — danh từ — nghĩa là chủ nghĩa bảo hộ, "
                            "chính sách bảo vệ ngành sản xuất trong nước bằng cách hạn chế hàng nhập khẩu. "
                            "Ví dụ: 'Protectionism through high tariffs may save domestic jobs in the short run but raises prices for consumers.' "
                            "Trong bài đọc, protectionism là mặt đối lập của tự do thương mại — "
                            "chính phủ dựng rào cản để bảo vệ doanh nghiệp nội địa.\n\n"
                            "Từ thứ ba là liberalization — danh từ — nghĩa là tự do hóa, "
                            "quá trình giảm bớt rào cản thương mại và mở cửa thị trường. "
                            "Ví dụ: 'Vietnam's trade liberalization since the 1986 Doi Moi reforms has transformed it into one of Asia's fastest-growing economies.' "
                            "Trong bài đọc, liberalization mô tả xu hướng toàn cầu — "
                            "các quốc gia dần dỡ bỏ thuế quan và hạn ngạch để thúc đẩy giao thương.\n\n"
                            "Từ thứ tư là reciprocal — tính từ — nghĩa là có đi có lại, tương hỗ. "
                            "Trong thương mại, reciprocal nghĩa là hai bên cùng giảm rào cản cho nhau. "
                            "Ví dụ: 'A reciprocal trade agreement means both countries lower tariffs on each other's goods at the same time.' "
                            "Trong bài đọc, reciprocal giải thích nguyên tắc cốt lõi của đàm phán thương mại — "
                            "không ai muốn mở cửa nếu đối tác không làm điều tương tự.\n\n"
                            "Từ thứ năm là bilateral — tính từ — nghĩa là song phương, "
                            "liên quan đến hai quốc gia hoặc hai bên. "
                            "Ví dụ: 'The bilateral trade agreement between Vietnam and Japan has boosted investment flows in both directions.' "
                            "Trong bài đọc, bilateral mô tả hình thức đàm phán thương mại phổ biến nhất — "
                            "hai nước ngồi lại và thỏa thuận điều kiện giao thương.\n\n"
                            "Từ cuối cùng là multilateral — tính từ — nghĩa là đa phương, "
                            "liên quan đến nhiều quốc gia cùng lúc. "
                            "Ví dụ: 'The World Trade Organization promotes multilateral trade negotiations involving over 160 member countries.' "
                            "Trong bài đọc, multilateral là cấp độ cao nhất của hợp tác thương mại — "
                            "nhiều quốc gia cùng đàm phán để tạo ra luật chơi chung cho thương mại toàn cầu.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về chính sách thương mại và hội nhập quốc tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chính sách thương mại và hội nhập",
                    "description": "Học 6 từ: autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chính sách thương mại và hội nhập",
                    "description": "Học 6 từ: autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chính sách thương mại và hội nhập",
                    "description": "Học 6 từ: autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chính sách thương mại và hội nhập",
                    "description": "Học 6 từ: autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chính sách thương mại và hội nhập",
                    "description": "Học 6 từ: autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chính sách thương mại — từ bảo hộ đến hội nhập",
                    "description": "Imagine a country that produces everything it needs without trading with anyone else.",
                    "data": {
                        "text": (
                            "Imagine a country that produces everything it needs without trading with anyone else. "
                            "This state of complete self-sufficiency is called autarky. "
                            "In theory, an autarkic nation does not export or import anything. "
                            "In practice, true autarky is extremely rare and costly. "
                            "A country in autarky must produce its own food, energy, medicine, and technology, "
                            "even if it is very inefficient at making some of these goods.\n\n"
                            "History shows that autarky leads to lower living standards. "
                            "When a country cuts itself off from trade, its consumers pay higher prices "
                            "and have fewer choices. Its producers cannot access foreign markets "
                            "or benefit from foreign technology. "
                            "This is why most economists argue that some degree of trade openness is beneficial.\n\n"
                            "However, opening up to trade creates winners and losers within a country. "
                            "Industries that face competition from cheaper imports may shrink, "
                            "and workers in those industries may lose their jobs. "
                            "This is where protectionism enters the picture. "
                            "Protectionism is the policy of shielding domestic industries from foreign competition "
                            "through tariffs, quotas, and other barriers. "
                            "Supporters of protectionism argue that it saves jobs and protects infant industries "
                            "that need time to grow before they can compete internationally.\n\n"
                            "On the other side of the debate is liberalization — "
                            "the process of reducing trade barriers and opening markets to foreign goods and services. "
                            "Vietnam's experience with liberalization is a powerful example. "
                            "After the Doi Moi reforms in 1986, Vietnam gradually lowered tariffs, "
                            "welcomed foreign investment, and joined international trade organizations. "
                            "The result was rapid economic growth, rising incomes, and millions of people lifted out of poverty.\n\n"
                            "Trade agreements are the main tool for liberalization. "
                            "These agreements are usually reciprocal — both sides agree to lower barriers at the same time. "
                            "A bilateral agreement involves two countries. "
                            "For example, the Vietnam-Japan Economic Partnership Agreement "
                            "reduced tariffs on goods traded between the two nations. "
                            "A multilateral agreement involves many countries at once. "
                            "The Comprehensive and Progressive Agreement for Trans-Pacific Partnership, or CPTPP, "
                            "is a multilateral deal that includes eleven countries across the Pacific region.\n\n"
                            "The choice between protectionism and liberalization is never simple. "
                            "Most countries use a mix of both — protecting sensitive industries "
                            "while opening others to international competition. "
                            "The goal is to capture the gains from trade while managing the costs of adjustment."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chính sách thương mại — từ bảo hộ đến hội nhập",
                    "description": "Imagine a country that produces everything it needs without trading with anyone else.",
                    "data": {
                        "text": (
                            "Imagine a country that produces everything it needs without trading with anyone else. "
                            "This state of complete self-sufficiency is called autarky. "
                            "In theory, an autarkic nation does not export or import anything. "
                            "In practice, true autarky is extremely rare and costly. "
                            "A country in autarky must produce its own food, energy, medicine, and technology, "
                            "even if it is very inefficient at making some of these goods.\n\n"
                            "History shows that autarky leads to lower living standards. "
                            "When a country cuts itself off from trade, its consumers pay higher prices "
                            "and have fewer choices. Its producers cannot access foreign markets "
                            "or benefit from foreign technology. "
                            "This is why most economists argue that some degree of trade openness is beneficial.\n\n"
                            "However, opening up to trade creates winners and losers within a country. "
                            "Industries that face competition from cheaper imports may shrink, "
                            "and workers in those industries may lose their jobs. "
                            "This is where protectionism enters the picture. "
                            "Protectionism is the policy of shielding domestic industries from foreign competition "
                            "through tariffs, quotas, and other barriers. "
                            "Supporters of protectionism argue that it saves jobs and protects infant industries "
                            "that need time to grow before they can compete internationally.\n\n"
                            "On the other side of the debate is liberalization — "
                            "the process of reducing trade barriers and opening markets to foreign goods and services. "
                            "Vietnam's experience with liberalization is a powerful example. "
                            "After the Doi Moi reforms in 1986, Vietnam gradually lowered tariffs, "
                            "welcomed foreign investment, and joined international trade organizations. "
                            "The result was rapid economic growth, rising incomes, and millions of people lifted out of poverty.\n\n"
                            "Trade agreements are the main tool for liberalization. "
                            "These agreements are usually reciprocal — both sides agree to lower barriers at the same time. "
                            "A bilateral agreement involves two countries. "
                            "For example, the Vietnam-Japan Economic Partnership Agreement "
                            "reduced tariffs on goods traded between the two nations. "
                            "A multilateral agreement involves many countries at once. "
                            "The Comprehensive and Progressive Agreement for Trans-Pacific Partnership, or CPTPP, "
                            "is a multilateral deal that includes eleven countries across the Pacific region.\n\n"
                            "The choice between protectionism and liberalization is never simple. "
                            "Most countries use a mix of both — protecting sensitive industries "
                            "while opening others to international competition. "
                            "The goal is to capture the gains from trade while managing the costs of adjustment."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chính sách thương mại — từ bảo hộ đến hội nhập",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine a country that produces everything it needs without trading with anyone else. "
                            "This state of complete self-sufficiency is called autarky. "
                            "In theory, an autarkic nation does not export or import anything. "
                            "In practice, true autarky is extremely rare and costly. "
                            "A country in autarky must produce its own food, energy, medicine, and technology, "
                            "even if it is very inefficient at making some of these goods.\n\n"
                            "History shows that autarky leads to lower living standards. "
                            "When a country cuts itself off from trade, its consumers pay higher prices "
                            "and have fewer choices. Its producers cannot access foreign markets "
                            "or benefit from foreign technology. "
                            "This is why most economists argue that some degree of trade openness is beneficial.\n\n"
                            "However, opening up to trade creates winners and losers within a country. "
                            "Industries that face competition from cheaper imports may shrink, "
                            "and workers in those industries may lose their jobs. "
                            "This is where protectionism enters the picture. "
                            "Protectionism is the policy of shielding domestic industries from foreign competition "
                            "through tariffs, quotas, and other barriers. "
                            "Supporters of protectionism argue that it saves jobs and protects infant industries "
                            "that need time to grow before they can compete internationally.\n\n"
                            "On the other side of the debate is liberalization — "
                            "the process of reducing trade barriers and opening markets to foreign goods and services. "
                            "Vietnam's experience with liberalization is a powerful example. "
                            "After the Doi Moi reforms in 1986, Vietnam gradually lowered tariffs, "
                            "welcomed foreign investment, and joined international trade organizations. "
                            "The result was rapid economic growth, rising incomes, and millions of people lifted out of poverty.\n\n"
                            "Trade agreements are the main tool for liberalization. "
                            "These agreements are usually reciprocal — both sides agree to lower barriers at the same time. "
                            "A bilateral agreement involves two countries. "
                            "For example, the Vietnam-Japan Economic Partnership Agreement "
                            "reduced tariffs on goods traded between the two nations. "
                            "A multilateral agreement involves many countries at once. "
                            "The Comprehensive and Progressive Agreement for Trans-Pacific Partnership, or CPTPP, "
                            "is a multilateral deal that includes eleven countries across the Pacific region.\n\n"
                            "The choice between protectionism and liberalization is never simple. "
                            "Most countries use a mix of both — protecting sensitive industries "
                            "while opening others to international competition. "
                            "The goal is to capture the gains from trade while managing the costs of adjustment."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chính sách thương mại và hội nhập",
                    "description": "Viết câu sử dụng 6 từ vựng về chính sách thương mại.",
                    "data": {
                        "vocabList": ["autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"],
                        "items": [
                            {
                                "targetVocab": "autarky",
                                "prompt": "Dùng từ 'autarky' để viết một câu về hậu quả kinh tế khi một quốc gia tự cô lập khỏi thương mại quốc tế. Ví dụ: Myanmar's decades of near-autarky left its economy far behind its Southeast Asian neighbors who embraced international trade."
                            },
                            {
                                "targetVocab": "protectionism",
                                "prompt": "Dùng từ 'protectionism' để viết một câu về chính sách bảo hộ và tác động đến người tiêu dùng. Ví dụ: Protectionism in the form of high tariffs on imported steel may protect domestic steelmakers but raises costs for car manufacturers and construction companies."
                            },
                            {
                                "targetVocab": "liberalization",
                                "prompt": "Dùng từ 'liberalization' để viết một câu về quá trình mở cửa thị trường và tác động tích cực đến nền kinh tế. Ví dụ: Trade liberalization in the 1990s helped China become the world's largest exporter by giving its factories access to global markets."
                            },
                            {
                                "targetVocab": "reciprocal",
                                "prompt": "Dùng từ 'reciprocal' để viết một câu về nguyên tắc có đi có lại trong đàm phán thương mại. Ví dụ: The reciprocal reduction of tariffs between the EU and Vietnam means European wine is cheaper in Hanoi and Vietnamese shrimp is cheaper in Paris."
                            },
                            {
                                "targetVocab": "bilateral",
                                "prompt": "Dùng từ 'bilateral' để viết một câu về hiệp định thương mại song phương giữa hai quốc gia. Ví dụ: The bilateral free trade agreement between Vietnam and the United Kingdom took effect in 2021, opening new markets for Vietnamese agricultural products."
                            },
                            {
                                "targetVocab": "multilateral",
                                "prompt": "Dùng từ 'multilateral' để viết một câu về hợp tác thương mại đa phương giữa nhiều quốc gia. Ví dụ: ASEAN's multilateral trade framework allows goods to move more freely among ten Southeast Asian countries, reducing costs for businesses in the region."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Lý thuyết thương mại. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "comparative — so sánh, tương đối, absolute — tuyệt đối, advantage — lợi thế, "
                            "specialization — chuyên môn hóa, export — xuất khẩu, và import — nhập khẩu. "
                            "Đây là bộ khung cơ bản để hiểu vì sao các quốc gia giao thương.\n\n"
                            "Trong phần 2, bạn đã đi sâu hơn với: "
                            "trade — thương mại, surplus — thặng dư, deficit — thâm hụt, "
                            "balance — cán cân, terms — điều kiện thương mại, và gains — lợi ích. "
                            "Những từ này giúp bạn đọc hiểu báo cáo kinh tế về xuất nhập khẩu.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "autarky — tự cung tự cấp, protectionism — chủ nghĩa bảo hộ, "
                            "liberalization — tự do hóa, reciprocal — có đi có lại, "
                            "bilateral — song phương, và multilateral — đa phương. "
                            "Đây là những từ về chính sách thương mại và hội nhập quốc tế.\n\n"
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
                    "description": "Học 18 từ: comparative, absolute, advantage, specialization, export, import, trade, surplus, deficit, balance, terms, gains, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: comparative, absolute, advantage, specialization, export, import, trade, surplus, deficit, balance, terms, gains, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: comparative, absolute, advantage, specialization, export, import, trade, surplus, deficit, balance, terms, gains, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: comparative, absolute, advantage, specialization, export, import, trade, surplus, deficit, balance, terms, gains, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: comparative, absolute, advantage, specialization, export, import, trade, surplus, deficit, balance, terms, gains, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral",
                    "data": {"vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng thương mại",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"],
                        "items": [
                            {
                                "targetVocab": "comparative",
                                "prompt": "Dùng từ 'comparative' để viết một câu về lợi thế so sánh của Việt Nam trong một ngành cụ thể. Ví dụ: Vietnam's comparative advantage in seafood processing comes from its long coastline, abundant labor, and generations of fishing expertise."
                            },
                            {
                                "targetVocab": "absolute",
                                "prompt": "Dùng từ 'absolute' để viết một câu về lợi thế tuyệt đối của một quốc gia trong sản xuất năng lượng. Ví dụ: Australia has an absolute advantage in iron ore mining because its massive deposits allow extraction at a fraction of the cost faced by most other countries."
                            },
                            {
                                "targetVocab": "advantage",
                                "prompt": "Dùng từ 'advantage' để viết một câu về cách một quốc gia tận dụng lợi thế để phát triển kinh tế. Ví dụ: Singapore turned its geographic advantage as a shipping hub into one of the busiest ports in the world, handling millions of containers each year."
                            },
                            {
                                "targetVocab": "specialization",
                                "prompt": "Dùng từ 'specialization' để viết một câu về chuyên môn hóa trong chuỗi cung ứng toàn cầu. Ví dụ: Taiwan's specialization in advanced semiconductor manufacturing has made it an indispensable link in the global technology supply chain."
                            },
                            {
                                "targetVocab": "export",
                                "prompt": "Dùng từ 'export' để viết một câu về mặt hàng xuất khẩu chủ lực của một quốc gia Đông Nam Á. Ví dụ: The Philippines' export of electronic components accounts for nearly half of its total merchandise trade with the rest of the world."
                            },
                            {
                                "targetVocab": "import",
                                "prompt": "Dùng từ 'import' để viết một câu về sự phụ thuộc vào hàng nhập khẩu trong một lĩnh vực cụ thể. Ví dụ: Vietnam's growing middle class has driven a sharp increase in the import of luxury goods, from European cars to Japanese cosmetics."
                            },
                            {
                                "targetVocab": "trade",
                                "prompt": "Dùng từ 'trade' để viết một câu về tầm quan trọng của thương mại đối với tăng trưởng kinh tế. Ví dụ: International trade now accounts for over sixty percent of Vietnam's GDP, making it one of the most trade-dependent economies in Asia."
                            },
                            {
                                "targetVocab": "surplus",
                                "prompt": "Dùng từ 'surplus' để viết một câu về thặng dư thương mại và ý nghĩa kinh tế của nó. Ví dụ: Vietnam's trade surplus with the United States has grown steadily as American consumers buy more Vietnamese-made furniture, clothing, and electronics."
                            },
                            {
                                "targetVocab": "deficit",
                                "prompt": "Dùng từ 'deficit' để viết một câu về thâm hụt thương mại và nguyên nhân cấu trúc. Ví dụ: Vietnam runs a persistent trade deficit with China because it imports large quantities of raw materials and machinery for its manufacturing sector."
                            },
                            {
                                "targetVocab": "balance",
                                "prompt": "Dùng từ 'balance' để viết một câu về cán cân thương mại tổng thể của một quốc gia. Ví dụ: Japan's balance of trade shifted from surplus to deficit after the 2011 earthquake forced the country to import more energy to replace its nuclear power plants."
                            },
                            {
                                "targetVocab": "terms",
                                "prompt": "Dùng từ 'terms' để viết một câu về điều kiện thương mại và tác động đến các nước đang phát triển. Ví dụ: Many African nations face unfavorable terms of trade because they export cheap raw materials and import expensive manufactured goods."
                            },
                            {
                                "targetVocab": "gains",
                                "prompt": "Dùng từ 'gains' để viết một câu về lợi ích từ thương mại và cách phân phối chúng. Ví dụ: The gains from joining the CPTPP are expected to boost Vietnam's GDP by several percentage points over the next decade."
                            },
                            {
                                "targetVocab": "autarky",
                                "prompt": "Dùng từ 'autarky' để viết một câu về lý do tại sao tự cung tự cấp không phải là chiến lược kinh tế hiệu quả. Ví dụ: Cuba's long period of near-autarky resulted in chronic shortages of consumer goods and outdated industrial equipment."
                            },
                            {
                                "targetVocab": "protectionism",
                                "prompt": "Dùng từ 'protectionism' để viết một câu về cuộc tranh luận giữa bảo hộ và tự do thương mại. Ví dụ: The rise of protectionism in several major economies has raised concerns about a potential slowdown in global trade growth."
                            },
                            {
                                "targetVocab": "liberalization",
                                "prompt": "Dùng từ 'liberalization' để viết một câu về tác động của tự do hóa thương mại đến đời sống người dân. Ví dụ: Trade liberalization brought affordable imported goods to Vietnamese consumers, from Korean electronics to Thai snacks."
                            },
                            {
                                "targetVocab": "reciprocal",
                                "prompt": "Dùng từ 'reciprocal' để viết một câu về nguyên tắc có đi có lại trong quan hệ thương mại. Ví dụ: The reciprocal nature of the EU-Vietnam Free Trade Agreement means both sides benefit from lower tariffs on thousands of product categories."
                            },
                            {
                                "targetVocab": "bilateral",
                                "prompt": "Dùng từ 'bilateral' để viết một câu về hiệp định song phương và tác động đến dòng chảy đầu tư. Ví dụ: The bilateral investment treaty between Vietnam and Germany has encouraged German companies to set up factories in Vietnamese industrial zones."
                            },
                            {
                                "targetVocab": "multilateral",
                                "prompt": "Dùng từ 'multilateral' để viết một câu về vai trò của tổ chức đa phương trong thương mại toàn cầu. Ví dụ: Multilateral trade rules set by the WTO help prevent trade wars by providing a framework for resolving disputes between member countries."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về lý thuyết thương mại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về lý thuyết thương mại — từ lợi thế so sánh "
                            "đến chính sách hội nhập quốc tế.\n\n"
                            "Bạn sẽ gặp lại comparative, absolute, advantage, specialization, export, import "
                            "trong phần mở đầu về lý thuyết thương mại cổ điển. "
                            "Tiếp theo, trade, surplus, deficit, balance, terms, gains "
                            "sẽ giúp bạn hiểu kết quả của giao thương quốc tế. "
                            "Và cuối cùng, autarky, protectionism, liberalization, reciprocal, bilateral, multilateral "
                            "sẽ đưa bạn vào thế giới chính sách thương mại hiện đại.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Lý thuyết thương mại — Bức tranh toàn cảnh",
                    "description": "For most of human history, communities produced nearly everything they consumed.",
                    "data": {
                        "text": (
                            "For most of human history, communities produced nearly everything they consumed. "
                            "This state of autarky — complete self-sufficiency — was not a choice but a necessity. "
                            "Without roads, ships, or communication networks, trade between distant regions was slow, "
                            "dangerous, and expensive. But as transportation improved and nations formed, "
                            "a question emerged: should a country try to make everything itself, "
                            "or should it trade with others?\n\n"
                            "Adam Smith offered the first clear answer in 1776. "
                            "He argued that if one country has an absolute advantage in producing a good — "
                            "meaning it can produce that good using fewer resources than any other country — "
                            "then it should specialize in that good and trade for the rest. "
                            "The logic was simple: why grow your own wheat if your neighbor grows it cheaper "
                            "and you can make cloth faster?\n\n"
                            "David Ricardo took this idea further in 1817 with the theory of comparative advantage. "
                            "Even if one country has an absolute advantage in everything, "
                            "both countries still benefit from trade. "
                            "The key insight is opportunity cost. "
                            "A country has a comparative advantage in a good if producing it means giving up "
                            "less of another good compared to its trading partner. "
                            "When each country pursues specialization based on comparative advantage, "
                            "total world output increases and both sides enjoy gains from trade.\n\n"
                            "Consider Vietnam and Japan. Vietnam can produce rice at a very low opportunity cost "
                            "but would need enormous resources to build advanced electronics. "
                            "Japan excels at electronics but would find rice farming relatively expensive. "
                            "Through specialization, Vietnam focuses on rice and Japan focuses on electronics. "
                            "Vietnam can then export rice to Japan and import electronics in return. "
                            "Both countries end up with more of both goods than they could produce alone.\n\n"
                            "The results of trade show up in a country's balance of trade. "
                            "When the value of exports exceeds the value of imports, "
                            "the country runs a trade surplus. "
                            "When imports exceed exports, it runs a trade deficit. "
                            "Neither is inherently good or bad — what matters is the context. "
                            "A deficit might mean consumers enjoy affordable imported goods. "
                            "A surplus might mean the country is a strong exporter "
                            "but its own consumers are not spending enough.\n\n"
                            "Economists also examine the terms of trade — "
                            "the ratio of export prices to import prices. "
                            "When a country's terms of trade improve, each unit of exports buys more imports. "
                            "Developing countries that rely on exporting raw materials "
                            "often face worsening terms of trade as commodity prices fluctuate.\n\n"
                            "Despite the clear gains from trade, not everyone benefits equally. "
                            "Industries that cannot compete with cheaper imports may shrink, "
                            "and workers in those industries may lose their jobs. "
                            "This is the argument behind protectionism — "
                            "the policy of shielding domestic industries through tariffs and quotas. "
                            "Protectionism can save jobs in the short run, "
                            "but it raises prices for consumers and can slow economic growth.\n\n"
                            "The opposite approach is liberalization — "
                            "reducing trade barriers to allow goods and services to flow more freely. "
                            "Vietnam's Doi Moi reforms are a textbook example of successful liberalization. "
                            "By lowering tariffs and welcoming foreign investment, "
                            "Vietnam transformed from one of the poorest countries in Asia "
                            "to a dynamic export-driven economy.\n\n"
                            "Trade agreements are the primary tool for liberalization, "
                            "and they are almost always reciprocal — both sides agree to open their markets. "
                            "A bilateral agreement involves two countries, "
                            "like the Vietnam-EU Free Trade Agreement. "
                            "A multilateral agreement involves many countries, "
                            "like the rules set by the World Trade Organization. "
                            "Both types aim to create a predictable, fair environment for international trade.\n\n"
                            "The story of trade theory is ultimately a story about choices. "
                            "Autarky is costly. Protectionism has trade-offs. "
                            "Liberalization creates winners and losers. "
                            "But the evidence from two centuries of economic history is clear: "
                            "countries that engage in trade, guided by comparative advantage "
                            "and supported by smart policy, tend to grow faster and offer their citizens "
                            "a higher standard of living than those that close their doors."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lý thuyết thương mại — Bức tranh toàn cảnh",
                    "description": "For most of human history, communities produced nearly everything they consumed.",
                    "data": {
                        "text": (
                            "For most of human history, communities produced nearly everything they consumed. "
                            "This state of autarky — complete self-sufficiency — was not a choice but a necessity. "
                            "Without roads, ships, or communication networks, trade between distant regions was slow, "
                            "dangerous, and expensive. But as transportation improved and nations formed, "
                            "a question emerged: should a country try to make everything itself, "
                            "or should it trade with others?\n\n"
                            "Adam Smith offered the first clear answer in 1776. "
                            "He argued that if one country has an absolute advantage in producing a good — "
                            "meaning it can produce that good using fewer resources than any other country — "
                            "then it should specialize in that good and trade for the rest. "
                            "The logic was simple: why grow your own wheat if your neighbor grows it cheaper "
                            "and you can make cloth faster?\n\n"
                            "David Ricardo took this idea further in 1817 with the theory of comparative advantage. "
                            "Even if one country has an absolute advantage in everything, "
                            "both countries still benefit from trade. "
                            "The key insight is opportunity cost. "
                            "A country has a comparative advantage in a good if producing it means giving up "
                            "less of another good compared to its trading partner. "
                            "When each country pursues specialization based on comparative advantage, "
                            "total world output increases and both sides enjoy gains from trade.\n\n"
                            "Consider Vietnam and Japan. Vietnam can produce rice at a very low opportunity cost "
                            "but would need enormous resources to build advanced electronics. "
                            "Japan excels at electronics but would find rice farming relatively expensive. "
                            "Through specialization, Vietnam focuses on rice and Japan focuses on electronics. "
                            "Vietnam can then export rice to Japan and import electronics in return. "
                            "Both countries end up with more of both goods than they could produce alone.\n\n"
                            "The results of trade show up in a country's balance of trade. "
                            "When the value of exports exceeds the value of imports, "
                            "the country runs a trade surplus. "
                            "When imports exceed exports, it runs a trade deficit. "
                            "Neither is inherently good or bad — what matters is the context. "
                            "A deficit might mean consumers enjoy affordable imported goods. "
                            "A surplus might mean the country is a strong exporter "
                            "but its own consumers are not spending enough.\n\n"
                            "Economists also examine the terms of trade — "
                            "the ratio of export prices to import prices. "
                            "When a country's terms of trade improve, each unit of exports buys more imports. "
                            "Developing countries that rely on exporting raw materials "
                            "often face worsening terms of trade as commodity prices fluctuate.\n\n"
                            "Despite the clear gains from trade, not everyone benefits equally. "
                            "Industries that cannot compete with cheaper imports may shrink, "
                            "and workers in those industries may lose their jobs. "
                            "This is the argument behind protectionism — "
                            "the policy of shielding domestic industries through tariffs and quotas. "
                            "Protectionism can save jobs in the short run, "
                            "but it raises prices for consumers and can slow economic growth.\n\n"
                            "The opposite approach is liberalization — "
                            "reducing trade barriers to allow goods and services to flow more freely. "
                            "Vietnam's Doi Moi reforms are a textbook example of successful liberalization. "
                            "By lowering tariffs and welcoming foreign investment, "
                            "Vietnam transformed from one of the poorest countries in Asia "
                            "to a dynamic export-driven economy.\n\n"
                            "Trade agreements are the primary tool for liberalization, "
                            "and they are almost always reciprocal — both sides agree to open their markets. "
                            "A bilateral agreement involves two countries, "
                            "like the Vietnam-EU Free Trade Agreement. "
                            "A multilateral agreement involves many countries, "
                            "like the rules set by the World Trade Organization. "
                            "Both types aim to create a predictable, fair environment for international trade.\n\n"
                            "The story of trade theory is ultimately a story about choices. "
                            "Autarky is costly. Protectionism has trade-offs. "
                            "Liberalization creates winners and losers. "
                            "But the evidence from two centuries of economic history is clear: "
                            "countries that engage in trade, guided by comparative advantage "
                            "and supported by smart policy, tend to grow faster and offer their citizens "
                            "a higher standard of living than those that close their doors."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lý thuyết thương mại — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "For most of human history, communities produced nearly everything they consumed. "
                            "This state of autarky — complete self-sufficiency — was not a choice but a necessity. "
                            "Without roads, ships, or communication networks, trade between distant regions was slow, "
                            "dangerous, and expensive. But as transportation improved and nations formed, "
                            "a question emerged: should a country try to make everything itself, "
                            "or should it trade with others?\n\n"
                            "Adam Smith offered the first clear answer in 1776. "
                            "He argued that if one country has an absolute advantage in producing a good — "
                            "meaning it can produce that good using fewer resources than any other country — "
                            "then it should specialize in that good and trade for the rest. "
                            "The logic was simple: why grow your own wheat if your neighbor grows it cheaper "
                            "and you can make cloth faster?\n\n"
                            "David Ricardo took this idea further in 1817 with the theory of comparative advantage. "
                            "Even if one country has an absolute advantage in everything, "
                            "both countries still benefit from trade. "
                            "The key insight is opportunity cost. "
                            "A country has a comparative advantage in a good if producing it means giving up "
                            "less of another good compared to its trading partner. "
                            "When each country pursues specialization based on comparative advantage, "
                            "total world output increases and both sides enjoy gains from trade.\n\n"
                            "Consider Vietnam and Japan. Vietnam can produce rice at a very low opportunity cost "
                            "but would need enormous resources to build advanced electronics. "
                            "Japan excels at electronics but would find rice farming relatively expensive. "
                            "Through specialization, Vietnam focuses on rice and Japan focuses on electronics. "
                            "Vietnam can then export rice to Japan and import electronics in return. "
                            "Both countries end up with more of both goods than they could produce alone.\n\n"
                            "The results of trade show up in a country's balance of trade. "
                            "When the value of exports exceeds the value of imports, "
                            "the country runs a trade surplus. "
                            "When imports exceed exports, it runs a trade deficit. "
                            "Neither is inherently good or bad — what matters is the context. "
                            "A deficit might mean consumers enjoy affordable imported goods. "
                            "A surplus might mean the country is a strong exporter "
                            "but its own consumers are not spending enough.\n\n"
                            "Economists also examine the terms of trade — "
                            "the ratio of export prices to import prices. "
                            "When a country's terms of trade improve, each unit of exports buys more imports. "
                            "Developing countries that rely on exporting raw materials "
                            "often face worsening terms of trade as commodity prices fluctuate.\n\n"
                            "Despite the clear gains from trade, not everyone benefits equally. "
                            "Industries that cannot compete with cheaper imports may shrink, "
                            "and workers in those industries may lose their jobs. "
                            "This is the argument behind protectionism — "
                            "the policy of shielding domestic industries through tariffs and quotas. "
                            "Protectionism can save jobs in the short run, "
                            "but it raises prices for consumers and can slow economic growth.\n\n"
                            "The opposite approach is liberalization — "
                            "reducing trade barriers to allow goods and services to flow more freely. "
                            "Vietnam's Doi Moi reforms are a textbook example of successful liberalization. "
                            "By lowering tariffs and welcoming foreign investment, "
                            "Vietnam transformed from one of the poorest countries in Asia "
                            "to a dynamic export-driven economy.\n\n"
                            "Trade agreements are the primary tool for liberalization, "
                            "and they are almost always reciprocal — both sides agree to open their markets. "
                            "A bilateral agreement involves two countries, "
                            "like the Vietnam-EU Free Trade Agreement. "
                            "A multilateral agreement involves many countries, "
                            "like the rules set by the World Trade Organization. "
                            "Both types aim to create a predictable, fair environment for international trade.\n\n"
                            "The story of trade theory is ultimately a story about choices. "
                            "Autarky is costly. Protectionism has trade-offs. "
                            "Liberalization creates winners and losers. "
                            "But the evidence from two centuries of economic history is clear: "
                            "countries that engage in trade, guided by comparative advantage "
                            "and supported by smart policy, tend to grow faster and offer their citizens "
                            "a higher standard of living than those that close their doors."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích lý thuyết thương mại",
                    "description": "Viết đoạn văn tiếng Anh phân tích về lý thuyết thương mại sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["comparative", "absolute", "advantage", "specialization", "export", "import", "trade", "surplus", "deficit", "balance", "terms", "gains", "autarky", "protectionism", "liberalization", "reciprocal", "bilateral", "multilateral"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thương mại quốc tế thực tế. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích hành trình hội nhập kinh tế của Việt Nam từ sau Đổi Mới 1986. Giải thích vì sao Việt Nam chuyển từ autarky sang liberalization, comparative advantage của Việt Nam nằm ở đâu, và quá trình ký kết các hiệp định bilateral và multilateral đã tạo ra gains from trade như thế nào.",
                            "Hãy chọn hai quốc gia và phân tích mối quan hệ thương mại giữa họ. Giải thích ai có comparative advantage trong sản phẩm nào, specialization diễn ra như thế nào, balance of trade nghiêng về phía nào (surplus hay deficit), và liệu protectionism hay liberalization là chính sách phù hợp hơn."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay đầy năng lượng.",
                    "data": {
                        "text": (
                            "Xong rồi! Bạn vừa hoàn thành bài học đầu tiên trong chuỗi Thương mại quốc tế. "
                            "Hãy tự hào về điều đó — vì bạn không chỉ học từ vựng, "
                            "bạn đang xây dựng nền tảng để đọc, hiểu và thảo luận về thương mại toàn cầu "
                            "bằng tiếng Anh.\n\n"
                            "Hãy cùng ôn lại một số từ quan trọng nhất — lần này với góc nhìn mới.\n\n"
                            "Comparative advantage — lợi thế so sánh. Đây là ý tưởng thay đổi cách thế giới "
                            "nghĩ về thương mại. Không cần phải giỏi nhất — chỉ cần giỏi tương đối. "
                            "Ví dụ mới: Even a small country like Vietnam can thrive in global trade "
                            "by focusing on industries where it has a comparative advantage, "
                            "such as agriculture and light manufacturing.\n\n"
                            "Gains from trade — lợi ích từ thương mại. Khi hai nước giao thương dựa trên "
                            "lợi thế so sánh, cả hai đều có thêm — đó là gains. "
                            "Ví dụ mới: The gains from trade between ASEAN countries have lifted millions "
                            "of people out of poverty by creating jobs in export-oriented factories.\n\n"
                            "Liberalization — tự do hóa. Đây là con đường mà Việt Nam đã chọn, "
                            "và kết quả thì bạn thấy rõ — từ một nền kinh tế khép kín "
                            "đến một trong những nước xuất khẩu lớn nhất Đông Nam Á. "
                            "Ví dụ mới: India's gradual liberalization of its technology sector "
                            "turned Bangalore into one of the world's leading software development hubs.\n\n"
                            "Bilateral — song phương. Mỗi hiệp định song phương là một cánh cửa mới mở ra. "
                            "Việt Nam đã ký hàng chục hiệp định bilateral, và mỗi hiệp định "
                            "đều tạo thêm cơ hội cho doanh nghiệp và người lao động. "
                            "Ví dụ mới: The bilateral partnership between Vietnam and Australia "
                            "has expanded beyond trade to include education, defense, and cultural exchange.\n\n"
                            "Protectionism — chủ nghĩa bảo hộ. Đôi khi cần thiết, nhưng luôn có cái giá. "
                            "Hiểu protectionism giúp bạn đọc tin tức kinh tế quốc tế "
                            "với con mắt phân tích thay vì chỉ tiếp nhận thụ động. "
                            "Ví dụ mới: The recent wave of protectionism in global trade "
                            "has disrupted supply chains and raised prices for everyday consumer goods.\n\n"
                            "Autarky — tự cung tự cấp. Từ này nhắc nhở chúng ta rằng "
                            "không quốc gia nào có thể thịnh vượng một mình. "
                            "Thương mại không phải là lựa chọn — nó là điều kiện để phát triển. "
                            "Ví dụ mới: The economic struggles of countries that pursued autarky "
                            "serve as a powerful reminder that isolation comes at a steep price.\n\n"
                            "Bạn biết không, 18 từ vựng này không chỉ là công cụ để thi cử. "
                            "Chúng là ngôn ngữ của thế giới kinh doanh quốc tế — "
                            "ngôn ngữ mà bạn sẽ cần khi đọc báo cáo WTO, khi thảo luận với đối tác nước ngoài, "
                            "khi viết luận văn về hội nhập kinh tế.\n\n"
                            "Và bạn không đi một mình. Hàng triệu sinh viên kinh tế trên khắp Việt Nam "
                            "cũng đang trên cùng hành trình này — nâng cấp tiếng Anh chuyên ngành "
                            "để sẵn sàng cho một thế giới ngày càng kết nối. "
                            "Bạn vừa hoàn thành bước đầu tiên, và bước tiếp theo đang chờ.\n\n"
                            "Hẹn gặp lại bạn ở bài học tiếp theo — Trade Barriers, Rào cản thương mại. "
                            "Cùng nhau, chúng ta sẽ chinh phục từng chủ đề một. Chúc bạn học vui nhé!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Trade Theory – Lý Thuyết Thương Mại' AND uid = '{UID}' ORDER BY created_at;")
