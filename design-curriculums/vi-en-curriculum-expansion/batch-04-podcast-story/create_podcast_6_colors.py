import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from firebase_token import get_firebase_id_token
from validate_curriculum import (
    validate_balanced_skills_standard,
    validate_content_type_tags,
    validate_bilingual_prompts,
)

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Curriculum #46: Radiolab: Colors
# Level: intermediate | Skill focus: balanced_skills | Content type: ["podcast"]
# Topic: Arts | 18 words (3 groups of 6), 5 sessions, bilingual (vi-en)
# Description tone: metaphor_led (completing the full palette for podcast series)
# Farewell tone: introspective_guide (cycling back, different from Sports' quiet_awe)
# W1: spectrum, pigment, hue, shade, palette, canvas
# W2: perception, wavelength, vibrant, contrast, saturate, tint
# W3: illuminate, prism, gradient, opaque, translucent, aesthetic

content = {
    "title": "Radiolab: Colors",
    "contentTypeTags": ["podcast"],
    "description": "MÀU SẮC LÀ NGÔN NGỮ MÀ MẮT BẠN NÓI NHƯNG NÃO BẠN PHẢI DỊCH — VÀ KHÔNG PHẢI AI CŨNG DỊCH GIỐNG NHAU.\n\nBạn nhìn bầu trời và nói 'xanh.' Nhưng liệu 'xanh' của bạn có giống 'xanh' của người ngồi cạnh? Câu trả lời phức tạp hơn bạn tưởng. Mỗi spectrum ánh sáng đi qua mắt bạn được não bộ giải mã theo cách riêng — bị ảnh hưởng bởi ngôn ngữ, văn hóa, và thậm chí cả cảm xúc. Người Nhật có hai từ riêng cho hai shade xanh dương mà người Việt gọi chung là một. Người Himba ở Namibia nhìn thấy sự khác biệt giữa các hue xanh lá mà mắt bạn hoàn toàn bỏ qua.\n\nHãy nghĩ về màu sắc như một tấm canvas — bề mặt trống mà mỗi nền văn hóa vẽ lên theo cách riêng. Pigment trên palette của họa sĩ Phục Hưng khác hoàn toàn với pigment trên màn hình điện thoại bạn, nhưng cả hai đều cố gắng bắt lấy cùng một thứ: perception — cách con người cảm nhận thế giới qua ánh sáng.\n\nHai nhân vật Hà và Minh sẽ dẫn bạn vào hành trình khám phá — từ cách wavelength ánh sáng tạo ra màu sắc, đến cách nghệ sĩ dùng contrast và gradient để đánh lừa mắt bạn, đến lý do tại sao một số vật thể opaque trong khi những vật khác translucent. Hà là sinh viên mỹ thuật đam mê hội họa, còn Minh là sinh viên vật lý muốn hiểu khoa học đằng sau vẻ đẹp.\n\n18 từ vựng trong bài học này — từ spectrum đến aesthetic — sẽ giúp bạn nói về nghệ thuật, khoa học, và cách chúng ta nhìn thế giới bằng tiếng Anh một cách tinh tế và sâu sắc.",
    "preview": {
        "text": "What if the colors you see are not the same colors everyone else sees? In this podcast-inspired lesson, you will learn 18 English words about the science and art of color: spectrum, pigment, hue, shade, palette, canvas, perception, wavelength, vibrant, contrast, saturate, tint, illuminate, prism, gradient, opaque, translucent, and aesthetic. Follow Hà and Minh as they explore how light becomes color, why different cultures perceive colors differently, and how artists manipulate color to create emotion. Hà is an art student passionate about painting, while Minh studies physics and wants to understand the science behind beauty. Through three conversational reading passages, a full review session, and a final combined reading, you will discover the hidden world of color perception. By the end, you will be able to discuss art techniques, explain how light and color work, and describe visual experiences — all in English."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng — Khoa học và nghệ thuật của màu sắc",
                    "description": "Giới thiệu chủ đề màu sắc và tổng quan bài học.",
                    "data": {
                        "text": "Chào mừng bạn đến với Radiolab: Colors — bài học podcast tiếng Anh về một chủ đề mà bạn nhìn thấy mỗi ngày nhưng hiếm khi thực sự suy nghĩ về nó: màu sắc. Bạn có biết rằng con người có thể phân biệt khoảng mười triệu màu khác nhau không? Nhưng điều kỳ lạ là — không phải ai cũng nhìn thấy cùng một màu theo cùng một cách. Ngôn ngữ, văn hóa, và thậm chí cả cảm xúc đều ảnh hưởng đến cách chúng ta cảm nhận màu sắc.\n\nBài học này có 18 từ vựng chia thành 3 phần. Trong phần 1, bạn sẽ học 6 từ đầu tiên: spectrum, pigment, hue, shade, palette, và canvas. Đây là những từ về nền tảng của màu sắc — từ vật liệu mà họa sĩ dùng đến cách chúng ta đặt tên cho các sắc thái khác nhau."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Dạy 6 từ vựng: spectrum, pigment, hue, shade, palette, canvas.",
                    "data": {
                        "text": "Hãy cùng tìm hiểu 6 từ vựng đầu tiên nhé.\n\nTừ đầu tiên là spectrum — danh từ — nghĩa là quang phổ, dải màu. Spectrum là dải đầy đủ các màu sắc mà ánh sáng trắng tạo ra khi đi qua lăng kính — từ đỏ đến tím. Ví dụ: 'When sunlight passes through a glass prism, it separates into the full spectrum of visible colors.' Trong bài đọc, Minh giải thích rằng mắt người chỉ nhìn thấy một phần nhỏ của toàn bộ spectrum ánh sáng.\n\nTừ thứ hai là pigment — danh từ — nghĩa là sắc tố, chất tạo màu. Pigment là chất hóa học tạo ra màu sắc — có thể là tự nhiên như đất son, hoặc nhân tạo như sơn acrylic. Ví dụ: 'Ancient Egyptian artists ground minerals into fine pigments to create paints that have lasted thousands of years.' Trong bài đọc, Hà kể rằng pigment đắt nhất trong lịch sử là ultramarine — được làm từ đá lapis lazuli nghiền nhỏ.\n\nTừ thứ ba là hue — danh từ — nghĩa là sắc, màu. Hue là tên gọi thuần túy của một màu — đỏ, xanh, vàng — không tính đến độ sáng hay độ đậm. Ví dụ: 'The artist chose a warm hue of orange for the sunset, creating a feeling of peace and nostalgia.' Trong bài đọc, Hà giải thích rằng hue là cách chính xác nhất để nói về màu sắc trong nghệ thuật.\n\nTừ thứ tư là shade — danh từ — nghĩa là sắc thái, tông màu tối. Shade là khi bạn thêm đen vào một màu để làm nó tối hơn — ngược lại với tint. Ví dụ: 'The painter mixed several shades of blue to create the illusion of deep ocean water.' Trong bài đọc, Minh ngạc nhiên khi biết rằng có hàng trăm shade của mỗi màu mà mắt người có thể phân biệt.\n\nTừ thứ năm là palette — danh từ — nghĩa là bảng màu, bảng pha màu. Palette vừa là tấm bảng vật lý mà họa sĩ dùng để trộn sơn, vừa là tập hợp các màu được chọn cho một tác phẩm. Ví dụ: 'Picasso's Blue Period is famous for its limited palette of cold blues and grays that express deep sadness.' Trong bài đọc, Hà nói rằng việc chọn palette là quyết định quan trọng nhất của họa sĩ.\n\nTừ cuối cùng là canvas — danh từ — nghĩa là toan vẽ, bức vải. Canvas là bề mặt vải mà họa sĩ vẽ lên — nhưng cũng được dùng theo nghĩa bóng để chỉ bất kỳ không gian sáng tạo nào. Ví dụ: 'The artist stood before a blank canvas, imagining the landscape she was about to bring to life.' Trong bài đọc, Hà nói rằng canvas trống là cả cơ hội lẫn thách thức — vì mọi khả năng đều mở ra trước mắt.\n\nSáu từ đầu tiên đã sẵn sàng! Hãy bắt đầu với flashcard, rồi đọc cuộc trò chuyện giữa Hà và Minh về nền tảng của màu sắc nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng của màu sắc",
                    "description": "Học 6 từ: spectrum, pigment, hue, shade, palette, canvas",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng của màu sắc",
                    "description": "Học 6 từ: spectrum, pigment, hue, shade, palette, canvas",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng của màu sắc",
                    "description": "Học 6 từ: spectrum, pigment, hue, shade, palette, canvas",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng của màu sắc",
                    "description": "Học 6 từ: spectrum, pigment, hue, shade, palette, canvas",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 1",
                    "description": "Giới thiệu ngữ pháp và cách dùng từ vựng trong ngữ cảnh bài đọc.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc cuộc trò chuyện giữa Hà và Minh. Hà là sinh viên mỹ thuật đam mê hội họa — cô ấy dành hàng giờ trong xưởng vẽ mỗi ngày. Minh là sinh viên vật lý muốn hiểu khoa học đằng sau vẻ đẹp — anh ấy luôn tò mò về cách ánh sáng và mắt người tương tác. Trong bài đọc này, họ nói về nền tảng của màu sắc — spectrum ánh sáng, pigment trong sơn, và cách họa sĩ chọn palette. Hãy chú ý cách các từ spectrum, pigment, hue, shade, palette, và canvas được dùng trong câu chuyện nhé. Một điểm ngữ pháp quan trọng: khi mô tả quá trình hoặc cách thức, chúng ta dùng mệnh đề quan hệ — ví dụ 'the pigment that artists use' hoặc 'the spectrum which contains all visible colors.' Hãy đọc chậm và chú ý nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nền tảng của màu sắc — Từ ánh sáng đến sơn",
                    "description": "Hà and Minh discuss the fundamentals of color — from the light spectrum to the artist's palette.",
                    "data": {
                        "text": "Hà and Minh are sitting in the art studio at their university in Hanoi. Hà is mixing paints on a wooden palette while Minh watches with curiosity.\n\n'I have a question,' Minh says. 'Where does color actually come from? Is it in the object, or is it in the light?'\n\nHà smiles. 'That is one of the oldest questions in both art and science. The short answer is — it is in the light. White light from the sun contains the entire spectrum of visible colors. When light hits an object, the object absorbs some wavelengths and reflects others. The wavelengths that bounce back to your eyes are what you perceive as color.'\n\n'So a red apple is not actually red?' Minh asks.\n\n'Not exactly,' Hà says. 'The apple absorbs every color in the spectrum except red. It reflects the red wavelengths back to your eyes. Your brain then interprets those wavelengths as the hue we call red. The color is not in the apple — it is in the interaction between light, the object, and your brain.'\n\n'That is fascinating,' Minh says. 'So what about paint? How do artists create color?'\n\n'Paint works differently from light,' Hà explains, holding up a tube of blue paint. 'This contains pigment — tiny particles of colored material suspended in a liquid. Historically, pigments came from natural sources. Red came from iron oxide in the earth. Blue came from grinding lapis lazuli stones. Yellow came from saffron or certain minerals. Each pigment absorbs and reflects light differently, which is what gives it its specific hue.'\n\n'Were some pigments more valuable than others?' Minh asks.\n\n'Absolutely,' Hà says. 'Ultramarine blue — made from lapis lazuli — was more expensive than gold during the Renaissance. Artists had to use it sparingly. That is why in many old paintings, only the most important figures wear blue. The Virgin Mary is almost always painted in ultramarine because the pigment was so precious that it was reserved for the most sacred subjects.'\n\n'So the economics of pigment actually shaped art history,' Minh says.\n\n'Exactly. And that brings us to the palette,' Hà says, gesturing to the wooden board in her hand. 'A palette is both a physical tool and a creative decision. When I choose my palette for a painting, I am deciding which hues and shades I will work with. A limited palette — maybe just three or four colors — can create a powerful, unified feeling. A wide palette gives more variety but can also feel chaotic if not controlled.'\n\n'What about the canvas?' Minh asks, pointing to the blank white surface on the easel.\n\n'The canvas is where everything comes together,' Hà says. 'It is just a piece of stretched fabric, but it represents possibility. Every shade I mix, every hue I choose, every stroke of pigment — it all happens on this canvas. Some artists find a blank canvas exciting. Others find it terrifying. I find it both.'\n\nMinh looks at the spectrum of colors on Hà's palette. 'I never realized how much science is hidden inside art.'\n\n'And I never realized how much art is hidden inside science,' Hà replies. 'The spectrum is beautiful precisely because it follows the laws of physics.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nền tảng của màu sắc — Từ ánh sáng đến sơn",
                    "description": "Hà and Minh discuss the fundamentals of color — from the light spectrum to the artist's palette.",
                    "data": {
                        "text": "Hà and Minh are sitting in the art studio at their university in Hanoi. Hà is mixing paints on a wooden palette while Minh watches with curiosity.\n\n'I have a question,' Minh says. 'Where does color actually come from? Is it in the object, or is it in the light?'\n\nHà smiles. 'That is one of the oldest questions in both art and science. The short answer is — it is in the light. White light from the sun contains the entire spectrum of visible colors. When light hits an object, the object absorbs some wavelengths and reflects others. The wavelengths that bounce back to your eyes are what you perceive as color.'\n\n'So a red apple is not actually red?' Minh asks.\n\n'Not exactly,' Hà says. 'The apple absorbs every color in the spectrum except red. It reflects the red wavelengths back to your eyes. Your brain then interprets those wavelengths as the hue we call red. The color is not in the apple — it is in the interaction between light, the object, and your brain.'\n\n'That is fascinating,' Minh says. 'So what about paint? How do artists create color?'\n\n'Paint works differently from light,' Hà explains, holding up a tube of blue paint. 'This contains pigment — tiny particles of colored material suspended in a liquid. Historically, pigments came from natural sources. Red came from iron oxide in the earth. Blue came from grinding lapis lazuli stones. Yellow came from saffron or certain minerals. Each pigment absorbs and reflects light differently, which is what gives it its specific hue.'\n\n'Were some pigments more valuable than others?' Minh asks.\n\n'Absolutely,' Hà says. 'Ultramarine blue — made from lapis lazuli — was more expensive than gold during the Renaissance. Artists had to use it sparingly. That is why in many old paintings, only the most important figures wear blue. The Virgin Mary is almost always painted in ultramarine because the pigment was so precious that it was reserved for the most sacred subjects.'\n\n'So the economics of pigment actually shaped art history,' Minh says.\n\n'Exactly. And that brings us to the palette,' Hà says, gesturing to the wooden board in her hand. 'A palette is both a physical tool and a creative decision. When I choose my palette for a painting, I am deciding which hues and shades I will work with. A limited palette — maybe just three or four colors — can create a powerful, unified feeling. A wide palette gives more variety but can also feel chaotic if not controlled.'\n\n'What about the canvas?' Minh asks, pointing to the blank white surface on the easel.\n\n'The canvas is where everything comes together,' Hà says. 'It is just a piece of stretched fabric, but it represents possibility. Every shade I mix, every hue I choose, every stroke of pigment — it all happens on this canvas. Some artists find a blank canvas exciting. Others find it terrifying. I find it both.'\n\nMinh looks at the spectrum of colors on Hà's palette. 'I never realized how much science is hidden inside art.'\n\n'And I never realized how much art is hidden inside science,' Hà replies. 'The spectrum is beautiful precisely because it follows the laws of physics.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nền tảng của màu sắc — Từ ánh sáng đến sơn",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Hà and Minh are sitting in the art studio at their university in Hanoi. Hà is mixing paints on a wooden palette while Minh watches with curiosity.\n\n'I have a question,' Minh says. 'Where does color actually come from? Is it in the object, or is it in the light?'\n\nHà smiles. 'That is one of the oldest questions in both art and science. The short answer is — it is in the light. White light from the sun contains the entire spectrum of visible colors. When light hits an object, the object absorbs some wavelengths and reflects others. The wavelengths that bounce back to your eyes are what you perceive as color.'\n\n'So a red apple is not actually red?' Minh asks.\n\n'Not exactly,' Hà says. 'The apple absorbs every color in the spectrum except red. It reflects the red wavelengths back to your eyes. Your brain then interprets those wavelengths as the hue we call red. The color is not in the apple — it is in the interaction between light, the object, and your brain.'\n\n'That is fascinating,' Minh says. 'So what about paint? How do artists create color?'\n\n'Paint works differently from light,' Hà explains, holding up a tube of blue paint. 'This contains pigment — tiny particles of colored material suspended in a liquid. Historically, pigments came from natural sources. Red came from iron oxide in the earth. Blue came from grinding lapis lazuli stones. Yellow came from saffron or certain minerals. Each pigment absorbs and reflects light differently, which is what gives it its specific hue.'\n\n'Were some pigments more valuable than others?' Minh asks.\n\n'Absolutely,' Hà says. 'Ultramarine blue — made from lapis lazuli — was more expensive than gold during the Renaissance. Artists had to use it sparingly. That is why in many old paintings, only the most important figures wear blue. The Virgin Mary is almost always painted in ultramarine because the pigment was so precious that it was reserved for the most sacred subjects.'\n\n'So the economics of pigment actually shaped art history,' Minh says.\n\n'Exactly. And that brings us to the palette,' Hà says, gesturing to the wooden board in her hand. 'A palette is both a physical tool and a creative decision. When I choose my palette for a painting, I am deciding which hues and shades I will work with. A limited palette — maybe just three or four colors — can create a powerful, unified feeling. A wide palette gives more variety but can also feel chaotic if not controlled.'\n\n'What about the canvas?' Minh asks, pointing to the blank white surface on the easel.\n\n'The canvas is where everything comes together,' Hà says. 'It is just a piece of stretched fabric, but it represents possibility. Every shade I mix, every hue I choose, every stroke of pigment — it all happens on this canvas. Some artists find a blank canvas exciting. Others find it terrifying. I find it both.'\n\nMinh looks at the spectrum of colors on Hà's palette. 'I never realized how much science is hidden inside art.'\n\n'And I never realized how much art is hidden inside science,' Hà replies. 'The spectrum is beautiful precisely because it follows the laws of physics.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng của màu sắc",
                    "description": "Viết câu sử dụng từ vựng về quang phổ, sắc tố, và bảng màu.",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas"],
                        "items": [
                            {
                                "targetVocab": "spectrum",
                                "prompt": "Hãy dùng từ 'spectrum' để viết một câu về dải màu sắc. Ví dụ: A rainbow displays the full spectrum of visible light, from deep red to violet."
                            },
                            {
                                "targetVocab": "pigment",
                                "prompt": "Hãy dùng từ 'pigment' để viết một câu về chất tạo màu. Ví dụ: Natural pigments from plants and minerals were the only source of color for artists before modern chemistry."
                            },
                            {
                                "targetVocab": "hue",
                                "prompt": "Hãy dùng từ 'hue' để viết một câu về sắc màu. Ví dụ: The designer selected a warm hue of gold to give the room a feeling of luxury and comfort."
                            },
                            {
                                "targetVocab": "shade",
                                "prompt": "Hãy dùng từ 'shade' để viết một câu về tông màu. Ví dụ: The ocean changes through dozens of shades of blue depending on the depth and the angle of sunlight."
                            },
                            {
                                "targetVocab": "palette",
                                "prompt": "Hãy dùng từ 'palette' để viết một câu về bảng màu. Ví dụ: The film director worked with a muted palette of grays and browns to create a feeling of melancholy."
                            },
                            {
                                "targetVocab": "canvas",
                                "prompt": "Hãy dùng từ 'canvas' để viết một câu về toan vẽ hoặc không gian sáng tạo. Ví dụ: For a street artist, the entire city becomes a canvas where buildings and walls transform into works of art."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng phần 2 — Cảm nhận và sức mạnh của màu sắc",
                    "description": "Ôn lại phần 1 và giới thiệu chủ đề cảm nhận màu sắc và cách nghệ sĩ dùng màu.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với phần 2 của Radiolab: Colors! Trong phần trước, bạn đã học 6 từ vựng về nền tảng của màu sắc: spectrum là quang phổ — dải đầy đủ các màu trong ánh sáng trắng. Pigment là sắc tố — chất hóa học tạo ra màu sắc trong sơn. Hue là sắc — tên gọi thuần túy của một màu. Shade là sắc thái tối — khi thêm đen vào một màu. Palette là bảng màu — tập hợp các màu được chọn cho một tác phẩm. Và canvas là toan vẽ — bề mặt mà họa sĩ sáng tạo trên đó.\n\nBạn cũng đã đọc cuộc trò chuyện giữa Hà và Minh — Hà giải thích cách ánh sáng tạo ra màu sắc và cách pigment hoạt động trong hội họa.\n\nBây giờ, chúng ta sẽ đi sâu hơn vào cách con người cảm nhận màu sắc và cách nghệ sĩ dùng màu để tạo cảm xúc. Bạn sẽ học 6 từ mới: perception, wavelength, vibrant, contrast, saturate, và tint."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Dạy 6 từ vựng: perception, wavelength, vibrant, contrast, saturate, tint.",
                    "data": {
                        "text": "Hãy cùng học 6 từ mới nhé.\n\nTừ đầu tiên là perception — danh từ — nghĩa là sự cảm nhận, nhận thức. Perception là cách não bộ giải thích thông tin từ các giác quan — trong trường hợp màu sắc, đó là cách não bạn biến ánh sáng thành trải nghiệm thị giác. Ví dụ: 'Color perception varies between individuals — some people can distinguish millions of shades while others see a much narrower range.' Trong bài đọc, Minh khám phá rằng perception không chỉ phụ thuộc vào mắt mà còn vào ngôn ngữ và văn hóa.\n\nTừ thứ hai là wavelength — danh từ — nghĩa là bước sóng. Wavelength là khoảng cách giữa hai đỉnh sóng liên tiếp — trong ánh sáng, wavelength quyết định màu sắc mà mắt bạn nhìn thấy. Ví dụ: 'Red light has a longer wavelength than blue light, which is why the sky appears blue — shorter wavelengths scatter more easily.' Trong bài đọc, Minh giải thích rằng mỗi màu tương ứng với một wavelength cụ thể.\n\nTừ thứ ba là vibrant — tính từ — nghĩa là rực rỡ, sống động. Vibrant mô tả màu sắc mạnh mẽ, tươi sáng, đầy năng lượng — ngược lại với nhạt hoặc xỉn. Ví dụ: 'The vibrant colors of a tropical coral reef make it one of the most visually stunning ecosystems on Earth.' Trong bài đọc, Hà nói rằng màu vibrant thu hút sự chú ý và tạo cảm giác năng lượng.\n\nTừ thứ tư là contrast — danh từ và động từ — nghĩa là sự tương phản. Contrast là sự khác biệt rõ rệt giữa hai thứ đặt cạnh nhau — trong nghệ thuật, đó là cách dùng màu sáng và tối để tạo chiều sâu. Ví dụ: 'The photographer used strong contrast between light and shadow to create a dramatic portrait.' Trong bài đọc, Hà giải thích rằng contrast là công cụ mạnh nhất của họa sĩ để hướng mắt người xem.\n\nTừ thứ năm là saturate — động từ — nghĩa là bão hòa, làm đậm màu. Saturate là khi một màu ở mức độ đậm nhất, tinh khiết nhất — không bị pha loãng bởi trắng, đen, hoặc xám. Ví dụ: 'The artist chose to saturate the background with deep red to create a feeling of intensity and passion.' Trong bài đọc, Hà nói rằng mức độ saturate ảnh hưởng mạnh đến cảm xúc mà một bức tranh truyền tải.\n\nTừ cuối cùng là tint — danh từ và động từ — nghĩa là sắc nhạt, pha nhạt. Tint là khi bạn thêm trắng vào một màu để làm nó nhạt hơn — ngược lại với shade. Ví dụ: 'A soft tint of pink on the walls made the nursery feel warm and gentle.' Trong bài đọc, Hà giải thích rằng tint và shade là hai cách cơ bản để tạo ra hàng trăm biến thể từ một hue duy nhất.\n\nSáu từ mới đã sẵn sàng! Hãy luyện flashcard rồi đọc về cảm nhận và sức mạnh của màu sắc nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cảm nhận và sức mạnh của màu sắc",
                    "description": "Học 6 từ: perception, wavelength, vibrant, contrast, saturate, tint",
                    "data": {
                        "vocabList": ["perception", "wavelength", "vibrant", "contrast", "saturate", "tint"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cảm nhận và sức mạnh của màu sắc",
                    "description": "Học 6 từ: perception, wavelength, vibrant, contrast, saturate, tint",
                    "data": {
                        "vocabList": ["perception", "wavelength", "vibrant", "contrast", "saturate", "tint"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cảm nhận và sức mạnh của màu sắc",
                    "description": "Học 6 từ: perception, wavelength, vibrant, contrast, saturate, tint",
                    "data": {
                        "vocabList": ["perception", "wavelength", "vibrant", "contrast", "saturate", "tint"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cảm nhận và sức mạnh của màu sắc",
                    "description": "Học 6 từ: perception, wavelength, vibrant, contrast, saturate, tint",
                    "data": {
                        "vocabList": ["perception", "wavelength", "vibrant", "contrast", "saturate", "tint"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 2",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về cảm nhận màu sắc.",
                    "data": {
                        "text": "Bạn đã luyện xong flashcard rồi! Bây giờ hãy đọc cuộc trò chuyện tiếp theo giữa Hà và Minh. Lần này, họ nói về cách con người cảm nhận màu sắc khác nhau tùy theo văn hóa, và cách nghệ sĩ dùng contrast, tint, và saturate để tạo cảm xúc. Hãy chú ý cách các từ perception, wavelength, vibrant, contrast, saturate, và tint xuất hiện trong câu chuyện. Một điểm ngữ pháp: khi so sánh cách nhìn nhận khác nhau, chúng ta dùng 'while' và 'whereas' — ví dụ 'while English speakers use one word for blue, Russian speakers distinguish between light blue and dark blue.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tại sao chúng ta nhìn màu sắc khác nhau",
                    "description": "Hà and Minh explore how culture shapes color perception and how artists use color to create emotion.",
                    "data": {
                        "text": "The next day, Hà and Minh are walking through the Vietnam Fine Arts Museum in Hanoi. They stop in front of a large painting with vibrant reds and deep blues.\n\n'This painting makes me feel something strong,' Minh says. 'But I cannot explain why. Is it the subject, or is it the colors?'\n\n'It is mostly the colors,' Hà says. 'Artists have understood for centuries that color affects emotion. Warm colors like red and orange create feelings of energy and passion. Cool colors like blue and green create feelings of calm and distance. This painting uses vibrant, highly saturated reds to create intensity. If the artist had used a soft tint of pink instead, the feeling would be completely different.'\n\n'What do you mean by saturated?' Minh asks.\n\n'Saturation is how pure and intense a color is,' Hà explains. 'A fully saturated red is bold and powerful. When you add white to it, you get a tint — a softer, lighter version. When you add black, you get a shade — a darker, heavier version. When you add gray, you desaturate it — making it duller and more muted. Artists control emotion by controlling saturation.'\n\n'And contrast?' Minh asks, pointing to a section where bright yellow sits next to deep purple.\n\n'Contrast is the difference between elements,' Hà says. 'When you place a vibrant color next to a dark shade, the vibrant color appears even brighter. Your eye is drawn to the area of highest contrast. That is why this painting works — the artist placed the brightest red right next to the darkest blue, creating a focal point that your eye cannot ignore.'\n\nMinh thinks for a moment. 'You know, I listened to a Radiolab episode about color perception. They talked about how different cultures actually see colors differently.'\n\n'That is one of the most fascinating topics in color science,' Hà says. 'Tell me more.'\n\n'The episode explained that perception of color is not purely physical,' Minh says. 'Yes, wavelength determines what color light is — red has a longer wavelength around seven hundred nanometers, while violet has a shorter wavelength around four hundred nanometers. But how your brain categorizes those wavelengths depends on your language and culture.'\n\n'Can you give me an example?' Hà asks.\n\n'Russian speakers have two separate words for light blue and dark blue,' Minh says. 'They are not shades of the same color — they are completely different colors in Russian. And research shows that Russian speakers can actually distinguish between those two blues faster than English speakers, who use one word for both. Their language literally changes their perception.'\n\n'That is incredible,' Hà says. 'So the words we have for colors shape what we see?'\n\n'To some extent, yes,' Minh says. 'The Himba people in Namibia have many words for different hues of green but no separate word for blue. When researchers showed them a circle of green squares with one blue square, they had difficulty finding the blue one. But when shown a circle of green squares with one slightly different green, they found it instantly — something most English speakers cannot do.'\n\n'So our perception is filtered through language,' Hà says quietly. 'We think we see the world as it is, but we actually see it through the lens of the words we have.'\n\n'Exactly,' Minh says. 'Color is not just wavelength. It is wavelength plus brain plus language plus culture. That is what makes it so fascinating.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tại sao chúng ta nhìn màu sắc khác nhau",
                    "description": "Hà and Minh explore how culture shapes color perception and how artists use color to create emotion.",
                    "data": {
                        "text": "The next day, Hà and Minh are walking through the Vietnam Fine Arts Museum in Hanoi. They stop in front of a large painting with vibrant reds and deep blues.\n\n'This painting makes me feel something strong,' Minh says. 'But I cannot explain why. Is it the subject, or is it the colors?'\n\n'It is mostly the colors,' Hà says. 'Artists have understood for centuries that color affects emotion. Warm colors like red and orange create feelings of energy and passion. Cool colors like blue and green create feelings of calm and distance. This painting uses vibrant, highly saturated reds to create intensity. If the artist had used a soft tint of pink instead, the feeling would be completely different.'\n\n'What do you mean by saturated?' Minh asks.\n\n'Saturation is how pure and intense a color is,' Hà explains. 'A fully saturated red is bold and powerful. When you add white to it, you get a tint — a softer, lighter version. When you add black, you get a shade — a darker, heavier version. When you add gray, you desaturate it — making it duller and more muted. Artists control emotion by controlling saturation.'\n\n'And contrast?' Minh asks, pointing to a section where bright yellow sits next to deep purple.\n\n'Contrast is the difference between elements,' Hà says. 'When you place a vibrant color next to a dark shade, the vibrant color appears even brighter. Your eye is drawn to the area of highest contrast. That is why this painting works — the artist placed the brightest red right next to the darkest blue, creating a focal point that your eye cannot ignore.'\n\nMinh thinks for a moment. 'You know, I listened to a Radiolab episode about color perception. They talked about how different cultures actually see colors differently.'\n\n'That is one of the most fascinating topics in color science,' Hà says. 'Tell me more.'\n\n'The episode explained that perception of color is not purely physical,' Minh says. 'Yes, wavelength determines what color light is — red has a longer wavelength around seven hundred nanometers, while violet has a shorter wavelength around four hundred nanometers. But how your brain categorizes those wavelengths depends on your language and culture.'\n\n'Can you give me an example?' Hà asks.\n\n'Russian speakers have two separate words for light blue and dark blue,' Minh says. 'They are not shades of the same color — they are completely different colors in Russian. And research shows that Russian speakers can actually distinguish between those two blues faster than English speakers, who use one word for both. Their language literally changes their perception.'\n\n'That is incredible,' Hà says. 'So the words we have for colors shape what we see?'\n\n'To some extent, yes,' Minh says. 'The Himba people in Namibia have many words for different hues of green but no separate word for blue. When researchers showed them a circle of green squares with one blue square, they had difficulty finding the blue one. But when shown a circle of green squares with one slightly different green, they found it instantly — something most English speakers cannot do.'\n\n'So our perception is filtered through language,' Hà says quietly. 'We think we see the world as it is, but we actually see it through the lens of the words we have.'\n\n'Exactly,' Minh says. 'Color is not just wavelength. It is wavelength plus brain plus language plus culture. That is what makes it so fascinating.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tại sao chúng ta nhìn màu sắc khác nhau",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "The next day, Hà and Minh are walking through the Vietnam Fine Arts Museum in Hanoi. They stop in front of a large painting with vibrant reds and deep blues.\n\n'This painting makes me feel something strong,' Minh says. 'But I cannot explain why. Is it the subject, or is it the colors?'\n\n'It is mostly the colors,' Hà says. 'Artists have understood for centuries that color affects emotion. Warm colors like red and orange create feelings of energy and passion. Cool colors like blue and green create feelings of calm and distance. This painting uses vibrant, highly saturated reds to create intensity. If the artist had used a soft tint of pink instead, the feeling would be completely different.'\n\n'What do you mean by saturated?' Minh asks.\n\n'Saturation is how pure and intense a color is,' Hà explains. 'A fully saturated red is bold and powerful. When you add white to it, you get a tint — a softer, lighter version. When you add black, you get a shade — a darker, heavier version. When you add gray, you desaturate it — making it duller and more muted. Artists control emotion by controlling saturation.'\n\n'And contrast?' Minh asks, pointing to a section where bright yellow sits next to deep purple.\n\n'Contrast is the difference between elements,' Hà says. 'When you place a vibrant color next to a dark shade, the vibrant color appears even brighter. Your eye is drawn to the area of highest contrast. That is why this painting works — the artist placed the brightest red right next to the darkest blue, creating a focal point that your eye cannot ignore.'\n\nMinh thinks for a moment. 'You know, I listened to a Radiolab episode about color perception. They talked about how different cultures actually see colors differently.'\n\n'That is one of the most fascinating topics in color science,' Hà says. 'Tell me more.'\n\n'The episode explained that perception of color is not purely physical,' Minh says. 'Yes, wavelength determines what color light is — red has a longer wavelength around seven hundred nanometers, while violet has a shorter wavelength around four hundred nanometers. But how your brain categorizes those wavelengths depends on your language and culture.'\n\n'Can you give me an example?' Hà asks.\n\n'Russian speakers have two separate words for light blue and dark blue,' Minh says. 'They are not shades of the same color — they are completely different colors in Russian. And research shows that Russian speakers can actually distinguish between those two blues faster than English speakers, who use one word for both. Their language literally changes their perception.'\n\n'That is incredible,' Hà says. 'So the words we have for colors shape what we see?'\n\n'To some extent, yes,' Minh says. 'The Himba people in Namibia have many words for different hues of green but no separate word for blue. When researchers showed them a circle of green squares with one blue square, they had difficulty finding the blue one. But when shown a circle of green squares with one slightly different green, they found it instantly — something most English speakers cannot do.'\n\n'So our perception is filtered through language,' Hà says quietly. 'We think we see the world as it is, but we actually see it through the lens of the words we have.'\n\n'Exactly,' Minh says. 'Color is not just wavelength. It is wavelength plus brain plus language plus culture. That is what makes it so fascinating.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cảm nhận và sức mạnh của màu sắc",
                    "description": "Viết câu sử dụng từ vựng về cảm nhận, bước sóng, và tương phản.",
                    "data": {
                        "vocabList": ["perception", "wavelength", "vibrant", "contrast", "saturate", "tint"],
                        "items": [
                            {
                                "targetVocab": "perception",
                                "prompt": "Hãy dùng từ 'perception' để viết một câu về cách con người cảm nhận màu sắc. Ví dụ: Our perception of color is shaped not only by physics but also by the language we speak and the culture we grow up in."
                            },
                            {
                                "targetVocab": "wavelength",
                                "prompt": "Hãy dùng từ 'wavelength' để viết một câu về ánh sáng và màu sắc. Ví dụ: Each color in the rainbow corresponds to a specific wavelength of light, from long red waves to short violet ones."
                            },
                            {
                                "targetVocab": "vibrant",
                                "prompt": "Hãy dùng từ 'vibrant' để viết một câu về màu sắc rực rỡ. Ví dụ: The vibrant colors of Vietnamese silk lanterns in Hoi An attract thousands of photographers every year."
                            },
                            {
                                "targetVocab": "contrast",
                                "prompt": "Hãy dùng từ 'contrast' để viết một câu về sự tương phản. Ví dụ: The contrast between the dark storm clouds and the golden sunset created one of the most beautiful skies I have ever seen."
                            },
                            {
                                "targetVocab": "saturate",
                                "prompt": "Hãy dùng từ 'saturate' để viết một câu về độ bão hòa màu sắc. Ví dụ: The photographer chose to saturate the colors in the image to make the autumn leaves look even more dramatic."
                            },
                            {
                                "targetVocab": "tint",
                                "prompt": "Hãy dùng từ 'tint' để viết một câu về sắc nhạt. Ví dụ: Adding a slight tint of blue to white paint can make a room feel cooler and more spacious."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng phần 3 — Ánh sáng, vật liệu, và vẻ đẹp",
                    "description": "Ôn lại phần 1-2 và giới thiệu chủ đề ánh sáng đi qua vật liệu và thẩm mỹ.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần 3 — phần cuối cùng trước khi ôn tập! Bạn đã đi được hai phần ba chặng đường rồi. Hãy cùng nhìn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ về nền tảng của màu sắc: spectrum là quang phổ, pigment là sắc tố, hue là sắc, shade là sắc thái tối, palette là bảng màu, và canvas là toan vẽ. Trong phần 2, bạn học 6 từ về cảm nhận và sức mạnh của màu sắc: perception là sự cảm nhận, wavelength là bước sóng, vibrant là rực rỡ, contrast là sự tương phản, saturate là bão hòa, và tint là sắc nhạt.\n\nBây giờ, trong phần 3, chúng ta sẽ nói về cách ánh sáng tương tác với vật liệu — từ cách prism tách ánh sáng, đến cách gradient tạo chiều sâu, đến sự khác biệt giữa vật liệu opaque và translucent. Bạn sẽ học 6 từ cuối cùng: illuminate, prism, gradient, opaque, translucent, và aesthetic."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Dạy 6 từ vựng: illuminate, prism, gradient, opaque, translucent, aesthetic.",
                    "data": {
                        "text": "Hãy cùng học 6 từ cuối cùng nhé.\n\nTừ đầu tiên là illuminate — động từ — nghĩa là chiếu sáng, làm sáng tỏ. Illuminate vừa có nghĩa vật lý — chiếu ánh sáng lên một vật — vừa có nghĩa bóng — làm cho ai đó hiểu rõ hơn. Ví dụ: 'The setting sun illuminated the cathedral windows, filling the interior with golden light.' Trong bài đọc, Hà nói rằng cách ánh sáng illuminate một bức tranh có thể thay đổi hoàn toàn cách bạn cảm nhận nó.\n\nTừ thứ hai là prism — danh từ — nghĩa là lăng kính. Prism là một khối thủy tinh hình tam giác có khả năng tách ánh sáng trắng thành các màu cầu vồng — đây là cách Isaac Newton chứng minh rằng ánh sáng trắng chứa tất cả các màu. Ví dụ: 'Newton's famous experiment with a prism proved that white light is actually a mixture of all the colors of the spectrum.' Trong bài đọc, Minh giải thích rằng prism hoạt động bằng cách bẻ cong mỗi wavelength một góc khác nhau.\n\nTừ thứ ba là gradient — danh từ — nghĩa là sự chuyển màu, dải chuyển tiếp. Gradient là sự thay đổi dần dần từ một màu sang màu khác — không có ranh giới rõ ràng, chỉ có sự chuyển tiếp mượt mà. Ví dụ: 'The sky at sunset displays a natural gradient from deep orange near the horizon to dark blue overhead.' Trong bài đọc, Hà nói rằng gradient là một trong những kỹ thuật khó nhất trong hội họa vì nó đòi hỏi sự kiên nhẫn và kiểm soát.\n\nTừ thứ tư là opaque — tính từ — nghĩa là đục, không trong suốt. Opaque mô tả vật liệu không cho ánh sáng đi qua — bạn không thể nhìn xuyên qua nó. Ví dụ: 'Oil paint is naturally opaque, which allows artists to paint light colors over dark ones without the dark showing through.' Trong bài đọc, Hà so sánh sơn dầu opaque với màu nước translucent và giải thích cách mỗi loại tạo ra hiệu ứng khác nhau.\n\nTừ thứ năm là translucent — tính từ — nghĩa là mờ, bán trong suốt. Translucent mô tả vật liệu cho ánh sáng đi qua nhưng không rõ ràng — bạn thấy ánh sáng nhưng không thấy hình ảnh chi tiết phía sau. Ví dụ: 'The translucent paper lanterns glowed softly in the evening breeze, creating a magical atmosphere.' Trong bài đọc, Minh nói rằng sự khác biệt giữa opaque và translucent là chìa khóa để hiểu cách ánh sáng tương tác với vật liệu.\n\nTừ cuối cùng là aesthetic — tính từ và danh từ — nghĩa là thẩm mỹ, thuộc về cái đẹp. Aesthetic là về cảm nhận và đánh giá vẻ đẹp — trong nghệ thuật, đó là phong cách thị giác tổng thể của một tác phẩm. Ví dụ: 'The minimalist aesthetic of Japanese design uses empty space and simple colors to create a feeling of peace.' Trong bài đọc, Hà và Minh thảo luận rằng aesthetic không chỉ là về cái đẹp mà còn về cách chúng ta quyết định thứ gì là đẹp.\n\nBạn đã có đủ 18 từ vựng rồi! Hãy luyện flashcard rồi đọc phần cuối của cuộc trò chuyện nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ánh sáng, vật liệu, và vẻ đẹp",
                    "description": "Học 6 từ: illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ánh sáng, vật liệu, và vẻ đẹp",
                    "description": "Học 6 từ: illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ánh sáng, vật liệu, và vẻ đẹp",
                    "description": "Học 6 từ: illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ánh sáng, vật liệu, và vẻ đẹp",
                    "description": "Học 6 từ: illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 3",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về ánh sáng và vật liệu.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc phần cuối của cuộc trò chuyện giữa Hà và Minh. Lần này, họ nói về cách ánh sáng tương tác với vật liệu khác nhau — từ lăng kính đến giấy mờ — và cách những hiểu biết này ảnh hưởng đến thẩm mỹ trong nghệ thuật. Hãy chú ý cách các từ illuminate, prism, gradient, opaque, translucent, và aesthetic được dùng trong câu chuyện. Một điểm ngữ pháp: khi giải thích nguyên nhân và kết quả trong khoa học, chúng ta dùng 'because,' 'which causes,' và 'as a result' — ví dụ 'the prism bends light because each wavelength travels at a different speed through glass.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Khi ánh sáng gặp vật chất — Khoa học của vẻ đẹp",
                    "description": "Hà and Minh discuss how light interacts with materials and what makes something aesthetically beautiful.",
                    "data": {
                        "text": "On Saturday afternoon, Hà and Minh visit a glass art exhibition at a gallery in Hanoi's Old Quarter. The room is filled with sculptures that catch and bend light in extraordinary ways.\n\n'Look at this one,' Minh says, pointing to a triangular glass sculpture. 'It works exactly like a prism. The white light from the ceiling enters one side and exits the other as a rainbow.'\n\n'Newton would be proud,' Hà says. 'He was the first to use a prism to prove that white light contains the entire spectrum. Before his experiment, people believed that the prism added color to the light. Newton showed that the colors were already there — the prism just separated them because each wavelength bends at a slightly different angle.'\n\n'So a prism does not create color — it reveals color that was hidden,' Minh says.\n\n'Exactly. And that idea is beautiful in itself,' Hà says. 'Now look at this sculpture next to it. See how the color changes gradually from blue at the bottom to green at the top? That is a gradient — a smooth transition between colors with no sharp boundary.'\n\n'Gradients are everywhere in nature,' Minh says. 'The sky at sunset, the color of the ocean as it gets deeper, the way a leaf changes from green to yellow in autumn.'\n\n'And they are incredibly difficult to create in painting,' Hà says. 'A perfect gradient requires mixing colors so smoothly that you cannot see where one ends and the other begins. In digital art, a computer can calculate a gradient mathematically. But on a canvas, it takes hours of careful blending. That is why I respect traditional painters so much — they create with their hands what a computer does with algorithms.'\n\nThey move to another section of the gallery where light passes through different materials.\n\n'This is fascinating,' Minh says. 'Look at these three panels. The first one is completely opaque — no light passes through at all. The second is translucent — light passes through but you cannot see clear shapes on the other side. The third is transparent — you can see right through it.'\n\n'The difference between opaque and translucent materials is one of the most important concepts in painting,' Hà says. 'Oil paint is naturally opaque. When you apply it, it completely covers whatever is underneath. That gives you incredible control — you can paint light over dark, correct mistakes, build up layers. Watercolor, on the other hand, is translucent. The white paper shows through the paint, which is what gives watercolor its characteristic luminous quality.'\n\n'So the material itself shapes the aesthetic,' Minh says.\n\n'Absolutely,' Hà agrees. 'And that brings us to the big question — what makes something aesthetically beautiful? Is beauty objective or subjective?'\n\n'The physicist in me wants to say there are objective principles,' Minh says. 'Symmetry, proportion, the golden ratio. These mathematical relationships appear in nature and in art that humans find beautiful across cultures.'\n\n'The artist in me agrees — partially,' Hà says. 'There are principles that work. Contrast draws the eye. Gradients create depth. Vibrant, saturated colors create energy. Soft tints create calm. But the aesthetic of a culture changes over time. What the Renaissance considered beautiful is different from what modern art considers beautiful. The Japanese aesthetic of wabi-sabi finds beauty in imperfection — cracked pottery, faded colors, asymmetry.'\n\n'So beauty is both universal and cultural,' Minh says.\n\n'Just like color itself,' Hà says. 'The wavelengths are universal physics. But how we perceive them, name them, and find them beautiful — that is deeply human. And that is what I love about studying color. It sits right at the intersection of science and art, of physics and perception, of the universal and the personal.'\n\nMinh looks around the gallery, seeing the light and color with new eyes. 'I think I understand now why Radiolab dedicated an entire episode to colors. It is not just about what we see. It is about how we see — and why.'\n\n'And how we illuminate the world,' Hà adds, 'both with light and with understanding.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Khi ánh sáng gặp vật chất — Khoa học của vẻ đẹp",
                    "description": "Hà and Minh discuss how light interacts with materials and what makes something aesthetically beautiful.",
                    "data": {
                        "text": "On Saturday afternoon, Hà and Minh visit a glass art exhibition at a gallery in Hanoi's Old Quarter. The room is filled with sculptures that catch and bend light in extraordinary ways.\n\n'Look at this one,' Minh says, pointing to a triangular glass sculpture. 'It works exactly like a prism. The white light from the ceiling enters one side and exits the other as a rainbow.'\n\n'Newton would be proud,' Hà says. 'He was the first to use a prism to prove that white light contains the entire spectrum. Before his experiment, people believed that the prism added color to the light. Newton showed that the colors were already there — the prism just separated them because each wavelength bends at a slightly different angle.'\n\n'So a prism does not create color — it reveals color that was hidden,' Minh says.\n\n'Exactly. And that idea is beautiful in itself,' Hà says. 'Now look at this sculpture next to it. See how the color changes gradually from blue at the bottom to green at the top? That is a gradient — a smooth transition between colors with no sharp boundary.'\n\n'Gradients are everywhere in nature,' Minh says. 'The sky at sunset, the color of the ocean as it gets deeper, the way a leaf changes from green to yellow in autumn.'\n\n'And they are incredibly difficult to create in painting,' Hà says. 'A perfect gradient requires mixing colors so smoothly that you cannot see where one ends and the other begins. In digital art, a computer can calculate a gradient mathematically. But on a canvas, it takes hours of careful blending. That is why I respect traditional painters so much — they create with their hands what a computer does with algorithms.'\n\nThey move to another section of the gallery where light passes through different materials.\n\n'This is fascinating,' Minh says. 'Look at these three panels. The first one is completely opaque — no light passes through at all. The second is translucent — light passes through but you cannot see clear shapes on the other side. The third is transparent — you can see right through it.'\n\n'The difference between opaque and translucent materials is one of the most important concepts in painting,' Hà says. 'Oil paint is naturally opaque. When you apply it, it completely covers whatever is underneath. That gives you incredible control — you can paint light over dark, correct mistakes, build up layers. Watercolor, on the other hand, is translucent. The white paper shows through the paint, which is what gives watercolor its characteristic luminous quality.'\n\n'So the material itself shapes the aesthetic,' Minh says.\n\n'Absolutely,' Hà agrees. 'And that brings us to the big question — what makes something aesthetically beautiful? Is beauty objective or subjective?'\n\n'The physicist in me wants to say there are objective principles,' Minh says. 'Symmetry, proportion, the golden ratio. These mathematical relationships appear in nature and in art that humans find beautiful across cultures.'\n\n'The artist in me agrees — partially,' Hà says. 'There are principles that work. Contrast draws the eye. Gradients create depth. Vibrant, saturated colors create energy. Soft tints create calm. But the aesthetic of a culture changes over time. What the Renaissance considered beautiful is different from what modern art considers beautiful. The Japanese aesthetic of wabi-sabi finds beauty in imperfection — cracked pottery, faded colors, asymmetry.'\n\n'So beauty is both universal and cultural,' Minh says.\n\n'Just like color itself,' Hà says. 'The wavelengths are universal physics. But how we perceive them, name them, and find them beautiful — that is deeply human. And that is what I love about studying color. It sits right at the intersection of science and art, of physics and perception, of the universal and the personal.'\n\nMinh looks around the gallery, seeing the light and color with new eyes. 'I think I understand now why Radiolab dedicated an entire episode to colors. It is not just about what we see. It is about how we see — and why.'\n\n'And how we illuminate the world,' Hà adds, 'both with light and with understanding.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Khi ánh sáng gặp vật chất — Khoa học của vẻ đẹp",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "On Saturday afternoon, Hà and Minh visit a glass art exhibition at a gallery in Hanoi's Old Quarter. The room is filled with sculptures that catch and bend light in extraordinary ways.\n\n'Look at this one,' Minh says, pointing to a triangular glass sculpture. 'It works exactly like a prism. The white light from the ceiling enters one side and exits the other as a rainbow.'\n\n'Newton would be proud,' Hà says. 'He was the first to use a prism to prove that white light contains the entire spectrum. Before his experiment, people believed that the prism added color to the light. Newton showed that the colors were already there — the prism just separated them because each wavelength bends at a slightly different angle.'\n\n'So a prism does not create color — it reveals color that was hidden,' Minh says.\n\n'Exactly. And that idea is beautiful in itself,' Hà says. 'Now look at this sculpture next to it. See how the color changes gradually from blue at the bottom to green at the top? That is a gradient — a smooth transition between colors with no sharp boundary.'\n\n'Gradients are everywhere in nature,' Minh says. 'The sky at sunset, the color of the ocean as it gets deeper, the way a leaf changes from green to yellow in autumn.'\n\n'And they are incredibly difficult to create in painting,' Hà says. 'A perfect gradient requires mixing colors so smoothly that you cannot see where one ends and the other begins. In digital art, a computer can calculate a gradient mathematically. But on a canvas, it takes hours of careful blending. That is why I respect traditional painters so much — they create with their hands what a computer does with algorithms.'\n\nThey move to another section of the gallery where light passes through different materials.\n\n'This is fascinating,' Minh says. 'Look at these three panels. The first one is completely opaque — no light passes through at all. The second is translucent — light passes through but you cannot see clear shapes on the other side. The third is transparent — you can see right through it.'\n\n'The difference between opaque and translucent materials is one of the most important concepts in painting,' Hà says. 'Oil paint is naturally opaque. When you apply it, it completely covers whatever is underneath. That gives you incredible control — you can paint light over dark, correct mistakes, build up layers. Watercolor, on the other hand, is translucent. The white paper shows through the paint, which is what gives watercolor its characteristic luminous quality.'\n\n'So the material itself shapes the aesthetic,' Minh says.\n\n'Absolutely,' Hà agrees. 'And that brings us to the big question — what makes something aesthetically beautiful? Is beauty objective or subjective?'\n\n'The physicist in me wants to say there are objective principles,' Minh says. 'Symmetry, proportion, the golden ratio. These mathematical relationships appear in nature and in art that humans find beautiful across cultures.'\n\n'The artist in me agrees — partially,' Hà says. 'There are principles that work. Contrast draws the eye. Gradients create depth. Vibrant, saturated colors create energy. Soft tints create calm. But the aesthetic of a culture changes over time. What the Renaissance considered beautiful is different from what modern art considers beautiful. The Japanese aesthetic of wabi-sabi finds beauty in imperfection — cracked pottery, faded colors, asymmetry.'\n\n'So beauty is both universal and cultural,' Minh says.\n\n'Just like color itself,' Hà says. 'The wavelengths are universal physics. But how we perceive them, name them, and find them beautiful — that is deeply human. And that is what I love about studying color. It sits right at the intersection of science and art, of physics and perception, of the universal and the personal.'\n\nMinh looks around the gallery, seeing the light and color with new eyes. 'I think I understand now why Radiolab dedicated an entire episode to colors. It is not just about what we see. It is about how we see — and why.'\n\n'And how we illuminate the world,' Hà adds, 'both with light and with understanding.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ánh sáng, vật liệu, và vẻ đẹp",
                    "description": "Viết câu sử dụng từ vựng về lăng kính, chuyển màu, và thẩm mỹ.",
                    "data": {
                        "vocabList": ["illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"],
                        "items": [
                            {
                                "targetVocab": "illuminate",
                                "prompt": "Hãy dùng từ 'illuminate' để viết một câu về ánh sáng hoặc sự hiểu biết. Ví dụ: The morning sun illuminated the stained glass windows, casting colorful patterns across the stone floor."
                            },
                            {
                                "targetVocab": "prism",
                                "prompt": "Hãy dùng từ 'prism' để viết một câu về lăng kính và ánh sáng. Ví dụ: A crystal chandelier acts like hundreds of tiny prisms, splitting light into rainbows that dance across the walls."
                            },
                            {
                                "targetVocab": "gradient",
                                "prompt": "Hãy dùng từ 'gradient' để viết một câu về sự chuyển màu. Ví dụ: The artist spent three hours creating a perfect gradient from midnight blue to pale lavender across the canvas."
                            },
                            {
                                "targetVocab": "opaque",
                                "prompt": "Hãy dùng từ 'opaque' để viết một câu về vật liệu không trong suốt. Ví dụ: The opaque curtains blocked all sunlight from entering the room, creating complete darkness."
                            },
                            {
                                "targetVocab": "translucent",
                                "prompt": "Hãy dùng từ 'translucent' để viết một câu về vật liệu bán trong suốt. Ví dụ: The translucent jellyfish glowed softly as light passed through its delicate body."
                            },
                            {
                                "targetVocab": "aesthetic",
                                "prompt": "Hãy dùng từ 'aesthetic' để viết một câu về thẩm mỹ. Ví dụ: The minimalist aesthetic of the gallery allowed visitors to focus entirely on the artwork without distraction."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng — ôn lại tất cả trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã học xong tất cả 18 từ vựng về màu sắc, nghệ thuật, và cảm nhận thị giác. Hãy cùng ôn lại nhanh trước khi bước vào phần ôn tập.\n\nTrong phần 1, bạn học 6 từ về nền tảng: spectrum là quang phổ — dải đầy đủ các màu trong ánh sáng. Pigment là sắc tố — chất tạo ra màu sắc. Hue là sắc — tên gọi thuần túy của một màu. Shade là sắc thái tối — khi thêm đen vào màu. Palette là bảng màu — tập hợp các màu cho một tác phẩm. Canvas là toan vẽ — bề mặt sáng tạo.\n\nTrong phần 2, bạn học 6 từ về cảm nhận: perception là sự cảm nhận — cách não giải thích màu sắc. Wavelength là bước sóng — quyết định màu của ánh sáng. Vibrant là rực rỡ — màu mạnh mẽ, tươi sáng. Contrast là sự tương phản — sự khác biệt giữa sáng và tối. Saturate là bão hòa — mức độ đậm nhất của màu. Tint là sắc nhạt — khi thêm trắng vào màu.\n\nTrong phần 3, bạn học 6 từ về ánh sáng và vẻ đẹp: illuminate là chiếu sáng. Prism là lăng kính — tách ánh sáng thành cầu vồng. Gradient là sự chuyển màu — thay đổi dần dần giữa các màu. Opaque là đục — không cho ánh sáng đi qua. Translucent là mờ — cho ánh sáng đi qua nhưng không rõ. Aesthetic là thẩm mỹ — về cảm nhận vẻ đẹp.\n\nBây giờ hãy ôn tập tất cả 18 từ với flashcard và bài viết nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: spectrum, pigment, hue, shade, palette, canvas, perception, wavelength, vibrant, contrast, saturate, tint, illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas", "perception", "wavelength", "vibrant", "contrast", "saturate", "tint", "illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: spectrum, pigment, hue, shade, palette, canvas, perception, wavelength, vibrant, contrast, saturate, tint, illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas", "perception", "wavelength", "vibrant", "contrast", "saturate", "tint", "illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: spectrum, pigment, hue, shade, palette, canvas, perception, wavelength, vibrant, contrast, saturate, tint, illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas", "perception", "wavelength", "vibrant", "contrast", "saturate", "tint", "illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: spectrum, pigment, hue, shade, palette, canvas, perception, wavelength, vibrant, contrast, saturate, tint, illuminate, prism, gradient, opaque, translucent, aesthetic",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas", "perception", "wavelength", "vibrant", "contrast", "saturate", "tint", "illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập màu sắc và nghệ thuật",
                    "description": "Viết câu ôn tập sử dụng tất cả 18 từ vựng về màu sắc và nghệ thuật.",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas", "perception", "wavelength", "vibrant", "contrast", "saturate", "tint", "illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"],
                        "items": [
                            {
                                "targetVocab": "spectrum",
                                "prompt": "Hãy dùng từ 'spectrum' để viết một câu về sự đa dạng. Ví dụ: Human emotions exist on a wide spectrum, from the deepest sadness to the most intense joy."
                            },
                            {
                                "targetVocab": "pigment",
                                "prompt": "Hãy dùng từ 'pigment' để viết một câu về màu sắc trong tự nhiên hoặc nghệ thuật. Ví dụ: The brilliant pigment in a peacock's feathers does not come from chemicals but from the microscopic structure of the feathers themselves."
                            },
                            {
                                "targetVocab": "hue",
                                "prompt": "Hãy dùng từ 'hue' để viết một câu về sắc màu. Ví dụ: The same hue of green can feel completely different depending on whether it is placed next to yellow or next to purple."
                            },
                            {
                                "targetVocab": "shade",
                                "prompt": "Hãy dùng từ 'shade' để viết một câu về tông màu. Ví dụ: Every culture has its own preferred shade of white for wedding dresses, from pure snow white to warm ivory."
                            },
                            {
                                "targetVocab": "palette",
                                "prompt": "Hãy dùng từ 'palette' để viết một câu về bảng màu. Ví dụ: A chef's palette of ingredients is just as important as a painter's palette of colors — both create experiences through careful combination."
                            },
                            {
                                "targetVocab": "canvas",
                                "prompt": "Hãy dùng từ 'canvas' để viết một câu về không gian sáng tạo. Ví dụ: Social media has become a digital canvas where millions of people express their creativity through photos, videos, and design."
                            },
                            {
                                "targetVocab": "perception",
                                "prompt": "Hãy dùng từ 'perception' để viết một câu về cách nhìn nhận. Ví dụ: Travel changes your perception of the world by showing you that the way you see things is just one of many possible perspectives."
                            },
                            {
                                "targetVocab": "wavelength",
                                "prompt": "Hãy dùng từ 'wavelength' để viết một câu về bước sóng hoặc sự đồng điệu. Ví dụ: When two people are on the same wavelength, they understand each other without needing to explain every detail."
                            },
                            {
                                "targetVocab": "vibrant",
                                "prompt": "Hãy dùng từ 'vibrant' để viết một câu về sự sống động. Ví dụ: Hanoi's Old Quarter is one of the most vibrant neighborhoods in Southeast Asia, full of color, sound, and energy at every hour."
                            },
                            {
                                "targetVocab": "contrast",
                                "prompt": "Hãy dùng từ 'contrast' để viết một câu về sự tương phản. Ví dụ: The contrast between the ancient temples and modern skyscrapers in Tokyo creates a unique visual experience."
                            },
                            {
                                "targetVocab": "saturate",
                                "prompt": "Hãy dùng từ 'saturate' để viết một câu về sự bão hòa. Ví dụ: After three hours of studying, my brain felt completely saturated and I could not absorb any more information."
                            },
                            {
                                "targetVocab": "tint",
                                "prompt": "Hãy dùng từ 'tint' để viết một câu về sắc nhạt. Ví dụ: The early morning sky had a delicate tint of rose that lasted only a few minutes before the sun fully rose."
                            },
                            {
                                "targetVocab": "illuminate",
                                "prompt": "Hãy dùng từ 'illuminate' để viết một câu về ánh sáng hoặc sự hiểu biết. Ví dụ: A single conversation with a wise teacher can illuminate ideas that years of reading alone could not."
                            },
                            {
                                "targetVocab": "prism",
                                "prompt": "Hãy dùng từ 'prism' để viết một câu về lăng kính hoặc góc nhìn. Ví dụ: Literature allows us to see the world through the prism of another person's experience and emotions."
                            },
                            {
                                "targetVocab": "gradient",
                                "prompt": "Hãy dùng từ 'gradient' để viết một câu về sự chuyển đổi dần dần. Ví dụ: Learning a language is not a sudden leap but a gentle gradient from confusion to understanding."
                            },
                            {
                                "targetVocab": "opaque",
                                "prompt": "Hãy dùng từ 'opaque' để viết một câu về sự không trong suốt. Ví dụ: The company's financial reports were so opaque that even experienced analysts struggled to understand them."
                            },
                            {
                                "targetVocab": "translucent",
                                "prompt": "Hãy dùng từ 'translucent' để viết một câu về sự bán trong suốt. Ví dụ: The thin translucent curtains softened the harsh afternoon sunlight into a warm, gentle glow."
                            },
                            {
                                "targetVocab": "aesthetic",
                                "prompt": "Hãy dùng từ 'aesthetic' để viết một câu về thẩm mỹ. Ví dụ: Every generation develops its own aesthetic — what looks beautiful to teenagers today would have seemed strange to their grandparents."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc tổng hợp",
                    "description": "Giới thiệu bài đọc cuối cùng kết hợp tất cả 18 từ vựng về màu sắc và nghệ thuật.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của Radiolab: Colors! Bạn đã đi một chặng đường ấn tượng. Trong phần 1, bạn học về nền tảng của màu sắc với 6 từ: spectrum, pigment, hue, shade, palette, canvas. Trong phần 2, bạn khám phá cảm nhận và sức mạnh của màu sắc với 6 từ: perception, wavelength, vibrant, contrast, saturate, tint. Trong phần 3, bạn tìm hiểu ánh sáng, vật liệu, và vẻ đẹp với 6 từ: illuminate, prism, gradient, opaque, translucent, aesthetic. Trong phần ôn tập, bạn đã luyện lại tất cả 18 từ.\n\nBây giờ, bạn sẽ đọc một bài tổng hợp — Hà và Minh gặp lại nhau và chia sẻ những gì họ đã học được về thế giới ẩn giấu của màu sắc. Bài đọc này dùng tất cả 18 từ vựng bạn đã học. Hãy đọc chậm, thưởng thức câu chuyện, và chú ý cách mỗi từ được dùng trong ngữ cảnh thực tế nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Thế giới ẩn giấu của màu sắc — Khi khoa học gặp nghệ thuật",
                    "description": "Hà and Minh reflect on the complete picture of color — from physics to perception to beauty.",
                    "data": {
                        "text": "Two weeks have passed since Hà and Minh began their exploration of color. They are sitting on the rooftop of their university building at sunset, watching the sky transform through a natural gradient of colors — from deep orange near the horizon to violet overhead.\n\n'This is the most beautiful canvas in the world,' Hà says, looking at the sky. 'And no artist could ever reproduce it perfectly.'\n\n'Do you know why sunsets have so many colors?' Minh asks. 'When the sun is low on the horizon, its light has to travel through more of the atmosphere. The shorter wavelengths — blue and violet — get scattered away, leaving the longer wavelengths — red, orange, and yellow — to illuminate the sky. That is why sunsets are warm-colored while the midday sky is blue.'\n\n'Science explains the mechanism,' Hà says. 'But it does not explain why it is beautiful. That is where art and perception come in.'\n\nMinh nods. 'You know, these past two weeks have completely changed how I see the world. Before, I thought color was simple — just wavelengths of light hitting your eyes. Now I understand that color is one of the most complex phenomena in human experience.'\n\n'Tell me what you have learned,' Hà says.\n\n'Let me start with the physics,' Minh says. 'White light contains the entire spectrum of visible colors — every hue from red to violet. When that light passes through a prism, each wavelength bends at a different angle, separating the colors. Newton proved this over three hundred years ago, and it remains one of the most elegant experiments in science.'\n\n'And when light hits an object?' Hà asks.\n\n'That is where it gets interesting,' Minh continues. 'Every object absorbs some wavelengths and reflects others. The reflected wavelengths are what we perceive as color. A red rose absorbs every color in the spectrum except red. A blue ocean reflects the shorter wavelengths. And the pigments that artists use work on the same principle — each pigment absorbs certain wavelengths and reflects others, which is what gives it its specific hue.'\n\n'Now let me add the art perspective,' Hà says. 'Understanding the physics is important, but creating with color requires something more. When I stand before a blank canvas, I have to make hundreds of decisions. Which palette will I use? Should the colors be vibrant and saturated, or soft and muted? Where will I place the strongest contrast to draw the viewer's eye? Should I use opaque paint that covers everything underneath, or translucent layers that let the light shine through?'\n\n'Each of those decisions changes the emotional impact,' Minh says.\n\n'Exactly,' Hà says. 'A painting with vibrant, highly saturated colors feels energetic and alive. The same composition with soft tints feels gentle and dreamlike. A strong contrast between light and dark creates drama. A smooth gradient creates peace. The artist is not just putting color on canvas — they are engineering an emotional experience.'\n\n'And then there is the perception side,' Minh adds. 'What fascinated me most was learning that color perception is not universal. Different cultures literally see colors differently because their languages categorize the spectrum in different ways. Russian speakers distinguish between light blue and dark blue as separate colors. The Himba people see shades of green that English speakers cannot differentiate. Our perception is filtered through the lens of our language and culture.'\n\n'That is what makes color so philosophical,' Hà says. 'Is the sunset objectively beautiful, or do we find it beautiful because our culture taught us to? Is the hue of this sky the same for everyone, or does each person's brain create a slightly different version?'\n\n'I think the answer is both,' Minh says. 'The wavelengths are objective physics. But the experience of color — the perception, the emotion, the aesthetic judgment — that is deeply personal and cultural.'\n\nHà picks up a small glass prism from her bag and holds it up to the fading sunlight. A tiny rainbow appears on her palm.\n\n'Look at that,' she says. 'All the colors were hidden inside that white light. The prism just revealed them. I think that is what learning does too — it illuminates things that were always there but that we could not see before.'\n\n'Before these conversations, I walked past paintings without stopping,' Minh says. 'I saw sunsets without wondering why they were orange. I wore clothes without thinking about why certain colors made me feel certain ways. Now I cannot unsee it. Color is everywhere, and it is telling a story that I am finally learning to read.'\n\n'And I used to think physics was cold and mathematical,' Hà says. 'Now I see that the science of light is one of the most beautiful stories ever told. Every gradient in the sky, every translucent petal, every opaque stone — they are all following the same laws of physics. The universe has an aesthetic, and it is written in wavelengths.'\n\nThe sky has shifted to a deep shade of purple. The first stars are appearing.\n\n'You know what Radiolab does best?' Minh says. 'It shows you that the ordinary things you take for granted — like color — are actually extraordinary when you look closely enough.'\n\n'And that the boundary between science and art is not a wall,' Hà adds. 'It is a gradient.'\n\nThey sit in comfortable silence, watching the last tint of orange fade from the horizon, as the night sky illuminates itself with stars — each one a different wavelength, a different hue, a different story waiting to be perceived."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Thế giới ẩn giấu của màu sắc — Khi khoa học gặp nghệ thuật",
                    "description": "Hà and Minh reflect on the complete picture of color — from physics to perception to beauty.",
                    "data": {
                        "text": "Two weeks have passed since Hà and Minh began their exploration of color. They are sitting on the rooftop of their university building at sunset, watching the sky transform through a natural gradient of colors — from deep orange near the horizon to violet overhead.\n\n'This is the most beautiful canvas in the world,' Hà says, looking at the sky. 'And no artist could ever reproduce it perfectly.'\n\n'Do you know why sunsets have so many colors?' Minh asks. 'When the sun is low on the horizon, its light has to travel through more of the atmosphere. The shorter wavelengths — blue and violet — get scattered away, leaving the longer wavelengths — red, orange, and yellow — to illuminate the sky. That is why sunsets are warm-colored while the midday sky is blue.'\n\n'Science explains the mechanism,' Hà says. 'But it does not explain why it is beautiful. That is where art and perception come in.'\n\nMinh nods. 'You know, these past two weeks have completely changed how I see the world. Before, I thought color was simple — just wavelengths of light hitting your eyes. Now I understand that color is one of the most complex phenomena in human experience.'\n\n'Tell me what you have learned,' Hà says.\n\n'Let me start with the physics,' Minh says. 'White light contains the entire spectrum of visible colors — every hue from red to violet. When that light passes through a prism, each wavelength bends at a different angle, separating the colors. Newton proved this over three hundred years ago, and it remains one of the most elegant experiments in science.'\n\n'And when light hits an object?' Hà asks.\n\n'That is where it gets interesting,' Minh continues. 'Every object absorbs some wavelengths and reflects others. The reflected wavelengths are what we perceive as color. A red rose absorbs every color in the spectrum except red. A blue ocean reflects the shorter wavelengths. And the pigments that artists use work on the same principle — each pigment absorbs certain wavelengths and reflects others, which is what gives it its specific hue.'\n\n'Now let me add the art perspective,' Hà says. 'Understanding the physics is important, but creating with color requires something more. When I stand before a blank canvas, I have to make hundreds of decisions. Which palette will I use? Should the colors be vibrant and saturated, or soft and muted? Where will I place the strongest contrast to draw the viewer's eye? Should I use opaque paint that covers everything underneath, or translucent layers that let the light shine through?'\n\n'Each of those decisions changes the emotional impact,' Minh says.\n\n'Exactly,' Hà says. 'A painting with vibrant, highly saturated colors feels energetic and alive. The same composition with soft tints feels gentle and dreamlike. A strong contrast between light and dark creates drama. A smooth gradient creates peace. The artist is not just putting color on canvas — they are engineering an emotional experience.'\n\n'And then there is the perception side,' Minh adds. 'What fascinated me most was learning that color perception is not universal. Different cultures literally see colors differently because their languages categorize the spectrum in different ways. Russian speakers distinguish between light blue and dark blue as separate colors. The Himba people see shades of green that English speakers cannot differentiate. Our perception is filtered through the lens of our language and culture.'\n\n'That is what makes color so philosophical,' Hà says. 'Is the sunset objectively beautiful, or do we find it beautiful because our culture taught us to? Is the hue of this sky the same for everyone, or does each person's brain create a slightly different version?'\n\n'I think the answer is both,' Minh says. 'The wavelengths are objective physics. But the experience of color — the perception, the emotion, the aesthetic judgment — that is deeply personal and cultural.'\n\nHà picks up a small glass prism from her bag and holds it up to the fading sunlight. A tiny rainbow appears on her palm.\n\n'Look at that,' she says. 'All the colors were hidden inside that white light. The prism just revealed them. I think that is what learning does too — it illuminates things that were always there but that we could not see before.'\n\n'Before these conversations, I walked past paintings without stopping,' Minh says. 'I saw sunsets without wondering why they were orange. I wore clothes without thinking about why certain colors made me feel certain ways. Now I cannot unsee it. Color is everywhere, and it is telling a story that I am finally learning to read.'\n\n'And I used to think physics was cold and mathematical,' Hà says. 'Now I see that the science of light is one of the most beautiful stories ever told. Every gradient in the sky, every translucent petal, every opaque stone — they are all following the same laws of physics. The universe has an aesthetic, and it is written in wavelengths.'\n\nThe sky has shifted to a deep shade of purple. The first stars are appearing.\n\n'You know what Radiolab does best?' Minh says. 'It shows you that the ordinary things you take for granted — like color — are actually extraordinary when you look closely enough.'\n\n'And that the boundary between science and art is not a wall,' Hà adds. 'It is a gradient.'\n\nThey sit in comfortable silence, watching the last tint of orange fade from the horizon, as the night sky illuminates itself with stars — each one a different wavelength, a different hue, a different story waiting to be perceived."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Thế giới ẩn giấu của màu sắc — Khi khoa học gặp nghệ thuật",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Two weeks have passed since Hà and Minh began their exploration of color. They are sitting on the rooftop of their university building at sunset, watching the sky transform through a natural gradient of colors — from deep orange near the horizon to violet overhead.\n\n'This is the most beautiful canvas in the world,' Hà says, looking at the sky. 'And no artist could ever reproduce it perfectly.'\n\n'Do you know why sunsets have so many colors?' Minh asks. 'When the sun is low on the horizon, its light has to travel through more of the atmosphere. The shorter wavelengths — blue and violet — get scattered away, leaving the longer wavelengths — red, orange, and yellow — to illuminate the sky. That is why sunsets are warm-colored while the midday sky is blue.'\n\n'Science explains the mechanism,' Hà says. 'But it does not explain why it is beautiful. That is where art and perception come in.'\n\nMinh nods. 'You know, these past two weeks have completely changed how I see the world. Before, I thought color was simple — just wavelengths of light hitting your eyes. Now I understand that color is one of the most complex phenomena in human experience.'\n\n'Tell me what you have learned,' Hà says.\n\n'Let me start with the physics,' Minh says. 'White light contains the entire spectrum of visible colors — every hue from red to violet. When that light passes through a prism, each wavelength bends at a different angle, separating the colors. Newton proved this over three hundred years ago, and it remains one of the most elegant experiments in science.'\n\n'And when light hits an object?' Hà asks.\n\n'That is where it gets interesting,' Minh continues. 'Every object absorbs some wavelengths and reflects others. The reflected wavelengths are what we perceive as color. A red rose absorbs every color in the spectrum except red. A blue ocean reflects the shorter wavelengths. And the pigments that artists use work on the same principle — each pigment absorbs certain wavelengths and reflects others, which is what gives it its specific hue.'\n\n'Now let me add the art perspective,' Hà says. 'Understanding the physics is important, but creating with color requires something more. When I stand before a blank canvas, I have to make hundreds of decisions. Which palette will I use? Should the colors be vibrant and saturated, or soft and muted? Where will I place the strongest contrast to draw the viewer's eye? Should I use opaque paint that covers everything underneath, or translucent layers that let the light shine through?'\n\n'Each of those decisions changes the emotional impact,' Minh says.\n\n'Exactly,' Hà says. 'A painting with vibrant, highly saturated colors feels energetic and alive. The same composition with soft tints feels gentle and dreamlike. A strong contrast between light and dark creates drama. A smooth gradient creates peace. The artist is not just putting color on canvas — they are engineering an emotional experience.'\n\n'And then there is the perception side,' Minh adds. 'What fascinated me most was learning that color perception is not universal. Different cultures literally see colors differently because their languages categorize the spectrum in different ways. Russian speakers distinguish between light blue and dark blue as separate colors. The Himba people see shades of green that English speakers cannot differentiate. Our perception is filtered through the lens of our language and culture.'\n\n'That is what makes color so philosophical,' Hà says. 'Is the sunset objectively beautiful, or do we find it beautiful because our culture taught us to? Is the hue of this sky the same for everyone, or does each person's brain create a slightly different version?'\n\n'I think the answer is both,' Minh says. 'The wavelengths are objective physics. But the experience of color — the perception, the emotion, the aesthetic judgment — that is deeply personal and cultural.'\n\nHà picks up a small glass prism from her bag and holds it up to the fading sunlight. A tiny rainbow appears on her palm.\n\n'Look at that,' she says. 'All the colors were hidden inside that white light. The prism just revealed them. I think that is what learning does too — it illuminates things that were always there but that we could not see before.'\n\n'Before these conversations, I walked past paintings without stopping,' Minh says. 'I saw sunsets without wondering why they were orange. I wore clothes without thinking about why certain colors made me feel certain ways. Now I cannot unsee it. Color is everywhere, and it is telling a story that I am finally learning to read.'\n\n'And I used to think physics was cold and mathematical,' Hà says. 'Now I see that the science of light is one of the most beautiful stories ever told. Every gradient in the sky, every translucent petal, every opaque stone — they are all following the same laws of physics. The universe has an aesthetic, and it is written in wavelengths.'\n\nThe sky has shifted to a deep shade of purple. The first stars are appearing.\n\n'You know what Radiolab does best?' Minh says. 'It shows you that the ordinary things you take for granted — like color — are actually extraordinary when you look closely enough.'\n\n'And that the boundary between science and art is not a wall,' Hà adds. 'It is a gradient.'\n\nThey sit in comfortable silence, watching the last tint of orange fade from the horizon, as the night sky illuminates itself with stars — each one a different wavelength, a different hue, a different story waiting to be perceived."
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích khoa học và nghệ thuật của màu sắc",
                    "description": "Viết đoạn văn phân tích về màu sắc sử dụng từ vựng đã học.",
                    "data": {
                        "vocabList": ["spectrum", "pigment", "hue", "shade", "palette", "canvas", "perception", "wavelength", "vibrant", "contrast", "saturate", "tint", "illuminate", "prism", "gradient", "opaque", "translucent", "aesthetic"],
                        "instructions": "Viết một đoạn văn tiếng Anh (80-120 từ) phân tích cách khoa học và nghệ thuật giao nhau trong thế giới màu sắc. Sử dụng ít nhất 6 từ vựng đã học trong bài.",
                        "prompts": [
                            "Explain how the science of light and color connects to the art of painting. Use words like spectrum, wavelength, pigment, hue, palette, and canvas to describe how artists use scientific principles — whether they know it or not — to create emotional experiences through color.",
                            "Analyze how culture and language shape our perception of color. Use words like perception, contrast, vibrant, shade, tint, and aesthetic to explain why different people can look at the same sunset and have completely different experiences of its beauty."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay — farewell tone: introspective_guide.",
                    "data": {
                        "text": "Bạn đã hoàn thành Radiolab: Colors. Trước khi kết thúc, tôi muốn mời bạn làm một điều — hãy nhắm mắt lại một giây. Bây giờ mở mắt ra. Mọi thứ bạn nhìn thấy — màn hình, bức tường, bầu trời ngoài cửa sổ — tất cả đều là màu sắc. Nhưng sau bài học này, bạn nhìn thấy nhiều hơn trước. Bạn không chỉ nhìn thấy 'xanh' hay 'đỏ' nữa — bạn nhìn thấy câu chuyện đằng sau mỗi màu.\n\nHãy cùng nhìn lại 18 từ vựng — nhưng lần này, tôi muốn bạn tự hỏi: từ nào đã thay đổi cách bạn nhìn thế giới?\n\nSpectrum — quang phổ. Mỗi tia sáng trắng chứa cả một vũ trụ màu sắc ẩn giấu. Câu mới: The spectrum of human experience is as vast and varied as the spectrum of light — we just need the right lens to see it all.\n\nPigment — sắc tố. Từ đất son của người Ai Cập cổ đại đến sơn acrylic hiện đại — con người luôn tìm cách bắt giữ màu sắc. Câu mới: The rarest pigments in history were worth more than gold because they gave artists the power to capture what the eye sees but the hand cannot hold.\n\nHue — sắc. Tên gọi đơn giản nhất của màu — nhưng đằng sau mỗi hue là cả một thế giới cảm xúc. Câu mới: Two people can agree on the hue of a flower but disagree completely on the feeling it creates.\n\nShade — sắc thái tối. Thêm một chút bóng tối vào bất kỳ màu nào, và nó trở nên sâu hơn, bí ẩn hơn. Câu mới: Life, like color, gains depth through its darker shades — without shadow, we would never appreciate the light.\n\nPalette — bảng màu. Mỗi quyết định bạn đưa ra trong cuộc sống đều thêm một màu vào palette cá nhân của bạn. Câu mới: The palette you choose for your life — the people, the places, the experiences — determines the masterpiece you create.\n\nCanvas — toan vẽ. Mỗi ngày mới là một canvas trống — bạn sẽ vẽ gì lên đó? Câu mới: Every morning offers a blank canvas, and the colors you choose to paint it with are entirely your own.\n\nPerception — sự cảm nhận. Có lẽ điều quan trọng nhất bạn học được hôm nay là: cách bạn nhìn thế giới không phải là cách duy nhất. Câu mới: Changing your perception does not change reality, but it changes everything about how you experience it.\n\nWavelength — bước sóng. Mỗi màu là một bước sóng — mỗi người là một tần số — và khi chúng ta tìm được người cùng wavelength, mọi thứ trở nên hài hòa. Câu mới: The most meaningful connections happen when two people find themselves on the same wavelength, seeing the world in the same light.\n\nVibrant — rực rỡ. Những khoảnh khắc vibrant nhất trong cuộc sống thường là những khoảnh khắc bạn thực sự hiện diện. Câu mới: A vibrant life is not about doing extraordinary things — it is about being fully present in ordinary moments.\n\nContrast — sự tương phản. Không có bóng tối, bạn không thể thấy ánh sáng. Không có contrast, cuộc sống sẽ phẳng lặng. Câu mới: The contrast between where you started and where you are now is the truest measure of how far you have come.\n\nSaturate — bão hòa. Khi bạn đắm chìm hoàn toàn vào một điều gì đó — đó là lúc bạn sống trọn vẹn nhất. Câu mới: To truly learn something, you must saturate yourself in it — read about it, talk about it, dream about it.\n\nTint — sắc nhạt. Đôi khi vẻ đẹp không nằm ở màu sắc mạnh mẽ mà ở những tint nhẹ nhàng, tinh tế. Câu mới: The most beautiful moments often come in soft tints — a quiet smile, a gentle word, a brief glance that says everything.\n\nIlluminate — chiếu sáng. Học không phải là thêm thứ mới vào đầu — mà là illuminate những gì đã luôn ở đó. Câu mới: The purpose of education is not to fill an empty mind but to illuminate a curious one.\n\nPrism — lăng kính. Mỗi trải nghiệm mới là một prism — nó tách thế giới thành những màu sắc mà trước đó bạn không biết là tồn tại. Câu mới: Every new language you learn is a prism that reveals colors in the world you never knew existed.\n\nGradient — sự chuyển màu. Cuộc sống không phải là đen trắng — mà là một gradient vô tận giữa hai cực. Câu mới: Growth is never a sudden jump — it is a gradient, so slow that you only notice it when you look back.\n\nOpaque — đục. Có những thứ trong cuộc sống mà bạn không thể nhìn xuyên qua — và đôi khi đó là điều tốt. Câu mới: Some mysteries are meant to remain opaque — not everything needs to be understood to be appreciated.\n\nTranslucent — mờ. Giữa hoàn toàn rõ ràng và hoàn toàn bí ẩn, có một vùng translucent — nơi bạn thấy đủ để tò mò nhưng không đủ để chắc chắn. Câu mới: The best art is translucent — it lets enough light through to intrigue you but keeps enough hidden to make you wonder.\n\nAesthetic — thẩm mỹ. Cuối cùng, aesthetic không phải là về cái đẹp khách quan — mà là về cách bạn chọn nhìn thế giới. Câu mới: Your aesthetic is your signature — the unique way you see beauty in a world that everyone else takes for granted.\n\nBạn đã đi qua 18 từ — 18 cánh cửa mở ra một thế giới mà trước đây bạn nhìn mỗi ngày nhưng chưa thực sự thấy. Từ bây giờ, mỗi khi bạn nhìn một bức tranh, một hoàng hôn, hay thậm chí một chiếc áo — hãy tự hỏi: tôi đang thấy gì, và tại sao tôi thấy nó theo cách này? Câu trả lời sẽ luôn phức tạp hơn bạn tưởng — và đó chính là vẻ đẹp của nó. Chúc bạn luôn nhìn thế giới bằng đôi mắt tò mò và trái tim rộng mở."
                    }
                }
            ]
        }
    ]
}

# ── Validate ──
print("Validating content...")
validate_balanced_skills_standard(content)
print("  ✓ balanced_skills_standard structure OK")
validate_content_type_tags(content)
print("  ✓ contentTypeTags OK")
validate_bilingual_prompts(content, "intermediate")
print("  ✓ bilingual prompts OK")
print("All validations passed!\n")

# ── Upload ──
token = get_firebase_id_token(UID)
resp = requests.post(
    f"{API_BASE}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
resp.raise_for_status()
data = resp.json()
curriculum_id = data.get("id") or data.get("curriculum", {}).get("id")
print(f"Created curriculum: {curriculum_id}")
print(f"Title: {content['title']}")
print(f"Level: intermediate | Skill: balanced_skills | Content: podcast")
print(f"Words: 18 (3 groups of 6)")
