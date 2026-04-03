"""
Create en-zh podcast curriculum #2:
曾之喬 (Joanne Tseng) — "不要太努力"
(Don't Work Too Hard)

TEDxTaipeiFuhsingPrivateSchool, ~21 minutes, about self-acceptance, career pressure, and balance.
YouTube: https://www.youtube.com/watch?v=t7ZI9c6Ze7E

18 HSK2-HSK3 vocabulary words in 3 groups of 6.
SAME 18 words and reading passages as vi-zh podcast #2.
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

VOCAB_GROUP_1 = ["努力", "工作", "压力", "成功", "梦想", "坚持"]
VOCAB_GROUP_2 = ["失败", "休息", "完美", "自信", "改变", "勇敢"]
VOCAB_GROUP_3 = ["选择", "放弃", "快乐", "真实", "平衡", "价值"]
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



# ── Chinese reading passages (SAME as vi-zh #2, simplified Chinese) ──

READING_1 = (
    "大家好，我是曾之乔。今天我想跟大家分享一个我花了很多年才明白的道理："
    "不要太努力。\n\n"
    "听起来很奇怪，对吧？从小到大，所有人都告诉我们要努力，要坚持，"
    "要拼命工作才能成功。我也是这样相信的。十五岁的时候，我进入了演艺圈。"
    "那时候我觉得，只要我够努力，只要我不停地工作，我就一定能实现我的梦想。\n\n"
    "所以我拼命地工作。每天只睡四五个小时，一个接一个地接工作。"
    "别人休息的时候，我在练习。别人放假的时候，我在拍戏。"
    "我告诉自己：你不能停下来，停下来就意味着失败。\n\n"
    "可是，你知道结果是什么吗？我的身体越来越差，压力越来越大。"
    "我开始失眠，开始焦虑，开始怀疑自己。我那么努力，为什么还是觉得不够好？"
    "为什么成功的感觉总是那么短暂？为什么我越努力，越不快乐？"
)

READING_2 = (
    "后来我才慢慢明白：问题不是我不够努力，而是我太努力了。\n\n"
    "我一直在追求一个完美的自己——完美的演员、完美的歌手、完美的公众人物。"
    "可是这个世界上根本没有完美的人。当你把所有的时间和精力都用来追求完美的时候，"
    "你就失去了做真实自己的自由。\n\n"
    "我记得有一次，我在拍一部电视剧。导演跟我说：'之乔，你不要那么用力。"
    "你越放松，表演越自然。'那一刻我突然明白了——不只是表演，"
    "人生也是一样的。当你太用力的时候，反而做不好。\n\n"
    "于是我开始学习改变。我学会了给自己选择的权利——选择休息，"
    "选择说'不'，选择不去做那些让我不快乐的事情。"
    "我开始重新找回自信，不是因为我做了多少工作，"
    "而是因为我终于敢做真实的自己。\n\n"
    "失败并不可怕。可怕的是你因为害怕失败，而不敢停下来思考："
    "我真正想要的是什么？"
)

READING_3 = (
    "现在的我，学会了一件很重要的事情：平衡。\n\n"
    "工作很重要，但休息也很重要。努力很重要，但快乐也很重要。"
    "成功很重要，但做真实的自己更重要。\n\n"
    "我不再追求完美，因为完美是一个永远到不了的目标。"
    "我开始追求真实——真实地面对自己的感受，真实地表达自己的想法，"
    "真实地过自己想要的生活。\n\n"
    "很多人问我：'你不害怕吗？不害怕别人怎么看你？'"
    "说实话，我当然害怕。但是我学会了勇敢。勇敢不是不害怕，"
    "而是即使害怕，也选择做自己认为对的事情。\n\n"
    "所以，我想对每一个正在拼命努力的你说：偶尔停下来，没关系的。"
    "给自己一点休息的时间，给自己一点自由的空间。"
    "不要让工作和压力控制你的生活。\n\n"
    "找到你自己的平衡，找到让你真正快乐的事情。"
    "当你不再那么努力地追求成功的时候，你会发现——"
    "成功反而会自己找上门来。因为一个快乐的、真实的你，"
    "才是最有价值的你。\n\n"
    "记住：不要太努力。做真实的自己，就已经足够好了。谢谢大家。"
)

FULL_TRANSCRIPT = (
    "大家好，我是曾之乔。今天我想跟大家分享一个我花了很多年才明白的道理："
    "不要太努力。\n\n"
    "听起来很奇怪，对吧？从小到大，所有人都告诉我们要努力，要坚持，"
    "要拼命工作才能成功。我也是这样相信的。十五岁的时候，我进入了演艺圈。"
    "那时候我觉得，只要我够努力，只要我不停地工作，我就一定能实现我的梦想。\n\n"
    "所以我拼命地工作。每天只睡四五个小时，一个接一个地接工作。"
    "别人休息的时候，我在练习。别人放假的时候，我在拍戏。"
    "我告诉自己：你不能停下来，停下来就意味着失败。\n\n"
    "可是，你知道结果是什么吗？我的身体越来越差，压力越来越大。"
    "我开始失眠，开始焦虑，开始怀疑自己。我那么努力，为什么还是觉得不够好？"
    "为什么成功的感觉总是那么短暂？为什么我越努力，越不快乐？\n\n"
    "后来我才慢慢明白：问题不是我不够努力，而是我太努力了。\n\n"
    "我一直在追求一个完美的自己——完美的演员、完美的歌手、完美的公众人物。"
    "可是这个世界上根本没有完美的人。当你把所有的时间和精力都用来追求完美的时候，"
    "你就失去了做真实自己的自由。\n\n"
    "我记得有一次，我在拍一部电视剧。导演跟我说：'之乔，你不要那么用力。"
    "你越放松，表演越自然。'那一刻我突然明白了——不只是表演，"
    "人生也是一样的。当你太用力的时候，反而做不好。\n\n"
    "于是我开始学习改变。我学会了给自己选择的权利——选择休息，"
    "选择说'不'，选择不去做那些让我不快乐的事情。"
    "我开始重新找回自信，不是因为我做了多少工作，"
    "而是因为我终于敢做真实的自己。\n\n"
    "失败并不可怕。可怕的是你因为害怕失败，而不敢停下来思考："
    "我真正想要的是什么？\n\n"
    "现在的我，学会了一件很重要的事情：平衡。\n\n"
    "工作很重要，但休息也很重要。努力很重要，但快乐也很重要。"
    "成功很重要，但做真实的自己更重要。\n\n"
    "我不再追求完美，因为完美是一个永远到不了的目标。"
    "我开始追求真实——真实地面对自己的感受，真实地表达自己的想法，"
    "真实地过自己想要的生活。\n\n"
    "很多人问我：'你不害怕吗？不害怕别人怎么看你？'"
    "说实话，我当然害怕。但是我学会了勇敢。勇敢不是不害怕，"
    "而是即使害怕，也选择做自己认为对的事情。\n\n"
    "所以，我想对每一个正在拼命努力的你说：偶尔停下来，没关系的。"
    "给自己一点休息的时间，给自己一点自由的空间。"
    "不要让工作和压力控制你的生活。\n\n"
    "找到你自己的平衡，找到让你真正快乐的事情。"
    "当你不再那么努力地追求成功的时候，你会发现——"
    "成功反而会自己找上门来。因为一个快乐的、真实的你，"
    "才是最有价值的你。\n\n"
    "记住：不要太努力。做真实的自己，就已经足够好了。谢谢大家。"
)


def build_content():
    # ── Session 1: Group 1 — 努力, 工作, 压力, 成功, 梦想, 坚持 ──

    session_1 = {
        "title": "Session 1: Effort and Dreams — 努力与梦想",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Introduction to the Talk",
                "description": "Introduction to Joanne Tseng's TEDx talk on not working too hard",
                "data": {
                    "text": (
                        "Welcome to the Chinese vocabulary podcast course! "
                        "Today we're diving into a deeply personal and inspiring talk from "
                        "TEDxTaipeiFuhsingPrivateSchool — '不要太努力' (Don't Work Too Hard) "
                        "by Taiwanese actress and singer Joanne Tseng (曾之喬). "
                        "Joanne entered the entertainment industry at just 15 years old, "
                        "and for years she believed that if she just worked hard enough — "
                        "sleeping only four or five hours a night, never turning down a job — "
                        "success would follow. But the reality was far more brutal: "
                        "the harder she pushed, the more exhausted, anxious, and unhappy she became. "
                        "Then one day, a director told her something that changed everything: "
                        "'Don't try so hard. The more relaxed you are, the more natural your performance.' "
                        "That single sentence transformed not just her acting, but her entire approach to life. "
                        "In this first session, you'll learn 6 essential vocabulary words "
                        "related to effort, work, and ambition. Each word appears throughout the talk "
                        "and will help you understand how Chinese speakers discuss "
                        "career, dreams, and the pressure to succeed. Let's get started!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 1 Vocabulary",
                "description": "Learn 6 words: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "data": {
                    "text": (
                        "Let's learn our first 6 vocabulary words. Each one is closely tied to the content "
                        "of Joanne Tseng's talk about her career journey and life lessons.\n\n"

                        "The first word is 努力 (nǔlì). 努力 works as both a verb and an adjective, "
                        "meaning 'to work hard' or 'hardworking'. This is the central word of the entire talk. "
                        "Joanne says she spent years being 努力 (nǔlì) — working nonstop, sacrificing sleep, "
                        "sacrificing health — but the results weren't what she expected. For example: "
                        "我一直很努力地工作，但还是觉得不够好 — I've always worked very hard, "
                        "but I still feel it's not good enough. "
                        "努 (nǔ) means 'to exert' and 力 (lì) means 'strength'. "
                        "When you 努力 (nǔlì), you're pouring all your energy into something. "
                        "Another usage: 只要努力，就一定会有收获 — As long as you work hard, "
                        "you'll definitely see results.\n\n"

                        "The second word is 工作 (gōngzuò). 工作 works as both a noun and a verb, "
                        "meaning 'work' or 'to work'. Joanne describes how she kept taking on 工作 (gōngzuò) "
                        "after 工作 (gōngzuò), never daring to turn down any opportunity for fear of being forgotten. "
                        "For example: 她每天工作十几个小时，完全没有休息的时间 — She works over ten hours "
                        "every day with absolutely no time to rest. "
                        "工 (gōng) means 'labor' and 作 (zuò) means 'to do'. "
                        "This word is extremely common in daily life: "
                        "找工作 (zhǎo gōngzuò — look for a job), 工作经验 (gōngzuò jīngyàn — work experience), "
                        "工作压力 (gōngzuò yālì — work pressure).\n\n"

                        "The third word is 压力 (yālì). 压力 is a noun meaning 'pressure' or 'stress'. "
                        "In the talk, Joanne describes 压力 (yālì) like a snowball — "
                        "the more it rolls, the bigger it gets, until you can't bear it anymore. "
                        "For example: 工作压力太大了，我需要好好休息一下 — "
                        "The work pressure is too much, I need a good rest. "
                        "压 (yā) means 'to press down' and 力 (lì) means 'force'. "
                        "Common patterns: 有压力 (yǒu yālì — have pressure), "
                        "减轻压力 (jiǎnqīng yālì — relieve pressure), "
                        "压力很大 (yālì hěn dà — a lot of pressure).\n\n"

                        "The fourth word is 成功 (chénggōng). 成功 works as both a noun and a verb, "
                        "meaning 'success' or 'to succeed'. Joanne asks a profound question: "
                        "what is real success? Is it working more, earning more, becoming more famous? "
                        "Or is success being able to live as your true self? "
                        "For example: 成功不只是赚很多钱，更重要的是过自己想要的生活 — "
                        "Success isn't just about making a lot of money; what matters more is living the life you want. "
                        "成 (chéng) means 'to become' and 功 (gōng) means 'achievement'. "
                        "Common usage: 祝你成功 (zhù nǐ chénggōng — wishing you success), "
                        "成功的秘诀 (chénggōng de mìjué — the secret to success).\n\n"

                        "The fifth word is 梦想 (mèngxiǎng). 梦想 works as both a noun and a verb, "
                        "meaning 'dream' or 'to dream of'. When Joanne first entered the industry, "
                        "she had so many 梦想 (mèngxiǎng) — to become a great actress, a famous singer, "
                        "to be loved by everyone. But she realized that chasing 梦想 (mèngxiǎng) "
                        "while forgetting yourself isn't worth it. "
                        "For example: 每个人都有自己的梦想，但不要为了梦想而失去自己 — "
                        "Everyone has their own dreams, but don't lose yourself chasing them. "
                        "梦 (mèng) means 'dream' and 想 (xiǎng) means 'to think, to wish'. "
                        "Common usage: 实现梦想 (shíxiàn mèngxiǎng — realize a dream), "
                        "追求梦想 (zhuīqiú mèngxiǎng — pursue a dream).\n\n"

                        "The last word for today is 坚持 (jiānchí). 坚持 is a verb meaning "
                        "'to persist' or 'to persevere'. Joanne once believed 坚持 (jiānchí) was "
                        "the most important virtue — never give up, never stop. "
                        "But she learned that sometimes stopping isn't giving up; "
                        "it's finding the right direction. "
                        "For example: 坚持是好事，但也要知道什么时候该停下来 — "
                        "Perseverance is good, but you also need to know when to stop. "
                        "坚 (jiān) means 'firm' and 持 (chí) means 'to hold'. "
                        "Common usage: 坚持到底 (jiānchí dàodǐ — persevere to the end), "
                        "坚持自己的想法 (jiānchí zìjǐ de xiǎngfǎ — stick to your own ideas).\n\n"

                        "So now you know your first 6 words: "
                        "努力 (nǔlì), 工作 (gōngzuò), 压力 (yālì), "
                        "成功 (chénggōng), 梦想 (mèngxiǎng), 坚持 (jiānchí). "
                        "Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Effort and Dreams",
                "description": "Learn 6 words: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 1 Vocabulary",
                "description": "Practice speaking 6 words: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 1 Vocabulary",
                "description": "Recognize 6 words: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 1 Vocabulary",
                "description": "Match meanings for 6 words: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 1 Vocabulary",
                "description": "Write 6 words: 努力, 工作, 压力, 成功, 梦想, 坚持",
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
                        "努力 (nǔlì) often pairs with 地 (de) when modifying a verb: "
                        "努力地学习 (nǔlì de xuéxí — study hard), "
                        "努力地工作 (nǔlì de gōngzuò — work hard). "
                        "As an adjective: 他是一个很努力的人 (tā shì yīgè hěn nǔlì de rén — "
                        "He's a very hardworking person). Pattern: 努力 + verb, or 很努力.\n\n"
                        "工作 (gōngzuò) is very flexible. As a noun: "
                        "我的工作很忙 (wǒ de gōngzuò hěn máng — My work is very busy). "
                        "As a verb: 他在一家公司工作 (tā zài yī jiā gōngsī gōngzuò — "
                        "He works at a company). Common phrases: "
                        "工作时间 (gōngzuò shíjiān — working hours), "
                        "工作效率 (gōngzuò xiàolǜ — work efficiency).\n\n"
                        "压力 (yālì) pairs with 大 (dà) or 小 (xiǎo): "
                        "压力很大 (yālì hěn dà — a lot of pressure). "
                        "Patterns: 给...压力 (gěi...yālì — put pressure on...), "
                        "感到压力 (gǎndào yālì — feel pressure), "
                        "来自...的压力 (láizì...de yālì — pressure from...).\n\n"
                        "成功 (chénggōng) as a verb: "
                        "他终于成功了 (tā zhōngyú chénggōngle — He finally succeeded). "
                        "As a noun: 成功需要时间 (chénggōng xūyào shíjiān — Success takes time). "
                        "Pattern: 成功地 + verb (chénggōng de + verb — successfully + verb).\n\n"
                        "梦想 (mèngxiǎng) often pairs with 实现 (shíxiàn) or 追求 (zhuīqiú): "
                        "实现梦想 (shíxiàn mèngxiǎng — realize a dream), "
                        "追求梦想 (zhuīqiú mèngxiǎng — pursue a dream). "
                        "Pattern: 我的梦想是... (wǒ de mèngxiǎng shì... — My dream is...).\n\n"
                        "坚持 (jiānchí) usually takes a verb or noun: "
                        "坚持学习 (jiānchí xuéxí — persist in studying), "
                        "坚持运动 (jiānchí yùndòng — keep exercising). "
                        "Negative patterns: 无法坚持 (wúfǎ jiānchí — unable to persist), "
                        "坚持不下去 (jiānchí bù xiàqù — can't keep going)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 1)",
                "description": "大家好，我是曾之乔。今天我想跟大家分享一个我花了很多年才明白的道理：不要太努力。",
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 1)",
                "description": "Practice speaking along with the excerpt about effort and career pressure",
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
                "title": "Write: Effort and Dreams",
                "description": "Write sentences using Session 1 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "努力",
                            "prompt": (
                                "Use the word 努力 (nǔlì) to talk about hard work or effort — "
                                "as Joanne Tseng describes how she worked relentlessly for years but only grew more exhausted. "
                                "Example: 努力是好事，但不要忘记照顾自己的身体。"
                            ),
                        },
                        {
                            "targetVocab": "工作",
                            "prompt": (
                                "Use the word 工作 (gōngzuò) to talk about work or career — "
                                "as the talk describes how Joanne kept taking on jobs without daring to refuse. "
                                "Example: 工作很重要，但不应该是生活的全部。"
                            ),
                        },
                        {
                            "targetVocab": "压力",
                            "prompt": (
                                "Use the word 压力 (yālì) to talk about pressure in life — "
                                "as Joanne describes how pressure kept growing the harder she pushed herself. "
                                "Example: 现代人的压力来自很多方面，比如工作、家庭和社会。"
                            ),
                        },
                        {
                            "targetVocab": "成功",
                            "prompt": (
                                "Use the word 成功 (chénggōng) to talk about success — "
                                "as the talk asks: what does real success actually mean? "
                                "Example: 真正的成功不是别人怎么看你，而是你自己是否快乐。"
                            ),
                        },
                        {
                            "targetVocab": "梦想",
                            "prompt": (
                                "Use the word 梦想 (mèngxiǎng) to talk about dreams or aspirations — "
                                "as Joanne recalls the dreams she had when she first entered the entertainment industry. "
                                "Example: 追求梦想的路上，不要忘记享受过程。"
                            ),
                        },
                        {
                            "targetVocab": "坚持",
                            "prompt": (
                                "Use the word 坚持 (jiānchí) to talk about perseverance — "
                                "as the talk teaches that sometimes stopping isn't giving up, it's finding the right path. "
                                "Example: 坚持很重要，但也要学会在适当的时候放手。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_1[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Session 2: Group 2 — 失败, 休息, 完美, 自信, 改变, 勇敢 ──

    session_2 = {
        "title": "Session 2: Failure and Change — 失败与改变",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Session 2 Introduction",
                "description": "Recap Session 1 and introduce Session 2 theme",
                "data": {
                    "text": (
                        "Welcome back to Session 2! In the previous session, we learned 6 important words: "
                        "努力 (nǔlì — effort), 工作 (gōngzuò — work), 压力 (yālì — pressure), "
                        "成功 (chénggōng — success), 梦想 (mèngxiǎng — dream), and 坚持 (jiānchí — persevere). "
                        "Do you remember them? Joanne Tseng told us about entering the entertainment industry "
                        "at 15 and pushing herself relentlessly. Today we'll dive deeper into the next part "
                        "of the talk, where she realizes she's been trying too hard and begins to change. "
                        "You'll learn 6 new words related to failure, rest, "
                        "perfection, and courage. Let's go!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 2 Vocabulary",
                "description": "Learn 6 words: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "data": {
                    "text": (
                        "Let's learn today's 6 new vocabulary words. These words come from the middle section "
                        "of the talk, where Joanne begins to recognize the problem and find a way to change.\n\n"

                        "The first word is 失败 (shībài). 失败 works as both a noun and a verb, "
                        "meaning 'failure' or 'to fail'. Joanne describes how she was always terrified of "
                        "失败 (shībài) — afraid that stopping would mean being forgotten, "
                        "afraid that not being good enough would mean being replaced. "
                        "But she realized that 失败 (shībài) itself isn't scary — "
                        "what's scary is being so afraid of failure that you don't dare stop and think. "
                        "For example: 失败并不可怕，可怕的是不敢再尝试 — "
                        "Failure isn't scary; what's scary is not daring to try again. "
                        "失 (shī) means 'to lose' and 败 (bài) means 'defeat'. "
                        "Another usage: 这次考试我失败了，但我不会放弃 — "
                        "I failed this exam, but I won't give up.\n\n"

                        "The second word is 休息 (xiūxi). 休息 is a verb meaning 'to rest'. "
                        "This is one of the most important lessons Joanne shares: "
                        "learning to 休息 (xiūxi). She used to think resting was a waste of time, "
                        "but in reality, not resting is the real waste — because you'll burn out "
                        "and won't be able to do anything well. "
                        "For example: 累了就休息一下，不要勉强自己 — "
                        "When you're tired, take a rest; don't force yourself. "
                        "休 (xiū) means 'to cease' and 息 (xi) means 'to breathe'. "
                        "Common usage: 周末好好休息 (zhōumò hǎohǎo xiūxi — rest well on the weekend), "
                        "休息时间 (xiūxi shíjiān — rest time).\n\n"

                        "The third word is 完美 (wánměi). 完美 is an adjective meaning 'perfect' or 'flawless'. "
                        "Joanne confesses that she was trapped in the pursuit of 完美 (wánměi) — "
                        "always wanting to be the perfect actress, the perfect singer, the perfect person. "
                        "But nobody in this world is 完美 (wánměi). "
                        "For example: 不要追求完美，因为没有人是完美的 — "
                        "Don't chase perfection, because nobody is perfect. "
                        "完 (wán) means 'complete' and 美 (měi) means 'beautiful'. "
                        "Common usage: 完美主义 (wánměi zhǔyì — perfectionism), "
                        "追求完美 (zhuīqiú wánměi — pursue perfection).\n\n"

                        "The fourth word is 自信 (zìxìn). 自信 works as both a noun and an adjective, "
                        "meaning 'confidence' or 'confident'. When Joanne stopped chasing perfection "
                        "and started accepting her true self, she found her 自信 (zìxìn) again. "
                        "Not confidence from doing more work, but confidence from daring to be herself. "
                        "For example: 真正的自信来自接受自己的不完美 — "
                        "True confidence comes from accepting your own imperfections. "
                        "自 (zì) means 'self' and 信 (xìn) means 'trust, believe'. "
                        "Common usage: 他是一个很自信的人 (tā shì yīgè hěn zìxìn de rén — "
                        "He's a very confident person), 缺乏自信 (quēfá zìxìn — lack confidence).\n\n"

                        "The fifth word is 改变 (gǎibiàn). 改变 works as both a verb and a noun, "
                        "meaning 'to change' or 'change'. After realizing she was living the wrong way, "
                        "Joanne decided to 改变 (gǎibiàn). She changed how she viewed success, "
                        "how she treated herself, and how she lived. "
                        "For example: 改变自己比改变别人容易得多 — "
                        "Changing yourself is much easier than changing others. "
                        "改 (gǎi) means 'to alter' and 变 (biàn) means 'to transform'. "
                        "Common usage: 改变想法 (gǎibiàn xiǎngfǎ — change your thinking), "
                        "改变习惯 (gǎibiàn xíguàn — change a habit).\n\n"

                        "The last word is 勇敢 (yǒnggǎn). 勇敢 is an adjective meaning 'brave' or 'courageous'. "
                        "Joanne says 勇敢 (yǒnggǎn) isn't about not being afraid — "
                        "it's about choosing to do what you believe is right even when you are afraid. "
                        "Daring to stop, daring to say 'no', daring to be yourself — that's real 勇敢 (yǒnggǎn). "
                        "For example: 勇敢不是不害怕，而是害怕了还敢去做 — "
                        "Bravery isn't the absence of fear; it's doing it even when you're afraid. "
                        "勇 (yǒng) means 'brave' and 敢 (gǎn) means 'to dare'. "
                        "Common usage: 勇敢地面对困难 (yǒnggǎn de miànduì kùnnan — bravely face difficulties), "
                        "做一个勇敢的人 (zuò yīgè yǒnggǎn de rén — be a brave person).\n\n"

                        "So now you've learned 6 more words: "
                        "失败 (shībài), 休息 (xiūxi), 完美 (wánměi), "
                        "自信 (zìxìn), 改变 (gǎibiàn), 勇敢 (yǒnggǎn). "
                        "Together with the 6 from Session 1, you now have 12 vocabulary words! Let's keep practicing!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Failure and Change",
                "description": "Learn 6 words: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 2 Vocabulary",
                "description": "Practice speaking 6 words: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 2 Vocabulary",
                "description": "Recognize 6 words: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 2 Vocabulary",
                "description": "Match meanings for 6 words: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 2 Vocabulary",
                "description": "Write 6 words: 失败, 休息, 完美, 自信, 改变, 勇敢",
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
                        "失败 (shībài) often pairs with 了 (le) for results: "
                        "他失败了 (tā shībàile — He failed). "
                        "As a noun: 失败是成功之母 (shībài shì chénggōng zhī mǔ — "
                        "Failure is the mother of success). "
                        "Patterns: 害怕失败 (hàipà shībài — afraid of failure), "
                        "接受失败 (jiēshòu shībài — accept failure).\n\n"
                        "休息 (xiūxi) often pairs with time expressions: "
                        "休息一下 (xiūxi yīxià — take a short rest), "
                        "休息两天 (xiūxi liǎng tiān — rest for two days). "
                        "Patterns: 好好休息 (hǎohǎo xiūxi — rest well), "
                        "需要休息 (xūyào xiūxi — need to rest).\n\n"
                        "完美 (wánměi) usually comes before a noun: "
                        "完美的计划 (wánměi de jìhuà — a perfect plan), "
                        "完美的表演 (wánměi de biǎoyǎn — a perfect performance). "
                        "Negative: 不完美 (bù wánměi — imperfect), "
                        "没有完美的人 (méiyǒu wánměi de rén — nobody is perfect).\n\n"
                        "自信 (zìxìn) as an adjective: "
                        "她很自信 (tā hěn zìxìn — She's very confident). "
                        "As a noun: 自信是成功的关键 (zìxìn shì chénggōng de guānjiàn — "
                        "Confidence is the key to success). "
                        "Patterns: 充满自信 (chōngmǎn zìxìn — full of confidence), "
                        "建立自信 (jiànlì zìxìn — build confidence).\n\n"
                        "改变 (gǎibiàn) can take a specific object: "
                        "改变世界 (gǎibiàn shìjiè — change the world), "
                        "改变命运 (gǎibiàn mìngyùn — change your fate). "
                        "Passive: 被...改变 (bèi...gǎibiàn — be changed by...). "
                        "As a noun: 这是一个很大的改变 (zhè shì yīgè hěn dà de gǎibiàn — "
                        "This is a big change).\n\n"
                        "勇敢 (yǒnggǎn) often pairs with 地 (de): "
                        "勇敢地面对 (yǒnggǎn de miànduì — bravely face), "
                        "勇敢地说出来 (yǒnggǎn de shuō chūlái — bravely speak up). "
                        "Patterns: 要勇敢 (yào yǒnggǎn — be brave), "
                        "勇敢的人 (yǒnggǎn de rén — a brave person)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 2)",
                "description": "后来我才慢慢明白：问题不是我不够努力，而是我太努力了。",
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 2)",
                "description": "Practice speaking along with the excerpt about change and finding yourself",
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
                "title": "Write: Failure and Change",
                "description": "Write sentences using Session 2 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "失败",
                            "prompt": (
                                "Use the word 失败 (shībài) to talk about failure — "
                                "as Joanne says what's truly scary isn't failure itself, but not daring to stop and think. "
                                "Example: 每一次失败都教会了我一些重要的东西。"
                            ),
                        },
                        {
                            "targetVocab": "休息",
                            "prompt": (
                                "Use the word 休息 (xiūxi) to talk about resting — "
                                "as the talk emphasizes that resting isn't wasting time. "
                                "Example: 学会休息的人，才能走得更远。"
                            ),
                        },
                        {
                            "targetVocab": "完美",
                            "prompt": (
                                "Use the word 完美 (wánměi) to talk about perfection — "
                                "as Joanne confesses she was trapped in the pursuit of being perfect. "
                                "Example: 世界上没有完美的人，接受自己的不完美才是智慧。"
                            ),
                        },
                        {
                            "targetVocab": "自信",
                            "prompt": (
                                "Use the word 自信 (zìxìn) to talk about confidence — "
                                "as the talk shows that true confidence comes from daring to be yourself. "
                                "Example: 自信不是觉得自己什么都好，而是接受自己的样子。"
                            ),
                        },
                        {
                            "targetVocab": "改变",
                            "prompt": (
                                "Use the word 改变 (gǎibiàn) to talk about change — "
                                "as Joanne decided to change her way of living after realizing she was on the wrong path. "
                                "Example: 想要改变生活，首先要改变自己的想法。"
                            ),
                        },
                        {
                            "targetVocab": "勇敢",
                            "prompt": (
                                "Use the word 勇敢 (yǒnggǎn) to talk about bravery — "
                                "as the talk teaches that bravery means doing what's right even when you're afraid. "
                                "Example: 做自己需要很大的勇敢，但这是值得的。"
                            ),
                        },
                    ],
                    "vocabList": VOCAB_GROUP_2[:],
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Session 3: Group 3 — 选择, 放弃, 快乐, 真实, 平衡, 价值 ──

    session_3 = {
        "title": "Session 3: Balance and Value — 平衡与价值",
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
                        "努力 (nǔlì), 工作 (gōngzuò), 压力 (yālì), 成功 (chénggōng), "
                        "梦想 (mèngxiǎng), 坚持 (jiānchí) in Session 1, and "
                        "失败 (shībài), 休息 (xiūxi), 完美 (wánměi), 自信 (zìxìn), "
                        "改变 (gǎibiàn), 勇敢 (yǒnggǎn) in Session 2. "
                        "You've understood that Joanne went through a journey from pushing herself "
                        "too hard to realizing she needed to change. Today, we'll explore the final part "
                        "of the talk, where she shares about balance, true happiness, "
                        "and the value of living authentically. "
                        "The last 6 words will help you talk about the most important choices "
                        "in life. Let's begin!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words, ENGLISH with PINYIN)
            {
                "activityType": "introAudio",
                "title": "Session 3 Vocabulary",
                "description": "Learn 6 words: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {
                    "text": (
                        "Let's learn our final 6 vocabulary words. These come from the closing section of the talk, "
                        "where Joanne delivers her most powerful message: be true to yourself.\n\n"
                        "The first word is 选择 (xuǎnzé). 选择 works as both a noun and a verb, "
                        "meaning 'choice' or 'to choose'. Joanne says that when she stopped trying so hard, "
                        "she began to have the right to 选择 (xuǎnzé) — to choose rest, "
                        "to choose to say 'no', to choose not to do things that made her unhappy. "
                        "For example: 人生就是不断地选择，每一个选择都很重要 — "
                        "Life is a series of choices, and every choice matters. "
                        "选 (xuǎn) means 'to select' and 择 (zé) means 'to pick'. "
                        "Common usage: 做出选择 (zuòchū xuǎnzé — make a choice), "
                        "选择权 (xuǎnzé quán — the right to choose), "
                        "我选择相信自己 (wǒ xuǎnzé xiāngxìn zìjǐ — I choose to believe in myself).\n\n"

                        "The second word is 放弃 (fàngqì). 放弃 is a verb meaning 'to give up' or 'to abandon'. "
                        "Many people think 放弃 (fàngqì) is always a bad thing. But Joanne argues that "
                        "sometimes giving up things that don't suit you is exactly how you find something better. "
                        "Giving up perfection, giving up others' expectations — that's not weakness. "
                        "For example: 有时候放弃不是失败，而是为了找到更好的方向 — "
                        "Sometimes giving up isn't failure; it's finding a better direction. "
                        "放 (fàng) means 'to release' and 弃 (qì) means 'to discard'. "
                        "Common usage: 不要轻易放弃 (bùyào qīngyì fàngqì — don't give up easily), "
                        "放弃幻想 (fàngqì huànxiǎng — give up illusions).\n\n"

                        "The third word is 快乐 (kuàilè). 快乐 works as both an adjective and a noun, "
                        "meaning 'happy' or 'happiness'. Joanne asks: why did she become less and less "
                        "快乐 (kuàilè) the harder she worked? The answer is that she was living for "
                        "other people's expectations, not for herself. When she started living authentically, "
                        "快乐 (kuàilè) naturally returned. "
                        "For example: 快乐不是拥有很多，而是需要的不多 — "
                        "Happiness isn't about having a lot; it's about needing little. "
                        "快 (kuài) means 'quick, joyful' and 乐 (lè) means 'joy, pleasure'. "
                        "Common usage: 快乐的生活 (kuàilè de shēnghuó — a happy life), "
                        "祝你快乐 (zhù nǐ kuàilè — wishing you happiness).\n\n"
                        "The fourth word is 真实 (zhēnshí). 真实 is an adjective meaning 'real' or 'authentic'. "
                        "This is the most important word in the closing section of the talk. "
                        "Joanne says she no longer chases perfection — she chases 真实 (zhēnshí): "
                        "being real with her feelings, real with her thoughts, real with how she lives. "
                        "For example: 做一个真实的人比做一个完美的人更重要 — "
                        "Being a real person is more important than being a perfect person. "
                        "真 (zhēn) means 'true' and 实 (shí) means 'solid, real'. "
                        "Common usage: 真实的自己 (zhēnshí de zìjǐ — your true self), "
                        "真实的感受 (zhēnshí de gǎnshòu — real feelings).\n\n"

                        "The fifth word is 平衡 (pínghéng). 平衡 works as both a noun and a verb, "
                        "meaning 'balance' or 'to balance'. Joanne says the biggest lesson she learned is "
                        "平衡 (pínghéng) — balance between work and rest, between effort and relaxation, "
                        "between success and happiness. "
                        "For example: 找到工作和生活的平衡是很重要的 — "
                        "Finding balance between work and life is very important. "
                        "平 (píng) means 'flat, even' and 衡 (héng) means 'to weigh'. "
                        "Common usage: 保持平衡 (bǎochí pínghéng — maintain balance), "
                        "心理平衡 (xīnlǐ pínghéng — psychological balance).\n\n"

                        "The last word is 价值 (jiàzhí). 价值 is a noun meaning 'value' or 'worth'. "
                        "Joanne ends the talk with this message: a happy, authentic person "
                        "is the most 有价值 (yǒu jiàzhí — valuable) person. "
                        "Your value doesn't come from how much you do, "
                        "but from whether you dare to live authentically. "
                        "For example: 每个人都有自己的价值，不需要跟别人比较 — "
                        "Everyone has their own value; there's no need to compare with others. "
                        "价 (jià) means 'price' and 值 (zhí) means 'worth'. "
                        "Common usage: 有价值 (yǒu jiàzhí — valuable), "
                        "价值观 (jiàzhí guān — values, worldview), "
                        "人生的价值 (rénshēng de jiàzhí — the value of life).\n\n"

                        "Excellent! You've now learned all 18 vocabulary words: "
                        "努力 (nǔlì), 工作 (gōngzuò), 压力 (yālì), 成功 (chénggōng), "
                        "梦想 (mèngxiǎng), 坚持 (jiānchí), 失败 (shībài), 休息 (xiūxi), "
                        "完美 (wánměi), 自信 (zìxìn), 改变 (gǎibiàn), 勇敢 (yǒnggǎn), "
                        "选择 (xuǎnzé), 放弃 (fàngqì), 快乐 (kuàilè), 真实 (zhēnshí), "
                        "平衡 (pínghéng), 价值 (jiàzhí). Let's practice them in the activities ahead!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Balance and Value",
                "description": "Learn 6 words: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak Session 3 Vocabulary",
                "description": "Practice speaking 6 words: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize Session 3 Vocabulary",
                "description": "Recognize 6 words: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Match Session 3 Vocabulary",
                "description": "Match meanings for 6 words: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Write Session 3 Vocabulary",
                "description": "Write 6 words: 选择, 放弃, 快乐, 真实, 平衡, 价值",
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
                        "选择 (xuǎnzé) usually takes a noun or verb: "
                        "选择工作 (xuǎnzé gōngzuò — choose a job), "
                        "选择放弃 (xuǎnzé fàngqì — choose to give up). "
                        "Patterns: 做出选择 (zuòchū xuǎnzé — make a choice), "
                        "没有选择 (méiyǒu xuǎnzé — no choice), "
                        "正确的选择 (zhèngquè de xuǎnzé — the right choice).\n\n"
                        "放弃 (fàngqì) usually takes a noun: "
                        "放弃梦想 (fàngqì mèngxiǎng — give up a dream), "
                        "放弃机会 (fàngqì jīhuì — give up an opportunity). "
                        "Negative: 不要放弃 (bùyào fàngqì — don't give up), "
                        "永远不放弃 (yǒngyuǎn bù fàngqì — never give up). "
                        "But remember: sometimes 放弃 (fàngqì) is the wise choice.\n\n"
                        "快乐 (kuàilè) usually comes before a noun or after 很 (hěn): "
                        "快乐的人 (kuàilè de rén — a happy person), "
                        "很快乐 (hěn kuàilè — very happy). "
                        "Patterns: 感到快乐 (gǎndào kuàilè — feel happy), "
                        "快乐地生活 (kuàilè de shēnghuó — live happily).\n\n"
                        "真实 (zhēnshí) usually modifies a noun: "
                        "真实的故事 (zhēnshí de gùshi — a true story), "
                        "真实的感情 (zhēnshí de gǎnqíng — genuine feelings). "
                        "Pattern: 面对真实的自己 (miànduì zhēnshí de zìjǐ — face your true self).\n\n"
                        "平衡 (pínghéng) as a noun: "
                        "找到平衡 (zhǎodào pínghéng — find balance). "
                        "As a verb: 平衡工作和生活 (pínghéng gōngzuò hé shēnghuó — "
                        "balance work and life). "
                        "Patterns: 保持平衡 (bǎochí pínghéng — maintain balance), "
                        "失去平衡 (shīqù pínghéng — lose balance).\n\n"
                        "价值 (jiàzhí) often pairs with 有 (yǒu) or an adjective: "
                        "有价值 (yǒu jiàzhí — valuable), "
                        "很有价值 (hěn yǒu jiàzhí — very valuable). "
                        "Patterns: 价值观 (jiàzhí guān — values, worldview), "
                        "人生价值 (rénshēng jiàzhí — the value of life), "
                        "实现自己的价值 (shíxiàn zìjǐ de jiàzhí — realize your own value)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Read: Talk Excerpt (Part 3)",
                "description": "现在的我，学会了一件很重要的事情：平衡。",
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Speak: Talk Excerpt (Part 3)",
                "description": "Practice speaking along with the excerpt about balance and authenticity",
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
                "title": "Write: Balance and Value",
                "description": "Write sentences using Session 3 vocabulary",
                "data": {
                    "items": [
                        {
                            "targetVocab": "选择",
                            "prompt": (
                                "Use the word 选择 (xuǎnzé) to talk about a choice in life — "
                                "as Joanne learned to give herself the right to choose rest and say 'no'. "
                                "Example: 我们每天都在做选择，重要的是选择让自己快乐的事。"
                            ),
                        },
                        {
                            "targetVocab": "放弃",
                            "prompt": (
                                "Use the word 放弃 (fàngqì) to talk about giving something up — "
                                "as the talk teaches that sometimes letting go is how you find a better path. "
                                "Example: 放弃不适合自己的东西，才能找到真正属于自己的。"
                            ),
                        },
                        {
                            "targetVocab": "快乐",
                            "prompt": (
                                "Use the word 快乐 (kuàilè) to talk about happiness or joy — "
                                "as Joanne realized that the harder she tried, the less happy she became. "
                                "Example: 真正的快乐不是来自成功，而是来自做自己喜欢的事。"
                            ),
                        },
                        {
                            "targetVocab": "真实",
                            "prompt": (
                                "Use the word 真实 (zhēnshí) to talk about being authentic — "
                                "as the talk emphasizes that living authentically matters more than living perfectly. "
                                "Example: 一个真实的人比一个完美的人更有魅力。"
                            ),
                        },
                        {
                            "targetVocab": "平衡",
                            "prompt": (
                                "Use the word 平衡 (pínghéng) to talk about balance — "
                                "as Joanne says the biggest lesson she learned was finding balance in life. "
                                "Example: 工作和生活的平衡是现代人最大的挑战之一。"
                            ),
                        },
                        {
                            "targetVocab": "价值",
                            "prompt": (
                                "Use the word 价值 (jiàzhí) to talk about value or worth — "
                                "as the talk ends with the message: an authentic person is the most valuable person. "
                                "Example: 一个人的价值不在于他做了多少，而在于他是否真实。"
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
                        "words on the theme of career, balance, and living authentically. Let's review them all!\n\n"
                        "In Session 1, you learned: 努力 (nǔlì — effort), 工作 (gōngzuò — work), "
                        "压力 (yālì — pressure), 成功 (chénggōng — success), 梦想 (mèngxiǎng — dream), "
                        "坚持 (jiānchí — persevere). These are the foundational words that help you talk about "
                        "career and ambition.\n\n"
                        "In Session 2, you learned: 失败 (shībài — failure), 休息 (xiūxi — rest), "
                        "完美 (wánměi — perfect), 自信 (zìxìn — confidence), 改变 (gǎibiàn — change), "
                        "勇敢 (yǒnggǎn — brave). These words help you talk about recognizing problems "
                        "and beginning to change.\n\n"
                        "In Session 3, you learned: 选择 (xuǎnzé — choice), 放弃 (fàngqì — give up), "
                        "快乐 (kuàilè — happy), 真实 (zhēnshí — authentic), 平衡 (pínghéng — balance), "
                        "价值 (jiàzhí — value). These words help you talk about living authentically "
                        "and finding happiness.\n\n"
                        "Now let's review all 18 words through flashcard activities!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Review All 18 Words",
                "description": "Review 18 words: 努力, 工作, 压力, 成功, 梦想, 坚持, 失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Speak All 18 Words",
                "description": "Practice speaking 18 words: 努力, 工作, 压力, 成功, 梦想, 坚持, 失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Recognize All Vocabulary",
                "description": "Recognize 18 words: 努力, 工作, 压力, 成功, 梦想, 坚持, 失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值",
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
                        "by Joanne Tseng from start to finish. You've learned 18 vocabulary words "
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
                "description": "大家好，我是曾之乔。今天我想跟大家分享一个我花了很多年才明白的道理：不要太努力。",
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

                        "努力 (nǔlì) — effort, to work hard. "
                        "Example: 努力很重要，但方向比努力更重要 — "
                        "Effort is important, but direction matters more than effort.\n\n"

                        "工作 (gōngzuò) — work, to work. "
                        "Example: 找到自己热爱的工作是一种幸福 — "
                        "Finding work you love is a kind of happiness.\n\n"

                        "压力 (yālì) — pressure, stress. "
                        "Example: 学会释放压力，才能更好地生活 — "
                        "Learn to release pressure so you can live better.\n\n"

                        "成功 (chénggōng) — success, to succeed. "
                        "Example: 成功的定义因人而异 — "
                        "The definition of success varies from person to person.\n\n"

                        "梦想 (mèngxiǎng) — dream. "
                        "Example: 梦想不分大小，只要是你的就好 — "
                        "Dreams don't have to be big or small; as long as they're yours, that's enough.\n\n"

                        "坚持 (jiānchí) — to persevere. "
                        "Example: 坚持做对的事，时间会给你答案 — "
                        "Persevere in doing the right thing, and time will give you the answer.\n\n"
                        "失败 (shībài) — failure, to fail. "
                        "Example: 从失败中学习，比从成功中学到的更多 — "
                        "You learn more from failure than from success.\n\n"

                        "休息 (xiūxi) — to rest. "
                        "Example: 休息是为了走更远的路 — "
                        "Rest is for going further down the road.\n\n"

                        "完美 (wánměi) — perfect. "
                        "Example: 不完美才是最真实的美 — "
                        "Imperfection is the most authentic beauty.\n\n"

                        "自信 (zìxìn) — confidence, confident. "
                        "Example: 自信的人不需要别人的认可 — "
                        "A confident person doesn't need others' approval.\n\n"

                        "改变 (gǎibiàn) — to change, change. "
                        "Example: 改变从今天开始，永远不会太晚 — "
                        "Change starts today; it's never too late.\n\n"

                        "勇敢 (yǒnggǎn) — brave, courageous. "
                        "Example: 勇敢地做自己，这就是最好的人生 — "
                        "Bravely be yourself — that's the best life.\n\n"

                        "选择 (xuǎnzé) — choice, to choose. "
                        "Example: 人生最重要的选择是选择做自己 — "
                        "The most important choice in life is choosing to be yourself.\n\n"

                        "放弃 (fàngqì) — to give up. "
                        "Example: 放弃不等于失败，有时候是一种智慧 — "
                        "Giving up doesn't equal failure; sometimes it's wisdom.\n\n"

                        "快乐 (kuàilè) — happy, happiness. "
                        "Example: 快乐是一种选择，不是一种结果 — "
                        "Happiness is a choice, not a result.\n\n"

                        "真实 (zhēnshí) — real, authentic. "
                        "Example: 真实地活着，比完美地表演更有意义 — "
                        "Living authentically is more meaningful than performing perfectly.\n\n"

                        "平衡 (pínghéng) — balance. "
                        "Example: 平衡不是完美，而是知道什么最重要 — "
                        "Balance isn't perfection; it's knowing what matters most.\n\n"

                        "价值 (jiàzhí) — value, worth. "
                        "Example: 你的价值不取决于你的工作，而取决于你是谁 — "
                        "Your value doesn't depend on your work; it depends on who you are.\n\n"
                        "As Joanne Tseng said: 不要太努力。做真实的自己，就已经足够好了 "
                        "(bùyào tài nǔlì. zuò zhēnshí de zìjǐ, jiù yǐjīng zúgòu hǎole) — "
                        "Don't work too hard. Being your true self is already good enough. "
                        "You haven't just learned 18 Chinese vocabulary words — you've gained a deeper understanding "
                        "of how to find balance in life. Remember: your value doesn't come from how hard you push, "
                        "but from whether you dare to live authentically. "
                        "Thank you for learning with us, and we wish you confidence, courage, "
                        "and happiness always! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Learn Through Podcasts: '不要太努力' — 曾之喬 (Don't Work Too Hard)",
        "description": (
            "ARE YOU BURNING YOURSELF OUT JUST TO PROVE YOUR WORTH?\n\n"
            "Every sleepless night chasing a deadline, every time you say no to friends "
            "so you can work overtime, every time you tell yourself 'just a little more effort' — "
            "you're walking the exact path that Taiwanese actress Joanne Tseng (曾之喬) walked "
            "for years. And she'll tell you where that path leads: exhaustion, insomnia, "
            "anxiety, and losing yourself completely.\n\n"
            "Joanne entered the entertainment industry at 15, convinced that if she just "
            "worked hard enough — 努力 (nǔlì) — 成功 (chénggōng) would follow. "
            "But one sentence from a director flipped everything upside down: "
            "'Don't try so hard. The more relaxed you are, the more natural your performance.' "
            "Like a bow pulled too tight — pull too hard and it snaps, "
            "but release at the right moment and the arrow flies the farthest.\n\n"
            "When you stop chasing perfection and start living as your true self, "
            "you'll rediscover confidence, joy, and the real value of your life.\n\n"
            "Learn 18 powerful vocabulary words about career, balance, and authenticity "
            "through an immersive multi-sensory experience that upgrades both your thinking "
            "and your Chinese at the same time."
        ),
        "preview": {
            "text": (
                "Did you know that sometimes the harder you try, the further you drift from happiness? "
                "Taiwanese actress Joanne Tseng from TEDxTaipeiFuhsingPrivateSchool will share her journey "
                "from burnout to freedom. In this course, you'll learn 18 Chinese vocabulary words "
                "at HSK2-HSK3 level about career and work-life balance: "
                "努力 (nǔlì — effort), 工作 (gōngzuò — work), "
                "压力 (yālì — pressure), 成功 (chénggōng — success), "
                "梦想 (mèngxiǎng — dream), 坚持 (jiānchí — persevere), "
                "失败 (shībài — failure), 休息 (xiūxi — rest), "
                "完美 (wánměi — perfect), 自信 (zìxìn — confidence), "
                "改变 (gǎibiàn — change), 勇敢 (yǒnggǎn — brave), "
                "选择 (xuǎnzé — choice), 放弃 (fàngqì — give up), "
                "快乐 (kuàilè — happy), 真实 (zhēnshí — authentic), "
                "平衡 (pínghéng — balance), 价值 (jiàzhí — value). "
                "Across 5 sessions of flashcards, reading, speaking, and writing, "
                "you'll not only master the vocabulary but also gain a deeper understanding "
                "of how Chinese speakers talk about career, pressure, and happiness — "
                "and learn to live authentically instead of chasing perfection."
            ),
        },
        "youtubeUrl": "https://www.youtube.com/watch?v=t7ZI9c6Ze7E",
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
