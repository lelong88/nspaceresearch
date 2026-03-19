#!/usr/bin/env python3
"""
Song 1 Curriculum: "Heal the World" by Michael Jackson
Creates a vocabulary curriculum based on the song lyrics.
"""

import sys, json, re, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API = "https://helloapi.step.is"

# ---------------------------------------------------------------------------
# Strip keys
# ---------------------------------------------------------------------------
STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}

def strip_keys(obj):
    if isinstance(obj, dict):
        return {k: strip_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
    if isinstance(obj, list):
        return [strip_keys(i) for i in obj]
    return obj

# ---------------------------------------------------------------------------
# Song metadata
# ---------------------------------------------------------------------------
SONG_TITLE = "Heal the World"
ARTIST = "Michael Jackson"
YOUTUBE_URL = "https://www.youtube.com/watch?v=nhcG9wqn0gU"

# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------
W1 = ["heal", "brighter", "sorrow", "entire", "care", "space"]
W2 = ["bliss", "dread", "joyful", "grace", "reveal", "existing"]
W3 = ["spirits", "fear", "create", "nations", "plain", "heavenly"]
ALL = W1 + W2 + W3

# ---------------------------------------------------------------------------
# Lyrics
# ---------------------------------------------------------------------------
LYRICS_1 = """\
There's a place in your heart
And I know that it is love
And this place could be much brighter than tomorrow
And if you really try
You'll find there's no need to cry
In this place you'll feel there's no hurt or sorrow

There are ways to get there
If you care enough for the living
Make a little space
Make a better place

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me"""

LYRICS_2 = """\
If you want to know why
There's a love that cannot lie
Love is strong, it only cares of joyful giving
If we try, we shall see
In this bliss, we cannot feel fear or dread
We stop existing and start living

Then it feels that always
Love's enough for us growing
So make a better world
Make a better world

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

And the dream we were conceived in
Will reveal a joyful face
And the world we once believed in
Will shine again in grace
Then why do we keep strangling life
Wound this earth, crucify its soul
Though it's plain to see
This world is heavenly be God's glow"""

LYRICS_3 = """\
We could fly so high
Let our spirits never die
In my heart I feel you are all my brothers
Create a world with no fear
Together we cry happy tears
See the nations turn their swords into plowshares
We could really get there
If you cared enough for the living
Make a little space
To make a better place

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

There are people dying
If you care enough for the living
Make a better place for you and for me

There are people dying
If you care enough for the living
Make a better place for you and for me

You and for me"""


FULL_LYRICS = """\
There's a place in your heart
And I know that it is love
And this place could be much brighter than tomorrow
And if you really try
You'll find there's no need to cry
In this place you'll feel there's no hurt or sorrow

There are ways to get there
If you care enough for the living
Make a little space
Make a better place

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

If you want to know why
There's a love that cannot lie
Love is strong, it only cares of joyful giving
If we try, we shall see
In this bliss, we cannot feel fear or dread
We stop existing and start living

Then it feels that always
Love's enough for us growing
So make a better world
Make a better world

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

And the dream we were conceived in
Will reveal a joyful face
And the world we once believed in
Will shine again in grace
Then why do we keep strangling life
Wound this earth, crucify its soul
Though it's plain to see
This world is heavenly be God's glow

We could fly so high
Let our spirits never die
In my heart I feel you are all my brothers
Create a world with no fear
Together we cry happy tears
See the nations turn their swords into plowshares
We could really get there
If you cared enough for the living
Make a little space
To make a better place

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

Heal the world, make it a better place
For you and for me and the entire human race
There are people dying
If you care enough for the living
Make a better place for you and for me

There are people dying
If you care enough for the living
Make a better place for you and for me

There are people dying
If you care enough for the living
Make a better place for you and for me

You and for me"""


# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------
content = {
    "title": "Học Qua Bài Hát: 'Heal the World' – Michael Jackson",
    "description": (
        "BẠN CÓ BAO GIỜ NGHE MỘT BÀI HÁT MÀ TIM BẠN NHƯ NGHẸN LẠI?\n\n"
        "Có những giai điệu chạm đến nơi sâu nhất trong lòng bạn — nơi mà lời nói thường ngày không thể chạm tới. "
        "'Heal the World' của Michael Jackson là một trong những bài hát hiếm hoi có sức mạnh ấy. "
        "Từ đứa trẻ ở châu Phi đến người già ở Tokyo, ai cũng hiểu được thông điệp: "
        "thế giới này cần được chữa lành, và bạn — chính bạn — có thể bắt đầu.\n\n"
        "Hãy tưởng tượng bạn không chỉ nghe bài hát, mà còn HIỂU từng từ Michael Jackson hát. "
        "Từ 'sorrow' (nỗi buồn) đến 'grace' (ân sủng), từ 'bliss' (hạnh phúc tuyệt đối) đến 'spirits' (tinh thần) — "
        "mỗi từ vựng là một mảnh ghép giúp bạn cảm nhận bài hát sâu hơn gấp mười lần.\n\n"
        "Khi bạn hiểu được rằng 'heal' không chỉ là 'chữa lành' mà còn mang ý nghĩa phục hồi, tái sinh — "
        "bạn sẽ nghe bài hát bằng một đôi tai hoàn toàn mới. "
        "Đó là lúc âm nhạc trở thành người thầy vĩ đại nhất của bạn.\n\n"
        "18 từ vựng được chọn lọc trực tiếp từ lời bài hát, kết hợp với phương pháp học đa giác quan — "
        "nghe, đọc, nói, viết — giúp bạn vừa nâng trình tiếng Anh, vừa mang theo thông điệp yêu thương của Michael Jackson trong trái tim mình."
    ),
    "preview": {
        "text": (
            "Bạn đã bao giờ nghe 'Heal the World' và cảm thấy như cả thế giới đang ôm lấy bạn chưa? "
            "Michael Jackson đã viết bài hát này như một lời kêu gọi yêu thương — và bây giờ, bạn sẽ học tiếng Anh qua chính những lời ca ấy. "
            "18 từ vựng được chọn trực tiếp từ lời bài hát: heal, brighter, sorrow, entire, care, space, "
            "bliss, dread, joyful, grace, reveal, existing, spirits, fear, create, nations, plain, heavenly. "
            "Qua 5 buổi học, bạn sẽ đọc từng đoạn lời bài hát, hiểu ý nghĩa từng từ trong ngữ cảnh âm nhạc, "
            "và cuối cùng đọc trọn vẹn toàn bộ lời bài hát như một người thực sự hiểu tiếng Anh. "
            "Hãy để giai điệu của Michael Jackson dẫn lối bạn trên hành trình chinh phục ngôn ngữ."
        )
    },
    "youtubeUrl": YOUTUBE_URL,
    "learningSessions": [],
}


# ===== SESSION 1 =====
session_1 = {
    "title": "Buổi 1: Chữa lành thế giới — Heal the World",
    "activities": [
        # --- introAudio 1: Welcome + song context ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu bài hát",
            "description": "Nghe giới thiệu về bài hát Heal the World và hành trình học từ vựng qua âm nhạc",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn đến với khóa học từ vựng qua âm nhạc! Hôm nay chúng ta sẽ bắt đầu với một trong những bài hát "
                    "đẹp nhất mọi thời đại — 'Heal the World' của Michael Jackson. "
                    "Bài hát này được phát hành năm 1992 trong album Dangerous, và Michael Jackson từng nói đây là bài hát "
                    "ông tự hào nhất khi sáng tác. Giai điệu nhẹ nhàng, lời ca đầy yêu thương — bài hát kêu gọi mỗi người "
                    "hãy làm cho thế giới trở nên tốt đẹp hơn. "
                    "Trong buổi học đầu tiên, bạn sẽ học 6 từ vựng xuất hiện ngay trong phần mở đầu và điệp khúc của bài hát: "
                    "heal, brighter, sorrow, entire, care, và space. "
                    "Những từ này sẽ giúp bạn hiểu được thông điệp cốt lõi mà Michael Jackson muốn truyền tải. "
                    "Hãy sẵn sàng — chúng ta bắt đầu nhé!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- introAudio 2: Vocab teaching ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu từ vựng buổi 1",
            "description": "Học 6 từ vựng từ phần mở đầu và điệp khúc bài hát",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Bây giờ chúng ta sẽ tìm hiểu 6 từ vựng đầu tiên từ bài hát 'Heal the World'. "
                    "Mỗi từ đều xuất hiện trong lời bài hát, và bạn sẽ thấy chúng khi đọc phần lời ca ở phần sau.\n\n"

                    "Từ đầu tiên là 'heal' — động từ, nghĩa là chữa lành, làm lành. "
                    "Trong bài hát, Michael Jackson hát 'Heal the world, make it a better place' — "
                    "Hãy chữa lành thế giới, hãy làm cho nó trở nên tốt đẹp hơn. "
                    "Từ 'heal' không chỉ dùng cho vết thương thể xác mà còn cho tâm hồn, cho mối quan hệ. "
                    "Ví dụ: Time can heal a broken heart — Thời gian có thể chữa lành trái tim tan vỡ.\n\n"

                    "Từ thứ hai là 'brighter' — tính từ so sánh hơn của 'bright', nghĩa là sáng hơn, tươi sáng hơn. "
                    "Michael Jackson hát 'And this place could be much brighter than tomorrow' — "
                    "Nơi này có thể tươi sáng hơn cả ngày mai. "
                    "Ông ấy nói về tình yêu trong trái tim mỗi người — nó có sức mạnh làm sáng cả tương lai. "
                    "Ví dụ: The future looks brighter when we work together — Tương lai tươi sáng hơn khi chúng ta cùng nhau.\n\n"

                    "Từ thứ ba là 'sorrow' — danh từ, nghĩa là nỗi buồn, nỗi đau. "
                    "Trong bài hát: 'In this place you'll feel there's no hurt or sorrow' — "
                    "Ở nơi này bạn sẽ cảm thấy không có đau đớn hay buồn phiền. "
                    "Michael Jackson muốn nói rằng khi có tình yêu, nỗi buồn sẽ tan biến. "
                    "Ví dụ: She felt deep sorrow after losing her grandmother — Cô ấy cảm thấy nỗi buồn sâu sắc sau khi mất bà.\n\n"

                    "Từ thứ tư là 'entire' — tính từ, nghĩa là toàn bộ, trọn vẹn. "
                    "Trong điệp khúc: 'For you and for me and the entire human race' — "
                    "Cho bạn, cho tôi, và cho toàn bộ nhân loại. "
                    "Đây là một từ rất hữu ích trong tiếng Anh hàng ngày. "
                    "Ví dụ: I spent the entire weekend reading — Tôi dành toàn bộ cuối tuần để đọc sách.\n\n"

                    "Từ thứ năm là 'care' — động từ, nghĩa là quan tâm, chăm sóc. "
                    "Michael Jackson hát 'If you care enough for the living' — "
                    "Nếu bạn quan tâm đủ đến những người đang sống. "
                    "Đây là thông điệp trung tâm của bài hát — sự quan tâm có thể thay đổi thế giới. "
                    "Ví dụ: I care about my friends and always try to help them — Tôi quan tâm đến bạn bè và luôn cố gắng giúp đỡ họ.\n\n"

                    "Từ cuối cùng là 'space' — danh từ, nghĩa là không gian, chỗ trống. "
                    "Trong bài hát: 'Make a little space, make a better place' — "
                    "Hãy tạo một chút không gian, hãy tạo một nơi tốt đẹp hơn. "
                    "Ở đây 'space' mang nghĩa bóng — tạo chỗ trong trái tim cho tình yêu thương. "
                    "Ví dụ: We need more space in our lives for the things that matter — Chúng ta cần nhiều không gian hơn cho những điều quan trọng."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Chữa lành & Yêu thương",
            "description": "Học các từ: heal, brighter, sorrow, entire, care, space",
            "practiceMinutes": "6",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- speakFlashcards ---
        {
            "activityType": "speakFlashcards",
            "title": "Flashcards: Tập nói từ vựng buổi 1",
            "description": "Tập nói các từ: heal, brighter, sorrow, entire, care, space",
            "practiceMinutes": "6",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết từ vựng buổi 1",
            "description": "Chọn nghĩa đúng cho các từ: heal, brighter, sorrow, entire, care, space",
            "practiceMinutes": "10",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại từ vựng buổi 1",
            "description": "Điền từ thích hợp vào chỗ trống: heal, brighter, sorrow, entire, care, space",
            "practiceMinutes": "10",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- vocabLevel3 ---
        {
            "activityType": "vocabLevel3",
            "title": "Flashcards: Hiểu sâu từ vựng buổi 1",
            "description": "Vận dụng từ vựng trong ngữ cảnh: heal, brighter, sorrow, entire, care, space",
            "practiceMinutes": "10",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- introAudio 3: Grammar/usage ---
        {
            "activityType": "introAudio",
            "title": "Ngữ pháp và cách dùng từ buổi 1",
            "description": "Nghe giải thích cách dùng từ vựng trong ngữ cảnh bài hát",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Bây giờ chúng ta sẽ xem xét cách các từ vựng buổi 1 được sử dụng trong ngữ pháp tiếng Anh.\n\n"

                    "Từ 'heal' là một động từ thường — 'heal the world' là dạng mệnh lệnh, kêu gọi hành động. "
                    "Bạn có thể dùng 'heal' với nhiều chủ ngữ: 'The wound healed quickly' (vết thương lành nhanh), "
                    "'Music heals the soul' (âm nhạc chữa lành tâm hồn). Lưu ý: 'heal' có thể là nội động từ (tự lành) "
                    "hoặc ngoại động từ (chữa lành cái gì đó).\n\n"

                    "Từ 'brighter' là dạng so sánh hơn của 'bright'. Trong tiếng Anh, tính từ một âm tiết thêm '-er': "
                    "bright → brighter, tall → taller. Michael Jackson dùng 'much brighter' — từ 'much' nhấn mạnh mức độ so sánh. "
                    "Bạn có thể nói 'much bigger', 'much faster' theo cùng cấu trúc.\n\n"

                    "Từ 'sorrow' là danh từ không đếm được, thường đi với 'deep sorrow', 'great sorrow'. "
                    "Trong bài hát, nó đi cặp với 'hurt' — 'no hurt or sorrow' — tạo nhịp điệu đẹp.\n\n"

                    "Từ 'entire' luôn đứng trước danh từ: 'the entire world', 'the entire human race'. "
                    "Nó mạnh hơn 'whole' và thường dùng trong văn viết trang trọng.\n\n"

                    "Từ 'care' khi là động từ thường đi với 'about' hoặc 'for': "
                    "'care about someone' (quan tâm đến ai), 'care for the living' (chăm sóc người sống). "
                    "Trong bài hát, Michael Jackson dùng 'care enough for' — đủ quan tâm cho.\n\n"

                    "Từ 'space' có thể là không gian vật lý (outer space — vũ trụ) hoặc không gian trừu tượng "
                    "(personal space — không gian cá nhân). Trong bài hát, 'make a little space' mang nghĩa bóng — "
                    "tạo chỗ trong trái tim cho sự thay đổi."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading ---
        {
            "activityType": "reading",
            "title": "Đọc: Lời bài hát Heal the World (phần 1)",
            "description": LYRICS_1[:80],
            "practiceMinutes": "5",
            "data": {"text": LYRICS_1, "audioSpeed": -0.1},
        },
        # --- speakReading ---
        {
            "activityType": "speakReading",
            "title": "Đọc: Tập phát âm lời bài hát (phần 1)",
            "description": "Tập phát âm đoạn lời bài hát phần 1",
            "practiceMinutes": "5",
            "data": {"text": LYRICS_1, "audioSpeed": -0.1},
        },
        # --- readAlong ---
        {
            "activityType": "readAlong",
            "title": "Nghe: Heal the World (phần 1)",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": LYRICS_1, "audioSpeed": -0.1},
        },
        # --- writingSentence ---
        {
            "activityType": "writingSentence",
            "title": "Viết: Thực hành từ vựng qua chủ đề yêu thương",
            "description": "Viết câu tiếng Anh sử dụng từ vựng buổi 1: heal, brighter, sorrow, entire, care, space",
            "practiceMinutes": "10",
            "data": {
                "vocabList": W1,
                "audioSpeed": 0.01,
                "items": [
                    {
                        "targetVocab": "heal",
                        "prompt": "Sử dụng từ 'heal' để nói về việc chữa lành — giống như Michael Jackson kêu gọi chữa lành thế giới bằng tình yêu. Ví dụ: Music has the power to heal even the deepest wounds in our hearts.",
                    },
                    {
                        "targetVocab": "brighter",
                        "prompt": "Sử dụng từ 'brighter' để nói về một tương lai tươi sáng hơn — như lời bài hát nói rằng tình yêu có thể làm mọi thứ sáng hơn cả ngày mai. Ví dụ: Every small act of kindness makes the world a little brighter.",
                    },
                    {
                        "targetVocab": "sorrow",
                        "prompt": "Sử dụng từ 'sorrow' để nói về nỗi buồn — như Michael Jackson hát rằng ở nơi có tình yêu, sẽ không còn sorrow. Ví dụ: After the storm passed, the sorrow in the village slowly turned into hope.",
                    },
                    {
                        "targetVocab": "entire",
                        "prompt": "Sử dụng từ 'entire' để nói về sự trọn vẹn — như bài hát nói về toàn bộ nhân loại cùng chung tay. Ví dụ: The entire class worked together to organize a charity event for the community.",
                    },
                    {
                        "targetVocab": "care",
                        "prompt": "Sử dụng từ 'care' để nói về sự quan tâm — như thông điệp cốt lõi của bài hát: nếu bạn quan tâm đủ, bạn có thể thay đổi thế giới. Ví dụ: If we care enough about the environment, we can make a real difference.",
                    },
                    {
                        "targetVocab": "space",
                        "prompt": "Sử dụng từ 'space' để nói về không gian — như bài hát kêu gọi tạo một chút không gian cho sự thay đổi. Ví dụ: Sometimes we need to make space in our busy lives for the people we love.",
                    },
                ],
            },
        },
    ],
}
content["learningSessions"].append(session_1)


# ===== SESSION 2 =====
session_2 = {
    "title": "Buổi 2: Hạnh phúc & Ân sủng — Bliss and Grace",
    "activities": [
        # --- introAudio 1: Welcome + recap ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu buổi 2",
            "description": "Ôn lại buổi 1 và giới thiệu phần tiếp theo của bài hát",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn trở lại với buổi học thứ hai! Ở buổi trước, bạn đã học 6 từ vựng từ phần mở đầu "
                    "bài hát 'Heal the World': heal, brighter, sorrow, entire, care, và space. "
                    "Bạn đã hiểu được thông điệp đầu tiên của Michael Jackson — rằng trong trái tim mỗi người "
                    "đều có một nơi tràn đầy tình yêu, và nếu chúng ta quan tâm đủ, chúng ta có thể chữa lành thế giới.\n\n"
                    "Hôm nay chúng ta sẽ đi sâu hơn vào bài hát — phần mà Michael Jackson nói về tình yêu mạnh mẽ đến mức "
                    "có thể xóa tan nỗi sợ, và về giấc mơ của một thế giới tràn đầy ân sủng. "
                    "6 từ vựng mới của buổi 2 là: bliss, dread, joyful, grace, reveal, và existing. "
                    "Hãy cùng khám phá nhé!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- introAudio 2: Vocab teaching ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu từ vựng buổi 2",
            "description": "Học 6 từ vựng từ phần giữa bài hát về tình yêu và ân sủng",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng tìm hiểu 6 từ vựng mới từ phần giữa bài hát 'Heal the World'.\n\n"

                    "Từ đầu tiên là 'bliss' — danh từ, nghĩa là hạnh phúc tuyệt đối, niềm hoan lạc. "
                    "Michael Jackson hát 'In this bliss, we cannot feel fear or dread' — "
                    "Trong niềm hạnh phúc này, chúng ta không thể cảm thấy sợ hãi hay kinh hoàng. "
                    "Từ 'bliss' diễn tả một trạng thái hạnh phúc hoàn hảo, sâu sắc hơn 'happiness'. "
                    "Ví dụ: Sitting by the ocean at sunset was pure bliss — Ngồi bên biển lúc hoàng hôn là niềm hạnh phúc thuần khiết.\n\n"

                    "Từ thứ hai là 'dread' — danh từ hoặc động từ, nghĩa là nỗi kinh hoàng, sự sợ hãi sâu sắc. "
                    "Trong bài hát: 'we cannot feel fear or dread' — chúng ta không thể cảm thấy sợ hãi hay kinh hoàng. "
                    "Michael Jackson đặt 'dread' cạnh 'fear' để nhấn mạnh rằng tình yêu xóa tan mọi nỗi sợ. "
                    "Ví dụ: She felt a sense of dread before the exam results came out — Cô ấy cảm thấy lo sợ trước khi kết quả thi được công bố.\n\n"

                    "Từ thứ ba là 'joyful' — tính từ, nghĩa là vui vẻ, tràn đầy niềm vui. "
                    "Michael Jackson hát 'Love is strong, it only cares of joyful giving' — "
                    "Tình yêu mạnh mẽ, nó chỉ quan tâm đến việc cho đi trong niềm vui. "
                    "Và ở đoạn sau: 'Will reveal a joyful face' — Sẽ hé lộ một gương mặt tràn đầy niềm vui. "
                    "Ví dụ: The children had joyful expressions on Christmas morning — Bọn trẻ có những biểu cảm vui vẻ vào sáng Giáng sinh.\n\n"

                    "Từ thứ tư là 'grace' — danh từ, nghĩa là ân sủng, sự duyên dáng, vẻ thanh nhã. "
                    "Trong bài hát: 'And the world we once believed in will shine again in grace' — "
                    "Và thế giới mà chúng ta từng tin tưởng sẽ lại tỏa sáng trong ân sủng. "
                    "Từ 'grace' ở đây mang nghĩa vẻ đẹp thanh cao, sự tốt lành. "
                    "Ví dụ: She accepted the award with grace and humility — Cô ấy nhận giải thưởng với sự thanh nhã và khiêm tốn.\n\n"

                    "Từ thứ năm là 'reveal' — động từ, nghĩa là hé lộ, tiết lộ, bày tỏ. "
                    "Michael Jackson hát 'And the dream we were conceived in will reveal a joyful face' — "
                    "Và giấc mơ mà chúng ta được thai nghén trong đó sẽ hé lộ một gương mặt tràn đầy niềm vui. "
                    "Ví dụ: The investigation revealed the truth about what happened — Cuộc điều tra đã tiết lộ sự thật về những gì đã xảy ra.\n\n"

                    "Từ cuối cùng là 'existing' — tính từ hoặc động từ dạng V-ing, nghĩa là tồn tại, hiện có. "
                    "Trong bài hát: 'We stop existing and start living' — "
                    "Chúng ta ngừng chỉ tồn tại và bắt đầu thực sự sống. "
                    "Đây là một câu rất sâu sắc — Michael Jackson phân biệt giữa 'existing' (chỉ tồn tại) và 'living' (thực sự sống). "
                    "Ví dụ: There is a big difference between merely existing and truly living — Có sự khác biệt lớn giữa chỉ tồn tại và thực sự sống."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Hạnh phúc & Ân sủng",
            "description": "Học các từ: bliss, dread, joyful, grace, reveal, existing",
            "practiceMinutes": "6",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- speakFlashcards ---
        {
            "activityType": "speakFlashcards",
            "title": "Flashcards: Tập nói từ vựng buổi 2",
            "description": "Tập nói các từ: bliss, dread, joyful, grace, reveal, existing",
            "practiceMinutes": "6",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết từ vựng buổi 2",
            "description": "Chọn nghĩa đúng cho các từ: bliss, dread, joyful, grace, reveal, existing",
            "practiceMinutes": "10",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại từ vựng buổi 2",
            "description": "Điền từ thích hợp vào chỗ trống: bliss, dread, joyful, grace, reveal, existing",
            "practiceMinutes": "10",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- vocabLevel3 ---
        {
            "activityType": "vocabLevel3",
            "title": "Flashcards: Hiểu sâu từ vựng buổi 2",
            "description": "Vận dụng từ vựng trong ngữ cảnh: bliss, dread, joyful, grace, reveal, existing",
            "practiceMinutes": "10",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- introAudio 3: Grammar/usage ---
        {
            "activityType": "introAudio",
            "title": "Ngữ pháp và cách dùng từ buổi 2",
            "description": "Nghe giải thích cách dùng từ vựng buổi 2 trong ngữ cảnh bài hát",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng xem xét cách sử dụng các từ vựng buổi 2 trong ngữ pháp tiếng Anh.\n\n"

                    "Từ 'bliss' là danh từ không đếm được — bạn không nói 'a bliss' hay 'blisses'. "
                    "Nó thường đi với 'pure bliss', 'sheer bliss', 'marital bliss'. "
                    "Trong bài hát, 'in this bliss' dùng 'this' để chỉ trạng thái hạnh phúc cụ thể mà tình yêu mang lại.\n\n"

                    "Từ 'dread' vừa là danh từ vừa là động từ. Là danh từ: 'a sense of dread' (cảm giác kinh hoàng). "
                    "Là động từ: 'I dread Monday mornings' (Tôi sợ sáng thứ Hai). "
                    "Trong bài hát, nó được dùng như danh từ, đi cặp với 'fear' tạo hiệu ứng nhấn mạnh.\n\n"

                    "Từ 'joyful' là tính từ, được tạo từ 'joy' + hậu tố '-ful'. "
                    "Cấu trúc này rất phổ biến: hope → hopeful, care → careful, beauty → beautiful. "
                    "Michael Jackson dùng 'joyful giving' — sự cho đi trong niềm vui — và 'joyful face' — gương mặt vui vẻ.\n\n"

                    "Từ 'grace' có nhiều nghĩa: ân sủng (tôn giáo), sự duyên dáng (cử chỉ), thời gian gia hạn (grace period). "
                    "Trong bài hát, 'shine again in grace' mang nghĩa tỏa sáng trong vẻ đẹp thanh cao.\n\n"

                    "Từ 'reveal' là ngoại động từ — luôn cần tân ngữ: 'reveal the truth', 'reveal a secret'. "
                    "Trong bài hát: 'will reveal a joyful face' — sẽ hé lộ một gương mặt vui vẻ. "
                    "Lưu ý: không nhầm với 'revel' (vui chơi) — hai từ phát âm khác nhau.\n\n"

                    "Từ 'existing' trong bài hát được dùng như động từ dạng V-ing: 'We stop existing and start living'. "
                    "Cấu trúc 'stop + V-ing' nghĩa là ngừng làm gì đó. "
                    "Đây là một trong những cấu trúc quan trọng nhất trong tiếng Anh — "
                    "phân biệt 'stop to do' (dừng lại để làm) và 'stop doing' (ngừng làm)."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading ---
        {
            "activityType": "reading",
            "title": "Đọc: Lời bài hát Heal the World (phần 2)",
            "description": LYRICS_2[:80],
            "practiceMinutes": "5",
            "data": {"text": LYRICS_2, "audioSpeed": -0.1},
        },
        # --- speakReading ---
        {
            "activityType": "speakReading",
            "title": "Đọc: Tập phát âm lời bài hát (phần 2)",
            "description": "Tập phát âm đoạn lời bài hát phần 2",
            "practiceMinutes": "5",
            "data": {"text": LYRICS_2, "audioSpeed": -0.1},
        },
        # --- readAlong ---
        {
            "activityType": "readAlong",
            "title": "Nghe: Heal the World (phần 2)",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": LYRICS_2, "audioSpeed": -0.1},
        },
        # --- writingSentence ---
        {
            "activityType": "writingSentence",
            "title": "Viết: Thực hành từ vựng qua chủ đề ân sủng và hy vọng",
            "description": "Viết câu tiếng Anh sử dụng từ vựng buổi 2: bliss, dread, joyful, grace, reveal, existing",
            "practiceMinutes": "10",
            "data": {
                "vocabList": W2,
                "audioSpeed": 0.01,
                "items": [
                    {
                        "targetVocab": "bliss",
                        "prompt": "Sử dụng từ 'bliss' để nói về khoảnh khắc hạnh phúc tuyệt đối — như Michael Jackson mô tả trạng thái khi tình yêu xóa tan mọi nỗi sợ. Ví dụ: Listening to my favorite song on a rainy afternoon is pure bliss.",
                    },
                    {
                        "targetVocab": "dread",
                        "prompt": "Sử dụng từ 'dread' để nói về nỗi sợ hãi sâu sắc — như bài hát nói rằng trong hạnh phúc, chúng ta không còn cảm thấy dread. Ví dụ: Many students feel a sense of dread before important exams.",
                    },
                    {
                        "targetVocab": "joyful",
                        "prompt": "Sử dụng từ 'joyful' để nói về niềm vui — như Michael Jackson hát về sự cho đi trong niềm vui và gương mặt tràn đầy hạnh phúc. Ví dụ: The wedding was a joyful celebration that brought the whole family together.",
                    },
                    {
                        "targetVocab": "grace",
                        "prompt": "Sử dụng từ 'grace' để nói về sự thanh nhã hoặc ân sủng — như bài hát nói thế giới sẽ lại tỏa sáng trong grace. Ví dụ: The dancer moved across the stage with incredible grace.",
                    },
                    {
                        "targetVocab": "reveal",
                        "prompt": "Sử dụng từ 'reveal' để nói về việc hé lộ điều gì đó — như bài hát nói giấc mơ sẽ reveal một gương mặt tràn đầy niềm vui. Ví dụ: The sunrise revealed a beautiful landscape hidden by the morning fog.",
                    },
                    {
                        "targetVocab": "existing",
                        "prompt": "Sử dụng từ 'existing' để nói về sự tồn tại — như Michael Jackson phân biệt giữa chỉ existing và thực sự sống. Ví dụ: She realized she had been merely existing, not truly living, and decided to make a change.",
                    },
                ],
            },
        },
    ],
}
content["learningSessions"].append(session_2)


# ===== SESSION 3 =====
session_3 = {
    "title": "Buổi 3: Tinh thần & Hòa bình — Spirits and Peace",
    "activities": [
        # --- introAudio 1: Welcome + recap ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu buổi 3",
            "description": "Ôn lại buổi 1-2 và giới thiệu phần cuối bài hát",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn đến với buổi học thứ ba — buổi học cuối cùng trước khi chúng ta ôn tập! "
                    "Bạn đã đi được một chặng đường dài rồi đấy. Ở buổi 1, bạn học về sự chữa lành và yêu thương "
                    "với heal, brighter, sorrow, entire, care, space. Ở buổi 2, bạn khám phá hạnh phúc và ân sủng "
                    "với bliss, dread, joyful, grace, reveal, existing.\n\n"
                    "Hôm nay chúng ta sẽ đến với phần hùng tráng nhất của bài hát — nơi Michael Jackson kêu gọi "
                    "nhân loại bay cao, giữ cho tinh thần không bao giờ tắt, và tạo ra một thế giới không còn sợ hãi. "
                    "Đây là phần mà các quốc gia biến gươm thành lưỡi cày — một hình ảnh đầy sức mạnh về hòa bình. "
                    "6 từ vựng mới: spirits, fear, create, nations, plain, heavenly. Hãy bắt đầu nào!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- introAudio 2: Vocab teaching ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu từ vựng buổi 3",
            "description": "Học 6 từ vựng từ phần cuối bài hát về tinh thần và hòa bình",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng tìm hiểu 6 từ vựng cuối cùng từ bài hát 'Heal the World'.\n\n"

                    "Từ đầu tiên là 'spirits' — danh từ số nhiều, nghĩa là tinh thần, tâm hồn. "
                    "Michael Jackson hát 'Let our spirits never die' — Hãy để tinh thần chúng ta không bao giờ chết. "
                    "Đây là lời kêu gọi giữ vững niềm tin và hy vọng, dù hoàn cảnh có khó khăn đến đâu. "
                    "Ví dụ: The team's spirits were high after winning the championship — Tinh thần đội rất cao sau khi vô địch.\n\n"

                    "Từ thứ hai là 'fear' — danh từ hoặc động từ, nghĩa là nỗi sợ, sự sợ hãi. "
                    "Trong bài hát: 'Create a world with no fear' — Tạo ra một thế giới không có sợ hãi. "
                    "Michael Jackson mơ về một thế giới nơi con người sống mà không phải lo sợ. "
                    "Ví dụ: She overcame her fear of public speaking by practicing every day — Cô ấy vượt qua nỗi sợ nói trước đám đông bằng cách luyện tập mỗi ngày.\n\n"

                    "Từ thứ ba là 'create' — động từ, nghĩa là tạo ra, sáng tạo. "
                    "Michael Jackson hát 'Create a world with no fear' — Hãy tạo ra một thế giới không có sợ hãi. "
                    "Từ 'create' mang sức mạnh của hành động — không chỉ mơ ước mà còn xây dựng. "
                    "Ví dụ: Artists create beauty from ordinary materials — Nghệ sĩ tạo ra vẻ đẹp từ những vật liệu bình thường.\n\n"

                    "Từ thứ tư là 'nations' — danh từ số nhiều, nghĩa là các quốc gia, các dân tộc. "
                    "Trong bài hát: 'See the nations turn their swords into plowshares' — "
                    "Hãy nhìn các quốc gia biến gươm thành lưỡi cày. "
                    "Đây là hình ảnh kinh điển về hòa bình — khi chiến tranh kết thúc và con người quay về cuộc sống bình yên. "
                    "Ví dụ: Many nations came together to sign the peace agreement — Nhiều quốc gia cùng nhau ký hiệp định hòa bình.\n\n"

                    "Từ thứ năm là 'plain' — tính từ, nghĩa là rõ ràng, hiển nhiên, đơn giản. "
                    "Michael Jackson hát 'Though it's plain to see, this world is heavenly' — "
                    "Dù rõ ràng là thế giới này thật thiên đường. "
                    "Từ 'plain' ở đây nghĩa là dễ thấy, hiển nhiên — 'plain to see' là cụm từ rất phổ biến. "
                    "Ví dụ: It was plain to see that she was happy with the results — Rõ ràng là cô ấy hài lòng với kết quả.\n\n"

                    "Từ cuối cùng là 'heavenly' — tính từ, nghĩa là thuộc về thiên đường, tuyệt vời. "
                    "Trong bài hát: 'This world is heavenly be God's glow' — "
                    "Thế giới này thật thiên đường nhờ ánh sáng của Chúa. "
                    "Trong đời thường, 'heavenly' cũng dùng để khen ngợi: 'heavenly food' (đồ ăn tuyệt vời). "
                    "Ví dụ: The view from the mountain top was absolutely heavenly — Quang cảnh từ đỉnh núi thật sự tuyệt vời."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Tinh thần & Hòa bình",
            "description": "Học các từ: spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "6",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- speakFlashcards ---
        {
            "activityType": "speakFlashcards",
            "title": "Flashcards: Tập nói từ vựng buổi 3",
            "description": "Tập nói các từ: spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "6",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết từ vựng buổi 3",
            "description": "Chọn nghĩa đúng cho các từ: spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "10",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại từ vựng buổi 3",
            "description": "Điền từ thích hợp vào chỗ trống: spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "10",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- vocabLevel3 ---
        {
            "activityType": "vocabLevel3",
            "title": "Flashcards: Hiểu sâu từ vựng buổi 3",
            "description": "Vận dụng từ vựng trong ngữ cảnh: spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "10",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- introAudio 3: Grammar/usage ---
        {
            "activityType": "introAudio",
            "title": "Ngữ pháp và cách dùng từ buổi 3",
            "description": "Nghe giải thích cách dùng từ vựng buổi 3 trong ngữ cảnh bài hát",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng xem xét cách sử dụng các từ vựng buổi 3 trong ngữ pháp tiếng Anh.\n\n"

                    "Từ 'spirits' ở đây là danh từ số nhiều, chỉ tinh thần của nhiều người. "
                    "Khi nói về một người: 'Her spirit is strong' (tinh thần cô ấy mạnh mẽ). "
                    "Khi nói về nhóm: 'Our spirits are high' (tinh thần chúng tôi cao). "
                    "Lưu ý: 'spirits' cũng có nghĩa là đồ uống có cồn — 'wine and spirits'.\n\n"

                    "Từ 'fear' vừa là danh từ vừa là động từ. Là danh từ: 'a fear of heights' (sợ độ cao). "
                    "Là động từ: 'I fear the worst' (Tôi sợ điều tồi tệ nhất). "
                    "Trong bài hát, 'no fear' dùng như danh từ — 'a world with no fear' — thế giới không có sợ hãi.\n\n"

                    "Từ 'create' là động từ thường, theo sau bởi tân ngữ: 'create a world', 'create art', 'create opportunities'. "
                    "Danh từ tương ứng là 'creation' (sự sáng tạo) và tính từ là 'creative' (sáng tạo). "
                    "Michael Jackson dùng mệnh lệnh: 'Create a world with no fear' — Hãy tạo ra một thế giới.\n\n"

                    "Từ 'nations' là danh từ đếm được số nhiều. 'Nation' khác 'country' ở chỗ 'nation' nhấn mạnh "
                    "con người và văn hóa, còn 'country' nhấn mạnh lãnh thổ. "
                    "'The United Nations' (Liên Hợp Quốc) dùng 'nations' vì nói về các dân tộc hợp tác.\n\n"

                    "Từ 'plain' có nhiều nghĩa: rõ ràng (plain to see), đơn giản (plain food), đồng bằng (the Great Plains). "
                    "Trong bài hát, 'it's plain to see' là thành ngữ nghĩa là 'rõ ràng là'. "
                    "Cấu trúc tương tự: 'it's easy to see', 'it's hard to believe'.\n\n"

                    "Từ 'heavenly' là tính từ, tạo từ 'heaven' + '-ly'. "
                    "Cấu trúc tương tự: friend → friendly, love → lovely, earth → earthly. "
                    "Trong bài hát, 'this world is heavenly' nghĩa là thế giới này đẹp như thiên đường."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading ---
        {
            "activityType": "reading",
            "title": "Đọc: Lời bài hát Heal the World (phần 3)",
            "description": LYRICS_3[:80],
            "practiceMinutes": "5",
            "data": {"text": LYRICS_3, "audioSpeed": -0.1},
        },
        # --- speakReading ---
        {
            "activityType": "speakReading",
            "title": "Đọc: Tập phát âm lời bài hát (phần 3)",
            "description": "Tập phát âm đoạn lời bài hát phần 3",
            "practiceMinutes": "5",
            "data": {"text": LYRICS_3, "audioSpeed": -0.1},
        },
        # --- readAlong ---
        {
            "activityType": "readAlong",
            "title": "Nghe: Heal the World (phần 3)",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": LYRICS_3, "audioSpeed": -0.1},
        },
        # --- writingSentence ---
        {
            "activityType": "writingSentence",
            "title": "Viết: Thực hành từ vựng qua chủ đề hòa bình và hy vọng",
            "description": "Viết câu tiếng Anh sử dụng từ vựng buổi 3: spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "10",
            "data": {
                "vocabList": W3,
                "audioSpeed": 0.01,
                "items": [
                    {
                        "targetVocab": "spirits",
                        "prompt": "Sử dụng từ 'spirits' để nói về tinh thần — như Michael Jackson kêu gọi giữ cho tinh thần không bao giờ tắt. Ví dụ: Despite the difficulties, the volunteers kept their spirits high throughout the project.",
                    },
                    {
                        "targetVocab": "fear",
                        "prompt": "Sử dụng từ 'fear' để nói về nỗi sợ — như bài hát mơ về một thế giới không còn fear. Ví dụ: The greatest fear we face is often the fear of the unknown.",
                    },
                    {
                        "targetVocab": "create",
                        "prompt": "Sử dụng từ 'create' để nói về việc tạo ra điều gì đó mới — như Michael Jackson kêu gọi tạo ra một thế giới tốt đẹp hơn. Ví dụ: Together, we can create a community where everyone feels welcome and valued.",
                    },
                    {
                        "targetVocab": "nations",
                        "prompt": "Sử dụng từ 'nations' để nói về các quốc gia — như bài hát nói về các nations biến gươm thành lưỡi cày. Ví dụ: When nations work together on climate change, the results are much more powerful.",
                    },
                    {
                        "targetVocab": "plain",
                        "prompt": "Sử dụng từ 'plain' để nói về sự rõ ràng — như bài hát nói 'it's plain to see' rằng thế giới này thật đẹp. Ví dụ: It was plain to see that the new policy had a positive effect on the students.",
                    },
                    {
                        "targetVocab": "heavenly",
                        "prompt": "Sử dụng từ 'heavenly' để nói về điều gì đó tuyệt vời — như Michael Jackson mô tả thế giới này đẹp như thiên đường. Ví dụ: The smell of fresh bread from the bakery was absolutely heavenly.",
                    },
                ],
            },
        },
    ],
}
content["learningSessions"].append(session_3)


# ===== SESSION 4 (Review) =====
session_4 = {
    "title": "Ôn tập",
    "activities": [
        # --- introAudio: Congratulations + recap ---
        {
            "activityType": "introAudio",
            "title": "Chúc mừng và ôn tập",
            "description": "Nghe lời chúc mừng và ôn lại toàn bộ 18 từ vựng từ bài hát",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chúc mừng bạn! Bạn đã hoàn thành 3 buổi học và nắm vững 18 từ vựng từ bài hát 'Heal the World' "
                    "của Michael Jackson. Đây là một thành tựu đáng tự hào!\n\n"
                    "Hãy cùng nhìn lại hành trình của bạn. Ở buổi 1, bạn bắt đầu với phần mở đầu bài hát — "
                    "nơi Michael Jackson nói về nơi chốn tình yêu trong trái tim và kêu gọi chữa lành thế giới. "
                    "Bạn đã học heal, brighter, sorrow, entire, care, và space.\n\n"
                    "Ở buổi 2, bạn đi sâu vào phần giữa bài hát — nơi tình yêu mạnh mẽ đến mức xóa tan mọi nỗi sợ, "
                    "và giấc mơ về một thế giới tràn đầy ân sủng. Bạn đã học bliss, dread, joyful, grace, reveal, và existing.\n\n"
                    "Ở buổi 3, bạn đến với phần hùng tráng nhất — lời kêu gọi các quốc gia hòa bình, "
                    "tinh thần không bao giờ tắt, và một thế giới đẹp như thiên đường. "
                    "Bạn đã học spirits, fear, create, nations, plain, và heavenly.\n\n"
                    "Bây giờ là lúc ôn tập tất cả 18 từ. Hãy tập trung và cho thấy bạn đã nhớ được bao nhiêu nhé!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards (ALL 18 words) ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Ôn tập toàn bộ 18 từ vựng",
            "description": "Ôn lại tất cả 18 từ: heal, brighter, sorrow, entire, care, space, bliss, dread, joyful, grace, reveal, existing, spirits, fear, create, nations, plain, heavenly",
            "practiceMinutes": "6",
            "data": {"vocabList": ALL, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 (ALL 18 words) ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết toàn bộ từ vựng",
            "description": "Chọn nghĩa đúng cho tất cả 18 từ vựng từ bài hát Heal the World",
            "practiceMinutes": "10",
            "data": {"vocabList": ALL, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 (ALL 18 words) ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại toàn bộ từ vựng",
            "description": "Điền từ thích hợp vào chỗ trống cho tất cả 18 từ vựng từ bài hát Heal the World",
            "practiceMinutes": "10",
            "data": {"vocabList": ALL, "audioSpeed": -0.1},
        },
    ],
}
content["learningSessions"].append(session_4)


# ===== SESSION 5 (Full reading + farewell) =====
session_5 = {
    "title": "Đọc toàn bộ lời bài hát",
    "activities": [
        # --- introAudio 1: Intro to full reading ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu buổi đọc trọn vẹn",
            "description": "Nghe giới thiệu trước khi đọc toàn bộ lời bài hát Heal the World",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn đến với buổi học cuối cùng! Đây là khoảnh khắc bạn đã chờ đợi — "
                    "bạn sẽ đọc toàn bộ lời bài hát 'Heal the World' từ đầu đến cuối. "
                    "Với 18 từ vựng đã học, bạn sẽ hiểu bài hát ở một tầm hoàn toàn mới. "
                    "Hãy đọc chậm, cảm nhận từng câu, và để giai điệu của Michael Jackson vang lên trong tâm trí bạn. "
                    "Sau khi đọc xong, chúng ta sẽ cùng ôn lại tất cả từ vựng một lần cuối. Hãy bắt đầu nhé!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading (FULL LYRICS) ---
        {
            "activityType": "reading",
            "title": "Đọc: Toàn bộ lời bài hát Heal the World",
            "description": FULL_LYRICS[:80],
            "practiceMinutes": "5",
            "data": {"text": FULL_LYRICS, "audioSpeed": -0.1},
        },
        # --- speakReading (FULL LYRICS) ---
        {
            "activityType": "speakReading",
            "title": "Đọc: Tập phát âm toàn bộ lời bài hát",
            "description": "Tập phát âm toàn bộ lời bài hát Heal the World",
            "practiceMinutes": "5",
            "data": {"text": FULL_LYRICS, "audioSpeed": -0.1},
        },
        # --- readAlong (FULL LYRICS) ---
        {
            "activityType": "readAlong",
            "title": "Nghe: Toàn bộ bài hát Heal the World",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": FULL_LYRICS, "audioSpeed": -0.1},
        },
        # --- introAudio 2: Farewell with all 18 words ---
        {
            "activityType": "introAudio",
            "title": "Lời chia tay và ôn tập từ vựng",
            "description": "Ôn lại toàn bộ 18 từ vựng với ví dụ mới và lời chia tay ấm áp",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Bạn đã hoàn thành toàn bộ khóa học 'Heal the World'! Hãy cùng ôn lại 18 từ vựng "
                    "một lần cuối với những ví dụ mới, để chúng thực sự trở thành một phần vốn từ của bạn.\n\n"

                    "Từ 'heal' — chữa lành. Kindness has the power to heal wounds that medicine cannot touch. "
                    "Sự tử tế có sức mạnh chữa lành những vết thương mà thuốc men không thể chạm tới.\n\n"

                    "Từ 'brighter' — tươi sáng hơn. After the rain, the sky always looks brighter and more beautiful. "
                    "Sau cơn mưa, bầu trời luôn trông tươi sáng hơn và đẹp hơn.\n\n"

                    "Từ 'sorrow' — nỗi buồn. Even in times of great sorrow, we can find strength in the people around us. "
                    "Ngay cả trong những lúc buồn nhất, chúng ta có thể tìm thấy sức mạnh từ những người xung quanh.\n\n"

                    "Từ 'entire' — toàn bộ. The entire neighborhood came together to help the family rebuild their home. "
                    "Toàn bộ khu phố cùng nhau giúp gia đình xây lại ngôi nhà.\n\n"

                    "Từ 'care' — quan tâm. When you truly care about someone, you show it through your actions, not just words. "
                    "Khi bạn thực sự quan tâm đến ai đó, bạn thể hiện qua hành động, không chỉ lời nói.\n\n"

                    "Từ 'space' — không gian. Everyone needs a quiet space where they can think and recharge. "
                    "Mọi người đều cần một không gian yên tĩnh để suy nghĩ và nạp lại năng lượng.\n\n"

                    "Từ 'bliss' — hạnh phúc tuyệt đối. Waking up on a holiday morning with no plans is absolute bliss. "
                    "Thức dậy vào sáng ngày nghỉ mà không có kế hoạch gì là hạnh phúc tuyệt đối.\n\n"

                    "Từ 'dread' — nỗi kinh hoàng. He felt a growing sense of dread as the deadline approached. "
                    "Anh ấy cảm thấy nỗi lo sợ ngày càng tăng khi hạn chót đến gần.\n\n"

                    "Từ 'joyful' — vui vẻ. The park was filled with joyful laughter from children playing in the sunshine. "
                    "Công viên tràn ngập tiếng cười vui vẻ của trẻ em chơi đùa dưới nắng.\n\n"

                    "Từ 'grace' — ân sủng, thanh nhã. She handled the difficult situation with remarkable grace and patience. "
                    "Cô ấy xử lý tình huống khó khăn với sự thanh nhã và kiên nhẫn đáng ngưỡng mộ.\n\n"

                    "Từ 'reveal' — hé lộ. The documentary revealed surprising facts about ocean pollution. "
                    "Bộ phim tài liệu hé lộ những sự thật đáng ngạc nhiên về ô nhiễm đại dương.\n\n"

                    "Từ 'existing' — tồn tại. Many people go through life merely existing without pursuing their dreams. "
                    "Nhiều người sống cuộc đời chỉ tồn tại mà không theo đuổi ước mơ.\n\n"

                    "Từ 'spirits' — tinh thần. Good friends have a way of lifting your spirits when you feel down. "
                    "Bạn tốt có cách nâng cao tinh thần bạn khi bạn cảm thấy buồn.\n\n"

                    "Từ 'fear' — nỗi sợ. The only way to conquer fear is to face it directly. "
                    "Cách duy nhất để chinh phục nỗi sợ là đối mặt trực tiếp với nó.\n\n"

                    "Từ 'create' — tạo ra. Every day is an opportunity to create something meaningful. "
                    "Mỗi ngày là cơ hội để tạo ra điều gì đó có ý nghĩa.\n\n"

                    "Từ 'nations' — các quốc gia. When nations cooperate on education, children everywhere benefit. "
                    "Khi các quốc gia hợp tác về giáo dục, trẻ em ở khắp nơi đều được hưởng lợi.\n\n"

                    "Từ 'plain' — rõ ràng. It is plain to see that learning through music makes vocabulary stick better. "
                    "Rõ ràng là học qua âm nhạc giúp từ vựng ghi nhớ tốt hơn.\n\n"

                    "Từ 'heavenly' — tuyệt vời, thiên đường. The feeling of understanding every word of a beautiful song is truly heavenly. "
                    "Cảm giác hiểu được từng từ của một bài hát đẹp thật sự tuyệt vời.\n\n"

                    "Bạn đã đi một hành trình tuyệt vời cùng Michael Jackson và bài hát 'Heal the World'. "
                    "Từ nay, mỗi khi nghe bài hát này, bạn sẽ hiểu từng lời ca, cảm nhận từng thông điệp. "
                    "Hãy nhớ rằng âm nhạc là cầu nối tuyệt vời nhất giữa ngôn ngữ và trái tim. "
                    "Cảm ơn bạn đã đồng hành — và hãy tiếp tục heal the world theo cách riêng của bạn! "
                    "Chúc bạn luôn vui vẻ trên hành trình học tiếng Anh. Tạm biệt và hẹn gặp lại!"
                ),
                "audioSpeed": 0.01,
            },
        },
    ],
}
content["learningSessions"].append(session_5)


# ---------------------------------------------------------------------------
# Validate
# ---------------------------------------------------------------------------
def validate(content):
    errors = []

    # Property 1: 18 unique vocab words across W1 + W2 + W3
    all_words = W1 + W2 + W3
    if len(all_words) != 18:
        errors.append(f"Expected 18 vocab words, got {len(all_words)}")
    if len(set(all_words)) != 18:
        errors.append(f"Vocab words not unique: {len(set(all_words))} unique out of {len(all_words)}")

    # Property 2: 5 sessions with correct activity type sequences
    sessions = content["learningSessions"]
    if len(sessions) != 5:
        errors.append(f"Expected 5 sessions, got {len(sessions)}")

    expected_sequences = {
        0: ["introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
            "vocabLevel1", "vocabLevel2", "vocabLevel3", "introAudio",
            "reading", "speakReading", "readAlong", "writingSentence"],
        1: ["introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
            "vocabLevel1", "vocabLevel2", "vocabLevel3", "introAudio",
            "reading", "speakReading", "readAlong", "writingSentence"],
        2: ["introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
            "vocabLevel1", "vocabLevel2", "vocabLevel3", "introAudio",
            "reading", "speakReading", "readAlong", "writingSentence"],
        3: ["introAudio", "viewFlashcards", "vocabLevel1", "vocabLevel2"],
        4: ["introAudio", "reading", "speakReading", "readAlong", "introAudio"],
    }
    for idx, expected in expected_sequences.items():
        if idx < len(sessions):
            actual = [a["activityType"] for a in sessions[idx]["activities"]]
            if actual != expected:
                errors.append(f"Session {idx+1} activity sequence mismatch: expected {expected}, got {actual}")

    # Property 3: All activities have title and description (non-empty strings)
    for si, session in enumerate(sessions):
        if not session.get("title") or not isinstance(session["title"], str):
            errors.append(f"Session {si+1} missing or empty title")
        for ai, activity in enumerate(session["activities"]):
            if not activity.get("title") or not isinstance(activity["title"], str):
                errors.append(f"Session {si+1} activity {ai} missing or empty title")
            if not activity.get("description") or not isinstance(activity["description"], str):
                errors.append(f"Session {si+1} activity {ai} missing or empty description")

    # Property 4: No strip keys present in content (recursive check)
    def check_strip_keys(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in STRIP_KEYS:
                    errors.append(f"Strip key '{k}' found at {path}.{k}")
                check_strip_keys(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                check_strip_keys(item, f"{path}[{i}]")
    check_strip_keys(content)

    # Property 5: youtubeUrl exists at top level and matches YouTube URL pattern
    yt = content.get("youtubeUrl", "")
    if not yt:
        errors.append("Missing youtubeUrl at top level")
    elif not (yt.startswith("https://www.youtube.com/watch?v=") or yt.startswith("https://youtu.be/")):
        errors.append(f"youtubeUrl does not match YouTube pattern: {yt}")

    # Property 6: All 18 vocab words appear in FULL_LYRICS (case-insensitive)
    lyrics_lower = FULL_LYRICS.lower()
    for word in all_words:
        if word.lower() not in lyrics_lower:
            errors.append(f"Vocab word '{word}' not found in FULL_LYRICS")

    # Property 7: Session 1-3 reading texts are substrings of FULL_LYRICS
    full_normalized = " ".join(FULL_LYRICS.split())
    for si in range(3):
        if si < len(sessions):
            for activity in sessions[si]["activities"]:
                if activity["activityType"] == "reading":
                    reading_text = activity["data"]["text"]
                    reading_normalized = " ".join(reading_text.split())
                    if reading_normalized not in full_normalized:
                        errors.append(f"Session {si+1} reading text is not a substring of FULL_LYRICS")

    # Property 8: writingSentence items have targetVocab and prompt with "Ví dụ:" marker
    for si, session in enumerate(sessions):
        for activity in session["activities"]:
            if activity["activityType"] == "writingSentence":
                for ii, item in enumerate(activity["data"].get("items", [])):
                    if not item.get("targetVocab"):
                        errors.append(f"Session {si+1} writingSentence item {ii} missing targetVocab")
                    if "Ví dụ:" not in item.get("prompt", ""):
                        errors.append(f"Session {si+1} writingSentence item {ii} missing 'Ví dụ:' in prompt")

    # Property 9: vocabList in flashcard activities matches the correct word group
    word_groups = {0: W1, 1: W2, 2: W3}
    flashcard_types = {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"}
    for si in range(3):
        if si < len(sessions):
            for activity in sessions[si]["activities"]:
                if activity["activityType"] in flashcard_types:
                    vl = activity["data"].get("vocabList", [])
                    if vl != word_groups[si]:
                        errors.append(f"Session {si+1} {activity['activityType']} vocabList mismatch: expected {word_groups[si]}, got {vl}")
    # Session 4: ALL words
    if len(sessions) > 3:
        for activity in sessions[3]["activities"]:
            if activity["activityType"] in flashcard_types:
                vl = activity["data"].get("vocabList", [])
                if vl != ALL:
                    errors.append(f"Session 4 {activity['activityType']} vocabList should be ALL 18 words")

    # Property 10: Curriculum title contains song title and artist name
    title = content.get("title", "")
    if SONG_TITLE not in title:
        errors.append(f"Curriculum title does not contain song title '{SONG_TITLE}'")
    if ARTIST not in title:
        errors.append(f"Curriculum title does not contain artist name '{ARTIST}'")

    # Property 11: Farewell introAudio (session 5, last activity) contains all 18 vocab words
    if len(sessions) >= 5:
        farewell = sessions[4]["activities"][-1]
        if farewell["activityType"] == "introAudio":
            farewell_text = farewell["data"]["text"].lower()
            for word in all_words:
                if word.lower() not in farewell_text:
                    errors.append(f"Farewell introAudio missing vocab word '{word}'")
        else:
            errors.append("Last activity in session 5 is not introAudio")

    # Property 12: Activity title format matches activity type
    for si, session in enumerate(sessions):
        for ai, activity in enumerate(session["activities"]):
            atype = activity["activityType"]
            atitle = activity.get("title", "")
            if atype in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"):
                if not atitle.startswith("Flashcards:"):
                    errors.append(f"Session {si+1} activity {ai} ({atype}) title should start with 'Flashcards:': '{atitle}'")
            elif atype in ("reading", "speakReading"):
                if "Đọc:" not in atitle:
                    errors.append(f"Session {si+1} activity {ai} ({atype}) title should contain 'Đọc:': '{atitle}'")
            elif atype == "readAlong":
                if "Nghe:" not in atitle:
                    errors.append(f"Session {si+1} activity {ai} ({atype}) title should contain 'Nghe:': '{atitle}'")
            elif atype == "writingSentence":
                if "Viết:" not in atitle:
                    errors.append(f"Session {si+1} activity {ai} ({atype}) title should contain 'Viết:': '{atitle}'")

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("Validation passed — all 12 properties OK")


# ---------------------------------------------------------------------------
# Strip and validate
# ---------------------------------------------------------------------------
content = strip_keys(content)
validate(content)

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
token = get_firebase_id_token(UID)
r = requests.post(
    f"{API}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
r.raise_for_status()
print("Created curriculum:", r.json()["id"])
