#!/usr/bin/env python3
"""Chapter 16: The Deep Place — bilingual Vietnamese-English curriculum."""

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
    "They found it in the late afternoon.\n\n"
    "Maya had been following the pull in her chest for hours, directing Sam down smaller and smaller roads until they "
    "ran out of road entirely. They parked at the end of a dirt track and hiked through coastal scrubland — low bushes, "
    "wild grass, and twisted cypress trees bent by decades of wind.\n\n"
    "The cliff edge appeared suddenly. One moment they were walking through bushes, and the next they were standing at "
    "the edge of the world. The cliff dropped three hundred feet straight down to the ocean. The water below was dark — "
    "almost black — and Maya could see why. The ocean floor dropped away sharply here, plunging into a deep underwater "
    "canyon.\n\n"
    '"The Deep Place," Sam said. "I can see why Catherine named it that."\n\n'
    "Maya looked down. The pull in her chest was almost painful now — a deep, aching tug that pointed straight down, "
    "into the cliff, into the ocean, into the darkness below.\n\n"
    '"It\'s down there," she said. "Way down."\n\n'
    '"How do we reach it?"\n\n'
    "Maya scanned the cliff face. Unlike the other sites, there was no obvious path, no stairs, no trail. The cliff "
    "was sheer rock, covered with seabird nests and patches of lichen. Climbing down was impossible without "
    "equipment.\n\n"
    "But then she saw it. About fifty feet down the cliff face, partially hidden by an overhang, there was a dark "
    "opening in the rock. A cave entrance, larger than any of the others she had seen.\n\n"
    '"There," she pointed. "But I don\'t see how to get to it from up here."\n\n'
    '"Maybe from the water?" Sam suggested.\n\n'
    "They looked at each other. The ocean below was rough — big swells rolling in from the open Pacific, crashing "
    "against the cliff base with tremendous force. Swimming to the cave would be dangerous, maybe suicidal.\n\n"
    '"There has to be another way," Maya said.'
)

SECTION_2 = (
    "She closed her eyes and focused on the pull in her chest. She let it guide her, turning slowly until she was "
    "facing inland, away from the cliff.\n\n"
    '"This way," she said.\n\n'
    "She walked back through the scrubland, following the invisible thread. Sam followed without question. They walked "
    "for about ten minutes, pushing through thick bushes, until Maya stopped at a spot that looked no different from "
    "any other.\n\n"
    '"Here," she said.\n\n'
    "She knelt and brushed away the grass and dirt. Beneath it, she found stone — flat, smooth stone, like a paving "
    "slab. She cleared more dirt and found the edges of the stone. It was about three feet square, set into the ground "
    "like a trapdoor.\n\n"
    '"Help me," she said.\n\n'
    "Together, they lifted the stone slab. It was heavy but moved smoothly, as if it had been designed to be opened. "
    "Beneath it was a shaft — a vertical tunnel going straight down into the earth, with iron rungs set into the wall "
    "like a ladder.\n\n"
    "And from the bottom of the shaft came the light. Brighter than any of the others. So bright that it lit up the "
    "shaft like a lantern, casting blue-white shadows on the stone walls.\n\n"
    '"That\'s a long way down," Sam said, peering into the shaft.\n\n'
    '"I know." Maya tested the first rung. It was solid — iron, set deep into the rock. "I\'m going."\n\n'
    '"Maya, wait. Let me go first. If the rungs are—"\n\n'
    '"No. This one is for me. The light called me here. I need to go alone."\n\n'
    "Sam looked like he wanted to argue, but something in Maya's face stopped him. He nodded.\n\n"
    '"I\'ll be right here," he said. "If anything goes wrong, shout. I\'ll find a way down."\n\n'
    "Maya put her foot on the first rung and began to descend."
)

SECTION_3 = (
    "The shaft went down about a hundred feet — Maya counted the rungs. The light grew brighter with each step, until "
    "she had to squint against the glare. The air grew warmer, then hot, then almost uncomfortably warm.\n\n"
    'At the bottom, the shaft opened into a cave. But "cave" was the wrong word. It was a cathedral.\n\n'
    "The space was enormous — a hundred feet across and at least fifty feet high. The walls were smooth and curved, "
    "like the inside of an egg. And every surface was covered with the symbols Maya had seen in the basement at Alder "
    "House — hundreds of them, thousands of them, carved into the rock in spiraling patterns that covered the walls "
    "from floor to ceiling.\n\n"
    "And in the center of the cathedral, the light.\n\n"
    "It was not in a hole. It was not in a wall. It was everywhere. The light filled the entire space, rising from the "
    "floor, falling from the ceiling, flowing along the walls like water. It was so bright that Maya could barely see, "
    "so warm that she could barely breathe.\n\n"
    "And it was alive. More alive than any of the other lights. She could feel its awareness, its intelligence, its "
    "age. This light was old — older than the cliff, older than the ocean, older than anything Maya could imagine.\n\n"
    "She walked to the center of the cathedral. The light swirled around her, touching her skin, flowing through her "
    "hair. She felt it entering her — not painfully, but deeply, like water soaking into dry earth.\n\n"
    "And then the visions came. Not images this time. Knowledge. Pure, direct knowledge, flowing into her mind like a "
    "river."
)

SECTION_4 = (
    "She understood.\n\n"
    "The seven lights were not separate entities. They were one being — one vast, ancient consciousness that existed "
    "beneath the surface of the earth. It had been there since the beginning — since the planet was young and the "
    "continents were forming. It was part of the earth itself, as essential as the core, the mantle, the crust.\n\n"
    "The lights were its eyes. Its hands. Its voice. Through them, it maintained the balance of the planet — the "
    "tides, the weather, the movement of the tectonic plates. Without the lights, the earth would become unstable. "
    "Earthquakes, tsunamis, volcanic eruptions — all held in check by this ancient, patient consciousness.\n\n"
    "And the Voss family — Maya's family — had been chosen. Not by accident, not by fate, but by the light itself. "
    "Thousands of years ago, it had reached out to a woman on the shore — a woman with something special in her blood, "
    "something that resonated with the light's frequency. It had bonded with her, and through her, with all her "
    "descendants.\n\n"
    "The Voss women were the light's connection to the surface world. Its translators. Its guardians. Its family.\n\n"
    "And Maya was the strongest of them all.\n\n"
    "She felt it now — the power flowing through her, filling every cell of her body. She could feel all seven lights "
    "at once, pulsing in harmony. She could feel the connections between them, strong and bright. She could feel the "
    "nexus — the central point, deep beneath the ocean — calling to her.\n\n"
    '"I understand," she said. "I understand everything."\n\n'
    "The light pulsed once, brightly, and Maya felt something like joy radiating from it. After so long — after decades "
    "of weakening connections and fading strength — it had found its guardian again.\n\n"
    '"But I need to reach the nexus," Maya said. "I need to go to the center. How?"\n\n'
    "The light showed her. A vision of the ocean floor — the deep canyon off the coast, plunging down into darkness. "
    "At the bottom of the canyon, a cave. And in the cave, the nexus — the heart of the network, where all seven "
    "connections met."
)

SECTION_5 = (
    '"I can\'t breathe underwater," Maya said.\n\n'
    "The light pulsed again. And Maya felt something change inside her. A warmth in her lungs, a tingling in her skin. "
    "The light was giving her something — a gift, a tool, a transformation.\n\n"
    '"You will breathe," the voice said. "When the time comes, you will breathe."\n\n'
    "Maya stood in the cathedral of light for a long time, letting the knowledge and power flow through her. She felt "
    "herself changing — not physically, but fundamentally. She was becoming something new. Something more.\n\n"
    "Finally, she turned and climbed back up the shaft. The light dimmed behind her, but she could still feel it — all "
    "seven lights, burning inside her like seven small suns.\n\n"
    "Sam was waiting at the top, his face tight with worry.\n\n"
    '"You were down there for two hours," he said. "I was about to come after you."\n\n'
    '"Two hours?" It had felt like minutes.\n\n'
    '"Are you okay? You look... different."\n\n'
    "Maya looked at her hands. In the fading daylight, she could see a faint glow beneath her skin — blue-white, "
    "pulsing gently with her heartbeat.\n\n"
    '"I am different," she said. "Sam, I know what I need to do. I know how to fix everything. But I need to get to '
    "the nexus — the center of the network. It's underwater, in a canyon off the coast.\"\n\n"
    '"Underwater? Maya, that\'s—"\n\n'
    '"I know. But the light gave me something. A way to survive down there. I can feel it." She took his hand. "Trust '
    'me."\n\n'
    "Sam looked at her glowing hands, at her bright eyes, at the calm certainty on her face. And slowly, he nodded.\n\n"
    '"I trust you," he said.\n\n'
    "They walked back to the truck in silence. The sun was setting over the Pacific, painting the sky in shades of "
    "gold and purple. Maya felt the seven lights pulsing inside her, synchronized, harmonious, strong.\n\n"
    "Seven of seven. The network was complete.\n\n"
    "Now she just had to reach the center.\n\n"
    "And she had ten days to figure out how."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["scrubland", "plunging", "overhang", "tremendous"]
S2_VOCAB = ["inland", "vertical", "descended", "lantern"]
S3_VOCAB = ["cathedral", "spiraling", "awareness", "intelligence"]
S4_VOCAB = ["consciousness", "tectonic", "descendants", "radiating"]
S5_VOCAB = ["transformation", "fundamentally", "synchronized", "harmonious"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 16: Nơi Sâu Thẳm (The Deep Place)",
        "preview": {
            "text": (
                "Maya tìm thấy ánh sáng thứ 7 qua một hầm giếng ẩn dưới đất. Bên dưới là một "
                "nhà thờ khổng lồ phủ đầy ký hiệu cổ đại. Ánh sáng truyền cho cô tri thức — bảy "
                "ánh sáng là một ý thức duy nhất giữ cân bằng Trái Đất, và dòng họ Voss là người "
                "bảo hộ. Maya nhận được khả năng thở dưới nước. Bảy trên bảy hoàn thành. Học 20 "
                "từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 16. Maya xuống hầm sâu, khám phá bí "
            "mật của bảy ánh sáng, và nhận được sức mạnh mới để chuẩn bị lặn xuống nexus."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Bờ vực cuối đường",
                "activities": [
                    {"title": "Flashcards: Bờ vực cuối đường",
                     "description": "Học 4 từ: scrubland, plunging, overhang, tremendous",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bờ vực cuối đường",
                     "description": "Maya và Sam đi bộ qua bụi rậm đến mép vách đá cao 300 feet. Bên dưới là hẻm núi ngầm sâu thẳm. Có cửa hang nhưng không cách nào leo xuống.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bờ vực cuối đường",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Hầm giếng bí mật",
                "activities": [
                    {"title": "Flashcards: Hầm giếng bí mật",
                     "description": "Học 4 từ: inland, vertical, descended, lantern",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Hầm giếng bí mật",
                     "description": "Maya để ánh sáng dẫn đường vào đất liền, tìm thấy tấm đá che hầm giếng thẳng đứng với bậc sắt. Ánh sáng chói lòa từ đáy. Cô một mình leo xuống.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Hầm giếng bí mật",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Nhà thờ ánh sáng",
                "activities": [
                    {"title": "Flashcards: Nhà thờ ánh sáng",
                     "description": "Học 4 từ: cathedral, spiraling, awareness, intelligence",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhà thờ ánh sáng",
                     "description": "Dưới đáy hầm là không gian khổng lồ như nhà thờ, tường phủ đầy ký hiệu xoắn ốc. Ánh sáng tràn ngập mọi nơi — sống động, cổ xưa, và thông minh. Tri thức tuôn vào tâm trí Maya.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhà thờ ánh sáng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Bí mật của bảy ánh sáng",
                "activities": [
                    {"title": "Flashcards: Bí mật bảy ánh sáng",
                     "description": "Học 4 từ: consciousness, tectonic, descendants, radiating",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bí mật bảy ánh sáng",
                     "description": "Bảy ánh sáng là một ý thức cổ đại duy nhất giữ cân bằng Trái Đất. Dòng họ Voss được chọn làm người bảo hộ. Maya là người mạnh nhất — cô cảm nhận cả bảy ánh sáng cùng lúc.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bí mật bảy ánh sáng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Món quà và sứ mệnh",
                "activities": [
                    {"title": "Flashcards: Món quà và sứ mệnh",
                     "description": "Học 4 từ: transformation, fundamentally, synchronized, harmonious",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Món quà và sứ mệnh",
                     "description": "Ánh sáng ban cho Maya khả năng thở dưới nước. Cô leo lên sau 2 giờ, da phát sáng nhẹ. Bảy trên bảy hoàn thành — giờ cô cần đến nexus dưới đáy đại dương.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Món quà và sứ mệnh",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 16",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 16 từ lúc tìm hầm giếng đến khi hoàn thành bảy trên bảy.",
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
    print(f"Chapter 16 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
