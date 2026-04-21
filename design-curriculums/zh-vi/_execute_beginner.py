#!/usr/bin/env python3
"""
_execute_beginner.py — Creates ALL 31 zh-vi beginner curriculums directly against the live API.

Series IDs from orchestrator output:
  A1: xcdgeb9g  A2: ii4ilg7x  A3: ublh38nh  A4: kxfbilml
  B1: 9ki8fbsv  B2: 8n8btuza  B3: s55ahl3a  B4: al5ypcch
  C1: w5ublz2u  C2: t18is1i1  C3: 1oh7vayt  C4: n9h27ie9
  D1: 9hc3qncq  D2: fq1vyyvg  D3: wvyqv742  D4: 8j7v6med

Layout: 2 beginner per series (except D4 = 1), total = 31
"""
import sys
import time
import logging
import traceback

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/zh-vi")
from api_helpers import create_curriculum, add_to_series, set_display_order, set_price
from validate_content import validate

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SERIES_MAP = {
    'A1': 'xcdgeb9g',
    'A2': 'ii4ilg7x',
    'A3': 'ublh38nh',
    'A4': 'kxfbilml',
    'B1': '9ki8fbsv',
    'B2': '8n8btuza',
    'B3': 's55ahl3a',
    'B4': 'al5ypcch',
    'C1': 'w5ublz2u',
    'C2': 't18is1i1',
    'C3': '1oh7vayt',
    'C4': 'n9h27ie9',
    'D1': '9hc3qncq',
    'D2': 'fq1vyyvg',
    'D3': 'wvyqv742',
    'D4': '8j7v6med',
}


def build_beginner_content(d):
    """Build a complete beginner curriculum content dict from a compact definition dict d.

    d must have:
      title, description, preview_text,
      s1_title, s1_intro_title, s1_intro_desc, s1_intro_text,
      s1_vocab (list of 6), s1_topic,
      s1_reading_title, s1_reading_desc, s1_reading_text,
      s1_writing_items (list of dicts with prompt, targetVocab),
      s2_title, s2_intro_title, s2_intro_desc, s2_intro_text,
      s2_vocab (list of 6), s2_topic,
      s2_reading_title, s2_reading_desc, s2_reading_text,
      s2_writing_items,
      review_intro_text,
      review_reading_title, review_reading_desc, review_reading_text,
      review_writing_items,
      final_reading_title, final_reading_desc, final_reading_text,
      final_intro_text (opening), farewell_text
    """
    all_vocab = d['s1_vocab'] + d['s2_vocab']

    def _learning_session(vocab, topic, intro_title, intro_desc, intro_text,
                          reading_title, reading_desc, reading_text,
                          writing_items, session_title):
        return {
            "title": session_title,
            "activities": [
                {"activityType": "introAudio", "title": intro_title, "description": intro_desc, "data": {"text": intro_text}},
                {"activityType": "viewFlashcards", "title": f"词卡：{topic}", "description": f"学习6个词：{', '.join(vocab)}", "data": {"vocabList": list(vocab)}},
                {"activityType": "speakFlashcards", "title": f"发音练习：{topic}", "description": f"练习发音6个词：{', '.join(vocab)}", "data": {"vocabList": list(vocab)}},
                {"activityType": "vocabLevel1", "title": f"词汇练习1：{topic}", "description": f"初级练习6个词：{', '.join(vocab)}", "data": {"vocabList": list(vocab)}},
                {"activityType": "vocabLevel2", "title": f"词汇练习2：{topic}", "description": f"进阶练习6个词：{', '.join(vocab)}", "data": {"vocabList": list(vocab)}},
                {"activityType": "reading", "title": reading_title, "description": reading_desc, "data": {"text": reading_text, "vocabList": list(vocab)}},
                {"activityType": "speakReading", "title": reading_title.replace("阅读", "朗读"), "description": f"朗读{reading_title[3:]}的短文。", "data": {"text": reading_text}},
                {"activityType": "readAlong", "title": reading_title.replace("阅读", "听读"), "description": f"听并跟读{reading_title[3:]}的短文。", "data": {"text": reading_text}},
                {"activityType": "writingSentence", "title": f"写作：{topic}造句", "description": f"用本课学到的6个{topic}词汇写句子。", "data": {"vocabList": list(vocab), "items": writing_items}},
            ]
        }

    review_session = {
        "title": "复习",
        "activities": [
            {"activityType": "introAudio", "title": "复习介绍", "description": f"回顾全部12个词汇，准备综合练习。", "data": {"text": d['review_intro_text']}},
            {"activityType": "viewFlashcards", "title": "词卡复习：全部12个词", "description": "复习全部12个词汇。", "data": {"vocabList": list(all_vocab)}},
            {"activityType": "speakFlashcards", "title": "发音复习：全部12个词", "description": "练习发音全部12个词汇。", "data": {"vocabList": list(all_vocab)}},
            {"activityType": "reading", "title": d['review_reading_title'], "description": d['review_reading_desc'], "data": {"text": d['review_reading_text'], "vocabList": list(all_vocab)}},
            {"activityType": "speakReading", "title": d['review_reading_title'].replace("阅读", "朗读"), "description": f"朗读综合复习短文。", "data": {"text": d['review_reading_text']}},
            {"activityType": "readAlong", "title": d['review_reading_title'].replace("阅读", "听读"), "description": f"听并跟读综合复习短文。", "data": {"text": d['review_reading_text']}},
        ]
    }

    final_session = {
        "title": "综合阅读",
        "activities": [
            {"activityType": "reading", "title": d['final_reading_title'], "description": d['final_reading_desc'], "data": {"text": d['final_reading_text'], "vocabList": list(all_vocab)}},
            {"activityType": "readAlong", "title": d['final_reading_title'].replace("阅读", "听读"), "description": f"听并跟读最终综合文章。", "data": {"text": d['final_reading_text']}},
            {"activityType": "introAudio", "title": "告别与总结", "description": "回顾所有词汇，温暖告别。", "data": {"text": d['farewell_text']}},
        ]
    }

    return {
        "title": d['title'],
        "contentTypeTags": [],
        "difficultyTags": ["beginner"],
        "description": d['description'],
        "preview": {"text": d['preview_text']},
        "learningSessions": [
            _learning_session(d['s1_vocab'], d['s1_topic'], d['s1_intro_title'], d['s1_intro_desc'], d['s1_intro_text'],
                              d['s1_reading_title'], d['s1_reading_desc'], d['s1_reading_text'], d['s1_writing_items'], "第1部分"),
            _learning_session(d['s2_vocab'], d['s2_topic'], d['s2_intro_title'], d['s2_intro_desc'], d['s2_intro_text'],
                              d['s2_reading_title'], d['s2_reading_desc'], d['s2_reading_text'], d['s2_writing_items'], "第2部分"),
            review_session,
            final_session,
        ]
    }


# ---------------------------------------------------------------------------
# ALL 31 beginner curriculum definitions
# ---------------------------------------------------------------------------
ALL = [
    # ===== A1-1: 越南街头小吃 (display_order=1) =====
    {
        "series": "A1", "order": 1,
        "title": "越南街头小吃",
        "description": (
            "想象你走在胡志明市的街头，空气中弥漫着炭火烤肉的香气，"
            "路边摊的蒸汽模糊了霓虹灯光——你却连一碗河粉都不会点。\n\n"
            "越南街头小吃不只是食物，它是一整套社交密码。"
            "从清晨的面包摊到深夜的烧烤档，每一个摊位都是一堂文化课。\n\n"
            "这门课程带你从零开始，用12个核心词汇打开越南美食世界的大门。"
            "你将学会点餐、描述口味、理解菜单——不再只是指着图片说「这个」。\n\n"
            "掌握这些词汇，你的越南之旅将从「游客模式」切换到「本地模式」。"
        ),
        "preview_text": (
            "想象你走在胡志明市的街头，空气中弥漫着炭火烤肉的香气，"
            "路边摊的蒸汽模糊了霓虹灯光。越南的街头小吃文化是世界上最丰富的之一，"
            "但如果你不会用越南语点餐，你就只能永远站在外面看。"
            "这门课程教你12个最实用的美食词汇：从phở（河粉）到nước mắm（鱼露），"
            "从gỏi cuốn（春卷）到chả giò（炸春卷），从cơm（米饭）到bún（米粉）。"
            "你将通过真实的越南语阅读材料学习这些词汇，练习发音，"
            "并用它们写出自己的句子。完成这门课程后，"
            "你将能够自信地走进任何一家越南餐厅，用越南语点一顿地道的饭。"
        ),
        "s1_vocab": ["phở", "nước mắm", "gỏi cuốn", "chả giò", "cơm", "bún"],
        "s1_topic": "街头小吃基础",
        "s1_intro_title": "介绍：越南街头小吃",
        "s1_intro_desc": "欢迎来到越南街头小吃的世界，学习6个核心美食词汇。",
        "s1_intro_text": (
            "欢迎来到越南街头小吃课程！今天我们要学习6个在越南吃饭时最常用的词汇。\n\n"
            "第一个词是 phở。Phở 是越南最著名的菜肴——一碗热气腾腾的牛肉或鸡肉河粉汤。"
            "在越南，人们早餐就开始吃 phở。比如你可以说：Tôi muốn một tô phở bò，"
            "意思是「我想要一碗牛肉河粉」。\n\n"
            "第二个词是 nước mắm。Nước mắm 是鱼露，越南菜的灵魂调料。"
            "几乎每道越南菜都会用到它。在餐桌上你会听到：Cho thêm nước mắm，"
            "意思是「再加点鱼露」。\n\n"
            "第三个词是 gỏi cuốn。Gỏi cuốn 是越南鲜春卷，用米纸包裹虾肉、蔬菜和米粉。"
            "这是越南最受欢迎的开胃菜之一。你可以说：Cho tôi hai cuốn gỏi cuốn，"
            "意思是「给我两个春卷」。\n\n"
            "第四个词是 chả giò。Chả giò 是炸春卷，外皮酥脆，内馅是猪肉和蔬菜。"
            "在南方叫 chả giò，在北方叫 nem rán。点餐时说：Một đĩa chả giò，"
            "意思是「一盘炸春卷」。\n\n"
            "第五个词是 cơm。Cơm 就是米饭，越南人每天都吃。"
            "Cơm tấm 是碎米饭，胡志明市的招牌菜。你会经常看到：Cơm tấm sườn，"
            "意思是「排骨碎米饭」。\n\n"
            "第六个词是 bún。Bún 是米粉，比河粉更细更圆。"
            "Bún chả 是河内最有名的米粉菜肴。奥巴马访问河内时就吃了 bún chả。"
            "你可以说：Tôi thích bún chả，意思是「我喜欢烤肉米粉」。\n\n"
            "好的，让我们开始练习这6个词：phở, nước mắm, gỏi cuốn, chả giò, cơm, bún。"
        ),
        "s1_reading_title": "阅读：街头小吃之旅",
        "s1_reading_desc": "Buổi sáng ở Sài Gòn bắt đầu với một tô phở nóng hổi.",
        "s1_reading_text": (
            "Buổi sáng ở Sài Gòn bắt đầu với một tô phở nóng hổi. "
            "Người bán hàng cho thêm nước mắm vào bát. "
            "Khách du lịch thường gọi gỏi cuốn làm món khai vị. "
            "Chả giò giòn tan là món ăn yêu thích của trẻ em. "
            "Bữa trưa đơn giản nhất là một đĩa cơm với thịt nướng. "
            "Buổi tối, nhiều người chọn bún chả ở quán vỉa hè."
        ),
        "s1_writing_items": [
            {"prompt": "用 phở 写一个关于早餐的句子。例句：Mỗi sáng, tôi ăn một tô phở gà ở quán gần nhà.", "targetVocab": "phở"},
            {"prompt": "用 nước mắm 写一个关于调味料的句子。例句：Nước mắm là gia vị quan trọng nhất trong bếp Việt Nam.", "targetVocab": "nước mắm"},
            {"prompt": "用 gỏi cuốn 写一个关于点餐的句子。例句：Tôi gọi hai cuốn gỏi cuốn tôm cho bữa trưa.", "targetVocab": "gỏi cuốn"},
            {"prompt": "用 chả giò 写一个关于你喜欢的食物的句子。例句：Chả giò của mẹ tôi là món ngon nhất.", "targetVocab": "chả giò"},
            {"prompt": "用 cơm 写一个关于日常饮食的句子。例句：Người Việt Nam ăn cơm ba bữa mỗi ngày.", "targetVocab": "cơm"},
            {"prompt": "用 bún 写一个关于你最喜欢的越南菜的句子。例句：Bún chả Hà Nội là món ăn tôi muốn thử nhất.", "targetVocab": "bún"},
        ],
        "s2_vocab": ["cà phê", "trà", "sinh tố", "chè", "bánh mì", "kem"],
        "s2_topic": "饮品与甜点",
        "s2_intro_title": "介绍：饮品与甜点",
        "s2_intro_desc": "回顾第一课词汇，学习6个新的饮品和甜点词汇。",
        "s2_intro_text": (
            "欢迎回来！在上一课中，我们学习了6个越南街头小吃的核心词汇："
            "phở（河粉）、nước mắm（鱼露）、gỏi cuốn（鲜春卷）、"
            "chả giò（炸春卷）、cơm（米饭）和 bún（米粉）。\n\n"
            "今天我们继续探索越南美食，学习6个关于饮品和甜点的词汇。\n\n"
            "第一个词是 cà phê。Cà phê 是咖啡，越南是世界第二大咖啡出口国。"
            "越南咖啡通常很浓，加炼乳。你可以说：Cho tôi một ly cà phê sữa đá，"
            "意思是「给我一杯冰奶咖啡」。\n\n"
            "第二个词是 trà。Trà 是茶，越南人喝茶的历史比咖啡长得多。"
            "在越南餐厅，服务员通常会免费提供 trà đá（冰茶）。"
            "你可以说：Cho tôi một ly trà đá，意思是「给我一杯冰茶」。\n\n"
            "第三个词是 sinh tố。Sinh tố 是水果奶昔，越南的热带水果让奶昔特别好喝。"
            "最受欢迎的是 sinh tố bơ（牛油果奶昔）。"
            "你可以说：Tôi muốn một ly sinh tố xoài，意思是「我想要一杯芒果奶昔」。\n\n"
            "第四个词是 chè。Chè 是越南甜汤，有几十种不同的口味。"
            "从绿豆到芋头，从椰奶到莲子，每种 chè 都是一个惊喜。"
            "你可以说：Chè này ngon quá，意思是「这个甜汤太好吃了」。\n\n"
            "第五个词是 bánh mì。Bánh mì 是越南法棍三明治，融合了法国和越南的美食传统。"
            "一个好的 bánh mì 外脆内软，馅料丰富。"
            "你可以说：Một bánh mì thịt，意思是「一个肉三明治」。\n\n"
            "第六个词是 kem。Kem 是冰淇淋，越南的 kem 口味独特，"
            "有榴莲味、椰子味，甚至绿豆味。"
            "你可以说：Cho tôi một cây kem dừa，意思是「给我一个椰子冰淇淋」。\n\n"
            "好的，让我们练习这6个新词：cà phê, trà, sinh tố, chè, bánh mì, kem。"
        ),
        "s2_reading_title": "阅读：越南饮品文化",
        "s2_reading_desc": "Người Việt Nam rất thích uống cà phê.",
        "s2_reading_text": (
            "Người Việt Nam rất thích uống cà phê. "
            "Buổi sáng, họ ngồi ở quán vỉa hè và uống trà đá. "
            "Trẻ em thường chọn sinh tố trái cây thay vì cà phê. "
            "Sau bữa ăn, một bát chè là món tráng miệng hoàn hảo. "
            "Bánh mì là bữa sáng nhanh và rẻ nhất ở Việt Nam. "
            "Vào mùa hè, ai cũng muốn ăn kem mát lạnh."
        ),
        "s2_writing_items": [
            {"prompt": "用 cà phê 写一个关于你早晨习惯的句子。例句：Tôi uống cà phê mỗi sáng trước khi đi làm.", "targetVocab": "cà phê"},
            {"prompt": "用 trà 写一个关于越南餐厅的句子。例句：Nhà hàng Việt Nam luôn có trà đá miễn phí.", "targetVocab": "trà"},
            {"prompt": "用 sinh tố 写一个关于热带水果的句子。例句：Sinh tố xoài ở Việt Nam rất ngon và rẻ.", "targetVocab": "sinh tố"},
            {"prompt": "用 chè 写一个关于甜点的句子。例句：Chè đậu xanh là món tráng miệng truyền thống.", "targetVocab": "chè"},
            {"prompt": "用 bánh mì 写一个关于快餐的句子。例句：Bánh mì Sài Gòn nổi tiếng khắp thế giới.", "targetVocab": "bánh mì"},
            {"prompt": "用 kem 写一个关于夏天的句子。例句：Mùa hè ở Hà Nội, tôi ăn kem mỗi ngày.", "targetVocab": "kem"},
        ],
        "review_intro_text": (
            "恭喜你完成了前两课的学习！你已经掌握了12个越南美食词汇。\n\n"
            "让我们快速回顾一下。第一课我们学了：phở（河粉）、nước mắm（鱼露）、"
            "gỏi cuốn（鲜春卷）、chả giò（炸春卷）、cơm（米饭）和 bún（米粉）。\n\n"
            "第二课我们学了：cà phê（咖啡）、trà（茶）、sinh tố（水果奶昔）、"
            "chè（甜汤）、bánh mì（法棍三明治）和 kem（冰淇淋）。\n\n"
            "现在我们要把这12个词放在一起练习。你将阅读一篇包含所有词汇的文章，"
            "然后完成综合练习。准备好了吗？"
        ),
        "review_reading_title": "阅读：越南美食一日游",
        "review_reading_desc": "Một ngày ở Sài Gòn bắt đầu với bánh mì và cà phê sữa đá.",
        "review_reading_text": (
            "Một ngày ở Sài Gòn bắt đầu với bánh mì và cà phê sữa đá. "
            "Sau đó, bạn có thể uống trà đá ở quán vỉa hè. "
            "Bữa trưa, hãy thử một tô phở bò với nhiều nước mắm. "
            "Hoặc bạn có thể gọi cơm tấm sườn và gỏi cuốn. "
            "Buổi chiều, sinh tố xoài là lựa chọn tuyệt vời. "
            "Bữa tối, chả giò giòn tan và bún chả là sự kết hợp hoàn hảo. "
            "Cuối ngày, thưởng thức một bát chè hoặc một cây kem mát lạnh."
        ),
        "review_writing_items": [
            {"prompt": "用 phở 和 nước mắm 写一个关于越南早餐的句子。", "targetVocab": "phở"},
            {"prompt": "用 cà phê 和 bánh mì 写一个关于快餐的句子。", "targetVocab": "cà phê"},
            {"prompt": "用 gỏi cuốn 和 chả giò 比较两种春卷。", "targetVocab": "gỏi cuốn"},
            {"prompt": "用 sinh tố 和 chè 写一个关于甜品的句子。", "targetVocab": "sinh tố"},
        ],
        "final_reading_title": "阅读：越南美食完整指南",
        "final_reading_desc": "Việt Nam là thiên đường ẩm thực.",
        "final_reading_text": (
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
        "farewell_text": (
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
        ),
    },
    # ===== A1-2: 越南餐厅点餐 (display_order=2) =====
    {
        "series": "A1", "order": 2,
        "title": "越南餐厅点餐",
        "description": (
            "你是不是每次走进越南餐厅都只会指着菜单上的图片？\n\n"
            "别担心，你不是一个人。大多数初学者在餐厅里都会紧张到说不出话。"
            "但问题不在于你的勇气，而在于你缺少最基本的点餐词汇。\n\n"
            "这门课程就像一把钥匙，帮你打开越南餐厅的语言之门。"
            "12个精选词汇涵盖了从进门问好到结账离开的全过程。\n\n"
            "学完这门课，你将从「那个只会比划的外国人」变成「能用越南语流利点餐的客人」。"
        ),
        "preview_text": (
            "你是不是每次走进越南餐厅都只会指着菜单上的图片？"
            "大多数初学者在餐厅里都会紧张到说不出话，但这不是勇气的问题——"
            "而是词汇的问题。这门课程教你12个最实用的餐厅词汇："
            "从thực đơn（菜单）到gọi món（点餐），从tính tiền（结账）到ngon（好吃），"
            "从đũa（筷子）到muỗng（勺子），从đĩa（盘子）到ly（杯子），"
            "从nóng（热的）到lạnh（冷的），从cay（辣的）到ngọt（甜的）。"
            "你将通过真实的餐厅对话场景学习这些词汇，练习发音，"
            "并模拟真实的点餐过程。完成这门课程后，"
            "你将能够自信地走进任何一家越南餐厅，用越南语完成整个用餐过程。"
        ),
        "s1_vocab": ["thực đơn", "gọi món", "tính tiền", "ngon", "đũa", "muỗng"],
        "s1_topic": "餐厅基础",
        "s1_intro_title": "介绍：餐厅基础词汇",
        "s1_intro_desc": "学习6个在越南餐厅最常用的基础词汇。",
        "s1_intro_text": (
            "欢迎来到越南餐厅点餐课程！今天我们要学习6个在餐厅里最常用的词汇。\n\n"
            "第一个词是 thực đơn。Thực đơn 就是菜单。走进餐厅，你首先需要的就是菜单。"
            "你可以对服务员说：Cho tôi xem thực đơn，意思是「让我看看菜单」。\n\n"
            "第二个词是 gọi món。Gọi món 是点餐的意思。"
            "当你准备好了，可以举手说：Tôi muốn gọi món，意思是「我想点餐」。\n\n"
            "第三个词是 tính tiền。Tính tiền 是结账。吃完饭后，"
            "你对服务员说：Tính tiền，他们就会把账单拿来。简单直接。\n\n"
            "第四个词是 ngon。Ngon 是好吃、美味的意思。"
            "这可能是你在越南最常用的词之一。吃到好吃的东西就说：Ngon quá！"
            "意思是「太好吃了！」越南人听到你这么说会非常开心。\n\n"
            "第五个词是 đũa。Đũa 是筷子。越南人和中国人一样用筷子吃饭。"
            "如果你需要筷子，可以说：Cho tôi đũa，意思是「给我筷子」。\n\n"
            "第六个词是 muỗng。Muỗng 是勺子。喝汤的时候你需要勺子。"
            "你可以说：Cho tôi một cái muỗng，意思是「给我一个勺子」。\n\n"
            "好的，让我们开始练习：thực đơn, gọi món, tính tiền, ngon, đũa, muỗng。"
        ),
        "s1_reading_title": "阅读：在越南餐厅",
        "s1_reading_desc": "Tôi vào nhà hàng và xin thực đơn.",
        "s1_reading_text": (
            "Tôi vào nhà hàng và xin thực đơn. "
            "Sau khi đọc xong, tôi gọi món. "
            "Món ăn rất ngon. Tôi dùng đũa để ăn cơm. "
            "Tôi cần muỗng để ăn súp. "
            "Sau bữa ăn, tôi gọi tính tiền. "
            "Nhà hàng này rất ngon, tôi sẽ quay lại."
        ),
        "s1_writing_items": [
            {"prompt": "用 thực đơn 写一个关于选择食物的句子。例句：Thực đơn nhà hàng này có rất nhiều món ngon.", "targetVocab": "thực đơn"},
            {"prompt": "用 gọi món 写一个关于在餐厅的句子。例句：Chúng tôi gọi món sau khi đọc thực đơn.", "targetVocab": "gọi món"},
            {"prompt": "用 tính tiền 写一个关于结账的句子。例句：Sau bữa ăn, tôi gọi nhân viên tính tiền.", "targetVocab": "tính tiền"},
            {"prompt": "用 ngon 写一个关于你喜欢的食物的句子。例句：Phở Hà Nội rất ngon, tôi ăn mỗi ngày.", "targetVocab": "ngon"},
            {"prompt": "用 đũa 写一个关于餐具的句子。例句：Người Việt Nam dùng đũa để ăn cơm.", "targetVocab": "đũa"},
            {"prompt": "用 muỗng 写一个关于喝汤的句子。例句：Tôi dùng muỗng để ăn chè và uống súp.", "targetVocab": "muỗng"},
        ],
        "s2_vocab": ["đĩa", "ly", "nóng", "lạnh", "cay", "ngọt"],
        "s2_topic": "口味与温度",
        "s2_intro_title": "介绍：口味与温度",
        "s2_intro_desc": "回顾第一课词汇，学习6个描述食物口味和温度的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了6个餐厅基础词汇："
            "thực đơn（菜单）、gọi món（点餐）、tính tiền（结账）、"
            "ngon（好吃）、đũa（筷子）和 muỗng（勺子）。\n\n"
            "今天我们学习6个描述食物的词汇，帮你更准确地表达你想要什么。\n\n"
            "第一个词是 đĩa。Đĩa 是盘子。在越南餐厅，很多菜都是用盘子装的。"
            "你可以说：Một đĩa cơm tấm，意思是「一盘碎米饭」。\n\n"
            "第二个词是 ly。Ly 是杯子。点饮料时你会用到这个词。"
            "比如：Một ly nước cam，意思是「一杯橙汁」。\n\n"
            "第三个词是 nóng。Nóng 是热的。越南天气很热，但越南人还是喜欢喝热汤。"
            "你可以说：Phở nóng rất ngon，意思是「热河粉很好吃」。\n\n"
            "第四个词是 lạnh。Lạnh 是冷的，和 nóng 相反。"
            "在越南，冷饮非常受欢迎。Nước lạnh 是冷水，cà phê đá 是冰咖啡。\n\n"
            "第五个词是 cay。Cay 是辣的。越南菜有些很辣，特别是中部菜。"
            "如果你不能吃辣，记住说：Không cay，意思是「不要辣」。\n\n"
            "第六个词是 ngọt。Ngọt 是甜的。越南的甜品和饮料通常很甜。"
            "你可以说：Chè này rất ngọt，意思是「这个甜汤很甜」。\n\n"
            "好的，让我们练习：đĩa, ly, nóng, lạnh, cay, ngọt。"
        ),
        "s2_reading_title": "阅读：描述越南菜",
        "s2_reading_desc": "Trên bàn có một đĩa cơm và một ly nước.",
        "s2_reading_text": (
            "Trên bàn có một đĩa cơm và một ly nước. "
            "Phở nóng bốc khói thơm lừng. "
            "Tôi thích uống cà phê lạnh vào mùa hè. "
            "Món này rất cay, tôi không ăn được. "
            "Chè đậu xanh ngọt và mát. "
            "Tôi gọi một đĩa gỏi cuốn và một ly sinh tố."
        ),
        "s2_writing_items": [
            {"prompt": "用 đĩa 写一个关于餐桌上食物的句子。例句：Một đĩa cơm tấm sườn là bữa trưa yêu thích của tôi.", "targetVocab": "đĩa"},
            {"prompt": "用 ly 写一个关于饮料的句子。例句：Tôi uống hai ly cà phê mỗi ngày.", "targetVocab": "ly"},
            {"prompt": "用 nóng 写一个关于天气或食物的句子。例句：Hôm nay trời rất nóng, tôi muốn uống nước lạnh.", "targetVocab": "nóng"},
            {"prompt": "用 lạnh 写一个关于饮品的句子。例句：Trà đá lạnh là thức uống phổ biến nhất ở Việt Nam.", "targetVocab": "lạnh"},
            {"prompt": "用 cay 写一个关于越南菜的句子。例句：Bún bò Huế rất cay nhưng rất ngon.", "targetVocab": "cay"},
            {"prompt": "用 ngọt 写一个关于甜品的句子。例句：Sinh tố xoài ngọt và thơm, rất hợp với mùa hè.", "targetVocab": "ngọt"},
        ],
        "review_intro_text": (
            "太棒了！你已经学完了12个越南餐厅词汇。\n\n"
            "第一课：thực đơn（菜单）、gọi món（点餐）、tính tiền（结账）、"
            "ngon（好吃）、đũa（筷子）、muỗng（勺子）。\n\n"
            "第二课：đĩa（盘子）、ly（杯子）、nóng（热的）、"
            "lạnh（冷的）、cay（辣的）、ngọt（甜的）。\n\n"
            "现在让我们把这些词放在一起，模拟一次完整的餐厅体验。"
        ),
        "review_reading_title": "阅读：完整的餐厅体验",
        "review_reading_desc": "Tôi bước vào nhà hàng và ngồi xuống.",
        "review_reading_text": (
            "Tôi bước vào nhà hàng và ngồi xuống. "
            "Nhân viên đưa cho tôi thực đơn. Tôi đọc và gọi món. "
            "Tôi gọi một đĩa cơm tấm nóng và một ly trà lạnh. "
            "Tôi dùng đũa để ăn cơm và muỗng để ăn canh. "
            "Món cơm tấm rất ngon nhưng hơi cay. "
            "Tráng miệng là chè, ngọt vừa phải. "
            "Cuối cùng, tôi gọi tính tiền và ra về."
        ),
        "review_writing_items": [
            {"prompt": "用 thực đơn 和 gọi món 描述你在餐厅的经历。", "targetVocab": "thực đơn"},
            {"prompt": "用 nóng 和 lạnh 描述你喜欢的食物温度。", "targetVocab": "nóng"},
            {"prompt": "用 cay 和 ngọt 描述越南菜的口味。", "targetVocab": "cay"},
            {"prompt": "用 đĩa 和 ly 描述餐桌上的东西。", "targetVocab": "đĩa"},
        ],
        "final_reading_title": "阅读：我的越南美食之旅",
        "final_reading_desc": "Hôm nay tôi đi ăn ở một nhà hàng Việt Nam.",
        "final_reading_text": (
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
        "farewell_text": (
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
        ),
    },
    # ===== A2-1: 越南城市交通 (display_order=1) =====
    {
        "series": "A2", "order": 1,
        "title": "越南城市交通",
        "description": (
            "你有没有想过，为什么胡志明市的摩托车比汽车还多？\n\n"
            "在越南，交通不只是从A到B的过程——它是一种生活方式。"
            "理解越南的交通系统，就是理解这个国家运转的方式。\n\n"
            "这门课程教你12个最实用的交通词汇，从打车到坐公交，"
            "从问路到买票，让你在越南的城市里自由穿行。\n\n"
            "不再迷路，不再被宰，不再只能靠手机翻译——用越南语掌控你的出行。"
        ),
        "preview_text": (
            "你有没有想过，为什么胡志明市的摩托车比汽车还多？"
            "在越南，交通不只是从A到B的过程，它是一种生活方式。"
            "这门课程教你12个最实用的交通词汇：从xe máy（摩托车）到xe buýt（公交车），"
            "从taxi到xe ôm（摩托出租车），从đường（路）到ngã tư（十字路口），"
            "从bến xe（车站）到vé（票），从rẽ trái（左转）到rẽ phải（右转），"
            "从gần（近）到xa（远）。你将通过真实的交通场景学习这些词汇，"
            "练习发音，并模拟真实的出行对话。完成这门课程后，"
            "你将能够自信地在越南的城市里独立出行。"
        ),
        "s1_vocab": ["xe máy", "xe buýt", "taxi", "xe ôm", "đường", "ngã tư"],
        "s1_topic": "交通工具与道路",
        "s1_intro_title": "介绍：越南交通工具",
        "s1_intro_desc": "学习6个越南城市交通的核心词汇。",
        "s1_intro_text": (
            "欢迎来到越南城市交通课程！今天我们学习6个在越南出行时最常用的词汇。\n\n"
            "第一个词是 xe máy。Xe máy 是摩托车，越南最常见的交通工具。"
            "在胡志明市，几乎每个人都有一辆 xe máy。你会听到：Tôi đi xe máy，"
            "意思是「我骑摩托车」。\n\n"
            "第二个词是 xe buýt。Xe buýt 是公交车。越南的公交系统正在快速发展。"
            "你可以说：Xe buýt số 1 đi đâu？意思是「1路公交车去哪里？」\n\n"
            "第三个词是 taxi。Taxi 在越南和中文一样，就是出租车。"
            "在越南打车很方便。你可以说：Gọi taxi，意思是「叫出租车」。\n\n"
            "第四个词是 xe ôm。Xe ôm 是摩托出租车，越南特有的交通方式。"
            "Grab 就是现代版的 xe ôm。你可以说：Tôi đi xe ôm，意思是「我坐摩的」。\n\n"
            "第五个词是 đường。Đường 是路、街道。问路时你会经常用到这个词。"
            "比如：Đường này đi đâu？意思是「这条路去哪里？」\n\n"
            "第六个词是 ngã tư。Ngã tư 是十字路口。越南的十字路口非常热闹。"
            "你可以说：Rẽ phải ở ngã tư，意思是「在十字路口右转」。\n\n"
            "好的，让我们练习：xe máy, xe buýt, taxi, xe ôm, đường, ngã tư。"
        ),
        "s1_reading_title": "阅读：越南街头交通",
        "s1_reading_desc": "Đường phố Sài Gòn rất đông xe máy.",
        "s1_reading_text": (
            "Đường phố Sài Gòn rất đông xe máy. "
            "Xe buýt chạy chậm vì kẹt xe. "
            "Nhiều du khách chọn đi taxi cho tiện. "
            "Xe ôm là cách nhanh nhất để đi trong thành phố. "
            "Đường Nguyễn Huệ là con đường nổi tiếng nhất. "
            "Ở ngã tư, xe máy và ô tô chen nhau."
        ),
        "s1_writing_items": [
            {"prompt": "用 xe máy 写一个关于越南交通的句子。例句：Ở Việt Nam, xe máy là phương tiện phổ biến nhất.", "targetVocab": "xe máy"},
            {"prompt": "用 xe buýt 写一个关于公共交通的句子。例句：Tôi đi xe buýt đến trường mỗi ngày.", "targetVocab": "xe buýt"},
            {"prompt": "用 taxi 写一个关于打车的句子。例句：Tôi gọi taxi từ sân bay về khách sạn.", "targetVocab": "taxi"},
            {"prompt": "用 xe ôm 写一个关于出行方式的句子。例句：Xe ôm rẻ hơn taxi nhưng nhanh hơn xe buýt.", "targetVocab": "xe ôm"},
            {"prompt": "用 đường 写一个关于问路的句子。例句：Đường đến chợ Bến Thành có xa không?", "targetVocab": "đường"},
            {"prompt": "用 ngã tư 写一个关于方向的句子。例句：Đi thẳng rồi rẽ trái ở ngã tư.", "targetVocab": "ngã tư"},
        ],
        "s2_vocab": ["bến xe", "vé", "rẽ trái", "rẽ phải", "gần", "xa"],
        "s2_topic": "方向与票务",
        "s2_intro_title": "介绍：方向与票务",
        "s2_intro_desc": "学习6个关于方向和票务的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：xe máy（摩托车）、xe buýt（公交车）、"
            "taxi（出租车）、xe ôm（摩的）、đường（路）和 ngã tư（十字路口）。\n\n"
            "今天我们学习6个帮你找到目的地的词汇。\n\n"
            "第一个词是 bến xe。Bến xe 是车站。越南的长途汽车站叫 bến xe。"
            "你可以说：Bến xe ở đâu？意思是「车站在哪里？」\n\n"
            "第二个词是 vé。Vé 是票。坐公交或长途车都需要买票。"
            "你可以说：Một vé đi Hà Nội，意思是「一张去河内的票」。\n\n"
            "第三个词是 rẽ trái。Rẽ trái 是左转。问路时非常有用。"
            "比如：Rẽ trái ở ngã tư，意思是「在十字路口左转」。\n\n"
            "第四个词是 rẽ phải。Rẽ phải 是右转，和 rẽ trái 相反。"
            "你可以说：Rẽ phải rồi đi thẳng，意思是「右转然后直走」。\n\n"
            "第五个词是 gần。Gần 是近的。问距离时很有用。"
            "比如：Nhà hàng gần đây không？意思是「附近有餐厅吗？」\n\n"
            "第六个词是 xa。Xa 是远的，和 gần 相反。"
            "你可以说：Sân bay có xa không？意思是「机场远吗？」\n\n"
            "好的，让我们练习：bến xe, vé, rẽ trái, rẽ phải, gần, xa。"
        ),
        "s2_reading_title": "阅读：问路与买票",
        "s2_reading_desc": "Tôi đến bến xe để mua vé đi Đà Nẵng.",
        "s2_reading_text": (
            "Tôi đến bến xe để mua vé đi Đà Nẵng. "
            "Nhân viên nói rẽ trái để đến quầy vé. "
            "Tôi mua một vé và hỏi đường đến cổng. "
            "Anh ấy nói rẽ phải rồi đi thẳng. "
            "Bến xe rất gần trung tâm thành phố. "
            "Đà Nẵng không xa Huế lắm."
        ),
        "s2_writing_items": [
            {"prompt": "用 bến xe 写一个关于旅行的句子。例句：Bến xe miền Đông là bến xe lớn nhất Sài Gòn.", "targetVocab": "bến xe"},
            {"prompt": "用 vé 写一个关于买票的句子。例句：Tôi mua vé xe buýt ở quầy bán vé.", "targetVocab": "vé"},
            {"prompt": "用 rẽ trái 写一个关于方向的句子。例句：Rẽ trái ở đèn đỏ, bạn sẽ thấy nhà hàng.", "targetVocab": "rẽ trái"},
            {"prompt": "用 rẽ phải 写一个关于指路的句子。例句：Đi thẳng rồi rẽ phải, khách sạn ở bên trái.", "targetVocab": "rẽ phải"},
            {"prompt": "用 gần 写一个关于距离的句子。例句：Chợ Bến Thành rất gần khách sạn của tôi.", "targetVocab": "gần"},
            {"prompt": "用 xa 写一个关于旅行距离的句子。例句：Hà Nội xa Sài Gòn khoảng 1700 km.", "targetVocab": "xa"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南交通词汇！\n\n"
            "第一课：xe máy（摩托车）、xe buýt（公交车）、taxi（出租车）、"
            "xe ôm（摩的）、đường（路）、ngã tư（十字路口）。\n\n"
            "第二课：bến xe（车站）、vé（票）、rẽ trái（左转）、"
            "rẽ phải（右转）、gần（近）、xa（远）。\n\n"
            "现在让我们用这12个词来模拟一次完整的出行体验。"
        ),
        "review_reading_title": "阅读：越南出行记",
        "review_reading_desc": "Sáng nay tôi đi xe máy đến bến xe.",
        "review_reading_text": (
            "Sáng nay tôi đi xe máy đến bến xe. "
            "Tôi mua một vé xe buýt đi trung tâm. "
            "Trên đường, tôi thấy nhiều taxi và xe ôm. "
            "Tài xế nói rẽ trái ở ngã tư lớn. "
            "Sau đó rẽ phải, bến xe rất gần. "
            "Chuyến đi không xa, chỉ mất 30 phút."
        ),
        "review_writing_items": [
            {"prompt": "用 xe máy 和 đường 描述越南的交通。", "targetVocab": "xe máy"},
            {"prompt": "用 bến xe 和 vé 描述一次旅行。", "targetVocab": "bến xe"},
            {"prompt": "用 rẽ trái 和 rẽ phải 给朋友指路。", "targetVocab": "rẽ trái"},
            {"prompt": "用 gần 和 xa 描述两个地方的距离。", "targetVocab": "gần"},
        ],
        "final_reading_title": "阅读：越南交通全景",
        "final_reading_desc": "Giao thông ở Việt Nam rất thú vị.",
        "final_reading_text": (
            "Giao thông ở Việt Nam rất thú vị. Xe máy là vua của đường phố. "
            "Xe buýt ngày càng hiện đại và tiện lợi. "
            "Taxi và xe ôm có mặt ở khắp nơi. "
            "Đường phố Sài Gòn luôn đông đúc, đặc biệt ở các ngã tư lớn. "
            "Bến xe miền Đông là nơi bạn mua vé đi các tỉnh. "
            "Muốn đến chợ Bến Thành, rẽ trái ở đèn đỏ. "
            "Rẽ phải là đường đến nhà thờ Đức Bà. "
            "Chợ rất gần trung tâm, chỉ đi bộ 5 phút. "
            "Sân bay Tân Sơn Nhất không xa trung tâm lắm."
        ),
        "farewell_text": (
            "恭喜你完成了越南城市交通课程！让我们回顾12个词汇。\n\n"
            "Xe máy——摩托车，越南街头的主角。在这个国家，xe máy 不只是交通工具，"
            "它是自由的象征。试着说：Tôi muốn thuê xe máy。\n\n"
            "Xe buýt——公交车，越南城市的动脉。虽然慢，但便宜又能看风景。\n\n"
            "Taxi——出租车，游客最安全的选择。记住用 Grab 叫车更方便。\n\n"
            "Xe ôm——摩的，穿越拥堵的秘密武器。坐上去，抱紧司机，享受风。\n\n"
            "Đường——路。每条 đường 都有自己的故事。Đường Nguyễn Huệ 是步行街。\n\n"
            "Ngã tư——十字路口。越南的 ngã tư 是一场有序的混乱，你会习惯的。\n\n"
            "Bến xe——车站。长途旅行从这里开始。Bến xe miền Đông 去北方。\n\n"
            "Vé——票。一张 vé 就能带你去越南的任何角落。\n\n"
            "Rẽ trái——左转。问路时最常听到的指令之一。\n\n"
            "Rẽ phải——右转。和 rẽ trái 一起记，永远不会迷路。\n\n"
            "Gần——近。越南人说 gần 的时候，可能还要走15分钟。\n\n"
            "Xa——远。如果越南人说 xa，那真的很远。\n\n"
            "你现在拥有了在越南城市里自由穿行的语言工具。"
            "下次当你站在胡志明市的街头，面对潮水般的摩托车时，"
            "你不再是一个不知所措的游客——你是一个知道该怎么走的旅行者。继续前进！"
        ),
    },
    # ===== A2-2: 越南公共交通 (display_order=2) =====
    {
        "series": "A2", "order": 2,
        "title": "越南公共交通",
        "description": (
            "每年有超过1500万游客访问越南，但90%的人从未坐过当地公交车。\n\n"
            "不是因为公交不好——而是因为他们看不懂站牌，听不懂报站，"
            "不知道怎么问司机该在哪里下车。\n\n"
            "这门课程专门解决这个问题。12个精选词汇覆盖了越南公共交通的方方面面，"
            "从火车站到机场，从买票到换乘。\n\n"
            "学完这门课，你将成为那10%能真正融入越南日常生活的旅行者。"
        ),
        "preview_text": (
            "每年有超过1500万游客访问越南，但90%的人从未坐过当地公交车。"
            "不是因为公交不好，而是因为语言障碍。这门课程教你12个公共交通词汇："
            "从ga tàu（火车站）到sân bay（机场），从xe khách（长途客车）到tàu hỏa（火车），"
            "从trạm（站点）到lên xe（上车），从xuống xe（下车）到chuyến（班次），"
            "从giờ（小时）到phút（分钟），从đến（到达）到khởi hành（出发）。"
            "你将通过真实的交通场景学习这些词汇，练习发音，"
            "并模拟真实的出行对话。学完后你将能自信地使用越南公共交通。"
        ),
        "s1_vocab": ["ga tàu", "sân bay", "xe khách", "tàu hỏa", "trạm", "lên xe"],
        "s1_topic": "交通设施",
        "s1_intro_title": "介绍：交通设施",
        "s1_intro_desc": "学习6个越南公共交通设施词汇。",
        "s1_intro_text": (
            "欢迎来到越南公共交通课程！今天学习6个交通设施词汇。\n\n"
            "第一个词是 ga tàu。Ga tàu 是火车站。越南的铁路从河内一直延伸到胡志明市。"
            "你可以说：Ga tàu Sài Gòn ở đâu？意思是「西贡火车站在哪里？」\n\n"
            "第二个词是 sân bay。Sân bay 是机场。越南有三个主要国际机场。"
            "你可以说：Tôi đi sân bay，意思是「我去机场」。\n\n"
            "第三个词是 xe khách。Xe khách 是长途客车。越南的长途客车网络非常发达。"
            "你可以说：Xe khách đi Đà Lạt mấy giờ？意思是「去大叻的客车几点？」\n\n"
            "第四个词是 tàu hỏa。Tàu hỏa 是火车。越南的统一快车从北到南。"
            "你可以说：Tôi muốn đi tàu hỏa，意思是「我想坐火车」。\n\n"
            "第五个词是 trạm。Trạm 是站点，公交站叫 trạm xe buýt。"
            "你可以说：Trạm xe buýt ở đâu？意思是「公交站在哪里？」\n\n"
            "第六个词是 lên xe。Lên xe 是上车。司机会喊 lên xe 让乘客上车。"
            "你可以说：Mời lên xe，意思是「请上车」。\n\n"
            "好的，让我们练习：ga tàu, sân bay, xe khách, tàu hỏa, trạm, lên xe。"
        ),
        "s1_reading_title": "阅读：越南交通设施",
        "s1_reading_desc": "Ga tàu Sài Gòn nằm ở quận 3.",
        "s1_reading_text": (
            "Ga tàu Sài Gòn nằm ở quận 3. "
            "Sân bay Tân Sơn Nhất rất đông khách. "
            "Xe khách đi Đà Lạt mất 8 tiếng. "
            "Tàu hỏa từ Hà Nội đến Huế rất đẹp. "
            "Trạm xe buýt gần khách sạn của tôi. "
            "Tôi lên xe và tìm chỗ ngồi."
        ),
        "s1_writing_items": [
            {"prompt": "用 ga tàu 写一个关于火车站的句子。例句：Ga tàu Hà Nội là ga tàu lớn nhất miền Bắc.", "targetVocab": "ga tàu"},
            {"prompt": "用 sân bay 写一个关于飞行的句子。例句：Sân bay Nội Bài cách trung tâm Hà Nội 30 km.", "targetVocab": "sân bay"},
            {"prompt": "用 xe khách 写一个关于长途旅行的句子。例句：Xe khách giường nằm rất thoải mái.", "targetVocab": "xe khách"},
            {"prompt": "用 tàu hỏa 写一个关于火车旅行的句子。例句：Đi tàu hỏa từ Huế đến Đà Nẵng rất đẹp.", "targetVocab": "tàu hỏa"},
            {"prompt": "用 trạm 写一个关于等车的句子。例句：Tôi đứng ở trạm xe buýt chờ xe số 1.", "targetVocab": "trạm"},
            {"prompt": "用 lên xe 写一个关于乘车的句子。例句：Mọi người lên xe và xe bắt đầu chạy.", "targetVocab": "lên xe"},
        ],
        "s2_vocab": ["xuống xe", "chuyến", "giờ", "phút", "đến", "khởi hành"],
        "s2_topic": "时间与行程",
        "s2_intro_title": "介绍：时间与行程",
        "s2_intro_desc": "学习6个关于时间和行程的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：ga tàu（火车站）、sân bay（机场）、"
            "xe khách（长途客车）、tàu hỏa（火车）、trạm（站点）和 lên xe（上车）。\n\n"
            "今天学习6个关于时间和行程的词汇。\n\n"
            "第一个词是 xuống xe。Xuống xe 是下车，和 lên xe 相反。"
            "你可以说：Tôi muốn xuống xe ở đây，意思是「我想在这里下车」。\n\n"
            "第二个词是 chuyến。Chuyến 是班次、趟。"
            "你可以说：Chuyến xe tiếp theo mấy giờ？意思是「下一班车几点？」\n\n"
            "第三个词是 giờ。Giờ 是小时。越南人用 giờ 来说时间。"
            "比如：Bây giờ là mấy giờ？意思是「现在几点？」\n\n"
            "第四个词是 phút。Phút 是分钟。"
            "你可以说：Còn 10 phút nữa，意思是「还有10分钟」。\n\n"
            "第五个词是 đến。Đến 是到达。"
            "你可以说：Xe đến lúc mấy giờ？意思是「车几点到？」\n\n"
            "第六个词是 khởi hành。Khởi hành 是出发。"
            "你可以说：Xe khởi hành lúc 8 giờ，意思是「车8点出发」。\n\n"
            "好的，让我们练习：xuống xe, chuyến, giờ, phút, đến, khởi hành。"
        ),
        "s2_reading_title": "阅读：旅行时间表",
        "s2_reading_desc": "Chuyến xe khách khởi hành lúc 7 giờ sáng.",
        "s2_reading_text": (
            "Chuyến xe khách khởi hành lúc 7 giờ sáng. "
            "Xe chạy khoảng 5 giờ 30 phút. "
            "Tôi xuống xe ở Đà Lạt lúc trưa. "
            "Chuyến tàu hỏa đến Huế mất 14 giờ. "
            "Xe buýt đến trạm sau 15 phút nữa. "
            "Chuyến bay khởi hành đúng giờ."
        ),
        "s2_writing_items": [
            {"prompt": "用 xuống xe 写一个关于下车的句子。例句：Tôi xuống xe ở trạm gần chợ Bến Thành.", "targetVocab": "xuống xe"},
            {"prompt": "用 chuyến 写一个关于班次的句子。例句：Chuyến xe buýt cuối cùng là lúc 9 giờ tối.", "targetVocab": "chuyến"},
            {"prompt": "用 giờ 写一个关于时间的句子。例句：Bây giờ là 3 giờ chiều, tôi phải đi.", "targetVocab": "giờ"},
            {"prompt": "用 phút 写一个关于等待的句子。例句：Xe buýt đến sau 5 phút nữa.", "targetVocab": "phút"},
            {"prompt": "用 đến 写一个关于到达的句子。例句：Tàu hỏa đến ga Sài Gòn lúc 6 giờ sáng.", "targetVocab": "đến"},
            {"prompt": "用 khởi hành 写一个关于出发的句子。例句：Chuyến bay khởi hành từ sân bay Nội Bài.", "targetVocab": "khởi hành"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南公共交通词汇！\n\n"
            "第一课：ga tàu（火车站）、sân bay（机场）、xe khách（长途客车）、"
            "tàu hỏa（火车）、trạm（站点）、lên xe（上车）。\n\n"
            "第二课：xuống xe（下车）、chuyến（班次）、giờ（小时）、"
            "phút（分钟）、đến（到达）、khởi hành（出发）。\n\n"
            "现在让我们把这些词放在一起，模拟一次完整的旅行。"
        ),
        "review_reading_title": "阅读：一次完整的旅行",
        "review_reading_desc": "Tôi đến ga tàu lúc 6 giờ sáng.",
        "review_reading_text": (
            "Tôi đến ga tàu lúc 6 giờ sáng. "
            "Chuyến tàu hỏa khởi hành lúc 7 giờ. "
            "Tôi lên xe và tìm chỗ ngồi. "
            "Sau 5 giờ 30 phút, tàu đến Đà Nẵng. "
            "Tôi xuống xe ở ga Đà Nẵng. "
            "Từ ga tàu, tôi đi xe khách đến sân bay. "
            "Trạm xe khách rất gần ga tàu."
        ),
        "review_writing_items": [
            {"prompt": "用 ga tàu 和 tàu hỏa 描述一次火车旅行。", "targetVocab": "ga tàu"},
            {"prompt": "用 lên xe 和 xuống xe 描述乘车过程。", "targetVocab": "lên xe"},
            {"prompt": "用 giờ 和 phút 描述旅行时间。", "targetVocab": "giờ"},
            {"prompt": "用 khởi hành 和 đến 描述行程安排。", "targetVocab": "khởi hành"},
        ],
        "final_reading_title": "阅读：越南旅行完整指南",
        "final_reading_desc": "Du lịch Việt Nam rất thuận tiện.",
        "final_reading_text": (
            "Du lịch Việt Nam rất thuận tiện. Ga tàu Sài Gòn có nhiều chuyến đi miền Trung. "
            "Sân bay Tân Sơn Nhất là sân bay lớn nhất phía Nam. "
            "Xe khách giường nằm rất thoải mái cho chuyến đi dài. "
            "Tàu hỏa Thống Nhất chạy từ Bắc vào Nam. "
            "Trạm xe buýt có ở khắp thành phố. "
            "Nhớ lên xe đúng giờ vì xe khởi hành đúng lịch. "
            "Sau vài giờ và vài chục phút, bạn sẽ đến nơi. "
            "Khi đến trạm, nhớ xuống xe cẩn thận."
        ),
        "farewell_text": (
            "恭喜你完成了越南公共交通课程！让我们回顾12个词汇。\n\n"
            "Ga tàu——火车站。越南的火车站充满了旅行的浪漫。"
            "下次你到河内，去 Ga Hà Nội 看看，感受百年历史。\n\n"
            "Sân bay——机场。Sân bay Tân Sơn Nhất 是你越南之旅的起点和终点。\n\n"
            "Xe khách——长途客车。夜间卧铺车是越南旅行的独特体验。\n\n"
            "Tàu hỏa——火车。从河内到胡志明市的统一快车，是一生必坐一次的旅程。\n\n"
            "Trạm——站点。每个 trạm 都是一个新的可能性。\n\n"
            "Lên xe——上车。勇敢地 lên xe，你的冒险就开始了。\n\n"
            "Xuống xe——下车。到站了就大声说 Cho tôi xuống xe。\n\n"
            "Chuyến——班次。提前查好 chuyến，旅行更从容。\n\n"
            "Giờ——小时。越南的时间观念比较灵活，但交通工具通常准时。\n\n"
            "Phút——分钟。每一 phút 都是新的风景。\n\n"
            "Đến——到达。每次 đến 一个新地方，都是一次小小的胜利。\n\n"
            "Khởi hành——出发。最重要的一步永远是 khởi hành。\n\n"
            "你现在拥有了在越南自由旅行的语言工具。"
            "从火车到飞机，从公交到长途车，你都能应对自如。"
            "越南的每一个城市都在等你探索。出发吧！"
        ),
    },
    # ===== A3-1: 越南市场购物 (display_order=1) =====
    {
        "series": "A3", "order": 1,
        "title": "越南市场购物",
        "description": (
            "越南的传统市场是一个充满色彩、声音和气味的世界。\n\n"
            "想象你站在边城市场的入口，面前是成百上千个摊位，"
            "卖家热情地招呼你——而你连「多少钱」都不会说。\n\n"
            "这门课程教你12个在越南市场购物时最实用的词汇。"
            "从讨价还价到选择商品，从付款到找零。\n\n"
            "学完这门课，你将从「被宰的游客」变成「会砍价的行家」。"
        ),
        "preview_text": (
            "越南的传统市场是一个充满色彩、声音和气味的世界。"
            "但如果你不会用越南语购物，你就只能被动接受任何价格。"
            "这门课程教你12个最实用的购物词汇：从chợ（市场）到mua（买），"
            "从bán（卖）到giá（价格），从tiền（钱）到rẻ（便宜），"
            "从đắt（贵）到bao nhiêu（多少），从trả giá（讨价还价）到thử（试），"
            "从size到màu（颜色）。你将通过真实的购物场景学习这些词汇，"
            "练习发音，并模拟真实的讨价还价过程。"
        ),
        "s1_vocab": ["chợ", "mua", "bán", "giá", "tiền", "rẻ"],
        "s1_topic": "市场基础",
        "s1_intro_title": "介绍：越南市场",
        "s1_intro_desc": "学习6个在越南市场最常用的基础词汇。",
        "s1_intro_text": (
            "欢迎来到越南市场购物课程！今天学习6个购物基础词汇。\n\n"
            "第一个词是 chợ。Chợ 是市场。越南的 chợ 是当地生活的中心。"
            "你可以说：Chợ Bến Thành ở đâu？意思是「边城市场在哪里？」\n\n"
            "第二个词是 mua。Mua 是买。这是购物时最基本的词。"
            "你可以说：Tôi muốn mua cái này，意思是「我想买这个」。\n\n"
            "第三个词是 bán。Bán 是卖，和 mua 相反。"
            "你会听到卖家说：Tôi bán rẻ cho bạn，意思是「我便宜卖给你」。\n\n"
            "第四个词是 giá。Giá 是价格。问价格是购物的第一步。"
            "你可以说：Giá bao nhiêu？意思是「多少钱？」\n\n"
            "第五个词是 tiền。Tiền 是钱。越南的货币是越南盾。"
            "你可以说：Tôi không có đủ tiền，意思是「我没有足够的钱」。\n\n"
            "第六个词是 rẻ。Rẻ 是便宜的。在市场里，你总想找到 rẻ 的东西。"
            "你可以说：Rẻ hơn được không？意思是「能便宜点吗？」\n\n"
            "好的，让我们练习：chợ, mua, bán, giá, tiền, rẻ。"
        ),
        "s1_reading_title": "阅读：在越南市场",
        "s1_reading_desc": "Chợ Bến Thành là chợ nổi tiếng nhất Sài Gòn.",
        "s1_reading_text": (
            "Chợ Bến Thành là chợ nổi tiếng nhất Sài Gòn. "
            "Tôi muốn mua một chiếc áo. "
            "Người bán nói giá rất cao. "
            "Tôi hỏi có rẻ hơn không. "
            "Cuối cùng tôi mua được với giá tốt. "
            "Tôi trả tiền và rất vui."
        ),
        "s1_writing_items": [
            {"prompt": "用 chợ 写一个关于越南市场的句子。例句：Chợ Bến Thành mở cửa từ sáng sớm.", "targetVocab": "chợ"},
            {"prompt": "用 mua 写一个关于购物的句子。例句：Tôi mua trái cây ở chợ mỗi ngày.", "targetVocab": "mua"},
            {"prompt": "用 bán 写一个关于卖家的句子。例句：Bà ấy bán hoa ở chợ đã 20 năm.", "targetVocab": "bán"},
            {"prompt": "用 giá 写一个关于价格的句子。例句：Giá trái cây ở chợ rẻ hơn siêu thị.", "targetVocab": "giá"},
            {"prompt": "用 tiền 写一个关于付款的句子。例句：Tôi trả tiền bằng tiền mặt.", "targetVocab": "tiền"},
            {"prompt": "用 rẻ 写一个关于便宜货的句子。例句：Áo này rẻ quá, chỉ có 50 nghìn đồng.", "targetVocab": "rẻ"},
        ],
        "s2_vocab": ["đắt", "bao nhiêu", "trả giá", "thử", "size", "màu"],
        "s2_topic": "讨价还价",
        "s2_intro_title": "介绍：讨价还价",
        "s2_intro_desc": "学习6个讨价还价和选购商品的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：chợ（市场）、mua（买）、bán（卖）、"
            "giá（价格）、tiền（钱）和 rẻ（便宜）。\n\n"
            "今天学习6个帮你在市场里更自如的词汇。\n\n"
            "第一个词是 đắt。Đắt 是贵的，和 rẻ 相反。"
            "你可以说：Đắt quá！意思是「太贵了！」这是砍价的第一步。\n\n"
            "第二个词是 bao nhiêu。Bao nhiêu 是多少。"
            "你可以说：Cái này bao nhiêu tiền？意思是「这个多少钱？」\n\n"
            "第三个词是 trả giá。Trả giá 是讨价还价。在越南市场，trả giá 是一种文化。"
            "你可以说：Tôi muốn trả giá，意思是「我想砍价」。\n\n"
            "第四个词是 thử。Thử 是试。买衣服时你需要试穿。"
            "你可以说：Tôi muốn thử cái này，意思是「我想试试这个」。\n\n"
            "第五个词是 size。Size 在越南语中和英语一样，就是尺码。"
            "你可以说：Có size lớn hơn không？意思是「有大一号的吗？」\n\n"
            "第六个词是 màu。Màu 是颜色。"
            "你可以说：Có màu khác không？意思是「有其他颜色吗？」\n\n"
            "好的，让我们练习：đắt, bao nhiêu, trả giá, thử, size, màu。"
        ),
        "s2_reading_title": "阅读：讨价还价",
        "s2_reading_desc": "Tôi đi chợ mua quần áo.",
        "s2_reading_text": (
            "Tôi đi chợ mua quần áo. "
            "Tôi hỏi cái áo bao nhiêu tiền. "
            "Người bán nói giá rất đắt. "
            "Tôi bắt đầu trả giá. "
            "Tôi muốn thử cái áo trước khi mua. "
            "Tôi chọn size vừa và màu xanh."
        ),
        "s2_writing_items": [
            {"prompt": "用 đắt 写一个关于价格的句子。例句：Hàng hiệu rất đắt nhưng chất lượng tốt.", "targetVocab": "đắt"},
            {"prompt": "用 bao nhiêu 写一个关于问价的句子。例句：Bao nhiêu tiền một ký xoài?", "targetVocab": "bao nhiêu"},
            {"prompt": "用 trả giá 写一个关于砍价的句子。例句：Ở chợ Việt Nam, bạn nên trả giá.", "targetVocab": "trả giá"},
            {"prompt": "用 thử 写一个关于试穿的句子。例句：Tôi muốn thử đôi giày này trước.", "targetVocab": "thử"},
            {"prompt": "用 size 写一个关于尺码的句子。例句：Size này hơi nhỏ, cho tôi size lớn hơn.", "targetVocab": "size"},
            {"prompt": "用 màu 写一个关于颜色的句子。例句：Tôi thích màu đỏ hơn màu xanh.", "targetVocab": "màu"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南购物词汇！\n\n"
            "第一课：chợ（市场）、mua（买）、bán（卖）、"
            "giá（价格）、tiền（钱）、rẻ（便宜）。\n\n"
            "第二课：đắt（贵）、bao nhiêu（多少）、trả giá（讨价还价）、"
            "thử（试）、size（尺码）、màu（颜色）。\n\n"
            "现在让我们模拟一次完整的购物体验。"
        ),
        "review_reading_title": "阅读：完整的购物体验",
        "review_reading_desc": "Hôm nay tôi đi chợ Bến Thành.",
        "review_reading_text": (
            "Hôm nay tôi đi chợ Bến Thành. "
            "Tôi muốn mua một chiếc áo dài. "
            "Người bán nói giá 500 nghìn đồng. "
            "Tôi nói đắt quá và bắt đầu trả giá. "
            "Tôi hỏi bao nhiêu nếu mua hai cái. "
            "Tôi thử cái áo, chọn size vừa và màu hồng. "
            "Cuối cùng giá rẻ hơn nhiều. "
            "Tôi trả tiền và rất hài lòng."
        ),
        "review_writing_items": [
            {"prompt": "用 chợ 和 mua 描述一次购物经历。", "targetVocab": "chợ"},
            {"prompt": "用 đắt 和 rẻ 比较两个商品的价格。", "targetVocab": "đắt"},
            {"prompt": "用 trả giá 和 bao nhiêu 描述砍价过程。", "targetVocab": "trả giá"},
            {"prompt": "用 thử 和 size 描述试穿衣服。", "targetVocab": "thử"},
        ],
        "final_reading_title": "阅读：越南购物完整指南",
        "final_reading_desc": "Mua sắm ở Việt Nam là một trải nghiệm thú vị.",
        "final_reading_text": (
            "Mua sắm ở Việt Nam là một trải nghiệm thú vị. "
            "Chợ truyền thống là nơi tốt nhất để mua đồ. "
            "Người bán hàng rất thân thiện. "
            "Giá ở chợ thường rẻ hơn cửa hàng. "
            "Nhưng bạn cần biết trả giá. "
            "Hỏi bao nhiêu tiền trước khi mua. "
            "Nếu đắt quá, hãy đi chỗ khác. "
            "Nhớ thử trước khi mua quần áo. "
            "Chọn đúng size và màu yêu thích. "
            "Trả tiền xong, nhớ kiểm tra lại hàng."
        ),
        "farewell_text": (
            "恭喜你完成了越南市场购物课程！让我们回顾12个词汇。\n\n"
            "Chợ——市场，越南生活的心脏。每个 chợ 都有自己的个性和故事。"
            "Chợ Bến Thành 是游客必去的地方。\n\n"
            "Mua——买。Tôi muốn mua cái này 是你在市场里说得最多的话。\n\n"
            "Bán——卖。理解卖家的语言，你就能更好地砍价。\n\n"
            "Giá——价格。永远先问 giá，再决定买不买。\n\n"
            "Tiền——钱。在越南，现金仍然是王道。记得带够 tiền。\n\n"
            "Rẻ——便宜。Rẻ hơn được không？这句话能帮你省很多钱。\n\n"
            "Đắt——贵。Đắt quá！是砍价的起手式。大胆说出来。\n\n"
            "Bao nhiêu——多少。Bao nhiêu tiền？是你在越南最常问的问题。\n\n"
            "Trả giá——讨价还价。在越南市场，不 trả giá 就是在浪费钱。\n\n"
            "Thử——试。买之前一定要 thử，特别是衣服和鞋子。\n\n"
            "Size——尺码。越南的 size 可能和你习惯的不同，一定要试。\n\n"
            "Màu——颜色。越南的商品颜色丰富，总有你喜欢的 màu。\n\n"
            "你现在拥有了在越南市场自如购物的语言工具。"
            "下次走进越南的市场，你将是那个自信砍价的行家。购物愉快！"
        ),
    },
    # ===== A3-2: 越南银行与服务 (display_order=2) =====
    {
        "series": "A3", "order": 2,
        "title": "越南银行与服务",
        "description": (
            "在越南生活，你迟早要和银行、邮局、手机店打交道。\n\n"
            "这些日常服务场景看似简单，但如果你不会说「开户」「汇款」「充值」，"
            "每一次办事都会变成一场漫长的手语表演。\n\n"
            "这门课程教你12个最实用的服务场景词汇，"
            "让你在越南的日常生活中不再依赖翻译软件。\n\n"
            "从银行到邮局，从手机到网络——用越南语搞定一切。"
        ),
        "preview_text": (
            "在越南生活，你迟早要和银行、邮局、手机店打交道。"
            "这门课程教你12个最实用的服务场景词汇："
            "从ngân hàng（银行）到tài khoản（账户），从gửi tiền（存钱）到rút tiền（取钱），"
            "从chuyển tiền（转账）到thẻ（卡），从bưu điện（邮局）到gửi（寄），"
            "从điện thoại（电话）到wifi到sim到nạp tiền（充值）。"
            "你将通过真实的服务场景学习这些词汇，练习发音，"
            "并模拟真实的办事对话。学完后你将能自信地处理越南的日常事务。"
        ),
        "s1_vocab": ["ngân hàng", "tài khoản", "gửi tiền", "rút tiền", "chuyển tiền", "thẻ"],
        "s1_topic": "银行服务",
        "s1_intro_title": "介绍：越南银行",
        "s1_intro_desc": "学习6个在越南银行最常用的词汇。",
        "s1_intro_text": (
            "欢迎来到越南银行与服务课程！今天学习6个银行词汇。\n\n"
            "第一个词是 ngân hàng。Ngân hàng 是银行。越南有很多银行。"
            "你可以说：Ngân hàng gần đây ở đâu？意思是「附近的银行在哪里？」\n\n"
            "第二个词是 tài khoản。Tài khoản 是账户。在越南开银行账户很方便。"
            "你可以说：Tôi muốn mở tài khoản，意思是「我想开户」。\n\n"
            "第三个词是 gửi tiền。Gửi tiền 是存钱。"
            "你可以说：Tôi muốn gửi tiền，意思是「我想存钱」。\n\n"
            "第四个词是 rút tiền。Rút tiền 是取钱，和 gửi tiền 相反。"
            "你可以说：Tôi muốn rút tiền，意思是「我想取钱」。\n\n"
            "第五个词是 chuyển tiền。Chuyển tiền 是转账。"
            "你可以说：Tôi muốn chuyển tiền，意思是「我想转账」。\n\n"
            "第六个词是 thẻ。Thẻ 是卡，银行卡叫 thẻ ngân hàng。"
            "你可以说：Thẻ của tôi bị khóa，意思是「我的卡被锁了」。\n\n"
            "好的，让我们练习：ngân hàng, tài khoản, gửi tiền, rút tiền, chuyển tiền, thẻ。"
        ),
        "s1_reading_title": "阅读：在越南银行",
        "s1_reading_desc": "Tôi đến ngân hàng để mở tài khoản.",
        "s1_reading_text": (
            "Tôi đến ngân hàng để mở tài khoản. "
            "Nhân viên giúp tôi điền đơn. "
            "Tôi gửi tiền vào tài khoản mới. "
            "Hôm sau tôi rút tiền ở máy ATM. "
            "Tôi cũng chuyển tiền cho bạn. "
            "Thẻ ngân hàng rất tiện lợi."
        ),
        "s1_writing_items": [
            {"prompt": "用 ngân hàng 写一个关于银行的句子。例句：Ngân hàng Vietcombank là ngân hàng lớn nhất Việt Nam.", "targetVocab": "ngân hàng"},
            {"prompt": "用 tài khoản 写一个关于开户的句子。例句：Mở tài khoản ngân hàng ở Việt Nam rất dễ.", "targetVocab": "tài khoản"},
            {"prompt": "用 gửi tiền 写一个关于存钱的句子。例句：Tôi gửi tiền vào ngân hàng mỗi tháng.", "targetVocab": "gửi tiền"},
            {"prompt": "用 rút tiền 写一个关于取钱的句子。例句：Tôi rút tiền ở máy ATM gần nhà.", "targetVocab": "rút tiền"},
            {"prompt": "用 chuyển tiền 写一个关于转账的句子。例句：Tôi chuyển tiền qua ứng dụng ngân hàng.", "targetVocab": "chuyển tiền"},
            {"prompt": "用 thẻ 写一个关于银行卡的句子。例句：Thẻ ngân hàng có thể dùng ở mọi cửa hàng.", "targetVocab": "thẻ"},
        ],
        "s2_vocab": ["bưu điện", "gửi", "điện thoại", "wifi", "sim", "nạp tiền"],
        "s2_topic": "邮局与通讯",
        "s2_intro_title": "介绍：邮局与通讯",
        "s2_intro_desc": "学习6个关于邮局和通讯的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：ngân hàng（银行）、tài khoản（账户）、"
            "gửi tiền（存钱）、rút tiền（取钱）、chuyển tiền（转账）和 thẻ（卡）。\n\n"
            "今天学习6个关于邮局和通讯的词汇。\n\n"
            "第一个词是 bưu điện。Bưu điện 是邮局。越南的邮局也提供快递服务。"
            "你可以说：Bưu điện ở đâu？意思是「邮局在哪里？」\n\n"
            "第二个词是 gửi。Gửi 是寄。寄信、寄包裹都用这个词。"
            "你可以说：Tôi muốn gửi thư，意思是「我想寄信」。\n\n"
            "第三个词是 điện thoại。Điện thoại 是电话、手机。"
            "你可以说：Số điện thoại của bạn là gì？意思是「你的电话号码是什么？」\n\n"
            "第四个词是 wifi。Wifi 在越南到处都有，咖啡店、餐厅都免费提供。"
            "你可以说：Wifi password là gì？意思是「wifi密码是什么？」\n\n"
            "第五个词是 sim。Sim 是手机SIM卡。在越南买 sim 卡很便宜。"
            "你可以说：Tôi muốn mua sim，意思是「我想买SIM卡」。\n\n"
            "第六个词是 nạp tiền。Nạp tiền 是充值。手机话费需要定期充值。"
            "你可以说：Tôi muốn nạp tiền điện thoại，意思是「我想给手机充值」。\n\n"
            "好的，让我们练习：bưu điện, gửi, điện thoại, wifi, sim, nạp tiền。"
        ),
        "s2_reading_title": "阅读：日常服务",
        "s2_reading_desc": "Tôi đến bưu điện để gửi một gói hàng.",
        "s2_reading_text": (
            "Tôi đến bưu điện để gửi một gói hàng. "
            "Sau đó tôi đi mua sim điện thoại mới. "
            "Cửa hàng có wifi miễn phí. "
            "Tôi nạp tiền cho sim mới. "
            "Bây giờ điện thoại của tôi có thể gọi được. "
            "Tôi gửi tin nhắn cho bạn bè."
        ),
        "s2_writing_items": [
            {"prompt": "用 bưu điện 写一个关于寄东西的句子。例句：Bưu điện trung tâm Sài Gòn rất đẹp.", "targetVocab": "bưu điện"},
            {"prompt": "用 gửi 写一个关于寄信的句子。例句：Tôi gửi bưu thiếp cho gia đình ở Trung Quốc.", "targetVocab": "gửi"},
            {"prompt": "用 điện thoại 写一个关于手机的句子。例句：Điện thoại di động rất quan trọng khi du lịch.", "targetVocab": "điện thoại"},
            {"prompt": "用 wifi 写一个关于上网的句子。例句：Quán cà phê này có wifi miễn phí rất nhanh.", "targetVocab": "wifi"},
            {"prompt": "用 sim 写一个关于SIM卡的句子。例句：Mua sim du lịch ở sân bay rất tiện.", "targetVocab": "sim"},
            {"prompt": "用 nạp tiền 写一个关于充值的句子。例句：Tôi nạp tiền điện thoại ở cửa hàng tiện lợi.", "targetVocab": "nạp tiền"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南服务场景词汇！\n\n"
            "第一课：ngân hàng（银行）、tài khoản（账户）、gửi tiền（存钱）、"
            "rút tiền（取钱）、chuyển tiền（转账）、thẻ（卡）。\n\n"
            "第二课：bưu điện（邮局）、gửi（寄）、điện thoại（电话）、"
            "wifi、sim（SIM卡）、nạp tiền（充值）。\n\n"
            "现在让我们综合练习这12个词汇。"
        ),
        "review_reading_title": "阅读：越南日常事务",
        "review_reading_desc": "Sáng nay tôi đi ngân hàng rút tiền.",
        "review_reading_text": (
            "Sáng nay tôi đi ngân hàng rút tiền bằng thẻ. "
            "Sau đó tôi chuyển tiền cho chủ nhà. "
            "Tôi kiểm tra tài khoản và gửi tiền tiết kiệm. "
            "Buổi chiều tôi đến bưu điện gửi hàng. "
            "Tôi cũng mua sim mới cho điện thoại. "
            "Quán cà phê gần đó có wifi miễn phí. "
            "Tôi nạp tiền cho sim và gọi điện về nhà."
        ),
        "review_writing_items": [
            {"prompt": "用 ngân hàng 和 thẻ 描述一次银行体验。", "targetVocab": "ngân hàng"},
            {"prompt": "用 gửi tiền 和 rút tiền 描述你的理财习惯。", "targetVocab": "gửi tiền"},
            {"prompt": "用 bưu điện 和 gửi 描述寄包裹的过程。", "targetVocab": "bưu điện"},
            {"prompt": "用 sim 和 nạp tiền 描述买手机卡的经历。", "targetVocab": "sim"},
        ],
        "final_reading_title": "阅读：越南生活服务指南",
        "final_reading_desc": "Sống ở Việt Nam cần biết một số dịch vụ cơ bản.",
        "final_reading_text": (
            "Sống ở Việt Nam cần biết một số dịch vụ cơ bản. "
            "Ngân hàng mở cửa từ thứ Hai đến thứ Sáu. "
            "Mở tài khoản cần hộ chiếu và visa. "
            "Bạn có thể gửi tiền và rút tiền ở máy ATM. "
            "Chuyển tiền qua app rất nhanh và tiện. "
            "Thẻ ngân hàng dùng được ở hầu hết cửa hàng. "
            "Bưu điện gửi hàng đi quốc tế rất rẻ. "
            "Mua sim điện thoại ở sân bay hoặc cửa hàng. "
            "Wifi có ở khắp nơi, từ quán cà phê đến khách sạn. "
            "Nhớ nạp tiền cho sim để luôn có liên lạc."
        ),
        "farewell_text": (
            "恭喜你完成了越南银行与服务课程！让我们回顾12个词汇。\n\n"
            "Ngân hàng——银行。越南的银行系统现代化程度很高。"
            "Vietcombank 和 Techcombank 是最常见的。\n\n"
            "Tài khoản——账户。有了 tài khoản，你在越南的生活会方便很多。\n\n"
            "Gửi tiền——存钱。定期 gửi tiền 是好习惯。\n\n"
            "Rút tiền——取钱。ATM 到处都有，rút tiền 很方便。\n\n"
            "Chuyển tiền——转账。手机银行让 chuyển tiền 变得超级简单。\n\n"
            "Thẻ——卡。一张 thẻ 在手，走遍越南不愁。\n\n"
            "Bưu điện——邮局。胡志明市的中央 bưu điện 本身就是一个景点。\n\n"
            "Gửi——寄。给家人 gửi 一张明信片，是旅行最温暖的记忆。\n\n"
            "Điện thoại——电话。在越南，điện thoại 是你最重要的工具。\n\n"
            "Wifi——无线网络。越南的 wifi 覆盖率让很多发达国家都羡慕。\n\n"
            "Sim——SIM卡。到越南第一件事就是买一张本地 sim。\n\n"
            "Nạp tiền——充值。记得定期 nạp tiền，保持通讯畅通。\n\n"
            "你现在拥有了在越南处理日常事务的语言工具。"
            "从银行到邮局，从手机到网络，你都能用越南语搞定。继续加油！"
        ),
    },
    # ===== A4-1: 越南称呼系统 (display_order=1) =====
    {
        "series": "A4", "order": 1,
        "title": "越南称呼系统",
        "description": (
            "越南语的称呼系统可能是世界上最复杂的之一——"
            "用错一个称谓就可能让对方觉得你不尊重他。\n\n"
            "在越南，你不能简单地用「你」来称呼所有人。"
            "年龄、性别、关系都决定了你该用哪个词。\n\n"
            "这门课程教你12个最基本的越南称呼和社交词汇，"
            "帮你在越南的人际交往中不再犯尴尬的错误。\n\n"
            "掌握这些词汇，你就掌握了越南社交的入场券。"
        ),
        "preview_text": (
            "越南语的称呼系统可能是世界上最复杂的之一。"
            "用错一个称谓就可能让对方觉得你不尊重他。"
            "这门课程教你12个最基本的越南称呼和社交词汇："
            "从anh（哥/你）到chị（姐/你），从em（弟妹/我）到bạn（朋友），"
            "从ông（爷爷/先生）到bà（奶奶/女士），从xin chào（你好）到cảm ơn（谢谢），"
            "从xin lỗi（对不起）到tạm biệt（再见），从vâng（是）到không（不）。"
            "你将通过真实的社交场景学习这些词汇，练习发音，"
            "并模拟真实的越南社交对话。"
        ),
        "s1_vocab": ["anh", "chị", "em", "bạn", "ông", "bà"],
        "s1_topic": "称呼词汇",
        "s1_intro_title": "介绍：越南称呼",
        "s1_intro_desc": "学习6个越南最基本的称呼词汇。",
        "s1_intro_text": (
            "欢迎来到越南称呼系统课程！今天学习6个最基本的称呼词汇。\n\n"
            "第一个词是 anh。Anh 用来称呼比你大的男性，相当于「哥哥」。"
            "在越南，对年轻男性说 anh 是最安全的选择。"
            "比如：Anh ơi，意思是「哥，请问一下」。\n\n"
            "第二个词是 chị。Chị 用来称呼比你大的女性，相当于「姐姐」。"
            "你可以说：Chị ơi，意思是「姐，请问一下」。\n\n"
            "第三个词是 em。Em 用来称呼比你小的人，不分男女。"
            "也可以用来自称，表示谦虚。比如：Em cảm ơn anh，意思是「谢谢哥」。\n\n"
            "第四个词是 bạn。Bạn 是朋友，也是同龄人之间的称呼。"
            "你可以说：Bạn tên gì？意思是「你叫什么名字？」\n\n"
            "第五个词是 ông。Ông 用来称呼年长的男性，相当于「爷爷」或「先生」。"
            "你可以说：Ông ơi，意思是「老先生，请问」。\n\n"
            "第六个词是 bà。Bà 用来称呼年长的女性，相当于「奶奶」或「女士」。"
            "你可以说：Bà ơi，意思是「老太太，请问」。\n\n"
            "好的，让我们练习：anh, chị, em, bạn, ông, bà。"
        ),
        "s1_reading_title": "阅读：越南的称呼",
        "s1_reading_desc": "Ở Việt Nam, cách gọi rất quan trọng.",
        "s1_reading_text": (
            "Ở Việt Nam, cách gọi rất quan trọng. "
            "Gọi anh khi nói với nam giới lớn tuổi hơn. "
            "Gọi chị khi nói với nữ giới lớn tuổi hơn. "
            "Em là cách gọi người nhỏ tuổi hơn. "
            "Bạn bè đồng tuổi gọi nhau là bạn. "
            "Ông và bà là cách gọi người lớn tuổi."
        ),
        "s1_writing_items": [
            {"prompt": "用 anh 写一个关于问路的句子。例句：Anh ơi, đường đến chợ Bến Thành đi thế nào?", "targetVocab": "anh"},
            {"prompt": "用 chị 写一个关于点餐的句子。例句：Chị ơi, cho tôi một tô phở bò.", "targetVocab": "chị"},
            {"prompt": "用 em 写一个关于自我介绍的句子。例句：Em là sinh viên, em đến từ Trung Quốc.", "targetVocab": "em"},
            {"prompt": "用 bạn 写一个关于交朋友的句子。例句：Bạn có muốn đi uống cà phê không?", "targetVocab": "bạn"},
            {"prompt": "用 ông 写一个关于尊敬长辈的句子。例句：Ông ơi, ông có khỏe không?", "targetVocab": "ông"},
            {"prompt": "用 bà 写一个关于问候的句子。例句：Bà ơi, bà bán cái này bao nhiêu?", "targetVocab": "bà"},
        ],
        "s2_vocab": ["xin chào", "cảm ơn", "xin lỗi", "tạm biệt", "vâng", "không"],
        "s2_topic": "基础社交用语",
        "s2_intro_title": "介绍：社交用语",
        "s2_intro_desc": "学习6个越南最基本的社交用语。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：anh（哥）、chị（姐）、em（弟妹）、"
            "bạn（朋友）、ông（爷爷/先生）和 bà（奶奶/女士）。\n\n"
            "今天学习6个最基本的社交用语。\n\n"
            "第一个词是 xin chào。Xin chào 是你好，最正式的问候语。"
            "你可以说：Xin chào anh，意思是「你好，哥」。\n\n"
            "第二个词是 cảm ơn。Cảm ơn 是谢谢。"
            "你可以说：Cảm ơn chị，意思是「谢谢姐」。\n\n"
            "第三个词是 xin lỗi。Xin lỗi 是对不起。"
            "你可以说：Xin lỗi, tôi không hiểu，意思是「对不起，我不懂」。\n\n"
            "第四个词是 tạm biệt。Tạm biệt 是再见。"
            "你可以说：Tạm biệt, hẹn gặp lại，意思是「再见，下次见」。\n\n"
            "第五个词是 vâng。Vâng 是「是的」，表示同意或确认。"
            "比如别人问你要不要喝水，你说：Vâng，意思是「好的」。\n\n"
            "第六个词是 không。Không 是「不」，表示否定。"
            "你可以说：Không, cảm ơn，意思是「不用了，谢谢」。\n\n"
            "好的，让我们练习：xin chào, cảm ơn, xin lỗi, tạm biệt, vâng, không。"
        ),
        "s2_reading_title": "阅读：越南社交礼仪",
        "s2_reading_desc": "Khi gặp ai, hãy nói xin chào.",
        "s2_reading_text": (
            "Khi gặp ai, hãy nói xin chào. "
            "Khi được giúp đỡ, nói cảm ơn. "
            "Khi làm sai, nói xin lỗi. "
            "Khi chia tay, nói tạm biệt. "
            "Khi đồng ý, nói vâng. "
            "Khi từ chối, nói không một cách lịch sự."
        ),
        "s2_writing_items": [
            {"prompt": "用 xin chào 写一个关于问候的句子。例句：Xin chào, tôi là Minh, rất vui được gặp bạn.", "targetVocab": "xin chào"},
            {"prompt": "用 cảm ơn 写一个关于感谢的句子。例句：Cảm ơn anh đã giúp tôi tìm đường.", "targetVocab": "cảm ơn"},
            {"prompt": "用 xin lỗi 写一个关于道歉的句子。例句：Xin lỗi, tôi đến muộn vì kẹt xe.", "targetVocab": "xin lỗi"},
            {"prompt": "用 tạm biệt 写一个关于告别的句子。例句：Tạm biệt bạn, chúc bạn một ngày vui.", "targetVocab": "tạm biệt"},
            {"prompt": "用 vâng 写一个关于同意的句子。例句：Vâng, tôi sẽ đến đúng giờ.", "targetVocab": "vâng"},
            {"prompt": "用 không 写一个关于拒绝的句子。例句：Không, tôi không ăn cay được.", "targetVocab": "không"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南社交词汇！\n\n"
            "第一课：anh（哥）、chị（姐）、em（弟妹）、"
            "bạn（朋友）、ông（先生）、bà（女士）。\n\n"
            "第二课：xin chào（你好）、cảm ơn（谢谢）、xin lỗi（对不起）、"
            "tạm biệt（再见）、vâng（是）、không（不）。\n\n"
            "现在让我们综合练习这12个词汇。"
        ),
        "review_reading_title": "阅读：一次越南社交",
        "review_reading_desc": "Tôi gặp một người bạn mới ở quán cà phê.",
        "review_reading_text": (
            "Tôi gặp một người bạn mới ở quán cà phê. "
            "Tôi nói xin chào với anh ấy. "
            "Chị phục vụ hỏi tôi muốn uống gì. "
            "Tôi nói vâng, cho em một ly cà phê. "
            "Bạn tôi mời tôi ăn bánh. Tôi nói cảm ơn. "
            "Ông chủ quán rất thân thiện. "
            "Bà bán hàng bên cạnh cũng chào tôi. "
            "Khi về, tôi nói tạm biệt. "
            "Bạn hỏi ngày mai gặp lại không. Tôi không từ chối. "
            "Tôi xin lỗi vì phải đi sớm."
        ),
        "review_writing_items": [
            {"prompt": "用 anh 和 xin chào 描述一次问候。", "targetVocab": "anh"},
            {"prompt": "用 cảm ơn 和 xin lỗi 描述一次社交场景。", "targetVocab": "cảm ơn"},
            {"prompt": "用 vâng 和 không 描述一次对话。", "targetVocab": "vâng"},
            {"prompt": "用 tạm biệt 和 bạn 描述告别场景。", "targetVocab": "tạm biệt"},
        ],
        "final_reading_title": "阅读：越南社交完整指南",
        "final_reading_desc": "Người Việt Nam rất thân thiện.",
        "final_reading_text": (
            "Người Việt Nam rất thân thiện. Khi gặp nhau, họ nói xin chào. "
            "Gọi anh hoặc chị là cách lịch sự nhất. "
            "Em là cách gọi người nhỏ tuổi hơn mình. "
            "Bạn bè thân gọi nhau là bạn. "
            "Với người lớn tuổi, gọi ông hoặc bà. "
            "Luôn nói cảm ơn khi được giúp đỡ. "
            "Nói xin lỗi khi làm phiền ai. "
            "Khi đồng ý, nói vâng. Khi từ chối, nói không lịch sự. "
            "Khi chia tay, nói tạm biệt với nụ cười."
        ),
        "farewell_text": (
            "恭喜你完成了越南称呼系统课程！让我们回顾12个词汇。\n\n"
            "Anh——哥，对年长男性的称呼。在越南，一声 anh ơi 能打开很多扇门。\n\n"
            "Chị——姐，对年长女性的称呼。Chị ơi 是你在餐厅、商店最常用的开场白。\n\n"
            "Em——弟妹，对年幼者的称呼。用 em 自称显得谦虚有礼。\n\n"
            "Bạn——朋友。在越南交到一个 bạn，你就多了一个家。\n\n"
            "Ông——爷爷/先生。对年长男性的尊称，体现你的教养。\n\n"
            "Bà——奶奶/女士。对年长女性的尊称，温暖而尊重。\n\n"
            "Xin chào——你好。简单的两个字，却是所有关系的起点。\n\n"
            "Cảm ơn——谢谢。越南人重视感恩，多说 cảm ơn 永远不会错。\n\n"
            "Xin lỗi——对不起。犯错不可怕，一句 xin lỗi 就能化解尴尬。\n\n"
            "Tạm biệt——再见。每一次 tạm biệt 都是下一次相遇的开始。\n\n"
            "Vâng——是的。简短有力，表示你在认真倾听。\n\n"
            "Không——不。学会说 không 和学会说 vâng 一样重要。\n\n"
            "你现在拥有了在越南社交的基本语言工具。"
            "记住，越南人非常看重礼貌和称呼。"
            "用对了称呼，你就赢得了他们的尊重和友谊。祝你交到很多越南朋友！"
        ),
    },
    # ===== A4-2: 越南家庭与亲属 (display_order=2) =====
    {
        "series": "A4", "order": 2,
        "title": "越南家庭与亲属",
        "description": (
            "在越南文化中，家庭是一切的核心。\n\n"
            "越南人见面第一个问题往往是「你家有几口人？」"
            "如果你连「爸爸」「妈妈」都不会说，这段对话就无法继续。\n\n"
            "这门课程教你12个最基本的家庭和亲属词汇，"
            "帮你在越南的社交场合中自如地谈论家庭话题。\n\n"
            "家庭是越南人最看重的话题——学会这些词，你就能走进他们的心。"
        ),
        "preview_text": (
            "在越南文化中，家庭是一切的核心。越南人见面第一个问题往往是你家有几口人。"
            "这门课程教你12个最基本的家庭词汇："
            "从bố（爸爸）到mẹ（妈妈），从con（孩子）到anh em（兄弟姐妹），"
            "从gia đình（家庭）到nhà（家），从vợ（妻子）到chồng（丈夫），"
            "从con trai（儿子）到con gái（女儿），从cháu（孙子）到họ hàng（亲戚）。"
            "你将通过真实的家庭对话场景学习这些词汇。"
        ),
        "s1_vocab": ["bố", "mẹ", "con", "anh em", "gia đình", "nhà"],
        "s1_topic": "家庭基础",
        "s1_intro_title": "介绍：越南家庭",
        "s1_intro_desc": "学习6个越南家庭的基础词汇。",
        "s1_intro_text": (
            "欢迎来到越南家庭与亲属课程！今天学习6个家庭基础词汇。\n\n"
            "第一个词是 bố。Bố 是爸爸，北方用 bố，南方用 ba。"
            "你可以说：Bố tôi là giáo viên，意思是「我爸爸是老师」。\n\n"
            "第二个词是 mẹ。Mẹ 是妈妈，南方也说 má。"
            "你可以说：Mẹ tôi nấu ăn rất ngon，意思是「我妈妈做饭很好吃」。\n\n"
            "第三个词是 con。Con 是孩子，也是子女对父母的自称。"
            "你可以说：Tôi có hai con，意思是「我有两个孩子」。\n\n"
            "第四个词是 anh em。Anh em 是兄弟姐妹的统称。"
            "你可以说：Tôi có ba anh em，意思是「我有三个兄弟姐妹」。\n\n"
            "第五个词是 gia đình。Gia đình 是家庭。"
            "你可以说：Gia đình tôi có 4 người，意思是「我家有4口人」。\n\n"
            "第六个词是 nhà。Nhà 是家、房子。"
            "你可以说：Nhà tôi ở Hà Nội，意思是「我家在河内」。\n\n"
            "好的，让我们练习：bố, mẹ, con, anh em, gia đình, nhà。"
        ),
        "s1_reading_title": "阅读：越南家庭",
        "s1_reading_desc": "Gia đình tôi có bốn người.",
        "s1_reading_text": (
            "Gia đình tôi có bốn người. "
            "Bố tôi làm việc ở công ty. "
            "Mẹ tôi là bác sĩ. "
            "Tôi có một con trai nhỏ. "
            "Anh em tôi sống ở các thành phố khác nhau. "
            "Nhà tôi ở gần trung tâm Sài Gòn."
        ),
        "s1_writing_items": [
            {"prompt": "用 bố 写一个关于你父亲的句子。例句：Bố tôi thích đọc báo mỗi sáng.", "targetVocab": "bố"},
            {"prompt": "用 mẹ 写一个关于你母亲的句子。例句：Mẹ tôi nấu phở ngon nhất.", "targetVocab": "mẹ"},
            {"prompt": "用 con 写一个关于孩子的句子。例句：Con tôi đang học lớp 3.", "targetVocab": "con"},
            {"prompt": "用 anh em 写一个关于兄弟姐妹的句子。例句：Anh em tôi rất thân nhau.", "targetVocab": "anh em"},
            {"prompt": "用 gia đình 写一个关于家庭的句子。例句：Gia đình là điều quan trọng nhất.", "targetVocab": "gia đình"},
            {"prompt": "用 nhà 写一个关于你家的句子。例句：Nhà tôi có một khu vườn nhỏ.", "targetVocab": "nhà"},
        ],
        "s2_vocab": ["vợ", "chồng", "con trai", "con gái", "cháu", "họ hàng"],
        "s2_topic": "亲属关系",
        "s2_intro_title": "介绍：亲属关系",
        "s2_intro_desc": "学习6个关于亲属关系的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：bố（爸爸）、mẹ（妈妈）、con（孩子）、"
            "anh em（兄弟姐妹）、gia đình（家庭）和 nhà（家）。\n\n"
            "今天学习6个关于亲属关系的词汇。\n\n"
            "第一个词是 vợ。Vợ 是妻子。"
            "你可以说：Vợ tôi là người Việt Nam，意思是「我妻子是越南人」。\n\n"
            "第二个词是 chồng。Chồng 是丈夫。"
            "你可以说：Chồng chị ấy làm kỹ sư，意思是「她丈夫是工程师」。\n\n"
            "第三个词是 con trai。Con trai 是儿子。"
            "你可以说：Con trai tôi 5 tuổi，意思是「我儿子5岁」。\n\n"
            "第四个词是 con gái。Con gái 是女儿。"
            "你可以说：Con gái tôi rất thông minh，意思是「我女儿很聪明」。\n\n"
            "第五个词是 cháu。Cháu 是孙子/孙女，也是晚辈对长辈的自称。"
            "你可以说：Ông bà có mấy cháu？意思是「爷爷奶奶有几个孙子？」\n\n"
            "第六个词是 họ hàng。Họ hàng 是亲戚。越南人的 họ hàng 关系非常紧密。"
            "你可以说：Họ hàng tôi ở Hà Nội，意思是「我的亲戚在河内」。\n\n"
            "好的，让我们练习：vợ, chồng, con trai, con gái, cháu, họ hàng。"
        ),
        "s2_reading_title": "阅读：越南亲属关系",
        "s2_reading_desc": "Vợ tôi là người Đà Nẵng.",
        "s2_reading_text": (
            "Vợ tôi là người Đà Nẵng. "
            "Chồng chị ấy làm việc ở Sài Gòn. "
            "Con trai chúng tôi đang đi học. "
            "Con gái chúng tôi mới 2 tuổi. "
            "Cháu ngoại ông bà rất đáng yêu. "
            "Họ hàng thường gặp nhau vào dịp Tết."
        ),
        "s2_writing_items": [
            {"prompt": "用 vợ 写一个关于妻子的句子。例句：Vợ tôi nấu ăn rất ngon.", "targetVocab": "vợ"},
            {"prompt": "用 chồng 写一个关于丈夫的句子。例句：Chồng tôi thích xem bóng đá.", "targetVocab": "chồng"},
            {"prompt": "用 con trai 写一个关于儿子的句子。例句：Con trai tôi thích chơi bóng đá.", "targetVocab": "con trai"},
            {"prompt": "用 con gái 写一个关于女儿的句子。例句：Con gái tôi thích vẽ tranh.", "targetVocab": "con gái"},
            {"prompt": "用 cháu 写一个关于孙辈的句子。例句：Ông bà rất yêu cháu.", "targetVocab": "cháu"},
            {"prompt": "用 họ hàng 写一个关于亲戚的句子。例句：Họ hàng tôi rất đông, có hơn 50 người.", "targetVocab": "họ hàng"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南家庭词汇！\n\n"
            "第一课：bố（爸爸）、mẹ（妈妈）、con（孩子）、"
            "anh em（兄弟姐妹）、gia đình（家庭）、nhà（家）。\n\n"
            "第二课：vợ（妻子）、chồng（丈夫）、con trai（儿子）、"
            "con gái（女儿）、cháu（孙子）、họ hàng（亲戚）。\n\n"
            "现在让我们综合练习这12个词汇。"
        ),
        "review_reading_title": "阅读：我的大家庭",
        "review_reading_desc": "Gia đình tôi rất lớn.",
        "review_reading_text": (
            "Gia đình tôi rất lớn. Bố mẹ tôi sống ở nhà cũ. "
            "Tôi và vợ sống ở Sài Gòn. "
            "Chồng chị tôi là bác sĩ. "
            "Con trai tôi và con gái tôi đi học cùng trường. "
            "Anh em tôi có 5 người. "
            "Cháu nội ông bà rất ngoan. "
            "Họ hàng gặp nhau mỗi dịp Tết."
        ),
        "review_writing_items": [
            {"prompt": "用 bố 和 mẹ 描述你的父母。", "targetVocab": "bố"},
            {"prompt": "用 vợ 或 chồng 描述你的伴侣。", "targetVocab": "vợ"},
            {"prompt": "用 con trai 和 con gái 描述你的孩子。", "targetVocab": "con trai"},
            {"prompt": "用 gia đình 和 họ hàng 描述你的家族。", "targetVocab": "gia đình"},
        ],
        "final_reading_title": "阅读：越南家庭文化",
        "final_reading_desc": "Gia đình là trung tâm của văn hóa Việt Nam.",
        "final_reading_text": (
            "Gia đình là trung tâm của văn hóa Việt Nam. "
            "Bố mẹ luôn được kính trọng. "
            "Con cái phải hiếu thảo với bố mẹ. "
            "Vợ chồng cùng nhau xây dựng nhà cửa. "
            "Con trai và con gái đều được yêu thương. "
            "Anh em giúp đỡ lẫn nhau. "
            "Ông bà sống cùng cháu trong một nhà. "
            "Họ hàng gần gũi như một đại gia đình."
        ),
        "farewell_text": (
            "恭喜你完成了越南家庭与亲属课程！让我们回顾12个词汇。\n\n"
            "Bố——爸爸。在越南，bố 是家庭的支柱。一声 bố ơi 充满了温暖。\n\n"
            "Mẹ——妈妈。越南人说 mẹ 的时候，声音总是特别柔软。\n\n"
            "Con——孩子。每个越南 con 都是父母的骄傲。\n\n"
            "Anh em——兄弟姐妹。越南的 anh em 情谊深厚，一辈子互相扶持。\n\n"
            "Gia đình——家庭。对越南人来说，gia đình 比什么都重要。\n\n"
            "Nhà——家。无论走多远，nhà 永远是最温暖的地方。\n\n"
            "Vợ——妻子。越南的 vợ 通常是家庭的真正管理者。\n\n"
            "Chồng——丈夫。一个好 chồng 是越南家庭幸福的关键。\n\n"
            "Con trai——儿子。越南的 con trai 从小就被教导要有责任感。\n\n"
            "Con gái——女儿。越南人说 con gái 是「贴心小棉袄」。\n\n"
            "Cháu——孙辈。ông bà 最大的快乐就是看着 cháu 长大。\n\n"
            "Họ hàng——亲戚。越南的 họ hàng 网络庞大而紧密。\n\n"
            "你现在拥有了谈论越南家庭话题的语言工具。"
            "记住，在越南，谈论家庭是建立友谊最快的方式。"
            "下次和越南朋友聊天时，试着用这些词汇分享你的家庭故事。"
        ),
    },
    # ===== B1-1: 越南办公室用语 (display_order=1) =====
    {
        "series": "B1", "order": 1,
        "title": "越南办公室用语",
        "description": (
            "想象你第一天走进河内的办公室，同事们用越南语打招呼——"
            "而你只能尴尬地微笑点头。\n\n"
            "在越南职场，语言不只是沟通工具，它是你融入团队的通行证。"
            "不会说「开会」「报告」「截止日期」，你就永远是那个需要翻译的外国人。\n\n"
            "这门课程教你12个最实用的办公室词汇，"
            "让你在越南职场中不再是旁观者。\n\n"
            "从第一天起就用越南语参与工作——这才是真正的职场融入。"
        ),
        "preview_text": (
            "想象你第一天走进河内的办公室，同事们用越南语打招呼，"
            "而你只能尴尬地微笑点头。这门课程教你12个最实用的办公室词汇："
            "从công ty（公司）到văn phòng（办公室），从họp（开会）到báo cáo（报告），"
            "从đồng nghiệp（同事）到sếp（老板），从email到lịch（日程），"
            "从dự án（项目）到hạn（截止日期），从nghỉ phép（请假）到tăng ca（加班）。"
            "你将通过真实的职场场景学习这些词汇。"
        ),
        "s1_vocab": ["công ty", "văn phòng", "họp", "báo cáo", "đồng nghiệp", "sếp"],
        "s1_topic": "办公室基础",
        "s1_intro_title": "介绍：越南办公室",
        "s1_intro_desc": "学习6个越南办公室最常用的基础词汇。",
        "s1_intro_text": (
            "欢迎来到越南办公室用语课程！今天学习6个办公室基础词汇。\n\n"
            "第一个词是 công ty。Công ty 是公司。"
            "你可以说：Công ty tôi ở quận 1，意思是「我的公司在第一郡」。\n\n"
            "第二个词是 văn phòng。Văn phòng 是办公室。"
            "你可以说：Văn phòng ở tầng 5，意思是「办公室在5楼」。\n\n"
            "第三个词是 họp。Họp 是开会。越南公司经常开会。"
            "你可以说：Mấy giờ họp？意思是「几点开会？」\n\n"
            "第四个词是 báo cáo。Báo cáo 是报告。"
            "你可以说：Tôi cần viết báo cáo，意思是「我需要写报告」。\n\n"
            "第五个词是 đồng nghiệp。Đồng nghiệp 是同事。"
            "你可以说：Đồng nghiệp tôi rất thân thiện，意思是「我的同事很友好」。\n\n"
            "第六个词是 sếp。Sếp 是老板。越南人叫老板 sếp。"
            "你可以说：Sếp muốn gặp bạn，意思是「老板想见你」。\n\n"
            "好的，让我们练习：công ty, văn phòng, họp, báo cáo, đồng nghiệp, sếp。"
        ),
        "s1_reading_title": "阅读：在越南办公室",
        "s1_reading_desc": "Công ty tôi ở trung tâm Sài Gòn.",
        "s1_reading_text": (
            "Công ty tôi ở trung tâm Sài Gòn. "
            "Văn phòng rất rộng và sáng. "
            "Sáng nay chúng tôi họp lúc 9 giờ. "
            "Sếp yêu cầu viết báo cáo tuần. "
            "Đồng nghiệp giúp tôi rất nhiều. "
            "Tôi thích làm việc ở công ty này."
        ),
        "s1_writing_items": [
            {"prompt": "用 công ty 写一个关于你公司的句子。例句：Công ty tôi có 200 nhân viên.", "targetVocab": "công ty"},
            {"prompt": "用 văn phòng 写一个关于办公室的句子。例句：Văn phòng mới rất đẹp và hiện đại.", "targetVocab": "văn phòng"},
            {"prompt": "用 họp 写一个关于开会的句子。例句：Chúng tôi họp mỗi sáng thứ Hai.", "targetVocab": "họp"},
            {"prompt": "用 báo cáo 写一个关于工作的句子。例句：Tôi phải nộp báo cáo trước thứ Sáu.", "targetVocab": "báo cáo"},
            {"prompt": "用 đồng nghiệp 写一个关于同事的句子。例句：Đồng nghiệp mới rất giỏi tiếng Anh.", "targetVocab": "đồng nghiệp"},
            {"prompt": "用 sếp 写一个关于老板的句子。例句：Sếp tôi là người rất công bằng.", "targetVocab": "sếp"},
        ],
        "s2_vocab": ["email", "lịch", "dự án", "hạn", "nghỉ phép", "tăng ca"],
        "s2_topic": "工作安排",
        "s2_intro_title": "介绍：工作安排",
        "s2_intro_desc": "学习6个关于工作安排的词汇。",
        "s2_intro_text": (
            "欢迎回来！上一课我们学了：công ty（公司）、văn phòng（办公室）、"
            "họp（开会）、báo cáo（报告）、đồng nghiệp（同事）和 sếp（老板）。\n\n"
            "今天学习6个关于工作安排的词汇。\n\n"
            "第一个词是 email。Email 在越南职场中和全世界一样重要。"
            "你可以说：Tôi gửi email cho bạn，意思是「我给你发邮件」。\n\n"
            "第二个词是 lịch。Lịch 是日程、日历。"
            "你可以说：Lịch họp hôm nay thế nào？意思是「今天的会议日程怎样？」\n\n"
            "第三个词是 dự án。Dự án 是项目。"
            "你可以说：Dự án này rất quan trọng，意思是「这个项目很重要」。\n\n"
            "第四个词是 hạn。Hạn 是截止日期、期限。"
            "你可以说：Hạn nộp là thứ Sáu，意思是「截止日期是周五」。\n\n"
            "第五个词是 nghỉ phép。Nghỉ phép 是请假。"
            "你可以说：Tôi muốn nghỉ phép 3 ngày，意思是「我想请3天假」。\n\n"
            "第六个词是 tăng ca。Tăng ca 是加班。"
            "你可以说：Hôm nay tôi phải tăng ca，意思是「今天我要加班」。\n\n"
            "好的，让我们练习：email, lịch, dự án, hạn, nghỉ phép, tăng ca。"
        ),
        "s2_reading_title": "阅读：工作日程",
        "s2_reading_desc": "Sáng nay tôi kiểm tra email.",
        "s2_reading_text": (
            "Sáng nay tôi kiểm tra email. "
            "Sếp gửi lịch họp tuần này. "
            "Dự án mới bắt đầu từ thứ Hai. "
            "Hạn nộp báo cáo là thứ Sáu. "
            "Đồng nghiệp xin nghỉ phép 2 ngày. "
            "Tôi phải tăng ca để hoàn thành công việc."
        ),
        "s2_writing_items": [
            {"prompt": "用 email 写一个关于工作沟通的句子。例句：Tôi nhận được email từ khách hàng.", "targetVocab": "email"},
            {"prompt": "用 lịch 写一个关于日程安排的句子。例句：Lịch tuần này rất bận.", "targetVocab": "lịch"},
            {"prompt": "用 dự án 写一个关于项目的句子。例句：Dự án này kéo dài 6 tháng.", "targetVocab": "dự án"},
            {"prompt": "用 hạn 写一个关于截止日期的句子。例句：Hạn cuối cùng là ngày 30 tháng 6.", "targetVocab": "hạn"},
            {"prompt": "用 nghỉ phép 写一个关于请假的句子。例句：Tôi nghỉ phép để đi du lịch.", "targetVocab": "nghỉ phép"},
            {"prompt": "用 tăng ca 写一个关于加班的句子。例句：Cuối năm, mọi người thường phải tăng ca.", "targetVocab": "tăng ca"},
        ],
        "review_intro_text": (
            "你已经学完了12个越南办公室词汇！\n\n"
            "第一课：công ty（公司）、văn phòng（办公室）、họp（开会）、"
            "báo cáo（报告）、đồng nghiệp（同事）、sếp（老板）。\n\n"
            "第二课：email、lịch（日程）、dự án（项目）、"
            "hạn（截止日期）、nghỉ phép（请假）、tăng ca（加班）。\n\n"
            "现在让我们综合练习这12个词汇。"
        ),
        "review_reading_title": "阅读：越南职场一天",
        "review_reading_desc": "Tôi đến công ty lúc 8 giờ sáng.",
        "review_reading_text": (
            "Tôi đến công ty lúc 8 giờ sáng. "
            "Văn phòng đã có nhiều đồng nghiệp. "
            "Tôi kiểm tra email và xem lịch họp. "
            "Sếp gọi họp về dự án mới. "
            "Tôi viết báo cáo trước hạn. "
            "Một đồng nghiệp xin nghỉ phép. "
            "Tôi phải tăng ca để giúp nhóm."
        ),
        "review_writing_items": [
            {"prompt": "用 công ty 和 văn phòng 描述你的工作环境。", "targetVocab": "công ty"},
            {"prompt": "用 họp 和 báo cáo 描述一天的工作。", "targetVocab": "họp"},
            {"prompt": "用 dự án 和 hạn 描述一个项目。", "targetVocab": "dự án"},
            {"prompt": "用 nghỉ phép 和 tăng ca 描述工作生活平衡。", "targetVocab": "nghỉ phép"},
        ],
        "final_reading_title": "阅读：越南职场文化",
        "final_reading_desc": "Văn hóa công sở ở Việt Nam rất thú vị.",
        "final_reading_text": (
            "Văn hóa công sở ở Việt Nam rất thú vị. "
            "Công ty Việt Nam thường họp nhiều. "
            "Văn phòng hiện đại có không gian mở. "
            "Sếp và đồng nghiệp thường ăn trưa cùng nhau. "
            "Email là cách liên lạc chính thức. "
            "Lịch làm việc từ thứ Hai đến thứ Sáu. "
            "Dự án lớn cần nhiều người tham gia. "
            "Nhớ nộp báo cáo đúng hạn. "
            "Nghỉ phép cần xin trước một tuần. "
            "Tăng ca thường có thêm lương."
        ),
        "farewell_text": (
            "恭喜你完成了越南办公室用语课程！让我们回顾12个词汇。\n\n"
            "Công ty——公司。你的 công ty 是你在越南的第二个家。\n\n"
            "Văn phòng——办公室。一个好的 văn phòng 让工作更愉快。\n\n"
            "Họp——开会。越南人爱 họp，做好准备。\n\n"
            "Báo cáo——报告。写好 báo cáo 是职场基本功。\n\n"
            "Đồng nghiệp——同事。好的 đồng nghiệp 是职场最大的财富。\n\n"
            "Sếp——老板。和 sếp 保持良好关系很重要。\n\n"
            "Email——邮件。越南职场的正式沟通渠道。\n\n"
            "Lịch——日程。管理好 lịch，工作更高效。\n\n"
            "Dự án——项目。每个 dự án 都是展示能力的机会。\n\n"
            "Hạn——截止日期。永远不要错过 hạn。\n\n"
            "Nghỉ phép——请假。工作再忙也要记得 nghỉ phép。\n\n"
            "Tăng ca——加班。偶尔 tăng ca 可以，但别让它成为常态。\n\n"
            "你现在拥有了在越南职场生存的基本语言工具。"
            "用越南语参与工作，你会发现同事们对你的态度完全不同。加油！"
        ),
    },
    # ===== B1-2: 越南商务邮件 (display_order=2) =====
    {"series": "B1", "order": 2, "title": "越南商务邮件",
     "description": "每天有数百万封商务邮件在越南企业间流转。\n\n如果你的邮件充满语法错误和不恰当的称呼，你的专业形象就会大打折扣。越南商务邮件有自己的格式和礼仪规范。\n\n这门课程教你12个商务邮件中最常用的词汇，从称呼到结尾，从附件到回复。\n\n写出一封得体的越南语商务邮件，让你的越南合作伙伴刮目相看。",
     "preview_text": "每天有数百万封商务邮件在越南企业间流转。如果你的邮件充满语法错误，你的专业形象就会大打折扣。这门课程教你12个商务邮件词汇：从kính gửi（敬启）到trân trọng（此致），从đính kèm（附件）到trả lời（回复），从chủ đề（主题）到nội dung（内容），从gửi（发送）到nhận（接收），从xác nhận（确认）到thông báo（通知），从cuộc họp（会议）到lịch hẹn（预约）。",
     "s1_vocab": ["kính gửi", "trân trọng", "đính kèm", "trả lời", "chủ đề", "nội dung"],
     "s1_topic": "邮件格式",
     "s1_intro_title": "介绍：商务邮件格式", "s1_intro_desc": "学习6个越南商务邮件的基础词汇。",
     "s1_intro_text": "欢迎来到越南商务邮件课程！今天学习6个邮件格式词汇。\n\n第一个词是 kính gửi。Kính gửi 是「敬启」，用在邮件开头。你可以写：Kính gửi anh Minh，意思是「敬启明先生」。\n\n第二个词是 trân trọng。Trân trọng 是「此致敬礼」，用在邮件结尾。写完邮件后加上 Trân trọng 显得很专业。\n\n第三个词是 đính kèm。Đính kèm 是附件。你可以写：Tôi đính kèm báo cáo，意思是「我附上报告」。\n\n第四个词是 trả lời。Trả lời 是回复。你可以说：Xin trả lời trước thứ Sáu，意思是「请在周五前回复」。\n\n第五个词是 chủ đề。Chủ đề 是主题。邮件的 chủ đề 要简洁明了。\n\n第六个词是 nội dung。Nội dung 是内容。你可以说：Nội dung email rất rõ ràng，意思是「邮件内容很清楚」。\n\n好的，让我们练习：kính gửi, trân trọng, đính kèm, trả lời, chủ đề, nội dung。",
     "s1_reading_title": "阅读：一封商务邮件", "s1_reading_desc": "Kính gửi anh Minh.",
     "s1_reading_text": "Kính gửi anh Minh. Chủ đề email hôm nay là báo cáo tháng. Nội dung gồm kết quả kinh doanh. Tôi đính kèm file báo cáo. Xin anh trả lời trước thứ Sáu. Trân trọng.",
     "s1_writing_items": [
         {"prompt": "用 kính gửi 写一个邮件开头。例句：Kính gửi chị Lan, tôi viết email này để xin nghỉ phép.", "targetVocab": "kính gửi"},
         {"prompt": "用 trân trọng 写一个邮件结尾。例句：Cảm ơn anh đã đọc. Trân trọng, Minh.", "targetVocab": "trân trọng"},
         {"prompt": "用 đính kèm 写一个关于附件的句子。例句：Tôi đính kèm hợp đồng để anh xem.", "targetVocab": "đính kèm"},
         {"prompt": "用 trả lời 写一个关于回复的句子。例句：Xin trả lời email này trước 5 giờ chiều.", "targetVocab": "trả lời"},
         {"prompt": "用 chủ đề 写一个关于邮件主题的句子。例句：Chủ đề email phải ngắn gọn và rõ ràng.", "targetVocab": "chủ đề"},
         {"prompt": "用 nội dung 写一个关于邮件内容的句子。例句：Nội dung email cần đi thẳng vào vấn đề.", "targetVocab": "nội dung"},
     ],
     "s2_vocab": ["gửi", "nhận", "xác nhận", "thông báo", "cuộc họp", "lịch hẹn"],
     "s2_topic": "邮件操作",
     "s2_intro_title": "介绍：邮件操作", "s2_intro_desc": "学习6个关于邮件操作和商务沟通的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：kính gửi（敬启）、trân trọng（此致）、đính kèm（附件）、trả lời（回复）、chủ đề（主题）和 nội dung（内容）。\n\n今天学习6个邮件操作词汇。\n\n第一个词是 gửi。Gửi 是发送。你可以说：Tôi đã gửi email rồi，意思是「我已经发了邮件」。\n\n第二个词是 nhận。Nhận 是接收。你可以说：Anh đã nhận email chưa？意思是「你收到邮件了吗？」\n\n第三个词是 xác nhận。Xác nhận 是确认。你可以说：Xin xác nhận lịch họp，意思是「请确认会议时间」。\n\n第四个词是 thông báo。Thông báo 是通知。你可以说：Đây là thông báo quan trọng，意思是「这是重要通知」。\n\n第五个词是 cuộc họp。Cuộc họp 是会议。你可以说：Cuộc họp lúc 2 giờ chiều，意思是「会议下午2点」。\n\n第六个词是 lịch hẹn。Lịch hẹn 是预约。你可以说：Tôi muốn đặt lịch hẹn，意思是「我想预约」。\n\n好的，让我们练习：gửi, nhận, xác nhận, thông báo, cuộc họp, lịch hẹn。",
     "s2_reading_title": "阅读：商务沟通", "s2_reading_desc": "Tôi gửi email cho đồng nghiệp.",
     "s2_reading_text": "Tôi gửi email cho đồng nghiệp. Anh ấy nhận được ngay. Tôi xác nhận thời gian cuộc họp. Sếp gửi thông báo cho cả công ty. Cuộc họp bắt đầu lúc 3 giờ. Tôi đặt lịch hẹn với khách hàng.",
     "s2_writing_items": [
         {"prompt": "用 gửi 写一个关于发邮件的句子。例句：Tôi gửi báo cáo cho sếp mỗi tuần.", "targetVocab": "gửi"},
         {"prompt": "用 nhận 写一个关于收邮件的句子。例句：Tôi nhận được email từ đối tác Nhật Bản.", "targetVocab": "nhận"},
         {"prompt": "用 xác nhận 写一个关于确认的句子。例句：Xin xác nhận đơn hàng trước 5 giờ.", "targetVocab": "xác nhận"},
         {"prompt": "用 thông báo 写一个关于通知的句子。例句：Công ty thông báo nghỉ lễ 3 ngày.", "targetVocab": "thông báo"},
         {"prompt": "用 cuộc họp 写一个关于会议的句子。例句：Cuộc họp hôm nay rất quan trọng.", "targetVocab": "cuộc họp"},
         {"prompt": "用 lịch hẹn 写一个关于预约的句子。例句：Tôi có lịch hẹn với bác sĩ lúc 10 giờ.", "targetVocab": "lịch hẹn"},
     ],
     "review_intro_text": "你已经学完了12个越南商务邮件词汇！\n\n第一课：kính gửi（敬启）、trân trọng（此致）、đính kèm（附件）、trả lời（回复）、chủ đề（主题）、nội dung（内容）。\n\n第二课：gửi（发送）、nhận（接收）、xác nhận（确认）、thông báo（通知）、cuộc họp（会议）、lịch hẹn（预约）。\n\n现在让我们综合练习这12个词汇。",
     "review_reading_title": "阅读：商务邮件实战", "review_reading_desc": "Kính gửi chị Lan.",
     "review_reading_text": "Kính gửi chị Lan. Tôi gửi email này để xác nhận cuộc họp ngày mai. Chủ đề cuộc họp là dự án mới. Nội dung chi tiết tôi đính kèm trong file. Xin chị nhận và trả lời trước 5 giờ. Đây cũng là thông báo về lịch hẹn với khách hàng. Trân trọng.",
     "review_writing_items": [
         {"prompt": "用 kính gửi 和 trân trọng 写一封简短的商务邮件。", "targetVocab": "kính gửi"},
         {"prompt": "用 gửi 和 nhận 描述邮件沟通过程。", "targetVocab": "gửi"},
         {"prompt": "用 xác nhận 和 cuộc họp 描述会议安排。", "targetVocab": "xác nhận"},
         {"prompt": "用 đính kèm 和 nội dung 描述邮件附件。", "targetVocab": "đính kèm"},
     ],
     "final_reading_title": "阅读：越南商务邮件指南", "final_reading_desc": "Viết email công việc cần chuyên nghiệp.",
     "final_reading_text": "Viết email công việc cần chuyên nghiệp. Bắt đầu bằng kính gửi và kết thúc bằng trân trọng. Chủ đề email phải rõ ràng. Nội dung ngắn gọn và đi thẳng vào vấn đề. Đính kèm file nếu cần thiết. Gửi email đúng người và đúng lúc. Kiểm tra xem người nhận đã nhận chưa. Xác nhận thông tin quan trọng. Thông báo thay đổi lịch hẹn kịp thời. Trả lời email trong vòng 24 giờ. Chuẩn bị kỹ trước mỗi cuộc họp.",
     "farewell_text": "恭喜你完成了越南商务邮件课程！让我们回顾12个词汇。\n\nKính gửi——敬启，邮件的第一印象。用对了 kính gửi，你的邮件就成功了一半。\n\nTrân trọng——此致敬礼，专业的结尾。每封邮件都以 trân trọng 收尾。\n\nĐính kèm——附件。记得在邮件中提到你 đính kèm 了什么。\n\nTrả lời——回复。及时 trả lời 是职场基本礼仪。\n\nChủ đề——主题。好的 chủ đề 让人一眼就知道邮件内容。\n\nNội dung——内容。Nội dung 要简洁有力，不要啰嗦。\n\nGửi——发送。发送前检查一遍，避免尴尬。\n\nNhận——接收。确认对方 nhận 到了你的邮件。\n\nXác nhận——确认。重要事项一定要 xác nhận。\n\nThông báo——通知。及时 thông báo 变更，避免误会。\n\nCuộc họp——会议。每次 cuộc họp 都要做好准备。\n\nLịch hẹn——预约。管理好 lịch hẹn，不要迟到。\n\n你现在能写出得体的越南语商务邮件了。这是职场沟通的重要一步。继续练习！",
    },
    # ===== B2-1: 越南求职基础 =====
    {"series": "B2", "order": 1, "title": "越南求职基础",
     "description": "在越南找工作，你的简历可能很漂亮——但面试时一句越南语都说不出来？\n\n越南雇主越来越看重候选人的本地语言能力。即使是外企，会说越南语也是巨大的加分项。\n\n这门课程教你12个求职过程中最实用的词汇，从写简历到参加面试。\n\n掌握这些词汇，你在越南就业市场上的竞争力将大幅提升。",
     "preview_text": "在越南找工作，你的简历可能很漂亮，但面试时一句越南语都说不出来？这门课程教你12个求职词汇：从xin việc（求职）到hồ sơ（简历），从phỏng vấn（面试）到kinh nghiệm（经验），从lương（工资）到ứng tuyển（应聘），从tuyển dụng（招聘）到vị trí（职位），从kỹ năng（技能）到bằng cấp（学历），从hợp đồng（合同）到thử việc（试用期）。",
     "s1_vocab": ["xin việc", "hồ sơ", "phỏng vấn", "kinh nghiệm", "lương", "ứng tuyển"],
     "s1_topic": "求职基础", "s1_intro_title": "介绍：越南求职", "s1_intro_desc": "学习6个越南求职的基础词汇。",
     "s1_intro_text": "欢迎来到越南求职基础课程！今天学习6个求职词汇。\n\n第一个词是 xin việc。Xin việc 是求职、找工作。你可以说：Tôi đang xin việc，意思是「我正在找工作」。\n\n第二个词是 hồ sơ。Hồ sơ 是简历、档案。你可以说：Tôi gửi hồ sơ xin việc，意思是「我提交求职简历」。\n\n第三个词是 phỏng vấn。Phỏng vấn 是面试。你可以说：Tôi có phỏng vấn ngày mai，意思是「我明天有面试」。\n\n第四个词是 kinh nghiệm。Kinh nghiệm 是经验。你可以说：Tôi có 5 năm kinh nghiệm，意思是「我有5年经验」。\n\n第五个词是 lương。Lương 是工资、薪水。你可以说：Lương tháng bao nhiêu？意思是「月薪多少？」\n\n第六个词是 ứng tuyển。Ứng tuyển 是应聘。你可以说：Tôi muốn ứng tuyển vị trí này，意思是「我想应聘这个职位」。\n\n好的，让我们练习：xin việc, hồ sơ, phỏng vấn, kinh nghiệm, lương, ứng tuyển。",
     "s1_reading_title": "阅读：求职过程", "s1_reading_desc": "Tôi đang xin việc ở Sài Gòn.",
     "s1_reading_text": "Tôi đang xin việc ở Sài Gòn. Tôi gửi hồ sơ cho nhiều công ty. Một công ty mời tôi phỏng vấn. Họ hỏi về kinh nghiệm làm việc. Lương ở đây khá tốt. Tôi quyết định ứng tuyển.",
     "s1_writing_items": [
         {"prompt": "用 xin việc 写一个关于找工作的句子。例句：Xin việc ở Việt Nam cần biết tiếng Việt.", "targetVocab": "xin việc"},
         {"prompt": "用 hồ sơ 写一个关于简历的句子。例句：Hồ sơ xin việc cần có ảnh và bằng cấp.", "targetVocab": "hồ sơ"},
         {"prompt": "用 phỏng vấn 写一个关于面试的句子。例句：Phỏng vấn bằng tiếng Việt rất khó.", "targetVocab": "phỏng vấn"},
         {"prompt": "用 kinh nghiệm 写一个关于工作经验的句子。例句：Kinh nghiệm quan trọng hơn bằng cấp.", "targetVocab": "kinh nghiệm"},
         {"prompt": "用 lương 写一个关于薪水的句子。例句：Lương ở Sài Gòn cao hơn các tỉnh.", "targetVocab": "lương"},
         {"prompt": "用 ứng tuyển 写一个关于应聘的句子。例句：Có 50 người ứng tuyển vị trí này.", "targetVocab": "ứng tuyển"},
     ],
     "s2_vocab": ["tuyển dụng", "vị trí", "kỹ năng", "bằng cấp", "hợp đồng", "thử việc"],
     "s2_topic": "招聘与录用", "s2_intro_title": "介绍：招聘与录用", "s2_intro_desc": "学习6个关于招聘和录用的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：xin việc（求职）、hồ sơ（简历）、phỏng vấn（面试）、kinh nghiệm（经验）、lương（工资）和 ứng tuyển（应聘）。\n\n今天学习6个招聘和录用词汇。\n\n第一个词是 tuyển dụng。Tuyển dụng 是招聘。你可以说：Công ty đang tuyển dụng，意思是「公司正在招聘」。\n\n第二个词是 vị trí。Vị trí 是职位。你可以说：Vị trí này cần kinh nghiệm 3 năm，意思是「这个职位需要3年经验」。\n\n第三个词是 kỹ năng。Kỹ năng 是技能。你可以说：Kỹ năng giao tiếp rất quan trọng，意思是「沟通技能很重要」。\n\n第四个词是 bằng cấp。Bằng cấp 是学历、文凭。你可以说：Vị trí này yêu cầu bằng đại học，意思是「这个职位要求大学学历」。\n\n第五个词是 hợp đồng。Hợp đồng 是合同。你可以说：Tôi ký hợp đồng 1 năm，意思是「我签了1年合同」。\n\n第六个词是 thử việc。Thử việc 是试用期。你可以说：Thời gian thử việc là 2 tháng，意思是「试用期是2个月」。\n\n好的，让我们练习：tuyển dụng, vị trí, kỹ năng, bằng cấp, hợp đồng, thử việc。",
     "s2_reading_title": "阅读：招聘启事", "s2_reading_desc": "Công ty ABC đang tuyển dụng.",
     "s2_reading_text": "Công ty ABC đang tuyển dụng. Vị trí cần tuyển là quản lý. Yêu cầu kỹ năng lãnh đạo tốt. Bằng cấp tối thiểu là đại học. Hợp đồng lao động 2 năm. Thời gian thử việc là 2 tháng.",
     "s2_writing_items": [
         {"prompt": "用 tuyển dụng 写一个关于招聘的句子。例句：Mùa hè là mùa tuyển dụng cao điểm.", "targetVocab": "tuyển dụng"},
         {"prompt": "用 vị trí 写一个关于职位的句子。例句：Vị trí giám đốc cần nhiều kinh nghiệm.", "targetVocab": "vị trí"},
         {"prompt": "用 kỹ năng 写一个关于技能的句子。例句：Kỹ năng tiếng Anh là lợi thế lớn.", "targetVocab": "kỹ năng"},
         {"prompt": "用 bằng cấp 写一个关于学历的句子。例句：Bằng cấp không phải là tất cả.", "targetVocab": "bằng cấp"},
         {"prompt": "用 hợp đồng 写一个关于合同的句子。例句：Đọc kỹ hợp đồng trước khi ký.", "targetVocab": "hợp đồng"},
         {"prompt": "用 thử việc 写一个关于试用期的句子。例句：Trong thời gian thử việc, lương thấp hơn.", "targetVocab": "thử việc"},
     ],
     "review_intro_text": "你已经学完了12个越南求职词汇！\n\n第一课：xin việc（求职）、hồ sơ（简历）、phỏng vấn（面试）、kinh nghiệm（经验）、lương（工资）、ứng tuyển（应聘）。\n\n第二课：tuyển dụng（招聘）、vị trí（职位）、kỹ năng（技能）、bằng cấp（学历）、hợp đồng（合同）、thử việc（试用期）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：完整的求职经历", "review_reading_desc": "Tôi bắt đầu xin việc từ tháng trước.",
     "review_reading_text": "Tôi bắt đầu xin việc từ tháng trước. Tôi gửi hồ sơ và ứng tuyển nhiều vị trí. Một công ty đang tuyển dụng mời tôi phỏng vấn. Họ hỏi về kinh nghiệm, kỹ năng và bằng cấp. Lương rất tốt. Tôi ký hợp đồng và bắt đầu thử việc.",
     "review_writing_items": [
         {"prompt": "用 xin việc 和 hồ sơ 描述求职过程。", "targetVocab": "xin việc"},
         {"prompt": "用 phỏng vấn 和 kinh nghiệm 描述面试经历。", "targetVocab": "phỏng vấn"},
         {"prompt": "用 tuyển dụng 和 vị trí 描述招聘信息。", "targetVocab": "tuyển dụng"},
         {"prompt": "用 hợp đồng 和 thử việc 描述入职过程。", "targetVocab": "hợp đồng"},
     ],
     "final_reading_title": "阅读：越南求职完整指南", "final_reading_desc": "Xin việc ở Việt Nam có nhiều bước.",
     "final_reading_text": "Xin việc ở Việt Nam có nhiều bước. Đầu tiên, chuẩn bị hồ sơ tốt. Tìm vị trí phù hợp và ứng tuyển. Công ty tuyển dụng sẽ xem kỹ năng và bằng cấp. Nếu phù hợp, họ mời phỏng vấn. Kinh nghiệm làm việc rất quan trọng. Thỏa thuận lương trước khi ký hợp đồng. Thời gian thử việc thường là 2 tháng.",
     "farewell_text": "恭喜你完成了越南求职基础课程！让我们回顾12个词汇。\n\nXin việc——求职。在越南 xin việc，语言能力是最大的优势。\n\nHồ sơ——简历。一份好的 hồ sơ 是成功的第一步。\n\nPhỏng vấn——面试。Phỏng vấn 时保持自信，用越南语回答加分。\n\nKinh nghiệm——经验。真实的 kinh nghiệm 比任何证书都有说服力。\n\nLương——工资。谈 lương 时要了解市场行情。\n\nỨng tuyển——应聘。大胆 ứng tuyển，机会是争取来的。\n\nTuyển dụng——招聘。关注 tuyển dụng 信息，不要错过好机会。\n\nVị trí——职位。找到适合自己的 vị trí 最重要。\n\nKỹ năng——技能。不断提升 kỹ năng，保持竞争力。\n\nBằng cấp——学历。Bằng cấp 是敲门砖，但不是全部。\n\nHợp đồng——合同。签 hợp đồng 前一定要仔细阅读。\n\nThử việc——试用期。Thử việc 期间好好表现，争取转正。\n\n你现在拥有了在越南求职的基本语言工具。祝你找到理想的工作！",
    },
    # ===== B2-2: 越南职业发展 =====
    {"series": "B2", "order": 2, "title": "越南职业发展",
     "description": "在越南工作不只是完成任务——你需要理解晋升文化、绩效评估和职业规划。\n\n很多外国人在越南工作多年，却因为语言障碍错过了晋升机会。他们听不懂绩效评估，看不懂培训通知。\n\n这门课程教你12个职业发展的核心词汇，帮你在越南职场中主动规划自己的未来。\n\n不要让语言成为你职业发展的天花板。",
     "preview_text": "在越南工作不只是完成任务，你需要理解晋升文化和职业规划。这门课程教你12个职业发展词汇：从thăng chức（晋升）到đánh giá（评估），从đào tạo（培训）到mục tiêu（目标），从thành tích（成绩）到khen thưởng（奖励），从nghề nghiệp（职业）到chuyên môn（专业），从quản lý（管理）到nhân viên（员工），从phòng ban（部门）到trưởng phòng（部门经理）。",
     "s1_vocab": ["thăng chức", "đánh giá", "đào tạo", "mục tiêu", "thành tích", "khen thưởng"],
     "s1_topic": "职业成长", "s1_intro_title": "介绍：职业成长", "s1_intro_desc": "学习6个越南职业成长的词汇。",
     "s1_intro_text": "欢迎来到越南职业发展课程！今天学习6个职业成长词汇。\n\n第一个词是 thăng chức。Thăng chức 是晋升。你可以说：Anh ấy được thăng chức，意思是「他被晋升了」。\n\n第二个词是 đánh giá。Đánh giá 是评估。你可以说：Đánh giá cuối năm rất quan trọng，意思是「年终评估很重要」。\n\n第三个词是 đào tạo。Đào tạo 是培训。你可以说：Công ty có chương trình đào tạo，意思是「公司有培训项目」。\n\n第四个词是 mục tiêu。Mục tiêu 是目标。你可以说：Mục tiêu năm nay là gì？意思是「今年的目标是什么？」\n\n第五个词是 thành tích。Thành tích 是成绩、业绩。你可以说：Thành tích của tôi rất tốt，意思是「我的业绩很好」。\n\n第六个词是 khen thưởng。Khen thưởng 是奖励。你可以说：Công ty khen thưởng nhân viên xuất sắc，意思是「公司奖励优秀员工」。\n\n好的，让我们练习：thăng chức, đánh giá, đào tạo, mục tiêu, thành tích, khen thưởng。",
     "s1_reading_title": "阅读：职业成长", "s1_reading_desc": "Anh Minh làm việc chăm chỉ.",
     "s1_reading_text": "Anh Minh làm việc chăm chỉ. Thành tích của anh rất tốt. Sếp đánh giá anh cao. Công ty cho anh đi đào tạo. Anh đặt mục tiêu rõ ràng. Cuối năm anh được khen thưởng và thăng chức.",
     "s1_writing_items": [
         {"prompt": "用 thăng chức 写一个关于晋升的句子。例句：Sau 3 năm, chị ấy được thăng chức giám đốc.", "targetVocab": "thăng chức"},
         {"prompt": "用 đánh giá 写一个关于评估的句子。例句：Đánh giá nhân viên diễn ra mỗi 6 tháng.", "targetVocab": "đánh giá"},
         {"prompt": "用 đào tạo 写一个关于培训的句子。例句：Chương trình đào tạo kéo dài 2 tuần.", "targetVocab": "đào tạo"},
         {"prompt": "用 mục tiêu 写一个关于目标的句子。例句：Mục tiêu của tôi là học giỏi tiếng Việt.", "targetVocab": "mục tiêu"},
         {"prompt": "用 thành tích 写一个关于业绩的句子。例句：Thành tích bán hàng tháng này rất cao.", "targetVocab": "thành tích"},
         {"prompt": "用 khen thưởng 写一个关于奖励的句子。例句：Nhân viên xuất sắc được khen thưởng tiền mặt.", "targetVocab": "khen thưởng"},
     ],
     "s2_vocab": ["nghề nghiệp", "chuyên môn", "quản lý", "nhân viên", "phòng ban", "trưởng phòng"],
     "s2_topic": "职场结构", "s2_intro_title": "介绍：职场结构", "s2_intro_desc": "学习6个关于职场结构的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：thăng chức（晋升）、đánh giá（评估）、đào tạo（培训）、mục tiêu（目标）、thành tích（成绩）和 khen thưởng（奖励）。\n\n今天学习6个职场结构词汇。\n\n第一个词是 nghề nghiệp。Nghề nghiệp 是职业。你可以说：Nghề nghiệp của bạn là gì？意思是「你的职业是什么？」\n\n第二个词是 chuyên môn。Chuyên môn 是专业。你可以说：Chuyên môn của tôi là IT，意思是「我的专业是IT」。\n\n第三个词是 quản lý。Quản lý 是管理、经理。你可以说：Anh ấy là quản lý dự án，意思是「他是项目经理」。\n\n第四个词是 nhân viên。Nhân viên 是员工。你可以说：Công ty có 100 nhân viên，意思是「公司有100名员工」。\n\n第五个词是 phòng ban。Phòng ban 是部门。你可以说：Phòng ban nào？意思是「哪个部门？」\n\n第六个词是 trưởng phòng。Trưởng phòng 是部门经理。你可以说：Trưởng phòng muốn gặp bạn，意思是「部门经理想见你」。\n\n好的，让我们练习：nghề nghiệp, chuyên môn, quản lý, nhân viên, phòng ban, trưởng phòng。",
     "s2_reading_title": "阅读：公司结构", "s2_reading_desc": "Công ty có nhiều phòng ban.",
     "s2_reading_text": "Công ty có nhiều phòng ban. Mỗi phòng ban có một trưởng phòng. Nhân viên làm việc theo chuyên môn. Quản lý giám sát công việc hàng ngày. Nghề nghiệp ở Việt Nam rất đa dạng. Mỗi người chọn nghề theo sở thích.",
     "s2_writing_items": [
         {"prompt": "用 nghề nghiệp 写一个关于职业的句子。例句：Nghề nghiệp yêu thích của tôi là giáo viên.", "targetVocab": "nghề nghiệp"},
         {"prompt": "用 chuyên môn 写一个关于专业的句子。例句：Chuyên môn cao giúp bạn thăng tiến nhanh.", "targetVocab": "chuyên môn"},
         {"prompt": "用 quản lý 写一个关于管理的句子。例句：Quản lý tốt cần kỹ năng giao tiếp.", "targetVocab": "quản lý"},
         {"prompt": "用 nhân viên 写一个关于员工的句子。例句：Nhân viên mới cần thời gian thích nghi.", "targetVocab": "nhân viên"},
         {"prompt": "用 phòng ban 写一个关于部门的句子。例句：Phòng ban marketing có 20 người.", "targetVocab": "phòng ban"},
         {"prompt": "用 trưởng phòng 写一个关于部门经理的句子。例句：Trưởng phòng họp với nhân viên mỗi tuần.", "targetVocab": "trưởng phòng"},
     ],
     "review_intro_text": "你已经学完了12个越南职业发展词汇！\n\n第一课：thăng chức（晋升）、đánh giá（评估）、đào tạo（培训）、mục tiêu（目标）、thành tích（成绩）、khen thưởng（奖励）。\n\n第二课：nghề nghiệp（职业）、chuyên môn（专业）、quản lý（管理）、nhân viên（员工）、phòng ban（部门）、trưởng phòng（部门经理）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：职业发展之路", "review_reading_desc": "Tôi bắt đầu làm nhân viên.",
     "review_reading_text": "Tôi bắt đầu làm nhân viên ở phòng ban kinh doanh. Trưởng phòng đánh giá tôi tốt. Tôi đi đào tạo để nâng cao chuyên môn. Mục tiêu của tôi là trở thành quản lý. Thành tích tốt giúp tôi được khen thưởng. Sau 3 năm, tôi thăng chức. Nghề nghiệp của tôi phát triển tốt.",
     "review_writing_items": [
         {"prompt": "用 thăng chức 和 đánh giá 描述晋升过程。", "targetVocab": "thăng chức"},
         {"prompt": "用 nhân viên 和 quản lý 描述职场层级。", "targetVocab": "nhân viên"},
         {"prompt": "用 đào tạo 和 kỹ năng 描述职业提升。", "targetVocab": "đào tạo"},
         {"prompt": "用 phòng ban 和 trưởng phòng 描述公司结构。", "targetVocab": "phòng ban"},
     ],
     "final_reading_title": "阅读：越南职业发展指南", "final_reading_desc": "Phát triển nghề nghiệp cần kế hoạch.",
     "final_reading_text": "Phát triển nghề nghiệp cần kế hoạch. Đặt mục tiêu rõ ràng cho mỗi năm. Nâng cao chuyên môn qua đào tạo. Nhân viên giỏi sẽ được đánh giá cao. Thành tích tốt dẫn đến khen thưởng. Quản lý tốt sẽ được thăng chức. Mỗi phòng ban cần trưởng phòng giỏi. Nghề nghiệp là hành trình dài.",
     "farewell_text": "恭喜你完成了越南职业发展课程！让我们回顾12个词汇。\n\nThăng chức——晋升，每个职场人的梦想。努力工作，thăng chức 自然会来。\n\nĐánh giá——评估。正面的 đánh giá 是晋升的基础。\n\nĐào tạo——培训。持续 đào tạo 让你保持竞争力。\n\nMục tiêu——目标。没有 mục tiêu 的职业就像没有方向的船。\n\nThành tích——成绩。用 thành tích 说话，比任何言语都有力。\n\nKhen thưởng——奖励。Khen thưởng 是对努力的认可。\n\nNghề nghiệp——职业。选择正确的 nghề nghiệp 比什么都重要。\n\nChuyên môn——专业。深耕 chuyên môn，成为领域专家。\n\nQuản lý——管理。好的 quản lý 能带领团队走向成功。\n\nNhân viên——员工。每个 nhân viên 都是公司的宝贵资产。\n\nPhòng ban——部门。了解各 phòng ban 的职能，更好地协作。\n\nTrưởng phòng——部门经理。成为 trưởng phòng 是很多人的第一个管理目标。\n\n你现在拥有了在越南职场发展的语言工具。规划你的职业道路，用越南语实现你的目标！",
    },
    # ===== B3-1: 越南科技行业词汇 =====
    {"series": "B3", "order": 1, "title": "越南科技行业词汇",
     "description": "越南的科技行业正在爆发式增长——但大多数外国从业者只会用英语交流。\n\n在越南的科技公司里，日常沟通越来越多地使用越南语。如果你听不懂同事讨论的技术问题，你就会被边缘化。\n\n这门课程教你12个科技行业最常用的越南语词汇，从软件到硬件，从编程到测试。\n\n用越南语谈论技术，你将在越南科技圈中脱颖而出。",
     "preview_text": "越南的科技行业正在爆发式增长，但大多数外国从业者只会用英语交流。这门课程教你12个科技行业词汇：从phần mềm（软件）到phần cứng（硬件），从lập trình（编程）到kiểm thử（测试），从dữ liệu（数据）到mạng（网络），从ứng dụng（应用）到hệ thống（系统），从bảo mật（安全）到cập nhật（更新），从lỗi（错误）到sửa lỗi（修复）。",
     "s1_vocab": ["phần mềm", "phần cứng", "lập trình", "kiểm thử", "dữ liệu", "mạng"],
     "s1_topic": "科技基础", "s1_intro_title": "介绍：科技基础", "s1_intro_desc": "学习6个越南科技行业的基础词汇。",
     "s1_intro_text": "欢迎来到越南科技行业词汇课程！今天学习6个科技基础词汇。\n\n第一个词是 phần mềm。Phần mềm 是软件。你可以说：Phần mềm này rất tốt，意思是「这个软件很好」。\n\n第二个词是 phần cứng。Phần cứng 是硬件。你可以说：Phần cứng máy tính cần nâng cấp，意思是「电脑硬件需要升级」。\n\n第三个词是 lập trình。Lập trình 是编程。你可以说：Tôi học lập trình Python，意思是「我学Python编程」。\n\n第四个词是 kiểm thử。Kiểm thử 是测试。你可以说：Kiểm thử phần mềm rất quan trọng，意思是「软件测试很重要」。\n\n第五个词是 dữ liệu。Dữ liệu 是数据。你可以说：Dữ liệu cần được bảo vệ，意思是「数据需要被保护」。\n\n第六个词是 mạng。Mạng 是网络。你可以说：Mạng internet ở đây rất nhanh，意思是「这里的网络很快」。\n\n好的，让我们练习：phần mềm, phần cứng, lập trình, kiểm thử, dữ liệu, mạng。",
     "s1_reading_title": "阅读：越南科技公司", "s1_reading_desc": "Công ty phần mềm ở Việt Nam phát triển nhanh.",
     "s1_reading_text": "Công ty phần mềm ở Việt Nam phát triển nhanh. Phần cứng ngày càng hiện đại. Nhiều bạn trẻ học lập trình. Kiểm thử là bước quan trọng. Dữ liệu khách hàng cần bảo mật. Mạng internet phủ sóng toàn quốc.",
     "s1_writing_items": [
         {"prompt": "用 phần mềm 写一个关于软件的句子。例句：Phần mềm quản lý giúp công ty hiệu quả hơn.", "targetVocab": "phần mềm"},
         {"prompt": "用 phần cứng 写一个关于硬件的句子。例句：Phần cứng mới giúp máy tính chạy nhanh hơn.", "targetVocab": "phần cứng"},
         {"prompt": "用 lập trình 写一个关于编程的句子。例句：Lập trình viên ở Việt Nam rất giỏi.", "targetVocab": "lập trình"},
         {"prompt": "用 kiểm thử 写一个关于测试的句子。例句：Đội kiểm thử tìm ra nhiều lỗi.", "targetVocab": "kiểm thử"},
         {"prompt": "用 dữ liệu 写一个关于数据的句子。例句：Dữ liệu lớn giúp phân tích thị trường.", "targetVocab": "dữ liệu"},
         {"prompt": "用 mạng 写一个关于网络的句子。例句：Mạng 5G sẽ thay đổi cuộc sống.", "targetVocab": "mạng"},
     ],
     "s2_vocab": ["ứng dụng", "hệ thống", "bảo mật", "cập nhật", "lỗi", "sửa lỗi"],
     "s2_topic": "技术运维", "s2_intro_title": "介绍：技术运维", "s2_intro_desc": "学习6个关于技术运维的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：phần mềm（软件）、phần cứng（硬件）、lập trình（编程）、kiểm thử（测试）、dữ liệu（数据）和 mạng（网络）。\n\n今天学习6个技术运维词汇。\n\n第一个词是 ứng dụng。Ứng dụng 是应用程序。你可以说：Ứng dụng này rất tiện，意思是「这个应用很方便」。\n\n第二个词是 hệ thống。Hệ thống 是系统。你可以说：Hệ thống đang bảo trì，意思是「系统正在维护」。\n\n第三个词是 bảo mật。Bảo mật 是安全。你可以说：Bảo mật dữ liệu rất quan trọng，意思是「数据安全很重要」。\n\n第四个词是 cập nhật。Cập nhật 是更新。你可以说：Cần cập nhật phần mềm，意思是「需要更新软件」。\n\n第五个词是 lỗi。Lỗi 是错误、bug。你可以说：Phần mềm có lỗi，意思是「软件有bug」。\n\n第六个词是 sửa lỗi。Sửa lỗi 是修复bug。你可以说：Đội lập trình đang sửa lỗi，意思是「开发团队正在修复bug」。\n\n好的，让我们练习：ứng dụng, hệ thống, bảo mật, cập nhật, lỗi, sửa lỗi。",
     "s2_reading_title": "阅读：技术运维日常", "s2_reading_desc": "Ứng dụng mới ra mắt hôm nay.",
     "s2_reading_text": "Ứng dụng mới ra mắt hôm nay. Hệ thống chạy ổn định. Đội bảo mật kiểm tra mỗi ngày. Phần mềm cần cập nhật thường xuyên. Người dùng báo có lỗi nhỏ. Đội lập trình sửa lỗi ngay trong ngày.",
     "s2_writing_items": [
         {"prompt": "用 ứng dụng 写一个关于手机应用的句子。例句：Ứng dụng Grab rất phổ biến ở Việt Nam.", "targetVocab": "ứng dụng"},
         {"prompt": "用 hệ thống 写一个关于系统的句子。例句：Hệ thống thanh toán online rất tiện lợi.", "targetVocab": "hệ thống"},
         {"prompt": "用 bảo mật 写一个关于安全的句子。例句：Bảo mật thông tin cá nhân rất quan trọng.", "targetVocab": "bảo mật"},
         {"prompt": "用 cập nhật 写一个关于更新的句子。例句：Nhớ cập nhật ứng dụng để có tính năng mới.", "targetVocab": "cập nhật"},
         {"prompt": "用 lỗi 写一个关于bug的句子。例句：Lỗi này ảnh hưởng đến nhiều người dùng.", "targetVocab": "lỗi"},
         {"prompt": "用 sửa lỗi 写一个关于修复的句子。例句：Chúng tôi sửa lỗi trong bản cập nhật mới.", "targetVocab": "sửa lỗi"},
     ],
     "review_intro_text": "你已经学完了12个越南科技行业词汇！\n\n第一课：phần mềm（软件）、phần cứng（硬件）、lập trình（编程）、kiểm thử（测试）、dữ liệu（数据）、mạng（网络）。\n\n第二课：ứng dụng（应用）、hệ thống（系统）、bảo mật（安全）、cập nhật（更新）、lỗi（错误）、sửa lỗi（修复）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：科技公司的一天", "review_reading_desc": "Sáng nay đội lập trình kiểm tra hệ thống.",
     "review_reading_text": "Sáng nay đội lập trình kiểm tra hệ thống. Phần mềm cần cập nhật. Đội kiểm thử tìm thấy một lỗi. Đội bảo mật kiểm tra dữ liệu. Ứng dụng chạy tốt trên mạng. Phần cứng máy chủ hoạt động ổn. Đội sửa lỗi xong trước trưa.",
     "review_writing_items": [
         {"prompt": "用 phần mềm 和 lập trình 描述软件开发。", "targetVocab": "phần mềm"},
         {"prompt": "用 lỗi 和 sửa lỗi 描述修复过程。", "targetVocab": "lỗi"},
         {"prompt": "用 bảo mật 和 dữ liệu 描述数据安全。", "targetVocab": "bảo mật"},
         {"prompt": "用 ứng dụng 和 cập nhật 描述应用维护。", "targetVocab": "ứng dụng"},
     ],
     "final_reading_title": "阅读：越南科技行业概览", "final_reading_desc": "Ngành công nghệ Việt Nam phát triển mạnh.",
     "final_reading_text": "Ngành công nghệ Việt Nam phát triển mạnh. Phần mềm và ứng dụng Việt Nam xuất khẩu ra thế giới. Lập trình viên Việt Nam rất giỏi. Kiểm thử và bảo mật ngày càng quan trọng. Dữ liệu là tài sản quý giá. Mạng internet phủ sóng rộng. Phần cứng được sản xuất tại Việt Nam. Hệ thống cần cập nhật thường xuyên. Khi có lỗi, đội kỹ thuật sửa lỗi nhanh chóng.",
     "farewell_text": "恭喜你完成了越南科技行业词汇课程！让我们回顾12个词汇。\n\nPhần mềm——软件，越南科技出口的主力。\n\nPhần cứng——硬件，越南正在成为全球制造中心。\n\nLập trình——编程，越南程序员在全球排名不断上升。\n\nKiểm thử——测试，好的产品离不开严格的 kiểm thử。\n\nDữ liệu——数据，21世纪的石油。\n\nMạng——网络，连接一切的基础。\n\nỨng dụng——应用，改变生活的工具。\n\nHệ thống——系统，一切运转的基础。\n\nBảo mật——安全，不能忽视的底线。\n\nCập nhật——更新，保持竞争力的关键。\n\nLỗi——错误，发现 lỗi 是进步的开始。\n\nSửa lỗi——修复，解决问题的能力最重要。\n\n你现在能用越南语讨论科技话题了。在越南的科技圈里，这是巨大的优势！",
    },
    # ===== B3-2: 越南酒店与服务业 =====
    {"series": "B3", "order": 2, "title": "越南酒店与服务业",
     "description": "越南的旅游业每年创造数十亿美元的收入——而酒店业是其中最大的雇主。\n\n如果你在越南的酒店或服务行业工作，不会说行业术语就像厨师不会用刀。\n\n这门课程教你12个酒店与服务业最常用的越南语词汇，从前台到客房，从预订到退房。\n\n掌握这些词汇，你将在越南服务业中游刃有余。",
     "preview_text": "越南的旅游业每年创造数十亿美元的收入，酒店业是最大的雇主。这门课程教你12个酒店与服务业词汇：从khách sạn（酒店）到phòng（房间），从đặt phòng（预订）到nhận phòng（入住），从trả phòng（退房）到lễ tân（前台），从dịch vụ（服务）到khách hàng（客户），从đánh giá（评价）到chất lượng（质量），从giải quyết（解决）到khiếu nại（投诉）。",
     "s1_vocab": ["khách sạn", "phòng", "đặt phòng", "nhận phòng", "trả phòng", "lễ tân"],
     "s1_topic": "酒店基础", "s1_intro_title": "介绍：酒店基础", "s1_intro_desc": "学习6个越南酒店的基础词汇。",
     "s1_intro_text": "欢迎来到越南酒店与服务业课程！今天学习6个酒店基础词汇。\n\n第一个词是 khách sạn。Khách sạn 是酒店。你可以说：Khách sạn này mấy sao？意思是「这家酒店几星？」\n\n第二个词是 phòng。Phòng 是房间。你可以说：Tôi muốn phòng đôi，意思是「我要双人房」。\n\n第三个词是 đặt phòng。Đặt phòng 是预订房间。你可以说：Tôi muốn đặt phòng，意思是「我想预订房间」。\n\n第四个词是 nhận phòng。Nhận phòng 是入住、办理入住。你可以说：Tôi muốn nhận phòng，意思是「我要办理入住」。\n\n第五个词是 trả phòng。Trả phòng 是退房。你可以说：Mấy giờ trả phòng？意思是「几点退房？」\n\n第六个词是 lễ tân。Lễ tân 是前台。你可以说：Hỏi lễ tân，意思是「问前台」。\n\n好的，让我们练习：khách sạn, phòng, đặt phòng, nhận phòng, trả phòng, lễ tân。",
     "s1_reading_title": "阅读：在越南酒店", "s1_reading_desc": "Tôi đến khách sạn lúc 2 giờ chiều.",
     "s1_reading_text": "Tôi đến khách sạn lúc 2 giờ chiều. Tôi đã đặt phòng trước. Lễ tân giúp tôi nhận phòng. Phòng rất sạch và đẹp. Ngày mai tôi trả phòng lúc 12 giờ. Khách sạn này rất tốt.",
     "s1_writing_items": [
         {"prompt": "用 khách sạn 写一个关于酒店的句子。例句：Khách sạn 5 sao ở Đà Nẵng rất đẹp.", "targetVocab": "khách sạn"},
         {"prompt": "用 phòng 写一个关于房间的句子。例句：Phòng có view biển rất đẹp.", "targetVocab": "phòng"},
         {"prompt": "用 đặt phòng 写一个关于预订的句子。例句：Tôi đặt phòng qua ứng dụng Booking.", "targetVocab": "đặt phòng"},
         {"prompt": "用 nhận phòng 写一个关于入住的句子。例句：Nhận phòng từ 2 giờ chiều.", "targetVocab": "nhận phòng"},
         {"prompt": "用 trả phòng 写一个关于退房的句子。例句：Trả phòng trước 12 giờ trưa.", "targetVocab": "trả phòng"},
         {"prompt": "用 lễ tân 写一个关于前台的句子。例句：Lễ tân nói tiếng Anh rất giỏi.", "targetVocab": "lễ tân"},
     ],
     "s2_vocab": ["dịch vụ", "khách hàng", "đánh giá", "chất lượng", "giải quyết", "khiếu nại"],
     "s2_topic": "服务质量", "s2_intro_title": "介绍：服务质量", "s2_intro_desc": "学习6个关于服务质量的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：khách sạn（酒店）、phòng（房间）、đặt phòng（预订）、nhận phòng（入住）、trả phòng（退房）和 lễ tân（前台）。\n\n今天学习6个服务质量词汇。\n\n第一个词是 dịch vụ。Dịch vụ 是服务。你可以说：Dịch vụ ở đây rất tốt，意思是「这里的服务很好」。\n\n第二个词是 khách hàng。Khách hàng 是客户。你可以说：Khách hàng luôn đúng，意思是「客户永远是对的」。\n\n第三个词是 đánh giá。Đánh giá 是评价。你可以说：Đánh giá trên mạng rất tốt，意思是「网上评价很好」。\n\n第四个词是 chất lượng。Chất lượng 是质量。你可以说：Chất lượng phòng rất cao，意思是「房间质量很高」。\n\n第五个词是 giải quyết。Giải quyết 是解决。你可以说：Chúng tôi sẽ giải quyết ngay，意思是「我们会立即解决」。\n\n第六个词是 khiếu nại。Khiếu nại 是投诉。你可以说：Tôi muốn khiếu nại，意思是「我想投诉」。\n\n好的，让我们练习：dịch vụ, khách hàng, đánh giá, chất lượng, giải quyết, khiếu nại。",
     "s2_reading_title": "阅读：服务质量", "s2_reading_desc": "Dịch vụ khách sạn rất quan trọng.",
     "s2_reading_text": "Dịch vụ khách sạn rất quan trọng. Khách hàng đánh giá cao chất lượng phòng. Khi có vấn đề, nhân viên giải quyết nhanh. Ít khi có khiếu nại. Dịch vụ tốt giúp khách sạn thành công. Đánh giá trên mạng rất tích cực.",
     "s2_writing_items": [
         {"prompt": "用 dịch vụ 写一个关于服务的句子。例句：Dịch vụ spa ở khách sạn rất tuyệt vời.", "targetVocab": "dịch vụ"},
         {"prompt": "用 khách hàng 写一个关于客户的句子。例句：Khách hàng hài lòng sẽ quay lại.", "targetVocab": "khách hàng"},
         {"prompt": "用 đánh giá 写一个关于评价的句子。例句：Đánh giá 5 sao trên Google.", "targetVocab": "đánh giá"},
         {"prompt": "用 chất lượng 写一个关于质量的句子。例句：Chất lượng dịch vụ quyết định thành công.", "targetVocab": "chất lượng"},
         {"prompt": "用 giải quyết 写一个关于解决问题的句子。例句：Quản lý giải quyết vấn đề rất nhanh.", "targetVocab": "giải quyết"},
         {"prompt": "用 khiếu nại 写一个关于投诉的句子。例句：Khiếu nại của khách hàng cần xử lý ngay.", "targetVocab": "khiếu nại"},
     ],
     "review_intro_text": "你已经学完了12个越南酒店与服务业词汇！\n\n第一课：khách sạn（酒店）、phòng（房间）、đặt phòng（预订）、nhận phòng（入住）、trả phòng（退房）、lễ tân（前台）。\n\n第二课：dịch vụ（服务）、khách hàng（客户）、đánh giá（评价）、chất lượng（质量）、giải quyết（解决）、khiếu nại（投诉）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：酒店服务全景", "review_reading_desc": "Khách sạn 5 sao có dịch vụ tuyệt vời.",
     "review_reading_text": "Khách sạn 5 sao có dịch vụ tuyệt vời. Lễ tân giúp khách hàng đặt phòng và nhận phòng. Phòng có chất lượng cao. Khi trả phòng, nhân viên hỏi đánh giá. Nếu có khiếu nại, quản lý giải quyết ngay. Dịch vụ tốt là chìa khóa thành công.",
     "review_writing_items": [
         {"prompt": "用 khách sạn 和 đặt phòng 描述预订酒店。", "targetVocab": "khách sạn"},
         {"prompt": "用 dịch vụ 和 chất lượng 描述酒店服务。", "targetVocab": "dịch vụ"},
         {"prompt": "用 khiếu nại 和 giải quyết 描述处理投诉。", "targetVocab": "khiếu nại"},
         {"prompt": "用 đánh giá 和 khách hàng 描述客户反馈。", "targetVocab": "đánh giá"},
     ],
     "final_reading_title": "阅读：越南酒店业指南", "final_reading_desc": "Ngành khách sạn Việt Nam phát triển nhanh.",
     "final_reading_text": "Ngành khách sạn Việt Nam phát triển nhanh. Khách sạn mới mở khắp nơi. Đặt phòng online rất tiện. Lễ tân chuyên nghiệp giúp nhận phòng nhanh. Phòng sạch sẽ, chất lượng cao. Dịch vụ tốt làm khách hàng hài lòng. Đánh giá tích cực thu hút khách mới. Giải quyết khiếu nại nhanh giữ uy tín. Trả phòng đúng giờ là quy tắc cơ bản.",
     "farewell_text": "恭喜你完成了越南酒店与服务业课程！让我们回顾12个词汇。\n\nKhách sạn——酒店，越南旅游业的支柱。\n\nPhòng——房间，旅行中最重要的空间。\n\nĐặt phòng——预订，提前 đặt phòng 省钱又省心。\n\nNhận phòng——入住，旅行的正式开始。\n\nTrả phòng——退房，记得检查行李。\n\nLễ tân——前台，你在酒店的第一个朋友。\n\nDịch vụ——服务，好的 dịch vụ 让旅行更完美。\n\nKhách hàng——客户，每个 khách hàng 都值得尊重。\n\nĐánh giá——评价，你的 đánh giá 帮助其他旅行者。\n\nChất lượng——质量，不要在 chất lượng 上妥协。\n\nGiải quyết——解决，遇到问题不要慌，总能 giải quyết。\n\nKhiếu nại——投诉，合理的 khiếu nại 是你的权利。\n\n你现在能用越南语处理酒店和服务场景了。无论是旅行还是工作，这些词汇都很实用！",
    },
    # ===== B4-1: 越南商务基础 =====
    {"series": "B4", "order": 1, "title": "越南商务基础",
     "description": "企业如同一台精密机器——而你连零件的名字都不知道。\n\n在越南做生意，不懂基本的商务词汇就像蒙着眼睛开车。合同、发票、预算——这些词你必须会说。\n\n这门课程教你12个越南商务中最基础的词汇，从公司运营到财务管理。\n\n掌握这些词汇，你就能用越南语参与商务讨论，而不是只能在旁边听。",
     "preview_text": "在越南做生意，不懂基本的商务词汇就像蒙着眼睛开车。这门课程教你12个商务基础词汇：从hợp đồng（合同）到hóa đơn（发票），从ngân sách（预算）到lợi nhuận（利润），从đầu tư（投资）到đối tác（合作伙伴），从sản phẩm（产品）到thị trường（市场），从xuất khẩu（出口）到nhập khẩu（进口），从đơn hàng（订单）到giao hàng（交货）。",
     "s1_vocab": ["hợp đồng", "hóa đơn", "ngân sách", "lợi nhuận", "đầu tư", "đối tác"],
     "s1_topic": "商务运营", "s1_intro_title": "介绍：商务运营", "s1_intro_desc": "学习6个越南商务运营的基础词汇。",
     "s1_intro_text": "欢迎来到越南商务基础课程！今天学习6个商务运营词汇。\n\n第一个词是 hợp đồng。Hợp đồng 是合同。你可以说：Ký hợp đồng，意思是「签合同」。\n\n第二个词是 hóa đơn。Hóa đơn 是发票。你可以说：Cho tôi hóa đơn，意思是「给我发票」。\n\n第三个词是 ngân sách。Ngân sách 是预算。你可以说：Ngân sách năm nay là bao nhiêu？意思是「今年的预算是多少？」\n\n第四个词是 lợi nhuận。Lợi nhuận 是利润。你可以说：Lợi nhuận tăng 20%，意思是「利润增长20%」。\n\n第五个词是 đầu tư。Đầu tư 是投资。你可以说：Đầu tư vào Việt Nam，意思是「投资越南」。\n\n第六个词是 đối tác。Đối tác 是合作伙伴。你可以说：Đối tác Nhật Bản，意思是「日本合作伙伴」。\n\n好的，让我们练习：hợp đồng, hóa đơn, ngân sách, lợi nhuận, đầu tư, đối tác。",
     "s1_reading_title": "阅读：商务运营", "s1_reading_desc": "Công ty ký hợp đồng với đối tác mới.",
     "s1_reading_text": "Công ty ký hợp đồng với đối tác mới. Hóa đơn được gửi qua email. Ngân sách năm nay tăng 15%. Lợi nhuận quý này rất tốt. Nhiều công ty nước ngoài đầu tư vào Việt Nam. Đối tác Hàn Quốc rất hài lòng.",
     "s1_writing_items": [
         {"prompt": "用 hợp đồng 写一个关于合同的句子。例句：Hợp đồng có hiệu lực từ ngày 1 tháng 1.", "targetVocab": "hợp đồng"},
         {"prompt": "用 hóa đơn 写一个关于发票的句子。例句：Hóa đơn điện tử rất tiện lợi.", "targetVocab": "hóa đơn"},
         {"prompt": "用 ngân sách 写一个关于预算的句子。例句：Ngân sách marketing năm nay là 1 tỷ đồng.", "targetVocab": "ngân sách"},
         {"prompt": "用 lợi nhuận 写一个关于利润的句子。例句：Lợi nhuận năm nay cao hơn năm ngoái.", "targetVocab": "lợi nhuận"},
         {"prompt": "用 đầu tư 写一个关于投资的句子。例句：Đầu tư vào giáo dục là đầu tư tốt nhất.", "targetVocab": "đầu tư"},
         {"prompt": "用 đối tác 写一个关于合作的句子。例句：Đối tác chiến lược giúp công ty phát triển.", "targetVocab": "đối tác"},
     ],
     "s2_vocab": ["sản phẩm", "thị trường", "xuất khẩu", "nhập khẩu", "đơn hàng", "giao hàng"],
     "s2_topic": "贸易基础", "s2_intro_title": "介绍：贸易基础", "s2_intro_desc": "学习6个关于贸易的基础词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：hợp đồng（合同）、hóa đơn（发票）、ngân sách（预算）、lợi nhuận（利润）、đầu tư（投资）和 đối tác（合作伙伴）。\n\n今天学习6个贸易基础词汇。\n\n第一个词是 sản phẩm。Sản phẩm 是产品。你可以说：Sản phẩm mới ra mắt，意思是「新产品上市」。\n\n第二个词是 thị trường。Thị trường 是市场。你可以说：Thị trường Việt Nam rất tiềm năng，意思是「越南市场很有潜力」。\n\n第三个词是 xuất khẩu。Xuất khẩu 是出口。你可以说：Việt Nam xuất khẩu gạo，意思是「越南出口大米」。\n\n第四个词是 nhập khẩu。Nhập khẩu 是进口。你可以说：Nhập khẩu máy móc từ Nhật，意思是「从日本进口机器」。\n\n第五个词是 đơn hàng。Đơn hàng 是订单。你可以说：Đơn hàng mới rất lớn，意思是「新订单很大」。\n\n第六个词是 giao hàng。Giao hàng 是交货、送货。你可以说：Giao hàng trong 3 ngày，意思是「3天内交货」。\n\n好的，让我们练习：sản phẩm, thị trường, xuất khẩu, nhập khẩu, đơn hàng, giao hàng。",
     "s2_reading_title": "阅读：越南贸易", "s2_reading_desc": "Sản phẩm Việt Nam xuất khẩu ra thế giới.",
     "s2_reading_text": "Sản phẩm Việt Nam xuất khẩu ra thế giới. Thị trường châu Âu rất lớn. Việt Nam nhập khẩu công nghệ cao. Đơn hàng tháng này tăng mạnh. Giao hàng đúng hạn rất quan trọng. Thị trường nội địa cũng phát triển.",
     "s2_writing_items": [
         {"prompt": "用 sản phẩm 写一个关于产品的句子。例句：Sản phẩm này được sản xuất tại Việt Nam.", "targetVocab": "sản phẩm"},
         {"prompt": "用 thị trường 写一个关于市场的句子。例句：Thị trường bất động sản đang nóng.", "targetVocab": "thị trường"},
         {"prompt": "用 xuất khẩu 写一个关于出口的句子。例句：Cà phê là mặt hàng xuất khẩu chính.", "targetVocab": "xuất khẩu"},
         {"prompt": "用 nhập khẩu 写一个关于进口的句子。例句：Nhập khẩu ô tô từ Hàn Quốc rất phổ biến.", "targetVocab": "nhập khẩu"},
         {"prompt": "用 đơn hàng 写一个关于订单的句子。例句：Đơn hàng online tăng mạnh trong mùa dịch.", "targetVocab": "đơn hàng"},
         {"prompt": "用 giao hàng 写一个关于送货的句子。例句：Giao hàng miễn phí cho đơn trên 500 nghìn.", "targetVocab": "giao hàng"},
     ],
     "review_intro_text": "你已经学完了12个越南商务基础词汇！\n\n第一课：hợp đồng（合同）、hóa đơn（发票）、ngân sách（预算）、lợi nhuận（利润）、đầu tư（投资）、đối tác（合作伙伴）。\n\n第二课：sản phẩm（产品）、thị trường（市场）、xuất khẩu（出口）、nhập khẩu（进口）、đơn hàng（订单）、giao hàng（交货）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：越南商务全景", "review_reading_desc": "Kinh doanh ở Việt Nam rất sôi động.",
     "review_reading_text": "Kinh doanh ở Việt Nam rất sôi động. Công ty ký hợp đồng với đối tác nước ngoài. Hóa đơn và ngân sách được quản lý chặt. Lợi nhuận tăng nhờ đầu tư đúng. Sản phẩm Việt Nam có mặt trên thị trường quốc tế. Xuất khẩu và nhập khẩu đều tăng. Đơn hàng nhiều, giao hàng đúng hạn.",
     "review_writing_items": [
         {"prompt": "用 hợp đồng 和 đối tác 描述商务合作。", "targetVocab": "hợp đồng"},
         {"prompt": "用 xuất khẩu 和 nhập khẩu 描述贸易。", "targetVocab": "xuất khẩu"},
         {"prompt": "用 sản phẩm 和 thị trường 描述市场策略。", "targetVocab": "sản phẩm"},
         {"prompt": "用 đơn hàng 和 giao hàng 描述订单流程。", "targetVocab": "đơn hàng"},
     ],
     "final_reading_title": "阅读：越南商务环境", "final_reading_desc": "Việt Nam là thị trường hấp dẫn.",
     "final_reading_text": "Việt Nam là thị trường hấp dẫn cho đầu tư. Đối tác quốc tế ngày càng nhiều. Hợp đồng thương mại tăng mạnh. Hóa đơn điện tử phổ biến. Ngân sách doanh nghiệp được quản lý tốt. Lợi nhuận các ngành đều tăng. Sản phẩm Việt Nam xuất khẩu đi nhiều nước. Nhập khẩu công nghệ giúp phát triển. Đơn hàng online bùng nổ. Giao hàng nhanh là lợi thế cạnh tranh.",
     "farewell_text": "恭喜你完成了越南商务基础课程！让我们回顾12个词汇。\n\nHợp đồng——合同，商务关系的法律基础。\n\nHóa đơn——发票，每笔交易的凭证。\n\nNgân sách——预算，企业运营的指南针。\n\nLợi nhuận——利润，企业存在的意义。\n\nĐầu tư——投资，用今天的钱换明天的回报。\n\nĐối tác——合作伙伴，好的 đối tác 让你走得更远。\n\nSản phẩm——产品，企业的核心竞争力。\n\nThị trường——市场，了解 thị trường 才能赢。\n\nXuất khẩu——出口，越南经济的引擎。\n\nNhập khẩu——进口，获取全球资源的渠道。\n\nĐơn hàng——订单，业务增长的直接指标。\n\nGiao hàng——交货，承诺的兑现。\n\n你现在能用越南语参与基本的商务讨论了。这是在越南商界立足的重要一步！",
    },
    # ===== B4-2: 越南国际贸易 =====
    {"series": "B4", "order": 2, "title": "越南国际贸易",
     "description": "越南已经签署了16个自由贸易协定——但你能用越南语解释其中任何一个吗？\n\n在越南的国际贸易领域，语言能力直接影响你的谈判筹码。不懂关税、清关、物流这些词，你就无法有效参与贸易讨论。\n\n这门课程教你12个国际贸易的核心词汇，从海关到物流，从关税到报关。\n\n用越南语谈贸易，你将在越南商界赢得更多尊重。",
     "preview_text": "越南已经签署了16个自由贸易协定，但你能用越南语解释其中任何一个吗？这门课程教你12个国际贸易词汇：从hải quan（海关）到thuế（税），从vận chuyển（运输）到kho（仓库），从container到cảng（港口），从thủ tục（手续）到giấy phép（许可证），从chứng từ（单据）到bảo hiểm（保险），从thanh toán（支付）到tỷ giá（汇率）。",
     "s1_vocab": ["hải quan", "thuế", "vận chuyển", "kho", "container", "cảng"],
     "s1_topic": "贸易物流", "s1_intro_title": "介绍：贸易物流", "s1_intro_desc": "学习6个越南贸易物流的基础词汇。",
     "s1_intro_text": "欢迎来到越南国际贸易课程！今天学习6个贸易物流词汇。\n\n第一个词是 hải quan。Hải quan 是海关。你可以说：Hải quan kiểm tra hàng hóa，意思是「海关检查货物」。\n\n第二个词是 thuế。Thuế 是税。你可以说：Thuế nhập khẩu là bao nhiêu？意思是「进口税是多少？」\n\n第三个词是 vận chuyển。Vận chuyển 是运输。你可以说：Vận chuyển bằng đường biển，意思是「海运」。\n\n第四个词是 kho。Kho 是仓库。你可以说：Hàng đang ở trong kho，意思是「货在仓库里」。\n\n第五个词是 container。Container 在越南语中和英语一样。你可以说：Một container 40 feet，意思是「一个40英尺集装箱」。\n\n第六个词是 cảng。Cảng 是港口。你可以说：Cảng Sài Gòn rất lớn，意思是「西贡港很大」。\n\n好的，让我们练习：hải quan, thuế, vận chuyển, kho, container, cảng。",
     "s1_reading_title": "阅读：贸易物流", "s1_reading_desc": "Hàng hóa đến cảng Sài Gòn.",
     "s1_reading_text": "Hàng hóa đến cảng Sài Gòn. Container được kiểm tra ở hải quan. Thuế nhập khẩu đã được tính. Vận chuyển từ cảng đến kho mất 2 giờ. Kho hàng ở khu công nghiệp. Container được dỡ hàng nhanh chóng.",
     "s1_writing_items": [
         {"prompt": "用 hải quan 写一个关于海关的句子。例句：Hải quan Việt Nam ngày càng hiện đại.", "targetVocab": "hải quan"},
         {"prompt": "用 thuế 写一个关于税的句子。例句：Thuế nhập khẩu ô tô ở Việt Nam rất cao.", "targetVocab": "thuế"},
         {"prompt": "用 vận chuyển 写一个关于运输的句子。例句：Vận chuyển hàng không nhanh nhưng đắt.", "targetVocab": "vận chuyển"},
         {"prompt": "用 kho 写一个关于仓库的句子。例句：Kho hàng cần được quản lý tốt.", "targetVocab": "kho"},
         {"prompt": "用 container 写一个关于集装箱的句子。例句：Mỗi ngày có hàng nghìn container qua cảng.", "targetVocab": "container"},
         {"prompt": "用 cảng 写一个关于港口的句子。例句：Cảng Hải Phòng là cảng lớn nhất miền Bắc.", "targetVocab": "cảng"},
     ],
     "s2_vocab": ["thủ tục", "giấy phép", "chứng từ", "bảo hiểm", "thanh toán", "tỷ giá"],
     "s2_topic": "贸易手续", "s2_intro_title": "介绍：贸易手续", "s2_intro_desc": "学习6个关于贸易手续的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：hải quan（海关）、thuế（税）、vận chuyển（运输）、kho（仓库）、container（集装箱）和 cảng（港口）。\n\n今天学习6个贸易手续词汇。\n\n第一个词是 thủ tục。Thủ tục 是手续。你可以说：Thủ tục hải quan phức tạp，意思是「海关手续复杂」。\n\n第二个词是 giấy phép。Giấy phép 是许可证。你可以说：Cần giấy phép nhập khẩu，意思是「需要进口许可证」。\n\n第三个词是 chứng từ。Chứng từ 是单据。你可以说：Chuẩn bị đầy đủ chứng từ，意思是「准备齐全单据」。\n\n第四个词是 bảo hiểm。Bảo hiểm 是保险。你可以说：Hàng hóa cần mua bảo hiểm，意思是「货物需要买保险」。\n\n第五个词是 thanh toán。Thanh toán 是支付。你可以说：Thanh toán bằng L/C，意思是「用信用证支付」。\n\n第六个词是 tỷ giá。Tỷ giá 是汇率。你可以说：Tỷ giá hôm nay thế nào？意思是「今天汇率怎样？」\n\n好的，让我们练习：thủ tục, giấy phép, chứng từ, bảo hiểm, thanh toán, tỷ giá。",
     "s2_reading_title": "阅读：贸易手续", "s2_reading_desc": "Thủ tục xuất khẩu cần nhiều chứng từ.",
     "s2_reading_text": "Thủ tục xuất khẩu cần nhiều chứng từ. Giấy phép xuất khẩu phải có trước. Hàng hóa cần mua bảo hiểm. Thanh toán qua ngân hàng quốc tế. Tỷ giá ảnh hưởng đến lợi nhuận. Chuẩn bị tốt thủ tục giúp giao hàng nhanh.",
     "s2_writing_items": [
         {"prompt": "用 thủ tục 写一个关于手续的句子。例句：Thủ tục thành lập công ty ở Việt Nam khá đơn giản.", "targetVocab": "thủ tục"},
         {"prompt": "用 giấy phép 写一个关于许可证的句子。例句：Giấy phép kinh doanh cần gia hạn mỗi năm.", "targetVocab": "giấy phép"},
         {"prompt": "用 chứng từ 写一个关于单据的句子。例句：Chứng từ xuất khẩu phải chính xác.", "targetVocab": "chứng từ"},
         {"prompt": "用 bảo hiểm 写一个关于保险的句子。例句：Bảo hiểm hàng hóa bảo vệ doanh nghiệp.", "targetVocab": "bảo hiểm"},
         {"prompt": "用 thanh toán 写一个关于支付的句子。例句：Thanh toán online ngày càng phổ biến.", "targetVocab": "thanh toán"},
         {"prompt": "用 tỷ giá 写一个关于汇率的句子。例句：Tỷ giá USD/VND hôm nay là 24.000.", "targetVocab": "tỷ giá"},
     ],
     "review_intro_text": "你已经学完了12个越南国际贸易词汇！\n\n第一课：hải quan（海关）、thuế（税）、vận chuyển（运输）、kho（仓库）、container（集装箱）、cảng（港口）。\n\n第二课：thủ tục（手续）、giấy phép（许可证）、chứng từ（单据）、bảo hiểm（保险）、thanh toán（支付）、tỷ giá（汇率）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：国际贸易全流程", "review_reading_desc": "Xuất khẩu hàng hóa cần nhiều bước.",
     "review_reading_text": "Xuất khẩu hàng hóa cần nhiều bước. Chuẩn bị chứng từ và giấy phép. Mua bảo hiểm cho hàng hóa. Vận chuyển đến kho rồi đến cảng. Container được kiểm tra ở hải quan. Thuế được tính theo tỷ giá. Thanh toán qua ngân hàng. Thủ tục hoàn tất, hàng lên tàu.",
     "review_writing_items": [
         {"prompt": "用 hải quan 和 thuế 描述通关过程。", "targetVocab": "hải quan"},
         {"prompt": "用 vận chuyển 和 cảng 描述物流。", "targetVocab": "vận chuyển"},
         {"prompt": "用 chứng từ 和 thủ tục 描述贸易手续。", "targetVocab": "chứng từ"},
         {"prompt": "用 thanh toán 和 tỷ giá 描述国际支付。", "targetVocab": "thanh toán"},
     ],
     "final_reading_title": "阅读：越南国际贸易概览", "final_reading_desc": "Việt Nam là nước xuất khẩu lớn.",
     "final_reading_text": "Việt Nam là nước xuất khẩu lớn ở Đông Nam Á. Hải quan hiện đại giúp thông quan nhanh. Thuế nhập khẩu giảm nhờ FTA. Vận chuyển đường biển qua cảng lớn. Container đi khắp thế giới từ kho Việt Nam. Thủ tục ngày càng đơn giản. Giấy phép có thể xin online. Chứng từ điện tử phổ biến. Bảo hiểm hàng hóa là bắt buộc. Thanh toán quốc tế thuận tiện. Tỷ giá ổn định giúp doanh nghiệp yên tâm.",
     "farewell_text": "恭喜你完成了越南国际贸易课程！让我们回顾12个词汇。\n\nHải quan——海关，国际贸易的守门人。\n\nThuế——税，了解 thuế 才能计算成本。\n\nVận chuyển——运输，贸易的血管。\n\nKho——仓库，货物的临时家。\n\nContainer——集装箱，全球贸易的标准单位。\n\nCảng——港口，连接越南与世界的门户。\n\nThủ tục——手续，耐心是最好的策略。\n\nGiấy phép——许可证，合法经营的基础。\n\nChứng từ——单据，每一张都很重要。\n\nBảo hiểm——保险，为意外做好准备。\n\nThanh toán——支付，交易的最后一步。\n\nTỷ giá——汇率，影响每一笔国际交易。\n\n你现在能用越南语讨论国际贸易了。在越南的商务世界里，这是非常有价值的能力！",
    },
    # ===== C1-1: 越南科学基础 =====
    {"series": "C1", "order": 1, "title": "越南科学基础",
     "description": "读越南语科学文章时感到迷茫？你不是一个人。\n\n科学词汇是大多数语言学习者最后才接触的领域，但如果你在越南从事科技工作或学术研究，这些词汇是你的日常。\n\n这门课程教你12个最基础的科学词汇，从实验到研究，从数据到结论。\n\n用越南语讨论科学，你将在学术圈中赢得更多认可。",
     "preview_text": "读越南语科学文章时感到迷茫？你不是一个人。这门课程教你12个科学基础词汇：从khoa học（科学）到nghiên cứu（研究），从thí nghiệm（实验）到kết quả（结果），从phát hiện（发现）到chứng minh（证明），从lý thuyết（理论）到thực hành（实践），从phương pháp（方法）到công nghệ（技术），从môi trường（环境）到năng lượng（能源）。",
     "s1_vocab": ["khoa học", "nghiên cứu", "thí nghiệm", "kết quả", "phát hiện", "chứng minh"],
     "s1_topic": "科学研究", "s1_intro_title": "介绍：科学研究", "s1_intro_desc": "学习6个越南科学研究的基础词汇。",
     "s1_intro_text": "欢迎来到越南科学基础课程！今天学习6个科学研究词汇。\n\n第一个词是 khoa học。Khoa học 是科学。你可以说：Khoa học rất quan trọng，意思是「科学很重要」。\n\n第二个词是 nghiên cứu。Nghiên cứu 是研究。你可以说：Tôi đang nghiên cứu，意思是「我正在做研究」。\n\n第三个词是 thí nghiệm。Thí nghiệm 是实验。你可以说：Thí nghiệm thành công，意思是「实验成功了」。\n\n第四个词是 kết quả。Kết quả 是结果。你可以说：Kết quả rất tốt，意思是「结果很好」。\n\n第五个词是 phát hiện。Phát hiện 是发现。你可以说：Phát hiện mới rất quan trọng，意思是「新发现很重要」。\n\n第六个词是 chứng minh。Chứng minh 是证明。你可以说：Cần chứng minh bằng dữ liệu，意思是「需要用数据证明」。\n\n好的，让我们练习：khoa học, nghiên cứu, thí nghiệm, kết quả, phát hiện, chứng minh。",
     "s1_reading_title": "阅读：科学研究", "s1_reading_desc": "Khoa học giúp con người hiểu thế giới.",
     "s1_reading_text": "Khoa học giúp con người hiểu thế giới. Nghiên cứu cần thời gian và kiên nhẫn. Thí nghiệm phải được lặp lại nhiều lần. Kết quả cần chính xác. Mỗi phát hiện mới mở ra cánh cửa mới. Nhà khoa học phải chứng minh bằng dữ liệu.",
     "s1_writing_items": [
         {"prompt": "用 khoa học 写一个关于科学的句子。例句：Khoa học và công nghệ thay đổi cuộc sống.", "targetVocab": "khoa học"},
         {"prompt": "用 nghiên cứu 写一个关于研究的句子。例句：Nghiên cứu y học cứu sống nhiều người.", "targetVocab": "nghiên cứu"},
         {"prompt": "用 thí nghiệm 写一个关于实验的句子。例句：Thí nghiệm trong phòng lab rất thú vị.", "targetVocab": "thí nghiệm"},
         {"prompt": "用 kết quả 写一个关于结果的句子。例句：Kết quả nghiên cứu được công bố trên tạp chí.", "targetVocab": "kết quả"},
         {"prompt": "用 phát hiện 写一个关于发现的句子。例句：Phát hiện thuốc mới mất nhiều năm.", "targetVocab": "phát hiện"},
         {"prompt": "用 chứng minh 写一个关于证明的句子。例句：Lý thuyết cần được chứng minh bằng thực nghiệm.", "targetVocab": "chứng minh"},
     ],
     "s2_vocab": ["lý thuyết", "thực hành", "phương pháp", "công nghệ", "môi trường", "năng lượng"],
     "s2_topic": "科学应用", "s2_intro_title": "介绍：科学应用", "s2_intro_desc": "学习6个关于科学应用的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：khoa học（科学）、nghiên cứu（研究）、thí nghiệm（实验）、kết quả（结果）、phát hiện（发现）和 chứng minh（证明）。\n\n今天学习6个科学应用词汇。\n\n第一个词是 lý thuyết。Lý thuyết 是理论。你可以说：Lý thuyết và thực hành đều quan trọng，意思是「理论和实践都重要」。\n\n第二个词是 thực hành。Thực hành 是实践。你可以说：Thực hành nhiều mới giỏi，意思是「多实践才能精通」。\n\n第三个词是 phương pháp。Phương pháp 是方法。你可以说：Phương pháp nghiên cứu rất quan trọng，意思是「研究方法很重要」。\n\n第四个词是 công nghệ。Công nghệ 是技术。你可以说：Công nghệ phát triển nhanh，意思是「技术发展很快」。\n\n第五个词是 môi trường。Môi trường 是环境。你可以说：Bảo vệ môi trường là trách nhiệm，意思是「保护环境是责任」。\n\n第六个词是 năng lượng。Năng lượng 是能源。你可以说：Năng lượng mặt trời rất sạch，意思是「太阳能很清洁」。\n\n好的，让我们练习：lý thuyết, thực hành, phương pháp, công nghệ, môi trường, năng lượng。",
     "s2_reading_title": "阅读：科学与生活", "s2_reading_desc": "Lý thuyết cần kết hợp với thực hành.",
     "s2_reading_text": "Lý thuyết cần kết hợp với thực hành. Phương pháp đúng giúp nghiên cứu hiệu quả. Công nghệ mới thay đổi cuộc sống. Bảo vệ môi trường là ưu tiên hàng đầu. Năng lượng sạch là tương lai. Khoa học giúp giải quyết nhiều vấn đề.",
     "s2_writing_items": [
         {"prompt": "用 lý thuyết 写一个关于理论的句子。例句：Lý thuyết Einstein thay đổi vật lý học.", "targetVocab": "lý thuyết"},
         {"prompt": "用 thực hành 写一个关于实践的句子。例句：Sinh viên cần thực hành nhiều hơn.", "targetVocab": "thực hành"},
         {"prompt": "用 phương pháp 写一个关于方法的句子。例句：Phương pháp học tiếng Việt hiệu quả nhất là gì?", "targetVocab": "phương pháp"},
         {"prompt": "用 công nghệ 写一个关于技术的句子。例句：Công nghệ AI đang thay đổi mọi ngành.", "targetVocab": "công nghệ"},
         {"prompt": "用 môi trường 写一个关于环境的句子。例句：Ô nhiễm môi trường là vấn đề nghiêm trọng.", "targetVocab": "môi trường"},
         {"prompt": "用 năng lượng 写一个关于能源的句子。例句：Năng lượng gió ngày càng phổ biến.", "targetVocab": "năng lượng"},
     ],
     "review_intro_text": "你已经学完了12个越南科学基础词汇！\n\n第一课：khoa học（科学）、nghiên cứu（研究）、thí nghiệm（实验）、kết quả（结果）、phát hiện（发现）、chứng minh（证明）。\n\n第二课：lý thuyết（理论）、thực hành（实践）、phương pháp（方法）、công nghệ（技术）、môi trường（环境）、năng lượng（能源）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：科学改变世界", "review_reading_desc": "Khoa học và công nghệ thay đổi thế giới.",
     "review_reading_text": "Khoa học và công nghệ thay đổi thế giới. Nghiên cứu cần phương pháp đúng. Thí nghiệm cho kết quả chính xác. Phát hiện mới cần được chứng minh. Lý thuyết kết hợp thực hành. Công nghệ giúp bảo vệ môi trường. Năng lượng sạch là tương lai.",
     "review_writing_items": [
         {"prompt": "用 khoa học 和 nghiên cứu 描述科学研究。", "targetVocab": "khoa học"},
         {"prompt": "用 lý thuyết 和 thực hành 描述学习方法。", "targetVocab": "lý thuyết"},
         {"prompt": "用 công nghệ 和 môi trường 描述绿色科技。", "targetVocab": "công nghệ"},
         {"prompt": "用 phát hiện 和 kết quả 描述研究成果。", "targetVocab": "phát hiện"},
     ],
     "final_reading_title": "阅读：越南科学发展", "final_reading_desc": "Việt Nam đầu tư mạnh vào khoa học.",
     "final_reading_text": "Việt Nam đầu tư mạnh vào khoa học. Nghiên cứu được hỗ trợ nhiều hơn. Thí nghiệm hiện đại cho kết quả tốt. Nhiều phát hiện mới được chứng minh. Lý thuyết kết hợp thực hành trong giáo dục. Phương pháp giảng dạy đổi mới. Công nghệ phát triển nhanh chóng. Bảo vệ môi trường là ưu tiên. Năng lượng tái tạo ngày càng phổ biến.",
     "farewell_text": "恭喜你完成了越南科学基础课程！让我们回顾12个词汇。\n\nKhoa học——科学，人类进步的引擎。\n\nNghiên cứu——研究，探索未知的过程。\n\nThí nghiệm——实验，验证假设的方法。\n\nKết quả——结果，研究的产出。\n\nPhát hiện——发现，科学最激动人心的时刻。\n\nChứng minh——证明，让发现成为知识。\n\nLý thuyết——理论，理解世界的框架。\n\nThực hành——实践，将知识变为能力。\n\nPhương pháp——方法，做事的正确方式。\n\nCông nghệ——技术，改变生活的力量。\n\nMôi trường——环境，我们共同的家。\n\nNăng lượng——能源，驱动一切的动力。\n\n你现在能用越南语讨论基础科学话题了。这是学术交流的重要一步！",
    },
    # ===== C1-2: 越南计算机科学 =====
    {"series": "C1", "order": 2, "title": "越南计算机科学", "description": "人工智能、大数据、云计算——这些词你用中文说得很溜，但用越南语呢？\n\n在越南的科技公司里，技术讨论越来越多地使用越南语。如果你只会用英语谈技术，你就会错过很多重要的对话。\n\n这门课程教你12个计算机科学的核心词汇，从算法到数据库，从人工智能到云计算。\n\n用越南语谈论计算机科学，展示你的双语技术能力。", "preview_text": "人工智能、大数据、云计算——这些词你用中文说得很溜，但用越南语呢？这门课程教你12个计算机科学词汇：从thuật toán（算法）到cơ sở dữ liệu（数据库），从trí tuệ nhân tạo（人工智能）到điện toán đám mây（云计算），从máy tính（计算机）到internet，从trang web（网站）到tải xuống（下载），从tải lên（上传）到lưu trữ（存储），从mã hóa（加密）到giải mã（解密）。",
     "s1_vocab": ["thuật toán", "cơ sở dữ liệu", "trí tuệ nhân tạo", "điện toán đám mây", "máy tính", "internet"], "s1_topic": "计算机核心", "s1_intro_title": "介绍：计算机核心", "s1_intro_desc": "学习6个计算机科学的核心词汇。",
     "s1_intro_text": "欢迎来到越南计算机科学课程！今天学习6个核心词汇。\n\n第一个词是 thuật toán。Thuật toán 是算法。你可以说：Thuật toán này rất hiệu quả，意思是「这个算法很高效」。\n\n第二个词是 cơ sở dữ liệu。Cơ sở dữ liệu 是数据库。你可以说：Cơ sở dữ liệu rất lớn，意思是「数据库很大」。\n\n第三个词是 trí tuệ nhân tạo。Trí tuệ nhân tạo 是人工智能，简称 AI。你可以说：Trí tuệ nhân tạo thay đổi thế giới，意思是「人工智能改变世界」。\n\n第四个词是 điện toán đám mây。Điện toán đám mây 是云计算。你可以说：Dữ liệu lưu trên điện toán đám mây，意思是「数据存在云上」。\n\n第五个词是 máy tính。Máy tính 是计算机。你可以说：Máy tính xách tay rất tiện，意思是「笔记本电脑很方便」。\n\n第六个词是 internet。Internet 在越南语中和英语一样。你可以说：Internet ở Việt Nam rất nhanh，意思是「越南的网络很快」。\n\n好的，让我们练习：thuật toán, cơ sở dữ liệu, trí tuệ nhân tạo, điện toán đám mây, máy tính, internet。",
     "s1_reading_title": "阅读：计算机科学", "s1_reading_desc": "Thuật toán là nền tảng của khoa học máy tính.", "s1_reading_text": "Thuật toán là nền tảng của khoa học máy tính. Cơ sở dữ liệu lưu trữ thông tin quan trọng. Trí tuệ nhân tạo ngày càng thông minh. Điện toán đám mây giúp tiết kiệm chi phí. Máy tính hiện đại rất mạnh. Internet kết nối mọi người trên thế giới.",
     "s1_writing_items": [{"prompt": "用 thuật toán 写一个关于算法的句子。例句：Thuật toán tìm kiếm Google rất phức tạp.", "targetVocab": "thuật toán"}, {"prompt": "用 cơ sở dữ liệu 写一个关于数据库的句子。例句：Cơ sở dữ liệu khách hàng cần bảo mật.", "targetVocab": "cơ sở dữ liệu"}, {"prompt": "用 trí tuệ nhân tạo 写一个关于AI的句子。例句：Trí tuệ nhân tạo giúp chẩn đoán bệnh.", "targetVocab": "trí tuệ nhân tạo"}, {"prompt": "用 điện toán đám mây 写一个关于云计算的句子。例句：Điện toán đám mây giúp làm việc từ xa.", "targetVocab": "điện toán đám mây"}, {"prompt": "用 máy tính 写一个关于电脑的句子。例句：Máy tính bảng phổ biến ở Việt Nam.", "targetVocab": "máy tính"}, {"prompt": "用 internet 写一个关于网络的句子。例句：Internet tốc độ cao phủ sóng toàn Việt Nam.", "targetVocab": "internet"}],
     "s2_vocab": ["trang web", "tải xuống", "tải lên", "lưu trữ", "mã hóa", "giải mã"], "s2_topic": "数字操作", "s2_intro_title": "介绍：数字操作", "s2_intro_desc": "学习6个关于数字操作的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：thuật toán（算法）、cơ sở dữ liệu（数据库）、trí tuệ nhân tạo（人工智能）、điện toán đám mây（云计算）、máy tính（计算机）和 internet。\n\n今天学习6个数字操作词汇。\n\n第一个词是 trang web。Trang web 是网站。你可以说：Trang web này rất đẹp，意思是「这个网站很漂亮」。\n\n第二个词是 tải xuống。Tải xuống 是下载。你可以说：Tải xuống ứng dụng，意思是「下载应用」。\n\n第三个词是 tải lên。Tải lên 是上传。你可以说：Tải lên file，意思是「上传文件」。\n\n第四个词是 lưu trữ。Lưu trữ 是存储。你可以说：Lưu trữ dữ liệu trên cloud，意思是「在云上存储数据」。\n\n第五个词是 mã hóa。Mã hóa 是加密。你可以说：Dữ liệu được mã hóa，意思是「数据被加密了」。\n\n第六个词是 giải mã。Giải mã 是解密。你可以说：Giải mã thông tin，意思是「解密信息」。\n\n好的，让我们练习：trang web, tải xuống, tải lên, lưu trữ, mã hóa, giải mã。",
     "s2_reading_title": "阅读：数字世界", "s2_reading_desc": "Trang web là cửa sổ vào thế giới số.", "s2_reading_text": "Trang web là cửa sổ vào thế giới số. Tải xuống nhạc và phim rất dễ. Tải lên ảnh lên mạng xã hội. Lưu trữ dữ liệu trên đám mây an toàn. Mã hóa bảo vệ thông tin cá nhân. Chỉ người có quyền mới giải mã được.",
     "s2_writing_items": [{"prompt": "用 trang web 写一个关于网站的句子。例句：Trang web của công ty cần cập nhật.", "targetVocab": "trang web"}, {"prompt": "用 tải xuống 写一个关于下载的句子。例句：Tải xuống phần mềm miễn phí.", "targetVocab": "tải xuống"}, {"prompt": "用 tải lên 写一个关于上传的句子。例句：Tải lên video lên YouTube.", "targetVocab": "tải lên"}, {"prompt": "用 lưu trữ 写一个关于存储的句子。例句：Lưu trữ ảnh trên Google Drive.", "targetVocab": "lưu trữ"}, {"prompt": "用 mã hóa 写一个关于加密的句子。例句：Mã hóa tin nhắn để bảo mật.", "targetVocab": "mã hóa"}, {"prompt": "用 giải mã 写一个关于解密的句子。例句：Giải mã file cần mật khẩu.", "targetVocab": "giải mã"}],
     "review_intro_text": "你已经学完了12个越南计算机科学词汇！\n\n第一课：thuật toán（算法）、cơ sở dữ liệu（数据库）、trí tuệ nhân tạo（人工智能）、điện toán đám mây（云计算）、máy tính（计算机）、internet。\n\n第二课：trang web（网站）、tải xuống（下载）、tải lên（上传）、lưu trữ（存储）、mã hóa（加密）、giải mã（解密）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：数字时代", "review_reading_desc": "Máy tính và internet thay đổi cuộc sống.", "review_reading_text": "Máy tính và internet thay đổi cuộc sống. Thuật toán và trí tuệ nhân tạo ngày càng thông minh. Cơ sở dữ liệu lưu trữ trên điện toán đám mây. Trang web là nơi tải xuống và tải lên thông tin. Mã hóa bảo vệ dữ liệu. Chỉ người có quyền mới giải mã.",
     "review_writing_items": [{"prompt": "用 thuật toán 和 trí tuệ nhân tạo 描述AI技术。", "targetVocab": "thuật toán"}, {"prompt": "用 tải xuống 和 tải lên 描述数字操作。", "targetVocab": "tải xuống"}, {"prompt": "用 mã hóa 和 giải mã 描述数据安全。", "targetVocab": "mã hóa"}, {"prompt": "用 máy tính 和 internet 描述数字生活。", "targetVocab": "máy tính"}],
     "final_reading_title": "阅读：越南数字化转型", "final_reading_desc": "Việt Nam đang chuyển đổi số mạnh mẽ.", "final_reading_text": "Việt Nam đang chuyển đổi số mạnh mẽ. Thuật toán và trí tuệ nhân tạo được ứng dụng rộng rãi. Cơ sở dữ liệu quốc gia đang được xây dựng. Điện toán đám mây phổ biến trong doanh nghiệp. Máy tính và internet có mặt ở mọi nơi. Trang web chính phủ phục vụ người dân. Tải xuống và tải lên dữ liệu nhanh chóng. Lưu trữ an toàn với mã hóa hiện đại. Giải mã chỉ dành cho người có quyền.",
     "farewell_text": "恭喜你完成了越南计算机科学课程！让我们回顾12个词汇。\n\nThuật toán——算法，计算机思考的方式。\n\nCơ sở dữ liệu——数据库，信息的宝库。\n\nTrí tuệ nhân tạo——人工智能，未来已来。\n\nĐiện toán đám mây——云计算，无处不在的计算力。\n\nMáy tính——计算机，现代生活的必需品。\n\nInternet——互联网，连接世界的桥梁。\n\nTrang web——网站，数字世界的门户。\n\nTải xuống——下载，获取信息的方式。\n\nTải lên——上传，分享内容的方式。\n\nLưu trữ——存储，保存数据的方法。\n\nMã hóa——加密，保护隐私的盾牌。\n\nGiải mã——解密，打开信息的钥匙。\n\n你现在能用越南语讨论计算机科学了。在越南的科技圈里，这是非常有价值的能力！",
    },
    # ===== C2-1: 越南经济基础 =====
    {"series": "C2", "order": 1, "title": "越南经济基础", "description": "越南是东南亚增长最快的经济体之一——但大多数学习者忽略了经济词汇。\n\n如果你在越南从事商业或金融工作，不懂GDP、通胀、利率这些词，你就无法参与任何有深度的经济讨论。\n\n这门课程教你12个最基础的经济词汇，帮你用越南语理解和讨论经济话题。\n\n从宏观到微观，这些词汇是你理解越南经济的钥匙。", "preview_text": "越南是东南亚增长最快的经济体之一，但大多数学习者忽略了经济词汇。这门课程教你12个经济基础词汇：从kinh tế（经济）到tăng trưởng（增长），从lạm phát（通胀）到lãi suất（利率），从GDP到thu nhập（收入），从chi tiêu（支出）到tiết kiệm（储蓄），从ngân hàng trung ương（央行）到chính sách（政策），从thất nghiệp（失业）到việc làm（就业）。",
     "s1_vocab": ["kinh tế", "tăng trưởng", "lạm phát", "lãi suất", "gdp", "thu nhập"], "s1_topic": "宏观经济", "s1_intro_title": "介绍：宏观经济", "s1_intro_desc": "学习6个越南宏观经济的基础词汇。",
     "s1_intro_text": "欢迎来到越南经济基础课程！今天学习6个宏观经济词汇。\n\n第一个词是 kinh tế。Kinh tế 是经济。你可以说：Kinh tế Việt Nam phát triển nhanh，意思是「越南经济发展很快」。\n\n第二个词是 tăng trưởng。Tăng trưởng 是增长。你可以说：Tăng trưởng GDP là 7%，意思是「GDP增长7%」。\n\n第三个词是 lạm phát。Lạm phát 是通货膨胀。你可以说：Lạm phát ở mức thấp，意思是「通胀处于低水平」。\n\n第四个词是 lãi suất。Lãi suất 是利率。你可以说：Lãi suất ngân hàng giảm，意思是「银行利率下降」。\n\n第五个词是 GDP。GDP 在越南语中和英语一样。你可以说：GDP Việt Nam tăng mạnh，意思是「越南GDP大幅增长」。\n\n第六个词是 thu nhập。Thu nhập 是收入。你可以说：Thu nhập bình quân tăng，意思是「平均收入增长」。\n\n好的，让我们练习：kinh tế, tăng trưởng, lạm phát, lãi suất, gdp, thu nhập。",
     "s1_reading_title": "阅读：越南经济", "s1_reading_desc": "Kinh tế Việt Nam phát triển mạnh.", "s1_reading_text": "Kinh tế Việt Nam phát triển mạnh. Tăng trưởng GDP đạt 7% năm ngoái. Lạm phát được kiểm soát tốt. Lãi suất ngân hàng ổn định. GDP bình quân đầu người tăng. Thu nhập người dân ngày càng cao.",
     "s1_writing_items": [{"prompt": "用 kinh tế 写一个关于经济的句子。例句：Kinh tế số là xu hướng mới.", "targetVocab": "kinh tế"}, {"prompt": "用 tăng trưởng 写一个关于增长的句子。例句：Tăng trưởng kinh tế giúp giảm nghèo.", "targetVocab": "tăng trưởng"}, {"prompt": "用 lạm phát 写一个关于通胀的句子。例句：Lạm phát cao ảnh hưởng đến đời sống.", "targetVocab": "lạm phát"}, {"prompt": "用 lãi suất 写一个关于利率的句子。例句：Lãi suất tiết kiệm hiện nay là 5%.", "targetVocab": "lãi suất"}, {"prompt": "用 gdp 写一个关于GDP的句子。例句：GDP Việt Nam đứng thứ 5 ASEAN.", "targetVocab": "gdp"}, {"prompt": "用 thu nhập 写一个关于收入的句子。例句：Thu nhập ở thành phố cao hơn nông thôn.", "targetVocab": "thu nhập"}],
     "s2_vocab": ["chi tiêu", "tiết kiệm", "ngân hàng trung ương", "chính sách", "thất nghiệp", "việc làm"], "s2_topic": "经济政策", "s2_intro_title": "介绍：经济政策", "s2_intro_desc": "学习6个关于经济政策的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：kinh tế（经济）、tăng trưởng（增长）、lạm phát（通胀）、lãi suất（利率）、GDP 和 thu nhập（收入）。\n\n今天学习6个经济政策词汇。\n\n第一个词是 chi tiêu。Chi tiêu 是支出。你可以说：Chi tiêu chính phủ tăng，意思是「政府支出增加」。\n\n第二个词是 tiết kiệm。Tiết kiệm 是储蓄。你可以说：Người Việt Nam thích tiết kiệm，意思是「越南人喜欢储蓄」。\n\n第三个词是 ngân hàng trung ương。Ngân hàng trung ương 是央行。你可以说：Ngân hàng trung ương điều chỉnh lãi suất，意思是「央行调整利率」。\n\n第四个词是 chính sách。Chính sách 是政策。你可以说：Chính sách kinh tế mới，意思是「新经济政策」。\n\n第五个词是 thất nghiệp。Thất nghiệp 是失业。你可以说：Tỷ lệ thất nghiệp thấp，意思是「失业率低」。\n\n第六个词是 việc làm。Việc làm 是就业。你可以说：Tạo việc làm cho thanh niên，意思是「为年轻人创造就业」。\n\n好的，让我们练习：chi tiêu, tiết kiệm, ngân hàng trung ương, chính sách, thất nghiệp, việc làm。",
     "s2_reading_title": "阅读：经济政策", "s2_reading_desc": "Chính sách kinh tế ảnh hưởng đến mọi người.", "s2_reading_text": "Chính sách kinh tế ảnh hưởng đến mọi người. Chi tiêu hợp lý giúp tiết kiệm. Ngân hàng trung ương quản lý lãi suất. Chính sách tốt giảm thất nghiệp. Việc làm mới được tạo ra mỗi năm. Tiết kiệm giúp gia đình ổn định.",
     "s2_writing_items": [{"prompt": "用 chi tiêu 写一个关于支出的句子。例句：Chi tiêu cho giáo dục rất quan trọng.", "targetVocab": "chi tiêu"}, {"prompt": "用 tiết kiệm 写一个关于储蓄的句子。例句：Tiết kiệm 20% thu nhập mỗi tháng.", "targetVocab": "tiết kiệm"}, {"prompt": "用 ngân hàng trung ương 写一个关于央行的句子。例句：Ngân hàng trung ương in tiền.", "targetVocab": "ngân hàng trung ương"}, {"prompt": "用 chính sách 写一个关于政策的句子。例句：Chính sách mới hỗ trợ doanh nghiệp nhỏ.", "targetVocab": "chính sách"}, {"prompt": "用 thất nghiệp 写一个关于失业的句子。例句：Thất nghiệp ở thanh niên là vấn đề lớn.", "targetVocab": "thất nghiệp"}, {"prompt": "用 việc làm 写一个关于就业的句子。例句：Việc làm trong ngành IT rất nhiều.", "targetVocab": "việc làm"}],
     "review_intro_text": "你已经学完了12个越南经济基础词汇！\n\n第一课：kinh tế（经济）、tăng trưởng（增长）、lạm phát（通胀）、lãi suất（利率）、GDP、thu nhập（收入）。\n\n第二课：chi tiêu（支出）、tiết kiệm（储蓄）、ngân hàng trung ương（央行）、chính sách（政策）、thất nghiệp（失业）、việc làm（就业）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：越南经济全景", "review_reading_desc": "Kinh tế Việt Nam đang trên đà phát triển.", "review_reading_text": "Kinh tế Việt Nam đang trên đà phát triển. Tăng trưởng GDP ổn định. Lạm phát được kiểm soát. Lãi suất hợp lý. Thu nhập người dân tăng. Chi tiêu và tiết kiệm cân bằng. Ngân hàng trung ương có chính sách tốt. Thất nghiệp giảm, việc làm tăng.",
     "review_writing_items": [{"prompt": "用 kinh tế 和 tăng trưởng 描述越南经济。", "targetVocab": "kinh tế"}, {"prompt": "用 chi tiêu 和 tiết kiệm 描述理财。", "targetVocab": "chi tiêu"}, {"prompt": "用 chính sách 和 việc làm 描述就业政策。", "targetVocab": "chính sách"}, {"prompt": "用 lạm phát 和 lãi suất 描述货币政策。", "targetVocab": "lạm phát"}],
     "final_reading_title": "阅读：越南经济展望", "final_reading_desc": "Tương lai kinh tế Việt Nam rất sáng.", "final_reading_text": "Tương lai kinh tế Việt Nam rất sáng. Tăng trưởng GDP dự kiến cao. Lạm phát được kiểm soát tốt. Lãi suất ổn định giúp doanh nghiệp. Thu nhập bình quân tăng mỗi năm. Chi tiêu công hiệu quả. Tiết kiệm quốc gia tăng. Ngân hàng trung ương có chính sách linh hoạt. Thất nghiệp giảm nhờ tạo nhiều việc làm.",
     "farewell_text": "恭喜你完成了越南经济基础课程！让我们回顾12个词汇。\n\nKinh tế——经济，理解一个国家的钥匙。\n\nTăng trưởng——增长，越南经济的主旋律。\n\nLạm phát——通胀，需要警惕的经济指标。\n\nLãi suất——利率，影响每个人的钱包。\n\nGDP——国内生产总值，衡量经济的标尺。\n\nThu nhập——收入，生活质量的基础。\n\nChi tiêu——支出，管理好 chi tiêu 很重要。\n\nTiết kiệm——储蓄，为未来做准备。\n\nNgân hàng trung ương——央行，经济的守护者。\n\nChính sách——政策，影响经济走向。\n\nThất nghiệp——失业，社会需要解决的问题。\n\nViệc làm——就业，每个人的基本需求。\n\n你现在能用越南语讨论基础经济话题了！",
    },
    # ===== C2-2: 越南金融市场 =====
    {"series": "C2", "order": 2, "title": "越南金融市场", "description": "越南股市在过去十年增长了超过300%——你能用越南语解释这个现象吗？\n\n金融市场是越南经济最活跃的领域之一。如果你想在越南投资或从事金融工作，这些词汇是你的必备工具。\n\n这门课程教你12个金融市场的核心词汇，从股票到债券，从基金到保险。\n\n用越南语谈论金融，你将在越南投资圈中更加自如。", "preview_text": "越南股市在过去十年增长了超过300%。这门课程教你12个金融市场词汇：从cổ phiếu（股票）到trái phiếu（债券），从quỹ đầu tư（基金）到bảo hiểm（保险），从chứng khoán（证券）到sàn giao dịch（交易所），从cổ tức（股息）到rủi ro（风险），从danh mục（投资组合）到lãi（利润），从lỗ（亏损）到vốn（资本）。",
     "s1_vocab": ["cổ phiếu", "trái phiếu", "quỹ đầu tư", "bảo hiểm", "chứng khoán", "sàn giao dịch"], "s1_topic": "金融工具", "s1_intro_title": "介绍：金融工具", "s1_intro_desc": "学习6个越南金融工具的词汇。",
     "s1_intro_text": "欢迎来到越南金融市场课程！今天学习6个金融工具词汇。\n\n第一个词是 cổ phiếu。Cổ phiếu 是股票。你可以说：Cổ phiếu VinGroup tăng giá，意思是「VinGroup股票涨了」。\n\n第二个词是 trái phiếu。Trái phiếu 是债券。你可以说：Trái phiếu chính phủ an toàn，意思是「政府债券安全」。\n\n第三个词是 quỹ đầu tư。Quỹ đầu tư 是投资基金。你可以说：Quỹ đầu tư nước ngoài vào Việt Nam，意思是「外国投资基金进入越南」。\n\n第四个词是 bảo hiểm。Bảo hiểm 是保险。你可以说：Mua bảo hiểm nhân thọ，意思是「买人寿保险」。\n\n第五个词是 chứng khoán。Chứng khoán 是证券。你可以说：Thị trường chứng khoán sôi động，意思是「证券市场活跃」。\n\n第六个词是 sàn giao dịch。Sàn giao dịch 是交易所。你可以说：Sàn giao dịch Hồ Chí Minh，意思是「胡志明交易所」。\n\n好的，让我们练习：cổ phiếu, trái phiếu, quỹ đầu tư, bảo hiểm, chứng khoán, sàn giao dịch。",
     "s1_reading_title": "阅读：越南金融市场", "s1_reading_desc": "Thị trường chứng khoán Việt Nam phát triển nhanh.", "s1_reading_text": "Thị trường chứng khoán Việt Nam phát triển nhanh. Cổ phiếu công nghệ tăng mạnh. Trái phiếu chính phủ ổn định. Quỹ đầu tư nước ngoài quan tâm. Bảo hiểm ngày càng phổ biến. Sàn giao dịch Hồ Chí Minh là lớn nhất.",
     "s1_writing_items": [{"prompt": "用 cổ phiếu 写一个关于股票的句子。例句：Cổ phiếu ngân hàng là lựa chọn an toàn.", "targetVocab": "cổ phiếu"}, {"prompt": "用 trái phiếu 写一个关于债券的句子。例句：Trái phiếu doanh nghiệp lãi suất cao hơn.", "targetVocab": "trái phiếu"}, {"prompt": "用 quỹ đầu tư 写一个关于基金的句子。例句：Quỹ đầu tư giúp đa dạng hóa danh mục.", "targetVocab": "quỹ đầu tư"}, {"prompt": "用 bảo hiểm 写一个关于保险的句子。例句：Bảo hiểm y tế là bắt buộc ở Việt Nam.", "targetVocab": "bảo hiểm"}, {"prompt": "用 chứng khoán 写一个关于证券的句子。例句：Công ty chứng khoán mở tài khoản miễn phí.", "targetVocab": "chứng khoán"}, {"prompt": "用 sàn giao dịch 写一个关于交易所的句子。例句：Sàn giao dịch mở cửa từ 9 giờ sáng.", "targetVocab": "sàn giao dịch"}],
     "s2_vocab": ["cổ tức", "rủi ro", "danh mục", "lãi", "lỗ", "vốn"], "s2_topic": "投资概念", "s2_intro_title": "介绍：投资概念", "s2_intro_desc": "学习6个关于投资概念的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：cổ phiếu（股票）、trái phiếu（债券）、quỹ đầu tư（基金）、bảo hiểm（保险）、chứng khoán（证券）和 sàn giao dịch（交易所）。\n\n今天学习6个投资概念词汇。\n\n第一个词是 cổ tức。Cổ tức 是股息。你可以说：Cổ tức năm nay cao，意思是「今年股息高」。\n\n第二个词是 rủi ro。Rủi ro 是风险。你可以说：Đầu tư luôn có rủi ro，意思是「投资总有风险」。\n\n第三个词是 danh mục。Danh mục 是投资组合。你可以说：Đa dạng hóa danh mục，意思是「分散投资组合」。\n\n第四个词是 lãi。Lãi 是利润、盈利。你可以说：Năm nay có lãi，意思是「今年盈利了」。\n\n第五个词是 lỗ。Lỗ 是亏损。你可以说：Tháng này bị lỗ，意思是「这个月亏损了」。\n\n第六个词是 vốn。Vốn 是资本。你可以说：Cần vốn để kinh doanh，意思是「做生意需要资本」。\n\n好的，让我们练习：cổ tức, rủi ro, danh mục, lãi, lỗ, vốn。",
     "s2_reading_title": "阅读：投资基础", "s2_reading_desc": "Đầu tư cần hiểu rủi ro.", "s2_reading_text": "Đầu tư cần hiểu rủi ro. Cổ tức là thu nhập từ cổ phiếu. Danh mục đa dạng giảm rủi ro. Có lãi thì vui, có lỗ thì học. Vốn ban đầu rất quan trọng. Đầu tư thông minh là chìa khóa.",
     "s2_writing_items": [{"prompt": "用 cổ tức 写一个关于股息的句子。例句：Cổ tức được trả mỗi quý.", "targetVocab": "cổ tức"}, {"prompt": "用 rủi ro 写一个关于风险的句子。例句：Rủi ro cao thì lợi nhuận cao.", "targetVocab": "rủi ro"}, {"prompt": "用 danh mục 写一个关于投资组合的句子。例句：Danh mục của tôi có cổ phiếu và trái phiếu.", "targetVocab": "danh mục"}, {"prompt": "用 lãi 写一个关于盈利的句子。例句：Năm ngoái tôi có lãi 20%.", "targetVocab": "lãi"}, {"prompt": "用 lỗ 写一个关于亏损的句子。例句：Lỗ là bài học quý giá.", "targetVocab": "lỗ"}, {"prompt": "用 vốn 写一个关于资本的句子。例句：Vốn đầu tư ban đầu là 100 triệu.", "targetVocab": "vốn"}],
     "review_intro_text": "你已经学完了12个越南金融市场词汇！\n\n第一课：cổ phiếu（股票）、trái phiếu（债券）、quỹ đầu tư（基金）、bảo hiểm（保险）、chứng khoán（证券）、sàn giao dịch（交易所）。\n\n第二课：cổ tức（股息）、rủi ro（风险）、danh mục（投资组合）、lãi（利润）、lỗ（亏损）、vốn（资本）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：金融市场全景", "review_reading_desc": "Thị trường chứng khoán Việt Nam ngày càng hấp dẫn.", "review_reading_text": "Thị trường chứng khoán Việt Nam ngày càng hấp dẫn. Cổ phiếu và trái phiếu đều tăng. Quỹ đầu tư nước ngoài đổ vốn vào. Bảo hiểm bảo vệ nhà đầu tư. Sàn giao dịch hiện đại. Cổ tức hấp dẫn. Rủi ro được quản lý tốt. Danh mục đa dạng. Có lãi nhiều hơn lỗ.",
     "review_writing_items": [{"prompt": "用 cổ phiếu 和 rủi ro 描述股票投资。", "targetVocab": "cổ phiếu"}, {"prompt": "用 lãi 和 lỗ 描述投资结果。", "targetVocab": "lãi"}, {"prompt": "用 danh mục 和 vốn 描述投资策略。", "targetVocab": "danh mục"}, {"prompt": "用 chứng khoán 和 sàn giao dịch 描述金融市场。", "targetVocab": "chứng khoán"}],
     "final_reading_title": "阅读：越南金融展望", "final_reading_desc": "Thị trường tài chính Việt Nam đầy tiềm năng.", "final_reading_text": "Thị trường tài chính Việt Nam đầy tiềm năng. Cổ phiếu công nghệ và ngân hàng dẫn đầu. Trái phiếu chính phủ an toàn cho nhà đầu tư mới. Quỹ đầu tư giúp đa dạng danh mục. Bảo hiểm bảo vệ tài sản. Chứng khoán giao dịch trên sàn hiện đại. Cổ tức hấp dẫn nhà đầu tư dài hạn. Quản lý rủi ro là chìa khóa. Có lãi hay lỗ đều là kinh nghiệm. Vốn đầu tư vào Việt Nam tăng mạnh.",
     "farewell_text": "恭喜你完成了越南金融市场课程！让我们回顾12个词汇。\n\nCổ phiếu——股票，最常见的投资工具。\n\nTrái phiếu——债券，稳定的收益来源。\n\nQuỹ đầu tư——基金，专业管理你的钱。\n\nBảo hiểm——保险，为风险做准备。\n\nChứng khoán——证券，金融市场的总称。\n\nSàn giao dịch——交易所，买卖证券的地方。\n\nCổ tức——股息，持有股票的回报。\n\nRủi ro——风险，投资的另一面。\n\nDanh mục——投资组合，不要把鸡蛋放在一个篮子里。\n\nLãi——利润，投资的目标。\n\nLỗ——亏损，投资的教训。\n\nVốn——资本，一切的起点。\n\n你现在能用越南语讨论金融市场了。在越南的投资圈里，这是非常有价值的能力！",
    },
    # ===== C3-1: 越南历史基础 =====
    {"series": "C3", "order": 1, "title": "越南历史基础", "description": "越南有4000年的历史——但你能用越南语说出任何一个朝代的名字吗？\n\n理解越南历史是理解越南人思维方式的关键。从抗法战争到革新开放，历史塑造了今天的越南。\n\n这门课程教你12个最基础的历史词汇，帮你用越南语讨论越南的过去和现在。\n\n历史不只是过去——它是理解现在的钥匙。", "preview_text": "越南有4000年的历史，但你能用越南语说出任何一个朝代的名字吗？这门课程教你12个历史基础词汇：从lịch sử（历史）到triều đại（朝代），从chiến tranh（战争）到hòa bình（和平），从độc lập（独立）到thống nhất（统一），从cách mạng（革命）到đổi mới（革新），从văn hóa（文化）到truyền thống（传统），从di tích（遗迹）到bảo tàng（博物馆）。",
     "s1_vocab": ["lịch sử", "triều đại", "chiến tranh", "hòa bình", "độc lập", "thống nhất"], "s1_topic": "历史事件", "s1_intro_title": "介绍：越南历史", "s1_intro_desc": "学习6个越南历史的基础词汇。",
     "s1_intro_text": "欢迎来到越南历史基础课程！今天学习6个历史词汇。\n\n第一个词是 lịch sử。Lịch sử 是历史。你可以说：Lịch sử Việt Nam rất phong phú，意思是「越南历史很丰富」。\n\n第二个词是 triều đại。Triều đại 是朝代。你可以说：Triều đại Nguyễn là triều đại cuối cùng，意思是「阮朝是最后一个朝代」。\n\n第三个词是 chiến tranh。Chiến tranh 是战争。你可以说：Chiến tranh đã kết thúc，意思是「战争已经结束」。\n\n第四个词是 hòa bình。Hòa bình 是和平。你可以说：Hòa bình là điều quý giá nhất，意思是「和平是最珍贵的」。\n\n第五个词是 độc lập。Độc lập 是独立。你可以说：Ngày Độc lập là 2 tháng 9，意思是「独立日是9月2日」。\n\n第六个词是 thống nhất。Thống nhất 是统一。你可以说：Đất nước thống nhất năm 1975，意思是「国家1975年统一」。\n\n好的，让我们练习：lịch sử, triều đại, chiến tranh, hòa bình, độc lập, thống nhất。",
     "s1_reading_title": "阅读：越南历史", "s1_reading_desc": "Lịch sử Việt Nam có hơn 4000 năm.", "s1_reading_text": "Lịch sử Việt Nam có hơn 4000 năm. Nhiều triều đại đã cai trị đất nước. Chiến tranh kéo dài nhiều thế kỷ. Hòa bình là ước mơ của mọi người. Việt Nam độc lập năm 1945. Đất nước thống nhất năm 1975.",
     "s1_writing_items": [{"prompt": "用 lịch sử 写一个关于历史的句子。例句：Học lịch sử giúp hiểu hiện tại.", "targetVocab": "lịch sử"}, {"prompt": "用 triều đại 写一个关于朝代的句子。例句：Triều đại Lý xây dựng Thăng Long.", "targetVocab": "triều đại"}, {"prompt": "用 chiến tranh 写一个关于战争的句子。例句：Chiến tranh gây ra nhiều đau khổ.", "targetVocab": "chiến tranh"}, {"prompt": "用 hòa bình 写一个关于和平的句子。例句：Hòa bình giúp đất nước phát triển.", "targetVocab": "hòa bình"}, {"prompt": "用 độc lập 写一个关于独立的句子。例句：Độc lập là quyền thiêng liêng.", "targetVocab": "độc lập"}, {"prompt": "用 thống nhất 写一个关于统一的句子。例句：Thống nhất đất nước là niềm tự hào.", "targetVocab": "thống nhất"}],
     "s2_vocab": ["cách mạng", "đổi mới", "văn hóa", "truyền thống", "di tích", "bảo tàng"], "s2_topic": "文化遗产", "s2_intro_title": "介绍：文化遗产", "s2_intro_desc": "学习6个关于文化遗产的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：lịch sử（历史）、triều đại（朝代）、chiến tranh（战争）、hòa bình（和平）、độc lập（独立）和 thống nhất（统一）。\n\n今天学习6个文化遗产词汇。\n\n第一个词是 cách mạng。Cách mạng 是革命。你可以说：Cách mạng tháng Tám năm 1945，意思是「1945年八月革命」。\n\n第二个词是 đổi mới。Đổi mới 是革新、改革开放。你可以说：Đổi mới bắt đầu năm 1986，意思是「革新从1986年开始」。\n\n第三个词是 văn hóa。Văn hóa 是文化。你可以说：Văn hóa Việt Nam rất đa dạng，意思是「越南文化很多样」。\n\n第四个词是 truyền thống。Truyền thống 是传统。你可以说：Truyền thống Tết rất quan trọng，意思是「春节传统很重要」。\n\n第五个词是 di tích。Di tích 是遗迹。你可以说：Di tích Huế rất đẹp，意思是「顺化遗迹很美」。\n\n第六个词是 bảo tàng。Bảo tàng 是博物馆。你可以说：Bảo tàng lịch sử ở Hà Nội，意思是「历史博物馆在河内」。\n\n好的，让我们练习：cách mạng, đổi mới, văn hóa, truyền thống, di tích, bảo tàng。",
     "s2_reading_title": "阅读：越南文化遗产", "s2_reading_desc": "Cách mạng tháng Tám thay đổi lịch sử.", "s2_reading_text": "Cách mạng tháng Tám thay đổi lịch sử. Đổi mới giúp kinh tế phát triển. Văn hóa Việt Nam phong phú. Truyền thống được gìn giữ qua nhiều thế hệ. Di tích lịch sử thu hút du khách. Bảo tàng kể câu chuyện của đất nước.",
     "s2_writing_items": [{"prompt": "用 cách mạng 写一个关于革命的句子。例句：Cách mạng mang lại tự do cho nhân dân.", "targetVocab": "cách mạng"}, {"prompt": "用 đổi mới 写一个关于改革的句子。例句：Đổi mới giúp Việt Nam hội nhập thế giới.", "targetVocab": "đổi mới"}, {"prompt": "用 văn hóa 写一个关于文化的句子。例句：Văn hóa ẩm thực Việt Nam nổi tiếng.", "targetVocab": "văn hóa"}, {"prompt": "用 truyền thống 写一个关于传统的句子。例句：Truyền thống gia đình rất quan trọng.", "targetVocab": "truyền thống"}, {"prompt": "用 di tích 写一个关于遗迹的句子。例句：Di tích Mỹ Sơn là di sản thế giới.", "targetVocab": "di tích"}, {"prompt": "用 bảo tàng 写一个关于博物馆的句子。例句：Bảo tàng chiến tranh ở Sài Gòn rất ấn tượng.", "targetVocab": "bảo tàng"}],
     "review_intro_text": "你已经学完了12个越南历史基础词汇！\n\n第一课：lịch sử（历史）、triều đại（朝代）、chiến tranh（战争）、hòa bình（和平）、độc lập（独立）、thống nhất（统一）。\n\n第二课：cách mạng（革命）、đổi mới（革新）、văn hóa（文化）、truyền thống（传统）、di tích（遗迹）、bảo tàng（博物馆）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：越南历史全景", "review_reading_desc": "Lịch sử Việt Nam là câu chuyện về kiên cường.", "review_reading_text": "Lịch sử Việt Nam là câu chuyện về kiên cường. Nhiều triều đại xây dựng đất nước. Chiến tranh không thể phá vỡ tinh thần. Hòa bình và độc lập là thành quả. Thống nhất đất nước là niềm tự hào. Cách mạng và đổi mới mở ra tương lai. Văn hóa và truyền thống được gìn giữ. Di tích và bảo tàng kể câu chuyện.",
     "review_writing_items": [{"prompt": "用 lịch sử 和 triều đại 描述越南历史。", "targetVocab": "lịch sử"}, {"prompt": "用 chiến tranh 和 hòa bình 描述越南的过去。", "targetVocab": "chiến tranh"}, {"prompt": "用 cách mạng 和 đổi mới 描述越南的变革。", "targetVocab": "cách mạng"}, {"prompt": "用 di tích 和 bảo tàng 描述文化遗产。", "targetVocab": "di tích"}],
     "final_reading_title": "阅读：越南历史之旅", "final_reading_desc": "Du lịch lịch sử ở Việt Nam rất thú vị.", "final_reading_text": "Du lịch lịch sử ở Việt Nam rất thú vị. Lịch sử 4000 năm với nhiều triều đại. Chiến tranh đã qua, hòa bình đã đến. Độc lập và thống nhất là nền tảng. Cách mạng và đổi mới thay đổi đất nước. Văn hóa và truyền thống sống mãi. Di tích lịch sử ở khắp nơi. Bảo tàng kể câu chuyện cho thế hệ sau.",
     "farewell_text": "恭喜你完成了越南历史基础课程！让我们回顾12个词汇。\n\nLịch sử——历史，理解越南的钥匙。\n\nTriều đại——朝代，越南文明的篇章。\n\nChiến tranh——战争，越南人民的伤痛。\n\nHòa bình——和平，最珍贵的礼物。\n\nĐộc lập——独立，越南人民的骄傲。\n\nThống nhất——统一，国家完整的象征。\n\nCách mạng——革命，改变命运的力量。\n\nĐổi mới——革新，越南腾飞的起点。\n\nVăn hóa——文化，民族的灵魂。\n\nTruyền thống——传统，代代相传的智慧。\n\nDi tích——遗迹，历史的见证。\n\nBảo tàng——博物馆，记忆的守护者。\n\n你现在能用越南语讨论历史话题了。理解历史，你就能更深地理解越南！",
    },
    # ===== C3-2, C4-1, C4-2, D1-1, D1-2, D2-1, D2-2, D3-1, D3-2, D4-1 =====
    # Remaining 10 definitions follow the same pattern
    {"series": "C3", "order": 2, "title": "越南政治制度", "description": "越南的政治制度与中国有相似之处，但也有很多独特的地方。\n\n如果你在越南工作或生活，理解基本的政治词汇能帮你读懂新闻、理解政策。\n\n这门课程教你12个最基础的政治词汇，从政府到国会，从法律到选举。\n\n用越南语理解政治，你将更深入地融入越南社会。", "preview_text": "越南的政治制度与中国有相似之处，但也有很多独特的地方。这门课程教你12个政治基础词汇：从chính phủ（政府）到quốc hội（国会），从luật（法律）到bầu cử（选举），从đảng（党）到nhà nước（国家），从công dân（公民）到quyền（权利），从hiến pháp（宪法）到dân chủ（民主），从ngoại giao（外交）到hợp tác（合作）。",
     "s1_vocab": ["chính phủ", "quốc hội", "luật", "bầu cử", "đảng", "nhà nước"], "s1_topic": "政治基础", "s1_intro_title": "介绍：越南政治", "s1_intro_desc": "学习6个越南政治的基础词汇。",
     "s1_intro_text": "欢迎来到越南政治制度课程！今天学习6个政治基础词汇。\n\n第一个词是 chính phủ。Chính phủ 是政府。你可以说：Chính phủ Việt Nam，意思是「越南政府」。\n\n第二个词是 quốc hội。Quốc hội 是国会。你可以说：Quốc hội họp hai lần một năm，意思是「国会一年开两次会」。\n\n第三个词是 luật。Luật 是法律。你可以说：Luật mới có hiệu lực，意思是「新法律生效了」。\n\n第四个词是 bầu cử。Bầu cử 是选举。你可以说：Bầu cử quốc hội，意思是「国会选举」。\n\n第五个词是 đảng。Đảng 是党。你可以说：Đảng Cộng sản Việt Nam，意思是「越南共产党」。\n\n第六个词是 nhà nước。Nhà nước 是国家。你可以说：Nhà nước Việt Nam，意思是「越南国家」。\n\n好的，让我们练习：chính phủ, quốc hội, luật, bầu cử, đảng, nhà nước。",
     "s1_reading_title": "阅读：越南政治", "s1_reading_desc": "Chính phủ Việt Nam quản lý đất nước.", "s1_reading_text": "Chính phủ Việt Nam quản lý đất nước. Quốc hội là cơ quan quyền lực cao nhất. Luật được quốc hội thông qua. Bầu cử diễn ra 5 năm một lần. Đảng lãnh đạo đất nước. Nhà nước phục vụ nhân dân.",
     "s1_writing_items": [{"prompt": "用 chính phủ 写一个关于政府的句子。例句：Chính phủ hỗ trợ doanh nghiệp nhỏ.", "targetVocab": "chính phủ"}, {"prompt": "用 quốc hội 写一个关于国会的句子。例句：Quốc hội thảo luận luật mới.", "targetVocab": "quốc hội"}, {"prompt": "用 luật 写一个关于法律的句子。例句：Luật giao thông cần được tuân thủ.", "targetVocab": "luật"}, {"prompt": "用 bầu cử 写一个关于选举的句子。例句：Bầu cử là quyền của mọi công dân.", "targetVocab": "bầu cử"}, {"prompt": "用 đảng 写一个关于党的句子。例句：Đảng lãnh đạo công cuộc đổi mới.", "targetVocab": "đảng"}, {"prompt": "用 nhà nước 写一个关于国家的句子。例句：Nhà nước bảo vệ quyền lợi công dân.", "targetVocab": "nhà nước"}],
     "s2_vocab": ["công dân", "quyền", "hiến pháp", "dân chủ", "ngoại giao", "hợp tác"], "s2_topic": "公民与外交", "s2_intro_title": "介绍：公民与外交", "s2_intro_desc": "学习6个关于公民权利和外交的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：chính phủ（政府）、quốc hội（国会）、luật（法律）、bầu cử（选举）、đảng（党）和 nhà nước（国家）。\n\n今天学习6个公民与外交词汇。\n\n第一个词是 công dân。Công dân 是公民。你可以说：Công dân có quyền bầu cử，意思是「公民有选举权」。\n\n第二个词是 quyền。Quyền 是权利。你可以说：Quyền con người，意思是「人权」。\n\n第三个词是 hiến pháp。Hiến pháp 是宪法。你可以说：Hiến pháp là luật cao nhất，意思是「宪法是最高法律」。\n\n第四个词是 dân chủ。Dân chủ 是民主。你可以说：Dân chủ là quyền của nhân dân，意思是「民主是人民的权利」。\n\n第五个词是 ngoại giao。Ngoại giao 是外交。你可以说：Ngoại giao Việt Nam rất tích cực，意思是「越南外交很积极」。\n\n第六个词是 hợp tác。Hợp tác 是合作。你可以说：Hợp tác quốc tế rất quan trọng，意思是「国际合作很重要」。\n\n好的，让我们练习：công dân, quyền, hiến pháp, dân chủ, ngoại giao, hợp tác。",
     "s2_reading_title": "阅读：公民与外交", "s2_reading_desc": "Công dân Việt Nam có nhiều quyền.", "s2_reading_text": "Công dân Việt Nam có nhiều quyền. Hiến pháp bảo vệ quyền con người. Dân chủ được thực hiện qua bầu cử. Ngoại giao Việt Nam mở rộng. Hợp tác với nhiều nước trên thế giới. Công dân tự hào về đất nước.",
     "s2_writing_items": [{"prompt": "用 công dân 写一个关于公民的句子。例句：Mỗi công dân có trách nhiệm với đất nước.", "targetVocab": "công dân"}, {"prompt": "用 quyền 写一个关于权利的句子。例句：Quyền tự do ngôn luận rất quan trọng.", "targetVocab": "quyền"}, {"prompt": "用 hiến pháp 写一个关于宪法的句子。例句：Hiến pháp Việt Nam được sửa đổi năm 2013.", "targetVocab": "hiến pháp"}, {"prompt": "用 dân chủ 写一个关于民主的句子。例句：Dân chủ cơ sở giúp người dân tham gia.", "targetVocab": "dân chủ"}, {"prompt": "用 ngoại giao 写一个关于外交的句子。例句：Ngoại giao đa phương là chính sách của Việt Nam.", "targetVocab": "ngoại giao"}, {"prompt": "用 hợp tác 写一个关于合作的句子。例句：Hợp tác Việt-Trung ngày càng phát triển.", "targetVocab": "hợp tác"}],
     "review_intro_text": "你已经学完了12个越南政治制度词汇！\n\n第一课：chính phủ（政府）、quốc hội（国会）、luật（法律）、bầu cử（选举）、đảng（党）、nhà nước（国家）。\n\n第二课：công dân（公民）、quyền（权利）、hiến pháp（宪法）、dân chủ（民主）、ngoại giao（外交）、hợp tác（合作）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：越南政治全景", "review_reading_desc": "Việt Nam là nhà nước pháp quyền.", "review_reading_text": "Việt Nam là nhà nước pháp quyền. Chính phủ quản lý theo luật. Quốc hội đại diện cho công dân. Bầu cử thể hiện dân chủ. Đảng lãnh đạo đất nước. Hiến pháp bảo vệ quyền con người. Ngoại giao và hợp tác quốc tế phát triển.",
     "review_writing_items": [{"prompt": "用 chính phủ 和 quốc hội 描述越南政治。", "targetVocab": "chính phủ"}, {"prompt": "用 công dân 和 quyền 描述公民权利。", "targetVocab": "công dân"}, {"prompt": "用 ngoại giao 和 hợp tác 描述国际关系。", "targetVocab": "ngoại giao"}, {"prompt": "用 luật 和 hiến pháp 描述法律体系。", "targetVocab": "luật"}],
     "final_reading_title": "阅读：越南政治发展", "final_reading_desc": "Chính trị Việt Nam ngày càng minh bạch.", "final_reading_text": "Chính trị Việt Nam ngày càng minh bạch. Chính phủ phục vụ nhân dân. Quốc hội thông qua luật mới. Bầu cử công bằng và dân chủ. Đảng lãnh đạo nhà nước. Công dân có quyền theo hiến pháp. Ngoại giao mở rộng. Hợp tác quốc tế sâu rộng.",
     "farewell_text": "恭喜你完成了越南政治制度课程！让我们回顾12个词汇。\n\nChính phủ——政府，管理国家的机构。\n\nQuốc hội——国会，最高权力机关。\n\nLuật——法律，社会秩序的基础。\n\nBầu cử——选举，民主的体现。\n\nĐảng——党，越南政治的核心。\n\nNhà nước——国家，人民的共同体。\n\nCông dân——公民，国家的主人。\n\nQuyền——权利，每个人都应享有。\n\nHiến pháp——宪法，最高法律。\n\nDân chủ——民主，人民当家作主。\n\nNgoại giao——外交，连接世界的桥梁。\n\nHợp tác——合作，共同发展的基础。\n\n你现在能用越南语讨论政治话题了！",
    },
    # C4-1, C4-2, D1-1, D1-2, D2-1, D2-2, D3-1, D3-2, D4-1 — remaining 9 definitions
    # These follow the exact same pattern as above. Adding them now:
    {"series": "C4", "order": 1, "title": "越南心理学基础", "description": "为什么孩子学语言比成人快？心理学有答案。\n\n心理学不只是学术话题——它影响着教育、职场和日常生活的方方面面。\n\n这门课程教你12个最基础的心理学词汇，帮你用越南语讨论心理和教育话题。\n\n理解心理学词汇，你将更深入地理解越南的教育文化。", "preview_text": "为什么孩子学语言比成人快？心理学有答案。这门课程教你12个心理学基础词汇：从tâm lý（心理）到hành vi（行为），从cảm xúc（情感）到trí nhớ（记忆），从học tập（学习）到phát triển（发展），从giáo dục（教育）到giáo viên（老师），从học sinh（学生）到trường học（学校），从bài tập（作业）到thi（考试）。",
     "s1_vocab": ["tâm lý", "hành vi", "cảm xúc", "trí nhớ", "học tập", "phát triển"], "s1_topic": "心理学基础", "s1_intro_title": "介绍：心理学", "s1_intro_desc": "学习6个心理学基础词汇。",
     "s1_intro_text": "欢迎来到越南心理学基础课程！今天学习6个心理学词汇。\n\n第一个词是 tâm lý。Tâm lý 是心理。你可以说：Tâm lý học rất thú vị，意思是「心理学很有趣」。\n\n第二个词是 hành vi。Hành vi 是行为。你可以说：Hành vi con người rất phức tạp，意思是「人类行为很复杂」。\n\n第三个词是 cảm xúc。Cảm xúc 是情感。你可以说：Cảm xúc ảnh hưởng đến quyết định，意思是「情感影响决策」。\n\n第四个词是 trí nhớ。Trí nhớ 是记忆。你可以说：Trí nhớ ngắn hạn và dài hạn，意思是「短期记忆和长期记忆」。\n\n第五个词是 học tập。Học tập 是学习。你可以说：Học tập suốt đời，意思是「终身学习」。\n\n第六个词是 phát triển。Phát triển 是发展。你可以说：Phát triển trí tuệ của trẻ em，意思是「儿童智力发展」。\n\n好的，让我们练习：tâm lý, hành vi, cảm xúc, trí nhớ, học tập, phát triển。",
     "s1_reading_title": "阅读：心理学入门", "s1_reading_desc": "Tâm lý học nghiên cứu hành vi con người.", "s1_reading_text": "Tâm lý học nghiên cứu hành vi con người. Cảm xúc ảnh hưởng đến cuộc sống. Trí nhớ giúp chúng ta học tập. Học tập là quá trình suốt đời. Trẻ em phát triển rất nhanh. Tâm lý tích cực giúp sống vui hơn.",
     "s1_writing_items": [{"prompt": "用 tâm lý 写一个关于心理的句子。例句：Tâm lý ổn định giúp làm việc hiệu quả.", "targetVocab": "tâm lý"}, {"prompt": "用 hành vi 写一个关于行为的句子。例句：Hành vi tốt cần được khen ngợi.", "targetVocab": "hành vi"}, {"prompt": "用 cảm xúc 写一个关于情感的句子。例句：Quản lý cảm xúc là kỹ năng quan trọng.", "targetVocab": "cảm xúc"}, {"prompt": "用 trí nhớ 写一个关于记忆的句子。例句：Trí nhớ tốt giúp học ngoại ngữ nhanh.", "targetVocab": "trí nhớ"}, {"prompt": "用 học tập 写一个关于学习的句子。例句：Học tập mỗi ngày giúp tiến bộ.", "targetVocab": "học tập"}, {"prompt": "用 phát triển 写一个关于发展的句子。例句：Phát triển bản thân là mục tiêu quan trọng.", "targetVocab": "phát triển"}],
     "s2_vocab": ["giáo dục", "giáo viên", "học sinh", "trường học", "bài tập", "thi"], "s2_topic": "教育基础", "s2_intro_title": "介绍：越南教育", "s2_intro_desc": "学习6个关于教育的基础词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：tâm lý（心理）、hành vi（行为）、cảm xúc（情感）、trí nhớ（记忆）、học tập（学习）和 phát triển（发展）。\n\n今天学习6个教育词汇。\n\n第一个词是 giáo dục。Giáo dục 是教育。你可以说：Giáo dục Việt Nam đang đổi mới，意思是「越南教育正在改革」。\n\n第二个词是 giáo viên。Giáo viên 是老师。你可以说：Giáo viên rất được tôn trọng，意思是「老师很受尊重」。\n\n第三个词是 học sinh。Học sinh 是学生。你可以说：Học sinh Việt Nam rất chăm chỉ，意思是「越南学生很勤奋」。\n\n第四个词是 trường học。Trường học 是学校。你可以说：Trường học gần nhà，意思是「学校离家近」。\n\n第五个词是 bài tập。Bài tập 是作业。你可以说：Bài tập hôm nay nhiều quá，意思是「今天作业太多了」。\n\n第六个词是 thi。Thi 是考试。你可以说：Thi cuối kỳ tuần sau，意思是「期末考试下周」。\n\n好的，让我们练习：giáo dục, giáo viên, học sinh, trường học, bài tập, thi。",
     "s2_reading_title": "阅读：越南教育", "s2_reading_desc": "Giáo dục ở Việt Nam rất được coi trọng.", "s2_reading_text": "Giáo dục ở Việt Nam rất được coi trọng. Giáo viên được xã hội tôn trọng. Học sinh đi học từ 6 tuổi. Trường học có ở khắp nơi. Bài tập giúp học sinh ôn luyện. Thi là cách đánh giá kết quả học tập.",
     "s2_writing_items": [{"prompt": "用 giáo dục 写一个关于教育的句子。例句：Giáo dục là nền tảng phát triển đất nước.", "targetVocab": "giáo dục"}, {"prompt": "用 giáo viên 写一个关于老师的句子。例句：Giáo viên dạy tiếng Việt rất kiên nhẫn.", "targetVocab": "giáo viên"}, {"prompt": "用 học sinh 写一个关于学生的句子。例句：Học sinh lớp 12 chuẩn bị thi đại học.", "targetVocab": "học sinh"}, {"prompt": "用 trường học 写一个关于学校的句子。例句：Trường học mới xây rất đẹp.", "targetVocab": "trường học"}, {"prompt": "用 bài tập 写一个关于作业的句子。例句：Làm bài tập mỗi ngày giúp nhớ lâu.", "targetVocab": "bài tập"}, {"prompt": "用 thi 写一个关于考试的句子。例句：Thi IELTS cần chuẩn bị kỹ.", "targetVocab": "thi"}],
     "review_intro_text": "你已经学完了12个越南心理学与教育词汇！\n\n第一课：tâm lý（心理）、hành vi（行为）、cảm xúc（情感）、trí nhớ（记忆）、học tập（学习）、phát triển（发展）。\n\n第二课：giáo dục（教育）、giáo viên（老师）、học sinh（学生）、trường học（学校）、bài tập（作业）、thi（考试）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：心理与教育", "review_reading_desc": "Tâm lý học giúp cải thiện giáo dục.", "review_reading_text": "Tâm lý học giúp cải thiện giáo dục. Hiểu hành vi và cảm xúc của học sinh. Trí nhớ tốt giúp học tập hiệu quả. Phát triển toàn diện là mục tiêu. Giáo viên cần hiểu tâm lý học sinh. Trường học là nơi phát triển. Bài tập và thi đánh giá kết quả.",
     "review_writing_items": [{"prompt": "用 tâm lý 和 hành vi 描述心理学。", "targetVocab": "tâm lý"}, {"prompt": "用 giáo dục 和 giáo viên 描述教育。", "targetVocab": "giáo dục"}, {"prompt": "用 học tập 和 trí nhớ 描述学习方法。", "targetVocab": "học tập"}, {"prompt": "用 học sinh 和 thi 描述学校生活。", "targetVocab": "học sinh"}],
     "final_reading_title": "阅读：越南教育展望", "final_reading_desc": "Giáo dục Việt Nam đang thay đổi.", "final_reading_text": "Giáo dục Việt Nam đang thay đổi. Tâm lý học được ứng dụng trong giảng dạy. Hiểu hành vi và cảm xúc giúp dạy tốt hơn. Trí nhớ và học tập được nghiên cứu sâu. Phát triển toàn diện cho học sinh. Giáo viên được đào tạo tốt hơn. Trường học hiện đại hơn. Bài tập sáng tạo hơn. Thi cử công bằng hơn.",
     "farewell_text": "恭喜你完成了越南心理学基础课程！让我们回顾12个词汇。\n\nTâm lý——心理，理解人的内心世界。\n\nHành vi——行为，心理的外在表现。\n\nCảm xúc——情感，生活的色彩。\n\nTrí nhớ——记忆，学习的基础。\n\nHọc tập——学习，终身的旅程。\n\nPhát triển——发展，不断进步。\n\nGiáo dục——教育，国家的未来。\n\nGiáo viên——老师，知识的传递者。\n\nHọc sinh——学生，未来的主人。\n\nTrường học——学校，成长的摇篮。\n\nBài tập——作业，巩固知识的方式。\n\nThi——考试，检验学习的标尺。\n\n你现在能用越南语讨论心理学和教育话题了！",
    },
    {"series": "C4", "order": 2, "title": "越南教育体系", "description": "越南学生在国际数学和科学竞赛中屡获佳绩——这背后是怎样的教育体系？\n\n理解越南的教育体系，你就能理解越南人的价值观和思维方式。\n\n这门课程教你12个关于教育体系的词汇，从幼儿园到大学，从学位到奖学金。\n\n用越南语谈论教育，你将更深入地融入越南社会。", "preview_text": "越南学生在国际竞赛中屡获佳绩，这背后是怎样的教育体系？这门课程教你12个教育体系词汇：从mẫu giáo（幼儿园）到tiểu học（小学），从trung học（中学）到đại học（大学），从bằng（学位）到học bổng（奖学金），从lớp（班级）到môn học（科目），从điểm（分数）到tốt nghiệp（毕业），从thạc sĩ（硕士）到tiến sĩ（博士）。",
     "s1_vocab": ["mẫu giáo", "tiểu học", "trung học", "đại học", "bằng", "học bổng"], "s1_topic": "教育层级", "s1_intro_title": "介绍：教育层级", "s1_intro_desc": "学习6个越南教育层级的词汇。",
     "s1_intro_text": "欢迎来到越南教育体系课程！今天学习6个教育层级词汇。\n\n第一个词是 mẫu giáo。Mẫu giáo 是幼儿园。你可以说：Con tôi đi mẫu giáo，意思是「我孩子上幼儿园」。\n\n第二个词是 tiểu học。Tiểu học 是小学。你可以说：Tiểu học 5 năm，意思是「小学5年」。\n\n第三个词是 trung học。Trung học 是中学。你可以说：Trung học cơ sở 4 năm，意思是「初中4年」。\n\n第四个词是 đại học。Đại học 是大学。你可以说：Đại học Quốc gia Hà Nội，意思是「河内国家大学」。\n\n第五个词是 bằng。Bằng 是学位、文凭。你可以说：Bằng đại học，意思是「大学学位」。\n\n第六个词是 học bổng。Học bổng 是奖学金。你可以说：Tôi nhận học bổng，意思是「我获得了奖学金」。\n\n好的，让我们练习：mẫu giáo, tiểu học, trung học, đại học, bằng, học bổng。",
     "s1_reading_title": "阅读：越南教育层级", "s1_reading_desc": "Hệ thống giáo dục Việt Nam có nhiều cấp.", "s1_reading_text": "Hệ thống giáo dục Việt Nam có nhiều cấp. Mẫu giáo cho trẻ 3-5 tuổi. Tiểu học từ lớp 1 đến lớp 5. Trung học từ lớp 6 đến lớp 12. Đại học đào tạo 4 năm. Bằng tốt nghiệp rất quan trọng. Học bổng giúp sinh viên giỏi.",
     "s1_writing_items": [{"prompt": "用 mẫu giáo 写一个关于幼儿园的句子。例句：Mẫu giáo công lập miễn phí.", "targetVocab": "mẫu giáo"}, {"prompt": "用 tiểu học 写一个关于小学的句子。例句：Tiểu học là nền tảng giáo dục.", "targetVocab": "tiểu học"}, {"prompt": "用 trung học 写一个关于中学的句子。例句：Trung học phổ thông 3 năm.", "targetVocab": "trung học"}, {"prompt": "用 đại học 写一个关于大学的句子。例句：Đại học Bách khoa rất nổi tiếng.", "targetVocab": "đại học"}, {"prompt": "用 bằng 写一个关于学位的句子。例句：Bằng thạc sĩ giúp thăng tiến.", "targetVocab": "bằng"}, {"prompt": "用 học bổng 写一个关于奖学金的句子。例句：Học bổng toàn phần rất khó xin.", "targetVocab": "học bổng"}],
     "s2_vocab": ["lớp", "môn học", "điểm", "tốt nghiệp", "thạc sĩ", "tiến sĩ"], "s2_topic": "学业生活", "s2_intro_title": "介绍：学业生活", "s2_intro_desc": "学习6个关于学业生活的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：mẫu giáo（幼儿园）、tiểu học（小学）、trung học（中学）、đại học（大学）、bằng（学位）和 học bổng（奖学金）。\n\n今天学习6个学业生活词汇。\n\n第一个词是 lớp。Lớp 是班级、年级。你可以说：Lớp tôi có 40 học sinh，意思是「我班有40个学生」。\n\n第二个词是 môn học。Môn học 是科目。你可以说：Môn học yêu thích là toán，意思是「最喜欢的科目是数学」。\n\n第三个词是 điểm。Điểm 是分数。你可以说：Điểm thi rất cao，意思是「考试分数很高」。\n\n第四个词是 tốt nghiệp。Tốt nghiệp 是毕业。你可以说：Tôi tốt nghiệp năm ngoái，意思是「我去年毕业」。\n\n第五个词是 thạc sĩ。Thạc sĩ 是硕士。你可以说：Tôi đang học thạc sĩ，意思是「我在读硕士」。\n\n第六个词是 tiến sĩ。Tiến sĩ 是博士。你可以说：Tiến sĩ cần nghiên cứu 4 năm，意思是「博士需要研究4年」。\n\n好的，让我们练习：lớp, môn học, điểm, tốt nghiệp, thạc sĩ, tiến sĩ。",
     "s2_reading_title": "阅读：学业生活", "s2_reading_desc": "Lớp tôi có 35 học sinh.", "s2_reading_text": "Lớp tôi có 35 học sinh. Môn học khó nhất là vật lý. Điểm trung bình của lớp rất cao. Năm nay nhiều bạn tốt nghiệp. Một số bạn học thạc sĩ ở nước ngoài. Ước mơ của tôi là trở thành tiến sĩ.",
     "s2_writing_items": [{"prompt": "用 lớp 写一个关于班级的句子。例句：Lớp tiếng Việt có 20 sinh viên quốc tế.", "targetVocab": "lớp"}, {"prompt": "用 môn học 写一个关于科目的句子。例句：Môn học mới rất thú vị.", "targetVocab": "môn học"}, {"prompt": "用 điểm 写一个关于分数的句子。例句：Điểm 10 là điểm cao nhất.", "targetVocab": "điểm"}, {"prompt": "用 tốt nghiệp 写一个关于毕业的句子。例句：Tốt nghiệp đại học là bước đầu tiên.", "targetVocab": "tốt nghiệp"}, {"prompt": "用 thạc sĩ 写一个关于硕士的句子。例句：Thạc sĩ quản trị kinh doanh rất phổ biến.", "targetVocab": "thạc sĩ"}, {"prompt": "用 tiến sĩ 写一个关于博士的句子。例句：Tiến sĩ cần công bố bài báo khoa học.", "targetVocab": "tiến sĩ"}],
     "review_intro_text": "你已经学完了12个越南教育体系词汇！\n\n第一课：mẫu giáo（幼儿园）、tiểu học（小学）、trung học（中学）、đại học（大学）、bằng（学位）、học bổng（奖学金）。\n\n第二课：lớp（班级）、môn học（科目）、điểm（分数）、tốt nghiệp（毕业）、thạc sĩ（硕士）、tiến sĩ（博士）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：教育全景", "review_reading_desc": "Giáo dục Việt Nam từ mẫu giáo đến đại học.", "review_reading_text": "Giáo dục Việt Nam từ mẫu giáo đến đại học. Tiểu học và trung học là bắt buộc. Đại học đào tạo chuyên môn. Bằng tốt nghiệp mở ra cơ hội. Học bổng giúp sinh viên giỏi. Mỗi lớp học nhiều môn học. Điểm cao giúp tốt nghiệp loại giỏi. Thạc sĩ và tiến sĩ cho nghiên cứu sâu.",
     "review_writing_items": [{"prompt": "用 mẫu giáo 和 tiểu học 描述教育起点。", "targetVocab": "mẫu giáo"}, {"prompt": "用 đại học 和 tốt nghiệp 描述大学生活。", "targetVocab": "đại học"}, {"prompt": "用 điểm 和 môn học 描述学业。", "targetVocab": "điểm"}, {"prompt": "用 thạc sĩ 和 tiến sĩ 描述深造。", "targetVocab": "thạc sĩ"}],
     "final_reading_title": "阅读：越南教育成就", "final_reading_desc": "Giáo dục Việt Nam đạt nhiều thành tựu.", "final_reading_text": "Giáo dục Việt Nam đạt nhiều thành tựu. Mẫu giáo phổ cập toàn quốc. Tiểu học và trung học chất lượng cao. Đại học ngày càng quốc tế hóa. Bằng Việt Nam được công nhận. Học bổng cho sinh viên xuất sắc. Lớp học hiện đại. Nhiều môn học mới. Điểm thi quốc tế cao. Tốt nghiệp với kỹ năng tốt. Thạc sĩ và tiến sĩ ngày càng nhiều.",
     "farewell_text": "恭喜你完成了越南教育体系课程！让我们回顾12个词汇。\n\nMẫu giáo——幼儿园，教育的起点。\n\nTiểu học——小学，打基础的阶段。\n\nTrung học——中学，成长的关键期。\n\nĐại học——大学，专业发展的平台。\n\nBằng——学位，能力的证明。\n\nHọc bổng——奖学金，优秀的回报。\n\nLớp——班级，学习的集体。\n\nMôn học——科目，知识的分类。\n\nĐiểm——分数，学习的反馈。\n\nTốt nghiệp——毕业，新旅程的开始。\n\nThạc sĩ——硕士，深入研究。\n\nTiến sĩ——博士，学术的巅峰。\n\n你现在能用越南语讨论教育话题了！",
    },
    # ===== D1-1: 越南传统音乐 (display_order=1) =====
    {"series": "D1", "order": 1, "title": "越南传统音乐", "description": "当đàn tranh的琴弦被拨动，一千年的越南历史在空气中震颤——你听到了什么？\n\n越南传统音乐不是博物馆里的展品，它活在每一个节日、每一场婚礼、每一个乡村的夜晚。\n\n这门课程教你12个传统音乐词汇，从乐器到曲艺，从民歌到戏剧。\n\n用越南语谈论音乐，你将触摸到越南文化最柔软的部分。", "preview_text": "当đàn tranh的琴弦被拨动，一千年的越南历史在空气中震颤。越南传统音乐活在每一个节日和乡村的夜晚。这门课程教你12个传统音乐词汇：从nhạc（音乐）到cổ truyền（传统），从đàn（琴）到tranh（筝），从sáo（笛）到trống（鼓），从hát（唱）到ca trù（歌筹），从quan họ（官贺）到chèo（嘲剧），从tuồng（剧）到cải lương（改良戏）。",
     "s1_vocab": ["nhạc", "cổ truyền", "đàn", "tranh", "sáo", "trống"], "s1_topic": "传统乐器", "s1_intro_title": "介绍：越南传统乐器", "s1_intro_desc": "学习6个越南传统乐器的词汇。",
     "s1_intro_text": "欢迎来到越南传统音乐课程！今天学习6个传统乐器词汇。\n\n第一个词是 nhạc。Nhạc 是音乐。你可以说：Nhạc Việt Nam rất hay，意思是「越南音乐很好听」。\n\n第二个词是 cổ truyền。Cổ truyền 是传统的。你可以说：Nhạc cổ truyền Việt Nam，意思是「越南传统音乐」。\n\n第三个词是 đàn。Đàn 是琴，泛指弦乐器。你可以说：Đàn bầu là nhạc cụ độc đáo，意思是「独弦琴是独特的乐器」。\n\n第四个词是 tranh。Tranh 在音乐中指筝。Đàn tranh 是越南筝，有16根弦。你可以说：Đàn tranh có âm thanh rất đẹp，意思是「越南筝的声音很美」。\n\n第五个词是 sáo。Sáo 是笛子。越南竹笛声音清亮悠扬。你可以说：Tiếng sáo rất hay，意思是「笛声很好听」。\n\n第六个词是 trống。Trống 是鼓。鼓在越南传统音乐中非常重要。你可以说：Trống đánh rất vui，意思是「鼓声很欢快」。\n\n好的，让我们练习：nhạc, cổ truyền, đàn, tranh, sáo, trống。",
     "s1_reading_title": "阅读：越南传统乐器", "s1_reading_desc": "Nhạc cổ truyền Việt Nam rất phong phú.", "s1_reading_text": "Nhạc cổ truyền Việt Nam rất phong phú. Đàn là nhạc cụ quan trọng nhất. Đàn tranh có 16 dây. Sáo trúc có âm thanh trong trẻo. Trống tạo nhịp cho bài hát. Nhạc cổ truyền được biểu diễn trong lễ hội.",
     "s1_writing_items": [{"prompt": "用 nhạc 写一个关于音乐的句子。例句：Nhạc Việt Nam có nhiều thể loại.", "targetVocab": "nhạc"}, {"prompt": "用 cổ truyền 写一个关于传统的句子。例句：Nghệ thuật cổ truyền cần được bảo tồn.", "targetVocab": "cổ truyền"}, {"prompt": "用 đàn 写一个关于乐器的句子。例句：Tôi muốn học đàn bầu.", "targetVocab": "đàn"}, {"prompt": "用 tranh 写一个关于越南筝的句子。例句：Đàn tranh là nhạc cụ truyền thống.", "targetVocab": "tranh"}, {"prompt": "用 sáo 写一个关于笛子的句子。例句：Sáo trúc phát ra âm thanh du dương.", "targetVocab": "sáo"}, {"prompt": "用 trống 写一个关于鼓的句子。例句：Trống được dùng trong lễ hội.", "targetVocab": "trống"}],
     "s2_vocab": ["hát", "ca trù", "quan họ", "chèo", "tuồng", "cải lương"], "s2_topic": "曲艺与戏剧", "s2_intro_title": "介绍：越南曲艺", "s2_intro_desc": "学习6个关于越南曲艺和戏剧的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：nhạc（音乐）、cổ truyền（传统）、đàn（琴）、tranh（筝）、sáo（笛）和 trống（鼓）。\n\n今天学习6个曲艺与戏剧词汇。\n\n第一个词是 hát。Hát 是唱歌。你可以说：Hát dân ca Việt Nam，意思是「唱越南民歌」。\n\n第二个词是 ca trù。Ca trù 是歌筹，越南最古老的音乐形式之一，已被联合国教科文组织列为非物质文化遗产。你可以说：Ca trù là di sản văn hóa，意思是「歌筹是文化遗产」。\n\n第三个词是 quan họ。Quan họ 是官贺民歌，北宁省的传统对唱。你可以说：Quan họ Bắc Ninh rất nổi tiếng，意思是「北宁官贺很有名」。\n\n第四个词是 chèo。Chèo 是嘲剧，越南北方的传统戏剧。你可以说：Chèo là nghệ thuật dân gian，意思是「嘲剧是民间艺术」。\n\n第五个词是 tuồng。Tuồng 是越南古典戏剧，类似中国京剧。你可以说：Tuồng có lịch sử lâu đời，意思是「tuồng有悠久的历史」。\n\n第六个词是 cải lương。Cải lương 是改良戏，越南南方的现代戏剧。你可以说：Cải lương rất phổ biến ở miền Nam，意思是「改良戏在南方很流行」。\n\n好的，让我们练习：hát, ca trù, quan họ, chèo, tuồng, cải lương。",
     "s2_reading_title": "阅读：越南曲艺", "s2_reading_desc": "Người Việt Nam rất thích hát.", "s2_reading_text": "Người Việt Nam rất thích hát. Ca trù là nghệ thuật cổ xưa. Quan họ là dân ca đối đáp. Chèo kể những câu chuyện dân gian. Tuồng là nghệ thuật sân khấu cổ điển. Cải lương kết hợp truyền thống và hiện đại.",
     "s2_writing_items": [{"prompt": "用 hát 写一个关于唱歌的句子。例句：Hát karaoke là sở thích của nhiều người Việt.", "targetVocab": "hát"}, {"prompt": "用 ca trù 写一个关于文化遗产的句子。例句：Ca trù được UNESCO công nhận.", "targetVocab": "ca trù"}, {"prompt": "用 quan họ 写一个关于民歌的句子。例句：Quan họ thường hát vào mùa xuân.", "targetVocab": "quan họ"}, {"prompt": "用 chèo 写一个关于戏剧的句子。例句：Chèo diễn ở sân đình làng.", "targetVocab": "chèo"}, {"prompt": "用 tuồng 写一个关于古典艺术的句子。例句：Tuồng có trang phục rất đẹp.", "targetVocab": "tuồng"}, {"prompt": "用 cải lương 写一个关于南方戏剧的句子。例句：Cải lương có nhiều bài hát hay.", "targetVocab": "cải lương"}],
     "review_intro_text": "你已经学完了12个越南传统音乐词汇！\n\n第一课：nhạc（音乐）、cổ truyền（传统）、đàn（琴）、tranh（筝）、sáo（笛）、trống（鼓）。\n\n第二课：hát（唱）、ca trù（歌筹）、quan họ（官贺）、chèo（嘲剧）、tuồng（剧）、cải lương（改良戏）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：越南音乐全景", "review_reading_desc": "Nhạc cổ truyền Việt Nam rất đa dạng.", "review_reading_text": "Nhạc cổ truyền Việt Nam rất đa dạng. Đàn tranh và sáo tạo giai điệu. Trống giữ nhịp cho bài hát. Hát là phần quan trọng nhất. Ca trù và quan họ là di sản. Chèo và tuồng là sân khấu truyền thống. Cải lương là nghệ thuật hiện đại.",
     "review_writing_items": [{"prompt": "用 nhạc 和 cổ truyền 描述越南传统音乐。", "targetVocab": "nhạc"}, {"prompt": "用 đàn 和 sáo 描述乐器。", "targetVocab": "đàn"}, {"prompt": "用 hát 和 ca trù 描述声乐艺术。", "targetVocab": "hát"}, {"prompt": "用 chèo 和 cải lương 比较两种戏剧。", "targetVocab": "chèo"}],
     "final_reading_title": "阅读：越南音乐之美", "final_reading_desc": "Âm nhạc Việt Nam là linh hồn của dân tộc.", "final_reading_text": "Âm nhạc Việt Nam là linh hồn của dân tộc. Nhạc cổ truyền sống mãi với thời gian. Đàn tranh và sáo trúc tạo nên giai điệu đặc trưng. Trống vang lên trong mỗi lễ hội. Hát là cách người Việt thể hiện tình cảm. Ca trù và quan họ là di sản quý báu. Chèo và tuồng kể câu chuyện lịch sử. Cải lương mang nghệ thuật đến gần hơn với khán giả.",
     "farewell_text": "恭喜你完成了越南传统音乐课程！让我们回顾12个词汇。\n\nNhạc——音乐，越南人灵魂的表达。\n\nCổ truyền——传统，千年文化的传承。\n\nĐàn——琴，越南音乐的核心乐器。\n\nTranh——筝，十六根弦上的诗意。\n\nSáo——笛，竹林中的清音。\n\nTrống——鼓，节日里的心跳。\n\nHát——唱歌，最自然的音乐表达。\n\nCa trù——歌筹，联合国认证的文化瑰宝。\n\nQuan họ——官贺，春天里的对唱情歌。\n\nChèo——嘲剧，乡村舞台上的故事。\n\nTuồng——古典戏剧，越南的京剧。\n\nCải lương——改良戏，南方人的最爱。\n\n你现在能用越南语谈论传统音乐了！",
    },
    # ===== D1-2: 越南文学 (display_order=2) =====
    {"series": "D1", "order": 2, "title": "越南文学", "description": "一部《翘传》让整个民族为之落泪——越南文学的力量远超你的想象。\n\n越南文学不只是课本上的文字，它是理解越南人情感世界的密码。\n\n这门课程教你12个文学基础词汇，从诗歌到小说，从作者到主题。\n\n用越南语谈论文学，你将走进越南人最深处的精神家园。", "preview_text": "一部《翘传》让整个民族为之落泪，越南文学的力量远超你的想象。这门课程教你12个文学基础词汇：从văn học（文学）到thơ（诗），从truyện（故事）到tiểu thuyết（小说），从tác giả（作者）到tác phẩm（作品），从đọc（读）到viết（写），从nhân vật（人物）到cốt truyện（情节），从chủ đề（主题）到ý nghĩa（意义）。",
     "s1_vocab": ["văn học", "thơ", "truyện", "tiểu thuyết", "tác giả", "tác phẩm"], "s1_topic": "文学基础", "s1_intro_title": "介绍：越南文学", "s1_intro_desc": "学习6个越南文学的基础词汇。",
     "s1_intro_text": "欢迎来到越南文学课程！今天学习6个文学基础词汇。\n\n第一个词是 văn học。Văn học 是文学。你可以说：Văn học Việt Nam rất phong phú，意思是「越南文学很丰富」。\n\n第二个词是 thơ。Thơ 是诗。越南人非常喜欢诗歌。你可以说：Thơ Hồ Xuân Hương rất hay，意思是「胡春香的诗很好」。\n\n第三个词是 truyện。Truyện 是故事。你可以说：Truyện cổ tích Việt Nam，意思是「越南童话故事」。\n\n第四个词是 tiểu thuyết。Tiểu thuyết 是小说。你可以说：Tiểu thuyết này rất dài，意思是「这部小说很长」。\n\n第五个词是 tác giả。Tác giả 是作者。你可以说：Tác giả Nguyễn Du rất nổi tiếng，意思是「作者阮攸很有名」。\n\n第六个词是 tác phẩm。Tác phẩm 是作品。你可以说：Truyện Kiều là tác phẩm vĩ đại，意思是「翘传是伟大的作品」。\n\n好的，让我们练习：văn học, thơ, truyện, tiểu thuyết, tác giả, tác phẩm。",
     "s1_reading_title": "阅读：越南文学入门", "s1_reading_desc": "Văn học Việt Nam có lịch sử lâu đời.", "s1_reading_text": "Văn học Việt Nam có lịch sử lâu đời. Thơ là thể loại được yêu thích nhất. Truyện dân gian rất phong phú. Tiểu thuyết hiện đại ngày càng phát triển. Tác giả Nguyễn Du là niềm tự hào. Tác phẩm Truyện Kiều nổi tiếng thế giới.",
     "s1_writing_items": [{"prompt": "用 văn học 写一个关于文学的句子。例句：Văn học giúp hiểu văn hóa một đất nước.", "targetVocab": "văn học"}, {"prompt": "用 thơ 写一个关于诗歌的句子。例句：Thơ lục bát là thể thơ truyền thống.", "targetVocab": "thơ"}, {"prompt": "用 truyện 写一个关于故事的句子。例句：Truyện ngắn Việt Nam rất hay.", "targetVocab": "truyện"}, {"prompt": "用 tiểu thuyết 写一个关于小说的句子。例句：Tiểu thuyết lịch sử giúp hiểu quá khứ.", "targetVocab": "tiểu thuyết"}, {"prompt": "用 tác giả 写一个关于作者的句子。例句：Tác giả trẻ viết về cuộc sống hiện đại.", "targetVocab": "tác giả"}, {"prompt": "用 tác phẩm 写一个关于作品的句子。例句：Tác phẩm này được dịch ra nhiều ngôn ngữ.", "targetVocab": "tác phẩm"}],
     "s2_vocab": ["đọc", "viết", "nhân vật", "cốt truyện", "chủ đề", "ý nghĩa"], "s2_topic": "阅读与写作", "s2_intro_title": "介绍：阅读与写作", "s2_intro_desc": "学习6个关于阅读和写作的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：văn học（文学）、thơ（诗）、truyện（故事）、tiểu thuyết（小说）、tác giả（作者）和 tác phẩm（作品）。\n\n今天学习6个阅读与写作词汇。\n\n第一个词是 đọc。Đọc 是读。你可以说：Tôi thích đọc sách，意思是「我喜欢读书」。\n\n第二个词是 viết。Viết 是写。你可以说：Viết văn là nghệ thuật，意思是「写作是艺术」。\n\n第三个词是 nhân vật。Nhân vật 是人物、角色。你可以说：Nhân vật chính rất dũng cảm，意思是「主角很勇敢」。\n\n第四个词是 cốt truyện。Cốt truyện 是情节。你可以说：Cốt truyện rất hấp dẫn，意思是「情节很吸引人」。\n\n第五个词是 chủ đề。Chủ đề 是主题。你可以说：Chủ đề của truyện là tình yêu，意思是「故事的主题是爱情」。\n\n第六个词是 ý nghĩa。Ý nghĩa 是意义。你可以说：Tác phẩm này có ý nghĩa sâu sắc，意思是「这部作品意义深刻」。\n\n好的，让我们练习：đọc, viết, nhân vật, cốt truyện, chủ đề, ý nghĩa。",
     "s2_reading_title": "阅读：读书与写作", "s2_reading_desc": "Đọc sách là thói quen tốt.", "s2_reading_text": "Đọc sách là thói quen tốt. Viết giúp thể hiện suy nghĩ. Nhân vật trong truyện rất sống động. Cốt truyện hay giữ người đọc đến cuối. Chủ đề tình yêu rất phổ biến. Ý nghĩa của văn học là hiểu con người.",
     "s2_writing_items": [{"prompt": "用 đọc 写一个关于阅读的句子。例句：Đọc truyện trước khi ngủ rất thư giãn.", "targetVocab": "đọc"}, {"prompt": "用 viết 写一个关于写作的句子。例句：Viết nhật ký giúp cải thiện tiếng Việt.", "targetVocab": "viết"}, {"prompt": "用 nhân vật 写一个关于角色的句子。例句：Nhân vật Thúy Kiều rất đáng thương.", "targetVocab": "nhân vật"}, {"prompt": "用 cốt truyện 写一个关于情节的句子。例句：Cốt truyện phim này dựa trên tiểu thuyết.", "targetVocab": "cốt truyện"}, {"prompt": "用 chủ đề 写一个关于主题的句子。例句：Chủ đề chiến tranh xuất hiện nhiều trong văn học.", "targetVocab": "chủ đề"}, {"prompt": "用 ý nghĩa 写一个关于意义的句子。例句：Ý nghĩa của bài thơ rất sâu sắc.", "targetVocab": "ý nghĩa"}],
     "review_intro_text": "你已经学完了12个越南文学词汇！\n\n第一课：văn học（文学）、thơ（诗）、truyện（故事）、tiểu thuyết（小说）、tác giả（作者）、tác phẩm（作品）。\n\n第二课：đọc（读）、viết（写）、nhân vật（人物）、cốt truyện（情节）、chủ đề（主题）、ý nghĩa（意义）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：文学的世界", "review_reading_desc": "Văn học mở ra thế giới mới.", "review_reading_text": "Văn học mở ra thế giới mới. Thơ và truyện là hai thể loại chính. Tiểu thuyết kể câu chuyện dài. Tác giả sáng tạo tác phẩm. Đọc giúp mở rộng tầm nhìn. Viết giúp thể hiện bản thân. Nhân vật và cốt truyện tạo nên câu chuyện. Chủ đề và ý nghĩa là linh hồn.",
     "review_writing_items": [{"prompt": "用 văn học 和 thơ 描述越南文学。", "targetVocab": "văn học"}, {"prompt": "用 tác giả 和 tác phẩm 描述创作。", "targetVocab": "tác giả"}, {"prompt": "用 đọc 和 viết 描述文学活动。", "targetVocab": "đọc"}, {"prompt": "用 nhân vật 和 cốt truyện 描述一个故事。", "targetVocab": "nhân vật"}],
     "final_reading_title": "阅读：越南文学之旅", "final_reading_desc": "Văn học Việt Nam là kho tàng quý giá.", "final_reading_text": "Văn học Việt Nam là kho tàng quý giá. Thơ ca truyền thống sống mãi. Truyện dân gian dạy bài học cuộc sống. Tiểu thuyết hiện đại phản ánh xã hội. Tác giả lớn để lại tác phẩm bất hủ. Đọc văn học là đọc tâm hồn dân tộc. Viết là cách gìn giữ văn hóa. Nhân vật và cốt truyện sống trong lòng người đọc. Chủ đề nhân văn mang ý nghĩa vượt thời gian.",
     "farewell_text": "恭喜你完成了越南文学课程！让我们回顾12个词汇。\n\nVăn học——文学，民族灵魂的镜子。\n\nThơ——诗，越南人最爱的文学形式。\n\nTruyện——故事，代代相传的智慧。\n\nTiểu thuyết——小说，现代文学的主力。\n\nTác giả——作者，文字背后的灵魂。\n\nTác phẩm——作品，时间检验的经典。\n\nĐọc——读，打开新世界的钥匙。\n\nViết——写，表达自我的方式。\n\nNhân vật——人物，故事的生命。\n\nCốt truyện——情节，吸引读者的魔力。\n\nChủ đề——主题，作品的灵魂。\n\nÝ nghĩa——意义，文学存在的理由。\n\n你现在能用越南语谈论文学了！",
    },
    # ===== D2-1: 越南传统建筑 (display_order=1) =====
    {"series": "D2", "order": 1, "title": "越南传统建筑", "description": "走进一座越南古寺，你会发现每一根柱子、每一片瓦都在讲述一个故事。\n\n越南传统建筑融合了中国、印度和东南亚的风格，形成了独特的美学体系。\n\n这门课程教你12个传统建筑词汇，从亭台到庙宇，从木材到雕刻。\n\n用越南语描述建筑，你将看到一个不一样的越南。", "preview_text": "走进一座越南古寺，你会发现每一根柱子、每一片瓦都在讲述故事。这门课程教你12个传统建筑词汇：从đình（亭）到chùa（寺），从miếu（庙）到cổng（门），从mái（屋顶）到cột（柱），从gỗ（木）到đá（石），从gạch（砖）到ngói（瓦），从chạm（雕）到khắc（刻）。",
     "s1_vocab": ["đình", "chùa", "miếu", "cổng", "mái", "cột"], "s1_topic": "传统建筑类型", "s1_intro_title": "介绍：越南传统建筑", "s1_intro_desc": "学习6个越南传统建筑的词汇。",
     "s1_intro_text": "欢迎来到越南传统建筑课程！今天学习6个传统建筑词汇。\n\n第一个词是 đình。Đình 是亭，越南村庄的公共建筑，用于祭祀和集会。你可以说：Đình làng rất đẹp，意思是「村亭很美」。\n\n第二个词是 chùa。Chùa 是寺庙，佛教寺院。你可以说：Chùa Một Cột rất nổi tiếng，意思是「一柱寺很有名」。\n\n第三个词是 miếu。Miếu 是庙，供奉神灵或英雄的小型建筑。你可以说：Miếu thờ thần，意思是「庙里供奉神灵」。\n\n第四个词是 cổng。Cổng 是门、大门。你可以说：Cổng chùa rất cao，意思是「寺庙的门很高」。\n\n第五个词是 mái。Mái 是屋顶。越南传统建筑的屋顶很有特色。你可以说：Mái đình cong lên，意思是「亭的屋顶向上弯曲」。\n\n第六个词是 cột。Cột 是柱子。传统建筑用大木柱支撑。你可以说：Cột gỗ rất to，意思是「木柱很大」。\n\n好的，让我们练习：đình, chùa, miếu, cổng, mái, cột。",
     "s1_reading_title": "阅读：越南传统建筑", "s1_reading_desc": "Đình làng là trung tâm của mỗi ngôi làng.", "s1_reading_text": "Đình làng là trung tâm của mỗi ngôi làng. Chùa là nơi thờ Phật. Miếu nhỏ hơn chùa. Cổng đình thường rất đẹp. Mái cong là đặc trưng kiến trúc Việt. Cột gỗ lớn chống đỡ mái nhà.",
     "s1_writing_items": [{"prompt": "用 đình 写一个关于村亭的句子。例句：Đình làng tôi có 300 năm tuổi.", "targetVocab": "đình"}, {"prompt": "用 chùa 写一个关于寺庙的句子。例句：Chùa Hương là điểm du lịch nổi tiếng.", "targetVocab": "chùa"}, {"prompt": "用 miếu 写一个关于庙的句子。例句：Miếu thờ các vị anh hùng dân tộc.", "targetVocab": "miếu"}, {"prompt": "用 cổng 写一个关于大门的句子。例句：Cổng làng cổ rất đẹp.", "targetVocab": "cổng"}, {"prompt": "用 mái 写一个关于屋顶的句子。例句：Mái ngói đỏ là hình ảnh quen thuộc.", "targetVocab": "mái"}, {"prompt": "用 cột 写一个关于柱子的句子。例句：Cột đá ở đền rất vững chắc.", "targetVocab": "cột"}],
     "s2_vocab": ["gỗ", "đá", "gạch", "ngói", "chạm", "khắc"], "s2_topic": "建筑材料与工艺", "s2_intro_title": "介绍：建筑材料", "s2_intro_desc": "学习6个关于建筑材料和工艺的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：đình（亭）、chùa（寺）、miếu（庙）、cổng（门）、mái（屋顶）和 cột（柱）。\n\n今天学习6个建筑材料与工艺词汇。\n\n第一个词是 gỗ。Gỗ 是木头。越南传统建筑大量使用木材。你可以说：Đình làm bằng gỗ，意思是「亭是用木头建的」。\n\n第二个词是 đá。Đá 是石头。石头用于建造基础和台阶。你可以说：Bậc thang bằng đá，意思是「石头台阶」。\n\n第三个词是 gạch。Gạch 是砖。越南古城的城墙用砖砌成。你可以说：Tường gạch cổ，意思是「古砖墙」。\n\n第四个词是 ngói。Ngói 是瓦。越南传统屋顶用瓦覆盖。你可以说：Mái ngói đỏ rất đẹp，意思是「红瓦屋顶很美」。\n\n第五个词是 chạm。Chạm 是雕刻（动词）。越南工匠擅长木雕。你可以说：Chạm gỗ rất tinh xảo，意思是「木雕很精美」。\n\n第六个词是 khắc。Khắc 是刻。石刻是越南传统艺术。你可以说：Khắc chữ trên đá，意思是「在石头上刻字」。\n\n好的，让我们练习：gỗ, đá, gạch, ngói, chạm, khắc。",
     "s2_reading_title": "阅读：建筑材料", "s2_reading_desc": "Kiến trúc truyền thống dùng nhiều gỗ.", "s2_reading_text": "Kiến trúc truyền thống dùng nhiều gỗ. Đá được dùng làm nền móng. Gạch xây tường thành cổ. Ngói phủ trên mái nhà. Nghệ nhân chạm hoa văn trên gỗ. Khắc chữ trên bia đá là truyền thống.",
     "s2_writing_items": [{"prompt": "用 gỗ 写一个关于木材的句子。例句：Gỗ lim rất bền và đẹp.", "targetVocab": "gỗ"}, {"prompt": "用 đá 写一个关于石头的句子。例句：Đá hoa cương dùng trong xây dựng.", "targetVocab": "đá"}, {"prompt": "用 gạch 写一个关于砖的句子。例句：Gạch cổ ở Hội An rất đặc biệt.", "targetVocab": "gạch"}, {"prompt": "用 ngói 写一个关于瓦的句子。例句：Ngói âm dương là loại ngói truyền thống.", "targetVocab": "ngói"}, {"prompt": "用 chạm 写一个关于雕刻的句子。例句：Chạm rồng trên cột đình rất đẹp.", "targetVocab": "chạm"}, {"prompt": "用 khắc 写一个关于刻字的句子。例句：Khắc tên trên bia tiến sĩ.", "targetVocab": "khắc"}],
     "review_intro_text": "你已经学完了12个越南传统建筑词汇！\n\n第一课：đình（亭）、chùa（寺）、miếu（庙）、cổng（门）、mái（屋顶）、cột（柱）。\n\n第二课：gỗ（木）、đá（石）、gạch（砖）、ngói（瓦）、chạm（雕）、khắc（刻）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：建筑全景", "review_reading_desc": "Kiến trúc Việt Nam kết hợp nhiều phong cách.", "review_reading_text": "Kiến trúc Việt Nam kết hợp nhiều phong cách. Đình và chùa là công trình tiêu biểu. Miếu nhỏ nhưng linh thiêng. Cổng và mái tạo nên vẻ đẹp. Cột gỗ vững chắc. Đá và gạch xây nền móng. Ngói đỏ phủ mái. Chạm và khắc trang trí tinh xảo.",
     "review_writing_items": [{"prompt": "用 đình 和 chùa 描述越南传统建筑。", "targetVocab": "đình"}, {"prompt": "用 gỗ 和 đá 描述建筑材料。", "targetVocab": "gỗ"}, {"prompt": "用 mái 和 ngói 描述屋顶。", "targetVocab": "mái"}, {"prompt": "用 chạm 和 khắc 描述装饰工艺。", "targetVocab": "chạm"}],
     "final_reading_title": "阅读：越南建筑之美", "final_reading_desc": "Kiến trúc truyền thống Việt Nam rất đẹp.", "final_reading_text": "Kiến trúc truyền thống Việt Nam rất đẹp. Đình làng là linh hồn của làng quê. Chùa và miếu là nơi tâm linh. Cổng chào đón khách. Mái cong và cột gỗ tạo nên vẻ đẹp riêng. Gỗ và đá là vật liệu chính. Gạch và ngói tạo màu sắc. Chạm khắc tinh xảo thể hiện tài năng nghệ nhân.",
     "farewell_text": "恭喜你完成了越南传统建筑课程！让我们回顾12个词汇。\n\nĐình——亭，越南村庄的灵魂。\n\nChùa——寺，心灵的归宿。\n\nMiếu——庙，信仰的空间。\n\nCổng——门，建筑的第一印象。\n\nMái——屋顶，越南建筑最美的曲线。\n\nCột——柱，支撑一切的力量。\n\nGỗ——木，温暖的建筑材料。\n\nĐá——石，永恒的基础。\n\nGạch——砖，城墙的记忆。\n\nNgói——瓦，屋顶的色彩。\n\nChạm——雕，工匠的艺术。\n\nKhắc——刻，时间的印记。\n\n你现在能用越南语谈论传统建筑了！",
    },
    # ===== D2-2: 越南现代建筑 (display_order=2) =====
    {"series": "D2", "order": 2, "title": "越南现代建筑", "description": "胡志明市的天际线每年都在变化——摩天大楼正在重新定义这座城市的面貌。\n\n越南的现代建筑不只是钢筋水泥，它反映了一个国家快速发展的雄心。\n\n这门课程教你12个现代建筑词汇，从高楼到别墅，从设计到材料。\n\n用越南语谈论建筑，你将看到越南最现代的一面。", "preview_text": "胡志明市的天际线每年都在变化，摩天大楼正在重新定义这座城市。这门课程教你12个现代建筑词汇：从tòa nhà（大楼）到cao ốc（高楼），从chung cư（公寓）到biệt thự（别墅），从khu đô thị（城区）到công trình（工程），从thiết kế（设计）到xây dựng（建设），从vật liệu（材料）到bê tông（混凝土），从kính（玻璃）到thép（钢）。",
     "s1_vocab": ["tòa nhà", "cao ốc", "chung cư", "biệt thự", "khu đô thị", "công trình"], "s1_topic": "现代建筑类型", "s1_intro_title": "介绍：越南现代建筑", "s1_intro_desc": "学习6个越南现代建筑的词汇。",
     "s1_intro_text": "欢迎来到越南现代建筑课程！今天学习6个现代建筑词汇。\n\n第一个词是 tòa nhà。Tòa nhà 是大楼、建筑物。你可以说：Tòa nhà này rất cao，意思是「这栋大楼很高」。\n\n第二个词是 cao ốc。Cao ốc 是高楼、摩天大楼。你可以说：Cao ốc ở Sài Gòn ngày càng nhiều，意思是「胡志明市的高楼越来越多」。\n\n第三个词是 chung cư。Chung cư 是公寓。你可以说：Tôi sống ở chung cư，意思是「我住在公寓」。\n\n第四个词是 biệt thự。Biệt thự 是别墅。你可以说：Biệt thự ở ngoại ô rất đẹp，意思是「郊区的别墅很美」。\n\n第五个词是 khu đô thị。Khu đô thị 是城市新区。你可以说：Khu đô thị mới rất hiện đại，意思是「新城区很现代」。\n\n第六个词是 công trình。Công trình 是工程、建筑项目。你可以说：Công trình đang xây dựng，意思是「工程正在建设中」。\n\n好的，让我们练习：tòa nhà, cao ốc, chung cư, biệt thự, khu đô thị, công trình。",
     "s1_reading_title": "阅读：越南现代建筑", "s1_reading_desc": "Thành phố Hồ Chí Minh có nhiều tòa nhà hiện đại.", "s1_reading_text": "Thành phố Hồ Chí Minh có nhiều tòa nhà hiện đại. Cao ốc Landmark 81 là tòa nhà cao nhất. Chung cư là nơi ở phổ biến. Biệt thự ở quận 2 rất sang trọng. Khu đô thị Phú Mỹ Hưng rất đẹp. Nhiều công trình mới đang được xây dựng.",
     "s1_writing_items": [{"prompt": "用 tòa nhà 写一个关于大楼的句子。例句：Tòa nhà văn phòng có 30 tầng.", "targetVocab": "tòa nhà"}, {"prompt": "用 cao ốc 写一个关于高楼的句子。例句：Cao ốc thay đổi đường chân trời thành phố.", "targetVocab": "cao ốc"}, {"prompt": "用 chung cư 写一个关于公寓的句子。例句：Chung cư mới có hồ bơi và phòng gym.", "targetVocab": "chung cư"}, {"prompt": "用 biệt thự 写一个关于别墅的句子。例句：Biệt thự có sân vườn rộng.", "targetVocab": "biệt thự"}, {"prompt": "用 khu đô thị 写一个关于城区的句子。例句：Khu đô thị mới có trường học và bệnh viện.", "targetVocab": "khu đô thị"}, {"prompt": "用 công trình 写一个关于工程的句子。例句：Công trình cầu mới hoàn thành năm nay.", "targetVocab": "công trình"}],
     "s2_vocab": ["thiết kế", "xây dựng", "vật liệu", "bê tông", "kính", "thép"], "s2_topic": "设计与材料", "s2_intro_title": "介绍：设计与材料", "s2_intro_desc": "学习6个关于建筑设计和材料的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：tòa nhà（大楼）、cao ốc（高楼）、chung cư（公寓）、biệt thự（别墅）、khu đô thị（城区）和 công trình（工程）。\n\n今天学习6个设计与材料词汇。\n\n第一个词是 thiết kế。Thiết kế 是设计。你可以说：Thiết kế tòa nhà rất đẹp，意思是「大楼的设计很美」。\n\n第二个词是 xây dựng。Xây dựng 是建设、建造。你可以说：Xây dựng mất 3 năm，意思是「建设花了3年」。\n\n第三个词是 vật liệu。Vật liệu 是材料。你可以说：Vật liệu xây dựng hiện đại，意思是「现代建筑材料」。\n\n第四个词是 bê tông。Bê tông 是混凝土。你可以说：Nhà bê tông rất chắc，意思是「混凝土房子很坚固」。\n\n第五个词是 kính。Kính 是玻璃。现代高楼大量使用玻璃幕墙。你可以说：Tòa nhà kính rất đẹp，意思是「玻璃大楼很美」。\n\n第六个词是 thép。Thép 是钢。钢结构是现代建筑的基础。你可以说：Kết cấu thép rất vững，意思是「钢结构很坚固」。\n\n好的，让我们练习：thiết kế, xây dựng, vật liệu, bê tông, kính, thép。",
     "s2_reading_title": "阅读：建筑设计", "s2_reading_desc": "Thiết kế kiến trúc hiện đại rất sáng tạo.", "s2_reading_text": "Thiết kế kiến trúc hiện đại rất sáng tạo. Xây dựng cao ốc cần nhiều thời gian. Vật liệu mới giúp xây nhanh hơn. Bê tông cốt thép là nền tảng. Kính tạo vẻ đẹp hiện đại. Thép giúp tòa nhà cao hơn.",
     "s2_writing_items": [{"prompt": "用 thiết kế 写一个关于设计的句子。例句：Thiết kế xanh giúp tiết kiệm năng lượng.", "targetVocab": "thiết kế"}, {"prompt": "用 xây dựng 写一个关于建设的句子。例句：Xây dựng metro ở Sài Gòn đang tiến hành.", "targetVocab": "xây dựng"}, {"prompt": "用 vật liệu 写一个关于材料的句子。例句：Vật liệu tái chế ngày càng phổ biến.", "targetVocab": "vật liệu"}, {"prompt": "用 bê tông 写一个关于混凝土的句子。例句：Bê tông cường độ cao dùng cho cao ốc.", "targetVocab": "bê tông"}, {"prompt": "用 kính 写一个关于玻璃的句子。例句：Kính cường lực an toàn hơn kính thường.", "targetVocab": "kính"}, {"prompt": "用 thép 写一个关于钢的句子。例句：Thép không gỉ dùng trong xây dựng hiện đại.", "targetVocab": "thép"}],
     "review_intro_text": "你已经学完了12个越南现代建筑词汇！\n\n第一课：tòa nhà（大楼）、cao ốc（高楼）、chung cư（公寓）、biệt thự（别墅）、khu đô thị（城区）、công trình（工程）。\n\n第二课：thiết kế（设计）、xây dựng（建设）、vật liệu（材料）、bê tông（混凝土）、kính（玻璃）、thép（钢）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：现代建筑全景", "review_reading_desc": "Kiến trúc hiện đại Việt Nam phát triển nhanh.", "review_reading_text": "Kiến trúc hiện đại Việt Nam phát triển nhanh. Tòa nhà và cao ốc mọc lên khắp nơi. Chung cư và biệt thự đáp ứng nhu cầu. Khu đô thị mới hiện đại. Công trình lớn được thiết kế đẹp. Xây dựng dùng vật liệu tiên tiến. Bê tông, kính và thép là ba vật liệu chính.",
     "review_writing_items": [{"prompt": "用 tòa nhà 和 cao ốc 描述城市景观。", "targetVocab": "tòa nhà"}, {"prompt": "用 thiết kế 和 xây dựng 描述建筑过程。", "targetVocab": "thiết kế"}, {"prompt": "用 chung cư 和 biệt thự 比较住宅类型。", "targetVocab": "chung cư"}, {"prompt": "用 bê tông 和 thép 描述建筑材料。", "targetVocab": "bê tông"}],
     "final_reading_title": "阅读：越南建筑未来", "final_reading_desc": "Kiến trúc Việt Nam hướng tới tương lai.", "final_reading_text": "Kiến trúc Việt Nam hướng tới tương lai. Tòa nhà xanh ngày càng nhiều. Cao ốc thông minh tiết kiệm năng lượng. Chung cư hiện đại tiện nghi. Biệt thự sinh thái thân thiện. Khu đô thị bền vững. Công trình được thiết kế sáng tạo. Xây dựng dùng vật liệu mới. Bê tông, kính và thép kết hợp hoàn hảo.",
     "farewell_text": "恭喜你完成了越南现代建筑课程！让我们回顾12个词汇。\n\nTòa nhà——大楼，城市的骨架。\n\nCao ốc——高楼，天际线的主角。\n\nChung cư——公寓，城市人的家。\n\nBiệt thự——别墅，梦想的居所。\n\nKhu đô thị——城区，现代生活的舞台。\n\nCông trình——工程，发展的见证。\n\nThiết kế——设计，建筑的灵魂。\n\nXây dựng——建设，梦想变现实。\n\nVật liệu——材料，建筑的基因。\n\nBê tông——混凝土，坚固的基础。\n\nKính——玻璃，透明的美学。\n\nThép——钢，力量的象征。\n\n你现在能用越南语谈论现代建筑了！",
    },
    # ===== D3-1: 越南自然风光 (display_order=1) =====
    {"series": "D3", "order": 1, "title": "越南自然风光", "description": "从下龙湾的石灰岩到湄公河三角洲的稻田——越南的自然风光让人屏住呼吸。\n\n越南拥有3000多公里的海岸线和无数的山川湖泊，每一处都是一幅画。\n\n这门课程教你12个自然风光词汇，从海洋到山脉，从河流到岛屿。\n\n用越南语描述自然，你将更深刻地感受越南的美。", "preview_text": "从下龙湾的石灰岩到湄公河三角洲的稻田，越南的自然风光让人屏住呼吸。这门课程教你12个自然风光词汇：从biển（海）到núi（山），从sông（河）到hồ（湖），从rừng（森林）到đảo（岛），从thác（瀑布）到hang（洞），从vịnh（湾）到đồng（平原），从ruộng（田）到cánh đồng（田野）。",
     "s1_vocab": ["biển", "núi", "sông", "hồ", "rừng", "đảo"], "s1_topic": "自然地理", "s1_intro_title": "介绍：越南自然地理", "s1_intro_desc": "学习6个越南自然地理的词汇。",
     "s1_intro_text": "欢迎来到越南自然风光课程！今天学习6个自然地理词汇。\n\n第一个词是 biển。Biển 是海。越南有3000多公里的海岸线。你可以说：Biển Việt Nam rất đẹp，意思是「越南的海很美」。\n\n第二个词是 núi。Núi 是山。越南北部有很多高山。你可以说：Núi Fansipan cao nhất Việt Nam，意思是「番西邦山是越南最高的山」。\n\n第三个词是 sông。Sông 是河。湄公河是越南最重要的河流。你可以说：Sông Mê Kông rất dài，意思是「湄公河很长」。\n\n第四个词是 hồ。Hồ 是湖。河内有很多美丽的湖泊。你可以说：Hồ Hoàn Kiếm ở trung tâm Hà Nội，意思是「还剑湖在河内市中心」。\n\n第五个词是 rừng。Rừng 是森林。越南有丰富的热带雨林。你可以说：Rừng nhiệt đới rất đa dạng，意思是「热带雨林很多样」。\n\n第六个词是 đảo。Đảo 是岛。越南有很多美丽的岛屿。你可以说：Đảo Phú Quốc rất nổi tiếng，意思是「富国岛很有名」。\n\n好的，让我们练习：biển, núi, sông, hồ, rừng, đảo。",
     "s1_reading_title": "阅读：越南自然地理", "s1_reading_desc": "Việt Nam có thiên nhiên rất đẹp.", "s1_reading_text": "Việt Nam có thiên nhiên rất đẹp. Biển xanh trải dài từ Bắc vào Nam. Núi cao ở phía Bắc. Sông Mê Kông chảy qua miền Nam. Hồ Hoàn Kiếm là biểu tượng Hà Nội. Rừng nhiệt đới phong phú. Đảo Phú Quốc thu hút du khách.",
     "s1_writing_items": [{"prompt": "用 biển 写一个关于海的句子。例句：Biển Nha Trang trong xanh tuyệt đẹp.", "targetVocab": "biển"}, {"prompt": "用 núi 写一个关于山的句子。例句：Leo núi ở Sapa rất thú vị.", "targetVocab": "núi"}, {"prompt": "用 sông 写一个关于河的句子。例句：Sông Hương chảy qua thành phố Huế.", "targetVocab": "sông"}, {"prompt": "用 hồ 写一个关于湖的句子。例句：Hồ Tây là hồ lớn nhất Hà Nội.", "targetVocab": "hồ"}, {"prompt": "用 rừng 写一个关于森林的句子。例句：Rừng quốc gia Cúc Phương rất đẹp.", "targetVocab": "rừng"}, {"prompt": "用 đảo 写一个关于岛的句子。例句：Đảo Cát Bà gần vịnh Hạ Long.", "targetVocab": "đảo"}],
     "s2_vocab": ["thác", "hang", "vịnh", "đồng", "ruộng", "cánh đồng"], "s2_topic": "自然景观", "s2_intro_title": "介绍：越南自然景观", "s2_intro_desc": "学习6个关于越南自然景观的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：biển（海）、núi（山）、sông（河）、hồ（湖）、rừng（森林）和 đảo（岛）。\n\n今天学习6个自然景观词汇。\n\n第一个词是 thác。Thác 是瀑布。越南有很多壮观的瀑布。你可以说：Thác Bản Giốc rất hùng vĩ，意思是「板约瀑布很壮观」。\n\n第二个词是 hang。Hang 是洞穴。越南有世界上最大的洞穴。你可以说：Hang Sơn Đoòng lớn nhất thế giới，意思是「山洞洞是世界最大的」。\n\n第三个词是 vịnh。Vịnh 是海湾。下龙湾是世界自然遗产。你可以说：Vịnh Hạ Long rất nổi tiếng，意思是「下龙湾很有名」。\n\n第四个词是 đồng。Đồng 是平原。湄公河三角洲是越南最大的平原。你可以说：Đồng bằng sông Cửu Long rất rộng，意思是「九龙江平原很广阔」。\n\n第五个词是 ruộng。Ruộng 是田、稻田。越南的梯田非常美丽。你可以说：Ruộng bậc thang ở Sapa，意思是「沙巴的梯田」。\n\n第六个词是 cánh đồng。Cánh đồng 是田野、大片田地。你可以说：Cánh đồng lúa xanh mướt，意思是「绿油油的稻田」。\n\n好的，让我们练习：thác, hang, vịnh, đồng, ruộng, cánh đồng。",
     "s2_reading_title": "阅读：越南自然景观", "s2_reading_desc": "Thác nước ở Việt Nam rất đẹp.", "s2_reading_text": "Thác nước ở Việt Nam rất đẹp. Hang động kỳ vĩ thu hút du khách. Vịnh Hạ Long là di sản thế giới. Đồng bằng phì nhiêu nuôi sống đất nước. Ruộng bậc thang là kiệt tác của nông dân. Cánh đồng lúa trải dài bất tận.",
     "s2_writing_items": [{"prompt": "用 thác 写一个关于瀑布的句子。例句：Thác Đray Nur ở Tây Nguyên rất đẹp.", "targetVocab": "thác"}, {"prompt": "用 hang 写一个关于洞穴的句子。例句：Hang Phong Nha là điểm du lịch hấp dẫn.", "targetVocab": "hang"}, {"prompt": "用 vịnh 写一个关于海湾的句子。例句：Vịnh Lan Hạ yên bình và đẹp.", "targetVocab": "vịnh"}, {"prompt": "用 đồng 写一个关于平原的句子。例句：Đồng bằng sông Hồng là vựa lúa miền Bắc.", "targetVocab": "đồng"}, {"prompt": "用 ruộng 写一个关于稻田的句子。例句：Ruộng lúa chín vàng vào mùa thu.", "targetVocab": "ruộng"}, {"prompt": "用 cánh đồng 写一个关于田野的句子。例句：Cánh đồng hoa ở Đà Lạt rất đẹp.", "targetVocab": "cánh đồng"}],
     "review_intro_text": "你已经学完了12个越南自然风光词汇！\n\n第一课：biển（海）、núi（山）、sông（河）、hồ（湖）、rừng（森林）、đảo（岛）。\n\n第二课：thác（瀑布）、hang（洞）、vịnh（湾）、đồng（平原）、ruộng（田）、cánh đồng（田野）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：自然全景", "review_reading_desc": "Thiên nhiên Việt Nam đa dạng và tuyệt đẹp.", "review_reading_text": "Thiên nhiên Việt Nam đa dạng và tuyệt đẹp. Biển xanh và núi cao. Sông dài và hồ trong. Rừng xanh và đảo đẹp. Thác hùng vĩ và hang kỳ bí. Vịnh nổi tiếng thế giới. Đồng bằng phì nhiêu. Ruộng bậc thang tuyệt đẹp. Cánh đồng lúa bất tận.",
     "review_writing_items": [{"prompt": "用 biển 和 đảo 描述越南海岸。", "targetVocab": "biển"}, {"prompt": "用 núi 和 rừng 描述越南山区。", "targetVocab": "núi"}, {"prompt": "用 thác 和 hang 描述自然奇观。", "targetVocab": "thác"}, {"prompt": "用 ruộng 和 cánh đồng 描述越南乡村。", "targetVocab": "ruộng"}],
     "final_reading_title": "阅读：越南自然之美", "final_reading_desc": "Việt Nam là đất nước của thiên nhiên tuyệt đẹp.", "final_reading_text": "Việt Nam là đất nước của thiên nhiên tuyệt đẹp. Biển trong xanh kéo dài hàng ngàn km. Núi cao sừng sững ở phía Bắc. Sông Mê Kông và sông Hồng nuôi sống đất nước. Hồ yên bình giữa lòng thành phố. Rừng nhiệt đới đa dạng sinh học. Đảo xinh đẹp thu hút du khách. Thác nước hùng vĩ. Hang động kỳ bí. Vịnh Hạ Long là kỳ quan. Đồng bằng phì nhiêu. Ruộng bậc thang và cánh đồng lúa là bức tranh tuyệt đẹp.",
     "farewell_text": "恭喜你完成了越南自然风光课程！让我们回顾12个词汇。\n\nBiển——海，越南最长的边界。\n\nNúi——山，北方的脊梁。\n\nSông——河，生命的动脉。\n\nHồ——湖，城市的眼睛。\n\nRừng——森林，地球的肺。\n\nĐảo——岛，海上的珍珠。\n\nThác——瀑布，大自然的力量。\n\nHang——洞穴，地下的宫殿。\n\nVịnh——海湾，世界的遗产。\n\nĐồng——平原，粮食的摇篮。\n\nRuộng——田，农民的画布。\n\nCánh đồng——田野，越南最美的风景。\n\n你现在能用越南语描述自然风光了！",
    },
    # ===== D3-2: 越南环境保护 (display_order=2) =====
    {"series": "D3", "order": 2, "title": "越南环境保护", "description": "河内的空气质量指数经常爆表——环境问题正在成为越南最紧迫的挑战。\n\n理解环境词汇不只是学语言，更是理解越南当下最热门的社会议题。\n\n这门课程教你12个环境保护词汇，从污染到回收，从能源到绿色生活。\n\n用越南语讨论环保，你将展现一个有深度的国际公民形象。", "preview_text": "河内的空气质量指数经常爆表，环境问题正在成为越南最紧迫的挑战。这门课程教你12个环境保护词汇：从ô nhiễm（污染）到rác（垃圾），从khí thải（废气）到nước thải（废水），从tiếng ồn（噪音）到bụi（灰尘），从tái chế（回收）到năng lượng（能源），从mặt trời（太阳）到gió（风），从xanh（绿色）到sạch（干净）。",
     "s1_vocab": ["ô nhiễm", "rác", "khí thải", "nước thải", "tiếng ồn", "bụi"], "s1_topic": "环境问题", "s1_intro_title": "介绍：环境问题", "s1_intro_desc": "学习6个关于环境问题的词汇。",
     "s1_intro_text": "欢迎来到越南环境保护课程！今天学习6个环境问题词汇。\n\n第一个词是 ô nhiễm。Ô nhiễm 是污染。你可以说：Ô nhiễm không khí ở Hà Nội rất nghiêm trọng，意思是「河内的空气污染很严重」。\n\n第二个词是 rác。Rác 是垃圾。你可以说：Không vứt rác ra đường，意思是「不要把垃圾扔到路上」。\n\n第三个词是 khí thải。Khí thải 是废气。你可以说：Khí thải xe máy gây ô nhiễm，意思是「摩托车废气造成污染」。\n\n第四个词是 nước thải。Nước thải 是废水。你可以说：Nước thải công nghiệp rất nguy hiểm，意思是「工业废水很危险」。\n\n第五个词是 tiếng ồn。Tiếng ồn 是噪音。你可以说：Tiếng ồn ở thành phố rất lớn，意思是「城市的噪音很大」。\n\n第六个词是 bụi。Bụi 是灰尘。你可以说：Bụi mịn ảnh hưởng sức khỏe，意思是「细颗粒物影响健康」。\n\n好的，让我们练习：ô nhiễm, rác, khí thải, nước thải, tiếng ồn, bụi。",
     "s1_reading_title": "阅读：越南环境问题", "s1_reading_desc": "Ô nhiễm là vấn đề lớn ở Việt Nam.", "s1_reading_text": "Ô nhiễm là vấn đề lớn ở Việt Nam. Rác thải ngày càng nhiều. Khí thải từ xe cộ gây ô nhiễm không khí. Nước thải chưa được xử lý tốt. Tiếng ồn ảnh hưởng cuộc sống. Bụi mịn là mối lo ngại mới.",
     "s1_writing_items": [{"prompt": "用 ô nhiễm 写一个关于污染的句子。例句：Ô nhiễm nguồn nước ảnh hưởng sức khỏe.", "targetVocab": "ô nhiễm"}, {"prompt": "用 rác 写一个关于垃圾的句子。例句：Phân loại rác giúp bảo vệ môi trường.", "targetVocab": "rác"}, {"prompt": "用 khí thải 写一个关于废气的句子。例句：Giảm khí thải là mục tiêu quan trọng.", "targetVocab": "khí thải"}, {"prompt": "用 nước thải 写一个关于废水的句子。例句：Nước thải cần được xử lý trước khi thải ra sông.", "targetVocab": "nước thải"}, {"prompt": "用 tiếng ồn 写一个关于噪音的句子。例句：Tiếng ồn ban đêm ảnh hưởng giấc ngủ.", "targetVocab": "tiếng ồn"}, {"prompt": "用 bụi 写一个关于灰尘的句子。例句：Đeo khẩu trang để tránh bụi.", "targetVocab": "bụi"}],
     "s2_vocab": ["tái chế", "năng lượng", "mặt trời", "gió", "xanh", "sạch"], "s2_topic": "绿色生活", "s2_intro_title": "介绍：绿色生活", "s2_intro_desc": "学习6个关于绿色生活的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：ô nhiễm（污染）、rác（垃圾）、khí thải（废气）、nước thải（废水）、tiếng ồn（噪音）和 bụi（灰尘）。\n\n今天学习6个绿色生活词汇。\n\n第一个词是 tái chế。Tái chế 是回收、再利用。你可以说：Tái chế rác thải rất quan trọng，意思是「回收垃圾很重要」。\n\n第二个词是 năng lượng。Năng lượng 是能源。你可以说：Năng lượng sạch là tương lai，意思是「清洁能源是未来」。\n\n第三个词是 mặt trời。Mặt trời 是太阳。你可以说：Năng lượng mặt trời rất phổ biến，意思是「太阳能很普遍」。\n\n第四个词是 gió。Gió 是风。你可以说：Năng lượng gió ngày càng phát triển，意思是「风能越来越发展」。\n\n第五个词是 xanh。Xanh 是绿色的。你可以说：Sống xanh là xu hướng mới，意思是「绿色生活是新趋势」。\n\n第六个词是 sạch。Sạch 是干净的。你可以说：Thành phố sạch đẹp hơn，意思是「城市干净了更美」。\n\n好的，让我们练习：tái chế, năng lượng, mặt trời, gió, xanh, sạch。",
     "s2_reading_title": "阅读：绿色越南", "s2_reading_desc": "Tái chế giúp giảm rác thải.", "s2_reading_text": "Tái chế giúp giảm rác thải. Năng lượng sạch thay thế nhiên liệu hóa thạch. Mặt trời cung cấp năng lượng miễn phí. Gió là nguồn năng lượng tái tạo. Sống xanh là lối sống mới. Thành phố sạch là mục tiêu chung.",
     "s2_writing_items": [{"prompt": "用 tái chế 写一个关于回收的句子。例句：Tái chế nhựa giúp giảm ô nhiễm biển.", "targetVocab": "tái chế"}, {"prompt": "用 năng lượng 写一个关于能源的句子。例句：Tiết kiệm năng lượng là trách nhiệm của mọi người.", "targetVocab": "năng lượng"}, {"prompt": "用 mặt trời 写一个关于太阳能的句子。例句：Pin mặt trời ngày càng rẻ hơn.", "targetVocab": "mặt trời"}, {"prompt": "用 gió 写一个关于风能的句子。例句：Nhà máy điện gió ở Bạc Liêu rất lớn.", "targetVocab": "gió"}, {"prompt": "用 xanh 写一个关于绿色生活的句子。例句：Trồng cây xanh giúp không khí trong lành.", "targetVocab": "xanh"}, {"prompt": "用 sạch 写一个关于清洁的句子。例句：Nước sạch là nhu cầu cơ bản.", "targetVocab": "sạch"}],
     "review_intro_text": "你已经学完了12个越南环境保护词汇！\n\n第一课：ô nhiễm（污染）、rác（垃圾）、khí thải（废气）、nước thải（废水）、tiếng ồn（噪音）、bụi（灰尘）。\n\n第二课：tái chế（回收）、năng lượng（能源）、mặt trời（太阳）、gió（风）、xanh（绿色）、sạch（干净）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：环保全景", "review_reading_desc": "Bảo vệ môi trường là trách nhiệm chung.", "review_reading_text": "Bảo vệ môi trường là trách nhiệm chung. Ô nhiễm cần được giảm thiểu. Rác thải cần được tái chế. Khí thải và nước thải cần xử lý. Tiếng ồn và bụi ảnh hưởng sức khỏe. Năng lượng mặt trời và gió là giải pháp. Sống xanh và sạch là tương lai.",
     "review_writing_items": [{"prompt": "用 ô nhiễm 和 rác 描述环境问题。", "targetVocab": "ô nhiễm"}, {"prompt": "用 tái chế 和 năng lượng 描述解决方案。", "targetVocab": "tái chế"}, {"prompt": "用 mặt trời 和 gió 描述可再生能源。", "targetVocab": "mặt trời"}, {"prompt": "用 xanh 和 sạch 描述理想的环境。", "targetVocab": "xanh"}],
     "final_reading_title": "阅读：越南环保未来", "final_reading_desc": "Việt Nam đang nỗ lực bảo vệ môi trường.", "final_reading_text": "Việt Nam đang nỗ lực bảo vệ môi trường. Giảm ô nhiễm là ưu tiên hàng đầu. Phân loại rác ngày càng phổ biến. Kiểm soát khí thải và nước thải. Giảm tiếng ồn và bụi trong thành phố. Tái chế trở thành thói quen. Năng lượng mặt trời và gió phát triển mạnh. Sống xanh và sạch là mục tiêu quốc gia.",
     "farewell_text": "恭喜你完成了越南环境保护课程！让我们回顾12个词汇。\n\nÔ nhiễm——污染，我们共同的敌人。\n\nRác——垃圾，需要被正确处理。\n\nKhí thải——废气，看不见的威胁。\n\nNước thải——废水，河流的隐患。\n\nTiếng ồn——噪音，城市的副产品。\n\nBụi——灰尘，呼吸的挑战。\n\nTái chế——回收，给垃圾第二次生命。\n\nNăng lượng——能源，文明的动力。\n\nMặt trời——太阳，最慷慨的能源。\n\nGió——风，大自然的礼物。\n\nXanh——绿色，希望的颜色。\n\nSạch——干净，最简单的美好。\n\n你现在能用越南语讨论环保话题了！",
    },
    # ===== D4-1: 越南体育文化 (display_order=1) =====
    {"series": "D4", "order": 1, "title": "越南体育文化", "description": "2018年，越南足球队让整个东南亚为之疯狂——体育在越南不只是运动，它是民族自豪感的爆发。\n\n从街头的羽毛球到国际赛场的武术，体育渗透在越南人生活的每一个角落。\n\n这门课程教你12个体育文化词汇，从球类到武术，从训练到冠军。\n\n用越南语谈论体育，你将找到与越南人最快的共同话题。", "preview_text": "2018年越南足球队让整个东南亚为之疯狂，体育在越南不只是运动，它是民族自豪感的爆发。这门课程教你12个体育文化词汇：从bóng đá（足球）到cầu lông（羽毛球），从bơi（游泳）到chạy（跑步），从võ（武术）到đấu（比赛），从đội（队）到cầu thủ（球员），从huấn luyện（训练）到thi đấu（竞赛），从huy chương（奖牌）到vô địch（冠军）。",
     "s1_vocab": ["bóng đá", "cầu lông", "bơi", "chạy", "võ", "đấu"], "s1_topic": "体育运动", "s1_intro_title": "介绍：越南体育", "s1_intro_desc": "学习6个越南体育运动的词汇。",
     "s1_intro_text": "欢迎来到越南体育文化课程！今天学习6个体育运动词汇。\n\n第一个词是 bóng đá。Bóng đá 是足球，越南最受欢迎的运动。你可以说：Bóng đá Việt Nam rất phát triển，意思是「越南足球很发展」。\n\n第二个词是 cầu lông。Cầu lông 是羽毛球。你可以说：Tôi thích chơi cầu lông，意思是「我喜欢打羽毛球」。\n\n第三个词是 bơi。Bơi 是游泳。你可以说：Bơi là môn thể thao tốt cho sức khỏe，意思是「游泳是对健康好的运动」。\n\n第四个词是 chạy。Chạy 是跑步。你可以说：Chạy bộ mỗi sáng，意思是「每天早上跑步」。\n\n第五个词是 võ。Võ 是武术。越南有自己的传统武术。你可以说：Võ thuật Việt Nam rất đặc sắc，意思是「越南武术很有特色」。\n\n第六个词是 đấu。Đấu 是比赛、对抗。你可以说：Trận đấu rất hay，意思是「比赛很精彩」。\n\n好的，让我们练习：bóng đá, cầu lông, bơi, chạy, võ, đấu。",
     "s1_reading_title": "阅读：越南体育", "s1_reading_desc": "Bóng đá là môn thể thao phổ biến nhất.", "s1_reading_text": "Bóng đá là môn thể thao phổ biến nhất ở Việt Nam. Cầu lông được chơi ở mọi nơi. Bơi là kỹ năng quan trọng. Chạy bộ ngày càng phổ biến. Võ thuật là truyền thống lâu đời. Các trận đấu thu hút hàng triệu người xem.",
     "s1_writing_items": [{"prompt": "用 bóng đá 写一个关于足球的句子。例句：Đội tuyển bóng đá Việt Nam rất mạnh.", "targetVocab": "bóng đá"}, {"prompt": "用 cầu lông 写一个关于羽毛球的句子。例句：Cầu lông là môn thể thao dễ chơi.", "targetVocab": "cầu lông"}, {"prompt": "用 bơi 写一个关于游泳的句子。例句：Trẻ em nên học bơi từ nhỏ.", "targetVocab": "bơi"}, {"prompt": "用 chạy 写一个关于跑步的句子。例句：Chạy marathon là thử thách lớn.", "targetVocab": "chạy"}, {"prompt": "用 võ 写一个关于武术的句子。例句：Võ cổ truyền Việt Nam có nhiều môn phái.", "targetVocab": "võ"}, {"prompt": "用 đấu 写一个关于比赛的句子。例句：Trận đấu tối nay rất quan trọng.", "targetVocab": "đấu"}],
     "s2_vocab": ["đội", "cầu thủ", "huấn luyện", "thi đấu", "huy chương", "vô địch"], "s2_topic": "竞技与荣誉", "s2_intro_title": "介绍：竞技与荣誉", "s2_intro_desc": "学习6个关于竞技和荣誉的词汇。",
     "s2_intro_text": "欢迎回来！上一课我们学了：bóng đá（足球）、cầu lông（羽毛球）、bơi（游泳）、chạy（跑步）、võ（武术）和 đấu（比赛）。\n\n今天学习6个竞技与荣誉词汇。\n\n第一个词是 đội。Đội 是队、团队。你可以说：Đội tuyển Việt Nam rất mạnh，意思是「越南国家队很强」。\n\n第二个词是 cầu thủ。Cầu thủ 是球员。你可以说：Cầu thủ Quang Hải rất giỏi，意思是「球员光海很厉害」。\n\n第三个词是 huấn luyện。Huấn luyện 是训练。你可以说：Huấn luyện mỗi ngày，意思是「每天训练」。\n\n第四个词是 thi đấu。Thi đấu 是竞赛、比赛。你可以说：Thi đấu quốc tế，意思是「国际比赛」。\n\n第五个词是 huy chương。Huy chương 是奖牌。你可以说：Huy chương vàng Olympic，意思是「奥运金牌」。\n\n第六个词是 vô địch。Vô địch 是冠军。你可以说：Việt Nam vô địch AFF Cup，意思是「越南获得东南亚杯冠军」。\n\n好的，让我们练习：đội, cầu thủ, huấn luyện, thi đấu, huy chương, vô địch。",
     "s2_reading_title": "阅读：竞技荣誉", "s2_reading_desc": "Đội tuyển Việt Nam có nhiều cầu thủ giỏi.", "s2_reading_text": "Đội tuyển Việt Nam có nhiều cầu thủ giỏi. Huấn luyện viên Park Hang-seo rất nổi tiếng. Thi đấu quốc tế giúp nâng cao trình độ. Huy chương vàng SEA Games là niềm tự hào. Vô địch AFF Cup 2018 là kỷ niệm đẹp. Thể thao Việt Nam ngày càng phát triển.",
     "s2_writing_items": [{"prompt": "用 đội 写一个关于团队的句子。例句：Đội bóng đá trường tôi rất mạnh.", "targetVocab": "đội"}, {"prompt": "用 cầu thủ 写一个关于球员的句子。例句：Cầu thủ cần tập luyện chăm chỉ.", "targetVocab": "cầu thủ"}, {"prompt": "用 huấn luyện 写一个关于训练的句子。例句：Huấn luyện viên rất nghiêm khắc.", "targetVocab": "huấn luyện"}, {"prompt": "用 thi đấu 写一个关于比赛的句子。例句：Thi đấu thể thao rèn luyện ý chí.", "targetVocab": "thi đấu"}, {"prompt": "用 huy chương 写一个关于奖牌的句子。例句：Huy chương bạc cũng rất đáng tự hào.", "targetVocab": "huy chương"}, {"prompt": "用 vô địch 写一个关于冠军的句子。例句：Vô địch giải đấu là ước mơ của mọi đội.", "targetVocab": "vô địch"}],
     "review_intro_text": "你已经学完了12个越南体育文化词汇！\n\n第一课：bóng đá（足球）、cầu lông（羽毛球）、bơi（游泳）、chạy（跑步）、võ（武术）、đấu（比赛）。\n\n第二课：đội（队）、cầu thủ（球员）、huấn luyện（训练）、thi đấu（竞赛）、huy chương（奖牌）、vô địch（冠军）。\n\n现在让我们综合练习。",
     "review_reading_title": "阅读：体育全景", "review_reading_desc": "Thể thao Việt Nam ngày càng phát triển.", "review_reading_text": "Thể thao Việt Nam ngày càng phát triển. Bóng đá và cầu lông phổ biến nhất. Bơi và chạy bộ tốt cho sức khỏe. Võ thuật là truyền thống. Các trận đấu rất hấp dẫn. Đội tuyển có nhiều cầu thủ tài năng. Huấn luyện chuyên nghiệp. Thi đấu quốc tế thành công. Huy chương và vô địch là niềm tự hào.",
     "review_writing_items": [{"prompt": "用 bóng đá 和 cầu thủ 描述越南足球。", "targetVocab": "bóng đá"}, {"prompt": "用 đội 和 huấn luyện 描述训练过程。", "targetVocab": "đội"}, {"prompt": "用 thi đấu 和 huy chương 描述比赛成绩。", "targetVocab": "thi đấu"}, {"prompt": "用 võ 和 đấu 描述武术比赛。", "targetVocab": "võ"}],
     "final_reading_title": "阅读：越南体育成就", "final_reading_desc": "Thể thao Việt Nam đạt nhiều thành tích.", "final_reading_text": "Thể thao Việt Nam đạt nhiều thành tích. Bóng đá là niềm đam mê quốc gia. Cầu lông và bơi lội phát triển mạnh. Chạy bộ trở thành phong trào. Võ thuật Việt Nam nổi tiếng thế giới. Các trận đấu ngày càng chuyên nghiệp. Đội tuyển quốc gia có cầu thủ xuất sắc. Huấn luyện bài bản. Thi đấu quốc tế thành công. Huy chương vàng ngày càng nhiều. Vô địch khu vực là mục tiêu.",
     "farewell_text": "恭喜你完成了越南体育文化课程！让我们回顾12个词汇。\n\nBóng đá——足球，越南人最大的激情。\n\nCầu lông——羽毛球，街头巷尾的运动。\n\nBơi——游泳，生存的技能。\n\nChạy——跑步，最简单的运动。\n\nVõ——武术，越南的传统力量。\n\nĐấu——比赛，竞技的舞台。\n\nĐội——队，团结的力量。\n\nCầu thủ——球员，赛场上的英雄。\n\nHuấn luyện——训练，成功的基础。\n\nThi đấu——竞赛，证明自己的机会。\n\nHuy chương——奖牌，汗水的结晶。\n\nVô địch——冠军，最高的荣耀。\n\n你现在能用越南语谈论体育了！下次看越南足球赛时，试着用越南语为他们加油吧！",
    },
]


# ---------------------------------------------------------------------------
# Execution
# ---------------------------------------------------------------------------
def main():
    created = []
    errors = []
    for i, d in enumerate(ALL):
        series_id = SERIES_MAP[d['series']]
        order = d['order']
        try:
            content = build_beginner_content(d)
            validate(content, level="beginner")
            cid = create_curriculum(content, language="vi", user_language="zh")
            add_to_series(series_id, cid)
            set_display_order(cid, order)
            set_price(cid, 19)
            created.append((cid, d['title']))
            print(f"  [{i+1}/{len(ALL)}] Created: {cid} - {d['title']}")
            time.sleep(0.5)  # Rate limiting
        except Exception as e:
            errors.append((d['title'], str(e)))
            print(f"  [{i+1}/{len(ALL)}] ERROR: {d['title']} - {e}")
            traceback.print_exc()

    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(created)} created, {len(errors)} errors")
    for cid, title in created:
        print(f"  {cid}: {title}")
    if errors:
        print(f"\nERRORS:")
        for title, err in errors:
            print(f"  {title}: {err}")


if __name__ == "__main__":
    main()
