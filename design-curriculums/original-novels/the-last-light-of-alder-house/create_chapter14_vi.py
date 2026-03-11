#!/usr/bin/env python3
"""Chapter 14: The Road South — bilingual Vietnamese-English curriculum."""

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
    "Maya and Sam left Alder Bay at five in the morning, before the sun was up. Sam drove his truck — it was more "
    "reliable than Maya's old car for the rough coastal roads they might encounter.\n\n"
    "Maya had spent most of the night reading Eleanor's journals. She had found important things — things that changed "
    "her understanding of the light and her family's connection to it.\n\n"
    "Eleanor had discovered, late in her life, that the Voss women didn't just guard the light. They were part of it. "
    "The bond between the family and the light was not just emotional or spiritual — it was physical. Something in their "
    "blood, their DNA, resonated with the light's frequency. That was why the light responded to them. That was why it "
    "needed them.\n\n"
    "And Eleanor had discovered something else. The bond grew stronger with each generation. Catherine had been able to "
    "sense the light. Margaret had been able to communicate with it. Eleanor had been able to see through it — to use it "
    "as a window into the past and future.\n\n"
    "What would Maya be able to do?\n\n"
    "She didn't know yet. But she could feel the potential inside her, like a seed waiting to grow.\n\n"
    '"You\'re quiet," Sam said, glancing at her.\n\n'
    '"Thinking."\n\n'
    '"About?"\n\n'
    '"About what I\'m becoming." She looked out the window at the passing forest. "My grandmother could see visions in '
    "the light. My great-grandmother could talk to it. My great-great-grandmother could sense it. Each generation got "
    'stronger. What does that make me?"\n\n'
    '"Special," Sam said simply.\n\n'
    'Maya smiled. "Or dangerous."'
)

SECTION_2 = (
    "They drove south through the morning, following the coast highway. The landscape changed as they crossed into "
    "California — the forests became taller, the cliffs steeper, the ocean wilder. They stopped for gas and coffee at "
    "a small town called Crescent City, then continued south.\n\n"
    "Point Silence was marked on Catherine's map as being near a place called Gold Bluffs Beach, in a remote section "
    "of Redwood National Park. They arrived just before noon.\n\n"
    "The beach was stunning — a long stretch of golden sand backed by towering cliffs covered in ferns and moss. The "
    "ocean was rough here, with big waves rolling in from the west. And the beach was empty. Completely, perfectly "
    "empty.\n\n"
    '"I can see why they call it Point Silence," Sam said. "There\'s nobody here."\n\n'
    "They walked along the beach, looking for signs of the light. Maya held Catherine's map and tried to match the "
    "landmarks — a distinctive rock formation, a creek flowing across the sand, a section of cliff that jutted out "
    "further than the rest.\n\n"
    '"There," Maya said, pointing to the jutting cliff. "That\'s the spot."\n\n'
    "They climbed over rocks to reach the base of the cliff. And there, hidden behind a curtain of hanging ferns, was "
    "a cave entrance."
)

SECTION_3 = (
    "This cave was different from the others. It was larger, with a high ceiling and smooth walls that looked almost "
    "polished. The floor was covered with fine sand, and the air was warm and dry. And the light — the fourth light — "
    "was not in a hole in the floor.\n\n"
    "It was in the wall.\n\n"
    "A section of the cave wall, about six feet tall and three feet wide, was glowing. The blue-white light shone "
    "through the rock itself, as if the stone was transparent. Maya could see shapes moving inside the glow — slow, "
    "graceful shapes, like fish swimming in deep water.\n\n"
    '"It\'s beautiful," Sam whispered.\n\n'
    "Maya approached the wall and placed both hands flat against it. The stone was warm and smooth, and the light "
    "flowed around her fingers like water.\n\n"
    "The visions came. This time, they were different.\n\n"
    "She didn't see the past. She saw the present.\n\n"
    "She saw Alder Bay from above, as if she was a bird flying over the town. She saw the harbor, the main street, "
    "the houses climbing the hillside. She saw Alder House on the cliff, dark and solid. And she saw the light beneath "
    "it, pulsing steadily.\n\n"
    "Then her vision shifted south. She saw Cape Sorrow, its light glowing in the cave at the base of the cliff. She "
    "saw Redwood Cove, the light shining behind the waterfall. She saw Point Silence — herself, standing in this cave, "
    "her hands on the wall.\n\n"
    "And she saw the connections between them. Lines of light, running beneath the earth and the ocean, linking the "
    "four points she had touched. The lines were bright and strong — stronger than before. The network was healing.\n\n"
    "But the three remaining points were dim. Their lights were fading, their connections weak. Without someone to "
    "touch them, to strengthen them, they would eventually go dark. And when they did, the network would fail.\n\n"
    "Maya pulled her hands away. The vision faded.\n\n"
    '"Four down," she said. "Three to go."'
)

SECTION_4 = (
    "They left Point Silence and drove south. The next point — Mist Harbor — was about a hundred miles away, near a "
    "small town called Shelter Cove. They could reach it by evening if they hurried.\n\n"
    "As Sam drove, Maya studied Catherine's map more carefully. She noticed something she hadn't seen before. Next to "
    "each of the seven points, Catherine had written small notes in pencil, barely visible.\n\n"
    'Next to Alder Bay: "The Guardian"\n'
    'Next to Cape Sorrow: "The Messenger"\n'
    'Next to Redwood Cove: "The Healer"\n'
    'Next to Point Silence: "The Watcher"\n'
    'Next to Mist Harbor: "The Singer"\n'
    'Next to Shell Beach: "The Dreamer"\n'
    'Next to The Deep Place: "The Key"\n\n'
    '"Each light has a name," Maya said. "Or a role. The Guardian, The Messenger, The Healer, The Watcher, The Singer, '
    'The Dreamer, The Key."\n\n'
    '"The Key," Sam repeated. "That sounds important."\n\n'
    '"It\'s the last one. The furthest south. Near Big Sur." Maya traced the lines on the map. "And it\'s closest to '
    'the nexus."\n\n'
    '"The underwater one."\n\n'
    '"Yeah." Maya folded the map. "I think The Key is exactly what it sounds like — the key to reaching the nexus. If '
    "I can get to The Deep Place and touch that light, maybe it will show me how to reach the center of the network.\"\n\n"
    '"And then what?"\n\n'
    '"And then... I don\'t know. But I think that\'s where this is all leading. To the nexus. To the center of everything."'
)

SECTION_5 = (
    "Sam was quiet for a while. The highway curved along the coast, offering glimpses of the ocean between the trees.\n\n"
    '"Maya," he said finally. "Can I ask you something personal?"\n\n'
    '"Sure."\n\n'
    '"Are you scared?"\n\n'
    'Maya thought about it. "Yes," she said. "But not of the light. I\'m scared of failing. I\'m scared of letting '
    "people down — the town, Eleanor, my family. I'm scared that I'm not strong enough.\"\n\n"
    '"You found Ben in a cave sixty miles away in the middle of the night. You faced down Frank Burke and his concrete '
    "trucks. You're driving five hundred miles to touch magical lights in caves.\" Sam smiled. \"I think you're strong "
    'enough."\n\n'
    "Maya looked at him. In the afternoon light, his face was warm and kind. She felt something shift between them — a "
    "closeness that hadn't been there before.\n\n"
    '"Thanks, Sam," she said.\n\n'
    '"Anytime."\n\n'
    "They drove on. The sun was getting lower, painting the sky in shades of orange and pink. Somewhere ahead, the fifth "
    "light was waiting.\n\n"
    "And somewhere behind them, in Alder Bay, Frank Burke was counting the days.\n\n"
    "Thirteen left."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["reliable", "resonated", "spiritual", "potential"]
S2_VOCAB = ["stunning", "distinctive", "towering", "landmarks"]
S3_VOCAB = ["transparent", "graceful", "steadily", "connections"]
S4_VOCAB = ["visible", "traced", "furthest", "nexus"]
S5_VOCAB = ["glimpses", "closeness", "concrete", "magical"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 14: Con Đường Phía Nam (The Road South)",
        "preview": {
            "text": (
                "Maya và Sam lái xe về phía nam, chạm vào ánh sáng thứ 4 tại Point Silence — "
                "ẩn trong vách hang động. Maya thấy ảo ảnh về mạng lưới đang hồi phục và phát "
                "hiện bản đồ Catherine ghi tên cho từng ánh sáng: Guardian, Messenger, Healer, "
                "Watcher, Singer, Dreamer, Key. Học 20 từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 14. Maya và Sam lái xe về phía nam, "
            "chạm ánh sáng thứ 4, và khám phá mỗi ánh sáng đều có tên riêng trên bản đồ Catherine."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Lên đường lúc rạng sáng",
                "activities": [
                    {"title": "Flashcards: Lên đường lúc rạng sáng",
                     "description": "Học 4 từ: reliable, resonated, spiritual, potential",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lên đường lúc rạng sáng",
                     "description": "Maya và Sam rời Alder Bay lúc 5 giờ sáng. Maya suy ngẫm về sợi dây liên kết ngày càng mạnh giữa phụ nữ dòng họ Voss và ánh sáng.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lên đường lúc rạng sáng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Đến Point Silence",
                "activities": [
                    {"title": "Flashcards: Đến Point Silence",
                     "description": "Học 4 từ: stunning, distinctive, towering, landmarks",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đến Point Silence",
                     "description": "Họ đến Gold Bluffs Beach — bãi biển vắng lặng tuyệt đẹp. Maya tìm thấy cửa hang ẩn sau rèm dương xỉ dưới chân vách đá.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đến Point Silence",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Ánh sáng trong vách đá",
                "activities": [
                    {"title": "Flashcards: Ánh sáng trong vách đá",
                     "description": "Học 4 từ: transparent, graceful, steadily, connections",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ánh sáng trong vách đá",
                     "description": "Ánh sáng thứ 4 phát ra từ vách hang. Maya chạm vào và thấy ảo ảnh — bốn điểm sáng nối liền, mạng lưới đang hồi phục, nhưng ba điểm còn lại đang mờ dần.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ánh sáng trong vách đá",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Bảy cái tên trên bản đồ",
                "activities": [
                    {"title": "Flashcards: Bảy cái tên",
                     "description": "Học 4 từ: visible, traced, furthest, nexus",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bảy cái tên",
                     "description": "Maya phát hiện Catherine đã ghi tên cho từng ánh sáng — Guardian, Messenger, Healer, Watcher, Singer, Dreamer, Key. Ánh sáng cuối cùng có thể là chìa khóa đến nexus.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bảy cái tên",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Nỗi sợ và sức mạnh",
                "activities": [
                    {"title": "Flashcards: Nỗi sợ và sức mạnh",
                     "description": "Học 4 từ: glimpses, closeness, concrete, magical",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nỗi sợ và sức mạnh",
                     "description": "Sam hỏi Maya có sợ không. Cô thú nhận sợ thất bại — nhưng Sam nhắc cô về tất cả những gì cô đã làm được. Phía trước, ánh sáng thứ 5 đang chờ.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nỗi sợ và sức mạnh",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 14",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 14 từ lúc lên đường đến khi phát hiện tên của bảy ánh sáng.",
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
    print(f"Chapter 14 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
