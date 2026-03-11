#!/usr/bin/env python3
"""Chapter 12: Racing the Dawn — bilingual Vietnamese-English curriculum."""

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
    "Ben drove fast. The coast highway was empty at this hour — just their headlights cutting through the darkness, the "
    "ocean invisible but audible on their left.\n\n"
    '"So let me understand this," Ben said, his eyes on the road. "There are seven magical lights buried along the coast. '
    "They're connected like a network. The earth needs them to stay balanced. And you — specifically you — need to touch "
    'all seven before the next new moon, or the whole system collapses."\n\n'
    '"That\'s the short version, yes."\n\n'
    '"And Frank Burke wants to pour concrete into the one under your house."\n\n"Also yes."\n\n'
    '"And we\'re driving to the third light right now, in the middle of the night, because Frank is coming at dawn."\n\n'
    '"Correct."\n\n'
    "Ben was quiet for a moment. \"This is the strangest night of my life. And I was kidnapped by a glowing ocean, so "
    "that's saying something.\"\n\n"
    "Maya laughed. It felt good to laugh. \"Thank you for coming with me.\"\n\n"
    '"Thank me when we survive." He glanced at the map on the dashboard. "Redwood Cove is about twenty miles south. '
    "There's a state park there — I went camping once as a kid. The cove is at the bottom of a big cliff, surrounded by "
    'redwood trees."\n\n'
    '"Any caves?"\n\n'
    '"I don\'t remember. But if the other lights are anything like the ones we\'ve seen, there\'ll be a way down."'
)

SECTION_2 = (
    "They found the turnoff for Redwood Cove State Park at one in the morning. The park was closed — a chain blocked the "
    "entrance road — but Ben drove around it on the shoulder. They followed a dirt road through enormous redwood trees, "
    "their trunks wider than the car, their tops invisible in the darkness above.\n\n"
    "The road ended at a small parking lot near the cliff edge. They got out and stood in the silence of the forest. It "
    "was different here — no wind, no waves. Just the deep, ancient quiet of the redwoods.\n\n"
    '"There," Maya said, pointing her flashlight at the ground. A trail led from the parking lot to the cliff edge, marked '
    "with a wooden sign: COVE TRAIL — STEEP — USE CAUTION.\n\n"
    "They followed the trail down. It was better maintained than the paths at Alder House and Cape Sorrow — wooden steps, "
    "rope railings, signs warning about loose rocks. But it was still steep, and in the dark, every step felt dangerous.\n\n"
    "The trail ended at a small beach at the bottom of the cliff. The cove was sheltered and calm — the water barely moved. "
    "Redwood trees grew right to the edge of the cliff above, their roots hanging over the rock like curtains.\n\n"
    "And there, at the back of the cove, was the glow.\n\n"
    "It was coming from behind a waterfall — a thin stream of water falling from the cliff into a pool at its base. Behind "
    "the water, Maya could see the blue-white light, pulsing steadily.\n\n"
    '"Behind the waterfall," she said. "Of course."'
)

SECTION_3 = (
    "They waded through the shallow pool — the water was freezing — and pushed through the waterfall. Behind it was a "
    "cave, smaller than the one at Cape Sorrow but with the same features: rough stone walls, a low ceiling, and a hole "
    "in the floor filled with light.\n\n"
    "Maya knelt beside the hole and put her hands into the glow.\n\n"
    "The warmth flowed through her immediately. The visions came — faster this time, clearer. She saw the redwood forest "
    "as it was a thousand years ago, vast and untouched. She saw native people dancing around a fire near the cove. She "
    "saw the light beneath the earth, flowing like a river, connecting point to point along the coast.\n\n"
    "And she felt the connection strengthen. Like a wire being tightened, a string being tuned. The light at Redwood Cove "
    "recognized her, accepted her, and linked itself more firmly to the lights at Alder Bay and Cape Sorrow.\n\n"
    "Three down. Four to go.\n\n"
    "Maya pulled her hands back. She was breathing hard, and her whole body was tingling.\n\n"
    '"Are you okay?" Ben asked.\n\n'
    '"Better than okay. It\'s working. I can feel the connections getting stronger."'
)

SECTION_4 = (
    "They climbed back up the trail to the car. Maya checked her phone. It was two-thirty in the morning. Dawn was in "
    "about four hours.\n\n"
    '"We can\'t do another one tonight," Ben said, reading her mind. "We need to get back before Frank."\n\n'
    "He was right. The next point — Point Silence — was another fifty miles south. There wasn't enough time.\n\n"
    '"Okay," Maya said. "Let\'s go home."\n\n'
    "The drive back took almost three hours. Ben drove while Maya dozed in the passenger seat, exhausted but unable to "
    "fully sleep. Her mind kept turning over the same questions. How was she going to visit four more lights in less than "
    "a month? How was she going to stop Frank? And what would happen if she failed?\n\n"
    "They reached Alder Bay just before six in the morning. The sky was turning gray in the east. Maya dropped Ben at his "
    "house — Lily was waiting on the porch, and she ran to her brother with a cry that Maya could hear from the car.\n\n"
    "Then Maya drove up Cliff Road to Alder House."
)

SECTION_5 = (
    "Sam was sitting on the porch steps, wrapped in a blanket, drinking coffee from a thermos. He stood up when he saw "
    "her.\n\n"
    '"You look terrible," he said.\n\n"Thanks. Anything happen?"\n\n'
    '"Quiet night. But I saw headlights on the road about an hour ago. Someone drove up partway and then turned around. '
    'I think Frank was checking to see if anyone was here."\n\n'
    "Maya looked down the road. In the growing light, she could see the town below. Somewhere down there, Frank Burke was "
    "getting ready.\n\n"
    '"He\'s coming," she said.\n\n"I know." Sam handed her the thermos. "What\'s the plan?"\n\n'
    "Maya drank the coffee. It was hot and strong and exactly what she needed.\n\n"
    '"The plan," she said, "is to not let him in."\n\n'
    '"That\'s it? That\'s the whole plan?"\n\n'
    '"I\'m working on the rest." She looked at the house behind her. In the early morning light, it looked almost beautiful '
    "— old and proud, standing on the cliff like it had stood for over a century. Guarding what was below.\n\n"
    '"Sam, I need to tell you something. I went to two more lights last night. Cape Sorrow and Redwood Cove. I touched '
    'them, and I felt the connections strengthen. The network is real, and it\'s responding to me."\n\n'
    '"That\'s good, right?"\n\n'
    '"It\'s good. But I need to reach four more. And I need to do it before the next new moon — that\'s twenty-six days '
    "from now. And I need to keep Frank away from the basement while I do it.\"\n\n"
    'Sam was quiet for a moment. "You can\'t do all of that alone."\n\n"I know."\n\n'
    '"So let me help. And Ben — he\'ll help too, after what he\'s been through. And Lily. And maybe others. Not everyone '
    'in town agrees with Frank."\n\n'
    "Maya felt something warm in her chest — not the light this time, but something simpler. Gratitude. Friendship.\n\n"
    '"Thank you," she said.\n\n'
    "The sound of engines broke the morning quiet. Maya and Sam turned to look down Cliff Road.\n\n"
    "Three trucks were coming up the hill. The first one was Frank's black pickup. Behind it, two larger trucks — one "
    "carrying bags of concrete mix, the other loaded with tools and equipment.\n\n"
    "Frank Burke was here. And he had brought an army.\n\n"
    "Maya set down the coffee thermos and stood up straight.\n\n"
    '"Here we go," she said.'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["audible", "collapses", "dashboard", "kidnapped"]
S2_VOCAB = ["enormous", "sheltered", "maintained", "curtains"]
S3_VOCAB = ["tingling", "recognized", "untouched", "strengthen"]
S4_VOCAB = ["dozed", "exhausted", "partway", "thermos"]
S5_VOCAB = ["gratitude", "responding", "century", "equipment"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 12: Chạy Đua Với Bình Minh (Racing the Dawn)",
        "preview": {
            "text": (
                "Maya và Ben lái xe đến Redwood Cove giữa đêm — ánh sáng thứ ba ẩn sau thác "
                "nước. Maya chạm vào và cảm nhận mạng lưới mạnh lên. Họ chạy đua về Alder Bay "
                "trước bình minh, nhưng Frank đã đến với xe tải bê tông và đội quân sáu người. "
                "Học 20 từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 12. Maya và Ben tìm ánh sáng thứ ba "
            "ở Redwood Cove, rồi chạy đua về nhà trước khi Frank đến với bê tông lúc bình minh."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Lái xe trong đêm",
                "activities": [
                    {"title": "Flashcards: Lái xe trong đêm",
                     "description": "Học 4 từ: audible, collapses, dashboard, kidnapped",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lái xe trong đêm",
                     "description": "Ben lái xe trên đường ven biển vắng lặng. Hai người tóm tắt tình hình — bảy ánh sáng, Frank, và cuộc chạy đua với thời gian.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lái xe trong đêm",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Rừng cổ thụ Redwood",
                "activities": [
                    {"title": "Flashcards: Rừng cổ thụ Redwood",
                     "description": "Học 4 từ: enormous, sheltered, maintained, curtains",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Rừng cổ thụ Redwood",
                     "description": "Họ vào công viên đóng cửa, đi qua rừng redwood khổng lồ, leo xuống vịnh yên tĩnh — ánh sáng lấp lánh sau thác nước.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Rừng cổ thụ Redwood",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Chạm ánh sáng thứ ba",
                "activities": [
                    {"title": "Flashcards: Chạm ánh sáng thứ ba",
                     "description": "Học 4 từ: tingling, recognized, untouched, strengthen",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Chạm ánh sáng thứ ba",
                     "description": "Maya đặt tay vào ánh sáng — thấy rừng ngàn năm trước, người bản địa nhảy múa. Kết nối mạnh lên. Ba xong, còn bốn.",
                     "activityType": "reading", "practiceMinutes": 4,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Chạm ánh sáng thứ ba",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Chạy đua về nhà",
                "activities": [
                    {"title": "Flashcards: Chạy đua về nhà",
                     "description": "Học 4 từ: dozed, exhausted, partway, thermos",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Chạy đua về nhà",
                     "description": "Không đủ thời gian đến điểm tiếp theo. Họ lái ba tiếng về Alder Bay — Maya ngủ gật, Ben lái. Về đến nơi lúc sáu giờ sáng.",
                     "activityType": "reading", "practiceMinutes": 4,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Chạy đua về nhà",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Frank đến với đội quân",
                "activities": [
                    {"title": "Flashcards: Frank đến",
                     "description": "Học 4 từ: gratitude, responding, century, equipment",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Frank đến",
                     "description": "Sam canh nhà cả đêm. Maya kể về mạng lưới và xin giúp đỡ. Rồi tiếng động cơ — Frank đến với ba xe tải và sáu người.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Frank đến",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 12",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 12 từ chuyến đi Redwood Cove đến khi Frank xuất hiện lúc bình minh.",
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
    print(f"Chapter 12 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
