#!/usr/bin/env python3
"""Chapter 17: Coming Home — bilingual Vietnamese-English curriculum."""

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
    "The drive back to Alder Bay took twelve hours. They drove through the night, switching drivers every few hours, "
    "stopping only for gas and food. Maya slept when she wasn't driving — deep, restful sleep filled with dreams of "
    "light and water.\n\n"
    "They arrived in Alder Bay at noon the next day. The town looked the same — quiet, gray, huddled around the "
    "harbor. But Maya could feel something different. The air was cleaner. The ocean was calmer. And the strange, heavy "
    "feeling that had hung over the town since she arrived was lighter.\n\n"
    "The network was stronger. The town could feel it, even if the people didn't understand why.\n\n"
    "Ben and Lily were waiting at Alder House. They had kept watch in shifts, sleeping in the guest bedrooms on the "
    "second floor. Nothing had happened — no visits from Frank, no strange lights, no disturbances.\n\n"
    '"The dreams stopped," Lily said. "Two nights ago. My mom slept through the whole night for the first time in '
    'weeks. Same with half the town."\n\n'
    '"The tides are back to normal too," Ben added. "And the fish are coming back to the bay. Whatever you did out '
    'there, it\'s working."\n\n'
    "Maya felt a wave of relief. The connections were holding. The network was healing.\n\n"
    "But it wasn't enough. She still needed to reach the nexus."
)

SECTION_2 = (
    "She spread Catherine's map on the kitchen table and explained what she had learned at The Deep Place. The seven "
    "lights. The ancient consciousness. The nexus beneath the ocean.\n\n"
    '"So you need to go underwater," Ben said. "To the bottom of a deep ocean canyon. To touch the center of a network '
    'of magical lights."\n\n'
    '"Yes."\n\n'
    '"And the light gave you the ability to breathe underwater."\n\n'
    '"I think so. I can feel something different in my lungs. Something the light put there."\n\n'
    '"You think so," Lily repeated. "Maya, you can\'t just jump into the ocean and hope for the best. If you\'re '
    'wrong—"\n\n'
    '"I know. That\'s why I need to test it first."\n\n'
    "They went down to the harbor that afternoon. Maya stood at the end of the dock, looking at the cold, gray water. "
    "Sam, Ben, and Lily stood behind her, ready to pull her out if something went wrong.\n\n"
    "Maya took a deep breath and jumped in."
)

SECTION_3 = (
    "The water was freezing. It hit her like a wall of ice, and for a moment, she couldn't think, couldn't move, "
    "couldn't breathe. She sank below the surface, her body rigid with shock.\n\n"
    "Then the warmth came. Starting in her chest and spreading outward, pushing back the cold. Her lungs, which had "
    "been burning for air, suddenly relaxed. She opened her mouth — and breathed.\n\n"
    "Water flowed in and out of her lungs, and she could breathe. Not like breathing air — it was heavier, slower, "
    "stranger. But it worked. Oxygen flowed into her blood. Her heart beat steadily. She was alive, underwater, "
    "breathing.\n\n"
    "She opened her eyes. The harbor water was murky, but she could see — the wooden pillars of the dock, the sandy "
    "bottom, a school of small fish darting away from her. And she could see something else. A faint glow, coming from "
    "below — the light beneath Alder House, shining through the rock and earth, visible even from the harbor.\n\n"
    "She surfaced after three minutes. Sam grabbed her arm and pulled her onto the dock. She was soaking wet and "
    "grinning.\n\n"
    '"It works," she said. "I can breathe underwater."\n\n'
    '"That\'s impossible," Lily said.\n\n'
    '"A lot of impossible things have happened this week," Maya said.'
)

SECTION_4 = (
    "They spent the next few days preparing. Ben, who was an experienced fisherman, knew the waters off the coast. He "
    "studied nautical charts and identified the underwater canyon that Catherine's map pointed to — it was called the "
    "Alder Canyon, about two miles offshore, dropping to a depth of over a thousand feet.\n\n"
    '"A thousand feet," Sam said. "Maya, that\'s deep. Really deep. Even with the breathing thing, the pressure '
    'alone—"\n\n'
    '"The light will protect me," Maya said. She could feel it — the seven lights inside her, ready to shield her, '
    'guide her, sustain her. "I know it will."\n\n'
    '"How do you know?"\n\n'
    '"Because it needs me to get there. It wouldn\'t have given me this ability if it was going to let me die."\n\n'
    "It was a good argument, but Maya could see that her friends were not fully convinced. She wasn't fully convinced "
    "either. But she had no choice. The nexus was the key to everything — to stabilizing the network permanently, to "
    "freeing herself from the burden of constant guardianship, to ensuring that the light would be safe for generations "
    "to come.\n\n"
    "She had to try.\n\n"
    "They set the dive for three days later — the day before Frank's deadline. It would be the new moon, when the "
    "light was strongest. Maya would have the maximum power available to her.\n\n"
    "In the meantime, she continued reading Eleanor's journals. She was near the end now — the final years of "
    "Eleanor's life. The entries were shorter, more tired, but still sharp and clear.\n\n"
    "January 15, 2023\n\n"
    "I am eighty years old today. The light wished me happy birthday — I felt it pulse three times when I woke up, "
    "like a heartbeat saying hello.\n\n"
    "I am tired. My body is failing. But the light is patient. It knows that Maya will come. It showed me, years ago — "
    "a vision of a young woman with dark hair, standing in the basement, her hands full of light. My granddaughter. "
    "The one Margaret tried to hide from me.\n\n"
    "I have written everything down. I have left the journals, the map, the cave. Everything Maya will need.\n\n"
    "I only hope it is enough.\n\n"
    "Maya closed the journal. Tears were running down her cheeks.\n\n"
    '"I\'m here, Eleanor," she whispered. "I came. Just like you said I would."\n\n'
    "The house was quiet around her. But beneath the floor, the light pulsed once — warm, gentle, grateful."
)

SECTION_5 = (
    "The night before the dive, Maya couldn't sleep. She sat on the back porch of Alder House, wrapped in a blanket, "
    "looking at the ocean. The sky was clear for once, and the stars were brilliant — thousands of them, scattered "
    "across the darkness like diamonds.\n\n"
    "Sam came out and sat beside her.\n\n"
    '"Can\'t sleep either?" he said.\n\n'
    '"Too much thinking."\n\n'
    "They sat in comfortable silence for a while. The ocean murmured below the cliff, steady and eternal.\n\n"
    '"Maya," Sam said. "Whatever happens tomorrow — I want you to know something."\n\n'
    '"What?"\n\n'
    '"I\'m glad you came to Alder Bay. I\'m glad I met you. And I\'m glad I got to be part of this... whatever this '
    'is."\n\n'
    "Maya looked at him. In the starlight, his face was soft and serious.\n\n"
    '"Me too," she said.\n\n'
    "She reached over and took his hand. They sat like that for a long time, holding hands in the darkness, listening "
    "to the ocean.\n\n"
    "Tomorrow, Maya would dive into the deep. Tomorrow, she would face the nexus. Tomorrow, everything would change.\n\n"
    "But tonight, she was just a woman sitting with a friend, looking at the stars, feeling the warmth of another "
    "person's hand.\n\n"
    "And that was enough."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["huddled", "disturbances", "relief", "shifts"]
S2_VOCAB = ["consciousness", "ability", "dock", "canyon"]
S3_VOCAB = ["rigid", "murky", "surfaced", "soaking"]
S4_VOCAB = ["nautical", "stabilizing", "guardianship", "burden"]
S5_VOCAB = ["brilliant", "eternal", "scattered", "comfortable"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 17: Trở Về Nhà (Coming Home)",
        "preview": {
            "text": (
                "Maya và Sam trở về Alder Bay. Thị trấn đã khá hơn — ác mộng biến mất, cá quay "
                "lại vịnh. Maya nhảy xuống bến cảng thử thở dưới nước — và thành công. Họ lên kế "
                "hoạch lặn xuống nexus. Maya đọc những dòng nhật ký cuối cùng của Eleanor — bà đã "
                "biết trước cháu gái sẽ đến. Học 20 từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 17. Maya trở về nhà, thử khả năng thở "
            "dưới nước, đọc nhật ký cuối của Eleanor, và chuẩn bị cho chuyến lặn định mệnh."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Trở về Alder Bay",
                "activities": [
                    {"title": "Flashcards: Trở về Alder Bay",
                     "description": "Học 4 từ: huddled, disturbances, relief, shifts",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Trở về Alder Bay",
                     "description": "Maya và Sam lái xe 12 tiếng về nhà. Thị trấn đã thay đổi — ác mộng biến mất, thủy triều bình thường, cá quay lại. Mạng lưới đang hồi phục.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Trở về Alder Bay",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Thử nghiệm tại bến cảng",
                "activities": [
                    {"title": "Flashcards: Thử nghiệm",
                     "description": "Học 4 từ: consciousness, ability, dock, canyon",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Thử nghiệm",
                     "description": "Maya giải thích về nexus dưới đại dương. Lily lo lắng — không thể nhảy xuống biển rồi hy vọng. Maya quyết định phải thử trước, và nhảy xuống bến cảng.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Thử nghiệm",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Thở dưới nước",
                "activities": [
                    {"title": "Flashcards: Thở dưới nước",
                     "description": "Học 4 từ: rigid, murky, surfaced, soaking",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Thở dưới nước",
                     "description": "Nước lạnh cóng nhưng hơi ấm lan ra từ ngực Maya. Cô mở miệng — và thở được dưới nước. Sau 3 phút, cô trồi lên mặt nước, cười toe toét.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Thở dưới nước",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Nhật ký cuối của Eleanor",
                "activities": [
                    {"title": "Flashcards: Nhật ký Eleanor",
                     "description": "Học 4 từ: nautical, stabilizing, guardianship, burden",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhật ký Eleanor",
                     "description": "Họ lên kế hoạch lặn vào ngày trăng non. Maya đọc nhật ký cuối của Eleanor — bà 80 tuổi, mệt mỏi nhưng tin rằng Maya sẽ đến. Ánh sáng dưới sàn nhà đập nhẹ, biết ơn.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhật ký Eleanor",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Đêm trước chuyến lặn",
                "activities": [
                    {"title": "Flashcards: Đêm trước chuyến lặn",
                     "description": "Học 4 từ: brilliant, eternal, scattered, comfortable",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đêm trước chuyến lặn",
                     "description": "Maya không ngủ được. Sam ra ngồi cạnh cô dưới bầu trời đầy sao. Anh nói vui vì được gặp cô. Họ nắm tay nhau trong bóng tối, nghe tiếng biển.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đêm trước chuyến lặn",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 17",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 17 từ lúc trở về Alder Bay đến đêm trước chuyến lặn.",
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
    print(f"Chapter 17 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
