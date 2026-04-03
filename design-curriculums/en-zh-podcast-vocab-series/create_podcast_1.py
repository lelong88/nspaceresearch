"""
Create en-zh podcast curriculum #1:
蔣勳 (Chiang Hsun) — "留十八分鐘給自己"
(Give Yourself Eighteen Minutes)

TEDxTaipei 2012, ~25 minutes, about slowing down, art, beauty, and self-reflection.
YouTube: https://www.youtube.com/watch?v=6i7RcP39NB0

18 HSK2-HSK3 vocabulary words in 3 groups of 6.
SAME 18 words and reading passages as vi-zh podcast #1.
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

VOCAB_GROUP_1 = ["时间", "忙碌", "安静", "美", "生活", "感受"]
VOCAB_GROUP_2 = ["慢", "欣赏", "自然", "心灵", "放松", "享受"]
VOCAB_GROUP_3 = ["艺术", "孤独", "思考", "珍惜", "简单", "幸福"]
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



# ── Chinese reading passages (SAME as vi-zh #1, simplified Chinese) ──

READING_1 = (
    "大家好，我是蒋勋。今天我想跟大家聊一个很简单的问题：你有多久没有安静下来了？\n\n"
    "我们每天都很忙碌。早上起来看手机，上班的路上听新闻，到了公司开会、回邮件、"
    "处理各种事情。晚上回到家，又继续看手机、看电视。我们的生活被各种声音和信息填满了，"
    "可是我们有没有留一点时间给自己？\n\n"
    "我常常问我的学生：你今天有没有看过天空？你有没有注意到路边的花开了？"
    "你有没有感受到风吹在脸上的感觉？大部分人摇摇头。他们太忙了，"
    "忙到忘记了生活中最美的东西。\n\n"
    "美不在远方，美就在你身边。一杯热茶的温度，窗外树叶的颜色，"
    "清晨第一缕阳光——这些都是美。可是如果你一直在忙碌，"
    "你就看不见这些美好的东西。你的眼睛在看，但你的心没有在感受。"
)

READING_2 = (
    "我小时候住在台北，那时候的生活很慢。放学以后，我会在河边坐很久，"
    "看水慢慢地流，看天上的云慢慢地变。那种安静的感觉，让我觉得世界很大，"
    "时间很长，什么都不用着急。\n\n"
    "可是现在呢？我们总是在赶时间。吃饭要快，走路要快，连说话都要快。"
    "我们害怕慢下来，因为我们觉得慢就是浪费时间。但是，真的是这样吗？\n\n"
    "欣赏一幅画需要时间。理解一首诗需要时间。感受大自然的美也需要时间。"
    "如果你总是匆匆忙忙，你就错过了生活中最珍贵的东西。\n\n"
    "我认识一个朋友，他每天工作十几个小时。有一天他突然生病了，"
    "医生让他在家休息一个月。他说，那一个月是他最幸福的时光。"
    "因为他终于有时间坐在阳台上，看花开花落，听鸟叫虫鸣。"
    "他说：'我以前从来不知道，原来放松是这么美好的事情。'"
)

READING_3 = (
    "艺术教会我们一件很重要的事：慢下来，用心去看。\n\n"
    "你看过《蒙娜丽莎》吗？很多人去卢浮宫，在画前面拍一张照片就走了。"
    "可是如果你愿意站在那里十分钟，安静地看，你会发现她的微笑在变化。"
    "那不是一个简单的微笑，那是一千种感觉的混合。\n\n"
    "孤独不是坏事。当你一个人安静地坐着，你才能听到自己心灵的声音。"
    "现代人最大的问题就是害怕孤独。我们用社交媒体、用聚会、用各种活动"
    "来填满每一分钟，因为我们不敢面对安静。\n\n"
    "可是，真正的思考需要孤独。真正的创造需要安静。"
    "当你学会享受孤独的时候，你就找到了内心的自由。\n\n"
    "我希望每个人每天都能留十八分钟给自己。不看手机，不想工作，"
    "不跟任何人说话。就安静地坐着，感受呼吸，感受时间的流动。"
    "这十八分钟，也许会成为你一天中最珍惜的时光。\n\n"
    "生活不需要那么复杂。简单，就是幸福。"
)

FULL_TRANSCRIPT = (
    "大家好，我是蒋勋。今天我想跟大家聊一个很简单的问题：你有多久没有安静下来了？\n\n"
    "我们每天都很忙碌。早上起来看手机，上班的路上听新闻，到了公司开会、回邮件、"
    "处理各种事情。晚上回到家，又继续看手机、看电视。我们的生活被各种声音和信息填满了，"
    "可是我们有没有留一点时间给自己？\n\n"
    "我常常问我的学生：你今天有没有看过天空？你有没有注意到路边的花开了？"
    "你有没有感受到风吹在脸上的感觉？大部分人摇摇头。他们太忙了，"
    "忙到忘记了生活中最美的东西。\n\n"
    "美不在远方，美就在你身边。一杯热茶的温度，窗外树叶的颜色，"
    "清晨第一缕阳光——这些都是美。可是如果你一直在忙碌，"
    "你就看不见这些美好的东西。你的眼睛在看，但你的心没有在感受。\n\n"
    "我小时候住在台北，那时候的生活很慢。放学以后，我会在河边坐很久，"
    "看水慢慢地流，看天上的云慢慢地变。那种安静的感觉，让我觉得世界很大，"
    "时间很长，什么都不用着急。\n\n"
    "可是现在呢？我们总是在赶时间。吃饭要快，走路要快，连说话都要快。"
    "我们害怕慢下来，因为我们觉得慢就是浪费时间。但是，真的是这样吗？\n\n"
    "欣赏一幅画需要时间。理解一首诗需要时间。感受大自然的美也需要时间。"
    "如果你总是匆匆忙忙，你就错过了生活中最珍贵的东西。\n\n"
    "我认识一个朋友，他每天工作十几个小时。有一天他突然生病了，"
    "医生让他在家休息一个月。他说，那一个月是他最幸福的时光。"
    "因为他终于有时间坐在阳台上，看花开花落，听鸟叫虫鸣。"
    "他说：'我以前从来不知道，原来放松是这么美好的事情。'\n\n"
    "艺术教会我们一件很重要的事：慢下来，用心去看。\n\n"
    "你看过《蒙娜丽莎》吗？很多人去卢浮宫，在画前面拍一张照片就走了。"
    "可是如果你愿意站在那里十分钟，安静地看，你会发现她的微笑在变化。"
    "那不是一个简单的微笑，那是一千种感觉的混合。\n\n"
    "孤独不是坏事。当你一个人安静地坐着，你才能听到自己心灵的声音。"
    "现代人最大的问题就是害怕孤独。我们用社交媒体、用聚会、用各种活动"
    "来填满每一分钟，因为我们不敢面对安静。\n\n"
    "可是，真正的思考需要孤独。真正的创造需要安静。"
    "当你学会享受孤独的时候，你就找到了内心的自由。\n\n"
    "我希望每个人每天都能留十八分钟给自己。不看手机，不想工作，"
    "不跟任何人说话。就安静地坐着，感受呼吸，感受时间的流动。"
    "这十八分钟，也许会成为你一天中最珍惜的时光。\n\n"
    "生活不需要那么复杂。简单，就是幸福。"
)


def build_content():
    # ── Session 1: Group 1 — 时间, 忙碌, 安静, 美, 生活, 感受 ──

    session_1 = {
        "title": "Session 1: Time and Beauty — 时间与美",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Introduction to the Talk",
                "description": "Introduction to Chiang Hsun's TEDxTaipei talk on the art of slowing down",
                "data": {
                    "text": (
                        "Welcome to the Chinese vocabulary podcast course! "
                        "Today we're diving into a beautiful and deeply moving talk — "
                        "'留十八分鐘給自己' (Give Yourself Eighteen Minutes) by the renowned Taiwanese "
                        "writer and aesthetics scholar Chiang Hsun (蔣勳), delivered at TEDxTaipei 2012. "
                        "Chiang Hsun is one of Taiwan's most beloved writers, celebrated for his work "
                        "on art, beauty, and the philosophy of living. In this talk, he poses a deceptively "
                        "simple question: How long has it been since you truly stopped and listened to yourself? "
                        "Modern life pulls us into a relentless whirlpool of busyness — from morning to night, "
                        "from work to phone screens, we never pause. We've forgotten how to look at the sky, "
                        "notice a flower blooming by the road, or feel the wind on our face. "
                        "Chiang Hsun believes that beauty isn't somewhere far away — it's right beside you, "
                        "waiting for you to stop and notice. In this first session, you'll learn 6 essential "
                        "vocabulary words about time, daily life, and perceiving beauty. Let's begin!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 1 Vocabulary",
                "description": "Learn 6 words: 时间, 忙碌, 安静, 美, 生活, 感受",
                "data": {
                    "text": (
                        "Let's learn our first 6 vocabulary words. Each one is closely tied to the content "
                        "of Chiang Hsun's talk about the art of slowing down and perceiving beauty.\n\n"

                        "The first word is 时间 (shíjiān). 时间 is a noun meaning 'time'. "
                        "This is the word that runs through the entire talk. Chiang Hsun says we always feel "
                        "like we don't have enough 时间 (shíjiān), but the truth is we're wasting it on things "
                        "that don't matter. He urges everyone to set aside 18 minutes each day for themselves. "
                        "For example: 时间是最宝贵的东西，可是我们常常浪费它 — "
                        "Time is the most precious thing, but we often waste it. "
                        "时 (shí) means 'time, hour' and 间 (jiān) means 'space, interval'. "
                        "You can use this word in many ways: 你有时间吗？ — Do you have time? "
                        "Or: 时间过得真快 — Time flies so fast.\n\n"

                        "The second word is 忙碌 (mánglù). 忙碌 is an adjective meaning 'busy' or 'hectic'. "
                        "Chiang Hsun paints a vivid picture of modern life as an endless cycle of 忙碌 (mánglù) — "
                        "from morning to night, we chase work, messages, and meetings, forgetting ourselves entirely. "
                        "For example: 我们每天都很忙碌，忙到忘记了生活中最美的东西 — "
                        "We're so busy every day that we forget the most beautiful things in life. "
                        "忙 (máng) means 'busy' and 碌 (lù) means 'toiling, laboring'. "
                        "Another usage: 最近工作太忙碌了 — Work has been too hectic lately.\n\n"

                        "The third word is 安静 (ānjìng). 安静 is an adjective meaning 'quiet' or 'peaceful'. "
                        "Chiang Hsun believes 安静 (ānjìng) is the prerequisite for perceiving beauty. "
                        "Only when you sit in 安静 (ānjìng) can you hear the voice inside yourself. "
                        "For example: 安静下来，你才能听到自己心灵的声音 — "
                        "Only when you quiet down can you hear the voice of your soul. "
                        "安 (ān) means 'peace, calm' and 静 (jìng) means 'still, quiet'. "
                        "Another usage: 图书馆里很安静 — The library is very quiet. "
                        "Or: 请安静一下 — Please be quiet for a moment.\n\n"

                        "The fourth word is 美 (měi). 美 works as both a noun and an adjective, "
                        "meaning 'beautiful' or 'beauty'. This is the central theme of Chiang Hsun's entire career. "
                        "He says: 美不在远方，美就在你身边 — Beauty isn't far away; beauty is right beside you. "
                        "A cup of hot tea, the morning sunlight, leaves changing color — all of these are 美 (měi). "
                        "For example: 生活中到处都有美，只是我们没有发现 — "
                        "Beauty is everywhere in life; we just haven't noticed it. "
                        "This word is incredibly versatile: 美丽 (měilì — beautiful), "
                        "美好 (měihǎo — wonderful), 美食 (měishí — delicious food).\n\n"

                        "The fifth word is 生活 (shēnghuó). 生活 works as both a noun and a verb, "
                        "meaning 'life' or 'to live'. Chiang Hsun doesn't talk about lofty philosophy — "
                        "he talks about everyday 生活 (shēnghuó). The way you drink tea, the way you walk, "
                        "the way you look at the sky — that is 生活 (shēnghuó). "
                        "For example: 简单的生活才是最幸福的 — A simple life is the happiest life. "
                        "生 (shēng) means 'to be born, to live' and 活 (huó) means 'alive, living'. "
                        "Another usage: 你的生活怎么样？ — How's your life? "
                        "Or: 我喜欢在乡下生活 — I like living in the countryside.\n\n"

                        "The last word for today is 感受 (gǎnshòu). 感受 works as both a noun and a verb, "
                        "meaning 'to feel' or 'feeling, experience'. "
                        "Chiang Hsun emphasizes that we need to learn to 感受 (gǎnshòu) — "
                        "not just see with our eyes, but feel with our hearts. "
                        "For example: 你有没有感受到风吹在脸上的感觉？ — "
                        "Have you felt the wind blowing on your face? "
                        "感 (gǎn) means 'to sense' and 受 (shòu) means 'to receive'. "
                        "Another usage: 我能感受到你的善意 — I can feel your kindness. "
                        "Or: 这首歌给我很深的感受 — This song gives me a very deep feeling.\n\n"

                        "So now you know your first 6 words: "
                        "时间 (shíjiān), 忙碌 (mánglù), 安静 (ānjìng), "
                        "美 (měi), 生活 (shēnghuó), 感受 (gǎnshòu). "
                        "Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Time and Beauty",
                "description": "Learn 6 words: 时间, 忙碌, 安静, 美, 生活, 感受",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 1 Vocabulary",
                "description": "Practice speaking 6 words: 时间, 忙碌, 安静, 美, 生活, 感受",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 1 Vocabulary",
                "description": "Recognize 6 words: 时间, 忙碌, 安静, 美, 生活, 感受",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 1 Vocabulary",
                "description": "Match meanings for 6 words: 时间, 忙碌, 安静, 美, 生活, 感受",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 1 Vocabulary",
                "description": "Write 6 words: 时间, 忙碌, 安静, 美, 生活, 感受",
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
                        "时间 (shíjiān) often pairs with verbs: "
                        "有时间 (yǒu shíjiān — have time), 没有时间 (méiyǒu shíjiān — no time), "
                        "浪费时间 (làngfèi shíjiān — waste time), 节省时间 (jiéshěng shíjiān — save time). "
                        "A useful pattern: 时间 + 过得 + adjective: "
                        "时间过得很快 (shíjiān guòde hěn kuài — time passes quickly).\n\n"
                        "忙碌 (mánglù) usually follows 很 (hěn) or 太 (tài): "
                        "很忙碌 (hěn mánglù — very busy), 太忙碌了 (tài mánglùle — too busy). "
                        "Pattern: 忙碌的 + noun: 忙碌的一天 (mánglù de yītiān — a busy day), "
                        "忙碌的生活 (mánglù de shēnghuó — a hectic life). "
                        "A simpler synonym is just 忙 (máng).\n\n"
                        "安静 (ānjìng) can be an adjective or a verb. "
                        "Adjective: 这里很安静 (zhèlǐ hěn ānjìng — it's very quiet here). "
                        "Command: 安静！(ānjìng! — Be quiet!). "
                        "Patterns: 安静下来 (ānjìng xiàlái — quiet down), "
                        "安静地 + verb: 安静地坐着 (ānjìng de zuòzhe — sit quietly).\n\n"
                        "美 (měi) is very flexible. Standalone: 这里真美 (zhèlǐ zhēn měi — it's really beautiful here). "
                        "Compounds: 美丽 (měilì — beautiful), 美好 (měihǎo — wonderful), "
                        "美食 (měishí — fine food), 美术 (měishù — fine arts). "
                        "Pattern: 美不在...美在... (měi bùzài...měi zài... — beauty isn't in...beauty is in...).\n\n"
                        "生活 (shēnghuó) as a noun: 日常生活 (rìcháng shēnghuó — daily life), "
                        "生活方式 (shēnghuó fāngshì — lifestyle). "
                        "As a verb: 在北京生活 (zài Běijīng shēnghuó — live in Beijing). "
                        "Patterns: 生活中 (shēnghuó zhōng — in life), "
                        "生活质量 (shēnghuó zhìliàng — quality of life).\n\n"
                        "感受 (gǎnshòu) as a verb: "
                        "感受大自然 (gǎnshòu dàzìrán — feel nature), "
                        "感受温暖 (gǎnshòu wēnnuǎn — feel warmth). "
                        "As a noun: 我的感受 (wǒ de gǎnshòu — my feelings), "
                        "深刻的感受 (shēnkè de gǎnshòu — deep feelings). "
                        "Pattern: 感受到 + noun (gǎnshòu dào + noun — to feel/perceive something)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 1)",
                "description": "大家好，我是蒋勋。今天我想跟大家聊一个很简单的问题：你有多久没有安静下来了？",
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 1)",
                "description": "Practice speaking along with the excerpt about time and beauty in life",
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
                "title": "Write: Time and Beauty",
                "description": "Write sentences using Session 1 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "时间",
                            "prompt": (
                                "Use the word 时间 (shíjiān) to talk about time in life — "
                                "as Chiang Hsun urges us to set aside time for ourselves every day. "
                                "Example: 我们应该每天留一点时间给自己，安静地思考。"
                            ),
                        },
                        {
                            "targetVocab": "忙碌",
                            "prompt": (
                                "Use the word 忙碌 (mánglù) to talk about busyness — "
                                "as the talk describes how modern life is so hectic we forget beauty. "
                                "Example: 忙碌的生活让我们忘记了身边最简单的美好。"
                            ),
                        },
                        {
                            "targetVocab": "安静",
                            "prompt": (
                                "Use the word 安静 (ānjìng) to talk about quietness — "
                                "as Chiang Hsun believes only in quiet can you hear your inner voice. "
                                "Example: 在安静的环境中，我们才能真正地思考问题。"
                            ),
                        },
                        {
                            "targetVocab": "美",
                            "prompt": (
                                "Use the word 美 (měi) to talk about beauty in everyday life — "
                                "as the talk emphasizes that beauty is right beside you. "
                                "Example: 美不在远方，一杯热茶、一缕阳光都是美。"
                            ),
                        },
                        {
                            "targetVocab": "生活",
                            "prompt": (
                                "Use the word 生活 (shēnghuó) to talk about daily life — "
                                "as Chiang Hsun says a simple life is the happiest life. "
                                "Example: 我希望过一种简单而美好的生活。"
                            ),
                        },
                        {
                            "targetVocab": "感受",
                            "prompt": (
                                "Use the word 感受 (gǎnshòu) to talk about feeling or perceiving — "
                                "as the talk urges us to feel with our hearts, not just see with our eyes. "
                                "Example: 用心去感受生活中的每一个美好瞬间。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_1[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Session 2: Group 2 — 慢, 欣赏, 自然, 心灵, 放松, 享受 ──

    session_2 = {
        "title": "Session 2: Slowing Down and Savoring — 慢下来，去欣赏",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Session 2 Introduction",
                "description": "Recap Session 1 and introduce Session 2 theme",
                "data": {
                    "text": (
                        "Welcome back to Session 2! In the previous session, we learned 6 important words: "
                        "时间 (shíjiān — time), 忙碌 (mánglù — busy), 安静 (ānjìng — quiet), "
                        "美 (měi — beauty), 生活 (shēnghuó — life), and 感受 (gǎnshòu — to feel). "
                        "Do you remember them? Chiang Hsun asked: how long has it been since you stopped "
                        "to look at the sky? Today we'll go deeper into the next part of the talk, "
                        "where he shares childhood memories by the river, the philosophy of slowing down, "
                        "and how nature heals the soul. You'll learn 6 new words related to relaxation, "
                        "nature, and the inner world. Let's go!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 2 Vocabulary",
                "description": "Learn 6 words: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "data": {
                    "text": (
                        "Let's learn today's 6 new vocabulary words. These come from the middle section "
                        "of the talk, where Chiang Hsun recalls his childhood and his philosophy of slow living.\n\n"

                        "The first word is 慢 (màn). 慢 is an adjective meaning 'slow'. "
                        "This is the most important word in this section. Chiang Hsun recalls that when he was young, "
                        "life was very 慢 (màn) — he would sit by the river for hours, watching the water flow "
                        "and the clouds drift. But now, we're afraid of being 慢 (màn), because we think "
                        "slow means wasting time. For example: "
                        "我们害怕慢下来，因为觉得慢就是浪费时间 — "
                        "We're afraid of slowing down because we think slow means wasting time. "
                        "This word is simple but profound. "
                        "Another usage: 请说慢一点 (qǐng shuō màn yīdiǎn — please speak more slowly). "
                        "Or: 慢慢来，不要着急 (mànmàn lái, bùyào zhāojí — take it slow, don't rush).\n\n"

                        "The second word is 欣赏 (xīnshǎng). 欣赏 is a verb meaning 'to appreciate' "
                        "or 'to savor, to admire'. Chiang Hsun says that to 欣赏 (xīnshǎng) a painting "
                        "takes time — you can't just snap a photo and leave; you have to stand there and look. "
                        "For example: 欣赏一幅画需要时间 — Appreciating a painting takes time. "
                        "欣 (xīn) means 'joyful' and 赏 (shǎng) means 'to admire, to reward'. "
                        "When you 欣赏 (xīnshǎng), you're both admiring and taking joy from beauty. "
                        "Another usage: 我很欣赏你的才华 — I really admire your talent. "
                        "Or: 让我们一起欣赏这美丽的风景 — Let's enjoy this beautiful scenery together.\n\n"

                        "The third word is 自然 (zìrán). 自然 works as both a noun and an adjective, "
                        "meaning 'nature' or 'natural'. Chiang Hsun believes 自然 (zìrán) is the greatest "
                        "teacher of beauty. Watching leaves fall, hearing birds sing, feeling the wind — "
                        "these are all lessons from 自然 (zìrán). "
                        "For example: 大自然是最好的老师 — Nature is the best teacher. "
                        "自 (zì) means 'self' and 然 (rán) means 'so, thus'. "
                        "Another usage: 这里的自然风景很美 — The natural scenery here is beautiful. "
                        "Or: 他说话很自然 — He speaks very naturally.\n\n"

                        "The fourth word is 心灵 (xīnlíng). 心灵 is a noun meaning 'soul' or "
                        "'inner spirit, mind'. Chiang Hsun says that when you sit quietly in silence, "
                        "you can finally hear the voice of your 心灵 (xīnlíng). "
                        "The busyness of life drowns out that voice. "
                        "For example: 安静下来，你才能听到自己心灵的声音 — "
                        "Only when you quiet down can you hear the voice of your soul. "
                        "心 (xīn) means 'heart' and 灵 (líng) means 'spirit, soul'. "
                        "Another usage: 音乐可以净化心灵 — Music can purify the soul. "
                        "Or: 这本书触动了我的心灵 — This book touched my soul.\n\n"

                        "The fifth word is 放松 (fàngsōng). 放松 is a verb meaning 'to relax' "
                        "or 'to loosen up'. Chiang Hsun tells the story of a friend who worked over ten hours "
                        "a day until he fell ill. Only then did he discover that 放松 (fàngsōng) "
                        "was the most wonderful thing in the world. "
                        "For example: 原来放松是这么美好的事情 — "
                        "It turns out relaxing is such a wonderful thing. "
                        "放 (fàng) means 'to release' and 松 (sōng) means 'loose, relaxed'. "
                        "When you 放松 (fàngsōng), you're letting go of all tension. "
                        "Another usage: 周末我喜欢在家放松 — On weekends I like to relax at home.\n\n"

                        "The last word is 享受 (xiǎngshòu). 享受 is a verb meaning 'to enjoy' "
                        "or 'to savor'. Chiang Hsun wants us to learn to 享受 (xiǎngshòu) the small moments "
                        "in life — a quiet afternoon, a cup of coffee, a good book. "
                        "For example: 学会享受生活中的每一个小瞬间 — "
                        "Learn to enjoy every small moment in life. "
                        "享 (xiǎng) means 'to enjoy' and 受 (shòu) means 'to receive'. "
                        "Another usage: 我很享受一个人的时光 — I really enjoy my alone time. "
                        "Or: 享受过程比结果更重要 — Enjoying the process is more important than the result.\n\n"

                        "So now you've learned 6 more words: "
                        "慢 (màn), 欣赏 (xīnshǎng), 自然 (zìrán), "
                        "心灵 (xīnlíng), 放松 (fàngsōng), 享受 (xiǎngshòu). "
                        "Together with the 6 from Session 1, you now have 12 vocabulary words! Let's keep practicing!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Slowing Down and Savoring",
                "description": "Learn 6 words: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 2 Vocabulary",
                "description": "Practice speaking 6 words: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 2 Vocabulary",
                "description": "Recognize 6 words: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 2 Vocabulary",
                "description": "Match meanings for 6 words: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 2 Vocabulary",
                "description": "Write 6 words: 慢, 欣赏, 自然, 心灵, 放松, 享受",
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
                        "慢 (màn) often pairs with 下来 (xiàlái) to mean 'slow down': "
                        "慢下来 (màn xiàlái — slow down). "
                        "Reduplication: 慢慢 (mànmàn — slowly) — 慢慢走 (mànmàn zǒu — walk slowly), "
                        "慢慢来 (mànmàn lái — take your time). "
                        "Comparison: 比...慢 (bǐ...màn — slower than...).\n\n"
                        "欣赏 (xīnshǎng) usually takes a specific object: "
                        "欣赏音乐 (xīnshǎng yīnyuè — appreciate music), "
                        "欣赏风景 (xīnshǎng fēngjǐng — enjoy scenery), "
                        "欣赏艺术 (xīnshǎng yìshù — appreciate art). "
                        "Extended meaning: 欣赏一个人 (xīnshǎng yīgè rén — admire a person).\n\n"
                        "自然 (zìrán) as a noun: 大自然 (dàzìrán — great nature), "
                        "自然界 (zìránjiè — the natural world). "
                        "As an adjective: 很自然 (hěn zìrán — very natural), "
                        "自然而然 (zìrán érrán — naturally, of its own accord). "
                        "Pattern: 回归自然 (huíguī zìrán — return to nature).\n\n"
                        "心灵 (xīnlíng) often pairs with adjectives or nouns: "
                        "心灵美 (xīnlíng měi — beautiful soul), "
                        "心灵深处 (xīnlíng shēnchù — deep in the soul), "
                        "心灵鸡汤 (xīnlíng jītāng — chicken soup for the soul — inspirational writing). "
                        "Pattern: 触动心灵 (chùdòng xīnlíng — touch the soul).\n\n"
                        "放松 (fàngsōng) often pairs with 一下 (yīxià) or stands alone: "
                        "放松一下 (fàngsōng yīxià — relax a bit), "
                        "放松心情 (fàngsōng xīnqíng — relax your mood), "
                        "放松身体 (fàngsōng shēntǐ — relax your body). "
                        "Pattern: 让自己放松 (ràng zìjǐ fàngsōng — let yourself relax).\n\n"
                        "享受 (xiǎngshòu) usually takes a noun or noun phrase: "
                        "享受生活 (xiǎngshòu shēnghuó — enjoy life), "
                        "享受过程 (xiǎngshòu guòchéng — enjoy the process), "
                        "享受孤独 (xiǎngshòu gūdú — enjoy solitude). "
                        "Pattern: 享受...的乐趣 (xiǎngshòu...de lèqù — enjoy the pleasure of...)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 2)",
                "description": "我小时候住在台北，那时候的生活很慢。放学以后，我会在河边坐很久。",
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 2)",
                "description": "Practice speaking along with the excerpt about slowing down and savoring life",
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
                "title": "Write: Slowing Down and Savoring",
                "description": "Write sentences using Session 2 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "慢",
                            "prompt": (
                                "Use the word 慢 (màn) to talk about slowing down — "
                                "as Chiang Hsun says we fear slowness because we think it's wasting time. "
                                "Example: 慢下来不是浪费时间，而是更好地感受生活。"
                            ),
                        },
                        {
                            "targetVocab": "欣赏",
                            "prompt": (
                                "Use the word 欣赏 (xīnshǎng) to talk about appreciating beauty — "
                                "as the talk emphasizes that appreciating art takes time. "
                                "Example: 我喜欢在周末去公园欣赏大自然的美。"
                            ),
                        },
                        {
                            "targetVocab": "自然",
                            "prompt": (
                                "Use the word 自然 (zìrán) to talk about nature or being natural — "
                                "as Chiang Hsun believes nature is the greatest teacher of beauty. "
                                "Example: 回归自然是现代人最需要的一种生活方式。"
                            ),
                        },
                        {
                            "targetVocab": "心灵",
                            "prompt": (
                                "Use the word 心灵 (xīnlíng) to talk about the soul or inner spirit — "
                                "as the talk encourages listening to the voice of your soul. "
                                "Example: 好的音乐可以治愈我们疲惫的心灵。"
                            ),
                        },
                        {
                            "targetVocab": "放松",
                            "prompt": (
                                "Use the word 放松 (fàngsōng) to talk about relaxing — "
                                "as Chiang Hsun's friend discovered how wonderful relaxation truly is. "
                                "Example: 工作再忙也要找时间放松自己，这对健康很重要。"
                            ),
                        },
                        {
                            "targetVocab": "享受",
                            "prompt": (
                                "Use the word 享受 (xiǎngshòu) to talk about enjoying something — "
                                "as the talk urges us to savor the small moments in life. "
                                "Example: 享受一个人安静读书的时光，是一种简单的幸福。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_2[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Session 3: Group 3 — 艺术, 孤独, 思考, 珍惜, 简单, 幸福 ──

    session_3 = {
        "title": "Session 3: Art and Happiness — 艺术与幸福",
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
                        "时间 (shíjiān), 忙碌 (mánglù), 安静 (ānjìng), 美 (měi), "
                        "生活 (shēnghuó), 感受 (gǎnshòu) in Session 1, and "
                        "慢 (màn), 欣赏 (xīnshǎng), 自然 (zìrán), 心灵 (xīnlíng), "
                        "放松 (fàngsōng), 享受 (xiǎngshòu) in Session 2. "
                        "You've understood that Chiang Hsun wants us to stop, slow down, "
                        "and perceive the simple beauty around us. Today, we'll explore the final part "
                        "of the talk, where he discusses art, solitude, and the secret of true happiness. "
                        "The last 6 words will help you talk about the deepest values in life. Let's begin!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 3 Vocabulary",
                "description": "Learn 6 words: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {
                    "text": (
                        "Let's learn our final 6 vocabulary words. These come from the closing section of the talk, "
                        "where Chiang Hsun delivers his most profound message: happiness lies in simplicity.\n\n"

                        "The first word is 艺术 (yìshù). 艺术 is a noun meaning 'art'. "
                        "As an aesthetics scholar, 艺术 (yìshù) is the thread running through Chiang Hsun's "
                        "entire life. He says 艺术 (yìshù) teaches us something vital: slow down and look "
                        "with your heart. When you stand before the Mona Lisa for ten minutes instead of "
                        "snapping a photo and leaving, you'll notice her smile is changing. "
                        "For example: 艺术教会我们慢下来，用心去看 — "
                        "Art teaches us to slow down and look with our hearts. "
                        "艺 (yì) means 'art, skill' and 术 (shù) means 'technique, method'. "
                        "Another usage: 他对艺术很有兴趣 — He's very interested in art. "
                        "Or: 生活本身就是一种艺术 — Life itself is a form of art.\n\n"

                        "The second word is 孤独 (gūdú). 孤独 works as both a noun and an adjective, "
                        "meaning 'loneliness' or 'lonely, solitary'. Chiang Hsun has a very different view "
                        "of 孤独 (gūdú): he believes it's not a bad thing. When you sit alone in silence, "
                        "you can finally hear the voice of your soul. Modern people fear 孤独 (gūdú), "
                        "so they fill every minute with social media, parties, and activities. "
                        "For example: 孤独不是坏事，它让你听到自己心灵的声音 — "
                        "Loneliness isn't a bad thing; it lets you hear the voice of your soul. "
                        "孤 (gū) means 'alone, orphaned' and 独 (dú) means 'solitary, single'. "
                        "Another usage: 他享受孤独的时光 — He enjoys his time alone. "
                        "Or: 创作需要孤独 — Creation requires solitude.\n\n"

                        "The third word is 思考 (sīkǎo). 思考 is a verb meaning 'to think' or 'to reflect'. "
                        "Chiang Hsun emphasizes that real 思考 (sīkǎo) requires quiet and solitude. "
                        "In the noise and busyness, you can't think deeply. "
                        "For example: 真正的思考需要孤独和安静 — "
                        "Real thinking requires solitude and quiet. "
                        "思 (sī) means 'to think' and 考 (kǎo) means 'to examine, to consider'. "
                        "Another usage: 这个问题值得我们认真思考 — "
                        "This problem deserves our serious thought. "
                        "Or: 给我一点时间思考 — Give me a moment to think.\n\n"

                        "The fourth word is 珍惜 (zhēnxī). 珍惜 is a verb meaning 'to cherish' or 'to treasure'. "
                        "Chiang Hsun wants us to 珍惜 (zhēnxī) the simple moments — "
                        "those eighteen quiet minutes each day could become the time you "
                        "珍惜 (zhēnxī) most. For example: "
                        "这十八分钟，也许会成为你一天中最珍惜的时光 — "
                        "These eighteen minutes may become the most cherished time of your day. "
                        "珍 (zhēn) means 'precious' and 惜 (xī) means 'to value, to pity'. "
                        "Another usage: 珍惜眼前的人 — Cherish the people in front of you. "
                        "Or: 我们要珍惜每一天 — We should cherish every day.\n\n"

                        "The fifth word is 简单 (jiǎndān). 简单 is an adjective meaning 'simple' or 'uncomplicated'. "
                        "The closing line of Chiang Hsun's talk is short but carries immense weight: "
                        "生活不需要那么复杂。简单，就是幸福 — Life doesn't need to be so complicated. "
                        "Simplicity is happiness. "
                        "简 (jiǎn) means 'simple, brief' and 单 (dān) means 'single, alone'. "
                        "Another usage: 这道菜做法很简单 — This dish is very simple to make. "
                        "Or: 简单的生活最幸福 — A simple life is the happiest.\n\n"

                        "The last word is 幸福 (xìngfú). 幸福 works as both a noun and an adjective, "
                        "meaning 'happiness' or 'happy, blessed'. This is the word that closes the talk "
                        "and carries its core message. Chiang Hsun believes 幸福 (xìngfú) doesn't come "
                        "from money or success, but from the ability to perceive beauty in the simplest things. "
                        "For example: 幸福不是拥有很多，而是感受很多 — "
                        "Happiness isn't about having a lot; it's about feeling a lot. "
                        "幸 (xìng) means 'fortunate' and 福 (fú) means 'blessing, fortune'. "
                        "Another usage: 我觉得自己很幸福 — I feel very happy. "
                        "Or: 幸福就在身边 — Happiness is right beside you.\n\n"

                        "Excellent! You've now learned all 18 vocabulary words: "
                        "时间 (shíjiān), 忙碌 (mánglù), 安静 (ānjìng), 美 (měi), "
                        "生活 (shēnghuó), 感受 (gǎnshòu), 慢 (màn), 欣赏 (xīnshǎng), "
                        "自然 (zìrán), 心灵 (xīnlíng), 放松 (fàngsōng), 享受 (xiǎngshòu), "
                        "艺术 (yìshù), 孤独 (gūdú), 思考 (sīkǎo), 珍惜 (zhēnxī), "
                        "简单 (jiǎndān), 幸福 (xìngfú). Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Art and Happiness",
                "description": "Learn 6 words: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 3 Vocabulary",
                "description": "Practice speaking 6 words: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 3 Vocabulary",
                "description": "Recognize 6 words: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 3 Vocabulary",
                "description": "Match meanings for 6 words: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 3 Vocabulary",
                "description": "Write 6 words: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
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
                        "艺术 (yìshù) often pairs with other nouns: "
                        "艺术家 (yìshùjiā — artist), 艺术品 (yìshùpǐn — artwork), "
                        "艺术节 (yìshùjié — art festival). "
                        "Pattern: ...是一种艺术 (...shì yīzhǒng yìshù — ...is a form of art). "
                        "Example: 做饭也是一种艺术 — Cooking is also a form of art.\n\n"
                        "孤独 (gūdú) often pairs with 感到 (gǎndào) or 享受 (xiǎngshòu): "
                        "感到孤独 (gǎndào gūdú — feel lonely), "
                        "享受孤独 (xiǎngshòu gūdú — enjoy solitude). "
                        "Pattern: 孤独的 + noun: 孤独的夜晚 (gūdú de yèwǎn — a lonely night), "
                        "孤独的旅行 (gūdú de lǚxíng — a solo journey).\n\n"
                        "思考 (sīkǎo) often takes a direct object or pairs with 关于 (guānyú): "
                        "思考人生 (sīkǎo rénshēng — think about life), "
                        "思考问题 (sīkǎo wèntí — think about a problem). "
                        "Patterns: 独立思考 (dúlì sīkǎo — think independently), "
                        "深入思考 (shēnrù sīkǎo — think deeply).\n\n"
                        "珍惜 (zhēnxī) usually takes abstract nouns: "
                        "珍惜时间 (zhēnxī shíjiān — cherish time), "
                        "珍惜友谊 (zhēnxī yǒuyì — cherish friendship), "
                        "珍惜机会 (zhēnxī jīhuì — cherish opportunities). "
                        "Patterns: 要珍惜... (yào zhēnxī... — must cherish...), "
                        "学会珍惜 (xuéhuì zhēnxī — learn to cherish).\n\n"
                        "简单 (jiǎndān) usually comes before a noun: "
                        "简单的生活 (jiǎndān de shēnghuó — a simple life), "
                        "简单的道理 (jiǎndān de dàolǐ — a simple truth). "
                        "Patterns: 很简单 (hěn jiǎndān — very simple), "
                        "简简单单 (jiǎnjiǎndāndān — plain and simple — emphatic reduplication).\n\n"
                        "幸福 (xìngfú) as an adjective: "
                        "很幸福 (hěn xìngfú — very happy), "
                        "幸福的家庭 (xìngfú de jiātíng — a happy family). "
                        "As a noun: 追求幸福 (zhuīqiú xìngfú — pursue happiness), "
                        "幸福感 (xìngfúgǎn — sense of happiness). "
                        "Pattern: 幸福就是... (xìngfú jiùshì... — happiness is...)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 3)",
                "description": "艺术教会我们一件很重要的事：慢下来，用心去看。",
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 3)",
                "description": "Practice speaking along with the excerpt about art, solitude, and happiness",
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
                "title": "Write: Art and Happiness",
                "description": "Write sentences using Session 3 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "艺术",
                            "prompt": (
                                "Use the word 艺术 (yìshù) to talk about art — "
                                "as Chiang Hsun says art teaches us to slow down and look with our hearts. "
                                "Example: 艺术不只是画画和唱歌，生活本身就是最好的艺术。"
                            ),
                        },
                        {
                            "targetVocab": "孤独",
                            "prompt": (
                                "Use the word 孤独 (gūdú) to talk about solitude — "
                                "as the talk explains that solitude helps you hear the voice of your soul. "
                                "Example: 学会享受孤独的人，才能找到真正的自由。"
                            ),
                        },
                        {
                            "targetVocab": "思考",
                            "prompt": (
                                "Use the word 思考 (sīkǎo) to talk about thinking or reflecting — "
                                "as Chiang Hsun emphasizes that real thinking requires quiet. "
                                "Example: 在安静的环境中思考问题，往往能找到更好的答案。"
                            ),
                        },
                        {
                            "targetVocab": "珍惜",
                            "prompt": (
                                "Use the word 珍惜 (zhēnxī) to talk about cherishing something — "
                                "as the talk urges us to treasure those eighteen quiet minutes each day. "
                                "Example: 珍惜和家人在一起的每一刻，因为时间不会等人。"
                            ),
                        },
                        {
                            "targetVocab": "简单",
                            "prompt": (
                                "Use the word 简单 (jiǎndān) to talk about simplicity — "
                                "as Chiang Hsun concludes that life doesn't need to be complicated. "
                                "Example: 有时候，最简单的生活方式反而是最幸福的。"
                            ),
                        },
                        {
                            "targetVocab": "幸福",
                            "prompt": (
                                "Use the word 幸福 (xìngfú) to talk about happiness — "
                                "as the talk ends with the message: simplicity is happiness. "
                                "Example: 幸福不是拥有很多东西，而是能感受到生活中的美好。"
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
                        "words on the theme of slowing down, art, and happiness. Let's review them all!\n\n"
                        "In Session 1, you learned: 时间 (shíjiān — time), 忙碌 (mánglù — busy), "
                        "安静 (ānjìng — quiet), 美 (měi — beauty), 生活 (shēnghuó — life), "
                        "感受 (gǎnshòu — to feel). These are the foundational words that help you talk about "
                        "the rhythm of daily life and perceiving beauty.\n\n"
                        "In Session 2, you learned: 慢 (màn — slow), 欣赏 (xīnshǎng — appreciate), "
                        "自然 (zìrán — nature), 心灵 (xīnlíng — soul), 放松 (fàngsōng — relax), "
                        "享受 (xiǎngshòu — enjoy). These words help you talk about the art of slow living "
                        "and savoring life.\n\n"
                        "In Session 3, you learned: 艺术 (yìshù — art), 孤独 (gūdú — solitude), "
                        "思考 (sīkǎo — think), 珍惜 (zhēnxī — cherish), 简单 (jiǎndān — simple), "
                        "幸福 (xìngfú — happiness). These words help you understand that happiness "
                        "lies in simplicity.\n\n"
                        "Now let's review all 18 words through flashcard activities!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Review All 18 Words",
                "description": "Review 18 words: 时间, 忙碌, 安静, 美, 生活, 感受, 慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak All 18 Words",
                "description": "Practice speaking 18 words: 时间, 忙碌, 安静, 美, 生活, 感受, 慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize All Vocabulary",
                "description": "Recognize 18 words: 时间, 忙碌, 安静, 美, 生活, 感受, 慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
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
                        "by Chiang Hsun from start to finish. You've learned 18 vocabulary words "
                        "across 3 sessions and reviewed them in Session 4. Now it's time to put it all together. "
                        "Read slowly — just as the spirit of the talk suggests — pay attention to the words "
                        "you've learned, and notice how they connect with each other in real context. "
                        "Enjoy the reading!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. reading — full transcript
            {
                "activityType": "reading",
                "title": "Read: The Complete Talk",
                "description": "大家好，我是蒋勋。今天我想跟大家聊一个很简单的问题：你有多久没有安静下来了？",
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
                        "Congratulations on completing the entire course! You've come an incredible way "
                        "with Chiang Hsun and his philosophy of slow living. "
                        "Let's review all 18 vocabulary words one final time.\n\n"

                        "时间 (shíjiān) — time. "
                        "Example: 留一点时间给自己，这是最好的礼物 — "
                        "Set aside a little time for yourself; it's the best gift.\n\n"

                        "忙碌 (mánglù) — busy, hectic. "
                        "Example: 忙碌不是成功的标志，有时候它是迷失的开始 — "
                        "Busyness isn't a sign of success; sometimes it's the beginning of being lost.\n\n"

                        "安静 (ānjìng) — quiet, peaceful. "
                        "Example: 在安静中，你会发现世界比你想象的更美 — "
                        "In quiet, you'll discover the world is more beautiful than you imagined.\n\n"

                        "美 (měi) — beautiful, beauty. "
                        "Example: 美就在你身边，只要你愿意停下来看 — "
                        "Beauty is right beside you, if only you're willing to stop and look.\n\n"

                        "生活 (shēnghuó) — life, to live. "
                        "Example: 好好生活，就是对自己最大的尊重 — "
                        "Living well is the greatest respect you can show yourself.\n\n"

                        "感受 (gǎnshòu) — to feel, feeling. "
                        "Example: 闭上眼睛，感受阳光的温暖 — "
                        "Close your eyes and feel the warmth of the sunlight.\n\n"

                        "慢 (màn) — slow. "
                        "Example: 慢一点，你会看到更多的风景 — "
                        "Slow down a little, and you'll see more of the scenery.\n\n"

                        "欣赏 (xīnshǎng) — to appreciate, to savor. "
                        "Example: 学会欣赏平凡中的美好 — "
                        "Learn to appreciate the beauty in the ordinary.\n\n"

                        "自然 (zìrán) — nature, natural. "
                        "Example: 走进自然，让心灵得到休息 — "
                        "Step into nature and let your soul rest.\n\n"

                        "心灵 (xīnlíng) — soul, inner spirit. "
                        "Example: 一本好书可以丰富你的心灵 — "
                        "A good book can enrich your soul.\n\n"

                        "放松 (fàngsōng) — to relax. "
                        "Example: 放松不是懒惰，而是为了走更远的路 — "
                        "Relaxing isn't laziness; it's so you can go further.\n\n"

                        "享受 (xiǎngshòu) — to enjoy, to savor. "
                        "Example: 享受当下，不要总是担心未来 — "
                        "Enjoy the present; don't always worry about the future.\n\n"

                        "艺术 (yìshù) — art. "
                        "Example: 用艺术的眼光看世界，一切都变得不同 — "
                        "Look at the world through the eyes of art, and everything becomes different.\n\n"

                        "孤独 (gūdú) — solitude, lonely. "
                        "Example: 孤独是一种力量，它让你更了解自己 — "
                        "Solitude is a kind of strength; it helps you understand yourself better.\n\n"

                        "思考 (sīkǎo) — to think, to reflect. "
                        "Example: 每天花十分钟安静地思考，你会变得更清醒 — "
                        "Spend ten minutes thinking quietly each day, and you'll become more clear-headed.\n\n"

                        "珍惜 (zhēnxī) — to cherish, to treasure. "
                        "Example: 珍惜现在拥有的一切，不要等失去才后悔 — "
                        "Cherish everything you have now; don't wait until it's gone to feel regret.\n\n"

                        "简单 (jiǎndān) — simple. "
                        "Example: 把生活变简单，你会发现幸福其实很近 — "
                        "Simplify your life, and you'll find happiness is actually very close.\n\n"

                        "幸福 (xìngfú) — happiness, happy. "
                        "Example: 幸福不在远方，它就在每一个用心生活的瞬间 — "
                        "Happiness isn't far away; it's in every moment you live with your heart.\n\n"

                        "As Chiang Hsun said: 生活不需要那么复杂。简单，就是幸福 "
                        "(shēnghuó bù xūyào nàme fùzá. jiǎndān, jiùshì xìngfú) — "
                        "Life doesn't need to be so complicated. Simplicity is happiness. "
                        "You haven't just learned 18 Chinese vocabulary words — you've gained a deeper "
                        "understanding of the art of slow living and perceiving beauty. "
                        "Remember: give yourself eighteen minutes every day. "
                        "Thank you for learning with us, and may you always find beauty "
                        "in the simplest things! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Learn Through Podcasts: '留十八分鐘給自己' — 蔣勳 (Give Yourself Eighteen Minutes)",
        "description": (
            "ARE YOU RUNNING ALL DAY LONG AND FORGETTING WHO YOU ARE?\n\n"
            "You wake up and grab your phone. You commute while scrolling through news. "
            "At the office it's meetings, emails, deadlines. At night you collapse on the couch "
            "and scroll social media until you fall asleep. Day after day. "
            "You're so busy you can't remember the last time you looked at the sky. "
            "So busy you didn't notice the flowers blooming by the road.\n\n"
            "Renowned Taiwanese writer and aesthetics scholar Chiang Hsun (蔣勳) from TEDxTaipei "
            "will shake you awake with a question so simple it hurts: How long has it been since "
            "you truly stopped? He believes beauty isn't somewhere far away — it's in the warmth "
            "of your morning tea, in the sunlight streaming through your window, in the sound "
            "of wind rustling through leaves. But if you keep running, you'll be blind to all of it.\n\n"
            "When you dare to slow down, dare to sit quietly for eighteen minutes each day "
            "and listen to your own soul — you don't just find peace. You touch real happiness.\n\n"
            "Learn 18 powerful vocabulary words about life, art, and happiness through an immersive "
            "multi-sensory experience that upgrades both your thinking and your Chinese at the same time."
        ),
        "preview": {
            "text": (
                "Did you know that busyness is stealing your ability to feel happiness? "
                "Writer Chiang Hsun from TEDxTaipei will transform how you see time, beauty, and life. "
                "In this course, you'll learn 18 Chinese vocabulary words at HSK2-HSK3 level "
                "about slow living and art: "
                "时间 (shíjiān — time), 忙碌 (mánglù — busy), "
                "安静 (ānjìng — quiet), 美 (měi — beauty), "
                "生活 (shēnghuó — life), 感受 (gǎnshòu — to feel), "
                "慢 (màn — slow), 欣赏 (xīnshǎng — appreciate), "
                "自然 (zìrán — nature), 心灵 (xīnlíng — soul), "
                "放松 (fàngsōng — relax), 享受 (xiǎngshòu — enjoy), "
                "艺术 (yìshù — art), 孤独 (gūdú — solitude), "
                "思考 (sīkǎo — think), 珍惜 (zhēnxī — cherish), "
                "简单 (jiǎndān — simple), 幸福 (xìngfú — happiness). "
                "Across 5 sessions of flashcards, reading, speaking, and writing, "
                "you'll not only master the vocabulary but also discover the philosophy of slow living "
                "from one of Taiwan's most beloved writers — and find happiness in the simplest things."
            ),
        },
        "youtubeUrl": "https://www.youtube.com/watch?v=6i7RcP39NB0",
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
