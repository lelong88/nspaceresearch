#!/usr/bin/env python3
"""Chapter 4: Moving In — bilingual Vietnamese-English curriculum."""

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
    "Maya drove back to Portland that afternoon. She packed two suitcases, arranged for her neighbor to watch Oliver for a "
    "week, and told her boss she needed some time off.\n\n"
    '"Family stuff," she said on the phone.\n\n'
    '"Take as long as you need," her boss said. "You\'ve got three weeks of vacation saved up."\n\n'
    "By Monday morning, she was back in Alder Bay. She stopped at the grocery store to buy food, cleaning supplies, and "
    "candles — the house had electricity, but she didn't fully trust it.\n\n"
    "The woman at the checkout counter was young, maybe Maya's age, with red hair pulled back in a ponytail. Her name tag "
    'said "Lily."\n\n'
    '"Big shopping trip," Lily said, scanning the items.\n\n'
    '"I\'m moving into Alder House," Maya said.\n\n'
    "Lily's hands stopped moving. She looked up at Maya with wide green eyes. \"You're living there? In the house?\"\n\n"
    '"It\'s my house now. My grandmother left it to me."'
)

SECTION_2 = (
    "Lily finished scanning in silence. When Maya paid, Lily leaned forward and spoke quietly.\n\n"
    '"Be careful up there. Especially at night."\n\n'
    '"Why? What happens at night?"\n\n'
    "Lily glanced at the other customers in the store. \"The light,\" she whispered. \"Sometimes you can see it from town. "
    "A glow, coming from the cliff. It's been happening for years. Eleanor used to say it was just a lamp, but...\" She "
    "shook her head. \"It's not a lamp.\"\n\n"
    '"How do you know?"\n\n'
    '"Because it moves. It comes from inside the house, and then it moves outside, along the cliff. Like it\'s looking for '
    'something." Lily handed Maya her bags. "Just be careful. Okay?"\n\n'
    "Maya thanked her and left. She loaded the groceries into her car and sat for a moment, thinking.\n\n"
    "A light that moves. A light that looks for something.\n\n"
    "She drove up Cliff Road and parked inside the gate this time. The house looked different in the daylight — less "
    "threatening, more sad. Like an old person sitting alone, waiting for company."
)

SECTION_3 = (
    "Maya spent the rest of the day cleaning. She started with the kitchen, scrubbing the counters and stove, washing the "
    "dishes that Eleanor had left. She opened windows to let in fresh air, even though the wind was cold. She swept the "
    "floors and dusted the furniture.\n\n"
    "As she worked, she explored. The house was full of interesting things. In the living room, she found a collection of "
    "glass bottles in different colors — blue, green, amber, red — arranged on a shelf by the window. When the light came "
    "through them, they cast colored shadows across the floor.\n\n"
    "In the library, she found hundreds of books. Most were old — leather covers, gold lettering. Many were about subjects "
    "Maya didn't expect: astronomy, geology, folklore, botany. There were books in languages she didn't recognize. And on "
    "one shelf, separate from the others, she found a row of journals identical to the one she had already taken from "
    "Eleanor's room.\n\n"
    "Maya counted them. Twelve journals in total, including the one upstairs. Each one had a year range written on the spine "
    "in small, neat numbers. The earliest started in 1968. The latest ended in 2024.\n\n"
    "Fifty-six years of journals. Fifty-six years of Eleanor's life in this house."
)

SECTION_4 = (
    "Maya pulled out the second journal — 1973 to 1978 — and opened it at random.\n\n"
    "April 12, 1975\n\n"
    "The light is stronger tonight. I can feel it through the floor, even up here in the library. It wants something. It "
    "has been wanting something for weeks now, and I think I finally understand what.\n\n"
    "It wants to be let out.\n\n"
    "I cannot allow that. The light must stay below. That is the rule. That has always been the rule, since the house was "
    "built. My mother told me, and her mother told her.\n\n"
    "The light stays below. We stay above. And we keep the door locked.\n\n"
    "But it is getting harder. The light is patient, but it is also persistent. And I am getting tired.\n\n"
    "Maya closed the journal and put it back on the shelf. Her hands were trembling.\n\n"
    "She looked down at the floor. The wooden boards were old and dark. Somewhere beneath them, beneath the stone foundation "
    "of the house, was the basement. And in the basement was the light.\n\n"
    "She could almost feel it. A faint warmth, rising through the floor like heat from a fire. Or maybe she was imagining it.\n\n"
    "She went back to cleaning."
)

SECTION_5 = (
    "By evening, the kitchen and living room were usable. Maya made herself a simple dinner — pasta with tomato sauce — and "
    "ate at the kitchen table. The house was quiet around her, but it was not an empty quiet. It was the quiet of a place "
    "that was listening.\n\n"
    "After dinner, she sat in the living room with Eleanor's first journal and read by the light of a floor lamp.\n\n"
    "September 17, 1971 (continued)\n\n"
    "The light reached back toward my hand. I felt warmth, then something else — a tingling, like electricity but softer. "
    "And then I saw things.\n\n"
    "Images. Memories. But not mine.\n\n"
    "I saw this house being built. Men with tools, cutting stone, raising walls. I saw a woman standing where I stood, "
    "looking down into the same hole. She wore old clothes — 1890s, maybe. She was crying.\n\n"
    "I saw the ocean, but not as it is now. I saw it as it was thousands of years ago, when the cliff was taller and the "
    "bay was wider. I saw people on the shore — not like us. Older. Different.\n\n"
    "And I saw the light itself, as it truly is. Not just a glow in a hole. It is a doorway. A connection to something "
    "vast and ancient and alive.\n\n"
    "I pulled my hand away. The visions stopped. I was standing in the basement, alone, shaking.\n\n"
    "I went upstairs and locked the door behind me.\n\nI did not sleep that night.\n\n"
    "Maya put down the journal. The lamp flickered once, then steadied.\n\n"
    "She looked at the window. It was fully dark outside now. She could see her own reflection in the glass — a young woman "
    "sitting alone in an old house, looking scared.\n\n"
    "Then, behind her reflection, she saw something else.\n\n"
    "A light. Faint and blue-white, moving across the garden outside.\n\n"
    "Maya jumped up and ran to the window. She pressed her face against the cold glass and looked out.\n\n"
    "The garden was dark. The trees were dark. There was nothing there.\n\n"
    "But she was sure — absolutely sure — that for one moment, she had seen a light moving through the darkness. A light "
    "that pulsed like a heartbeat.\n\n"
    "She stepped back from the window and pulled the curtains closed.\n\n"
    "It was going to be a long night."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["suitcase", "arranged", "checkout", "ponytail"]
S2_VOCAB = ["threatening", "whispered", "glow", "cliff"]
S3_VOCAB = ["scrubbing", "amber", "astronomy", "folklore"]
S4_VOCAB = ["persistent", "trembling", "foundation", "beneath"]
S5_VOCAB = ["tingling", "visions", "vast", "ancient"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 4: Dọn Vào (Moving In)",
        "preview": {
            "text": (
                "Maya quyết định dọn vào Alder House. Cô gặp Lily ở cửa hàng — người cảnh "
                "báo về ánh sáng di chuyển trên vách đá ban đêm. Trong lúc dọn dẹp, Maya "
                "tìm thấy 12 cuốn nhật ký của Eleanor và đọc về ánh sáng muốn thoát ra. "
                "Đêm đầu tiên trong nhà, cô nhìn thấy ánh sáng xanh trắng ngoài vườn."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 4. Maya dọn vào Alder House, "
            "khám phá bộ sưu tập nhật ký của Eleanor, và trải qua đêm đầu tiên đáng sợ "
            "khi nhìn thấy ánh sáng bí ẩn di chuyển trong vườn."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Quay lại Alder Bay",
                "activities": [
                    {"title": "Flashcards: Quay lại Alder Bay",
                     "description": "Học 4 từ: suitcase, arranged, checkout, ponytail",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Quay lại Alder Bay",
                     "description": "Maya xin nghỉ phép, đóng gói đồ, quay lại Alder Bay và gặp Lily ở siêu thị.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Quay lại Alder Bay",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Lời cảnh báo của Lily",
                "activities": [
                    {"title": "Flashcards: Lời cảnh báo của Lily",
                     "description": "Học 4 từ: threatening, whispered, glow, cliff",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lời cảnh báo của Lily",
                     "description": "Lily thì thầm về ánh sáng — nó di chuyển từ trong nhà ra ngoài vách đá như đang tìm kiếm thứ gì đó.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lời cảnh báo của Lily",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Khám phá ngôi nhà",
                "activities": [
                    {"title": "Flashcards: Khám phá ngôi nhà",
                     "description": "Học 4 từ: scrubbing, amber, astronomy, folklore",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Khám phá ngôi nhà",
                     "description": "Maya dọn dẹp và khám phá — chai thủy tinh màu, sách về thiên văn và dân gian, và 12 cuốn nhật ký của Eleanor.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Khám phá ngôi nhà",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Ánh sáng muốn thoát ra",
                "activities": [
                    {"title": "Flashcards: Ánh sáng muốn thoát ra",
                     "description": "Học 4 từ: persistent, trembling, foundation, beneath",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ánh sáng muốn thoát ra",
                     "description": "Maya đọc nhật ký năm 1975 — Eleanor viết ánh sáng ngày càng mạnh và muốn được giải phóng.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ánh sáng muốn thoát ra",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Đêm đầu tiên",
                "activities": [
                    {"title": "Flashcards: Đêm đầu tiên",
                     "description": "Học 4 từ: tingling, visions, vast, ancient",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đêm đầu tiên",
                     "description": "Maya đọc về những ảo ảnh Eleanor nhìn thấy khi chạm vào ánh sáng — rồi chính cô cũng thấy ánh sáng ngoài cửa sổ.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đêm đầu tiên",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 4",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 4 từ lúc Maya dọn vào đến đêm đầu tiên đáng sợ.",
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
    print(f"Chapter 4 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
