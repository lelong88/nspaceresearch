#!/usr/bin/env python3
"""
Song 2 Curriculum: "Imagine" by John Lennon
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
SONG_TITLE = "Imagine"
ARTIST = "John Lennon"
YOUTUBE_URL = "https://www.youtube.com/watch?v=YkgkThdzX-8"

# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------
W1 = ["imagine", "heaven", "above", "below", "wonder", "dreamer"]
W2 = ["countries", "religion", "peace", "possessions", "greed", "hunger"]
W3 = ["brotherhood", "sharing", "join", "hope", "someday", "living"]
ALL = W1 + W2 + W3

# ---------------------------------------------------------------------------
# Lyrics
# ---------------------------------------------------------------------------
LYRICS_1 = """\
Imagine there's no heaven
It's easy if you try
No hell below us
Above us, only sky
Imagine all the people
Living for today

I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people
Sharing all the world

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will live as one"""

LYRICS_2 = """\
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people
Living life in peace

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will be as one"""

LYRICS_3 = """\
Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people
Sharing all the world

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will live as one"""

FULL_LYRICS = """\
Imagine there's no heaven
It's easy if you try
No hell below us
Above us, only sky
Imagine all the people
Living for today

Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people
Living life in peace

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will be as one

Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people
Sharing all the world

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will live as one"""


# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------
content = {
    "title": "Học Qua Bài Hát: 'Imagine' – John Lennon",
    "description": (
        "BẠN CÓ TỪNG NGHE MỘT BÀI HÁT MÀ CẢ THẾ GIỚI CÙNG HÁT THEO?\n\n"
        "Có những giai điệu vượt qua mọi biên giới, mọi ngôn ngữ, mọi thời đại. "
        "'Imagine' của John Lennon là bài hát như thế — một bản piano đơn giản mà lay động hàng tỷ trái tim "
        "suốt hơn 50 năm qua. Từ quảng trường Times Square đến một quán cà phê nhỏ ở Sài Gòn, "
        "ai cũng từng nghe giai điệu này ít nhất một lần trong đời.\n\n"
        "Nhưng bạn đã bao giờ thực sự HIỂU từng lời John Lennon hát chưa? "
        "Khi ông ấy nói 'Imagine no possessions' — bạn có biết 'possessions' là gì không? "
        "Khi ông ấy mơ về 'a brotherhood of man' — từ 'brotherhood' mang sức nặng nào? "
        "Mỗi từ trong bài hát này là một viên gạch xây nên giấc mơ hòa bình — "
        "và khi bạn hiểu từng viên gạch, bạn sẽ nghe bài hát bằng trái tim, không chỉ bằng tai.\n\n"
        "Đây không chỉ là học từ vựng — đây là hành trình đi vào tâm hồn của một trong những nghệ sĩ vĩ đại nhất lịch sử. "
        "John Lennon đã dùng những từ đơn giản nhất để nói về những ước mơ lớn nhất. "
        "Và bạn sẽ học cách làm điều tương tự.\n\n"
        "18 từ vựng được chọn trực tiếp từ lời bài hát, kết hợp phương pháp đa giác quan — "
        "nghe, đọc, nói, viết — giúp bạn vừa nâng trình tiếng Anh, "
        "vừa mang theo giấc mơ hòa bình của John Lennon trong mỗi câu nói."
    ),
    "preview": {
        "text": (
            "Hãy nhắm mắt lại và tưởng tượng — một thế giới không biên giới, không chiến tranh, "
            "nơi mọi người sống trong hòa bình. Đó chính là giấc mơ mà John Lennon đã gửi gắm "
            "trong 'Imagine' — bài hát được bình chọn là một trong những ca khúc vĩ đại nhất mọi thời đại. "
            "18 từ vựng được chọn trực tiếp từ lời bài hát: imagine, heaven, above, below, wonder, dreamer, "
            "countries, religion, peace, possessions, greed, hunger, brotherhood, sharing, join, hope, someday, living. "
            "Qua 5 buổi học, bạn sẽ đọc từng đoạn lời bài hát, hiểu ý nghĩa từng từ trong ngữ cảnh "
            "mà John Lennon đã chọn, và cuối cùng đọc trọn vẹn toàn bộ bài hát như một người thực sự "
            "cảm nhận được sức mạnh của ngôn từ. "
            "Hãy để giấc mơ của John Lennon trở thành bước đệm trên hành trình chinh phục tiếng Anh của bạn."
        )
    },
    "youtubeUrl": YOUTUBE_URL,
    "learningSessions": [],
}


# ===== SESSION 1 =====
session_1 = {
    "title": "Buổi 1: Hãy tưởng tượng — Imagine",
    "activities": [
        # --- introAudio 1: Welcome + song context ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu bài hát Imagine",
            "description": "Nghe giới thiệu về bài hát Imagine và hành trình học từ vựng qua âm nhạc",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn đến với khóa học từ vựng qua bài hát 'Imagine' của John Lennon! "
                    "Đây là một trong những bài hát nổi tiếng nhất trong lịch sử âm nhạc thế giới. "
                    "John Lennon — cựu thành viên của The Beatles — đã viết bài hát này vào năm 1971, "
                    "lấy cảm hứng từ thơ của vợ ông, Yoko Ono. "
                    "Bài hát chỉ có một cây piano và giọng hát nhẹ nhàng, nhưng thông điệp thì vô cùng mạnh mẽ: "
                    "hãy tưởng tượng một thế giới không có chiến tranh, không có biên giới, "
                    "nơi mọi người sống trong hòa bình và chia sẻ mọi thứ. "
                    "Trong buổi học đầu tiên, bạn sẽ học 6 từ vựng từ phần mở đầu và điệp khúc: "
                    "imagine, heaven, above, below, wonder, và dreamer. "
                    "Những từ này sẽ mở ra cánh cửa để bạn hiểu giấc mơ mà John Lennon muốn chia sẻ. "
                    "Hãy sẵn sàng nhé — chúng ta bắt đầu!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- introAudio 2: Vocab teaching ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu từ vựng buổi 1",
            "description": "Học 6 từ vựng từ phần mở đầu và điệp khúc bài hát Imagine",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Bây giờ chúng ta sẽ tìm hiểu 6 từ vựng đầu tiên từ bài hát 'Imagine'. "
                    "Mỗi từ đều nằm trong lời bài hát, và bạn sẽ gặp lại chúng khi đọc phần lời ca.\n\n"

                    "Từ đầu tiên là 'imagine' — động từ, nghĩa là tưởng tượng, hình dung. "
                    "Đây là từ quan trọng nhất của bài hát — John Lennon lặp đi lặp lại 'Imagine there's no heaven', "
                    "'Imagine there's no countries', 'Imagine no possessions'. "
                    "Ông ấy mời bạn nhắm mắt lại và hình dung một thế giới khác. "
                    "Ví dụ: Can you imagine a world where everyone lives in peace? — "
                    "Bạn có thể tưởng tượng một thế giới nơi mọi người sống trong hòa bình không?\n\n"

                    "Từ thứ hai là 'heaven' — danh từ, nghĩa là thiên đường, thiên đàng. "
                    "John Lennon hát 'Imagine there's no heaven' — Hãy tưởng tượng không có thiên đường. "
                    "Ông ấy không phản đối tôn giáo — ông ấy muốn mọi người tập trung vào cuộc sống hiện tại "
                    "thay vì chờ đợi một thế giới khác. "
                    "Ví dụ: The beach at sunset looked like heaven on earth — "
                    "Bãi biển lúc hoàng hôn trông như thiên đường trần gian.\n\n"

                    "Từ thứ ba là 'above' — giới từ hoặc trạng từ, nghĩa là ở trên, phía trên. "
                    "Trong bài hát: 'Above us, only sky' — Phía trên chúng ta, chỉ có bầu trời. "
                    "Đây là hình ảnh đẹp — khi không còn thiên đường hay địa ngục, "
                    "phía trên chỉ còn bầu trời bao la. "
                    "Ví dụ: The stars above reminded me how small we are — "
                    "Những ngôi sao phía trên nhắc tôi rằng chúng ta nhỏ bé biết bao.\n\n"

                    "Từ thứ tư là 'below' — giới từ hoặc trạng từ, nghĩa là ở dưới, phía dưới. "
                    "John Lennon hát 'No hell below us' — Không có địa ngục bên dưới chúng ta. "
                    "Cặp từ 'above' và 'below' là đối lập — rất dễ nhớ khi học cùng nhau. "
                    "Ví dụ: The temperature dropped below zero last night — "
                    "Nhiệt độ giảm xuống dưới 0 độ đêm qua.\n\n"

                    "Từ thứ năm là 'wonder' — động từ, nghĩa là tự hỏi, thắc mắc, ngạc nhiên. "
                    "Trong bài hát: 'I wonder if you can' — Tôi tự hỏi liệu bạn có thể không. "
                    "John Lennon tự hỏi liệu người nghe có thể tưởng tượng một thế giới không có tài sản riêng. "
                    "Ví dụ: I wonder what life will be like in fifty years — "
                    "Tôi tự hỏi cuộc sống sẽ như thế nào trong năm mươi năm nữa.\n\n"

                    "Từ cuối cùng là 'dreamer' — danh từ, nghĩa là người mơ mộng. "
                    "John Lennon hát 'You may say I'm a dreamer, but I'm not the only one' — "
                    "Bạn có thể nói tôi là người mơ mộng, nhưng tôi không phải người duy nhất. "
                    "Đây là câu nổi tiếng nhất bài hát — ông ấy thừa nhận mình mơ mộng, "
                    "nhưng tin rằng nhiều người cũng chia sẻ giấc mơ ấy. "
                    "Ví dụ: People called her a dreamer, but she turned her ideas into reality — "
                    "Mọi người gọi cô ấy là người mơ mộng, nhưng cô ấy biến ý tưởng thành hiện thực."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Tưởng tượng & Ước mơ",
            "description": "Học các từ: imagine, heaven, above, below, wonder, dreamer",
            "practiceMinutes": "6",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- speakFlashcards ---
        {
            "activityType": "speakFlashcards",
            "title": "Flashcards: Tập nói từ vựng buổi 1",
            "description": "Tập nói các từ: imagine, heaven, above, below, wonder, dreamer",
            "practiceMinutes": "6",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết từ vựng buổi 1",
            "description": "Chọn nghĩa đúng cho các từ: imagine, heaven, above, below, wonder, dreamer",
            "practiceMinutes": "10",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại từ vựng buổi 1",
            "description": "Điền từ thích hợp vào chỗ trống: imagine, heaven, above, below, wonder, dreamer",
            "practiceMinutes": "10",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- vocabLevel3 ---
        {
            "activityType": "vocabLevel3",
            "title": "Flashcards: Hiểu sâu từ vựng buổi 1",
            "description": "Vận dụng từ vựng trong ngữ cảnh: imagine, heaven, above, below, wonder, dreamer",
            "practiceMinutes": "10",
            "data": {"vocabList": W1, "audioSpeed": -0.1},
        },
        # --- introAudio 3: Grammar/usage ---
        {
            "activityType": "introAudio",
            "title": "Ngữ pháp và cách dùng từ buổi 1",
            "description": "Nghe giải thích cách dùng từ vựng trong ngữ cảnh bài hát Imagine",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng xem xét cách các từ vựng buổi 1 được sử dụng trong ngữ pháp tiếng Anh.\n\n"

                    "Từ 'imagine' là động từ thường, theo sau bởi mệnh đề hoặc danh động từ. "
                    "John Lennon dùng 'Imagine there's no heaven' — cấu trúc 'imagine + mệnh đề'. "
                    "Bạn cũng có thể nói 'Imagine living in a world without war' — 'imagine + V-ing'. "
                    "Lưu ý: không dùng 'imagine to do' — đây là lỗi phổ biến.\n\n"

                    "Từ 'heaven' là danh từ, thường không có mạo từ khi nói về khái niệm tôn giáo: "
                    "'go to heaven' (lên thiên đường). Nhưng khi dùng nghĩa bóng, có thể thêm mạo từ: "
                    "'This place is a heaven for book lovers' (Nơi này là thiên đường cho người yêu sách).\n\n"

                    "Từ 'above' và 'below' là cặp đối lập. 'Above' nghĩa là phía trên: "
                    "'above the clouds' (trên mây), 'above average' (trên trung bình). "
                    "'Below' nghĩa là phía dưới: 'below the surface' (dưới bề mặt), "
                    "'below zero' (dưới 0 độ). Trong bài hát, chúng tạo hình ảnh không gian: "
                    "không có địa ngục bên dưới, chỉ có bầu trời bên trên.\n\n"

                    "Từ 'wonder' khi là động từ thường đi với 'if' hoặc 'whether': "
                    "'I wonder if you can' (Tôi tự hỏi liệu bạn có thể). "
                    "Khi là danh từ: 'the wonders of nature' (những kỳ quan thiên nhiên). "
                    "Tính từ 'wonderful' (tuyệt vời) cũng từ gốc này.\n\n"

                    "Từ 'dreamer' được tạo từ 'dream' + hậu tố '-er' (người làm gì đó). "
                    "Cấu trúc này rất phổ biến: teach → teacher, sing → singer, play → player. "
                    "John Lennon tự gọi mình là 'a dreamer' — nhưng ông ấy nói thêm "
                    "'I'm not the only one' — tôi không phải người duy nhất."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading ---
        {
            "activityType": "reading",
            "title": "Đọc: Lời bài hát Imagine (phần 1)",
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
            "title": "Nghe: Imagine (phần 1)",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": LYRICS_1, "audioSpeed": -0.1},
        },
        # --- writingSentence ---
        {
            "activityType": "writingSentence",
            "title": "Viết: Thực hành từ vựng qua chủ đề ước mơ và tưởng tượng",
            "description": "Viết câu tiếng Anh sử dụng từ vựng buổi 1: imagine, heaven, above, below, wonder, dreamer",
            "practiceMinutes": "10",
            "data": {
                "vocabList": W1,
                "audioSpeed": 0.01,
                "items": [
                    {
                        "targetVocab": "imagine",
                        "prompt": "Sử dụng từ 'imagine' để nói về việc hình dung một điều gì đó — giống như John Lennon mời bạn tưởng tượng một thế giới tốt đẹp hơn. Ví dụ: Close your eyes and imagine a place where everyone treats each other with kindness.",
                    },
                    {
                        "targetVocab": "heaven",
                        "prompt": "Sử dụng từ 'heaven' để nói về một nơi hoặc trải nghiệm tuyệt vời — như John Lennon dùng hình ảnh thiên đường để nói về ước mơ hòa bình. Ví dụ: After a long week of work, spending Sunday morning in the garden feels like heaven.",
                    },
                    {
                        "targetVocab": "above",
                        "prompt": "Sử dụng từ 'above' để nói về vị trí phía trên — như bài hát mô tả bầu trời bao la phía trên chúng ta. Ví dụ: The eagle soared above the mountains, free and powerful against the blue sky.",
                    },
                    {
                        "targetVocab": "below",
                        "prompt": "Sử dụng từ 'below' để nói về vị trí phía dưới — như John Lennon hát rằng không có địa ngục bên dưới chúng ta. Ví dụ: From the top of the tower, we could see the entire city spread out below us.",
                    },
                    {
                        "targetVocab": "wonder",
                        "prompt": "Sử dụng từ 'wonder' để nói về sự tự hỏi hoặc thắc mắc — như John Lennon tự hỏi liệu bạn có thể tưởng tượng một thế giới không tài sản. Ví dụ: I often wonder what the world will look like when my children grow up.",
                    },
                    {
                        "targetVocab": "dreamer",
                        "prompt": "Sử dụng từ 'dreamer' để nói về người có ước mơ lớn — như John Lennon tự nhận mình là một dreamer nhưng không phải người duy nhất. Ví dụ: She was always called a dreamer, but her vision for the company changed everything.",
                    },
                ],
            },
        },
    ],
}
content["learningSessions"].append(session_1)


# ===== SESSION 2 =====
session_2 = {
    "title": "Buổi 2: Hòa bình & Tự do — Peace and Freedom",
    "activities": [
        # --- introAudio 1: Welcome + recap ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu buổi 2",
            "description": "Ôn lại buổi 1 và giới thiệu phần tiếp theo của bài hát Imagine",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn trở lại với buổi học thứ hai! Ở buổi trước, bạn đã học 6 từ vựng từ phần mở đầu "
                    "và điệp khúc bài hát 'Imagine': imagine, heaven, above, below, wonder, và dreamer. "
                    "Bạn đã bắt đầu hiểu giấc mơ của John Lennon — một thế giới nơi con người sống cho hiện tại, "
                    "không bị chia cắt bởi những ranh giới vô hình.\n\n"
                    "Hôm nay chúng ta sẽ đi vào phần sâu sắc nhất của bài hát — nơi John Lennon tưởng tượng "
                    "một thế giới không có quốc gia, không có tôn giáo, nơi mọi người sống trong hòa bình. "
                    "Và ông ấy cũng mơ về một thế giới không có tài sản riêng, không có lòng tham hay đói nghèo. "
                    "6 từ vựng mới của buổi 2 là: countries, religion, peace, possessions, greed, và hunger. "
                    "Hãy cùng khám phá nhé!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- introAudio 2: Vocab teaching ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu từ vựng buổi 2",
            "description": "Học 6 từ vựng từ phần giữa bài hát về hòa bình và tự do",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng tìm hiểu 6 từ vựng mới từ bài hát 'Imagine'.\n\n"

                    "Từ đầu tiên là 'countries' — danh từ số nhiều, nghĩa là các quốc gia, các nước. "
                    "John Lennon hát 'Imagine there's no countries' — Hãy tưởng tượng không có quốc gia nào. "
                    "Ông ấy không ghét đất nước — ông ấy mơ về một thế giới nơi biên giới "
                    "không còn là lý do để con người chia rẽ và chiến tranh. "
                    "Ví dụ: People from many different countries came together for the music festival — "
                    "Người từ nhiều quốc gia khác nhau cùng đến lễ hội âm nhạc.\n\n"

                    "Từ thứ hai là 'religion' — danh từ, nghĩa là tôn giáo, đạo. "
                    "Trong bài hát: 'And no religion too' — Và cũng không có tôn giáo. "
                    "John Lennon tưởng tượng một thế giới nơi con người không bị chia rẽ bởi tín ngưỡng khác nhau. "
                    "Ví dụ: Religion plays an important role in many people's daily lives — "
                    "Tôn giáo đóng vai trò quan trọng trong cuộc sống hàng ngày của nhiều người.\n\n"

                    "Từ thứ ba là 'peace' — danh từ, nghĩa là hòa bình, sự yên bình. "
                    "John Lennon hát 'Imagine all the people living life in peace' — "
                    "Hãy tưởng tượng tất cả mọi người sống cuộc đời trong hòa bình. "
                    "Đây là trung tâm của toàn bộ bài hát — giấc mơ hòa bình. "
                    "Ví dụ: After years of conflict, the two nations finally found peace — "
                    "Sau nhiều năm xung đột, hai quốc gia cuối cùng đã tìm được hòa bình.\n\n"

                    "Từ thứ tư là 'possessions' — danh từ số nhiều, nghĩa là tài sản, của cải, đồ đạc. "
                    "Trong bài hát: 'Imagine no possessions' — Hãy tưởng tượng không có tài sản. "
                    "John Lennon muốn nói rằng khi con người không bám víu vào của cải vật chất, "
                    "họ sẽ tự do hơn và chia sẻ nhiều hơn. "
                    "Ví dụ: She packed all her possessions into two small suitcases and moved abroad — "
                    "Cô ấy đóng gói tất cả tài sản vào hai chiếc vali nhỏ và chuyển ra nước ngoài.\n\n"

                    "Từ thứ năm là 'greed' — danh từ, nghĩa là lòng tham, sự tham lam. "
                    "Trong bài hát: 'No need for greed or hunger' — Không cần lòng tham hay đói nghèo. "
                    "John Lennon tin rằng nếu mọi người chia sẻ, sẽ không ai cần phải tham lam. "
                    "Ví dụ: Greed can destroy friendships and tear families apart — "
                    "Lòng tham có thể phá hủy tình bạn và chia rẽ gia đình.\n\n"

                    "Từ cuối cùng là 'hunger' — danh từ, nghĩa là sự đói, cơn đói, nạn đói. "
                    "Trong bài hát: 'No need for greed or hunger' — Không cần lòng tham hay đói nghèo. "
                    "John Lennon đặt 'greed' và 'hunger' cạnh nhau — lòng tham của người này "
                    "gây ra cái đói của người khác. "
                    "Ví dụ: Millions of people around the world still suffer from hunger every day — "
                    "Hàng triệu người trên thế giới vẫn chịu đựng cái đói mỗi ngày."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Hòa bình & Tự do",
            "description": "Học các từ: countries, religion, peace, possessions, greed, hunger",
            "practiceMinutes": "6",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- speakFlashcards ---
        {
            "activityType": "speakFlashcards",
            "title": "Flashcards: Tập nói từ vựng buổi 2",
            "description": "Tập nói các từ: countries, religion, peace, possessions, greed, hunger",
            "practiceMinutes": "6",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết từ vựng buổi 2",
            "description": "Chọn nghĩa đúng cho các từ: countries, religion, peace, possessions, greed, hunger",
            "practiceMinutes": "10",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại từ vựng buổi 2",
            "description": "Điền từ thích hợp vào chỗ trống: countries, religion, peace, possessions, greed, hunger",
            "practiceMinutes": "10",
            "data": {"vocabList": W2, "audioSpeed": -0.1},
        },
        # --- vocabLevel3 ---
        {
            "activityType": "vocabLevel3",
            "title": "Flashcards: Hiểu sâu từ vựng buổi 2",
            "description": "Vận dụng từ vựng trong ngữ cảnh: countries, religion, peace, possessions, greed, hunger",
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

                    "Từ 'countries' là danh từ đếm được số nhiều của 'country'. "
                    "Lưu ý cách viết: 'country' → 'countries' (đổi 'y' thành 'ies'). "
                    "Từ 'country' cũng có nghĩa là 'nông thôn': 'the countryside' (vùng quê). "
                    "Trong bài hát, John Lennon dùng nghĩa 'quốc gia' — 'no countries' nghĩa là không có biên giới.\n\n"

                    "Từ 'religion' là danh từ, có thể đếm được hoặc không đếm được. "
                    "Khi nói chung: 'Religion is important' (Tôn giáo quan trọng) — không đếm được. "
                    "Khi nói cụ thể: 'There are many religions in the world' (Có nhiều tôn giáo trên thế giới) — đếm được. "
                    "Tính từ tương ứng là 'religious' (thuộc về tôn giáo).\n\n"

                    "Từ 'peace' là danh từ không đếm được — bạn không nói 'a peace' hay 'peaces'. "
                    "Các cụm từ phổ biến: 'world peace' (hòa bình thế giới), 'peace of mind' (sự an tâm), "
                    "'at peace' (yên bình). Tính từ là 'peaceful' (yên bình), "
                    "trạng từ là 'peacefully' (một cách yên bình).\n\n"

                    "Từ 'possessions' thường dùng ở số nhiều khi nói về tài sản, đồ đạc. "
                    "Số ít 'possession' thường dùng trong cụm 'in possession of' (sở hữu). "
                    "Động từ gốc là 'possess' (sở hữu). "
                    "John Lennon dùng 'no possessions' — không có tài sản — một ý tưởng triết học sâu sắc.\n\n"

                    "Từ 'greed' là danh từ không đếm được — bạn không nói 'a greed'. "
                    "Tính từ là 'greedy' (tham lam): 'Don't be greedy' (Đừng tham lam). "
                    "Trong bài hát, 'no need for greed' — không cần lòng tham — "
                    "vì khi mọi người chia sẻ, không ai cần phải tham.\n\n"

                    "Từ 'hunger' là danh từ không đếm được. Tính từ là 'hungry' (đói). "
                    "Lưu ý: 'hunger' có thể dùng nghĩa bóng — 'a hunger for knowledge' (khát khao kiến thức). "
                    "Trong bài hát, John Lennon dùng nghĩa đen — nạn đói trên thế giới."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading ---
        {
            "activityType": "reading",
            "title": "Đọc: Lời bài hát Imagine (phần 2)",
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
            "title": "Nghe: Imagine (phần 2)",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": LYRICS_2, "audioSpeed": -0.1},
        },
        # --- writingSentence ---
        {
            "activityType": "writingSentence",
            "title": "Viết: Thực hành từ vựng qua chủ đề hòa bình và chia sẻ",
            "description": "Viết câu tiếng Anh sử dụng từ vựng buổi 2: countries, religion, peace, possessions, greed, hunger",
            "practiceMinutes": "10",
            "data": {
                "vocabList": W2,
                "audioSpeed": 0.01,
                "items": [
                    {
                        "targetVocab": "countries",
                        "prompt": "Sử dụng từ 'countries' để nói về các quốc gia — như John Lennon mơ về một thế giới không có biên giới giữa các countries. Ví dụ: Travelling to different countries has taught me that people everywhere share the same basic hopes and dreams.",
                    },
                    {
                        "targetVocab": "religion",
                        "prompt": "Sử dụng từ 'religion' để nói về tín ngưỡng hoặc đức tin — như bài hát tưởng tượng một thế giới nơi religion không chia rẽ con người. Ví dụ: Despite their different religion backgrounds, the neighbors always helped each other during difficult times.",
                    },
                    {
                        "targetVocab": "peace",
                        "prompt": "Sử dụng từ 'peace' để nói về sự hòa bình hoặc yên tĩnh — như John Lennon mơ về mọi người sống cuộc đời trong peace. Ví dụ: Walking through the quiet forest in the early morning gave her a deep sense of peace.",
                    },
                    {
                        "targetVocab": "possessions",
                        "prompt": "Sử dụng từ 'possessions' để nói về tài sản hoặc đồ đạc — như John Lennon tưởng tượng một thế giới không có possessions. Ví dụ: After the flood, the family lost most of their possessions but were grateful to be alive.",
                    },
                    {
                        "targetVocab": "greed",
                        "prompt": "Sử dụng từ 'greed' để nói về lòng tham — như bài hát nói rằng trong một thế giới chia sẻ, không cần greed. Ví dụ: The company's greed for profit led them to ignore the safety of their workers.",
                    },
                    {
                        "targetVocab": "hunger",
                        "prompt": "Sử dụng từ 'hunger' để nói về sự đói hoặc khát khao — như John Lennon mơ về một thế giới không còn hunger. Ví dụ: The organization works tirelessly to fight hunger in communities across the country.",
                    },
                ],
            },
        },
    ],
}
content["learningSessions"].append(session_2)


# ===== SESSION 3 =====
session_3 = {
    "title": "Buổi 3: Tình anh em & Chia sẻ — Brotherhood and Sharing",
    "activities": [
        # --- introAudio 1: Welcome + recap ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu buổi 3",
            "description": "Ôn lại buổi 1-2 và giới thiệu phần cuối bài hát Imagine",
            "practiceMinutes": "1",
            "data": {
                "text": (
                    "Chào mừng bạn đến với buổi học thứ ba — buổi cuối cùng trước khi ôn tập! "
                    "Bạn đã tiến rất xa rồi đấy. Ở buổi 1, bạn học về ước mơ và trí tưởng tượng "
                    "với imagine, heaven, above, below, wonder, dreamer. Ở buổi 2, bạn khám phá "
                    "hòa bình và tự do với countries, religion, peace, possessions, greed, hunger.\n\n"
                    "Hôm nay chúng ta sẽ đến với phần đẹp nhất của bài hát — nơi John Lennon nói về "
                    "tình anh em giữa con người, về việc chia sẻ tất cả, và về niềm hy vọng rằng "
                    "một ngày nào đó mọi người sẽ cùng nhau biến giấc mơ thành hiện thực. "
                    "6 từ vựng mới: brotherhood, sharing, join, hope, someday, living. Hãy bắt đầu nào!"
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- introAudio 2: Vocab teaching ---
        {
            "activityType": "introAudio",
            "title": "Giới thiệu từ vựng buổi 3",
            "description": "Học 6 từ vựng từ phần cuối bài hát về tình anh em và hy vọng",
            "practiceMinutes": "3",
            "data": {
                "text": (
                    "Hãy cùng tìm hiểu 6 từ vựng cuối cùng từ bài hát 'Imagine'.\n\n"

                    "Từ đầu tiên là 'brotherhood' — danh từ, nghĩa là tình anh em, tình huynh đệ. "
                    "John Lennon hát 'A brotherhood of man' — Tình anh em của nhân loại. "
                    "Đây là hình ảnh đẹp nhất bài hát — khi không còn biên giới, tài sản, hay tôn giáo chia rẽ, "
                    "tất cả con người trở thành anh em. "
                    "Ví dụ: The soldiers developed a strong sense of brotherhood during their time together — "
                    "Những người lính phát triển tình anh em sâu sắc trong thời gian bên nhau.\n\n"

                    "Từ thứ hai là 'sharing' — danh động từ hoặc tính từ, nghĩa là sự chia sẻ. "
                    "Trong bài hát: 'Imagine all the people sharing all the world' — "
                    "Hãy tưởng tượng tất cả mọi người chia sẻ cả thế giới. "
                    "Đây là giải pháp mà John Lennon đề xuất — khi mọi người chia sẻ, "
                    "không ai cần tham lam hay đói khổ. "
                    "Ví dụ: Sharing knowledge with others is one of the most rewarding things you can do — "
                    "Chia sẻ kiến thức với người khác là một trong những điều đáng làm nhất.\n\n"

                    "Từ thứ ba là 'join' — động từ, nghĩa là tham gia, gia nhập, cùng nhau. "
                    "John Lennon hát 'I hope someday you'll join us' — "
                    "Tôi hy vọng một ngày nào đó bạn sẽ tham gia cùng chúng tôi. "
                    "Ông ấy mời gọi người nghe — không ép buộc, chỉ hy vọng. "
                    "Ví dụ: Would you like to join us for dinner tonight? — "
                    "Bạn có muốn tham gia bữa tối với chúng tôi không?\n\n"

                    "Từ thứ tư là 'hope' — danh từ hoặc động từ, nghĩa là hy vọng, niềm hy vọng. "
                    "Trong bài hát: 'I hope someday you'll join us' — Tôi hy vọng một ngày nào đó bạn sẽ tham gia. "
                    "Toàn bộ bài hát 'Imagine' thực chất là một bài hát về hy vọng — "
                    "hy vọng rằng thế giới có thể thay đổi. "
                    "Ví dụ: Even in the darkest times, we must never lose hope — "
                    "Ngay cả trong những lúc tăm tối nhất, chúng ta không bao giờ được mất hy vọng.\n\n"

                    "Từ thứ năm là 'someday' — trạng từ, nghĩa là một ngày nào đó, ngày nào đó. "
                    "John Lennon hát 'I hope someday you'll join us' — "
                    "Tôi hy vọng một ngày nào đó bạn sẽ tham gia. "
                    "Từ 'someday' mang theo sự kiên nhẫn — ông ấy biết giấc mơ chưa thành hiện thực, "
                    "nhưng tin rằng nó sẽ đến. "
                    "Ví dụ: Someday I will travel around the world and see all the places I have read about — "
                    "Một ngày nào đó tôi sẽ đi vòng quanh thế giới và thăm tất cả những nơi tôi đã đọc.\n\n"

                    "Từ cuối cùng là 'living' — danh động từ hoặc tính từ, nghĩa là sống, cuộc sống. "
                    "John Lennon dùng từ này hai lần: 'Living for today' (Sống cho hôm nay) "
                    "và 'Living life in peace' (Sống cuộc đời trong hòa bình). "
                    "Cả hai đều nhấn mạnh việc sống trọn vẹn trong hiện tại. "
                    "Ví dụ: Living in a small town taught me the value of close relationships — "
                    "Sống ở một thị trấn nhỏ dạy tôi giá trị của những mối quan hệ gần gũi."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- viewFlashcards ---
        {
            "activityType": "viewFlashcards",
            "title": "Flashcards: Tình anh em & Chia sẻ",
            "description": "Học các từ: brotherhood, sharing, join, hope, someday, living",
            "practiceMinutes": "6",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- speakFlashcards ---
        {
            "activityType": "speakFlashcards",
            "title": "Flashcards: Tập nói từ vựng buổi 3",
            "description": "Tập nói các từ: brotherhood, sharing, join, hope, someday, living",
            "practiceMinutes": "6",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- vocabLevel1 ---
        {
            "activityType": "vocabLevel1",
            "title": "Flashcards: Nhận biết từ vựng buổi 3",
            "description": "Chọn nghĩa đúng cho các từ: brotherhood, sharing, join, hope, someday, living",
            "practiceMinutes": "10",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- vocabLevel2 ---
        {
            "activityType": "vocabLevel2",
            "title": "Flashcards: Nhớ lại từ vựng buổi 3",
            "description": "Điền từ thích hợp vào chỗ trống: brotherhood, sharing, join, hope, someday, living",
            "practiceMinutes": "10",
            "data": {"vocabList": W3, "audioSpeed": -0.1},
        },
        # --- vocabLevel3 ---
        {
            "activityType": "vocabLevel3",
            "title": "Flashcards: Hiểu sâu từ vựng buổi 3",
            "description": "Vận dụng từ vựng trong ngữ cảnh: brotherhood, sharing, join, hope, someday, living",
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

                    "Từ 'brotherhood' được tạo từ 'brother' + hậu tố '-hood'. "
                    "Hậu tố '-hood' biến danh từ thành trạng thái hoặc nhóm: "
                    "child → childhood (tuổi thơ), neighbor → neighborhood (khu phố), "
                    "father → fatherhood (vai trò làm cha). "
                    "'A brotherhood of man' nghĩa là tình anh em của toàn nhân loại.\n\n"

                    "Từ 'sharing' là dạng V-ing của 'share'. Trong bài hát, nó được dùng như danh động từ: "
                    "'Imagine all the people sharing all the world' — 'sharing' là hành động chính. "
                    "Cấu trúc 'imagine + someone + V-ing' rất phổ biến: "
                    "'Imagine yourself living in Paris' (Hãy tưởng tượng bạn sống ở Paris).\n\n"

                    "Từ 'join' là ngoại động từ — theo sau trực tiếp bởi tân ngữ, không cần giới từ: "
                    "'join us' (tham gia cùng chúng tôi), 'join a club' (gia nhập câu lạc bộ). "
                    "Lưu ý: không nói 'join to us' — đây là lỗi phổ biến. "
                    "Nhưng 'join in' (tham gia vào hoạt động) thì cần giới từ: 'join in the discussion'.\n\n"

                    "Từ 'hope' vừa là danh từ vừa là động từ. Là động từ: 'I hope you'll join us' — "
                    "theo sau bởi mệnh đề. Là danh từ: 'There is hope for the future' (Có hy vọng cho tương lai). "
                    "Tính từ 'hopeful' (đầy hy vọng) và 'hopeless' (vô vọng) là cặp đối lập.\n\n"

                    "Từ 'someday' là trạng từ chỉ thời gian tương lai không xác định. "
                    "Khác với 'some day' (hai từ) — 'some day' thường dùng với 'one': "
                    "'one day' hoặc 'some day'. 'Someday' (một từ) mang tính mơ mộng hơn, "
                    "phù hợp với tinh thần bài hát.\n\n"

                    "Từ 'living' trong bài hát được dùng như danh động từ: "
                    "'Living for today' (Sống cho hôm nay), 'Living life in peace' (Sống cuộc đời trong hòa bình). "
                    "Cấu trúc 'living + for/in' rất tự nhiên trong tiếng Anh. "
                    "Lưu ý: 'living' cũng là tính từ — 'living room' (phòng khách), 'living things' (sinh vật sống)."
                ),
                "audioSpeed": 0.01,
            },
        },
        # --- reading ---
        {
            "activityType": "reading",
            "title": "Đọc: Lời bài hát Imagine (phần 3)",
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
            "title": "Nghe: Imagine (phần 3)",
            "description": "Nghe lời bài hát và theo dõi.",
            "practiceMinutes": "3",
            "data": {"text": LYRICS_3, "audioSpeed": -0.1},
        },
        # --- writingSentence ---
        {
            "activityType": "writingSentence",
            "title": "Viết: Thực hành từ vựng qua chủ đề đoàn kết và hy vọng",
            "description": "Viết câu tiếng Anh sử dụng từ vựng buổi 3: brotherhood, sharing, join, hope, someday, living",
            "practiceMinutes": "10",
            "data": {
                "vocabList": W3,
                "audioSpeed": 0.01,
                "items": [
                    {
                        "targetVocab": "brotherhood",
                        "prompt": "Sử dụng từ 'brotherhood' để nói về tình anh em hoặc sự đoàn kết — như John Lennon mơ về một brotherhood of man nơi mọi người là anh em. Ví dụ: The volunteers felt a deep sense of brotherhood as they worked together to rebuild the school.",
                    },
                    {
                        "targetVocab": "sharing",
                        "prompt": "Sử dụng từ 'sharing' để nói về việc chia sẻ — như bài hát tưởng tượng mọi người sharing cả thế giới với nhau. Ví dụ: Sharing meals with friends and family is one of life's greatest pleasures.",
                    },
                    {
                        "targetVocab": "join",
                        "prompt": "Sử dụng từ 'join' để nói về việc tham gia — như John Lennon hy vọng bạn sẽ join cùng ông ấy trong giấc mơ hòa bình. Ví dụ: More than fifty people decided to join the community garden project this spring.",
                    },
                    {
                        "targetVocab": "hope",
                        "prompt": "Sử dụng từ 'hope' để nói về niềm hy vọng — như toàn bộ bài hát Imagine là một bài ca về hope cho tương lai. Ví dụ: Despite all the challenges, she never gave up hope that things would get better.",
                    },
                    {
                        "targetVocab": "someday",
                        "prompt": "Sử dụng từ 'someday' để nói về một ngày trong tương lai — như John Lennon hy vọng someday mọi người sẽ cùng nhau sống hòa bình. Ví dụ: Someday I hope to visit every continent and learn about different cultures.",
                    },
                    {
                        "targetVocab": "living",
                        "prompt": "Sử dụng từ 'living' để nói về cuộc sống hoặc cách sống — như John Lennon hát về living for today và living life in peace. Ví dụ: Living abroad for a year completely changed my perspective on the world.",
                    },
                ],
            },
        },
    ],
}
content["learningSessions"].append(session_3)

