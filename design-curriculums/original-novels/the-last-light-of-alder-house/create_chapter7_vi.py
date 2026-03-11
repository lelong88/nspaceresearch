#!/usr/bin/env python3
"""Chapter 7: The Descent — bilingual Vietnamese-English curriculum."""

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
    "Sam arrived at Alder House at eight o'clock that evening. The sun had set an hour ago, and the house was dark except "
    "for the lights Maya had turned on in the kitchen and entrance hall.\n\n"
    "He parked his truck next to Maya's car and sat for a moment, looking up at the house. Maya watched him from the porch. "
    "She could see that he was nervous. She was nervous too.\n\n"
    '"Nice place," Sam said as he climbed the porch steps. His voice was light, but his eyes were serious. "Very... gothic."\n\n'
    '"Wait until you see the inside," Maya said.\n\n'
    "She led him through the entrance hall. Sam looked around at the old paintings, the carved staircase, the dark wallpaper. "
    "He whistled softly.\n\n"
    '"Eleanor lived here alone? For fifty years?"\n\n'
    '"She wasn\'t alone," Maya said. "She had the light."'
)

SECTION_2 = (
    "They stood in front of the basement door. Maya had the third key ready — the one she hadn't used yet. It was smaller "
    "than the others, made of dark iron instead of brass.\n\n"
    '"Are you sure about this?" Sam asked.\n\n'
    '"No," Maya said honestly. "But I need to see it. I need to understand what I\'m dealing with."\n\n'
    "She put the key in the lock. It turned smoothly, as if it had been used recently. The door swung inward, revealing a "
    "set of stone steps leading down into darkness.\n\n"
    "And something else.\n\n"
    "Light. Faint, blue-white, coming from somewhere below. It was dim — barely visible — but it was there. A soft glow, "
    "like the last light of day reflected on water.\n\n"
    '"Oh," Sam said quietly.\n\n'
    "Maya took a flashlight from her pocket and turned it on. The beam cut through the darkness, illuminating the stone "
    "steps. They were old and worn, with shallow grooves where feet had walked for over a century.\n\n"
    '"Stay close," Maya said.\n\n'
    "They went down together. The steps were steep, and the air grew cooler with each one. The stone walls were rough and "
    "damp. Maya counted twenty-two steps before they reached the bottom."
)

SECTION_3 = (
    "The basement was exactly as Eleanor had described it. One large room, carved from the rock of the cliff. The ceiling "
    "was low — Sam had to duck slightly. The walls were natural stone, gray and cold. And in the center of the room, there "
    "it was.\n\nThe hole.\n\n"
    "It was a perfect circle in the stone floor, about three feet across. The edges were smooth, as if they had been "
    "polished by time or by something else entirely. And from the hole came the light.\n\n"
    "Maya turned off her flashlight. She didn't need it.\n\n"
    "The light was beautiful. It rose from the hole like a slow fountain, blue-white and shimmering. It pulsed gently — "
    "brighter, dimmer, brighter, dimmer — in a rhythm that reminded Maya of breathing. Or a heartbeat.\n\n"
    "The room was filled with it. The stone walls glowed. The air itself seemed to shine. And Maya felt something she had "
    "not expected.\n\nPeace.\n\n"
    "A deep, warm, overwhelming sense of peace. As if every worry, every fear, every sad thought she had ever had was being "
    "gently lifted away. She felt light. She felt safe. She felt, for the first time in years, like she was exactly where "
    "she was supposed to be.\n\n"
    '"Maya," Sam whispered. His voice was shaking. "Do you feel that?"\n\n'
    '"Yes," she said.\n\n'
    '"It\'s... it\'s incredible."'
)

SECTION_4 = (
    "They stood at the edge of the hole, looking down. The light came from deep below — how deep, Maya couldn't tell. It "
    "might have been ten feet. It might have been a thousand. The hole seemed to go down forever, filled with that gentle, "
    "pulsing glow.\n\n"
    "Maya knelt beside the hole. She remembered what Eleanor had written — about reaching her hand toward the light, and "
    "the light reaching back.\n\n"
    "She extended her hand over the opening.\n\n"
    '"Maya, wait—" Sam started.\n\n'
    "The light moved. It rose from the hole like a wave, flowing upward toward Maya's hand. It touched her fingers, and "
    "she gasped.\n\n"
    "Warmth. Not heat — warmth. Like holding a cup of tea on a cold day. Like sunlight on her face. And with the warmth "
    "came the visions.\n\n"
    "She saw the cliff as it was before the house — bare rock and wild grass, with the ocean crashing below. She saw people "
    "gathered around the hole, their faces painted, their voices raised in song. She saw Catherine Voss, young and determined, "
    "standing in the rain with blueprints in her hands. She saw Eleanor, middle-aged and tired, sitting beside the hole with "
    "tears on her cheeks.\n\n"
    "And she saw something else. Something new.\n\n"
    "She saw herself. But not as she was now. She saw herself older, standing in this same basement, her hands raised, light "
    "pouring from her palms. She was doing something — controlling the light, shaping it, directing it. And she was smiling.\n\n"
    "The vision faded. Maya pulled her hand back. The light sank slowly back into the hole, returning to its gentle pulse."
)

SECTION_5 = (
    "Maya sat on the cold stone floor, breathing hard. Her hand was tingling, and her heart was racing.\n\n"
    '"What happened?" Sam asked. He was standing a few feet back, his face pale in the blue-white glow. "What did you see?"\n\n'
    '"Everything," Maya said. "I saw everything."\n\n'
    "She told him about the visions — the ancient people, Catherine, Eleanor. She did not tell him about the vision of "
    "herself. She wasn't ready to share that yet.\n\n"
    '"So the light shows you the past?" Sam said.\n\n'
    '"The past. And maybe... the future." Maya stood up. Her legs were unsteady. "Eleanor was right. It\'s not just energy. '
    'It\'s aware. It knows who I am."\n\n'
    '"That\'s amazing," Sam said. Then he paused. "And terrifying."\n\n'
    '"Both," Maya agreed.\n\n'
    "They stood in silence for a moment, watching the light pulse. Then Maya noticed something she hadn't seen before. On "
    "the far wall of the basement, partially hidden by shadows, there were marks carved into the stone. She walked over and "
    "held up her flashlight.\n\n"
    "They were symbols. Dozens of them, carved in neat rows from floor to ceiling. Some looked like letters, but from no "
    "alphabet Maya recognized. Others were pictures — a circle, a wave, a hand, an eye. And at the bottom, in English, "
    "someone had carved three words:\n\nREMEMBER THE BALANCE\n\n"
    '"The balance," Maya said. "What balance?"\n\n'
    '"My grandmother used to say that. \'The balance must be kept.\' She never explained what it meant."\n\n'
    "Maya traced the carved words with her finger. The stone was cold.\n\n"
    '"I think it means the light and the dark," she said slowly. "The light wants to grow, to spread. But something keeps '
    "it contained. Not just the house, not just the Voss family. Something else. A balance between the light and... whatever "
    'is on the other side."\n\n'
    '"The other side of what?"\n\n'
    "Maya looked back at the hole. The light pulsed steadily, patient and eternal.\n\n"
    '"I don\'t know yet," she said. "But I\'m going to find out."\n\n'
    "They climbed back up the stairs. Maya locked the basement door behind them. Her hands were steady now, and the tingling "
    "in her fingers had faded.\n\n"
    "In the kitchen, she made tea for both of them. They sat at the table, not speaking for a while. The house was quiet "
    "around them, but it felt different now. Less empty. Less lonely.\n\n"
    '"Thank you for coming with me," Maya said.\n\n'
    '"Thank you for letting me," Sam said. He wrapped his hands around his mug. "Maya, what are you going to do?"\n\n'
    '"I\'m going to stay. I\'m going to read the rest of Eleanor\'s journals. And I\'m going to figure out what the balance '
    'means and how to maintain it."\n\n'
    '"And Frank Burke?"\n\n'
    "Maya's expression hardened. \"Frank Burke can wait. I have bigger things to worry about.\"\n\n"
    "Sam nodded. He finished his tea and stood up to leave. At the front door, he turned back.\n\n"
    '"Maya? The vision you had — the one of yourself. What did you see?"\n\n'
    "Maya blinked. \"I didn't say I had a vision of myself.\"\n\n"
    '"You didn\'t have to. I saw your face when you pulled your hand back. You saw something about your own future." He '
    'paused. "Was it good?"\n\n'
    "Maya thought about the vision — herself, older, standing in the basement with light pouring from her hands. Smiling.\n\n"
    '"I think so," she said. "I hope so."\n\n'
    "Sam left. Maya watched his truck disappear down Cliff Road, its taillights fading into the darkness.\n\n"
    "She turned back to the house. Through the entrance hall, she could see the basement door. And for just a moment, she "
    "thought she saw light — the faintest blue-white glow — leaking through the cracks around the frame.\n\n"
    "The light knew she had visited. And it was happy.\n\n"
    "Maya locked the front door, turned off the lights, and went upstairs to bed. For the first time since arriving at "
    "Alder House, she slept deeply and without dreams.\n\n"
    "But in the town below, the dreams continued. And they were getting worse."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["gothic", "whistled", "carved", "wallpaper"]
S2_VOCAB = ["illuminating", "grooves", "steep", "damp"]
S3_VOCAB = ["shimmering", "rhythm", "overwhelming", "incredible"]
S4_VOCAB = ["extended", "gasped", "blueprints", "determined"]
S5_VOCAB = ["symbols", "alphabet", "balance", "eternal"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 7: Xuống Sâu (The Descent)",
        "preview": {
            "text": (
                "Maya và Sam xuống tầng hầm lần đầu tiên. Họ nhìn thấy ánh sáng xanh trắng "
                "tuyệt đẹp phát ra từ cái lỗ tròn hoàn hảo trong sàn đá. Maya chạm vào ánh "
                "sáng và nhìn thấy quá khứ — người bản địa, Catherine, Eleanor — và cả tương "
                "lai của chính mình. Trên tường có dòng chữ khắc: REMEMBER THE BALANCE."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 7. Maya và Sam đối mặt với ánh "
            "sáng trong tầng hầm, Maya nhận được những ảo ảnh về quá khứ và tương lai."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Sam đến Alder House",
                "activities": [
                    {"title": "Flashcards: Sam đến Alder House",
                     "description": "Học 4 từ: gothic, whistled, carved, wallpaper",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Sam đến Alder House",
                     "description": "Sam đến lúc tám giờ tối — cả hai đều hồi hộp khi bước vào ngôi nhà gothic cũ kỹ.",
                     "activityType": "reading", "practiceMinutes": 3,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Sam đến Alder House",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Mở cửa tầng hầm",
                "activities": [
                    {"title": "Flashcards: Mở cửa tầng hầm",
                     "description": "Học 4 từ: illuminating, grooves, steep, damp",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Mở cửa tầng hầm",
                     "description": "Maya dùng chiếc chìa khóa thứ ba — cửa mở ra, ánh sáng xanh trắng mờ nhạt từ bên dưới. Hai mươi hai bậc thang đá.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Mở cửa tầng hầm",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Ánh sáng tuyệt đẹp",
                "activities": [
                    {"title": "Flashcards: Ánh sáng tuyệt đẹp",
                     "description": "Học 4 từ: shimmering, rhythm, overwhelming, incredible",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ánh sáng tuyệt đẹp",
                     "description": "Cái lỗ tròn hoàn hảo, ánh sáng xanh trắng nhịp nhàng như nhịp tim — Maya cảm thấy bình yên sâu thẳm chưa từng có.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ánh sáng tuyệt đẹp",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Những ảo ảnh",
                "activities": [
                    {"title": "Flashcards: Những ảo ảnh",
                     "description": "Học 4 từ: extended, gasped, blueprints, determined",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Những ảo ảnh",
                     "description": "Maya đưa tay vào ánh sáng — nhìn thấy người bản địa, Catherine cầm bản vẽ, Eleanor khóc, và chính mình trong tương lai.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Những ảo ảnh",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Remember the Balance",
                "activities": [
                    {"title": "Flashcards: Remember the Balance",
                     "description": "Học 4 từ: symbols, alphabet, balance, eternal",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Remember the Balance",
                     "description": "Maya phát hiện ký hiệu cổ trên tường và dòng chữ REMEMBER THE BALANCE. Cô quyết định ở lại và tìm hiểu sự thật.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Remember the Balance",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 7",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 7 từ lúc Sam đến đến khi Maya ngủ yên lần đầu tiên.",
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
    print(f"Chapter 7 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
