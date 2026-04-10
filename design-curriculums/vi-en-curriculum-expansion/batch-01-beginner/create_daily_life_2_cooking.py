"""
Create curriculum: Cooking at Home (Nấu Ăn Tại Nhà — Bước Đầu Tiên)
Level: beginner | Skill focus: balanced_skills | Content type: []
Topic: Daily life | 12 words (2 groups of 6) | 4 sessions | Bilingual (vi/en)
Tone: empathetic_observation | Farewell tone: quiet_awe
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from validate_curriculum import validate_balanced_skills_beginner, validate_content_type_tags, validate_bilingual_prompts

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Vocabulary ──
# Group 1 (Session 1): cook, recipe, ingredient, stir, boil, chop
# Group 2 (Session 2): pan, oven, taste, spice, meal, serve

W1 = ["cook", "recipe", "ingredient", "stir", "boil", "chop"]
W2 = ["pan", "oven", "taste", "spice", "meal", "serve"]
ALL_WORDS = W1 + W2

content = {
    "title": "Nấu Ăn Tại Nhà — Bước Đầu Tiên",
    "contentTypeTags": [],
    "description": (
        "BẠN ĐÃ BAO GIỜ ĐỨNG TRONG BẾP, MUỐN NẤU MỘT MÓN ĐƠN GIẢN, NHƯNG KHÔNG BIẾT GỌI TÊN TỪNG THỨ BẰNG TIẾNG ANH?\n\n"
        "Cái chảo trước mặt bạn — tiếng Anh gọi là gì? Hành động khuấy đều — nói sao cho đúng? "
        "Bạn muốn chia sẻ công thức nấu ăn với bạn bè nước ngoài, nhưng mỗi từ đều trở thành một bức tường.\n\n"
        "Nấu ăn bằng tiếng Anh giống như nấu mà không có công thức — "
        "bạn biết mùi vị mình muốn, nhưng không biết cách diễn đạt từng bước. "
        "12 từ vựng trong bài học này chính là cuốn sách dạy nấu ăn bằng tiếng Anh đầu tiên của bạn.\n\n"
        "Sau bài học, bạn sẽ tự tin mô tả cách nấu ăn, gọi tên dụng cụ bếp, "
        "và chia sẻ món ăn yêu thích bằng tiếng Anh — từ bếp nhà bạn ra thế giới.\n\n"
        "Vừa học từ vựng thiết thực, vừa nâng cấp khả năng diễn đạt — "
        "mỗi từ là một nguyên liệu giúp bạn \"nấu\" nên câu tiếng Anh hoàn chỉnh."
    ),
    "preview": {
        "text": (
            "You stand in your kitchen. The pot is boiling. The vegetables are ready. "
            "But how do you describe what you are doing — in English? "
            "This curriculum gives you 12 essential cooking words — "
            "cook, recipe, ingredient, stir, boil, chop, pan, oven, taste, spice, meal, and serve. "
            "Across four sessions, you will learn each word through flashcards, "
            "reading passages about real cooking moments at home, "
            "and guided writing exercises with Vietnamese instructions. "
            "By the end, you will confidently describe how to prepare a meal, "
            "name kitchen tools, and share your favorite recipes in English."
        )
    },
    "learningSessions": [
        # ════════════════════════════════════════════
        # SESSION 1 — Phần 1 (Words: cook, recipe, ingredient, stir, boil, chop)
        # ════════════════════════════════════════════
        {
            "title": "Phần 1",
            "activities": [
                # ── introAudio: Welcome + Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về nấu ăn tại nhà bằng tiếng Anh.",
                    "data": {
                        "text": (
                            "Xin chào và chào mừng bạn đến với bài học 'Nấu Ăn Tại Nhà'! "
                            "Hôm nay chúng ta sẽ học 6 từ vựng tiếng Anh rất quan trọng khi bạn nấu ăn. "
                            "Những từ này sẽ giúp bạn mô tả các bước nấu ăn và nguyên liệu bằng tiếng Anh. "
                            "Sáu từ hôm nay là: cook, recipe, ingredient, stir, boil, và chop.\n\n"

                            "Từ đầu tiên là 'cook'. Cook có thể là động từ hoặc danh từ. "
                            "Là động từ, nó nghĩa là 'nấu ăn'. Là danh từ, nó nghĩa là 'đầu bếp'. "
                            "Ví dụ: 'I cook dinner every evening.' — Tôi nấu bữa tối mỗi buổi chiều. "
                            "Trong bài đọc, bạn sẽ thấy từ 'cook' khi nhân vật nấu ăn cho gia đình.\n\n"

                            "Từ thứ hai là 'recipe'. Recipe là danh từ, nghĩa là 'công thức nấu ăn'. "
                            "Ví dụ: 'My grandmother has a great recipe for phở.' — Bà tôi có công thức nấu phở rất ngon. "
                            "Trong bài đọc, từ 'recipe' xuất hiện khi nhân vật tìm công thức trên điện thoại.\n\n"

                            "Từ thứ ba là 'ingredient'. Ingredient là danh từ, nghĩa là 'nguyên liệu'. "
                            "Ví dụ: 'We need fresh ingredients for this soup.' — Chúng ta cần nguyên liệu tươi cho món súp này. "
                            "Trong bài đọc, bạn sẽ thấy từ 'ingredient' khi nhân vật chuẩn bị nguyên liệu trước khi nấu.\n\n"

                            "Từ thứ tư là 'stir'. Stir là động từ, nghĩa là 'khuấy' hoặc 'đảo'. "
                            "Ví dụ: 'Stir the soup slowly.' — Khuấy súp từ từ. "
                            "Trong bài đọc, từ 'stir' xuất hiện khi nhân vật đảo thức ăn trong nồi.\n\n"

                            "Từ thứ năm là 'boil'. Boil là động từ, nghĩa là 'đun sôi' hoặc 'luộc'. "
                            "Ví dụ: 'Boil the water before you add the noodles.' — Đun sôi nước trước khi cho mì vào. "
                            "Trong bài đọc, bạn sẽ thấy từ 'boil' khi nhân vật đun nước để nấu ăn.\n\n"

                            "Từ cuối cùng là 'chop'. Chop là động từ, nghĩa là 'cắt' hoặc 'thái'. "
                            "Ví dụ: 'Chop the onions into small pieces.' — Thái hành thành miếng nhỏ. "
                            "Trong bài đọc, từ 'chop' xuất hiện khi nhân vật cắt rau chuẩn bị nấu ăn.\n\n"

                            "Bây giờ, hãy bắt đầu học từ vựng qua flashcards nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nấu ăn (Phần 1)",
                    "description": "Học 6 từ: cook, recipe, ingredient, stir, boil, chop",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nấu ăn (Phần 1)",
                    "description": "Học 6 từ: cook, recipe, ingredient, stir, boil, chop",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nấu ăn (Phần 1)",
                    "description": "Học 6 từ: cook, recipe, ingredient, stir, boil, chop",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nấu ăn (Phần 1)",
                    "description": "Học 6 từ: cook, recipe, ingredient, stir, boil, chop",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Lan nấu súp cho gia đình",
                    "description": "Lan follows a recipe to cook soup for her family.",
                    "data": {
                        "text": (
                            "Lan wants to cook dinner for her family. "
                            "She looks at a recipe on her phone. "
                            "The recipe is for vegetable soup.\n\n"
                            "First, she reads the ingredients. "
                            "She needs carrots, onions, and tomatoes. "
                            "She also needs salt and pepper.\n\n"
                            "Lan chops the carrots into small pieces. "
                            "She chops the onions too. "
                            "Then she boils water in a big pot.\n\n"
                            "She puts the vegetables in the pot. "
                            "She stirs the soup slowly. "
                            "The kitchen smells very good. "
                            "Lan is happy. She loves to cook."
                        ),
                        "vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lan nấu súp cho gia đình",
                    "description": "Lan follows a recipe to cook soup for her family.",
                    "data": {
                        "text": (
                            "Lan wants to cook dinner for her family. "
                            "She looks at a recipe on her phone. "
                            "The recipe is for vegetable soup.\n\n"
                            "First, she reads the ingredients. "
                            "She needs carrots, onions, and tomatoes. "
                            "She also needs salt and pepper.\n\n"
                            "Lan chops the carrots into small pieces. "
                            "She chops the onions too. "
                            "Then she boils water in a big pot.\n\n"
                            "She puts the vegetables in the pot. "
                            "She stirs the soup slowly. "
                            "The kitchen smells very good. "
                            "Lan is happy. She loves to cook."
                        ),
                        "vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lan nấu súp cho gia đình",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Lan wants to cook dinner for her family. "
                            "She looks at a recipe on her phone. "
                            "The recipe is for vegetable soup.\n\n"
                            "First, she reads the ingredients. "
                            "She needs carrots, onions, and tomatoes. "
                            "She also needs salt and pepper.\n\n"
                            "Lan chops the carrots into small pieces. "
                            "She chops the onions too. "
                            "Then she boils water in a big pot.\n\n"
                            "She puts the vegetables in the pot. "
                            "She stirs the soup slowly. "
                            "The kitchen smells very good. "
                            "Lan is happy. She loves to cook."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nấu ăn (Phần 1)",
                    "description": "Viết câu sử dụng 6 từ vựng về nấu ăn.",
                    "data": {
                        "vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop"],
                        "items": [
                            {
                                "targetVocab": "cook",
                                "prompt": "Hãy dùng từ 'cook' để viết một câu về việc nấu ăn ở nhà. Ví dụ: My mother cooks breakfast for us every morning."
                            },
                            {
                                "targetVocab": "recipe",
                                "prompt": "Hãy dùng từ 'recipe' để viết một câu về công thức nấu ăn. Ví dụ: I found a new recipe for fried rice online."
                            },
                            {
                                "targetVocab": "ingredient",
                                "prompt": "Hãy dùng từ 'ingredient' để viết một câu về nguyên liệu nấu ăn. Ví dụ: The main ingredient in this dish is chicken."
                            },
                            {
                                "targetVocab": "stir",
                                "prompt": "Hãy dùng từ 'stir' để viết một câu về việc khuấy thức ăn. Ví dụ: Please stir the sauce so it does not burn."
                            },
                            {
                                "targetVocab": "boil",
                                "prompt": "Hãy dùng từ 'boil' để viết một câu về việc đun sôi nước. Ví dụ: You need to boil the eggs for ten minutes."
                            },
                            {
                                "targetVocab": "chop",
                                "prompt": "Hãy dùng từ 'chop' để viết một câu về việc cắt thái thực phẩm. Ví dụ: He chops the garlic before adding it to the pan."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 2 — Phần 2 (Words: pan, oven, taste, spice, meal, serve)
        # ════════════════════════════════════════════
        {
            "title": "Phần 2",
            "activities": [
                # ── introAudio: Recap + New Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng mới",
                    "description": "Ôn lại từ vựng Phần 1 và giới thiệu 6 từ mới về nấu ăn.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong Phần 1, bạn đã học 6 từ rất hữu ích: "
                            "cook (nấu ăn), recipe (công thức), ingredient (nguyên liệu), "
                            "stir (khuấy), boil (đun sôi), và chop (cắt/thái). "
                            "Bạn còn nhớ không? Tuyệt vời!\n\n"
                            "Hôm nay chúng ta sẽ học thêm 6 từ mới. Những từ này giúp bạn nói về dụng cụ bếp, "
                            "gia vị, và cách phục vụ bữa ăn. "
                            "Sáu từ mới là: pan, oven, taste, spice, meal, và serve.\n\n"

                            "Từ đầu tiên là 'pan'. Pan là danh từ, nghĩa là 'chảo'. "
                            "Ví dụ: 'Heat the pan before you add the oil.' — Làm nóng chảo trước khi cho dầu vào. "
                            "Trong bài đọc, bạn sẽ thấy từ 'pan' khi nhân vật chiên trứng buổi sáng.\n\n"

                            "Từ thứ hai là 'oven'. Oven là danh từ, nghĩa là 'lò nướng'. "
                            "Ví dụ: 'Put the cake in the oven for thirty minutes.' — Cho bánh vào lò nướng ba mươi phút. "
                            "Trong bài đọc, từ 'oven' xuất hiện khi nhân vật nướng gà cho bữa tối.\n\n"

                            "Từ thứ ba là 'taste'. Taste có thể là động từ hoặc danh từ. "
                            "Là động từ, nó nghĩa là 'nếm'. Là danh từ, nó nghĩa là 'vị' hoặc 'hương vị'. "
                            "Ví dụ: 'Taste the soup before you add more salt.' — Nếm thử súp trước khi thêm muối. "
                            "Trong bài đọc, bạn sẽ thấy từ 'taste' khi nhân vật nếm thử món ăn.\n\n"

                            "Từ thứ tư là 'spice'. Spice là danh từ, nghĩa là 'gia vị'. "
                            "Ví dụ: 'Vietnamese food uses many spices.' — Món ăn Việt Nam dùng nhiều gia vị. "
                            "Trong bài đọc, từ 'spice' xuất hiện khi nhân vật thêm gia vị vào món ăn.\n\n"

                            "Từ thứ năm là 'meal'. Meal là danh từ, nghĩa là 'bữa ăn'. "
                            "Ví dụ: 'We eat three meals a day.' — Chúng tôi ăn ba bữa một ngày. "
                            "Trong bài đọc, bạn sẽ thấy từ 'meal' khi nhân vật chuẩn bị bữa ăn cho gia đình.\n\n"

                            "Từ cuối cùng là 'serve'. Serve là động từ, nghĩa là 'phục vụ' hoặc 'dọn ra'. "
                            "Ví dụ: 'She serves rice with every meal.' — Cô ấy dọn cơm trong mỗi bữa ăn. "
                            "Trong bài đọc, từ 'serve' xuất hiện khi nhân vật dọn bữa tối lên bàn.\n\n"

                            "Hãy bắt đầu với flashcards để ghi nhớ 6 từ mới này nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nấu ăn (Phần 2)",
                    "description": "Học 6 từ: pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nấu ăn (Phần 2)",
                    "description": "Học 6 từ: pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nấu ăn (Phần 2)",
                    "description": "Học 6 từ: pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nấu ăn (Phần 2)",
                    "description": "Học 6 từ: pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Minh nấu bữa tối đặc biệt",
                    "description": "Minh prepares a special dinner using the oven and spices.",
                    "data": {
                        "text": (
                            "Minh wants to make a special meal for his family. "
                            "Today is his mother's birthday. "
                            "He wants to cook her favorite food.\n\n"
                            "He heats a pan on the stove. "
                            "He puts oil in the pan. "
                            "Then he cooks some vegetables.\n\n"
                            "He also puts chicken in the oven. "
                            "He adds spice to the chicken. "
                            "It smells wonderful.\n\n"
                            "After thirty minutes, the food is ready. "
                            "Minh tastes the chicken. It is delicious! "
                            "He serves the meal on nice plates. "
                            "His mother smiles. She loves the meal."
                        ),
                        "vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Minh nấu bữa tối đặc biệt",
                    "description": "Minh prepares a special dinner using the oven and spices.",
                    "data": {
                        "text": (
                            "Minh wants to make a special meal for his family. "
                            "Today is his mother's birthday. "
                            "He wants to cook her favorite food.\n\n"
                            "He heats a pan on the stove. "
                            "He puts oil in the pan. "
                            "Then he cooks some vegetables.\n\n"
                            "He also puts chicken in the oven. "
                            "He adds spice to the chicken. "
                            "It smells wonderful.\n\n"
                            "After thirty minutes, the food is ready. "
                            "Minh tastes the chicken. It is delicious! "
                            "He serves the meal on nice plates. "
                            "His mother smiles. She loves the meal."
                        ),
                        "vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Minh nấu bữa tối đặc biệt",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Minh wants to make a special meal for his family. "
                            "Today is his mother's birthday. "
                            "He wants to cook her favorite food.\n\n"
                            "He heats a pan on the stove. "
                            "He puts oil in the pan. "
                            "Then he cooks some vegetables.\n\n"
                            "He also puts chicken in the oven. "
                            "He adds spice to the chicken. "
                            "It smells wonderful.\n\n"
                            "After thirty minutes, the food is ready. "
                            "Minh tastes the chicken. It is delicious! "
                            "He serves the meal on nice plates. "
                            "His mother smiles. She loves the meal."
                        )
                    }
                },
                # ── writingSentence ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nấu ăn (Phần 2)",
                    "description": "Viết câu sử dụng 6 từ vựng mới về nấu ăn.",
                    "data": {
                        "vocabList": ["pan", "oven", "taste", "spice", "meal", "serve"],
                        "items": [
                            {
                                "targetVocab": "pan",
                                "prompt": "Hãy dùng từ 'pan' để viết một câu về việc dùng chảo khi nấu ăn. Ví dụ: I fry eggs in a small pan every morning."
                            },
                            {
                                "targetVocab": "oven",
                                "prompt": "Hãy dùng từ 'oven' để viết một câu về việc dùng lò nướng. Ví dụ: My sister bakes bread in the oven on Sundays."
                            },
                            {
                                "targetVocab": "taste",
                                "prompt": "Hãy dùng từ 'taste' để viết một câu về việc nếm thử thức ăn. Ví dụ: Always taste the food before you serve it."
                            },
                            {
                                "targetVocab": "spice",
                                "prompt": "Hãy dùng từ 'spice' để viết một câu về gia vị trong nấu ăn. Ví dụ: This spice makes the soup taste much better."
                            },
                            {
                                "targetVocab": "meal",
                                "prompt": "Hãy dùng từ 'meal' để viết một câu về bữa ăn. Ví dụ: Dinner is the biggest meal of the day in my family."
                            },
                            {
                                "targetVocab": "serve",
                                "prompt": "Hãy dùng từ 'serve' để viết một câu về việc dọn thức ăn ra bàn. Ví dụ: My father serves the food when everyone sits down."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 3 — Ôn tập (Review: all 12 words)
        # ════════════════════════════════════════════
        {
            "title": "Ôn tập",
            "activities": [
                # ── introAudio: Review ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 12 từ vựng! Hãy ôn tập lại tất cả.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về nấu ăn tại nhà. Thật tuyệt vời!\n\n"
                            "Trong Phần 1, bạn đã học: cook (nấu ăn), recipe (công thức), "
                            "ingredient (nguyên liệu), stir (khuấy), boil (đun sôi), và chop (cắt/thái). "
                            "Bạn đã đọc về Lan nấu súp rau cho gia đình.\n\n"
                            "Trong Phần 2, bạn đã học: pan (chảo), oven (lò nướng), "
                            "taste (nếm/vị), spice (gia vị), meal (bữa ăn), và serve (dọn ra/phục vụ). "
                            "Bạn đã đọc về Minh nấu bữa tối đặc biệt cho sinh nhật mẹ.\n\n"
                            "Bây giờ là lúc ôn tập! Bạn sẽ xem lại tất cả 12 từ qua flashcards, "
                            "luyện tập qua các bài tập từ vựng, và viết câu với mỗi từ. "
                            "Sau phần ôn tập này, bạn sẽ sẵn sàng đọc toàn bộ bài đọc trong Phần 4. "
                            "Hãy cố gắng nhé!"
                        )
                    }
                },
                # ── viewFlashcards (all 12) ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập nấu ăn",
                    "description": "Ôn tập 12 từ: cook, recipe, ingredient, stir, boil, chop, pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── speakFlashcards (all 12) ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập nấu ăn",
                    "description": "Ôn tập 12 từ: cook, recipe, ingredient, stir, boil, chop, pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── vocabLevel1 (all 12) ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập nấu ăn",
                    "description": "Ôn tập 12 từ: cook, recipe, ingredient, stir, boil, chop, pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── vocabLevel2 (all 12) ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập nấu ăn",
                    "description": "Ôn tập 12 từ: cook, recipe, ingredient, stir, boil, chop, pan, oven, taste, spice, meal, serve",
                    "data": {"vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"]}
                },
                # ── writingSentence (all 12) ──
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập nấu ăn",
                    "description": "Viết câu sử dụng tất cả 12 từ vựng về nấu ăn.",
                    "data": {
                        "vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"],
                        "items": [
                            {
                                "targetVocab": "cook",
                                "prompt": "Hãy dùng từ 'cook' để viết một câu về người nấu ăn trong gia đình bạn. Ví dụ: My grandmother cooks the best phở in our family."
                            },
                            {
                                "targetVocab": "recipe",
                                "prompt": "Hãy dùng từ 'recipe' để viết một câu về một công thức bạn thích. Ví dụ: This recipe only needs five simple ingredients."
                            },
                            {
                                "targetVocab": "ingredient",
                                "prompt": "Hãy dùng từ 'ingredient' để viết một câu về nguyên liệu cho một món ăn. Ví dụ: Fresh ingredients make the food taste better."
                            },
                            {
                                "targetVocab": "stir",
                                "prompt": "Hãy dùng từ 'stir' để viết một câu về việc khuấy khi nấu ăn. Ví dụ: You should stir the rice so it does not stick to the pot."
                            },
                            {
                                "targetVocab": "boil",
                                "prompt": "Hãy dùng từ 'boil' để viết một câu về việc đun sôi. Ví dụ: I boil water every morning to make tea."
                            },
                            {
                                "targetVocab": "chop",
                                "prompt": "Hãy dùng từ 'chop' để viết một câu về việc cắt thái thực phẩm. Ví dụ: My brother helps me chop vegetables for dinner."
                            },
                            {
                                "targetVocab": "pan",
                                "prompt": "Hãy dùng từ 'pan' để viết một câu về việc dùng chảo. Ví dụ: The fish looks golden brown in the hot pan."
                            },
                            {
                                "targetVocab": "oven",
                                "prompt": "Hãy dùng từ 'oven' để viết một câu về lò nướng. Ví dụ: We use the oven to bake cookies for the holiday."
                            },
                            {
                                "targetVocab": "taste",
                                "prompt": "Hãy dùng từ 'taste' để viết một câu về hương vị thức ăn. Ví dụ: The soup has a sweet and sour taste."
                            },
                            {
                                "targetVocab": "spice",
                                "prompt": "Hãy dùng từ 'spice' để viết một câu về gia vị. Ví dụ: My mother keeps many spices in the kitchen."
                            },
                            {
                                "targetVocab": "meal",
                                "prompt": "Hãy dùng từ 'meal' để viết một câu về bữa ăn yêu thích của bạn. Ví dụ: Sunday lunch is my favorite meal of the week."
                            },
                            {
                                "targetVocab": "serve",
                                "prompt": "Hãy dùng từ 'serve' để viết một câu về việc dọn bữa ăn. Ví dụ: We serve dinner at seven o'clock every evening."
                            }
                        ]
                    }
                }
            ]
        },
        # ════════════════════════════════════════════
        # SESSION 4 — Đọc toàn bài (Final Reading)
        # ════════════════════════════════════════════
        {
            "title": "Đọc toàn bài",
            "activities": [
                # ── introAudio: Final reading intro ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc cuối",
                    "description": "Giới thiệu bài đọc tổng hợp với tất cả 12 từ vựng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của bài học 'Nấu Ăn Tại Nhà'!\n\n"
                            "Bạn đã học 12 từ vựng quan trọng: cook, recipe, ingredient, stir, boil, chop, "
                            "pan, oven, taste, spice, meal, và serve. "
                            "Trong Phần 1, bạn đọc về Lan nấu súp rau cho gia đình. "
                            "Trong Phần 2, bạn đọc về Minh nấu bữa tối đặc biệt cho sinh nhật mẹ.\n\n"
                            "Bây giờ, bạn sẽ đọc một bài đọc dài hơn. Bài đọc này kết hợp tất cả 12 từ vựng "
                            "trong một câu chuyện về việc nấu ăn tại nhà. Hãy chú ý cách mỗi từ được sử dụng trong ngữ cảnh thực tế.\n\n"
                            "Hãy đọc chậm, tận hưởng câu chuyện, và nhận ra những từ bạn đã học. Bạn sẽ ngạc nhiên "
                            "vì mình hiểu được nhiều hơn bạn nghĩ đấy!"
                        )
                    }
                },
                # ── reading: Full article ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Bữa ăn gia đình ngày chủ nhật",
                    "description": "A full story about a family cooking day using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "It is Sunday morning. Lan and Minh want to cook a big meal for their family. "
                            "They look at a recipe together. The recipe is for chicken soup and fried fish.\n\n"
                            "First, they go to the kitchen. Lan reads the ingredients for the soup. "
                            "She needs chicken, carrots, onions, and noodles. "
                            "Minh reads the ingredients for the fish. He needs fish, garlic, and lemon.\n\n"
                            "Lan starts with the soup. She chops the carrots and onions into small pieces. "
                            "She boils water in a big pot. Then she puts the chicken and vegetables in the pot. "
                            "She stirs the soup slowly. She adds a little spice to make it taste better.\n\n"
                            "Minh starts with the fish. He heats oil in a pan. "
                            "The pan gets very hot. He puts the fish in the pan. "
                            "It makes a loud sound. He cooks the fish for five minutes on each side.\n\n"
                            "Lan also wants to make bread. She puts the bread in the oven. "
                            "The oven is warm. After fifteen minutes, the bread is golden and soft.\n\n"
                            "The food is almost ready. Lan tastes the soup. "
                            "'It needs more spice,' she says. She adds pepper and stirs again. "
                            "Now the taste is perfect.\n\n"
                            "Minh takes the fish out of the pan. It looks beautiful. "
                            "Lan takes the bread out of the oven. It smells wonderful.\n\n"
                            "They serve the meal on the big table. "
                            "There is soup, fish, bread, and rice. "
                            "The whole family sits down together.\n\n"
                            "Their mother says, 'This meal is delicious!' "
                            "Their father says, 'You are both great cooks!' "
                            "Lan and Minh smile. They love to cook for their family. "
                            "Cooking at home is not just about food. It is about love."
                        ),
                        "vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"]
                    }
                },
                # ── speakReading ──
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Bữa ăn gia đình ngày chủ nhật",
                    "description": "A full story about a family cooking day using all 12 vocabulary words.",
                    "data": {
                        "text": (
                            "It is Sunday morning. Lan and Minh want to cook a big meal for their family. "
                            "They look at a recipe together. The recipe is for chicken soup and fried fish.\n\n"
                            "First, they go to the kitchen. Lan reads the ingredients for the soup. "
                            "She needs chicken, carrots, onions, and noodles. "
                            "Minh reads the ingredients for the fish. He needs fish, garlic, and lemon.\n\n"
                            "Lan starts with the soup. She chops the carrots and onions into small pieces. "
                            "She boils water in a big pot. Then she puts the chicken and vegetables in the pot. "
                            "She stirs the soup slowly. She adds a little spice to make it taste better.\n\n"
                            "Minh starts with the fish. He heats oil in a pan. "
                            "The pan gets very hot. He puts the fish in the pan. "
                            "It makes a loud sound. He cooks the fish for five minutes on each side.\n\n"
                            "Lan also wants to make bread. She puts the bread in the oven. "
                            "The oven is warm. After fifteen minutes, the bread is golden and soft.\n\n"
                            "The food is almost ready. Lan tastes the soup. "
                            "'It needs more spice,' she says. She adds pepper and stirs again. "
                            "Now the taste is perfect.\n\n"
                            "Minh takes the fish out of the pan. It looks beautiful. "
                            "Lan takes the bread out of the oven. It smells wonderful.\n\n"
                            "They serve the meal on the big table. "
                            "There is soup, fish, bread, and rice. "
                            "The whole family sits down together.\n\n"
                            "Their mother says, 'This meal is delicious!' "
                            "Their father says, 'You are both great cooks!' "
                            "Lan and Minh smile. They love to cook for their family. "
                            "Cooking at home is not just about food. It is about love."
                        ),
                        "vocabList": ["cook", "recipe", "ingredient", "stir", "boil", "chop", "pan", "oven", "taste", "spice", "meal", "serve"]
                    }
                },
                # ── readAlong ──
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Bữa ăn gia đình ngày chủ nhật",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "It is Sunday morning. Lan and Minh want to cook a big meal for their family. "
                            "They look at a recipe together. The recipe is for chicken soup and fried fish.\n\n"
                            "First, they go to the kitchen. Lan reads the ingredients for the soup. "
                            "She needs chicken, carrots, onions, and noodles. "
                            "Minh reads the ingredients for the fish. He needs fish, garlic, and lemon.\n\n"
                            "Lan starts with the soup. She chops the carrots and onions into small pieces. "
                            "She boils water in a big pot. Then she puts the chicken and vegetables in the pot. "
                            "She stirs the soup slowly. She adds a little spice to make it taste better.\n\n"
                            "Minh starts with the fish. He heats oil in a pan. "
                            "The pan gets very hot. He puts the fish in the pan. "
                            "It makes a loud sound. He cooks the fish for five minutes on each side.\n\n"
                            "Lan also wants to make bread. She puts the bread in the oven. "
                            "The oven is warm. After fifteen minutes, the bread is golden and soft.\n\n"
                            "The food is almost ready. Lan tastes the soup. "
                            "'It needs more spice,' she says. She adds pepper and stirs again. "
                            "Now the taste is perfect.\n\n"
                            "Minh takes the fish out of the pan. It looks beautiful. "
                            "Lan takes the bread out of the oven. It smells wonderful.\n\n"
                            "They serve the meal on the big table. "
                            "There is soup, fish, bread, and rice. "
                            "The whole family sits down together.\n\n"
                            "Their mother says, 'This meal is delicious!' "
                            "Their father says, 'You are both great cooks!' "
                            "Lan and Minh smile. They love to cook for their family. "
                            "Cooking at home is not just about food. It is about love."
                        )
                    }
                },
                # ── introAudio: Farewell (quiet_awe tone) ──
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay đầy cảm xúc.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học 'Nấu Ăn Tại Nhà'. "
                            "Hãy dừng lại một chút và cảm nhận điều này: bạn vừa học được 12 từ tiếng Anh "
                            "về một trong những điều đẹp đẽ nhất trong cuộc sống — nấu ăn cho người mình yêu thương.\n\n"

                            "Từ 'cook' nghĩa là nấu ăn. Mỗi khi bạn vào bếp, hãy nghĩ: "
                            "'I cook because I care.' — Tôi nấu ăn vì tôi quan tâm. "
                            "Nấu ăn không chỉ là kỹ năng — đó là tình yêu được thể hiện qua từng món ăn.\n\n"

                            "Từ 'recipe' nghĩa là công thức. Mỗi gia đình đều có những công thức riêng. "
                            "'My family's recipe has been passed down for generations.' — "
                            "Công thức của gia đình tôi đã được truyền qua nhiều thế hệ.\n\n"

                            "Từ 'ingredient' nghĩa là nguyên liệu. Nguyên liệu tươi tạo nên món ăn ngon. "
                            "'The secret is always fresh ingredients.' — Bí quyết luôn là nguyên liệu tươi.\n\n"

                            "Từ 'taste' nghĩa là nếm hoặc hương vị. Hương vị kết nối chúng ta với ký ức. "
                            "'The taste of my mother's soup brings back childhood memories.' — "
                            "Hương vị súp của mẹ tôi gợi lại ký ức tuổi thơ.\n\n"

                            "Từ 'meal' nghĩa là bữa ăn. Bữa ăn là lúc gia đình quây quần bên nhau. "
                            "'A home-cooked meal brings the whole family together.' — "
                            "Bữa ăn nhà nấu đưa cả gia đình lại gần nhau.\n\n"

                            "Từ 'serve' nghĩa là dọn ra hoặc phục vụ. Khi bạn dọn bữa ăn, bạn đang trao đi tình yêu. "
                            "'She serves the food with a warm smile.' — Cô ấy dọn thức ăn với nụ cười ấm áp.\n\n"

                            "Bạn biết không, nấu ăn và học ngôn ngữ có điểm chung rất đẹp: "
                            "cả hai đều cần kiên nhẫn, cả hai đều cần luyện tập, "
                            "và cả hai đều mang lại niềm vui khi bạn chia sẻ thành quả với người khác.\n\n"

                            "Hôm nay bạn đã có thêm 12 \"nguyên liệu\" mới trong vốn từ vựng tiếng Anh. "
                            "Hãy mang chúng vào bếp, vào cuộc sống, vào những cuộc trò chuyện của bạn. "
                            "Mỗi từ bạn dùng là một hương vị mới trong câu chuyện của riêng bạn.\n\n"

                            "Cảm ơn bạn đã học cùng mình. Hẹn gặp lại ở bài học tiếp theo."
                        )
                    }
                }
            ]
        }
    ]
}

# ── Validation ──
validate_content_type_tags(content)
validate_balanced_skills_beginner(content)
validate_bilingual_prompts(content, "beginner")

print("✅ Validation passed!")

# ── Create curriculum ──
token = get_firebase_id_token(UID)
res = requests.post(f"{API_BASE}/curriculum/create", json={
    "firebaseIdToken": token,
    "language": "en",
    "userLanguage": "vi",
    "content": json.dumps(content)
})
res.raise_for_status()
data = res.json()
print(f"Created curriculum: {data['id']}")
print(f"Title: {content['title']}")
