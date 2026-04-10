"""
Create curriculum: Trade Organizations – Tổ Chức Thương Mại
Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa (International Trade), curriculum #4
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
W1 = ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"]
W2 = ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"]
W3 = ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Trade Organizations – Tổ Chức Thương Mại",
    "contentTypeTags": [],
    "description": (
        "WTO CÓ 164 THÀNH VIÊN KIỂM SOÁT HƠN 98% THƯƠNG MẠI TOÀN CẦU — VÀ MỌI CUỘC ĐÀM PHÁN ĐỀU DIỄN RA BẰNG TIẾNG ANH.\n\n"
        "Bạn đọc tin về Việt Nam gia nhập CPTPP, nghe giảng viên nhắc đến WTO dispute settlement, "
        "thấy bài tập phân tích trade agreement — nhưng mỗi lần gặp từ ratification hay appellate body, "
        "bạn phải dừng lại tra từ điển. Những thuật ngữ này không khó về mặt khái niệm, "
        "nhưng chúng xuất hiện dày đặc trong mọi tài liệu thương mại quốc tế.\n\n"
        "Hãy nghĩ về vốn từ vựng thương mại quốc tế như tấm hộ chiếu ngôn ngữ — "
        "không có nó, bạn đứng ngoài cửa mọi cuộc thảo luận quan trọng. "
        "18 từ trong bài học này chính là 18 con dấu trên tấm hộ chiếu ấy.\n\n"
        "Sau khóa học, bạn sẽ đọc được báo cáo của WTO mà không cần dừng lại mỗi dòng, "
        "tự tin thảo luận về dispute resolution trong lớp, "
        "và viết bài phân tích về trade organizations bằng tiếng Anh chuyên ngành.\n\n"
        "18 từ vựng — từ organization đến harmonization — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy thương mại quốc tế, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về các tổ chức thương mại quốc tế — "
            "từ WTO đến các hiệp định thương mại tự do. "
            "Bạn sẽ học organization, treaty, agreement, negotiation, ratification, membership trong phần đầu tiên, "
            "nơi bài đọc giải thích cách các quốc gia hình thành và tham gia tổ chức thương mại. "
            "Tiếp theo là dispute, resolution, panel, appellate, ruling, enforcement — "
            "những từ giúp bạn hiểu cơ chế giải quyết tranh chấp thương mại quốc tế. "
            "Cuối cùng, accession, protocol, framework, consensus, sovereignty, harmonization "
            "đưa bạn vào thế giới đàm phán gia nhập và hài hòa hóa quy tắc thương mại. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tài liệu về tổ chức thương mại quốc tế bằng tiếng Anh — "
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
                    "description": "Chào mừng bạn đến với bài học về các tổ chức thương mại quốc tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ tư trong chuỗi từ vựng Thương mại quốc tế — "
                            "chủ đề hôm nay là Tổ chức thương mại, hay trong tiếng Anh là Trade Organizations. "
                            "Khi các quốc gia muốn buôn bán với nhau một cách công bằng và có trật tự, "
                            "họ cần những tổ chức, hiệp ước và thỏa thuận chung. "
                            "Từ WTO đến ASEAN, từ CPTPP đến các hiệp định song phương — "
                            "tất cả đều vận hành bằng một bộ thuật ngữ tiếng Anh mà bạn cần nắm vững.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: organization, treaty, agreement, negotiation, ratification, và membership. "
                            "Đây là những từ nền tảng mà bạn sẽ gặp trong bất kỳ tài liệu nào về thương mại quốc tế.\n\n"
                            "Từ đầu tiên là organization — danh từ — nghĩa là tổ chức, "
                            "một cơ quan hoặc nhóm được thành lập để thực hiện một mục đích chung. "
                            "Ví dụ: 'The World Trade Organization sets the rules for international trade among its member countries.' "
                            "Trong bài đọc, organization được dùng để chỉ các cơ quan quốc tế "
                            "như WTO, nơi các quốc gia cùng nhau xây dựng luật chơi thương mại.\n\n"
                            "Từ thứ hai là treaty — danh từ — nghĩa là hiệp ước, "
                            "một thỏa thuận chính thức giữa hai hoặc nhiều quốc gia có tính ràng buộc pháp lý. "
                            "Ví dụ: 'Vietnam signed a free trade treaty with the European Union that reduced tariffs on hundreds of products.' "
                            "Trong bài đọc, treaty mô tả những cam kết pháp lý mà các quốc gia "
                            "phải tuân thủ sau khi ký kết.\n\n"
                            "Từ thứ ba là agreement — danh từ — nghĩa là thỏa thuận, "
                            "sự đồng ý giữa các bên về các điều khoản cụ thể. "
                            "Ví dụ: 'The trade agreement between the two countries covers everything from agriculture to digital services.' "
                            "Trong bài đọc, agreement thường xuất hiện cùng với treaty — "
                            "agreement có thể rộng hơn và không phải lúc nào cũng có tính ràng buộc pháp lý như treaty.\n\n"
                            "Từ thứ tư là negotiation — danh từ — nghĩa là đàm phán, "
                            "quá trình thảo luận giữa các bên để đạt được thỏa thuận. "
                            "Ví dụ: 'The negotiation of the CPTPP took several years because eleven countries had to agree on thousands of trade rules.' "
                            "Trong bài đọc, negotiation mô tả quá trình dài và phức tạp "
                            "mà các quốc gia phải trải qua trước khi ký kết hiệp định.\n\n"
                            "Từ thứ năm là ratification — danh từ — nghĩa là phê chuẩn, "
                            "hành động chính thức phê duyệt một hiệp ước hoặc thỏa thuận để nó có hiệu lực pháp lý. "
                            "Ví dụ: 'The treaty does not take effect until ratification by at least six of the signatory nations.' "
                            "Trong bài đọc, ratification là bước cuối cùng — "
                            "sau khi đàm phán và ký kết, quốc hội mỗi nước phải phê chuẩn để hiệp ước có hiệu lực.\n\n"
                            "Từ cuối cùng là membership — danh từ — nghĩa là tư cách thành viên, "
                            "trạng thái thuộc về một tổ chức hoặc nhóm. "
                            "Ví dụ: 'Vietnam's membership in the WTO since 2007 has opened its markets to global competition.' "
                            "Trong bài đọc, membership cho thấy việc gia nhập một tổ chức thương mại "
                            "đi kèm với cả quyền lợi lẫn nghĩa vụ.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách các tổ chức thương mại quốc tế được hình thành nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tổ chức và hiệp ước thương mại",
                    "description": "Học 6 từ: organization, treaty, agreement, negotiation, ratification, membership",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tổ chức và hiệp ước thương mại",
                    "description": "Học 6 từ: organization, treaty, agreement, negotiation, ratification, membership",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tổ chức và hiệp ước thương mại",
                    "description": "Học 6 từ: organization, treaty, agreement, negotiation, ratification, membership",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tổ chức và hiệp ước thương mại",
                    "description": "Học 6 từ: organization, treaty, agreement, negotiation, ratification, membership",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Tổ chức và hiệp ước thương mại",
                    "description": "Học 6 từ: organization, treaty, agreement, negotiation, ratification, membership",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tổ chức thương mại quốc tế",
                    "description": "International trade does not happen in a vacuum — it is shaped by organizations, treaties, and agreements.",
                    "data": {
                        "text": (
                            "International trade does not happen in a vacuum — it is shaped by organizations, treaties, and agreements "
                            "that countries create together. Without these structures, trade between nations would be chaotic, "
                            "unpredictable, and often unfair.\n\n"
                            "The most important trade organization in the world is the World Trade Organization, or WTO. "
                            "Founded in 1995, the WTO replaced an older system called GATT — the General Agreement on Tariffs and Trade. "
                            "The organization provides a forum where countries negotiate trade rules, "
                            "resolve disputes, and work toward reducing barriers to commerce. "
                            "Today, the WTO has over one hundred and sixty member countries, "
                            "and its rules cover more than ninety-eight percent of global trade.\n\n"
                            "When countries want to formalize their trade relationship, they sign a treaty. "
                            "A treaty is a legally binding document between two or more nations. "
                            "For example, the Comprehensive and Progressive Agreement for Trans-Pacific Partnership, known as CPTPP, "
                            "is a treaty among eleven countries in the Asia-Pacific region. "
                            "It covers trade in goods, services, investment, and intellectual property.\n\n"
                            "Not all international deals are treaties. Some are broader agreements "
                            "that set general principles without the same level of legal obligation. "
                            "An agreement might outline goals for cooperation in areas like digital trade or environmental standards. "
                            "The difference matters: a treaty usually requires formal approval by a country's legislature, "
                            "while an agreement may only need executive action.\n\n"
                            "Before any treaty or agreement is signed, there is a long process of negotiation. "
                            "Negotiation is the back-and-forth discussion where each country tries to protect its own interests "
                            "while finding common ground with others. "
                            "Trade negotiations can take years. The Doha Round of WTO negotiations, "
                            "which began in 2001, has still not been completed after more than two decades.\n\n"
                            "Even after negotiation is finished and leaders sign a treaty, "
                            "the process is not over. The treaty must go through ratification — "
                            "the formal approval by each country's government or parliament. "
                            "Ratification turns a signed document into a binding commitment. "
                            "Some treaties require ratification by a minimum number of countries before they take effect.\n\n"
                            "Finally, membership in a trade organization comes with both rights and responsibilities. "
                            "Members gain access to lower tariffs, dispute resolution mechanisms, and a voice in setting trade rules. "
                            "But they must also follow the organization's rules, open their markets as promised, "
                            "and accept decisions made by the group. "
                            "For developing countries like Vietnam, membership in the WTO and regional trade groups "
                            "has been a powerful engine for economic growth — but it also means adapting domestic laws "
                            "and industries to meet international standards."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tổ chức thương mại quốc tế",
                    "description": "International trade does not happen in a vacuum — it is shaped by organizations, treaties, and agreements.",
                    "data": {
                        "text": (
                            "International trade does not happen in a vacuum — it is shaped by organizations, treaties, and agreements "
                            "that countries create together. Without these structures, trade between nations would be chaotic, "
                            "unpredictable, and often unfair.\n\n"
                            "The most important trade organization in the world is the World Trade Organization, or WTO. "
                            "Founded in 1995, the WTO replaced an older system called GATT — the General Agreement on Tariffs and Trade. "
                            "The organization provides a forum where countries negotiate trade rules, "
                            "resolve disputes, and work toward reducing barriers to commerce. "
                            "Today, the WTO has over one hundred and sixty member countries, "
                            "and its rules cover more than ninety-eight percent of global trade.\n\n"
                            "When countries want to formalize their trade relationship, they sign a treaty. "
                            "A treaty is a legally binding document between two or more nations. "
                            "For example, the Comprehensive and Progressive Agreement for Trans-Pacific Partnership, known as CPTPP, "
                            "is a treaty among eleven countries in the Asia-Pacific region. "
                            "It covers trade in goods, services, investment, and intellectual property.\n\n"
                            "Not all international deals are treaties. Some are broader agreements "
                            "that set general principles without the same level of legal obligation. "
                            "An agreement might outline goals for cooperation in areas like digital trade or environmental standards. "
                            "The difference matters: a treaty usually requires formal approval by a country's legislature, "
                            "while an agreement may only need executive action.\n\n"
                            "Before any treaty or agreement is signed, there is a long process of negotiation. "
                            "Negotiation is the back-and-forth discussion where each country tries to protect its own interests "
                            "while finding common ground with others. "
                            "Trade negotiations can take years. The Doha Round of WTO negotiations, "
                            "which began in 2001, has still not been completed after more than two decades.\n\n"
                            "Even after negotiation is finished and leaders sign a treaty, "
                            "the process is not over. The treaty must go through ratification — "
                            "the formal approval by each country's government or parliament. "
                            "Ratification turns a signed document into a binding commitment. "
                            "Some treaties require ratification by a minimum number of countries before they take effect.\n\n"
                            "Finally, membership in a trade organization comes with both rights and responsibilities. "
                            "Members gain access to lower tariffs, dispute resolution mechanisms, and a voice in setting trade rules. "
                            "But they must also follow the organization's rules, open their markets as promised, "
                            "and accept decisions made by the group. "
                            "For developing countries like Vietnam, membership in the WTO and regional trade groups "
                            "has been a powerful engine for economic growth — but it also means adapting domestic laws "
                            "and industries to meet international standards."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tổ chức thương mại quốc tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "International trade does not happen in a vacuum — it is shaped by organizations, treaties, and agreements "
                            "that countries create together. Without these structures, trade between nations would be chaotic, "
                            "unpredictable, and often unfair.\n\n"
                            "The most important trade organization in the world is the World Trade Organization, or WTO. "
                            "Founded in 1995, the WTO replaced an older system called GATT — the General Agreement on Tariffs and Trade. "
                            "The organization provides a forum where countries negotiate trade rules, "
                            "resolve disputes, and work toward reducing barriers to commerce. "
                            "Today, the WTO has over one hundred and sixty member countries, "
                            "and its rules cover more than ninety-eight percent of global trade.\n\n"
                            "When countries want to formalize their trade relationship, they sign a treaty. "
                            "A treaty is a legally binding document between two or more nations. "
                            "For example, the Comprehensive and Progressive Agreement for Trans-Pacific Partnership, known as CPTPP, "
                            "is a treaty among eleven countries in the Asia-Pacific region. "
                            "It covers trade in goods, services, investment, and intellectual property.\n\n"
                            "Not all international deals are treaties. Some are broader agreements "
                            "that set general principles without the same level of legal obligation. "
                            "An agreement might outline goals for cooperation in areas like digital trade or environmental standards. "
                            "The difference matters: a treaty usually requires formal approval by a country's legislature, "
                            "while an agreement may only need executive action.\n\n"
                            "Before any treaty or agreement is signed, there is a long process of negotiation. "
                            "Negotiation is the back-and-forth discussion where each country tries to protect its own interests "
                            "while finding common ground with others. "
                            "Trade negotiations can take years. The Doha Round of WTO negotiations, "
                            "which began in 2001, has still not been completed after more than two decades.\n\n"
                            "Even after negotiation is finished and leaders sign a treaty, "
                            "the process is not over. The treaty must go through ratification — "
                            "the formal approval by each country's government or parliament. "
                            "Ratification turns a signed document into a binding commitment. "
                            "Some treaties require ratification by a minimum number of countries before they take effect.\n\n"
                            "Finally, membership in a trade organization comes with both rights and responsibilities. "
                            "Members gain access to lower tariffs, dispute resolution mechanisms, and a voice in setting trade rules. "
                            "But they must also follow the organization's rules, open their markets as promised, "
                            "and accept decisions made by the group. "
                            "For developing countries like Vietnam, membership in the WTO and regional trade groups "
                            "has been a powerful engine for economic growth — but it also means adapting domestic laws "
                            "and industries to meet international standards."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tổ chức và hiệp ước thương mại",
                    "description": "Viết câu sử dụng 6 từ vựng về tổ chức và hiệp ước thương mại.",
                    "data": {
                        "vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership"],
                        "items": [
                            {
                                "targetVocab": "organization",
                                "prompt": "Dùng từ 'organization' để viết một câu về vai trò của một tổ chức thương mại quốc tế trong việc thiết lập luật chơi cho thương mại toàn cầu. Ví dụ: The World Trade Organization provides a platform where countries can negotiate trade rules and settle commercial disputes peacefully."
                            },
                            {
                                "targetVocab": "treaty",
                                "prompt": "Dùng từ 'treaty' để viết một câu về một hiệp ước thương mại giữa các quốc gia và tác động của nó. Ví dụ: The free trade treaty between Vietnam and the European Union eliminated tariffs on over ninety-nine percent of goods traded between the two sides."
                            },
                            {
                                "targetVocab": "agreement",
                                "prompt": "Dùng từ 'agreement' để viết một câu về một thỏa thuận thương mại và các lĩnh vực mà nó bao phủ. Ví dụ: The regional trade agreement covers not only tariff reductions but also rules on labor standards and environmental protection."
                            },
                            {
                                "targetVocab": "negotiation",
                                "prompt": "Dùng từ 'negotiation' để viết một câu về quá trình đàm phán thương mại giữa các quốc gia. Ví dụ: The negotiation of the RCEP agreement involved fifteen countries and took eight years of discussions before all parties could agree on the final terms."
                            },
                            {
                                "targetVocab": "ratification",
                                "prompt": "Dùng từ 'ratification' để viết một câu về quá trình phê chuẩn một hiệp ước thương mại. Ví dụ: The trade deal was signed in 2019, but ratification by the national assembly did not happen until the following year due to political debates."
                            },
                            {
                                "targetVocab": "membership",
                                "prompt": "Dùng từ 'membership' để viết một câu về lợi ích hoặc nghĩa vụ khi một quốc gia gia nhập tổ chức thương mại. Ví dụ: Vietnam's membership in ASEAN has given its exporters preferential access to a market of over six hundred million consumers."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về giải quyết tranh chấp thương mại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "organization — tổ chức, treaty — hiệp ước, agreement — thỏa thuận, "
                            "negotiation — đàm phán, ratification — phê chuẩn, và membership — tư cách thành viên. "
                            "Bạn đã hiểu cách các quốc gia hình thành và tham gia tổ chức thương mại. "
                            "Bây giờ, chúng ta sẽ đi vào một khía cạnh quan trọng không kém: "
                            "điều gì xảy ra khi các thành viên không đồng ý với nhau?\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: dispute, resolution, panel, appellate, ruling, và enforcement. "
                            "Đây là bộ từ vựng về cơ chế giải quyết tranh chấp — "
                            "hệ thống 'tòa án' của thương mại quốc tế.\n\n"
                            "Từ đầu tiên là dispute — danh từ — nghĩa là tranh chấp, "
                            "bất đồng chính thức giữa hai hoặc nhiều bên về một vấn đề thương mại. "
                            "Ví dụ: 'A trade dispute arose between the two countries when one side imposed unexpected tariffs on steel imports.' "
                            "Trong bài đọc, dispute mô tả những xung đột thương mại "
                            "mà các quốc gia đưa ra trước WTO để giải quyết.\n\n"
                            "Từ thứ hai là resolution — danh từ — nghĩa là giải quyết, "
                            "quá trình hoặc kết quả của việc tìm ra giải pháp cho một tranh chấp. "
                            "Ví dụ: 'The WTO's dispute resolution system has handled over six hundred cases since 1995.' "
                            "Trong bài đọc, resolution là mục tiêu cuối cùng — "
                            "đưa tranh chấp đến một kết quả mà các bên chấp nhận.\n\n"
                            "Từ thứ ba là panel — danh từ — nghĩa là hội đồng xét xử, "
                            "nhóm chuyên gia được chỉ định để xem xét và đưa ra phán quyết về một tranh chấp. "
                            "Ví dụ: 'The WTO appointed a panel of three trade experts to examine whether the tariffs violated international rules.' "
                            "Trong bài đọc, panel là bước đầu tiên trong quy trình xét xử — "
                            "họ nghe lập luận của cả hai bên và đưa ra báo cáo.\n\n"
                            "Từ thứ tư là appellate — tính từ — nghĩa là thuộc về phúc thẩm, "
                            "liên quan đến việc xem xét lại một phán quyết đã được đưa ra. "
                            "Ví dụ: 'If a country disagrees with the panel's decision, it can appeal to the appellate body for a second review.' "
                            "Trong bài đọc, appellate body là cấp xét xử cao nhất tại WTO — "
                            "quyết định của họ gần như là cuối cùng.\n\n"
                            "Từ thứ năm là ruling — danh từ — nghĩa là phán quyết, "
                            "quyết định chính thức của một cơ quan xét xử về một vụ tranh chấp. "
                            "Ví dụ: 'The ruling stated that the country's subsidies to its fishing industry were illegal under WTO rules.' "
                            "Trong bài đọc, ruling là kết quả cuối cùng của quá trình xét xử — "
                            "nó xác định bên nào đúng và bên nào phải thay đổi chính sách.\n\n"
                            "Từ cuối cùng là enforcement — danh từ — nghĩa là thực thi, "
                            "việc đảm bảo rằng các quy tắc và phán quyết được tuân thủ. "
                            "Ví dụ: 'The biggest challenge in international trade law is enforcement — there is no global police force to make countries obey.' "
                            "Trong bài đọc, enforcement là thách thức lớn nhất — "
                            "WTO có thể đưa ra phán quyết, nhưng việc buộc các nước tuân thủ lại là chuyện khác.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về cơ chế giải quyết tranh chấp thương mại quốc tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Giải quyết tranh chấp thương mại",
                    "description": "Học 6 từ: dispute, resolution, panel, appellate, ruling, enforcement",
                    "data": {"vocabList": ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Giải quyết tranh chấp thương mại",
                    "description": "Học 6 từ: dispute, resolution, panel, appellate, ruling, enforcement",
                    "data": {"vocabList": ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Giải quyết tranh chấp thương mại",
                    "description": "Học 6 từ: dispute, resolution, panel, appellate, ruling, enforcement",
                    "data": {"vocabList": ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Giải quyết tranh chấp thương mại",
                    "description": "Học 6 từ: dispute, resolution, panel, appellate, ruling, enforcement",
                    "data": {"vocabList": ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Giải quyết tranh chấp thương mại",
                    "description": "Học 6 từ: dispute, resolution, panel, appellate, ruling, enforcement",
                    "data": {"vocabList": ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cơ chế giải quyết tranh chấp thương mại",
                    "description": "When countries disagree about trade, they need a fair system to settle their differences.",
                    "data": {
                        "text": (
                            "When countries disagree about trade, they need a fair system to settle their differences. "
                            "Without such a system, powerful nations could bully smaller ones, "
                            "and trade conflicts could escalate into economic wars. "
                            "This is why the WTO created one of the most important mechanisms in international trade: "
                            "the dispute settlement system.\n\n"
                            "A trade dispute begins when one country believes that another country has broken the rules. "
                            "For example, Country A might claim that Country B is giving illegal subsidies to its steel industry, "
                            "making its steel cheaper than it should be on the world market. "
                            "Country A can file a formal complaint with the WTO.\n\n"
                            "The first step in resolution is consultation. "
                            "The two countries must sit down and try to solve the problem through direct talks. "
                            "Many disputes are actually resolved at this stage — "
                            "sometimes all it takes is a conversation to find a compromise. "
                            "But if consultation fails, the complaining country can ask the WTO to form a panel.\n\n"
                            "A panel is a group of three trade experts chosen to examine the case. "
                            "They review the evidence, listen to arguments from both sides, "
                            "and produce a detailed report with their findings. "
                            "The panel's report includes a ruling — a formal decision about whether the accused country "
                            "has violated WTO rules. The entire process typically takes about one year.\n\n"
                            "If either side disagrees with the panel's ruling, it can appeal to the appellate body. "
                            "The appellate body is a standing group of seven legal experts "
                            "who review the panel's legal reasoning. "
                            "They can uphold, modify, or reverse the original ruling. "
                            "The appellate body's decision is final — there is no further appeal.\n\n"
                            "Once a ruling is made, the losing country is expected to change its policies to comply. "
                            "But enforcement is the weakest link in the system. "
                            "The WTO has no police force and cannot directly punish a country. "
                            "Instead, if the losing country refuses to comply, "
                            "the winning country is authorized to impose retaliatory tariffs — "
                            "essentially, to raise its own trade barriers as compensation.\n\n"
                            "Despite its limitations, the WTO dispute settlement system has been remarkably successful. "
                            "Since 1995, over six hundred disputes have been filed, "
                            "and the vast majority have been resolved through consultation or panel rulings. "
                            "The system gives small countries the same legal standing as large ones, "
                            "which is a significant achievement in international relations. "
                            "For Vietnam, understanding this system is essential — "
                            "as the country's trade grows, so does the likelihood of being involved in disputes, "
                            "either as a complainant or as a respondent."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Cơ chế giải quyết tranh chấp thương mại",
                    "description": "When countries disagree about trade, they need a fair system to settle their differences.",
                    "data": {
                        "text": (
                            "When countries disagree about trade, they need a fair system to settle their differences. "
                            "Without such a system, powerful nations could bully smaller ones, "
                            "and trade conflicts could escalate into economic wars. "
                            "This is why the WTO created one of the most important mechanisms in international trade: "
                            "the dispute settlement system.\n\n"
                            "A trade dispute begins when one country believes that another country has broken the rules. "
                            "For example, Country A might claim that Country B is giving illegal subsidies to its steel industry, "
                            "making its steel cheaper than it should be on the world market. "
                            "Country A can file a formal complaint with the WTO.\n\n"
                            "The first step in resolution is consultation. "
                            "The two countries must sit down and try to solve the problem through direct talks. "
                            "Many disputes are actually resolved at this stage — "
                            "sometimes all it takes is a conversation to find a compromise. "
                            "But if consultation fails, the complaining country can ask the WTO to form a panel.\n\n"
                            "A panel is a group of three trade experts chosen to examine the case. "
                            "They review the evidence, listen to arguments from both sides, "
                            "and produce a detailed report with their findings. "
                            "The panel's report includes a ruling — a formal decision about whether the accused country "
                            "has violated WTO rules. The entire process typically takes about one year.\n\n"
                            "If either side disagrees with the panel's ruling, it can appeal to the appellate body. "
                            "The appellate body is a standing group of seven legal experts "
                            "who review the panel's legal reasoning. "
                            "They can uphold, modify, or reverse the original ruling. "
                            "The appellate body's decision is final — there is no further appeal.\n\n"
                            "Once a ruling is made, the losing country is expected to change its policies to comply. "
                            "But enforcement is the weakest link in the system. "
                            "The WTO has no police force and cannot directly punish a country. "
                            "Instead, if the losing country refuses to comply, "
                            "the winning country is authorized to impose retaliatory tariffs — "
                            "essentially, to raise its own trade barriers as compensation.\n\n"
                            "Despite its limitations, the WTO dispute settlement system has been remarkably successful. "
                            "Since 1995, over six hundred disputes have been filed, "
                            "and the vast majority have been resolved through consultation or panel rulings. "
                            "The system gives small countries the same legal standing as large ones, "
                            "which is a significant achievement in international relations. "
                            "For Vietnam, understanding this system is essential — "
                            "as the country's trade grows, so does the likelihood of being involved in disputes, "
                            "either as a complainant or as a respondent."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cơ chế giải quyết tranh chấp thương mại",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When countries disagree about trade, they need a fair system to settle their differences. "
                            "Without such a system, powerful nations could bully smaller ones, "
                            "and trade conflicts could escalate into economic wars. "
                            "This is why the WTO created one of the most important mechanisms in international trade: "
                            "the dispute settlement system.\n\n"
                            "A trade dispute begins when one country believes that another country has broken the rules. "
                            "For example, Country A might claim that Country B is giving illegal subsidies to its steel industry, "
                            "making its steel cheaper than it should be on the world market. "
                            "Country A can file a formal complaint with the WTO.\n\n"
                            "The first step in resolution is consultation. "
                            "The two countries must sit down and try to solve the problem through direct talks. "
                            "Many disputes are actually resolved at this stage — "
                            "sometimes all it takes is a conversation to find a compromise. "
                            "But if consultation fails, the complaining country can ask the WTO to form a panel.\n\n"
                            "A panel is a group of three trade experts chosen to examine the case. "
                            "They review the evidence, listen to arguments from both sides, "
                            "and produce a detailed report with their findings. "
                            "The panel's report includes a ruling — a formal decision about whether the accused country "
                            "has violated WTO rules. The entire process typically takes about one year.\n\n"
                            "If either side disagrees with the panel's ruling, it can appeal to the appellate body. "
                            "The appellate body is a standing group of seven legal experts "
                            "who review the panel's legal reasoning. "
                            "They can uphold, modify, or reverse the original ruling. "
                            "The appellate body's decision is final — there is no further appeal.\n\n"
                            "Once a ruling is made, the losing country is expected to change its policies to comply. "
                            "But enforcement is the weakest link in the system. "
                            "The WTO has no police force and cannot directly punish a country. "
                            "Instead, if the losing country refuses to comply, "
                            "the winning country is authorized to impose retaliatory tariffs — "
                            "essentially, to raise its own trade barriers as compensation.\n\n"
                            "Despite its limitations, the WTO dispute settlement system has been remarkably successful. "
                            "Since 1995, over six hundred disputes have been filed, "
                            "and the vast majority have been resolved through consultation or panel rulings. "
                            "The system gives small countries the same legal standing as large ones, "
                            "which is a significant achievement in international relations. "
                            "For Vietnam, understanding this system is essential — "
                            "as the country's trade grows, so does the likelihood of being involved in disputes, "
                            "either as a complainant or as a respondent."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Giải quyết tranh chấp thương mại",
                    "description": "Viết câu sử dụng 6 từ vựng về giải quyết tranh chấp.",
                    "data": {
                        "vocabList": ["dispute", "resolution", "panel", "appellate", "ruling", "enforcement"],
                        "items": [
                            {
                                "targetVocab": "dispute",
                                "prompt": "Dùng từ 'dispute' để viết một câu về một tranh chấp thương mại giữa hai quốc gia. Ví dụ: The trade dispute between the two neighboring countries began when one side accused the other of dumping cheap textiles on its market."
                            },
                            {
                                "targetVocab": "resolution",
                                "prompt": "Dùng từ 'resolution' để viết một câu về quá trình giải quyết một bất đồng thương mại. Ví dụ: The resolution of the fishing rights dispute took three years of negotiations before both countries agreed to share access to the coastal waters."
                            },
                            {
                                "targetVocab": "panel",
                                "prompt": "Dùng từ 'panel' để viết một câu về hội đồng xét xử được thành lập để xem xét một vụ tranh chấp. Ví dụ: The WTO panel concluded that the import restrictions violated the principle of non-discrimination and recommended their removal."
                            },
                            {
                                "targetVocab": "appellate",
                                "prompt": "Dùng từ 'appellate' để viết một câu về cơ quan phúc thẩm xem xét lại một phán quyết thương mại. Ví dụ: The losing country immediately filed an appeal with the appellate body, arguing that the panel had misinterpreted the trade agreement."
                            },
                            {
                                "targetVocab": "ruling",
                                "prompt": "Dùng từ 'ruling' để viết một câu về phán quyết của một cơ quan thương mại quốc tế. Ví dụ: The ruling required the country to remove its agricultural subsidies within eighteen months or face authorized retaliation from trading partners."
                            },
                            {
                                "targetVocab": "enforcement",
                                "prompt": "Dùng từ 'enforcement' để viết một câu về thách thức trong việc thực thi các quy tắc thương mại quốc tế. Ví dụ: Effective enforcement of trade rules remains difficult because no international body has the power to force a sovereign nation to change its laws."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về gia nhập và hài hòa hóa thương mại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: organization, treaty, agreement, negotiation, ratification, membership — "
                            "những khái niệm về cách các quốc gia hình thành và tham gia tổ chức thương mại. "
                            "Trong phần 2, bạn đã học thêm dispute, resolution, panel, appellate, ruling, enforcement — "
                            "bộ từ vựng về cơ chế giải quyết tranh chấp thương mại quốc tế.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh quan trọng khác: "
                            "quá trình gia nhập tổ chức thương mại và việc hài hòa hóa quy tắc giữa các quốc gia. "
                            "Bạn sẽ học 6 từ mới: accession, protocol, framework, consensus, sovereignty, và harmonization.\n\n"
                            "Từ đầu tiên là accession — danh từ — nghĩa là gia nhập, "
                            "quá trình chính thức trở thành thành viên của một tổ chức quốc tế. "
                            "Ví dụ: 'Vietnam's accession to the WTO in 2007 required years of preparation and reform of domestic trade laws.' "
                            "Trong bài đọc, accession mô tả hành trình dài và phức tạp "
                            "mà một quốc gia phải trải qua để được chấp nhận vào tổ chức thương mại.\n\n"
                            "Từ thứ hai là protocol — danh từ — nghĩa là nghị định thư, "
                            "một văn bản bổ sung hoặc sửa đổi cho một hiệp ước hoặc thỏa thuận hiện có. "
                            "Ví dụ: 'The protocol on digital trade was added to the original agreement to address the growth of e-commerce.' "
                            "Trong bài đọc, protocol là công cụ để cập nhật và mở rộng "
                            "các hiệp ước thương mại mà không cần đàm phán lại toàn bộ.\n\n"
                            "Từ thứ ba là framework — danh từ — nghĩa là khuôn khổ, "
                            "cấu trúc hoặc hệ thống nguyên tắc cơ bản làm nền tảng cho hành động. "
                            "Ví dụ: 'The ASEAN Economic Community provides a framework for economic integration among Southeast Asian nations.' "
                            "Trong bài đọc, framework là bộ khung mà các quốc gia dựa vào "
                            "để xây dựng các quy tắc thương mại cụ thể.\n\n"
                            "Từ thứ tư là consensus — danh từ — nghĩa là đồng thuận, "
                            "sự nhất trí chung giữa tất cả các bên mà không cần bỏ phiếu chính thức. "
                            "Ví dụ: 'WTO decisions are made by consensus, meaning every member must agree before a new rule is adopted.' "
                            "Trong bài đọc, consensus giải thích vì sao đàm phán tại WTO thường rất chậm — "
                            "khi hơn 160 quốc gia phải đồng ý, mỗi quyết định đều mất thời gian.\n\n"
                            "Từ thứ năm là sovereignty — danh từ — nghĩa là chủ quyền, "
                            "quyền tự quyết của một quốc gia trong việc quản lý lãnh thổ và chính sách của mình. "
                            "Ví dụ: 'Some countries resist joining trade organizations because they fear losing sovereignty over their economic policies.' "
                            "Trong bài đọc, sovereignty là mối lo ngại lớn nhất — "
                            "khi gia nhập tổ chức thương mại, quốc gia phải chấp nhận một số giới hạn về quyền tự quyết.\n\n"
                            "Từ cuối cùng là harmonization — danh từ — nghĩa là hài hòa hóa, "
                            "quá trình làm cho các quy tắc, tiêu chuẩn hoặc luật pháp giữa các quốc gia trở nên thống nhất. "
                            "Ví dụ: 'The harmonization of food safety standards across ASEAN countries makes it easier for producers to export to the entire region.' "
                            "Trong bài đọc, harmonization là mục tiêu dài hạn — "
                            "khi các nước có cùng tiêu chuẩn, thương mại trở nên dễ dàng và ít tốn kém hơn.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về gia nhập và hài hòa hóa thương mại nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Gia nhập và hài hòa hóa thương mại",
                    "description": "Học 6 từ: accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Gia nhập và hài hòa hóa thương mại",
                    "description": "Học 6 từ: accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Gia nhập và hài hòa hóa thương mại",
                    "description": "Học 6 từ: accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Gia nhập và hài hòa hóa thương mại",
                    "description": "Học 6 từ: accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Gia nhập và hài hòa hóa thương mại",
                    "description": "Học 6 từ: accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Gia nhập và hài hòa hóa quy tắc thương mại",
                    "description": "Joining a trade organization is not as simple as signing a document.",
                    "data": {
                        "text": (
                            "Joining a trade organization is not as simple as signing a document. "
                            "For most countries, the process of accession takes years of preparation, "
                            "negotiation, and domestic reform. "
                            "Vietnam's accession to the WTO, for example, began in 1995 and was not completed until 2007 — "
                            "a journey of twelve years.\n\n"
                            "During accession, the applying country must demonstrate that its trade policies "
                            "meet the organization's standards. "
                            "This often means changing domestic laws, reducing tariffs, "
                            "and opening markets that were previously protected. "
                            "Existing members negotiate with the applicant to ensure that the terms of entry are fair. "
                            "Each member can raise concerns and request specific commitments.\n\n"
                            "Once the terms are agreed upon, they are recorded in an accession protocol. "
                            "A protocol is a formal document that supplements or amends an existing treaty. "
                            "In the WTO context, the accession protocol lists all the commitments "
                            "the new member has made — which tariffs it will lower, "
                            "which markets it will open, and on what timeline. "
                            "The protocol becomes a binding part of the WTO's legal framework.\n\n"
                            "The concept of a framework is central to how trade organizations operate. "
                            "A framework is a set of basic principles and rules that guide decision-making. "
                            "The WTO framework includes agreements on goods, services, and intellectual property. "
                            "Regional organizations like ASEAN have their own frameworks "
                            "that cover economic cooperation, investment, and labor mobility.\n\n"
                            "Decision-making within trade organizations often relies on consensus. "
                            "Consensus means that all members must agree — or at least not actively object — "
                            "before a decision is adopted. "
                            "This gives every country, no matter how small, a voice. "
                            "But it also means that a single country can block progress. "
                            "The WTO's Doha Round stalled partly because consensus could not be reached "
                            "on agricultural subsidies between developed and developing nations.\n\n"
                            "One of the most sensitive issues in trade organizations is sovereignty. "
                            "Sovereignty is a country's right to govern itself and make its own laws. "
                            "When a country joins a trade organization, it agrees to follow certain rules "
                            "that may limit its freedom to set tariffs, subsidize industries, or regulate imports. "
                            "Critics argue that this erodes national sovereignty. "
                            "Supporters counter that the benefits of open trade — "
                            "more jobs, lower prices, faster growth — outweigh the loss of policy flexibility.\n\n"
                            "Finally, trade organizations work toward harmonization — "
                            "making rules and standards consistent across countries. "
                            "Harmonization of product safety standards, for instance, "
                            "means that a Vietnamese manufacturer only needs to meet one set of requirements "
                            "to sell in multiple markets. "
                            "Without harmonization, exporters face a patchwork of different regulations, "
                            "which raises costs and slows trade. "
                            "The push for harmonization is one of the most practical benefits "
                            "that trade organizations deliver to businesses and consumers alike."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Gia nhập và hài hòa hóa quy tắc thương mại",
                    "description": "Joining a trade organization is not as simple as signing a document.",
                    "data": {
                        "text": (
                            "Joining a trade organization is not as simple as signing a document. "
                            "For most countries, the process of accession takes years of preparation, "
                            "negotiation, and domestic reform. "
                            "Vietnam's accession to the WTO, for example, began in 1995 and was not completed until 2007 — "
                            "a journey of twelve years.\n\n"
                            "During accession, the applying country must demonstrate that its trade policies "
                            "meet the organization's standards. "
                            "This often means changing domestic laws, reducing tariffs, "
                            "and opening markets that were previously protected. "
                            "Existing members negotiate with the applicant to ensure that the terms of entry are fair. "
                            "Each member can raise concerns and request specific commitments.\n\n"
                            "Once the terms are agreed upon, they are recorded in an accession protocol. "
                            "A protocol is a formal document that supplements or amends an existing treaty. "
                            "In the WTO context, the accession protocol lists all the commitments "
                            "the new member has made — which tariffs it will lower, "
                            "which markets it will open, and on what timeline. "
                            "The protocol becomes a binding part of the WTO's legal framework.\n\n"
                            "The concept of a framework is central to how trade organizations operate. "
                            "A framework is a set of basic principles and rules that guide decision-making. "
                            "The WTO framework includes agreements on goods, services, and intellectual property. "
                            "Regional organizations like ASEAN have their own frameworks "
                            "that cover economic cooperation, investment, and labor mobility.\n\n"
                            "Decision-making within trade organizations often relies on consensus. "
                            "Consensus means that all members must agree — or at least not actively object — "
                            "before a decision is adopted. "
                            "This gives every country, no matter how small, a voice. "
                            "But it also means that a single country can block progress. "
                            "The WTO's Doha Round stalled partly because consensus could not be reached "
                            "on agricultural subsidies between developed and developing nations.\n\n"
                            "One of the most sensitive issues in trade organizations is sovereignty. "
                            "Sovereignty is a country's right to govern itself and make its own laws. "
                            "When a country joins a trade organization, it agrees to follow certain rules "
                            "that may limit its freedom to set tariffs, subsidize industries, or regulate imports. "
                            "Critics argue that this erodes national sovereignty. "
                            "Supporters counter that the benefits of open trade — "
                            "more jobs, lower prices, faster growth — outweigh the loss of policy flexibility.\n\n"
                            "Finally, trade organizations work toward harmonization — "
                            "making rules and standards consistent across countries. "
                            "Harmonization of product safety standards, for instance, "
                            "means that a Vietnamese manufacturer only needs to meet one set of requirements "
                            "to sell in multiple markets. "
                            "Without harmonization, exporters face a patchwork of different regulations, "
                            "which raises costs and slows trade. "
                            "The push for harmonization is one of the most practical benefits "
                            "that trade organizations deliver to businesses and consumers alike."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Gia nhập và hài hòa hóa quy tắc thương mại",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Joining a trade organization is not as simple as signing a document. "
                            "For most countries, the process of accession takes years of preparation, "
                            "negotiation, and domestic reform. "
                            "Vietnam's accession to the WTO, for example, began in 1995 and was not completed until 2007 — "
                            "a journey of twelve years.\n\n"
                            "During accession, the applying country must demonstrate that its trade policies "
                            "meet the organization's standards. "
                            "This often means changing domestic laws, reducing tariffs, "
                            "and opening markets that were previously protected. "
                            "Existing members negotiate with the applicant to ensure that the terms of entry are fair. "
                            "Each member can raise concerns and request specific commitments.\n\n"
                            "Once the terms are agreed upon, they are recorded in an accession protocol. "
                            "A protocol is a formal document that supplements or amends an existing treaty. "
                            "In the WTO context, the accession protocol lists all the commitments "
                            "the new member has made — which tariffs it will lower, "
                            "which markets it will open, and on what timeline. "
                            "The protocol becomes a binding part of the WTO's legal framework.\n\n"
                            "The concept of a framework is central to how trade organizations operate. "
                            "A framework is a set of basic principles and rules that guide decision-making. "
                            "The WTO framework includes agreements on goods, services, and intellectual property. "
                            "Regional organizations like ASEAN have their own frameworks "
                            "that cover economic cooperation, investment, and labor mobility.\n\n"
                            "Decision-making within trade organizations often relies on consensus. "
                            "Consensus means that all members must agree — or at least not actively object — "
                            "before a decision is adopted. "
                            "This gives every country, no matter how small, a voice. "
                            "But it also means that a single country can block progress. "
                            "The WTO's Doha Round stalled partly because consensus could not be reached "
                            "on agricultural subsidies between developed and developing nations.\n\n"
                            "One of the most sensitive issues in trade organizations is sovereignty. "
                            "Sovereignty is a country's right to govern itself and make its own laws. "
                            "When a country joins a trade organization, it agrees to follow certain rules "
                            "that may limit its freedom to set tariffs, subsidize industries, or regulate imports. "
                            "Critics argue that this erodes national sovereignty. "
                            "Supporters counter that the benefits of open trade — "
                            "more jobs, lower prices, faster growth — outweigh the loss of policy flexibility.\n\n"
                            "Finally, trade organizations work toward harmonization — "
                            "making rules and standards consistent across countries. "
                            "Harmonization of product safety standards, for instance, "
                            "means that a Vietnamese manufacturer only needs to meet one set of requirements "
                            "to sell in multiple markets. "
                            "Without harmonization, exporters face a patchwork of different regulations, "
                            "which raises costs and slows trade. "
                            "The push for harmonization is one of the most practical benefits "
                            "that trade organizations deliver to businesses and consumers alike."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Gia nhập và hài hòa hóa thương mại",
                    "description": "Viết câu sử dụng 6 từ vựng về gia nhập và hài hòa hóa.",
                    "data": {
                        "vocabList": ["accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"],
                        "items": [
                            {
                                "targetVocab": "accession",
                                "prompt": "Dùng từ 'accession' để viết một câu về quá trình gia nhập một tổ chức thương mại quốc tế. Ví dụ: China's accession to the WTO in 2001 required the country to lower tariffs on thousands of products and open its banking sector to foreign competition."
                            },
                            {
                                "targetVocab": "protocol",
                                "prompt": "Dùng từ 'protocol' để viết một câu về một nghị định thư bổ sung cho hiệp ước thương mại. Ví dụ: The new protocol on electronic commerce was added to the trade agreement to establish rules for cross-border data flows and digital payments."
                            },
                            {
                                "targetVocab": "framework",
                                "prompt": "Dùng từ 'framework' để viết một câu về khuôn khổ hợp tác kinh tế giữa các quốc gia. Ví dụ: The APEC framework encourages voluntary cooperation on trade liberalization rather than imposing binding obligations on its member economies."
                            },
                            {
                                "targetVocab": "consensus",
                                "prompt": "Dùng từ 'consensus' để viết một câu về cách các tổ chức thương mại đưa ra quyết định. Ví dụ: Reaching consensus among all WTO members proved impossible on the issue of agricultural subsidies, causing the Doha Round to stall for over a decade."
                            },
                            {
                                "targetVocab": "sovereignty",
                                "prompt": "Dùng từ 'sovereignty' để viết một câu về mối quan hệ giữa chủ quyền quốc gia và hội nhập thương mại. Ví dụ: Critics of the trade deal argued that it would undermine national sovereignty by allowing foreign corporations to challenge domestic environmental regulations."
                            },
                            {
                                "targetVocab": "harmonization",
                                "prompt": "Dùng từ 'harmonization' để viết một câu về việc thống nhất tiêu chuẩn giữa các quốc gia. Ví dụ: The harmonization of pharmaceutical standards across the region means that a medicine approved in one country can be sold in all member states without additional testing."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Tổ chức thương mại quốc tế. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "organization — tổ chức, treaty — hiệp ước, agreement — thỏa thuận, "
                            "negotiation — đàm phán, ratification — phê chuẩn, và membership — tư cách thành viên. "
                            "Đây là bộ từ vựng về cách các quốc gia xây dựng hệ thống thương mại quốc tế.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào cơ chế giải quyết tranh chấp: "
                            "dispute — tranh chấp, resolution — giải quyết, panel — hội đồng xét xử, "
                            "appellate — phúc thẩm, ruling — phán quyết, và enforcement — thực thi. "
                            "Những từ này giúp bạn hiểu 'tòa án' của thương mại quốc tế hoạt động ra sao.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "accession — gia nhập, protocol — nghị định thư, framework — khuôn khổ, "
                            "consensus — đồng thuận, sovereignty — chủ quyền, và harmonization — hài hòa hóa. "
                            "Đây là những từ về quá trình hội nhập và thống nhất quy tắc thương mại.\n\n"
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
                    "description": "Học 18 từ: organization, treaty, agreement, negotiation, ratification, membership, dispute, resolution, panel, appellate, ruling, enforcement, accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: organization, treaty, agreement, negotiation, ratification, membership, dispute, resolution, panel, appellate, ruling, enforcement, accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: organization, treaty, agreement, negotiation, ratification, membership, dispute, resolution, panel, appellate, ruling, enforcement, accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: organization, treaty, agreement, negotiation, ratification, membership, dispute, resolution, panel, appellate, ruling, enforcement, accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: organization, treaty, agreement, negotiation, ratification, membership, dispute, resolution, panel, appellate, ruling, enforcement, accession, protocol, framework, consensus, sovereignty, harmonization",
                    "data": {"vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"]}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng tổ chức thương mại",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"],
                        "items": [
                            {
                                "targetVocab": "organization",
                                "prompt": "Dùng từ 'organization' để viết một câu về vai trò của tổ chức thương mại trong việc thúc đẩy hợp tác kinh tế khu vực. Ví dụ: ASEAN is a regional organization that promotes economic cooperation and trade integration among ten Southeast Asian countries."
                            },
                            {
                                "targetVocab": "treaty",
                                "prompt": "Dùng từ 'treaty' để viết một câu về tác động của một hiệp ước thương mại đối với ngành xuất khẩu của Việt Nam. Ví dụ: The free trade treaty with South Korea helped Vietnamese garment exporters reduce tariffs and increase their market share in one of Asia's largest economies."
                            },
                            {
                                "targetVocab": "agreement",
                                "prompt": "Dùng từ 'agreement' để viết một câu về phạm vi của một thỏa thuận thương mại đa phương. Ví dụ: The RCEP agreement created the world's largest free trade zone, covering nearly thirty percent of global GDP and a third of the world's population."
                            },
                            {
                                "targetVocab": "negotiation",
                                "prompt": "Dùng từ 'negotiation' để viết một câu về thách thức trong đàm phán thương mại giữa các nước phát triển và đang phát triển. Ví dụ: The negotiation between developed and developing countries often stalls because each side has fundamentally different priorities regarding agricultural subsidies."
                            },
                            {
                                "targetVocab": "ratification",
                                "prompt": "Dùng từ 'ratification' để viết một câu về quá trình phê chuẩn hiệp định trong quốc hội. Ví dụ: The ratification of the EVFTA by Vietnam's National Assembly in June 2020 marked a historic milestone in the country's trade relations with Europe."
                            },
                            {
                                "targetVocab": "membership",
                                "prompt": "Dùng từ 'membership' để viết một câu về lợi ích kinh tế khi gia nhập tổ chức thương mại. Ví dụ: Since gaining WTO membership, Vietnam's total trade volume has increased more than tenfold, transforming the country into one of the most open economies in Southeast Asia."
                            },
                            {
                                "targetVocab": "dispute",
                                "prompt": "Dùng từ 'dispute' để viết một câu về một tranh chấp thương mại cụ thể và cách nó được xử lý. Ví dụ: The dispute over shrimp anti-dumping duties was one of the first cases Vietnam brought to the WTO after becoming a member."
                            },
                            {
                                "targetVocab": "resolution",
                                "prompt": "Dùng từ 'resolution' để viết một câu về tầm quan trọng của cơ chế giải quyết tranh chấp. Ví dụ: The peaceful resolution of trade conflicts through the WTO system has prevented many disagreements from escalating into full-scale trade wars."
                            },
                            {
                                "targetVocab": "panel",
                                "prompt": "Dùng từ 'panel' để viết một câu về quy trình xét xử của hội đồng chuyên gia. Ví dụ: The panel spent nine months reviewing thousands of pages of evidence before issuing its report on whether the subsidies violated WTO rules."
                            },
                            {
                                "targetVocab": "appellate",
                                "prompt": "Dùng từ 'appellate' để viết một câu về vai trò của cơ quan phúc thẩm trong hệ thống thương mại. Ví dụ: The appellate body overturned part of the original ruling, finding that the panel had applied the wrong legal standard to the subsidy calculation."
                            },
                            {
                                "targetVocab": "ruling",
                                "prompt": "Dùng từ 'ruling' để viết một câu về tác động của một phán quyết thương mại đối với chính sách quốc gia. Ví dụ: After the WTO ruling against its cotton subsidies, the country was given twelve months to reform its agricultural support programs."
                            },
                            {
                                "targetVocab": "enforcement",
                                "prompt": "Dùng từ 'enforcement' để viết một câu về khó khăn trong việc thực thi quy tắc thương mại quốc tế. Ví dụ: The lack of effective enforcement mechanisms means that some countries continue to violate trade rules even after losing a WTO case."
                            },
                            {
                                "targetVocab": "accession",
                                "prompt": "Dùng từ 'accession' để viết một câu về những cải cách mà một quốc gia phải thực hiện khi gia nhập tổ chức thương mại. Ví dụ: As part of its accession process, the country had to rewrite over fifty domestic laws to bring them in line with international trade standards."
                            },
                            {
                                "targetVocab": "protocol",
                                "prompt": "Dùng từ 'protocol' để viết một câu về một nghị định thư bổ sung cho hiệp ước hiện có. Ví dụ: The environmental protocol added to the trade agreement requires all member countries to meet minimum carbon emission standards for exported goods."
                            },
                            {
                                "targetVocab": "framework",
                                "prompt": "Dùng từ 'framework' để viết một câu về khuôn khổ hợp tác kinh tế trong khu vực. Ví dụ: The ASEAN Economic Community framework aims to create a single market where goods, services, and skilled workers can move freely across borders."
                            },
                            {
                                "targetVocab": "consensus",
                                "prompt": "Dùng từ 'consensus' để viết một câu về thách thức khi đạt đồng thuận trong tổ chức đa phương. Ví dụ: Building consensus among one hundred and sixty-four WTO members is extremely difficult, which is why major trade rounds often take decades to complete."
                            },
                            {
                                "targetVocab": "sovereignty",
                                "prompt": "Dùng từ 'sovereignty' để viết một câu về cuộc tranh luận giữa hội nhập thương mại và chủ quyền quốc gia. Ví dụ: The debate over sovereignty intensified when the trade agreement gave foreign investors the right to sue the government over policy changes that affected their profits."
                            },
                            {
                                "targetVocab": "harmonization",
                                "prompt": "Dùng từ 'harmonization' để viết một câu về lợi ích của việc thống nhất tiêu chuẩn thương mại. Ví dụ: The harmonization of customs procedures across the region has cut the average time for goods to clear the border from five days to just one."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về tổ chức thương mại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về các tổ chức thương mại quốc tế — từ cách chúng được thành lập, "
                            "cách chúng giải quyết tranh chấp, đến cách các quốc gia gia nhập và hài hòa hóa quy tắc.\n\n"
                            "Bạn sẽ gặp lại organization, treaty, agreement, negotiation, ratification, membership "
                            "trong phần mở đầu về nền tảng của hệ thống thương mại quốc tế. "
                            "Tiếp theo, dispute, resolution, panel, appellate, ruling, enforcement "
                            "sẽ giúp bạn hiểu cơ chế xử lý xung đột thương mại. "
                            "Và cuối cùng, accession, protocol, framework, consensus, sovereignty, harmonization "
                            "sẽ đưa bạn vào thế giới hội nhập và hợp tác thương mại.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tổ chức thương mại quốc tế — Bức tranh toàn cảnh",
                    "description": "For most of human history, trade between nations was governed by power, not rules.",
                    "data": {
                        "text": (
                            "For most of human history, trade between nations was governed by power, not rules. "
                            "Stronger countries could impose their will on weaker ones, "
                            "and there was no system to ensure fairness. "
                            "That began to change after World War II, when countries realized that economic cooperation "
                            "was essential for lasting peace. "
                            "The result was a new framework for international trade — "
                            "a set of principles and institutions designed to make commerce more predictable, "
                            "more open, and more fair.\n\n"
                            "At the center of this framework stands the World Trade Organization. "
                            "The WTO is an organization of over one hundred and sixty member countries "
                            "that sets the rules for global trade. "
                            "Its founding treaty, the Marrakesh Agreement of 1994, "
                            "established the organization and laid out its core functions: "
                            "to provide a forum for negotiation, to administer trade agreements, "
                            "and to settle disputes between members.\n\n"
                            "The process of creating a trade agreement begins with negotiation. "
                            "Countries send teams of diplomats and trade experts to discuss what each side wants. "
                            "These negotiations can be bilateral — between two countries — "
                            "or multilateral, involving dozens of nations at once. "
                            "The WTO's negotiating rounds are the largest multilateral negotiations in history. "
                            "Each round can take years, because reaching consensus among so many countries "
                            "with different economic interests is extraordinarily difficult.\n\n"
                            "Consensus is the WTO's primary decision-making method. "
                            "Unlike a vote, where the majority wins, consensus requires that no member actively objects. "
                            "This protects the sovereignty of every country — "
                            "no nation can be forced to accept a rule it opposes. "
                            "But it also means that progress is slow. "
                            "A single country can block an agreement that the rest of the membership supports.\n\n"
                            "Once a treaty or agreement is negotiated, it must be signed and then ratified. "
                            "Ratification is the formal process by which a country's government or parliament "
                            "approves the treaty and makes it legally binding. "
                            "Without ratification, a signed treaty is just a piece of paper. "
                            "Some agreements require ratification by a minimum number of countries before they take effect. "
                            "The CPTPP, for example, needed ratification by at least six of its eleven signatories.\n\n"
                            "For countries that want to join an existing organization, "
                            "the path is through accession. "
                            "Accession is a lengthy process in which the applying country must prove "
                            "that its trade policies meet the organization's standards. "
                            "Vietnam's accession to the WTO took twelve years of preparation and reform. "
                            "The terms of entry are recorded in an accession protocol — "
                            "a formal document that lists all the commitments the new member has made.\n\n"
                            "Membership in a trade organization brings significant benefits. "
                            "Members enjoy lower tariffs, access to dispute resolution, "
                            "and a voice in shaping the rules of global commerce. "
                            "But membership also comes with obligations. "
                            "Countries must open their markets, follow the organization's rules, "
                            "and accept the rulings of its dispute settlement system.\n\n"
                            "When a dispute arises — say, one country accuses another of unfair subsidies — "
                            "the WTO's dispute settlement system provides a structured path to resolution. "
                            "First, the countries try to resolve the issue through consultation. "
                            "If that fails, a panel of experts is appointed to examine the case. "
                            "The panel issues a ruling, which can be appealed to the appellate body. "
                            "The appellate body's decision is final.\n\n"
                            "The biggest challenge is enforcement. "
                            "The WTO cannot force a country to comply with a ruling. "
                            "If the losing country refuses to change its policies, "
                            "the winning country can impose retaliatory measures — "
                            "but this is a blunt tool that can hurt both sides.\n\n"
                            "Beyond settling disputes, trade organizations work toward harmonization — "
                            "aligning rules and standards across countries so that trade flows more smoothly. "
                            "When product safety standards, customs procedures, and labeling requirements are harmonized, "
                            "exporters face fewer barriers and consumers benefit from lower prices. "
                            "Protocols are often added to existing agreements to address new issues "
                            "like digital trade, environmental standards, or labor rights.\n\n"
                            "The story of trade organizations is a story of countries choosing cooperation over conflict. "
                            "It is not a perfect system — sovereignty concerns, enforcement gaps, "
                            "and the difficulty of reaching consensus all create friction. "
                            "But for a country like Vietnam, whose economy depends heavily on international trade, "
                            "understanding these organizations and their vocabulary "
                            "is not just an academic exercise — it is a practical necessity."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tổ chức thương mại quốc tế — Bức tranh toàn cảnh",
                    "description": "For most of human history, trade between nations was governed by power, not rules.",
                    "data": {
                        "text": (
                            "For most of human history, trade between nations was governed by power, not rules. "
                            "Stronger countries could impose their will on weaker ones, "
                            "and there was no system to ensure fairness. "
                            "That began to change after World War II, when countries realized that economic cooperation "
                            "was essential for lasting peace. "
                            "The result was a new framework for international trade — "
                            "a set of principles and institutions designed to make commerce more predictable, "
                            "more open, and more fair.\n\n"
                            "At the center of this framework stands the World Trade Organization. "
                            "The WTO is an organization of over one hundred and sixty member countries "
                            "that sets the rules for global trade. "
                            "Its founding treaty, the Marrakesh Agreement of 1994, "
                            "established the organization and laid out its core functions: "
                            "to provide a forum for negotiation, to administer trade agreements, "
                            "and to settle disputes between members.\n\n"
                            "The process of creating a trade agreement begins with negotiation. "
                            "Countries send teams of diplomats and trade experts to discuss what each side wants. "
                            "These negotiations can be bilateral — between two countries — "
                            "or multilateral, involving dozens of nations at once. "
                            "The WTO's negotiating rounds are the largest multilateral negotiations in history. "
                            "Each round can take years, because reaching consensus among so many countries "
                            "with different economic interests is extraordinarily difficult.\n\n"
                            "Consensus is the WTO's primary decision-making method. "
                            "Unlike a vote, where the majority wins, consensus requires that no member actively objects. "
                            "This protects the sovereignty of every country — "
                            "no nation can be forced to accept a rule it opposes. "
                            "But it also means that progress is slow. "
                            "A single country can block an agreement that the rest of the membership supports.\n\n"
                            "Once a treaty or agreement is negotiated, it must be signed and then ratified. "
                            "Ratification is the formal process by which a country's government or parliament "
                            "approves the treaty and makes it legally binding. "
                            "Without ratification, a signed treaty is just a piece of paper. "
                            "Some agreements require ratification by a minimum number of countries before they take effect. "
                            "The CPTPP, for example, needed ratification by at least six of its eleven signatories.\n\n"
                            "For countries that want to join an existing organization, "
                            "the path is through accession. "
                            "Accession is a lengthy process in which the applying country must prove "
                            "that its trade policies meet the organization's standards. "
                            "Vietnam's accession to the WTO took twelve years of preparation and reform. "
                            "The terms of entry are recorded in an accession protocol — "
                            "a formal document that lists all the commitments the new member has made.\n\n"
                            "Membership in a trade organization brings significant benefits. "
                            "Members enjoy lower tariffs, access to dispute resolution, "
                            "and a voice in shaping the rules of global commerce. "
                            "But membership also comes with obligations. "
                            "Countries must open their markets, follow the organization's rules, "
                            "and accept the rulings of its dispute settlement system.\n\n"
                            "When a dispute arises — say, one country accuses another of unfair subsidies — "
                            "the WTO's dispute settlement system provides a structured path to resolution. "
                            "First, the countries try to resolve the issue through consultation. "
                            "If that fails, a panel of experts is appointed to examine the case. "
                            "The panel issues a ruling, which can be appealed to the appellate body. "
                            "The appellate body's decision is final.\n\n"
                            "The biggest challenge is enforcement. "
                            "The WTO cannot force a country to comply with a ruling. "
                            "If the losing country refuses to change its policies, "
                            "the winning country can impose retaliatory measures — "
                            "but this is a blunt tool that can hurt both sides.\n\n"
                            "Beyond settling disputes, trade organizations work toward harmonization — "
                            "aligning rules and standards across countries so that trade flows more smoothly. "
                            "When product safety standards, customs procedures, and labeling requirements are harmonized, "
                            "exporters face fewer barriers and consumers benefit from lower prices. "
                            "Protocols are often added to existing agreements to address new issues "
                            "like digital trade, environmental standards, or labor rights.\n\n"
                            "The story of trade organizations is a story of countries choosing cooperation over conflict. "
                            "It is not a perfect system — sovereignty concerns, enforcement gaps, "
                            "and the difficulty of reaching consensus all create friction. "
                            "But for a country like Vietnam, whose economy depends heavily on international trade, "
                            "understanding these organizations and their vocabulary "
                            "is not just an academic exercise — it is a practical necessity."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tổ chức thương mại quốc tế — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "For most of human history, trade between nations was governed by power, not rules. "
                            "Stronger countries could impose their will on weaker ones, "
                            "and there was no system to ensure fairness. "
                            "That began to change after World War II, when countries realized that economic cooperation "
                            "was essential for lasting peace. "
                            "The result was a new framework for international trade — "
                            "a set of principles and institutions designed to make commerce more predictable, "
                            "more open, and more fair.\n\n"
                            "At the center of this framework stands the World Trade Organization. "
                            "The WTO is an organization of over one hundred and sixty member countries "
                            "that sets the rules for global trade. "
                            "Its founding treaty, the Marrakesh Agreement of 1994, "
                            "established the organization and laid out its core functions: "
                            "to provide a forum for negotiation, to administer trade agreements, "
                            "and to settle disputes between members.\n\n"
                            "The process of creating a trade agreement begins with negotiation. "
                            "Countries send teams of diplomats and trade experts to discuss what each side wants. "
                            "These negotiations can be bilateral — between two countries — "
                            "or multilateral, involving dozens of nations at once. "
                            "The WTO's negotiating rounds are the largest multilateral negotiations in history. "
                            "Each round can take years, because reaching consensus among so many countries "
                            "with different economic interests is extraordinarily difficult.\n\n"
                            "Consensus is the WTO's primary decision-making method. "
                            "Unlike a vote, where the majority wins, consensus requires that no member actively objects. "
                            "This protects the sovereignty of every country — "
                            "no nation can be forced to accept a rule it opposes. "
                            "But it also means that progress is slow. "
                            "A single country can block an agreement that the rest of the membership supports.\n\n"
                            "Once a treaty or agreement is negotiated, it must be signed and then ratified. "
                            "Ratification is the formal process by which a country's government or parliament "
                            "approves the treaty and makes it legally binding. "
                            "Without ratification, a signed treaty is just a piece of paper. "
                            "Some agreements require ratification by a minimum number of countries before they take effect. "
                            "The CPTPP, for example, needed ratification by at least six of its eleven signatories.\n\n"
                            "For countries that want to join an existing organization, "
                            "the path is through accession. "
                            "Accession is a lengthy process in which the applying country must prove "
                            "that its trade policies meet the organization's standards. "
                            "Vietnam's accession to the WTO took twelve years of preparation and reform. "
                            "The terms of entry are recorded in an accession protocol — "
                            "a formal document that lists all the commitments the new member has made.\n\n"
                            "Membership in a trade organization brings significant benefits. "
                            "Members enjoy lower tariffs, access to dispute resolution, "
                            "and a voice in shaping the rules of global commerce. "
                            "But membership also comes with obligations. "
                            "Countries must open their markets, follow the organization's rules, "
                            "and accept the rulings of its dispute settlement system.\n\n"
                            "When a dispute arises — say, one country accuses another of unfair subsidies — "
                            "the WTO's dispute settlement system provides a structured path to resolution. "
                            "First, the countries try to resolve the issue through consultation. "
                            "If that fails, a panel of experts is appointed to examine the case. "
                            "The panel issues a ruling, which can be appealed to the appellate body. "
                            "The appellate body's decision is final.\n\n"
                            "The biggest challenge is enforcement. "
                            "The WTO cannot force a country to comply with a ruling. "
                            "If the losing country refuses to change its policies, "
                            "the winning country can impose retaliatory measures — "
                            "but this is a blunt tool that can hurt both sides.\n\n"
                            "Beyond settling disputes, trade organizations work toward harmonization — "
                            "aligning rules and standards across countries so that trade flows more smoothly. "
                            "When product safety standards, customs procedures, and labeling requirements are harmonized, "
                            "exporters face fewer barriers and consumers benefit from lower prices. "
                            "Protocols are often added to existing agreements to address new issues "
                            "like digital trade, environmental standards, or labor rights.\n\n"
                            "The story of trade organizations is a story of countries choosing cooperation over conflict. "
                            "It is not a perfect system — sovereignty concerns, enforcement gaps, "
                            "and the difficulty of reaching consensus all create friction. "
                            "But for a country like Vietnam, whose economy depends heavily on international trade, "
                            "understanding these organizations and their vocabulary "
                            "is not just an academic exercise — it is a practical necessity."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích tổ chức thương mại quốc tế",
                    "description": "Viết đoạn văn tiếng Anh phân tích về tổ chức thương mại sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["organization", "treaty", "agreement", "negotiation", "ratification", "membership", "dispute", "resolution", "panel", "appellate", "ruling", "enforcement", "accession", "protocol", "framework", "consensus", "sovereignty", "harmonization"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của tổ chức thương mại quốc tế. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích quá trình gia nhập (accession) WTO của một quốc gia đang phát triển. Giải thích tại sao negotiation kéo dài, vai trò của ratification, và cách membership thay đổi nền kinh tế — đồng thời thảo luận về mối lo ngại sovereignty mà quốc gia đó phải đối mặt.",
                            "Hãy phân tích cơ chế giải quyết tranh chấp (dispute settlement) của WTO. Giải thích vai trò của panel và appellate body, thách thức trong enforcement, và tại sao hệ thống này quan trọng đối với framework thương mại quốc tế — đặc biệt đối với các quốc gia nhỏ."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần hành động.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học về Tổ chức thương mại quốc tế. "
                            "Đây không chỉ là 18 từ vựng — đây là bộ công cụ để bạn bước vào "
                            "thế giới thương mại quốc tế bằng tiếng Anh. "
                            "Hãy cùng ôn lại những từ quan trọng nhất và bàn về bước tiếp theo.\n\n"
                            "Treaty — hiệp ước. Mỗi khi bạn đọc tin về Việt Nam ký hiệp định thương mại mới, "
                            "bạn đang đọc về treaty. Đây là nền tảng pháp lý của mọi quan hệ thương mại. "
                            "Ví dụ mới: The bilateral treaty between the two countries eliminated tariffs on seafood, "
                            "giving Vietnamese shrimp farmers direct access to a market of fifty million consumers.\n\n"
                            "Dispute — tranh chấp. Thương mại không phải lúc nào cũng suôn sẻ. "
                            "Khi hai nước không đồng ý, dispute là từ bạn sẽ thấy trên mọi trang báo kinh tế. "
                            "Ví dụ mới: The trade dispute over rice export quotas lasted two years "
                            "before both sides agreed to a compromise through WTO mediation.\n\n"
                            "Panel — hội đồng xét xử. Đây là nhóm chuyên gia quyết định ai đúng ai sai "
                            "trong tranh chấp thương mại. Hiểu từ này, bạn hiểu cả hệ thống. "
                            "Ví dụ mới: The three-member panel reviewed evidence from both governments "
                            "and concluded that the import ban violated the principle of non-discrimination.\n\n"
                            "Accession — gia nhập. Việt Nam mất 12 năm để gia nhập WTO. "
                            "Từ này nhắc bạn rằng hội nhập không phải chuyện một sớm một chiều. "
                            "Ví dụ mới: The country's accession to the regional trade bloc required it to lower tariffs "
                            "on over three thousand product categories within five years.\n\n"
                            "Sovereignty — chủ quyền. Đây là từ nóng nhất trong mọi cuộc tranh luận "
                            "về hội nhập thương mại. Mỗi khi một quốc gia ký hiệp định, "
                            "câu hỏi luôn là: chúng ta đang nhượng bao nhiêu sovereignty? "
                            "Ví dụ mới: The opposition party argued that the investment chapter of the treaty "
                            "would compromise national sovereignty by allowing foreign companies to bypass domestic courts.\n\n"
                            "Harmonization — hài hòa hóa. Đây là mục tiêu thực tế nhất "
                            "mà các tổ chức thương mại mang lại. Khi tiêu chuẩn được thống nhất, "
                            "doanh nghiệp Việt Nam xuất khẩu dễ hơn, nhanh hơn, rẻ hơn. "
                            "Ví dụ mới: Thanks to the harmonization of organic certification standards, "
                            "Vietnamese coffee producers can now sell to European supermarkets "
                            "without going through a separate approval process in each country.\n\n"
                            "Bây giờ, đây là bước tiếp theo cụ thể cho bạn. "
                            "Tuần này, hãy mở một bài báo tiếng Anh về WTO hoặc CPTPP — "
                            "trên Reuters, Bloomberg, hoặc trang chủ của WTO. "
                            "Đọc hai đoạn đầu tiên và đánh dấu mỗi từ vựng bạn vừa học. "
                            "Bạn sẽ ngạc nhiên khi thấy mình nhận ra bao nhiêu từ.\n\n"
                            "Nếu bạn muốn đi xa hơn, hãy thử viết một đoạn tóm tắt ngắn bằng tiếng Anh "
                            "về bài báo đó — dùng ít nhất 5 từ vựng từ bài học. "
                            "Đó là cách nhanh nhất để biến kiến thức thụ động thành kỹ năng chủ động.\n\n"
                            "Bạn đã có công cụ. Bây giờ hãy dùng nó. "
                            "Chúc bạn tiếp tục hành trình học tập thật hiệu quả — "
                            "hẹn gặp lại ở bài học tiếp theo!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Trade Organizations – Tổ Chức Thương Mại' AND uid = '{UID}' ORDER BY created_at;")
