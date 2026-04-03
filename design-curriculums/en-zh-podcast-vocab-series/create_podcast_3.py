"""
Create en-zh podcast curriculum #3:
莊祖宜 (Tzui Chuang Mullinax) — "吃出更好的未來"
(Eating for a Better Future)

TED Shanghai 2013, ~17 minutes, about food, cooking, and sustainability.
YouTube: https://www.youtube.com/watch?v=wcfLMfo6LQc

18 HSK2-HSK3 vocabulary words in 3 groups of 6.
SAME 18 words and reading passages as vi-zh podcast #3.
All user-facing text in ENGLISH with PINYIN where Chinese words appear.
Reading passages in simplified Chinese (unchanged from vi-zh).

Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}

VOCAB_GROUP_1 = ["食物", "做饭", "健康", "环境", "选择", "未来"]
VOCAB_GROUP_2 = ["新鲜", "农民", "市场", "味道", "传统", "文化"]
VOCAB_GROUP_3 = ["责任", "改变", "习惯", "自然", "简单", "幸福"]
ALL_VOCAB = VOCAB_GROUP_1 + VOCAB_GROUP_2 + VOCAB_GROUP_3


def strip_keys(obj):
    if isinstance(obj, dict):
        return {k: strip_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
    if isinstance(obj, list):
        return [strip_keys(item) for item in obj]
    return obj


def validate(content):
    errors = []

    # 18 unique vocab words
    all_words = set()
    for session in content["learningSessions"][:3]:
        for act in session["activities"]:
            if act["activityType"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"):
                for w in act["data"].get("vocabList", []):
                    all_words.add(w)
    if len(all_words) != 18:
        errors.append(f"Expected 18 unique vocab words, got {len(all_words)}: {all_words}")

    # 5 sessions
    if len(content["learningSessions"]) != 5:
        errors.append(f"Expected 5 sessions, got {len(content['learningSessions'])}")

    # Activity counts: 12, 12, 12, 4, 5
    expected_counts = [12, 12, 12, 4, 5]
    for i, (session, exp) in enumerate(zip(content["learningSessions"], expected_counts)):
        actual = len(session["activities"])
        if actual != exp:
            errors.append(f"Session {i}: expected {exp} activities, got {actual}")

    # youtubeUrl present
    if not content.get("youtubeUrl"):
        errors.append("Missing youtubeUrl")

    # contentTypeTags present
    if "podcast" not in content.get("contentTypeTags", []):
        errors.append("Missing 'podcast' in contentTypeTags")

    # Every activity has title, description
    for i, session in enumerate(content["learningSessions"]):
        if "title" not in session:
            errors.append(f"Session {i} missing title")
        for j, act in enumerate(session["activities"]):
            for field in ("title", "description"):
                if field not in act:
                    errors.append(f"Session {i}, Activity {j} missing '{field}'")

    # No strip keys in content
    def check_no_strip(obj, path="root"):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in STRIP_KEYS:
                    errors.append(f"Strip key '{k}' found at {path}.{k}")
                check_no_strip(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                check_no_strip(item, f"{path}[{idx}]")

    check_no_strip(content)

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        raise ValueError(f"{len(errors)} validation error(s)")
    print("Validation passed.")



# ── Chinese reading passages (SAME as vi-zh #3, simplified Chinese) ──

READING_1 = (
    "大家好，我是庄祖宜。今天我想跟大家聊一个我最喜欢的话题：食物。\n\n"
    "你有没有想过，你每天吃的东西，不只是填饱肚子那么简单？"
    "每一口食物背后，都有一个故事——它从哪里来？谁种的？怎么做的？"
    "这些问题看起来很小，但其实跟我们的健康、我们的环境、"
    "甚至我们的未来都有很大的关系。\n\n"
    "我以前是一个人类学的研究生，后来我做了一个让所有人都觉得疯狂的选择——"
    "我放弃了学术，去了厨师学校。为什么？因为我发现，食物是了解一个文化"
    "最直接的方式。当你走进一个国家的菜市场，你就能看到那里的人怎么生活、"
    "他们重视什么、他们的传统是什么。\n\n"
    "可是现在，很多人已经不知道自己吃的东西从哪里来了。"
    "超市里的蔬菜水果，看起来都一样漂亮，但你知道它们是怎么种出来的吗？"
    "用了多少农药？运了多远的路？这些我们看不见的东西，"
    "正在慢慢改变我们的环境和我们的身体。"
)

READING_2 = (
    "那我们能做什么呢？其实很简单。第一步，就是回到厨房，自己做饭。\n\n"
    "做饭不是一件麻烦的事情。当你自己做饭的时候，你会开始关心食材——"
    "这个西红柿新鲜不新鲜？这个鸡蛋是哪里来的？这条鱼是今天的吗？"
    "你会自然而然地开始选择更好的食物。\n\n"
    "第二步，去认识你的农民。我住在上海的时候，每个周末都会去农民市场。"
    "那里的农民会告诉你，这些菜是昨天早上刚摘的，那些水果没有用农药。"
    "当你认识种菜的人，你就会更信任你吃的东西。"
    "而且，你会发现新鲜的食物味道完全不一样——"
    "一个刚从地里摘下来的西红柿，跟超市里放了一个星期的，"
    "味道简直是天壤之别。\n\n"
    "第三步，尊重传统。每个地方都有自己的饮食文化，"
    "这些传统不是随便形成的——它们是几百年、几千年的智慧。"
    "比如中国人讲究\u201c不时不食\u201d，就是说什么季节吃什么东西。"
    "这不只是为了味道好，也是为了身体健康，更是为了保护环境。"
)

READING_3 = (
    "我知道有人会说：\u201c我很忙，没有时间做饭。\u201d"
    "也有人说：\u201c新鲜的食物太贵了。\u201d\n\n"
    "可是你想想看，如果我们现在不改变自己的饮食习惯，"
    "未来我们的孩子会面对什么样的环境？土地越来越贫瘠，"
    "水源越来越污染，食物越来越没有味道——这是我们想要的未来吗？\n\n"
    "改变不需要很大。你不需要明天就变成一个素食主义者，"
    "也不需要每天花三个小时做饭。你只需要做一些简单的改变：\n\n"
    "多去菜市场，少去超市。多买当季的蔬菜水果。"
    "多自己做饭，少叫外卖。多了解你吃的东西从哪里来。\n\n"
    "这些看起来很小的改变，其实是一种责任——对自己的责任，"
    "对家人的责任，对自然的责任。\n\n"
    "我相信，当我们每个人都开始用心对待食物的时候，"
    "我们不只是在吃饭——我们是在创造一个更好的未来。"
    "而这个过程本身，就是一种幸福。\n\n"
    "做饭是一件简单的事情，但它可以改变世界。谢谢大家。"
)

FULL_TRANSCRIPT = (
    "大家好，我是庄祖宜。今天我想跟大家聊一个我最喜欢的话题：食物。\n\n"
    "你有没有想过，你每天吃的东西，不只是填饱肚子那么简单？"
    "每一口食物背后，都有一个故事——它从哪里来？谁种的？怎么做的？"
    "这些问题看起来很小，但其实跟我们的健康、我们的环境、"
    "甚至我们的未来都有很大的关系。\n\n"
    "我以前是一个人类学的研究生，后来我做了一个让所有人都觉得疯狂的选择——"
    "我放弃了学术，去了厨师学校。为什么？因为我发现，食物是了解一个文化"
    "最直接的方式。当你走进一个国家的菜市场，你就能看到那里的人怎么生活、"
    "他们重视什么、他们的传统是什么。\n\n"
    "可是现在，很多人已经不知道自己吃的东西从哪里来了。"
    "超市里的蔬菜水果，看起来都一样漂亮，但你知道它们是怎么种出来的吗？"
    "用了多少农药？运了多远的路？这些我们看不见的东西，"
    "正在慢慢改变我们的环境和我们的身体。\n\n"
    "那我们能做什么呢？其实很简单。第一步，就是回到厨房，自己做饭。\n\n"
    "做饭不是一件麻烦的事情。当你自己做饭的时候，你会开始关心食材——"
    "这个西红柿新鲜不新鲜？这个鸡蛋是哪里来的？这条鱼是今天的吗？"
    "你会自然而然地开始选择更好的食物。\n\n"
    "第二步，去认识你的农民。我住在上海的时候，每个周末都会去农民市场。"
    "那里的农民会告诉你，这些菜是昨天早上刚摘的，那些水果没有用农药。"
    "当你认识种菜的人，你就会更信任你吃的东西。"
    "而且，你会发现新鲜的食物味道完全不一样——"
    "一个刚从地里摘下来的西红柿，跟超市里放了一个星期的，"
    "味道简直是天壤之别。\n\n"
    "第三步，尊重传统。每个地方都有自己的饮食文化，"
    "这些传统不是随便形成的——它们是几百年、几千年的智慧。"
    "比如中国人讲究\u201c不时不食\u201d，就是说什么季节吃什么东西。"
    "这不只是为了味道好，也是为了身体健康，更是为了保护环境。\n\n"
    "我知道有人会说：\u201c我很忙，没有时间做饭。\u201d"
    "也有人说：\u201c新鲜的食物太贵了。\u201d\n\n"
    "可是你想想看，如果我们现在不改变自己的饮食习惯，"
    "未来我们的孩子会面对什么样的环境？土地越来越贫瘠，"
    "水源越来越污染，食物越来越没有味道——这是我们想要的未来吗？\n\n"
    "改变不需要很大。你不需要明天就变成一个素食主义者，"
    "也不需要每天花三个小时做饭。你只需要做一些简单的改变：\n\n"
    "多去菜市场，少去超市。多买当季的蔬菜水果。"
    "多自己做饭，少叫外卖。多了解你吃的东西从哪里来。\n\n"
    "这些看起来很小的改变，其实是一种责任——对自己的责任，"
    "对家人的责任，对自然的责任。\n\n"
    "我相信，当我们每个人都开始用心对待食物的时候，"
    "我们不只是在吃饭——我们是在创造一个更好的未来。"
    "而这个过程本身，就是一种幸福。\n\n"
    "做饭是一件简单的事情，但它可以改变世界。谢谢大家。"
)



def build_content():
    # ── Session 1: Group 1 — 食物, 做饭, 健康, 环境, 选择, 未来 ──

    session_1 = {
        "title": "Session 1: Food and the Future — 食物与未来",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Introduction to the Talk",
                "description": "Introduction to Tzui Chuang's TED Shanghai talk on food and sustainability",
                "data": {
                    "text": (
                        "Welcome to the Chinese vocabulary podcast course! "
                        "Today we're diving into a truly inspiring talk from TED Shanghai — "
                        "'吃出更好的未來' (Eating for a Better Future) by food writer and chef "
                        "Tzui Chuang Mullinax (莊祖宜). Tzui Chuang was once an anthropology graduate student "
                        "who made a decision everyone thought was crazy — she left academia to attend culinary school. "
                        "Why? Because she realized that food is the most direct way to understand a culture. "
                        "Walk into any country's local market, and you'll see how people live, "
                        "what they value, and what their traditions are. "
                        "In this talk, Tzui Chuang argues that our food choices directly impact "
                        "the environment and our future. Cooking consciously — choosing fresh ingredients, "
                        "supporting local farmers, respecting culinary traditions — "
                        "isn't just a personal pleasure, it's a social responsibility. "
                        "In this first session, you'll learn 6 essential vocabulary words "
                        "about food, health, and the environment. Each word appears in the talk "
                        "and will help you understand how Chinese speakers discuss "
                        "the relationship between what we eat and the world we live in. Let's get started!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 1 Vocabulary",
                "description": "Learn 6 words: 食物, 做饭, 健康, 环境, 选择, 未来",
                "data": {
                    "text": (
                        "Let's learn our first 6 vocabulary words. Each one is closely tied to the content "
                        "of Tzui Chuang's talk about food and our future.\n\n"

                        "The first word is 食物 (shíwù). 食物 is a noun meaning 'food' or 'foodstuff'. "
                        "This is the central word of the entire talk. Tzui Chuang says that every bite of "
                        "食物 (shíwù) has a story behind it — where did it come from? Who grew it? How was it made? "
                        "For example: 每一口食物背后都有一个故事 — Every bite of food has a story behind it. "
                        "食 (shí) means 'to eat' and 物 (wù) means 'thing, object'. "
                        "So 食物 (shíwù) literally means 'thing to eat'. "
                        "You can use this word when talking about daily eating: "
                        "健康的食物对身体很重要 — Healthy food is very important for the body.\n\n"

                        "The second word is 做饭 (zuòfàn). 做饭 is a verb meaning 'to cook' or 'to prepare a meal'. "
                        "Tzui Chuang argues that the first step to changing the world is going back to the kitchen "
                        "and 做饭 (zuòfàn) yourself. When you cook for yourself, you start caring about ingredients — "
                        "is this tomato fresh? Where did these eggs come from? "
                        "For example: 自己做饭比叫外卖健康多了 — Cooking yourself is much healthier than ordering takeout. "
                        "做 (zuò) means 'to do, to make' and 饭 (fàn) means 'rice, meal'. "
                        "In Chinese, 做饭 (zuòfàn) doesn't just mean cooking rice — it means cooking in general. "
                        "Another usage: 我每天都自己做饭 — I cook for myself every day.\n\n"

                        "The third word is 健康 (jiànkāng). 健康 works as both a noun and an adjective, "
                        "meaning 'health' or 'healthy'. Tzui Chuang connects food to 健康 (jiànkāng): "
                        "eating fresh, natural food helps your body stay healthier. "
                        "For example: 吃新鲜的食物对健康有好处 — Eating fresh food is good for your health. "
                        "健 (jiàn) means 'strong' and 康 (kāng) means 'well-being'. "
                        "You can use this word in many contexts: "
                        "身体健康是最重要的 — Physical health is the most important thing. "
                        "Or: 这种生活方式很健康 — This lifestyle is very healthy.\n\n"

                        "The fourth word is 环境 (huánjìng). 环境 is a noun meaning 'environment'. "
                        "This is a major theme in the talk. Tzui Chuang explains that how we choose our food "
                        "directly affects the 环境 (huánjìng) — from the soil to the water to the air. "
                        "For example: 保护环境是每个人的责任 — Protecting the environment is everyone's responsibility. "
                        "环 (huán) means 'ring, to surround' and 境 (jìng) means 'boundary, territory'. "
                        "环境 (huánjìng) is everything that surrounds us. "
                        "Another usage: 这里的环境很好，空气很新鲜 — The environment here is great, the air is very fresh.\n\n"

                        "The fifth word is 选择 (xuǎnzé). 选择 works as both a noun and a verb, "
                        "meaning 'choice' or 'to choose'. Tzui Chuang emphasizes that every time you buy food, "
                        "you're making a 选择 (xuǎnzé) — and every choice has consequences. "
                        "Local or imported? Fresh or packaged? "
                        "For example: 每一次选择都会影响我们的未来 — Every choice affects our future. "
                        "选 (xuǎn) means 'to select' and 择 (zé) means 'to pick'. "
                        "Another usage: 你可以选择更健康的生活方式 — You can choose a healthier lifestyle.\n\n"

                        "The last word for today is 未来 (wèilái). 未来 is a noun meaning 'future'. "
                        "This word appears right in the title of the talk: "
                        "吃出更好的未来 — Eating for a better future. Tzui Chuang believes that "
                        "when each of us treats food with care, we're creating a better 未来 (wèilái). "
                        "For example: 我们要为未来的孩子保护好环境 — We must protect the environment "
                        "for the children of the future. 未 (wèi) means 'not yet' and 来 (lái) means 'to come' — "
                        "the future is what hasn't come yet. "
                        "Another usage: 未来会更好的 — The future will be better.\n\n"

                        "So now you know your first 6 words: "
                        "食物 (shíwù), 做饭 (zuòfàn), 健康 (jiànkāng), "
                        "环境 (huánjìng), 选择 (xuǎnzé), 未来 (wèilái). "
                        "Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Food and the Future",
                "description": "Learn 6 words: 食物, 做饭, 健康, 环境, 选择, 未来",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 1 Vocabulary",
                "description": "Practice speaking 6 words: 食物, 做饭, 健康, 环境, 选择, 未来",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 1 Vocabulary",
                "description": "Recognize 6 words: 食物, 做饭, 健康, 环境, 选择, 未来",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 1 Vocabulary",
                "description": "Match meanings for 6 words: 食物, 做饭, 健康, 环境, 选择, 未来",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 1 Vocabulary",
                "description": "Write 6 words: 食物, 做饭, 健康, 环境, 选择, 未来",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Grammar and Usage Tips",
                "description": "How to use Session 1 vocabulary naturally in sentences",
                "data": {
                    "text": (
                        "Great work! You've met your first 6 vocabulary words. Now let's look at how "
                        "to use them naturally in sentences.\n\n"
                        "食物 (shíwù) often pairs with adjectives to describe it: "
                        "健康的食物 (jiànkāng de shíwù — healthy food), "
                        "新鲜的食物 (xīnxiān de shíwù — fresh food), "
                        "传统食物 (chuántǒng shíwù — traditional food). "
                        "Common patterns: 食物安全 (shíwù ānquán — food safety), "
                        "食物浪费 (shíwù làngfèi — food waste).\n\n"
                        "做饭 (zuòfàn) is a fixed verb-object compound. You can add adverbs: "
                        "自己做饭 (zìjǐ zuòfàn — cook yourself), "
                        "在家做饭 (zài jiā zuòfàn — cook at home). "
                        "Patterns: 给...做饭 (gěi...zuòfàn — cook for someone), "
                        "学做饭 (xué zuòfàn — learn to cook).\n\n"
                        "健康 (jiànkāng) as an adjective: "
                        "身体很健康 (shēntǐ hěn jiànkāng — body is very healthy). "
                        "As a noun: 注意健康 (zhùyì jiànkāng — pay attention to health). "
                        "Key phrase: 身心健康 (shēnxīn jiànkāng — healthy in body and mind), "
                        "健康饮食 (jiànkāng yǐnshí — healthy eating).\n\n"
                        "环境 (huánjìng) often pairs with 保护 or 污染: "
                        "保护环境 (bǎohù huánjìng — protect the environment), "
                        "环境污染 (huánjìng wūrǎn — environmental pollution). "
                        "Pattern: 对环境有影响 (duì huánjìng yǒu yǐngxiǎng — have an impact on the environment).\n\n"
                        "选择 (xuǎnzé) as a verb: "
                        "选择健康的食物 (xuǎnzé jiànkāng de shíwù — choose healthy food). "
                        "As a noun: 这是一个好的选择 (zhè shì yí gè hǎo de xuǎnzé — this is a good choice). "
                        "Patterns: 做出选择 (zuòchū xuǎnzé — make a choice), "
                        "没有选择 (méiyǒu xuǎnzé — no choice).\n\n"
                        "未来 (wèilái) usually comes before a noun: "
                        "未来的生活 (wèilái de shēnghuó — future life), "
                        "未来的孩子 (wèilái de háizi — future children). "
                        "Patterns: 在未来 (zài wèilái — in the future), "
                        "为了未来 (wèile wèilái — for the future). "
                        "Nice phrase: 未来可期 (wèilái kěqī — the future is worth looking forward to)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 1)",
                "description": "大家好，我是庄祖宜。今天我想跟大家聊一个我最喜欢的话题：食物。",
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 1)",
                "description": "Practice speaking along with the excerpt about food and culture",
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Listen: Talk Excerpt (Part 1)",
                "description": "Listen to the passage you just read and follow along.",
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Write: Food and the Future",
                "description": "Write sentences using Session 1 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "食物",
                            "prompt": (
                                "Use the word 食物 (shíwù) to talk about food — "
                                "as Tzui Chuang says every bite of food has a story behind it. "
                                "Example: 我们应该了解食物从哪里来，这样才能吃得更放心。"
                            ),
                        },
                        {
                            "targetVocab": "做饭",
                            "prompt": (
                                "Use the word 做饭 (zuòfàn) to talk about cooking — "
                                "as the talk emphasizes that cooking yourself is the first step to change. "
                                "Example: 周末在家做饭是一件很幸福的事情。"
                            ),
                        },
                        {
                            "targetVocab": "健康",
                            "prompt": (
                                "Use the word 健康 (jiànkāng) to talk about health — "
                                "as Tzui Chuang connects fresh food with better health. "
                                "Example: 多吃蔬菜水果对身体健康有很大的好处。"
                            ),
                        },
                        {
                            "targetVocab": "环境",
                            "prompt": (
                                "Use the word 环境 (huánjìng) to talk about the environment — "
                                "as the talk explains that food choices affect the environment. "
                                "Example: 如果我们不保护环境，未来的生活会越来越难。"
                            ),
                        },
                        {
                            "targetVocab": "选择",
                            "prompt": (
                                "Use the word 选择 (xuǎnzé) to talk about a choice — "
                                "as Tzui Chuang emphasizes that every food purchase is a choice with consequences. "
                                "Example: 选择当地的食物不仅新鲜，还能帮助农民。"
                            ),
                        },
                        {
                            "targetVocab": "未来",
                            "prompt": (
                                "Use the word 未来 (wèilái) to talk about the future — "
                                "as the talk title says: eating for a better future. "
                                "Example: 我们今天的选择会决定未来的世界是什么样子。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_1[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }



    # ── Session 2: Group 2 — 新鲜, 农民, 市场, 味道, 传统, 文化 ──

    session_2 = {
        "title": "Session 2: Markets and Traditions — 市场与传统",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Session 2 Introduction",
                "description": "Recap Session 1 and introduce Session 2 theme",
                "data": {
                    "text": (
                        "Welcome back to Session 2! In the previous session, we learned 6 important words: "
                        "食物 (shíwù — food), 做饭 (zuòfàn — to cook), 健康 (jiànkāng — health), "
                        "环境 (huánjìng — environment), 选择 (xuǎnzé — choice), and 未来 (wèilái — future). "
                        "Do you remember them? Tzui Chuang told us that every bite of food has a story, "
                        "and every food choice affects our future. "
                        "Today we'll dive deeper into the next part of the talk, "
                        "where she describes her weekend mornings at the farmers' market in Shanghai, "
                        "the incredible flavor of truly fresh food, and the hidden wisdom "
                        "in centuries-old culinary traditions. "
                        "You'll learn 6 new words related to freshness, farmers, and food culture. Let's go!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 2 Vocabulary",
                "description": "Learn 6 words: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "data": {
                    "text": (
                        "Let's learn today's 6 new vocabulary words. These come from the middle section "
                        "of the talk, where Tzui Chuang shares her experiences shopping at markets and cooking in Shanghai.\n\n"

                        "The first word is 新鲜 (xīnxiān). 新鲜 is an adjective meaning 'fresh' or 'novel'. "
                        "Tzui Chuang says that when you cook for yourself, you start caring about whether "
                        "your food is 新鲜 (xīnxiān) or not. A tomato just picked from the garden tastes "
                        "completely different from one that's been sitting in a supermarket for a week. "
                        "For example: 新鲜的蔬菜味道特别好 — Fresh vegetables taste especially good. "
                        "新 (xīn) means 'new' and 鲜 (xiān) means 'fresh, delicious'. "
                        "You can use this word for both food and ideas: "
                        "这个想法很新鲜 — This idea is very novel.\n\n"

                        "The second word is 农民 (nóngmín). 农民 is a noun meaning 'farmer'. "
                        "Tzui Chuang encourages everyone to visit farmers' markets and get to know "
                        "the people who grow your food. When you know who grew your vegetables, "
                        "you trust what you eat more. "
                        "For example: 农民每天早上很早就起来工作 — Farmers get up very early every morning to work. "
                        "农 (nóng) means 'agriculture' and 民 (mín) means 'people'. "
                        "Another usage: 我们应该支持当地的农民 — We should support local farmers.\n\n"

                        "The third word is 市场 (shìchǎng). 市场 is a noun meaning 'market' or 'marketplace'. "
                        "Tzui Chuang says that when you walk into a country's market, you can see "
                        "how the people there live, what they value, and what their traditions are. "
                        "For example: 菜市场里的蔬菜比超市的新鲜多了 — Vegetables at the market are much fresher "
                        "than at the supermarket. 市 (shì) means 'city, market' and 场 (chǎng) means 'field, place'. "
                        "市场 (shìchǎng) can refer to a traditional market or an economic market: "
                        "农民市场 (nóngmín shìchǎng — farmers' market), "
                        "市场经济 (shìchǎng jīngjì — market economy).\n\n"

                        "The fourth word is 味道 (wèidào). 味道 is a noun meaning 'flavor' or 'taste'. "
                        "Tzui Chuang compares the flavor of a freshly picked tomato to a supermarket one — "
                        "the difference is like 'heaven and earth'. Fresh food has a completely different 味道 (wèidào). "
                        "For example: 妈妈做的菜味道最好 — Mom's cooking has the best flavor. "
                        "味 (wèi) means 'taste' and 道 (dào) means 'way, path'. "
                        "Another usage: 这个菜的味道怎么样？ — How does this dish taste? "
                        "Or the poetic: 家乡的味道 (jiāxiāng de wèidào — the taste of home).\n\n"

                        "The fifth word is 传统 (chuántǒng). 传统 works as both a noun and an adjective, "
                        "meaning 'tradition' or 'traditional'. Tzui Chuang emphasizes that every place "
                        "has its own culinary traditions, and these 传统 (chuántǒng) aren't random — "
                        "they're the wisdom of hundreds, even thousands of years. "
                        "For example: 中国有很多传统的美食 — China has many traditional delicacies. "
                        "传 (chuán) means 'to pass on' and 统 (tǒng) means 'system'. "
                        "Common patterns: 传统文化 (chuántǒng wénhuà — traditional culture), "
                        "传统节日 (chuántǒng jiérì — traditional festival).\n\n"

                        "The last word is 文化 (wénhuà). 文化 is a noun meaning 'culture'. "
                        "Tzui Chuang was once an anthropology graduate student, and she realized that "
                        "食物 (shíwù) is the most direct way to understand the 文化 (wénhuà) of a place. "
                        "For example: 饮食文化是了解一个国家最好的方式 — Food culture is the best way "
                        "to understand a country. 文 (wén) means 'writing, literature' and 化 (huà) means 'to transform'. "
                        "Another usage: 中国文化博大精深 — Chinese culture is vast and profound. "
                        "Or: 文化交流 (wénhuà jiāoliú — cultural exchange).\n\n"

                        "So now you've learned 6 more words: "
                        "新鲜 (xīnxiān), 农民 (nóngmín), 市场 (shìchǎng), "
                        "味道 (wèidào), 传统 (chuántǒng), 文化 (wénhuà). "
                        "Together with the 6 from Session 1, you now have 12 vocabulary words! Let's keep practicing!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Markets and Traditions",
                "description": "Learn 6 words: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 2 Vocabulary",
                "description": "Practice speaking 6 words: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 2 Vocabulary",
                "description": "Recognize 6 words: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 2 Vocabulary",
                "description": "Match meanings for 6 words: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 2 Vocabulary",
                "description": "Write 6 words: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Grammar and Usage Tips",
                "description": "How to use Session 2 vocabulary naturally in sentences",
                "data": {
                    "text": (
                        "Well done! You've got 6 new words under your belt. Let's see how to use them "
                        "more naturally in sentences.\n\n"
                        "新鲜 (xīnxiān) usually comes before a noun: "
                        "新鲜的水果 (xīnxiān de shuǐguǒ — fresh fruit), "
                        "新鲜空气 (xīnxiān kōngqì — fresh air). "
                        "Figurative use: 新鲜事 (xīnxiān shì — something novel), "
                        "新鲜感 (xīnxiān gǎn — sense of novelty).\n\n"
                        "农民 (nóngmín) often pairs with occupations or activities: "
                        "农民伯伯 (nóngmín bóbo — uncle farmer, a respectful term), "
                        "农民市场 (nóngmín shìchǎng — farmers' market). "
                        "Patterns: 当农民 (dāng nóngmín — be a farmer), "
                        "农民的生活 (nóngmín de shēnghuó — a farmer's life).\n\n"
                        "市场 (shìchǎng) has two main meanings. Concrete: "
                        "菜市场 (cài shìchǎng — vegetable market), "
                        "农民市场 (nóngmín shìchǎng — farmers' market). "
                        "Abstract: 市场经济 (shìchǎng jīngjì — market economy), "
                        "市场需求 (shìchǎng xūqiú — market demand). "
                        "Pattern: 去市场买菜 (qù shìchǎng mǎi cài — go to the market to buy vegetables).\n\n"
                        "味道 (wèidào) often pairs with adjectives: "
                        "味道很好 (wèidào hěn hǎo — tastes great), "
                        "味道不错 (wèidào búcuò — tastes pretty good), "
                        "味道很奇怪 (wèidào hěn qíguài — tastes very strange). "
                        "Patterns: 有...的味道 (yǒu...de wèidào — has the taste of...), "
                        "尝一尝味道 (cháng yì cháng wèidào — have a taste).\n\n"
                        "传统 (chuántǒng) as an adjective: "
                        "传统文化 (chuántǒng wénhuà — traditional culture), "
                        "传统美食 (chuántǒng měishí — traditional cuisine). "
                        "As a noun: 保持传统 (bǎochí chuántǒng — maintain tradition), "
                        "打破传统 (dǎpò chuántǒng — break with tradition). "
                        "Pattern: 有...的传统 (yǒu...de chuántǒng — have a tradition of...).\n\n"
                        "文化 (wénhuà) often pairs with other nouns: "
                        "中国文化 (Zhōngguó wénhuà — Chinese culture), "
                        "饮食文化 (yǐnshí wénhuà — food culture), "
                        "文化差异 (wénhuà chāyì — cultural differences). "
                        "Patterns: 了解文化 (liǎojiě wénhuà — understand a culture), "
                        "文化交流 (wénhuà jiāoliú — cultural exchange)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 2)",
                "description": "那我们能做什么呢？其实很简单。第一步，就是回到厨房，自己做饭。",
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 2)",
                "description": "Practice speaking along with the excerpt about farmers' markets and traditions",
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Listen: Talk Excerpt (Part 2)",
                "description": "Listen to the passage you just read and follow along.",
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Write: Markets and Traditions",
                "description": "Write sentences using Session 2 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "新鲜",
                            "prompt": (
                                "Use the word 新鲜 (xīnxiān) to talk about freshness — "
                                "as Tzui Chuang compares the flavor of fresh tomatoes to supermarket ones. "
                                "Example: 早上去市场买的蔬菜特别新鲜，做出来的菜味道也好。"
                            ),
                        },
                        {
                            "targetVocab": "农民",
                            "prompt": (
                                "Use the word 农民 (nóngmín) to talk about farmers — "
                                "as the talk encourages getting to know the people who grow your food. "
                                "Example: 农民每天辛苦工作，我们应该尊重他们的劳动。"
                            ),
                        },
                        {
                            "targetVocab": "市场",
                            "prompt": (
                                "Use the word 市场 (shìchǎng) to talk about a market — "
                                "as Tzui Chuang says walking into a market is the best way to understand a culture. "
                                "Example: 每个周末我都喜欢去菜市场买新鲜的蔬菜和水果。"
                            ),
                        },
                        {
                            "targetVocab": "味道",
                            "prompt": (
                                "Use the word 味道 (wèidào) to talk about flavor — "
                                "as the talk emphasizes that fresh food tastes completely different. "
                                "Example: 这道菜的味道让我想起了小时候妈妈做的饭。"
                            ),
                        },
                        {
                            "targetVocab": "传统",
                            "prompt": (
                                "Use the word 传统 (chuántǒng) to talk about tradition — "
                                "as Tzui Chuang explains that culinary traditions are the wisdom of thousands of years. "
                                "Example: 传统的饮食方式往往比现代快餐更健康。"
                            ),
                        },
                        {
                            "targetVocab": "文化",
                            "prompt": (
                                "Use the word 文化 (wénhuà) to talk about culture — "
                                "as the talk argues that food is the most direct way to understand a culture. "
                                "Example: 通过一个国家的饮食文化，你可以了解那里的人怎么生活。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_2[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }



    # ── Session 3: Group 3 — 责任, 改变, 习惯, 自然, 简单, 幸福 ──

    session_3 = {
        "title": "Session 3: Responsibility and Happiness — 责任与幸福",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Session 3 Introduction",
                "description": "Recap Sessions 1-2 and introduce Session 3 theme",
                "data": {
                    "text": (
                        "Welcome to Session 3 — the final learning session before review! "
                        "Over the past two sessions, you've learned 12 vocabulary words: "
                        "食物 (shíwù), 做饭 (zuòfàn), 健康 (jiànkāng), 环境 (huánjìng), "
                        "选择 (xuǎnzé), 未来 (wèilái) in Session 1, and "
                        "新鲜 (xīnxiān), 农民 (nóngmín), 市场 (shìchǎng), 味道 (wèidào), "
                        "传统 (chuántǒng), 文化 (wénhuà) in Session 2. "
                        "You've understood that Tzui Chuang wants us to go back to the kitchen, "
                        "visit farmers' markets, and respect culinary traditions. "
                        "Today, we'll explore the final part of the talk, "
                        "where she talks about each person's responsibility, about changing habits, "
                        "and about the simple happiness that comes from cooking with care. "
                        "The last 6 words will help you talk about the deepest values "
                        "in life. Let's begin!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 3 Vocabulary",
                "description": "Learn 6 words: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {
                    "text": (
                        "Let's learn our final 6 vocabulary words. These come from the closing section of the talk, "
                        "where Tzui Chuang delivers her most powerful message: cooking can change the world.\n\n"

                        "The first word is 责任 (zérèn). 责任 is a noun meaning 'responsibility'. "
                        "Tzui Chuang says that choosing good food isn't just a personal preference — "
                        "it's a 责任 (zérèn). A responsibility to yourself, to your family, and to nature. "
                        "For example: 保护环境是每个人的责任 — Protecting the environment is everyone's responsibility. "
                        "责 (zé) means 'duty, to blame' and 任 (rèn) means 'to bear, to take on'. "
                        "Another usage: 父母有责任照顾孩子 — Parents have the responsibility to take care of their children. "
                        "Or: 这是我的责任 — This is my responsibility.\n\n"

                        "The second word is 改变 (gǎibiàn). 改变 works as both a noun and a verb, "
                        "meaning 'change' or 'to change'. Tzui Chuang emphasizes that 改变 (gǎibiàn) "
                        "doesn't have to be dramatic — you don't need to become a vegetarian overnight. "
                        "Even small changes make a big difference. "
                        "For example: 小小的改变可以带来大大的不同 — Small changes can bring big differences. "
                        "改 (gǎi) means 'to correct, to alter' and 变 (biàn) means 'to change, to transform'. "
                        "Another usage: 改变世界从改变自己开始 — Changing the world starts with changing yourself. "
                        "Or: 这件事改变了我的想法 — This matter changed my thinking.\n\n"

                        "The third word is 习惯 (xíguàn). 习惯 works as both a noun and a verb, "
                        "meaning 'habit' or 'to be used to'. Tzui Chuang says that if we don't change our "
                        "饮食习惯 (yǐnshí xíguàn — eating habits), the future will be very worrying. "
                        "For example: 养成好的饮食习惯对健康很重要 — Developing good eating habits "
                        "is very important for health. 习 (xí) means 'to practice' and 惯 (guàn) means 'accustomed'. "
                        "As a verb: 我已经习惯了早起 — I've already gotten used to waking up early. "
                        "Another usage: 改变习惯需要时间 — Changing habits takes time.\n\n"

                        "The fourth word is 自然 (zìrán). 自然 works as a noun, adjective, and adverb, "
                        "meaning 'nature', 'natural', or 'naturally'. Tzui Chuang says we have a "
                        "responsibility to 自然 (zìrán) — to nature. When we choose sustainable food, "
                        "we're protecting the natural world. "
                        "For example: 大自然给了我们最好的食物 — Nature has given us the best food. "
                        "自 (zì) means 'self' and 然 (rán) means 'so, thus'. "
                        "As an adjective: 这种变化是很自然的 — This change is very natural. "
                        "As an adverb: 你会自然而然地开始关心食物 — You'll naturally start caring about food.\n\n"

                        "The fifth word is 简单 (jiǎndān). 简单 is an adjective meaning 'simple' or 'uncomplicated'. "
                        "Tzui Chuang emphasizes that change doesn't need to be complex — just a few 简单 (jiǎndān) steps: "
                        "go to the market instead of the supermarket, buy seasonal produce, cook at home instead of ordering takeout. "
                        "For example: 做饭是一件简单的事情，但它可以改变世界 — Cooking is a simple thing, "
                        "but it can change the world. 简 (jiǎn) means 'simple' and 单 (dān) means 'single, alone'. "
                        "Another usage: 简单的生活最幸福 — A simple life is the happiest. "
                        "Or: 这个问题很简单 — This problem is very simple.\n\n"

                        "The last word is 幸福 (xìngfú). 幸福 works as both a noun and an adjective, "
                        "meaning 'happiness' or 'happy/blessed'. Tzui Chuang ends the talk with a beautiful message: "
                        "when we treat food with care, the process itself is 幸福 (xìngfú). "
                        "Cooking for loved ones, sharing a family meal — that's simple happiness. "
                        "For example: 和家人一起吃饭是一种简单的幸福 — Eating together with family is a kind of "
                        "simple happiness. 幸 (xìng) means 'fortunate' and 福 (fú) means 'blessing'. "
                        "Another usage: 幸福不在远方，就在身边 — Happiness isn't far away, it's right beside you. "
                        "Or: 我觉得自己很幸福 — I feel very happy.\n\n"

                        "Excellent! You've now learned all 18 vocabulary words: "
                        "食物 (shíwù), 做饭 (zuòfàn), 健康 (jiànkāng), 环境 (huánjìng), "
                        "选择 (xuǎnzé), 未来 (wèilái), 新鲜 (xīnxiān), 农民 (nóngmín), "
                        "市场 (shìchǎng), 味道 (wèidào), 传统 (chuántǒng), 文化 (wénhuà), "
                        "责任 (zérèn), 改变 (gǎibiàn), 习惯 (xíguàn), 自然 (zìrán), "
                        "简单 (jiǎndān), 幸福 (xìngfú). Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Responsibility and Happiness",
                "description": "Learn 6 words: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 3 Vocabulary",
                "description": "Practice speaking 6 words: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 3 Vocabulary",
                "description": "Recognize 6 words: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 3 Vocabulary",
                "description": "Match meanings for 6 words: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 3 Vocabulary",
                "description": "Write 6 words: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Grammar and Usage Tips",
                "description": "How to use Session 3 vocabulary naturally in sentences",
                "data": {
                    "text": (
                        "Outstanding! You've completed all 18 vocabulary words. Let's look at how to use "
                        "these last 6 naturally.\n\n"
                        "责任 (zérèn) often pairs with 有 (yǒu) or 是 (shì): "
                        "有责任 (yǒu zérèn — have responsibility), "
                        "这是我的责任 (zhè shì wǒ de zérèn — this is my responsibility). "
                        "Patterns: 对...有责任 (duì...yǒu zérèn — have responsibility toward...), "
                        "负责任 (fù zérèn — take responsibility), "
                        "责任感 (zérèn gǎn — sense of responsibility).\n\n"
                        "改变 (gǎibiàn) as a verb: "
                        "改变习惯 (gǎibiàn xíguàn — change habits), "
                        "改变世界 (gǎibiàn shìjiè — change the world). "
                        "As a noun: 一个大的改变 (yí gè dà de gǎibiàn — a big change). "
                        "Patterns: 被...改变 (bèi...gǎibiàn — be changed by...), "
                        "想要改变 (xiǎng yào gǎibiàn — want to change).\n\n"
                        "习惯 (xíguàn) as a noun: "
                        "好习惯 (hǎo xíguàn — good habit), "
                        "坏习惯 (huài xíguàn — bad habit), "
                        "生活习惯 (shēnghuó xíguàn — lifestyle habits). "
                        "As a verb: 习惯了 (xíguànle — gotten used to). "
                        "Patterns: 养成习惯 (yǎngchéng xíguàn — develop a habit), "
                        "改掉习惯 (gǎidiào xíguàn — break a habit).\n\n"
                        "自然 (zìrán) as a noun: "
                        "大自然 (dà zìrán — nature, the natural world), "
                        "自然界 (zìrán jiè — the natural world). "
                        "As an adjective: 很自然 (hěn zìrán — very natural), "
                        "自然的食物 (zìrán de shíwù — natural food). "
                        "As an adverb: 自然而然 (zìrán ér rán — naturally, of its own accord). "
                        "Pattern: 回归自然 (huíguī zìrán — return to nature).\n\n"
                        "简单 (jiǎndān) often pairs with 很 (hěn) or 不 (bù): "
                        "很简单 (hěn jiǎndān — very simple), "
                        "不简单 (bù jiǎndān — not simple). "
                        "Patterns: 简单来说 (jiǎndān lái shuō — to put it simply), "
                        "简简单单 (jiǎnjiǎn dāndān — plain and simple). "
                        "Figurative: 他不简单 (tā bù jiǎndān — he's not simple = he's impressive).\n\n"
                        "幸福 (xìngfú) as an adjective: "
                        "很幸福 (hěn xìngfú — very happy), "
                        "幸福的生活 (xìngfú de shēnghuó — a happy life). "
                        "As a noun: 追求幸福 (zhuīqiú xìngfú — pursue happiness), "
                        "幸福感 (xìngfú gǎn — sense of happiness). "
                        "Patterns: 感到幸福 (gǎndào xìngfú — feel happy), "
                        "幸福就在身边 (xìngfú jiù zài shēnbiān — happiness is right beside you)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 3)",
                "description": "我知道有人会说：我很忙，没有时间做饭。",
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 3)",
                "description": "Practice speaking along with the excerpt about responsibility and happiness",
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Listen: Talk Excerpt (Part 3)",
                "description": "Listen to the passage you just read and follow along.",
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Write: Responsibility and Happiness",
                "description": "Write sentences using Session 3 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "责任",
                            "prompt": (
                                "Use the word 责任 (zérèn) to talk about responsibility — "
                                "as Tzui Chuang says choosing good food is a responsibility to yourself and to nature. "
                                "Example: 每个人都有责任保护我们生活的环境。"
                            ),
                        },
                        {
                            "targetVocab": "改变",
                            "prompt": (
                                "Use the word 改变 (gǎibiàn) to talk about change — "
                                "as the talk emphasizes that even small changes make a big difference. "
                                "Example: 只要我们愿意改变，未来一定会更好。"
                            ),
                        },
                        {
                            "targetVocab": "习惯",
                            "prompt": (
                                "Use the word 习惯 (xíguàn) to talk about habits — "
                                "as Tzui Chuang urges us to change our eating habits to protect the future. "
                                "Example: 养成每天运动的习惯对身体健康非常有好处。"
                            ),
                        },
                        {
                            "targetVocab": "自然",
                            "prompt": (
                                "Use the word 自然 (zìrán) to talk about nature or naturalness — "
                                "as the talk emphasizes our responsibility to the natural world. "
                                "Example: 大自然给了我们一切，我们应该好好保护它。"
                            ),
                        },
                        {
                            "targetVocab": "简单",
                            "prompt": (
                                "Use the word 简单 (jiǎndān) to talk about simplicity — "
                                "as Tzui Chuang says cooking is a simple thing but it can change the world. "
                                "Example: 有时候最简单的食物反而是最好吃的。"
                            ),
                        },
                        {
                            "targetVocab": "幸福",
                            "prompt": (
                                "Use the word 幸福 (xìngfú) to talk about happiness — "
                                "as the talk ends with the message: treating food with care is itself happiness. "
                                "Example: 和家人一起做饭、一起吃饭，就是最大的幸福。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_3[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }



    # ── Session 4: Review — all 18 words ──

    session_4_review = {
        "title": "Review",
        "activities": [
            # 1. introAudio
            {
                "activityType": "introAudio",
                "title": "Congratulations and Review",
                "description": "Review all 18 vocabulary words learned so far",
                "data": {
                    "text": (
                        "Congratulations! You've completed 3 learning sessions and mastered 18 Chinese vocabulary "
                        "words on the theme of food, cooking, and sustainability. Let's review them all!\n\n"
                        "In Session 1, you learned: 食物 (shíwù — food), 做饭 (zuòfàn — to cook), "
                        "健康 (jiànkāng — health), 环境 (huánjìng — environment), "
                        "选择 (xuǎnzé — choice), 未来 (wèilái — future). These are the foundational words "
                        "that help you talk about the relationship between food and life.\n\n"
                        "In Session 2, you learned: 新鲜 (xīnxiān — fresh), 农民 (nóngmín — farmer), "
                        "市场 (shìchǎng — market), 味道 (wèidào — flavor), "
                        "传统 (chuántǒng — tradition), 文化 (wénhuà — culture). These words help you talk about "
                        "the experience of visiting markets and understanding food culture.\n\n"
                        "In Session 3, you learned: 责任 (zérèn — responsibility), 改变 (gǎibiàn — change), "
                        "习惯 (xíguàn — habit), 自然 (zìrán — nature), "
                        "简单 (jiǎndān — simple), 幸福 (xìngfú — happiness). These words help you understand "
                        "that cooking consciously is both a responsibility and a source of happiness.\n\n"
                        "Now let's review all 18 words through flashcard activities!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Review All 18 Words",
                "description": "Review 18 words: 食物, 做饭, 健康, 环境, 选择, 未来, 新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak All 18 Words",
                "description": "Practice speaking 18 words: 食物, 做饭, 健康, 环境, 选择, 未来, 新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize All Vocabulary",
                "description": "Recognize 18 words: 食物, 做饭, 健康, 环境, 选择, 未来, 新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
        ],
    }


    # ── Session 5: Full reading + farewell ──

    session_5_final = {
        "title": "Full Talk Reading",
        "activities": [
            # 1. introAudio — intro
            {
                "activityType": "introAudio",
                "title": "Introduction to Full Reading",
                "description": "Introduction to the complete talk reading session",
                "data": {
                    "text": (
                        "Welcome to the final session! Today you'll read the complete talk "
                        "by Tzui Chuang Mullinax from start to finish. You've learned 18 vocabulary words "
                        "across 3 sessions and reviewed them in Session 4. Now it's time to put it all together. "
                        "Read slowly, pay attention to the words you've learned, and notice how they "
                        "connect with each other in real context. Enjoy the reading!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. reading — full transcript
            {
                "activityType": "reading",
                "title": "Read: The Complete Talk",
                "description": "大家好，我是庄祖宜。今天我想跟大家聊一个我最喜欢的话题：食物。",
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 3. speakReading — full transcript
            {
                "activityType": "speakReading",
                "title": "Speak: The Complete Talk",
                "description": "Practice speaking along with the complete talk",
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 4. readAlong — full transcript
            {
                "activityType": "readAlong",
                "title": "Listen: The Complete Talk",
                "description": "Listen to the complete talk and follow along.",
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 5. introAudio — farewell reviewing all 18 words
            {
                "activityType": "introAudio",
                "title": "Farewell and Vocabulary Review",
                "description": "Review all 18 vocabulary words and farewell",
                "data": {
                    "text": (
                        "Congratulations on completing the entire course! You've come an incredible way. "
                        "Let's review all 18 vocabulary words one final time.\n\n"

                        "食物 (shíwù) — food, foodstuff. "
                        "Example: 了解食物的来源是对自己负责 — Understanding where your food comes from is being responsible to yourself.\n\n"

                        "做饭 (zuòfàn) — to cook, to prepare a meal. "
                        "Example: 学会做饭是一种生活技能 — Learning to cook is a life skill.\n\n"

                        "健康 (jiànkāng) — health, healthy. "
                        "Example: 好的食物是健康的基础 — Good food is the foundation of health.\n\n"

                        "环境 (huánjìng) — environment. "
                        "Example: 每一次购物都是对环境的投票 — Every purchase is a vote for the environment.\n\n"

                        "选择 (xuǎnzé) — choice, to choose. "
                        "Example: 聪明的选择从了解开始 — Smart choices start with understanding.\n\n"

                        "未来 (wèilái) — future. "
                        "Example: 我们的选择决定了未来的样子 — Our choices determine what the future looks like.\n\n"

                        "新鲜 (xīnxiān) — fresh, novel. "
                        "Example: 新鲜的食材不需要复杂的烹饪 — Fresh ingredients don't need complicated cooking.\n\n"

                        "农民 (nóngmín) — farmer. "
                        "Example: 感谢农民的辛苦劳动 — Thank the farmers for their hard work.\n\n"

                        "市场 (shìchǎng) — market, marketplace. "
                        "Example: 菜市场是城市最有生命力的地方 — The vegetable market is the most vibrant place in a city.\n\n"

                        "味道 (wèidào) — flavor, taste. "
                        "Example: 记忆中最好的味道是家的味道 — The best flavor in memory is the taste of home.\n\n"

                        "传统 (chuántǒng) — tradition, traditional. "
                        "Example: 传统的智慧值得我们学习 — Traditional wisdom is worth learning from.\n\n"

                        "文化 (wénhuà) — culture. "
                        "Example: 食物是文化最美味的表达 — Food is the most delicious expression of culture.\n\n"

                        "责任 (zérèn) — responsibility. "
                        "Example: 吃得好是对自己和地球的责任 — Eating well is a responsibility to yourself and the planet.\n\n"

                        "改变 (gǎibiàn) — change, to change. "
                        "Example: 每一个小改变都有意义 — Every small change has meaning.\n\n"

                        "习惯 (xíguàn) — habit, to be used to. "
                        "Example: 好的习惯会带来好的生活 — Good habits bring a good life.\n\n"

                        "自然 (zìrán) — nature, natural. "
                        "Example: 尊重自然就是尊重自己 — Respecting nature is respecting yourself.\n\n"

                        "简单 (jiǎndān) — simple, uncomplicated. "
                        "Example: 简单的食物，简单的快乐 — Simple food, simple joy.\n\n"

                        "幸福 (xìngfú) — happiness, happy. "
                        "Example: 用心做饭，用心生活，这就是幸福 — Cook with care, live with care, that is happiness.\n\n"

                        "As Tzui Chuang said: 做饭是一件简单的事情，但它可以改变世界 "
                        "(zuòfàn shì yí jiàn jiǎndān de shìqing, dàn tā kěyǐ gǎibiàn shìjiè) — "
                        "Cooking is a simple thing, but it can change the world. "
                        "You haven't just learned 18 Chinese vocabulary words — you've gained a deeper understanding "
                        "of how food connects culture, nature, and happiness. "
                        "Remember: every meal is an opportunity to create change. "
                        "Thank you for learning with us, and we wish you delicious food, "
                        "good health, and happiness in the simplest things! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Learn Through Podcasts: '吃出更好的未來' — 莊祖宜 (Eating for a Better Future)",
        "description": (
            "DID YOU KNOW EVERY MEAL YOU EAT IS DECIDING THE FUTURE OF THE PLANET?\n\n"
            "Every time you choose supermarket vegetables over the local market, every time you order "
            "takeout instead of cooking, every time you skip the question 'where did this food come from?' — "
            "you're unknowingly feeding a vicious cycle: depleted soil, polluted water, "
            "and food that's lost its real flavor.\n\n"
            "Food writer and chef Tzui Chuang Mullinax (莊祖宜) from TED Shanghai will open your eyes: "
            "she once left anthropology research to attend culinary school, because she realized that "
            "walking into a country's market is the fastest way to understand its culture. "
            "Tzui Chuang argues that cooking consciously — choosing fresh ingredients, supporting local "
            "farmers, respecting culinary traditions — isn't just a personal pleasure, "
            "it's a responsibility to nature and the future.\n\n"
            "When you go back to the kitchen and treat every bite of food with care, "
            "you're not just cooking — you're creating a better future. "
            "And that process itself is happiness.\n\n"
            "Learn 18 powerful vocabulary words about food, culture, and sustainability through an immersive "
            "multi-sensory experience that upgrades both your thinking and your Chinese at the same time."
        ),
        "preview": {
            "text": (
                "Did you know that every meal is a vote for the future? "
                "Chef and food writer Tzui Chuang Mullinax from TED Shanghai will completely transform "
                "how you see cooking and food choices. In this course, you'll learn "
                "18 Chinese vocabulary words at HSK2-HSK3 level about food and sustainability: "
                "食物 (shíwù — food), 做饭 (zuòfàn — to cook), "
                "健康 (jiànkāng — health), 环境 (huánjìng — environment), "
                "选择 (xuǎnzé — choice), 未来 (wèilái — future), "
                "新鲜 (xīnxiān — fresh), 农民 (nóngmín — farmer), "
                "市场 (shìchǎng — market), 味道 (wèidào — flavor), "
                "传统 (chuántǒng — tradition), 文化 (wénhuà — culture), "
                "责任 (zérèn — responsibility), 改变 (gǎibiàn — change), "
                "习惯 (xíguàn — habit), 自然 (zìrán — nature), "
                "简单 (jiǎndān — simple), 幸福 (xìngfú — happiness). "
                "Across 5 sessions of flashcards, reading, speaking, and writing, "
                "you'll not only master the vocabulary but also gain a deeper understanding "
                "of how food connects culture, nature, and happiness — "
                "and turn every meal into an act that changes the world."
            ),
        },
        "youtubeUrl": "https://www.youtube.com/watch?v=wcfLMfo6LQc",
        "contentTypeTags": ["podcast"],
        "difficultyTags": [
            "preintermediate",
            "vocab_intermediate",
            "reading_preintermediate",
            "writing_intermediate",
        ],
        "skillFocusTags": ["balanced_skills"],
        "learningSessions": [
            session_1,
            session_2,
            session_3,
            session_4_review,
            session_5_final,
        ],
    }

    return content


def create():
    token = get_firebase_id_token(UID)
    content = build_content()
    content = strip_keys(content)
    validate(content)

    resp = requests.post(
        f"{API_BASE}/curriculum/create",
        json={
            "firebaseIdToken": token,
            "language": "zh",
            "userLanguage": "en",
            "content": json.dumps(content),
        },
    )
    resp.raise_for_status()
    data = resp.json()
    curriculum_id = data["id"]
    print(f"Created curriculum: {curriculum_id}")

    # Set is_public = false (default, but explicit)
    requests.post(
        f"{API_BASE}/curriculum/setPublic",
        json={"firebaseIdToken": token, "id": curriculum_id, "isPublic": False},
    )
    print("Set is_public = false")

    return curriculum_id


if __name__ == "__main__":
    cid = create()
    print(f"\nDone! Curriculum ID: {cid}")
