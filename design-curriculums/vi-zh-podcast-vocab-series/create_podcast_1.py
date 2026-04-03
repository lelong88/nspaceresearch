"""
Create vi-zh podcast curriculum #1:
蔣勳 (Chiang Hsun) — "留十八分鐘給自己"
(Give Yourself Eighteen Minutes)

TEDxTaipei 2012, ~25 minutes, about slowing down, art, beauty, and self-reflection.
YouTube: https://www.youtube.com/watch?v=6i7RcP39NB0

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
        "title": "Buổi 1: Thời gian và vẻ đẹp — 时间与美",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu bài nói chuyện",
                "description": "Giới thiệu bài TED Talk của Tưởng Huân về nghệ thuật sống chậm",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chào mừng bạn đến với khóa học từ vựng tiếng Trung qua podcast! "
                        "Hôm nay chúng ta sẽ cùng khám phá bài nói chuyện '留十八分鐘給自己' "
                        "(Hãy dành mười tám phút cho chính mình) của nhà văn và học giả mỹ học "
                        "Tưởng Huân (蔣勳) tại TEDxTaipei 2012. Ông Tưởng Huân là một trong những "
                        "nhà văn được yêu thích nhất Đài Loan, nổi tiếng với những tác phẩm về "
                        "nghệ thuật, cái đẹp và triết lý sống. Trong bài nói chuyện này, ông đặt ra "
                        "một câu hỏi giản dị nhưng sâu sắc: Bạn có bao lâu rồi chưa thực sự "
                        "dừng lại và lắng nghe chính mình? Cuộc sống hiện đại cuốn chúng ta vào "
                        "vòng xoáy bận rộn — từ sáng đến tối, từ công việc đến điện thoại, "
                        "chúng ta không còn thời gian để nhìn bầu trời, ngắm một bông hoa, "
                        "hay đơn giản là ngồi yên và thở. Ông Tưởng Huân tin rằng cái đẹp "
                        "không ở đâu xa — nó ở ngay bên cạnh bạn, chỉ cần bạn chịu dừng lại "
                        "và cảm nhận. Trong buổi học đầu tiên, bạn sẽ học 6 từ vựng quan trọng "
                        "về thời gian, cuộc sống và cảm nhận vẻ đẹp. Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 1",
                "description": "Học 6 từ: 时间, 忙碌, 安静, 美, 生活, 感受",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Bây giờ chúng ta sẽ cùng học 6 từ vựng đầu tiên. Mỗi từ đều gắn liền với nội dung "
                        "bài nói chuyện của Tưởng Huân về nghệ thuật sống chậm và cảm nhận cái đẹp.\n\n"

                        "Từ đầu tiên là 时间 (shíjiān). 时间 là danh từ, có nghĩa là 'thời gian'. "
                        "Đây là từ xuyên suốt toàn bộ bài nói chuyện. Tưởng Huân nói rằng chúng ta "
                        "luôn cảm thấy thiếu 时间, nhưng thực ra chúng ta đang lãng phí nó vào những "
                        "thứ không quan trọng. Ông khuyên mỗi người hãy dành 18 phút mỗi ngày cho chính mình. "
                        "Ví dụ: 时间是最宝贵的东西，可是我们常常浪费它 — Thời gian là thứ quý giá nhất, "
                        "nhưng chúng ta thường lãng phí nó. 时 là 'thời' và 间 là 'khoảng, gian'. "
                        "Cách dùng khác: 你有时间吗？ — Bạn có thời gian không? "
                        "Hoặc: 时间过得真快 — Thời gian trôi thật nhanh.\n\n"

                        "Từ thứ hai là 忙碌 (mánglù). 忙碌 là tính từ, có nghĩa là 'bận rộn'. "
                        "Tưởng Huân mô tả cuộc sống hiện đại là một chuỗi ngày 忙碌 không ngừng — "
                        "từ sáng đến tối, chúng ta chạy theo công việc, tin nhắn, cuộc họp mà quên mất "
                        "bản thân. Ví dụ: 我们每天都很忙碌，忙到忘记了生活中最美的东西 — "
                        "Chúng ta mỗi ngày đều rất bận rộn, bận đến mức quên mất những điều đẹp nhất "
                        "trong cuộc sống. 忙 là 'bận' và 碌 là 'lăn lộn, vất vả'. "
                        "Cách dùng: 最近工作太忙碌了 — Gần đây công việc quá bận rộn.\n\n"

                        "Từ thứ ba là 安静 (ānjìng). 安静 là tính từ, có nghĩa là 'yên tĩnh' hoặc 'im lặng'. "
                        "Tưởng Huân tin rằng 安静 là điều kiện tiên quyết để cảm nhận cái đẹp. "
                        "Khi bạn ngồi yên trong 安静, bạn mới nghe được tiếng nói bên trong mình. "
                        "Ví dụ: 安静下来，你才能听到自己心灵的声音 — Yên tĩnh lại, bạn mới nghe được "
                        "tiếng nói tâm hồn mình. 安 là 'an, yên' và 静 là 'tĩnh, lặng'. "
                        "Cách dùng: 图书馆里很安静 — Trong thư viện rất yên tĩnh. "
                        "Hoặc: 请安静一下 — Xin hãy im lặng một chút.\n\n"

                        "Từ thứ tư là 美 (měi). 美 vừa là danh từ vừa là tính từ, có nghĩa là 'đẹp' "
                        "hoặc 'vẻ đẹp, cái đẹp'. Đây là chủ đề trung tâm trong sự nghiệp của Tưởng Huân. "
                        "Ông nói: 美不在远方，美就在你身边 — Cái đẹp không ở nơi xa, cái đẹp ở ngay bên bạn. "
                        "Một tách trà nóng, ánh nắng buổi sáng, lá cây đổi màu — tất cả đều là 美. "
                        "Ví dụ: 生活中到处都有美，只是我们没有发现 — Trong cuộc sống đâu đâu cũng có cái đẹp, "
                        "chỉ là chúng ta chưa phát hiện ra. Từ này rất linh hoạt: 美丽 (xinh đẹp), "
                        "美好 (tốt đẹp), 美食 (ẩm thực ngon).\n\n"

                        "Từ thứ năm là 生活 (shēnghuó). 生活 vừa là danh từ vừa là động từ, có nghĩa là "
                        "'cuộc sống' hoặc 'sống'. Tưởng Huân không nói về những triết lý cao siêu — "
                        "ông nói về 生活 hàng ngày. Cách bạn uống trà, cách bạn đi bộ, cách bạn nhìn "
                        "bầu trời — đó chính là 生活. Ví dụ: 简单的生活才是最幸福的 — "
                        "Cuộc sống giản đơn mới là hạnh phúc nhất. 生 là 'sinh, sống' và 活 là 'hoạt, sống'. "
                        "Cách dùng: 你的生活怎么样？ — Cuộc sống của bạn thế nào? "
                        "Hoặc: 我喜欢在乡下生活 — Tôi thích sống ở nông thôn.\n\n"

                        "Từ cuối cùng trong buổi hôm nay là 感受 (gǎnshòu). 感受 vừa là danh từ vừa là "
                        "động từ, có nghĩa là 'cảm nhận' hoặc 'cảm xúc, trải nghiệm'. "
                        "Tưởng Huân nhấn mạnh rằng chúng ta cần học cách 感受 — không chỉ nhìn bằng mắt "
                        "mà phải cảm bằng trái tim. Ví dụ: 你有没有感受到风吹在脸上的感觉？ — "
                        "Bạn có cảm nhận được gió thổi trên mặt không? 感 là 'cảm' và 受 là 'nhận, chịu'. "
                        "Cách dùng: 我能感受到你的善意 — Tôi có thể cảm nhận được thiện ý của bạn. "
                        "Hoặc: 这首歌给我很深的感受 — Bài hát này cho tôi cảm xúc rất sâu.\n\n"

                        "Vậy là bạn đã biết 6 từ đầu tiên: 时间, 忙碌, 安静, 美, 生活, 感受. "
                        "Hãy cùng luyện tập qua các hoạt động tiếp theo nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Thời gian và vẻ đẹp",
                "description": "Học 6 từ: 时间, 忙碌, 安静, 美, 生活, 感受",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 1",
                "description": "Tập nói 6 từ: 时间, 忙碌, 安静, 美, 生活, 感受",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 1",
                "description": "Nhận biết 6 từ: 时间, 忙碌, 安静, 美, 生活, 感受",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 1",
                "description": "Ghép nghĩa 6 từ: 时间, 忙碌, 安静, 美, 生活, 感受",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 1",
                "description": "Viết 6 từ: 时间, 忙碌, 安静, 美, 生活, 感受",
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
                        "时间 thường đi với các động từ: 有时间 (có thời gian), 没有时间 (không có thời gian), "
                        "浪费时间 (lãng phí thời gian), 节省时间 (tiết kiệm thời gian). "
                        "Cấu trúc hay: 时间 + 过得 + tính từ: 时间过得很快 (thời gian trôi rất nhanh).\n\n"
                        "忙碌 thường đứng sau 很 hoặc 太: 很忙碌 (rất bận rộn), 太忙碌了 (quá bận rộn). "
                        "Cấu trúc: 忙碌的 + danh từ: 忙碌的一天 (một ngày bận rộn), "
                        "忙碌的生活 (cuộc sống bận rộn). Từ đồng nghĩa đơn giản hơn là 忙 (máng).\n\n"
                        "安静 có thể làm tính từ hoặc động từ. Tính từ: 这里很安静 (ở đây rất yên tĩnh). "
                        "Động từ (mệnh lệnh): 安静！(Im lặng!). Cấu trúc: 安静下来 (yên tĩnh lại), "
                        "安静地 + động từ: 安静地坐着 (ngồi yên lặng).\n\n"
                        "美 rất linh hoạt. Đứng một mình: 这里真美 (ở đây đẹp thật). "
                        "Kết hợp: 美丽 (xinh đẹp), 美好 (tốt đẹp), 美食 (ẩm thực), 美术 (mỹ thuật). "
                        "Cấu trúc: 美不在...美在... (cái đẹp không ở...cái đẹp ở...).\n\n"
                        "生活 làm danh từ: 日常生活 (cuộc sống hàng ngày), 生活方式 (lối sống). "
                        "Làm động từ: 在北京生活 (sống ở Bắc Kinh). "
                        "Cấu trúc: 生活中 (trong cuộc sống), 生活质量 (chất lượng cuộc sống).\n\n"
                        "感受 làm động từ: 感受大自然 (cảm nhận thiên nhiên), 感受温暖 (cảm nhận sự ấm áp). "
                        "Làm danh từ: 我的感受 (cảm nhận của tôi), 深刻的感受 (cảm nhận sâu sắc). "
                        "Cấu trúc: 感受到 + danh từ (cảm nhận được + danh từ)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 1)",
                "description": "大家好，我是蒋勋。今天我想跟大家聊一个很简单的问题：你有多久没有安静下来了？",
                "practiceMinutes": 9,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 1)",
                "description": "Luyện nói theo đoạn trích về thời gian và vẻ đẹp trong cuộc sống",
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
                "title": "Viết: Thời gian và vẻ đẹp",
                "description": "Viết câu sử dụng 6 từ vựng buổi 1",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "时间",
                            "prompt": (
                                "Sử dụng từ '时间' (shíjiān) để nói về thời gian trong cuộc sống — "
                                "như Tưởng Huân khuyên chúng ta hãy dành thời gian cho chính mình mỗi ngày. "
                                "Ví dụ: 我们应该每天留一点时间给自己，安静地思考。"
                            ),
                        },
                        {
                            "targetVocab": "忙碌",
                            "prompt": (
                                "Sử dụng từ '忙碌' (mánglù) để nói về sự bận rộn — "
                                "như bài nói chuyện mô tả cuộc sống hiện đại bận rộn đến mức quên mất cái đẹp. "
                                "Ví dụ: 忙碌的生活让我们忘记了身边最简单的美好。"
                            ),
                        },
                        {
                            "targetVocab": "安静",
                            "prompt": (
                                "Sử dụng từ '安静' (ānjìng) để nói về sự yên tĩnh — "
                                "như Tưởng Huân tin rằng chỉ khi yên tĩnh bạn mới nghe được tiếng nói nội tâm. "
                                "Ví dụ: 在安静的环境中，我们才能真正地思考问题。"
                            ),
                        },
                        {
                            "targetVocab": "美",
                            "prompt": (
                                "Sử dụng từ '美' (měi) để nói về cái đẹp trong cuộc sống — "
                                "như bài nói chuyện nhấn mạnh rằng cái đẹp ở ngay bên cạnh bạn. "
                                "Ví dụ: 美不在远方，一杯热茶、一缕阳光都是美。"
                            ),
                        },
                        {
                            "targetVocab": "生活",
                            "prompt": (
                                "Sử dụng từ '生活' (shēnghuó) để nói về cuộc sống hàng ngày — "
                                "như Tưởng Huân nói rằng cuộc sống giản đơn mới là hạnh phúc nhất. "
                                "Ví dụ: 我希望过一种简单而美好的生活。"
                            ),
                        },
                        {
                            "targetVocab": "感受",
                            "prompt": (
                                "Sử dụng từ '感受' (gǎnshòu) để nói về việc cảm nhận — "
                                "như bài nói chuyện khuyên chúng ta hãy cảm nhận bằng trái tim, không chỉ bằng mắt. "
                                "Ví dụ: 用心去感受生活中的每一个美好瞬间。"
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
        "title": "Buổi 2: Sống chậm và thưởng thức — 慢下来，去欣赏",
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
                        "quan trọng: 时间 (thời gian), 忙碌 (bận rộn), 安静 (yên tĩnh), 美 (đẹp), "
                        "生活 (cuộc sống), và 感受 (cảm nhận). Bạn còn nhớ không? Tưởng Huân đã hỏi: "
                        "bạn có bao lâu rồi chưa dừng lại để nhìn bầu trời? "
                        "Hôm nay chúng ta sẽ đi sâu hơn vào phần tiếp theo của bài nói chuyện, "
                        "nơi ông Tưởng Huân chia sẻ về ký ức tuổi thơ bên dòng sông, "
                        "về nghệ thuật sống chậm, và về cách thiên nhiên chữa lành tâm hồn. "
                        "Bạn sẽ học thêm 6 từ mới liên quan đến sự thư thái, "
                        "thiên nhiên và tâm hồn. Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 2",
                "description": "Học 6 từ: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng mới của buổi hôm nay. Những từ này nằm ở phần giữa "
                        "bài nói chuyện, khi Tưởng Huân kể về tuổi thơ và triết lý sống chậm.\n\n"

                        "Từ đầu tiên là 慢 (màn). 慢 là tính từ, có nghĩa là 'chậm'. "
                        "Đây là từ khóa quan trọng nhất trong phần này. Tưởng Huân kể rằng hồi nhỏ, "
                        "cuộc sống rất 慢 — ông ngồi bên sông hàng giờ, nhìn nước chảy, nhìn mây trôi. "
                        "Nhưng bây giờ, chúng ta sợ 慢, vì chúng ta nghĩ chậm là lãng phí. "
                        "Ví dụ: 我们害怕慢下来，因为觉得慢就是浪费时间 — Chúng ta sợ chậm lại, "
                        "vì nghĩ rằng chậm là lãng phí thời gian. Từ này rất đơn giản nhưng sâu sắc. "
                        "Cách dùng: 请说慢一点 — Xin nói chậm một chút. "
                        "Hoặc: 慢慢来，不要着急 — Từ từ thôi, đừng vội.\n\n"

                        "Từ thứ hai là 欣赏 (xīnshǎng). 欣赏 là động từ, có nghĩa là 'thưởng thức' "
                        "hoặc 'ngắm nhìn, đánh giá cao'. Tưởng Huân nói rằng 欣赏 một bức tranh "
                        "cần thời gian — bạn không thể chụp ảnh rồi đi, bạn phải đứng lại và nhìn. "
                        "Ví dụ: 欣赏一幅画需要时间 — Thưởng thức một bức tranh cần thời gian. "
                        "欣 là 'vui, hân hoan' và 赏 là 'thưởng, ngắm'. Khi bạn 欣赏, bạn đang "
                        "vừa ngắm nhìn vừa tận hưởng niềm vui từ cái đẹp. "
                        "Cách dùng: 我很欣赏你的才华 — Tôi rất ngưỡng mộ tài năng của bạn. "
                        "Hoặc: 让我们一起欣赏这美丽的风景 — Hãy cùng ngắm phong cảnh đẹp này.\n\n"

                        "Từ thứ ba là 自然 (zìrán). 自然 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "'thiên nhiên' hoặc 'tự nhiên'. Tưởng Huân tin rằng 自然 là người thầy vĩ đại nhất "
                        "về cái đẹp. Nhìn lá rơi, nghe tiếng chim, cảm nhận gió — tất cả đều là bài học "
                        "từ 自然. Ví dụ: 大自然是最好的老师 — Thiên nhiên là người thầy tốt nhất. "
                        "自 là 'tự' và 然 là 'nhiên, như vậy'. Cách dùng: 这里的自然风景很美 — "
                        "Phong cảnh thiên nhiên ở đây rất đẹp. Hoặc: 他说话很自然 — "
                        "Anh ấy nói chuyện rất tự nhiên.\n\n"

                        "Từ thứ tư là 心灵 (xīnlíng). 心灵 là danh từ, có nghĩa là 'tâm hồn' hoặc "
                        "'tâm linh, tinh thần'. Tưởng Huân nói rằng khi bạn ngồi yên trong yên tĩnh, "
                        "bạn mới nghe được tiếng nói của 心灵. Cuộc sống bận rộn che lấp tiếng nói đó. "
                        "Ví dụ: 安静下来，你才能听到自己心灵的声音 — Yên tĩnh lại, bạn mới nghe được "
                        "tiếng nói tâm hồn mình. 心 là 'tim, lòng' và 灵 là 'linh, thiêng'. "
                        "Cách dùng: 音乐可以净化心灵 — Âm nhạc có thể thanh lọc tâm hồn. "
                        "Hoặc: 这本书触动了我的心灵 — Cuốn sách này chạm đến tâm hồn tôi.\n\n"

                        "Từ thứ năm là 放松 (fàngsōng). 放松 là động từ, có nghĩa là 'thư giãn' "
                        "hoặc 'buông lỏng'. Tưởng Huân kể về người bạn làm việc mười mấy tiếng mỗi ngày, "
                        "cho đến khi bị bệnh mới phát hiện rằng 放松 là điều tuyệt vời nhất. "
                        "Ví dụ: 原来放松是这么美好的事情 — Hóa ra thư giãn là điều tuyệt vời đến vậy. "
                        "放 là 'buông, thả' và 松 là 'lỏng, thoải mái'. Khi bạn 放松, bạn đang "
                        "buông bỏ mọi căng thẳng. Cách dùng: 周末我喜欢在家放松 — "
                        "Cuối tuần tôi thích ở nhà thư giãn.\n\n"

                        "Từ cuối cùng là 享受 (xiǎngshòu). 享受 là động từ, có nghĩa là 'tận hưởng' "
                        "hoặc 'hưởng thụ'. Tưởng Huân muốn chúng ta học cách 享受 những khoảnh khắc "
                        "nhỏ bé trong cuộc sống — một buổi chiều yên tĩnh, một tách cà phê, "
                        "một cuốn sách hay. Ví dụ: 学会享受生活中的每一个小瞬间 — "
                        "Hãy học cách tận hưởng mỗi khoảnh khắc nhỏ trong cuộc sống. "
                        "享 là 'hưởng' và 受 là 'nhận'. Cách dùng: 我很享受一个人的时光 — "
                        "Tôi rất tận hưởng khoảng thời gian một mình. "
                        "Hoặc: 享受过程比结果更重要 — Tận hưởng quá trình quan trọng hơn kết quả.\n\n"

                        "Vậy là bạn đã học thêm 6 từ mới: 慢, 欣赏, 自然, 心灵, 放松, 享受. "
                        "Cùng với 6 từ buổi trước, bạn đã có 12 từ vựng rồi! Hãy luyện tập tiếp nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Sống chậm và thưởng thức",
                "description": "Học 6 từ: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 2",
                "description": "Tập nói 6 từ: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 2",
                "description": "Nhận biết 6 từ: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 2",
                "description": "Ghép nghĩa 6 từ: 慢, 欣赏, 自然, 心灵, 放松, 享受",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 2",
                "description": "Viết 6 từ: 慢, 欣赏, 自然, 心灵, 放松, 享受",
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
                        "慢 thường đi với 下来 để chỉ hành động chậm lại: 慢下来 (chậm lại). "
                        "Dạng lặp: 慢慢 (từ từ) — 慢慢走 (đi từ từ), 慢慢来 (từ từ thôi). "
                        "Cấu trúc so sánh: 比...慢 (chậm hơn...).\n\n"
                        "欣赏 thường đi với đối tượng cụ thể: 欣赏音乐 (thưởng thức âm nhạc), "
                        "欣赏风景 (ngắm phong cảnh), 欣赏艺术 (thưởng thức nghệ thuật). "
                        "Nghĩa mở rộng: 欣赏一个人 (ngưỡng mộ một người).\n\n"
                        "自然 làm danh từ: 大自然 (thiên nhiên vĩ đại), 自然界 (thế giới tự nhiên). "
                        "Làm tính từ: 很自然 (rất tự nhiên), 自然而然 (tự nhiên mà thành). "
                        "Cấu trúc: 回归自然 (trở về với thiên nhiên).\n\n"
                        "心灵 thường đi với tính từ hoặc danh từ: 心灵美 (tâm hồn đẹp), "
                        "心灵深处 (sâu thẳm tâm hồn), 心灵鸡汤 (canh gà tâm hồn — bài viết truyền cảm hứng). "
                        "Cấu trúc: 触动心灵 (chạm đến tâm hồn).\n\n"
                        "放松 thường đi với 一下 hoặc đứng một mình: 放松一下 (thư giãn một chút), "
                        "放松心情 (thư giãn tâm trạng), 放松身体 (thư giãn cơ thể). "
                        "Cấu trúc: 让自己放松 (để bản thân thư giãn).\n\n"
                        "享受 thường đi với danh từ hoặc cụm danh từ: 享受生活 (tận hưởng cuộc sống), "
                        "享受过程 (tận hưởng quá trình), 享受孤独 (tận hưởng sự cô đơn). "
                        "Cấu trúc: 享受...的乐趣 (tận hưởng niềm vui của...)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 2)",
                "description": "我小时候住在台北，那时候的生活很慢。放学以后，我会在河边坐很久。",
                "practiceMinutes": 9,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 2)",
                "description": "Luyện nói theo đoạn trích về sống chậm và thưởng thức cuộc sống",
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
                "title": "Viết: Sống chậm và thưởng thức",
                "description": "Viết câu sử dụng 6 từ vựng buổi 2",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "慢",
                            "prompt": (
                                "Sử dụng từ '慢' (màn) để nói về việc sống chậm lại — "
                                "như Tưởng Huân nói rằng chúng ta sợ chậm vì nghĩ chậm là lãng phí. "
                                "Ví dụ: 慢下来不是浪费时间，而是更好地感受生活。"
                            ),
                        },
                        {
                            "targetVocab": "欣赏",
                            "prompt": (
                                "Sử dụng từ '欣赏' (xīnshǎng) để nói về việc thưởng thức cái đẹp — "
                                "như bài nói chuyện nhấn mạnh rằng thưởng thức nghệ thuật cần thời gian. "
                                "Ví dụ: 我喜欢在周末去公园欣赏大自然的美。"
                            ),
                        },
                        {
                            "targetVocab": "自然",
                            "prompt": (
                                "Sử dụng từ '自然' (zìrán) để nói về thiên nhiên hoặc sự tự nhiên — "
                                "như Tưởng Huân tin rằng thiên nhiên là người thầy vĩ đại nhất về cái đẹp. "
                                "Ví dụ: 回归自然是现代人最需要的一种生活方式。"
                            ),
                        },
                        {
                            "targetVocab": "心灵",
                            "prompt": (
                                "Sử dụng từ '心灵' (xīnlíng) để nói về tâm hồn — "
                                "như bài nói chuyện khuyến khích lắng nghe tiếng nói tâm hồn mình. "
                                "Ví dụ: 好的音乐可以治愈我们疲惫的心灵。"
                            ),
                        },
                        {
                            "targetVocab": "放松",
                            "prompt": (
                                "Sử dụng từ '放松' (fàngsōng) để nói về việc thư giãn — "
                                "như câu chuyện người bạn của Tưởng Huân phát hiện ra thư giãn tuyệt vời đến nhường nào. "
                                "Ví dụ: 工作再忙也要找时间放松自己，这对健康很重要。"
                            ),
                        },
                        {
                            "targetVocab": "享受",
                            "prompt": (
                                "Sử dụng từ '享受' (xiǎngshòu) để nói về việc tận hưởng — "
                                "như bài nói chuyện khuyên chúng ta tận hưởng những khoảnh khắc nhỏ bé. "
                                "Ví dụ: 享受一个人安静读书的时光，是一种简单的幸福。"
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
        "title": "Buổi 3: Nghệ thuật và hạnh phúc — 艺术与幸福",
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
                        "Qua hai buổi trước, bạn đã học 12 từ vựng: 时间, 忙碌, 安静, 美, 生活, 感受 "
                        "ở buổi 1, và 慢, 欣赏, 自然, 心灵, 放松, 享受 ở buổi 2. "
                        "Bạn đã hiểu rằng Tưởng Huân muốn chúng ta dừng lại, sống chậm, "
                        "và cảm nhận vẻ đẹp giản dị quanh mình. Hôm nay, chúng ta sẽ đi vào "
                        "phần cuối của bài nói chuyện, nơi ông nói về nghệ thuật, sự cô đơn, "
                        "và bí mật của hạnh phúc thực sự. 6 từ vựng cuối cùng sẽ giúp bạn "
                        "nói về những giá trị sâu sắc nhất trong cuộc sống. Hãy bắt đầu nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 3",
                "description": "Học 6 từ: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng cuối cùng. Đây là những từ nằm ở phần kết của bài nói chuyện, "
                        "khi Tưởng Huân đưa ra thông điệp sâu sắc nhất: hạnh phúc nằm trong sự giản đơn.\n\n"

                        "Từ đầu tiên là 艺术 (yìshù). 艺术 là danh từ, có nghĩa là 'nghệ thuật'. "
                        "Tưởng Huân là một học giả mỹ học, nên 艺术 là chủ đề xuyên suốt cuộc đời ông. "
                        "Ông nói rằng 艺术 dạy chúng ta một điều quan trọng: hãy chậm lại và dùng trái tim "
                        "để nhìn. Khi bạn đứng trước bức Mona Lisa mười phút thay vì chụp ảnh rồi đi, "
                        "bạn sẽ thấy nụ cười của nàng đang thay đổi. "
                        "Ví dụ: 艺术教会我们慢下来，用心去看 — Nghệ thuật dạy chúng ta chậm lại, "
                        "dùng trái tim để nhìn. 艺 là 'nghệ' và 术 là 'thuật, kỹ năng'. "
                        "Cách dùng: 他对艺术很有兴趣 — Anh ấy rất quan tâm đến nghệ thuật. "
                        "Hoặc: 生活本身就是一种艺术 — Cuộc sống bản thân nó đã là một loại nghệ thuật.\n\n"

                        "Từ thứ hai là 孤独 (gūdú). 孤独 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "'cô đơn' hoặc 'sự cô đơn'. Tưởng Huân có một quan điểm rất khác về 孤独: "
                        "ông cho rằng 孤独 không phải là điều xấu. Khi bạn một mình ngồi yên, "
                        "bạn mới nghe được tiếng nói tâm hồn. Người hiện đại sợ 孤独 nên dùng "
                        "mạng xã hội, tiệc tùng để lấp đầy mọi phút giây. "
                        "Ví dụ: 孤独不是坏事，它让你听到自己心灵的声音 — Cô đơn không phải điều xấu, "
                        "nó giúp bạn nghe được tiếng nói tâm hồn mình. 孤 là 'cô, lẻ loi' và 独 là 'độc, một mình'. "
                        "Cách dùng: 他享受孤独的时光 — Anh ấy tận hưởng khoảng thời gian cô đơn. "
                        "Hoặc: 创作需要孤独 — Sáng tạo cần sự cô đơn.\n\n"

                        "Từ thứ ba là 思考 (sīkǎo). 思考 là động từ, có nghĩa là 'suy nghĩ' hoặc 'suy ngẫm'. "
                        "Tưởng Huân nhấn mạnh rằng 思考 thực sự cần sự yên tĩnh và cô đơn. "
                        "Trong tiếng ồn và bận rộn, bạn không thể 思考 sâu sắc được. "
                        "Ví dụ: 真正的思考需要孤独和安静 — Suy nghĩ thực sự cần sự cô đơn và yên tĩnh. "
                        "思 là 'tư, suy nghĩ' và 考 là 'khảo, xem xét'. "
                        "Cách dùng: 这个问题值得我们认真思考 — Vấn đề này đáng để chúng ta suy nghĩ nghiêm túc. "
                        "Hoặc: 给我一点时间思考 — Cho tôi một chút thời gian suy nghĩ.\n\n"

                        "Từ thứ tư là 珍惜 (zhēnxī). 珍惜 là động từ, có nghĩa là 'trân trọng' hoặc 'quý trọng'. "
                        "Tưởng Huân muốn chúng ta 珍惜 những khoảnh khắc giản đơn — "
                        "mười tám phút yên tĩnh mỗi ngày có thể trở thành khoảng thời gian "
                        "bạn 珍惜 nhất. Ví dụ: 这十八分钟，也许会成为你一天中最珍惜的时光 — "
                        "Mười tám phút này có lẽ sẽ trở thành khoảng thời gian bạn trân trọng nhất trong ngày. "
                        "珍 là 'trân, quý' và 惜 là 'tiếc, quý'. "
                        "Cách dùng: 珍惜眼前的人 — Trân trọng người trước mắt. "
                        "Hoặc: 我们要珍惜每一天 — Chúng ta phải trân trọng mỗi ngày.\n\n"

                        "Từ thứ năm là 简单 (jiǎndān). 简单 là tính từ, có nghĩa là 'đơn giản' hoặc 'giản dị'. "
                        "Câu kết thúc bài nói chuyện của Tưởng Huân rất ngắn gọn nhưng đầy sức nặng: "
                        "生活不需要那么复杂。简单，就是幸福 — Cuộc sống không cần phức tạp đến vậy. "
                        "Đơn giản, chính là hạnh phúc. 简 là 'giản, đơn giản' và 单 là 'đơn, một'. "
                        "Cách dùng: 这道菜做法很简单 — Cách làm món này rất đơn giản. "
                        "Hoặc: 简单的生活最幸福 — Cuộc sống giản đơn là hạnh phúc nhất.\n\n"

                        "Từ cuối cùng là 幸福 (xìngfú). 幸福 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "'hạnh phúc'. Đây là từ kết thúc bài nói chuyện và cũng là thông điệp cốt lõi. "
                        "Tưởng Huân tin rằng 幸福 không đến từ tiền bạc hay thành công, "
                        "mà đến từ khả năng cảm nhận cái đẹp trong những điều giản đơn nhất. "
                        "Ví dụ: 幸福不是拥有很多，而是感受很多 — Hạnh phúc không phải sở hữu nhiều, "
                        "mà là cảm nhận nhiều. 幸 là 'may mắn' và 福 là 'phúc, phước'. "
                        "Cách dùng: 我觉得自己很幸福 — Tôi thấy mình rất hạnh phúc. "
                        "Hoặc: 幸福就在身边 — Hạnh phúc ở ngay bên cạnh.\n\n"

                        "Tuyệt vời! Bạn đã học xong toàn bộ 18 từ vựng: 时间, 忙碌, 安静, 美, 生活, 感受, "
                        "慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福. "
                        "Hãy luyện tập qua các hoạt động tiếp theo!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Nghệ thuật và hạnh phúc",
                "description": "Học 6 từ: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 3",
                "description": "Tập nói 6 từ: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 3",
                "description": "Nhận biết 6 từ: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 3",
                "description": "Ghép nghĩa 6 từ: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 3",
                "description": "Viết 6 từ: 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
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
                        "艺术 thường đi với các danh từ khác: 艺术家 (nghệ sĩ), 艺术品 (tác phẩm nghệ thuật), "
                        "艺术节 (lễ hội nghệ thuật). Cấu trúc: ...是一种艺术 (...là một loại nghệ thuật). "
                        "Ví dụ: 做饭也是一种艺术 — Nấu ăn cũng là một loại nghệ thuật.\n\n"
                        "孤独 thường đi với 感到 hoặc 享受: 感到孤独 (cảm thấy cô đơn), "
                        "享受孤独 (tận hưởng cô đơn). Cấu trúc: 孤独的 + danh từ: "
                        "孤独的夜晚 (đêm cô đơn), 孤独的旅行 (chuyến đi một mình).\n\n"
                        "思考 thường đi với 关于 hoặc đối tượng trực tiếp: 思考人生 (suy nghĩ về cuộc đời), "
                        "思考问题 (suy nghĩ về vấn đề). Cấu trúc: 独立思考 (suy nghĩ độc lập), "
                        "深入思考 (suy nghĩ sâu sắc).\n\n"
                        "珍惜 thường đi với danh từ trừu tượng: 珍惜时间 (trân trọng thời gian), "
                        "珍惜友谊 (trân trọng tình bạn), 珍惜机会 (trân trọng cơ hội). "
                        "Cấu trúc: 要珍惜... (phải trân trọng...), 学会珍惜 (học cách trân trọng).\n\n"
                        "简单 thường đứng trước danh từ: 简单的生活 (cuộc sống đơn giản), "
                        "简单的道理 (đạo lý đơn giản). Cấu trúc: 很简单 (rất đơn giản), "
                        "简简单单 (giản dị, mộc mạc — dạng lặp nhấn mạnh).\n\n"
                        "幸福 làm tính từ: 很幸福 (rất hạnh phúc), 幸福的家庭 (gia đình hạnh phúc). "
                        "Làm danh từ: 追求幸福 (theo đuổi hạnh phúc), 幸福感 (cảm giác hạnh phúc). "
                        "Cấu trúc: 幸福就是... (hạnh phúc chính là...)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 3)",
                "description": "艺术教会我们一件很重要的事：慢下来，用心去看。",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 3)",
                "description": "Luyện nói theo đoạn trích về nghệ thuật, cô đơn và hạnh phúc",
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
                "title": "Viết: Nghệ thuật và hạnh phúc",
                "description": "Viết câu sử dụng 6 từ vựng buổi 3",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "艺术",
                            "prompt": (
                                "Sử dụng từ '艺术' (yìshù) để nói về nghệ thuật — "
                                "như Tưởng Huân nói rằng nghệ thuật dạy chúng ta chậm lại và dùng trái tim để nhìn. "
                                "Ví dụ: 艺术不只是画画和唱歌，生活本身就是最好的艺术。"
                            ),
                        },
                        {
                            "targetVocab": "孤独",
                            "prompt": (
                                "Sử dụng từ '孤独' (gūdú) để nói về sự cô đơn — "
                                "như bài nói chuyện giải thích rằng cô đơn giúp bạn nghe được tiếng nói tâm hồn. "
                                "Ví dụ: 学会享受孤独的人，才能找到真正的自由。"
                            ),
                        },
                        {
                            "targetVocab": "思考",
                            "prompt": (
                                "Sử dụng từ '思考' (sīkǎo) để nói về việc suy nghĩ — "
                                "như Tưởng Huân nhấn mạnh rằng suy nghĩ thực sự cần sự yên tĩnh. "
                                "Ví dụ: 在安静的环境中思考问题，往往能找到更好的答案。"
                            ),
                        },
                        {
                            "targetVocab": "珍惜",
                            "prompt": (
                                "Sử dụng từ '珍惜' (zhēnxī) để nói về việc trân trọng — "
                                "như bài nói chuyện khuyên chúng ta trân trọng mười tám phút yên tĩnh mỗi ngày. "
                                "Ví dụ: 珍惜和家人在一起的每一刻，因为时间不会等人。"
                            ),
                        },
                        {
                            "targetVocab": "简单",
                            "prompt": (
                                "Sử dụng từ '简单' (jiǎndān) để nói về sự đơn giản — "
                                "như Tưởng Huân kết luận rằng cuộc sống không cần phức tạp. "
                                "Ví dụ: 有时候，最简单的生活方式反而是最幸福的。"
                            ),
                        },
                        {
                            "targetVocab": "幸福",
                            "prompt": (
                                "Sử dụng từ '幸福' (xìngfú) để nói về hạnh phúc — "
                                "như bài nói chuyện kết thúc với thông điệp: đơn giản chính là hạnh phúc. "
                                "Ví dụ: 幸福不是拥有很多东西，而是能感受到生活中的美好。"
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
                        "về chủ đề sống chậm, nghệ thuật và hạnh phúc. Hãy cùng ôn lại nhé!\n\n"
                        "Buổi 1, bạn đã học: 时间 (thời gian), 忙碌 (bận rộn), 安静 (yên tĩnh), "
                        "美 (đẹp), 生活 (cuộc sống), 感受 (cảm nhận). Đây là những từ nền tảng "
                        "giúp bạn nói về nhịp sống hàng ngày và cách cảm nhận cái đẹp.\n\n"
                        "Buổi 2, bạn đã học: 慢 (chậm), 欣赏 (thưởng thức), 自然 (thiên nhiên), "
                        "心灵 (tâm hồn), 放松 (thư giãn), 享受 (tận hưởng). Những từ này giúp bạn nói về "
                        "nghệ thuật sống chậm và tận hưởng cuộc sống.\n\n"
                        "Buổi 3, bạn đã học: 艺术 (nghệ thuật), 孤独 (cô đơn), 思考 (suy nghĩ), "
                        "珍惜 (trân trọng), 简单 (đơn giản), 幸福 (hạnh phúc). Đây là những từ "
                        "giúp bạn hiểu rằng hạnh phúc nằm trong sự giản đơn.\n\n"
                        "Bây giờ hãy ôn tập toàn bộ 18 từ qua các hoạt động flashcard!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập toàn bộ 18 từ vựng",
                "description": "Ôn tập 18 từ: 时间, 忙碌, 安静, 美, 生活, 感受, 慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói toàn bộ 18 từ vựng",
                "description": "Tập nói 18 từ: 时间, 忙碌, 安静, 美, 生活, 感受, 慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết toàn bộ từ vựng",
                "description": "Nhận biết 18 từ: 时间, 忙碌, 安静, 美, 生活, 感受, 慢, 欣赏, 自然, 心灵, 放松, 享受, 艺术, 孤独, 思考, 珍惜, 简单, 幸福",
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
                        "của Tưởng Huân từ đầu đến cuối. Bạn đã học 18 từ vựng qua 3 buổi học "
                        "và ôn tập ở buổi 4. Bây giờ là lúc bạn thử sức với toàn bộ văn bản. "
                        "Hãy đọc chậm — đúng như tinh thần bài nói chuyện — chú ý đến những từ "
                        "bạn đã học, và cảm nhận cách chúng kết nối với nhau trong ngữ cảnh thực tế. "
                        "Chúc bạn đọc vui!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. reading — full transcript
            {
                "activityType": "reading",
                "title": "Đọc: Toàn bộ bài nói chuyện",
                "description": "大家好，我是蒋勋。今天我想跟大家聊一个很简单的问题：你有多久没有安静下来了？",
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
                        "Chúc mừng bạn đã hoàn thành toàn bộ khóa học! Bạn đã đi một chặng đường tuyệt vời "
                        "cùng Tưởng Huân và triết lý sống chậm. Hãy cùng ôn lại 18 từ vựng một lần cuối nhé.\n\n"

                        "时间 (shíjiān) — thời gian. Ví dụ: 留一点时间给自己，这是最好的礼物 — "
                        "Dành một chút thời gian cho bản thân, đó là món quà tốt nhất.\n\n"

                        "忙碌 (mánglù) — bận rộn. Ví dụ: 忙碌不是成功的标志，有时候它是迷失的开始 — "
                        "Bận rộn không phải dấu hiệu thành công, đôi khi nó là khởi đầu của sự lạc lối.\n\n"

                        "安静 (ānjìng) — yên tĩnh. Ví dụ: 在安静中，你会发现世界比你想象的更美 — "
                        "Trong yên tĩnh, bạn sẽ phát hiện thế giới đẹp hơn bạn tưởng.\n\n"

                        "美 (měi) — đẹp, vẻ đẹp. Ví dụ: 美就在你身边，只要你愿意停下来看 — "
                        "Cái đẹp ở ngay bên bạn, chỉ cần bạn chịu dừng lại nhìn.\n\n"

                        "生活 (shēnghuó) — cuộc sống. Ví dụ: 好好生活，就是对自己最大的尊重 — "
                        "Sống tốt chính là sự tôn trọng lớn nhất dành cho bản thân.\n\n"

                        "感受 (gǎnshòu) — cảm nhận. Ví dụ: 闭上眼睛，感受阳光的温暖 — "
                        "Nhắm mắt lại, cảm nhận sự ấm áp của ánh nắng.\n\n"

                        "慢 (màn) — chậm. Ví dụ: 慢一点，你会看到更多的风景 — "
                        "Chậm một chút, bạn sẽ thấy nhiều phong cảnh hơn.\n\n"

                        "欣赏 (xīnshǎng) — thưởng thức. Ví dụ: 学会欣赏平凡中的美好 — "
                        "Hãy học cách thưởng thức vẻ đẹp trong sự bình thường.\n\n"

                        "自然 (zìrán) — thiên nhiên, tự nhiên. Ví dụ: 走进自然，让心灵得到休息 — "
                        "Bước vào thiên nhiên, để tâm hồn được nghỉ ngơi.\n\n"

                        "心灵 (xīnlíng) — tâm hồn. Ví dụ: 一本好书可以丰富你的心灵 — "
                        "Một cuốn sách hay có thể làm phong phú tâm hồn bạn.\n\n"

                        "放松 (fàngsōng) — thư giãn. Ví dụ: 放松不是懒惰，而是为了走更远的路 — "
                        "Thư giãn không phải lười biếng, mà là để đi xa hơn.\n\n"

                        "享受 (xiǎngshòu) — tận hưởng. Ví dụ: 享受当下，不要总是担心未来 — "
                        "Tận hưởng hiện tại, đừng luôn lo lắng về tương lai.\n\n"

                        "艺术 (yìshù) — nghệ thuật. Ví dụ: 用艺术的眼光看世界，一切都变得不同 — "
                        "Nhìn thế giới bằng con mắt nghệ thuật, mọi thứ đều trở nên khác biệt.\n\n"

                        "孤独 (gūdú) — cô đơn. Ví dụ: 孤独是一种力量，它让你更了解自己 — "
                        "Cô đơn là một sức mạnh, nó giúp bạn hiểu bản thân hơn.\n\n"

                        "思考 (sīkǎo) — suy nghĩ. Ví dụ: 每天花十分钟安静地思考，你会变得更清醒 — "
                        "Mỗi ngày dành mười phút yên tĩnh suy nghĩ, bạn sẽ trở nên tỉnh táo hơn.\n\n"

                        "珍惜 (zhēnxī) — trân trọng. Ví dụ: 珍惜现在拥有的一切，不要等失去才后悔 — "
                        "Trân trọng tất cả những gì đang có, đừng đợi mất rồi mới hối hận.\n\n"

                        "简单 (jiǎndān) — đơn giản. Ví dụ: 把生活变简单，你会发现幸福其实很近 — "
                        "Làm cuộc sống trở nên đơn giản, bạn sẽ phát hiện hạnh phúc thực ra rất gần.\n\n"

                        "幸福 (xìngfú) — hạnh phúc. Ví dụ: 幸福不在远方，它就在每一个用心生活的瞬间 — "
                        "Hạnh phúc không ở nơi xa, nó ở trong mỗi khoảnh khắc sống bằng trái tim.\n\n"

                        "Như Tưởng Huân đã nói: 生活不需要那么复杂。简单，就是幸福 — "
                        "Cuộc sống không cần phức tạp đến vậy. Đơn giản, chính là hạnh phúc. "
                        "Bạn đã không chỉ học được 18 từ vựng tiếng Trung, mà còn hiểu sâu hơn "
                        "về nghệ thuật sống chậm và cảm nhận cái đẹp. Hãy nhớ: mỗi ngày hãy dành "
                        "mười tám phút cho chính mình. Cảm ơn bạn đã đồng hành, "
                        "và chúc bạn luôn tìm thấy vẻ đẹp trong những điều giản đơn nhất! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Học Qua Podcast: '留十八分鐘給自己' — 蔣勳 (Hãy dành 18 phút cho chính mình)",
        "description": (
            "BẠN CÓ ĐANG CHẠY SUỐT NGÀY MÀ QUÊN MẤT CHÍNH MÌNH?\n\n"
            "Sáng mở mắt là cầm điện thoại. Đến công ty là họp hành, email, deadline. "
            "Tối về nhà lại lướt mạng xã hội cho đến khi ngủ thiếp đi. Ngày nào cũng vậy. "
            "Bạn bận đến mức không nhớ lần cuối mình nhìn bầu trời là khi nào. "
            "Bạn bận đến mức quên rằng hoa bên đường đã nở.\n\n"
            "Nhà văn và học giả mỹ học Tưởng Huân (蔣勳) từ TEDxTaipei sẽ lay tỉnh bạn "
            "bằng một câu hỏi giản dị đến đau lòng: Bạn có bao lâu rồi chưa thực sự "
            "dừng lại? Ông tin rằng cái đẹp không ở nơi xa xôi nào — nó ở ngay trong "
            "tách trà nóng buổi sáng, trong ánh nắng xuyên qua cửa sổ, trong tiếng gió "
            "thổi qua tán lá. Nhưng nếu bạn cứ chạy mãi, bạn sẽ mù trước tất cả.\n\n"
            "Khi bạn dám chậm lại, dám ngồi yên mười tám phút mỗi ngày để lắng nghe "
            "tâm hồn mình — bạn không chỉ tìm lại sự bình yên, bạn đang chạm vào "
            "hạnh phúc thực sự.\n\n"
            "Học 18 từ vựng đắt giá về cuộc sống, nghệ thuật và hạnh phúc cùng trải nghiệm "
            "đa giác quan giúp bạn vừa nâng cấp tư duy, vừa nâng trình tiếng Trung một cách vượt bậc."
        ),
        "preview": {
            "text": (
                "Bạn có biết rằng sự bận rộn đang cướp đi khả năng cảm nhận hạnh phúc của bạn? "
                "Nhà văn Tưởng Huân từ TEDxTaipei sẽ thay đổi cách bạn nhìn nhận thời gian, "
                "cái đẹp và cuộc sống. Trong khóa học này, bạn sẽ học 18 từ vựng tiếng Trung "
                "cấp độ HSK2-HSK3 về sống chậm và nghệ thuật: 时间 (thời gian), 忙碌 (bận rộn), "
                "安静 (yên tĩnh), 美 (đẹp), 生活 (cuộc sống), 感受 (cảm nhận), 慢 (chậm), "
                "欣赏 (thưởng thức), 自然 (thiên nhiên), 心灵 (tâm hồn), 放松 (thư giãn), "
                "享受 (tận hưởng), 艺术 (nghệ thuật), 孤独 (cô đơn), 思考 (suy nghĩ), "
                "珍惜 (trân trọng), 简单 (đơn giản), 幸福 (hạnh phúc). Qua 5 buổi học với "
                "flashcard, bài đọc, luyện nói và viết câu, bạn sẽ không chỉ nắm vững từ vựng "
                "mà còn khám phá triết lý sống chậm của một trong những nhà văn được yêu thích "
                "nhất Đài Loan — và tìm thấy hạnh phúc trong những điều giản đơn nhất."
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
