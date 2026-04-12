"""
Create curriculum: Fashion Through the Decades
Level: intermediate | Type: balanced_skills | Content: [] | Topic: Arts
18 words, 5 sessions (3 learning + 1 review + 1 final reading)
Bilingual (Vietnamese instructions, English reading passages)
Description tone: bold_declaration
Farewell tone: warm_accountability
"""

import sys, os, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from firebase_token import get_firebase_id_token
from validate_curriculum import validate_balanced_skills_standard, validate_content_type_tags, validate_bilingual_prompts

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Vocabulary (18 words, 3 groups of 6) ──

group1 = ["silhouette", "hemline", "couture", "textile", "garment", "tailor"]
group2 = ["runway", "vintage", "accessory", "embroidery", "drape", "ensemble"]
group3 = ["sustainable", "haute", "avant-garde", "minimalist", "iconic", "revival"]
all_words = group1 + group2 + group3

# ── Hand-written content ──

content = {
    "title": "Fashion Through the Decades — Thời Trang Qua Các Thập Kỷ",
    "contentTypeTags": [],
    # Tone: bold_declaration
    "description": (
        "THỜI TRANG KHÔNG BAO GIỜ CHỈ LÀ QUẦN ÁO — NÓ LÀ LỊCH SỬ ĐƯỢC MẶC TRÊN NGƯỜI.\n\n"
        "Mỗi thập kỷ để lại dấu ấn trên trang phục con người — từ chiếc váy flapper phóng khoáng "
        "của những năm 1920 đến phong cách tối giản của thập niên 90. Bạn mặc gì không chỉ nói về gu thẩm mỹ, "
        "mà còn nói về thời đại bạn sống, giá trị bạn theo đuổi, và câu chuyện bạn muốn kể.\n\n"
        "Thời trang giống như một cuốn nhật ký khổng lồ của nhân loại — mỗi đường cắt, mỗi loại vải, "
        "mỗi phụ kiện đều ghi lại một chương trong lịch sử văn hóa và xã hội.\n\n"
        "Từ những xưởng couture ở Paris đến phong trào thời trang bền vững đang thay đổi ngành công nghiệp, "
        "bạn sẽ khám phá cách thời trang phản ánh — và định hình — thế giới chúng ta.\n\n"
        "Học 18 từ vựng sống động qua trải nghiệm đa giác quan — vừa khám phá silhouette, hemline, "
        "couture, runway, vừa nâng trình tiếng Anh một cách tự nhiên nhất."
    ),
    "preview": {
        "text": (
            "Bạn có biết rằng chiều dài hemline từng được dùng để dự đoán nền kinh tế? "
            "Rằng một chiếc váy đen nhỏ của Coco Chanel đã thay đổi cách phụ nữ ăn mặc mãi mãi? "
            "Rằng ngành thời trang là ngành gây ô nhiễm lớn thứ hai thế giới?\n\n"
            "Trong bài học này, bạn sẽ học 18 từ vựng tiếng Anh về thời trang qua các thập kỷ: "
            "silhouette, hemline, couture, textile, garment, tailor, runway, vintage, accessory, "
            "embroidery, drape, ensemble, sustainable, haute, avant-garde, minimalist, iconic, revival. "
            "Bạn sẽ đọc về sự tiến hóa của phong cách từ thập niên 20 đến ngày nay, "
            "luyện phát âm qua các đoạn văn về lịch sử thời trang, và viết về quan điểm của mình. "
            "Kết thúc bài học, bạn sẽ tự tin thảo luận về thời trang bằng tiếng Anh — "
            "và nhìn tủ quần áo của mình bằng con mắt hoàn toàn mới."
        )
    },
    "learningSessions": [
        # ── Session 1: Phần 1 (group1: silhouette, hemline, couture, textile, garment, tailor) ──
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về lịch sử thời trang qua các thập kỷ.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với Fashion Through the Decades — Thời Trang Qua Các Thập Kỷ! "
                            "Bạn có bao giờ nhìn một bức ảnh cũ và đoán ngay đó là thập niên nào chỉ nhờ trang phục? "
                            "Thời trang là một trong những cách nhanh nhất để đọc lịch sử — "
                            "mỗi thập kỷ có ngôn ngữ riêng qua quần áo.\n\n"
                            "Từ những chiếc corset bó sát của thế kỷ 19 đến phong cách streetwear thoải mái ngày nay, "
                            "thời trang luôn phản ánh xã hội: chiến tranh, giải phóng phụ nữ, công nghệ, "
                            "và cả những cuộc cách mạng văn hóa.\n\n"
                            "Trong phần đầu tiên, bạn sẽ học 6 từ vựng nền tảng: silhouette, hemline, couture, "
                            "textile, garment, và tailor. Đây là những từ bạn cần biết để nói về thời trang "
                            "bằng tiếng Anh một cách chuyên nghiệp. Hãy bắt đầu nhé!"
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Học từ vựng Phần 1",
                    "description": "Học chi tiết 6 từ: silhouette, hemline, couture, textile, garment, tailor.",
                    "data": {
                        "text": (
                            "Bây giờ chúng ta sẽ học chi tiết 6 từ vựng đầu tiên.\n\n"
                            "Từ đầu tiên là 'silhouette' — danh từ, nghĩa là hình dáng tổng thể của một bộ trang phục "
                            "khi nhìn từ xa, đường viền ngoài của cơ thể khi mặc quần áo. "
                            "Trong bài đọc, bạn sẽ thấy câu: 'The 1920s silhouette was straight and loose, "
                            "freeing women from the tight corsets of the previous century.' "
                            "Silhouette là từ đầu tiên mà nhà thiết kế nghĩ đến khi tạo ra một bộ sưu tập mới.\n\n"
                            "Từ thứ hai là 'hemline' — danh từ, nghĩa là đường viền dưới cùng của váy hoặc áo, "
                            "quyết định chiều dài trang phục. Hemline đã thay đổi rất nhiều qua các thập kỷ. "
                            "Trong bài đọc: 'When hemlines rose in the 1960s, it was not just about fashion — "
                            "it was a statement of independence.' Hemline ngắn hay dài thường phản ánh tinh thần thời đại.\n\n"
                            "Từ thứ ba là 'couture' — danh từ, nghĩa là thời trang cao cấp được may đo thủ công "
                            "với chất lượng và kỹ thuật tối ưu. Couture là đỉnh cao của ngành thời trang. "
                            "Trong bài đọc: 'Paris couture houses set the standard for elegance that the rest of the world followed.' "
                            "Couture khác với ready-to-wear ở chỗ mỗi bộ đồ được làm riêng cho một khách hàng.\n\n"
                            "Từ thứ tư là 'textile' — danh từ, nghĩa là vải, chất liệu dệt dùng để may quần áo. "
                            "Textile bao gồm lụa, cotton, len, polyester, và hàng trăm loại vải khác. "
                            "Trong bài đọc: 'New textiles like nylon and polyester in the 1950s made fashion affordable for everyone.' "
                            "Sự phát triển của textile technology đã thay đổi hoàn toàn ngành thời trang.\n\n"
                            "Từ thứ năm là 'garment' — danh từ, nghĩa là một món đồ quần áo, trang phục. "
                            "Garment là từ trang trọng hơn 'clothes' hoặc 'clothing'. "
                            "Trong bài đọc: 'Each garment in the collection told a story about the decade that inspired it.' "
                            "Garment thường dùng trong ngữ cảnh công nghiệp: garment factory, garment worker.\n\n"
                            "Từ cuối cùng trong phần này là 'tailor' — danh từ hoặc động từ. "
                            "Danh từ: người thợ may, chuyên cắt may quần áo theo số đo. "
                            "Động từ: may đo, điều chỉnh cho vừa vặn. "
                            "Trong bài đọc: 'A skilled tailor could transform a simple piece of cloth into a masterpiece "
                            "that fit the body like a second skin.' Tailor là nghề thủ công lâu đời nhất trong thời trang."
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng thời trang (Phần 1)",
                    "description": "Học 6 từ: silhouette, hemline, couture, textile, garment, tailor.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng thời trang (Phần 1)",
                    "description": "Học 6 từ: silhouette, hemline, couture, textile, garment, tailor.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Nền tảng thời trang (Phần 1)",
                    "description": "Luyện tập 6 từ: silhouette, hemline, couture, textile, garment, tailor.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Nền tảng thời trang (Phần 1)",
                    "description": "Luyện tập 6 từ: silhouette, hemline, couture, textile, garment, tailor.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "introAudio",
                    "title": "Ngữ pháp và cách dùng từ",
                    "description": "Hướng dẫn cách sử dụng 6 từ vựng trong câu và ngữ cảnh thực tế.",
                    "data": {
                        "text": (
                            "Trước khi đọc bài, hãy cùng tìm hiểu cách dùng 6 từ vựng này trong câu nhé.\n\n"
                            "'Silhouette' là danh từ đếm được — 'a silhouette', 'silhouettes'. "
                            "Thường đi với: create a silhouette, an hourglass silhouette, a slim silhouette. "
                            "Ví dụ: 'The A-line dress creates a flattering silhouette for most body types.' "
                            "Phát âm: /ˌsɪl.uˈet/ — lưu ý âm cuối giống tiếng Pháp.\n\n"
                            "'Hemline' là danh từ đếm được — 'a hemline', 'hemlines'. "
                            "Thường đi với: raise the hemline, lower the hemline, hemline length. "
                            "Ví dụ: 'Designers raised hemlines dramatically in the 1960s with the invention of the miniskirt.' "
                            "Hemline cũng dùng trong thành ngữ 'hemline index' — chỉ số hemline dự đoán kinh tế.\n\n"
                            "'Couture' là danh từ không đếm được khi nói chung, nhưng đếm được khi nói về một bộ sưu tập. "
                            "Thường đi với: haute couture, couture house, couture collection. "
                            "Ví dụ: 'Only a handful of fashion houses in Paris are officially recognized as couture.' "
                            "Phát âm: /kuˈtjʊr/.\n\n"
                            "'Textile' là danh từ đếm được — 'a textile', 'textiles'. "
                            "Thường đi với: textile industry, textile production, natural textiles, synthetic textiles. "
                            "Ví dụ: 'The textile industry employs millions of workers across Southeast Asia.' "
                            "Textile cũng dùng như tính từ: 'textile design', 'textile art'.\n\n"
                            "'Garment' là danh từ đếm được — 'a garment', 'garments'. "
                            "Thường đi với: garment factory, garment worker, garment industry. "
                            "Ví dụ: 'Fast fashion produces cheap garments that often end up in landfills within a year.' "
                            "Garment trang trọng hơn 'clothes' — dùng trong văn viết và ngữ cảnh chuyên ngành.\n\n"
                            "'Tailor' vừa là danh từ vừa là động từ. Danh từ: 'a tailor', 'tailors'. "
                            "Động từ: 'to tailor something' — may đo hoặc điều chỉnh cho phù hợp. "
                            "Ví dụ: 'She tailored the jacket to fit perfectly around the shoulders.' "
                            "Tính từ liên quan: 'tailored' — được may đo vừa vặn. 'A tailored suit' là bộ vest may đo."
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Khi quần áo kể chuyện lịch sử",
                    "description": "The 1920s silhouette was straight and loose, freeing women from tight corsets.",
                    "data": {
                        "text": (
                            "Fashion has always been a mirror of society. In the early 1900s, women wore long dresses "
                            "with tight waists and heavy fabrics. Every garment was designed to restrict movement "
                            "and signal social status. A skilled tailor could transform a simple piece of cloth "
                            "into a masterpiece that fit the body like a second skin.\n\n"
                            "Then came the 1920s. The silhouette changed completely. The 1920s silhouette was straight "
                            "and loose, freeing women from the tight corsets of the previous century. "
                            "Young women called 'flappers' cut their hair short, raised their hemlines above the knee, "
                            "and danced in jazz clubs until dawn. When hemlines rose in the 1960s, it was not just about "
                            "fashion — it was a statement of independence.\n\n"
                            "Paris couture houses set the standard for elegance that the rest of the world followed. "
                            "Designers like Coco Chanel and Christian Dior created looks that defined entire decades. "
                            "New textiles like nylon and polyester in the 1950s made fashion affordable for everyone. "
                            "For the first time, ordinary people could dress in styles that once belonged only to the wealthy.\n\n"
                            "Each garment in the collection told a story about the decade that inspired it. "
                            "The textile revolution continued through the century, bringing stretch fabrics, "
                            "waterproof materials, and eventually recycled fibers. "
                            "Fashion was no longer just about beauty — it was about technology, identity, and change."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Khi quần áo kể chuyện lịch sử",
                    "description": "Luyện đọc to đoạn văn về lịch sử thời trang từ đầu thế kỷ 20.",
                    "data": {
                        "text": (
                            "Fashion has always been a mirror of society. In the early 1900s, women wore long dresses "
                            "with tight waists and heavy fabrics. Every garment was designed to restrict movement "
                            "and signal social status. A skilled tailor could transform a simple piece of cloth "
                            "into a masterpiece that fit the body like a second skin.\n\n"
                            "Then came the 1920s. The silhouette changed completely. The 1920s silhouette was straight "
                            "and loose, freeing women from the tight corsets of the previous century. "
                            "Young women called 'flappers' cut their hair short, raised their hemlines above the knee, "
                            "and danced in jazz clubs until dawn. When hemlines rose in the 1960s, it was not just about "
                            "fashion — it was a statement of independence.\n\n"
                            "Paris couture houses set the standard for elegance that the rest of the world followed. "
                            "Designers like Coco Chanel and Christian Dior created looks that defined entire decades. "
                            "New textiles like nylon and polyester in the 1950s made fashion affordable for everyone. "
                            "For the first time, ordinary people could dress in styles that once belonged only to the wealthy.\n\n"
                            "Each garment in the collection told a story about the decade that inspired it. "
                            "The textile revolution continued through the century, bringing stretch fabrics, "
                            "waterproof materials, and eventually recycled fibers. "
                            "Fashion was no longer just about beauty — it was about technology, identity, and change."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Khi quần áo kể chuyện lịch sử",
                    "description": "Nghe và theo dõi đoạn văn về lịch sử thời trang từ đầu thế kỷ 20.",
                    "data": {
                        "text": (
                            "Fashion has always been a mirror of society. In the early 1900s, women wore long dresses "
                            "with tight waists and heavy fabrics. Every garment was designed to restrict movement "
                            "and signal social status. A skilled tailor could transform a simple piece of cloth "
                            "into a masterpiece that fit the body like a second skin.\n\n"
                            "Then came the 1920s. The silhouette changed completely. The 1920s silhouette was straight "
                            "and loose, freeing women from the tight corsets of the previous century. "
                            "Young women called 'flappers' cut their hair short, raised their hemlines above the knee, "
                            "and danced in jazz clubs until dawn. When hemlines rose in the 1960s, it was not just about "
                            "fashion — it was a statement of independence.\n\n"
                            "Paris couture houses set the standard for elegance that the rest of the world followed. "
                            "Designers like Coco Chanel and Christian Dior created looks that defined entire decades. "
                            "New textiles like nylon and polyester in the 1950s made fashion affordable for everyone. "
                            "For the first time, ordinary people could dress in styles that once belonged only to the wealthy.\n\n"
                            "Each garment in the collection told a story about the decade that inspired it. "
                            "The textile revolution continued through the century, bringing stretch fabrics, "
                            "waterproof materials, and eventually recycled fibers. "
                            "Fashion was no longer just about beauty — it was about technology, identity, and change."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng thời trang (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về silhouette, hemline và couture.",
                    "data": {
                        "vocabList": group1,
                        "items": [
                            {
                                "targetVocab": "silhouette",
                                "prompt": "Hãy dùng từ 'silhouette' để viết một câu về hình dáng tổng thể của một bộ trang phục. Ví dụ: The designer created a dramatic silhouette with wide shoulders and a narrow waist that reminded people of the 1940s."
                            },
                            {
                                "targetVocab": "hemline",
                                "prompt": "Hãy dùng từ 'hemline' để viết một câu về chiều dài váy hoặc xu hướng thời trang. Ví dụ: The hemline of her dress fell just below the knee, a classic length that never goes out of style."
                            },
                            {
                                "targetVocab": "couture",
                                "prompt": "Hãy dùng từ 'couture' để viết một câu về thời trang cao cấp hoặc may đo thủ công. Ví dụ: The couture gown took three hundred hours to complete, with every bead sewn on by hand."
                            },
                            {
                                "targetVocab": "textile",
                                "prompt": "Hãy dùng từ 'textile' để viết một câu về vải hoặc chất liệu trong thời trang. Ví dụ: Vietnamese textile traditions include silk weaving techniques that have been passed down for generations."
                            },
                            {
                                "targetVocab": "garment",
                                "prompt": "Hãy dùng từ 'garment' để viết một câu về một món đồ quần áo hoặc ngành may mặc. Ví dụ: The average garment is worn only seven times before being thrown away, which creates enormous waste."
                            },
                            {
                                "targetVocab": "tailor",
                                "prompt": "Hãy dùng từ 'tailor' để viết một câu về nghề may đo hoặc việc điều chỉnh quần áo. Ví dụ: My grandmother was a tailor who could look at someone once and know their exact measurements."
                            }
                        ]
                    }
                }
            ]
        },

        # ── Session 2: Phần 2 (group2: runway, vintage, accessory, embroidery, drape, ensemble) ──
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu Phần 2",
                    "description": "Ôn lại Phần 1 và giới thiệu 6 từ vựng mới về thế giới thời trang.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại với Phần 2 của Fashion Through the Decades! "
                            "Trong Phần 1, bạn đã học 6 từ nền tảng: silhouette, hemline, couture, textile, garment, và tailor. "
                            "Bạn đã biết rằng thời trang không chỉ là quần áo — nó là tấm gương phản chiếu xã hội, "
                            "từ sự giải phóng phụ nữ đến cách mạng công nghệ vải.\n\n"
                            "Trong phần này, chúng ta sẽ khám phá thêm 6 từ mới: "
                            "runway, vintage, accessory, embroidery, drape, và ensemble. "
                            "Những từ này sẽ giúp bạn nói về sàn diễn thời trang, phong cách retro, "
                            "và nghệ thuật tạo nên một bộ trang phục hoàn chỉnh."
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Học từ vựng Phần 2",
                    "description": "Học chi tiết 6 từ: runway, vintage, accessory, embroidery, drape, ensemble.",
                    "data": {
                        "text": (
                            "Hãy cùng học 6 từ vựng mới của Phần 2.\n\n"
                            "Từ đầu tiên là 'runway' — danh từ, nghĩa là sàn diễn thời trang, "
                            "đường đi dài và hẹp nơi người mẫu trình diễn quần áo. "
                            "Runway cũng có nghĩa là đường băng sân bay, nhưng trong thời trang, "
                            "nó là nơi các bộ sưu tập được giới thiệu lần đầu. "
                            "Trong bài đọc: 'The runway show in Milan featured models wearing recycled ocean plastic "
                            "transformed into elegant evening gowns.' Runway show là sự kiện quan trọng nhất "
                            "trong lịch thời trang mỗi mùa.\n\n"
                            "Từ thứ hai là 'vintage' — tính từ hoặc danh từ, nghĩa là đồ cũ có giá trị, "
                            "thường từ một thập kỷ trước, được đánh giá cao vì phong cách độc đáo. "
                            "Vintage khác với 'second-hand' ở chỗ vintage mang giá trị thẩm mỹ và lịch sử. "
                            "Trong bài đọc: 'Vintage clothing stores became treasure hunts where shoppers searched "
                            "for one-of-a-kind pieces from the 1970s and 1980s.' Vintage fashion đang rất phổ biến "
                            "trong giới trẻ Việt Nam.\n\n"
                            "Từ thứ ba là 'accessory' — danh từ, nghĩa là phụ kiện thời trang — "
                            "túi xách, giày, mũ, trang sức, khăn quàng, thắt lưng. "
                            "Accessories hoàn thiện một bộ trang phục và thể hiện cá tính. "
                            "Trong bài đọc: 'The right accessory could elevate a simple outfit into something extraordinary — "
                            "a silk scarf, a bold necklace, or a pair of statement earrings.' "
                            "Số nhiều: accessories. Thường dùng ở dạng số nhiều.\n\n"
                            "Từ thứ tư là 'embroidery' — danh từ, nghĩa là nghệ thuật thêu, "
                            "trang trí vải bằng chỉ màu tạo thành hoa văn hoặc hình ảnh. "
                            "Embroidery là một trong những kỹ thuật thủ công lâu đời nhất trong thời trang. "
                            "Trong bài đọc: 'Traditional Vietnamese embroidery found its way onto Paris runways, "
                            "proving that craft and couture could speak the same language.' "
                            "Embroidery đòi hỏi sự kiên nhẫn và kỹ năng tuyệt vời.\n\n"
                            "Từ thứ năm là 'drape' — động từ hoặc danh từ. "
                            "Động từ: để vải rủ tự nhiên trên cơ thể hoặc bề mặt. "
                            "Danh từ: cách vải rủ xuống, tạo nếp gấp mềm mại. "
                            "Trong bài đọc: 'She learned to drape fabric directly on the mannequin, "
                            "letting the material find its own shape.' "
                            "Drape là kỹ thuật quan trọng trong thiết kế thời trang — "
                            "cách vải rủ quyết định vẻ đẹp của trang phục.\n\n"
                            "Từ cuối cùng là 'ensemble' — danh từ, nghĩa là một bộ trang phục hoàn chỉnh "
                            "gồm nhiều món phối hợp với nhau. Ensemble cũng dùng trong âm nhạc "
                            "(nhóm nhạc), nhưng trong thời trang nó chỉ tổng thể một bộ đồ. "
                            "Trong bài đọc: 'Her ensemble — a tailored blazer, wide-leg trousers, "
                            "and a vintage brooch — captured the spirit of 1970s power dressing.' "
                            "Phát âm: /ɒnˈsɒm.bəl/ — từ gốc tiếng Pháp."
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Sàn diễn và phong cách (Phần 2)",
                    "description": "Học 6 từ: runway, vintage, accessory, embroidery, drape, ensemble.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Sàn diễn và phong cách (Phần 2)",
                    "description": "Học 6 từ: runway, vintage, accessory, embroidery, drape, ensemble.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Sàn diễn và phong cách (Phần 2)",
                    "description": "Luyện tập 6 từ: runway, vintage, accessory, embroidery, drape, ensemble.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Sàn diễn và phong cách (Phần 2)",
                    "description": "Luyện tập 6 từ: runway, vintage, accessory, embroidery, drape, ensemble.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "introAudio",
                    "title": "Ngữ pháp và cách dùng từ",
                    "description": "Hướng dẫn cách sử dụng 6 từ vựng Phần 2 trong câu và ngữ cảnh thực tế.",
                    "data": {
                        "text": (
                            "Hãy cùng tìm hiểu cách dùng 6 từ vựng Phần 2 trong câu.\n\n"
                            "'Runway' là danh từ đếm được — 'a runway', 'runways'. "
                            "Thường đi với: runway show, runway model, hit the runway, walk the runway. "
                            "Ví dụ: 'She walked the runway for the first time at age nineteen and immediately caught "
                            "the attention of every photographer in the room.' Runway cũng dùng như tính từ: "
                            "'runway fashion' — thời trang sàn diễn.\n\n"
                            "'Vintage' vừa là tính từ vừa là danh từ. Tính từ: 'a vintage dress', 'vintage style'. "
                            "Danh từ: 'She collects vintage.' Thường đi với: vintage shop, vintage clothing, "
                            "vintage look. Ví dụ: 'The vintage Chanel jacket she found at a flea market "
                            "was worth ten times what she paid for it.'\n\n"
                            "'Accessory' là danh từ đếm được — 'an accessory', 'accessories'. "
                            "Thường dùng ở số nhiều. Thường đi với: fashion accessories, hair accessories, "
                            "accessorize (động từ). Ví dụ: 'She accessorized her simple black dress "
                            "with gold earrings and a red clutch bag.'\n\n"
                            "'Embroidery' là danh từ không đếm được khi nói chung, "
                            "nhưng đếm được khi nói về một tác phẩm thêu cụ thể. "
                            "Thường đi với: hand embroidery, machine embroidery, embroidery thread. "
                            "Động từ: 'embroider'. Ví dụ: 'She embroidered tiny flowers along the collar of the shirt.'\n\n"
                            "'Drape' vừa là động từ vừa là danh từ. Động từ: 'to drape fabric over something'. "
                            "Danh từ: 'the drape of the silk'. Quá khứ: 'draped'. "
                            "Ví dụ: 'The drape of the cashmere shawl was so soft that it felt like water on her shoulders.' "
                            "Tính từ: 'draped' — 'a draped neckline'.\n\n"
                            "'Ensemble' là danh từ đếm được — 'an ensemble', 'ensembles'. "
                            "Thường đi với: a chic ensemble, a coordinated ensemble, a complete ensemble. "
                            "Ví dụ: 'His ensemble of a linen shirt, khaki trousers, and leather sandals "
                            "was perfect for the summer garden party.' Ensemble nhấn mạnh sự phối hợp tổng thể."
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Sàn diễn và đường phố",
                    "description": "The runway show in Milan featured models wearing recycled ocean plastic.",
                    "data": {
                        "text": (
                            "The relationship between the runway and the street has always been complicated. "
                            "For decades, fashion moved in one direction: designers created, models walked the runway, "
                            "magazines published, and ordinary people copied. But in the 1960s and 1970s, "
                            "something shifted. Young people on the streets of London and New York began creating "
                            "their own styles that designers then borrowed.\n\n"
                            "Vintage clothing stores became treasure hunts where shoppers searched for one-of-a-kind "
                            "pieces from the 1970s and 1980s. A vintage leather jacket or a pair of bell-bottom jeans "
                            "carried more personality than anything hanging in a department store. "
                            "The right accessory could elevate a simple outfit into something extraordinary — "
                            "a silk scarf, a bold necklace, or a pair of statement earrings.\n\n"
                            "Traditional Vietnamese embroidery found its way onto Paris runways, "
                            "proving that craft and couture could speak the same language. "
                            "The runway show in Milan featured models wearing recycled ocean plastic "
                            "transformed into elegant evening gowns. Fashion was becoming a conversation "
                            "between cultures, between past and present.\n\n"
                            "She learned to drape fabric directly on the mannequin, letting the material find its own shape. "
                            "Her ensemble — a tailored blazer, wide-leg trousers, and a vintage brooch — "
                            "captured the spirit of 1970s power dressing. "
                            "In fashion, nothing is ever truly new. Everything is a remix of what came before."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Sàn diễn và đường phố",
                    "description": "Luyện đọc to đoạn văn về mối quan hệ giữa runway và street fashion.",
                    "data": {
                        "text": (
                            "The relationship between the runway and the street has always been complicated. "
                            "For decades, fashion moved in one direction: designers created, models walked the runway, "
                            "magazines published, and ordinary people copied. But in the 1960s and 1970s, "
                            "something shifted. Young people on the streets of London and New York began creating "
                            "their own styles that designers then borrowed.\n\n"
                            "Vintage clothing stores became treasure hunts where shoppers searched for one-of-a-kind "
                            "pieces from the 1970s and 1980s. A vintage leather jacket or a pair of bell-bottom jeans "
                            "carried more personality than anything hanging in a department store. "
                            "The right accessory could elevate a simple outfit into something extraordinary — "
                            "a silk scarf, a bold necklace, or a pair of statement earrings.\n\n"
                            "Traditional Vietnamese embroidery found its way onto Paris runways, "
                            "proving that craft and couture could speak the same language. "
                            "The runway show in Milan featured models wearing recycled ocean plastic "
                            "transformed into elegant evening gowns. Fashion was becoming a conversation "
                            "between cultures, between past and present.\n\n"
                            "She learned to drape fabric directly on the mannequin, letting the material find its own shape. "
                            "Her ensemble — a tailored blazer, wide-leg trousers, and a vintage brooch — "
                            "captured the spirit of 1970s power dressing. "
                            "In fashion, nothing is ever truly new. Everything is a remix of what came before."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Sàn diễn và đường phố",
                    "description": "Nghe và theo dõi đoạn văn về mối quan hệ giữa runway và street fashion.",
                    "data": {
                        "text": (
                            "The relationship between the runway and the street has always been complicated. "
                            "For decades, fashion moved in one direction: designers created, models walked the runway, "
                            "magazines published, and ordinary people copied. But in the 1960s and 1970s, "
                            "something shifted. Young people on the streets of London and New York began creating "
                            "their own styles that designers then borrowed.\n\n"
                            "Vintage clothing stores became treasure hunts where shoppers searched for one-of-a-kind "
                            "pieces from the 1970s and 1980s. A vintage leather jacket or a pair of bell-bottom jeans "
                            "carried more personality than anything hanging in a department store. "
                            "The right accessory could elevate a simple outfit into something extraordinary — "
                            "a silk scarf, a bold necklace, or a pair of statement earrings.\n\n"
                            "Traditional Vietnamese embroidery found its way onto Paris runways, "
                            "proving that craft and couture could speak the same language. "
                            "The runway show in Milan featured models wearing recycled ocean plastic "
                            "transformed into elegant evening gowns. Fashion was becoming a conversation "
                            "between cultures, between past and present.\n\n"
                            "She learned to drape fabric directly on the mannequin, letting the material find its own shape. "
                            "Her ensemble — a tailored blazer, wide-leg trousers, and a vintage brooch — "
                            "captured the spirit of 1970s power dressing. "
                            "In fashion, nothing is ever truly new. Everything is a remix of what came before."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Sàn diễn và phong cách (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng về runway, vintage và embroidery.",
                    "data": {
                        "vocabList": group2,
                        "items": [
                            {
                                "targetVocab": "runway",
                                "prompt": "Hãy dùng từ 'runway' để viết một câu về sàn diễn thời trang hoặc buổi trình diễn. Ví dụ: The young designer's first runway show was a huge success, with every seat in the front row taken by fashion editors."
                            },
                            {
                                "targetVocab": "vintage",
                                "prompt": "Hãy dùng từ 'vintage' để viết một câu về đồ cũ có giá trị hoặc phong cách retro. Ví dụ: She found a vintage silk dress from the 1950s at a market in Hội An and wore it to her graduation."
                            },
                            {
                                "targetVocab": "accessory",
                                "prompt": "Hãy dùng từ 'accessory' để viết một câu về phụ kiện thời trang. Ví dụ: A simple leather belt can be the perfect accessory to pull together a casual outfit and make it look polished."
                            },
                            {
                                "targetVocab": "embroidery",
                                "prompt": "Hãy dùng từ 'embroidery' để viết một câu về nghệ thuật thêu hoặc trang trí vải. Ví dụ: The embroidery on the áo dài featured golden dragons and lotus flowers that took weeks to complete."
                            },
                            {
                                "targetVocab": "drape",
                                "prompt": "Hãy dùng từ 'drape' để viết một câu về cách vải rủ hoặc kỹ thuật thiết kế. Ví dụ: The designer draped the silk over the model's shoulder to create a flowing, elegant look for the evening gown."
                            },
                            {
                                "targetVocab": "ensemble",
                                "prompt": "Hãy dùng từ 'ensemble' để viết một câu về một bộ trang phục hoàn chỉnh. Ví dụ: His ensemble of a navy blazer, white shirt, and brown loafers was the definition of smart casual."
                            }
                        ]
                    }
                }
            ]
        },

        # ── Session 3: Phần 3 (group3: sustainable, haute, avant-garde, minimalist, iconic, revival) ──
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu Phần 3",
                    "description": "Ôn lại Phần 1-2 và giới thiệu 6 từ vựng về xu hướng thời trang hiện đại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với Phần 3 — phần cuối cùng trước khi ôn tập! "
                            "Bạn đã đi một chặng đường dài. Trong Phần 1, bạn học về silhouette, hemline, couture, "
                            "textile, garment, và tailor — những khái niệm nền tảng của thời trang. "
                            "Trong Phần 2, bạn khám phá runway, vintage, accessory, embroidery, drape, và ensemble — "
                            "thế giới sàn diễn và nghệ thuật phối đồ.\n\n"
                            "Bây giờ, trong Phần 3, chúng ta sẽ nói về thời trang đương đại với 6 từ vựng: "
                            "sustainable, haute, avant-garde, minimalist, iconic, và revival. "
                            "Đây là những từ bạn cần khi muốn thảo luận về tương lai của thời trang — "
                            "từ phong trào bền vững đến sự trở lại của các xu hướng cũ."
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Học từ vựng Phần 3",
                    "description": "Học chi tiết 6 từ: sustainable, haute, avant-garde, minimalist, iconic, revival.",
                    "data": {
                        "text": (
                            "Hãy cùng học 6 từ vựng cuối cùng.\n\n"
                            "Từ đầu tiên là 'sustainable' — tính từ, nghĩa là bền vững, "
                            "có thể duy trì lâu dài mà không gây hại cho môi trường. "
                            "Sustainable fashion là phong trào lớn nhất trong ngành thời trang hiện nay. "
                            "Trong bài đọc: 'Sustainable fashion asks a simple question: who made your clothes, "
                            "and what happened to the planet in the process?' "
                            "Sustainable đối lập với 'fast fashion' — thời trang nhanh, rẻ, và gây ô nhiễm.\n\n"
                            "Từ thứ hai là 'haute' — tính từ, nghĩa là cao cấp, thượng hạng. "
                            "Haute gần như luôn đi với 'couture' — haute couture nghĩa là thời trang cao cấp nhất, "
                            "may đo thủ công hoàn toàn. Trong bài đọc: 'Haute couture represents the pinnacle of fashion — "
                            "where art meets craftsmanship and every stitch is a deliberate choice.' "
                            "Phát âm: /əʊt/ — chữ 'h' câm, giống tiếng Pháp.\n\n"
                            "Từ thứ ba là 'avant-garde' — tính từ hoặc danh từ, nghĩa là tiên phong, "
                            "đi trước thời đại, thử nghiệm những ý tưởng mới mẻ và táo bạo. "
                            "Trong bài đọc: 'Avant-garde designers challenged every rule — they made dresses from metal, "
                            "shoes from glass, and coats that changed color in the rain.' "
                            "Avant-garde trong thời trang thường gây sốc nhưng mở đường cho xu hướng tương lai.\n\n"
                            "Từ thứ tư là 'minimalist' — tính từ hoặc danh từ, nghĩa là tối giản, "
                            "sử dụng ít chi tiết nhất có thể để đạt hiệu quả tối đa. "
                            "Trong bài đọc: 'The minimalist movement of the 1990s stripped fashion down to its essence — "
                            "clean lines, neutral colors, and zero decoration.' "
                            "Minimalist fashion nổi tiếng với các nhà thiết kế như Calvin Klein và Jil Sander.\n\n"
                            "Từ thứ năm là 'iconic' — tính từ, nghĩa là mang tính biểu tượng, "
                            "được nhiều người biết đến và nhớ đến. "
                            "Trong bài đọc: 'Audrey Hepburn's little black dress in Breakfast at Tiffany's "
                            "became one of the most iconic fashion moments in cinema history.' "
                            "Iconic thường đi với: iconic look, iconic design, iconic brand.\n\n"
                            "Từ cuối cùng là 'revival' — danh từ, nghĩa là sự hồi sinh, sự trở lại "
                            "của một xu hướng hoặc phong cách đã từng phổ biến. "
                            "Trong bài đọc: 'The 1990s revival brought back baggy jeans, platform shoes, "
                            "and choker necklaces — proving that fashion always comes full circle.' "
                            "Revival thường đi với: fashion revival, cultural revival, a revival of interest."
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thời trang đương đại (Phần 3)",
                    "description": "Học 6 từ: sustainable, haute, avant-garde, minimalist, iconic, revival.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thời trang đương đại (Phần 3)",
                    "description": "Học 6 từ: sustainable, haute, avant-garde, minimalist, iconic, revival.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Thời trang đương đại (Phần 3)",
                    "description": "Luyện tập 6 từ: sustainable, haute, avant-garde, minimalist, iconic, revival.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Thời trang đương đại (Phần 3)",
                    "description": "Luyện tập 6 từ: sustainable, haute, avant-garde, minimalist, iconic, revival.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "introAudio",
                    "title": "Ngữ pháp và cách dùng từ",
                    "description": "Hướng dẫn cách sử dụng 6 từ vựng Phần 3 trong câu và ngữ cảnh thực tế.",
                    "data": {
                        "text": (
                            "Hãy cùng tìm hiểu cách dùng 6 từ vựng Phần 3.\n\n"
                            "'Sustainable' là tính từ, thường đứng trước danh từ: 'sustainable fashion', "
                            "'sustainable materials', 'sustainable practices'. "
                            "Danh từ liên quan: 'sustainability'. Động từ: 'sustain'. "
                            "Ví dụ: 'The brand's commitment to sustainability includes using only organic cotton "
                            "and paying fair wages to every garment worker.'\n\n"
                            "'Haute' là tính từ tiếng Pháp, gần như luôn đi với 'couture'. "
                            "'Haute couture' là cụm từ cố định — bạn hiếm khi thấy 'haute' đứng một mình trong tiếng Anh. "
                            "Ví dụ: 'The haute couture collection featured hand-painted silk gowns "
                            "that took six months to create.' Lưu ý: 'haute cuisine' — ẩm thực cao cấp — "
                            "cũng dùng 'haute' theo cách tương tự.\n\n"
                            "'Avant-garde' vừa là tính từ vừa là danh từ. Tính từ: 'an avant-garde designer'. "
                            "Danh từ: 'the avant-garde' — nhóm người tiên phong. "
                            "Ví dụ: 'The avant-garde collection divided critics — some called it genius, "
                            "others called it unwearable.' Lưu ý dấu gạch ngang khi viết.\n\n"
                            "'Minimalist' vừa là tính từ vừa là danh từ. Tính từ: 'a minimalist wardrobe'. "
                            "Danh từ: 'She is a minimalist.' Danh từ liên quan: 'minimalism'. "
                            "Ví dụ: 'A minimalist wardrobe of ten versatile pieces can create more outfits "
                            "than a closet full of trendy clothes.'\n\n"
                            "'Iconic' là tính từ, thường đứng trước danh từ: 'an iconic dress', 'an iconic moment'. "
                            "Danh từ liên quan: 'icon' — biểu tượng. "
                            "Ví dụ: 'The red-soled shoes became iconic — you could recognize the brand "
                            "from across the room just by looking at the soles.'\n\n"
                            "'Revival' là danh từ đếm được — 'a revival', 'revivals'. "
                            "Động từ liên quan: 'revive'. Thường đi với: a revival of, fashion revival, "
                            "cultural revival. Ví dụ: 'The revival of 1970s fashion brought back flared trousers, "
                            "suede jackets, and oversized sunglasses.'"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tương lai của thời trang",
                    "description": "Sustainable fashion asks a simple question: who made your clothes?",
                    "data": {
                        "text": (
                            "The fashion industry is at a crossroads. On one side stands haute couture — "
                            "the world of handmade luxury where a single dress can cost more than a house. "
                            "Haute couture represents the pinnacle of fashion — where art meets craftsmanship "
                            "and every stitch is a deliberate choice. On the other side stands fast fashion — "
                            "cheap, disposable clothing produced in massive quantities.\n\n"
                            "Between these extremes, a new movement is growing. Sustainable fashion asks a simple question: "
                            "who made your clothes, and what happened to the planet in the process? "
                            "Young designers are finding ways to create beautiful garments without destroying the environment. "
                            "They use recycled textiles, natural dyes, and zero-waste cutting techniques.\n\n"
                            "Avant-garde designers challenged every rule — they made dresses from metal, "
                            "shoes from glass, and coats that changed color in the rain. "
                            "Meanwhile, the minimalist movement of the 1990s stripped fashion down to its essence — "
                            "clean lines, neutral colors, and zero decoration. "
                            "Both approaches pushed fashion forward in different directions.\n\n"
                            "Audrey Hepburn's little black dress in Breakfast at Tiffany's became one of the most "
                            "iconic fashion moments in cinema history. The 1990s revival brought back baggy jeans, "
                            "platform shoes, and choker necklaces — proving that fashion always comes full circle. "
                            "What was old becomes new. What was forgotten becomes desired. "
                            "The only constant in fashion is change itself."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Tương lai của thời trang",
                    "description": "Luyện đọc to đoạn văn về thời trang bền vững và xu hướng đương đại.",
                    "data": {
                        "text": (
                            "The fashion industry is at a crossroads. On one side stands haute couture — "
                            "the world of handmade luxury where a single dress can cost more than a house. "
                            "Haute couture represents the pinnacle of fashion — where art meets craftsmanship "
                            "and every stitch is a deliberate choice. On the other side stands fast fashion — "
                            "cheap, disposable clothing produced in massive quantities.\n\n"
                            "Between these extremes, a new movement is growing. Sustainable fashion asks a simple question: "
                            "who made your clothes, and what happened to the planet in the process? "
                            "Young designers are finding ways to create beautiful garments without destroying the environment. "
                            "They use recycled textiles, natural dyes, and zero-waste cutting techniques.\n\n"
                            "Avant-garde designers challenged every rule — they made dresses from metal, "
                            "shoes from glass, and coats that changed color in the rain. "
                            "Meanwhile, the minimalist movement of the 1990s stripped fashion down to its essence — "
                            "clean lines, neutral colors, and zero decoration. "
                            "Both approaches pushed fashion forward in different directions.\n\n"
                            "Audrey Hepburn's little black dress in Breakfast at Tiffany's became one of the most "
                            "iconic fashion moments in cinema history. The 1990s revival brought back baggy jeans, "
                            "platform shoes, and choker necklaces — proving that fashion always comes full circle. "
                            "What was old becomes new. What was forgotten becomes desired. "
                            "The only constant in fashion is change itself."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tương lai của thời trang",
                    "description": "Nghe và theo dõi đoạn văn về thời trang bền vững và xu hướng đương đại.",
                    "data": {
                        "text": (
                            "The fashion industry is at a crossroads. On one side stands haute couture — "
                            "the world of handmade luxury where a single dress can cost more than a house. "
                            "Haute couture represents the pinnacle of fashion — where art meets craftsmanship "
                            "and every stitch is a deliberate choice. On the other side stands fast fashion — "
                            "cheap, disposable clothing produced in massive quantities.\n\n"
                            "Between these extremes, a new movement is growing. Sustainable fashion asks a simple question: "
                            "who made your clothes, and what happened to the planet in the process? "
                            "Young designers are finding ways to create beautiful garments without destroying the environment. "
                            "They use recycled textiles, natural dyes, and zero-waste cutting techniques.\n\n"
                            "Avant-garde designers challenged every rule — they made dresses from metal, "
                            "shoes from glass, and coats that changed color in the rain. "
                            "Meanwhile, the minimalist movement of the 1990s stripped fashion down to its essence — "
                            "clean lines, neutral colors, and zero decoration. "
                            "Both approaches pushed fashion forward in different directions.\n\n"
                            "Audrey Hepburn's little black dress in Breakfast at Tiffany's became one of the most "
                            "iconic fashion moments in cinema history. The 1990s revival brought back baggy jeans, "
                            "platform shoes, and choker necklaces — proving that fashion always comes full circle. "
                            "What was old becomes new. What was forgotten becomes desired. "
                            "The only constant in fashion is change itself."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thời trang đương đại (Phần 3)",
                    "description": "Viết câu sử dụng 6 từ vựng về sustainable fashion, avant-garde và iconic.",
                    "data": {
                        "vocabList": group3,
                        "items": [
                            {
                                "targetVocab": "sustainable",
                                "prompt": "Hãy dùng từ 'sustainable' để viết một câu về thời trang bền vững hoặc bảo vệ môi trường. Ví dụ: Many young Vietnamese designers are building sustainable brands that use locally sourced fabrics and traditional weaving methods."
                            },
                            {
                                "targetVocab": "haute",
                                "prompt": "Hãy dùng từ 'haute' để viết một câu về thời trang cao cấp hoặc xa xỉ. Ví dụ: The haute couture show in Paris displayed gowns so elaborate that each one required over five hundred hours of handwork."
                            },
                            {
                                "targetVocab": "avant-garde",
                                "prompt": "Hãy dùng từ 'avant-garde' để viết một câu về thiết kế tiên phong hoặc sáng tạo táo bạo. Ví dụ: The avant-garde collection featured jackets made entirely from recycled newspaper, blurring the line between fashion and sculpture."
                            },
                            {
                                "targetVocab": "minimalist",
                                "prompt": "Hãy dùng từ 'minimalist' để viết một câu về phong cách tối giản trong thời trang hoặc cuộc sống. Ví dụ: Her minimalist wardrobe contained only thirty items, but she never ran out of outfit combinations."
                            },
                            {
                                "targetVocab": "iconic",
                                "prompt": "Hãy dùng từ 'iconic' để viết một câu về một thiết kế hoặc khoảnh khắc thời trang nổi tiếng. Ví dụ: The iconic red dress that Marilyn Monroe wore in that photograph has been copied by designers around the world for decades."
                            },
                            {
                                "targetVocab": "revival",
                                "prompt": "Hãy dùng từ 'revival' để viết một câu về sự trở lại của một xu hướng thời trang. Ví dụ: The revival of traditional áo dài designs among young people shows that Vietnamese fashion heritage is alive and evolving."
                            }
                        ]
                    }
                }
            ]
        },

        # ── Session 4: Ôn tập (all 18 words) ──
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Hãy ôn tập lại tất cả.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng của Fashion Through the Decades. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong Phần 1, bạn học 6 từ nền tảng: silhouette, hemline, couture, textile, garment, và tailor. "
                            "Bạn đã đọc về cách thời trang thay đổi từ đầu thế kỷ 20 — từ corset bó sát "
                            "đến silhouette phóng khoáng của thập niên 20, và cách textile mới làm thời trang "
                            "trở nên phổ biến hơn.\n\n"
                            "Trong Phần 2, bạn khám phá thế giới sàn diễn và phong cách với 6 từ: "
                            "runway, vintage, accessory, embroidery, drape, và ensemble. "
                            "Bạn đã đọc về mối quan hệ phức tạp giữa runway fashion và street style, "
                            "và cách embroidery truyền thống Việt Nam xuất hiện trên sàn diễn Paris.\n\n"
                            "Trong Phần 3, bạn nâng tầm với 6 từ về thời trang đương đại: "
                            "sustainable, haute, avant-garde, minimalist, iconic, và revival. "
                            "Bạn đã đọc về cuộc đối đầu giữa haute couture và fast fashion, "
                            "và phong trào sustainable fashion đang thay đổi ngành công nghiệp.\n\n"
                            "Bây giờ, hãy ôn tập tất cả 18 từ vựng qua flashcards, bài tập, và viết câu. "
                            "Sau phần ôn tập này, bạn sẽ đọc một bài viết tổng hợp về hành trình "
                            "của một nhà thiết kế trẻ Việt Nam. Sẵn sàng chưa?"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về thời trang, phong cách và xu hướng qua các thập kỷ.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về thời trang, phong cách và xu hướng qua các thập kỷ.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về thời trang, phong cách và xu hướng qua các thập kỷ.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về thời trang, phong cách và xu hướng qua các thập kỷ.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng về thời trang qua các thập kỷ.",
                    "data": {
                        "vocabList": all_words,
                        "items": [
                            {
                                "targetVocab": "silhouette",
                                "prompt": "Hãy dùng từ 'silhouette' để viết một câu về hình dáng trang phục bạn thích. Ví dụ: The oversized silhouette of the 1980s power suit made women look confident and commanding in the workplace."
                            },
                            {
                                "targetVocab": "hemline",
                                "prompt": "Hãy dùng từ 'hemline' để viết một câu về xu hướng chiều dài váy. Ví dụ: Fashion historians say that hemlines tend to rise during times of economic prosperity and fall during recessions."
                            },
                            {
                                "targetVocab": "couture",
                                "prompt": "Hãy dùng từ 'couture' để viết một câu về thời trang cao cấp. Ví dụ: The couture wedding dress was so delicate that the bride was afraid to sit down during the entire ceremony."
                            },
                            {
                                "targetVocab": "textile",
                                "prompt": "Hãy dùng từ 'textile' để viết một câu về vải hoặc ngành dệt may. Ví dụ: Vietnam's textile industry has grown rapidly, making the country one of the largest garment exporters in the world."
                            },
                            {
                                "targetVocab": "garment",
                                "prompt": "Hãy dùng từ 'garment' để viết một câu về quần áo hoặc ngành may mặc. Ví dụ: The label inside the garment showed it had traveled through four countries before reaching the store shelf."
                            },
                            {
                                "targetVocab": "tailor",
                                "prompt": "Hãy dùng từ 'tailor' để viết một câu về nghề may đo hoặc sự vừa vặn. Ví dụ: A good tailor can make an inexpensive suit look like it costs a fortune just by adjusting the fit."
                            },
                            {
                                "targetVocab": "runway",
                                "prompt": "Hãy dùng từ 'runway' để viết một câu về sàn diễn thời trang. Ví dụ: What appears on the runway in September often shows up in regular clothing stores by the following spring."
                            },
                            {
                                "targetVocab": "vintage",
                                "prompt": "Hãy dùng từ 'vintage' để viết một câu về đồ cũ có giá trị. Ví dụ: The vintage denim jacket she inherited from her mother became the most complimented piece in her wardrobe."
                            },
                            {
                                "targetVocab": "accessory",
                                "prompt": "Hãy dùng từ 'accessory' để viết một câu về phụ kiện thời trang. Ví dụ: In Vietnamese fashion, the nón lá is more than an accessory — it is a cultural symbol recognized around the world."
                            },
                            {
                                "targetVocab": "embroidery",
                                "prompt": "Hãy dùng từ 'embroidery' để viết một câu về nghệ thuật thêu. Ví dụ: The embroidery on the traditional wedding áo dài depicted a phoenix and dragon, symbols of harmony and prosperity."
                            },
                            {
                                "targetVocab": "drape",
                                "prompt": "Hãy dùng từ 'drape' để viết một câu về cách vải rủ hoặc tạo dáng. Ví dụ: The way the fabric draped over her shoulders gave the simple dress an air of effortless elegance."
                            },
                            {
                                "targetVocab": "ensemble",
                                "prompt": "Hãy dùng từ 'ensemble' để viết một câu về một bộ trang phục phối hợp. Ví dụ: She put together an ensemble of a white blouse, high-waisted trousers, and a straw hat for the weekend trip to Đà Lạt."
                            },
                            {
                                "targetVocab": "sustainable",
                                "prompt": "Hãy dùng từ 'sustainable' để viết một câu về thời trang bền vững. Ví dụ: Buying fewer but higher-quality clothes is one of the easiest ways to support sustainable fashion."
                            },
                            {
                                "targetVocab": "haute",
                                "prompt": "Hãy dùng từ 'haute' để viết một câu về thời trang xa xỉ. Ví dụ: The haute couture industry in Paris employs thousands of skilled artisans who specialize in techniques like beading and featherwork."
                            },
                            {
                                "targetVocab": "avant-garde",
                                "prompt": "Hãy dùng từ 'avant-garde' để viết một câu về thiết kế tiên phong. Ví dụ: The avant-garde fashion show used drones instead of models to display the clothing, creating a futuristic spectacle."
                            },
                            {
                                "targetVocab": "minimalist",
                                "prompt": "Hãy dùng từ 'minimalist' để viết một câu về phong cách tối giản. Ví dụ: The minimalist approach to fashion taught her that owning less actually gave her more freedom to express herself."
                            },
                            {
                                "targetVocab": "iconic",
                                "prompt": "Hãy dùng từ 'iconic' để viết một câu về một biểu tượng thời trang. Ví dụ: The white áo dài has become an iconic image of Vietnamese schoolgirls that visitors from around the world recognize instantly."
                            },
                            {
                                "targetVocab": "revival",
                                "prompt": "Hãy dùng từ 'revival' để viết một câu về sự trở lại của một xu hướng. Ví dụ: The revival of handmade crafts in fashion shows that consumers are tired of mass-produced clothing and want something with a story."
                            }
                        ]
                    }
                }
            ]
        },

        # ── Session 5: Đọc toàn bài (final reading, all 18 words) ──
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc cuối",
                    "description": "Giới thiệu bài đọc tổng hợp với tất cả 18 từ vựng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của Fashion Through the Decades! "
                            "Đây là khoảnh khắc mà mọi thứ bạn đã học được kết nối lại.\n\n"
                            "Trong bài đọc tổng hợp này, bạn sẽ gặp lại tất cả 18 từ vựng: "
                            "silhouette, hemline, couture, textile, garment, tailor, runway, vintage, "
                            "accessory, embroidery, drape, ensemble, sustainable, haute, avant-garde, "
                            "minimalist, iconic, và revival. Bài đọc kể câu chuyện về Mai — "
                            "một nhà thiết kế trẻ Việt Nam và hành trình của cô ấy "
                            "từ xưởng may nhỏ ở Hội An đến sàn diễn quốc tế.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ vựng được sử dụng trong ngữ cảnh, "
                            "và thưởng thức câu chuyện. Sau bài đọc, bạn sẽ viết một đoạn văn "
                            "chia sẻ suy nghĩ của mình về thời trang và bản sắc. Bắt đầu nhé!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Sợi chỉ nối quá khứ và tương lai",
                    "description": "A complete article about Mai, a young Vietnamese designer bridging tradition and innovation.",
                    "data": {
                        "text": (
                            "Mai grew up watching her grandmother work. The old woman sat at a wooden table "
                            "in their house in Hội An, her fingers moving a needle through silk with the patience "
                            "of someone who had been doing this for sixty years. The embroidery was exquisite — "
                            "tiny lotus flowers, curving rivers, birds in flight. Each garment that left "
                            "her grandmother's hands was a piece of living history.\n\n"
                            "Mai's grandmother was a tailor. Not the kind who worked in a factory, "
                            "but the kind who could look at a person and know exactly how fabric should fall "
                            "across their shoulders. She could tailor an áo dài so perfectly that it moved "
                            "with the wearer like water. She taught Mai that clothing was never just clothing — "
                            "it was a conversation between the maker and the wearer.\n\n"
                            "At fashion school in Ho Chi Minh City, Mai discovered a different world. "
                            "She studied the history of silhouettes — how the hourglass shape of the 1950s "
                            "gave way to the straight lines of the 1960s, how hemlines rose and fell "
                            "with the mood of each decade. She learned about couture — the art of creating "
                            "one-of-a-kind garments by hand, where every stitch carried intention. "
                            "She studied textiles — silk, cotton, linen, and the new synthetic fabrics "
                            "that were changing what clothing could do.\n\n"
                            "Her first collection was a disaster. She tried to copy what she saw on international runways — "
                            "sharp angles, dark colors, aggressive silhouettes. The runway show was technically perfect, "
                            "but something was missing. A professor told her: 'You are wearing someone else's voice. "
                            "Find your own.'\n\n"
                            "Mai went home to Hội An. She spent a month sitting with her grandmother, "
                            "learning to drape fabric the old way — not on a mannequin, but on a living body, "
                            "feeling how the textile responded to movement. She studied vintage áo dài patterns "
                            "from the 1960s and 1970s, when Vietnamese fashion had its own golden age. "
                            "She collected accessories from local markets — handmade silver brooches, "
                            "woven bamboo clutches, silk scarves dyed with natural indigo.\n\n"
                            "When Mai returned to the city, her designs had changed completely. "
                            "Her new collection combined her grandmother's embroidery techniques "
                            "with modern minimalist cuts. The ensemble that opened her second runway show — "
                            "a flowing white top with hand-embroidered sleeves paired with wide-leg trousers — "
                            "made the audience gasp. The drape of the fabric was so natural "
                            "that the model seemed to float down the runway.\n\n"
                            "A fashion journalist called the collection 'a quiet revolution.' "
                            "It was not avant-garde in the shocking sense — there were no dresses made of metal "
                            "or shoes made of glass. Instead, it was avant-garde in its refusal to choose "
                            "between tradition and innovation. Mai proved that you could honor the past "
                            "while designing for the future.\n\n"
                            "The collection caught the attention of a haute couture house in Paris. "
                            "They invited Mai to present a capsule collection at their next show. "
                            "For the first time, traditional Vietnamese textile techniques appeared "
                            "alongside French haute couture — and they held their own. "
                            "The iconic image from that show was a model wearing a silk gown "
                            "with Hội An embroidery cascading down the back like a waterfall.\n\n"
                            "But Mai's greatest pride was not the Paris show. It was what she built at home. "
                            "She started a sustainable fashion workshop in Hội An, employing local women "
                            "who had learned embroidery and tailoring from their mothers and grandmothers. "
                            "Every garment was made from sustainable textiles — organic cotton, recycled silk, "
                            "and naturally dyed fabrics. The workshop became a model for how fashion "
                            "could support communities instead of exploiting them.\n\n"
                            "Today, Mai's brand is part of a larger revival — a movement of young Vietnamese designers "
                            "who are rediscovering their heritage and sharing it with the world. "
                            "They are proving that fashion does not have to choose between beautiful and responsible, "
                            "between local and global, between vintage soul and modern vision.\n\n"
                            "When asked about her grandmother, Mai smiles. 'She never walked a runway,' Mai says. "
                            "'She never heard the word couture. But every accessory she made, every hem she stitched, "
                            "every garment she tailored — that was haute couture. She just did not know it had a name.'"
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Sợi chỉ nối quá khứ và tương lai",
                    "description": "Luyện đọc to bài đọc tổng hợp về hành trình của Mai.",
                    "data": {
                        "text": (
                            "Mai grew up watching her grandmother work. The old woman sat at a wooden table "
                            "in their house in Hội An, her fingers moving a needle through silk with the patience "
                            "of someone who had been doing this for sixty years. The embroidery was exquisite — "
                            "tiny lotus flowers, curving rivers, birds in flight. Each garment that left "
                            "her grandmother's hands was a piece of living history.\n\n"
                            "Mai's grandmother was a tailor. Not the kind who worked in a factory, "
                            "but the kind who could look at a person and know exactly how fabric should fall "
                            "across their shoulders. She could tailor an áo dài so perfectly that it moved "
                            "with the wearer like water. She taught Mai that clothing was never just clothing — "
                            "it was a conversation between the maker and the wearer.\n\n"
                            "At fashion school in Ho Chi Minh City, Mai discovered a different world. "
                            "She studied the history of silhouettes — how the hourglass shape of the 1950s "
                            "gave way to the straight lines of the 1960s, how hemlines rose and fell "
                            "with the mood of each decade. She learned about couture — the art of creating "
                            "one-of-a-kind garments by hand, where every stitch carried intention. "
                            "She studied textiles — silk, cotton, linen, and the new synthetic fabrics "
                            "that were changing what clothing could do.\n\n"
                            "Her first collection was a disaster. She tried to copy what she saw on international runways — "
                            "sharp angles, dark colors, aggressive silhouettes. The runway show was technically perfect, "
                            "but something was missing. A professor told her: 'You are wearing someone else's voice. "
                            "Find your own.'\n\n"
                            "Mai went home to Hội An. She spent a month sitting with her grandmother, "
                            "learning to drape fabric the old way — not on a mannequin, but on a living body, "
                            "feeling how the textile responded to movement. She studied vintage áo dài patterns "
                            "from the 1960s and 1970s, when Vietnamese fashion had its own golden age. "
                            "She collected accessories from local markets — handmade silver brooches, "
                            "woven bamboo clutches, silk scarves dyed with natural indigo.\n\n"
                            "When Mai returned to the city, her designs had changed completely. "
                            "Her new collection combined her grandmother's embroidery techniques "
                            "with modern minimalist cuts. The ensemble that opened her second runway show — "
                            "a flowing white top with hand-embroidered sleeves paired with wide-leg trousers — "
                            "made the audience gasp. The drape of the fabric was so natural "
                            "that the model seemed to float down the runway.\n\n"
                            "A fashion journalist called the collection 'a quiet revolution.' "
                            "It was not avant-garde in the shocking sense — there were no dresses made of metal "
                            "or shoes made of glass. Instead, it was avant-garde in its refusal to choose "
                            "between tradition and innovation. Mai proved that you could honor the past "
                            "while designing for the future.\n\n"
                            "The collection caught the attention of a haute couture house in Paris. "
                            "They invited Mai to present a capsule collection at their next show. "
                            "For the first time, traditional Vietnamese textile techniques appeared "
                            "alongside French haute couture — and they held their own. "
                            "The iconic image from that show was a model wearing a silk gown "
                            "with Hội An embroidery cascading down the back like a waterfall.\n\n"
                            "But Mai's greatest pride was not the Paris show. It was what she built at home. "
                            "She started a sustainable fashion workshop in Hội An, employing local women "
                            "who had learned embroidery and tailoring from their mothers and grandmothers. "
                            "Every garment was made from sustainable textiles — organic cotton, recycled silk, "
                            "and naturally dyed fabrics. The workshop became a model for how fashion "
                            "could support communities instead of exploiting them.\n\n"
                            "Today, Mai's brand is part of a larger revival — a movement of young Vietnamese designers "
                            "who are rediscovering their heritage and sharing it with the world. "
                            "They are proving that fashion does not have to choose between beautiful and responsible, "
                            "between local and global, between vintage soul and modern vision.\n\n"
                            "When asked about her grandmother, Mai smiles. 'She never walked a runway,' Mai says. "
                            "'She never heard the word couture. But every accessory she made, every hem she stitched, "
                            "every garment she tailored — that was haute couture. She just did not know it had a name.'"
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Sợi chỉ nối quá khứ và tương lai",
                    "description": "Nghe và theo dõi bài đọc tổng hợp về hành trình của Mai.",
                    "data": {
                        "text": (
                            "Mai grew up watching her grandmother work. The old woman sat at a wooden table "
                            "in their house in Hội An, her fingers moving a needle through silk with the patience "
                            "of someone who had been doing this for sixty years. The embroidery was exquisite — "
                            "tiny lotus flowers, curving rivers, birds in flight. Each garment that left "
                            "her grandmother's hands was a piece of living history.\n\n"
                            "Mai's grandmother was a tailor. Not the kind who worked in a factory, "
                            "but the kind who could look at a person and know exactly how fabric should fall "
                            "across their shoulders. She could tailor an áo dài so perfectly that it moved "
                            "with the wearer like water. She taught Mai that clothing was never just clothing — "
                            "it was a conversation between the maker and the wearer.\n\n"
                            "At fashion school in Ho Chi Minh City, Mai discovered a different world. "
                            "She studied the history of silhouettes — how the hourglass shape of the 1950s "
                            "gave way to the straight lines of the 1960s, how hemlines rose and fell "
                            "with the mood of each decade. She learned about couture — the art of creating "
                            "one-of-a-kind garments by hand, where every stitch carried intention. "
                            "She studied textiles — silk, cotton, linen, and the new synthetic fabrics "
                            "that were changing what clothing could do.\n\n"
                            "Her first collection was a disaster. She tried to copy what she saw on international runways — "
                            "sharp angles, dark colors, aggressive silhouettes. The runway show was technically perfect, "
                            "but something was missing. A professor told her: 'You are wearing someone else's voice. "
                            "Find your own.'\n\n"
                            "Mai went home to Hội An. She spent a month sitting with her grandmother, "
                            "learning to drape fabric the old way — not on a mannequin, but on a living body, "
                            "feeling how the textile responded to movement. She studied vintage áo dài patterns "
                            "from the 1960s and 1970s, when Vietnamese fashion had its own golden age. "
                            "She collected accessories from local markets — handmade silver brooches, "
                            "woven bamboo clutches, silk scarves dyed with natural indigo.\n\n"
                            "When Mai returned to the city, her designs had changed completely. "
                            "Her new collection combined her grandmother's embroidery techniques "
                            "with modern minimalist cuts. The ensemble that opened her second runway show — "
                            "a flowing white top with hand-embroidered sleeves paired with wide-leg trousers — "
                            "made the audience gasp. The drape of the fabric was so natural "
                            "that the model seemed to float down the runway.\n\n"
                            "A fashion journalist called the collection 'a quiet revolution.' "
                            "It was not avant-garde in the shocking sense — there were no dresses made of metal "
                            "or shoes made of glass. Instead, it was avant-garde in its refusal to choose "
                            "between tradition and innovation. Mai proved that you could honor the past "
                            "while designing for the future.\n\n"
                            "The collection caught the attention of a haute couture house in Paris. "
                            "They invited Mai to present a capsule collection at their next show. "
                            "For the first time, traditional Vietnamese textile techniques appeared "
                            "alongside French haute couture — and they held their own. "
                            "The iconic image from that show was a model wearing a silk gown "
                            "with Hội An embroidery cascading down the back like a waterfall.\n\n"
                            "But Mai's greatest pride was not the Paris show. It was what she built at home. "
                            "She started a sustainable fashion workshop in Hội An, employing local women "
                            "who had learned embroidery and tailoring from their mothers and grandmothers. "
                            "Every garment was made from sustainable textiles — organic cotton, recycled silk, "
                            "and naturally dyed fabrics. The workshop became a model for how fashion "
                            "could support communities instead of exploiting them.\n\n"
                            "Today, Mai's brand is part of a larger revival — a movement of young Vietnamese designers "
                            "who are rediscovering their heritage and sharing it with the world. "
                            "They are proving that fashion does not have to choose between beautiful and responsible, "
                            "between local and global, between vintage soul and modern vision.\n\n"
                            "When asked about her grandmother, Mai smiles. 'She never walked a runway,' Mai says. "
                            "'She never heard the word couture. But every accessory she made, every hem she stitched, "
                            "every garment she tailored — that was haute couture. She just did not know it had a name.'"
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết đoạn văn: Thời trang và bản sắc",
                    "description": "Viết đoạn văn sử dụng từ vựng về thời trang, bản sắc văn hóa và sự bền vững.",
                    "data": {
                        "vocabList": all_words,
                        "instructions": (
                            "Viết một đoạn văn ngắn (80-120 từ) bằng tiếng Anh về chủ đề thời trang "
                            "và bản sắc văn hóa. Hãy sử dụng ít nhất 6 từ vựng từ danh sách. "
                            "Bạn có thể viết về phong cách cá nhân, về thời trang Việt Nam, "
                            "hoặc về mối quan hệ giữa truyền thống và hiện đại trong thời trang."
                        ),
                        "prompts": [
                            "Trong bài đọc, Mai kết hợp embroidery truyền thống của bà ngoại với thiết kế minimalist hiện đại. Bạn nghĩ thời trang truyền thống Việt Nam — như áo dài — nên được giữ nguyên hay nên được cải tiến cho phù hợp với cuộc sống hiện đại? Hãy dùng ví dụ cụ thể và từ vựng từ bài học.",
                            "Bài đọc nêu lên sự đối lập giữa haute couture và fast fashion. Sustainable fashion đang cố gắng tìm con đường giữa hai thái cực này. Theo bạn, người tiêu dùng có trách nhiệm gì trong việc thay đổi ngành thời trang? Bạn sẵn sàng thay đổi thói quen mua sắm không?",
                            "Mai được giáo sư khuyên: 'Bạn đang mặc giọng nói của người khác. Hãy tìm giọng nói của mình.' Theo bạn, phong cách thời trang cá nhân nói gì về con người bạn? Bạn chọn quần áo dựa trên xu hướng runway hay dựa trên cảm xúc và giá trị cá nhân?"
                        ]
                    }
                },
                # Farewell tone: warm_accountability
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần thử thách ấm áp.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành Fashion Through the Decades — và bây giờ là lúc đặt câu hỏi thật: "
                            "bạn sẽ làm gì với những gì vừa học?\n\n"
                            "Hãy cùng ôn lại 6 từ vựng quan trọng nhất — và lần này, "
                            "tôi muốn bạn nghĩ về cách dùng chúng trong cuộc sống thật.\n\n"
                            "'Sustainable' — bền vững, có thể duy trì lâu dài mà không gây hại. "
                            "Ví dụ mới: The next time you pick up a cheap shirt at the mall, ask yourself: "
                            "is this sustainable, or will it end up in a landfill within six months? "
                            "Thử thách cho bạn: lần tới khi mua quần áo, hãy kiểm tra nhãn mác "
                            "và tìm hiểu nơi sản xuất.\n\n"
                            "'Couture' — thời trang cao cấp, may đo thủ công. "
                            "Ví dụ mới: You do not need a couture budget to appreciate couture craftsmanship — "
                            "visit a local tailor in Hội An and watch how they transform flat fabric into a three-dimensional garment. "
                            "Thử thách: hãy tìm một thợ may địa phương và hỏi họ về nghề.\n\n"
                            "'Embroidery' — nghệ thuật thêu, trang trí vải bằng chỉ màu. "
                            "Ví dụ mới: Vietnamese embroidery is not a dying art — it is a living tradition "
                            "that young designers like Mai are bringing to the world stage. "
                            "Thử thách: lần tới khi thấy một sản phẩm thêu tay, hãy dừng lại "
                            "và tưởng tượng bao nhiêu giờ đã được đặt vào từng đường kim.\n\n"
                            "'Iconic' — mang tính biểu tượng, được nhiều người nhớ đến. "
                            "Ví dụ mới: Every culture has its iconic garments — the Japanese kimono, "
                            "the Indian sari, the Vietnamese áo dài. These are not just clothes; "
                            "they are stories woven into fabric. "
                            "Thử thách: hãy mô tả một bộ trang phục iconic bằng tiếng Anh cho một người bạn nước ngoài.\n\n"
                            "'Revival' — sự hồi sinh, sự trở lại của một xu hướng. "
                            "Ví dụ mới: The revival of interest in traditional crafts shows that people are hungry "
                            "for authenticity in a world of mass production. "
                            "Thử thách: hãy tìm một món đồ vintage hoặc truyền thống trong tủ quần áo "
                            "của gia đình bạn và tìm hiểu câu chuyện đằng sau nó.\n\n"
                            "'Ensemble' — bộ trang phục hoàn chỉnh gồm nhiều món phối hợp. "
                            "Ví dụ mới: Tomorrow morning, instead of grabbing the first thing you see, "
                            "try putting together a deliberate ensemble — choose each piece with intention, "
                            "like a designer preparing for a runway show. "
                            "Thử thách: hãy phối một bộ đồ mà bạn tự hào và mô tả nó bằng tiếng Anh.\n\n"
                            "Bạn bắt đầu bài học này với ý tưởng rằng thời trang chỉ là quần áo. "
                            "Bây giờ bạn biết nó là lịch sử, là văn hóa, là bản sắc, là trách nhiệm. "
                            "18 từ vựng bạn vừa học không chỉ giúp bạn nói về thời trang bằng tiếng Anh — "
                            "chúng giúp bạn nhìn thế giới xung quanh với đôi mắt tinh tế hơn.\n\n"
                            "Vậy đây là thử thách cuối cùng: tuần này, hãy dùng ít nhất 3 từ vựng "
                            "từ bài học trong một cuộc trò chuyện thật — với bạn bè, trên mạng xã hội, "
                            "hoặc trong nhật ký tiếng Anh của bạn. Ngôn ngữ chỉ sống khi bạn dùng nó.\n\n"
                            "Cảm ơn bạn đã đồng hành. Hẹn gặp lại ở bài học tiếp theo — "
                            "và nhớ rằng: mỗi ngày bạn chọn mặc gì, bạn đang viết một trang trong cuốn nhật ký "
                            "của chính mình. Hãy viết nó thật đẹp!"
                        )
                    }
                }
            ]
        }
    ]
}

# ── Validate and upload ──

validate_balanced_skills_standard(content)
validate_content_type_tags(content)
validate_bilingual_prompts(content, "intermediate")
print("✅ Validation passed")

token = get_firebase_id_token(UID)
res = requests.post(f"{API_BASE}/curriculum/create", json={
    "firebaseIdToken": token,
    "language": "en",
    "userLanguage": "vi",
    "content": json.dumps(content)
})
res.raise_for_status()
data = res.json()
curriculum_id = data["id"]
print(f"✅ Created curriculum: {curriculum_id}")
print(f"   Title: {content['title']}")

# Duplicate check
token = get_firebase_id_token(UID)
dup_res = requests.post(f"{API_BASE}/curriculum/list", json={
    "firebaseIdToken": token
})
dup_res.raise_for_status()
all_currs = dup_res.json()
dupes = [c for c in all_currs if c.get("content", {}).get("title") == content["title"]]
if len(dupes) > 1:
    print(f"⚠️  Found {len(dupes)} duplicates! Keeping earliest, deleting extras.")
    dupes.sort(key=lambda c: c.get("createdAt", ""))
    for d in dupes[1:]:
        del_token = get_firebase_id_token(UID)
        requests.post(f"{API_BASE}/curriculum/delete", json={
            "firebaseIdToken": del_token,
            "id": d["id"]
        })
        print(f"   Deleted duplicate: {d['id']}")
else:
    print("✅ No duplicates found")
