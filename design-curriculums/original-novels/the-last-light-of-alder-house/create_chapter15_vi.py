#!/usr/bin/env python3
"""Chapter 15: The Singer and The Dreamer — bilingual Vietnamese-English curriculum."""

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
    "They reached Mist Harbor at sunset. It was a tiny fishing village clinging to the edge of a cliff, even smaller "
    "than Alder Bay. A few houses, a general store, and a dock with three boats. The whole place was wrapped in fog — "
    "thick, white fog that rolled in from the ocean and filled the streets like smoke.\n\n"
    '"Mist Harbor," Sam said. "Well named."\n\n'
    "They parked near the dock and walked along the shore. The fog was so thick that Maya could barely see twenty feet "
    "ahead. The sound of the waves was muffled, distant, as if the ocean was whispering instead of roaring.\n\n"
    "Maya felt the light before she saw it. A pull in her chest, like a magnet. She followed the feeling along the "
    "shore, past the dock, past the last house, to a rocky point at the edge of the village.\n\n"
    "There, in a tidal pool between the rocks, the water was glowing.\n\n"
    "Not brightly — just a faint shimmer, like moonlight on the surface. But Maya knew what it was. The fifth light. "
    "The Singer.\n\n"
    "She knelt beside the tidal pool and put her hands in the water. It was warm — much warmer than it should have "
    "been. And as her fingers touched the glow, she heard something.\n\n"
    "Music.\n\n"
    "Not real music — not instruments or voices. But a sound that was like music, the way a sunset is like a painting. "
    "A deep, resonant hum that seemed to come from everywhere at once — from the water, from the rocks, from the fog "
    "itself. It was the most beautiful sound Maya had ever heard."
)

SECTION_2 = (
    "The visions came with the music. She saw the network from above — five points now glowing brightly, connected by "
    "lines of light. The remaining two points flickered weakly in the south. But the network was stronger. She could "
    "feel it — a stability, a solidity that hadn't been there before.\n\n"
    "And she heard the voice again — the voice of the light.\n\n"
    '"Five of seven," it said. "The song grows stronger. But the last two are fading. You must hurry."\n\n'
    '"I\'m trying," Maya said.\n\n'
    '"The Dreamer is close. You can reach it tonight. But The Key — The Deep Place — that one will test you. It is not '
    'like the others. It is deeper. Older. And it guards the way to the nexus."\n\n'
    '"What do I need to do when I get there?"\n\n'
    '"You will know. The light will show you. Trust yourself, Maya. You are more than you think."\n\n'
    "The music faded. The glow in the tidal pool dimmed. Maya pulled her hands out of the water and sat back on the "
    "rocks.\n\n"
    '"Five down," she said.\n\n'
    'Sam was standing behind her, his face pale in the fog. "I heard it," he said. "The music. It was..." He couldn\'t '
    "find the words.\n\n"
    '"I know," Maya said.'
)

SECTION_3 = (
    "They got back in the truck and drove south. Shell Beach — The Dreamer — was about eighty miles away, near a town "
    "called Bodega Bay. They drove through the night, taking turns at the wheel, stopping only for gas and coffee.\n\n"
    "They reached Shell Beach at two in the morning. It was a small, crescent-shaped beach surrounded by low cliffs. "
    "The sand was white and covered with shells — thousands of them, in every shape and size, gleaming in the "
    "starlight.\n\n"
    "The light here was underground. Maya found it by following the pull in her chest to a spot at the back of the "
    "beach, where the sand met the cliff. She dug with her hands, and after a few inches, the sand began to glow.\n\n"
    "She dug deeper. The glow grew brighter. And then her hands broke through into empty space — a cavity beneath the "
    "sand, filled with light.\n\n"
    "Maya lay flat on the beach and reached down into the cavity. The light wrapped around her hands like warm silk."
)

SECTION_4 = (
    "The visions were different this time. She didn't see the network or the coast. She saw dreams.\n\n"
    "Other people's dreams. Hundreds of them, thousands of them, flowing through the light like a river. She saw a "
    "child dreaming of flying. An old woman dreaming of her dead husband. A fisherman dreaming of a perfect catch. A "
    "mother dreaming of her daughter's future.\n\n"
    "And she understood. The Dreamer was exactly what its name suggested. This light was connected to the dreams of "
    "everyone who lived along the coast. It gathered their dreams, held them, and sent them back — transformed, "
    "enriched, made more vivid and more meaningful.\n\n"
    "The bad dreams that had been plaguing Alder Bay — they weren't caused by the light. They were caused by the "
    "light's weakness. When the network was strong, the dreams were good. When the network was weak, the dreams turned "
    "dark.\n\n"
    "Maya strengthened the connection. She felt the sixth point lock into place, bright and solid. Six of seven.\n\n"
    "She pulled her hands out and sat up. Sand clung to her clothes and hair. She was exhausted — more tired than she "
    "had ever been in her life. But she was also exhilarated.\n\n"
    "One more. Just one more.\n\n"
    '"The Deep Place," she said to Sam. "How far?"\n\n'
    'Sam checked the map. "About a hundred and fifty miles south. Near Big Sur. But Maya..." He looked at her with '
    'concern. "You need to rest. You\'ve touched four lights in twenty-four hours. You look like you\'re about to '
    'collapse."'
)

SECTION_5 = (
    '"I\'m fine."\n\n'
    '"You\'re not fine. You\'re shaking. Your nose is bleeding."\n\n'
    "Maya touched her upper lip. Her fingers came away red. She hadn't even noticed.\n\n"
    '"The light is taking something from you," Sam said. "Energy, or life force, or whatever you want to call it. Each '
    'time you connect, it costs you something. You need to recover before you try the last one."\n\n'
    "Maya wanted to argue, but her body agreed with Sam. Her legs were weak, her vision was blurry, and her hands were "
    "trembling.\n\n"
    '"Okay," she said. "We rest. But just for a few hours."\n\n'
    "They found a motel in Bodega Bay — a small, cheap place with a flickering neon sign. Sam got two rooms. Maya "
    "barely made it to the bed before she collapsed.\n\n"
    "She slept for six hours. Deep, dreamless sleep — the kind she hadn't had since before coming to Alder Bay. When "
    "she woke up, the sun was high, and she felt better. Not perfect, but better.\n\n"
    "Sam was waiting in the truck with coffee and sandwiches from a gas station.\n\n"
    '"How do you feel?" he asked.\n\n'
    '"Human again." She took the coffee gratefully. "How many days do we have left?"\n\n'
    '"Eleven. Frank\'s deadline is in eleven days."\n\n'
    '"Then let\'s go find The Deep Place."\n\n'
    "They drove south along Highway 1, the famous coast road that wound along the cliffs of Big Sur. The scenery was "
    "spectacular — towering cliffs, crashing waves, bridges spanning deep canyons. But Maya barely noticed. Her mind "
    "was focused on what lay ahead.\n\n"
    "The Deep Place. The Key. The last light.\n\n"
    "And beyond it, somehow, the nexus.\n\n"
    "Catherine's map showed The Deep Place at a point on the coast where the cliffs were highest and the ocean was "
    "deepest. There was no town nearby, no road, no trail. Just wilderness.\n\n"
    '"How do we even get there?" Sam asked, studying the map.\n\n'
    "Maya looked at the coastline passing outside the window. Somewhere out there, beneath the cliffs and the ocean, "
    "the seventh light was waiting.\n\n"
    '"I think," she said slowly, "that the light will show us the way."\n\n'
    "And as if in answer, she felt the pull in her chest again — stronger than ever, pulling her south, pulling her "
    "down, pulling her toward something ancient and powerful and unknown.\n\n"
    "The Key was calling.\n\n"
    "And Maya was almost there."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["clinging", "muffled", "shimmer", "resonant"]
S2_VOCAB = ["stability", "flickered", "solidity", "fading"]
S3_VOCAB = ["crescent", "gleaming", "cavity", "underground"]
S4_VOCAB = ["plaguing", "enriched", "exhilarated", "collapse"]
S5_VOCAB = ["trembling", "recover", "spectacular", "wilderness"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 15: Ca Sĩ Và Kẻ Mộng Mơ (The Singer and The Dreamer)",
        "preview": {
            "text": (
                "Maya chạm ánh sáng thứ 5 tại Mist Harbor — trong vũng thủy triều vang lên âm "
                "nhạc kỳ diệu. Rồi đến Shell Beach, ánh sáng thứ 6 nằm dưới cát, cho cô thấy "
                "giấc mơ của mọi người dọc bờ biển. Nhưng cái giá phải trả ngày càng lớn — mũi "
                "Maya chảy máu, cô kiệt sức. Họ dừng lại nghỉ ở motel. Học 20 từ vựng tiếng Anh "
                "trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 15. Maya chạm hai ánh sáng liên tiếp "
            "— The Singer và The Dreamer — nhưng cơ thể cô bắt đầu kiệt sức vì cái giá phải trả."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Âm nhạc tại Mist Harbor",
                "activities": [
                    {"title": "Flashcards: Âm nhạc tại Mist Harbor",
                     "description": "Học 4 từ: clinging, muffled, shimmer, resonant",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Âm nhạc tại Mist Harbor",
                     "description": "Maya và Sam đến làng chài nhỏ xíu chìm trong sương mù. Ánh sáng thứ 5 nằm trong vũng thủy triều — khi Maya chạm vào, cô nghe thấy âm nhạc tuyệt đẹp.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Âm nhạc tại Mist Harbor",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Lời cảnh báo của ánh sáng",
                "activities": [
                    {"title": "Flashcards: Lời cảnh báo",
                     "description": "Học 4 từ: stability, flickered, solidity, fading",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lời cảnh báo",
                     "description": "Ánh sáng cho Maya thấy mạng lưới 5 điểm đã sáng, nhưng cảnh báo — The Deep Place sẽ thử thách cô. Sam cũng nghe được âm nhạc.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lời cảnh báo",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Shell Beach lúc 2 giờ sáng",
                "activities": [
                    {"title": "Flashcards: Shell Beach",
                     "description": "Học 4 từ: crescent, gleaming, cavity, underground",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Shell Beach",
                     "description": "Họ lái xe xuyên đêm đến Shell Beach. Maya đào cát và tìm thấy ánh sáng thứ 6 ẩn trong khoang trống dưới lòng đất.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Shell Beach",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Giấc mơ của mọi người",
                "activities": [
                    {"title": "Flashcards: Giấc mơ",
                     "description": "Học 4 từ: plaguing, enriched, exhilarated, collapse",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Giấc mơ",
                     "description": "Ánh sáng The Dreamer cho Maya thấy giấc mơ của mọi người dọc bờ biển. Cô hiểu ra ác mộng ở Alder Bay là do mạng lưới yếu đi. Sáu trên bảy hoàn thành.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Giấc mơ",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Cái giá phải trả",
                "activities": [
                    {"title": "Flashcards: Cái giá phải trả",
                     "description": "Học 4 từ: trembling, recover, spectacular, wilderness",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Cái giá phải trả",
                     "description": "Mũi Maya chảy máu, tay run, mắt mờ. Sam bắt cô nghỉ ngơi. Sau 6 tiếng ngủ ở motel, họ lên đường tìm ánh sáng cuối cùng — The Deep Place.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Cái giá phải trả",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 15",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 15 từ Mist Harbor đến khi lên đường tìm The Deep Place.",
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
    print(f"Chapter 15 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
