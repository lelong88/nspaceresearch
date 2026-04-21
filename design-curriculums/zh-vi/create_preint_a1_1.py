#!/usr/bin/env python3
"""
create_preint_a1_1.py - Preintermediate zh-vi: Vietnamese Regional Cuisine
Series: A1 美食与餐饮 (xcdgeb9g), Display Order: 3, Price: 49
Tone: desc=surprising_fact, farewell=team_building_energy
"""
import sys, json, logging
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/zh-vi")
from api_helpers import create_curriculum, add_to_series, set_display_order, set_price
from validate_content import validate
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
SERIES_ID = "xcdgeb9g"
DISPLAY_ORDER = 3
PRICE = 49

# Existing beginner vocab in A1: pho, nuoc mam, goi cuon, cha gio, com, bun,
# ca phe, tra, sinh to, che, banh mi, kem, thuc don, goi mon, tinh tien,
# ngon, dua, muong, dia, ly, nong, lanh, cay, ngot
# New preintermediate vocab (18 words, 3 groups of 6):

content = {
    "title": "越南地方美食",
    "contentTypeTags": [],
    "difficultyTags": ["preintermediate"],
    "description": (
        "越南有63个省份，但90%的学习者只知道河粉和春卷——"
        "这意味着你错过了越南美食版图的绝大部分。\n\n"
        "从顺化的皇家宫廷菜到湄公河三角洲的乡村炖锅，"
        "每个地区都有自己独特的烹饪哲学。一道菜的名字可能在北方和南方完全不同，"
        "同一种食材在不同省份有截然不同的做法。\n\n"
        "这门课程就像一张美食地图，带你穿越越南三大区域的厨房。"
        "你将学会18个关键词汇，从食材到烹饪方法，从地方特色到饮食文化。\n\n"
        "掌握这些词汇后，你不仅能在越南任何一个城市自信点餐，"
        "还能和当地人讨论他们引以为豪的家乡味道。"
    ),
    "preview": {
        "text": (
            "越南有63个省份，每个省都有自己的招牌菜——但大多数学习者只知道河粉和春卷。"
            "这门课程带你深入越南三大区域的美食世界：北方的清淡精致、中部的辛辣浓郁、"
            "南方的甜美丰富。你将学习18个核心词汇：从hải sản（海鲜）到gia vị（香料），"
            "从nấu（烹饪）到hấp（蒸），从đặc sản（特产）到món chay（素食）。"
            "通过真实的越南语阅读材料，你将了解顺化宫廷菜的精致、"
            "岘港海鲜的新鲜、西贡街头的活力。完成课程后，"
            "你将能够用越南语讨论地方美食差异，在任何越南城市自信地探索当地餐厅。"
        )
    },
    "learningSessions": [
        {
            "title": "第1部分",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "介绍：越南北方美食",
                    "description": "学习6个关于越南北方烹饪传统的词汇。",
                    "data": {
                        "text": (
                            "欢迎来到越南地方美食课程！在之前的课程中，你已经学会了基础的美食词汇。"
                            "现在我们要深入探索越南三大区域各自独特的烹饪传统。\n\n"
                            "今天我们从北方开始，学习6个关键词汇。\n\n"
                            "第一个词是 hải sản。Hải sản 是海鲜的意思，包括鱼、虾、蟹、贝类等。"
                            "越南有超过3000公里的海岸线，海鲜是饮食中不可或缺的一部分。"
                            "在餐厅你可以说：Nhà hàng này có hải sản tươi không？"
                            "意思是'这家餐厅有新鲜海鲜吗？'\n\n"
                            "第二个词是 gia vị。Gia vị 是香料、调味料的统称。"
                            "越南北方菜的特点是用较少的 gia vị，追求食材本身的味道。"
                            "你可以说：Món này dùng gia vị gì？意思是'这道菜用了什么调料？'\n\n"
                            "第三个词是 nấu。Nấu 是烹饪、煮的意思，是越南语中最常用的烹饪动词。"
                            "比如 nấu cơm 是煮饭，nấu canh 是煮汤。"
                            "你可以说：Mẹ tôi nấu ăn rất ngon，意思是'我妈妈做饭很好吃'。\n\n"
                            "第四个词是 chiên。Chiên 是油炸的意思。"
                            "虽然越南菜以清淡著称，但炸食也很受欢迎。"
                            "Cá chiên 是炸鱼，đậu chiên 是炸豆腐。"
                            "你可以说：Tôi thích cá chiên giòn，意思是'我喜欢炸得酥脆的鱼'。\n\n"
                            "第五个词是 luộc。Luộc 是水煮的意思，是越南北方最常见的烹饪方式。"
                            "北方人喜欢 rau luộc（水煮蔬菜）和 gà luộc（白切鸡）。"
                            "你可以说：Gà luộc chấm muối tiêu chanh rất ngon，"
                            "意思是'白切鸡蘸盐胡椒柠檬很好吃'。\n\n"
                            "第六个词是 đặc sản。Đặc sản 是特产、地方名菜的意思。"
                            "每个越南省份都有自己的 đặc sản。"
                            "你可以说：Đặc sản Hà Nội là phở và bún chả，"
                            "意思是'河内的特产是河粉和烤肉米粉'。\n\n"
                            "好的，让我们练习这6个词：hải sản, gia vị, nấu, chiên, luộc, đặc sản。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：北方美食词汇",
                    "description": "学习6个词：hải sản, gia vị, nấu, chiên, luộc, đặc sản",
                    "data": {"vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：北方美食词汇",
                    "description": "练习发音6个词：hải sản, gia vị, nấu, chiên, luộc, đặc sản",
                    "data": {"vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：北方美食",
                    "description": "初级练习6个词：hải sản, gia vị, nấu, chiên, luộc, đặc sản",
                    "data": {"vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：北方美食",
                    "description": "进阶练习6个词：hải sản, gia vị, nấu, chiên, luộc, đặc sản",
                    "data": {"vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "词汇练习3：北方美食",
                    "description": "高级练习6个词：hải sản, gia vị, nấu, chiên, luộc, đặc sản",
                    "data": {"vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"]}
                },
                {
                    "activityType": "reading",
                    "title": "阅读：河内的厨房",
                    "description": "Hà Nội nổi tiếng với ẩm thực tinh tế và thanh đạm.",
                    "data": {
                        "text": (
                            "Hà Nội nổi tiếng với ẩm thực tinh tế và thanh đạm. "
                            "Người Hà Nội thích nấu những món đơn giản nhưng đòi hỏi kỹ thuật cao. "
                            "Hải sản tươi từ Hải Phòng được chuyển về Hà Nội mỗi ngày. "
                            "Khác với miền Nam, người miền Bắc dùng ít gia vị hơn trong nấu ăn. "
                            "Gà luộc là món ăn truyền thống trong ngày Tết và các dịp quan trọng. "
                            "Cá chiên giòn ăn kèm với rau sống là bữa cơm gia đình phổ biến. "
                            "Mỗi quận ở Hà Nội đều có đặc sản riêng mà du khách nên thử."
                        ),
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：河内的厨房",
                    "description": "朗读关于河内烹饪传统的短文。",
                    "data": {
                        "text": (
                            "Hà Nội nổi tiếng với ẩm thực tinh tế và thanh đạm. "
                            "Người Hà Nội thích nấu những món đơn giản nhưng đòi hỏi kỹ thuật cao. "
                            "Hải sản tươi từ Hải Phòng được chuyển về Hà Nội mỗi ngày. "
                            "Khác với miền Nam, người miền Bắc dùng ít gia vị hơn trong nấu ăn. "
                            "Gà luộc là món ăn truyền thống trong ngày Tết và các dịp quan trọng. "
                            "Cá chiên giòn ăn kèm với rau sống là bữa cơm gia đình phổ biến. "
                            "Mỗi quận ở Hà Nội đều có đặc sản riêng mà du khách nên thử."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：河内的厨房",
                    "description": "听并跟读关于河内烹饪传统的短文。",
                    "data": {
                        "text": (
                            "Hà Nội nổi tiếng với ẩm thực tinh tế và thanh đạm. "
                            "Người Hà Nội thích nấu những món đơn giản nhưng đòi hỏi kỹ thuật cao. "
                            "Hải sản tươi từ Hải Phòng được chuyển về Hà Nội mỗi ngày. "
                            "Khác với miền Nam, người miền Bắc dùng ít gia vị hơn trong nấu ăn. "
                            "Gà luộc là món ăn truyền thống trong ngày Tết và các dịp quan trọng. "
                            "Cá chiên giòn ăn kèm với rau sống là bữa cơm gia đình phổ biến. "
                            "Mỗi quận ở Hà Nội đều có đặc sản riêng mà du khách nên thử."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：用北方美食词汇造句",
                    "description": "用本课学到的6个北方美食词汇写句子。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản"],
                        "items": [
                            {"prompt": "用 hải sản 写一个关于越南海岸城市饮食的句子。例句：Đà Nẵng là thành phố nổi tiếng với hải sản tươi ngon và giá rẻ.", "targetVocab": "hải sản"},
                            {"prompt": "用 gia vị 写一个比较南北越南烹饪风格的句子。例句：Người miền Bắc dùng ít gia vị hơn so với người miền Nam.", "targetVocab": "gia vị"},
                            {"prompt": "用 nấu 写一个关于家庭烹饪的句子。例句：Bà tôi nấu phở ngon nhất trong gia đình.", "targetVocab": "nấu"},
                            {"prompt": "用 chiên 写一个关于你喜欢的炸食的句子。例句：Nem rán là món chiên truyền thống của Việt Nam.", "targetVocab": "chiên"},
                            {"prompt": "用 luộc 写一个关于健康饮食的句子。例句：Rau luộc là cách ăn uống lành mạnh nhất.", "targetVocab": "luộc"},
                            {"prompt": "用 đặc sản 写一个关于你想尝试的越南地方菜的句子。例句：Tôi muốn thử đặc sản của mỗi tỉnh khi đi du lịch Việt Nam.", "targetVocab": "đặc sản"}
                        ]
                    }
                }
            ]
        },
        {
            "title": "第2部分",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "介绍：越南中部美食",
                    "description": "回顾第一课词汇，学习6个关于越南中部烹饪的新词汇。",
                    "data": {
                        "text": (
                            "欢迎回来！在上一课中，我们学习了6个越南北方美食词汇："
                            "hải sản（海鲜）、gia vị（香料）、nấu（烹饪）、"
                            "chiên（油炸）、luộc（水煮）和 đặc sản（特产）。\n\n"
                            "今天我们来到越南中部，学习6个新词汇。中部美食以辛辣和精致著称，"
                            "尤其是顺化——越南最后一个王朝的首都。\n\n"
                            "第一个词是 hấp。Hấp 是蒸的意思，是越南中部非常流行的烹饪方式。"
                            "顺化的 bánh bèo hấp（蒸米糕）是最有名的蒸菜之一。"
                            "你可以说：Cá hấp bia là món ăn đặc biệt của miền Trung，"
                            "意思是'啤酒蒸鱼是中部的特色菜'。\n\n"
                            "第二个词是 nướng。Nướng 是烤的意思，包括炭烤和烘烤。"
                            "越南的 thịt nướng（烤肉）是街头最受欢迎的食物之一。"
                            "你可以说：Mực nướng ở biển Đà Nẵng rất tuyệt，"
                            "意思是'岘港海边的烤鱿鱼非常棒'。\n\n"
                            "第三个词是 xào。Xào 是炒的意思，快速翻炒是越南家常菜的基本技法。"
                            "Rau xào（炒蔬菜）和 mì xào（炒面）是最常见的炒菜。"
                            "你可以说：Bạn có thể xào rau với tỏi không？"
                            "意思是'你能用大蒜炒蔬菜吗？'\n\n"
                            "第四个词是 món chay。Món chay 是素食的意思。"
                            "越南有深厚的佛教传统，素食文化非常发达。"
                            "每月初一和十五，很多越南人会吃 món chay。"
                            "你可以说：Nhà hàng này có món chay không？"
                            "意思是'这家餐厅有素食吗？'\n\n"
                            "第五个词是 nguyên liệu。Nguyên liệu 是原料、食材的意思。"
                            "越南菜强调新鲜的 nguyên liệu，很多菜市场每天凌晨就开始营业。"
                            "你可以说：Nguyên liệu tươi là bí quyết của ẩm thực Việt Nam，"
                            "意思是'新鲜食材是越南美食的秘诀'。\n\n"
                            "第六个词是 công thức。Công thức 是食谱、配方的意思。"
                            "很多越南家庭的 công thức 是代代相传的秘密。"
                            "你可以说：Bạn có thể chia sẻ công thức nấu phở không？"
                            "意思是'你能分享河粉的食谱吗？'\n\n"
                            "好的，让我们练习这6个新词：hấp, nướng, xào, món chay, nguyên liệu, công thức。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：中部美食词汇",
                    "description": "学习6个词：hấp, nướng, xào, món chay, nguyên liệu, công thức",
                    "data": {"vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：中部美食词汇",
                    "description": "练习发音6个词：hấp, nướng, xào, món chay, nguyên liệu, công thức",
                    "data": {"vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：中部美食",
                    "description": "初级练习6个词：hấp, nướng, xào, món chay, nguyên liệu, công thức",
                    "data": {"vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：中部美食",
                    "description": "进阶练习6个词：hấp, nướng, xào, món chay, nguyên liệu, công thức",
                    "data": {"vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "词汇练习3：中部美食",
                    "description": "高级练习6个词：hấp, nướng, xào, món chay, nguyên liệu, công thức",
                    "data": {"vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"]}
                },
                {
                    "activityType": "reading",
                    "title": "阅读：顺化宫廷菜",
                    "description": "Huế là cố đô của Việt Nam và là nơi sinh ra ẩm thực cung đình.",
                    "data": {
                        "text": (
                            "Huế là cố đô của Việt Nam và là nơi sinh ra ẩm thực cung đình. "
                            "Người Huế rất giỏi hấp các loại bánh từ bột gạo. "
                            "Thịt nướng trên than hoa là cách chế biến phổ biến ở miền Trung. "
                            "Rau xào với tỏi và dầu hào là món ăn kèm trong mỗi bữa cơm. "
                            "Huế cũng nổi tiếng với nhiều món chay ngon vì có nhiều chùa chiền. "
                            "Nguyên liệu tươi từ chợ Đông Ba được các đầu bếp chọn lựa kỹ càng. "
                            "Công thức nấu ăn của hoàng gia Huế được giữ bí mật qua nhiều thế hệ."
                        ),
                        "vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：顺化宫廷菜",
                    "description": "朗读关于顺化宫廷菜的短文。",
                    "data": {
                        "text": (
                            "Huế là cố đô của Việt Nam và là nơi sinh ra ẩm thực cung đình. "
                            "Người Huế rất giỏi hấp các loại bánh từ bột gạo. "
                            "Thịt nướng trên than hoa là cách chế biến phổ biến ở miền Trung. "
                            "Rau xào với tỏi và dầu hào là món ăn kèm trong mỗi bữa cơm. "
                            "Huế cũng nổi tiếng với nhiều món chay ngon vì có nhiều chùa chiền. "
                            "Nguyên liệu tươi từ chợ Đông Ba được các đầu bếp chọn lựa kỹ càng. "
                            "Công thức nấu ăn của hoàng gia Huế được giữ bí mật qua nhiều thế hệ."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：顺化宫廷菜",
                    "description": "听并跟读关于顺化宫廷菜的短文。",
                    "data": {
                        "text": (
                            "Huế là cố đô của Việt Nam và là nơi sinh ra ẩm thực cung đình. "
                            "Người Huế rất giỏi hấp các loại bánh từ bột gạo. "
                            "Thịt nướng trên than hoa là cách chế biến phổ biến ở miền Trung. "
                            "Rau xào với tỏi và dầu hào là món ăn kèm trong mỗi bữa cơm. "
                            "Huế cũng nổi tiếng với nhiều món chay ngon vì có nhiều chùa chiền. "
                            "Nguyên liệu tươi từ chợ Đông Ba được các đầu bếp chọn lựa kỹ càng. "
                            "Công thức nấu ăn của hoàng gia Huế được giữ bí mật qua nhiều thế hệ."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：用中部美食词汇造句",
                    "description": "用本课学到的6个中部美食词汇写句子。",
                    "data": {
                        "vocabList": ["hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức"],
                        "items": [
                            {"prompt": "用 hấp 写一个关于健康烹饪方式的句子。例句：Hấp là cách nấu ăn giữ được nhiều chất dinh dưỡng nhất.", "targetVocab": "hấp"},
                            {"prompt": "用 nướng 写一个关于越南街头美食的句子。例句：Mùi thịt nướng trên vỉa hè Sài Gòn khiến ai cũng phải dừng lại.", "targetVocab": "nướng"},
                            {"prompt": "用 xào 写一个关于家常菜的句子。例句：Mỗi tối, mẹ tôi xào rau muống với tỏi cho cả nhà.", "targetVocab": "xào"},
                            {"prompt": "用 món chay 写一个关于越南佛教文化的句子。例句：Vào ngày rằm, nhiều người Việt Nam ăn món chay để tích phước.", "targetVocab": "món chay"},
                            {"prompt": "用 nguyên liệu 写一个关于越南菜市场的句子。例句：Chợ Bến Thành bán đủ loại nguyên liệu tươi ngon.", "targetVocab": "nguyên liệu"},
                            {"prompt": "用 công thức 写一个关于学做越南菜的句子。例句：Tôi đang học công thức nấu bún bò Huế từ một đầu bếp người Huế.", "targetVocab": "công thức"}
                        ]
                    }
                }
            ]
        },
        {
            "title": "第3部分",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "介绍：越南南方美食",
                    "description": "回顾前两课词汇，学习6个关于越南南方烹饪的新词汇。",
                    "data": {
                        "text": (
                            "欢迎来到第三课！让我们快速回顾一下。"
                            "第一课我们学了北方美食词汇：hải sản（海鲜）、gia vị（香料）、"
                            "nấu（烹饪）、chiên（油炸）、luộc（水煮）、đặc sản（特产）。"
                            "第二课我们学了中部美食词汇：hấp（蒸）、nướng（烤）、"
                            "xào（炒）、món chay（素食）、nguyên liệu（食材）、công thức（食谱）。\n\n"
                            "今天我们来到越南南方，学习最后6个词汇。南方菜以甜味和丰富的椰奶为特色。\n\n"
                            "第一个词是 kho。Kho 是炖、焖的意思，是越南南方最具代表性的烹饪方式。"
                            "Cá kho tộ（砂锅焖鱼）是南方家庭的经典菜肴。"
                            "你可以说：Thịt kho trứng là món ăn Tết của người miền Nam，"
                            "意思是'焖肉卤蛋是南方人的年菜'。\n\n"
                            "第二个词是 canh。Canh 是汤的意思，越南人每顿饭都要有一碗 canh。"
                            "Canh chua（酸汤）是南方最有名的汤品。"
                            "你可以说：Canh chua cá lóc là món canh ngon nhất miền Nam，"
                            "意思是'酸汤鲈鱼是南方最好喝的汤'。\n\n"
                            "第三个词是 trái cây。Trái cây 是水果的意思。"
                            "湄公河三角洲是越南的水果天堂，有几十种热带水果。"
                            "你可以说：Miền Tây có rất nhiều trái cây nhiệt đới，"
                            "意思是'西部有很多热带水果'。\n\n"
                            "第四个词是 nước dừa。Nước dừa 是椰子水的意思。"
                            "在南方，nước dừa 不仅是饮料，也是烹饪中常用的食材。"
                            "你可以说：Nước dừa tươi rất mát và bổ dưỡng，"
                            "意思是'新鲜椰子水很清凉又有营养'。\n\n"
                            "第五个词是 quán ăn。Quán ăn 是小餐馆、食堂的意思。"
                            "越南的 quán ăn 通常是家庭经营的小店，价格便宜，味道地道。"
                            "你可以说：Quán ăn này mở cửa từ sáng đến tối，"
                            "意思是'这家小餐馆从早开到晚'。\n\n"
                            "第六个词是 ẩm thực。Ẩm thực 是美食、饮食文化的意思，"
                            "比简单的'吃'更有文化内涵。"
                            "你可以说：Ẩm thực Việt Nam được UNESCO công nhận，"
                            "意思是'越南美食被联合国教科文组织认可'。\n\n"
                            "好的，让我们练习最后6个词：kho, canh, trái cây, nước dừa, quán ăn, ẩm thực。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：南方美食词汇",
                    "description": "学习6个词：kho, canh, trái cây, nước dừa, quán ăn, ẩm thực",
                    "data": {"vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：南方美食词汇",
                    "description": "练习发音6个词：kho, canh, trái cây, nước dừa, quán ăn, ẩm thực",
                    "data": {"vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：南方美食",
                    "description": "初级练习6个词：kho, canh, trái cây, nước dừa, quán ăn, ẩm thực",
                    "data": {"vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：南方美食",
                    "description": "进阶练习6个词：kho, canh, trái cây, nước dừa, quán ăn, ẩm thực",
                    "data": {"vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "词汇练习3：南方美食",
                    "description": "高级练习6个词：kho, canh, trái cây, nước dừa, quán ăn, ẩm thực",
                    "data": {"vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]}
                },
                {
                    "activityType": "reading",
                    "title": "阅读：湄公河三角洲的味道",
                    "description": "Miền Tây Nam Bộ là vùng đất của sông nước và trái cây.",
                    "data": {
                        "text": (
                            "Miền Tây Nam Bộ là vùng đất của sông nước và trái cây. "
                            "Người dân ở đây thích kho cá với nước màu và tiêu. "
                            "Mỗi bữa cơm đều có một tô canh nóng hổi trên bàn. "
                            "Trái cây nhiệt đới như xoài, chôm chôm và sầu riêng bán đầy chợ. "
                            "Nước dừa tươi là thức uống giải khát phổ biến nhất vào mùa hè. "
                            "Dọc theo sông Mekong, quán ăn nhỏ phục vụ những món ăn dân dã ngon tuyệt. "
                            "Ẩm thực miền Tây mang đậm hương vị ngọt ngào của đường thốt nốt và nước cốt dừa."
                        ),
                        "vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：湄公河三角洲的味道",
                    "description": "朗读关于湄公河三角洲美食的短文。",
                    "data": {
                        "text": (
                            "Miền Tây Nam Bộ là vùng đất của sông nước và trái cây. "
                            "Người dân ở đây thích kho cá với nước màu và tiêu. "
                            "Mỗi bữa cơm đều có một tô canh nóng hổi trên bàn. "
                            "Trái cây nhiệt đới như xoài, chôm chôm và sầu riêng bán đầy chợ. "
                            "Nước dừa tươi là thức uống giải khát phổ biến nhất vào mùa hè. "
                            "Dọc theo sông Mekong, quán ăn nhỏ phục vụ những món ăn dân dã ngon tuyệt. "
                            "Ẩm thực miền Tây mang đậm hương vị ngọt ngào của đường thốt nốt và nước cốt dừa."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：湄公河三角洲的味道",
                    "description": "听并跟读关于湄公河三角洲美食的短文。",
                    "data": {
                        "text": (
                            "Miền Tây Nam Bộ là vùng đất của sông nước và trái cây. "
                            "Người dân ở đây thích kho cá với nước màu và tiêu. "
                            "Mỗi bữa cơm đều có một tô canh nóng hổi trên bàn. "
                            "Trái cây nhiệt đới như xoài, chôm chôm và sầu riêng bán đầy chợ. "
                            "Nước dừa tươi là thức uống giải khát phổ biến nhất vào mùa hè. "
                            "Dọc theo sông Mekong, quán ăn nhỏ phục vụ những món ăn dân dã ngon tuyệt. "
                            "Ẩm thực miền Tây mang đậm hương vị ngọt ngào của đường thốt nốt và nước cốt dừa."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：用南方美食词汇造句",
                    "description": "用本课学到的6个南方美食词汇写句子。",
                    "data": {
                        "vocabList": ["kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"],
                        "items": [
                            {"prompt": "用 kho 写一个关于越南传统菜肴的句子。例句：Cá kho tộ là món ăn mà mọi gia đình miền Nam đều biết nấu.", "targetVocab": "kho"},
                            {"prompt": "用 canh 写一个关于越南家庭饮食习惯的句子。例句：Người Việt Nam không thể thiếu canh trong bữa cơm hàng ngày.", "targetVocab": "canh"},
                            {"prompt": "用 trái cây 写一个关于越南热带水果的句子。例句：Trái cây ở chợ nổi Cái Răng tươi ngon và rẻ hơn thành phố.", "targetVocab": "trái cây"},
                            {"prompt": "用 nước dừa 写一个关于越南饮品的句子。例句：Uống nước dừa tươi dưới bóng dừa là trải nghiệm tuyệt vời ở miền Tây.", "targetVocab": "nước dừa"},
                            {"prompt": "用 quán ăn 写一个关于越南街头饮食文化的句子。例句：Quán ăn vỉa hè ở Sài Gòn mở cửa từ sáng sớm đến khuya.", "targetVocab": "quán ăn"},
                            {"prompt": "用 ẩm thực 写一个关于越南美食在世界上的地位的句子。例句：Ẩm thực Việt Nam ngày càng được thế giới biết đến và yêu thích.", "targetVocab": "ẩm thực"}
                        ]
                    }
                }
            ]
        },
        {
            "title": "复习",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "复习介绍",
                    "description": "回顾全部18个越南地方美食词汇，准备综合练习。",
                    "data": {
                        "text": (
                            "恭喜你完成了前三课的学习！你已经掌握了18个越南地方美食词汇。\n\n"
                            "让我们回顾一下。第一课我们学了北方美食词汇：hải sản（海鲜）、"
                            "gia vị（香料）、nấu（烹饪）、chiên（油炸）、luộc（水煮）、đặc sản（特产）。\n\n"
                            "第二课我们学了中部美食词汇：hấp（蒸）、nướng（烤）、"
                            "xào（炒）、món chay（素食）、nguyên liệu（食材）、công thức（食谱）。\n\n"
                            "第三课我们学了南方美食词汇：kho（炖）、canh（汤）、"
                            "trái cây（水果）、nước dừa（椰子水）、quán ăn（小餐馆）、ẩm thực（美食文化）。\n\n"
                            "现在我们要把这18个词放在一起综合练习。准备好了吗？"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡复习：全部18个词",
                    "description": "复习全部18个地方美食词汇。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音复习：全部18个词",
                    "description": "练习发音全部18个地方美食词汇。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "综合词汇练习1",
                    "description": "综合练习全部18个地方美食词汇。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "综合词汇练习2",
                    "description": "进阶综合练习全部18个地方美食词汇。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "综合词汇练习3",
                    "description": "高级综合练习全部18个地方美食词汇。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：越南美食之旅",
                    "description": "Việt Nam là đất nước có nền ẩm thực phong phú bậc nhất Đông Nam Á.",
                    "data": {
                        "text": (
                            "Việt Nam là đất nước có nền ẩm thực phong phú bậc nhất Đông Nam Á. "
                            "Ở miền Bắc, người ta nấu ăn thanh đạm với ít gia vị. "
                            "Hải sản tươi được luộc hoặc chiên giòn để giữ vị nguyên bản. "
                            "Mỗi tỉnh đều tự hào về đặc sản riêng của mình. "
                            "Miền Trung nổi tiếng với bánh hấp và thịt nướng trên than hoa. "
                            "Rau xào là món ăn kèm không thể thiếu trong bữa cơm gia đình. "
                            "Nhiều người chọn món chay vào ngày rằm theo truyền thống Phật giáo. "
                            "Đầu bếp giỏi luôn chọn nguyên liệu tươi nhất từ chợ sáng. "
                            "Công thức nấu ăn truyền thống được truyền từ mẹ sang con gái. "
                            "Ở miền Nam, cá kho tộ và canh chua là hai món kinh điển. "
                            "Trái cây nhiệt đới bán đầy các chợ nổi trên sông Mekong. "
                            "Nước dừa tươi là thức uống giải khát tự nhiên nhất. "
                            "Quán ăn vỉa hè là nơi bạn tìm thấy những món ngon nhất với giá rẻ nhất. "
                            "Ẩm thực Việt Nam là sự kết hợp hài hòa giữa truyền thống và sáng tạo."
                        ),
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：越南美食之旅",
                    "description": "朗读关于越南三大区域美食的综合短文。",
                    "data": {
                        "text": (
                            "Việt Nam là đất nước có nền ẩm thực phong phú bậc nhất Đông Nam Á. "
                            "Ở miền Bắc, người ta nấu ăn thanh đạm với ít gia vị. "
                            "Hải sản tươi được luộc hoặc chiên giòn để giữ vị nguyên bản. "
                            "Mỗi tỉnh đều tự hào về đặc sản riêng của mình. "
                            "Miền Trung nổi tiếng với bánh hấp và thịt nướng trên than hoa. "
                            "Rau xào là món ăn kèm không thể thiếu trong bữa cơm gia đình. "
                            "Nhiều người chọn món chay vào ngày rằm theo truyền thống Phật giáo. "
                            "Đầu bếp giỏi luôn chọn nguyên liệu tươi nhất từ chợ sáng. "
                            "Công thức nấu ăn truyền thống được truyền từ mẹ sang con gái. "
                            "Ở miền Nam, cá kho tộ và canh chua là hai món kinh điển. "
                            "Trái cây nhiệt đới bán đầy các chợ nổi trên sông Mekong. "
                            "Nước dừa tươi là thức uống giải khát tự nhiên nhất. "
                            "Quán ăn vỉa hè là nơi bạn tìm thấy những món ngon nhất với giá rẻ nhất. "
                            "Ẩm thực Việt Nam là sự kết hợp hài hòa giữa truyền thống và sáng tạo."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：越南美食之旅",
                    "description": "听并跟读关于越南三大区域美食的综合短文。",
                    "data": {
                        "text": (
                            "Việt Nam là đất nước có nền ẩm thực phong phú bậc nhất Đông Nam Á. "
                            "Ở miền Bắc, người ta nấu ăn thanh đạm với ít gia vị. "
                            "Hải sản tươi được luộc hoặc chiên giòn để giữ vị nguyên bản. "
                            "Mỗi tỉnh đều tự hào về đặc sản riêng của mình. "
                            "Miền Trung nổi tiếng với bánh hấp và thịt nướng trên than hoa. "
                            "Rau xào là món ăn kèm không thể thiếu trong bữa cơm gia đình. "
                            "Nhiều người chọn món chay vào ngày rằm theo truyền thống Phật giáo. "
                            "Đầu bếp giỏi luôn chọn nguyên liệu tươi nhất từ chợ sáng. "
                            "Công thức nấu ăn truyền thống được truyền từ mẹ sang con gái. "
                            "Ở miền Nam, cá kho tộ và canh chua là hai món kinh điển. "
                            "Trái cây nhiệt đới bán đầy các chợ nổi trên sông Mekong. "
                            "Nước dừa tươi là thức uống giải khát tự nhiên nhất. "
                            "Quán ăn vỉa hè là nơi bạn tìm thấy những món ngon nhất với giá rẻ nhất. "
                            "Ẩm thực Việt Nam là sự kết hợp hài hòa giữa truyền thống và sáng tạo."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：综合地方美食造句",
                    "description": "用全部18个地方美食词汇进行综合写作练习。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"],
                        "items": [
                            {"prompt": "用 nấu 和 gia vị 写一个比较越南南北烹饪差异的句子。例句：Người miền Bắc nấu ăn với ít gia vị hơn người miền Nam.", "targetVocab": "nấu"},
                            {"prompt": "用 hấp 和 nướng 写一个关于越南中部烹饪方式的句子。例句：Ở Huế, người ta thích hấp bánh và nướng thịt trên than hoa.", "targetVocab": "hấp"},
                            {"prompt": "用 kho 和 canh 写一个关于越南家庭饮食的句子。例句：Bữa cơm gia đình miền Nam luôn có cá kho và một tô canh nóng.", "targetVocab": "kho"},
                            {"prompt": "用 ẩm thực 和 đặc sản 写一个关于越南美食多样性的句子。例句：Ẩm thực Việt Nam đa dạng vì mỗi vùng miền đều có đặc sản riêng.", "targetVocab": "ẩm thực"}
                        ]
                    }
                }
            ]
        },
        {
            "title": "综合阅读",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "最终阅读介绍",
                    "description": "介绍最终综合阅读环节。",
                    "data": {
                        "text": (
                            "欢迎来到最后一课！在这门课程中，你已经学会了18个越南地方美食词汇，"
                            "涵盖了北方、中部和南方三大区域的烹饪传统。\n\n"
                            "现在你将阅读一篇完整的文章，里面包含了所有18个词汇。"
                            "然后你将完成一个段落写作练习，展示你对越南地方美食的理解。享受阅读吧！"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：越南美食完整指南",
                    "description": "Từ Bắc vào Nam, ẩm thực Việt Nam là một hành trình đầy hương vị.",
                    "data": {
                        "text": (
                            "Từ Bắc vào Nam, ẩm thực Việt Nam là một hành trình đầy hương vị. "
                            "Mỗi vùng miền có cách nấu ăn riêng, phản ánh khí hậu và văn hóa địa phương. "
                            "Miền Bắc nổi tiếng với hải sản tươi từ vịnh Hạ Long và cách dùng gia vị tinh tế. "
                            "Người Hà Nội thích luộc gà và chiên cá theo phong cách truyền thống. "
                            "Đặc sản của mỗi tỉnh miền Bắc đều mang nét riêng không lẫn vào đâu. "
                            "Miền Trung, đặc biệt là Huế, nổi tiếng với bánh hấp tinh xảo. "
                            "Thịt nướng trên than hoa và rau xào tỏi là những món ăn hàng ngày. "
                            "Huế cũng là thiên đường của món chay với hàng trăm công thức khác nhau. "
                            "Đầu bếp miền Trung rất kỹ tính trong việc chọn nguyên liệu. "
                            "Miền Nam mang hương vị ngọt ngào với cá kho tộ và canh chua. "
                            "Trái cây nhiệt đới từ miền Tây được bán khắp cả nước. "
                            "Nước dừa tươi là thức uống không thể thiếu trong ngày hè nóng bức. "
                            "Quán ăn vỉa hè ở Sài Gòn phục vụ từ sáng sớm đến tận khuya. "
                            "Ẩm thực Việt Nam không chỉ là ăn uống — đó là cách người Việt kể câu chuyện "
                            "về quê hương, gia đình và truyền thống của mình qua từng món ăn."
                        ),
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"]
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：越南美食完整指南",
                    "description": "听并跟读越南美食完整指南。",
                    "data": {
                        "text": (
                            "Từ Bắc vào Nam, ẩm thực Việt Nam là một hành trình đầy hương vị. "
                            "Mỗi vùng miền có cách nấu ăn riêng, phản ánh khí hậu và văn hóa địa phương. "
                            "Miền Bắc nổi tiếng với hải sản tươi từ vịnh Hạ Long và cách dùng gia vị tinh tế. "
                            "Người Hà Nội thích luộc gà và chiên cá theo phong cách truyền thống. "
                            "Đặc sản của mỗi tỉnh miền Bắc đều mang nét riêng không lẫn vào đâu. "
                            "Miền Trung, đặc biệt là Huế, nổi tiếng với bánh hấp tinh xảo. "
                            "Thịt nướng trên than hoa và rau xào tỏi là những món ăn hàng ngày. "
                            "Huế cũng là thiên đường của món chay với hàng trăm công thức khác nhau. "
                            "Đầu bếp miền Trung rất kỹ tính trong việc chọn nguyên liệu. "
                            "Miền Nam mang hương vị ngọt ngào với cá kho tộ và canh chua. "
                            "Trái cây nhiệt đới từ miền Tây được bán khắp cả nước. "
                            "Nước dừa tươi là thức uống không thể thiếu trong ngày hè nóng bức. "
                            "Quán ăn vỉa hè ở Sài Gòn phục vụ từ sáng sớm đến tận khuya. "
                            "Ẩm thực Việt Nam không chỉ là ăn uống — đó là cách người Việt kể câu chuyện "
                            "về quê hương, gia đình và truyền thống của mình qua từng món ăn."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "段落写作：越南地方美食比较",
                    "description": "用所学词汇写一段关于越南三大区域美食差异的文章。",
                    "data": {
                        "vocabList": ["hải sản", "gia vị", "nấu", "chiên", "luộc", "đặc sản",
                                      "hấp", "nướng", "xào", "món chay", "nguyên liệu", "công thức",
                                      "kho", "canh", "trái cây", "nước dừa", "quán ăn", "ẩm thực"],
                        "instructions": (
                            "请用越南语写一段150-200字的文章，比较越南北方、中部和南方的美食特色。"
                            "尽量使用本课学到的词汇，描述每个地区独特的烹饪方式和代表性菜肴。"
                        ),
                        "prompts": [
                            "比较越南三大区域的主要烹饪方式（如北方的luộc和chiên、中部的hấp和nướng、南方的kho），并解释为什么每个地区偏好不同的烹饪方法。",
                            "描述你最想去越南哪个地区品尝当地ẩm thực，解释你想尝试哪些đặc sản，以及你会在什么样的quán ăn用餐。"
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "告别与总结",
                    "description": "回顾所有词汇，温暖告别。",
                    "data": {
                        "text": (
                            "恭喜你完成了越南地方美食课程！让我们一起回顾你学到的18个词汇。\n\n"
                            "Hải sản——海鲜，越南3000公里海岸线的馈赠。"
                            "下次去海边城市，试着说：Cho tôi một đĩa hải sản nướng。\n\n"
                            "Gia vị——香料，越南菜的灵魂。北方用得少，南方用得多，"
                            "但每一种 gia vị 都有它存在的理由。\n\n"
                            "Nấu——烹饪，最基本也最重要的动词。"
                            "当你说 Tôi muốn học nấu ăn Việt Nam，你就打开了一扇新的大门。\n\n"
                            "Chiên——油炸，让食物变得酥脆诱人。"
                            "Nem rán chiên giòn 是每个越南家庭节日餐桌上的必备菜。\n\n"
                            "Luộc——水煮，北方人最爱的烹饪方式。"
                            "简单的 gà luộc 配上 muối tiêu chanh，就是一道完美的菜。\n\n"
                            "Đặc sản——特产，每个省份的骄傲。"
                            "旅行时问一句 Đặc sản ở đây là gì，你就能发现最地道的美食。\n\n"
                            "Hấp——蒸，顺化人的拿手好戏。"
                            "Bánh bèo hấp 是你在顺化必须尝试的第一道菜。\n\n"
                            "Nướng——烤，炭火赋予食物独特的烟熏香气。"
                            "走在越南街头，thịt nướng 的香味会让你停下脚步。\n\n"
                            "Xào——炒，快速翻炒锁住食材的新鲜。"
                            "一盘简单的 rau xào tỏi 就能让一碗白饭变得美味无比。\n\n"
                            "Món chay——素食，越南佛教文化的美食表达。"
                            "越南的 món chay 精致到让你忘记它没有肉。\n\n"
                            "Nguyên liệu——食材，好菜的起点。"
                            "越南厨师说：Nguyên liệu tươi thì không cần nhiều gia vị。\n\n"
                            "Công thức——食谱，家族传承的宝藏。"
                            "每个越南家庭都有自己秘密的 công thức，代代相传。\n\n"
                            "Kho——炖，南方家庭的温暖记忆。"
                            "一锅 cá kho tộ 慢慢炖煮，整个厨房都充满了家的味道。\n\n"
                            "Canh——汤，越南餐桌上永远的主角。"
                            "没有 canh 的一餐，越南人会觉得不完整。\n\n"
                            "Trái cây——水果，湄公河三角洲的甜蜜礼物。"
                            "在越南，trái cây 不只是饭后甜点，它是生活的一部分。\n\n"
                            "Nước dừa——椰子水，大自然最清爽的饮料。"
                            "炎热的午后，一杯 nước dừa tươi 就是最好的享受。\n\n"
                            "Quán ăn——小餐馆，越南美食的真正舞台。"
                            "最好吃的越南菜往往不在豪华餐厅，而在街边的 quán ăn。\n\n"
                            "Ẩm thực——美食文化，越南人引以为豪的软实力。"
                            "当你能用越南语谈论 ẩm thực，你就真正走进了越南文化的核心。\n\n"
                            "你现在拥有了探索越南美食版图的语言工具。"
                            "从北方的清淡到中部的辛辣，从南方的甜美到全国的多样——"
                            "越南的每一口食物都在讲述一个故事。"
                            "而你，已经学会了听懂这些故事的语言。"
                            "带着这18个词汇，去越南的每一个角落，品尝每一种味道吧！"
                            "我们下次课程再见！"
                        )
                    }
                }
            ]
        }
    ]
}

print(f"Validating: {content['title']}")
validate(content, level="standard")
print("  Validation passed")

print(f"Creating curriculum: {content['title']}")
cid = create_curriculum(content, language="vi", user_language="zh")
print(f"  Created: {cid}")

add_to_series(SERIES_ID, cid)
print(f"  Added to series A1 ({SERIES_ID})")

set_display_order(cid, DISPLAY_ORDER)
print(f"  Display order: {DISPLAY_ORDER}")

set_price(cid, PRICE)
print(f"  Price: {PRICE}")

print(f"Done: {content['title']} -> {cid}")
