"""
Create vi-zh podcast curriculum #0:
陳永儀 (May Chen) — "沒有「負面能量」是好事嗎？需要重新認識的「情緒反應」"
(Acknowledge and Embrace Your Negative Emotions)

TEDxTaipei, ~15 minutes, about emotions and psychology.
YouTube: https://www.youtube.com/watch?v=uiJ4zibW8_M

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



# ── Chinese reading passages (shared across reading/speakReading/readAlong) ──

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
        "title": "Buổi 1: Cảm xúc và năng lượng \u2014 情绪与能量",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu bài nói chuyện",
                "description": "Giới thiệu bài TED Talk của Trần Vĩnh Nghi về cảm xúc tiêu cực",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chào mừng bạn đến với khóa học từ vựng tiếng Trung qua podcast! "
                        "Hôm nay chúng ta sẽ cùng khám phá một bài nói chuyện rất đặc biệt từ TEDxTaipei \u2014 "
                        "bài \u201c沒有「負面能量」是好事嗎？\u201d của giáo sư tâm lý học Trần Vĩnh Nghi (陳永儀). "
                        "Bà Trần đặt ra một câu hỏi khiến nhiều người phải suy nghĩ lại: "
                        "Liệu việc không có năng lượng tiêu cực có thực sự là điều tốt? "
                        "Trong cuộc sống hàng ngày, chúng ta thường được dạy rằng phải luôn vui vẻ, "
                        "phải tích cực, phải mỉm cười. Nhưng bà Trần cho rằng những cảm xúc như giận dữ, "
                        "buồn bã, sợ hãi \u2014 tất cả đều là phản ứng tự nhiên và cần thiết của con người. "
                        "Kìm nén cảm xúc không giúp bạn mạnh mẽ hơn \u2014 ngược lại, nó gây hại cho sức khỏe "
                        "cả về thể chất lẫn tinh thần. Trong buổi học đầu tiên này, bạn sẽ học 6 từ vựng "
                        "quan trọng liên quan đến chủ đề cảm xúc và tâm lý. Mỗi từ đều xuất hiện trong "
                        "bài nói chuyện và sẽ giúp bạn hiểu sâu hơn về cách người Trung Quốc nói về "
                        "thế giới nội tâm của mình. Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 1",
                "description": "Học 6 từ: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Bây giờ chúng ta sẽ cùng học 6 từ vựng đầu tiên. Mỗi từ đều gắn liền với nội dung "
                        "bài nói chuyện của giáo sư Trần Vĩnh Nghi về cảm xúc con người.\n\n"

                        "Từ đầu tiên là 情绪 (q\u00edngx\u00f9). 情绪 là danh từ, có nghĩa là \u2018cảm xúc\u2019 hoặc \u2018tâm trạng\u2019. "
                        "Đây là từ trung tâm của toàn bộ bài nói chuyện. Giáo sư Trần nói rằng mỗi người đều có "
                        "情绪, và mọi loại cảm xúc đều có giá trị. Ví dụ: 每个人都有情绪，这是很正常的 \u2014 "
                        "Mỗi người đều có cảm xúc, đây là điều rất bình thường. Trong tiếng Trung, 情 là \u2018tình cảm\u2019 "
                        "và 绪 là \u2018sợi tơ, mạch\u2019, nên 情绪 gợi lên hình ảnh những sợi tơ cảm xúc đan xen trong lòng. "
                        "Bạn có thể dùng từ này khi nói về tâm trạng hàng ngày: 今天我的情绪不太好 \u2014 "
                        "Hôm nay tâm trạng tôi không tốt lắm.\n\n"

                        "Từ thứ hai là 负面 (f\u00f9mi\u00e0n). 负面 là tính từ, có nghĩa là \u2018tiêu cực\u2019 hoặc \u2018mặt trái\u2019. "
                        "Trong bài nói chuyện, giáo sư Trần thách thức quan niệm rằng 负面情绪 \u2014 cảm xúc tiêu cực \u2014 "
                        "là xấu. Bà cho rằng xã hội đã dán nhãn sai cho nhiều cảm xúc tự nhiên. "
                        "Ví dụ: 负面情绪不一定是坏事 \u2014 Cảm xúc tiêu cực không nhất thiết là điều xấu. "
                        "负 có nghĩa là \u2018gánh, mang\u2019 và 面 là \u2018mặt, bề mặt\u2019, nên 负面 nghĩa đen là \u2018mặt gánh nặng\u2019. "
                        "Từ này thường đi kèm với 情绪, 能量 (năng lượng), hoặc 影响 (ảnh hưởng): "
                        "不要害怕负面的感觉 \u2014 Đừng sợ những cảm giác tiêu cực.\n\n"

                        "Từ thứ ba là 感觉 (g\u01cenju\u00e9). 感觉 vừa là danh từ vừa là động từ, có nghĩa là \u2018cảm giác\u2019 "
                        "hoặc \u2018cảm thấy\u2019. Đây là một trong những từ phổ biến nhất trong tiếng Trung khi nói về "
                        "trải nghiệm cá nhân. Giáo sư Trần nhấn mạnh rằng chúng ta cần lắng nghe 感觉 của mình "
                        "thay vì phớt lờ chúng. Ví dụ: 你现在有什么感觉？ \u2014 Bây giờ bạn cảm thấy thế nào? "
                        "感 là \u2018cảm\u2019 và 觉 là \u2018giác, nhận biết\u2019. Bạn sẽ gặp từ này rất nhiều trong giao tiếp hàng ngày: "
                        "我感觉今天会下雨 \u2014 Tôi cảm thấy hôm nay sẽ mưa.\n\n"

                        "Từ thứ tư là 表达 (bi\u01ceo d\u00e1). 表达 là động từ, có nghĩa là \u2018biểu đạt\u2019 hoặc \u2018thể hiện\u2019. "
                        "Một trong những thông điệp quan trọng nhất của bài nói chuyện là: hãy học cách 表达 cảm xúc "
                        "của mình. Kìm nén không phải là giải pháp \u2014 biểu đạt mới là con đường đúng. "
                        "Ví dụ: 我们应该学会表达自己的情绪 \u2014 Chúng ta nên học cách biểu đạt cảm xúc của mình. "
                        "表 là \u2018bên ngoài, biểu lộ\u2019 và 达 là \u2018đạt đến\u2019. Khi bạn 表达, bạn đang đưa những gì bên trong "
                        "ra bên ngoài. Một cách dùng khác: 他不善于表达感情 \u2014 Anh ấy không giỏi biểu đạt tình cảm.\n\n"

                        "Từ thứ năm là 压力 (y\u0101l\u00ec). 压力 là danh từ, có nghĩa là \u2018áp lực\u2019 hoặc \u2018stress\u2019. "
                        "Giáo sư Trần giải thích rằng khi chúng ta kìm nén cảm xúc, 压力 sẽ tích tụ bên trong "
                        "và cuối cùng bùng nổ theo những cách không lành mạnh. Ví dụ: 工作压力太大了，我需要休息 \u2014 "
                        "Áp lực công việc quá lớn, tôi cần nghỉ ngơi. 压 là \u2018ép, đè\u2019 và 力 là \u2018sức mạnh\u2019. "
                        "Hình ảnh rất rõ ràng: áp lực là một lực đè nén lên bạn. Từ này cực kỳ phổ biến trong "
                        "cuộc sống hiện đại: 学生的压力越来越大 \u2014 Áp lực của học sinh ngày càng lớn.\n\n"

                        "Từ cuối cùng trong buổi hôm nay là 健康 (ji\u00e0nk\u0101ng). 健康 vừa là danh từ vừa là tính từ, "
                        "có nghĩa là \u2018sức khỏe\u2019 hoặc \u2018khỏe mạnh\u2019. Giáo sư Trần kết nối cảm xúc với 健康: "
                        "việc đối mặt và chấp nhận cảm xúc giúp chúng ta sống khỏe mạnh hơn cả về thể chất lẫn "
                        "tinh thần. Ví dụ: 心理健康和身体健康一样重要 \u2014 Sức khỏe tâm lý quan trọng như sức khỏe "
                        "thể chất. 健 là \u2018mạnh khỏe\u2019 và 康 là \u2018an khang\u2019. Bạn có thể dùng từ này trong nhiều ngữ cảnh: "
                        "祝你身体健康 \u2014 Chúc bạn sức khỏe. Hoặc: 这种生活方式不健康 \u2014 Lối sống này không lành mạnh.\n\n"

                        "Vậy là bạn đã biết 6 từ đầu tiên: 情绪, 负面, 感觉, 表达, 压力, 健康. "
                        "Hãy cùng luyện tập qua các hoạt động tiếp theo nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Cảm xúc và năng lượng",
                "description": "Học 6 từ: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 1",
                "description": "Tập nói 6 từ: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 1",
                "description": "Nhận biết 6 từ: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 1",
                "description": "Ghép nghĩa 6 từ: 情绪, 负面, 感觉, 表达, 压力, 健康",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 1",
                "description": "Viết 6 từ: 情绪, 负面, 感觉, 表达, 压力, 健康",
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
                        "情绪 thường đi với các tính từ để mô tả trạng thái: 情绪很好 (tâm trạng tốt), "
                        "情绪不稳定 (tâm trạng không ổn định). Bạn cũng có thể nói 控制情绪 (kiểm soát cảm xúc) "
                        "hoặc 情绪反应 (phản ứng cảm xúc).\n\n"
                        "负面 luôn đứng trước danh từ để bổ nghĩa: 负面情绪, 负面影响 (ảnh hưởng tiêu cực), "
                        "负面消息 (tin tiêu cực). Từ đối lập là 正面 (zh\u00e8ngmi\u00e0n) \u2014 tích cực.\n\n"
                        "感觉 rất linh hoạt. Làm động từ: 我感觉很累 (Tôi cảm thấy rất mệt). "
                        "Làm danh từ: 这种感觉很奇怪 (Cảm giác này rất kỳ lạ). "
                        "Cấu trúc phổ biến: 感觉 + hình dung từ hoặc 感觉 + 像 + ...\n\n"
                        "表达 thường đi với đối tượng: 表达感情 (biểu đạt tình cảm), 表达想法 (biểu đạt suy nghĩ), "
                        "表达意见 (biểu đạt ý kiến). Cấu trúc: 用...来表达... (dùng...để biểu đạt...).\n\n"
                        "压力 có thể đi với 大 hoặc 小: 压力很大 (áp lực rất lớn), 没有压力 (không có áp lực). "
                        "Cấu trúc hay: 给...压力 (gây áp lực cho...), 减轻压力 (giảm bớt áp lực).\n\n"
                        "健康 làm tính từ: 身体很健康 (cơ thể rất khỏe mạnh). Làm danh từ: 注意健康 (chú ý sức khỏe). "
                        "Cụm từ phổ biến: 身心健康 (khỏe mạnh cả thể chất lẫn tinh thần) \u2014 đây chính là thông điệp "
                        "cốt lõi của giáo sư Trần."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 1)",
                "description": "大家好，我是陈永仪。今天我想跟大家聊一个话题：负面情绪真的是坏事吗？",
                "practiceMinutes": 9,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 1)",
                "description": "Luyện nói theo đoạn trích về cảm xúc tiêu cực",
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
                "title": "Viết: Cảm xúc và năng lượng",
                "description": "Viết câu sử dụng 6 từ vựng buổi 1",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "情绪",
                            "prompt": (
                                "Sử dụng từ \u2018情绪\u2019 (q\u00edngx\u00f9) để nói về tâm trạng hoặc cảm xúc của bạn \u2014 "
                                "như giáo sư Trần nói rằng mọi loại cảm xúc đều có giá trị và cần được lắng nghe. "
                                "Ví dụ: 每个人都有情绪，我们不应该害怕自己的情绪。"
                            ),
                        },
                        {
                            "targetVocab": "负面",
                            "prompt": (
                                "Sử dụng từ \u2018负面\u2019 (f\u00f9mi\u00e0n) để nói về điều gì đó tiêu cực \u2014 "
                                "như bài nói chuyện thách thức quan niệm rằng cảm xúc tiêu cực luôn là xấu. "
                                "Ví dụ: 负面情绪并不可怕，可怕的是我们不敢面对它。"
                            ),
                        },
                        {
                            "targetVocab": "感觉",
                            "prompt": (
                                "Sử dụng từ \u2018感觉\u2019 (g\u01cenju\u00e9) để mô tả một cảm giác hoặc trải nghiệm \u2014 "
                                "như giáo sư Trần khuyên chúng ta hãy lắng nghe cảm giác thay vì phớt lờ chúng. "
                                "Ví dụ: 我感觉今天的天气让人心情很好。"
                            ),
                        },
                        {
                            "targetVocab": "表达",
                            "prompt": (
                                "Sử dụng từ \u2018表达\u2019 (bi\u01ceod\u00e1) để nói về việc thể hiện suy nghĩ hoặc cảm xúc \u2014 "
                                "như bài nói chuyện nhấn mạnh rằng biểu đạt cảm xúc tốt hơn kìm nén. "
                                "Ví dụ: 学会表达自己的想法是一件很重要的事情。"
                            ),
                        },
                        {
                            "targetVocab": "压力",
                            "prompt": (
                                "Sử dụng từ \u2018压力\u2019 (y\u0101l\u00ec) để nói về áp lực trong cuộc sống \u2014 "
                                "như giáo sư Trần giải thích rằng kìm nén cảm xúc khiến áp lực tích tụ. "
                                "Ví dụ: 现在年轻人的工作压力越来越大，需要学会放松。"
                            ),
                        },
                        {
                            "targetVocab": "健康",
                            "prompt": (
                                "Sử dụng từ \u2018健康\u2019 (ji\u00e0nk\u0101ng) để nói về sức khỏe thể chất hoặc tinh thần \u2014 "
                                "như bài nói chuyện kết nối việc đối mặt cảm xúc với sức khỏe tổng thể. "
                                "Ví dụ: 心理健康和身体健康一样重要，我们都应该重视。"
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
        "title": "Buổi 2: Đối mặt và chấp nhận \u2014 面对与接受",
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
                        "quan trọng: 情绪 (cảm xúc), 负面 (tiêu cực), 感觉 (cảm giác), 表达 (biểu đạt), "
                        "压力 (áp lực), và 健康 (sức khỏe). Bạn còn nhớ không? Giáo sư Trần Vĩnh Nghi đã "
                        "đặt câu hỏi: liệu việc không có cảm xúc tiêu cực có thực sự tốt? "
                        "Hôm nay chúng ta sẽ đi sâu hơn vào phần tiếp theo của bài nói chuyện, "
                        "nơi bà Trần nói về việc đối mặt với cảm xúc thay vì chạy trốn. "
                        "Bạn sẽ học thêm 6 từ mới liên quan đến sự chấp nhận, ảnh hưởng, "
                        "và lòng dũng cảm. Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 2",
                "description": "Học 6 từ: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng mới của buổi hôm nay. Những từ này nằm ở phần giữa "
                        "bài nói chuyện, khi giáo sư Trần bắt đầu đưa ra giải pháp cho vấn đề kìm nén cảm xúc.\n\n"

                        "Từ đầu tiên là 接受 (ji\u0113sh\u00f2u). 接受 là động từ, có nghĩa là \u2018chấp nhận\u2019 hoặc \u2018tiếp nhận\u2019. "
                        "Đây là từ khóa quan trọng nhất trong phần này của bài nói chuyện. Giáo sư Trần nói rằng "
                        "bước đầu tiên để sống khỏe mạnh về mặt cảm xúc là 接受 \u2014 chấp nhận rằng bạn đang buồn, "
                        "đang giận, đang sợ. Không phải chống lại, mà là đón nhận. "
                        "Ví dụ: 我们要学会接受自己的不完美 \u2014 Chúng ta cần học cách chấp nhận sự không hoàn hảo "
                        "của bản thân. 接 là \u2018đón, nhận\u2019 và 受 là \u2018chịu, nhận\u2019. Khi bạn 接受, bạn mở lòng đón nhận "
                        "thay vì đẩy đi. Cách dùng khác: 他终于接受了这个事实 \u2014 Anh ấy cuối cùng đã chấp nhận "
                        "sự thật này.\n\n"

                        "Từ thứ hai là 影响 (y\u01d0ngxi\u01ceng). 影响 vừa là danh từ vừa là động từ, có nghĩa là "
                        "\u2018ảnh hưởng\u2019. Giáo sư Trần giải thích rằng cảm xúc bị kìm nén sẽ 影响 đến mọi khía cạnh "
                        "của cuộc sống \u2014 từ các mối quan hệ đến sức khỏe thể chất. "
                        "Ví dụ: 情绪会影响我们的身体健康 \u2014 Cảm xúc sẽ ảnh hưởng đến sức khỏe thể chất của chúng ta. "
                        "影 là \u2018bóng\u2019 và 响 là \u2018vang, tiếng vọng\u2019. Ảnh hưởng giống như cái bóng \u2014 bạn không thấy rõ "
                        "nhưng nó luôn ở đó. Cấu trúc phổ biến: 对...有影响 (có ảnh hưởng đến...), "
                        "受到...的影响 (chịu ảnh hưởng của...).\n\n"

                        "Từ thứ ba là 控制 (k\u00f2ngzh\u00ec). 控制 là động từ, có nghĩa là \u2018kiểm soát\u2019 hoặc \u2018khống chế\u2019. "
                        "Nhiều người nghĩ rằng 控制情绪 \u2014 kiểm soát cảm xúc \u2014 có nghĩa là kìm nén chúng. "
                        "Nhưng giáo sư Trần cho rằng kiểm soát thực sự là hiểu và điều hướng cảm xúc, "
                        "không phải đè nén. Ví dụ: 控制情绪不是压抑情绪，而是理解情绪 \u2014 Kiểm soát cảm xúc "
                        "không phải là đè nén cảm xúc, mà là hiểu cảm xúc. 控 là \u2018nắm giữ\u2019 và 制 là \u2018chế ngự\u2019. "
                        "Cách dùng khác: 他很难控制自己的脾气 \u2014 Anh ấy rất khó kiểm soát tính nóng của mình.\n\n"

                        "Từ thứ tư là 内心 (n\u00e8ix\u012bn). 内心 là danh từ, có nghĩa là \u2018nội tâm\u2019 hoặc \u2018trong lòng\u2019. "
                        "Giáo sư Trần khuyến khích mọi người nhìn vào 内心 của mình \u2014 lắng nghe tiếng nói bên trong "
                        "thay vì chỉ nghe theo kỳ vọng của xã hội. Ví dụ: 我们应该倾听自己内心的声音 \u2014 "
                        "Chúng ta nên lắng nghe tiếng nói nội tâm của mình. 内 là \u2018bên trong\u2019 và 心 là \u2018trái tim\u2019. "
                        "内心 là thế giới bên trong trái tim bạn. Cách dùng: 他内心其实很善良 \u2014 "
                        "Nội tâm anh ấy thực ra rất lương thiện.\n\n"

                        "Từ thứ năm là 勇气 (y\u01d2ngq\u00ec). 勇气 là danh từ, có nghĩa là \u2018dũng khí\u2019 hoặc \u2018lòng can đảm\u2019. "
                        "Để đối mặt với cảm xúc của mình, bạn cần 勇气. Thừa nhận rằng mình đang buồn, "
                        "đang sợ \u2014 đó không phải là yếu đuối, mà là dũng cảm. "
                        "Ví dụ: 承认自己的弱点需要很大的勇气 \u2014 Thừa nhận điểm yếu của mình cần rất nhiều dũng khí. "
                        "勇 là \u2018dũng cảm\u2019 và 气 là \u2018khí, tinh thần\u2019. Cách dùng: 你要有勇气面对困难 \u2014 "
                        "Bạn cần có dũng khí đối mặt với khó khăn.\n\n"

                        "Từ cuối cùng là 害怕 (h\u00e0ip\u00e0). 害怕 là động từ, có nghĩa là \u2018sợ hãi\u2019 hoặc \u2018lo sợ\u2019. "
                        "Giáo sư Trần nói rằng 害怕 là một trong những cảm xúc bị hiểu lầm nhiều nhất. "
                        "Sợ hãi không có nghĩa là yếu đuối \u2014 nó là tín hiệu cảnh báo giúp bạn tránh nguy hiểm. "
                        "Ví dụ: 不要害怕犯错，犯错是学习的一部分 \u2014 Đừng sợ mắc lỗi, mắc lỗi là một phần "
                        "của việc học. 害 là \u2018hại, gây hại\u2019 và 怕 là \u2018sợ\u2019. Cách dùng: 小孩子害怕黑暗是很正常的 \u2014 "
                        "Trẻ con sợ bóng tối là rất bình thường.\n\n"

                        "Vậy là bạn đã học thêm 6 từ mới: 接受, 影响, 控制, 内心, 勇气, 害怕. "
                        "Cùng với 6 từ buổi trước, bạn đã có 12 từ vựng rồi! Hãy luyện tập tiếp nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Đối mặt và chấp nhận",
                "description": "Học 6 từ: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 2",
                "description": "Tập nói 6 từ: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 2",
                "description": "Nhận biết 6 từ: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 2",
                "description": "Ghép nghĩa 6 từ: 接受, 影响, 控制, 内心, 勇气, 害怕",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 2",
                "description": "Viết 6 từ: 接受, 影响, 控制, 内心, 勇气, 害怕",
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
                        "接受 thường đi với danh từ: 接受现实 (chấp nhận thực tế), 接受批评 (chấp nhận phê bình), "
                        "接受邀请 (nhận lời mời). Cấu trúc phủ định: 无法接受 (không thể chấp nhận), "
                        "难以接受 (khó chấp nhận).\n\n"
                        "影响 có hai cách dùng chính. Làm động từ: 这件事影响了我的心情 (Việc này ảnh hưởng đến "
                        "tâm trạng tôi). Làm danh từ: 他对我有很大的影响 (Anh ấy có ảnh hưởng lớn đến tôi).\n\n"
                        "控制 thường đi với đối tượng cụ thể: 控制情绪, 控制体重 (kiểm soát cân nặng), "
                        "控制时间 (kiểm soát thời gian). Cấu trúc bị động: 被...控制 (bị...kiểm soát).\n\n"
                        "内心 thường đứng trước danh từ hoặc tính từ: 内心世界 (thế giới nội tâm), "
                        "内心深处 (sâu thẳm trong lòng), 内心强大 (nội tâm mạnh mẽ).\n\n"
                        "勇气 thường đi với 有 hoặc 没有: 有勇气 (có dũng khí), 没有勇气 (không có dũng khí). "
                        "Cấu trúc: 鼓起勇气 (lấy hết dũng khí), 需要勇气 (cần dũng khí).\n\n"
                        "害怕 có thể đi với danh từ hoặc động từ: 害怕失败 (sợ thất bại), 害怕孤独 (sợ cô đơn), "
                        "害怕被拒绝 (sợ bị từ chối). Cấu trúc: 不要害怕 + động từ (đừng sợ + động từ)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 2)",
                "description": "所以，我们应该怎么做呢？第一步，就是接受。接受你现在的感觉。",
                "practiceMinutes": 9,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 2)",
                "description": "Luyện nói theo đoạn trích về việc chấp nhận cảm xúc",
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
                "title": "Viết: Đối mặt và chấp nhận",
                "description": "Viết câu sử dụng 6 từ vựng buổi 2",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "接受",
                            "prompt": (
                                "Sử dụng từ \u2018接受\u2019 (ji\u0113sh\u00f2u) để nói về việc chấp nhận một điều gì đó \u2014 "
                                "như giáo sư Trần nói rằng bước đầu tiên là chấp nhận cảm xúc của mình. "
                                "Ví dụ: 接受自己的缺点是成长的第一步。"
                            ),
                        },
                        {
                            "targetVocab": "影响",
                            "prompt": (
                                "Sử dụng từ \u2018影响\u2019 (y\u01d0ngxi\u01ceng) để nói về sự ảnh hưởng \u2014 "
                                "như bài nói chuyện giải thích rằng cảm xúc bị kìm nén ảnh hưởng đến sức khỏe. "
                                "Ví dụ: 父母的教育方式会影响孩子的一生。"
                            ),
                        },
                        {
                            "targetVocab": "控制",
                            "prompt": (
                                "Sử dụng từ \u2018控制\u2019 (k\u00f2ngzh\u00ec) để nói về việc kiểm soát \u2014 "
                                "như giáo sư Trần phân biệt giữa kiểm soát cảm xúc và kìm nén cảm xúc. "
                                "Ví dụ: 学会控制自己的情绪是一种很重要的能力。"
                            ),
                        },
                        {
                            "targetVocab": "内心",
                            "prompt": (
                                "Sử dụng từ \u2018内心\u2019 (n\u00e8ix\u012bn) để nói về thế giới nội tâm \u2014 "
                                "như bài nói chuyện khuyến khích lắng nghe tiếng nói bên trong. "
                                "Ví dụ: 虽然他看起来很开心，但内心其实很孤独。"
                            ),
                        },
                        {
                            "targetVocab": "勇气",
                            "prompt": (
                                "Sử dụng từ \u2018勇气\u2019 (y\u01d2ngq\u00ec) để nói về lòng dũng cảm \u2014 "
                                "như giáo sư Trần nói rằng thừa nhận cảm xúc cần rất nhiều dũng khí. "
                                "Ví dụ: 说出自己的真实感受需要很大的勇气。"
                            ),
                        },
                        {
                            "targetVocab": "害怕",
                            "prompt": (
                                "Sử dụng từ \u2018害怕\u2019 (h\u00e0ip\u00e0) để nói về nỗi sợ \u2014 "
                                "như bài nói chuyện giải thích rằng sợ hãi là tín hiệu cảnh báo tự nhiên. "
                                "Ví dụ: 每个人都会害怕，重要的是不要让害怕控制你。"
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
        "title": "Buổi 3: Sức mạnh của cảm xúc — 情绪的力量",
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
                        "Qua hai buổi trước, bạn đã học 12 từ vựng: 情绪, 负面, 感觉, 表达, 压力, 健康 "
                        "ở buổi 1, và 接受, 影响, 控制, 内心, 勇气, 害怕 ở buổi 2. "
                        "Bạn đã hiểu rằng giáo sư Trần Vĩnh Nghi muốn chúng ta ngừng kìm nén cảm xúc "
                        "và bắt đầu chấp nhận chúng. Hôm nay, chúng ta sẽ đi vào phần cuối của bài nói chuyện, "
                        "nơi bà Trần giải thích tại sao mỗi loại cảm xúc — kể cả giận dữ và buồn bã — "
                        "đều mang trong mình sức mạnh giúp chúng ta trưởng thành. "
                        "6 từ vựng cuối cùng sẽ giúp bạn nói về những trải nghiệm sâu sắc nhất "
                        "trong cuộc sống. Hãy bắt đầu nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 3",
                "description": "Học 6 từ: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng cuối cùng. Đây là những từ nằm ở phần kết của bài nói chuyện, "
                        "khi giáo sư Trần đưa ra thông điệp mạnh mẽ nhất: mỗi cảm xúc đều là sức mạnh.\n\n"

                        "Từ đầu tiên là 愤怒 (fènnù). 愤怒 là danh từ và tính từ, có nghĩa là 'giận dữ' "
                        "hoặc 'phẫn nộ'. Đây là một trong những cảm xúc bị coi là 'xấu' nhất trong xã hội. "
                        "Nhưng giáo sư Trần giải thích rằng 愤怒 có vai trò quan trọng: nó cho bạn biết "
                        "khi nào ai đó đã vượt qua giới hạn của bạn. Ví dụ: 愤怒告诉你：有人越过了你的底线 — "
                        "Giận dữ cho bạn biết: có người đã vượt qua giới hạn của bạn. "
                        "愤 là 'phẫn, bất bình' và 怒 là 'nộ, giận'. Hai chữ kết hợp tạo nên một cảm xúc "
                        "mãnh liệt. Cách dùng khác: 他非常愤怒，因为被朋友欺骗了 — Anh ấy rất giận dữ "
                        "vì bị bạn bè lừa dối. Bạn cũng có thể nói: 愤怒是一种正常的情绪 — "
                        "Giận dữ là một loại cảm xúc bình thường.\n\n"

                        "Từ thứ hai là 悲伤 (bēishāng). 悲伤 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "'buồn bã' hoặc 'đau buồn'. Giáo sư Trần nói rằng 悲伤 cho bạn biết bạn đã mất đi "
                        "điều gì đó quan trọng — và chính sự buồn bã đó dạy bạn biết trân trọng. "
                        "Ví dụ: 悲伤告诉你：你失去了重要的东西 — Buồn bã cho bạn biết: bạn đã mất đi "
                        "điều quan trọng. 悲 là 'bi, buồn' và 伤 là 'thương, đau'. "
                        "Cách dùng: 失去亲人的悲伤是很难用语言表达的 — Nỗi buồn mất người thân "
                        "rất khó diễn tả bằng lời. Hoặc: 她的眼神里充满了悲伤 — "
                        "Ánh mắt cô ấy tràn đầy nỗi buồn.\n\n"

                        "Từ thứ ba là 理解 (lǐjiě). 理解 là động từ, có nghĩa là 'hiểu' hoặc 'thông cảm'. "
                        "Đây là một từ rất quan trọng trong bài nói chuyện. Giáo sư Trần nhấn mạnh rằng "
                        "để kiểm soát cảm xúc thực sự, bạn cần 理解 — hiểu tại sao mình có cảm xúc đó. "
                        "Không phải đè nén, mà là thấu hiểu. Ví dụ: 理解自己的情绪是控制情绪的第一步 — "
                        "Hiểu cảm xúc của mình là bước đầu tiên để kiểm soát cảm xúc. "
                        "理 là 'lý, đạo lý' và 解 là 'giải, tháo gỡ'. Khi bạn 理解, bạn đang dùng lý trí "
                        "để tháo gỡ những điều phức tạp. Cách dùng: 我理解你的感受 — Tôi hiểu cảm giác "
                        "của bạn. Hoặc: 这个问题很难理解 — Vấn đề này rất khó hiểu.\n\n"

                        "Từ thứ tư là 成长 (chéngzhǎng). 成长 là động từ và danh từ, có nghĩa là "
                        "'trưởng thành' hoặc 'lớn lên'. Giáo sư Trần kết luận rằng mỗi cảm xúc — "
                        "kể cả những cảm xúc đau đớn nhất — đều là cơ hội để 成长. "
                        "Khi bạn trải qua giận dữ, bạn học được thế nào là công bằng. "
                        "Khi bạn trải qua buồn bã, bạn học được thế nào là trân trọng. "
                        "Ví dụ: 每一种情绪都是成长的力量 — Mỗi loại cảm xúc đều là sức mạnh của sự trưởng thành. "
                        "成 là 'thành, hoàn thành' và 长 là 'trưởng, lớn'. Cách dùng: "
                        "孩子在困难中成长 — Trẻ con trưởng thành trong khó khăn. "
                        "Hoặc: 这段经历让我成长了很多 — Trải nghiệm này giúp tôi trưởng thành rất nhiều.\n\n"

                        "Từ thứ năm là 经历 (jīnglì). 经历 vừa là động từ vừa là danh từ, có nghĩa là "
                        "'trải nghiệm' hoặc 'kinh nghiệm'. Giáo sư Trần nói rằng tất cả cảm xúc đều là "
                        "một phần của 经历 cuộc sống. Khi bạn 经历 giận dữ, buồn bã, sợ hãi — "
                        "bạn đang sống một cuộc đời trọn vẹn. Ví dụ: 所有的情绪都是我们生命经历的一部分 — "
                        "Tất cả cảm xúc đều là một phần trải nghiệm cuộc sống của chúng ta. "
                        "经 là 'kinh, trải qua' và 历 là 'lịch, trải'. Cách dùng: "
                        "他有很丰富的工作经历 — Anh ấy có kinh nghiệm làm việc rất phong phú. "
                        "Hoặc: 我从来没有经历过这样的事情 — Tôi chưa bao giờ trải qua chuyện như vậy.\n\n"

                        "Từ cuối cùng là 力量 (lìliàng). 力量 là danh từ, có nghĩa là 'sức mạnh' hoặc "
                        "'lực lượng'. Đây là từ kết thúc bài nói chuyện. Giáo sư Trần nói: "
                        "你的情绪就是你的力量 — Cảm xúc của bạn chính là sức mạnh của bạn. "
                        "Thông điệp cuối cùng rất rõ ràng: đừng sợ cảm xúc, hãy biến chúng thành 力量. "
                        "力 là 'lực' và 量 là 'lượng, khối lượng'. Cách dùng: "
                        "知识就是力量 — Kiến thức là sức mạnh. Hoặc: "
                        "团结的力量是无穷的 — Sức mạnh đoàn kết là vô tận.\n\n"

                        "Tuyệt vời! Bạn đã học xong toàn bộ 18 từ vựng: 情绪, 负面, 感觉, 表达, 压力, 健康, "
                        "接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量. "
                        "Hãy luyện tập qua các hoạt động tiếp theo!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Sức mạnh của cảm xúc",
                "description": "Học 6 từ: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 3",
                "description": "Tập nói 6 từ: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 3",
                "description": "Nhận biết 6 từ: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 3",
                "description": "Ghép nghĩa 6 từ: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 3",
                "description": "Viết 6 từ: 愤怒, 悲伤, 理解, 成长, 经历, 力量",
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
                        "愤怒 thường đi với 感到 hoặc 非常: 感到愤怒 (cảm thấy giận dữ), "
                        "非常愤怒 (rất giận dữ). Cấu trúc: 对...感到愤怒 (giận dữ về...). "
                        "Từ đồng nghĩa nhẹ hơn là 生气 (shēngqì).\n\n"
                        "悲伤 thường đi với 感到 hoặc 充满: 感到悲伤 (cảm thấy buồn bã), "
                        "充满悲伤 (tràn đầy nỗi buồn). Cấu trúc: 为...感到悲伤 (buồn vì...). "
                        "Từ đồng nghĩa nhẹ hơn là 难过 (nánguò).\n\n"
                        "理解 có thể đi với người hoặc sự việc: 理解你 (hiểu bạn), "
                        "理解这个问题 (hiểu vấn đề này). Cấu trúc phủ định: 无法理解 (không thể hiểu), "
                        "难以理解 (khó hiểu). Cấu trúc hay: 互相理解 (hiểu nhau).\n\n"
                        "成长 thường đi với 在...中: 在困难中成长 (trưởng thành trong khó khăn), "
                        "在经历中成长 (trưởng thành qua trải nghiệm). Làm danh từ: 个人成长 (sự trưởng thành cá nhân).\n\n"
                        "经历 làm động từ: 经历困难 (trải qua khó khăn), 经历失败 (trải qua thất bại). "
                        "Làm danh từ: 人生经历 (trải nghiệm cuộc đời), 工作经历 (kinh nghiệm làm việc). "
                        "Cấu trúc: 经历过...才知道... (trải qua...mới biết...).\n\n"
                        "力量 thường đi với 有 hoặc tính từ: 有力量 (có sức mạnh), "
                        "强大的力量 (sức mạnh to lớn). Cấu trúc hay: 给...力量 (cho...sức mạnh), "
                        "力量来自... (sức mạnh đến từ...). Cụm từ nổi tiếng: 知识就是力量 (kiến thức là sức mạnh)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 3)",
                "description": "愤怒、悲伤、害怕——这些情绪都有它们存在的理由。",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 3)",
                "description": "Luyện nói theo đoạn trích về sức mạnh của cảm xúc",
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
                "title": "Viết: Sức mạnh của cảm xúc",
                "description": "Viết câu sử dụng 6 từ vựng buổi 3",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "愤怒",
                            "prompt": (
                                "Sử dụng từ '愤怒' (fènnù) để nói về sự giận dữ — "
                                "như giáo sư Trần giải thích rằng giận dữ cho bạn biết ai đó đã vượt qua giới hạn. "
                                "Ví dụ: 当看到不公平的事情时，我们会感到愤怒。"
                            ),
                        },
                        {
                            "targetVocab": "悲伤",
                            "prompt": (
                                "Sử dụng từ '悲伤' (bēishāng) để nói về nỗi buồn — "
                                "như bài nói chuyện giải thích rằng buồn bã dạy chúng ta biết trân trọng. "
                                "Ví dụ: 悲伤是一种很深的情绪，它让我们学会珍惜。"
                            ),
                        },
                        {
                            "targetVocab": "理解",
                            "prompt": (
                                "Sử dụng từ '理解' (lǐjiě) để nói về sự thấu hiểu — "
                                "như giáo sư Trần nhấn mạnh rằng hiểu cảm xúc là bước đầu tiên để kiểm soát chúng. "
                                "Ví dụ: 只有理解别人的感受，我们才能建立真正的友谊。"
                            ),
                        },
                        {
                            "targetVocab": "成长",
                            "prompt": (
                                "Sử dụng từ '成长' (chéngzhǎng) để nói về sự trưởng thành — "
                                "như bài nói chuyện kết luận rằng mỗi cảm xúc đều là cơ hội để trưởng thành. "
                                "Ví dụ: 每一次失败都是成长的机会，不要害怕犯错。"
                            ),
                        },
                        {
                            "targetVocab": "经历",
                            "prompt": (
                                "Sử dụng từ '经历' (jīnglì) để nói về một trải nghiệm — "
                                "như giáo sư Trần nói rằng tất cả cảm xúc đều là một phần trải nghiệm cuộc sống. "
                                "Ví dụ: 这次旅行是我人生中最难忘的经历之一。"
                            ),
                        },
                        {
                            "targetVocab": "力量",
                            "prompt": (
                                "Sử dụng từ '力量' (lìliàng) để nói về sức mạnh — "
                                "như bài nói chuyện kết thúc với thông điệp: cảm xúc chính là sức mạnh của bạn. "
                                "Ví dụ: 爱是世界上最强大的力量，它可以改变一切。"
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
                        "về chủ đề cảm xúc và tâm lý. Hãy cùng ôn lại nhé!\n\n"
                        "Buổi 1, bạn đã học: 情绪 (cảm xúc), 负面 (tiêu cực), 感觉 (cảm giác), "
                        "表达 (biểu đạt), 压力 (áp lực), 健康 (sức khỏe). Đây là những từ nền tảng "
                        "giúp bạn nói về thế giới cảm xúc bên trong.\n\n"
                        "Buổi 2, bạn đã học: 接受 (chấp nhận), 影响 (ảnh hưởng), 控制 (kiểm soát), "
                        "内心 (nội tâm), 勇气 (dũng khí), 害怕 (sợ hãi). Những từ này giúp bạn nói về "
                        "cách đối mặt và xử lý cảm xúc.\n\n"
                        "Buổi 3, bạn đã học: 愤怒 (giận dữ), 悲伤 (buồn bã), 理解 (hiểu), "
                        "成长 (trưởng thành), 经历 (trải nghiệm), 力量 (sức mạnh). Đây là những từ "
                        "giúp bạn hiểu rằng mỗi cảm xúc đều có giá trị.\n\n"
                        "Bây giờ hãy ôn tập toàn bộ 18 từ qua các hoạt động flashcard!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập toàn bộ 18 từ vựng",
                "description": "Ôn tập 18 từ: 情绪, 负面, 感觉, 表达, 压力, 健康, 接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói toàn bộ 18 từ vựng",
                "description": "Tập nói 18 từ: 情绪, 负面, 感觉, 表达, 压力, 健康, 接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết toàn bộ từ vựng",
                "description": "Nhận biết 18 từ: 情绪, 负面, 感觉, 表达, 压力, 健康, 接受, 影响, 控制, 内心, 勇气, 害怕, 愤怒, 悲伤, 理解, 成长, 经历, 力量",
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
                        "của giáo sư Trần Vĩnh Nghi từ đầu đến cuối. Bạn đã học 18 từ vựng qua 3 buổi học "
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
                "description": "大家好，我是陈永仪。今天我想跟大家聊一个话题：负面情绪真的是坏事吗？",
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

                        "情绪 (qíngxù) — cảm xúc, tâm trạng. Ví dụ: 学会管理自己的情绪是一种智慧 — "
                        "Học cách quản lý cảm xúc của mình là một loại trí tuệ.\n\n"

                        "负面 (fùmiàn) — tiêu cực, mặt trái. Ví dụ: 不要只看到事情的负面 — "
                        "Đừng chỉ nhìn thấy mặt tiêu cực của sự việc.\n\n"

                        "感觉 (gǎnjué) — cảm giác, cảm thấy. Ví dụ: 相信你自己的感觉 — "
                        "Hãy tin vào cảm giác của chính mình.\n\n"

                        "表达 (biǎodá) — biểu đạt, thể hiện. Ví dụ: 音乐是一种美丽的表达方式 — "
                        "Âm nhạc là một cách biểu đạt tuyệt đẹp.\n\n"

                        "压力 (yālì) — áp lực, stress. Ví dụ: 适当的压力可以让人进步 — "
                        "Áp lực vừa phải có thể giúp người ta tiến bộ.\n\n"

                        "健康 (jiànkāng) — sức khỏe, khỏe mạnh. Ví dụ: 快乐是最好的健康秘诀 — "
                        "Vui vẻ là bí quyết sức khỏe tốt nhất.\n\n"

                        "接受 (jiēshòu) — chấp nhận, tiếp nhận. Ví dụ: 接受不完美，才能找到真正的幸福 — "
                        "Chấp nhận sự không hoàn hảo mới có thể tìm thấy hạnh phúc thực sự.\n\n"

                        "影响 (yǐngxiǎng) — ảnh hưởng. Ví dụ: 好朋友会给你正面的影响 — "
                        "Bạn tốt sẽ mang đến cho bạn ảnh hưởng tích cực.\n\n"

                        "控制 (kòngzhì) — kiểm soát, khống chế. Ví dụ: 深呼吸可以帮助你控制情绪 — "
                        "Hít thở sâu có thể giúp bạn kiểm soát cảm xúc.\n\n"

                        "内心 (nèixīn) — nội tâm, trong lòng. Ví dụ: 跟随你内心的声音 — "
                        "Hãy đi theo tiếng nói nội tâm của bạn.\n\n"

                        "勇气 (yǒngqì) — dũng khí, lòng can đảm. Ví dụ: 做自己需要最大的勇气 — "
                        "Làm chính mình cần dũng khí lớn nhất.\n\n"

                        "害怕 (hàipà) — sợ hãi, lo sợ. Ví dụ: 害怕是正常的，勇敢是选择 — "
                        "Sợ hãi là bình thường, dũng cảm là sự lựa chọn.\n\n"

                        "愤怒 (fènnù) — giận dữ, phẫn nộ. Ví dụ: 愤怒的时候，先冷静再说话 — "
                        "Khi giận dữ, hãy bình tĩnh trước rồi mới nói.\n\n"

                        "悲伤 (bēishāng) — buồn bã, đau buồn. Ví dụ: 悲伤过后，阳光总会来 — "
                        "Sau nỗi buồn, ánh nắng sẽ luôn đến.\n\n"

                        "理解 (lǐjiě) — hiểu, thông cảm. Ví dụ: 世界需要更多的理解和包容 — "
                        "Thế giới cần nhiều sự thấu hiểu và bao dung hơn.\n\n"

                        "成长 (chéngzhǎng) — trưởng thành, lớn lên. Ví dụ: 每一天都是成长的机会 — "
                        "Mỗi ngày đều là cơ hội để trưởng thành.\n\n"

                        "经历 (jīnglì) — trải nghiệm, kinh nghiệm. Ví dụ: 感谢所有的经历，它们让我变得更强 — "
                        "Cảm ơn tất cả trải nghiệm, chúng giúp tôi trở nên mạnh mẽ hơn.\n\n"

                        "力量 (lìliàng) — sức mạnh, lực lượng. Ví dụ: 你比你想象的更有力量 — "
                        "Bạn mạnh mẽ hơn bạn tưởng.\n\n"

                        "Như giáo sư Trần Vĩnh Nghi đã nói: 你的情绪就是你的力量 — "
                        "Cảm xúc của bạn chính là sức mạnh của bạn. "
                        "Bạn đã không chỉ học được 18 từ vựng tiếng Trung, mà còn hiểu sâu hơn "
                        "về cách đối mặt với cảm xúc của mình. Hãy nhớ: đừng sợ cảm xúc, "
                        "hãy biến chúng thành sức mạnh. Cảm ơn bạn đã đồng hành, "
                        "và chúc bạn luôn khỏe mạnh cả về thể chất lẫn tinh thần! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Học Qua Podcast: '沒有負面能量是好事嗎？' — 陳永儀 (Cảm xúc tiêu cực có thực sự xấu?)",
        "description": (
            "BẠN CÓ ĐANG CỐ TỎ RA MẠNH MẼ BẰNG CÁCH KÌM NÉN MỌI CẢM XÚC?\n\n"
            "Mỗi lần bạn nuốt nước mắt, mỗi lần bạn giấu đi cơn giận, mỗi lần bạn nói "
            "'tôi ổn' trong khi lòng đang tan nát — bạn đang tự đầu độc chính mình. "
            "Không phải ẩn dụ. Nghiên cứu khoa học cho thấy kìm nén cảm xúc lâu dài "
            "phá hủy hệ miễn dịch, tăng nguy cơ bệnh tim, và đẩy bạn vào vòng xoáy "
            "stress không lối thoát.\n\n"
            "Giáo sư tâm lý học Trần Vĩnh Nghi (陳永儀) từ TEDxTaipei sẽ lật ngược "
            "mọi thứ bạn từng tin: cảm xúc tiêu cực không phải kẻ thù — chúng là "
            "hệ thống cảnh báo tinh vi nhất mà cơ thể bạn sở hữu. Giận dữ cho bạn biết "
            "ai đó đã vượt qua giới hạn. Buồn bã dạy bạn biết trân trọng. Sợ hãi "
            "bảo vệ bạn khỏi nguy hiểm.\n\n"
            "Khi bạn có dũng khí đối mặt với nội tâm thay vì chạy trốn, bạn không chỉ "
            "sống khỏe mạnh hơn — bạn đang thực sự trưởng thành.\n\n"
            "Học 18 từ vựng đắt giá về cảm xúc và tâm lý cùng trải nghiệm đa giác quan "
            "giúp bạn vừa nâng cấp tư duy, vừa nâng trình tiếng Trung một cách vượt bậc."
        ),
        "preview": {
            "text": (
                "Bạn có biết rằng mỗi lần bạn kìm nén cảm xúc, cơ thể bạn đang trả giá? "
                "Giáo sư tâm lý học Trần Vĩnh Nghi từ TEDxTaipei sẽ thay đổi hoàn toàn cách bạn "
                "nhìn nhận giận dữ, buồn bã và sợ hãi. Trong khóa học này, bạn sẽ học 18 từ vựng "
                "tiếng Trung cấp độ HSK2-HSK3 về cảm xúc và tâm lý: 情绪 (cảm xúc), 负面 (tiêu cực), "
                "感觉 (cảm giác), 表达 (biểu đạt), 压力 (áp lực), 健康 (sức khỏe), 接受 (chấp nhận), "
                "影响 (ảnh hưởng), 控制 (kiểm soát), 内心 (nội tâm), 勇气 (dũng khí), 害怕 (sợ hãi), "
                "愤怒 (giận dữ), 悲伤 (buồn bã), 理解 (hiểu), 成长 (trưởng thành), 经历 (trải nghiệm), "
                "力量 (sức mạnh). Qua 5 buổi học với flashcard, bài đọc, luyện nói và viết câu, "
                "bạn sẽ không chỉ nắm vững từ vựng mà còn hiểu sâu hơn về cách người Trung Quốc "
                "nói về thế giới nội tâm — và biến cảm xúc thành sức mạnh thực sự của mình."
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
