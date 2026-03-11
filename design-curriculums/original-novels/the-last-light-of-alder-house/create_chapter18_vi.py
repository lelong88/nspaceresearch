#!/usr/bin/env python3
"""Chapter 18: The Dive — bilingual Vietnamese-English curriculum."""

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
    'The morning of the dive was calm and gray. No wind, no waves — the ocean was flat and still, like a sheet of '
    'glass. Even the seagulls were quiet.\n\n'
    'Ben had his boat ready at the harbor — the Lucky Star, the same boat the light had taken him from. He had loaded '
    'it with supplies: rope, a waterproof flashlight, a first aid kit, and a wetsuit for Maya.\n\n'
    '"The wetsuit won\'t help much at a thousand feet," Ben said. "But it\'s better than nothing."\n\n'
    'Maya, Sam, Ben, and Lily drove to the harbor together. The town was quiet — it was early, and most people were '
    'still asleep. But as they walked to the dock, Maya noticed a figure standing at the end of the harbor wall.\n\n'
    'Frank Burke.\n\n'
    'He was alone, his hands in his pockets, watching them. Maya expected anger, but his face was different today. He '
    'looked tired. Old. Almost sad.\n\n'
    'Maya walked over to him.\n\n'
    '"Tomorrow is your deadline," she said.\n\n'
    '"I know."\n\n'
    '"I\'m going to fix this. Today. Right now."\n\n'
    'Frank looked at the ocean. "How?"\n\n'
    '"I\'m going to dive to the bottom of the canyon. To the center of the network. I\'m going to stabilize it '
    'permanently."\n\n'
    'Frank was quiet for a long moment. "You really believe all this, don\'t you? The lights, the network, the balance."\n\n'
    '"I\'ve seen it. I\'ve felt it. It\'s real, Frank."\n\n'
    '"My father believed it was real too. He spent his whole life fighting it. Trying to protect this town from it." '
    'Frank\'s voice was rough. "He died angry. Angry at the light, angry at Eleanor, angry at himself for never being '
    'able to fix things."\n\n'
    '"I\'m sorry," Maya said.\n\n'
    '"Don\'t be sorry. Just..." He paused. "Just come back alive. Whatever you think of me, I don\'t want anyone else '
    'to disappear."\n\n'
    'Maya nodded. "I\'ll come back."\n\n'
    'Frank turned and walked away without another word. Maya watched him go, then joined the others on the boat.'
)

SECTION_2 = (
    'Ben guided the Lucky Star out of the harbor and north along the coast. The cliff where Alder House stood grew '
    'larger as they approached, dark and imposing against the gray sky. Maya could see the house at the top — small '
    'from this distance, but solid. Permanent.\n\n'
    '"The canyon starts about here," Ben said, checking his instruments. "The bottom drops away fast — from fifty feet '
    'to over a thousand in less than a mile."\n\n'
    'Maya looked over the side of the boat. The water was dark — not the blue-green of the shallow bay, but a deep, '
    'almost black color. She could feel the pull in her chest, stronger than ever, pointing straight down.\n\n'
    '"This is the spot," she said.\n\n'
    'She put on the wetsuit and tied the rope around her waist. Sam held the other end.\n\n'
    '"If you tug three times, we pull you up," Sam said. "No matter what."\n\n'
    '"Okay."\n\n'
    '"And if you\'re not back in one hour, we\'re coming after you."\n\n'
    '"You can\'t dive to a thousand feet, Sam."\n\n'
    '"Then come back in less than an hour."\n\n'
    'Maya smiled. She looked at each of them — Sam, Ben, Lily. Her friends. The first real friends she\'d had in years.\n\n'
    '"Thank you," she said. "For everything."\n\n'
    '"Go save the world," Lily said. "And then come back and have dinner with us."\n\n'
    'Maya laughed. Then she climbed onto the edge of the boat, took a deep breath of air — her last for a while — and '
    'dove into the ocean.'
)

SECTION_3 = (
    'The cold hit her first, then the darkness. She sank quickly, the weight of the wetsuit pulling her down. The rope '
    'trailed behind her, unspooling from the boat above.\n\n'
    'At fifty feet, the light in her chest activated. Warmth spread through her body, pushing back the cold. Her lungs '
    'shifted, and she began to breathe the water. The pressure, which should have been crushing, felt like nothing more '
    'than a gentle squeeze.\n\n'
    'She could see. Not with normal vision — the water was too dark for that. But the light inside her illuminated '
    'everything in a soft blue-white glow. She could see the canyon walls on either side, dropping away into the depths. '
    'She could see fish and jellyfish and strange, deep-sea creatures drifting past her. She could see the rock and sand '
    'of the ocean floor, far below.\n\n'
    'She swam deeper. A hundred feet. Two hundred. Three hundred. The water grew colder and darker, but the light inside '
    'her grew brighter. She was a small sun, falling through the darkness.\n\n'
    'At five hundred feet, she saw something on the canyon wall. Symbols. The same symbols from the basement, from the '
    'cathedral at The Deep Place — carved into the underwater rock, glowing faintly with their own light. They formed a '
    'path, a trail leading down into the depths.\n\n'
    'She followed them.\n\n'
    'At eight hundred feet, the canyon narrowed. The walls closed in on either side, and the symbols grew denser, '
    'covering every surface. Maya felt like she was swimming through a tunnel of light.\n\n'
    'At a thousand feet, the canyon opened up again — into a vast underwater chamber. The chamber was enormous, bigger '
    'than anything Maya had seen on land. The ceiling was a hundred feet above her, the walls curved away into darkness '
    'on all sides.'
)


SECTION_4 = (
    'And in the center of the chamber, the nexus.\n\n'
    'It was not what she expected. She had imagined another hole, another cave, another pool of light. But the nexus was '
    'something else entirely.\n\n'
    'It was a sphere. A perfect sphere of light, about ten feet across, floating in the center of the chamber. It was '
    'brighter than anything Maya had ever seen — brighter than the sun, brighter than the stars. But it didn\'t hurt her '
    'eyes. It was warm and welcoming, like coming home.\n\n'
    'The seven connections were visible here — seven lines of light, stretching from the sphere in different directions, '
    'passing through the rock and water and earth to reach the seven points along the coast. Maya could see them all, '
    'bright and strong, pulsing in perfect harmony.\n\n'
    'She swam toward the sphere. As she got closer, she felt the power of it — immense, ancient, patient. This was the '
    'heart of the network. The center of everything.\n\n'
    'She reached out and touched it.\n\n'
    'The world exploded into light.\n\n'
    'Maya was everywhere at once. She was in the basement at Alder House. She was in the cave at Cape Sorrow. She was '
    'behind the waterfall at Redwood Cove. She was at Point Silence, at Mist Harbor, at Shell Beach, at The Deep Place. '
    'She was in all seven places simultaneously, seeing through all seven lights, feeling the entire network as if it '
    'was her own body.\n\n'
    'And she understood what she needed to do.'
)

SECTION_5 = (
    'The network was like a machine — a vast, complex machine that had been running for millions of years. But it was '
    'wearing down. The connections were fraying. The lights were dimming. Without maintenance, without care, it would '
    'eventually fail.\n\n'
    'Catherine had tried to understand it. Margaret had tried to maintain it. Eleanor had tried to hold it together. But '
    'none of them had been strong enough to do what needed to be done.\n\n'
    'Maya was.\n\n'
    'She gathered the light inside her — all of it, every drop of power the seven lights had given her — and pushed it '
    'into the sphere. She felt it flow out of her like water from a broken dam, pouring into the nexus, filling it, '
    'strengthening it.\n\n'
    'The sphere blazed brighter. The seven connections thickened, solidified, became permanent. The network locked into '
    'place — not fragile and temporary, but strong and self-sustaining.\n\n'
    'Maya felt the change ripple outward. Along the coast, the seven lights flared once, brilliantly, then settled into '
    'a steady, powerful glow. The earth beneath them hummed with renewed energy. The ocean currents shifted, the tides '
    'corrected, the deep geological forces that shaped the coastline found their balance again.\n\n'
    'It was done.\n\n'
    'The network was stable. Permanently. It no longer needed a Voss to maintain it. It no longer needed a guardian '
    'sitting in a house on a cliff, sacrificing her life to keep the balance.\n\n'
    'Maya had set it free.\n\n'
    'And in doing so, she had set herself free too.\n\n'
    'She floated in the chamber, surrounded by light, feeling the last of the power drain from her body. She was '
    'exhausted — more tired than she had ever been. Her vision was fading, her limbs were heavy, and the warmth in her '
    'chest was dimming.\n\n'
    'The rope around her waist tugged. Once. Twice. Three times.\n\n'
    'Sam. Pulling her up.\n\n'
    'Maya smiled and let go. Let go of the light, the power, the visions. Let go of everything except the rope and the '
    'knowledge that her friends were waiting above.\n\n'
    'She began to rise. Slowly at first, then faster, pulled upward through the dark water toward the surface. The light '
    'of the nexus faded below her, growing smaller and smaller until it was just a point of brightness in the deep.\n\n'
    'But it was still there. It would always be there. Strong and steady and eternal.\n\n'
    'Maya broke the surface gasping. The air hit her lungs like a shock, and she coughed water for a full minute before '
    'she could breathe normally. Strong hands grabbed her arms and pulled her into the boat.\n\n'
    '"Maya! Maya, are you okay?"\n\n'
    'Sam\'s face, white with fear. Ben and Lily, leaning over her, their eyes wide.\n\n'
    'Maya lay on the bottom of the boat, soaking wet, shivering, smiling.\n\n'
    '"It\'s done," she said. "It\'s over."\n\n'
    'And far below, in the deep dark water, the nexus pulsed once — a single, brilliant flash of blue-white light that '
    'was visible even from the surface.\n\n'
    'A thank you. A goodbye. A promise.\n\n'
    'The balance was restored.'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["deadline", "stabilize", "permanently", "disappear"]
S2_VOCAB = ["imposing", "instruments", "shallow", "unspooling"]
S3_VOCAB = ["illuminated", "creatures", "cathedral", "enormous"]
S4_VOCAB = ["sphere", "simultaneously", "immense", "harmony"]
S5_VOCAB = ["fraying", "self-sustaining", "geological", "eternal"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 18: Lặn Xuống (The Dive)",
        "preview": {
            "text": (
                "Maya lặn xuống hẻm núi ngầm sâu hàng ngàn feet để chạm vào nexus — trái tim "
                "của mạng lưới ánh sáng. Trước khi đi, Frank Burke bất ngờ xuất hiện ở bến cảng, "
                "không còn giận dữ mà chỉ mệt mỏi, và nói 'just come back alive.' Dưới đáy đại "
                "dương, Maya tìm thấy một quả cầu ánh sáng hoàn hảo, chạm vào nó và trở thành "
                "một phần của cả bảy điểm sáng cùng lúc. Cô dồn hết sức mạnh vào nexus, biến "
                "mạng lưới từ mong manh thành tự duy trì vĩnh viễn. Học 20 từ vựng tiếng Anh "
                "qua chương cao trào nhất của câu chuyện."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 18 — chương cao trào. Maya lặn xuống "
            "đáy đại dương, chạm vào nexus, và giải phóng mạng lưới ánh sáng khỏi sự phụ thuộc "
            "vào dòng họ Voss."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Cuộc đối thoại với Frank Burke",
                "activities": [
                    {"title": "Flashcards: Cuộc đối thoại với Frank",
                     "description": "Học 4 từ: deadline, stabilize, permanently, disappear",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Cuộc đối thoại với Frank",
                     "description": "Sáng sớm tại bến cảng, Maya gặp Frank Burke — không còn giận dữ, chỉ mệt mỏi. Ông kể về cha mình và nói 'just come back alive.'",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Cuộc đối thoại với Frank",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Nhảy xuống đại dương",
                "activities": [
                    {"title": "Flashcards: Nhảy xuống đại dương",
                     "description": "Học 4 từ: imposing, instruments, shallow, unspooling",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhảy xuống đại dương",
                     "description": "Thuyền Lucky Star ra khơi. Maya buộc dây quanh eo, từ biệt bạn bè, và lặn xuống vùng nước tối đen phía trên hẻm núi ngầm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhảy xuống đại dương",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Xuống sâu ngàn feet",
                "activities": [
                    {"title": "Flashcards: Xuống sâu ngàn feet",
                     "description": "Học 4 từ: illuminated, creatures, cathedral, enormous",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Xuống sâu ngàn feet",
                     "description": "Ánh sáng trong ngực Maya bật sáng, cô thở được dưới nước. Bơi qua cá, sứa, sinh vật biển sâu, theo dấu ký hiệu phát sáng trên vách đá đến căn phòng khổng lồ dưới đáy.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Xuống sâu ngàn feet",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Chạm vào nexus",
                "activities": [
                    {"title": "Flashcards: Chạm vào nexus",
                     "description": "Học 4 từ: sphere, simultaneously, immense, harmony",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Chạm vào nexus",
                     "description": "Nexus là một quả cầu ánh sáng hoàn hảo lơ lửng giữa phòng. Maya chạm vào — và bỗng hiện diện ở cả bảy điểm sáng cùng lúc, cảm nhận toàn bộ mạng lưới như chính cơ thể mình.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Chạm vào nexus",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Giải phóng ánh sáng",
                "activities": [
                    {"title": "Flashcards: Giải phóng ánh sáng",
                     "description": "Học 4 từ: fraying, self-sustaining, geological, eternal",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Giải phóng ánh sáng",
                     "description": "Maya dồn hết sức mạnh vào nexus. Mạng lưới trở nên tự duy trì vĩnh viễn — không còn cần người canh giữ. Cô trồi lên mặt nước, kiệt sức nhưng mỉm cười: 'It's done. It's over.'",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Giải phóng ánh sáng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 18",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 18 từ bến cảng đến khoảnh khắc nexus phát sáng dưới đáy đại dương.",
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
    print(f"Chapter 18 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
