"""
Create vi-zh podcast curriculum #3:
莊祖宜 (Tzui Chuang Mullinax) — "吃出更好的未來"
(Eating for a Better Future)

TED Shanghai 2013, ~17 minutes, about food, cooking, and sustainability.
YouTube: https://www.youtube.com/watch?v=wcfLMfo6LQc

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
        "title": "Buổi 1: Thực phẩm và tương lai — 食物与未来",
        "activities": [
            # 1. introAudio — welcome/intro
            {
                "activityType": "introAudio",
                "title": "Giới thiệu bài nói chuyện",
                "description": "Giới thiệu bài TED Talk của Trang Tổ Nghi về ẩm thực và tương lai",
                "practiceMinutes": 2,
                "data": {
                    "text": (
                        "Chào mừng bạn đến với khóa học từ vựng tiếng Trung qua podcast! "
                        "Hôm nay chúng ta sẽ cùng khám phá một bài nói chuyện đầy cảm hứng từ TED Shanghai — "
                        "bài \u201c吃出更好的未來\u201d (Ăn vì một tương lai tốt đẹp hơn) của nhà văn ẩm thực "
                        "và đầu bếp Trang Tổ Nghi (莊祖宜). Cô Trang từng là nghiên cứu sinh ngành nhân học, "
                        "nhưng đã bỏ học thuật để theo đuổi đam mê nấu ăn. Tại sao? Vì cô nhận ra rằng "
                        "thực phẩm là cách trực tiếp nhất để hiểu một nền văn hóa. "
                        "Trong bài nói chuyện này, cô Trang chia sẻ rằng mỗi lựa chọn thực phẩm "
                        "của chúng ta đều ảnh hưởng đến môi trường và tương lai. "
                        "Nấu ăn có ý thức, chọn nguyên liệu bền vững, ủng hộ nông dân địa phương — "
                        "đây không chỉ là niềm vui cá nhân mà còn là trách nhiệm xã hội. "
                        "Trong buổi học đầu tiên, bạn sẽ học 6 từ vựng nền tảng về thực phẩm, "
                        "sức khỏe và môi trường. Mỗi từ đều xuất hiện trong bài nói chuyện "
                        "và sẽ giúp bạn hiểu sâu hơn về mối quan hệ giữa con người và thức ăn. "
                        "Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 1",
                "description": "Học 6 từ: 食物, 做饭, 健康, 环境, 选择, 未来",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Bây giờ chúng ta sẽ cùng học 6 từ vựng đầu tiên. Mỗi từ đều gắn liền với nội dung "
                        "bài nói chuyện của cô Trang Tổ Nghi về thực phẩm và tương lai.\n\n"

                        "Từ đầu tiên là 食物 (shíwù). 食物 là danh từ, có nghĩa là \u2018thực phẩm\u2019 hoặc \u2018đồ ăn\u2019. "
                        "Đây là từ trung tâm của toàn bộ bài nói chuyện. Cô Trang nói rằng mỗi miếng 食物 "
                        "đều có một câu chuyện — nó đến từ đâu, ai trồng, làm như thế nào. "
                        "Ví dụ: 每一口食物背后都有一个故事 — Mỗi miếng thực phẩm đều có một câu chuyện phía sau. "
                        "食 là \u2018ăn, thực\u2019 và 物 là \u2018vật, đồ vật\u2019, nên 食物 nghĩa đen là \u2018vật để ăn\u2019. "
                        "Bạn có thể dùng từ này khi nói về đồ ăn hàng ngày: 健康的食物对身体很重要 — "
                        "Thực phẩm lành mạnh rất quan trọng cho cơ thể.\n\n"

                        "Từ thứ hai là 做饭 (zuòfàn). 做饭 là động từ, có nghĩa là \u2018nấu cơm\u2019 hoặc \u2018nấu ăn\u2019. "
                        "Cô Trang cho rằng bước đầu tiên để thay đổi là quay lại nhà bếp và tự 做饭. "
                        "Khi bạn tự nấu ăn, bạn bắt đầu quan tâm đến nguyên liệu — cà chua có tươi không? "
                        "Trứng từ đâu đến? Ví dụ: 自己做饭比叫外卖健康多了 — Tự nấu ăn lành mạnh hơn "
                        "gọi đồ ăn ngoài nhiều. 做 là \u2018làm\u2019 và 饭 là \u2018cơm\u2019. Trong tiếng Trung, 做饭 "
                        "không chỉ là nấu cơm mà là nấu ăn nói chung. Cách dùng khác: "
                        "我每天都自己做饭 — Tôi tự nấu ăn mỗi ngày.\n\n"

                        "Từ thứ ba là 健康 (jiànkāng). 健康 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "\u2018sức khỏe\u2019 hoặc \u2018khỏe mạnh\u2019. Cô Trang kết nối thực phẩm với 健康: "
                        "ăn thực phẩm tươi, tự nhiên giúp cơ thể khỏe mạnh hơn. "
                        "Ví dụ: 吃新鲜的食物对健康有好处 — Ăn thực phẩm tươi có lợi cho sức khỏe. "
                        "健 là \u2018mạnh khỏe\u2019 và 康 là \u2018an khang\u2019. Bạn có thể dùng từ này trong nhiều ngữ cảnh: "
                        "身体健康是最重要的 — Sức khỏe cơ thể là quan trọng nhất. "
                        "Hoặc: 这种生活方式很健康 — Lối sống này rất lành mạnh.\n\n"

                        "Từ thứ tư là 环境 (huánjìng). 环境 là danh từ, có nghĩa là \u2018môi trường\u2019. "
                        "Đây là một chủ đề quan trọng trong bài nói chuyện. Cô Trang giải thích rằng "
                        "cách chúng ta chọn thực phẩm ảnh hưởng trực tiếp đến 环境 — từ đất đai, "
                        "nguồn nước đến không khí. Ví dụ: 保护环境是每个人的责任 — "
                        "Bảo vệ môi trường là trách nhiệm của mỗi người. "
                        "环 là \u2018vòng, bao quanh\u2019 và 境 là \u2018cảnh, ranh giới\u2019. "
                        "环境 là tất cả những gì bao quanh chúng ta. Cách dùng khác: "
                        "这里的环境很好，空气很新鲜 — Môi trường ở đây rất tốt, không khí rất trong lành.\n\n"

                        "Từ thứ năm là 选择 (xuǎnzé). 选择 vừa là danh từ vừa là động từ, có nghĩa là "
                        "\u2018lựa chọn\u2019 hoặc \u2018sự lựa chọn\u2019. Cô Trang nhấn mạnh rằng mỗi lần bạn mua đồ ăn, "
                        "bạn đang đưa ra một 选择 — và mỗi lựa chọn đều có hệ quả. "
                        "Chọn thực phẩm địa phương hay nhập khẩu? Tươi hay đóng gói? "
                        "Ví dụ: 每一次选择都会影响我们的未来 — Mỗi lần lựa chọn đều ảnh hưởng đến tương lai. "
                        "选 là \u2018chọn\u2019 và 择 là \u2018lựa\u2019. Cách dùng: "
                        "你可以选择更健康的生活方式 — Bạn có thể lựa chọn lối sống lành mạnh hơn.\n\n"

                        "Từ cuối cùng trong buổi hôm nay là 未来 (wèilái). 未来 là danh từ, có nghĩa là "
                        "\u2018tương lai\u2019. Đây là từ xuất hiện ngay trong tiêu đề bài nói chuyện: "
                        "吃出更好的未来 — Ăn vì một tương lai tốt đẹp hơn. Cô Trang tin rằng "
                        "khi mỗi người dùng tâm đối xử với thực phẩm, chúng ta đang tạo ra một 未来 tốt hơn. "
                        "Ví dụ: 我们要为未来的孩子保护好环境 — Chúng ta phải bảo vệ môi trường "
                        "cho con cái tương lai. 未 là \u2018chưa\u2019 và 来 là \u2018đến\u2019 — tương lai là điều chưa đến. "
                        "Cách dùng: 未来会更好的 — Tương lai sẽ tốt đẹp hơn.\n\n"

                        "Vậy là bạn đã biết 6 từ đầu tiên: 食物, 做饭, 健康, 环境, 选择, 未来. "
                        "Hãy cùng luyện tập qua các hoạt động tiếp theo nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Thực phẩm và tương lai",
                "description": "Học 6 từ: 食物, 做饭, 健康, 环境, 选择, 未来",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 1",
                "description": "Tập nói 6 từ: 食物, 做饭, 健康, 环境, 选择, 未来",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 1",
                "description": "Nhận biết 6 từ: 食物, 做饭, 健康, 环境, 选择, 未来",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 1",
                "description": "Ghép nghĩa 6 từ: 食物, 做饭, 健康, 环境, 选择, 未来",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_1[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 1",
                "description": "Viết 6 từ: 食物, 做饭, 健康, 环境, 选择, 未来",
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
                        "食物 thường đi với các tính từ để mô tả: 健康的食物 (thực phẩm lành mạnh), "
                        "新鲜的食物 (thực phẩm tươi), 传统食物 (thực phẩm truyền thống). "
                        "Cấu trúc phổ biến: 食物安全 (an toàn thực phẩm), 食物浪费 (lãng phí thực phẩm).\n\n"
                        "做饭 là một cụm động-tân cố định. Bạn có thể thêm trạng từ: "
                        "自己做饭 (tự nấu ăn), 在家做饭 (nấu ăn ở nhà). "
                        "Cấu trúc: 给...做饭 (nấu ăn cho...), 学做饭 (học nấu ăn).\n\n"
                        "健康 làm tính từ: 身体很健康 (cơ thể rất khỏe mạnh). Làm danh từ: "
                        "注意健康 (chú ý sức khỏe). Cụm từ phổ biến: 身心健康 (khỏe mạnh cả thể chất "
                        "lẫn tinh thần), 健康饮食 (ăn uống lành mạnh).\n\n"
                        "环境 thường đi với 保护 hoặc 污染: 保护环境 (bảo vệ môi trường), "
                        "环境污染 (ô nhiễm môi trường). Cấu trúc: 对环境有影响 (có ảnh hưởng đến môi trường).\n\n"
                        "选择 làm động từ: 选择健康的食物 (chọn thực phẩm lành mạnh). "
                        "Làm danh từ: 这是一个好的选择 (đây là một lựa chọn tốt). "
                        "Cấu trúc: 做出选择 (đưa ra lựa chọn), 没有选择 (không có lựa chọn).\n\n"
                        "未来 thường đứng trước danh từ: 未来的生活 (cuộc sống tương lai), "
                        "未来的孩子 (con cái tương lai). Cấu trúc: 在未来 (trong tương lai), "
                        "为了未来 (vì tương lai). Cụm từ hay: 未来可期 (tương lai đáng mong đợi)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 1)",
                "description": "大家好，我是庄祖宜。今天我想跟大家聊一个我最喜欢的话题：食物。",
                "practiceMinutes": 9,
                "data": {"text": READING_1, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 1)",
                "description": "Luyện nói theo đoạn trích về thực phẩm và văn hóa",
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
                "title": "Viết: Thực phẩm và tương lai",
                "description": "Viết câu sử dụng 6 từ vựng buổi 1",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "食物",
                            "prompt": (
                                "Sử dụng từ \u2018食物\u2019 (shíwù) để nói về thực phẩm hoặc đồ ăn — "
                                "như cô Trang nói rằng mỗi miếng thực phẩm đều có một câu chuyện phía sau. "
                                "Ví dụ: 我们应该了解食物从哪里来，这样才能吃得更放心。"
                            ),
                        },
                        {
                            "targetVocab": "做饭",
                            "prompt": (
                                "Sử dụng từ \u2018做饭\u2019 (zuòfàn) để nói về việc nấu ăn — "
                                "như bài nói chuyện nhấn mạnh rằng tự nấu ăn là bước đầu tiên để thay đổi. "
                                "Ví dụ: 周末在家做饭是一件很幸福的事情。"
                            ),
                        },
                        {
                            "targetVocab": "健康",
                            "prompt": (
                                "Sử dụng từ \u2018健康\u2019 (jiànkāng) để nói về sức khỏe — "
                                "như cô Trang kết nối thực phẩm tươi với sức khỏe tốt. "
                                "Ví dụ: 多吃蔬菜水果对身体健康有很大的好处。"
                            ),
                        },
                        {
                            "targetVocab": "环境",
                            "prompt": (
                                "Sử dụng từ \u2018环境\u2019 (huánjìng) để nói về môi trường — "
                                "như bài nói chuyện giải thích rằng lựa chọn thực phẩm ảnh hưởng đến môi trường. "
                                "Ví dụ: 如果我们不保护环境，未来的生活会越来越难。"
                            ),
                        },
                        {
                            "targetVocab": "选择",
                            "prompt": (
                                "Sử dụng từ \u2018选择\u2019 (xuǎnzé) để nói về một sự lựa chọn — "
                                "như cô Trang nhấn mạnh rằng mỗi lần mua đồ ăn là một lựa chọn có hệ quả. "
                                "Ví dụ: 选择当地的食物不仅新鲜，还能帮助农民。"
                            ),
                        },
                        {
                            "targetVocab": "未来",
                            "prompt": (
                                "Sử dụng từ \u2018未来\u2019 (wèilái) để nói về tương lai — "
                                "như tiêu đề bài nói chuyện: ăn vì một tương lai tốt đẹp hơn. "
                                "Ví dụ: 我们今天的选择会决定未来的世界是什么样子。"
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
        "title": "Buổi 2: Chợ và truyền thống — 市场与传统",
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
                        "quan trọng: 食物 (thực phẩm), 做饭 (nấu ăn), 健康 (sức khỏe), 环境 (môi trường), "
                        "选择 (lựa chọn), và 未来 (tương lai). Bạn còn nhớ không? Cô Trang Tổ Nghi đã "
                        "nói rằng mỗi miếng thực phẩm đều có một câu chuyện, và mỗi lựa chọn ăn uống "
                        "đều ảnh hưởng đến tương lai. Hôm nay chúng ta sẽ đi sâu hơn vào phần tiếp theo "
                        "của bài nói chuyện, nơi cô Trang kể về những buổi sáng ở chợ nông dân, "
                        "về hương vị của thực phẩm tươi, và về trí tuệ ẩn giấu trong truyền thống ẩm thực. "
                        "Bạn sẽ học thêm 6 từ mới liên quan đến chợ, nông dân, và văn hóa ẩm thực. "
                        "Hãy sẵn sàng nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 2",
                "description": "Học 6 từ: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng mới của buổi hôm nay. Những từ này nằm ở phần giữa "
                        "bài nói chuyện, khi cô Trang kể về trải nghiệm đi chợ và nấu ăn ở Thượng Hải.\n\n"

                        "Từ đầu tiên là 新鲜 (xīnxiān). 新鲜 là tính từ, có nghĩa là \u2018tươi\u2019 hoặc \u2018mới mẻ\u2019. "
                        "Cô Trang nói rằng khi bạn tự nấu ăn, bạn sẽ bắt đầu quan tâm đến thực phẩm "
                        "có 新鲜 hay không. Một quả cà chua vừa hái từ vườn có hương vị hoàn toàn khác "
                        "so với quả để trong siêu thị cả tuần. Ví dụ: 新鲜的蔬菜味道特别好 — "
                        "Rau tươi có hương vị đặc biệt ngon. 新 là \u2018mới\u2019 và 鲜 là \u2018tươi, thơm\u2019. "
                        "Bạn có thể dùng từ này cho cả thực phẩm và ý tưởng: "
                        "这个想法很新鲜 — Ý tưởng này rất mới mẻ.\n\n"

                        "Từ thứ hai là 农民 (nóngmín). 农民 là danh từ, có nghĩa là \u2018nông dân\u2019. "
                        "Cô Trang khuyến khích mọi người đi chợ nông dân và làm quen với những người "
                        "trồng rau cho mình. Khi bạn biết ai trồng thức ăn của bạn, bạn sẽ tin tưởng hơn. "
                        "Ví dụ: 农民每天早上很早就起来工作 — Nông dân mỗi sáng dậy rất sớm để làm việc. "
                        "农 là \u2018nông, nông nghiệp\u2019 và 民 là \u2018dân, người dân\u2019. "
                        "Cách dùng khác: 我们应该支持当地的农民 — Chúng ta nên ủng hộ nông dân địa phương.\n\n"

                        "Từ thứ ba là 市场 (shìchǎng). 市场 là danh từ, có nghĩa là \u2018chợ\u2019 hoặc \u2018thị trường\u2019. "
                        "Cô Trang nói rằng khi bạn bước vào chợ của một quốc gia, bạn có thể thấy "
                        "người dân ở đó sống như thế nào, họ coi trọng điều gì. "
                        "Ví dụ: 菜市场里的蔬菜比超市的新鲜多了 — Rau ở chợ tươi hơn ở siêu thị nhiều. "
                        "市 là \u2018thành phố, chợ\u2019 và 场 là \u2018bãi, nơi\u2019. "
                        "市场 có thể chỉ chợ truyền thống hoặc thị trường kinh tế: "
                        "农民市场 (chợ nông dân), 市场经济 (kinh tế thị trường).\n\n"

                        "Từ thứ tư là 味道 (wèidào). 味道 là danh từ, có nghĩa là \u2018hương vị\u2019 hoặc \u2018mùi vị\u2019. "
                        "Cô Trang so sánh hương vị của cà chua vừa hái với cà chua siêu thị — "
                        "sự khác biệt là \u201ctrời và đất\u201d. Thực phẩm tươi có 味道 hoàn toàn khác. "
                        "Ví dụ: 妈妈做的菜味道最好 — Món ăn mẹ nấu có hương vị ngon nhất. "
                        "味 là \u2018vị, mùi\u2019 và 道 là \u2018đạo, con đường\u2019. "
                        "Cách dùng: 这个菜的味道怎么样？ — Hương vị món này thế nào? "
                        "Hoặc: 家乡的味道 — Hương vị quê nhà.\n\n"

                        "Từ thứ năm là 传统 (chuántǒng). 传统 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "\u2018truyền thống\u2019. Cô Trang nhấn mạnh rằng mỗi nơi đều có truyền thống ẩm thực riêng, "
                        "và những 传统 này không phải ngẫu nhiên — chúng là trí tuệ của hàng trăm, "
                        "hàng ngàn năm. Ví dụ: 中国有很多传统的美食 — Trung Quốc có rất nhiều món ăn truyền thống. "
                        "传 là \u2018truyền, chuyển giao\u2019 và 统 là \u2018thống, hệ thống\u2019. "
                        "Cách dùng: 传统文化 (văn hóa truyền thống), 传统节日 (lễ hội truyền thống).\n\n"

                        "Từ cuối cùng là 文化 (wénhuà). 文化 là danh từ, có nghĩa là \u2018văn hóa\u2019. "
                        "Cô Trang từng là nghiên cứu sinh ngành nhân học, và cô nhận ra rằng "
                        "食物 là cách trực tiếp nhất để hiểu 文化 của một nơi. "
                        "Ví dụ: 饮食文化是了解一个国家最好的方式 — Văn hóa ẩm thực là cách tốt nhất "
                        "để hiểu một quốc gia. 文 là \u2018văn, chữ viết\u2019 và 化 là \u2018hóa, biến đổi\u2019. "
                        "Cách dùng: 中国文化博大精深 — Văn hóa Trung Quốc rộng lớn và sâu sắc. "
                        "Hoặc: 文化交流 — Giao lưu văn hóa.\n\n"

                        "Vậy là bạn đã học thêm 6 từ mới: 新鲜, 农民, 市场, 味道, 传统, 文化. "
                        "Cùng với 6 từ buổi trước, bạn đã có 12 từ vựng rồi! Hãy luyện tập tiếp nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Chợ và truyền thống",
                "description": "Học 6 từ: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 2",
                "description": "Tập nói 6 từ: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 2",
                "description": "Nhận biết 6 từ: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 2",
                "description": "Ghép nghĩa 6 từ: 新鲜, 农民, 市场, 味道, 传统, 文化",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_2[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 2",
                "description": "Viết 6 từ: 新鲜, 农民, 市场, 味道, 传统, 文化",
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
                        "新鲜 thường đứng trước danh từ: 新鲜的水果 (trái cây tươi), 新鲜空气 (không khí trong lành). "
                        "Cấu trúc: 不新鲜 (không tươi), 很新鲜 (rất tươi). "
                        "Nghĩa bóng: 新鲜事 (chuyện mới lạ), 新鲜感 (cảm giác mới mẻ).\n\n"
                        "农民 thường đi với nghề nghiệp hoặc hoạt động: 农民伯伯 (bác nông dân), "
                        "农民市场 (chợ nông dân). Cấu trúc: 当农民 (làm nông dân), "
                        "农民的生活 (cuộc sống của nông dân).\n\n"
                        "市场 có hai nghĩa chính. Nghĩa cụ thể: 菜市场 (chợ rau), 农民市场 (chợ nông dân). "
                        "Nghĩa trừu tượng: 市场经济 (kinh tế thị trường), 市场需求 (nhu cầu thị trường). "
                        "Cấu trúc: 去市场买菜 (đi chợ mua rau).\n\n"
                        "味道 thường đi với tính từ: 味道很好 (hương vị rất ngon), 味道不错 (hương vị khá tốt), "
                        "味道很奇怪 (hương vị rất kỳ lạ). Cấu trúc: 有...的味道 (có hương vị của...), "
                        "尝一尝味道 (nếm thử hương vị).\n\n"
                        "传统 làm tính từ: 传统文化 (văn hóa truyền thống), 传统美食 (ẩm thực truyền thống). "
                        "Làm danh từ: 保持传统 (giữ gìn truyền thống), 打破传统 (phá vỡ truyền thống). "
                        "Cấu trúc: 有...的传统 (có truyền thống...).\n\n"
                        "文化 thường đi với tính từ hoặc danh từ khác: 中国文化 (văn hóa Trung Quốc), "
                        "饮食文化 (văn hóa ẩm thực), 文化差异 (khác biệt văn hóa). "
                        "Cấu trúc: 了解文化 (tìm hiểu văn hóa), 文化交流 (giao lưu văn hóa)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 2)",
                "description": "那我们能做什么呢？其实很简单。第一步，就是回到厨房，自己做饭。",
                "practiceMinutes": 9,
                "data": {"text": READING_2, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 2)",
                "description": "Luyện nói theo đoạn trích về chợ nông dân và truyền thống",
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
                "title": "Viết: Chợ và truyền thống",
                "description": "Viết câu sử dụng 6 từ vựng buổi 2",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "新鲜",
                            "prompt": (
                                "Sử dụng từ \u2018新鲜\u2019 (xīnxiān) để nói về sự tươi mới — "
                                "như cô Trang so sánh hương vị cà chua tươi với cà chua siêu thị. "
                                "Ví dụ: 早上去市场买的蔬菜特别新鲜，做出来的菜味道也好。"
                            ),
                        },
                        {
                            "targetVocab": "农民",
                            "prompt": (
                                "Sử dụng từ \u2018农民\u2019 (nóngmín) để nói về nông dân — "
                                "như bài nói chuyện khuyến khích làm quen với người trồng rau cho mình. "
                                "Ví dụ: 农民每天辛苦工作，我们应该尊重他们的劳动。"
                            ),
                        },
                        {
                            "targetVocab": "市场",
                            "prompt": (
                                "Sử dụng từ \u2018市场\u2019 (shìchǎng) để nói về chợ hoặc thị trường — "
                                "như cô Trang nói rằng bước vào chợ là cách hiểu văn hóa một nơi. "
                                "Ví dụ: 每个周末我都喜欢去菜市场买新鲜的蔬菜和水果。"
                            ),
                        },
                        {
                            "targetVocab": "味道",
                            "prompt": (
                                "Sử dụng từ \u2018味道\u2019 (wèidào) để nói về hương vị — "
                                "như bài nói chuyện nhấn mạnh rằng thực phẩm tươi có hương vị khác hẳn. "
                                "Ví dụ: 这道菜的味道让我想起了小时候妈妈做的饭。"
                            ),
                        },
                        {
                            "targetVocab": "传统",
                            "prompt": (
                                "Sử dụng từ \u2018传统\u2019 (chuántǒng) để nói về truyền thống — "
                                "như cô Trang giải thích rằng truyền thống ẩm thực là trí tuệ ngàn năm. "
                                "Ví dụ: 传统的饮食方式往往比现代快餐更健康。"
                            ),
                        },
                        {
                            "targetVocab": "文化",
                            "prompt": (
                                "Sử dụng từ \u2018文化\u2019 (wénhuà) để nói về văn hóa — "
                                "như bài nói chuyện cho rằng thực phẩm là cách hiểu văn hóa trực tiếp nhất. "
                                "Ví dụ: 通过一个国家的饮食文化，你可以了解那里的人怎么生活。"
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
        "title": "Buổi 3: Trách nhiệm và hạnh phúc — 责任与幸福",
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
                        "Qua hai buổi trước, bạn đã học 12 từ vựng: 食物, 做饭, 健康, 环境, 选择, 未来 "
                        "ở buổi 1, và 新鲜, 农民, 市场, 味道, 传统, 文化 ở buổi 2. "
                        "Bạn đã hiểu rằng cô Trang Tổ Nghi muốn chúng ta quay lại nhà bếp, "
                        "đi chợ nông dân, và tôn trọng truyền thống ẩm thực. "
                        "Hôm nay, chúng ta sẽ đi vào phần cuối của bài nói chuyện, "
                        "nơi cô Trang nói về trách nhiệm của mỗi người, về việc thay đổi thói quen, "
                        "và về hạnh phúc giản dị đến từ việc nấu ăn. "
                        "6 từ vựng cuối cùng sẽ giúp bạn nói về những giá trị sâu sắc nhất "
                        "trong cuộc sống. Hãy bắt đầu nhé!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. introAudio — vocabulary teaching (500-800 words)
            {
                "activityType": "introAudio",
                "title": "Giới thiệu từ vựng buổi 3",
                "description": "Học 6 từ: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 3,
                "data": {
                    "text": (
                        "Hãy cùng học 6 từ vựng cuối cùng. Đây là những từ nằm ở phần kết của bài nói chuyện, "
                        "khi cô Trang đưa ra thông điệp mạnh mẽ nhất: nấu ăn có thể thay đổi thế giới.\n\n"

                        "Từ đầu tiên là 责任 (zérèn). 责任 là danh từ, có nghĩa là \u2018trách nhiệm\u2019. "
                        "Cô Trang nói rằng việc chọn thực phẩm tốt không chỉ là sở thích cá nhân — "
                        "đó là một 责任. Trách nhiệm với bản thân, với gia đình, và với tự nhiên. "
                        "Ví dụ: 保护环境是每个人的责任 — Bảo vệ môi trường là trách nhiệm của mỗi người. "
                        "责 là \u2018trách, trách cứ\u2019 và 任 là \u2018nhiệm, gánh vác\u2019. "
                        "Cách dùng khác: 父母有责任照顾孩子 — Cha mẹ có trách nhiệm chăm sóc con cái. "
                        "Hoặc: 这是我的责任 — Đây là trách nhiệm của tôi.\n\n"

                        "Từ thứ hai là 改变 (gǎibiàn). 改变 vừa là danh từ vừa là động từ, có nghĩa là "
                        "\u2018thay đổi\u2019. Cô Trang nhấn mạnh rằng 改变 không cần phải lớn lao — "
                        "bạn không cần trở thành người ăn chay ngay ngày mai. Chỉ cần những thay đổi nhỏ "
                        "cũng đủ tạo ra sự khác biệt. Ví dụ: 小小的改变可以带来大大的不同 — "
                        "Những thay đổi nhỏ có thể mang lại sự khác biệt lớn. "
                        "改 là \u2018sửa, cải\u2019 và 变 là \u2018biến, thay đổi\u2019. "
                        "Cách dùng: 改变世界从改变自己开始 — Thay đổi thế giới bắt đầu từ thay đổi bản thân. "
                        "Hoặc: 这件事改变了我的想法 — Việc này đã thay đổi suy nghĩ của tôi.\n\n"

                        "Từ thứ ba là 习惯 (xíguàn). 习惯 vừa là danh từ vừa là động từ, có nghĩa là "
                        "\u2018thói quen\u2019 hoặc \u2018quen\u2019. Cô Trang nói rằng nếu chúng ta không thay đổi "
                        "饮食习惯 — thói quen ăn uống — thì tương lai sẽ rất đáng lo. "
                        "Ví dụ: 养成好的饮食习惯对健康很重要 — Hình thành thói quen ăn uống tốt "
                        "rất quan trọng cho sức khỏe. 习 là \u2018tập, luyện\u2019 và 惯 là \u2018quen\u2019. "
                        "Làm động từ: 我已经习惯了早起 — Tôi đã quen dậy sớm rồi. "
                        "Cách dùng: 改变习惯需要时间 — Thay đổi thói quen cần thời gian.\n\n"

                        "Từ thứ tư là 自然 (zìrán). 自然 vừa là danh từ vừa là tính từ và phó từ, "
                        "có nghĩa là \u2018tự nhiên\u2019 hoặc \u2018thiên nhiên\u2019. Cô Trang nói rằng chúng ta có "
                        "trách nhiệm với 自然 — với thiên nhiên. Khi chúng ta chọn thực phẩm bền vững, "
                        "chúng ta đang bảo vệ tự nhiên. Ví dụ: 大自然给了我们最好的食物 — "
                        "Thiên nhiên đã cho chúng ta thực phẩm tốt nhất. "
                        "自 là \u2018tự, bản thân\u2019 và 然 là \u2018nhiên, như vậy\u2019. "
                        "Làm tính từ: 这种变化是很自然的 — Sự thay đổi này rất tự nhiên. "
                        "Làm phó từ: 你会自然而然地开始关心食物 — Bạn sẽ tự nhiên bắt đầu quan tâm đến thực phẩm.\n\n"

                        "Từ thứ năm là 简单 (jiǎndān). 简单 là tính từ, có nghĩa là \u2018đơn giản\u2019 hoặc \u2018giản dị\u2019. "
                        "Cô Trang nhấn mạnh rằng thay đổi không cần phức tạp — chỉ cần những bước 简单: "
                        "đi chợ thay vì siêu thị, mua rau theo mùa, tự nấu ăn thay vì gọi đồ ăn ngoài. "
                        "Ví dụ: 做饭是一件简单的事情，但它可以改变世界 — Nấu ăn là một việc đơn giản, "
                        "nhưng nó có thể thay đổi thế giới. 简 là \u2018giản, đơn giản\u2019 và 单 là \u2018đơn, một mình\u2019. "
                        "Cách dùng: 简单的生活最幸福 — Cuộc sống giản dị là hạnh phúc nhất. "
                        "Hoặc: 这个问题很简单 — Vấn đề này rất đơn giản.\n\n"

                        "Từ cuối cùng là 幸福 (xìngfú). 幸福 vừa là danh từ vừa là tính từ, có nghĩa là "
                        "\u2018hạnh phúc\u2019. Cô Trang kết thúc bài nói chuyện bằng một thông điệp đẹp: "
                        "khi chúng ta dùng tâm đối xử với thực phẩm, quá trình đó chính là 幸福. "
                        "Nấu ăn cho người thân, chia sẻ bữa cơm gia đình — đó là hạnh phúc giản dị. "
                        "Ví dụ: 和家人一起吃饭是一种简单的幸福 — Ăn cơm cùng gia đình là một loại "
                        "hạnh phúc giản dị. 幸 là \u2018may mắn\u2019 và 福 là \u2018phúc, phước\u2019. "
                        "Cách dùng: 幸福不在远方，就在身边 — Hạnh phúc không ở nơi xa, mà ở ngay bên cạnh. "
                        "Hoặc: 我觉得自己很幸福 — Tôi thấy mình rất hạnh phúc.\n\n"

                        "Tuyệt vời! Bạn đã học xong toàn bộ 18 từ vựng: 食物, 做饭, 健康, 环境, 选择, 未来, "
                        "新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福. "
                        "Hãy luyện tập qua các hoạt động tiếp theo!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 3. viewFlashcards
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Trách nhiệm và hạnh phúc",
                "description": "Học 6 từ: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 4. speakFlashcards
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói từ vựng buổi 3",
                "description": "Tập nói 6 từ: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 5. vocabLevel1
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết từ vựng buổi 3",
                "description": "Nhận biết 6 từ: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 2,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 6. vocabLevel2
            {
                "activityType": "vocabLevel2",
                "title": "Flashcards: Ghép nghĩa từ vựng buổi 3",
                "description": "Ghép nghĩa 6 từ: 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 3,
                "data": {"vocabList": VOCAB_GROUP_3[:], "audioSpeed": 0},
            },
            # 7. vocabLevel3
            {
                "activityType": "vocabLevel3",
                "title": "Flashcards: Viết từ vựng buổi 3",
                "description": "Viết 6 từ: 责任, 改变, 习惯, 自然, 简单, 幸福",
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
                        "责任 thường đi với 有 hoặc 是: 有责任 (có trách nhiệm), "
                        "这是我的责任 (đây là trách nhiệm của tôi). Cấu trúc: 对...有责任 (có trách nhiệm với...), "
                        "负责任 (chịu trách nhiệm), 责任感 (tinh thần trách nhiệm).\n\n"
                        "改变 làm động từ: 改变习惯 (thay đổi thói quen), 改变世界 (thay đổi thế giới). "
                        "Làm danh từ: 一个大的改变 (một thay đổi lớn). "
                        "Cấu trúc: 被...改变 (bị...thay đổi), 想要改变 (muốn thay đổi).\n\n"
                        "习惯 làm danh từ: 好习惯 (thói quen tốt), 坏习惯 (thói quen xấu), "
                        "生活习惯 (thói quen sinh hoạt). Làm động từ: 习惯了 (đã quen rồi). "
                        "Cấu trúc: 养成习惯 (hình thành thói quen), 改掉习惯 (bỏ thói quen).\n\n"
                        "自然 làm danh từ: 大自然 (thiên nhiên), 自然界 (giới tự nhiên). "
                        "Làm tính từ: 很自然 (rất tự nhiên), 自然的食物 (thực phẩm tự nhiên). "
                        "Làm phó từ: 自然而然 (tự nhiên mà thành). Cấu trúc: 回归自然 (trở về với tự nhiên).\n\n"
                        "简单 thường đi với 很 hoặc 不: 很简单 (rất đơn giản), 不简单 (không đơn giản). "
                        "Cấu trúc: 简单来说 (nói đơn giản), 简简单单 (giản dị, mộc mạc). "
                        "Nghĩa bóng: 他不简单 (anh ấy không đơn giản = anh ấy giỏi lắm).\n\n"
                        "幸福 làm tính từ: 很幸福 (rất hạnh phúc), 幸福的生活 (cuộc sống hạnh phúc). "
                        "Làm danh từ: 追求幸福 (theo đuổi hạnh phúc), 幸福感 (cảm giác hạnh phúc). "
                        "Cấu trúc: 感到幸福 (cảm thấy hạnh phúc), 幸福就在身边 (hạnh phúc ở ngay bên cạnh)."
                    ),
                    "audioSpeed": 0,
                },
            },
            # 9. reading
            {
                "activityType": "reading",
                "title": "Đọc: Đoạn trích bài nói chuyện (phần 3)",
                "description": "我知道有人会说：我很忙，没有时间做饭。",
                "practiceMinutes": 5,
                "data": {"text": READING_3, "audioSpeed": 0},
            },
            # 10. speakReading
            {
                "activityType": "speakReading",
                "title": "Tập nói: Đoạn trích bài nói chuyện (phần 3)",
                "description": "Luyện nói theo đoạn trích về trách nhiệm và hạnh phúc",
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
                "title": "Viết: Trách nhiệm và hạnh phúc",
                "description": "Viết câu sử dụng 6 từ vựng buổi 3",
                "practiceMinutes": 12,
                "data": {
                    "items": [
                        {
                            "targetVocab": "责任",
                            "prompt": (
                                "Sử dụng từ \u2018责任\u2019 (zérèn) để nói về trách nhiệm — "
                                "như cô Trang nói rằng chọn thực phẩm tốt là trách nhiệm với bản thân và tự nhiên. "
                                "Ví dụ: 每个人都有责任保护我们生活的环境。"
                            ),
                        },
                        {
                            "targetVocab": "改变",
                            "prompt": (
                                "Sử dụng từ \u2018改变\u2019 (gǎibiàn) để nói về sự thay đổi — "
                                "như bài nói chuyện nhấn mạnh rằng thay đổi nhỏ cũng tạo ra sự khác biệt lớn. "
                                "Ví dụ: 只要我们愿意改变，未来一定会更好。"
                            ),
                        },
                        {
                            "targetVocab": "习惯",
                            "prompt": (
                                "Sử dụng từ \u2018习惯\u2019 (xíguàn) để nói về thói quen — "
                                "như cô Trang kêu gọi thay đổi thói quen ăn uống để bảo vệ tương lai. "
                                "Ví dụ: 养成每天运动的习惯对身体健康非常有好处。"
                            ),
                        },
                        {
                            "targetVocab": "自然",
                            "prompt": (
                                "Sử dụng từ \u2018自然\u2019 (zìrán) để nói về thiên nhiên hoặc sự tự nhiên — "
                                "như bài nói chuyện nhấn mạnh trách nhiệm của chúng ta với tự nhiên. "
                                "Ví dụ: 大自然给了我们一切，我们应该好好保护它。"
                            ),
                        },
                        {
                            "targetVocab": "简单",
                            "prompt": (
                                "Sử dụng từ \u2018简单\u2019 (jiǎndān) để nói về sự đơn giản — "
                                "như cô Trang nói rằng nấu ăn là việc đơn giản nhưng có thể thay đổi thế giới. "
                                "Ví dụ: 有时候最简单的食物反而是最好吃的。"
                            ),
                        },
                        {
                            "targetVocab": "幸福",
                            "prompt": (
                                "Sử dụng từ \u2018幸福\u2019 (xìngfú) để nói về hạnh phúc — "
                                "như bài nói chuyện kết thúc với thông điệp: dùng tâm đối xử với thực phẩm là hạnh phúc. "
                                "Ví dụ: 和家人一起做饭、一起吃饭，就是最大的幸福。"
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
                        "về chủ đề thực phẩm, nấu ăn và bền vững. Hãy cùng ôn lại nhé!\n\n"
                        "Buổi 1, bạn đã học: 食物 (thực phẩm), 做饭 (nấu ăn), 健康 (sức khỏe), "
                        "环境 (môi trường), 选择 (lựa chọn), 未来 (tương lai). Đây là những từ nền tảng "
                        "giúp bạn nói về mối quan hệ giữa thực phẩm và cuộc sống.\n\n"
                        "Buổi 2, bạn đã học: 新鲜 (tươi), 农民 (nông dân), 市场 (chợ), "
                        "味道 (hương vị), 传统 (truyền thống), 文化 (văn hóa). Những từ này giúp bạn nói về "
                        "trải nghiệm đi chợ và văn hóa ẩm thực.\n\n"
                        "Buổi 3, bạn đã học: 责任 (trách nhiệm), 改变 (thay đổi), 习惯 (thói quen), "
                        "自然 (tự nhiên), 简单 (đơn giản), 幸福 (hạnh phúc). Đây là những từ "
                        "giúp bạn hiểu rằng nấu ăn có ý thức là trách nhiệm và cũng là hạnh phúc.\n\n"
                        "Bây giờ hãy ôn tập toàn bộ 18 từ qua các hoạt động flashcard!"
                    ),
                    "audioSpeed": 0,
                },
            },
            # 2. viewFlashcards — all 18 words
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập toàn bộ 18 từ vựng",
                "description": "Ôn tập 18 từ: 食物, 做饭, 健康, 环境, 选择, 未来, 新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 3. speakFlashcards — all 18 words
            {
                "activityType": "speakFlashcards",
                "title": "Flashcards: Tập nói toàn bộ 18 từ vựng",
                "description": "Tập nói 18 từ: 食物, 做饭, 健康, 环境, 选择, 未来, 新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福",
                "practiceMinutes": 5,
                "data": {"vocabList": ALL_VOCAB[:], "audioSpeed": 0},
            },
            # 4. vocabLevel1 — all 18 words
            {
                "activityType": "vocabLevel1",
                "title": "Flashcards: Nhận biết toàn bộ từ vựng",
                "description": "Nhận biết 18 từ: 食物, 做饭, 健康, 环境, 选择, 未来, 新鲜, 农民, 市场, 味道, 传统, 文化, 责任, 改变, 习惯, 自然, 简单, 幸福",
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
                        "của cô Trang Tổ Nghi từ đầu đến cuối. Bạn đã học 18 từ vựng qua 3 buổi học "
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
                "description": "大家好，我是庄祖宜。今天我想跟大家聊一个我最喜欢的话题：食物。",
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

                        "食物 (shíwù) — thực phẩm, đồ ăn. Ví dụ: 了解食物的来源是对自己负责 — "
                        "Tìm hiểu nguồn gốc thực phẩm là có trách nhiệm với bản thân.\n\n"

                        "做饭 (zuòfàn) — nấu ăn, nấu cơm. Ví dụ: 学会做饭是一种生活技能 — "
                        "Học nấu ăn là một kỹ năng sống.\n\n"

                        "健康 (jiànkāng) — sức khỏe, khỏe mạnh. Ví dụ: 好的食物是健康的基础 — "
                        "Thực phẩm tốt là nền tảng của sức khỏe.\n\n"

                        "环境 (huánjìng) — môi trường. Ví dụ: 每一次购物都是对环境的投票 — "
                        "Mỗi lần mua sắm đều là một lá phiếu cho môi trường.\n\n"

                        "选择 (xuǎnzé) — lựa chọn. Ví dụ: 聪明的选择从了解开始 — "
                        "Lựa chọn thông minh bắt đầu từ sự hiểu biết.\n\n"

                        "未来 (wèilái) — tương lai. Ví dụ: 我们的选择决定了未来的样子 — "
                        "Lựa chọn của chúng ta quyết định hình dáng tương lai.\n\n"

                        "新鲜 (xīnxiān) — tươi, mới mẻ. Ví dụ: 新鲜的食材不需要复杂的烹饪 — "
                        "Nguyên liệu tươi không cần nấu nướng phức tạp.\n\n"

                        "农民 (nóngmín) — nông dân. Ví dụ: 感谢农民的辛苦劳动 — "
                        "Cảm ơn sự lao động vất vả của nông dân.\n\n"

                        "市场 (shìchǎng) — chợ, thị trường. Ví dụ: 菜市场是城市最有生命力的地方 — "
                        "Chợ rau là nơi có sức sống nhất trong thành phố.\n\n"

                        "味道 (wèidào) — hương vị, mùi vị. Ví dụ: 记忆中最好的味道是家的味道 — "
                        "Hương vị ngon nhất trong ký ức là hương vị của nhà.\n\n"

                        "传统 (chuántǒng) — truyền thống. Ví dụ: 传统的智慧值得我们学习 — "
                        "Trí tuệ truyền thống đáng để chúng ta học hỏi.\n\n"

                        "文化 (wénhuà) — văn hóa. Ví dụ: 食物是文化最美味的表达 — "
                        "Thực phẩm là cách biểu đạt ngon nhất của văn hóa.\n\n"

                        "责任 (zérèn) — trách nhiệm. Ví dụ: 吃得好是对自己和地球的责任 — "
                        "Ăn uống tốt là trách nhiệm với bản thân và trái đất.\n\n"

                        "改变 (gǎibiàn) — thay đổi. Ví dụ: 每一个小改变都有意义 — "
                        "Mỗi thay đổi nhỏ đều có ý nghĩa.\n\n"

                        "习惯 (xíguàn) — thói quen. Ví dụ: 好的习惯会带来好的生活 — "
                        "Thói quen tốt sẽ mang lại cuộc sống tốt.\n\n"

                        "自然 (zìrán) — tự nhiên, thiên nhiên. Ví dụ: 尊重自然就是尊重自己 — "
                        "Tôn trọng tự nhiên chính là tôn trọng bản thân.\n\n"

                        "简单 (jiǎndān) — đơn giản, giản dị. Ví dụ: 简单的食物，简单的快乐 — "
                        "Thực phẩm giản dị, niềm vui giản dị.\n\n"

                        "幸福 (xìngfú) — hạnh phúc. Ví dụ: 用心做饭，用心生活，这就是幸福 — "
                        "Dùng tâm nấu ăn, dùng tâm sống, đó chính là hạnh phúc.\n\n"

                        "Như cô Trang Tổ Nghi đã nói: 做饭是一件简单的事情，但它可以改变世界 — "
                        "Nấu ăn là một việc đơn giản, nhưng nó có thể thay đổi thế giới. "
                        "Bạn đã không chỉ học được 18 từ vựng tiếng Trung, mà còn hiểu sâu hơn "
                        "về mối quan hệ giữa thực phẩm, văn hóa và tương lai. "
                        "Hãy nhớ: mỗi bữa ăn là một cơ hội để tạo ra sự thay đổi. "
                        "Cảm ơn bạn đã đồng hành, và chúc bạn luôn ăn ngon, sống khỏe, "
                        "và tìm thấy hạnh phúc trong những điều giản dị nhất! 再见！"
                    ),
                    "audioSpeed": 0,
                },
            },
        ],
    }


    # ── Assemble content ──

    content = {
        "title": "Học Qua Podcast: '吃出更好的未來' — 莊祖宜 (Ăn vì một tương lai tốt đẹp hơn)",
        "description": (
            "BẠN CÓ BIẾT MỖI BỮA ĂN CỦA BẠN ĐANG QUYẾT ĐỊNH TƯƠNG LAI CỦA TRÁI ĐẤT?\n\n"
            "Mỗi lần bạn chọn mua rau ở siêu thị thay vì chợ, mỗi lần bạn gọi đồ ăn ngoài "
            "thay vì tự nấu, mỗi lần bạn bỏ qua câu hỏi \u201cthức ăn này từ đâu đến?\u201d — "
            "bạn đang vô tình góp phần vào một vòng xoáy: đất đai cạn kiệt, nguồn nước ô nhiễm, "
            "và thực phẩm ngày càng mất đi hương vị thật.\n\n"
            "Nhà văn ẩm thực và đầu bếp Trang Tổ Nghi (莊祖宜) từ TED Shanghai sẽ mở mắt bạn: "
            "cô từng bỏ nghiên cứu nhân học để vào trường đầu bếp, vì nhận ra rằng bước vào "
            "chợ của một quốc gia là cách nhanh nhất để hiểu văn hóa nơi đó. "
            "Cô Trang cho rằng nấu ăn có ý thức — chọn nguyên liệu tươi, ủng hộ nông dân "
            "địa phương, tôn trọng truyền thống ẩm thực — không chỉ là niềm vui cá nhân "
            "mà còn là trách nhiệm với tự nhiên và tương lai.\n\n"
            "Khi bạn quay lại nhà bếp và dùng tâm đối xử với từng miếng thực phẩm, "
            "bạn không chỉ đang nấu ăn — bạn đang tạo ra một tương lai tốt đẹp hơn. "
            "Và quá trình đó, chính là hạnh phúc.\n\n"
            "Học 18 từ vựng đắt giá về ẩm thực, văn hóa và bền vững cùng trải nghiệm "
            "đa giác quan giúp bạn vừa nâng cấp tư duy, vừa nâng trình tiếng Trung một cách vượt bậc."
        ),
        "preview": {
            "text": (
                "Bạn có biết rằng mỗi bữa ăn là một lá phiếu cho tương lai? "
                "Đầu bếp và nhà văn ẩm thực Trang Tổ Nghi từ TED Shanghai sẽ thay đổi hoàn toàn "
                "cách bạn nhìn nhận việc nấu ăn và chọn thực phẩm. Trong khóa học này, bạn sẽ học "
                "18 từ vựng tiếng Trung cấp độ HSK2-HSK3 về ẩm thực và bền vững: "
                "食物 (thực phẩm), 做饭 (nấu ăn), 健康 (sức khỏe), 环境 (môi trường), "
                "选择 (lựa chọn), 未来 (tương lai), 新鲜 (tươi), 农民 (nông dân), "
                "市场 (chợ), 味道 (hương vị), 传统 (truyền thống), 文化 (văn hóa), "
                "责任 (trách nhiệm), 改变 (thay đổi), 习惯 (thói quen), 自然 (tự nhiên), "
                "简单 (đơn giản), 幸福 (hạnh phúc). Qua 5 buổi học với flashcard, bài đọc, "
                "luyện nói và viết câu, bạn sẽ không chỉ nắm vững từ vựng mà còn hiểu sâu hơn "
                "về cách thực phẩm kết nối văn hóa, thiên nhiên và hạnh phúc — "
                "và biến mỗi bữa ăn thành một hành động thay đổi thế giới."
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
