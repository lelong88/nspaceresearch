"""
Create curriculum: Branding Strategy – Chiến Lược Thương Hiệu
Series E — Marketing & Quản Trị (Marketing & Management), curriculum #2, displayOrder 1
18 words | 5 sessions | bold_declaration tone | team-building energy farewell
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
W1 = ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"]
W2 = ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"]
W3 = ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Branding Strategy – Chiến Lược Thương Hiệu",
    "contentTypeTags": [],
    "description": (
        "THƯƠNG HIỆU KHÔNG PHẢI LÀ LOGO — MÀ LÀ LỜI HỨA MÀ KHÁCH HÀNG TIN VÀO MỖI LẦN HỌ CHỌN BẠN.\n\n"
        "Bạn đang ngồi trong lớp marketing, giảng viên hỏi: 'Vì sao người ta sẵn sàng trả gấp ba lần "
        "cho một ly cà phê Starbucks khi quán cà phê bên đường cũng ngon không kém?' "
        "Bạn biết câu trả lời bằng tiếng Việt — nhưng khi đề thi yêu cầu phân tích "
        "brand positioning, differentiation, và brand equity bằng tiếng Anh, bạn bắt đầu lúng túng. "
        "Những khái niệm này không khó hiểu, nhưng chúng là ngôn ngữ chung "
        "của mọi chiến lược thương hiệu trên thế giới.\n\n"
        "Hãy nghĩ về 18 từ vựng này như bản đồ chiến lược — "
        "một khi bạn đọc được bản đồ, bạn sẽ thấy rõ cách các thương hiệu lớn "
        "xây dựng nhận diện, chiếm lĩnh tâm trí khách hàng, và tạo ra lòng trung thành. "
        "Từ brand awareness đến brand narrative, từ premium pricing đến niche marketing — "
        "bạn sẽ nắm được 'ngôn ngữ' mà mọi giám đốc marketing trên thế giới dùng để ra quyết định.\n\n"
        "Sau khóa học, bạn sẽ tự tin phân tích chiến lược thương hiệu bằng tiếng Anh, "
        "thuyết trình về brand positioning trong bài tập nhóm, "
        "và viết báo cáo đánh giá thương hiệu bằng thuật ngữ chuyên ngành quốc tế.\n\n"
        "18 từ vựng — từ brand đến narrative — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy chiến lược thương hiệu, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về chiến lược thương hiệu — "
            "ngôn ngữ chung của mọi giám đốc marketing trên thế giới. "
            "Bạn sẽ học brand, positioning, differentiation, perception, loyalty, awareness trong phần đầu tiên, "
            "nơi bài đọc giải thích cách thương hiệu chiếm lĩnh tâm trí khách hàng. "
            "Tiếp theo là identity, equity, portfolio, extension, endorsement, licensing — "
            "những từ giúp bạn hiểu cách doanh nghiệp xây dựng và mở rộng giá trị thương hiệu. "
            "Cuối cùng, rebranding, premium, niche, archetype, touchpoint, narrative "
            "đưa bạn vào thế giới tái định vị thương hiệu và kể chuyện thương hiệu. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin phân tích chiến lược thương hiệu bằng tiếng Anh — "
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
                    "description": "Chào mừng bạn đến với bài học về chiến lược thương hiệu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ hai trong chuỗi từ vựng Marketing và Quản trị — "
                            "chủ đề hôm nay là Chiến lược thương hiệu, hay trong tiếng Anh là Branding Strategy. "
                            "Mỗi sản phẩm bạn mua, mỗi dịch vụ bạn chọn — đằng sau đó đều có một thương hiệu "
                            "với chiến lược rõ ràng để chiếm lĩnh tâm trí bạn. "
                            "Từ Vinamilk đến Apple, từ Grab đến Nike — "
                            "tất cả đều dùng cùng một bộ công cụ chiến lược thương hiệu.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: brand, positioning, differentiation, perception, loyalty, và awareness. "
                            "Đây là những từ nền tảng nhất — bạn sẽ gặp chúng trong mọi bài giảng về marketing.\n\n"
                            "Từ đầu tiên là brand — danh từ — nghĩa là thương hiệu, "
                            "tổng hợp tất cả những gì khách hàng nghĩ, cảm nhận và liên tưởng khi nghe tên một sản phẩm hoặc công ty. "
                            "Ví dụ: 'A strong brand is more than a logo — it is the promise a company makes to its customers about quality, experience, and values.' "
                            "Trong bài đọc, brand là khái niệm trung tâm — "
                            "mọi chiến lược marketing đều xoay quanh việc xây dựng và bảo vệ thương hiệu.\n\n"
                            "Từ thứ hai là positioning — danh từ — nghĩa là định vị, "
                            "cách một thương hiệu tạo ra vị trí riêng biệt trong tâm trí khách hàng so với đối thủ. "
                            "Ví dụ: 'The company's positioning strategy focused on being the most affordable option for young Vietnamese professionals who want quality without the premium price.' "
                            "Trong bài đọc, positioning quyết định cách khách hàng phân biệt bạn với hàng trăm lựa chọn khác trên thị trường.\n\n"
                            "Từ thứ ba là differentiation — danh từ — nghĩa là sự khác biệt hóa, "
                            "quá trình tạo ra những đặc điểm độc đáo khiến sản phẩm nổi bật so với đối thủ cạnh tranh. "
                            "Ví dụ: 'Product differentiation through superior design and customer service helped the Vietnamese electronics brand compete against established international players.' "
                            "Trong bài đọc, differentiation là vũ khí chiến lược — "
                            "không có sự khác biệt, thương hiệu chỉ là một cái tên trong đám đông.\n\n"
                            "Từ thứ tư là perception — danh từ — nghĩa là nhận thức, "
                            "cách khách hàng nhìn nhận và đánh giá một thương hiệu dựa trên trải nghiệm và thông tin họ tiếp nhận. "
                            "Ví dụ: 'Consumer perception of the brand shifted dramatically after the company launched a sustainability campaign showing its commitment to reducing plastic waste.' "
                            "Trong bài đọc, perception là thực tế trong marketing — "
                            "không quan trọng sản phẩm thực sự tốt đến đâu, mà quan trọng khách hàng nghĩ nó tốt đến đâu.\n\n"
                            "Từ thứ năm là loyalty — danh từ — nghĩa là lòng trung thành, "
                            "sự gắn bó lâu dài của khách hàng với một thương hiệu, khiến họ quay lại mua hàng nhiều lần. "
                            "Ví dụ: 'Brand loyalty among Vietnamese coffee drinkers is remarkably strong — many customers refuse to switch even when competitors offer lower prices.' "
                            "Trong bài đọc, loyalty là mục tiêu cuối cùng của mọi chiến lược thương hiệu — "
                            "khách hàng trung thành không chỉ mua hàng mà còn giới thiệu cho người khác.\n\n"
                            "Từ cuối cùng là awareness — danh từ — nghĩa là nhận biết thương hiệu, "
                            "mức độ mà khách hàng tiềm năng biết đến sự tồn tại của một thương hiệu. "
                            "Ví dụ: 'The startup invested heavily in social media advertising to build brand awareness among university students in Ho Chi Minh City and Hanoi.' "
                            "Trong bài đọc, awareness là bước đầu tiên trong hành trình khách hàng — "
                            "nếu người ta không biết bạn tồn tại, họ không thể mua hàng của bạn.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách thương hiệu chiếm lĩnh tâm trí khách hàng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thương hiệu, định vị và lòng trung thành",
                    "description": "Học 6 từ: brand, positioning, differentiation, perception, loyalty, awareness",
                    "data": {"vocabList": ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thương hiệu, định vị và lòng trung thành",
                    "description": "Học 6 từ: brand, positioning, differentiation, perception, loyalty, awareness",
                    "data": {"vocabList": ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thương hiệu, định vị và lòng trung thành",
                    "description": "Học 6 từ: brand, positioning, differentiation, perception, loyalty, awareness",
                    "data": {"vocabList": ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thương hiệu, định vị và lòng trung thành",
                    "description": "Học 6 từ: brand, positioning, differentiation, perception, loyalty, awareness",
                    "data": {"vocabList": ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Thương hiệu, định vị và lòng trung thành",
                    "description": "Học 6 từ: brand, positioning, differentiation, perception, loyalty, awareness",
                    "data": {"vocabList": ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thương hiệu và tâm trí khách hàng",
                    "description": "Every product on a supermarket shelf is fighting for the same thing — a place in the customer's mind.",
                    "data": {
                        "text": (
                            "Every product on a supermarket shelf is fighting for the same thing — "
                            "a place in the customer's mind. "
                            "This battle is not won by having the best ingredients or the lowest price. "
                            "It is won by building a strong brand.\n\n"
                            "A brand is far more than a name or a logo. "
                            "It is the total impression that a company creates in the minds of its customers. "
                            "When Vietnamese consumers hear the name Vinamilk, they do not just think of milk — "
                            "they think of trust, nutrition, and a company that has been part of their lives for decades. "
                            "That collection of thoughts and feelings is the brand.\n\n"
                            "But how does a company make sure its brand stands out? "
                            "The answer begins with positioning. "
                            "Positioning is the strategy of placing a brand in a specific spot "
                            "in the customer's mental landscape. "
                            "A luxury watch brand positions itself as a symbol of success and craftsmanship. "
                            "A budget airline positions itself as the smart choice for price-conscious travelers. "
                            "Each brand chooses a position and then builds everything — "
                            "advertising, packaging, pricing — to reinforce that position.\n\n"
                            "Positioning only works when there is clear differentiation. "
                            "Differentiation means offering something that competitors do not. "
                            "It could be a unique feature, a superior experience, or even a distinctive personality. "
                            "A Vietnamese coffee chain might differentiate itself by roasting beans "
                            "from a single highland province and telling the story of the farmers who grow them. "
                            "Without differentiation, a brand has no reason to exist in a crowded market.\n\n"
                            "Once a brand is positioned and differentiated, "
                            "the next challenge is shaping customer perception. "
                            "Perception is reality in marketing. "
                            "A product may be identical to its competitor in quality, "
                            "but if customers perceive one brand as more trustworthy or more innovative, "
                            "that brand wins. Companies invest heavily in advertising, packaging, "
                            "and customer service to shape how people perceive them. "
                            "A single negative experience can shift perception overnight.\n\n"
                            "The ultimate goal of all branding efforts is loyalty. "
                            "Brand loyalty means customers choose the same brand again and again, "
                            "even when alternatives are available. "
                            "Loyal customers are valuable because they cost less to retain than new customers cost to acquire. "
                            "They also become advocates — recommending the brand to friends and family. "
                            "In Vietnam, loyalty programs at supermarkets and coffee chains "
                            "are designed specifically to turn occasional buyers into repeat customers.\n\n"
                            "But loyalty cannot exist without awareness. "
                            "Brand awareness is the foundation of the entire branding process. "
                            "Before customers can form opinions, develop preferences, or become loyal, "
                            "they must first know that the brand exists. "
                            "A new Vietnamese skincare startup might create an excellent product, "
                            "but if nobody has heard of it, sales will remain low. "
                            "That is why companies spend enormous budgets on advertising, "
                            "social media campaigns, and influencer partnerships — "
                            "all to build awareness and start the journey from stranger to loyal customer."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thương hiệu và tâm trí khách hàng",
                    "description": "Every product on a supermarket shelf is fighting for the same thing — a place in the customer's mind.",
                    "data": {
                        "text": (
                            "Every product on a supermarket shelf is fighting for the same thing — "
                            "a place in the customer's mind. "
                            "This battle is not won by having the best ingredients or the lowest price. "
                            "It is won by building a strong brand.\n\n"
                            "A brand is far more than a name or a logo. "
                            "It is the total impression that a company creates in the minds of its customers. "
                            "When Vietnamese consumers hear the name Vinamilk, they do not just think of milk — "
                            "they think of trust, nutrition, and a company that has been part of their lives for decades. "
                            "That collection of thoughts and feelings is the brand.\n\n"
                            "But how does a company make sure its brand stands out? "
                            "The answer begins with positioning. "
                            "Positioning is the strategy of placing a brand in a specific spot "
                            "in the customer's mental landscape. "
                            "A luxury watch brand positions itself as a symbol of success and craftsmanship. "
                            "A budget airline positions itself as the smart choice for price-conscious travelers. "
                            "Each brand chooses a position and then builds everything — "
                            "advertising, packaging, pricing — to reinforce that position.\n\n"
                            "Positioning only works when there is clear differentiation. "
                            "Differentiation means offering something that competitors do not. "
                            "It could be a unique feature, a superior experience, or even a distinctive personality. "
                            "A Vietnamese coffee chain might differentiate itself by roasting beans "
                            "from a single highland province and telling the story of the farmers who grow them. "
                            "Without differentiation, a brand has no reason to exist in a crowded market.\n\n"
                            "Once a brand is positioned and differentiated, "
                            "the next challenge is shaping customer perception. "
                            "Perception is reality in marketing. "
                            "A product may be identical to its competitor in quality, "
                            "but if customers perceive one brand as more trustworthy or more innovative, "
                            "that brand wins. Companies invest heavily in advertising, packaging, "
                            "and customer service to shape how people perceive them. "
                            "A single negative experience can shift perception overnight.\n\n"
                            "The ultimate goal of all branding efforts is loyalty. "
                            "Brand loyalty means customers choose the same brand again and again, "
                            "even when alternatives are available. "
                            "Loyal customers are valuable because they cost less to retain than new customers cost to acquire. "
                            "They also become advocates — recommending the brand to friends and family. "
                            "In Vietnam, loyalty programs at supermarkets and coffee chains "
                            "are designed specifically to turn occasional buyers into repeat customers.\n\n"
                            "But loyalty cannot exist without awareness. "
                            "Brand awareness is the foundation of the entire branding process. "
                            "Before customers can form opinions, develop preferences, or become loyal, "
                            "they must first know that the brand exists. "
                            "A new Vietnamese skincare startup might create an excellent product, "
                            "but if nobody has heard of it, sales will remain low. "
                            "That is why companies spend enormous budgets on advertising, "
                            "social media campaigns, and influencer partnerships — "
                            "all to build awareness and start the journey from stranger to loyal customer."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thương hiệu và tâm trí khách hàng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every product on a supermarket shelf is fighting for the same thing — "
                            "a place in the customer's mind. "
                            "This battle is not won by having the best ingredients or the lowest price. "
                            "It is won by building a strong brand.\n\n"
                            "A brand is far more than a name or a logo. "
                            "It is the total impression that a company creates in the minds of its customers. "
                            "When Vietnamese consumers hear the name Vinamilk, they do not just think of milk — "
                            "they think of trust, nutrition, and a company that has been part of their lives for decades. "
                            "That collection of thoughts and feelings is the brand.\n\n"
                            "But how does a company make sure its brand stands out? "
                            "The answer begins with positioning. "
                            "Positioning is the strategy of placing a brand in a specific spot "
                            "in the customer's mental landscape. "
                            "A luxury watch brand positions itself as a symbol of success and craftsmanship. "
                            "A budget airline positions itself as the smart choice for price-conscious travelers. "
                            "Each brand chooses a position and then builds everything — "
                            "advertising, packaging, pricing — to reinforce that position.\n\n"
                            "Positioning only works when there is clear differentiation. "
                            "Differentiation means offering something that competitors do not. "
                            "It could be a unique feature, a superior experience, or even a distinctive personality. "
                            "A Vietnamese coffee chain might differentiate itself by roasting beans "
                            "from a single highland province and telling the story of the farmers who grow them. "
                            "Without differentiation, a brand has no reason to exist in a crowded market.\n\n"
                            "Once a brand is positioned and differentiated, "
                            "the next challenge is shaping customer perception. "
                            "Perception is reality in marketing. "
                            "A product may be identical to its competitor in quality, "
                            "but if customers perceive one brand as more trustworthy or more innovative, "
                            "that brand wins. Companies invest heavily in advertising, packaging, "
                            "and customer service to shape how people perceive them. "
                            "A single negative experience can shift perception overnight.\n\n"
                            "The ultimate goal of all branding efforts is loyalty. "
                            "Brand loyalty means customers choose the same brand again and again, "
                            "even when alternatives are available. "
                            "Loyal customers are valuable because they cost less to retain than new customers cost to acquire. "
                            "They also become advocates — recommending the brand to friends and family. "
                            "In Vietnam, loyalty programs at supermarkets and coffee chains "
                            "are designed specifically to turn occasional buyers into repeat customers.\n\n"
                            "But loyalty cannot exist without awareness. "
                            "Brand awareness is the foundation of the entire branding process. "
                            "Before customers can form opinions, develop preferences, or become loyal, "
                            "they must first know that the brand exists. "
                            "A new Vietnamese skincare startup might create an excellent product, "
                            "but if nobody has heard of it, sales will remain low. "
                            "That is why companies spend enormous budgets on advertising, "
                            "social media campaigns, and influencer partnerships — "
                            "all to build awareness and start the journey from stranger to loyal customer."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thương hiệu, định vị và lòng trung thành",
                    "description": "Viết câu sử dụng 6 từ vựng về thương hiệu và định vị.",
                    "data": {
                        "vocabList": ["brand", "positioning", "differentiation", "perception", "loyalty", "awareness"],
                        "items": [
                            {
                                "targetVocab": "brand",
                                "prompt": "Dùng từ 'brand' để viết một câu về cách một thương hiệu tạo ấn tượng trong tâm trí khách hàng. Ví dụ: The Vietnamese dairy brand built its reputation over thirty years by consistently delivering safe, high-quality products that families across the country trust."
                            },
                            {
                                "targetVocab": "positioning",
                                "prompt": "Dùng từ 'positioning' để viết một câu về chiến lược định vị của một thương hiệu trên thị trường. Ví dụ: The startup's positioning as an eco-friendly alternative to plastic packaging attracted environmentally conscious consumers willing to pay a higher price."
                            },
                            {
                                "targetVocab": "differentiation",
                                "prompt": "Dùng từ 'differentiation' để viết một câu về cách một sản phẩm tạo sự khác biệt so với đối thủ. Ví dụ: The phone manufacturer achieved differentiation by offering a camera system specifically designed for low-light photography, a feature no competitor could match at the same price point."
                            },
                            {
                                "targetVocab": "perception",
                                "prompt": "Dùng từ 'perception' để viết một câu về cách nhận thức của khách hàng ảnh hưởng đến quyết định mua hàng. Ví dụ: Customer perception of the restaurant chain improved significantly after it published detailed reports about the origin and quality of every ingredient on its menu."
                            },
                            {
                                "targetVocab": "loyalty",
                                "prompt": "Dùng từ 'loyalty' để viết một câu về lòng trung thành của khách hàng và giá trị kinh doanh của nó. Ví dụ: The coffee chain's loyalty program rewarded frequent customers with free drinks and exclusive discounts, reducing the rate at which customers switched to competing brands."
                            },
                            {
                                "targetVocab": "awareness",
                                "prompt": "Dùng từ 'awareness' để viết một câu về chiến dịch xây dựng nhận biết thương hiệu. Ví dụ: The company partnered with popular Vietnamese influencers on social media to rapidly build brand awareness among young consumers in major cities."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về xây dựng và mở rộng giá trị thương hiệu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "brand — thương hiệu, positioning — định vị, differentiation — khác biệt hóa, "
                            "perception — nhận thức, loyalty — lòng trung thành, và awareness — nhận biết thương hiệu. "
                            "Bạn đã hiểu cách thương hiệu chiếm lĩnh tâm trí khách hàng — "
                            "từ nhận biết ban đầu đến lòng trung thành lâu dài. "
                            "Bây giờ, chúng ta sẽ đi sâu hơn vào cách doanh nghiệp xây dựng "
                            "và mở rộng giá trị thương hiệu.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: identity, equity, portfolio, extension, endorsement, và licensing. "
                            "Đây là bộ từ vựng giúp bạn hiểu cách thương hiệu được quản lý như một tài sản chiến lược.\n\n"
                            "Từ đầu tiên là identity — danh từ — nghĩa là bản sắc thương hiệu, "
                            "tập hợp các yếu tố hữu hình và vô hình tạo nên diện mạo riêng của thương hiệu. "
                            "Ví dụ: 'The company redesigned its brand identity — including a new logo, color palette, and typography — to appeal to a younger generation of Vietnamese consumers.' "
                            "Trong bài đọc, identity là bộ mặt của thương hiệu — "
                            "nó bao gồm logo, màu sắc, giọng nói, và mọi thứ mà khách hàng nhìn thấy và cảm nhận.\n\n"
                            "Từ thứ hai là equity — danh từ — nghĩa là giá trị thương hiệu, "
                            "giá trị vô hình mà một thương hiệu mạnh mang lại cho sản phẩm vượt xa giá trị vật chất. "
                            "Ví dụ: 'Brand equity allows the company to charge a thirty percent premium over generic competitors because customers trust the name and associate it with quality.' "
                            "Trong bài đọc, equity là lý do vì sao hai sản phẩm giống hệt nhau "
                            "có thể bán với giá chênh lệch rất lớn — thương hiệu mạnh tạo ra giá trị thặng dư.\n\n"
                            "Từ thứ ba là portfolio — danh từ — nghĩa là danh mục thương hiệu, "
                            "tập hợp tất cả các thương hiệu mà một công ty sở hữu và quản lý. "
                            "Ví dụ: 'The consumer goods corporation manages a portfolio of over twenty brands, each targeting a different market segment from budget to luxury.' "
                            "Trong bài đọc, portfolio cho thấy cách các tập đoàn lớn "
                            "sử dụng nhiều thương hiệu khác nhau để phục vụ nhiều phân khúc khách hàng.\n\n"
                            "Từ thứ tư là extension — danh từ — nghĩa là mở rộng thương hiệu, "
                            "chiến lược sử dụng tên thương hiệu hiện có để ra mắt sản phẩm mới trong danh mục khác. "
                            "Ví dụ: 'The sportswear brand's extension into casual lifestyle clothing was a success because customers already associated the name with comfort and quality.' "
                            "Trong bài đọc, extension là con dao hai lưỡi — "
                            "nếu thành công, nó tận dụng được uy tín sẵn có; nếu thất bại, nó có thể làm loãng thương hiệu gốc.\n\n"
                            "Từ thứ năm là endorsement — danh từ — nghĩa là sự chứng thực, "
                            "việc một người nổi tiếng hoặc chuyên gia công khai ủng hộ và quảng bá cho một thương hiệu. "
                            "Ví dụ: 'The celebrity endorsement deal cost the company five billion dong, but it doubled brand awareness among young consumers within three months.' "
                            "Trong bài đọc, endorsement là chiến lược mượn uy tín — "
                            "khi một ngôi sao được yêu thích nói tốt về sản phẩm, khách hàng có xu hướng tin tưởng hơn.\n\n"
                            "Từ cuối cùng là licensing — danh từ — nghĩa là cấp phép thương hiệu, "
                            "thỏa thuận cho phép bên thứ ba sử dụng tên hoặc hình ảnh thương hiệu để sản xuất sản phẩm. "
                            "Ví dụ: 'Through licensing agreements, the fashion brand earns royalties from manufacturers who produce accessories, perfumes, and home goods under its name.' "
                            "Trong bài đọc, licensing là cách thương hiệu mở rộng phạm vi "
                            "mà không cần tự sản xuất — họ cho thuê tên tuổi và thu phí bản quyền.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về cách doanh nghiệp xây dựng và mở rộng giá trị thương hiệu nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Bản sắc và giá trị thương hiệu",
                    "description": "Học 6 từ: identity, equity, portfolio, extension, endorsement, licensing",
                    "data": {"vocabList": ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Bản sắc và giá trị thương hiệu",
                    "description": "Học 6 từ: identity, equity, portfolio, extension, endorsement, licensing",
                    "data": {"vocabList": ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Bản sắc và giá trị thương hiệu",
                    "description": "Học 6 từ: identity, equity, portfolio, extension, endorsement, licensing",
                    "data": {"vocabList": ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Bản sắc và giá trị thương hiệu",
                    "description": "Học 6 từ: identity, equity, portfolio, extension, endorsement, licensing",
                    "data": {"vocabList": ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Bản sắc và giá trị thương hiệu",
                    "description": "Học 6 từ: identity, equity, portfolio, extension, endorsement, licensing",
                    "data": {"vocabList": ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Xây dựng và mở rộng giá trị thương hiệu",
                    "description": "Behind every successful brand is a carefully constructed identity — a set of visual and emotional elements that make it instantly recognizable.",
                    "data": {
                        "text": (
                            "Behind every successful brand is a carefully constructed identity — "
                            "a set of visual and emotional elements that make it instantly recognizable. "
                            "Brand identity includes the logo, the color scheme, the tone of voice in advertising, "
                            "and even the way employees interact with customers. "
                            "When a Vietnamese bank redesigns its branches with modern furniture and warm lighting, "
                            "it is not just renovating — it is reshaping its identity "
                            "to signal that it is a forward-thinking institution.\n\n"
                            "A strong identity contributes to brand equity — "
                            "the additional value that a brand name adds to a product. "
                            "Consider two identical white T-shirts. "
                            "One carries no label; the other carries the logo of a famous fashion house. "
                            "The branded shirt can sell for ten times the price. "
                            "The difference is not in the fabric — it is in the equity "
                            "that the brand has built over years of consistent quality, marketing, and customer experience. "
                            "Brand equity is an intangible asset, but it has very real financial consequences.\n\n"
                            "Large companies often manage not just one brand but an entire portfolio. "
                            "A brand portfolio is the collection of all brands owned by a single corporation. "
                            "A Vietnamese food conglomerate, for example, might own a premium organic brand, "
                            "a mid-range family brand, and a budget brand for price-sensitive shoppers. "
                            "Each brand in the portfolio serves a different segment, "
                            "and the company must ensure they do not compete with each other.\n\n"
                            "One way to grow a brand is through extension. "
                            "Brand extension means using an established brand name to launch a new product "
                            "in a different category. A well-known Vietnamese tea company might use its name "
                            "to launch a line of bottled fruit juices. "
                            "The advantage is that customers already trust the brand, "
                            "so the new product starts with built-in credibility. "
                            "The risk is that if the new product fails or is of lower quality, "
                            "it can damage the reputation of the original brand.\n\n"
                            "Another growth strategy is endorsement. "
                            "Celebrity endorsement involves paying a famous person — "
                            "an athlete, an actor, or a social media influencer — "
                            "to publicly support the brand. "
                            "In Vietnam, endorsement deals with popular singers and football players "
                            "are common in industries from beverages to electronics. "
                            "The logic is simple: if consumers admire the celebrity, "
                            "some of that admiration transfers to the brand. "
                            "However, endorsement carries risk — if the celebrity is involved in a scandal, "
                            "the brand's reputation can suffer.\n\n"
                            "Finally, licensing allows a brand to expand without manufacturing new products itself. "
                            "In a licensing agreement, the brand owner grants another company "
                            "the right to produce and sell products using the brand name. "
                            "A luxury fashion brand might license its name to a company that makes sunglasses "
                            "or perfumes. The brand earns royalties without investing in new factories. "
                            "Licensing is especially popular in fashion, entertainment, and sports, "
                            "where brand names carry enormous value across multiple product categories."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Xây dựng và mở rộng giá trị thương hiệu",
                    "description": "Behind every successful brand is a carefully constructed identity — a set of visual and emotional elements that make it instantly recognizable.",
                    "data": {
                        "text": (
                            "Behind every successful brand is a carefully constructed identity — "
                            "a set of visual and emotional elements that make it instantly recognizable. "
                            "Brand identity includes the logo, the color scheme, the tone of voice in advertising, "
                            "and even the way employees interact with customers. "
                            "When a Vietnamese bank redesigns its branches with modern furniture and warm lighting, "
                            "it is not just renovating — it is reshaping its identity "
                            "to signal that it is a forward-thinking institution.\n\n"
                            "A strong identity contributes to brand equity — "
                            "the additional value that a brand name adds to a product. "
                            "Consider two identical white T-shirts. "
                            "One carries no label; the other carries the logo of a famous fashion house. "
                            "The branded shirt can sell for ten times the price. "
                            "The difference is not in the fabric — it is in the equity "
                            "that the brand has built over years of consistent quality, marketing, and customer experience. "
                            "Brand equity is an intangible asset, but it has very real financial consequences.\n\n"
                            "Large companies often manage not just one brand but an entire portfolio. "
                            "A brand portfolio is the collection of all brands owned by a single corporation. "
                            "A Vietnamese food conglomerate, for example, might own a premium organic brand, "
                            "a mid-range family brand, and a budget brand for price-sensitive shoppers. "
                            "Each brand in the portfolio serves a different segment, "
                            "and the company must ensure they do not compete with each other.\n\n"
                            "One way to grow a brand is through extension. "
                            "Brand extension means using an established brand name to launch a new product "
                            "in a different category. A well-known Vietnamese tea company might use its name "
                            "to launch a line of bottled fruit juices. "
                            "The advantage is that customers already trust the brand, "
                            "so the new product starts with built-in credibility. "
                            "The risk is that if the new product fails or is of lower quality, "
                            "it can damage the reputation of the original brand.\n\n"
                            "Another growth strategy is endorsement. "
                            "Celebrity endorsement involves paying a famous person — "
                            "an athlete, an actor, or a social media influencer — "
                            "to publicly support the brand. "
                            "In Vietnam, endorsement deals with popular singers and football players "
                            "are common in industries from beverages to electronics. "
                            "The logic is simple: if consumers admire the celebrity, "
                            "some of that admiration transfers to the brand. "
                            "However, endorsement carries risk — if the celebrity is involved in a scandal, "
                            "the brand's reputation can suffer.\n\n"
                            "Finally, licensing allows a brand to expand without manufacturing new products itself. "
                            "In a licensing agreement, the brand owner grants another company "
                            "the right to produce and sell products using the brand name. "
                            "A luxury fashion brand might license its name to a company that makes sunglasses "
                            "or perfumes. The brand earns royalties without investing in new factories. "
                            "Licensing is especially popular in fashion, entertainment, and sports, "
                            "where brand names carry enormous value across multiple product categories."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Xây dựng và mở rộng giá trị thương hiệu",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Behind every successful brand is a carefully constructed identity — "
                            "a set of visual and emotional elements that make it instantly recognizable. "
                            "Brand identity includes the logo, the color scheme, the tone of voice in advertising, "
                            "and even the way employees interact with customers. "
                            "When a Vietnamese bank redesigns its branches with modern furniture and warm lighting, "
                            "it is not just renovating — it is reshaping its identity "
                            "to signal that it is a forward-thinking institution.\n\n"
                            "A strong identity contributes to brand equity — "
                            "the additional value that a brand name adds to a product. "
                            "Consider two identical white T-shirts. "
                            "One carries no label; the other carries the logo of a famous fashion house. "
                            "The branded shirt can sell for ten times the price. "
                            "The difference is not in the fabric — it is in the equity "
                            "that the brand has built over years of consistent quality, marketing, and customer experience. "
                            "Brand equity is an intangible asset, but it has very real financial consequences.\n\n"
                            "Large companies often manage not just one brand but an entire portfolio. "
                            "A brand portfolio is the collection of all brands owned by a single corporation. "
                            "A Vietnamese food conglomerate, for example, might own a premium organic brand, "
                            "a mid-range family brand, and a budget brand for price-sensitive shoppers. "
                            "Each brand in the portfolio serves a different segment, "
                            "and the company must ensure they do not compete with each other.\n\n"
                            "One way to grow a brand is through extension. "
                            "Brand extension means using an established brand name to launch a new product "
                            "in a different category. A well-known Vietnamese tea company might use its name "
                            "to launch a line of bottled fruit juices. "
                            "The advantage is that customers already trust the brand, "
                            "so the new product starts with built-in credibility. "
                            "The risk is that if the new product fails or is of lower quality, "
                            "it can damage the reputation of the original brand.\n\n"
                            "Another growth strategy is endorsement. "
                            "Celebrity endorsement involves paying a famous person — "
                            "an athlete, an actor, or a social media influencer — "
                            "to publicly support the brand. "
                            "In Vietnam, endorsement deals with popular singers and football players "
                            "are common in industries from beverages to electronics. "
                            "The logic is simple: if consumers admire the celebrity, "
                            "some of that admiration transfers to the brand. "
                            "However, endorsement carries risk — if the celebrity is involved in a scandal, "
                            "the brand's reputation can suffer.\n\n"
                            "Finally, licensing allows a brand to expand without manufacturing new products itself. "
                            "In a licensing agreement, the brand owner grants another company "
                            "the right to produce and sell products using the brand name. "
                            "A luxury fashion brand might license its name to a company that makes sunglasses "
                            "or perfumes. The brand earns royalties without investing in new factories. "
                            "Licensing is especially popular in fashion, entertainment, and sports, "
                            "where brand names carry enormous value across multiple product categories."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Bản sắc và giá trị thương hiệu",
                    "description": "Viết câu sử dụng 6 từ vựng về xây dựng và mở rộng thương hiệu.",
                    "data": {
                        "vocabList": ["identity", "equity", "portfolio", "extension", "endorsement", "licensing"],
                        "items": [
                            {
                                "targetVocab": "identity",
                                "prompt": "Dùng từ 'identity' để viết một câu về cách một thương hiệu xây dựng bản sắc riêng. Ví dụ: The airline completely overhauled its brand identity by introducing a new logo, redesigning its uniforms, and adopting a warmer tone in all customer communications."
                            },
                            {
                                "targetVocab": "equity",
                                "prompt": "Dùng từ 'equity' để viết một câu về giá trị vô hình mà thương hiệu mang lại. Ví dụ: Years of consistent quality and clever advertising built enormous brand equity, allowing the company to charge premium prices that competitors could not match."
                            },
                            {
                                "targetVocab": "portfolio",
                                "prompt": "Dùng từ 'portfolio' để viết một câu về cách một tập đoàn quản lý nhiều thương hiệu. Ví dụ: The corporation's brand portfolio includes a luxury cosmetics line, a mid-range skincare brand, and an affordable daily-use brand, each targeting a distinct customer group."
                            },
                            {
                                "targetVocab": "extension",
                                "prompt": "Dùng từ 'extension' để viết một câu về chiến lược mở rộng thương hiệu sang danh mục sản phẩm mới. Ví dụ: The successful brand extension into frozen meals surprised analysts, but customers trusted the brand's reputation for quality and were willing to try the new product line."
                            },
                            {
                                "targetVocab": "endorsement",
                                "prompt": "Dùng từ 'endorsement' để viết một câu về tác động của người nổi tiếng đối với thương hiệu. Ví dụ: The endorsement deal with the national football team captain boosted sales by forty percent in the first quarter, proving the power of celebrity influence in the Vietnamese market."
                            },
                            {
                                "targetVocab": "licensing",
                                "prompt": "Dùng từ 'licensing' để viết một câu về cách thương hiệu mở rộng thông qua cấp phép. Ví dụ: Through licensing agreements with local manufacturers, the international fashion brand now sells handbags, watches, and perfumes in Vietnam without operating a single factory in the country."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về tái định vị và kể chuyện thương hiệu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: brand, positioning, differentiation, perception, loyalty, awareness — "
                            "những khái niệm cốt lõi về cách thương hiệu chiếm lĩnh tâm trí khách hàng. "
                            "Trong phần 2, bạn đã học thêm identity, equity, portfolio, extension, endorsement, licensing — "
                            "bộ từ vựng về xây dựng và mở rộng giá trị thương hiệu.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh sâu hơn: "
                            "tái định vị thương hiệu, chiến lược giá, và nghệ thuật kể chuyện thương hiệu. "
                            "Bạn sẽ học 6 từ mới: rebranding, premium, niche, archetype, touchpoint, và narrative.\n\n"
                            "Từ đầu tiên là rebranding — danh từ — nghĩa là tái định vị thương hiệu, "
                            "quá trình thay đổi hình ảnh, thông điệp hoặc chiến lược của thương hiệu "
                            "để phù hợp với thị trường mới hoặc khắc phục hình ảnh cũ. "
                            "Ví dụ: 'The company's rebranding effort included a new name, a modern logo, and a completely different advertising tone to attract younger customers who had ignored the brand for years.' "
                            "Trong bài đọc, rebranding là quyết định táo bạo — "
                            "nó có thể cứu sống một thương hiệu đang chết hoặc phá hủy di sản mà thương hiệu đã xây dựng.\n\n"
                            "Từ thứ hai là premium — tính từ/danh từ — nghĩa là cao cấp, "
                            "phân khúc sản phẩm hoặc dịch vụ có giá cao hơn đáng kể so với mức trung bình thị trường. "
                            "Ví dụ: 'The premium pricing strategy worked because the brand had built enough equity for customers to believe the product was worth three times the price of ordinary alternatives.' "
                            "Trong bài đọc, premium không chỉ là giá cao — "
                            "nó là lời hứa về chất lượng vượt trội và trải nghiệm đặc biệt.\n\n"
                            "Từ thứ ba là niche — danh từ/tính từ — nghĩa là thị trường ngách, "
                            "phân khúc thị trường nhỏ nhưng chuyên biệt với nhu cầu riêng biệt. "
                            "Ví dụ: 'Instead of competing with giant corporations, the startup found a profitable niche by creating organic baby food specifically for Vietnamese families with food allergy concerns.' "
                            "Trong bài đọc, niche là chiến lược của kẻ thông minh — "
                            "thay vì cạnh tranh với tất cả, bạn trở thành số một trong một lĩnh vực nhỏ.\n\n"
                            "Từ thứ tư là archetype — danh từ — nghĩa là nguyên mẫu thương hiệu, "
                            "mô hình tính cách phổ quát mà thương hiệu sử dụng để tạo kết nối cảm xúc với khách hàng. "
                            "Ví dụ: 'Nike uses the Hero archetype in its branding — every advertisement tells a story of ordinary people overcoming obstacles through determination and athletic achievement.' "
                            "Trong bài đọc, archetype giải thích vì sao một số thương hiệu "
                            "khiến bạn cảm thấy được truyền cảm hứng, trong khi thương hiệu khác khiến bạn cảm thấy an toàn.\n\n"
                            "Từ thứ năm là touchpoint — danh từ — nghĩa là điểm tiếp xúc, "
                            "bất kỳ khoảnh khắc nào mà khách hàng tương tác với thương hiệu. "
                            "Ví dụ: 'The marketing team mapped every customer touchpoint — from the first social media ad to the post-purchase email — to ensure a consistent and positive brand experience at every stage.' "
                            "Trong bài đọc, touchpoint là nơi thương hiệu sống hoặc chết — "
                            "mỗi lần khách hàng tiếp xúc là một cơ hội để củng cố hoặc phá hủy niềm tin.\n\n"
                            "Từ cuối cùng là narrative — danh từ — nghĩa là câu chuyện thương hiệu, "
                            "câu chuyện xuyên suốt mà thương hiệu kể để tạo ý nghĩa và kết nối cảm xúc. "
                            "Ví dụ: 'The brand's narrative centers on the founder's journey from a small village in the Mekong Delta to building one of Vietnam's most recognized organic food companies.' "
                            "Trong bài đọc, narrative là linh hồn của thương hiệu — "
                            "con người không nhớ số liệu, nhưng họ nhớ câu chuyện.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về tái định vị và kể chuyện thương hiệu nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Tái định vị và kể chuyện thương hiệu",
                    "description": "Học 6 từ: rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Tái định vị và kể chuyện thương hiệu",
                    "description": "Học 6 từ: rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Tái định vị và kể chuyện thương hiệu",
                    "description": "Học 6 từ: rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Tái định vị và kể chuyện thương hiệu",
                    "description": "Học 6 từ: rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Tái định vị và kể chuyện thương hiệu",
                    "description": "Học 6 từ: rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tái định vị, chiến lược giá và kể chuyện thương hiệu",
                    "description": "Brands are not permanent — they evolve, and sometimes they must be completely reinvented.",
                    "data": {
                        "text": (
                            "Brands are not permanent — they evolve, and sometimes they must be completely reinvented. "
                            "When a brand's image no longer matches the market it serves, "
                            "the company may decide on rebranding. "
                            "Rebranding is more than changing a logo. "
                            "It can involve a new name, a new visual identity, a new tone of voice, "
                            "and even a new target audience. "
                            "A Vietnamese telecommunications company, for example, might rebrand "
                            "to shed its image as a traditional phone service provider "
                            "and reposition itself as a digital lifestyle platform for young professionals.\n\n"
                            "Rebranding is risky because it asks loyal customers to accept change. "
                            "If the new identity feels disconnected from what people loved about the original brand, "
                            "the company can lose the very customers it was trying to keep. "
                            "Successful rebranding requires careful research, clear communication, "
                            "and a genuine reason for the change — not just a desire to look modern.\n\n"
                            "One strategic choice that defines a brand is whether to pursue a premium or niche position. "
                            "A premium brand charges higher prices and promises superior quality, "
                            "exclusive experiences, or elevated status. "
                            "Vietnamese consumers increasingly seek premium products — "
                            "from specialty coffee to imported skincare — "
                            "and are willing to pay more when they believe the brand delivers real value. "
                            "Premium pricing only works when the brand has enough equity "
                            "to justify the higher cost in the customer's mind.\n\n"
                            "A niche brand takes a different approach. "
                            "Instead of trying to appeal to everyone, it focuses on a small, "
                            "specific segment of the market with specialized needs. "
                            "A company that makes gluten-free snacks for health-conscious Vietnamese athletes "
                            "is operating in a niche. The market is small, "
                            "but the lack of competition and the intensity of customer loyalty "
                            "can make niche brands highly profitable.\n\n"
                            "To connect with customers on a deeper level, "
                            "many brands adopt an archetype — a universal character pattern "
                            "that people instinctively recognize and respond to. "
                            "The twelve brand archetypes include the Hero, the Explorer, the Caregiver, "
                            "the Rebel, and others. A sportswear brand might adopt the Hero archetype, "
                            "telling stories of athletes who push beyond their limits. "
                            "A children's food brand might use the Caregiver archetype, "
                            "emphasizing nurturing and protection. "
                            "Archetypes give brands a consistent personality "
                            "that resonates across cultures and languages.\n\n"
                            "Every interaction between a customer and a brand is a touchpoint. "
                            "Touchpoints include the company's website, its social media posts, "
                            "the packaging of its products, the behavior of its sales staff, "
                            "and even the receipt a customer receives after a purchase. "
                            "Smart marketers map every touchpoint in the customer journey "
                            "and design each one to reinforce the brand's positioning and values. "
                            "A single inconsistent touchpoint — a rude employee, a confusing website — "
                            "can undo months of careful brand building.\n\n"
                            "Finally, the most powerful brands are built on a compelling narrative. "
                            "A brand narrative is the overarching story that gives meaning "
                            "to everything the brand does. "
                            "It is not a slogan or a tagline — it is the deeper story "
                            "about why the brand exists and what it stands for. "
                            "A Vietnamese organic farm brand might build its narrative "
                            "around the founder's childhood memories of eating fresh vegetables "
                            "from her grandmother's garden in the countryside. "
                            "That story connects the brand to values of tradition, health, and authenticity — "
                            "values that no competitor can copy because the narrative is uniquely theirs."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tái định vị, chiến lược giá và kể chuyện thương hiệu",
                    "description": "Brands are not permanent — they evolve, and sometimes they must be completely reinvented.",
                    "data": {
                        "text": (
                            "Brands are not permanent — they evolve, and sometimes they must be completely reinvented. "
                            "When a brand's image no longer matches the market it serves, "
                            "the company may decide on rebranding. "
                            "Rebranding is more than changing a logo. "
                            "It can involve a new name, a new visual identity, a new tone of voice, "
                            "and even a new target audience. "
                            "A Vietnamese telecommunications company, for example, might rebrand "
                            "to shed its image as a traditional phone service provider "
                            "and reposition itself as a digital lifestyle platform for young professionals.\n\n"
                            "Rebranding is risky because it asks loyal customers to accept change. "
                            "If the new identity feels disconnected from what people loved about the original brand, "
                            "the company can lose the very customers it was trying to keep. "
                            "Successful rebranding requires careful research, clear communication, "
                            "and a genuine reason for the change — not just a desire to look modern.\n\n"
                            "One strategic choice that defines a brand is whether to pursue a premium or niche position. "
                            "A premium brand charges higher prices and promises superior quality, "
                            "exclusive experiences, or elevated status. "
                            "Vietnamese consumers increasingly seek premium products — "
                            "from specialty coffee to imported skincare — "
                            "and are willing to pay more when they believe the brand delivers real value. "
                            "Premium pricing only works when the brand has enough equity "
                            "to justify the higher cost in the customer's mind.\n\n"
                            "A niche brand takes a different approach. "
                            "Instead of trying to appeal to everyone, it focuses on a small, "
                            "specific segment of the market with specialized needs. "
                            "A company that makes gluten-free snacks for health-conscious Vietnamese athletes "
                            "is operating in a niche. The market is small, "
                            "but the lack of competition and the intensity of customer loyalty "
                            "can make niche brands highly profitable.\n\n"
                            "To connect with customers on a deeper level, "
                            "many brands adopt an archetype — a universal character pattern "
                            "that people instinctively recognize and respond to. "
                            "The twelve brand archetypes include the Hero, the Explorer, the Caregiver, "
                            "the Rebel, and others. A sportswear brand might adopt the Hero archetype, "
                            "telling stories of athletes who push beyond their limits. "
                            "A children's food brand might use the Caregiver archetype, "
                            "emphasizing nurturing and protection. "
                            "Archetypes give brands a consistent personality "
                            "that resonates across cultures and languages.\n\n"
                            "Every interaction between a customer and a brand is a touchpoint. "
                            "Touchpoints include the company's website, its social media posts, "
                            "the packaging of its products, the behavior of its sales staff, "
                            "and even the receipt a customer receives after a purchase. "
                            "Smart marketers map every touchpoint in the customer journey "
                            "and design each one to reinforce the brand's positioning and values. "
                            "A single inconsistent touchpoint — a rude employee, a confusing website — "
                            "can undo months of careful brand building.\n\n"
                            "Finally, the most powerful brands are built on a compelling narrative. "
                            "A brand narrative is the overarching story that gives meaning "
                            "to everything the brand does. "
                            "It is not a slogan or a tagline — it is the deeper story "
                            "about why the brand exists and what it stands for. "
                            "A Vietnamese organic farm brand might build its narrative "
                            "around the founder's childhood memories of eating fresh vegetables "
                            "from her grandmother's garden in the countryside. "
                            "That story connects the brand to values of tradition, health, and authenticity — "
                            "values that no competitor can copy because the narrative is uniquely theirs."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tái định vị, chiến lược giá và kể chuyện thương hiệu",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Brands are not permanent — they evolve, and sometimes they must be completely reinvented. "
                            "When a brand's image no longer matches the market it serves, "
                            "the company may decide on rebranding. "
                            "Rebranding is more than changing a logo. "
                            "It can involve a new name, a new visual identity, a new tone of voice, "
                            "and even a new target audience. "
                            "A Vietnamese telecommunications company, for example, might rebrand "
                            "to shed its image as a traditional phone service provider "
                            "and reposition itself as a digital lifestyle platform for young professionals.\n\n"
                            "Rebranding is risky because it asks loyal customers to accept change. "
                            "If the new identity feels disconnected from what people loved about the original brand, "
                            "the company can lose the very customers it was trying to keep. "
                            "Successful rebranding requires careful research, clear communication, "
                            "and a genuine reason for the change — not just a desire to look modern.\n\n"
                            "One strategic choice that defines a brand is whether to pursue a premium or niche position. "
                            "A premium brand charges higher prices and promises superior quality, "
                            "exclusive experiences, or elevated status. "
                            "Vietnamese consumers increasingly seek premium products — "
                            "from specialty coffee to imported skincare — "
                            "and are willing to pay more when they believe the brand delivers real value. "
                            "Premium pricing only works when the brand has enough equity "
                            "to justify the higher cost in the customer's mind.\n\n"
                            "A niche brand takes a different approach. "
                            "Instead of trying to appeal to everyone, it focuses on a small, "
                            "specific segment of the market with specialized needs. "
                            "A company that makes gluten-free snacks for health-conscious Vietnamese athletes "
                            "is operating in a niche. The market is small, "
                            "but the lack of competition and the intensity of customer loyalty "
                            "can make niche brands highly profitable.\n\n"
                            "To connect with customers on a deeper level, "
                            "many brands adopt an archetype — a universal character pattern "
                            "that people instinctively recognize and respond to. "
                            "The twelve brand archetypes include the Hero, the Explorer, the Caregiver, "
                            "the Rebel, and others. A sportswear brand might adopt the Hero archetype, "
                            "telling stories of athletes who push beyond their limits. "
                            "A children's food brand might use the Caregiver archetype, "
                            "emphasizing nurturing and protection. "
                            "Archetypes give brands a consistent personality "
                            "that resonates across cultures and languages.\n\n"
                            "Every interaction between a customer and a brand is a touchpoint. "
                            "Touchpoints include the company's website, its social media posts, "
                            "the packaging of its products, the behavior of its sales staff, "
                            "and even the receipt a customer receives after a purchase. "
                            "Smart marketers map every touchpoint in the customer journey "
                            "and design each one to reinforce the brand's positioning and values. "
                            "A single inconsistent touchpoint — a rude employee, a confusing website — "
                            "can undo months of careful brand building.\n\n"
                            "Finally, the most powerful brands are built on a compelling narrative. "
                            "A brand narrative is the overarching story that gives meaning "
                            "to everything the brand does. "
                            "It is not a slogan or a tagline — it is the deeper story "
                            "about why the brand exists and what it stands for. "
                            "A Vietnamese organic farm brand might build its narrative "
                            "around the founder's childhood memories of eating fresh vegetables "
                            "from her grandmother's garden in the countryside. "
                            "That story connects the brand to values of tradition, health, and authenticity — "
                            "values that no competitor can copy because the narrative is uniquely theirs."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tái định vị và kể chuyện thương hiệu",
                    "description": "Viết câu sử dụng 6 từ vựng về tái định vị và kể chuyện thương hiệu.",
                    "data": {
                        "vocabList": ["rebranding", "premium", "niche", "archetype", "touchpoint", "narrative"],
                        "items": [
                            {
                                "targetVocab": "rebranding",
                                "prompt": "Dùng từ 'rebranding' để viết một câu về quá trình tái định vị thương hiệu và lý do doanh nghiệp thực hiện. Ví dụ: The telecommunications company's rebranding from a traditional phone service to a digital lifestyle platform attracted two million new young subscribers within the first year."
                            },
                            {
                                "targetVocab": "premium",
                                "prompt": "Dùng từ 'premium' để viết một câu về chiến lược giá cao cấp và điều kiện để thành công. Ví dụ: The Vietnamese chocolate maker justified its premium pricing by sourcing single-origin cacao from Lam Dong province and packaging each bar in handcrafted bamboo boxes."
                            },
                            {
                                "targetVocab": "niche",
                                "prompt": "Dùng từ 'niche' để viết một câu về cách một doanh nghiệp tìm thấy thị trường ngách. Ví dụ: By focusing on the niche market of plant-based protein for Vietnamese gym enthusiasts, the startup avoided direct competition with major food corporations and built a fiercely loyal customer base."
                            },
                            {
                                "targetVocab": "archetype",
                                "prompt": "Dùng từ 'archetype' để viết một câu về cách thương hiệu sử dụng nguyên mẫu tính cách. Ví dụ: The outdoor adventure brand adopted the Explorer archetype, filling its advertisements with images of young Vietnamese travelers discovering hidden waterfalls and remote mountain trails."
                            },
                            {
                                "targetVocab": "touchpoint",
                                "prompt": "Dùng từ 'touchpoint' để viết một câu về tầm quan trọng của các điểm tiếp xúc trong hành trình khách hàng. Ví dụ: The hotel chain trained every employee to deliver exceptional service at each customer touchpoint, from the greeting at the front desk to the farewell message left in the room on checkout day."
                            },
                            {
                                "targetVocab": "narrative",
                                "prompt": "Dùng từ 'narrative' để viết một câu về cách câu chuyện thương hiệu tạo kết nối cảm xúc. Ví dụ: The brand's narrative about a grandmother's traditional recipes passed down through three generations resonated deeply with Vietnamese consumers who value family heritage and authentic flavors."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Chiến lược thương hiệu. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "brand — thương hiệu, positioning — định vị, differentiation — khác biệt hóa, "
                            "perception — nhận thức, loyalty — lòng trung thành, và awareness — nhận biết thương hiệu. "
                            "Đây là bộ từ vựng cốt lõi về cách thương hiệu chiếm lĩnh tâm trí khách hàng.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào xây dựng và mở rộng giá trị thương hiệu: "
                            "identity — bản sắc, equity — giá trị thương hiệu, portfolio — danh mục thương hiệu, "
                            "extension — mở rộng thương hiệu, endorsement — chứng thực, và licensing — cấp phép. "
                            "Những từ này giúp bạn hiểu cách doanh nghiệp quản lý thương hiệu như một tài sản chiến lược.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "rebranding — tái định vị, premium — cao cấp, niche — thị trường ngách, "
                            "archetype — nguyên mẫu thương hiệu, touchpoint — điểm tiếp xúc, và narrative — câu chuyện thương hiệu. "
                            "Đây là những từ về chiến lược nâng cao và nghệ thuật kể chuyện thương hiệu.\n\n"
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
                    "description": "Học 18 từ: brand, positioning, differentiation, perception, loyalty, awareness, identity, equity, portfolio, extension, endorsement, licensing, rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: brand, positioning, differentiation, perception, loyalty, awareness, identity, equity, portfolio, extension, endorsement, licensing, rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: brand, positioning, differentiation, perception, loyalty, awareness, identity, equity, portfolio, extension, endorsement, licensing, rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: brand, positioning, differentiation, perception, loyalty, awareness, identity, equity, portfolio, extension, endorsement, licensing, rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: brand, positioning, differentiation, perception, loyalty, awareness, identity, equity, portfolio, extension, endorsement, licensing, rebranding, premium, niche, archetype, touchpoint, narrative",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng chiến lược thương hiệu",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "brand",
                                "prompt": "Dùng từ 'brand' để viết một câu về cách thương hiệu ảnh hưởng đến quyết định mua hàng của người tiêu dùng Việt Nam. Ví dụ: Vietnamese consumers increasingly choose products based on brand reputation rather than price alone, especially in categories like dairy, electronics, and personal care."
                            },
                            {
                                "targetVocab": "positioning",
                                "prompt": "Dùng từ 'positioning' để viết một câu về cách hai thương hiệu cạnh tranh bằng chiến lược định vị khác nhau. Ví dụ: While one coffee chain focused its positioning on speed and convenience for office workers, its competitor positioned itself as a relaxing social space for students and freelancers."
                            },
                            {
                                "targetVocab": "differentiation",
                                "prompt": "Dùng từ 'differentiation' để viết một câu về sự khác biệt hóa trong ngành công nghệ. Ví dụ: The Vietnamese fintech startup achieved differentiation by offering instant loan approvals through artificial intelligence, a service that traditional banks could not match due to their slower approval processes."
                            },
                            {
                                "targetVocab": "perception",
                                "prompt": "Dùng từ 'perception' để viết một câu về cách một sự kiện thay đổi nhận thức của khách hàng. Ví dụ: Public perception of the food brand collapsed overnight when a viral video showed unsanitary conditions at one of its factories, erasing years of carefully built trust."
                            },
                            {
                                "targetVocab": "loyalty",
                                "prompt": "Dùng từ 'loyalty' để viết một câu về mối quan hệ giữa chất lượng dịch vụ và lòng trung thành. Ví dụ: The airline built extraordinary customer loyalty by consistently delivering on-time flights, comfortable seating, and friendly service, making passengers reluctant to switch to cheaper competitors."
                            },
                            {
                                "targetVocab": "awareness",
                                "prompt": "Dùng từ 'awareness' để viết một câu về chiến lược xây dựng nhận biết thương hiệu trên mạng xã hội. Ví dụ: The brand awareness campaign on TikTok generated fifty million views in two weeks, introducing the new skincare line to an audience that had never heard of the company before."
                            },
                            {
                                "targetVocab": "identity",
                                "prompt": "Dùng từ 'identity' để viết một câu về cách bản sắc thương hiệu phản ánh giá trị cốt lõi. Ví dụ: The company's brand identity — from its earth-toned packaging to its handwritten-style logo — communicates its commitment to natural ingredients and environmental responsibility."
                            },
                            {
                                "targetVocab": "equity",
                                "prompt": "Dùng từ 'equity' để viết một câu về cách đo lường giá trị thương hiệu. Ví dụ: The marketing team measured brand equity through customer surveys that tracked awareness, perceived quality, and willingness to pay a premium compared to unbranded alternatives."
                            },
                            {
                                "targetVocab": "portfolio",
                                "prompt": "Dùng từ 'portfolio' để viết một câu về chiến lược quản lý danh mục thương hiệu. Ví dụ: After acquiring three smaller competitors, the corporation restructured its brand portfolio to eliminate overlap and ensure each brand served a clearly defined market segment."
                            },
                            {
                                "targetVocab": "extension",
                                "prompt": "Dùng từ 'extension' để viết một câu về rủi ro và cơ hội của mở rộng thương hiệu. Ví dụ: The brand extension into ready-to-drink beverages failed because consumers associated the brand exclusively with solid food products and could not accept it in a completely different category."
                            },
                            {
                                "targetVocab": "endorsement",
                                "prompt": "Dùng từ 'endorsement' để viết một câu về hiệu quả của chiến lược chứng thực thương hiệu. Ví dụ: The endorsement by a respected Vietnamese chef transformed the unknown olive oil brand into a household name, with sales tripling in the six months following the campaign launch."
                            },
                            {
                                "targetVocab": "licensing",
                                "prompt": "Dùng từ 'licensing' để viết một câu về cách cấp phép thương hiệu tạo nguồn thu mới. Ví dụ: The entertainment company's licensing revenue from toys, clothing, and school supplies exceeded its box office earnings, proving that brand licensing can be more profitable than the core business."
                            },
                            {
                                "targetVocab": "rebranding",
                                "prompt": "Dùng từ 'rebranding' để viết một câu về kết quả của một chiến dịch tái định vị thương hiệu. Ví dụ: The bank's rebranding from a conservative institution to a tech-savvy digital platform attracted three hundred thousand new accounts from customers under thirty within the first six months."
                            },
                            {
                                "targetVocab": "premium",
                                "prompt": "Dùng từ 'premium' để viết một câu về xu hướng tiêu dùng cao cấp tại Việt Nam. Ví dụ: The rise of the Vietnamese middle class has created strong demand for premium products, from organic vegetables to imported wines, as consumers increasingly prioritize quality over quantity."
                            },
                            {
                                "targetVocab": "niche",
                                "prompt": "Dùng từ 'niche' để viết một câu về lợi thế cạnh tranh của thương hiệu ngách. Ví dụ: The company dominated its niche in handmade ceramic tableware by building personal relationships with restaurant owners who valued craftsmanship over mass-produced alternatives."
                            },
                            {
                                "targetVocab": "archetype",
                                "prompt": "Dùng từ 'archetype' để viết một câu về cách nguyên mẫu thương hiệu định hình chiến lược truyền thông. Ví dụ: By adopting the Sage archetype, the educational technology company positioned itself as a trusted source of knowledge, using calm and authoritative language in all its marketing materials."
                            },
                            {
                                "targetVocab": "touchpoint",
                                "prompt": "Dùng từ 'touchpoint' để viết một câu về cách tối ưu hóa trải nghiệm khách hàng tại mỗi điểm tiếp xúc. Ví dụ: The retail chain redesigned every customer touchpoint — from store layout to checkout process to delivery packaging — resulting in a thirty percent increase in customer satisfaction scores."
                            },
                            {
                                "targetVocab": "narrative",
                                "prompt": "Dùng từ 'narrative' để viết một câu về sức mạnh của câu chuyện thương hiệu trong việc xây dựng kết nối cảm xúc. Ví dụ: The brand's narrative about empowering Vietnamese women entrepreneurs resonated so deeply that customers began sharing their own stories on social media, creating a community around the brand's mission."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về chiến lược thương hiệu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về chiến lược thương hiệu — từ xây dựng nhận biết, "
                            "định vị và khác biệt hóa, đến quản lý giá trị thương hiệu và kể chuyện thương hiệu.\n\n"
                            "Bạn sẽ gặp lại brand, positioning, differentiation, perception, loyalty, awareness "
                            "trong phần mở đầu về nền tảng của chiến lược thương hiệu. "
                            "Tiếp theo, identity, equity, portfolio, extension, endorsement, licensing "
                            "sẽ giúp bạn hiểu cách doanh nghiệp xây dựng và mở rộng giá trị thương hiệu. "
                            "Và cuối cùng, rebranding, premium, niche, archetype, touchpoint, narrative "
                            "sẽ đưa bạn vào thế giới tái định vị và nghệ thuật kể chuyện thương hiệu.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chiến lược thương hiệu — Bức tranh toàn cảnh",
                    "description": "Imagine you are a marketing consultant hired by a Vietnamese company that makes traditional herbal teas.",
                    "data": {
                        "text": (
                            "Imagine you are a marketing consultant hired by a Vietnamese company "
                            "that makes traditional herbal teas. "
                            "The company has been in business for fifteen years, "
                            "but sales have stagnated and younger consumers are choosing imported brands instead. "
                            "The CEO asks you one question: how do we fix our brand?\n\n"
                            "You begin with the fundamentals. "
                            "A brand is not just a name printed on a box of tea. "
                            "It is the sum of every thought, feeling, and memory "
                            "that customers associate with the company. "
                            "Right now, the company's brand is associated with tradition and older generations — "
                            "not necessarily a bad thing, but not enough to attract young professionals "
                            "who want modern, health-conscious products.\n\n"
                            "The first step is to define a clear positioning strategy. "
                            "You recommend that the company position itself as the bridge "
                            "between Vietnamese herbal wisdom and modern wellness culture. "
                            "This positioning is specific enough to stand out "
                            "but broad enough to allow future growth. "
                            "To make this positioning credible, the company needs differentiation — "
                            "something concrete that competitors cannot easily copy. "
                            "You suggest highlighting the company's exclusive partnerships "
                            "with highland farmers who grow rare medicinal herbs "
                            "using traditional methods passed down through generations.\n\n"
                            "Next, you address perception. "
                            "Customer surveys reveal that many young consumers perceive the brand "
                            "as old-fashioned and boring. "
                            "To shift this perception, you propose a complete redesign "
                            "of the packaging, website, and social media presence. "
                            "The goal is to make the brand feel contemporary and aspirational "
                            "while preserving its authentic heritage.\n\n"
                            "Building awareness among the new target audience is critical. "
                            "You design a digital marketing campaign that introduces the brand "
                            "to health-conscious millennials through Instagram, TikTok, and wellness blogs. "
                            "The campaign focuses on storytelling rather than product features, "
                            "showing real people incorporating herbal tea into their daily routines. "
                            "As awareness grows, the company can begin building loyalty "
                            "through a subscription service that delivers curated tea selections monthly, "
                            "rewarding repeat customers with exclusive blends and early access to new products.\n\n"
                            "With the foundation in place, you turn to brand identity. "
                            "The company's current identity — an old-fashioned logo, "
                            "brown packaging, and formal language — does not match its new positioning. "
                            "You commission a new visual identity: a clean, modern logo inspired by tea leaves, "
                            "a color palette of deep green and warm gold, "
                            "and a friendly, knowledgeable tone of voice in all communications. "
                            "This new identity must appear consistently across every touchpoint — "
                            "the website, the packaging, the social media accounts, "
                            "the retail displays, and even the way customer service representatives speak.\n\n"
                            "As the brand gains traction, its equity grows. "
                            "Brand equity is the premium value that the brand name adds to the product. "
                            "Before the transformation, the company's teas sold for the same price "
                            "as generic alternatives. Now, with stronger equity, "
                            "customers are willing to pay twenty percent more "
                            "because they trust the brand and value what it represents.\n\n"
                            "The CEO wants to expand. You advise building a brand portfolio "
                            "with three distinct lines: a premium organic collection for high-end consumers, "
                            "a mainstream wellness line for everyday use, "
                            "and a niche medicinal line for customers with specific health needs. "
                            "Each line serves a different segment without cannibalizing the others.\n\n"
                            "For the premium line, you recommend a brand extension strategy — "
                            "using the company's trusted name to launch herbal supplements and wellness snacks. "
                            "The extension leverages existing brand equity "
                            "so the new products do not have to build trust from scratch. "
                            "To accelerate growth, you negotiate an endorsement deal "
                            "with a popular Vietnamese wellness influencer "
                            "whose audience of two million followers matches the target demographic perfectly. "
                            "You also explore licensing opportunities, "
                            "allowing a hotel chain to serve the company's teas under its brand name "
                            "in exchange for royalty payments.\n\n"
                            "Six months later, the transformation is working — "
                            "but the CEO notices that the original product line is losing its identity "
                            "amid all the new launches. You recommend a careful rebranding "
                            "of the original line, updating its packaging and messaging "
                            "while preserving the heritage elements that loyal customers love. "
                            "The rebranding must feel like an evolution, not a revolution.\n\n"
                            "To deepen the emotional connection, "
                            "you help the company define its brand archetype. "
                            "After analysis, you choose the Sage archetype — "
                            "a brand that is wise, knowledgeable, and committed to helping people "
                            "make better decisions about their health. "
                            "Every piece of content, from blog posts to product descriptions, "
                            "now reflects this archetype's calm authority and genuine desire to educate.\n\n"
                            "Finally, you craft the brand narrative — "
                            "the story that ties everything together. "
                            "The narrative centers on the founder's grandmother, "
                            "who spent decades collecting herbal recipes from villages across central Vietnam. "
                            "Her knowledge, nearly lost to modernization, "
                            "is now preserved and shared with a new generation through every cup of tea. "
                            "This narrative gives the brand meaning that goes beyond commerce — "
                            "it connects customers to a living tradition, "
                            "and it is a story that no competitor can replicate."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chiến lược thương hiệu — Bức tranh toàn cảnh",
                    "description": "Imagine you are a marketing consultant hired by a Vietnamese company that makes traditional herbal teas.",
                    "data": {
                        "text": (
                            "Imagine you are a marketing consultant hired by a Vietnamese company "
                            "that makes traditional herbal teas. "
                            "The company has been in business for fifteen years, "
                            "but sales have stagnated and younger consumers are choosing imported brands instead. "
                            "The CEO asks you one question: how do we fix our brand?\n\n"
                            "You begin with the fundamentals. "
                            "A brand is not just a name printed on a box of tea. "
                            "It is the sum of every thought, feeling, and memory "
                            "that customers associate with the company. "
                            "Right now, the company's brand is associated with tradition and older generations — "
                            "not necessarily a bad thing, but not enough to attract young professionals "
                            "who want modern, health-conscious products.\n\n"
                            "The first step is to define a clear positioning strategy. "
                            "You recommend that the company position itself as the bridge "
                            "between Vietnamese herbal wisdom and modern wellness culture. "
                            "This positioning is specific enough to stand out "
                            "but broad enough to allow future growth. "
                            "To make this positioning credible, the company needs differentiation — "
                            "something concrete that competitors cannot easily copy. "
                            "You suggest highlighting the company's exclusive partnerships "
                            "with highland farmers who grow rare medicinal herbs "
                            "using traditional methods passed down through generations.\n\n"
                            "Next, you address perception. "
                            "Customer surveys reveal that many young consumers perceive the brand "
                            "as old-fashioned and boring. "
                            "To shift this perception, you propose a complete redesign "
                            "of the packaging, website, and social media presence. "
                            "The goal is to make the brand feel contemporary and aspirational "
                            "while preserving its authentic heritage.\n\n"
                            "Building awareness among the new target audience is critical. "
                            "You design a digital marketing campaign that introduces the brand "
                            "to health-conscious millennials through Instagram, TikTok, and wellness blogs. "
                            "The campaign focuses on storytelling rather than product features, "
                            "showing real people incorporating herbal tea into their daily routines. "
                            "As awareness grows, the company can begin building loyalty "
                            "through a subscription service that delivers curated tea selections monthly, "
                            "rewarding repeat customers with exclusive blends and early access to new products.\n\n"
                            "With the foundation in place, you turn to brand identity. "
                            "The company's current identity — an old-fashioned logo, "
                            "brown packaging, and formal language — does not match its new positioning. "
                            "You commission a new visual identity: a clean, modern logo inspired by tea leaves, "
                            "a color palette of deep green and warm gold, "
                            "and a friendly, knowledgeable tone of voice in all communications. "
                            "This new identity must appear consistently across every touchpoint — "
                            "the website, the packaging, the social media accounts, "
                            "the retail displays, and even the way customer service representatives speak.\n\n"
                            "As the brand gains traction, its equity grows. "
                            "Brand equity is the premium value that the brand name adds to the product. "
                            "Before the transformation, the company's teas sold for the same price "
                            "as generic alternatives. Now, with stronger equity, "
                            "customers are willing to pay twenty percent more "
                            "because they trust the brand and value what it represents.\n\n"
                            "The CEO wants to expand. You advise building a brand portfolio "
                            "with three distinct lines: a premium organic collection for high-end consumers, "
                            "a mainstream wellness line for everyday use, "
                            "and a niche medicinal line for customers with specific health needs. "
                            "Each line serves a different segment without cannibalizing the others.\n\n"
                            "For the premium line, you recommend a brand extension strategy — "
                            "using the company's trusted name to launch herbal supplements and wellness snacks. "
                            "The extension leverages existing brand equity "
                            "so the new products do not have to build trust from scratch. "
                            "To accelerate growth, you negotiate an endorsement deal "
                            "with a popular Vietnamese wellness influencer "
                            "whose audience of two million followers matches the target demographic perfectly. "
                            "You also explore licensing opportunities, "
                            "allowing a hotel chain to serve the company's teas under its brand name "
                            "in exchange for royalty payments.\n\n"
                            "Six months later, the transformation is working — "
                            "but the CEO notices that the original product line is losing its identity "
                            "amid all the new launches. You recommend a careful rebranding "
                            "of the original line, updating its packaging and messaging "
                            "while preserving the heritage elements that loyal customers love. "
                            "The rebranding must feel like an evolution, not a revolution.\n\n"
                            "To deepen the emotional connection, "
                            "you help the company define its brand archetype. "
                            "After analysis, you choose the Sage archetype — "
                            "a brand that is wise, knowledgeable, and committed to helping people "
                            "make better decisions about their health. "
                            "Every piece of content, from blog posts to product descriptions, "
                            "now reflects this archetype's calm authority and genuine desire to educate.\n\n"
                            "Finally, you craft the brand narrative — "
                            "the story that ties everything together. "
                            "The narrative centers on the founder's grandmother, "
                            "who spent decades collecting herbal recipes from villages across central Vietnam. "
                            "Her knowledge, nearly lost to modernization, "
                            "is now preserved and shared with a new generation through every cup of tea. "
                            "This narrative gives the brand meaning that goes beyond commerce — "
                            "it connects customers to a living tradition, "
                            "and it is a story that no competitor can replicate."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chiến lược thương hiệu — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine you are a marketing consultant hired by a Vietnamese company "
                            "that makes traditional herbal teas. "
                            "The company has been in business for fifteen years, "
                            "but sales have stagnated and younger consumers are choosing imported brands instead. "
                            "The CEO asks you one question: how do we fix our brand?\n\n"
                            "You begin with the fundamentals. "
                            "A brand is not just a name printed on a box of tea. "
                            "It is the sum of every thought, feeling, and memory "
                            "that customers associate with the company. "
                            "Right now, the company's brand is associated with tradition and older generations — "
                            "not necessarily a bad thing, but not enough to attract young professionals "
                            "who want modern, health-conscious products.\n\n"
                            "The first step is to define a clear positioning strategy. "
                            "You recommend that the company position itself as the bridge "
                            "between Vietnamese herbal wisdom and modern wellness culture. "
                            "This positioning is specific enough to stand out "
                            "but broad enough to allow future growth. "
                            "To make this positioning credible, the company needs differentiation — "
                            "something concrete that competitors cannot easily copy. "
                            "You suggest highlighting the company's exclusive partnerships "
                            "with highland farmers who grow rare medicinal herbs "
                            "using traditional methods passed down through generations.\n\n"
                            "Next, you address perception. "
                            "Customer surveys reveal that many young consumers perceive the brand "
                            "as old-fashioned and boring. "
                            "To shift this perception, you propose a complete redesign "
                            "of the packaging, website, and social media presence. "
                            "The goal is to make the brand feel contemporary and aspirational "
                            "while preserving its authentic heritage.\n\n"
                            "Building awareness among the new target audience is critical. "
                            "You design a digital marketing campaign that introduces the brand "
                            "to health-conscious millennials through Instagram, TikTok, and wellness blogs. "
                            "The campaign focuses on storytelling rather than product features, "
                            "showing real people incorporating herbal tea into their daily routines. "
                            "As awareness grows, the company can begin building loyalty "
                            "through a subscription service that delivers curated tea selections monthly, "
                            "rewarding repeat customers with exclusive blends and early access to new products.\n\n"
                            "With the foundation in place, you turn to brand identity. "
                            "The company's current identity — an old-fashioned logo, "
                            "brown packaging, and formal language — does not match its new positioning. "
                            "You commission a new visual identity: a clean, modern logo inspired by tea leaves, "
                            "a color palette of deep green and warm gold, "
                            "and a friendly, knowledgeable tone of voice in all communications. "
                            "This new identity must appear consistently across every touchpoint — "
                            "the website, the packaging, the social media accounts, "
                            "the retail displays, and even the way customer service representatives speak.\n\n"
                            "As the brand gains traction, its equity grows. "
                            "Brand equity is the premium value that the brand name adds to the product. "
                            "Before the transformation, the company's teas sold for the same price "
                            "as generic alternatives. Now, with stronger equity, "
                            "customers are willing to pay twenty percent more "
                            "because they trust the brand and value what it represents.\n\n"
                            "The CEO wants to expand. You advise building a brand portfolio "
                            "with three distinct lines: a premium organic collection for high-end consumers, "
                            "a mainstream wellness line for everyday use, "
                            "and a niche medicinal line for customers with specific health needs. "
                            "Each line serves a different segment without cannibalizing the others.\n\n"
                            "For the premium line, you recommend a brand extension strategy — "
                            "using the company's trusted name to launch herbal supplements and wellness snacks. "
                            "The extension leverages existing brand equity "
                            "so the new products do not have to build trust from scratch. "
                            "To accelerate growth, you negotiate an endorsement deal "
                            "with a popular Vietnamese wellness influencer "
                            "whose audience of two million followers matches the target demographic perfectly. "
                            "You also explore licensing opportunities, "
                            "allowing a hotel chain to serve the company's teas under its brand name "
                            "in exchange for royalty payments.\n\n"
                            "Six months later, the transformation is working — "
                            "but the CEO notices that the original product line is losing its identity "
                            "amid all the new launches. You recommend a careful rebranding "
                            "of the original line, updating its packaging and messaging "
                            "while preserving the heritage elements that loyal customers love. "
                            "The rebranding must feel like an evolution, not a revolution.\n\n"
                            "To deepen the emotional connection, "
                            "you help the company define its brand archetype. "
                            "After analysis, you choose the Sage archetype — "
                            "a brand that is wise, knowledgeable, and committed to helping people "
                            "make better decisions about their health. "
                            "Every piece of content, from blog posts to product descriptions, "
                            "now reflects this archetype's calm authority and genuine desire to educate.\n\n"
                            "Finally, you craft the brand narrative — "
                            "the story that ties everything together. "
                            "The narrative centers on the founder's grandmother, "
                            "who spent decades collecting herbal recipes from villages across central Vietnam. "
                            "Her knowledge, nearly lost to modernization, "
                            "is now preserved and shared with a new generation through every cup of tea. "
                            "This narrative gives the brand meaning that goes beyond commerce — "
                            "it connects customers to a living tradition, "
                            "and it is a story that no competitor can replicate."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chiến lược thương hiệu",
                    "description": "Viết đoạn văn phân tích chiến lược thương hiệu sử dụng từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của chiến lược thương hiệu. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích chiến lược xây dựng thương hiệu của một công ty Việt Nam mà bạn biết. Giải thích cách họ sử dụng positioning và differentiation để tạo chỗ đứng trên thị trường, vai trò của brand identity và touchpoint trong việc tạo trải nghiệm nhất quán, và cách brand narrative kết nối cảm xúc với khách hàng.",
                            "Hãy tưởng tượng bạn là giám đốc marketing của một startup Việt Nam. Giải thích cách bạn sẽ xây dựng brand awareness từ con số không, chiến lược premium hay niche mà bạn chọn, cách sử dụng endorsement hoặc licensing để mở rộng, và archetype nào phù hợp nhất với thương hiệu của bạn."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần đồng đội.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Chiến lược thương hiệu — "
                            "và mình muốn nói thẳng: bạn vừa trang bị cho mình "
                            "một bộ công cụ mà nhiều sinh viên marketing mơ ước. "
                            "18 từ vựng này không chỉ là kiến thức — "
                            "chúng là vũ khí để bạn bước vào bất kỳ cuộc thảo luận nào về thương hiệu "
                            "và đóng góp bằng tiếng Anh một cách tự tin.\n\n"
                            "Positioning — định vị. Đây là từ mà mọi giám đốc marketing "
                            "phải trả lời trước khi làm bất cứ điều gì khác: "
                            "'Thương hiệu của chúng ta đứng ở đâu trong tâm trí khách hàng?' "
                            "Ví dụ mới: The company's positioning as the only Vietnamese brand "
                            "offering certified organic baby food gave it an unassailable advantage "
                            "in a market where parents are increasingly worried about food safety.\n\n"
                            "Equity — giá trị thương hiệu. Đây là thước đo thực sự "
                            "của mọi nỗ lực xây dựng thương hiệu. "
                            "Khi equity cao, khách hàng sẵn sàng trả nhiều hơn, "
                            "tha thứ cho sai lầm nhỏ, và giới thiệu bạn cho người khác. "
                            "Ví dụ mới: The brand's equity was so strong that when it raised prices "
                            "by fifteen percent, ninety percent of customers stayed loyal "
                            "because they believed no alternative could match the quality.\n\n"
                            "Touchpoint — điểm tiếp xúc. Mỗi lần khách hàng chạm vào thương hiệu "
                            "là một cơ hội — hoặc một rủi ro. "
                            "Từ quảng cáo đầu tiên đến email sau mua hàng, "
                            "mỗi touchpoint phải kể cùng một câu chuyện. "
                            "Ví dụ mới: The brand audit revealed that the company's strongest touchpoint "
                            "was its in-store experience, where trained staff created personal connections "
                            "that no online competitor could replicate.\n\n"
                            "Archetype — nguyên mẫu thương hiệu. Đây là bí mật "
                            "đằng sau những thương hiệu khiến bạn cảm thấy điều gì đó — "
                            "không chỉ nghĩ về sản phẩm, mà thực sự cảm nhận. "
                            "Ví dụ mới: By embracing the Creator archetype, "
                            "the Vietnamese design studio attracted clients who valued imagination and originality, "
                            "building a reputation as the go-to agency for brands that wanted to stand out.\n\n"
                            "Narrative — câu chuyện thương hiệu. Đây có lẽ là từ quan trọng nhất "
                            "bạn học hôm nay, vì trong thời đại mà mọi sản phẩm đều có thể bị sao chép, "
                            "câu chuyện là thứ duy nhất không ai lấy được. "
                            "Ví dụ mới: The brand's narrative about preserving traditional Vietnamese craftsmanship "
                            "in a modern world turned every purchase into an act of cultural pride, "
                            "creating an emotional bond that price discounts from competitors could never break.\n\n"
                            "Niche — thị trường ngách. Trong một thế giới mà ai cũng muốn lớn, "
                            "đôi khi chiến lược thông minh nhất là chọn nhỏ — "
                            "nhưng nhỏ đúng chỗ, nhỏ đúng lúc, và trở thành số một trong lĩnh vực đó. "
                            "Ví dụ mới: The company found its niche in premium Vietnamese craft chocolate, "
                            "exporting single-origin bars to specialty stores in Tokyo and Paris "
                            "where customers paid ten times the price of mass-produced alternatives.\n\n"
                            "Bạn biết không, xây dựng thương hiệu không phải là công việc của một người — "
                            "nó là công việc của cả đội. Từ người thiết kế logo đến nhân viên bán hàng, "
                            "từ giám đốc marketing đến người viết nội dung — "
                            "mỗi người đều là một phần của câu chuyện thương hiệu. "
                            "Và bây giờ, với 18 từ vựng này, bạn đã sẵn sàng "
                            "để tham gia vào cuộc trò chuyện đó bằng tiếng Anh.\n\n"
                            "Hãy mang theo bộ từ vựng này vào lớp học, vào bài thuyết trình nhóm, "
                            "vào buổi thảo luận case study — và bạn sẽ thấy mình không chỉ hiểu, "
                            "mà còn dẫn dắt cuộc thảo luận. "
                            "Chúng ta cùng nhau tiến lên — hẹn gặp lại ở bài học tiếp theo!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Branding Strategy – Chiến Lược Thương Hiệu' AND uid = '{UID}' ORDER BY created_at;")
