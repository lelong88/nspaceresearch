#!/usr/bin/env python3
"""Chapter 10: The Disappearance — bilingual Vietnamese-English curriculum."""

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
    "Maya drove Lily into town. Lily sat in the passenger seat, wiping her eyes and trying to explain what had happened.\n\n"
    '"It\'s Ben," she said. "My brother. He went fishing last night and didn\'t come back."\n\n'
    '"Maybe he\'s just late," Maya said, but she could hear the weakness in her own words.\n\n'
    '"His boat is in the harbor. Empty. His phone, his jacket, his lunch — everything is still on the boat. But Ben is gone."\n\n'
    "Maya's hands tightened on the steering wheel. She thought of the newspaper article Frank had given her. Three fishermen, "
    "1952. Boats found empty. Men never seen again.\n\n"
    "The harbor was crowded when they arrived. It seemed like half the town was there, standing in small groups, talking in "
    "low voices. A police car was parked near the dock, its lights flashing.\n\n"
    "Maya and Lily pushed through the crowd to the dock. A young police officer was standing next to a small fishing boat — "
    "white with a blue stripe, rocking gently in the water. The name \"Lucky Star\" was painted on the side.\n\n"
    '"That\'s Ben\'s boat," Lily said.\n\n'
    'The officer — his name tag said "Deputy Torres" — looked at Lily with sympathy. "We\'re doing everything we can, Lily. '
    'The coast guard is searching the area."\n\n'
    '"He didn\'t fall in," Lily said firmly. "Ben is the best swimmer in town. And the water was calm last night. Something took him."'
)

SECTION_2 = (
    'Deputy Torres looked uncomfortable. "Lily—"\n\n'
    '"Something took him," she repeated. She turned to Maya. "Tell him. Tell him about the light."\n\n'
    "Everyone nearby went quiet. Maya felt dozens of eyes on her.\n\n"
    '"I don\'t think this is the time—" Maya started.\n\n'
    '"It\'s exactly the time." Frank Burke\'s voice cut through the crowd. He pushed forward, his face red with anger. '
    '"This is what I warned you about. The light is getting out of control, and now someone is missing. Just like 1952."\n\n'
    "The crowd murmured. Some people nodded. Others looked confused.\n\n"
    '"We don\'t know what happened to Ben," Maya said carefully. "It could be an accident—"\n\n'
    '"It\'s not an accident," Frank said. "And you know it. You went into that basement. You woke it up. And now it\'s hungry."\n\n'
    '"That\'s not how it works," Maya said, but she wasn\'t sure. She wasn\'t sure of anything.\n\n'
    '"Then how does it work?" Frank demanded. "Explain it to us. Tell us what\'s in that basement. Tell us why people '
    'disappear when the light gets strong."\n\n'
    "The crowd was watching. Waiting. Maya could feel their fear — it was thick in the air, like fog.\n\n"
    'She took a breath. "There is something under Alder House," she said. "A light. It\'s been there for a very long time — '
    "longer than the house, longer than the town. My grandmother spent her life keeping it contained. I'm trying to do the "
    'same."\n\n'
    '"You\'re failing," Frank said.'
)

SECTION_3 = (
    '"I\'ve been here two weeks. Give me time."\n\n'
    '"Ben doesn\'t have time." Frank stepped closer. "I\'m done waiting. Tomorrow, I\'m going up to that house with concrete '
    'and equipment, and I\'m sealing that hole. With or without your permission."\n\n'
    '"You can\'t do that," Maya said. "If you seal it, the other lights—"\n\n'
    "She stopped. She hadn't meant to say that.\n\n"
    '"Other lights?" Frank said. "What other lights?"\n\n'
    "The crowd pressed closer. Maya could see Sam at the edge, watching with worried eyes.\n\n"
    '"There are other places like this," Maya said slowly. "Along the coast. The lights are connected. If you destroy one, '
    'it could affect the others. It could make things worse."\n\n'
    '"That\'s convenient," Frank said. "Every time someone wants to fix this problem, there\'s always a reason not to. Your '
    'grandmother said the same thing for fifty years. And now a man is missing."\n\n'
    'He turned to the crowd. "I say we end this. Tomorrow. Who\'s with me?"\n\n'
    "Several people raised their hands. Not everyone — maybe a third of the crowd. But it was enough.\n\n"
    'Frank looked back at Maya. "You have until tomorrow morning. After that, we\'re coming up."\n\n'
    "He walked away. The crowd began to break apart, people drifting away in small groups, talking quietly.\n\n"
    'Lily grabbed Maya\'s arm. "Find my brother," she said. "Please. I don\'t care about the light or the house or any of '
    'it. Just find Ben."\n\n'
    "Maya looked into Lily's red, desperate eyes. \"I'll try,\" she said. \"I promise I'll try.\""
)

SECTION_4 = (
    "Maya drove back to Alder House alone. Sam had offered to come, but she needed to think. She needed to be alone with "
    "the house and the light.\n\n"
    "She went straight to the basement.\n\n"
    "She unlocked the door, walked down the stairs, and stood at the edge of the hole. The light pulsed steadily, blue-white "
    "and beautiful. Calm. Peaceful.\n\n"
    '"Did you take him?" Maya asked out loud. Her voice echoed off the stone walls. "Did you take Ben?"\n\n'
    "The light pulsed. No answer. No vision. Just the steady, rhythmic glow.\n\n"
    "Maya knelt beside the hole and put her hands into the light. The warmth flowed through her fingers, up her arms, into "
    "her chest. The visions came.\n\n"
    "She saw the ocean at night. Dark water, dark sky. A small boat — white with a blue stripe. A young man sitting in the "
    "boat, fishing line in the water, headphones in his ears.\n\n"
    "Then the water began to glow. A blue-white light, rising from the depths. The young man — Ben — looked over the side "
    "of the boat. His eyes went wide.\n\n"
    "The light rose higher. It broke the surface of the water, spreading across the bay like spilled paint. Ben stood up in "
    "the boat, staring.\n\n"
    "And then the light wrapped around him. Gently, like arms. Like an embrace. Ben didn't scream. He didn't fight. He "
    "looked... peaceful. Almost happy.\n\n"
    "The light pulled him down. Into the water. Into the glow. And he was gone.\n\n"
    "Maya pulled her hands out of the light. She was shaking."
)

SECTION_5 = (
    '"Where is he?" she demanded. "Where did you take him?"\n\n'
    "The light pulsed once, brighter than before. And Maya felt something — not a vision this time, but a feeling. A "
    "direction. Like a compass needle turning in her chest, pointing south.\n\n"
    "South. Along the coast.\n\n"
    "Toward one of the other lights.\n\n"
    "Maya stood up. Her mind was racing. The light had taken Ben — not to hurt him, she thought, but to move him. To send "
    "him somewhere. To one of the other points on Catherine's map.\n\n"
    "But why? What did the light want with a fisherman from Alder Bay?\n\n"
    "She didn't know. But she knew where to start looking.\n\n"
    "She ran up the stairs, locked the basement door, and grabbed Catherine's map from the library. She spread it on the "
    "kitchen table and found the nearest point south of Alder Bay.\n\n"
    "Cape Sorrow. About sixty miles down the coast.\n\n"
    "Maya looked at the clock. It was four in the afternoon. She could be there before dark if she left now.\n\n"
    "She grabbed her keys, her flashlight, and her jacket. She was halfway to the front door when she stopped.\n\n"
    "Frank was coming tomorrow morning with concrete and equipment. If she left now, there would be no one to stop him.\n\n"
    "She stood in the entrance hall, torn between two impossible choices. Go south and find Ben. Or stay and protect the "
    "light.\n\nShe couldn't do both.\n\n"
    'Her phone buzzed. A text from Sam: "Frank is gathering people. He\'s serious about tomorrow. What do we do?"\n\n'
    "Maya stared at the phone. Then she made her decision.\n\n"
    "She called Sam.\n\n"
    '"I need you to do something for me," she said. "I need you to watch the house tonight. Don\'t let anyone in. '
    'Especially not Frank."\n\n'
    '"Where are you going?"\n\n'
    '"South. Cape Sorrow. I think that\'s where Ben is."\n\n'
    'There was a long pause. "Maya, that\'s sixty miles away. And it\'s almost dark."\n\n'
    '"I know. But Ben is alive. I\'m sure of it. And if I don\'t go now, I might not get another chance."\n\n'
    'Another pause. Then: "Okay. I\'ll watch the house. But Maya — be careful. Please."\n\n'
    '"I will."\n\n'
    "She hung up, got in her car, and drove down Cliff Road. At the bottom, she turned south, toward the coast highway.\n\n"
    "Behind her, Alder House grew smaller in the rearview mirror. And in the basement, the light pulsed faster, as if it "
    "was excited.\n\nAs if it had been waiting for her to go."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["sympathy", "harbor", "passenger", "firmly"]
S2_VOCAB = ["murmured", "contained", "demanded", "convenient"]
S3_VOCAB = ["desperate", "drifting", "consequences", "permission"]
S4_VOCAB = ["embrace", "rhythmic", "depths", "visions"]
S5_VOCAB = ["compass", "rearview", "entrance", "impossible"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 10: Sự Mất Tích (The Disappearance)",
        "preview": {
            "text": (
                "Ben mất tích — thuyền còn đó nhưng người biến mất. Frank đổ lỗi cho ánh sáng "
                "và dọa đổ bê tông bịt lỗ ngay sáng mai. Maya dùng ánh sáng để tìm Ben — cô "
                "thấy ảo ảnh ánh sáng cuốn anh xuống biển, rồi cảm nhận hướng nam dẫn đến Cape "
                "Sorrow. Học 20 từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 10. Ben biến mất, Frank đe dọa phá "
            "hủy ánh sáng, và Maya phải chọn giữa bảo vệ ngôi nhà hay đi tìm Ben."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Ben mất tích",
                "activities": [
                    {"title": "Flashcards: Ben mất tích",
                     "description": "Học 4 từ: sympathy, harbor, passenger, firmly",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ben mất tích",
                     "description": "Lily báo tin Ben đi câu cá đêm qua không về — thuyền còn đó nhưng người biến mất. Cả thị trấn tụ tập ở bến cảng.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ben mất tích",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Frank đổ lỗi cho ánh sáng",
                "activities": [
                    {"title": "Flashcards: Frank đổ lỗi",
                     "description": "Học 4 từ: murmured, contained, demanded, convenient",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Frank đổ lỗi",
                     "description": "Frank xuất hiện giữa đám đông, buộc tội Maya đã đánh thức ánh sáng. Maya buộc phải thú nhận có thứ gì đó dưới tầng hầm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Frank đổ lỗi",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Tối hậu thư",
                "activities": [
                    {"title": "Flashcards: Tối hậu thư",
                     "description": "Học 4 từ: desperate, drifting, consequences, permission",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Tối hậu thư",
                     "description": "Frank tuyên bố sáng mai sẽ đổ bê tông. Lily nắm tay Maya van xin — hãy tìm anh trai tôi.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Tối hậu thư",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Ảo ảnh về Ben",
                "activities": [
                    {"title": "Flashcards: Ảo ảnh về Ben",
                     "description": "Học 4 từ: embrace, rhythmic, depths, visions",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ảo ảnh về Ben",
                     "description": "Maya đặt tay vào ánh sáng và thấy cảnh Ben bị cuốn xuống biển — nhẹ nhàng như vòng tay ôm, không đau đớn.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ảo ảnh về Ben",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Lên đường về phía nam",
                "activities": [
                    {"title": "Flashcards: Lên đường về phía nam",
                     "description": "Học 4 từ: compass, rearview, entrance, impossible",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lên đường về phía nam",
                     "description": "Maya cảm nhận hướng nam — Cape Sorrow. Cô nhờ Sam canh nhà, rồi lái xe đi tìm Ben trong đêm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lên đường về phía nam",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 10",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 10 từ lúc Ben mất tích đến khi Maya lái xe về phía nam.",
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
    print(f"Chapter 10 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
