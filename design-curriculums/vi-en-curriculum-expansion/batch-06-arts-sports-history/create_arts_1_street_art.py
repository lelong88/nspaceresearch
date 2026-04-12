"""
Create curriculum: Street Art Revolution
Level: preintermediate | Type: balanced_skills | Content: [] | Topic: Arts
18 words, 5 sessions (3 learning + 1 review + 1 final reading)
Bilingual (Vietnamese instructions, English reading passages)
Description tone: provocative_question
Farewell tone: introspective guide
"""

import sys, os, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from firebase_token import get_firebase_id_token
from validate_curriculum import validate_balanced_skills_standard, validate_content_type_tags, validate_bilingual_prompts

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Vocabulary (18 words, 3 groups of 6) ──

group1 = ["graffiti", "mural", "vandalism", "canvas", "spray", "tag"]
group2 = ["stencil", "commission", "gallery", "anonymous", "provocative", "urban"]
group3 = ["installation", "curator", "gentrification", "aesthetic", "subculture", "activism"]
all_words = group1 + group2 + group3

# ── Hand-written content ──

content = {
    "title": "Street Art Revolution — Khi Đường Phố Trở Thành Bảo Tàng",
    "contentTypeTags": [],
    # Tone: provocative_question
    "description": (
        "NGHỆ THUẬT ĐƯỜNG PHỐ LÀ PHÁ HOẠI HAY LÀ TIẾNG NÓI CỦA NHỮNG NGƯỜI KHÔNG CÓ SÂN KHẤU?\n\n"
        "Bạn đi ngang một bức tường cũ kỹ mỗi ngày — cho đến khi ai đó phun lên đó một khuôn mặt khổng lồ "
        "với đôi mắt nhìn thẳng vào bạn. Bỗng nhiên, bạn dừng lại. Bạn chụp ảnh. Bạn tự hỏi: ai đã vẽ cái này?\n\n"
        "Nghệ thuật đường phố giống như một cuộc trò chuyện bí mật giữa thành phố và cư dân — "
        "không cần vé vào cửa, không cần hiểu biết hàn lâm, chỉ cần mở mắt và cảm nhận.\n\n"
        "Từ Banksy ẩn danh đến những bức tranh tường khổng lồ ở Sài Gòn, nghệ thuật đường phố đang thay đổi "
        "cách chúng ta nhìn nhận không gian công cộng — và cách chúng ta định nghĩa 'nghệ sĩ'.\n\n"
        "Học 18 từ vựng sống động qua trải nghiệm đa giác quan — vừa khám phá thế giới graffiti, mural, "
        "stencil art, vừa nâng trình tiếng Anh một cách tự nhiên nhất."
    ),
    "preview": {
        "text": (
            "Hãy tưởng tượng bạn đang đi bộ qua một con hẻm ở Melbourne, Berlin, hay ngay tại Sài Gòn — "
            "và bất ngờ bắt gặp một bức tranh tường rực rỡ kể câu chuyện về tự do, bất công, hay đơn giản là vẻ đẹp. "
            "Ai đã vẽ nó? Tại sao? Đó là vandalism hay art?\n\n"
            "Trong bài học này, bạn sẽ học 18 từ vựng tiếng Anh về nghệ thuật đường phố: "
            "graffiti, mural, vandalism, canvas, spray, tag, stencil, commission, gallery, anonymous, "
            "provocative, urban, installation, curator, gentrification, aesthetic, subculture, activism. "
            "Bạn sẽ đọc về hành trình của street art từ những bức tag bất hợp pháp đến các gallery danh giá, "
            "luyện phát âm qua các đoạn văn sống động, và viết về quan điểm của mình. "
            "Kết thúc bài học, bạn sẽ tự tin nói về nghệ thuật đường phố bằng tiếng Anh — "
            "và có lẽ sẽ nhìn những bức tường quanh mình bằng con mắt hoàn toàn khác."
        )
    },
    "learningSessions": [
        # ── Session 1: Phần 1 (group1: graffiti, mural, vandalism, canvas, spray, tag) ──
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về nghệ thuật đường phố và văn hóa graffiti.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học Street Art Revolution — Khi Đường Phố Trở Thành Bảo Tàng! "
                            "Bạn có bao giờ đi ngang một bức tường đầy màu sắc và tự hỏi: đây là nghệ thuật hay phá hoại? "
                            "Câu hỏi đó chính là trung tâm của bài học hôm nay.\n\n"
                            "Nghệ thuật đường phố — hay street art — đã tồn tại hàng thập kỷ, từ những bức graffiti "
                            "trên tàu điện ngầm New York những năm 1970 đến những bức tranh tường khổng lồ ở São Paulo, "
                            "Berlin, và ngay tại Việt Nam. Nó là tiếng nói của những người trẻ, của những cộng đồng "
                            "muốn được nhìn thấy, được lắng nghe.\n\n"
                            "Trong phần đầu tiên, bạn sẽ học 6 từ vựng nền tảng: graffiti, mural, vandalism, canvas, "
                            "spray, và tag. Đây là những từ bạn sẽ gặp liên tục khi đọc hoặc nói về street art bằng tiếng Anh. "
                            "Hãy sẵn sàng khám phá nhé!"
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Học từ vựng Phần 1",
                    "description": "Học chi tiết 6 từ: graffiti, mural, vandalism, canvas, spray, tag.",
                    "data": {
                        "text": (
                            "Bây giờ chúng ta sẽ học chi tiết 6 từ vựng đầu tiên.\n\n"
                            "Từ đầu tiên là 'graffiti' — danh từ, nghĩa là hình vẽ hoặc chữ viết được phun hoặc vẽ "
                            "lên tường, thường ở nơi công cộng mà không được phép. Trong bài đọc, bạn sẽ thấy câu: "
                            "'The graffiti on the abandoned building told stories that newspapers never printed.' "
                            "Graffiti có thể là nghệ thuật, có thể là phá hoại — tùy vào góc nhìn của bạn.\n\n"
                            "Từ thứ hai là 'mural' — danh từ, nghĩa là một bức tranh lớn được vẽ trực tiếp lên tường. "
                            "Khác với graffiti, mural thường được đặt hàng chính thức và có quy mô lớn. "
                            "Trong bài đọc: 'The mural stretched across the entire side of the five-story building, "
                            "depicting the neighborhood's history.' Mural thường kể một câu chuyện hoặc truyền tải thông điệp cộng đồng.\n\n"
                            "Từ thứ ba là 'vandalism' — danh từ, nghĩa là hành vi cố ý phá hoại tài sản. "
                            "Đây là từ mà nhiều người dùng để chỉ trích graffiti. "
                            "Trong bài đọc: 'Critics called it vandalism, but the residents saw it as a gift to their gray street.' "
                            "Ranh giới giữa vandalism và art là chủ đề tranh luận không bao giờ kết thúc.\n\n"
                            "Từ thứ tư là 'canvas' — danh từ, nghĩa gốc là vải bạt dùng để vẽ tranh, "
                            "nhưng trong street art, canvas có nghĩa mở rộng là bất kỳ bề mặt nào mà nghệ sĩ vẽ lên — "
                            "tường, cầu, tàu hỏa. Trong bài đọc: 'For street artists, the entire city is their canvas.' "
                            "Canvas trong ngữ cảnh này mang tính ẩn dụ rất đẹp.\n\n"
                            "Từ thứ năm là 'spray' — động từ, nghĩa là phun sơn hoặc chất lỏng dưới dạng sương mù. "
                            "Spray paint là công cụ chính của nghệ sĩ đường phố. "
                            "Trong bài đọc: 'She sprayed the final line of color just as the sun came up.' "
                            "Spray cũng có thể dùng như danh từ — a spray of paint.\n\n"
                            "Từ cuối cùng trong phần này là 'tag' — danh từ hoặc động từ, nghĩa là chữ ký nghệ thuật "
                            "của một nghệ sĩ graffiti, thường được viết nhanh bằng spray paint hoặc marker. "
                            "Trong bài đọc: 'His tag appeared on walls across three continents, yet nobody knew his real name.' "
                            "Tag là dạng graffiti đơn giản nhất — chỉ là tên hoặc biệt danh của nghệ sĩ."
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nghệ thuật đường phố cơ bản (Phần 1)",
                    "description": "Học 6 từ: graffiti, mural, vandalism, canvas, spray, tag.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nghệ thuật đường phố cơ bản (Phần 1)",
                    "description": "Học 6 từ: graffiti, mural, vandalism, canvas, spray, tag.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Nghệ thuật đường phố cơ bản (Phần 1)",
                    "description": "Luyện tập 6 từ: graffiti, mural, vandalism, canvas, spray, tag.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Nghệ thuật đường phố cơ bản (Phần 1)",
                    "description": "Luyện tập 6 từ: graffiti, mural, vandalism, canvas, spray, tag.",
                    "data": {"vocabList": group1}
                },
                {
                    "activityType": "introAudio",
                    "title": "Ngữ pháp và cách dùng từ",
                    "description": "Hướng dẫn cách sử dụng 6 từ vựng trong câu và ngữ cảnh thực tế.",
                    "data": {
                        "text": (
                            "Trước khi đọc bài, hãy cùng tìm hiểu cách dùng 6 từ vựng này trong câu nhé.\n\n"
                            "'Graffiti' là danh từ không đếm được — bạn nói 'graffiti is' chứ không phải 'graffiti are'. "
                            "Ví dụ: 'The graffiti is beautiful but illegal.' Bạn cũng có thể nói 'a piece of graffiti' "
                            "khi muốn chỉ một tác phẩm cụ thể.\n\n"
                            "'Mural' là danh từ đếm được — 'a mural', 'two murals'. Thường đi với 'paint a mural', "
                            "'commission a mural'. Ví dụ: 'The city commissioned a mural to celebrate its 100th anniversary.'\n\n"
                            "'Vandalism' là danh từ không đếm được, thường đi với 'commit vandalism' hoặc 'an act of vandalism'. "
                            "Ví dụ: 'The police charged him with vandalism after he painted the bridge.'\n\n"
                            "'Canvas' có thể đếm được — 'a canvas', 'canvases'. Trong street art, nó thường dùng theo nghĩa ẩn dụ: "
                            "'The wall became her canvas.' Lưu ý phát âm: /ˈkæn.vəs/.\n\n"
                            "'Spray' vừa là động từ vừa là danh từ. Động từ: 'She sprayed the wall.' "
                            "Danh từ: 'a spray of red paint.' Quá khứ: 'sprayed'. Thường đi với 'spray paint' (danh từ ghép).\n\n"
                            "'Tag' vừa là danh từ vừa là động từ. Danh từ: 'His tag was everywhere.' "
                            "Động từ: 'Someone tagged the new building overnight.' Quá khứ: 'tagged'. "
                            "Trong ngữ cảnh street art, tag khác với graffiti ở chỗ tag chỉ là chữ ký, "
                            "còn graffiti có thể là hình vẽ phức tạp hơn."
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Khi bức tường bắt đầu nói",
                    "description": "The graffiti on the abandoned building told stories that newspapers never printed.",
                    "data": {
                        "text": (
                            "Last summer, a quiet street in District 3 of Ho Chi Minh City changed overnight. "
                            "Someone had painted a massive mural on the side of an old apartment building. "
                            "The mural showed a young girl releasing paper birds into the sky. Nobody knew who the artist was.\n\n"
                            "The graffiti on the abandoned building next door told stories that newspapers never printed. "
                            "One piece showed factory workers with tired eyes. Another showed children playing in a flooded street. "
                            "Critics called it vandalism, but the residents saw it as a gift to their gray street.\n\n"
                            "For street artists, the entire city is their canvas. They do not need a gallery or a frame. "
                            "A blank wall is enough. She sprayed the final line of color just as the sun came up, "
                            "then disappeared before anyone could see her face.\n\n"
                            "His tag appeared on walls across three continents, yet nobody knew his real name. "
                            "That is the nature of street art — the work speaks louder than the artist. "
                            "The spray paint dries, the colors fade in the rain, but the message stays."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Khi bức tường bắt đầu nói",
                    "description": "Luyện đọc to đoạn văn về nghệ thuật đường phố ở Sài Gòn.",
                    "data": {
                        "text": (
                            "Last summer, a quiet street in District 3 of Ho Chi Minh City changed overnight. "
                            "Someone had painted a massive mural on the side of an old apartment building. "
                            "The mural showed a young girl releasing paper birds into the sky. Nobody knew who the artist was.\n\n"
                            "The graffiti on the abandoned building next door told stories that newspapers never printed. "
                            "One piece showed factory workers with tired eyes. Another showed children playing in a flooded street. "
                            "Critics called it vandalism, but the residents saw it as a gift to their gray street.\n\n"
                            "For street artists, the entire city is their canvas. They do not need a gallery or a frame. "
                            "A blank wall is enough. She sprayed the final line of color just as the sun came up, "
                            "then disappeared before anyone could see her face.\n\n"
                            "His tag appeared on walls across three continents, yet nobody knew his real name. "
                            "That is the nature of street art — the work speaks louder than the artist. "
                            "The spray paint dries, the colors fade in the rain, but the message stays."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Khi bức tường bắt đầu nói",
                    "description": "Nghe và theo dõi đoạn văn về nghệ thuật đường phố ở Sài Gòn.",
                    "data": {
                        "text": (
                            "Last summer, a quiet street in District 3 of Ho Chi Minh City changed overnight. "
                            "Someone had painted a massive mural on the side of an old apartment building. "
                            "The mural showed a young girl releasing paper birds into the sky. Nobody knew who the artist was.\n\n"
                            "The graffiti on the abandoned building next door told stories that newspapers never printed. "
                            "One piece showed factory workers with tired eyes. Another showed children playing in a flooded street. "
                            "Critics called it vandalism, but the residents saw it as a gift to their gray street.\n\n"
                            "For street artists, the entire city is their canvas. They do not need a gallery or a frame. "
                            "A blank wall is enough. She sprayed the final line of color just as the sun came up, "
                            "then disappeared before anyone could see her face.\n\n"
                            "His tag appeared on walls across three continents, yet nobody knew his real name. "
                            "That is the nature of street art — the work speaks louder than the artist. "
                            "The spray paint dries, the colors fade in the rain, but the message stays."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nghệ thuật đường phố cơ bản (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về graffiti, mural và nghệ thuật đường phố.",
                    "data": {
                        "vocabList": group1,
                        "items": [
                            {
                                "targetVocab": "graffiti",
                                "prompt": "Hãy dùng từ 'graffiti' để viết một câu về những hình vẽ bạn thấy trên đường phố. Ví dụ: The colorful graffiti on the old train station made the boring building look alive."
                            },
                            {
                                "targetVocab": "mural",
                                "prompt": "Hãy dùng từ 'mural' để viết một câu về một bức tranh tường lớn. Ví dụ: The community painted a mural of local heroes on the school wall to inspire young students."
                            },
                            {
                                "targetVocab": "vandalism",
                                "prompt": "Hãy dùng từ 'vandalism' để viết một câu về việc phá hoại tài sản công cộng. Ví dụ: Some people consider street art to be vandalism because it damages public property."
                            },
                            {
                                "targetVocab": "canvas",
                                "prompt": "Hãy dùng từ 'canvas' để viết một câu về bề mặt mà nghệ sĩ sử dụng để sáng tạo. Ví dụ: The abandoned factory wall became the perfect canvas for the young artist's first large painting."
                            },
                            {
                                "targetVocab": "spray",
                                "prompt": "Hãy dùng từ 'spray' để viết một câu về việc phun sơn hoặc tạo tác phẩm nghệ thuật. Ví dụ: The artist sprayed bright yellow paint across the concrete wall to create a giant sunflower."
                            },
                            {
                                "targetVocab": "tag",
                                "prompt": "Hãy dùng từ 'tag' để viết một câu về chữ ký nghệ thuật của một nghệ sĩ graffiti. Ví dụ: The mysterious artist's tag appeared on buildings all over the city, but nobody knew who was behind it."
                            }
                        ]
                    }
                }
            ]
        },

        # ── Session 2: Phần 2 (group2: stencil, commission, gallery, anonymous, provocative, urban) ──
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu Phần 2",
                    "description": "Ôn lại Phần 1 và giới thiệu 6 từ vựng mới về thế giới nghệ thuật đường phố.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại với Phần 2 của Street Art Revolution! "
                            "Trong Phần 1, bạn đã học 6 từ nền tảng: graffiti, mural, vandalism, canvas, spray, và tag. "
                            "Bạn đã biết rằng street art có thể là tiếng nói của cộng đồng, và ranh giới giữa nghệ thuật "
                            "và phá hoại không phải lúc nào cũng rõ ràng.\n\n"
                            "Trong phần này, chúng ta sẽ đi sâu hơn vào thế giới street art với 6 từ mới: "
                            "stencil, commission, gallery, anonymous, provocative, và urban. "
                            "Những từ này sẽ giúp bạn hiểu cách street art chuyển từ đường phố vào bảo tàng, "
                            "và tại sao sự ẩn danh lại là một phần quan trọng của văn hóa này."
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Học từ vựng Phần 2",
                    "description": "Học chi tiết 6 từ: stencil, commission, gallery, anonymous, provocative, urban.",
                    "data": {
                        "text": (
                            "Hãy cùng học 6 từ vựng mới của Phần 2.\n\n"
                            "Từ đầu tiên là 'stencil' — danh từ hoặc động từ. Stencil là một tấm khuôn có hình cắt sẵn, "
                            "khi phun sơn qua sẽ tạo ra hình ảnh trên tường. Banksy — nghệ sĩ đường phố nổi tiếng nhất thế giới — "
                            "nổi tiếng với kỹ thuật stencil. Trong bài đọc: 'Banksy's stencil art proved that a simple cutout "
                            "and a can of spray paint could shake the entire art world.' Stencil cho phép nghệ sĩ tạo hình nhanh "
                            "và chính xác, rất phù hợp khi cần hoàn thành tác phẩm trước khi bị phát hiện.\n\n"
                            "Từ thứ hai là 'commission' — động từ hoặc danh từ, nghĩa là đặt hàng hoặc thuê ai đó tạo ra "
                            "một tác phẩm nghệ thuật. Khi một thành phố commission một bức mural, nghĩa là họ chính thức "
                            "trả tiền cho nghệ sĩ để vẽ. Trong bài đọc: 'The city council commissioned local artists to transform "
                            "the ugly parking garage into an outdoor gallery.' Commission đánh dấu bước chuyển từ bất hợp pháp "
                            "sang được công nhận.\n\n"
                            "Từ thứ ba là 'gallery' — danh từ, nghĩa là phòng trưng bày nghệ thuật. "
                            "Trong street art, gallery là biểu tượng của sự công nhận chính thống. "
                            "Trong bài đọc: 'When street art enters a gallery, does it lose its soul?' "
                            "Đây là câu hỏi mà nhiều nghệ sĩ đường phố phải đối mặt.\n\n"
                            "Từ thứ tư là 'anonymous' — tính từ, nghĩa là ẩn danh, không ai biết danh tính. "
                            "Nhiều nghệ sĩ đường phố chọn ẩn danh vì lý do pháp lý hoặc triết lý. "
                            "Trong bài đọc: 'The anonymous artist wanted the work to speak for itself, "
                            "not the fame of a name.' Phát âm: /əˈnɒn.ɪ.məs/.\n\n"
                            "Từ thứ năm là 'provocative' — tính từ, nghĩa là khiêu khích, gây tranh cãi, "
                            "kích thích suy nghĩ. Street art thường cố tình provocative để buộc người xem phải phản ứng. "
                            "Trong bài đọc: 'The most provocative pieces forced people to stop, stare, and argue.' "
                            "Provocative không nhất thiết là tiêu cực — nó có thể là tích cực khi khiến người ta suy nghĩ.\n\n"
                            "Từ cuối cùng là 'urban' — tính từ, nghĩa là thuộc về thành thị, đô thị. "
                            "Street art là một phần của urban culture — văn hóa đô thị. "
                            "Trong bài đọc: 'Urban landscapes became open-air museums where anyone could be an audience.' "
                            "Urban thường đi với: urban art, urban landscape, urban culture, urban planning."
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Từ đường phố đến gallery (Phần 2)",
                    "description": "Học 6 từ: stencil, commission, gallery, anonymous, provocative, urban.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Từ đường phố đến gallery (Phần 2)",
                    "description": "Học 6 từ: stencil, commission, gallery, anonymous, provocative, urban.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Từ đường phố đến gallery (Phần 2)",
                    "description": "Luyện tập 6 từ: stencil, commission, gallery, anonymous, provocative, urban.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Từ đường phố đến gallery (Phần 2)",
                    "description": "Luyện tập 6 từ: stencil, commission, gallery, anonymous, provocative, urban.",
                    "data": {"vocabList": group2}
                },
                {
                    "activityType": "introAudio",
                    "title": "Ngữ pháp và cách dùng từ",
                    "description": "Hướng dẫn cách sử dụng 6 từ vựng Phần 2 trong câu và ngữ cảnh thực tế.",
                    "data": {
                        "text": (
                            "Hãy cùng tìm hiểu cách dùng 6 từ vựng Phần 2 trong câu.\n\n"
                            "'Stencil' có thể là danh từ hoặc động từ. Danh từ: 'a stencil of a dove'. "
                            "Động từ: 'She stenciled the image onto the wall.' Quá khứ: 'stenciled' hoặc 'stencilled'. "
                            "Thường đi với: stencil art, stencil technique, cut a stencil.\n\n"
                            "'Commission' là động từ hoặc danh từ. Động từ: 'The museum commissioned a new mural.' "
                            "Danh từ: 'She received a commission to paint the hospital entrance.' "
                            "Lưu ý: commission cũng có nghĩa 'hoa hồng' trong kinh doanh, nhưng trong nghệ thuật "
                            "nó luôn nghĩa là 'đặt hàng tác phẩm'.\n\n"
                            "'Gallery' là danh từ đếm được — 'a gallery', 'galleries'. "
                            "Thường đi với: art gallery, gallery opening, gallery owner. "
                            "Ví dụ: 'The gallery opening attracted hundreds of visitors on the first night.'\n\n"
                            "'Anonymous' là tính từ, thường đứng trước danh từ: 'an anonymous artist', 'an anonymous donation'. "
                            "Danh từ liên quan: 'anonymity' — sự ẩn danh. Ví dụ: 'Anonymity gives street artists freedom.'\n\n"
                            "'Provocative' là tính từ, thường đứng trước danh từ: 'a provocative image', 'provocative art'. "
                            "Danh từ liên quan: 'provocation'. Động từ: 'provoke'. "
                            "Ví dụ: 'His provocative murals provoked heated debates in the community.'\n\n"
                            "'Urban' là tính từ, luôn đứng trước danh từ: 'urban art', 'urban landscape', 'urban decay'. "
                            "Trái nghĩa: 'rural'. Ví dụ: 'Urban art reflects the energy and chaos of city life.'"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Từ bóng tối ra ánh sáng",
                    "description": "Banksy's stencil art proved that a simple cutout could shake the art world.",
                    "data": {
                        "text": (
                            "In 2003, an anonymous artist held a secret exhibition in a London warehouse. "
                            "There were no invitations, no press releases, and no name on the door. "
                            "Inside, visitors found stencil art on every wall — images of rats carrying protest signs, "
                            "soldiers throwing flowers, and children reaching for red balloons. "
                            "Banksy's stencil art proved that a simple cutout and a can of spray paint "
                            "could shake the entire art world.\n\n"
                            "The exhibition was provocative. One piece showed a police officer hugging a teddy bear. "
                            "Another showed the Queen of England as a chimpanzee. "
                            "The most provocative pieces forced people to stop, stare, and argue. "
                            "Was this genius or disrespect?\n\n"
                            "Soon, cities around the world began to change their approach. "
                            "The city council commissioned local artists to transform the ugly parking garage "
                            "into an outdoor gallery. When street art enters a gallery, does it lose its soul? "
                            "Some artists refused the invitation. They believed that urban landscapes "
                            "became open-air museums where anyone could be an audience — "
                            "and that was more powerful than any gallery wall.\n\n"
                            "The anonymous artist wanted the work to speak for itself, not the fame of a name. "
                            "In the urban jungle, art does not need permission. It just needs a wall and a voice."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Từ bóng tối ra ánh sáng",
                    "description": "Luyện đọc to đoạn văn về Banksy và nghệ thuật stencil.",
                    "data": {
                        "text": (
                            "In 2003, an anonymous artist held a secret exhibition in a London warehouse. "
                            "There were no invitations, no press releases, and no name on the door. "
                            "Inside, visitors found stencil art on every wall — images of rats carrying protest signs, "
                            "soldiers throwing flowers, and children reaching for red balloons. "
                            "Banksy's stencil art proved that a simple cutout and a can of spray paint "
                            "could shake the entire art world.\n\n"
                            "The exhibition was provocative. One piece showed a police officer hugging a teddy bear. "
                            "Another showed the Queen of England as a chimpanzee. "
                            "The most provocative pieces forced people to stop, stare, and argue. "
                            "Was this genius or disrespect?\n\n"
                            "Soon, cities around the world began to change their approach. "
                            "The city council commissioned local artists to transform the ugly parking garage "
                            "into an outdoor gallery. When street art enters a gallery, does it lose its soul? "
                            "Some artists refused the invitation. They believed that urban landscapes "
                            "became open-air museums where anyone could be an audience — "
                            "and that was more powerful than any gallery wall.\n\n"
                            "The anonymous artist wanted the work to speak for itself, not the fame of a name. "
                            "In the urban jungle, art does not need permission. It just needs a wall and a voice."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Từ bóng tối ra ánh sáng",
                    "description": "Nghe và theo dõi đoạn văn về Banksy và nghệ thuật stencil.",
                    "data": {
                        "text": (
                            "In 2003, an anonymous artist held a secret exhibition in a London warehouse. "
                            "There were no invitations, no press releases, and no name on the door. "
                            "Inside, visitors found stencil art on every wall — images of rats carrying protest signs, "
                            "soldiers throwing flowers, and children reaching for red balloons. "
                            "Banksy's stencil art proved that a simple cutout and a can of spray paint "
                            "could shake the entire art world.\n\n"
                            "The exhibition was provocative. One piece showed a police officer hugging a teddy bear. "
                            "Another showed the Queen of England as a chimpanzee. "
                            "The most provocative pieces forced people to stop, stare, and argue. "
                            "Was this genius or disrespect?\n\n"
                            "Soon, cities around the world began to change their approach. "
                            "The city council commissioned local artists to transform the ugly parking garage "
                            "into an outdoor gallery. When street art enters a gallery, does it lose its soul? "
                            "Some artists refused the invitation. They believed that urban landscapes "
                            "became open-air museums where anyone could be an audience — "
                            "and that was more powerful than any gallery wall.\n\n"
                            "The anonymous artist wanted the work to speak for itself, not the fame of a name. "
                            "In the urban jungle, art does not need permission. It just needs a wall and a voice."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Từ đường phố đến gallery (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng về stencil, gallery và nghệ sĩ ẩn danh.",
                    "data": {
                        "vocabList": group2,
                        "items": [
                            {
                                "targetVocab": "stencil",
                                "prompt": "Hãy dùng từ 'stencil' để viết một câu về kỹ thuật tạo hình trong nghệ thuật đường phố. Ví dụ: The artist used a stencil to create dozens of identical bird images along the riverside wall."
                            },
                            {
                                "targetVocab": "commission",
                                "prompt": "Hãy dùng từ 'commission' để viết một câu về việc đặt hàng một tác phẩm nghệ thuật. Ví dụ: The school commissioned a local painter to create a mural about the history of education in Vietnam."
                            },
                            {
                                "targetVocab": "gallery",
                                "prompt": "Hãy dùng từ 'gallery' để viết một câu về nơi trưng bày nghệ thuật. Ví dụ: The new gallery in District 1 displays both traditional paintings and modern street art photography."
                            },
                            {
                                "targetVocab": "anonymous",
                                "prompt": "Hãy dùng từ 'anonymous' để viết một câu về một người hoặc hành động không rõ danh tính. Ví dụ: An anonymous donor paid for the restoration of the damaged mural in the city center."
                            },
                            {
                                "targetVocab": "provocative",
                                "prompt": "Hãy dùng từ 'provocative' để viết một câu về điều gì đó gây tranh cãi hoặc kích thích suy nghĩ. Ví dụ: The provocative sculpture in the park divided the community into those who loved it and those who wanted it removed."
                            },
                            {
                                "targetVocab": "urban",
                                "prompt": "Hãy dùng từ 'urban' để viết một câu về cuộc sống hoặc văn hóa thành thị. Ví dụ: Urban neighborhoods often have the most creative street art because artists draw inspiration from city life."
                            }
                        ]
                    }
                }
            ]
        },

        # ── Session 3: Phần 3 (group3: installation, curator, gentrification, aesthetic, subculture, activism) ──
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu Phần 3",
                    "description": "Ôn lại Phần 1-2 và giới thiệu 6 từ vựng nâng cao về nghệ thuật đường phố.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với Phần 3 — phần cuối cùng trước khi ôn tập! "
                            "Bạn đã đi một chặng đường dài. Trong Phần 1, bạn học về graffiti, mural, vandalism, "
                            "canvas, spray, và tag — những khái niệm cơ bản nhất. "
                            "Trong Phần 2, bạn khám phá stencil, commission, gallery, anonymous, provocative, và urban — "
                            "cách street art chuyển từ bất hợp pháp sang được công nhận.\n\n"
                            "Bây giờ, trong Phần 3, chúng ta sẽ nâng tầm với 6 từ vựng mang tính phân tích hơn: "
                            "installation, curator, gentrification, aesthetic, subculture, và activism. "
                            "Đây là những từ bạn cần khi muốn thảo luận sâu về street art — "
                            "không chỉ mô tả nó, mà còn hiểu tác động xã hội của nó."
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Học từ vựng Phần 3",
                    "description": "Học chi tiết 6 từ: installation, curator, gentrification, aesthetic, subculture, activism.",
                    "data": {
                        "text": (
                            "Hãy cùng học 6 từ vựng cuối cùng.\n\n"
                            "Từ đầu tiên là 'installation' — danh từ, nghĩa là một tác phẩm nghệ thuật được thiết kế "
                            "cho một không gian cụ thể, thường có kích thước lớn và mang tính tương tác. "
                            "Khác với tranh treo tường, installation chiếm cả một căn phòng hoặc không gian ngoài trời. "
                            "Trong bài đọc: 'The installation filled an entire alley with hanging mirrors and painted shadows.' "
                            "Installation art là sự giao thoa giữa street art và nghệ thuật đương đại.\n\n"
                            "Từ thứ hai là 'curator' — danh từ, nghĩa là người phụ trách tuyển chọn và tổ chức "
                            "các tác phẩm nghệ thuật trong bảo tàng hoặc triển lãm. "
                            "Trong bài đọc: 'The curator invited five street artists to display their work inside the museum — "
                            "a decision that angered both traditional artists and graffiti purists.' "
                            "Curator là cầu nối giữa thế giới đường phố và thế giới nghệ thuật chính thống.\n\n"
                            "Từ thứ ba là 'gentrification' — danh từ, nghĩa là quá trình khu vực nghèo được cải tạo, "
                            "giá nhà tăng, và cư dân gốc bị đẩy ra ngoài. Street art thường liên quan đến gentrification — "
                            "khi nghệ thuật làm đẹp một khu phố, giá thuê tăng. "
                            "Trong bài đọc: 'Gentrification turned the artists' neighborhood into a place they could no longer afford.' "
                            "Đây là nghịch lý đau đớn nhất của street art.\n\n"
                            "Từ thứ tư là 'aesthetic' — tính từ hoặc danh từ, nghĩa là thuộc về thẩm mỹ, "
                            "hoặc phong cách thị giác đặc trưng. Mỗi nghệ sĩ đường phố có aesthetic riêng. "
                            "Trong bài đọc: 'Her aesthetic combined Japanese calligraphy with Latin American color palettes.' "
                            "Phát âm: /esˈθet.ɪk/.\n\n"
                            "Từ thứ năm là 'subculture' — danh từ, nghĩa là một nhóm văn hóa nhỏ tồn tại bên trong "
                            "văn hóa chủ đạo, với giá trị và phong cách riêng. Graffiti bắt đầu như một subculture "
                            "của giới trẻ đô thị. Trong bài đọc: 'What began as a subculture of rebellious teenagers "
                            "has become a global movement worth billions.' Subculture thường đi với: youth subculture, "
                            "underground subculture.\n\n"
                            "Từ cuối cùng là 'activism' — danh từ, nghĩa là hoạt động vận động, đấu tranh cho "
                            "một mục đích xã hội hoặc chính trị. Nhiều nghệ sĩ đường phố dùng tác phẩm như một hình thức activism. "
                            "Trong bài đọc: 'For many artists, street art is not decoration — it is activism, "
                            "a way to fight injustice with color instead of violence.' "
                            "Activism liên quan đến: activist (người hoạt động), activate (kích hoạt)."
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nghệ thuật và xã hội (Phần 3)",
                    "description": "Học 6 từ: installation, curator, gentrification, aesthetic, subculture, activism.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nghệ thuật và xã hội (Phần 3)",
                    "description": "Học 6 từ: installation, curator, gentrification, aesthetic, subculture, activism.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Nghệ thuật và xã hội (Phần 3)",
                    "description": "Luyện tập 6 từ: installation, curator, gentrification, aesthetic, subculture, activism.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Nghệ thuật và xã hội (Phần 3)",
                    "description": "Luyện tập 6 từ: installation, curator, gentrification, aesthetic, subculture, activism.",
                    "data": {"vocabList": group3}
                },
                {
                    "activityType": "introAudio",
                    "title": "Ngữ pháp và cách dùng từ",
                    "description": "Hướng dẫn cách sử dụng 6 từ vựng Phần 3 trong câu và ngữ cảnh thực tế.",
                    "data": {
                        "text": (
                            "Hãy cùng tìm hiểu cách dùng 6 từ vựng Phần 3.\n\n"
                            "'Installation' là danh từ đếm được — 'an installation', 'installations'. "
                            "Thường đi với: art installation, site-specific installation, interactive installation. "
                            "Ví dụ: 'The interactive installation invited visitors to add their own drawings to the wall.'\n\n"
                            "'Curator' là danh từ đếm được — 'a curator', 'curators'. "
                            "Động từ liên quan: 'curate' — tuyển chọn và tổ chức. "
                            "Ví dụ: 'She curated an exhibition of street art from twelve different countries.' "
                            "Bạn cũng có thể nói 'a curated collection' — một bộ sưu tập được tuyển chọn kỹ lưỡng.\n\n"
                            "'Gentrification' là danh từ không đếm được. Động từ: 'gentrify'. "
                            "Tính từ: 'gentrified'. Ví dụ: 'The gentrified neighborhood lost its original character.' "
                            "Thường mang nghĩa tiêu cực trong ngữ cảnh xã hội.\n\n"
                            "'Aesthetic' vừa là tính từ vừa là danh từ. Tính từ: 'aesthetic value', 'aesthetic choice'. "
                            "Danh từ: 'the aesthetic of the 1990s'. Số nhiều danh từ: 'aesthetics' — ngành mỹ học. "
                            "Ví dụ: 'The artist's aesthetic is a mix of punk and traditional Vietnamese patterns.'\n\n"
                            "'Subculture' là danh từ đếm được — 'a subculture', 'subcultures'. "
                            "Tiền tố 'sub-' nghĩa là 'dưới, bên trong'. "
                            "Ví dụ: 'Hip-hop, skateboarding, and graffiti all grew from the same urban subculture.'\n\n"
                            "'Activism' là danh từ không đếm được. Người hoạt động: 'activist'. "
                            "Thường đi với: political activism, social activism, environmental activism. "
                            "Ví dụ: 'Her art is a form of activism — every piece carries a message about climate change.'"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nghệ thuật hay hoạt động xã hội?",
                    "description": "The installation filled an entire alley with hanging mirrors and painted shadows.",
                    "data": {
                        "text": (
                            "In the Wynwood district of Miami, an entire neighborhood was transformed by street art. "
                            "What was once a forgotten warehouse area became one of the most visited art destinations in America. "
                            "The installation filled an entire alley with hanging mirrors and painted shadows, "
                            "creating a space where visitors felt like they were walking inside a painting.\n\n"
                            "The curator invited five street artists to display their work inside the museum — "
                            "a decision that angered both traditional artists and graffiti purists. "
                            "Traditional artists felt that street art did not deserve museum space. "
                            "Graffiti purists felt that putting street art in a museum killed its rebellious spirit.\n\n"
                            "But the biggest problem was gentrification. Gentrification turned the artists' neighborhood "
                            "into a place they could no longer afford. The murals that made the area beautiful "
                            "also made it expensive. Coffee shops replaced repair shops. Tourists replaced residents.\n\n"
                            "Her aesthetic combined Japanese calligraphy with Latin American color palettes — "
                            "a style that could only exist in a globalized world. What began as a subculture "
                            "of rebellious teenagers has become a global movement worth billions. "
                            "For many artists, street art is not decoration — it is activism, "
                            "a way to fight injustice with color instead of violence."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Nghệ thuật hay hoạt động xã hội?",
                    "description": "Luyện đọc to đoạn văn về Wynwood và tác động xã hội của street art.",
                    "data": {
                        "text": (
                            "In the Wynwood district of Miami, an entire neighborhood was transformed by street art. "
                            "What was once a forgotten warehouse area became one of the most visited art destinations in America. "
                            "The installation filled an entire alley with hanging mirrors and painted shadows, "
                            "creating a space where visitors felt like they were walking inside a painting.\n\n"
                            "The curator invited five street artists to display their work inside the museum — "
                            "a decision that angered both traditional artists and graffiti purists. "
                            "Traditional artists felt that street art did not deserve museum space. "
                            "Graffiti purists felt that putting street art in a museum killed its rebellious spirit.\n\n"
                            "But the biggest problem was gentrification. Gentrification turned the artists' neighborhood "
                            "into a place they could no longer afford. The murals that made the area beautiful "
                            "also made it expensive. Coffee shops replaced repair shops. Tourists replaced residents.\n\n"
                            "Her aesthetic combined Japanese calligraphy with Latin American color palettes — "
                            "a style that could only exist in a globalized world. What began as a subculture "
                            "of rebellious teenagers has become a global movement worth billions. "
                            "For many artists, street art is not decoration — it is activism, "
                            "a way to fight injustice with color instead of violence."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nghệ thuật hay hoạt động xã hội?",
                    "description": "Nghe và theo dõi đoạn văn về Wynwood và tác động xã hội của street art.",
                    "data": {
                        "text": (
                            "In the Wynwood district of Miami, an entire neighborhood was transformed by street art. "
                            "What was once a forgotten warehouse area became one of the most visited art destinations in America. "
                            "The installation filled an entire alley with hanging mirrors and painted shadows, "
                            "creating a space where visitors felt like they were walking inside a painting.\n\n"
                            "The curator invited five street artists to display their work inside the museum — "
                            "a decision that angered both traditional artists and graffiti purists. "
                            "Traditional artists felt that street art did not deserve museum space. "
                            "Graffiti purists felt that putting street art in a museum killed its rebellious spirit.\n\n"
                            "But the biggest problem was gentrification. Gentrification turned the artists' neighborhood "
                            "into a place they could no longer afford. The murals that made the area beautiful "
                            "also made it expensive. Coffee shops replaced repair shops. Tourists replaced residents.\n\n"
                            "Her aesthetic combined Japanese calligraphy with Latin American color palettes — "
                            "a style that could only exist in a globalized world. What began as a subculture "
                            "of rebellious teenagers has become a global movement worth billions. "
                            "For many artists, street art is not decoration — it is activism, "
                            "a way to fight injustice with color instead of violence."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nghệ thuật và xã hội (Phần 3)",
                    "description": "Viết câu sử dụng 6 từ vựng về installation, gentrification và activism.",
                    "data": {
                        "vocabList": group3,
                        "items": [
                            {
                                "targetVocab": "installation",
                                "prompt": "Hãy dùng từ 'installation' để viết một câu về một tác phẩm nghệ thuật chiếm không gian lớn. Ví dụ: The art installation in the park used recycled plastic bottles to create a giant ocean wave."
                            },
                            {
                                "targetVocab": "curator",
                                "prompt": "Hãy dùng từ 'curator' để viết một câu về người tổ chức triển lãm nghệ thuật. Ví dụ: The curator spent six months traveling to find the best street artists for the exhibition."
                            },
                            {
                                "targetVocab": "gentrification",
                                "prompt": "Hãy dùng từ 'gentrification' để viết một câu về sự thay đổi của một khu phố khi giá nhà tăng. Ví dụ: Gentrification forced many families to move away from the neighborhood where they had lived for decades."
                            },
                            {
                                "targetVocab": "aesthetic",
                                "prompt": "Hãy dùng từ 'aesthetic' để viết một câu về phong cách thị giác hoặc thẩm mỹ. Ví dụ: The cafe's aesthetic was inspired by 1960s pop art, with bright colors and bold patterns on every wall."
                            },
                            {
                                "targetVocab": "subculture",
                                "prompt": "Hãy dùng từ 'subculture' để viết một câu về một nhóm văn hóa nhỏ trong xã hội. Ví dụ: The skateboarding subculture has its own fashion, music, and language that outsiders rarely understand."
                            },
                            {
                                "targetVocab": "activism",
                                "prompt": "Hãy dùng từ 'activism' để viết một câu về việc dùng nghệ thuật hoặc hành động để thay đổi xã hội. Ví dụ: Environmental activism has inspired many street artists to paint murals about ocean pollution and deforestation."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng của Street Art Revolution. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong Phần 1, bạn học 6 từ nền tảng về street art: graffiti, mural, vandalism, "
                            "canvas, spray, và tag. Bạn đã đọc về một bức tranh tường bí ẩn xuất hiện ở Quận 3 Sài Gòn "
                            "và hiểu rằng ranh giới giữa nghệ thuật và phá hoại không hề đơn giản.\n\n"
                            "Trong Phần 2, bạn khám phá cách street art chuyển từ đường phố vào gallery với 6 từ: "
                            "stencil, commission, gallery, anonymous, provocative, và urban. "
                            "Bạn đã đọc về Banksy và câu hỏi liệu nghệ thuật đường phố có mất đi linh hồn "
                            "khi bước vào bảo tàng.\n\n"
                            "Trong Phần 3, bạn nâng tầm phân tích với 6 từ: installation, curator, gentrification, "
                            "aesthetic, subculture, và activism. Bạn đã đọc về Wynwood Miami và nghịch lý đau đớn "
                            "khi nghệ thuật làm đẹp khu phố nhưng cũng đẩy cư dân gốc ra ngoài.\n\n"
                            "Bây giờ, hãy ôn tập tất cả 18 từ vựng qua flashcards, bài tập, và viết câu. "
                            "Sau phần ôn tập này, bạn sẽ đọc một bài viết tổng hợp sử dụng toàn bộ 18 từ. Sẵn sàng chưa?"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về nghệ thuật đường phố, graffiti và văn hóa đô thị.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về nghệ thuật đường phố, graffiti và văn hóa đô thị.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Từ vựng cấp 1: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về nghệ thuật đường phố, graffiti và văn hóa đô thị.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Từ vựng cấp 2: Ôn tập toàn bộ",
                    "description": "Ôn tập 18 từ vựng về nghệ thuật đường phố, graffiti và văn hóa đô thị.",
                    "data": {"vocabList": all_words}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng về nghệ thuật đường phố.",
                    "data": {
                        "vocabList": all_words,
                        "items": [
                            {
                                "targetVocab": "graffiti",
                                "prompt": "Hãy dùng từ 'graffiti' để viết một câu về nghệ thuật đường phố trong thành phố của bạn. Ví dụ: The graffiti under the highway bridge has been there for years, and most people walk past without noticing it."
                            },
                            {
                                "targetVocab": "mural",
                                "prompt": "Hãy dùng từ 'mural' để viết một câu về một bức tranh tường mà bạn ấn tượng. Ví dụ: The mural on the hospital wall shows a garden full of flowers to bring comfort to patients."
                            },
                            {
                                "targetVocab": "vandalism",
                                "prompt": "Hãy dùng từ 'vandalism' để viết một câu về ranh giới giữa nghệ thuật và phá hoại. Ví dụ: What one person calls vandalism, another person might call a powerful form of self-expression."
                            },
                            {
                                "targetVocab": "canvas",
                                "prompt": "Hãy dùng từ 'canvas' để viết một câu về bề mặt sáng tạo của nghệ sĩ. Ví dụ: The old train station became a canvas for young artists who wanted to bring life back to the abandoned space."
                            },
                            {
                                "targetVocab": "spray",
                                "prompt": "Hãy dùng từ 'spray' để viết một câu về công cụ hoặc hành động phun sơn. Ví dụ: She learned to spray paint in smooth, even layers after months of practice on cardboard boxes."
                            },
                            {
                                "targetVocab": "tag",
                                "prompt": "Hãy dùng từ 'tag' để viết một câu về chữ ký của nghệ sĩ graffiti. Ví dụ: The police tried to find the person behind the tag that appeared on every bus stop in the city."
                            },
                            {
                                "targetVocab": "stencil",
                                "prompt": "Hãy dùng từ 'stencil' để viết một câu về kỹ thuật tạo hình nhanh. Ví dụ: Using a stencil allows artists to reproduce the same image quickly on multiple walls in one night."
                            },
                            {
                                "targetVocab": "commission",
                                "prompt": "Hãy dùng từ 'commission' để viết một câu về việc thuê nghệ sĩ tạo tác phẩm. Ví dụ: The restaurant owner commissioned a street artist to paint a colorful scene of Vietnamese street food on the back wall."
                            },
                            {
                                "targetVocab": "gallery",
                                "prompt": "Hãy dùng từ 'gallery' để viết một câu về nơi trưng bày nghệ thuật. Ví dụ: The gallery hosted a special night where visitors could watch street artists create live paintings."
                            },
                            {
                                "targetVocab": "anonymous",
                                "prompt": "Hãy dùng từ 'anonymous' để viết một câu về sự ẩn danh trong nghệ thuật. Ví dụ: The anonymous letter left at the gallery praised the exhibition and promised a generous donation."
                            },
                            {
                                "targetVocab": "provocative",
                                "prompt": "Hãy dùng từ 'provocative' để viết một câu về tác phẩm gây tranh cãi. Ví dụ: The provocative poster on the bus stop made commuters stop and think about plastic waste in the ocean."
                            },
                            {
                                "targetVocab": "urban",
                                "prompt": "Hãy dùng từ 'urban' để viết một câu về đời sống hoặc không gian thành thị. Ví dụ: Urban parks provide a green escape for city residents who rarely see trees or open sky."
                            },
                            {
                                "targetVocab": "installation",
                                "prompt": "Hãy dùng từ 'installation' để viết một câu về tác phẩm nghệ thuật không gian. Ví dụ: The light installation in the tunnel turned a dark, scary passage into a magical walkway."
                            },
                            {
                                "targetVocab": "curator",
                                "prompt": "Hãy dùng từ 'curator' để viết một câu về người tổ chức triển lãm. Ví dụ: The curator carefully selected works that showed the evolution of street art from the 1970s to today."
                            },
                            {
                                "targetVocab": "gentrification",
                                "prompt": "Hãy dùng từ 'gentrification' để viết một câu về sự thay đổi kinh tế của một khu phố. Ví dụ: Gentrification brought new cafes and boutiques to the area, but the original residents could no longer pay the rising rent."
                            },
                            {
                                "targetVocab": "aesthetic",
                                "prompt": "Hãy dùng từ 'aesthetic' để viết một câu về phong cách thẩm mỹ. Ví dụ: The minimalist aesthetic of the new coffee shop attracted young people who loved clean lines and natural light."
                            },
                            {
                                "targetVocab": "subculture",
                                "prompt": "Hãy dùng từ 'subculture' để viết một câu về một nhóm văn hóa đặc biệt. Ví dụ: The street dance subculture in Ho Chi Minh City has grown rapidly, with competitions held every weekend."
                            },
                            {
                                "targetVocab": "activism",
                                "prompt": "Hãy dùng từ 'activism' để viết một câu về việc dùng hành động để thay đổi xã hội. Ví dụ: Student activism on social media helped raise awareness about the importance of protecting old buildings in Hanoi."
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
                            "Chào mừng bạn đến với phần cuối cùng của Street Art Revolution! "
                            "Đây là khoảnh khắc mà mọi thứ bạn đã học được kết nối lại.\n\n"
                            "Trong bài đọc tổng hợp này, bạn sẽ gặp lại tất cả 18 từ vựng: "
                            "graffiti, mural, vandalism, canvas, spray, tag, stencil, commission, gallery, "
                            "anonymous, provocative, urban, installation, curator, gentrification, aesthetic, "
                            "subculture, và activism. Bài đọc kể câu chuyện về một nghệ sĩ đường phố trẻ ở Việt Nam "
                            "và hành trình của cô ấy từ những bức tag đầu tiên đến triển lãm quốc tế.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ vựng được sử dụng trong ngữ cảnh, "
                            "và thưởng thức câu chuyện. Sau bài đọc, bạn sẽ viết một đoạn văn "
                            "chia sẻ suy nghĩ của mình về nghệ thuật đường phố. Bắt đầu nhé!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Cách mạng trên những bức tường",
                    "description": "A complete article about a young Vietnamese street artist's journey from tags to galleries.",
                    "data": {
                        "text": (
                            "Linh started with a tag. She was sixteen, armed with nothing but a marker and a restless need "
                            "to leave her mark on the world. Her tag — a small lotus flower with sharp edges — appeared "
                            "on walls, bridges, and bus stops across Da Nang. The police called it vandalism. "
                            "Her parents called it a phase. But Linh called it freedom.\n\n"
                            "By eighteen, she had moved from tags to graffiti. She saved money from her part-time job "
                            "at a noodle shop to buy spray paint. Every weekend, she would find an abandoned wall "
                            "and turn it into her canvas. She sprayed portraits of elderly street vendors, "
                            "fishermen mending nets, and children chasing dragonflies. The city was her gallery, "
                            "and every passerby was her audience.\n\n"
                            "One night, she discovered stencil art through an online video about Banksy. "
                            "The technique changed everything. With a stencil, she could create detailed images "
                            "in minutes instead of hours. She cut her first stencil from a pizza box — "
                            "a woman's face with flowers growing from her hair. By morning, the image appeared "
                            "on seven different walls across the city.\n\n"
                            "Her work was provocative. One mural showed a construction crane demolishing a traditional house "
                            "while a grandmother watched from the sidewalk. Another showed smartphones growing from a rice field "
                            "like strange metal plants. The images forced people to stop and think about what their city "
                            "was becoming. Some residents loved the murals. Others demanded they be removed.\n\n"
                            "Then something unexpected happened. A curator from Ho Chi Minh City saw photographs "
                            "of Linh's work on social media. He was organizing an exhibition about urban art in Southeast Asia "
                            "and wanted to include her pieces. For the first time, an anonymous street artist "
                            "had to decide whether to reveal her identity.\n\n"
                            "Linh agreed to participate but kept her real name hidden. She created an installation "
                            "for the exhibition — a room filled with crumbling brick walls covered in her stencil art, "
                            "with the sound of traffic and street vendors playing from hidden speakers. "
                            "Visitors said it felt like stepping into a living street. The installation was the most "
                            "talked-about piece in the entire show.\n\n"
                            "After the exhibition, the Da Nang city government commissioned Linh to paint a series "
                            "of murals along the Han River. It was the first time the city officially recognized "
                            "street art as legitimate public art. The commission paid enough for Linh to quit her noodle shop job "
                            "and focus on art full-time.\n\n"
                            "But success brought complications. As more artists followed Linh's path, "
                            "the neighborhoods where they worked began to change. Tourists came to photograph the murals. "
                            "New cafes opened with carefully designed aesthetic interiors inspired by street art. "
                            "Rent prices climbed. Gentrification turned the artists' favorite streets "
                            "into places they could barely afford to visit, let alone live in.\n\n"
                            "Linh watched the subculture she loved transform into a commercial industry. "
                            "What began as rebellion was now being sold on tote bags and phone cases. "
                            "She felt torn between gratitude for the recognition and grief for what was lost.\n\n"
                            "Today, Linh uses her platform for activism. Her latest project is a series of murals "
                            "in low-income neighborhoods — not to attract tourists, but to give residents a voice. "
                            "Each mural is designed with the community, telling their stories in their colors. "
                            "She does not sign these works. The community is the artist.\n\n"
                            "When asked if street art is vandalism or art, Linh smiles and says: "
                            "'It is neither. It is a conversation between the city and the people who live in it. "
                            "And conversations do not need permission.'"
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Nói: Cách mạng trên những bức tường",
                    "description": "Luyện đọc to bài đọc tổng hợp về hành trình của Linh.",
                    "data": {
                        "text": (
                            "Linh started with a tag. She was sixteen, armed with nothing but a marker and a restless need "
                            "to leave her mark on the world. Her tag — a small lotus flower with sharp edges — appeared "
                            "on walls, bridges, and bus stops across Da Nang. The police called it vandalism. "
                            "Her parents called it a phase. But Linh called it freedom.\n\n"
                            "By eighteen, she had moved from tags to graffiti. She saved money from her part-time job "
                            "at a noodle shop to buy spray paint. Every weekend, she would find an abandoned wall "
                            "and turn it into her canvas. She sprayed portraits of elderly street vendors, "
                            "fishermen mending nets, and children chasing dragonflies. The city was her gallery, "
                            "and every passerby was her audience.\n\n"
                            "One night, she discovered stencil art through an online video about Banksy. "
                            "The technique changed everything. With a stencil, she could create detailed images "
                            "in minutes instead of hours. She cut her first stencil from a pizza box — "
                            "a woman's face with flowers growing from her hair. By morning, the image appeared "
                            "on seven different walls across the city.\n\n"
                            "Her work was provocative. One mural showed a construction crane demolishing a traditional house "
                            "while a grandmother watched from the sidewalk. Another showed smartphones growing from a rice field "
                            "like strange metal plants. The images forced people to stop and think about what their city "
                            "was becoming. Some residents loved the murals. Others demanded they be removed.\n\n"
                            "Then something unexpected happened. A curator from Ho Chi Minh City saw photographs "
                            "of Linh's work on social media. He was organizing an exhibition about urban art in Southeast Asia "
                            "and wanted to include her pieces. For the first time, an anonymous street artist "
                            "had to decide whether to reveal her identity.\n\n"
                            "Linh agreed to participate but kept her real name hidden. She created an installation "
                            "for the exhibition — a room filled with crumbling brick walls covered in her stencil art, "
                            "with the sound of traffic and street vendors playing from hidden speakers. "
                            "Visitors said it felt like stepping into a living street. The installation was the most "
                            "talked-about piece in the entire show.\n\n"
                            "After the exhibition, the Da Nang city government commissioned Linh to paint a series "
                            "of murals along the Han River. It was the first time the city officially recognized "
                            "street art as legitimate public art. The commission paid enough for Linh to quit her noodle shop job "
                            "and focus on art full-time.\n\n"
                            "But success brought complications. As more artists followed Linh's path, "
                            "the neighborhoods where they worked began to change. Tourists came to photograph the murals. "
                            "New cafes opened with carefully designed aesthetic interiors inspired by street art. "
                            "Rent prices climbed. Gentrification turned the artists' favorite streets "
                            "into places they could barely afford to visit, let alone live in.\n\n"
                            "Linh watched the subculture she loved transform into a commercial industry. "
                            "What began as rebellion was now being sold on tote bags and phone cases. "
                            "She felt torn between gratitude for the recognition and grief for what was lost.\n\n"
                            "Today, Linh uses her platform for activism. Her latest project is a series of murals "
                            "in low-income neighborhoods — not to attract tourists, but to give residents a voice. "
                            "Each mural is designed with the community, telling their stories in their colors. "
                            "She does not sign these works. The community is the artist.\n\n"
                            "When asked if street art is vandalism or art, Linh smiles and says: "
                            "'It is neither. It is a conversation between the city and the people who live in it. "
                            "And conversations do not need permission.'"
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Cách mạng trên những bức tường",
                    "description": "Nghe và theo dõi bài đọc tổng hợp về hành trình của Linh.",
                    "data": {
                        "text": (
                            "Linh started with a tag. She was sixteen, armed with nothing but a marker and a restless need "
                            "to leave her mark on the world. Her tag — a small lotus flower with sharp edges — appeared "
                            "on walls, bridges, and bus stops across Da Nang. The police called it vandalism. "
                            "Her parents called it a phase. But Linh called it freedom.\n\n"
                            "By eighteen, she had moved from tags to graffiti. She saved money from her part-time job "
                            "at a noodle shop to buy spray paint. Every weekend, she would find an abandoned wall "
                            "and turn it into her canvas. She sprayed portraits of elderly street vendors, "
                            "fishermen mending nets, and children chasing dragonflies. The city was her gallery, "
                            "and every passerby was her audience.\n\n"
                            "One night, she discovered stencil art through an online video about Banksy. "
                            "The technique changed everything. With a stencil, she could create detailed images "
                            "in minutes instead of hours. She cut her first stencil from a pizza box — "
                            "a woman's face with flowers growing from her hair. By morning, the image appeared "
                            "on seven different walls across the city.\n\n"
                            "Her work was provocative. One mural showed a construction crane demolishing a traditional house "
                            "while a grandmother watched from the sidewalk. Another showed smartphones growing from a rice field "
                            "like strange metal plants. The images forced people to stop and think about what their city "
                            "was becoming. Some residents loved the murals. Others demanded they be removed.\n\n"
                            "Then something unexpected happened. A curator from Ho Chi Minh City saw photographs "
                            "of Linh's work on social media. He was organizing an exhibition about urban art in Southeast Asia "
                            "and wanted to include her pieces. For the first time, an anonymous street artist "
                            "had to decide whether to reveal her identity.\n\n"
                            "Linh agreed to participate but kept her real name hidden. She created an installation "
                            "for the exhibition — a room filled with crumbling brick walls covered in her stencil art, "
                            "with the sound of traffic and street vendors playing from hidden speakers. "
                            "Visitors said it felt like stepping into a living street. The installation was the most "
                            "talked-about piece in the entire show.\n\n"
                            "After the exhibition, the Da Nang city government commissioned Linh to paint a series "
                            "of murals along the Han River. It was the first time the city officially recognized "
                            "street art as legitimate public art. The commission paid enough for Linh to quit her noodle shop job "
                            "and focus on art full-time.\n\n"
                            "But success brought complications. As more artists followed Linh's path, "
                            "the neighborhoods where they worked began to change. Tourists came to photograph the murals. "
                            "New cafes opened with carefully designed aesthetic interiors inspired by street art. "
                            "Rent prices climbed. Gentrification turned the artists' favorite streets "
                            "into places they could barely afford to visit, let alone live in.\n\n"
                            "Linh watched the subculture she loved transform into a commercial industry. "
                            "What began as rebellion was now being sold on tote bags and phone cases. "
                            "She felt torn between gratitude for the recognition and grief for what was lost.\n\n"
                            "Today, Linh uses her platform for activism. Her latest project is a series of murals "
                            "in low-income neighborhoods — not to attract tourists, but to give residents a voice. "
                            "Each mural is designed with the community, telling their stories in their colors. "
                            "She does not sign these works. The community is the artist.\n\n"
                            "When asked if street art is vandalism or art, Linh smiles and says: "
                            "'It is neither. It is a conversation between the city and the people who live in it. "
                            "And conversations do not need permission.'"
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết đoạn văn: Nghệ thuật đường phố và xã hội",
                    "description": "Viết đoạn văn sử dụng từ vựng về nghệ thuật đường phố, gentrification và activism.",
                    "data": {
                        "vocabList": all_words,
                        "instructions": (
                            "Viết một đoạn văn ngắn (80-120 từ) bằng tiếng Anh về chủ đề nghệ thuật đường phố "
                            "và tác động của nó đến xã hội. Hãy sử dụng ít nhất 6 từ vựng từ danh sách. "
                            "Bạn có thể viết về trải nghiệm cá nhân với street art, về câu chuyện của Linh, "
                            "hoặc về quan điểm của bạn về ranh giới giữa nghệ thuật và phá hoại."
                        ),
                        "prompts": [
                            "Trong bài đọc, Linh bắt đầu với những bức tag bất hợp pháp và cuối cùng được commission vẽ mural chính thức. Hành trình này cho thấy ranh giới giữa vandalism và art có thể thay đổi theo thời gian. Theo bạn, điều gì quyết định khi nào graffiti là phá hoại và khi nào là nghệ thuật? Hãy dùng ví dụ từ bài đọc hoặc cuộc sống thật.",
                            "Bài đọc nêu lên nghịch lý của gentrification: nghệ thuật làm đẹp khu phố nhưng cũng đẩy cư dân gốc ra ngoài. Linh chuyển sang activism để giải quyết vấn đề này. Bạn nghĩ street art nên phục vụ ai — khách du lịch, gallery, hay cộng đồng địa phương? Tại sao?",
                            "Linh chọn giữ anonymous khi tham gia triển lãm. Nhiều nghệ sĩ đường phố tin rằng tác phẩm nên nói thay cho nghệ sĩ. Bạn đồng ý hay không? Sự ẩn danh giúp hay cản trở nghệ thuật đường phố?"
                        ]
                    }
                },
                # Farewell tone: introspective guide
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần suy ngẫm.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành Street Art Revolution. Trước khi chia tay, hãy dành một phút "
                            "nhìn lại những gì bạn đã học — không chỉ từ vựng, mà cả cách nhìn nhận thế giới xung quanh.\n\n"
                            "Hãy cùng ôn lại 6 từ vựng quan trọng nhất.\n\n"
                            "'Mural' — một bức tranh lớn vẽ trực tiếp lên tường. "
                            "Ví dụ mới: The mural on the old library wall tells the story of the neighborhood's immigrant families "
                            "through vibrant colors and symbolic images. "
                            "Lần tới khi bạn thấy một bức tranh tường, hãy dừng lại và tự hỏi: ai đã vẽ nó, và tại sao?\n\n"
                            "'Provocative' — gây tranh cãi, kích thích suy nghĩ. "
                            "Ví dụ mới: The most provocative art does not give you answers — it forces you to ask better questions. "
                            "Nghệ thuật tốt nhất không bao giờ để bạn thờ ơ.\n\n"
                            "'Anonymous' — ẩn danh, không ai biết danh tính. "
                            "Ví dụ mới: An anonymous volunteer left fresh flowers at the memorial every morning for three years "
                            "before anyone discovered who it was. "
                            "Đôi khi, hành động đẹp nhất là hành động không cần ai biết tên.\n\n"
                            "'Gentrification' — quá trình khu phố nghèo bị biến đổi khi giá nhà tăng. "
                            "Ví dụ mới: Gentrification is a double-edged sword — it brings investment and improvement, "
                            "but it also erases the history and community that made the neighborhood special in the first place. "
                            "Đây là một trong những vấn đề phức tạp nhất của đô thị hóa.\n\n"
                            "'Subculture' — nhóm văn hóa nhỏ với giá trị và phong cách riêng. "
                            "Ví dụ mới: Every city has subcultures hiding in plain sight — from the midnight runners "
                            "who jog through empty streets to the rooftop gardeners who grow vegetables above the traffic. "
                            "Bạn thuộc về subculture nào?\n\n"
                            "'Activism' — hoạt động vận động để thay đổi xã hội. "
                            "Ví dụ mới: Activism does not always mean marching in the streets — sometimes it means "
                            "painting a mural that makes your neighbor see the world differently. "
                            "Linh đã chứng minh rằng một lon sơn có thể mạnh mẽ hơn một bài diễn thuyết.\n\n"
                            "Bạn bắt đầu bài học này với câu hỏi: nghệ thuật đường phố là phá hoại hay là tiếng nói? "
                            "Bây giờ, sau 18 từ vựng và 3 bài đọc, có lẽ bạn nhận ra câu trả lời không đơn giản. "
                            "Và đó chính là điều đẹp nhất — khi bạn học một ngôn ngữ mới, "
                            "bạn không chỉ học từ vựng, bạn học cách nhìn thế giới từ nhiều góc độ hơn.\n\n"
                            "Lần tới khi bạn đi ngang một bức tường đầy màu sắc, hãy dừng lại. "
                            "Nhìn kỹ hơn. Đọc thông điệp. Và tự hỏi: bức tường này đang nói gì với mình?\n\n"
                            "Cảm ơn bạn đã đồng hành. Hẹn gặp lại ở bài học tiếp theo!"
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
validate_bilingual_prompts(content, "preintermediate")
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
