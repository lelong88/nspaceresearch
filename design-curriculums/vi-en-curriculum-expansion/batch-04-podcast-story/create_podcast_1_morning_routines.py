import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from firebase_token import get_firebase_id_token
from validate_curriculum import (
    validate_balanced_skills_beginner,
    validate_content_type_tags,
    validate_bilingual_prompts,
)

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Curriculum #41: Easy English: Morning Routines
# Level: beginner | Skill focus: balanced_skills | Content type: ["podcast"]
# Topic: Daily life | 12 words (2 groups of 6), 4 sessions, bilingual (vi-en)
# Description tone: provocative_question (first in podcast series)
# Farewell tone: introspective_guide (first in podcast series)
# W1: routine, alarm, breakfast, shower, commute, schedule
# W2: habit, awake, prepare, organize, productive, energize

content = {
    "title": "Easy English: Morning Routines",
    "contentTypeTags": ["podcast"],
    "description": "BẠN THỨC DẬY MỖI SÁNG VÀ LÀM GÌ ĐẦU TIÊN — KIỂM TRA ĐIỆN THOẠI HAY KIỂM TRA CHÍNH MÌNH?\n\nMỗi buổi sáng, bạn có khoảng 90 phút vàng — khoảng thời gian mà não bộ tỉnh táo nhất, tập trung nhất, sẵn sàng nhất. Nhưng hầu hết chúng ta dùng 90 phút đó để lướt mạng xã hội, đọc tin nhắn, và chạy đua với đồng hồ. Bạn có bao giờ tự hỏi: tại sao mình luôn cảm thấy mệt mỏi dù đã ngủ đủ giấc?\n\nBuổi sáng giống như trang đầu tiên của một cuốn sách — nếu trang đầu nhàm chán, bạn sẽ không muốn đọc tiếp. Nhưng nếu bạn biết cách viết trang đầu đó — với một thói quen rõ ràng, một lịch trình có chủ đích — cả ngày của bạn sẽ khác.\n\nHai nhân vật Lan và Minh sẽ chia sẻ buổi sáng của họ — từ tiếng chuông báo thức đến bữa sáng, từ việc chuẩn bị đến hành trình đi làm. Bạn sẽ nghe họ nói về thói quen, lịch trình, và cách họ tổ chức buổi sáng để bắt đầu ngày mới tràn đầy năng lượng.\n\n12 từ vựng trong bài học này — từ routine đến energize — sẽ giúp bạn tự tin nói về buổi sáng của mình bằng tiếng Anh, vừa xây dựng thói quen tốt hơn, vừa nâng trình ngoại ngữ mỗi ngày.",
    "preview": {
        "text": "What does your morning look like? Do you jump out of bed full of energy, or do you hit the alarm five times before dragging yourself to the shower? In this podcast-inspired lesson, you will learn 12 essential English words about morning routines: routine, alarm, breakfast, shower, commute, schedule, habit, awake, prepare, organize, productive, and energize. Follow Lan and Minh as they share their very different mornings — Lan wakes up early to prepare a healthy breakfast and organize her schedule, while Minh hits snooze and rushes through his commute. Through two conversational reading passages, a full review session, and a final combined reading, you will practice describing your own morning habits in English. By the end, you will be able to talk about daily routines, time management, and morning habits with confidence."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về thói quen buổi sáng — giới thiệu 6 từ vựng đầu tiên.",
                    "data": {
                        "text": "Chào mừng bạn đến với Easy English: Morning Routines — bài học đầu tiên trong chuỗi podcast tiếng Anh dành cho người mới bắt đầu. Hôm nay chúng ta sẽ nói về một chủ đề rất gần gũi: buổi sáng của bạn. Mỗi ngày bạn thức dậy, bạn làm gì? Bạn ăn sáng không? Bạn đi làm bằng gì? Đây là những câu hỏi đơn giản, nhưng khi nói bằng tiếng Anh, bạn cần biết đúng từ.\n\nTrong phần này, bạn sẽ học 6 từ vựng tiếng Anh: routine, alarm, breakfast, shower, commute, và schedule. Đây là những từ bạn sẽ dùng mỗi ngày khi nói về buổi sáng.\n\nTừ đầu tiên là routine — danh từ — nghĩa là thói quen, lề thói hàng ngày. Routine là những việc bạn làm đi làm lại mỗi ngày theo một trật tự nhất định. Ví dụ: 'My morning routine starts at six o'clock.' Trong bài đọc, Lan sẽ kể về morning routine của cô ấy — những việc cô ấy làm mỗi sáng.\n\nTừ thứ hai là alarm — danh từ — nghĩa là chuông báo thức. Alarm là âm thanh đánh thức bạn mỗi sáng. Ví dụ: 'I set my alarm for six thirty every day.' Trong bài đọc, bạn sẽ thấy Minh luôn tắt alarm rồi ngủ tiếp — một thói quen không tốt lắm!\n\nTừ thứ ba là breakfast — danh từ — nghĩa là bữa sáng. Breakfast là bữa ăn đầu tiên trong ngày. Ví dụ: 'She eats breakfast before going to work.' Trong bài đọc, Lan chuẩn bị breakfast rất cẩn thận mỗi sáng.\n\nTừ thứ tư là shower — danh từ — nghĩa là vòi sen, việc tắm. Shower là khi bạn đứng dưới vòi nước để tắm rửa. Ví dụ: 'He takes a quick shower every morning.' Trong bài đọc, shower là một phần quan trọng trong buổi sáng của cả Lan và Minh.\n\nTừ thứ năm là commute — danh từ và động từ — nghĩa là hành trình đi làm, đi lại hàng ngày. Commute là quãng đường bạn đi từ nhà đến nơi làm việc. Ví dụ: 'Her commute takes about thirty minutes.' Trong bài đọc, Lan và Minh có cách commute rất khác nhau.\n\nTừ cuối cùng là schedule — danh từ — nghĩa là lịch trình, thời gian biểu. Schedule là kế hoạch cho những việc bạn sẽ làm trong ngày. Ví dụ: 'I check my schedule every morning.' Trong bài đọc, Lan luôn xem schedule trước khi ra khỏi nhà.\n\nBạn đã có 6 từ vựng đầu tiên rồi! Hãy bắt đầu với flashcard, sau đó đọc bài về buổi sáng của Lan nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Buổi sáng cơ bản",
                    "description": "Học 6 từ: routine, alarm, breakfast, shower, commute, schedule",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Buổi sáng cơ bản",
                    "description": "Học 6 từ: routine, alarm, breakfast, shower, commute, schedule",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Buổi sáng cơ bản",
                    "description": "Học 6 từ: routine, alarm, breakfast, shower, commute, schedule",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Buổi sáng cơ bản",
                    "description": "Học 6 từ: routine, alarm, breakfast, shower, commute, schedule",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Buổi sáng của Lan",
                    "description": "Lan shares her calm and organized morning routine before work.",
                    "data": {
                        "text": "Lan wakes up at six every day. Her alarm rings once, and she gets out of bed. She does not hit snooze. That is her rule.\n\nFirst, Lan takes a shower. The warm water helps her feel awake. After her shower, she goes to the kitchen.\n\nBreakfast is important to Lan. She makes rice and eggs. Sometimes she eats bread with jam. She always drinks a glass of water first.\n\nWhile she eats, Lan checks her schedule. She looks at her phone and reads her plan for the day. She likes to know what is coming.\n\nAfter breakfast, Lan gets dressed. She picks her clothes the night before. This saves time in the morning.\n\nHer commute is short. She rides her motorbike to the office. It takes about twenty minutes. She listens to English podcasts on the way.\n\nLan likes her morning routine. It is simple and calm. She says a good morning makes a good day."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Buổi sáng của Lan",
                    "description": "Lan shares her calm and organized morning routine before work.",
                    "data": {
                        "text": "Lan wakes up at six every day. Her alarm rings once, and she gets out of bed. She does not hit snooze. That is her rule.\n\nFirst, Lan takes a shower. The warm water helps her feel awake. After her shower, she goes to the kitchen.\n\nBreakfast is important to Lan. She makes rice and eggs. Sometimes she eats bread with jam. She always drinks a glass of water first.\n\nWhile she eats, Lan checks her schedule. She looks at her phone and reads her plan for the day. She likes to know what is coming.\n\nAfter breakfast, Lan gets dressed. She picks her clothes the night before. This saves time in the morning.\n\nHer commute is short. She rides her motorbike to the office. It takes about twenty minutes. She listens to English podcasts on the way.\n\nLan likes her morning routine. It is simple and calm. She says a good morning makes a good day."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Buổi sáng của Lan",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Lan wakes up at six every day. Her alarm rings once, and she gets out of bed. She does not hit snooze. That is her rule.\n\nFirst, Lan takes a shower. The warm water helps her feel awake. After her shower, she goes to the kitchen.\n\nBreakfast is important to Lan. She makes rice and eggs. Sometimes she eats bread with jam. She always drinks a glass of water first.\n\nWhile she eats, Lan checks her schedule. She looks at her phone and reads her plan for the day. She likes to know what is coming.\n\nAfter breakfast, Lan gets dressed. She picks her clothes the night before. This saves time in the morning.\n\nHer commute is short. She rides her motorbike to the office. It takes about twenty minutes. She listens to English podcasts on the way.\n\nLan likes her morning routine. It is simple and calm. She says a good morning makes a good day."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Buổi sáng cơ bản",
                    "description": "Viết câu sử dụng từ vựng về thói quen buổi sáng.",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule"],
                        "items": [
                            {
                                "targetVocab": "routine",
                                "prompt": "Hãy dùng từ 'routine' để viết một câu về thói quen buổi sáng của bạn. Ví dụ: My morning routine is very simple — I wake up, shower, and eat breakfast."
                            },
                            {
                                "targetVocab": "alarm",
                                "prompt": "Hãy dùng từ 'alarm' để viết một câu về cách bạn thức dậy. Ví dụ: I set my alarm for seven o'clock every morning."
                            },
                            {
                                "targetVocab": "breakfast",
                                "prompt": "Hãy dùng từ 'breakfast' để viết một câu về bữa sáng của bạn. Ví dụ: I usually eat breakfast with my family before work."
                            },
                            {
                                "targetVocab": "shower",
                                "prompt": "Hãy dùng từ 'shower' để viết một câu về việc tắm buổi sáng. Ví dụ: I take a hot shower to wake up every morning."
                            },
                            {
                                "targetVocab": "commute",
                                "prompt": "Hãy dùng từ 'commute' để viết một câu về hành trình đi làm hoặc đi học của bạn. Ví dụ: My commute to work takes about thirty minutes by bus."
                            },
                            {
                                "targetVocab": "schedule",
                                "prompt": "Hãy dùng từ 'schedule' để viết một câu về lịch trình trong ngày của bạn. Ví dụ: I always check my schedule before I leave the house."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Ôn lại phần 1 và giới thiệu 6 từ vựng mới về thói quen và năng lượng buổi sáng.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với phần 2 của Easy English: Morning Routines! Trong phần trước, bạn đã học 6 từ vựng: routine là thói quen hàng ngày, alarm là chuông báo thức, breakfast là bữa sáng, shower là việc tắm, commute là hành trình đi làm, và schedule là lịch trình. Bạn cũng đã đọc về buổi sáng yên bình của Lan — cô ấy dậy sớm, tắm, ăn sáng cẩn thận, và đi làm bằng xe máy.\n\nBây giờ, hãy gặp Minh — buổi sáng của Minh rất khác Lan! Trong phần này, bạn sẽ học thêm 6 từ vựng mới: habit, awake, prepare, organize, productive, và energize.\n\nTừ đầu tiên là habit — danh từ — nghĩa là thói quen. Habit giống routine nhưng tập trung vào một hành động cụ thể mà bạn làm lặp đi lặp lại. Ví dụ: 'Drinking coffee is his morning habit.' Trong bài đọc, Minh có một số habit không tốt lắm vào buổi sáng.\n\nTừ thứ hai là awake — tính từ — nghĩa là tỉnh giấc, tỉnh táo. Awake là trạng thái khi bạn không còn ngủ nữa. Ví dụ: 'She is awake at five every morning.' Trong bài đọc, Minh rất khó để hoàn toàn awake vào buổi sáng.\n\nTừ thứ ba là prepare — động từ — nghĩa là chuẩn bị. Prepare là khi bạn làm mọi thứ sẵn sàng trước. Ví dụ: 'I prepare my bag the night before.' Trong bài đọc, Minh không prepare gì cả — và đó là vấn đề.\n\nTừ thứ tư là organize — động từ — nghĩa là sắp xếp, tổ chức. Organize là khi bạn đặt mọi thứ vào đúng chỗ, đúng thứ tự. Ví dụ: 'She likes to organize her desk before work.' Trong bài đọc, Minh muốn organize buổi sáng tốt hơn.\n\nTừ thứ năm là productive — tính từ — nghĩa là hiệu quả, năng suất. Productive là khi bạn làm được nhiều việc trong ít thời gian. Ví dụ: 'A good morning makes you more productive.' Trong bài đọc, Minh nhận ra rằng buổi sáng lộn xộn khiến cả ngày kém productive.\n\nTừ cuối cùng là energize — động từ — nghĩa là tiếp thêm năng lượng, làm cho tràn đầy sức sống. Energize là khi một thứ gì đó giúp bạn cảm thấy khỏe khoắn và sẵn sàng hành động. Ví dụ: 'A cold glass of water can energize you in the morning.' Trong bài đọc, Minh tìm cách energize bản thân mà không cần ba ly cà phê.\n\nSáu từ mới đã sẵn sàng! Hãy học flashcard rồi đọc về buổi sáng hỗn loạn của Minh nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thói quen và năng lượng",
                    "description": "Học 6 từ: habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Thói quen và năng lượng",
                    "description": "Học 6 từ: habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thói quen và năng lượng",
                    "description": "Học 6 từ: habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Thói quen và năng lượng",
                    "description": "Học 6 từ: habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Buổi sáng của Minh",
                    "description": "Minh shares his chaotic morning and his plan to build better habits.",
                    "data": {
                        "text": "Minh is not a morning person. His alarm goes off at seven, but he does not get up. He hits snooze three times. By seven thirty, he is still in bed.\n\nWhen Minh finally wakes up, he grabs his phone. He checks social media for ten minutes. This is a bad habit, but he does it every day.\n\nHe is not fully awake until he drinks coffee. He makes a strong cup and drinks it fast. Then he runs to the shower.\n\nMinh does not prepare anything the night before. His clothes are on the chair. His bag is on the floor. He cannot find his keys. Every morning is a small race.\n\nHe does not eat breakfast at home. He buys bread on the way to work. He eats while he rides his motorbike. This is not safe, but he is always late.\n\nHis commute is long. He sits in traffic for forty minutes. He feels tired and stressed before the day even starts.\n\nMinh wants to change. He wants to organize his mornings better. He wants to be more productive. He thinks a good routine can energize him.\n\nLast week, Minh tried something new. He set his alarm fifteen minutes earlier. He did not check his phone first. He ate breakfast at home. It was a small change, but he felt different. He felt ready.\n\nMinh knows it takes time to build a new habit. But he is trying. One morning at a time."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Buổi sáng của Minh",
                    "description": "Minh shares his chaotic morning and his plan to build better habits.",
                    "data": {
                        "text": "Minh is not a morning person. His alarm goes off at seven, but he does not get up. He hits snooze three times. By seven thirty, he is still in bed.\n\nWhen Minh finally wakes up, he grabs his phone. He checks social media for ten minutes. This is a bad habit, but he does it every day.\n\nHe is not fully awake until he drinks coffee. He makes a strong cup and drinks it fast. Then he runs to the shower.\n\nMinh does not prepare anything the night before. His clothes are on the chair. His bag is on the floor. He cannot find his keys. Every morning is a small race.\n\nHe does not eat breakfast at home. He buys bread on the way to work. He eats while he rides his motorbike. This is not safe, but he is always late.\n\nHis commute is long. He sits in traffic for forty minutes. He feels tired and stressed before the day even starts.\n\nMinh wants to change. He wants to organize his mornings better. He wants to be more productive. He thinks a good routine can energize him.\n\nLast week, Minh tried something new. He set his alarm fifteen minutes earlier. He did not check his phone first. He ate breakfast at home. It was a small change, but he felt different. He felt ready.\n\nMinh knows it takes time to build a new habit. But he is trying. One morning at a time."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Buổi sáng của Minh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Minh is not a morning person. His alarm goes off at seven, but he does not get up. He hits snooze three times. By seven thirty, he is still in bed.\n\nWhen Minh finally wakes up, he grabs his phone. He checks social media for ten minutes. This is a bad habit, but he does it every day.\n\nHe is not fully awake until he drinks coffee. He makes a strong cup and drinks it fast. Then he runs to the shower.\n\nMinh does not prepare anything the night before. His clothes are on the chair. His bag is on the floor. He cannot find his keys. Every morning is a small race.\n\nHe does not eat breakfast at home. He buys bread on the way to work. He eats while he rides his motorbike. This is not safe, but he is always late.\n\nHis commute is long. He sits in traffic for forty minutes. He feels tired and stressed before the day even starts.\n\nMinh wants to change. He wants to organize his mornings better. He wants to be more productive. He thinks a good routine can energize him.\n\nLast week, Minh tried something new. He set his alarm fifteen minutes earlier. He did not check his phone first. He ate breakfast at home. It was a small change, but he felt different. He felt ready.\n\nMinh knows it takes time to build a new habit. But he is trying. One morning at a time."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Thói quen và năng lượng",
                    "description": "Viết câu sử dụng từ vựng về thói quen và năng lượng buổi sáng.",
                    "data": {
                        "vocabList": ["habit", "awake", "prepare", "organize", "productive", "energize"],
                        "items": [
                            {
                                "targetVocab": "habit",
                                "prompt": "Hãy dùng từ 'habit' để viết một câu về một thói quen buổi sáng của bạn (tốt hoặc xấu). Ví dụ: Checking my phone in bed is a bad habit I want to change."
                            },
                            {
                                "targetVocab": "awake",
                                "prompt": "Hãy dùng từ 'awake' để viết một câu về lúc bạn tỉnh giấc. Ví dụ: I am usually fully awake after I drink my first cup of coffee."
                            },
                            {
                                "targetVocab": "prepare",
                                "prompt": "Hãy dùng từ 'prepare' để viết một câu về việc chuẩn bị buổi sáng. Ví dụ: I prepare my clothes and bag the night before to save time."
                            },
                            {
                                "targetVocab": "organize",
                                "prompt": "Hãy dùng từ 'organize' để viết một câu về cách bạn sắp xếp buổi sáng. Ví dụ: I organize my desk before I start working every day."
                            },
                            {
                                "targetVocab": "productive",
                                "prompt": "Hãy dùng từ 'productive' để viết một câu về hiệu quả làm việc. Ví dụ: I feel more productive when I wake up early and exercise."
                            },
                            {
                                "targetVocab": "energize",
                                "prompt": "Hãy dùng từ 'energize' để viết một câu về điều gì giúp bạn có năng lượng. Ví dụ: A morning walk in the park can energize you for the whole day."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 12 từ vựng — ôn lại tất cả trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã học xong 12 từ vựng về morning routines — thói quen buổi sáng. Hãy cùng ôn lại nhanh nhé.\n\nTrong phần 1, bạn đã học 6 từ cùng Lan: routine là thói quen hàng ngày — Lan có một morning routine rất ngăn nắp. Alarm là chuông báo thức — Lan chỉ cần nghe alarm một lần là dậy ngay. Breakfast là bữa sáng — Lan luôn ăn breakfast tại nhà. Shower là việc tắm — Lan tắm shower đầu tiên mỗi sáng. Commute là hành trình đi làm — Lan đi xe máy, commute mất khoảng hai mươi phút. Schedule là lịch trình — Lan kiểm tra schedule trước khi ra khỏi nhà.\n\nTrong phần 2, bạn đã học 6 từ cùng Minh: habit là thói quen — Minh có habit xem điện thoại ngay khi thức dậy. Awake là tỉnh giấc — Minh cần cà phê mới hoàn toàn awake. Prepare là chuẩn bị — Minh không prepare gì trước, nên sáng nào cũng vội. Organize là sắp xếp — Minh muốn organize buổi sáng tốt hơn. Productive là hiệu quả — một buổi sáng tốt giúp bạn productive cả ngày. Energize là tiếp năng lượng — Minh tìm cách energize bản thân mà không cần ba ly cà phê.\n\nBây giờ, bạn sẽ ôn lại tất cả 12 từ qua flashcard và bài tập viết. Sau đó, trong phần cuối, bạn sẽ đọc một bài tổng hợp về cả Lan và Minh. Sẵn sàng chưa? Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: routine, alarm, breakfast, shower, commute, schedule, habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule", "habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: routine, alarm, breakfast, shower, commute, schedule, habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule", "habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: routine, alarm, breakfast, shower, commute, schedule, habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule", "habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: routine, alarm, breakfast, shower, commute, schedule, habit, awake, prepare, organize, productive, energize",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule", "habit", "awake", "prepare", "organize", "productive", "energize"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập buổi sáng",
                    "description": "Viết câu ôn tập sử dụng tất cả 12 từ vựng về thói quen buổi sáng.",
                    "data": {
                        "vocabList": ["routine", "alarm", "breakfast", "shower", "commute", "schedule", "habit", "awake", "prepare", "organize", "productive", "energize"],
                        "items": [
                            {
                                "targetVocab": "routine",
                                "prompt": "Hãy dùng từ 'routine' để viết một câu so sánh thói quen buổi sáng của hai người. Ví dụ: Lan has a calm routine, but Minh's routine is always rushed."
                            },
                            {
                                "targetVocab": "alarm",
                                "prompt": "Hãy dùng từ 'alarm' để viết một câu về việc đặt báo thức. Ví dụ: If you set your alarm earlier, you will have more time in the morning."
                            },
                            {
                                "targetVocab": "breakfast",
                                "prompt": "Hãy dùng từ 'breakfast' để viết một câu về tầm quan trọng của bữa sáng. Ví dụ: Eating a healthy breakfast gives you energy for the whole morning."
                            },
                            {
                                "targetVocab": "shower",
                                "prompt": "Hãy dùng từ 'shower' để viết một câu về thói quen tắm buổi sáng. Ví dụ: A quick shower in the morning helps me feel fresh and ready."
                            },
                            {
                                "targetVocab": "commute",
                                "prompt": "Hãy dùng từ 'commute' để viết một câu về hành trình đi làm. Ví dụ: A long commute in traffic can make you feel tired before work starts."
                            },
                            {
                                "targetVocab": "schedule",
                                "prompt": "Hãy dùng từ 'schedule' để viết một câu về lịch trình hàng ngày. Ví dụ: Checking your schedule every morning helps you stay organized."
                            },
                            {
                                "targetVocab": "habit",
                                "prompt": "Hãy dùng từ 'habit' để viết một câu về một thói quen bạn muốn thay đổi. Ví dụ: I want to break the habit of looking at my phone first thing in the morning."
                            },
                            {
                                "targetVocab": "awake",
                                "prompt": "Hãy dùng từ 'awake' để viết một câu về cách bạn tỉnh táo buổi sáng. Ví dụ: I am not fully awake until I drink a glass of cold water."
                            },
                            {
                                "targetVocab": "prepare",
                                "prompt": "Hãy dùng từ 'prepare' để viết một câu về việc chuẩn bị từ tối hôm trước. Ví dụ: If you prepare your things at night, your morning will be much easier."
                            },
                            {
                                "targetVocab": "organize",
                                "prompt": "Hãy dùng từ 'organize' để viết một câu về cách sắp xếp buổi sáng. Ví dụ: I organize my morning into three parts — exercise, breakfast, and work."
                            },
                            {
                                "targetVocab": "productive",
                                "prompt": "Hãy dùng từ 'productive' để viết một câu về ngày làm việc hiệu quả. Ví dụ: People who wake up early are often more productive at work."
                            },
                            {
                                "targetVocab": "energize",
                                "prompt": "Hãy dùng từ 'energize' để viết một câu về điều gì tiếp thêm năng lượng cho bạn. Ví dụ: Listening to music in the morning can energize you for the day ahead."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc tổng hợp",
                    "description": "Giới thiệu bài đọc cuối cùng kết hợp câu chuyện của Lan và Minh.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của Easy English: Morning Routines! Bạn đã đi một chặng đường tuyệt vời. Trong phần 1, bạn học về buổi sáng ngăn nắp của Lan với 6 từ: routine, alarm, breakfast, shower, commute, schedule. Trong phần 2, bạn gặp Minh và buổi sáng hỗn loạn của anh ấy với 6 từ: habit, awake, prepare, organize, productive, energize. Trong phần ôn tập, bạn đã luyện lại tất cả 12 từ.\n\nBây giờ, bạn sẽ đọc một bài tổng hợp — Lan và Minh ngồi uống cà phê và nói chuyện về buổi sáng của họ. Bài đọc này dùng tất cả 12 từ vựng bạn đã học. Hãy đọc chậm, chú ý từng từ, và thưởng thức câu chuyện nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Lan và Minh nói về buổi sáng",
                    "description": "Lan and Minh sit down for coffee and compare their very different mornings.",
                    "data": {
                        "text": "It is Saturday afternoon. Lan and Minh sit at a small coffee shop near their office. They are talking about mornings.\n\n'I love my morning routine,' Lan says. 'I wake up at six. My alarm rings once, and I get up right away. I take a shower, eat breakfast, check my schedule, and leave the house by seven thirty. It is the same every day.'\n\nMinh laughs. 'My morning is very different. My alarm goes off at seven, but I hit snooze three times. I am not awake until I drink coffee. I do not eat breakfast at home. I buy bread on the way to work.'\n\n'That sounds stressful,' Lan says.\n\n'It is,' Minh agrees. 'I never prepare anything the night before. My clothes are everywhere. I cannot find my keys. My commute takes forty minutes because I leave late and sit in traffic.'\n\nLan nods. 'My commute is only twenty minutes. I think it is because I leave early. I organize everything before I go to bed. I pick my clothes, pack my bag, and set my alarm.'\n\n'I want to change my habits,' Minh says. 'Last week, I tried waking up fifteen minutes earlier. I did not check my phone first. I ate breakfast at home. It was a small change, but I felt more productive.'\n\n'That is great!' Lan says. 'Small habits make a big difference. When I started my routine two years ago, I also started small. Just one thing at a time.'\n\n'What energizes you in the morning?' Minh asks.\n\n'My shower,' Lan says. 'The warm water wakes me up. And breakfast — I feel strong after I eat. What about you?'\n\n'Coffee,' Minh says with a smile. 'But I want to find something better. Maybe exercise. Maybe a walk. Something to energize me without three cups of coffee.'\n\n'You should try it,' Lan says. 'A good morning routine can change your whole day. You feel calm. You feel ready. You feel like you can do anything.'\n\nMinh takes a sip of his coffee. 'Okay,' he says. 'Starting Monday, I will organize my mornings. I will prepare my things at night. I will wake up when my alarm rings — no snooze. I will eat breakfast at home.'\n\n'And check your schedule before you leave?' Lan adds.\n\n'Yes,' Minh says. 'And check my schedule. One step at a time.'\n\nThey both smile. A good morning starts with a good plan."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Lan và Minh nói về buổi sáng",
                    "description": "Lan and Minh sit down for coffee and compare their very different mornings.",
                    "data": {
                        "text": "It is Saturday afternoon. Lan and Minh sit at a small coffee shop near their office. They are talking about mornings.\n\n'I love my morning routine,' Lan says. 'I wake up at six. My alarm rings once, and I get up right away. I take a shower, eat breakfast, check my schedule, and leave the house by seven thirty. It is the same every day.'\n\nMinh laughs. 'My morning is very different. My alarm goes off at seven, but I hit snooze three times. I am not awake until I drink coffee. I do not eat breakfast at home. I buy bread on the way to work.'\n\n'That sounds stressful,' Lan says.\n\n'It is,' Minh agrees. 'I never prepare anything the night before. My clothes are everywhere. I cannot find my keys. My commute takes forty minutes because I leave late and sit in traffic.'\n\nLan nods. 'My commute is only twenty minutes. I think it is because I leave early. I organize everything before I go to bed. I pick my clothes, pack my bag, and set my alarm.'\n\n'I want to change my habits,' Minh says. 'Last week, I tried waking up fifteen minutes earlier. I did not check my phone first. I ate breakfast at home. It was a small change, but I felt more productive.'\n\n'That is great!' Lan says. 'Small habits make a big difference. When I started my routine two years ago, I also started small. Just one thing at a time.'\n\n'What energizes you in the morning?' Minh asks.\n\n'My shower,' Lan says. 'The warm water wakes me up. And breakfast — I feel strong after I eat. What about you?'\n\n'Coffee,' Minh says with a smile. 'But I want to find something better. Maybe exercise. Maybe a walk. Something to energize me without three cups of coffee.'\n\n'You should try it,' Lan says. 'A good morning routine can change your whole day. You feel calm. You feel ready. You feel like you can do anything.'\n\nMinh takes a sip of his coffee. 'Okay,' he says. 'Starting Monday, I will organize my mornings. I will prepare my things at night. I will wake up when my alarm rings — no snooze. I will eat breakfast at home.'\n\n'And check your schedule before you leave?' Lan adds.\n\n'Yes,' Minh says. 'And check my schedule. One step at a time.'\n\nThey both smile. A good morning starts with a good plan."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Lan và Minh nói về buổi sáng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "It is Saturday afternoon. Lan and Minh sit at a small coffee shop near their office. They are talking about mornings.\n\n'I love my morning routine,' Lan says. 'I wake up at six. My alarm rings once, and I get up right away. I take a shower, eat breakfast, check my schedule, and leave the house by seven thirty. It is the same every day.'\n\nMinh laughs. 'My morning is very different. My alarm goes off at seven, but I hit snooze three times. I am not awake until I drink coffee. I do not eat breakfast at home. I buy bread on the way to work.'\n\n'That sounds stressful,' Lan says.\n\n'It is,' Minh agrees. 'I never prepare anything the night before. My clothes are everywhere. I cannot find my keys. My commute takes forty minutes because I leave late and sit in traffic.'\n\nLan nods. 'My commute is only twenty minutes. I think it is because I leave early. I organize everything before I go to bed. I pick my clothes, pack my bag, and set my alarm.'\n\n'I want to change my habits,' Minh says. 'Last week, I tried waking up fifteen minutes earlier. I did not check my phone first. I ate breakfast at home. It was a small change, but I felt more productive.'\n\n'That is great!' Lan says. 'Small habits make a big difference. When I started my routine two years ago, I also started small. Just one thing at a time.'\n\n'What energizes you in the morning?' Minh asks.\n\n'My shower,' Lan says. 'The warm water wakes me up. And breakfast — I feel strong after I eat. What about you?'\n\n'Coffee,' Minh says with a smile. 'But I want to find something better. Maybe exercise. Maybe a walk. Something to energize me without three cups of coffee.'\n\n'You should try it,' Lan says. 'A good morning routine can change your whole day. You feel calm. You feel ready. You feel like you can do anything.'\n\nMinh takes a sip of his coffee. 'Okay,' he says. 'Starting Monday, I will organize my mornings. I will prepare my things at night. I will wake up when my alarm rings — no snooze. I will eat breakfast at home.'\n\n'And check your schedule before you leave?' Lan adds.\n\n'Yes,' Minh says. 'And check my schedule. One step at a time.'\n\nThey both smile. A good morning starts with a good plan."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay ấm áp — farewell tone: introspective_guide.",
                    "data": {
                        "text": "Bạn đã hoàn thành Easy English: Morning Routines. Hãy dừng lại một chút và nhìn lại hành trình bạn vừa đi qua.\n\nBạn bắt đầu với buổi sáng của Lan — một người phụ nữ biết chính xác mình muốn gì mỗi sáng. Rồi bạn gặp Minh — một người đang cố gắng thay đổi, từng bước nhỏ một. Và qua câu chuyện của họ, bạn đã học được 12 từ vựng tiếng Anh quan trọng.\n\nHãy cùng ôn lại nhé.\n\nRoutine — thói quen hàng ngày. Mỗi người có một routine khác nhau. Câu mới: Building a morning routine takes patience, but it is worth the effort.\n\nAlarm — chuông báo thức. Alarm đánh thức bạn, nhưng bạn chọn có dậy hay không. Câu mới: Some people need two alarms, but one alarm is enough if you go to bed early.\n\nBreakfast — bữa sáng. Breakfast cho bạn năng lượng để bắt đầu ngày mới. Câu mới: A simple breakfast of fruit and toast can make a big difference in how you feel.\n\nShower — việc tắm. Shower giúp bạn tỉnh táo và sẵn sàng. Câu mới: Whether you prefer a hot shower or a cold one, it is a great way to start the day.\n\nCommute — hành trình đi làm. Commute có thể là thời gian lãng phí, hoặc thời gian học hỏi. Câu mới: Many people use their commute to listen to podcasts or audiobooks.\n\nSchedule — lịch trình. Schedule giúp bạn biết mình đang đi đâu. Câu mới: Writing your schedule on paper can help you remember things better than using your phone.\n\nBây giờ, tôi muốn bạn nghĩ về buổi sáng của chính mình. Bạn giống Lan hay giống Minh? Hay bạn ở đâu đó giữa hai người? Không có câu trả lời đúng hay sai. Điều quan trọng là bạn nhận ra buổi sáng của mình trông như thế nào — và bạn muốn nó trông như thế nào.\n\nHabit — thói quen. Mỗi thói quen nhỏ tạo nên con người bạn. Câu mới: Reading for ten minutes every morning is a habit that can change your life.\n\nAwake — tỉnh giấc. Awake không chỉ là mở mắt — mà là thực sự sẵn sàng. Câu mới: Being awake means your mind is clear and your body is ready to move.\n\nPrepare — chuẩn bị. Prepare hôm nay để ngày mai dễ dàng hơn. Câu mới: The best way to prepare for a busy day is to plan the night before.\n\nOrganize — sắp xếp. Organize không phải là hoàn hảo — mà là biết mọi thứ ở đâu. Câu mới: When you organize your space, you also organize your thoughts.\n\nProductive — hiệu quả. Productive không phải là làm nhiều — mà là làm đúng việc. Câu mới: You do not need to work twelve hours to be productive — you just need a clear plan.\n\nEnergize — tiếp năng lượng. Energize bản thân bằng những điều đơn giản. Câu mới: Fresh air and sunlight can energize you more than any cup of coffee.\n\nBạn đã học 12 từ. Bạn đã đọc về Lan và Minh. Bạn đã viết những câu của riêng mình. Nhưng điều quan trọng nhất không phải là từ vựng — mà là câu hỏi bạn mang theo sau bài học này: Ngày mai sáng dậy, mình sẽ làm gì đầu tiên?\n\nCảm ơn bạn đã học cùng tôi. Hẹn gặp lại bạn trong bài học tiếp theo. Chúc bạn có những buổi sáng thật đẹp!"
                    }
                }
            ]
        }
    ]
}

# ── Validate ──
print("Validating content...")
validate_balanced_skills_beginner(content)
print("  ✓ balanced_skills_beginner structure OK")
validate_content_type_tags(content)
print("  ✓ contentTypeTags OK")
validate_bilingual_prompts(content, "beginner")
print("  ✓ bilingual prompts OK")
print("All validations passed!\n")

# ── Upload ──
token = get_firebase_id_token(UID)
resp = requests.post(
    f"{API_BASE}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
resp.raise_for_status()
data = resp.json()
curriculum_id = data.get("id") or data.get("curriculum", {}).get("id")
print(f"Created curriculum: {curriculum_id}")
print(f"Title: {content['title']}")
print(f"Level: beginner | Skill: balanced_skills | Content: podcast")
print(f"Words: 12 (2 groups of 6)")
