#!/usr/bin/env python3
"""Chapter 6: Sam's Story — bilingual Vietnamese-English curriculum."""

import json, sys, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API_URL = "https://helloapi.step.is/curriculum/create"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
KEYS_TO_STRIP = {"mp3Url","illustrationSet","chapterBookmarks","segments",
    "whiteboardItems","userReadingId","lessonUniqueId","curriculumTags","taskId","imageId"}

def strip_keys(obj, keys):
    if isinstance(obj, dict):
        return {k: strip_keys(v, keys) for k, v in obj.items() if k not in keys}
    if isinstance(obj, list):
        return [strip_keys(i, keys) for i in obj]
    return obj

SECTION_1 = (
    "The next morning, Maya drove into town. She needed to talk to someone — someone who would be honest with her. She "
    "thought of Sam at the café.\n\n"
    "The Wheelhouse was quiet when she arrived. It was early, and only a few fishermen sat at the tables, eating breakfast "
    "before heading to the harbor. Sam was behind the counter, as usual.\n\n"
    '"Morning," he said, pouring her coffee. "You look tired."\n\n'
    '"I\'ve been reading a lot," Maya said. She wrapped her hands around the warm cup. "Sam, can I ask you something?"\n\n'
    '"Sure."\n\n'
    '"What do you know about the Keepers?"\n\n'
    "Sam's hand stopped mid-pour. He set the coffee pot down carefully and looked at Maya. His friendly expression didn't "
    "change, but something shifted behind his eyes.\n\n"
    '"Where did you hear that name?" he asked.\n\n'
    '"My grandmother\'s journals. She wrote about a group of families in town who knew about... about what\'s under the '
    'house. She called them the Keepers."\n\n'
    "Sam was quiet for a moment. He looked around the café, then leaned closer.\n\n"
    '"Not here," he said. "Come back at two. The café closes between two and four. We can talk then."'
)

SECTION_2 = (
    "Maya nodded. She drank her coffee, ate a piece of toast, and left. She spent the morning walking around town, trying "
    "to learn its geography. Alder Bay was small but spread out. The main street ran along the harbor. Behind it, residential "
    "streets climbed the hillside in neat rows. To the north, Cliff Road led up to Alder House. To the south, a path "
    "followed the coast to a lighthouse that Maya could see in the distance.\n\n"
    "She walked to the lighthouse. It was old and no longer working — the light at the top was dark, and the door was "
    "padlocked. A sign said it had been built in 1887, five years before Alder House.\n\n"
    "Maya stood at the base of the lighthouse and looked north along the coast. She could see the cliff where Alder House "
    "stood, dark and solid against the sky. From this angle, she could also see something she hadn't noticed before — a path, "
    "or maybe stairs, cut into the face of the cliff below the house. They led down to a small beach at the base of the "
    "cliff, hidden from the town by rocks.\n\n"
    "She made a mental note to explore that later."
)

SECTION_3 = (
    'At two o\'clock, she returned to The Wheelhouse. Sam had locked the front door and turned the sign to "Closed." He '
    "let her in and led her to a table in the back corner.\n\n"
    '"Okay," he said, sitting across from her. "The Keepers. What do you want to know?"\n\n'
    '"Everything."\n\n'
    'Sam ran a hand through his curly hair. "I don\'t know everything. But I know more than most people in town." He paused. '
    '"My grandmother was one of them."\n\n'
    '"Your grandmother?"\n\n'
    '"Yeah. Her name was Dolores. She died when I was fifteen. But before she died, she told me things. She said I needed to '
    'know, in case..." He trailed off.\n\n'
    '"In case what?"\n\n'
    '"In case something happened with the light."\n\n'
    "Maya felt a chill. \"So you know about the light.\"\n\n"
    '"I know it exists. I\'ve never seen it. But my grandmother described it to me. She said it was beautiful and terrible '
    'at the same time." Sam looked down at his hands. "She said it was the reason Alder Bay exists. The town was built here '
    'because of the light — or rather, because of the people who came to guard it."'
)

SECTION_4 = (
    '"Guard it from what?"\n\n'
    '"From getting out. From spreading. My grandmother said the light is like... like water behind a dam. It\'s always '
    'pushing, always looking for cracks. And if the dam breaks..." He shook his head. "She never told me exactly what would '
    'happen. But she was scared of it. Really scared."\n\n'
    '"Eleanor wrote about the Keepers," Maya said. "She said they wanted to destroy the light. Seal the hole permanently."\n\n'
    'Sam nodded slowly. "That\'s what some of them wanted. Not all. There were always two sides. Some thought the light '
    'should be destroyed. Others thought it should be studied, understood. They argued about it for decades."\n\n'
    '"Which side was your grandmother on?"\n\n'
    '"She was somewhere in the middle. She thought the light was dangerous, but she also thought destroying it might be '
    'worse. She said you can\'t just erase something that old and that powerful without consequences."\n\n'
    '"Smart woman," Maya said.\n\n'
    '"She was." Sam smiled sadly. "She also said something else. She said the light was connected to the Voss family in a '
    "way that nobody fully understood. That the Voss women had a bond with it — like a mother and child, or like two halves "
    "of the same thing. She said that's why a Voss always had to live in the house. Not just to guard the light, but because "
    'the light needed them. Without a Voss, it would become... unstable."'
)

SECTION_5 = (
    "Maya thought about the three months since Eleanor's death. Three months with no Voss in the house.\n\n"
    '"Sam," she said carefully. "Has anything strange happened in town recently? Since my grandmother died?"\n\n'
    "Sam's expression changed. He looked uncomfortable.\n\n"
    '"What?" Maya pressed.\n\n'
    '"There have been... things. Small things. The tides have been wrong — higher than they should be, at the wrong times. '
    "Fish have been disappearing from the bay. And people have been having dreams.\"\n\n"
    '"Dreams?"\n\n'
    '"Bad dreams. The same dream, actually. Half the town has had it. A dream about blue light coming out of the ocean. '
    'About the water rising and the town disappearing." He paused. "My mom had it three times last week."\n\n'
    "Maya's stomach tightened. \"The light is getting restless. Because Eleanor is gone.\"\n\n"
    '"That\'s what I think, yeah." Sam looked at her directly. "Maya, I don\'t want to pressure you. But if what my '
    "grandmother said is true — if the light needs a Voss — then you might be the only person who can calm it down.\"\n\n"
    '"By doing what? Going into the basement?"\n\n'
    '"I don\'t know. Maybe. Or maybe just being in the house is enough. Eleanor lived there for fifty years, and the light '
    'stayed contained. Maybe your presence alone will help."\n\n'
    "Maya thought about the knocking she had heard last night. Three slow knocks from below the floor.\n\n"
    '"There\'s something else," she said. "Eleanor\'s letter warned me not to trust everyone in town. And a man named Frank '
    'Burke told me to sell the house and leave."\n\n'
    "Sam's jaw tightened. \"Frank Burke. Yeah. He's Harold Burke's son.\"\n\n"
    '"Harold Burke — the leader of the Keepers?"\n\n'
    '"Was the leader. Harold died about ten years ago. Frank took over." Sam lowered his voice. "Frank is not like his '
    "father. Harold was tough but fair. Frank is... angry. He's been angry his whole life. He thinks the light is evil, and "
    "he thinks the Voss family is responsible for keeping it alive.\"\n\n"
    '"What does he want?"\n\n'
    '"He wants to seal the basement. Pour concrete into the hole, fill it up, bury it forever. He\'s been talking about it '
    "for years. Eleanor wouldn't let him near the house. But now that Eleanor is gone...\"\n\n"
    '"He thinks he can do it," Maya finished.\n\n'
    '"He thinks he should do it. And he\'s not the kind of man who waits for permission."\n\n'
    "Maya sat back in her chair. The café was quiet around them, but her mind was loud with thoughts.\n\n"
    "A light that needed her. A man who wanted to destroy it. A town full of secrets and bad dreams.\n\n"
    "And she had been here less than a week.\n\n"
    '"Sam," she said. "Will you help me?"\n\n'
    "He looked at her for a long moment. Then he nodded.\n\n"
    '"Yeah," he said. "I will."\n\n'
    '"Good. Because I think I need to go into the basement. And I don\'t want to do it alone."\n\n'
    "Sam's face went pale, but he didn't look away.\n\n"
    '"When?" he asked.\n\n'
    "Maya looked out the window at the gray sky.\n\n"
    '"Tonight," she said.'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["shifted", "leaned", "expression", "mid-pour"]
S2_VOCAB = ["geography", "residential", "lighthouse", "padlocked"]
S3_VOCAB = ["trailed", "chill", "guard", "terrible"]
S4_VOCAB = ["dam", "permanently", "consequences", "unstable"]
S5_VOCAB = ["tides", "pressure", "concrete", "permission"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 6: Câu Chuyện Của Sam (Sam's Story)",
        "preview": {
            "text": (
                "Maya hỏi Sam về nhóm Keepers và biết bà nội Sam cũng là thành viên. Sam kể "
                "về ánh sáng, mối liên kết với gia đình Voss, và những giấc mơ xấu đang ám "
                "ảnh cả thị trấn. Frank Burke muốn đổ bê tông lấp tầng hầm. Maya quyết định "
                "xuống tầng hầm tối nay — và nhờ Sam đi cùng."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 6. Sam tiết lộ bí mật về nhóm "
            "Keepers, mối đe dọa từ Frank Burke, và Maya quyết định đối mặt với ánh sáng."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Hỏi Sam về Keepers",
                "activities": [
                    {"title": "Flashcards: Hỏi Sam về Keepers",
                     "description": "Học 4 từ: shifted, leaned, expression, mid-pour",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Hỏi Sam về Keepers",
                     "description": "Maya hỏi Sam về nhóm Keepers — anh ấy im lặng rồi hẹn gặp lúc hai giờ khi quán đóng cửa.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Hỏi Sam về Keepers",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Khám phá thị trấn",
                "activities": [
                    {"title": "Flashcards: Khám phá thị trấn",
                     "description": "Học 4 từ: geography, residential, lighthouse, padlocked",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Khám phá thị trấn",
                     "description": "Maya đi bộ quanh thị trấn, đến ngọn hải đăng cũ, và phát hiện con đường bí mật trên vách đá dưới Alder House.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Khám phá thị trấn",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Bà nội của Sam",
                "activities": [
                    {"title": "Flashcards: Bà nội của Sam",
                     "description": "Học 4 từ: trailed, chill, guard, terrible",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bà nội của Sam",
                     "description": "Sam kể bà nội Dolores là thành viên Keepers — bà mô tả ánh sáng vừa đẹp vừa đáng sợ.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bà nội của Sam",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Nước sau con đập",
                "activities": [
                    {"title": "Flashcards: Nước sau con đập",
                     "description": "Học 4 từ: dam, permanently, consequences, unstable",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nước sau con đập",
                     "description": "Ánh sáng như nước sau con đập — luôn tìm kẽ hở. Gia đình Voss có mối liên kết đặc biệt mà không ai hiểu hết.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nước sau con đập",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Quyết định xuống tầng hầm",
                "activities": [
                    {"title": "Flashcards: Quyết định xuống tầng hầm",
                     "description": "Học 4 từ: tides, pressure, concrete, permission",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Quyết định xuống tầng hầm",
                     "description": "Thủy triều sai, cá biến mất, giấc mơ xấu khắp thị trấn. Maya quyết định xuống tầng hầm tối nay — Sam đồng ý đi cùng.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Quyết định xuống tầng hầm",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 6",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 6 từ cuộc trò chuyện với Sam đến quyết định xuống tầng hầm.",
                     "activityType": "readAlong", "practiceMinutes": 10,
                     "data": {"text": FULL_CHAPTER, "audioSpeed": -0.2}},
                ],
            },
        ],
    }

def main():
    token = get_firebase_id_token(UID)
    content = strip_keys(build_curriculum(), KEYS_TO_STRIP)
    payload = {"uid": UID, "language": "en", "userLanguage": "vi",
               "content": json.dumps(content, ensure_ascii=False), "firebaseIdToken": token}
    resp = requests.post(API_URL, json=payload)
    resp.raise_for_status()
    cid = resp.json().get("id", "unknown")
    print(f"Chapter 6 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
