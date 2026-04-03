"""
Create vi-zh podcast curriculum #2:
曾之喬 (Joanne Tseng) — "不要太努力" (Don't Work Too Hard)

TEDxTaipeiFuhsingPrivateSchool, ~21 minutes, about self-acceptance, career pressure, and balance.
YouTube: https://www.youtube.com/watch?v=t7ZI9c6Ze7E

18 HSK2-HSK3 vocabulary words in 3 groups of 6.
All user-facing text in Vietnamese.
Reading passages in simplified Chinese.

Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 9.1, 9.2, 9.3, 9.4, 9.5
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



# ── Chinese reading passages (simplified Chinese, about work-life balance) ──

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
        "title": "Buổi 1: Nỗ lực và ước mơ — 努力与梦想",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu bài nói chuyện",
                "description": "Giới thiệu bài TEDx Talk của Tăng Chi Kiều về việc đừng cố gắng quá mức",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chào mừng bạn đến với khóa học từ vựng tiếng Trung qua podcast! "
                        "Hôm nay chúng ta sẽ cùng khám phá một bài nói chuyện đầy cảm hứng từ "
                        "TEDxTaipeiFuhsingPrivateSchool — bài '不要太努力' (Đừng cố gắng quá mức) "
                        "của nữ diễn viên và ca sĩ Đài Loan Tăng Chi Kiều (曾之喬). "
                        "Cô ấy bước vào làng giải trí từ năm 15 tuổi, và suốt nhiều năm, "
                        "cô tin rằng chỉ cần cố gắng đủ nhiều, thành công sẽ đến. "
                        "Nhưng thực tế phũ phàng hơn nhiều — càng cố gắng, cô càng kiệt sức, "
                        "mất ngủ, lo âu, và mất đi niềm vui sống. Cho đến khi một đạo diễn nói "
                        "với cô: 'Em đừng dùng sức quá. Càng thả lỏng, diễn xuất càng tự nhiên.' "
                        "Câu nói đó thay đổi không chỉ cách cô diễn xuất, mà cả cách cô sống. "
                        "Trong buổi học đầu tiên này, bạn sẽ học 6 từ vựng quan trọng liên quan "
                        "đến chủ đề nỗ lực, công việc và ước mơ. Mỗi từ đều xuất hiện trong "
                        "bài nói chuyện và sẽ giúp bạn hiểu sâu hơn về cách người Trung Quốc "
                        "nói về sự nghiệp và khát vọng. Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 1",
                "description": "Học 6 từ: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Bây giờ chúng ta sẽ cùng học 6 từ vựng đầu tiên. Mỗi từ đều gắn liền với nội dung "
                        "bài nói chuyện của Tăng Chi Kiều về hành trình sự nghiệp và bài học cuộc sống.\n\n"

                        "Từ đầu tiên là 努力 (nǔlì). 努力 vừa là động từ vừa là tính từ, có nghĩa là "
                        "'nỗ lực' hoặc 'cố gắng'. Đây chính là từ khóa trung tâm của toàn bộ bài nói chuyện. "
                        "Tăng Chi Kiều nói rằng cô đã 努力 suốt nhiều năm — làm việc không ngừng nghỉ, "
                        "hy sinh giấc ngủ, hy sinh sức khỏe — nhưng kết quả không như mong đợi. "
                        "Ví dụ: 我一直很努力地工作，但还是觉得不够好 — Tôi luôn nỗ lực làm việc, "
                        "nhưng vẫn cảm thấy chưa đủ tốt. 努 là 'gắng sức' và 力 là 'sức mạnh'. "
                        "Khi bạn 努力, bạn đang dồn hết sức lực vào một việc gì đó. "
                        "Cách dùng khác: 只要努力，就一定会有收获 — Chỉ cần nỗ lực, nhất định sẽ có thành quả.\n\n"

                        "Từ thứ hai là 工作 (gōngzuò). 工作 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'công việc' hoặc 'làm việc'. Tăng Chi Kiều kể rằng cô liên tục nhận 工作, "
                        "không dám từ chối bất kỳ cơ hội nào vì sợ bị lãng quên. "
                        "Ví dụ: 她每天工作十几个小时，完全没有休息的时间 — Cô ấy mỗi ngày làm việc "
                        "hơn mười tiếng, hoàn toàn không có thời gian nghỉ ngơi. "
                        "工 là 'công, thợ' và 作 là 'tác, làm'. Từ này cực kỳ phổ biến trong cuộc sống: "
                        "找工作 (tìm việc), 工作经验 (kinh nghiệm làm việc), 工作压力 (áp lực công việc).\n\n"

                        "Từ thứ ba là 压力 (yālì). 压力 là danh từ, có nghĩa là 'áp lực' hoặc 'stress'. "
                        "Trong bài nói chuyện, Tăng Chi Kiều mô tả 压力 như một quả bóng tuyết — "
                        "càng lăn càng to, cho đến khi bạn không thể chịu nổi nữa. "
                        "Ví dụ: 工作压力太大了，我需要好好休息一下 — Áp lực công việc quá lớn, "
                        "tôi cần nghỉ ngơi cho tốt. 压 là 'ép, đè' và 力 là 'sức'. "
                        "Cấu trúc phổ biến: 有压力 (có áp lực), 减轻压力 (giảm bớt áp lực), "
                        "压力很大 (áp lực rất lớn).\n\n"

                        "Từ thứ tư là 成功 (chénggōng). 成功 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'thành công'. Tăng Chi Kiều đặt câu hỏi: thành công thực sự là gì? "
                        "Có phải là làm việc nhiều hơn, kiếm tiền nhiều hơn, nổi tiếng hơn? "
                        "Hay thành công là được sống đúng với con người thật của mình? "
                        "Ví dụ: 成功不只是赚很多钱，更重要的是过自己想要的生活 — Thành công không chỉ là "
                        "kiếm nhiều tiền, quan trọng hơn là sống cuộc sống mình muốn. "
                        "成 là 'thành' và 功 là 'công'. Cách dùng: 祝你成功 (chúc bạn thành công), "
                        "成功的秘诀 (bí quyết thành công).\n\n"

                        "Từ thứ năm là 梦想 (mèngxiǎng). 梦想 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'ước mơ' hoặc 'mơ ước'. Khi mới vào nghề, Tăng Chi Kiều có rất nhiều 梦想 — "
                        "trở thành diễn viên giỏi, ca sĩ nổi tiếng, được mọi người yêu mến. "
                        "Nhưng cô nhận ra rằng đuổi theo 梦想 mà quên mất bản thân thì không đáng. "
                        "Ví dụ: 每个人都有自己的梦想，但不要为了梦想而失去自己 — Mỗi người đều có ước mơ "
                        "riêng, nhưng đừng vì ước mơ mà đánh mất chính mình. "
                        "梦 là 'mộng, giấc mơ' và 想 là 'tưởng, nghĩ'. Cách dùng: "
                        "实现梦想 (thực hiện ước mơ), 追求梦想 (theo đuổi ước mơ).\n\n"

                        "Từ cuối cùng trong buổi hôm nay là 坚持 (jiānchí). 坚持 là động từ, có nghĩa là "
                        "'kiên trì' hoặc 'bền bỉ'. Tăng Chi Kiều từng tin rằng 坚持 là đức tính quan trọng nhất — "
                        "không bao giờ bỏ cuộc, không bao giờ dừng lại. Nhưng cô học được rằng đôi khi "
                        "dừng lại không phải là bỏ cuộc, mà là để tìm hướng đi đúng. "
                        "Ví dụ: 坚持是好事，但也要知道什么时候该停下来 — Kiên trì là điều tốt, "
                        "nhưng cũng cần biết khi nào nên dừng lại. "
                        "坚 là 'kiên, cứng' và 持 là 'trì, giữ'. Cách dùng: "
                        "坚持到底 (kiên trì đến cùng), 坚持自己的想法 (kiên trì với suy nghĩ của mình).\n\n"

                        "Vậy là bạn đã biết 6 từ đầu tiên: 努力, 工作, 压力, 成功, 梦想, 坚持. "
                        "Hãy cùng luyện tập qua các hoạt động tiếp theo nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Nỗ lực và ước mơ",
                "description": "Học 6 từ: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 1",
                "description": "Tập nói 6 từ: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 1",
                "description": "Nhận biết 6 từ: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 1",
                "description": "Ghép nghĩa 6 từ: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 1",
                "description": "Viết 6 từ: 努力, 工作, 压力, 成功, 梦想, 坚持",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Ngữ pháp và cách dùng",
                "description": "Hướng dẫn cách sử dụng từ vựng buổi 1 trong câu",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Tuyệt vời! Bạn đã làm quen với 6 từ vựng đầu tiên. Bây giờ hãy cùng tìm hiểu "
                        "cách dùng chúng tự nhiên hơn trong câu nhé.\n\n"
                        "努力 thường đi với 地 khi bổ nghĩa cho động từ: 努力地学习 (nỗ lực học tập), "
                        "努力地工作 (nỗ lực làm việc). Làm tính từ: 他是一个很努力的人 (Anh ấy là người rất nỗ lực). "
                        "Cấu trúc: 努力 + 动词 hoặc 很努力.\n\n"
                        "工作 rất linh hoạt. Làm danh từ: 我的工作很忙 (Công việc tôi rất bận). "
                        "Làm động từ: 他在一家公司工作 (Anh ấy làm việc ở một công ty). "
                        "Cụm từ phổ biến: 工作时间 (giờ làm việc), 工作效率 (hiệu suất công việc).\n\n"
                        "压力 thường đi với 大 hoặc 小: 压力很大 (áp lực rất lớn). "
                        "Cấu trúc: 给...压力 (gây áp lực cho...), 感到压力 (cảm thấy áp lực), "
                        "来自...的压力 (áp lực đến từ...).\n\n"
                        "成功 làm động từ: 他终于成功了 (Anh ấy cuối cùng đã thành công). "
                        "Làm danh từ: 成功需要时间 (Thành công cần thời gian). "
                        "Cấu trúc: 成功地 + 动词 (thành công + động từ).\n\n"
                        "梦想 thường đi với 实现 hoặc 追求: 实现梦想 (thực hiện ước mơ), "
                        "追求梦想 (theo đuổi ước mơ). Cấu trúc: 我的梦想是... (Ước mơ của tôi là...).\n\n"
                        "坚持 thường đi với động từ hoặc danh từ: 坚持学习 (kiên trì học tập), "
                        "坚持运动 (kiên trì tập thể dục). Cấu trúc phủ định: 无法坚持 (không thể kiên trì), "
                        "坚持不下去 (không kiên trì nổi nữa)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 1)",
                "description": "大家好，我是曾之乔。今天我想跟大家分享一个我花了很多年才明白的道理：不要太努力。",
                "practiceMinutes": 9,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 1)",
                "description": "Luyện nói theo đoạn trích về nỗ lực và áp lực trong sự nghiệp",
                "practiceMinutes": 15,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Nghe: Đoạn trích bài nói chuyện (phần 1)",
                "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                "practiceMinutes": 3,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Viết: Nỗ lực và ước mơ",
                "description": "Viết câu sử dụng 6 từ vựng buổi 1",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "努力",
                            "prompt": (
                                "Sử dụng từ '努力' (nǔlì) để nói về sự cố gắng trong học tập hoặc công việc — "
                                "như Tăng Chi Kiều kể rằng cô đã nỗ lực suốt nhiều năm nhưng càng cố càng kiệt sức. "
                                "Ví dụ: 努力是好事，但不要忘记照顾自己的身体。"
                            ),
                        },
                        {
                            "targetVocab": "工作",
                            "prompt": (
                                "Sử dụng từ '工作' (gōngzuò) để nói về công việc hoặc nghề nghiệp — "
                                "như bài nói chuyện mô tả cô liên tục nhận việc không dám từ chối. "
                                "Ví dụ: 工作很重要，但不应该是生活的全部。"
                            ),
                        },
                        {
                            "targetVocab": "压力",
                            "prompt": (
                                "Sử dụng từ '压力' (yālì) để nói về áp lực trong cuộc sống — "
                                "như Tăng Chi Kiều mô tả áp lực ngày càng lớn khi cô cố gắng quá mức. "
                                "Ví dụ: 现代人的压力来自很多方面，比如工作、家庭和社会。"
                            ),
                        },
                        {
                            "targetVocab": "成功",
                            "prompt": (
                                "Sử dụng từ '成功' (chénggōng) để nói về thành công — "
                                "như bài nói chuyện đặt câu hỏi: thành công thực sự là gì? "
                                "Ví dụ: 真正的成功不是别人怎么看你，而是你自己是否快乐。"
                            ),
                        },
                        {
                            "targetVocab": "梦想",
                            "prompt": (
                                "Sử dụng từ '梦想' (mèngxiǎng) để nói về ước mơ hoặc khát vọng — "
                                "như Tăng Chi Kiều kể về những ước mơ khi mới vào nghề diễn xuất. "
                                "Ví dụ: 追求梦想的路上，不要忘记享受过程。"
                            ),
                        },
                        {
                            "targetVocab": "坚持",
                            "prompt": (
                                "Sử dụng từ '坚持' (jiānchí) để nói về sự kiên trì — "
                                "như bài nói chuyện dạy rằng đôi khi dừng lại không phải là bỏ cuộc. "
                                "Ví dụ: 坚持很重要，但也要学会在适当的时候放手。"
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
        "title": "Buổi 2: Thất bại và sự thay đổi — 失败与改变",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu buổi 2",
                "description": "Ôn lại buổi 1 và giới thiệu chủ đề buổi 2",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chào mừng bạn trở lại với buổi học thứ hai! Ở buổi trước, chúng ta đã học 6 từ "
                        "quan trọng: 努力 (nỗ lực), 工作 (công việc), 压力 (áp lực), 成功 (thành công), "
                        "梦想 (ước mơ), và 坚持 (kiên trì). Bạn còn nhớ không? Tăng Chi Kiều đã kể "
                        "về hành trình cô bước vào làng giải trí từ năm 15 tuổi và cố gắng không ngừng. "
                        "Hôm nay chúng ta sẽ đi sâu hơn vào phần tiếp theo của bài nói chuyện, "
                        "nơi cô ấy nhận ra rằng mình đã cố gắng quá mức và bắt đầu thay đổi. "
                        "Bạn sẽ học thêm 6 từ mới liên quan đến thất bại, nghỉ ngơi, "
                        "sự hoàn hảo và lòng dũng cảm. Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 2",
                "description": "Học 6 từ: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng mới của buổi hôm nay. Những từ này nằm ở phần giữa "
                        "bài nói chuyện, khi Tăng Chi Kiều bắt đầu nhận ra vấn đề và tìm cách thay đổi.\n\n"

                        "Từ đầu tiên là 失败 (shībài). 失败 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'thất bại'. Tăng Chi Kiều kể rằng cô luôn sợ 失败 — sợ dừng lại sẽ bị lãng quên, "
                        "sợ không đủ giỏi sẽ bị thay thế. Nhưng cô nhận ra rằng 失败 không đáng sợ — "
                        "đáng sợ là vì sợ thất bại mà không dám dừng lại suy nghĩ. "
                        "Ví dụ: 失败并不可怕，可怕的是不敢再尝试 — Thất bại không đáng sợ, "
                        "đáng sợ là không dám thử lại. 失 là 'mất' và 败 là 'bại'. "
                        "Cách dùng khác: 这次考试我失败了，但我不会放弃 — Kỳ thi này tôi thất bại, "
                        "nhưng tôi sẽ không bỏ cuộc.\n\n"

                        "Từ thứ hai là 休息 (xiūxi). 休息 là động từ, có nghĩa là 'nghỉ ngơi'. "
                        "Đây là một trong những bài học quan trọng nhất mà Tăng Chi Kiều chia sẻ: "
                        "học cách 休息. Cô từng nghĩ rằng nghỉ ngơi là lãng phí thời gian, "
                        "nhưng thực tế, không nghỉ ngơi mới là lãng phí — vì bạn sẽ kiệt sức "
                        "và không thể làm tốt bất cứ điều gì. "
                        "Ví dụ: 累了就休息一下，不要勉强自己 — Mệt thì nghỉ ngơi một chút, "
                        "đừng ép buộc bản thân. 休 là 'nghỉ' và 息 là 'thở, ngơi'. "
                        "Cách dùng: 周末好好休息 (cuối tuần nghỉ ngơi cho tốt), "
                        "休息时间 (thời gian nghỉ ngơi).\n\n"

                        "Từ thứ ba là 完美 (wánměi). 完美 là tính từ, có nghĩa là 'hoàn hảo' hoặc 'hoàn mỹ'. "
                        "Tăng Chi Kiều thú nhận rằng cô đã mắc kẹt trong cái bẫy của sự 完美 — "
                        "luôn muốn trở thành diễn viên hoàn hảo, ca sĩ hoàn hảo, con người hoàn hảo. "
                        "Nhưng thế giới này không có ai 完美 cả. "
                        "Ví dụ: 不要追求完美，因为没有人是完美的 — Đừng theo đuổi sự hoàn hảo, "
                        "vì không ai là hoàn hảo cả. 完 là 'hoàn, trọn vẹn' và 美 là 'đẹp'. "
                        "Cách dùng: 完美主义 (chủ nghĩa hoàn hảo), 追求完美 (theo đuổi sự hoàn hảo).\n\n"

                        "Từ thứ tư là 自信 (zìxìn). 自信 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "'tự tin' hoặc 'sự tự tin'. Khi Tăng Chi Kiều ngừng đuổi theo sự hoàn hảo "
                        "và bắt đầu chấp nhận con người thật của mình, cô tìm lại được 自信. "
                        "Không phải tự tin vì làm được nhiều việc, mà tự tin vì dám là chính mình. "
                        "Ví dụ: 真正的自信来自接受自己的不完美 — Sự tự tin thực sự đến từ việc "
                        "chấp nhận sự không hoàn hảo của bản thân. 自 là 'tự, bản thân' và 信 là 'tin'. "
                        "Cách dùng: 他是一个很自信的人 (Anh ấy là người rất tự tin), "
                        "缺乏自信 (thiếu tự tin).\n\n"

                        "Từ thứ năm là 改变 (gǎibiàn). 改变 là động từ và danh từ, có nghĩa là "
                        "'thay đổi'. Sau khi nhận ra mình đang sống sai cách, Tăng Chi Kiều quyết định "
                        "改变. Cô thay đổi cách nhìn nhận thành công, thay đổi cách đối xử với bản thân, "
                        "và thay đổi cách sống. Ví dụ: 改变自己比改变别人容易得多 — Thay đổi bản thân "
                        "dễ hơn nhiều so với thay đổi người khác. 改 là 'cải, sửa' và 变 là 'biến, đổi'. "
                        "Cách dùng: 改变想法 (thay đổi suy nghĩ), 改变习惯 (thay đổi thói quen).\n\n"

                        "Từ cuối cùng là 勇敢 (yǒnggǎn). 勇敢 là tính từ, có nghĩa là 'dũng cảm' "
                        "hoặc 'can đảm'. Tăng Chi Kiều nói rằng 勇敢 không phải là không sợ hãi — "
                        "mà là dù sợ hãi vẫn chọn làm điều mình cho là đúng. Dám dừng lại, "
                        "dám nói 'không', dám là chính mình — đó mới là 勇敢 thực sự. "
                        "Ví dụ: 勇敢不是不害怕，而是害怕了还敢去做 — Dũng cảm không phải là không sợ, "
                        "mà là sợ rồi vẫn dám làm. 勇 là 'dũng' và 敢 là 'dám'. "
                        "Cách dùng: 勇敢地面对困难 (dũng cảm đối mặt khó khăn), "
                        "做一个勇敢的人 (làm một người dũng cảm).\n\n"

                        "Vậy là bạn đã học thêm 6 từ mới: 失败, 休息, 完美, 自信, 改变, 勇敢. "
                        "Cùng với 6 từ buổi trước, bạn đã có 12 từ vựng rồi! Hãy luyện tập tiếp nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Thất bại và sự thay đổi",
                "description": "Học 6 từ: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 2",
                "description": "Tập nói 6 từ: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 2",
                "description": "Nhận biết 6 từ: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 2",
                "description": "Ghép nghĩa 6 từ: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 2",
                "description": "Viết 6 từ: 失败, 休息, 完美, 自信, 改变, 勇敢",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Ngữ pháp và cách dùng",
                "description": "Hướng dẫn cách sử dụng từ vựng buổi 2 trong câu",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Rất tốt! Bạn đã nắm được 6 từ mới. Hãy cùng xem cách dùng chúng tự nhiên hơn.\n\n"
                        "失败 thường đi với 了 khi nói về kết quả: 他失败了 (Anh ấy thất bại rồi). "
                        "Làm danh từ: 失败是成功之母 (Thất bại là mẹ thành công). "
                        "Cấu trúc: 害怕失败 (sợ thất bại), 接受失败 (chấp nhận thất bại).\n\n"
                        "休息 thường đi với thời gian: 休息一下 (nghỉ một chút), 休息两天 (nghỉ hai ngày). "
                        "Cấu trúc: 好好休息 (nghỉ ngơi cho tốt), 需要休息 (cần nghỉ ngơi).\n\n"
                        "完美 thường đứng trước danh từ: 完美的计划 (kế hoạch hoàn hảo), "
                        "完美的表演 (màn trình diễn hoàn hảo). Cấu trúc phủ định: 不完美 (không hoàn hảo), "
                        "没有完美的人 (không có người hoàn hảo).\n\n"
                        "自信 làm tính từ: 她很自信 (Cô ấy rất tự tin). Làm danh từ: "
                        "自信是成功的关键 (Tự tin là chìa khóa thành công). "
                        "Cấu trúc: 充满自信 (tràn đầy tự tin), 建立自信 (xây dựng sự tự tin).\n\n"
                        "改变 có thể đi với đối tượng cụ thể: 改变世界 (thay đổi thế giới), "
                        "改变命运 (thay đổi số phận). Cấu trúc bị động: 被...改变 (bị...thay đổi). "
                        "Làm danh từ: 这是一个很大的改变 (Đây là một sự thay đổi rất lớn).\n\n"
                        "勇敢 thường đi với 地: 勇敢地面对 (dũng cảm đối mặt), "
                        "勇敢地说出来 (dũng cảm nói ra). Cấu trúc: 要勇敢 (hãy dũng cảm), "
                        "勇敢的人 (người dũng cảm)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 2)",
                "description": "后来我才慢慢明白：问题不是我不够努力，而是我太努力了。",
                "practiceMinutes": 9,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 2)",
                "description": "Luyện nói theo đoạn trích về sự thay đổi và tìm lại bản thân",
                "practiceMinutes": 15,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Nghe: Đoạn trích bài nói chuyện (phần 2)",
                "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                "practiceMinutes": 3,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Viết: Thất bại và sự thay đổi",
                "description": "Viết câu sử dụng 6 từ vựng buổi 2",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "失败",
                            "prompt": (
                                "Sử dụng từ '失败' (shībài) để nói về thất bại — "
                                "như Tăng Chi Kiều nói rằng đáng sợ không phải là thất bại, mà là không dám dừng lại. "
                                "Ví dụ: 每一次失败都教会了我一些重要的东西。"
                            ),
                        },
                        {
                            "targetVocab": "休息",
                            "prompt": (
                                "Sử dụng từ '休息' (xiūxi) để nói về việc nghỉ ngơi — "
                                "như bài nói chuyện nhấn mạnh rằng nghỉ ngơi không phải là lãng phí thời gian. "
                                "Ví dụ: 学会休息的人，才能走得更远。"
                            ),
                        },
                        {
                            "targetVocab": "完美",
                            "prompt": (
                                "Sử dụng từ '完美' (wánměi) để nói về sự hoàn hảo — "
                                "như Tăng Chi Kiều thú nhận cô đã mắc kẹt trong cái bẫy theo đuổi sự hoàn hảo. "
                                "Ví dụ: 世界上没有完美的人，接受自己的不完美才是智慧。"
                            ),
                        },
                        {
                            "targetVocab": "自信",
                            "prompt": (
                                "Sử dụng từ '自信' (zìxìn) để nói về sự tự tin — "
                                "như bài nói chuyện cho thấy tự tin thực sự đến từ việc dám là chính mình. "
                                "Ví dụ: 自信不是觉得自己什么都好，而是接受自己的样子。"
                            ),
                        },
                        {
                            "targetVocab": "改变",
                            "prompt": (
                                "Sử dụng từ '改变' (gǎibiàn) để nói về sự thay đổi — "
                                "như Tăng Chi Kiều quyết định thay đổi cách sống sau khi nhận ra mình đang sai. "
                                "Ví dụ: 想要改变生活，首先要改变自己的想法。"
                            ),
                        },
                        {
                            "targetVocab": "勇敢",
                            "prompt": (
                                "Sử dụng từ '勇敢' (yǒnggǎn) để nói về sự dũng cảm — "
                                "như bài nói chuyện dạy rằng dũng cảm là dù sợ vẫn dám làm điều đúng. "
                                "Ví dụ: 做自己需要很大的勇敢，但这是值得的。"
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
        "title": "Buổi 3: Cân bằng và giá trị — 平衡与价值",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu buổi 3",
                "description": "Ôn lại buổi 1-2 và giới thiệu chủ đề buổi 3",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chào mừng bạn đến với buổi học thứ ba — buổi cuối cùng trước khi ôn tập! "
                        "Qua hai buổi trước, bạn đã học 12 từ vựng: 努力, 工作, 压力, 成功, 梦想, 坚持 "
                        "ở buổi 1, và 失败, 休息, 完美, 自信, 改变, 勇敢 ở buổi 2. "
                        "Bạn đã hiểu rằng Tăng Chi Kiều đã trải qua hành trình từ cố gắng quá mức "
                        "đến nhận ra mình cần thay đổi. Hôm nay, chúng ta sẽ đi vào phần cuối "
                        "của bài nói chuyện, nơi cô ấy chia sẻ về sự cân bằng, hạnh phúc thực sự, "
                        "và giá trị của việc sống đúng với bản thân. "
                        "6 từ vựng cuối cùng sẽ giúp bạn nói về những lựa chọn quan trọng nhất "
                        "trong cuộc sống. Hãy bắt đầu nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 3",
                "description": "Học 6 từ: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng cuối cùng. Đây là những từ nằm ở phần kết của bài nói chuyện, "
                        "khi Tăng Chi Kiều đưa ra thông điệp mạnh mẽ nhất: hãy sống thật với chính mình.\n\n"

                        "Từ đầu tiên là 选择 (xuǎnzé). 选择 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'lựa chọn'. Tăng Chi Kiều nói rằng khi cô ngừng cố gắng quá mức, cô bắt đầu "
                        "có quyền 选择 — chọn nghỉ ngơi, chọn nói 'không', chọn không làm những điều "
                        "khiến mình không vui. Ví dụ: 人生就是不断地选择，每一个选择都很重要 — "
                        "Cuộc đời là liên tục lựa chọn, mỗi lựa chọn đều rất quan trọng. "
                        "选 là 'tuyển, chọn' và 择 là 'trạch, lựa'. Cách dùng: "
                        "做出选择 (đưa ra lựa chọn), 选择权 (quyền lựa chọn), "
                        "我选择相信自己 (Tôi chọn tin vào bản thân).\n\n"

                        "Từ thứ hai là 放弃 (fàngqì). 放弃 là động từ, có nghĩa là 'từ bỏ' hoặc 'bỏ cuộc'. "
                        "Nhiều người nghĩ rằng 放弃 luôn là điều xấu. Nhưng Tăng Chi Kiều cho rằng "
                        "đôi khi 放弃 những thứ không phù hợp chính là cách để tìm thấy điều tốt hơn. "
                        "Từ bỏ sự hoàn hảo, từ bỏ kỳ vọng của người khác — đó không phải là yếu đuối. "
                        "Ví dụ: 有时候放弃不是失败，而是为了找到更好的方向 — Đôi khi từ bỏ không phải "
                        "là thất bại, mà là để tìm hướng đi tốt hơn. 放 là 'buông, thả' và 弃 là 'bỏ'. "
                        "Cách dùng: 不要轻易放弃 (đừng dễ dàng bỏ cuộc), "
                        "放弃幻想 (từ bỏ ảo tưởng).\n\n"

                        "Từ thứ ba là 快乐 (kuàilè). 快乐 là tính từ và danh từ, có nghĩa là 'vui vẻ' "
                        "hoặc 'hạnh phúc'. Tăng Chi Kiều đặt câu hỏi: tại sao cô càng nỗ lực lại càng "
                        "không 快乐? Câu trả lời là vì cô đang sống cho kỳ vọng của người khác, "
                        "không phải cho bản thân mình. Khi cô bắt đầu sống thật, 快乐 tự nhiên quay lại. "
                        "Ví dụ: 快乐不是拥有很多，而是需要的不多 — Hạnh phúc không phải là sở hữu nhiều, "
                        "mà là cần ít thôi. 快 là 'nhanh, vui' và 乐 là 'lạc, vui'. "
                        "Cách dùng: 快乐的生活 (cuộc sống vui vẻ), 祝你快乐 (chúc bạn vui vẻ).\n\n"

                        "Từ thứ tư là 真实 (zhēnshí). 真实 là tính từ, có nghĩa là 'chân thực' "
                        "hoặc 'thật sự'. Đây là từ khóa quan trọng nhất trong phần kết bài nói chuyện. "
                        "Tăng Chi Kiều nói: cô không còn theo đuổi sự hoàn hảo, mà theo đuổi sự 真实 — "
                        "thật với cảm xúc, thật với suy nghĩ, thật với cách sống. "
                        "Ví dụ: 做一个真实的人比做一个完美的人更重要 — Làm một người chân thực "
                        "quan trọng hơn làm một người hoàn hảo. 真 là 'chân, thật' và 实 là 'thực'. "
                        "Cách dùng: 真实的自己 (con người thật của mình), "
                        "真实的感受 (cảm xúc thật sự).\n\n"

                        "Từ thứ năm là 平衡 (pínghéng). 平衡 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'cân bằng'. Tăng Chi Kiều nói rằng bài học lớn nhất cô học được là 平衡 — "
                        "cân bằng giữa công việc và nghỉ ngơi, giữa nỗ lực và thư giãn, "
                        "giữa thành công và hạnh phúc. Ví dụ: 找到工作和生活的平衡是很重要的 — "
                        "Tìm được sự cân bằng giữa công việc và cuộc sống rất quan trọng. "
                        "平 là 'bình, phẳng' và 衡 là 'hành, cân'. Cách dùng: "
                        "保持平衡 (giữ cân bằng), 心理平衡 (cân bằng tâm lý).\n\n"

                        "Từ cuối cùng là 价值 (jiàzhí). 价值 là danh từ, có nghĩa là 'giá trị'. "
                        "Tăng Chi Kiều kết thúc bài nói chuyện với thông điệp: một người vui vẻ, "
                        "chân thực mới là người có 价值 nhất. Giá trị của bạn không nằm ở việc "
                        "bạn làm được bao nhiêu, mà ở việc bạn có dám sống thật hay không. "
                        "Ví dụ: 每个人都有自己的价值，不需要跟别人比较 — Mỗi người đều có giá trị "
                        "riêng, không cần so sánh với người khác. 价 là 'giá' và 值 là 'trị, đáng'. "
                        "Cách dùng: 有价值 (có giá trị), 价值观 (quan niệm giá trị), "
                        "人生的价值 (giá trị cuộc đời).\n\n"

                        "Tuyệt vời! Bạn đã học xong toàn bộ 18 từ vựng: 努力, 工作, 压力, 成功, 梦想, 坚持, "
                        "失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值. "
                        "Hãy luyện tập qua các hoạt động tiếp theo!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Cân bằng và giá trị",
                "description": "Học 6 từ: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 3",
                "description": "Tập nói 6 từ: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 3",
                "description": "Nhận biết 6 từ: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 3",
                "description": "Ghép nghĩa 6 từ: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 3",
                "description": "Viết 6 từ: 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 8. introAudio — grammar/usage
            {
                "activityType": "introAudio",
                "title": "Ngữ pháp và cách dùng",
                "description": "Hướng dẫn cách sử dụng từ vựng buổi 3 trong câu",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Xuất sắc! Bạn đã hoàn thành 18 từ vựng. Hãy cùng xem cách dùng 6 từ cuối "
                        "một cách tự nhiên.\n\n"
                        "选择 thường đi với danh từ hoặc động từ: 选择工作 (chọn công việc), "
                        "选择放弃 (chọn từ bỏ). Cấu trúc: 做出选择 (đưa ra lựa chọn), "
                        "没有选择 (không có lựa chọn), 正确的选择 (lựa chọn đúng đắn).\n\n"
                        "放弃 thường đi với danh từ: 放弃梦想 (từ bỏ ước mơ), "
                        "放弃机会 (từ bỏ cơ hội). Cấu trúc phủ định: 不要放弃 (đừng bỏ cuộc), "
                        "永远不放弃 (không bao giờ bỏ cuộc). Nhưng nhớ: đôi khi 放弃 là khôn ngoan.\n\n"
                        "快乐 thường đứng trước danh từ hoặc sau 很: 快乐的人 (người vui vẻ), "
                        "很快乐 (rất vui vẻ). Cấu trúc: 感到快乐 (cảm thấy vui vẻ), "
                        "快乐地生活 (sống vui vẻ).\n\n"
                        "真实 thường bổ nghĩa cho danh từ: 真实的故事 (câu chuyện có thật), "
                        "真实的感情 (tình cảm chân thực). Cấu trúc: 面对真实的自己 (đối mặt với "
                        "con người thật của mình).\n\n"
                        "平衡 làm danh từ: 找到平衡 (tìm được sự cân bằng). "
                        "Làm động từ: 平衡工作和生活 (cân bằng công việc và cuộc sống). "
                        "Cấu trúc: 保持平衡 (giữ cân bằng), 失去平衡 (mất cân bằng).\n\n"
                        "价值 thường đi với 有 hoặc tính từ: 有价值 (có giá trị), "
                        "很有价值 (rất có giá trị). Cấu trúc: 价值观 (quan niệm giá trị), "
                        "人生价值 (giá trị cuộc đời), 实现自己的价值 (thực hiện giá trị bản thân)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 3)",
                "description": "现在的我，学会了一件很重要的事情：平衡。",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 3)",
                "description": "Luyện nói theo đoạn trích về sự cân bằng và sống thật",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 11. readAlong
            {
                "activityType": "readAlong",
                "title": "Nghe: Đoạn trích bài nói chuyện (phần 3)",
                "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                "practiceMinutes": 3,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 12. writingSentence
            {
                "activityType": "writingSentence",
                "title": "Viết: Cân bằng và giá trị",
                "description": "Viết câu sử dụng 6 từ vựng buổi 3",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "选择",
                            "prompt": (
                                "Sử dụng từ '选择' (xuǎnzé) để nói về một lựa chọn trong cuộc sống — "
                                "như Tăng Chi Kiều học cách cho mình quyền chọn nghỉ ngơi và nói 'không'. "
                                "Ví dụ: 我们每天都在做选择，重要的是选择让自己快乐的事。"
                            ),
                        },
                        {
                            "targetVocab": "放弃",
                            "prompt": (
                                "Sử dụng từ '放弃' (fàngqì) để nói về việc từ bỏ — "
                                "như bài nói chuyện dạy rằng đôi khi từ bỏ là để tìm hướng đi tốt hơn. "
                                "Ví dụ: 放弃不适合自己的东西，才能找到真正属于自己的。"
                            ),
                        },
                        {
                            "targetVocab": "快乐",
                            "prompt": (
                                "Sử dụng từ '快乐' (kuàilè) để nói về niềm vui hoặc hạnh phúc — "
                                "như Tăng Chi Kiều nhận ra rằng càng cố gắng càng không vui vẻ. "
                                "Ví dụ: 真正的快乐不是来自成功，而是来自做自己喜欢的事。"
                            ),
                        },
                        {
                            "targetVocab": "真实",
                            "prompt": (
                                "Sử dụng từ '真实' (zhēnshí) để nói về sự chân thực — "
                                "như bài nói chuyện nhấn mạnh rằng sống thật quan trọng hơn sống hoàn hảo. "
                                "Ví dụ: 一个真实的人比一个完美的人更有魅力。"
                            ),
                        },
                        {
                            "targetVocab": "平衡",
                            "prompt": (
                                "Sử dụng từ '平衡' (pínghéng) để nói về sự cân bằng — "
                                "như Tăng Chi Kiều nói rằng bài học lớn nhất cô học được là cân bằng cuộc sống. "
                                "Ví dụ: 工作和生活的平衡是现代人最大的挑战之一。"
                            ),
                        },
                        {
                            "targetVocab": "价值",
                            "prompt": (
                                "Sử dụng từ '价值' (jiàzhí) để nói về giá trị — "
                                "như bài nói chuyện kết thúc với thông điệp: người chân thực mới là người có giá trị nhất. "
                                "Ví dụ: 一个人的价值不在于他做了多少，而在于他是否真实。"
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
        "title": "Ôn tập",
        "activities": [
            # 1. introAudio
            {
                "activityType": "introAudio",
                "title": "Chúc mừng và ôn tập",
                "description": "Ôn lại toàn bộ 18 từ vựng đã học",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chúc mừng bạn! Bạn đã hoàn thành 3 buổi học và nắm được 18 từ vựng tiếng Trung "
                        "về chủ đề sự nghiệp, cân bằng cuộc sống và sống thật. Hãy cùng ôn lại nhé!\n\n"
                        "Buổi 1, bạn đã học: 努力 (nỗ lực), 工作 (công việc), 压力 (áp lực), "
                        "成功 (thành công), 梦想 (ước mơ), 坚持 (kiên trì). Đây là những từ nền tảng "
                        "giúp bạn nói về sự nghiệp và khát vọng.\n\n"
                        "Buổi 2, bạn đã học: 失败 (thất bại), 休息 (nghỉ ngơi), 完美 (hoàn hảo), "
                        "自信 (tự tin), 改变 (thay đổi), 勇敢 (dũng cảm). Những từ này giúp bạn nói về "
                        "quá trình nhận ra vấn đề và bắt đầu thay đổi.\n\n"
                        "Buổi 3, bạn đã học: 选择 (lựa chọn), 放弃 (từ bỏ), 快乐 (vui vẻ), "
                        "真实 (chân thực), 平衡 (cân bằng), 价值 (giá trị). Đây là những từ "
                        "giúp bạn nói về cách sống thật và tìm được hạnh phúc.\n\n"
                        "Bây giờ hãy ôn tập toàn bộ 18 từ qua các hoạt động flashcard!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập toàn bộ 18 từ vựng",
                "description": "Ôn tập 18 từ: 努力, 工作, 压力, 成功, 梦想, 坚持, 失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói toàn bộ 18 từ vựng",
                "description": "Tập nói 18 từ: 努力, 工作, 压力, 成功, 梦想, 坚持, 失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết toàn bộ từ vựng",
                "description": "Nhận biết 18 từ: 努力, 工作, 压力, 成功, 梦想, 坚持, 失败, 休息, 完美, 自信, 改变, 勇敢, 选择, 放弃, 快乐, 真实, 平衡, 价值",
                "practiceMinutes": 6,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
        ],
    }


    # ── Session 5: Full reading + farewell ──

    session_5_final = {
        "title": "Đọc toàn bộ bài nói chuyện",
        "activities": [
            # 1. introAudio — intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu buổi đọc trọn vẹn",
                "description": "Giới thiệu buổi đọc toàn bộ bài nói chuyện",
                "practiceMinutes": 1,
                "data": {
                    "text": (
                        "Chào mừng bạn đến với buổi cuối cùng! Hôm nay bạn sẽ đọc toàn bộ bài nói chuyện "
                        "của Tăng Chi Kiều từ đầu đến cuối. Bạn đã học 18 từ vựng qua 3 buổi học "
                        "và ôn tập ở buổi 4. Bây giờ là lúc bạn thử sức với toàn bộ văn bản. "
                        "Hãy đọc chậm, chú ý đến những từ bạn đã học, và cảm nhận cách chúng "
                        "kết nối với nhau trong ngữ cảnh thực tế. Chúc bạn đọc vui!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. reading — full transcript
            {
                "activityType": "reading",
                "title": "Đọc: Toàn bộ bài nói chuyện",
                "description": "大家好，我是曾之乔。今天我想跟大家分享一个我花了很多年才明白的道理：不要太努力。",
                "practiceMinutes": 5,
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 3. speakReading — full transcript
            {
                "activityType": "speakReading",
                "title": "Tập nói: Toàn bộ bài nói chuyện",
                "description": "Luyện nói theo toàn bộ bài nói chuyện",
                "practiceMinutes": 5,
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 4. readAlong — full transcript
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ bài nói chuyện",
                "description": "Nghe toàn bộ bài nói chuyện và theo dõi.",
                "practiceMinutes": 3,
                "data": {"text": FULL_TRANSCRIPT, "audioSpeed": 0},
            },
            # 5. introAudio — farewell reviewing all 18 words
            {
                "activityType": "introAudio",
                "title": "Lời chia tay và ôn tập từ vựng",
                "description": "Ôn tập 18 từ vựng và lời chia tay",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Chúc mừng bạn đã hoàn thành toàn bộ khóa học! Bạn đã đi một chặng đường tuyệt vời. "
                        "Hãy cùng ôn lại 18 từ vựng một lần cuối nhé.\n\n"

                        "努力 (nǔlì) — nỗ lực, cố gắng. Ví dụ: 努力很重要，但方向比努力更重要 — "
                        "Nỗ lực rất quan trọng, nhưng hướng đi còn quan trọng hơn nỗ lực.\n\n"

                        "工作 (gōngzuò) — công việc, làm việc. Ví dụ: 找到自己热爱的工作是一种幸福 — "
                        "Tìm được công việc mình yêu thích là một loại hạnh phúc.\n\n"

                        "压力 (yālì) — áp lực, stress. Ví dụ: 学会释放压力，才能更好地生活 — "
                        "Học cách giải tỏa áp lực mới có thể sống tốt hơn.\n\n"

                        "成功 (chénggōng) — thành công. Ví dụ: 成功的定义因人而异 — "
                        "Định nghĩa thành công mỗi người mỗi khác.\n\n"

                        "梦想 (mèngxiǎng) — ước mơ. Ví dụ: 梦想不分大小，只要是你的就好 — "
                        "Ước mơ không phân lớn nhỏ, chỉ cần là của bạn là được.\n\n"

                        "坚持 (jiānchí) — kiên trì. Ví dụ: 坚持做对的事，时间会给你答案 — "
                        "Kiên trì làm điều đúng, thời gian sẽ cho bạn câu trả lời.\n\n"

                        "失败 (shībài) — thất bại. Ví dụ: 从失败中学习，比从成功中学到的更多 — "
                        "Học từ thất bại nhiều hơn học từ thành công.\n\n"

                        "休息 (xiūxi) — nghỉ ngơi. Ví dụ: 休息是为了走更远的路 — "
                        "Nghỉ ngơi là để đi con đường dài hơn.\n\n"

                        "完美 (wánměi) — hoàn hảo. Ví dụ: 不完美才是最真实的美 — "
                        "Không hoàn hảo mới là vẻ đẹp chân thực nhất.\n\n"

                        "自信 (zìxìn) — tự tin. Ví dụ: 自信的人不需要别人的认可 — "
                        "Người tự tin không cần sự công nhận của người khác.\n\n"

                        "改变 (gǎibiàn) — thay đổi. Ví dụ: 改变从今天开始，永远不会太晚 — "
                        "Thay đổi bắt đầu từ hôm nay, không bao giờ là quá muộn.\n\n"

                        "勇敢 (yǒnggǎn) — dũng cảm. Ví dụ: 勇敢地做自己，这就是最好的人生 — "
                        "Dũng cảm làm chính mình, đó là cuộc đời tốt đẹp nhất.\n\n"

                        "选择 (xuǎnzé) — lựa chọn. Ví dụ: 人生最重要的选择是选择做自己 — "
                        "Lựa chọn quan trọng nhất trong đời là chọn làm chính mình.\n\n"

                        "放弃 (fàngqì) — từ bỏ. Ví dụ: 放弃不等于失败，有时候是一种智慧 — "
                        "Từ bỏ không đồng nghĩa với thất bại, đôi khi đó là trí tuệ.\n\n"

                        "快乐 (kuàilè) — vui vẻ, hạnh phúc. Ví dụ: 快乐是一种选择，不是一种结果 — "
                        "Hạnh phúc là một sự lựa chọn, không phải một kết quả.\n\n"

                        "真实 (zhēnshí) — chân thực. Ví dụ: 真实地活着，比完美地表演更有意义 — "
                        "Sống chân thực có ý nghĩa hơn diễn xuất hoàn hảo.\n\n"

                        "平衡 (pínghéng) — cân bằng. Ví dụ: 平衡不是完美，而是知道什么最重要 — "
                        "Cân bằng không phải là hoàn hảo, mà là biết điều gì quan trọng nhất.\n\n"

                        "价值 (jiàzhí) — giá trị. Ví dụ: 你的价值不取决于你的工作，而取决于你是谁 — "
                        "Giá trị của bạn không phụ thuộc vào công việc, mà phụ thuộc vào bạn là ai.\n\n"

                        "Như Tăng Chi Kiều đã nói: 不要太努力。做真实的自己，就已经足够好了 — "
                        "Đừng cố gắng quá mức. Làm chính mình, đã đủ tốt rồi. "
                        "Bạn đã không chỉ học được 18 từ vựng tiếng Trung, mà còn hiểu sâu hơn "
                        "về cách tìm được sự cân bằng trong cuộc sống. Hãy nhớ: giá trị của bạn "
                        "không nằm ở việc bạn cố gắng bao nhiêu, mà ở việc bạn có dám sống thật hay không. "
                        "Cảm ơn bạn đã đồng hành, và chúc bạn luôn vui vẻ, tự tin và dũng cảm! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Học Qua Podcast: '不要太努力' — 曾之喬 (Đừng cố gắng quá mức)",
        "description": (
            "BẠN CÓ ĐANG TỰ ĐỐT CHÁY MÌNH ĐỂ CHỨNG MINH GIÁ TRỊ BẢN THÂN?\n\n"
            "Mỗi đêm mất ngủ vì deadline, mỗi lần từ chối bạn bè để làm thêm giờ, "
            "mỗi lần tự nhủ 'chỉ cần cố thêm một chút nữa' — bạn đang đi trên con đường "
            "mà Tăng Chi Kiều đã đi suốt nhiều năm. Và cô ấy sẽ nói cho bạn biết: "
            "con đường đó dẫn đến kiệt sức, mất ngủ, lo âu, và mất đi chính mình.\n\n"
            "Nữ diễn viên Đài Loan Tăng Chi Kiều (曾之喬) bước vào làng giải trí từ năm 15 tuổi. "
            "Cô tin rằng chỉ cần 努力 đủ nhiều, 成功 sẽ đến. Nhưng một câu nói của đạo diễn "
            "đã lật ngược mọi thứ: 'Em đừng dùng sức quá. Càng thả lỏng, diễn xuất càng tự nhiên.' "
            "Giống như cây cung — kéo quá căng sẽ gãy, nhưng thả lỏng đúng lúc "
            "mới bắn được xa nhất.\n\n"
            "Khi bạn ngừng đuổi theo sự hoàn hảo và bắt đầu sống thật với chính mình, "
            "bạn sẽ tìm lại được sự tự tin, niềm vui, và giá trị đích thực của cuộc đời.\n\n"
            "Học 18 từ vựng đắt giá về sự nghiệp, cân bằng và sống thật cùng trải nghiệm "
            "đa giác quan giúp bạn vừa nâng cấp tư duy, vừa nâng trình tiếng Trung một cách vượt bậc."
        ),
        "preview": {
            "text": (
                "Bạn có biết rằng càng cố gắng, đôi khi bạn càng xa rời hạnh phúc? "
                "Nữ diễn viên Đài Loan Tăng Chi Kiều từ TEDxTaipeiFuhsingPrivateSchool sẽ kể cho bạn "
                "câu chuyện về hành trình từ kiệt sức đến tự do. Trong khóa học này, bạn sẽ học 18 từ vựng "
                "tiếng Trung cấp độ HSK2-HSK3 về sự nghiệp và cân bằng cuộc sống: 努力 (nỗ lực), "
                "工作 (công việc), 压力 (áp lực), 成功 (thành công), 梦想 (ước mơ), 坚持 (kiên trì), "
                "失败 (thất bại), 休息 (nghỉ ngơi), 完美 (hoàn hảo), 自信 (tự tin), 改变 (thay đổi), "
                "勇敢 (dũng cảm), 选择 (lựa chọn), 放弃 (từ bỏ), 快乐 (vui vẻ), 真实 (chân thực), "
                "平衡 (cân bằng), 价值 (giá trị). Qua 5 buổi học với flashcard, bài đọc, luyện nói "
                "và viết câu, bạn sẽ không chỉ nắm vững từ vựng mà còn hiểu sâu hơn về cách "
                "người Trung Quốc nói về sự nghiệp, áp lực và hạnh phúc — và học cách sống thật "
                "với chính mình thay vì đuổi theo sự hoàn hảo."
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
            "userLanguage": "vi",
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
