#!/usr/bin/env python3
"""
create_beg_a1_2.py - Beginner zh-vi: Vietnamese Restaurant Ordering
Series: A1 (xcdgeb9g), Display Order: 2, Price: 19
Tone: desc=empathetic_observation, farewell=warm_accountability
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
DISPLAY_ORDER = 2
PRICE = 19

content = {
    "title": "越南餐厅点餐",
    "contentTypeTags": [],
    "difficultyTags": ["beginner"],
    "description": (
        "你是不是每次走进越南餐厅都只会指着菜单上的图片？\n\n"
        "别担心，你不是一个人。大多数初学者在餐厅里都会紧张到说不出话。"
        "但问题不在于你的勇气，而在于你缺少最基本的点餐词汇。\n\n"
        "这门课程就像一把钥匙，帮你打开越南餐厅的语言之门。"
        "12个精选词汇涵盖了从进门问好到结账离开的全过程。\n\n"
        "学完这门课，你将从'那个只会比划的外国人'变成'能用越南语流利点餐的客人'。"
    ),
    "preview": {
        "text": (
            "你是不是每次走进越南餐厅都只会指着菜单上的图片？"
            "大多数初学者在餐厅里都会紧张到说不出话，但这不是勇气的问题——"
            "而是词汇的问题。这门课程教你12个最实用的餐厅词汇："
            "从thực đơn（菜单）到gọi món（点餐），从tính tiền（结账）到ngon（好吃），"
            "从đũa（筷子）到muỗng（勺子），从đĩa（盘子）到ly（杯子），"
            "从nóng（热的）到lạnh（冷的），从cay（辣的）到ngọt（甜的）。"
            "你将通过真实的餐厅对话场景学习这些词汇，练习发音，"
            "并模拟真实的点餐过程。完成这门课程后，"
            "你将能够自信地走进任何一家越南餐厅，用越南语完成整个用餐过程。"
        )
    },
    "learningSessions": [
        {
            "title": "第1部分",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "介绍：餐厅基础词汇",
                    "description": "学习6个在越南餐厅最常用的基础词汇。",
                    "data": {
                        "text": (
                            "欢迎来到越南餐厅点餐课程！今天我们要学习6个在餐厅里最常用的词汇。\n\n"
                            "第一个词是 thực đơn。Thực đơn 就是菜单。走进餐厅，你首先需要的就是菜单。"
                            "你可以对服务员说：Cho tôi xem thực đơn，意思是'让我看看菜单'。\n\n"
                            "第二个词是 gọi món。Gọi món 是点餐的意思。"
                            "当你准备好了，可以举手说：Tôi muốn gọi món，意思是'我想点餐'。\n\n"
                            "第三个词是 tính tiền。Tính tiền 是结账。吃完饭后，"
                            "你对服务员说：Tính tiền，他们就会把账单拿来。简单直接。\n\n"
                            "第四个词是 ngon。Ngon 是好吃、美味的意思。"
                            "这可能是你在越南最常用的词之一。吃到好吃的东西就说：Ngon quá！"
                            "意思是'太好吃了！'越南人听到你这么说会非常开心。\n\n"
                            "第五个词是 đũa。Đũa 是筷子。越南人和中国人一样用筷子吃饭。"
                            "如果你需要筷子，可以说：Cho tôi đũa，意思是'给我筷子'。\n\n"
                            "第六个词是 muỗng。Muỗng 是勺子。喝汤的时候你需要勺子。"
                            "你可以说：Cho tôi một cái muỗng，意思是'给我一个勺子'。\n\n"
                            "好的，让我们开始练习：thực đơn, gọi món, tính tiền, ngon, đũa, muỗng。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：餐厅基础",
                    "description": "学习6个词：thực đơn, gọi món, tính tiền, ngon, đũa, muỗng",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：餐厅基础",
                    "description": "练习发音6个词：thực đơn, gọi món, tính tiền, ngon, đũa, muỗng",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：餐厅基础",
                    "description": "初级练习6个词：thực đơn, gọi món, tính tiền, ngon, đũa, muỗng",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：餐厅基础",
                    "description": "进阶练习6个词：thực đơn, gọi món, tính tiền, ngon, đũa, muỗng",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"]}
                },
                {
                    "activityType": "reading",
                    "title": "阅读：在越南餐厅",
                    "description": "Tôi vào nhà hàng và xin thực đơn.",
                    "data": {
                        "text": (
                            "Tôi vào nhà hàng và xin thực đơn. "
                            "Sau khi đọc xong, tôi gọi món. "
                            "Món ăn rất ngon. Tôi dùng đũa để ăn cơm. "
                            "Tôi cần muỗng để ăn súp. "
                            "Sau bữa ăn, tôi gọi tính tiền. "
                            "Nhà hàng này rất ngon, tôi sẽ quay lại."
                        ),
                        "vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：在越南餐厅",
                    "description": "朗读关于在越南餐厅用餐的短文。",
                    "data": {
                        "text": (
                            "Tôi vào nhà hàng và xin thực đơn. "
                            "Sau khi đọc xong, tôi gọi món. "
                            "Món ăn rất ngon. Tôi dùng đũa để ăn cơm. "
                            "Tôi cần muỗng để ăn súp. "
                            "Sau bữa ăn, tôi gọi tính tiền. "
                            "Nhà hàng này rất ngon, tôi sẽ quay lại."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：在越南餐厅",
                    "description": "听并跟读关于在越南餐厅用餐的短文。",
                    "data": {
                        "text": (
                            "Tôi vào nhà hàng và xin thực đơn. "
                            "Sau khi đọc xong, tôi gọi món. "
                            "Món ăn rất ngon. Tôi dùng đũa để ăn cơm. "
                            "Tôi cần muỗng để ăn súp. "
                            "Sau bữa ăn, tôi gọi tính tiền. "
                            "Nhà hàng này rất ngon, tôi sẽ quay lại."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：餐厅场景造句",
                    "description": "用本课学到的6个餐厅词汇写句子。",
                    "data": {
                        "vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"],
                        "items": [
                            {"prompt": "用 thực đơn 写一个关于选择食物的句子。例句：Thực đơn nhà hàng này có rất nhiều món ngon.", "targetVocab": "thực đơn"},
                            {"prompt": "用 gọi món 写一个关于在餐厅的句子。例句：Chúng tôi gọi món sau khi đọc thực đơn.", "targetVocab": "gọi món"},
                            {"prompt": "用 tính tiền 写一个关于结账的句子。例句：Sau bữa ăn, tôi gọi nhân viên tính tiền.", "targetVocab": "tính tiền"},
                            {"prompt": "用 ngon 写一个关于你喜欢的食物的句子。例句：Phở Hà Nội rất ngon, tôi ăn mỗi ngày.", "targetVocab": "ngon"},
                            {"prompt": "用 đũa 写一个关于餐具的句子。例句：Người Việt Nam dùng đũa để ăn cơm.", "targetVocab": "đũa"},
                            {"prompt": "用 muỗng 写一个关于喝汤的句子。例句：Tôi dùng muỗng để ăn chè và uống súp.", "targetVocab": "muỗng"}
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
                    "title": "介绍：口味与温度",
                    "description": "回顾第一课词汇，学习6个描述食物口味和温度的词汇。",
                    "data": {
                        "text": (
                            "欢迎回来！上一课我们学了6个餐厅基础词汇："
                            "thực đơn（菜单）、gọi món（点餐）、tính tiền（结账）、"
                            "ngon（好吃）、đũa（筷子）和 muỗng（勺子）。\n\n"
                            "今天我们学习6个描述食物的词汇，帮你更准确地表达你想要什么。\n\n"
                            "第一个词是 đĩa。Đĩa 是盘子。在越南餐厅，很多菜都是用盘子装的。"
                            "你可以说：Một đĩa cơm tấm，意思是'一盘碎米饭'。\n\n"
                            "第二个词是 ly。Ly 是杯子。点饮料时你会用到这个词。"
                            "比如：Một ly nước cam，意思是'一杯橙汁'。\n\n"
                            "第三个词是 nóng。Nóng 是热的。越南天气很热，但越南人还是喜欢喝热汤。"
                            "你可以说：Phở nóng rất ngon，意思是'热河粉很好吃'。\n\n"
                            "第四个词是 lạnh。Lạnh 是冷的，和 nóng 相反。"
                            "在越南，冷饮非常受欢迎。Nước lạnh 是冷水，cà phê đá 是冰咖啡。\n\n"
                            "第五个词是 cay。Cay 是辣的。越南菜有些很辣，特别是中部菜。"
                            "如果你不能吃辣，记住说：Không cay，意思是'不要辣'。\n\n"
                            "第六个词是 ngọt。Ngọt 是甜的。越南的甜品和饮料通常很甜。"
                            "你可以说：Chè này rất ngọt，意思是'这个甜汤很甜'。\n\n"
                            "好的，让我们练习：đĩa, ly, nóng, lạnh, cay, ngọt。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡：口味与温度",
                    "description": "学习6个词：đĩa, ly, nóng, lạnh, cay, ngọt",
                    "data": {"vocabList": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音练习：口味与温度",
                    "description": "练习发音6个词：đĩa, ly, nóng, lạnh, cay, ngọt",
                    "data": {"vocabList": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "词汇练习1：口味与温度",
                    "description": "初级练习6个词：đĩa, ly, nóng, lạnh, cay, ngọt",
                    "data": {"vocabList": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "词汇练习2：口味与温度",
                    "description": "进阶练习6个词：đĩa, ly, nóng, lạnh, cay, ngọt",
                    "data": {"vocabList": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "reading",
                    "title": "阅读：描述越南菜",
                    "description": "Trên bàn có một đĩa cơm và một ly nước.",
                    "data": {
                        "text": (
                            "Trên bàn có một đĩa cơm và một ly nước. "
                            "Phở nóng bốc khói thơm lừng. "
                            "Tôi thích uống cà phê lạnh vào mùa hè. "
                            "Món này rất cay, tôi không ăn được. "
                            "Chè đậu xanh ngọt và mát. "
                            "Tôi gọi một đĩa gỏi cuốn và một ly sinh tố."
                        ),
                        "vocabList": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：描述越南菜",
                    "description": "朗读关于描述越南菜的短文。",
                    "data": {
                        "text": (
                            "Trên bàn có một đĩa cơm và một ly nước. "
                            "Phở nóng bốc khói thơm lừng. "
                            "Tôi thích uống cà phê lạnh vào mùa hè. "
                            "Món này rất cay, tôi không ăn được. "
                            "Chè đậu xanh ngọt và mát. "
                            "Tôi gọi một đĩa gỏi cuốn và một ly sinh tố."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：描述越南菜",
                    "description": "听并跟读关于描述越南菜的短文。",
                    "data": {
                        "text": (
                            "Trên bàn có một đĩa cơm và một ly nước. "
                            "Phở nóng bốc khói thơm lừng. "
                            "Tôi thích uống cà phê lạnh vào mùa hè. "
                            "Món này rất cay, tôi không ăn được. "
                            "Chè đậu xanh ngọt và mát. "
                            "Tôi gọi một đĩa gỏi cuốn và một ly sinh tố."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：描述食物",
                    "description": "用本课学到的6个口味和温度词汇写句子。",
                    "data": {
                        "vocabList": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"],
                        "items": [
                            {"prompt": "用 đĩa 写一个关于餐桌上食物的句子。例句：Một đĩa cơm tấm sườn là bữa trưa yêu thích của tôi.", "targetVocab": "đĩa"},
                            {"prompt": "用 ly 写一个关于饮料的句子。例句：Tôi uống hai ly cà phê mỗi ngày.", "targetVocab": "ly"},
                            {"prompt": "用 nóng 写一个关于天气或食物的句子。例句：Hôm nay trời rất nóng, tôi muốn uống nước lạnh.", "targetVocab": "nóng"},
                            {"prompt": "用 lạnh 写一个关于饮品的句子。例句：Trà đá lạnh là thức uống phổ biến nhất ở Việt Nam.", "targetVocab": "lạnh"},
                            {"prompt": "用 cay 写一个关于越南菜的句子。例句：Bún bò Huế rất cay nhưng rất ngon.", "targetVocab": "cay"},
                            {"prompt": "用 ngọt 写一个关于甜品的句子。例句：Sinh tố xoài ngọt và thơm, rất hợp với mùa hè.", "targetVocab": "ngọt"}
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
                    "description": "回顾全部12个餐厅词汇，准备综合练习。",
                    "data": {
                        "text": (
                            "太棒了！你已经学完了12个越南餐厅词汇。\n\n"
                            "第一课：thực đơn（菜单）、gọi món（点餐）、tính tiền（结账）、"
                            "ngon（好吃）、đũa（筷子）、muỗng（勺子）。\n\n"
                            "第二课：đĩa（盘子）、ly（杯子）、nóng（热的）、"
                            "lạnh（冷的）、cay（辣的）、ngọt（甜的）。\n\n"
                            "现在让我们把这些词放在一起，模拟一次完整的餐厅体验。"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "词卡复习：全部12个词",
                    "description": "复习全部12个餐厅词汇。",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "发音复习：全部12个词",
                    "description": "练习发音全部12个餐厅词汇。",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "综合词汇练习1",
                    "description": "综合练习全部12个餐厅词汇。",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "综合词汇练习2",
                    "description": "进阶综合练习全部12个餐厅词汇。",
                    "data": {"vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]}
                },
                {
                    "activityType": "reading",
                    "title": "阅读：完整的餐厅体验",
                    "description": "Tôi bước vào nhà hàng và ngồi xuống.",
                    "data": {
                        "text": (
                            "Tôi bước vào nhà hàng và ngồi xuống. "
                            "Nhân viên đưa cho tôi thực đơn. Tôi đọc và gọi món. "
                            "Tôi gọi một đĩa cơm tấm nóng và một ly trà lạnh. "
                            "Tôi dùng đũa để ăn cơm và muỗng để ăn canh. "
                            "Món cơm tấm rất ngon nhưng hơi cay. "
                            "Tráng miệng là chè, ngọt vừa phải. "
                            "Cuối cùng, tôi gọi tính tiền và ra về."
                        ),
                        "vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "朗读：完整的餐厅体验",
                    "description": "朗读关于完整餐厅体验的短文。",
                    "data": {
                        "text": (
                            "Tôi bước vào nhà hàng và ngồi xuống. "
                            "Nhân viên đưa cho tôi thực đơn. Tôi đọc và gọi món. "
                            "Tôi gọi một đĩa cơm tấm nóng và một ly trà lạnh. "
                            "Tôi dùng đũa để ăn cơm và muỗng để ăn canh. "
                            "Món cơm tấm rất ngon nhưng hơi cay. "
                            "Tráng miệng là chè, ngọt vừa phải. "
                            "Cuối cùng, tôi gọi tính tiền và ra về."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：完整的餐厅体验",
                    "description": "听并跟读关于完整餐厅体验的短文。",
                    "data": {
                        "text": (
                            "Tôi bước vào nhà hàng và ngồi xuống. "
                            "Nhân viên đưa cho tôi thực đơn. Tôi đọc và gọi món. "
                            "Tôi gọi một đĩa cơm tấm nóng và một ly trà lạnh. "
                            "Tôi dùng đũa để ăn cơm và muỗng để ăn canh. "
                            "Món cơm tấm rất ngon nhưng hơi cay. "
                            "Tráng miệng là chè, ngọt vừa phải. "
                            "Cuối cùng, tôi gọi tính tiền và ra về."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "写作：模拟点餐",
                    "description": "用全部12个餐厅词汇进行综合写作练习。",
                    "data": {
                        "vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"],
                        "items": [
                            {"prompt": "用 thực đơn 和 gọi món 描述你在餐厅的经历。例句：Tôi xem thực đơn rồi gọi món yêu thích.", "targetVocab": "thực đơn"},
                            {"prompt": "用 nóng 和 lạnh 描述你喜欢的食物温度。例句：Tôi thích phở nóng nhưng thích cà phê lạnh.", "targetVocab": "nóng"},
                            {"prompt": "用 cay 和 ngọt 描述越南菜的口味。例句：Bún bò Huế cay, còn chè thì ngọt.", "targetVocab": "cay"},
                            {"prompt": "用 đĩa 和 ly 描述餐桌上的东西。例句：Trên bàn có một đĩa cơm và một ly nước cam.", "targetVocab": "đĩa"}
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
                            "欢迎来到最后一课！你已经掌握了12个越南餐厅词汇。\n\n"
                            "从菜单到结账，从筷子到勺子，从热到冷，从辣到甜——"
                            "你现在拥有了在越南餐厅完成一次完整用餐所需的全部词汇。\n\n"
                            "让我们通过最后一篇文章来巩固这些知识。"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "阅读：我的越南美食之旅",
                    "description": "Hôm nay tôi đi ăn ở một nhà hàng Việt Nam.",
                    "data": {
                        "text": (
                            "Hôm nay tôi đi ăn ở một nhà hàng Việt Nam. "
                            "Nhân viên mang thực đơn đến bàn. Tôi xem và gọi món. "
                            "Tôi gọi một đĩa cơm tấm sườn nóng hổi. "
                            "Tôi cũng gọi một ly cà phê sữa đá lạnh. "
                            "Nhân viên hỏi tôi có muốn ăn cay không. Tôi nói không cay. "
                            "Món ăn đến rồi. Tôi dùng đũa ăn cơm và muỗng ăn canh. "
                            "Cơm tấm rất ngon. Tráng miệng là chè, ngọt vừa phải. "
                            "Tôi rất hài lòng. Tôi gọi tính tiền và cảm ơn nhân viên. "
                            "Đây là bữa ăn ngon nhất trong chuyến đi của tôi."
                        ),
                        "vocabList": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng", "đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"]
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "听读：我的越南美食之旅",
                    "description": "听并跟读越南美食之旅的完整文章。",
                    "data": {
                        "text": (
                            "Hôm nay tôi đi ăn ở một nhà hàng Việt Nam. "
                            "Nhân viên mang thực đơn đến bàn. Tôi xem và gọi món. "
                            "Tôi gọi một đĩa cơm tấm sườn nóng hổi. "
                            "Tôi cũng gọi một ly cà phê sữa đá lạnh. "
                            "Nhân viên hỏi tôi có muốn ăn cay không. Tôi nói không cay. "
                            "Món ăn đến rồi. Tôi dùng đũa ăn cơm và muỗng ăn canh. "
                            "Cơm tấm rất ngon. Tráng miệng là chè, ngọt vừa phải. "
                            "Tôi rất hài lòng. Tôi gọi tính tiền và cảm ơn nhân viên. "
                            "Đây là bữa ăn ngon nhất trong chuyến đi của tôi."
                        )
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "告别与总结",
                    "description": "回顾所有词汇，鼓励继续学习。",
                    "data": {
                        "text": (
                            "恭喜你完成了越南餐厅点餐课程！让我们回顾你学到的12个词汇。\n\n"
                            "Thực đơn——菜单。走进任何一家越南餐厅，第一件事就是要菜单。"
                            "现在你知道怎么说了：Cho tôi xem thực đơn。试试看，下次真的用出来。\n\n"
                            "Gọi món——点餐。看完菜单，举手说 Tôi muốn gọi món。"
                            "这比用手指比划要自信得多，对吧？\n\n"
                            "Tính tiền——结账。吃完饭，一句 Tính tiền 就搞定。"
                            "不用再尴尬地做出签字的手势了。\n\n"
                            "Ngon——好吃。这个词你会用得最多。Ngon quá！"
                            "越南厨师听到这个词会给你最灿烂的笑容。\n\n"
                            "Đũa——筷子。你已经会用筷子了，现在你也会用越南语说它了。"
                            "Cho tôi đũa，简单明了。\n\n"
                            "Muỗng——勺子。喝汤必备。Cho tôi một cái muỗng。\n\n"
                            "Đĩa——盘子。Một đĩa cơm tấm，这是你在胡志明市最常说的话之一。\n\n"
                            "Ly——杯子。Một ly cà phê sữa đá，越南最经典的饮品点法。\n\n"
                            "Nóng——热的。越南人相信热汤能治百病。Phở nóng 是最好的证明。\n\n"
                            "Lạnh——冷的。在35度的天气里，一杯 nước lạnh 就是救命稻草。\n\n"
                            "Cay——辣的。记住 Không cay 这个救命短语。"
                            "除非你真的能吃辣，否则中部菜会让你流泪。\n\n"
                            "Ngọt——甜的。越南的甜品世界等你探索。Chè ngọt 是最好的开始。\n\n"
                            "现在我要给你一个挑战：下次去越南餐厅时，"
                            "试着用今天学到的词汇完成整个用餐过程。"
                            "从要菜单到结账，全程用越南语。你做得到的。"
                            "记住，犯错是学习的一部分。越南人会欣赏你的努力。加油！"
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
