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

# Curriculum #44: TED-Ed: The History of Chocolate
# Level: preintermediate | Skill focus: balanced_skills | Content type: ["podcast"]
# Topic: Food | 18 words (3 groups of 6), 5 sessions, bilingual (vi-en)
# Description tone: vivid_scenario (different from previous podcast tones: provocative_question, empathetic_observation, bold_declaration)
# Farewell tone: practical_momentum (different from previous: introspective_guide, warm_accountability, team_building_energy)
# W1: cacao, harvest, ferment, roast, bitter, plantation
# W2: trade, export, luxury, confection, bean, grind
# W3: mold, temper, artisan, origin, cultivate, blend

content = {
    "title": "TED-Ed: The History of Chocolate",
    "contentTypeTags": ["podcast"],
    "description": "BẠN ĐANG CẦM TRÊN TAY MỘT THANH SOCOLA — NHƯNG BẠN CÓ BIẾT NÓ ĐÃ ĐI QUA BAO NHIÊU THẾ KỶ ĐỂ ĐẾN ĐƯỢC VỚI BẠN KHÔNG?\n\nHãy tưởng tượng bạn đang đứng giữa một khu rừng nhiệt đới ở Mexico, cách đây hơn 3.000 năm. Xung quanh bạn là những cây cacao cao lớn, trái chín vàng treo lủng lẳng trên thân. Một người nông dân Maya đang cẩn thận harvest những trái cacao, tách hạt ra, và để chúng ferment dưới lá chuối. Mùi hương nồng nàn, hơi chua, hơi đắng — đó là mùi của socola nguyên bản, trước khi đường và sữa được thêm vào.\n\nTừ thức uống đắng của các vị vua Aztec đến thanh socola ngọt ngào trong cửa hàng tiện lợi, hành trình của chocolate là một câu chuyện về trade, plantation, và sự sáng tạo không ngừng. Người châu Âu đã biến nó từ một thức uống luxury của giới quý tộc thành một confection phổ biến toàn cầu.\n\nHai nhân vật Hà và Minh sẽ dẫn bạn qua hành trình này — từ cách người Mesoamerica cultivate cacao, đến cách các artisan hiện đại temper và mold socola thành những tác phẩm nghệ thuật. Bạn sẽ hiểu tại sao hạt cacao từng được dùng làm tiền tệ, tại sao socola Bỉ nổi tiếng thế giới, và tại sao blend đúng cách là bí quyết của mọi thanh socola ngon.\n\n18 từ vựng trong bài học này — từ cacao đến blend — sẽ giúp bạn nói về lịch sử ẩm thực, thương mại quốc tế, và nghệ thuật làm socola bằng tiếng Anh một cách tự tin.",
    "preview": {
        "text": "How did a bitter drink from ancient Mesoamerica become the world's favorite sweet treat? In this podcast-inspired lesson, you will learn 18 English words about the history of chocolate: cacao, harvest, ferment, roast, bitter, plantation, trade, export, luxury, confection, bean, grind, mold, temper, artisan, origin, cultivate, and blend. Follow Hà and Minh as they explore how the Maya and Aztec civilizations first used cacao, how European traders transformed it into a global commodity, and how modern artisans craft chocolate today. Hà is passionate about food history and shares fascinating stories from TED-Ed, while Minh loves chocolate and wants to understand what makes a great bar. Through three conversational reading passages, a full review session, and a final combined reading, you will discover the journey from cacao plantation to chocolate shop. By the end, you will be able to discuss food history, describe production processes, and explain the cultural significance of chocolate — all in English."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng — Lịch sử socola",
                    "description": "Giới thiệu chủ đề lịch sử socola và tổng quan bài học.",
                    "data": {
                        "text": "Chào mừng bạn đến với TED-Ed: The History of Chocolate — bài học podcast tiếng Anh về một trong những câu chuyện ẩm thực hấp dẫn nhất thế giới: lịch sử của socola. Bạn có biết rằng socola đã tồn tại hơn 3.000 năm không? Và ban đầu, nó không hề ngọt — mà rất đắng? Từ thức uống thiêng liêng của người Maya đến thanh kẹo trong túi bạn, hành trình của socola là một câu chuyện đầy bất ngờ.\n\nBài học này có 18 từ vựng chia thành 3 phần. Trong phần 1, bạn sẽ học 6 từ đầu tiên: cacao, harvest, ferment, roast, bitter, và plantation. Đây là những từ về nguồn gốc và cách chế biến cacao — bước đầu tiên trong hành trình tạo ra socola."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Dạy 6 từ vựng: cacao, harvest, ferment, roast, bitter, plantation.",
                    "data": {
                        "text": "Hãy cùng tìm hiểu 6 từ vựng đầu tiên nhé.\n\nTừ đầu tiên là cacao — danh từ — nghĩa là cây cacao, hạt cacao. Cacao là loại cây nhiệt đới có trái chứa hạt — và từ những hạt đó, người ta làm ra socola. Ví dụ: 'The Maya were among the first people to cultivate cacao trees.' Trong bài đọc, Hà giải thích rằng cacao mọc ở vùng nhiệt đới gần xích đạo.\n\nTừ thứ hai là harvest — động từ và danh từ — nghĩa là thu hoạch. Harvest là khi bạn hái hoặc cắt nông sản khi chúng đã chín. Ví dụ: 'Farmers harvest cacao pods by hand because machines can damage the trees.' Trong bài đọc, Minh ngạc nhiên khi biết rằng việc harvest cacao vẫn được làm thủ công.\n\nTừ thứ ba là ferment — động từ — nghĩa là lên men. Ferment là quá trình vi sinh vật phân hủy đường trong thực phẩm, tạo ra hương vị mới. Ví dụ: 'After harvesting, cacao beans must ferment for several days to develop their flavor.' Trong bài đọc, Hà nói rằng nếu không ferment đúng cách, socola sẽ không có hương vị đặc trưng.\n\nTừ thứ tư là roast — động từ — nghĩa là rang, nướng. Roast là khi bạn nấu thực phẩm bằng nhiệt độ cao trong lò hoặc trên chảo. Ví dụ: 'The way you roast cacao beans determines the final taste of the chocolate.' Trong bài đọc, Hà giải thích rằng mỗi nhà sản xuất có cách roast riêng — đó là bí quyết của họ.\n\nTừ thứ năm là bitter — tính từ — nghĩa là đắng. Bitter là vị ngược lại với ngọt — như vị cà phê đen không đường hoặc socola đen 90%. Ví dụ: 'Ancient Mesoamericans drank chocolate as a bitter beverage without any sugar.' Trong bài đọc, Minh thử nếm cacao nguyên chất và thấy nó rất bitter.\n\nTừ cuối cùng là plantation — danh từ — nghĩa là đồn điền, trang trại lớn. Plantation là một khu đất rộng lớn nơi người ta trồng một loại cây nhất định — như cacao, cà phê, hoặc cao su. Ví dụ: 'Many cacao plantations are located in West Africa and South America.' Trong bài đọc, Hà kể về những plantation cacao đầu tiên ở Trung Mỹ.\n\nSáu từ đầu tiên đã sẵn sàng! Hãy bắt đầu với flashcard, rồi đọc cuộc trò chuyện giữa Hà và Minh về nguồn gốc socola nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nguồn gốc cacao",
                    "description": "Học 6 từ: cacao, harvest, ferment, roast, bitter, plantation",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nguồn gốc cacao",
                    "description": "Học 6 từ: cacao, harvest, ferment, roast, bitter, plantation",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nguồn gốc cacao",
                    "description": "Học 6 từ: cacao, harvest, ferment, roast, bitter, plantation",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nguồn gốc cacao",
                    "description": "Học 6 từ: cacao, harvest, ferment, roast, bitter, plantation",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 1",
                    "description": "Giới thiệu ngữ pháp và cách dùng từ vựng trong ngữ cảnh bài đọc.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc cuộc trò chuyện giữa Hà và Minh. Hà rất đam mê lịch sử ẩm thực và thường xem các video TED-Ed. Minh thì yêu socola và muốn hiểu tại sao socola lại đặc biệt đến vậy. Trong bài đọc này, họ nói về nguồn gốc cacao ở Trung Mỹ cổ đại và cách người Maya chế biến nó. Hãy chú ý cách các từ cacao, harvest, ferment, roast, bitter, và plantation được dùng trong câu chuyện nhé. Một điểm ngữ pháp quan trọng: khi kể về lịch sử, chúng ta dùng thì quá khứ đơn — ví dụ 'the Maya harvested cacao' hoặc 'they roasted the beans over fire.' Hãy đọc chậm và thưởng thức nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nguồn gốc cacao ở Trung Mỹ",
                    "description": "Hà and Minh discuss the ancient origins of cacao in Mesoamerica.",
                    "data": {
                        "text": "Hà and Minh are sitting in a small chocolate café in Hanoi. Minh is eating a piece of dark chocolate. He makes a face.\n\n'This is so bitter,' he says. 'I prefer milk chocolate.'\n\nHà laughs. 'That bitter taste is actually closer to the original chocolate. Did you know that chocolate was not sweet at all for most of its history?'\n\n'Really?' Minh asks. 'How did it taste?'\n\n'Very bitter,' Hà says. 'I watched a TED-Ed video about this. The story of chocolate begins with cacao — a tropical tree that grows near the equator. The Maya civilization in Central America was one of the first to use cacao, more than three thousand years ago.'\n\n'Three thousand years?' Minh is surprised. 'That is older than most countries.'\n\n'Yes,' Hà says. 'The Maya would harvest the cacao pods from the trees by hand. Inside each pod, there are about thirty to fifty cacao beans covered in white pulp. After they harvest the pods, they remove the beans and let them ferment under banana leaves for about five to seven days.'\n\n'Why do they need to ferment them?' Minh asks.\n\n'Fermentation is what gives chocolate its flavor,' Hà explains. 'Without it, the beans taste flat and sour. The fermentation process breaks down the sugars and creates the complex flavors we associate with chocolate. After the beans ferment, they dry them in the sun and then roast them over fire.'\n\n'So roasting is like what we do with coffee beans?' Minh asks.\n\n'Exactly,' Hà says. 'The way you roast the beans changes the flavor completely. A light roast keeps more of the fruity, acidic notes. A dark roast brings out deeper, more bitter flavors.'\n\n'And where did they grow all this cacao?' Minh asks.\n\n'The first cacao trees grew wild in the rainforests of Central America,' Hà says. 'But as demand grew, people started creating plantations — large farms dedicated to growing cacao. The Maya had cacao plantations in what is now Guatemala, Belize, and southern Mexico. Cacao was so valuable that they even used the beans as money.'\n\nMinh looks at his chocolate bar. 'So I am eating ancient currency right now.'\n\nHà smiles. 'In a way, yes. Every piece of chocolate has thousands of years of history behind it.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nguồn gốc cacao ở Trung Mỹ",
                    "description": "Hà and Minh discuss the ancient origins of cacao in Mesoamerica.",
                    "data": {
                        "text": "Hà and Minh are sitting in a small chocolate café in Hanoi. Minh is eating a piece of dark chocolate. He makes a face.\n\n'This is so bitter,' he says. 'I prefer milk chocolate.'\n\nHà laughs. 'That bitter taste is actually closer to the original chocolate. Did you know that chocolate was not sweet at all for most of its history?'\n\n'Really?' Minh asks. 'How did it taste?'\n\n'Very bitter,' Hà says. 'I watched a TED-Ed video about this. The story of chocolate begins with cacao — a tropical tree that grows near the equator. The Maya civilization in Central America was one of the first to use cacao, more than three thousand years ago.'\n\n'Three thousand years?' Minh is surprised. 'That is older than most countries.'\n\n'Yes,' Hà says. 'The Maya would harvest the cacao pods from the trees by hand. Inside each pod, there are about thirty to fifty cacao beans covered in white pulp. After they harvest the pods, they remove the beans and let them ferment under banana leaves for about five to seven days.'\n\n'Why do they need to ferment them?' Minh asks.\n\n'Fermentation is what gives chocolate its flavor,' Hà explains. 'Without it, the beans taste flat and sour. The fermentation process breaks down the sugars and creates the complex flavors we associate with chocolate. After the beans ferment, they dry them in the sun and then roast them over fire.'\n\n'So roasting is like what we do with coffee beans?' Minh asks.\n\n'Exactly,' Hà says. 'The way you roast the beans changes the flavor completely. A light roast keeps more of the fruity, acidic notes. A dark roast brings out deeper, more bitter flavors.'\n\n'And where did they grow all this cacao?' Minh asks.\n\n'The first cacao trees grew wild in the rainforests of Central America,' Hà says. 'But as demand grew, people started creating plantations — large farms dedicated to growing cacao. The Maya had cacao plantations in what is now Guatemala, Belize, and southern Mexico. Cacao was so valuable that they even used the beans as money.'\n\nMinh looks at his chocolate bar. 'So I am eating ancient currency right now.'\n\nHà smiles. 'In a way, yes. Every piece of chocolate has thousands of years of history behind it.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nguồn gốc cacao ở Trung Mỹ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Hà and Minh are sitting in a small chocolate café in Hanoi. Minh is eating a piece of dark chocolate. He makes a face.\n\n'This is so bitter,' he says. 'I prefer milk chocolate.'\n\nHà laughs. 'That bitter taste is actually closer to the original chocolate. Did you know that chocolate was not sweet at all for most of its history?'\n\n'Really?' Minh asks. 'How did it taste?'\n\n'Very bitter,' Hà says. 'I watched a TED-Ed video about this. The story of chocolate begins with cacao — a tropical tree that grows near the equator. The Maya civilization in Central America was one of the first to use cacao, more than three thousand years ago.'\n\n'Three thousand years?' Minh is surprised. 'That is older than most countries.'\n\n'Yes,' Hà says. 'The Maya would harvest the cacao pods from the trees by hand. Inside each pod, there are about thirty to fifty cacao beans covered in white pulp. After they harvest the pods, they remove the beans and let them ferment under banana leaves for about five to seven days.'\n\n'Why do they need to ferment them?' Minh asks.\n\n'Fermentation is what gives chocolate its flavor,' Hà explains. 'Without it, the beans taste flat and sour. The fermentation process breaks down the sugars and creates the complex flavors we associate with chocolate. After the beans ferment, they dry them in the sun and then roast them over fire.'\n\n'So roasting is like what we do with coffee beans?' Minh asks.\n\n'Exactly,' Hà says. 'The way you roast the beans changes the flavor completely. A light roast keeps more of the fruity, acidic notes. A dark roast brings out deeper, more bitter flavors.'\n\n'And where did they grow all this cacao?' Minh asks.\n\n'The first cacao trees grew wild in the rainforests of Central America,' Hà says. 'But as demand grew, people started creating plantations — large farms dedicated to growing cacao. The Maya had cacao plantations in what is now Guatemala, Belize, and southern Mexico. Cacao was so valuable that they even used the beans as money.'\n\nMinh looks at his chocolate bar. 'So I am eating ancient currency right now.'\n\nHà smiles. 'In a way, yes. Every piece of chocolate has thousands of years of history behind it.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nguồn gốc cacao",
                    "description": "Viết câu sử dụng từ vựng về cacao, thu hoạch, và chế biến.",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation"],
                        "items": [
                            {
                                "targetVocab": "cacao",
                                "prompt": "Hãy dùng từ 'cacao' để viết một câu về cây cacao hoặc hạt cacao. Ví dụ: Cacao trees need warm temperatures and plenty of rain to produce healthy pods."
                            },
                            {
                                "targetVocab": "harvest",
                                "prompt": "Hãy dùng từ 'harvest' để viết một câu về việc thu hoạch. Ví dụ: Farmers harvest cacao pods twice a year during the wet and dry seasons."
                            },
                            {
                                "targetVocab": "ferment",
                                "prompt": "Hãy dùng từ 'ferment' để viết một câu về quá trình lên men. Ví dụ: You must ferment the cacao beans for several days to bring out the chocolate flavor."
                            },
                            {
                                "targetVocab": "roast",
                                "prompt": "Hãy dùng từ 'roast' để viết một câu về việc rang. Ví dụ: The factory workers roast the beans at different temperatures depending on the type of chocolate."
                            },
                            {
                                "targetVocab": "bitter",
                                "prompt": "Hãy dùng từ 'bitter' để viết một câu về vị đắng. Ví dụ: Dark chocolate with ninety percent cacao has a strong bitter taste that not everyone enjoys."
                            },
                            {
                                "targetVocab": "plantation",
                                "prompt": "Hãy dùng từ 'plantation' để viết một câu về đồn điền. Ví dụ: The largest cacao plantations in the world are found in Ivory Coast and Ghana."
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
                    "title": "Chào mừng phần 2 — Thương mại và xa xỉ",
                    "description": "Ôn lại phần 1 và giới thiệu chủ đề thương mại socola.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với phần 2 của TED-Ed: The History of Chocolate! Trong phần trước, bạn đã học 6 từ vựng về nguồn gốc cacao: cacao là cây và hạt cacao — nguyên liệu gốc của socola. Harvest là thu hoạch — hái trái cacao từ cây. Ferment là lên men — quá trình tạo hương vị cho hạt cacao. Roast là rang — bước quan trọng quyết định vị socola. Bitter là đắng — vị nguyên bản của cacao không đường. Và plantation là đồn điền — nơi trồng cacao quy mô lớn.\n\nBạn cũng đã đọc cuộc trò chuyện giữa Hà và Minh — Hà kể về cách người Maya harvest cacao, ferment hạt dưới lá chuối, và roast trên lửa.\n\nBây giờ, chúng ta sẽ đi tiếp vào giai đoạn thương mại — khi socola từ Trung Mỹ lan ra khắp thế giới. Bạn sẽ học 6 từ mới: trade, export, luxury, confection, bean, và grind."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Dạy 6 từ vựng: trade, export, luxury, confection, bean, grind.",
                    "data": {
                        "text": "Hãy cùng học 6 từ mới nhé.\n\nTừ đầu tiên là trade — danh từ và động từ — nghĩa là thương mại, buôn bán. Trade là hoạt động mua bán hàng hóa giữa các quốc gia hoặc vùng miền. Ví dụ: 'The chocolate trade connects farmers in Africa with consumers in Europe.' Trong bài đọc, Hà giải thích rằng trade đã đưa cacao từ châu Mỹ sang châu Âu vào thế kỷ 16.\n\nTừ thứ hai là export — động từ và danh từ — nghĩa là xuất khẩu. Export là khi một quốc gia bán hàng hóa sang quốc gia khác. Ví dụ: 'Ghana exports more than eight hundred thousand tons of cacao beans every year.' Trong bài đọc, Hà nói rằng các nước châu Phi hiện export phần lớn cacao trên thế giới.\n\nTừ thứ ba là luxury — danh từ và tính từ — nghĩa là xa xỉ, sang trọng. Luxury là thứ đắt tiền, hiếm có, và chỉ dành cho người giàu. Ví dụ: 'For centuries, chocolate was a luxury that only the wealthy could afford.' Trong bài đọc, Hà kể rằng ở châu Âu thế kỷ 17, socola là thức uống luxury của giới quý tộc.\n\nTừ thứ tư là confection — danh từ — nghĩa là bánh kẹo, đồ ngọt. Confection là bất kỳ loại thực phẩm ngọt nào được làm từ đường — kẹo, socola, bánh ngọt. Ví dụ: 'Modern chocolate bars are confections made with sugar, milk, and cacao.' Trong bài đọc, Minh nhận ra rằng socola ngày nay là một confection rất khác so với thức uống đắng nguyên bản.\n\nTừ thứ năm là bean — danh từ — nghĩa là hạt, đậu. Bean là hạt của một số loại cây — cacao bean, coffee bean, soy bean. Ví dụ: 'Each cacao pod contains about forty beans that will eventually become chocolate.' Trong bài đọc, Hà giải thích rằng chất lượng của bean quyết định chất lượng socola cuối cùng.\n\nTừ cuối cùng là grind — động từ — nghĩa là xay, nghiền. Grind là khi bạn nghiền thứ gì đó thành bột hoặc hỗn hợp mịn. Ví dụ: 'Workers grind the roasted cacao beans into a thick paste called chocolate liquor.' Trong bài đọc, Hà mô tả cách người xưa dùng đá để grind hạt cacao thành bột.\n\nSáu từ mới đã sẵn sàng! Hãy luyện flashcard rồi đọc về hành trình thương mại của socola nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thương mại và xa xỉ",
                    "description": "Học 6 từ: trade, export, luxury, confection, bean, grind",
                    "data": {
                        "vocabList": ["trade", "export", "luxury", "confection", "bean", "grind"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thương mại và xa xỉ",
                    "description": "Học 6 từ: trade, export, luxury, confection, bean, grind",
                    "data": {
                        "vocabList": ["trade", "export", "luxury", "confection", "bean", "grind"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thương mại và xa xỉ",
                    "description": "Học 6 từ: trade, export, luxury, confection, bean, grind",
                    "data": {
                        "vocabList": ["trade", "export", "luxury", "confection", "bean", "grind"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thương mại và xa xỉ",
                    "description": "Học 6 từ: trade, export, luxury, confection, bean, grind",
                    "data": {
                        "vocabList": ["trade", "export", "luxury", "confection", "bean", "grind"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 2",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về thương mại socola.",
                    "data": {
                        "text": "Bạn đã luyện xong flashcard rồi! Bây giờ hãy đọc cuộc trò chuyện tiếp theo giữa Hà và Minh. Lần này, họ nói về cách socola từ Trung Mỹ lan ra châu Âu qua thương mại, và cách nó trở thành thức uống xa xỉ của giới quý tộc. Hãy chú ý cách các từ trade, export, luxury, confection, bean, và grind xuất hiện trong câu chuyện. Một điểm ngữ pháp: khi kể về sự thay đổi qua thời gian, chúng ta dùng 'used to' và thì quá khứ — ví dụ 'chocolate used to be a luxury drink' hoặc 'they ground the beans by hand.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Socola chinh phục châu Âu",
                    "description": "Hà and Minh explore how chocolate traveled from the Americas to Europe through trade.",
                    "data": {
                        "text": "The next day, Hà and Minh meet at the same café. Minh has been thinking about what Hà told him.\n\n'So the Maya had chocolate for thousands of years,' Minh says. 'How did it get to Europe?'\n\n'Through trade,' Hà says. 'When Spanish explorers arrived in Central America in the early fifteen hundreds, they discovered that the Aztec people — who came after the Maya — valued cacao beans more than gold. The Aztec emperor Montezuma reportedly drank fifty cups of chocolate a day.'\n\n'Fifty cups?' Minh laughs. 'That is a lot of chocolate.'\n\n'It was a bitter drink mixed with chili peppers and spices,' Hà says. 'Very different from what we drink today. The Spanish brought cacao beans back to Europe. At first, Europeans did not like the bitter taste. But then someone had the idea to add sugar and honey. That changed everything.'\n\n'So Europeans made it sweet,' Minh says.\n\n'Yes. And it quickly became a luxury item,' Hà explains. 'In the sixteen hundreds, chocolate houses opened in London, Paris, and Madrid — like coffee shops, but for chocolate. Only wealthy people could afford it because cacao beans had to be exported from the Americas. The trade routes were long and expensive.'\n\n'How did they make the drink?' Minh asks.\n\n'They would grind the roasted beans into a fine paste using stone tools,' Hà says. 'Then they mixed the paste with hot water or milk and sugar. It was thick, rich, and very different from the thin hot chocolate we make today.'\n\n'So grinding was all done by hand?' Minh asks.\n\n'For centuries, yes,' Hà says. 'Workers would grind the beans for hours. It was hard physical work. But in the eighteen hundreds, machines were invented that could grind beans much faster. That made chocolate cheaper to produce.'\n\n'And that is when it stopped being a luxury?' Minh asks.\n\n'Gradually, yes,' Hà says. 'As more cacao plantations were established in Africa and Asia, the export of beans increased dramatically. More beans meant lower prices. And in eighteen forty-seven, a British company created the first chocolate bar — a solid confection you could eat, not just drink.'\n\nMinh takes a bite of his chocolate. 'So this little bar is the result of centuries of trade, export, and innovation.'\n\n'Exactly,' Hà says. 'From a bitter bean to a sweet confection — that is the power of global trade.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Socola chinh phục châu Âu",
                    "description": "Hà and Minh explore how chocolate traveled from the Americas to Europe through trade.",
                    "data": {
                        "text": "The next day, Hà and Minh meet at the same café. Minh has been thinking about what Hà told him.\n\n'So the Maya had chocolate for thousands of years,' Minh says. 'How did it get to Europe?'\n\n'Through trade,' Hà says. 'When Spanish explorers arrived in Central America in the early fifteen hundreds, they discovered that the Aztec people — who came after the Maya — valued cacao beans more than gold. The Aztec emperor Montezuma reportedly drank fifty cups of chocolate a day.'\n\n'Fifty cups?' Minh laughs. 'That is a lot of chocolate.'\n\n'It was a bitter drink mixed with chili peppers and spices,' Hà says. 'Very different from what we drink today. The Spanish brought cacao beans back to Europe. At first, Europeans did not like the bitter taste. But then someone had the idea to add sugar and honey. That changed everything.'\n\n'So Europeans made it sweet,' Minh says.\n\n'Yes. And it quickly became a luxury item,' Hà explains. 'In the sixteen hundreds, chocolate houses opened in London, Paris, and Madrid — like coffee shops, but for chocolate. Only wealthy people could afford it because cacao beans had to be exported from the Americas. The trade routes were long and expensive.'\n\n'How did they make the drink?' Minh asks.\n\n'They would grind the roasted beans into a fine paste using stone tools,' Hà says. 'Then they mixed the paste with hot water or milk and sugar. It was thick, rich, and very different from the thin hot chocolate we make today.'\n\n'So grinding was all done by hand?' Minh asks.\n\n'For centuries, yes,' Hà says. 'Workers would grind the beans for hours. It was hard physical work. But in the eighteen hundreds, machines were invented that could grind beans much faster. That made chocolate cheaper to produce.'\n\n'And that is when it stopped being a luxury?' Minh asks.\n\n'Gradually, yes,' Hà says. 'As more cacao plantations were established in Africa and Asia, the export of beans increased dramatically. More beans meant lower prices. And in eighteen forty-seven, a British company created the first chocolate bar — a solid confection you could eat, not just drink.'\n\nMinh takes a bite of his chocolate. 'So this little bar is the result of centuries of trade, export, and innovation.'\n\n'Exactly,' Hà says. 'From a bitter bean to a sweet confection — that is the power of global trade.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Socola chinh phục châu Âu",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "The next day, Hà and Minh meet at the same café. Minh has been thinking about what Hà told him.\n\n'So the Maya had chocolate for thousands of years,' Minh says. 'How did it get to Europe?'\n\n'Through trade,' Hà says. 'When Spanish explorers arrived in Central America in the early fifteen hundreds, they discovered that the Aztec people — who came after the Maya — valued cacao beans more than gold. The Aztec emperor Montezuma reportedly drank fifty cups of chocolate a day.'\n\n'Fifty cups?' Minh laughs. 'That is a lot of chocolate.'\n\n'It was a bitter drink mixed with chili peppers and spices,' Hà says. 'Very different from what we drink today. The Spanish brought cacao beans back to Europe. At first, Europeans did not like the bitter taste. But then someone had the idea to add sugar and honey. That changed everything.'\n\n'So Europeans made it sweet,' Minh says.\n\n'Yes. And it quickly became a luxury item,' Hà explains. 'In the sixteen hundreds, chocolate houses opened in London, Paris, and Madrid — like coffee shops, but for chocolate. Only wealthy people could afford it because cacao beans had to be exported from the Americas. The trade routes were long and expensive.'\n\n'How did they make the drink?' Minh asks.\n\n'They would grind the roasted beans into a fine paste using stone tools,' Hà says. 'Then they mixed the paste with hot water or milk and sugar. It was thick, rich, and very different from the thin hot chocolate we make today.'\n\n'So grinding was all done by hand?' Minh asks.\n\n'For centuries, yes,' Hà says. 'Workers would grind the beans for hours. It was hard physical work. But in the eighteen hundreds, machines were invented that could grind beans much faster. That made chocolate cheaper to produce.'\n\n'And that is when it stopped being a luxury?' Minh asks.\n\n'Gradually, yes,' Hà says. 'As more cacao plantations were established in Africa and Asia, the export of beans increased dramatically. More beans meant lower prices. And in eighteen forty-seven, a British company created the first chocolate bar — a solid confection you could eat, not just drink.'\n\nMinh takes a bite of his chocolate. 'So this little bar is the result of centuries of trade, export, and innovation.'\n\n'Exactly,' Hà says. 'From a bitter bean to a sweet confection — that is the power of global trade.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thương mại và xa xỉ",
                    "description": "Viết câu sử dụng từ vựng về thương mại, xuất khẩu, và sản phẩm socola.",
                    "data": {
                        "vocabList": ["trade", "export", "luxury", "confection", "bean", "grind"],
                        "items": [
                            {
                                "targetVocab": "trade",
                                "prompt": "Hãy dùng từ 'trade' để viết một câu về thương mại. Ví dụ: The global chocolate trade is worth more than one hundred billion dollars every year."
                            },
                            {
                                "targetVocab": "export",
                                "prompt": "Hãy dùng từ 'export' để viết một câu về xuất khẩu. Ví dụ: Vietnam has started to export high-quality cacao beans to European chocolate makers."
                            },
                            {
                                "targetVocab": "luxury",
                                "prompt": "Hãy dùng từ 'luxury' để viết một câu về sự xa xỉ. Ví dụ: Handmade Belgian chocolate is still considered a luxury gift in many countries."
                            },
                            {
                                "targetVocab": "confection",
                                "prompt": "Hãy dùng từ 'confection' để viết một câu về bánh kẹo. Ví dụ: The shop sells beautiful confections made from dark chocolate and tropical fruits."
                            },
                            {
                                "targetVocab": "bean",
                                "prompt": "Hãy dùng từ 'bean' để viết một câu về hạt cacao. Ví dụ: The quality of the bean determines whether the chocolate will taste fruity, nutty, or earthy."
                            },
                            {
                                "targetVocab": "grind",
                                "prompt": "Hãy dùng từ 'grind' để viết một câu về việc xay nghiền. Ví dụ: Modern machines can grind cacao beans into smooth chocolate paste in just a few hours."
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
                    "title": "Chào mừng phần 3 — Nghệ thuật làm socola hiện đại",
                    "description": "Ôn lại phần 1-2 và giới thiệu chủ đề nghệ thuật làm socola.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần 3 — phần cuối cùng trước khi ôn tập! Bạn đã đi được hai phần ba chặng đường rồi. Hãy cùng nhìn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ về nguồn gốc cacao: cacao là cây và hạt cacao, harvest là thu hoạch, ferment là lên men, roast là rang, bitter là đắng, và plantation là đồn điền. Trong phần 2, bạn học 6 từ về thương mại: trade là buôn bán, export là xuất khẩu, luxury là xa xỉ, confection là bánh kẹo, bean là hạt, và grind là xay nghiền.\n\nBây giờ, trong phần 3, chúng ta sẽ nói về nghệ thuật làm socola hiện đại — từ cách đổ khuôn đến kỹ thuật temper, và những nghệ nhân đang tạo ra socola tuyệt vời nhất thế giới. Bạn sẽ học 6 từ cuối cùng: mold, temper, artisan, origin, cultivate, và blend."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Dạy 6 từ vựng: mold, temper, artisan, origin, cultivate, blend.",
                    "data": {
                        "text": "Hãy cùng học 6 từ cuối cùng nhé.\n\nTừ đầu tiên là mold — danh từ và động từ — nghĩa là khuôn, đổ khuôn. Mold là dụng cụ có hình dạng nhất định mà bạn đổ chất lỏng vào để tạo hình. Ví dụ: 'The chocolate maker pours the liquid chocolate into a mold shaped like a heart.' Trong bài đọc, Minh được xem cách nghệ nhân đổ socola vào mold để tạo ra những viên socola đẹp mắt.\n\nTừ thứ hai là temper — động từ — nghĩa là ủ, xử lý nhiệt. Temper trong ngữ cảnh socola là kỹ thuật làm nóng và làm nguội socola theo trình tự chính xác để tạo ra bề mặt bóng và giòn. Ví dụ: 'If you do not temper chocolate properly, it will look dull and feel soft.' Trong bài đọc, Hà giải thích rằng temper là bước khó nhất trong nghệ thuật làm socola.\n\nTừ thứ ba là artisan — danh từ và tính từ — nghĩa là nghệ nhân, thủ công. Artisan là người làm sản phẩm bằng tay với kỹ năng cao — artisan chocolate là socola thủ công chất lượng cao. Ví dụ: 'Artisan chocolate makers often source their beans directly from small farms.' Trong bài đọc, Hà dẫn Minh đến một cửa hàng artisan chocolate ở Hà Nội.\n\nTừ thứ tư là origin — danh từ — nghĩa là nguồn gốc, xuất xứ. Origin là nơi bắt đầu hoặc nơi xuất phát của một thứ gì đó. Ví dụ: 'Single-origin chocolate is made from beans that come from one specific region.' Trong bài đọc, Hà giải thích rằng origin của hạt cacao ảnh hưởng lớn đến hương vị socola.\n\nTừ thứ năm là cultivate — động từ — nghĩa là trồng trọt, canh tác. Cultivate là khi bạn chăm sóc và phát triển cây trồng một cách có hệ thống. Ví dụ: 'Farmers in Vietnam have started to cultivate high-quality cacao in the Mekong Delta.' Trong bài đọc, Hà kể rằng Việt Nam đang cultivate cacao và trở thành nguồn cung mới cho thị trường socola thế giới.\n\nTừ cuối cùng là blend — danh từ và động từ — nghĩa là pha trộn, hỗn hợp. Blend là khi bạn kết hợp nhiều nguyên liệu khác nhau để tạo ra sản phẩm cuối cùng. Ví dụ: 'Each chocolate company has its own secret blend of cacao beans from different regions.' Trong bài đọc, Minh học được rằng blend đúng cách là bí quyết tạo ra hương vị socola độc đáo.\n\nBạn đã có đủ 18 từ vựng rồi! Hãy luyện flashcard rồi đọc phần cuối của cuộc trò chuyện nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nghệ thuật làm socola",
                    "description": "Học 6 từ: mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nghệ thuật làm socola",
                    "description": "Học 6 từ: mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nghệ thuật làm socola",
                    "description": "Học 6 từ: mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nghệ thuật làm socola",
                    "description": "Học 6 từ: mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 3",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về nghệ thuật làm socola hiện đại.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc phần cuối của cuộc trò chuyện giữa Hà và Minh. Lần này, họ đến thăm một cửa hàng socola thủ công và tìm hiểu về nghệ thuật làm socola hiện đại. Hãy chú ý cách các từ mold, temper, artisan, origin, cultivate, và blend được dùng trong câu chuyện. Một điểm ngữ pháp: khi mô tả quy trình sản xuất, chúng ta thường dùng thì hiện tại đơn với bị động — ví dụ 'the chocolate is tempered carefully' hoặc 'beans are blended from different origins.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nghệ thuật làm socola thủ công",
                    "description": "Hà and Minh visit an artisan chocolate shop and learn about modern chocolate making.",
                    "data": {
                        "text": "On Saturday morning, Hà takes Minh to a small artisan chocolate shop in the Old Quarter of Hanoi. The shop smells incredible — warm, sweet, and slightly bitter.\n\n'This is amazing,' Minh says. 'I did not know we had artisan chocolate shops in Hanoi.'\n\n'Vietnam is actually becoming an important origin for cacao,' Hà says. 'Farmers in the Mekong Delta and the Central Highlands have started to cultivate cacao trees. The climate is perfect — warm, humid, with plenty of rain. Some international chocolate makers now buy Vietnamese beans because of their unique flavor.'\n\n'Vietnamese cacao?' Minh is surprised. 'I had no idea.'\n\nThe shop owner, a young woman named Lan, invites them to watch her work. She is making a batch of dark chocolate truffles.\n\n'The most important step is tempering,' Lan explains. 'When I temper the chocolate, I heat it to a specific temperature, then cool it down, then heat it again slightly. This process creates the perfect crystal structure in the cocoa butter. If I temper it correctly, the chocolate will be shiny, smooth, and will snap when you break it.'\n\n'What happens if you do not temper it?' Minh asks.\n\n'The chocolate looks dull and gray,' Lan says. 'It feels soft and melts too quickly in your hands. Tempering is what separates good chocolate from great chocolate.'\n\nShe pours the tempered chocolate into small molds — each one shaped like a cacao pod. 'I use these molds to create my signature shape,' she says. 'Every artisan has their own style.'\n\n'Where do your beans come from?' Hà asks.\n\n'I use a blend of beans from three different origins,' Lan says. 'Some from Ben Tre province in Vietnam — they have a fruity, slightly acidic flavor. Some from Ecuador — they are more floral and complex. And some from Ghana — they give a deep, classic chocolate taste. When I blend them together, I get a flavor that is unique to my shop.'\n\n'So the origin of the bean matters that much?' Minh asks.\n\n'Absolutely,' Lan says. 'Just like wine, chocolate tastes different depending on where the cacao was cultivated. The soil, the climate, the variety of cacao tree — everything affects the flavor. That is why single-origin chocolate has become so popular. People want to taste the difference.'\n\nMinh tries one of Lan's truffles. His eyes widen. 'This is the best chocolate I have ever tasted. It is not just sweet — it has layers of flavor.'\n\nLan smiles. 'That is what happens when you start with great beans, ferment and roast them carefully, grind them slowly, temper the chocolate with patience, and mold it with love. Every step matters.'\n\n'I will never look at a chocolate bar the same way again,' Minh says.\n\nHà nods. 'That is the beauty of understanding origin. When you know where something comes from and how it is made, you appreciate it so much more.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nghệ thuật làm socola thủ công",
                    "description": "Hà and Minh visit an artisan chocolate shop and learn about modern chocolate making.",
                    "data": {
                        "text": "On Saturday morning, Hà takes Minh to a small artisan chocolate shop in the Old Quarter of Hanoi. The shop smells incredible — warm, sweet, and slightly bitter.\n\n'This is amazing,' Minh says. 'I did not know we had artisan chocolate shops in Hanoi.'\n\n'Vietnam is actually becoming an important origin for cacao,' Hà says. 'Farmers in the Mekong Delta and the Central Highlands have started to cultivate cacao trees. The climate is perfect — warm, humid, with plenty of rain. Some international chocolate makers now buy Vietnamese beans because of their unique flavor.'\n\n'Vietnamese cacao?' Minh is surprised. 'I had no idea.'\n\nThe shop owner, a young woman named Lan, invites them to watch her work. She is making a batch of dark chocolate truffles.\n\n'The most important step is tempering,' Lan explains. 'When I temper the chocolate, I heat it to a specific temperature, then cool it down, then heat it again slightly. This process creates the perfect crystal structure in the cocoa butter. If I temper it correctly, the chocolate will be shiny, smooth, and will snap when you break it.'\n\n'What happens if you do not temper it?' Minh asks.\n\n'The chocolate looks dull and gray,' Lan says. 'It feels soft and melts too quickly in your hands. Tempering is what separates good chocolate from great chocolate.'\n\nShe pours the tempered chocolate into small molds — each one shaped like a cacao pod. 'I use these molds to create my signature shape,' she says. 'Every artisan has their own style.'\n\n'Where do your beans come from?' Hà asks.\n\n'I use a blend of beans from three different origins,' Lan says. 'Some from Ben Tre province in Vietnam — they have a fruity, slightly acidic flavor. Some from Ecuador — they are more floral and complex. And some from Ghana — they give a deep, classic chocolate taste. When I blend them together, I get a flavor that is unique to my shop.'\n\n'So the origin of the bean matters that much?' Minh asks.\n\n'Absolutely,' Lan says. 'Just like wine, chocolate tastes different depending on where the cacao was cultivated. The soil, the climate, the variety of cacao tree — everything affects the flavor. That is why single-origin chocolate has become so popular. People want to taste the difference.'\n\nMinh tries one of Lan's truffles. His eyes widen. 'This is the best chocolate I have ever tasted. It is not just sweet — it has layers of flavor.'\n\nLan smiles. 'That is what happens when you start with great beans, ferment and roast them carefully, grind them slowly, temper the chocolate with patience, and mold it with love. Every step matters.'\n\n'I will never look at a chocolate bar the same way again,' Minh says.\n\nHà nods. 'That is the beauty of understanding origin. When you know where something comes from and how it is made, you appreciate it so much more.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nghệ thuật làm socola thủ công",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "On Saturday morning, Hà takes Minh to a small artisan chocolate shop in the Old Quarter of Hanoi. The shop smells incredible — warm, sweet, and slightly bitter.\n\n'This is amazing,' Minh says. 'I did not know we had artisan chocolate shops in Hanoi.'\n\n'Vietnam is actually becoming an important origin for cacao,' Hà says. 'Farmers in the Mekong Delta and the Central Highlands have started to cultivate cacao trees. The climate is perfect — warm, humid, with plenty of rain. Some international chocolate makers now buy Vietnamese beans because of their unique flavor.'\n\n'Vietnamese cacao?' Minh is surprised. 'I had no idea.'\n\nThe shop owner, a young woman named Lan, invites them to watch her work. She is making a batch of dark chocolate truffles.\n\n'The most important step is tempering,' Lan explains. 'When I temper the chocolate, I heat it to a specific temperature, then cool it down, then heat it again slightly. This process creates the perfect crystal structure in the cocoa butter. If I temper it correctly, the chocolate will be shiny, smooth, and will snap when you break it.'\n\n'What happens if you do not temper it?' Minh asks.\n\n'The chocolate looks dull and gray,' Lan says. 'It feels soft and melts too quickly in your hands. Tempering is what separates good chocolate from great chocolate.'\n\nShe pours the tempered chocolate into small molds — each one shaped like a cacao pod. 'I use these molds to create my signature shape,' she says. 'Every artisan has their own style.'\n\n'Where do your beans come from?' Hà asks.\n\n'I use a blend of beans from three different origins,' Lan says. 'Some from Ben Tre province in Vietnam — they have a fruity, slightly acidic flavor. Some from Ecuador — they are more floral and complex. And some from Ghana — they give a deep, classic chocolate taste. When I blend them together, I get a flavor that is unique to my shop.'\n\n'So the origin of the bean matters that much?' Minh asks.\n\n'Absolutely,' Lan says. 'Just like wine, chocolate tastes different depending on where the cacao was cultivated. The soil, the climate, the variety of cacao tree — everything affects the flavor. That is why single-origin chocolate has become so popular. People want to taste the difference.'\n\nMinh tries one of Lan's truffles. His eyes widen. 'This is the best chocolate I have ever tasted. It is not just sweet — it has layers of flavor.'\n\nLan smiles. 'That is what happens when you start with great beans, ferment and roast them carefully, grind them slowly, temper the chocolate with patience, and mold it with love. Every step matters.'\n\n'I will never look at a chocolate bar the same way again,' Minh says.\n\nHà nods. 'That is the beauty of understanding origin. When you know where something comes from and how it is made, you appreciate it so much more.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nghệ thuật làm socola",
                    "description": "Viết câu sử dụng từ vựng về kỹ thuật làm socola và nghệ nhân.",
                    "data": {
                        "vocabList": ["mold", "temper", "artisan", "origin", "cultivate", "blend"],
                        "items": [
                            {
                                "targetVocab": "mold",
                                "prompt": "Hãy dùng từ 'mold' để viết một câu về khuôn đổ socola. Ví dụ: The chocolate maker uses a special mold to create beautiful shapes for each piece."
                            },
                            {
                                "targetVocab": "temper",
                                "prompt": "Hãy dùng từ 'temper' để viết một câu về kỹ thuật ủ socola. Ví dụ: Learning to temper chocolate takes years of practice and careful attention to temperature."
                            },
                            {
                                "targetVocab": "artisan",
                                "prompt": "Hãy dùng từ 'artisan' để viết một câu về nghệ nhân. Ví dụ: The artisan chocolate shop on our street makes everything by hand using local ingredients."
                            },
                            {
                                "targetVocab": "origin",
                                "prompt": "Hãy dùng từ 'origin' để viết một câu về nguồn gốc. Ví dụ: The origin of the cacao beans gives each chocolate bar its unique character and taste."
                            },
                            {
                                "targetVocab": "cultivate",
                                "prompt": "Hãy dùng từ 'cultivate' để viết một câu về trồng trọt. Ví dụ: Vietnamese farmers cultivate cacao trees in the warm climate of the southern provinces."
                            },
                            {
                                "targetVocab": "blend",
                                "prompt": "Hãy dùng từ 'blend' để viết một câu về pha trộn. Ví dụ: The secret to this chocolate is a special blend of beans from three different countries."
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
                        "text": "Chúc mừng bạn! Bạn đã học xong tất cả 18 từ vựng về lịch sử socola. Đây là một thành tích tuyệt vời — hãy cùng ôn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ về nguồn gốc: cacao là cây và hạt cacao — nguyên liệu gốc của mọi thanh socola. Harvest là thu hoạch — hái trái cacao từ cây bằng tay. Ferment là lên men — bước tạo hương vị đặc trưng cho hạt cacao. Roast là rang — quyết định vị cuối cùng của socola. Bitter là đắng — vị nguyên bản của cacao trước khi thêm đường. Plantation là đồn điền — nơi trồng cacao quy mô lớn.\n\nTrong phần 2, bạn học 6 từ về thương mại: trade là buôn bán — hoạt động đưa cacao từ châu Mỹ sang châu Âu. Export là xuất khẩu — các nước châu Phi export phần lớn cacao thế giới. Luxury là xa xỉ — socola từng chỉ dành cho giới quý tộc. Confection là bánh kẹo — socola ngày nay là một confection phổ biến. Bean là hạt — chất lượng bean quyết định chất lượng socola. Grind là xay nghiền — bước biến hạt thành bột socola.\n\nTrong phần 3, bạn học 6 từ cuối: mold là khuôn — dụng cụ tạo hình socola. Temper là ủ nhiệt — kỹ thuật tạo bề mặt bóng và giòn. Artisan là nghệ nhân — người làm socola thủ công chất lượng cao. Origin là nguồn gốc — nơi hạt cacao được trồng. Cultivate là trồng trọt — Việt Nam đang cultivate cacao chất lượng cao. Blend là pha trộn — kết hợp hạt từ nhiều vùng để tạo hương vị độc đáo.\n\nBây giờ, bạn sẽ ôn lại tất cả 18 từ qua flashcard và bài tập viết. Sẵn sàng chưa? Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: cacao, harvest, ferment, roast, bitter, plantation, trade, export, luxury, confection, bean, grind, mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation", "trade", "export", "luxury", "confection", "bean", "grind", "mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: cacao, harvest, ferment, roast, bitter, plantation, trade, export, luxury, confection, bean, grind, mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation", "trade", "export", "luxury", "confection", "bean", "grind", "mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: cacao, harvest, ferment, roast, bitter, plantation, trade, export, luxury, confection, bean, grind, mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation", "trade", "export", "luxury", "confection", "bean", "grind", "mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: cacao, harvest, ferment, roast, bitter, plantation, trade, export, luxury, confection, bean, grind, mold, temper, artisan, origin, cultivate, blend",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation", "trade", "export", "luxury", "confection", "bean", "grind", "mold", "temper", "artisan", "origin", "cultivate", "blend"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập lịch sử socola",
                    "description": "Viết câu ôn tập sử dụng tất cả 18 từ vựng về lịch sử socola.",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation", "trade", "export", "luxury", "confection", "bean", "grind", "mold", "temper", "artisan", "origin", "cultivate", "blend"],
                        "items": [
                            {
                                "targetVocab": "cacao",
                                "prompt": "Hãy dùng từ 'cacao' để viết một câu về vai trò của cacao trong lịch sử. Ví dụ: Cacao has been an important crop for over three thousand years, from ancient Maya rituals to modern desserts."
                            },
                            {
                                "targetVocab": "harvest",
                                "prompt": "Hãy dùng từ 'harvest' để viết một câu về mùa thu hoạch. Ví dụ: The harvest season for cacao varies by region, but most farms collect pods twice a year."
                            },
                            {
                                "targetVocab": "ferment",
                                "prompt": "Hãy dùng từ 'ferment' để viết một câu về tầm quan trọng của lên men. Ví dụ: Without proper fermentation, even the best cacao beans will not develop their full chocolate flavor."
                            },
                            {
                                "targetVocab": "roast",
                                "prompt": "Hãy dùng từ 'roast' để viết một câu về cách rang ảnh hưởng đến hương vị. Ví dụ: The temperature and time you use to roast cacao beans can completely change the taste of the final product."
                            },
                            {
                                "targetVocab": "bitter",
                                "prompt": "Hãy dùng từ 'bitter' để viết một câu về sở thích vị đắng. Ví dụ: Some people prefer bitter dark chocolate because it has more antioxidants and less sugar than milk chocolate."
                            },
                            {
                                "targetVocab": "plantation",
                                "prompt": "Hãy dùng từ 'plantation' để viết một câu về đồn điền cacao ngày nay. Ví dụ: Many modern cacao plantations are working to improve conditions for farmers and protect the environment."
                            },
                            {
                                "targetVocab": "trade",
                                "prompt": "Hãy dùng từ 'trade' để viết một câu về thương mại socola toàn cầu. Ví dụ: Fair trade programs help ensure that cacao farmers receive a fair price for their hard work."
                            },
                            {
                                "targetVocab": "export",
                                "prompt": "Hãy dùng từ 'export' để viết một câu về xuất khẩu cacao. Ví dụ: Countries in West Africa export the majority of the world's cacao, but they produce very little finished chocolate."
                            },
                            {
                                "targetVocab": "luxury",
                                "prompt": "Hãy dùng từ 'luxury' để viết một câu về socola xa xỉ ngày nay. Ví dụ: Luxury chocolate brands charge high prices because they use rare beans and traditional production methods."
                            },
                            {
                                "targetVocab": "confection",
                                "prompt": "Hãy dùng từ 'confection' để viết một câu về các loại bánh kẹo socola. Ví dụ: Valentine's Day is the biggest season for chocolate confections, with millions of boxes sold worldwide."
                            },
                            {
                                "targetVocab": "bean",
                                "prompt": "Hãy dùng từ 'bean' để viết một câu về các loại hạt cacao. Ví dụ: There are three main types of cacao beans: Criollo, Forastero, and Trinitario, each with a different flavor profile."
                            },
                            {
                                "targetVocab": "grind",
                                "prompt": "Hãy dùng từ 'grind' để viết một câu về quy trình xay. Ví dụ: Some artisan makers grind their beans using traditional stone mills to preserve the natural flavors."
                            },
                            {
                                "targetVocab": "mold",
                                "prompt": "Hãy dùng từ 'mold' để viết một câu về khuôn socola. Ví dụ: The chocolate maker designed a custom mold in the shape of famous Vietnamese landmarks."
                            },
                            {
                                "targetVocab": "temper",
                                "prompt": "Hãy dùng từ 'temper' để viết một câu về kỹ thuật ủ socola. Ví dụ: Professional chocolatiers must temper their chocolate precisely to achieve the perfect glossy finish."
                            },
                            {
                                "targetVocab": "artisan",
                                "prompt": "Hãy dùng từ 'artisan' để viết một câu về nghệ nhân socola. Ví dụ: The number of artisan chocolate makers in Vietnam has grown rapidly in the last five years."
                            },
                            {
                                "targetVocab": "origin",
                                "prompt": "Hãy dùng từ 'origin' để viết một câu về nguồn gốc socola. Ví dụ: Knowing the origin of your chocolate helps you understand its flavor and support ethical farming practices."
                            },
                            {
                                "targetVocab": "cultivate",
                                "prompt": "Hãy dùng từ 'cultivate' để viết một câu về trồng cacao. Ví dụ: It takes about five years for a newly planted cacao tree to cultivate enough pods for a commercial harvest."
                            },
                            {
                                "targetVocab": "blend",
                                "prompt": "Hãy dùng từ 'blend' để viết một câu về pha trộn socola. Ví dụ: The master chocolatier creates a unique blend by combining beans from Vietnam, Ecuador, and Madagascar."
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
                    "description": "Giới thiệu bài đọc cuối cùng kết hợp tất cả 18 từ vựng về lịch sử socola.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của TED-Ed: The History of Chocolate! Bạn đã đi một chặng đường ấn tượng. Trong phần 1, bạn học về nguồn gốc cacao với 6 từ: cacao, harvest, ferment, roast, bitter, plantation. Trong phần 2, bạn khám phá thương mại socola với 6 từ: trade, export, luxury, confection, bean, grind. Trong phần 3, bạn tìm hiểu nghệ thuật làm socola hiện đại với 6 từ: mold, temper, artisan, origin, cultivate, blend. Trong phần ôn tập, bạn đã luyện lại tất cả 18 từ.\n\nBây giờ, bạn sẽ đọc một bài tổng hợp — Hà và Minh gặp lại nhau và chia sẻ những gì họ đã học được về socola. Bài đọc này dùng tất cả 18 từ vựng bạn đã học. Hãy đọc chậm, thưởng thức câu chuyện, và chú ý cách mỗi từ được dùng trong ngữ cảnh thực tế nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Từ hạt cacao đến thanh socola — Hành trình 3.000 năm",
                    "description": "Hà and Minh reflect on the complete journey of chocolate from ancient times to modern artisan craft.",
                    "data": {
                        "text": "Two weeks have passed since Hà and Minh visited the artisan chocolate shop. They are sitting in a park, sharing a box of Vietnamese single-origin chocolate that Minh bought from Lan's shop.\n\n'I have been thinking a lot about chocolate since our conversations,' Minh says. 'I even watched the TED-Ed video you told me about. It is incredible how one little bean changed the world.'\n\nHà smiles. 'Tell me what you learned.'\n\n'Well, it all starts with cacao,' Minh says. 'A tropical tree that grows near the equator. The Maya were the first to cultivate it — they planted cacao trees on plantations in Central America more than three thousand years ago. They would harvest the pods by hand, remove the beans, and let them ferment under leaves for days. Then they would roast the beans over fire and grind them into a paste.'\n\n'And what did they do with the paste?' Hà asks.\n\n'They mixed it with water, chili peppers, and spices to make a bitter drink,' Minh says. 'No sugar at all. It was completely different from the sweet chocolate we know today. The Aztecs loved it so much that they used cacao beans as money. Imagine paying for your lunch with chocolate.'\n\nHà laughs. 'I would spend all my money very quickly.'\n\n'Then the Spanish came to the Americas and discovered cacao,' Minh continues. 'They brought the beans back to Europe through trade routes. At first, Europeans thought the bitter taste was strange. But when they added sugar, everything changed. Chocolate became a luxury drink for kings and queens. Chocolate houses opened in London and Paris — like exclusive clubs where only the wealthy could afford to drink chocolate.'\n\n'And how did it become available to everyone?' Hà asks.\n\n'Through industrialization and global trade,' Minh says. 'As European countries established cacao plantations in Africa and Asia, the export of beans increased enormously. More supply meant lower prices. Then in the eighteen hundreds, someone invented a way to make solid chocolate — the first confection you could eat instead of drink. That was the beginning of the chocolate bar.'\n\n'You really did your research,' Hà says, impressed.\n\n'But the part that fascinated me most was the modern artisan movement,' Minh says. 'People like Lan who care about every step — from the origin of the beans to the way they blend different varieties. She told us that the soil and climate where cacao is cultivated affect the flavor, just like wine. Vietnamese cacao from Ben Tre has a fruity taste, while Ghanaian cacao is deeper and more classic.'\n\n'And the technical skills,' Hà adds. 'The way she tempers the chocolate to get that perfect shine and snap. The way she pours it into molds to create beautiful shapes. It is truly an art.'\n\n'It is,' Minh agrees. 'I used to think chocolate was just a simple confection — something sweet you buy at the convenience store. But now I understand that every piece of chocolate represents thousands of years of history. Farmers who cultivate and harvest cacao by hand. Workers who ferment and roast the beans with care. Artisans who grind, temper, blend, and mold the chocolate into something extraordinary.'\n\nHe picks up a piece from the box. 'This piece right here — it started as a bean on a tree somewhere in Vietnam. A farmer harvested it. Someone fermented it, roasted it, ground it. Lan tempered it and poured it into a mold. And now it is here, in this park, with us.'\n\n'That is a beautiful way to think about it,' Hà says.\n\nMinh takes a bite. 'You know what? I think I finally understand why people call chocolate the food of the gods. It is not just about the taste. It is about the journey — from a bitter bean on a plantation to a luxury confection in your hand. Three thousand years of human creativity, trade, and craftsmanship in every single bite.'\n\nHà raises her piece of chocolate like a toast. 'To the history of chocolate.'\n\n'To the history of chocolate,' Minh repeats. And they both take a bite, savoring every layer of flavor that three millennia of human ingenuity created.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Từ hạt cacao đến thanh socola — Hành trình 3.000 năm",
                    "description": "Hà and Minh reflect on the complete journey of chocolate from ancient times to modern artisan craft.",
                    "data": {
                        "text": "Two weeks have passed since Hà and Minh visited the artisan chocolate shop. They are sitting in a park, sharing a box of Vietnamese single-origin chocolate that Minh bought from Lan's shop.\n\n'I have been thinking a lot about chocolate since our conversations,' Minh says. 'I even watched the TED-Ed video you told me about. It is incredible how one little bean changed the world.'\n\nHà smiles. 'Tell me what you learned.'\n\n'Well, it all starts with cacao,' Minh says. 'A tropical tree that grows near the equator. The Maya were the first to cultivate it — they planted cacao trees on plantations in Central America more than three thousand years ago. They would harvest the pods by hand, remove the beans, and let them ferment under leaves for days. Then they would roast the beans over fire and grind them into a paste.'\n\n'And what did they do with the paste?' Hà asks.\n\n'They mixed it with water, chili peppers, and spices to make a bitter drink,' Minh says. 'No sugar at all. It was completely different from the sweet chocolate we know today. The Aztecs loved it so much that they used cacao beans as money. Imagine paying for your lunch with chocolate.'\n\nHà laughs. 'I would spend all my money very quickly.'\n\n'Then the Spanish came to the Americas and discovered cacao,' Minh continues. 'They brought the beans back to Europe through trade routes. At first, Europeans thought the bitter taste was strange. But when they added sugar, everything changed. Chocolate became a luxury drink for kings and queens. Chocolate houses opened in London and Paris — like exclusive clubs where only the wealthy could afford to drink chocolate.'\n\n'And how did it become available to everyone?' Hà asks.\n\n'Through industrialization and global trade,' Minh says. 'As European countries established cacao plantations in Africa and Asia, the export of beans increased enormously. More supply meant lower prices. Then in the eighteen hundreds, someone invented a way to make solid chocolate — the first confection you could eat instead of drink. That was the beginning of the chocolate bar.'\n\n'You really did your research,' Hà says, impressed.\n\n'But the part that fascinated me most was the modern artisan movement,' Minh says. 'People like Lan who care about every step — from the origin of the beans to the way they blend different varieties. She told us that the soil and climate where cacao is cultivated affect the flavor, just like wine. Vietnamese cacao from Ben Tre has a fruity taste, while Ghanaian cacao is deeper and more classic.'\n\n'And the technical skills,' Hà adds. 'The way she tempers the chocolate to get that perfect shine and snap. The way she pours it into molds to create beautiful shapes. It is truly an art.'\n\n'It is,' Minh agrees. 'I used to think chocolate was just a simple confection — something sweet you buy at the convenience store. But now I understand that every piece of chocolate represents thousands of years of history. Farmers who cultivate and harvest cacao by hand. Workers who ferment and roast the beans with care. Artisans who grind, temper, blend, and mold the chocolate into something extraordinary.'\n\nHe picks up a piece from the box. 'This piece right here — it started as a bean on a tree somewhere in Vietnam. A farmer harvested it. Someone fermented it, roasted it, ground it. Lan tempered it and poured it into a mold. And now it is here, in this park, with us.'\n\n'That is a beautiful way to think about it,' Hà says.\n\nMinh takes a bite. 'You know what? I think I finally understand why people call chocolate the food of the gods. It is not just about the taste. It is about the journey — from a bitter bean on a plantation to a luxury confection in your hand. Three thousand years of human creativity, trade, and craftsmanship in every single bite.'\n\nHà raises her piece of chocolate like a toast. 'To the history of chocolate.'\n\n'To the history of chocolate,' Minh repeats. And they both take a bite, savoring every layer of flavor that three millennia of human ingenuity created.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Từ hạt cacao đến thanh socola — Hành trình 3.000 năm",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Two weeks have passed since Hà and Minh visited the artisan chocolate shop. They are sitting in a park, sharing a box of Vietnamese single-origin chocolate that Minh bought from Lan's shop.\n\n'I have been thinking a lot about chocolate since our conversations,' Minh says. 'I even watched the TED-Ed video you told me about. It is incredible how one little bean changed the world.'\n\nHà smiles. 'Tell me what you learned.'\n\n'Well, it all starts with cacao,' Minh says. 'A tropical tree that grows near the equator. The Maya were the first to cultivate it — they planted cacao trees on plantations in Central America more than three thousand years ago. They would harvest the pods by hand, remove the beans, and let them ferment under leaves for days. Then they would roast the beans over fire and grind them into a paste.'\n\n'And what did they do with the paste?' Hà asks.\n\n'They mixed it with water, chili peppers, and spices to make a bitter drink,' Minh says. 'No sugar at all. It was completely different from the sweet chocolate we know today. The Aztecs loved it so much that they used cacao beans as money. Imagine paying for your lunch with chocolate.'\n\nHà laughs. 'I would spend all my money very quickly.'\n\n'Then the Spanish came to the Americas and discovered cacao,' Minh continues. 'They brought the beans back to Europe through trade routes. At first, Europeans thought the bitter taste was strange. But when they added sugar, everything changed. Chocolate became a luxury drink for kings and queens. Chocolate houses opened in London and Paris — like exclusive clubs where only the wealthy could afford to drink chocolate.'\n\n'And how did it become available to everyone?' Hà asks.\n\n'Through industrialization and global trade,' Minh says. 'As European countries established cacao plantations in Africa and Asia, the export of beans increased enormously. More supply meant lower prices. Then in the eighteen hundreds, someone invented a way to make solid chocolate — the first confection you could eat instead of drink. That was the beginning of the chocolate bar.'\n\n'You really did your research,' Hà says, impressed.\n\n'But the part that fascinated me most was the modern artisan movement,' Minh says. 'People like Lan who care about every step — from the origin of the beans to the way they blend different varieties. She told us that the soil and climate where cacao is cultivated affect the flavor, just like wine. Vietnamese cacao from Ben Tre has a fruity taste, while Ghanaian cacao is deeper and more classic.'\n\n'And the technical skills,' Hà adds. 'The way she tempers the chocolate to get that perfect shine and snap. The way she pours it into molds to create beautiful shapes. It is truly an art.'\n\n'It is,' Minh agrees. 'I used to think chocolate was just a simple confection — something sweet you buy at the convenience store. But now I understand that every piece of chocolate represents thousands of years of history. Farmers who cultivate and harvest cacao by hand. Workers who ferment and roast the beans with care. Artisans who grind, temper, blend, and mold the chocolate into something extraordinary.'\n\nHe picks up a piece from the box. 'This piece right here — it started as a bean on a tree somewhere in Vietnam. A farmer harvested it. Someone fermented it, roasted it, ground it. Lan tempered it and poured it into a mold. And now it is here, in this park, with us.'\n\n'That is a beautiful way to think about it,' Hà says.\n\nMinh takes a bite. 'You know what? I think I finally understand why people call chocolate the food of the gods. It is not just about the taste. It is about the journey — from a bitter bean on a plantation to a luxury confection in your hand. Three thousand years of human creativity, trade, and craftsmanship in every single bite.'\n\nHà raises her piece of chocolate like a toast. 'To the history of chocolate.'\n\n'To the history of chocolate,' Minh repeats. And they both take a bite, savoring every layer of flavor that three millennia of human ingenuity created.'"
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích lịch sử socola",
                    "description": "Viết đoạn văn phân tích về lịch sử socola sử dụng từ vựng đã học.",
                    "data": {
                        "vocabList": ["cacao", "harvest", "ferment", "roast", "bitter", "plantation", "trade", "export", "luxury", "confection", "bean", "grind", "mold", "temper", "artisan", "origin", "cultivate", "blend"],
                        "instructions": "Viết một đoạn văn tiếng Anh (80-120 từ) phân tích hành trình của socola từ nguyên liệu thô đến sản phẩm hoàn chỉnh. Sử dụng ít nhất 6 từ vựng đã học trong bài.",
                        "prompts": [
                            "Describe the journey of chocolate from a cacao bean on a plantation to a finished product in a shop. Use words like harvest, ferment, roast, grind, temper, and mold to explain each step of the process.",
                            "Explain how chocolate changed from a bitter drink of ancient civilizations to a luxury confection enjoyed worldwide. Use words like trade, export, origin, artisan, cultivate, and blend to discuss the cultural and economic transformation."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay — farewell tone: practical_momentum.",
                    "data": {
                        "text": "Bạn đã hoàn thành TED-Ed: The History of Chocolate — và bây giờ bạn có 18 từ vựng mới sẵn sàng để dùng ngay trong cuộc sống thực. Hãy cùng ôn lại một lần cuối — lần này, tôi muốn bạn nghĩ về cách dùng mỗi từ trong tuần tới.\n\nCacao — cây và hạt cacao. Lần tới bạn mua socola, hãy đọc nhãn và tìm từ cacao. Câu mới: The percentage of cacao on a chocolate label tells you how much real chocolate is inside.\n\nHarvest — thu hoạch. Hãy nghĩ về harvest khi bạn ăn bất kỳ loại trái cây nào. Câu mới: Knowing when to harvest each crop is one of the most important skills a farmer can learn.\n\nFerment — lên men. Nhiều thực phẩm Việt Nam cũng được ferment — nước mắm, mắm tôm, dưa chua. Câu mới: Many traditional Vietnamese foods like fish sauce and pickled vegetables are made through fermentation.\n\nRoast — rang. Hãy dùng từ này khi nói về cà phê hoặc hạt. Câu mới: The aroma of freshly roasted coffee beans is one of the most recognizable smells in the world.\n\nBitter — đắng. Hãy mô tả vị của thức ăn bằng tiếng Anh khi bạn ăn. Câu mới: Vietnamese iced coffee has a pleasant bitter taste that pairs perfectly with sweet condensed milk.\n\nPlantation — đồn điền. Hãy dùng từ này khi nói về nông nghiệp. Câu mới: Coffee and rubber plantations played an important role in Vietnam's economic history.\n\nTrade — thương mại. Từ này xuất hiện rất nhiều trong tin tức kinh tế. Câu mới: International trade agreements affect the prices of everyday products like chocolate and coffee.\n\nExport — xuất khẩu. Việt Nam là nước export nhiều mặt hàng nông sản. Câu mới: Vietnam is one of the top exporters of coffee, rice, and seafood in the world.\n\nLuxury — xa xỉ. Hãy dùng từ này khi mô tả sản phẩm cao cấp. Câu mới: What was once a luxury for the wealthy often becomes an everyday item for everyone over time.\n\nConfection — bánh kẹo. Hãy dùng từ này thay vì chỉ nói candy hoặc sweet. Câu mới: The bakery on the corner makes beautiful confections using local chocolate and tropical fruits.\n\nBean — hạt. Từ này dùng cho nhiều loại hạt — coffee bean, soy bean, cacao bean. Câu mới: The type of bean a farmer chooses to plant determines the quality of the final product.\n\nGrind — xay nghiền. Hãy dùng từ này khi nói về cà phê hoặc gia vị. Câu mới: I prefer to grind my own coffee beans at home because the flavor is much fresher.\n\nMold — khuôn. Hãy dùng từ này khi nói về nấu ăn hoặc thủ công. Câu mới: You can buy silicone molds in many shapes to make homemade chocolate treats for your friends.\n\nTemper — ủ nhiệt. Đây là từ chuyên ngành rất ấn tượng khi bạn dùng đúng. Câu mới: If you want to make professional-looking chocolate at home, you need to learn how to temper it correctly.\n\nArtisan — nghệ nhân. Hãy dùng từ này khi nói về sản phẩm thủ công chất lượng cao. Câu mới: Supporting artisan producers helps preserve traditional skills and creates better products for everyone.\n\nOrigin — nguồn gốc. Hãy hỏi về origin khi bạn mua thực phẩm. Câu mới: Asking about the origin of your food is a simple way to become a more conscious consumer.\n\nCultivate — trồng trọt. Hãy dùng từ này khi nói về nông nghiệp hoặc phát triển kỹ năng. Câu mới: Vietnam has the perfect climate to cultivate many tropical crops that are in high demand worldwide.\n\nBlend — pha trộn. Hãy dùng từ này khi nói về cà phê, trà, hoặc socola. Câu mới: Creating the perfect blend requires tasting hundreds of samples and understanding how different flavors work together.\n\nVà thế là xong — 18 từ vựng, 18 công cụ mới trong hành trang tiếng Anh của bạn. Nhưng đây không phải là kiến thức để cất trong ngăn kéo. Đây là những từ bạn có thể dùng ngay — khi đi mua socola, khi đọc nhãn sản phẩm, khi nói chuyện về ẩm thực với bạn bè, hoặc khi xem video TED-Ed tiếp theo.\n\nTuần này, hãy thử một thử thách nhỏ: mua một thanh socola, đọc nhãn, và tìm xem origin của nó là đâu. Rồi khi ăn, hãy nghĩ về hành trình 3.000 năm mà mỗi miếng socola đã đi qua — từ harvest đến ferment, từ roast đến grind, từ temper đến mold. Bạn sẽ thấy mỗi miếng socola ngon hơn rất nhiều khi bạn hiểu câu chuyện đằng sau nó.\n\nCảm ơn bạn đã học cùng tôi. Hãy mang những từ này ra thế giới thật — và nhớ, kiến thức chỉ có giá trị khi bạn dùng nó. Hẹn gặp lại trong bài học tiếp theo!"
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
validate_bilingual_prompts(content, "preintermediate")
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
print(f"Level: preintermediate | Skill: balanced_skills | Content: podcast")
print(f"Words: 18 (3 groups of 6)")
