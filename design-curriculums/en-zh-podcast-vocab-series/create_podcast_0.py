"""
Create en-zh podcast curriculum #0:
陳永儀 (May Chen) — "沒有「負面能量」是好事嗎？需要重新認識的「情緒反應」"
(Acknowledge and Embrace Your Negative Emotions)

TEDxTaipei, ~15 minutes, about emotions and psychology.
YouTube: https://www.youtube.com/watch?v=uiJ4zibW8_M

18 HSK2-HSK3 vocabulary words in 3 groups of 6.
SAME 18 words and reading passages as vi-zh podcast #0.
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

VOCAB_GROUP_1 = ["情绪", "负面", "感觉", "表达", "压力", "健康"]
VOCAB_GROUP_2 = ["接受", "影响", "控制", "内心", "勇气", "害怕"]
VOCAB_GROUP_3 = ["愤怒", "悲伤", "理解", "成长", "经历", "力量"]
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

    # Every activity has title, description, practiceMinutes
    for i, session in enumerate(content["learningSessions"]):
        if "title" not in session:
            errors.append(f"Session {i} missing title")
        for j, act in enumerate(session["activities"]):
            for field in ("title", "description", "practiceMinutes"):
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



# ── Chinese reading passages (SAME as vi-zh #0, simplified Chinese) ──

READING_1 = (
    "大家好，我是陈永仪。今天我想跟大家聊一个话题：负面情绪真的是坏事吗？\n\n"
    "我们从小就被教导要开心、要积极、要正面。生气是不好的，哭是软弱的表现，"
    "害怕说明你不够勇敢。可是，你有没有想过，这些所谓的\u201c负面情绪\u201d，"
    "其实是我们身体发出的信号？\n\n"
    "情绪就像身体的温度计。当你发烧的时候，你不会说\u201c发烧是坏事，"
    "我要假装没有发烧\u201d。你会去看医生，去找原因。情绪也是一样的。"
    "当你感觉愤怒、悲伤或者害怕的时候，这些感觉在告诉你：有些事情需要你注意。\n\n"
    "可是很多人选择压抑自己的情绪。他们不表达，不说出来，"
    "觉得这样才是\u201c坚强\u201d。结果呢？压力越来越大，身体越来越不健康。"
    "研究表明，长期压抑情绪会影响免疫系统，增加生病的风险。"
)

READING_2 = (
    "所以，我们应该怎么做呢？第一步，就是接受。接受你现在的感觉。\n\n"
    "你生气了？好，承认你在生气。你害怕了？好，告诉自己：我现在很害怕。"
    "这不是软弱，这是勇气。承认自己的情绪需要很大的勇气。\n\n"
    "很多人以为控制情绪就是不让自己有情绪。其实不是的。"
    "真正的控制是：你知道自己在感觉什么，你理解为什么会有这种感觉，"
    "然后你选择怎么回应。\n\n"
    "我遇到过一个学生，他从来不表达自己的情绪。他觉得男生不应该哭，"
    "不应该害怕，不应该说\u201c我不行\u201d。结果呢？他的内心越来越封闭，"
    "压力越来越大，最后影响了他的学习和人际关系。\n\n"
    "当他终于有勇气说出\u201c我很害怕\u201d的时候，他哭了。"
    "但那一刻，他开始接受自己，开始真正地面对内心的感觉。"
)

READING_3 = (
    "愤怒、悲伤、害怕\u2014\u2014这些情绪都有它们存在的理由。\n\n"
    "愤怒告诉你：有人越过了你的底线。悲伤告诉你：你失去了重要的东西。"
    "害怕告诉你：前面可能有危险。这些都是身体在保护你。\n\n"
    "我希望大家能理解一件事：情绪不分好坏。所有的情绪都是我们生命经历的一部分。"
    "当你经历愤怒，你学会了什么是公平。当你经历悲伤，你学会了什么是珍惜。"
    "当你经历害怕，你学会了什么是勇气。\n\n"
    "每一种情绪都是成长的力量。不要害怕你的感觉，不要压抑你的内心。"
    "学会接受，学会表达，学会理解\u2014\u2014这就是真正的健康。\n\n"
    "最后我想说：你的情绪就是你的力量。当你有勇气面对自己的内心，"
    "你就已经在成长了。谢谢大家。"
)

FULL_TRANSCRIPT = (
    "大家好，我是陈永仪。今天我想跟大家聊一个话题：负面情绪真的是坏事吗？\n\n"
    "我们从小就被教导要开心、要积极、要正面。生气是不好的，哭是软弱的表现，"
    "害怕说明你不够勇敢。可是，你有没有想过，这些所谓的\u201c负面情绪\u201d，"
    "其实是我们身体发出的信号？\n\n"
    "情绪就像身体的温度计。当你发烧的时候，你不会说\u201c发烧是坏事，"
    "我要假装没有发烧\u201d。你会去看医生，去找原因。情绪也是一样的。"
    "当你感觉愤怒、悲伤或者害怕的时候，这些感觉在告诉你：有些事情需要你注意。\n\n"
    "可是很多人选择压抑自己的情绪。他们不表达，不说出来，"
    "觉得这样才是\u201c坚强\u201d。结果呢？压力越来越大，身体越来越不健康。"
    "研究表明，长期压抑情绪会影响免疫系统，增加生病的风险。\n\n"
    "所以，我们应该怎么做呢？第一步，就是接受。接受你现在的感觉。\n\n"
    "你生气了？好，承认你在生气。你害怕了？好，告诉自己：我现在很害怕。"
    "这不是软弱，这是勇气。承认自己的情绪需要很大的勇气。\n\n"
    "很多人以为控制情绪就是不让自己有情绪。其实不是的。"
    "真正的控制是：你知道自己在感觉什么，你理解为什么会有这种感觉，"
    "然后你选择怎么回应。\n\n"
    "我遇到过一个学生，他从来不表达自己的情绪。他觉得男生不应该哭，"
    "不应该害怕，不应该说\u201c我不行\u201d。结果呢？他的内心越来越封闭，"
    "压力越来越大，最后影响了他的学习和人际关系。\n\n"
    "当他终于有勇气说出\u201c我很害怕\u201d的时候，他哭了。"
    "但那一刻，他开始接受自己，开始真正地面对内心的感觉。\n\n"
    "愤怒、悲伤、害怕\u2014\u2014这些情绪都有它们存在的理由。\n\n"
    "愤怒告诉你：有人越过了你的底线。悲伤告诉你：你失去了重要的东西。"
    "害怕告诉你：前面可能有危险。这些都是身体在保护你。\n\n"
    "我希望大家能理解一件事：情绪不分好坏。所有的情绪都是我们生命经历的一部分。"
    "当你经历愤怒，你学会了什么是公平。当你经历悲伤，你学会了什么是珍惜。"
    "当你经历害怕，你学会了什么是勇气。\n\n"
    "每一种情绪都是成长的力量。不要害怕你的感觉，不要压抑你的内心。"
    "学会接受，学会表达，学会理解\u2014\u2014这就是真正的健康。\n\n"
    "最后我想说：你的情绪就是你的力量。当你有勇气面对自己的内心，"
    "你就已经在成长了。谢谢大家。"
)


def build_content():
    # ── Session 1: Group 1 — 情绪, 负面, 感觉, 表达, 压力, 健康 ──

    session_1 = {
        "title": "Session 1: Emotions and Energy — 情绪与能量",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Introduction to the Talk",
                "description": "Introduction to May Chen's TEDxTaipei talk on negative emotions",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Welcome to the Chinese vocabulary podcast course! "
                        "Today we're going to explore a truly thought-provoking talk from TEDxTaipei — "
                        "'沒有「負面能量」是好事嗎？' by psychology professor May Chen (陳永儀). "
                        "Professor Chen poses a question that forces us to rethink everything: "
                        "Is it really a good thing to have no negative energy? "
                        "In everyday life, we're taught to always be happy, stay positive, keep smiling. "
                        "But Professor Chen argues that emotions like anger, sadness, and fear — "
                        "all of them are natural and necessary human responses. "
                        "Suppressing your emotions doesn't make you stronger — on the contrary, "
                        "it damages your health, both physically and mentally. "
                        "In this first session, you'll learn 6 essential vocabulary words "
                        "related to emotions and psychology. Each word appears in the talk "
                        "and will help you understand how Chinese speakers discuss "
                        "their inner emotional world. Let's get started!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 1 Vocabulary",
                "description": "Learn 6 words: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Let's learn our first 6 vocabulary words. Each one is closely tied to the content "
                        "of Professor May Chen's talk about human emotions.\n\n"

                        "The first word is 情绪 (qíngxù). 情绪 is a noun meaning 'emotions' or 'mood'. "
                        "This is the central word of the entire talk. Professor Chen says that everyone has "
                        "情绪 (qíngxù), and every type of emotion has value. For example: "
                        "每个人都有情绪，这是很正常的 — Everyone has emotions, this is perfectly normal. "
                        "In Chinese, 情 (qíng) means 'feelings' and 绪 (xù) means 'threads'. "
                        "So 情绪 (qíngxù) evokes the image of emotional threads woven together inside you. "
                        "You can use this word when talking about daily moods: "
                        "今天我的情绪不太好 — My mood isn't great today.\n\n"

                        "The second word is 负面 (fùmiàn). 负面 is an adjective meaning 'negative' or "
                        "'the downside'. In the talk, Professor Chen challenges the idea that "
                        "负面情绪 (fùmiàn qíngxù) — negative emotions — are bad. She argues that society "
                        "has wrongly labeled many natural emotions. For example: "
                        "负面情绪不一定是坏事 — Negative emotions aren't necessarily a bad thing. "
                        "负 (fù) means 'to bear, to carry' and 面 (miàn) means 'face, surface', "
                        "so 负面 (fùmiàn) literally means 'the burdened side'. "
                        "This word often pairs with 情绪 (qíngxù), 能量 (néngliàng, energy), "
                        "or 影响 (yǐngxiǎng, influence): "
                        "不要害怕负面的感觉 — Don't be afraid of negative feelings.\n\n"

                        "The third word is 感觉 (gǎnjué). 感觉 works as both a noun and a verb, "
                        "meaning 'feeling' or 'to feel'. This is one of the most common words in Chinese "
                        "when talking about personal experience. Professor Chen emphasizes that we need "
                        "to listen to our 感觉 (gǎnjué) rather than ignore them. For example: "
                        "你现在有什么感觉？ — How do you feel right now? "
                        "感 (gǎn) means 'to sense' and 觉 (jué) means 'to perceive'. "
                        "You'll encounter this word constantly in daily conversation: "
                        "我感觉今天会下雨 — I feel like it's going to rain today.\n\n"

                        "The fourth word is 表达 (biǎodá). 表达 is a verb meaning 'to express' or "
                        "'to convey'. One of the most important messages of the talk is: learn to "
                        "表达 (biǎodá) your emotions. Suppression isn't the answer — expression is "
                        "the right path. For example: "
                        "我们应该学会表达自己的情绪 — We should learn to express our emotions. "
                        "表 (biǎo) means 'outer, to show' and 达 (dá) means 'to reach'. "
                        "When you 表达 (biǎodá), you're bringing what's inside out. "
                        "Another usage: 他不善于表达感情 — He's not good at expressing feelings.\n\n"

                        "The fifth word is 压力 (yālì). 压力 is a noun meaning 'pressure' or 'stress'. "
                        "Professor Chen explains that when we suppress our emotions, "
                        "压力 (yālì) builds up inside and eventually explodes in unhealthy ways. "
                        "For example: 工作压力太大了，我需要休息 — "
                        "The work pressure is too much, I need a break. "
                        "压 (yā) means 'to press down' and 力 (lì) means 'force'. "
                        "The image is vivid: pressure is a force pressing down on you. "
                        "This word is extremely common in modern life: "
                        "学生的压力越来越大 — Students are under more and more pressure.\n\n"

                        "The last word for today is 健康 (jiànkāng). 健康 works as both a noun and "
                        "an adjective, meaning 'health' or 'healthy'. Professor Chen connects emotions "
                        "to 健康 (jiànkāng): facing and accepting your emotions helps you live healthier "
                        "in both body and mind. For example: "
                        "心理健康和身体健康一样重要 — Mental health is just as important as physical health. "
                        "健 (jiàn) means 'strong' and 康 (kāng) means 'well-being'. "
                        "You can use this word in many contexts: "
                        "祝你身体健康 — Wishing you good health. "
                        "Or: 这种生活方式不健康 — This lifestyle isn't healthy.\n\n"

                        "So now you know your first 6 words: "
                        "情绪 (qíngxù), 负面 (fùmiàn), 感觉 (gǎnjué), "
                        "表达 (biǎodá), 压力 (yālì), 健康 (jiànkāng). "
                        "Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Emotions and Energy",
                "description": "Learn 6 words: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 1 Vocabulary",
                "description": "Practice speaking 6 words: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 1 Vocabulary",
                "description": "Recognize 6 words: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 1 Vocabulary",
                "description": "Match meanings for 6 words: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 1 Vocabulary",
                "description": "Write 6 words: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Grammar and Usage Tips",
                "description": "How to use Session 1 vocabulary naturally in sentences",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Great work! You've met your first 6 vocabulary words. Now let's look at how "
                        "to use them naturally in sentences.\n\n"
                        "情绪 (qíngxù) often pairs with adjectives to describe a state: "
                        "情绪很好 (mood is good), 情绪不稳定 (mood is unstable). "
                        "You can also say 控制情绪 (kòngzhì qíngxù — control emotions) "
                        "or 情绪反应 (qíngxù fǎnyìng — emotional reaction).\n\n"
                        "负面 (fùmiàn) always comes before a noun as a modifier: "
                        "负面情绪 (fùmiàn qíngxù), 负面影响 (fùmiàn yǐngxiǎng — negative influence), "
                        "负面消息 (fùmiàn xiāoxi — negative news). "
                        "The opposite is 正面 (zhèngmiàn) — positive.\n\n"
                        "感觉 (gǎnjué) is very flexible. As a verb: "
                        "我感觉很累 (wǒ gǎnjué hěn lèi — I feel very tired). "
                        "As a noun: 这种感觉很奇怪 (zhè zhǒng gǎnjué hěn qíguài — "
                        "This feeling is very strange). Common pattern: 感觉 + adjective, "
                        "or 感觉 + 像 + comparison.\n\n"
                        "表达 (biǎodá) usually takes an object: "
                        "表达感情 (biǎodá gǎnqíng — express feelings), "
                        "表达想法 (biǎodá xiǎngfǎ — express thoughts), "
                        "表达意见 (biǎodá yìjiàn — express opinions). "
                        "Pattern: 用...来表达... (yòng...lái biǎodá... — use...to express...).\n\n"
                        "压力 (yālì) pairs with 大 or 小: "
                        "压力很大 (yālì hěn dà — a lot of pressure), "
                        "没有压力 (méiyǒu yālì — no pressure). "
                        "Useful patterns: 给...压力 (gěi...yālì — put pressure on...), "
                        "减轻压力 (jiǎnqīng yālì — relieve pressure).\n\n"
                        "健康 (jiànkāng) as an adjective: "
                        "身体很健康 (shēntǐ hěn jiànkāng — body is very healthy). "
                        "As a noun: 注意健康 (zhùyì jiànkāng — pay attention to health). "
                        "A key phrase: 身心健康 (shēnxīn jiànkāng — healthy in body and mind) — "
                        "this is exactly the core message of Professor Chen's talk."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 1)",
                "description": "大家好，我是陈永仪。今天我想跟大家聊一个话题：负面情绪真的是坏事吗？",
                "practiceMinutes": 9,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 1)",
                "description": "Practice speaking along with the excerpt about negative emotions",
                "practiceMinutes": 15,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Listen: Talk Excerpt (Part 1)",
                "description": "Listen to the passage you just read and follow along.",
                "practiceMinutes": 3,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Write: Emotions and Energy",
                "description": "Write sentences using Session 1 vocabulary",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "情绪",
                            "prompt": (
                                "Use the word 情绪 (qíngxù) to talk about mood or emotions — "
                                "as Professor Chen says, every type of emotion has value and deserves to be heard. "
                                "Example: 每个人都有情绪，我们不应该害怕自己的情绪。"
                            ),
                        },
                        {
                            "targetVocab": "负面",
                            "prompt": (
                                "Use the word 负面 (fùmiàn) to describe something negative — "
                                "as the talk challenges the idea that negative emotions are always bad. "
                                "Example: 负面情绪并不可怕，可怕的是我们不敢面对它。"
                            ),
                        },
                        {
                            "targetVocab": "感觉",
                            "prompt": (
                                "Use the word 感觉 (gǎnjué) to describe a feeling or experience — "
                                "as Professor Chen urges us to listen to our feelings instead of ignoring them. "
                                "Example: 我感觉今天的天气让人心情很好。"
                            ),
                        },
                        {
                            "targetVocab": "表达",
                            "prompt": (
                                "Use the word 表达 (biǎodá) to talk about expressing thoughts or emotions — "
                                "as the talk emphasizes that expressing emotions is better than suppressing them. "
                                "Example: 学会表达自己的想法是一件很重要的事情。"
                            ),
                        },
                        {
                            "targetVocab": "压力",
                            "prompt": (
                                "Use the word 压力 (yālì) to talk about pressure in life — "
                                "as Professor Chen explains that suppressing emotions causes pressure to build up. "
                                "Example: 现在年轻人的工作压力越来越大，需要学会放松。"
                            ),
                        },
                        {
                            "targetVocab": "健康",
                            "prompt": (
                                "Use the word 健康 (jiànkāng) to talk about physical or mental health — "
                                "as the talk connects facing emotions with overall well-being. "
                                "Example: 心理健康和身体健康一样重要，我们都应该重视。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_1[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Session 2: Group 2 — 接受, 影响, 控制, 内心, 勇气, 害怕 ──

    session_2 = {
        "title": "Session 2: Facing and Accepting — 面对与接受",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Session 2 Introduction",
                "description": "Recap Session 1 and introduce Session 2 theme",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Welcome back to Session 2! In the previous session, we learned 6 important words: "
                        "情绪 (qíngxù — emotions), 负面 (fùmiàn — negative), 感觉 (gǎnjué — feeling), "
                        "表达 (biǎodá — express), 压力 (yālì — pressure), and 健康 (jiànkāng — health). "
                        "Do you remember them? Professor May Chen asked whether having no negative emotions "
                        "is truly a good thing. Today we'll dive deeper into the next part of the talk, "
                        "where she discusses facing your emotions instead of running away from them. "
                        "You'll learn 6 new words related to acceptance, influence, "
                        "and courage. Let's go!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 2 Vocabulary",
                "description": "Learn 6 words: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Let's learn today's 6 new vocabulary words. These words come from the middle section "
                        "of the talk, where Professor Chen begins offering solutions to the problem of emotional suppression.\n\n"

                        "The first word is 接受 (jiēshòu). 接受 is a verb meaning 'to accept' or 'to receive'. "
                        "This is the single most important word in this section of the talk. Professor Chen says "
                        "the first step to emotional health is 接受 (jiēshòu) — accepting that you're sad, "
                        "angry, or scared. Not fighting it, but embracing it. "
                        "For example: 我们要学会接受自己的不完美 — We need to learn to accept our own imperfections. "
                        "接 (jiē) means 'to receive' and 受 (shòu) means 'to bear, to accept'. "
                        "When you 接受 (jiēshòu), you open your heart to receive rather than push away. "
                        "Another usage: 他终于接受了这个事实 — He finally accepted this fact.\n\n"

                        "The second word is 影响 (yǐngxiǎng). 影响 works as both a noun and a verb, "
                        "meaning 'influence' or 'to affect'. Professor Chen explains that suppressed emotions "
                        "will 影响 (yǐngxiǎng) every aspect of your life — from relationships to physical health. "
                        "For example: 情绪会影响我们的身体健康 — Emotions can affect our physical health. "
                        "影 (yǐng) means 'shadow' and 响 (xiǎng) means 'echo, sound'. "
                        "Influence is like a shadow — you can't always see it clearly, but it's always there. "
                        "Common patterns: 对...有影响 (duì...yǒu yǐngxiǎng — have an influence on...), "
                        "受到...的影响 (shòudào...de yǐngxiǎng — be influenced by...).\n\n"

                        "The third word is 控制 (kòngzhì). 控制 is a verb meaning 'to control' or 'to manage'. "
                        "Many people think 控制情绪 (kòngzhì qíngxù — controlling emotions) means suppressing them. "
                        "But Professor Chen argues that real control means understanding and navigating your emotions, "
                        "not crushing them. For example: "
                        "控制情绪不是压抑情绪，而是理解情绪 — Controlling emotions isn't suppressing them, "
                        "it's understanding them. 控 (kòng) means 'to hold' and 制 (zhì) means 'to restrain'. "
                        "Another usage: 他很难控制自己的脾气 — He finds it hard to control his temper.\n\n"

                        "The fourth word is 内心 (nèixīn). 内心 is a noun meaning 'inner heart' or "
                        "'one's inner world'. Professor Chen encourages everyone to look into their 内心 (nèixīn) — "
                        "to listen to the voice inside rather than just following society's expectations. "
                        "For example: 我们应该倾听自己内心的声音 — We should listen to the voice of our inner heart. "
                        "内 (nèi) means 'inside' and 心 (xīn) means 'heart'. "
                        "内心 (nèixīn) is the world inside your heart. "
                        "Another usage: 他内心其实很善良 — Deep down, he's actually very kind.\n\n"

                        "The fifth word is 勇气 (yǒngqì). 勇气 is a noun meaning 'courage' or 'bravery'. "
                        "To face your emotions, you need 勇气 (yǒngqì). Admitting that you're sad or scared — "
                        "that's not weakness, that's courage. "
                        "For example: 承认自己的弱点需要很大的勇气 — Admitting your weaknesses takes great courage. "
                        "勇 (yǒng) means 'brave' and 气 (qì) means 'spirit, energy'. "
                        "Another usage: 你要有勇气面对困难 — You need the courage to face difficulties.\n\n"

                        "The last word is 害怕 (hàipà). 害怕 is a verb meaning 'to be afraid' or 'to fear'. "
                        "Professor Chen says 害怕 (hàipà) is one of the most misunderstood emotions. "
                        "Being afraid doesn't mean you're weak — it's a warning signal that helps you avoid danger. "
                        "For example: 不要害怕犯错，犯错是学习的一部分 — Don't be afraid of making mistakes; "
                        "mistakes are part of learning. 害 (hài) means 'harm' and 怕 (pà) means 'to fear'. "
                        "Another usage: 小孩子害怕黑暗是很正常的 — It's perfectly normal for children to be afraid of the dark.\n\n"

                        "So now you've learned 6 more words: "
                        "接受 (jiēshòu), 影响 (yǐngxiǎng), 控制 (kòngzhì), "
                        "内心 (nèixīn), 勇气 (yǒngqì), 害怕 (hàipà). "
                        "Together with the 6 from Session 1, you now have 12 vocabulary words! Let's keep practicing!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Facing and Accepting",
                "description": "Learn 6 words: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 2 Vocabulary",
                "description": "Practice speaking 6 words: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 2 Vocabulary",
                "description": "Recognize 6 words: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 2 Vocabulary",
                "description": "Match meanings for 6 words: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 2 Vocabulary",
                "description": "Write 6 words: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Grammar and Usage Tips",
                "description": "How to use Session 2 vocabulary naturally in sentences",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Well done! You've got 6 new words under your belt. Let's see how to use them "
                        "more naturally in sentences.\n\n"
                        "接受 (jiēshòu) often takes a noun object: "
                        "接受现实 (jiēshòu xiànshí — accept reality), "
                        "接受批评 (jiēshòu pīpíng — accept criticism), "
                        "接受邀请 (jiēshòu yāoqǐng — accept an invitation). "
                        "Negative patterns: 无法接受 (wúfǎ jiēshòu — unable to accept), "
                        "难以接受 (nányǐ jiēshòu — hard to accept).\n\n"
                        "影响 (yǐngxiǎng) has two main uses. As a verb: "
                        "这件事影响了我的心情 (zhè jiàn shì yǐngxiǎngle wǒ de xīnqíng — "
                        "This matter affected my mood). As a noun: "
                        "他对我有很大的影响 (tā duì wǒ yǒu hěn dà de yǐngxiǎng — "
                        "He has a big influence on me).\n\n"
                        "控制 (kòngzhì) usually takes a specific object: "
                        "控制情绪 (kòngzhì qíngxù), 控制体重 (kòngzhì tǐzhòng — control weight), "
                        "控制时间 (kòngzhì shíjiān — manage time). "
                        "Passive pattern: 被...控制 (bèi...kòngzhì — be controlled by...).\n\n"
                        "内心 (nèixīn) usually comes before a noun or adjective: "
                        "内心世界 (nèixīn shìjiè — inner world), "
                        "内心深处 (nèixīn shēnchù — deep inside one's heart), "
                        "内心强大 (nèixīn qiángdà — inner strength).\n\n"
                        "勇气 (yǒngqì) often pairs with 有 or 没有: "
                        "有勇气 (yǒu yǒngqì — have courage), 没有勇气 (méiyǒu yǒngqì — lack courage). "
                        "Patterns: 鼓起勇气 (gǔqǐ yǒngqì — muster up courage), "
                        "需要勇气 (xūyào yǒngqì — need courage).\n\n"
                        "害怕 (hàipà) can be followed by a noun or verb: "
                        "害怕失败 (hàipà shībài — afraid of failure), "
                        "害怕孤独 (hàipà gūdú — afraid of loneliness), "
                        "害怕被拒绝 (hàipà bèi jùjué — afraid of being rejected). "
                        "Pattern: 不要害怕 + verb (bùyào hàipà + verb — don't be afraid to...)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 2)",
                "description": "所以，我们应该怎么做呢？第一步，就是接受。接受你现在的感觉。",
                "practiceMinutes": 9,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 2)",
                "description": "Practice speaking along with the excerpt about accepting emotions",
                "practiceMinutes": 15,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Listen: Talk Excerpt (Part 2)",
                "description": "Listen to the passage you just read and follow along.",
                "practiceMinutes": 3,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Write: Facing and Accepting",
                "description": "Write sentences using Session 2 vocabulary",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "接受",
                            "prompt": (
                                "Use the word 接受 (jiēshòu) to talk about accepting something — "
                                "as Professor Chen says the first step is to accept your emotions. "
                                "Example: 接受自己的缺点是成长的第一步。"
                            ),
                        },
                        {
                            "targetVocab": "影响",
                            "prompt": (
                                "Use the word 影响 (yǐngxiǎng) to talk about influence or impact — "
                                "as the talk explains that suppressed emotions affect your health. "
                                "Example: 父母的教育方式会影响孩子的一生。"
                            ),
                        },
                        {
                            "targetVocab": "控制",
                            "prompt": (
                                "Use the word 控制 (kòngzhì) to talk about control — "
                                "as Professor Chen distinguishes between controlling emotions and suppressing them. "
                                "Example: 学会控制自己的情绪是一种很重要的能力。"
                            ),
                        },
                        {
                            "targetVocab": "内心",
                            "prompt": (
                                "Use the word 内心 (nèixīn) to talk about one's inner world — "
                                "as the talk encourages listening to the voice inside. "
                                "Example: 虽然他看起来很开心，但内心其实很孤独。"
                            ),
                        },
                        {
                            "targetVocab": "勇气",
                            "prompt": (
                                "Use the word 勇气 (yǒngqì) to talk about courage — "
                                "as Professor Chen says admitting your emotions takes great courage. "
                                "Example: 说出自己的真实感受需要很大的勇气。"
                            ),
                        },
                        {
                            "targetVocab": "害怕",
                            "prompt": (
                                "Use the word 害怕 (hàipà) to talk about fear — "
                                "as the talk explains that fear is a natural warning signal. "
                                "Example: 每个人都会害怕，重要的是不要让害怕控制你。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_2[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Session 3: Group 3 — 愤怒, 悲伤, 理解, 成长, 经历, 力量 ──

    session_3 = {
        "title": "Session 3: The Power of Emotions — 情绪的力量",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Session 3 Introduction",
                "description": "Recap Sessions 1-2 and introduce Session 3 theme",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Welcome to Session 3 — the final learning session before review! "
                        "Over the past two sessions, you've learned 12 vocabulary words: "
                        "情绪 (qíngxù), 负面 (fùmiàn), 感觉 (gǎnjué), 表达 (biǎodá), "
                        "压力 (yālì), 健康 (jiànkāng) in Session 1, and "
                        "接受 (jiēshòu), 影响 (yǐngxiǎng), 控制 (kòngzhì), 内心 (nèixīn), "
                        "勇气 (yǒngqì), 害怕 (hàipà) in Session 2. "
                        "You've understood that Professor Chen wants us to stop suppressing emotions "
                        "and start accepting them. Today, we'll explore the final part of the talk, "
                        "where she explains why every emotion — including anger and sadness — "
                        "carries within it the power to help us grow. "
                        "The last 6 words will help you talk about the deepest experiences "
                        "in life. Let's begin!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 3 Vocabulary",
                "description": "Learn 6 words: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Let's learn our final 6 vocabulary words. These come from the closing section of the talk, "
                        "where Professor Chen delivers her most powerful message: every emotion is a source of strength.\n\n"

                        "The first word is 愤怒 (fènnù). 愤怒 works as both a noun and an adjective, "
                        "meaning 'anger' or 'furious'. This is one of the emotions most commonly labeled as 'bad' "
                        "by society. But Professor Chen explains that 愤怒 (fènnù) serves an important purpose: "
                        "it tells you when someone has crossed your boundaries. For example: "
                        "愤怒告诉你：有人越过了你的底线 — Anger tells you: someone has crossed your line. "
                        "愤 (fèn) means 'indignation' and 怒 (nù) means 'rage'. Together they form an intense emotion. "
                        "Another usage: 他非常愤怒，因为被朋友欺骗了 — He was furious because his friend deceived him. "
                        "You can also say: 愤怒是一种正常的情绪 — Anger is a normal emotion.\n\n"

                        "The second word is 悲伤 (bēishāng). 悲伤 works as both a noun and an adjective, "
                        "meaning 'sadness' or 'sorrowful'. Professor Chen says 悲伤 (bēishāng) tells you "
                        "that you've lost something important — and that very sadness teaches you to cherish things. "
                        "For example: 悲伤告诉你：你失去了重要的东西 — Sadness tells you: you've lost something important. "
                        "悲 (bēi) means 'sorrow' and 伤 (shāng) means 'wound, hurt'. "
                        "Another usage: 失去亲人的悲伤是很难用语言表达的 — "
                        "The sadness of losing a loved one is hard to put into words. "
                        "Or: 她的眼神里充满了悲伤 — Her eyes were filled with sadness.\n\n"

                        "The third word is 理解 (lǐjiě). 理解 is a verb meaning 'to understand' or "
                        "'to comprehend'. This is a crucial word in the talk. Professor Chen emphasizes that "
                        "to truly control your emotions, you need to 理解 (lǐjiě) — understand why you feel "
                        "the way you do. Not suppress, but comprehend. For example: "
                        "理解自己的情绪是控制情绪的第一步 — Understanding your emotions is the first step "
                        "to controlling them. 理 (lǐ) means 'reason, logic' and 解 (jiě) means 'to untangle'. "
                        "When you 理解 (lǐjiě), you're using reason to untangle complexity. "
                        "Another usage: 我理解你的感受 — I understand how you feel. "
                        "Or: 这个问题很难理解 — This problem is hard to understand.\n\n"

                        "The fourth word is 成长 (chéngzhǎng). 成长 works as both a verb and a noun, "
                        "meaning 'to grow up' or 'growth'. Professor Chen concludes that every emotion — "
                        "even the most painful ones — is an opportunity to 成长 (chéngzhǎng). "
                        "When you experience anger, you learn what fairness means. "
                        "When you experience sadness, you learn what it means to cherish. "
                        "For example: 每一种情绪都是成长的力量 — Every emotion is a force for growth. "
                        "成 (chéng) means 'to become' and 长 (zhǎng) means 'to grow'. "
                        "Another usage: 孩子在困难中成长 — Children grow through difficulties. "
                        "Or: 这段经历让我成长了很多 — This experience helped me grow a lot.\n\n"

                        "The fifth word is 经历 (jīnglì). 经历 works as both a verb and a noun, "
                        "meaning 'to experience' or 'experience'. Professor Chen says all emotions are "
                        "part of our life's 经历 (jīnglì). When you 经历 (jīnglì) anger, sadness, fear — "
                        "you're living a full life. For example: "
                        "所有的情绪都是我们生命经历的一部分 — All emotions are part of our life experience. "
                        "经 (jīng) means 'to pass through' and 历 (lì) means 'to undergo'. "
                        "Another usage: 他有很丰富的工作经历 — He has very rich work experience. "
                        "Or: 我从来没有经历过这样的事情 — I've never experienced anything like this.\n\n"

                        "The last word is 力量 (lìliàng). 力量 is a noun meaning 'strength' or 'power'. "
                        "This is the word that closes the talk. Professor Chen says: "
                        "你的情绪就是你的力量 (nǐ de qíngxù jiùshì nǐ de lìliàng) — "
                        "Your emotions are your strength. The final message is clear: "
                        "don't fear your emotions, turn them into 力量 (lìliàng). "
                        "力 (lì) means 'force' and 量 (liàng) means 'quantity, measure'. "
                        "Another usage: 知识就是力量 — Knowledge is power. "
                        "Or: 团结的力量是无穷的 — The power of unity is limitless.\n\n"

                        "Excellent! You've now learned all 18 vocabulary words: "
                        "情绪 (qíngxù), 负面 (fùmiàn), 感觉 (gǎnjué), 表达 (biǎodá), "
                        "压力 (yālì), 健康 (jiànkāng), 接受 (jiēshòu), 影响 (yǐngxiǎng), "
                        "控制 (kòngzhì), 内心 (nèixīn), 勇气 (yǒngqì), 害怕 (hàipà), "
                        "愤怒 (fènnù), 悲伤 (bēishāng), 理解 (lǐjiě), 成长 (chéngzhǎng), "
                        "经历 (jīnglì), 力量 (lìliàng). Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: The Power of Emotions",
                "description": "Learn 6 words: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 3 Vocabulary",
                "description": "Practice speaking 6 words: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 3 Vocabulary",
                "description": "Recognize 6 words: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 3 Vocabulary",
                "description": "Match meanings for 6 words: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 3 Vocabulary",
                "description": "Write 6 words: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Grammar and Usage Tips",
                "description": "How to use Session 3 vocabulary naturally in sentences",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Outstanding! You've completed all 18 vocabulary words. Let's look at how to use "
                        "these last 6 naturally.\n\n"
                        "愤怒 (fènnù) often pairs with 感到 (gǎndào) or 非常 (fēicháng): "
                        "感到愤怒 (gǎndào fènnù — feel angry), 非常愤怒 (fēicháng fènnù — very angry). "
                        "Pattern: 对...感到愤怒 (duì...gǎndào fènnù — angry about...). "
                        "A milder synonym is 生气 (shēngqì).\n\n"
                        "悲伤 (bēishāng) often pairs with 感到 (gǎndào) or 充满 (chōngmǎn): "
                        "感到悲伤 (gǎndào bēishāng — feel sad), "
                        "充满悲伤 (chōngmǎn bēishāng — filled with sadness). "
                        "Pattern: 为...感到悲伤 (wèi...gǎndào bēishāng — sad about...). "
                        "A milder synonym is 难过 (nánguò).\n\n"
                        "理解 (lǐjiě) can take a person or a thing as its object: "
                        "理解你 (lǐjiě nǐ — understand you), "
                        "理解这个问题 (lǐjiě zhège wèntí — understand this problem). "
                        "Negative patterns: 无法理解 (wúfǎ lǐjiě — unable to understand), "
                        "难以理解 (nányǐ lǐjiě — hard to understand). "
                        "A nice pattern: 互相理解 (hùxiāng lǐjiě — understand each other).\n\n"
                        "成长 (chéngzhǎng) often pairs with 在...中 (zài...zhōng): "
                        "在困难中成长 (zài kùnnan zhōng chéngzhǎng — grow through difficulties), "
                        "在经历中成长 (zài jīnglì zhōng chéngzhǎng — grow through experience). "
                        "As a noun: 个人成长 (gèrén chéngzhǎng — personal growth).\n\n"
                        "经历 (jīnglì) as a verb: 经历困难 (jīnglì kùnnan — experience difficulties), "
                        "经历失败 (jīnglì shībài — experience failure). "
                        "As a noun: 人生经历 (rénshēng jīnglì — life experience), "
                        "工作经历 (gōngzuò jīnglì — work experience). "
                        "Pattern: 经历过...才知道... (jīnglìguò...cái zhīdào... — "
                        "only after experiencing...do you know...).\n\n"
                        "力量 (lìliàng) often pairs with 有 (yǒu) or an adjective: "
                        "有力量 (yǒu lìliàng — have strength), "
                        "强大的力量 (qiángdà de lìliàng — great power). "
                        "Useful patterns: 给...力量 (gěi...lìliàng — give...strength), "
                        "力量来自... (lìliàng láizì... — strength comes from...). "
                        "Famous phrase: 知识就是力量 (zhīshi jiùshì lìliàng — knowledge is power)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 3)",
                "description": "愤怒、悲伤、害怕——这些情绪都有它们存在的理由。",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 3)",
                "description": "Practice speaking along with the excerpt about the power of emotions",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Listen: Talk Excerpt (Part 3)",
                "description": "Listen to the passage you just read and follow along.",
                "practiceMinutes": 3,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Write: The Power of Emotions",
                "description": "Write sentences using Session 3 vocabulary",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "愤怒",
                            "prompt": (
                                "Use the word 愤怒 (fènnù) to talk about anger — "
                                "as Professor Chen explains that anger tells you someone has crossed your boundaries. "
                                "Example: 当看到不公平的事情时，我们会感到愤怒。"
                            ),
                        },
                        {
                            "targetVocab": "悲伤",
                            "prompt": (
                                "Use the word 悲伤 (bēishāng) to talk about sadness — "
                                "as the talk explains that sadness teaches us to cherish what we have. "
                                "Example: 悲伤是一种很深的情绪，它让我们学会珍惜。"
                            ),
                        },
                        {
                            "targetVocab": "理解",
                            "prompt": (
                                "Use the word 理解 (lǐjiě) to talk about understanding — "
                                "as Professor Chen emphasizes that understanding emotions is the first step to controlling them. "
                                "Example: 只有理解别人的感受，我们才能建立真正的友谊。"
                            ),
                        },
                        {
                            "targetVocab": "成长",
                            "prompt": (
                                "Use the word 成长 (chéngzhǎng) to talk about growth — "
                                "as the talk concludes that every emotion is an opportunity to grow. "
                                "Example: 每一次失败都是成长的机会，不要害怕犯错。"
                            ),
                        },
                        {
                            "targetVocab": "经历",
                            "prompt": (
                                "Use the word 经历 (jīnglì) to talk about an experience — "
                                "as Professor Chen says all emotions are part of our life experience. "
                                "Example: 这次旅行是我人生中最难忘的经历之一。"
                            ),
                        },
                        {
                            "targetVocab": "力量",
                            "prompt": (
                                "Use the word 力量 (lìliàng) to talk about strength or power — "
                                "as the talk ends with the message: your emotions are your strength. "
                                "Example: 爱是世界上最强大的力量，它可以改变一切。"
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
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Congratulations! You've completed 3 learning sessions and mastered 18 Chinese vocabulary "
                        "words on the theme of emotions and psychology. Let's review them all!\n\n"
                        "In Session 1, you learned: 情绪 (qíngxù — emotions), 负面 (fùmiàn — negative), "
                        "感觉 (gǎnjué — feeling), 表达 (biǎodá — express), 压力 (yālì — pressure), "
                        "健康 (jiànkāng — health). These are the foundational words that help you talk about "
                        "the emotional world inside.\n\n"
                        "In Session 2, you learned: 接受 (jiēshòu — accept), 影响 (yǐngxiǎng — influence), "
                        "控制 (kòngzhì — control), 内心 (nèixīn — inner heart), 勇气 (yǒngqì — courage), "
                        "害怕 (hàipà — afraid). These words help you talk about facing and processing emotions.\n\n"
                        "In Session 3, you learned: 愤怒 (fènnù — anger), 悲伤 (bēishāng — sadness), "
                        "理解 (lǐjiě — understand), 成长 (chéngzhǎng — growth), 经历 (jīnglì — experience), "
                        "力量 (lìliàng — strength). These words help you understand that every emotion has value.\n\n"
                        "Now let's review all 18 words through flashcard activities!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Review All 18 Words",
                "description": "Review 18 words: 情绪, 负面, 感觉, 表达, 压力, 健康, 接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak All 18 Words",
                "description": "Practice speaking 18 words: 情绪, 负面, 感觉, 表达, 压力, 健康, 接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize All Vocabulary",
                "description": "Recognize 18 words: 情绪, 负面, 感觉, 表达, 压力, 健康, 接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 6,
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
                "practiceMinutes": 1,
                "data": {
                    "text": (
                        "Welcome to the final session! Today you'll read the complete talk "
                        "by Professor May Chen from start to finish. You've learned 18 vocabulary words "
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
                "description": "大家好，我是陈永仪。今天我想跟大家聊一个话题：负面情绪真的是坏事吗？",
                "practiceMinutes": 5,
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 3. speakReading — full transcript
            {
                "activityType": "speakReading",
                "title": "Speak: The Complete Talk",
                "description": "Practice speaking along with the complete talk",
                "practiceMinutes": 5,
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 4. readAlong — full transcript
            {
                "activityType": "readAlong",
                "title": "Listen: The Complete Talk",
                "description": "Listen to the complete talk and follow along.",
                "practiceMinutes": 3,
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 5. introAudio — farewell reviewing all 18 words
            {
                "activityType": "introAudio",
                "title": "Farewell and Vocabulary Review",
                "description": "Review all 18 vocabulary words and farewell",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Congratulations on completing the entire course! You've come an incredible way. "
                        "Let's review all 18 vocabulary words one final time.\n\n"

                        "情绪 (qíngxù) — emotions, mood. "
                        "Example: 学会管理自己的情绪是一种智慧 — Learning to manage your emotions is a form of wisdom.\n\n"

                        "负面 (fùmiàn) — negative, the downside. "
                        "Example: 不要只看到事情的负面 — Don't only see the negative side of things.\n\n"

                        "感觉 (gǎnjué) — feeling, to feel. "
                        "Example: 相信你自己的感觉 — Trust your own feelings.\n\n"

                        "表达 (biǎodá) — to express, to convey. "
                        "Example: 音乐是一种美丽的表达方式 — Music is a beautiful form of expression.\n\n"

                        "压力 (yālì) — pressure, stress. "
                        "Example: 适当的压力可以让人进步 — The right amount of pressure can help you improve.\n\n"

                        "健康 (jiànkāng) — health, healthy. "
                        "Example: 快乐是最好的健康秘诀 — Happiness is the best health secret.\n\n"

                        "接受 (jiēshòu) — to accept, to receive. "
                        "Example: 接受不完美，才能找到真正的幸福 — Accept imperfection, and you'll find true happiness.\n\n"

                        "影响 (yǐngxiǎng) — influence, to affect. "
                        "Example: 好朋友会给你正面的影响 — Good friends bring you positive influence.\n\n"

                        "控制 (kòngzhì) — to control, to manage. "
                        "Example: 深呼吸可以帮助你控制情绪 — Deep breathing can help you control your emotions.\n\n"

                        "内心 (nèixīn) — inner heart, one's inner world. "
                        "Example: 跟随你内心的声音 — Follow the voice of your heart.\n\n"

                        "勇气 (yǒngqì) — courage, bravery. "
                        "Example: 做自己需要最大的勇气 — Being yourself takes the greatest courage.\n\n"

                        "害怕 (hàipà) — to be afraid, to fear. "
                        "Example: 害怕是正常的，勇敢是选择 — Fear is normal; bravery is a choice.\n\n"

                        "愤怒 (fènnù) — anger, furious. "
                        "Example: 愤怒的时候，先冷静再说话 — When you're angry, calm down before you speak.\n\n"

                        "悲伤 (bēishāng) — sadness, sorrowful. "
                        "Example: 悲伤过后，阳光总会来 — After sadness, the sunshine always comes.\n\n"

                        "理解 (lǐjiě) — to understand, to comprehend. "
                        "Example: 世界需要更多的理解和包容 — The world needs more understanding and tolerance.\n\n"

                        "成长 (chéngzhǎng) — to grow, growth. "
                        "Example: 每一天都是成长的机会 — Every day is an opportunity to grow.\n\n"

                        "经历 (jīnglì) — to experience, experience. "
                        "Example: 感谢所有的经历，它们让我变得更强 — "
                        "Be grateful for all your experiences; they've made you stronger.\n\n"

                        "力量 (lìliàng) — strength, power. "
                        "Example: 你比你想象的更有力量 — You are stronger than you think.\n\n"

                        "As Professor May Chen said: 你的情绪就是你的力量 (nǐ de qíngxù jiùshì nǐ de lìliàng) — "
                        "Your emotions are your strength. "
                        "You haven't just learned 18 Chinese vocabulary words — you've gained a deeper understanding "
                        "of how to face your own emotions. Remember: don't fear your feelings; "
                        "turn them into your strength. Thank you for learning with us, "
                        "and we wish you health in both body and mind! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Learn Through Podcasts: '沒有負面能量是好事嗎？' — 陳永儀 (Are Negative Emotions Really Bad?)",
        "description": (
            "ARE YOU PRETENDING TO BE STRONG BY BURYING EVERY EMOTION?\n\n"
            "Every time you swallow your tears, every time you hide your anger, every time you say "
            "'I'm fine' while your heart is breaking — you're slowly poisoning yourself. "
            "This isn't a metaphor. Scientific research shows that long-term emotional suppression "
            "destroys your immune system, increases the risk of heart disease, and traps you in "
            "a spiral of stress with no way out.\n\n"
            "Psychology professor May Chen (陳永儀) from TEDxTaipei is about to flip everything "
            "you've ever believed: negative emotions aren't the enemy — they're the most sophisticated "
            "warning system your body possesses. Anger tells you someone has crossed your boundaries. "
            "Sadness teaches you to cherish what matters. Fear protects you from danger.\n\n"
            "When you find the courage to face your inner world instead of running from it, "
            "you don't just become healthier — you truly grow.\n\n"
            "Learn 18 powerful vocabulary words about emotions and psychology through an immersive "
            "multi-sensory experience that upgrades both your thinking and your Chinese at the same time."
        ),
        "preview": {
            "text": (
                "Did you know that every time you suppress an emotion, your body pays the price? "
                "Psychology professor May Chen from TEDxTaipei will completely transform how you see "
                "anger, sadness, and fear. In this course, you'll learn 18 Chinese vocabulary words "
                "at HSK2-HSK3 level about emotions and psychology: "
                "情绪 (qíngxù — emotions), 负面 (fùmiàn — negative), "
                "感觉 (gǎnjué — feeling), 表达 (biǎodá — express), "
                "压力 (yālì — pressure), 健康 (jiànkāng — health), "
                "接受 (jiēshòu — accept), 影响 (yǐngxiǎng — influence), "
                "控制 (kòngzhì — control), 内心 (nèixīn — inner heart), "
                "勇气 (yǒngqì — courage), 害怕 (hàipà — afraid), "
                "愤怒 (fènnù — anger), 悲伤 (bēishāng — sadness), "
                "理解 (lǐjiě — understand), 成长 (chéngzhǎng — growth), "
                "经历 (jīnglì — experience), 力量 (lìliàng — strength). "
                "Across 5 sessions of flashcards, reading, speaking, and writing, "
                "you'll not only master the vocabulary but also gain a deeper understanding "
                "of how Chinese speakers talk about their inner emotional world — "
                "and turn your emotions into your greatest strength."
            ),
        },
        "youtubeUrl": "https://www.youtube.com/watch?v=uiJ4zibW8_M",
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
