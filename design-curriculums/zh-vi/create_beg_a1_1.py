#!/usr/bin/env python3
"""
create_beg_a1_1.py - Beginner zh-vi: Vietnamese Street Food Basics
Series: A1 (xcdgeb9g), Display Order: 1, Price: 19
Tone: desc=vivid_scenario, farewell=introspective_guide
"""
import sys
import json
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/zh-vi")
from api_helpers import create_curriculum, add_to_series, set_display_order, set_price
from validate_content import validate

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

SERIES_ID = "xcdgeb9g"
DISPLAY_ORDER = 1
PRICE = 19

content = {
    "title": "越南街头小吃",
    "contentTypeTags": [],
    "difficultyTags": ["beginner"],
    "description": (
        "想象你走在胡志明市的街头，空气中弥漫着炭火烤肉的香气，"
        "路边摊的蒸汽模糊了霓虹灯光——你却连一碗河粉都不会点。\n\n"
        "越南街头小吃不只是食物，它是一整套社交密码。"
        "从清晨的面包摊到深夜的烧烤档，每一个摊位都是一堂文化课。\n\n"
        "这门课程带你从零开始，用12个核心词汇打开越南美食世界的大门。"
        "你将学会点餐、描述口味、理解菜单——不再只是指着图片说'这个'。\n\n"
        "掌握这些词汇，你的越南之旅将从'游客模式'切换到'本地模式'。"
    ),
    "preview": {
        "text": (
            "想象你走在胡志明市的街头，空气中弥漫着炭火烤肉的香气，"
            "路边摊的蒸汽模糊了霓虹灯光。越南的街头小吃文化是世界上最丰富的之一，"
            "但如果你不会用越南语点餐，你就只能永远站在外面看。"
            "这门课程教你12个最实用的美食词汇：从phở（河粉）到nước mắm（鱼露），"
            "从gỏi cuốn（春卷）到chả giò（炸春卷），从cơm（米饭）到bún（米粉）。"
            "你将通过真实的越南语阅读材料学习这些词汇，练习发音，"
            "并用它们写出自己的句子。完成这门课程后，"
            "你将能够自信地走进任何一家越南餐厅，用越南语点一顿地道的饭。"
        )
    },
    "learningSessions": [
        {
            "title": "第1部分",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "介绍：越南街头小吃",
                    "description": "欢迎来到越南街头小吃的世界，学习6个核心美食词汇。",
                    "data": {
                        "text": (
                            "欢迎来到越南街头小吃课程！今天我们要学习6个在越南吃饭时最常用的词汇。\n\n"
                            "第一个词是 phở。Phở 是越南最著名的菜肴——一碗热气腾腾的牛肉或鸡肉河粉汤。"
                            "在越南，人们早餐就开始吃 phở。比如你可以说：Tôi muốn một tô phở bò，"
                            "意思是'我想要一碗牛肉河粉'。\n\n"
                            "第二个词是 nước mắm。Nước mắm 是鱼露，越南菜的灵魂调料。"
                            "几乎每道越南菜都会用到它。在餐桌上你会听到：Cho thêm nước mắm，"
                            "意思是'再加点鱼露'。\n\n"
                            "第三个词是 gỏi cuốn。Gỏi cuốn 是越南鲜春卷，用米纸包裹虾肉、蔬菜和米粉。"
                            "这是越南最受欢迎的开胃菜之一。你可以说：Cho tôi hai cuốn gỏi cuốn，"
                            "意思是'给我两个春卷'。\n\n"
                            "第四个词是 chả giò。Chả giò 是炸春卷，外皮酥脆，内馅是猪肉和蔬菜。"
                            "在南方叫 chả giò，在北方叫 nem rán。点餐时说：Một đĩa chả giò，"
                            "意思是'一盘炸春卷'。\n\n"
                            "第五个词是 cơm。Cơm 就是米饭，越南人每天都吃。"
                            "Cơm tấm 是碎米饭，胡志明市的招牌菜。你会经常看到：Cơm tấm sườn，"
                            "意思是'排骨碎米饭'。\n\n"
                            "第六个词是 bún。Bún 是米粉，比河粉更细更圆。"
                            "Bún chả 是河内最有名的米粉菜肴。奥巴马访问河内时就吃了 bún chả。"
                            "你可以说：Tôi thích bún chả，意思是'我喜欢烤肉米粉'。\n\n"
                            "好的，让我们开始练习这6个词：phở, nước mắm, gỏi cuốn, chả giò, cơm, bún。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：街头小吃基础",
                    "description": "学习6个词：phở, nước mắm, gỏi cuốn, chả giò, cơm, bún",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：街头小吃基础",
                    "description": "练习发音6个词：phở, nước mắm, gỏi cuốn, chả giò, cơm, bún",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：街头小吃基础",
                    "description": "初级练习6个词：phở, nước mắm, gỏi cuốn, chả giò, cơm, bún",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：街头小吃基础",
                    "description": "进阶练习6个词：phở, nước mắm, gỏi cuốn, chả giò, cơm, bún",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：街头小吃之旅",
                    "description": "Buổi sáng ở Sài Gòn bắt đầu với một tô phở nóng hổi.",
                    "data": {
                        "text": (
                            "Buổi sáng ở Sài Gòn bắt đầu với một tô phở nóng hổi. "
                            "Người bán hàng cho thêm nước mắm vào bát. "
                            "Khách du lịch thường gọi gỏi cuốn làm món khai vị. "
                            "Chả giò giòn tan là món ăn yêu thích của trẻ em. "
                            "Bữa trưa đơn giản nhất là một đĩa cơm với thịt nướng. "
                            "Buổi tối, nhiều người chọn bún chả ở quán vỉa hè."
                        ),
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：街头小吃之旅",
                    "description": "朗读关于越南街头小吃的短文。",
                    "data": {
                        "text": (
                            "Buổi sáng ở Sài Gòn bắt đầu với một tô phở nóng hổi. "
                            "Người bán hàng cho thêm nước mắm vào bát. "
                            "Khách du lịch thường gọi gỏi cuốn làm món khai vị. "
                            "Chả giò giòn tan là món ăn yêu thích của trẻ em. "
                            "Bữa trưa đơn giản nhất là một đĩa cơm với thịt nướng. "
                            "Buổi tối, nhiều người chọn bún chả ở quán vỉa hè."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：街头小吃之旅",
                    "description": "听并跟读关于越南街头小吃的短文。",
                    "data": {
                        "text": (
                            "Buổi sáng ở Sài Gòn bắt đầu với một tô phở nóng hổi. "
                            "Người bán hàng cho thêm nước mắm vào bát. "
                            "Khách du lịch thường gọi gỏi cuốn làm món khai vị. "
                            "Chả giò giòn tan là món ăn yêu thích của trẻ em. "
                            "Bữa trưa đơn giản nhất là một đĩa cơm với thịt nướng. "
                            "Buổi tối, nhiều người chọn bún chả ở quán vỉa hè."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：用美食词汇造句",
                    "description": "用本课学到的6个美食词汇写句子。",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"],
                        "items": [
                            {"prompt": "用 phở 写一个关于早餐的句子。例句：Mỗi sáng, tôi ăn một tô phở gà ở quán gần nhà.", "targetVocab": "phở"},
                            {"prompt": "用 nước mắm 写一个关于调味料的句子。例句：Nước mắm là gia vị quan trọng nhất trong bếp Việt Nam.", "targetVocab": "nước mắm"},
                            {"prompt": "用 gỏi cuốn 写一个关于点餐的句子。例句：Tôi gọi hai cuốn gỏi cuốn tôm cho bữa trưa.", "targetVocab": "gỏi cuốn"},
                            {"prompt": "用 chả giò 写一个关于你喜欢的食物的句子。例句：Chả giò của mẹ tôi là món ngon nhất.", "targetVocab": "chả giò"},
                            {"prompt": "用 cơm 写一个关于日常饮食的句子。例句：Người Việt Nam ăn cơm ba bữa mỗi ngày.", "targetVocab": "cơm"},
                            {"prompt": "用 bún 写一个关于你最喜欢的越南菜的句子。例句：Bún chả Hà Nội là món ăn tôi muốn thử nhất.", "targetVocab": "bún"}
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
                    "title": "介绍：饮品与甜点",
                    "description": "回顾第一课词汇，学习6个新的饮品和甜点词汇。",
                    "data": {
                        "text": (
                            "欢迎回来！在上一课中，我们学习了6个越南街头小吃的核心词汇："
                            "phở（河粉）、nước mắm（鱼露）、gỏi cuốn（鲜春卷）、"
                            "chả giò（炸春卷）、cơm（米饭）和 bún（米粉）。\n\n"
                            "今天我们继续探索越南美食，学习6个关于饮品和甜点的词汇。\n\n"
                            "第一个词是 cà phê。Cà phê 是咖啡，越南是世界第二大咖啡出口国。"
                            "越南咖啡通常很浓，加炼乳。你可以说：Cho tôi một ly cà phê sữa đá，"
                            "意思是'给我一杯冰奶咖啡'。\n\n"
                            "第二个词是 trà。Trà 是茶，越南人喝茶的历史比咖啡长得多。"
                            "在越南餐厅，服务员通常会免费提供 trà đá（冰茶）。"
                            "你可以说：Cho tôi một ly trà đá，意思是'给我一杯冰茶'。\n\n"
                            "第三个词是 sinh tố。Sinh tố 是水果奶昔，越南的热带水果让奶昔特别好喝。"
                            "最受欢迎的是 sinh tố bơ（牛油果奶昔）。"
                            "你可以说：Tôi muốn một ly sinh tố xoài，意思是'我想要一杯芒果奶昔'。\n\n"
                            "第四个词是 chè。Chè 是越南甜汤，有几十种不同的口味。"
                            "从绿豆到芋头，从椰奶到莲子，每种 chè 都是一个惊喜。"
                            "你可以说：Chè này ngon quá，意思是'这个甜汤太好吃了'。\n\n"
                            "第五个词是 bánh mì。Bánh mì 是越南法棍三明治，融合了法国和越南的美食传统。"
                            "一个好的 bánh mì 外脆内软，馅料丰富。"
                            "你可以说：Một bánh mì thịt，意思是'一个肉三明治'。\n\n"
                            "第六个词是 kem。Kem 是冰淇淋，越南的 kem 口味独特，"
                            "有榴莲味、椰子味，甚至绿豆味。"
                            "你可以说：Cho tôi một cây kem dừa，意思是'给我一个椰子冰淇淋'。\n\n"
                            "好的，让我们练习这6个新词：cà phê, trà, sinh tố, chè, bánh mì, kem。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：饮品与甜点",
                    "description": "学习6个词：cà phê, trà, sinh tố, chè, bánh mì, kem",
                    "data": {
                        "vocabList": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：饮品与甜点",
                    "description": "练习发音6个词：cà phê, trà, sinh tố, chè, bánh mì, kem",
                    "data": {
                        "vocabList": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：饮品与甜点",
                    "description": "初级练习6个词：cà phê, trà, sinh tố, chè, bánh mì, kem",
                    "data": {
                        "vocabList": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：饮品与甜点",
                    "description": "进阶练习6个词：cà phê, trà, sinh tố, chè, bánh mì, kem",
                    "data": {
                        "vocabList": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：越南饮品文化",
                    "description": "Người Việt Nam rất thích uống cà phê.",
                    "data": {
                        "text": (
                            "Người Việt Nam rất thích uống cà phê. "
                            "Buổi sáng, họ ngồi ở quán vỉa hè và uống trà đá. "
                            "Trẻ em thường chọn sinh tố trái cây thay vì cà phê. "
                            "Sau bữa ăn, một bát chè là món tráng miệng hoàn hảo. "
                            "Bánh mì là bữa sáng nhanh và rẻ nhất ở Việt Nam. "
                            "Vào mùa hè, ai cũng muốn ăn kem mát lạnh."
                        ),
                        "vocabList": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：越南饮品文化",
                    "description": "朗读关于越南饮品文化的短文。",
                    "data": {
                        "text": (
                            "Người Việt Nam rất thích uống cà phê. "
                            "Buổi sáng, họ ngồi ở quán vỉa hè và uống trà đá. "
                            "Trẻ em thường chọn sinh tố trái cây thay vì cà phê. "
                            "Sau bữa ăn, một bát chè là món tráng miệng hoàn hảo. "
                            "Bánh mì là bữa sáng nhanh và rẻ nhất ở Việt Nam. "
                            "Vào mùa hè, ai cũng muốn ăn kem mát lạnh."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：越南饮品文化",
                    "description": "听并跟读关于越南饮品文化的短文。",
                    "data": {
                        "text": (
                            "Người Việt Nam rất thích uống cà phê. "
                            "Buổi sáng, họ ngồi ở quán vỉa hè và uống trà đá. "
                            "Trẻ em thường chọn sinh tố trái cây thay vì cà phê. "
                            "Sau bữa ăn, một bát chè là món tráng miệng hoàn hảo. "
                            "Bánh mì là bữa sáng nhanh và rẻ nhất ở Việt Nam. "
                            "Vào mùa hè, ai cũng muốn ăn kem mát lạnh."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：用饮品词汇造句",
                    "description": "用本课学到的6个饮品和甜点词汇写句子。",
                    "data": {
                        "vocabList": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"],
                        "items": [
                            {"prompt": "用 cà phê 写一个关于你早晨习惯的句子。例句：Tôi uống cà phê mỗi sáng trước khi đi làm.", "targetVocab": "cà phê"},
                            {"prompt": "用 trà 写一个关于越南餐厅的句子。例句：Nhà hàng Việt Nam luôn có trà đá miễn phí.", "targetVocab": "trà"},
                            {"prompt": "用 sinh tố 写一个关于热带水果的句子。例句：Sinh tố xoài ở Việt Nam rất ngon và rẻ.", "targetVocab": "sinh tố"},
                            {"prompt": "用 chè 写一个关于甜点的句子。例句：Chè đậu xanh là món tráng miệng truyền thống.", "targetVocab": "chè"},
                            {"prompt": "用 bánh mì 写一个关于快餐的句子。例句：Bánh mì Sài Gòn nổi tiếng khắp thế giới.", "targetVocab": "bánh mì"},
                            {"prompt": "用 kem 写一个关于夏天的句子。例句：Mùa hè ở Hà Nội, tôi ăn kem mỗi ngày.", "targetVocab": "kem"}
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
                    "description": "回顾全部12个越南美食词汇，准备综合练习。",
                    "data": {
                        "text": (
                            "恭喜你完成了前两课的学习！你已经掌握了12个越南美食词汇。\n\n"
                            "让我们快速回顾一下。第一课我们学了：phở（河粉）、nước mắm（鱼露）、"
                            "gỏi cuốn（鲜春卷）、chả giò（炸春卷）、cơm（米饭）和 bún（米粉）。\n\n"
                            "第二课我们学了：cà phê（咖啡）、trà（茶）、sinh tố（水果奶昔）、"
                            "chè（甜汤）、bánh mì（法棍三明治）和 kem（冰淇淋）。\n\n"
                            "现在我们要把这12个词放在一起练习。你将阅读一篇包含所有词汇的文章，"
                            "然后完成综合练习。准备好了吗？"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡复习：全部12个词",
                    "description": "复习全部12个美食词汇。",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音复习：全部12个词",
                    "description": "练习发音全部12个美食词汇。",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "综合词汇练习1",
                    "description": "综合练习全部12个美食词汇。",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "综合词汇练习2",
                    "description": "进阶综合练习全部12个美食词汇。",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：越南美食一日游",
                    "description": "Một ngày ở Sài Gòn bắt đầu với bánh mì và cà phê sữa đá.",
                    "data": {
                        "text": (
                            "Một ngày ở Sài Gòn bắt đầu với bánh mì và cà phê sữa đá. "
                            "Sau đó, bạn có thể uống trà đá ở quán vỉa hè. "
                            "Bữa trưa, hãy thử một tô phở bò với nhiều nước mắm. "
                            "Hoặc bạn có thể gọi cơm tấm sườn và gỏi cuốn. "
                            "Buổi chiều, sinh tố xoài là lựa chọn tuyệt vời. "
                            "Bữa tối, chả giò giòn tan và bún chả là sự kết hợp hoàn hảo. "
                            "Cuối ngày, thưởng thức một bát chè hoặc một cây kem mát lạnh."
                        ),
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：越南美食一日游",
                    "description": "朗读关于越南美食一日游的综合短文。",
                    "data": {
                        "text": (
                            "Một ngày ở Sài Gòn bắt đầu với bánh mì và cà phê sữa đá. "
                            "Sau đó, bạn có thể uống trà đá ở quán vỉa hè. "
                            "Bữa trưa, hãy thử một tô phở bò với nhiều nước mắm. "
                            "Hoặc bạn có thể gọi cơm tấm sườn và gỏi cuốn. "
                            "Buổi chiều, sinh tố xoài là lựa chọn tuyệt vời. "
                            "Bữa tối, chả giò giòn tan và bún chả là sự kết hợp hoàn hảo. "
                            "Cuối ngày, thưởng thức một bát chè hoặc một cây kem mát lạnh."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：越南美食一日游",
                    "description": "听并跟读关于越南美食一日游的综合短文。",
                    "data": {
                        "text": (
                            "Một ngày ở Sài Gòn bắt đầu với bánh mì và cà phê sữa đá. "
                            "Sau đó, bạn có thể uống trà đá ở quán vỉa hè. "
                            "Bữa trưa, hãy thử một tô phở bò với nhiều nước mắm. "
                            "Hoặc bạn có thể gọi cơm tấm sườn và gỏi cuốn. "
                            "Buổi chiều, sinh tố xoài là lựa chọn tuyệt vời. "
                            "Bữa tối, chả giò giòn tan và bún chả là sự kết hợp hoàn hảo. "
                            "Cuối ngày, thưởng thức một bát chè hoặc một cây kem mát lạnh."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：综合美食造句",
                    "description": "用全部12个美食词汇进行综合写作练习。",
                    "data": {
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"],
                        "items": [
                            {"prompt": "用 phở 和 nước mắm 写一个关于越南早餐的句子。例句：Tôi ăn phở và cho thêm nước mắm mỗi sáng.", "targetVocab": "phở"},
                            {"prompt": "用 cà phê 和 bánh mì 写一个关于快餐的句子。例句：Cà phê sữa đá và bánh mì là bữa sáng phổ biến nhất.", "targetVocab": "cà phê"},
                            {"prompt": "用 gỏi cuốn 和 chả giò 比较两种春卷。例句：Gỏi cuốn tươi mát, còn chả giò thì giòn rụm.", "targetVocab": "gỏi cuốn"},
                            {"prompt": "用 sinh tố 和 chè 写一个关于甜品的句子。例句：Sau bữa ăn, tôi chọn sinh tố hoặc chè làm tráng miệng.", "targetVocab": "sinh tố"}
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
                    "description": "介绍最终综合阅读环节，回顾学习旅程。",
                    "data": {
                        "text": (
                            "欢迎来到最后一课！在这门课程中，你已经学会了12个越南美食词汇。\n\n"
                            "从第一课的街头小吃——phở、nước mắm、gỏi cuốn、chả giò、cơm、bún，"
                            "到第二课的饮品甜点——cà phê、trà、sinh tố、chè、bánh mì、kem。\n\n"
                            "现在你将阅读一篇完整的文章，里面包含了所有12个词汇。"
                            "这是你展示学习成果的时刻。享受阅读吧！"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：越南美食完整指南",
                    "description": "Việt Nam là thiên đường ẩm thực.",
                    "data": {
                        "text": (
                            "Việt Nam là thiên đường ẩm thực. Mỗi thành phố có những món ăn đặc biệt. "
                            "Ở Hà Nội, phở là món ăn quốc hồn quốc túy. Người Hà Nội ăn phở với nước mắm ngon. "
                            "Gỏi cuốn tươi mát là món khai vị hoàn hảo cho mùa hè. "
                            "Chả giò giòn rụm thường xuất hiện trong các bữa tiệc gia đình. "
                            "Cơm là lương thực chính của người Việt Nam từ ngàn năm nay. "
                            "Bún chả là món ăn nổi tiếng nhất của Hà Nội. "
                            "Buổi sáng, người Sài Gòn thích uống cà phê sữa đá ở quán vỉa hè. "
                            "Trà đá miễn phí luôn có sẵn ở mọi nhà hàng. "
                            "Sinh tố trái cây nhiệt đới là thức uống yêu thích của du khách. "
                            "Chè có hàng trăm loại khác nhau ở mỗi vùng miền. "
                            "Bánh mì Sài Gòn đã trở thành món ăn đường phố nổi tiếng thế giới. "
                            "Và không gì tuyệt vời hơn một cây kem mát lạnh vào buổi chiều nóng bức."
                        ),
                        "vocabList": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún",
                                      "cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"]
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：越南美食完整指南",
                    "description": "听并跟读越南美食完整指南。",
                    "data": {
                        "text": (
                            "Việt Nam là thiên đường ẩm thực. Mỗi thành phố có những món ăn đặc biệt. "
                            "Ở Hà Nội, phở là món ăn quốc hồn quốc túy. Người Hà Nội ăn phở với nước mắm ngon. "
                            "Gỏi cuốn tươi mát là món khai vị hoàn hảo cho mùa hè. "
                            "Chả giò giòn rụm thường xuất hiện trong các bữa tiệc gia đình. "
                            "Cơm là lương thực chính của người Việt Nam từ ngàn năm nay. "
                            "Bún chả là món ăn nổi tiếng nhất của Hà Nội. "
                            "Buổi sáng, người Sài Gòn thích uống cà phê sữa đá ở quán vỉa hè. "
                            "Trà đá miễn phí luôn có sẵn ở mọi nhà hàng. "
                            "Sinh tố trái cây nhiệt đới là thức uống yêu thích của du khách. "
                            "Chè có hàng trăm loại khác nhau ở mỗi vùng miền. "
                            "Bánh mì Sài Gòn đã trở thành món ăn đường phố nổi tiếng thế giới. "
                            "Và không gì tuyệt vời hơn một cây kem mát lạnh vào buổi chiều nóng bức."
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "告别与总结",
                    "description": "回顾所有词汇，温暖告别。",
                    "data": {
                        "text": (
                            "恭喜你完成了越南街头小吃课程！让我们最后回顾一下你学到的12个词汇。\n\n"
                            "Phở——越南河粉，一碗热汤承载着整个国家的味觉记忆。"
                            "下次你走进越南餐厅，试着说：Cho tôi một tô phở bò。\n\n"
                            "Nước mắm——鱼露，越南厨房的灵魂。没有它，越南菜就失去了最核心的味道。"
                            "记住：Cho thêm nước mắm 是你在餐桌上最实用的一句话。\n\n"
                            "Gỏi cuốn——鲜春卷，清爽健康的开胃菜。"
                            "想象自己在河内的老街上，对摊主说：Hai cuốn gỏi cuốn。\n\n"
                            "Chả giò——炸春卷，酥脆的外皮包裹着丰富的馅料。"
                            "这是越南家庭聚会上必不可少的菜肴。\n\n"
                            "Cơm——米饭，越南人生活的基础。Cơm tấm sườn 是胡志明市最经典的午餐。\n\n"
                            "Bún——米粉，比河粉更细更圆。Bún chả 让奥巴马都赞不绝口。\n\n"
                            "Cà phê——越南咖啡，浓郁醇厚，加上炼乳就是完美的 cà phê sữa đá。\n\n"
                            "Trà——茶，越南最古老的饮品传统。免费的 trà đá 是每家餐厅的标配。\n\n"
                            "Sinh tố——水果奶昔，热带水果的甜蜜诱惑。Sinh tố bơ 是你必须尝试的。\n\n"
                            "Chè——甜汤，几十种口味等你探索。每个地区都有自己独特的 chè。\n\n"
                            "Bánh mì——法棍三明治，法国殖民历史留下的美味遗产。"
                            "一个好的 bánh mì 能让你忘记所有其他三明治。\n\n"
                            "Kem——冰淇淋，越南独特的口味让人惊喜。试试榴莲味的 kem，你会爱上它。\n\n"
                            "你现在已经拥有了在越南享受美食的语言工具。"
                            "下次当你站在越南的街头，面对琳琅满目的小吃摊时，"
                            "你不再是一个只能指着图片的游客——你是一个能用越南语点餐的旅行者。"
                            "继续学习，继续探索。越南的美食世界远比这12个词更丰富，"
                            "而你已经迈出了最重要的第一步。祝你好运！"
                        )
                    }
                }
            ]
        }
    ]
}

print(f"Validating: {content['title']}")
validate(content, level="beginner")
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
