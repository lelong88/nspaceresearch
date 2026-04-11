import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from firebase_token import get_firebase_id_token
from validate_curriculum import (
    validate_balanced_skills_standard,
    validate_content_type_tags,
    validate_bilingual_prompts,
)

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Curriculum #43: TED-Ed: Why We Sleep
# Level: preintermediate | Skill focus: balanced_skills | Content type: ["podcast"]
# Topic: Psychology | 18 words (3 groups of 6), 5 sessions, bilingual (vi-en)
# Description tone: bold_declaration (different from previous podcast tones: provocative_question, empathetic_observation)
# Farewell tone: team_building_energy (different from previous: introspective_guide, warm_accountability)
# W1: insomnia, drowsy, circadian, melatonin, fatigue, nap
# W2: restless, subconscious, dream, cognitive, deprive, rejuvenate
# W3: cycle, alert, hormone, therapy, anxiety, rem

content = {
    "title": "TED-Ed: Why We Sleep",
    "contentTypeTags": ["podcast"],
    "description": "GIẤC NGỦ KHÔNG PHẢI LÀ NGHỈ NGƠI — MÀ LÀ CỖ MÁY TÁI TẠO MẠNH MẼ NHẤT CƠ THỂ BẠN.\n\nMỗi đêm, khi bạn nhắm mắt, não bộ bắt đầu một ca làm việc phi thường: sắp xếp ký ức, sửa chữa tế bào, cân bằng cảm xúc. Nhưng nếu bạn thức khuya xem điện thoại, uống cà phê lúc 4 giờ chiều, hay nằm trằn trọc đếm cừu — bạn đang phá hoại chính cỗ máy đó mà không hề biết.\n\nHãy tưởng tượng cơ thể bạn như một nhà máy hoạt động 24/7. Ban ngày, nhà máy sản xuất năng lượng. Ban đêm, đội bảo trì vào làm việc — dọn dẹp, sửa chữa, nâng cấp. Nếu bạn không cho đội bảo trì đủ thời gian, nhà máy sẽ xuống cấp dần dần — và một ngày, nó sẽ ngừng hoạt động.\n\nHai nhân vật Linh và Đức sẽ dẫn bạn vào thế giới khoa học giấc ngủ — từ nhịp sinh học circadian đến hormone melatonin, từ giấc mơ REM đến liệu pháp chữa mất ngủ. Bạn sẽ hiểu tại sao giấc ngủ trưa có sức mạnh kỳ diệu, và tại sao thiếu ngủ ảnh hưởng đến trí nhớ, cảm xúc, và khả năng tư duy.\n\n18 từ vựng trong bài học này — từ insomnia đến rem — sẽ giúp bạn nói về giấc ngủ bằng tiếng Anh một cách tự tin, vừa hiểu sâu hơn về cơ thể mình, vừa nâng trình ngoại ngữ qua khoa học thực sự hấp dẫn.",
    "preview": {
        "text": "What happens inside your brain during the eight hours you spend asleep — and what goes wrong when you do not get enough? In this podcast-inspired lesson, you will learn 18 English words about sleep science and psychology: insomnia, drowsy, circadian, melatonin, fatigue, nap, restless, subconscious, dream, cognitive, deprive, rejuvenate, cycle, alert, hormone, therapy, anxiety, and rem. Follow Linh and Đức as they discuss why humans sleep, what dreams really mean, and how modern life disrupts our natural rhythms. Linh is fascinated by the science behind sleep cycles and shares research from TED-Ed, while Đức struggles with late nights and wants to fix his sleep habits. Through three conversational reading passages, a full review session, and a final combined reading, you will explore circadian rhythms, the power of naps, REM sleep, and cognitive restoration. By the end, you will be able to discuss sleep science, describe sleep problems, and explain why rest is essential for both body and mind — all in English."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng — Giấc ngủ và khoa học",
                    "description": "Giới thiệu chủ đề giấc ngủ và tổng quan bài học.",
                    "data": {
                        "text": "Chào mừng bạn đến với TED-Ed: Why We Sleep — bài học podcast tiếng Anh về một trong những bí ẩn lớn nhất của cơ thể con người: giấc ngủ. Bạn có bao giờ tự hỏi tại sao chúng ta dành gần một phần ba cuộc đời để ngủ không? Tại sao khi thiếu ngủ, bạn cảm thấy mệt mỏi, khó tập trung, và dễ cáu gắt? Khoa học đã có câu trả lời — và hôm nay, bạn sẽ học cách nói về những điều đó bằng tiếng Anh.\n\nBài học này có 18 từ vựng chia thành 3 phần. Trong phần 1, bạn sẽ học 6 từ đầu tiên: insomnia, drowsy, circadian, melatonin, fatigue, và nap. Đây là những từ cơ bản nhất khi nói về giấc ngủ và nhịp sinh học."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Dạy 6 từ vựng: insomnia, drowsy, circadian, melatonin, fatigue, nap.",
                    "data": {
                        "text": "Hãy cùng tìm hiểu 6 từ vựng đầu tiên nhé.\n\nTừ đầu tiên là insomnia — danh từ — nghĩa là chứng mất ngủ. Insomnia là khi bạn muốn ngủ nhưng không thể — bạn nằm trên giường hàng giờ mà mắt vẫn mở. Ví dụ: 'Many students suffer from insomnia during exam season.' Trong bài đọc, Đức kể rằng anh ấy thường bị insomnia vì xem điện thoại quá khuya.\n\nTừ thứ hai là drowsy — tính từ — nghĩa là buồn ngủ, lờ đờ. Drowsy là cảm giác khi mắt bạn nặng trĩu và bạn muốn ngủ ngay lập tức. Ví dụ: 'I always feel drowsy after lunch.' Trong bài đọc, Linh giải thích tại sao nhiều người cảm thấy drowsy vào buổi chiều — đó là do nhịp sinh học tự nhiên.\n\nTừ thứ ba là circadian — tính từ — nghĩa là thuộc về nhịp sinh học 24 giờ. Circadian rhythm là đồng hồ sinh học bên trong cơ thể bạn, điều khiển khi nào bạn buồn ngủ và khi nào bạn tỉnh táo. Ví dụ: 'Your circadian rhythm tells your body when to sleep and when to wake up.' Trong bài đọc, Linh nói rằng ánh sáng xanh từ điện thoại có thể phá vỡ circadian rhythm.\n\nTừ thứ tư là melatonin — danh từ — nghĩa là melatonin, hormone giấc ngủ. Melatonin là chất hóa học mà não bộ tiết ra khi trời tối để báo hiệu cơ thể rằng đã đến giờ ngủ. Ví dụ: 'Your brain produces melatonin when it gets dark outside.' Trong bài đọc, Linh giải thích rằng ánh sáng nhân tạo làm giảm sản xuất melatonin.\n\nTừ thứ năm là fatigue — danh từ — nghĩa là sự mệt mỏi, kiệt sức. Fatigue không chỉ là buồn ngủ — mà là cảm giác cơ thể và tinh thần đều cạn kiệt năng lượng. Ví dụ: 'After working twelve hours, she felt extreme fatigue.' Trong bài đọc, Đức mô tả cảm giác fatigue sau nhiều đêm thiếu ngủ liên tiếp.\n\nTừ cuối cùng là nap — danh từ và động từ — nghĩa là giấc ngủ ngắn, ngủ trưa. Nap là khi bạn ngủ một lúc ngắn trong ngày, thường từ 15 đến 30 phút. Ví dụ: 'A short nap in the afternoon can improve your focus.' Trong bài đọc, Linh chia sẻ nghiên cứu cho thấy một giấc nap ngắn có thể cải thiện trí nhớ đáng kể.\n\nSáu từ đầu tiên đã sẵn sàng! Hãy bắt đầu với flashcard, rồi đọc cuộc trò chuyện giữa Linh và Đức về khoa học giấc ngủ nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Giấc ngủ và nhịp sinh học",
                    "description": "Học 6 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Giấc ngủ và nhịp sinh học",
                    "description": "Học 6 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Giấc ngủ và nhịp sinh học",
                    "description": "Học 6 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Giấc ngủ và nhịp sinh học",
                    "description": "Học 6 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 1",
                    "description": "Giới thiệu ngữ pháp và cách dùng từ vựng trong ngữ cảnh bài đọc.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc cuộc trò chuyện giữa Linh và Đức. Linh rất thích khoa học và hay đọc các bài TED-Ed. Đức thì thường thức khuya và muốn cải thiện giấc ngủ. Trong bài đọc này, họ nói về nhịp sinh học, melatonin, và tại sao giấc ngủ trưa lại quan trọng. Hãy chú ý cách các từ insomnia, drowsy, circadian, melatonin, fatigue, và nap được dùng trong câu chuyện nhé. Một điểm ngữ pháp quan trọng: khi nói về thói quen và sự thật khoa học, chúng ta dùng thì hiện tại đơn — ví dụ 'melatonin helps you fall asleep' hoặc 'the circadian rhythm controls your sleep cycle.' Hãy đọc chậm và thưởng thức nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tại sao chúng ta cần ngủ?",
                    "description": "Linh and Đức discuss sleep science, circadian rhythms, and the power of naps.",
                    "data": {
                        "text": "Linh and Đức are sitting in a coffee shop after work. Đức looks tired. His eyes are half closed and he keeps yawning.\n\n'You look drowsy,' Linh says. 'Did you sleep well last night?'\n\n'Not really,' Đức says. 'I watched videos on my phone until two in the morning. Then I could not fall asleep. I think I have insomnia.'\n\nLinh shakes her head. 'That is not insomnia — that is a bad habit. Real insomnia is when you try to sleep but your brain will not let you. What you have is a screen problem.'\n\n'What do you mean?' Đức asks.\n\n'I watched a TED-Ed video about this,' Linh says. 'Your body has something called a circadian rhythm. It is like an internal clock. When the sun goes down, your brain starts making melatonin — a hormone that makes you feel sleepy. But when you look at your phone screen, the blue light tricks your brain into thinking it is still daytime. So your brain stops making melatonin.'\n\n'That explains a lot,' Đức says. 'I never feel sleepy when I am on my phone. But then I feel terrible in the morning.'\n\n'Exactly,' Linh says. 'And when you do not sleep enough, you build up fatigue. Not just feeling tired for one day — but deep exhaustion that affects your memory, your mood, and your ability to think clearly.'\n\nĐức takes a sip of his coffee. 'So what should I do?'\n\n'First, stop looking at your phone one hour before bed,' Linh says. 'Let your circadian rhythm do its job. Second, try taking a short nap in the afternoon. Research shows that a twenty-minute nap can improve your focus and energy for the rest of the day.'\n\n'A nap? At work?' Đức laughs.\n\n'Many companies in Japan and some in Vietnam now have nap rooms,' Linh says. 'A nap is not lazy — it is smart. Your brain needs rest to work well.'\n\nĐức thinks about this. 'Maybe I will try it. No phone after eleven, and a short nap after lunch.'\n\n'Good plan,' Linh says. 'Your body will thank you.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tại sao chúng ta cần ngủ?",
                    "description": "Linh and Đức discuss sleep science, circadian rhythms, and the power of naps.",
                    "data": {
                        "text": "Linh and Đức are sitting in a coffee shop after work. Đức looks tired. His eyes are half closed and he keeps yawning.\n\n'You look drowsy,' Linh says. 'Did you sleep well last night?'\n\n'Not really,' Đức says. 'I watched videos on my phone until two in the morning. Then I could not fall asleep. I think I have insomnia.'\n\nLinh shakes her head. 'That is not insomnia — that is a bad habit. Real insomnia is when you try to sleep but your brain will not let you. What you have is a screen problem.'\n\n'What do you mean?' Đức asks.\n\n'I watched a TED-Ed video about this,' Linh says. 'Your body has something called a circadian rhythm. It is like an internal clock. When the sun goes down, your brain starts making melatonin — a hormone that makes you feel sleepy. But when you look at your phone screen, the blue light tricks your brain into thinking it is still daytime. So your brain stops making melatonin.'\n\n'That explains a lot,' Đức says. 'I never feel sleepy when I am on my phone. But then I feel terrible in the morning.'\n\n'Exactly,' Linh says. 'And when you do not sleep enough, you build up fatigue. Not just feeling tired for one day — but deep exhaustion that affects your memory, your mood, and your ability to think clearly.'\n\nĐức takes a sip of his coffee. 'So what should I do?'\n\n'First, stop looking at your phone one hour before bed,' Linh says. 'Let your circadian rhythm do its job. Second, try taking a short nap in the afternoon. Research shows that a twenty-minute nap can improve your focus and energy for the rest of the day.'\n\n'A nap? At work?' Đức laughs.\n\n'Many companies in Japan and some in Vietnam now have nap rooms,' Linh says. 'A nap is not lazy — it is smart. Your brain needs rest to work well.'\n\nĐức thinks about this. 'Maybe I will try it. No phone after eleven, and a short nap after lunch.'\n\n'Good plan,' Linh says. 'Your body will thank you.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tại sao chúng ta cần ngủ?",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Linh and Đức are sitting in a coffee shop after work. Đức looks tired. His eyes are half closed and he keeps yawning.\n\n'You look drowsy,' Linh says. 'Did you sleep well last night?'\n\n'Not really,' Đức says. 'I watched videos on my phone until two in the morning. Then I could not fall asleep. I think I have insomnia.'\n\nLinh shakes her head. 'That is not insomnia — that is a bad habit. Real insomnia is when you try to sleep but your brain will not let you. What you have is a screen problem.'\n\n'What do you mean?' Đức asks.\n\n'I watched a TED-Ed video about this,' Linh says. 'Your body has something called a circadian rhythm. It is like an internal clock. When the sun goes down, your brain starts making melatonin — a hormone that makes you feel sleepy. But when you look at your phone screen, the blue light tricks your brain into thinking it is still daytime. So your brain stops making melatonin.'\n\n'That explains a lot,' Đức says. 'I never feel sleepy when I am on my phone. But then I feel terrible in the morning.'\n\n'Exactly,' Linh says. 'And when you do not sleep enough, you build up fatigue. Not just feeling tired for one day — but deep exhaustion that affects your memory, your mood, and your ability to think clearly.'\n\nĐức takes a sip of his coffee. 'So what should I do?'\n\n'First, stop looking at your phone one hour before bed,' Linh says. 'Let your circadian rhythm do its job. Second, try taking a short nap in the afternoon. Research shows that a twenty-minute nap can improve your focus and energy for the rest of the day.'\n\n'A nap? At work?' Đức laughs.\n\n'Many companies in Japan and some in Vietnam now have nap rooms,' Linh says. 'A nap is not lazy — it is smart. Your brain needs rest to work well.'\n\nĐức thinks about this. 'Maybe I will try it. No phone after eleven, and a short nap after lunch.'\n\n'Good plan,' Linh says. 'Your body will thank you.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Giấc ngủ và nhịp sinh học",
                    "description": "Viết câu sử dụng từ vựng về giấc ngủ, mệt mỏi, và nhịp sinh học.",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap"],
                        "items": [
                            {
                                "targetVocab": "insomnia",
                                "prompt": "Hãy dùng từ 'insomnia' để viết một câu về việc khó ngủ. Ví dụ: My friend suffers from insomnia and often stays awake until three in the morning."
                            },
                            {
                                "targetVocab": "drowsy",
                                "prompt": "Hãy dùng từ 'drowsy' để viết một câu về cảm giác buồn ngủ. Ví dụ: I always feel drowsy after eating a big lunch at the office."
                            },
                            {
                                "targetVocab": "circadian",
                                "prompt": "Hãy dùng từ 'circadian' để viết một câu về nhịp sinh học. Ví dụ: Traveling across time zones can disrupt your circadian rhythm for several days."
                            },
                            {
                                "targetVocab": "melatonin",
                                "prompt": "Hãy dùng từ 'melatonin' để viết một câu về hormone giấc ngủ. Ví dụ: Your brain releases melatonin when the lights go dim in the evening."
                            },
                            {
                                "targetVocab": "fatigue",
                                "prompt": "Hãy dùng từ 'fatigue' để viết một câu về sự mệt mỏi. Ví dụ: After three nights of poor sleep, the fatigue made it hard to concentrate at work."
                            },
                            {
                                "targetVocab": "nap",
                                "prompt": "Hãy dùng từ 'nap' để viết một câu về giấc ngủ trưa. Ví dụ: A twenty-minute nap after lunch helps me feel refreshed for the afternoon."
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
                    "title": "Chào mừng phần 2 — Giấc mơ và tiềm thức",
                    "description": "Ôn lại phần 1 và giới thiệu chủ đề giấc mơ.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với phần 2 của TED-Ed: Why We Sleep! Trong phần trước, bạn đã học 6 từ vựng về giấc ngủ cơ bản: insomnia là chứng mất ngủ — khi bạn muốn ngủ nhưng không thể. Drowsy là buồn ngủ, lờ đờ — cảm giác mắt nặng trĩu. Circadian là thuộc về nhịp sinh học 24 giờ — đồng hồ bên trong cơ thể bạn. Melatonin là hormone giấc ngủ — não tiết ra khi trời tối. Fatigue là sự mệt mỏi sâu — không chỉ buồn ngủ mà là kiệt sức. Và nap là giấc ngủ ngắn — 15 đến 30 phút giúp bạn tỉnh táo hơn.\n\nBạn cũng đã đọc cuộc trò chuyện giữa Linh và Đức — Linh giải thích tại sao ánh sáng xanh từ điện thoại phá vỡ nhịp circadian, và Đức quyết định thử ngủ trưa.\n\nBây giờ, chúng ta sẽ đi sâu hơn vào thế giới giấc ngủ — cụ thể là giấc mơ và những gì xảy ra trong tiềm thức khi bạn ngủ. Bạn sẽ học 6 từ mới: restless, subconscious, dream, cognitive, deprive, và rejuvenate."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Dạy 6 từ vựng: restless, subconscious, dream, cognitive, deprive, rejuvenate.",
                    "data": {
                        "text": "Hãy cùng học 6 từ mới nhé.\n\nTừ đầu tiên là restless — tính từ — nghĩa là bồn chồn, không yên. Restless là khi bạn không thể nằm yên — bạn cứ trở mình, thay đổi tư thế, và không tìm được sự thoải mái. Ví dụ: 'He had a restless night and woke up feeling worse than before.' Trong bài đọc, Đức kể rằng anh ấy có nhiều đêm restless khi lo lắng về công việc.\n\nTừ thứ hai là subconscious — danh từ và tính từ — nghĩa là tiềm thức. Subconscious là phần tâm trí hoạt động mà bạn không nhận biết — nó lưu trữ ký ức, cảm xúc, và suy nghĩ ẩn sâu. Ví dụ: 'Dreams often reveal what is hidden in your subconscious.' Trong bài đọc, Linh giải thích rằng giấc mơ là cách subconscious xử lý những trải nghiệm trong ngày.\n\nTừ thứ ba là dream — danh từ và động từ — nghĩa là giấc mơ, mơ. Dream là những hình ảnh, câu chuyện, và cảm xúc mà bạn trải nghiệm khi ngủ. Ví dụ: 'I had a strange dream about flying over the ocean last night.' Trong bài đọc, Đức kể về một giấc dream lặp đi lặp lại mà anh ấy không hiểu ý nghĩa.\n\nTừ thứ tư là cognitive — tính từ — nghĩa là thuộc về nhận thức, tư duy. Cognitive liên quan đến khả năng suy nghĩ, học hỏi, ghi nhớ, và giải quyết vấn đề của não bộ. Ví dụ: 'Sleep deprivation has a serious impact on cognitive performance.' Trong bài đọc, Linh nói rằng thiếu ngủ làm giảm cognitive function — khả năng tập trung và ra quyết định.\n\nTừ thứ năm là deprive — động từ — nghĩa là tước đoạt, làm thiếu hụt. Deprive là khi bạn không được nhận đủ thứ gì đó mà bạn cần — trong ngữ cảnh giấc ngủ, sleep-deprived nghĩa là thiếu ngủ. Ví dụ: 'If you deprive your body of sleep, your health will suffer.' Trong bài đọc, Linh cảnh báo rằng khi bạn deprive não bộ khỏi giấc ngủ, trí nhớ và cảm xúc đều bị ảnh hưởng.\n\nTừ cuối cùng là rejuvenate — động từ — nghĩa là tái tạo, làm trẻ lại. Rejuvenate là khi cơ thể hoặc tinh thần được phục hồi và trở nên tươi mới. Ví dụ: 'A good night of sleep can rejuvenate both your body and your mind.' Trong bài đọc, Linh giải thích rằng giấc ngủ sâu giúp rejuvenate tế bào não và cải thiện tâm trạng.\n\nSáu từ mới đã sẵn sàng! Hãy luyện flashcard rồi đọc về giấc mơ và tiềm thức nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Giấc mơ và tiềm thức",
                    "description": "Học 6 từ: restless, subconscious, dream, cognitive, deprive, rejuvenate",
                    "data": {
                        "vocabList": ["restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Giấc mơ và tiềm thức",
                    "description": "Học 6 từ: restless, subconscious, dream, cognitive, deprive, rejuvenate",
                    "data": {
                        "vocabList": ["restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Giấc mơ và tiềm thức",
                    "description": "Học 6 từ: restless, subconscious, dream, cognitive, deprive, rejuvenate",
                    "data": {
                        "vocabList": ["restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Giấc mơ và tiềm thức",
                    "description": "Học 6 từ: restless, subconscious, dream, cognitive, deprive, rejuvenate",
                    "data": {
                        "vocabList": ["restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 2",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về giấc mơ.",
                    "data": {
                        "text": "Bạn đã luyện xong flashcard rồi! Bây giờ hãy đọc cuộc trò chuyện tiếp theo giữa Linh và Đức. Lần này, họ nói về giấc mơ — tại sao chúng ta mơ, giấc mơ có ý nghĩa gì, và điều gì xảy ra khi não bộ bị thiếu ngủ. Hãy chú ý cách các từ restless, subconscious, dream, cognitive, deprive, và rejuvenate xuất hiện trong câu chuyện. Một điểm ngữ pháp: khi nói về hậu quả của việc thiếu ngủ, chúng ta thường dùng cấu trúc 'if you deprive... you will...' hoặc 'when you are deprived of... your brain cannot...' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Giấc mơ nói gì về bạn?",
                    "description": "Linh and Đức explore dreams, the subconscious mind, and cognitive effects of sleep loss.",
                    "data": {
                        "text": "A few days later, Linh and Đức meet again. This time, Đức has a question.\n\n'I had a strange dream last night,' he says. 'I was running through a forest, but I could not find the way out. I kept running and running. What does it mean?'\n\nLinh smiles. 'Dreams are fascinating. Scientists believe that dreams come from your subconscious — the part of your mind that works even when you are not aware of it. Your subconscious stores memories, feelings, and worries. When you sleep, it processes all of that through dreams.'\n\n'So my dream about the forest means I am worried about something?' Đức asks.\n\n'Maybe,' Linh says. 'Running and not finding a way out could mean you feel stuck in some area of your life. But dream interpretation is not exact science. The important thing is that dreaming is healthy. It means your brain is doing its job.'\n\n'I also had a restless night last week,' Đức says. 'I kept waking up every hour. I felt terrible the next day — I could not focus on anything at work.'\n\n'That makes sense,' Linh says. 'When you have a restless night, your brain does not get enough deep sleep. Deep sleep is when your brain does its most important work — it cleans out waste, strengthens memories, and rejuvenates your neurons. Without it, your cognitive abilities drop significantly.'\n\n'Cognitive abilities?' Đức asks.\n\n'Your ability to think, remember, and make decisions,' Linh explains. 'Studies show that if you deprive someone of sleep for just one night, their cognitive performance drops by twenty to thirty percent. That is like being slightly drunk.'\n\nĐức looks shocked. 'That bad?'\n\n'Yes,' Linh says. 'And it gets worse over time. Chronic sleep deprivation — when you consistently deprive your body of enough rest — can lead to serious health problems. But the good news is that your brain can rejuvenate quickly. Even two or three nights of good sleep can restore much of your cognitive function.'\n\n'So sleep is like charging a battery,' Đức says.\n\n'Exactly,' Linh says. 'And dreams are like the software updates that happen while you charge.'\n\nĐức laughs. 'I like that. I will try to let my brain finish its updates tonight.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Giấc mơ nói gì về bạn?",
                    "description": "Linh and Đức explore dreams, the subconscious mind, and cognitive effects of sleep loss.",
                    "data": {
                        "text": "A few days later, Linh and Đức meet again. This time, Đức has a question.\n\n'I had a strange dream last night,' he says. 'I was running through a forest, but I could not find the way out. I kept running and running. What does it mean?'\n\nLinh smiles. 'Dreams are fascinating. Scientists believe that dreams come from your subconscious — the part of your mind that works even when you are not aware of it. Your subconscious stores memories, feelings, and worries. When you sleep, it processes all of that through dreams.'\n\n'So my dream about the forest means I am worried about something?' Đức asks.\n\n'Maybe,' Linh says. 'Running and not finding a way out could mean you feel stuck in some area of your life. But dream interpretation is not exact science. The important thing is that dreaming is healthy. It means your brain is doing its job.'\n\n'I also had a restless night last week,' Đức says. 'I kept waking up every hour. I felt terrible the next day — I could not focus on anything at work.'\n\n'That makes sense,' Linh says. 'When you have a restless night, your brain does not get enough deep sleep. Deep sleep is when your brain does its most important work — it cleans out waste, strengthens memories, and rejuvenates your neurons. Without it, your cognitive abilities drop significantly.'\n\n'Cognitive abilities?' Đức asks.\n\n'Your ability to think, remember, and make decisions,' Linh explains. 'Studies show that if you deprive someone of sleep for just one night, their cognitive performance drops by twenty to thirty percent. That is like being slightly drunk.'\n\nĐức looks shocked. 'That bad?'\n\n'Yes,' Linh says. 'And it gets worse over time. Chronic sleep deprivation — when you consistently deprive your body of enough rest — can lead to serious health problems. But the good news is that your brain can rejuvenate quickly. Even two or three nights of good sleep can restore much of your cognitive function.'\n\n'So sleep is like charging a battery,' Đức says.\n\n'Exactly,' Linh says. 'And dreams are like the software updates that happen while you charge.'\n\nĐức laughs. 'I like that. I will try to let my brain finish its updates tonight.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Giấc mơ nói gì về bạn?",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "A few days later, Linh and Đức meet again. This time, Đức has a question.\n\n'I had a strange dream last night,' he says. 'I was running through a forest, but I could not find the way out. I kept running and running. What does it mean?'\n\nLinh smiles. 'Dreams are fascinating. Scientists believe that dreams come from your subconscious — the part of your mind that works even when you are not aware of it. Your subconscious stores memories, feelings, and worries. When you sleep, it processes all of that through dreams.'\n\n'So my dream about the forest means I am worried about something?' Đức asks.\n\n'Maybe,' Linh says. 'Running and not finding a way out could mean you feel stuck in some area of your life. But dream interpretation is not exact science. The important thing is that dreaming is healthy. It means your brain is doing its job.'\n\n'I also had a restless night last week,' Đức says. 'I kept waking up every hour. I felt terrible the next day — I could not focus on anything at work.'\n\n'That makes sense,' Linh says. 'When you have a restless night, your brain does not get enough deep sleep. Deep sleep is when your brain does its most important work — it cleans out waste, strengthens memories, and rejuvenates your neurons. Without it, your cognitive abilities drop significantly.'\n\n'Cognitive abilities?' Đức asks.\n\n'Your ability to think, remember, and make decisions,' Linh explains. 'Studies show that if you deprive someone of sleep for just one night, their cognitive performance drops by twenty to thirty percent. That is like being slightly drunk.'\n\nĐức looks shocked. 'That bad?'\n\n'Yes,' Linh says. 'And it gets worse over time. Chronic sleep deprivation — when you consistently deprive your body of enough rest — can lead to serious health problems. But the good news is that your brain can rejuvenate quickly. Even two or three nights of good sleep can restore much of your cognitive function.'\n\n'So sleep is like charging a battery,' Đức says.\n\n'Exactly,' Linh says. 'And dreams are like the software updates that happen while you charge.'\n\nĐức laughs. 'I like that. I will try to let my brain finish its updates tonight.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Giấc mơ và tiềm thức",
                    "description": "Viết câu sử dụng từ vựng về giấc mơ, nhận thức, và phục hồi.",
                    "data": {
                        "vocabList": ["restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate"],
                        "items": [
                            {
                                "targetVocab": "restless",
                                "prompt": "Hãy dùng từ 'restless' để viết một câu về một đêm ngủ không yên. Ví dụ: I had a restless night because I was worried about my exam the next morning."
                            },
                            {
                                "targetVocab": "subconscious",
                                "prompt": "Hãy dùng từ 'subconscious' để viết một câu về tiềm thức. Ví dụ: Sometimes your subconscious mind solves problems while you are sleeping."
                            },
                            {
                                "targetVocab": "dream",
                                "prompt": "Hãy dùng từ 'dream' để viết một câu về giấc mơ của bạn. Ví dụ: I had a vivid dream about traveling to a country I have never visited."
                            },
                            {
                                "targetVocab": "cognitive",
                                "prompt": "Hãy dùng từ 'cognitive' để viết một câu về khả năng tư duy. Ví dụ: Regular exercise can improve your cognitive abilities, especially memory and focus."
                            },
                            {
                                "targetVocab": "deprive",
                                "prompt": "Hãy dùng từ 'deprive' để viết một câu về việc thiếu ngủ. Ví dụ: When you deprive yourself of sleep, your body cannot repair itself properly."
                            },
                            {
                                "targetVocab": "rejuvenate",
                                "prompt": "Hãy dùng từ 'rejuvenate' để viết một câu về sự phục hồi. Ví dụ: A weekend of good sleep can rejuvenate your energy and improve your mood."
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng phần 3 — Chu kỳ giấc ngủ và liệu pháp",
                    "description": "Ôn lại phần 1-2 và giới thiệu chủ đề chu kỳ giấc ngủ, hormone, và liệu pháp.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần 3 — phần cuối cùng trước khi ôn tập! Bạn đã đi được hai phần ba chặng đường rồi. Hãy cùng nhìn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ về giấc ngủ cơ bản: insomnia là chứng mất ngủ, drowsy là buồn ngủ, circadian là thuộc về nhịp sinh học, melatonin là hormone giấc ngủ, fatigue là sự kiệt sức, và nap là giấc ngủ ngắn. Trong phần 2, bạn học 6 từ về giấc mơ và nhận thức: restless là bồn chồn không yên, subconscious là tiềm thức, dream là giấc mơ, cognitive là thuộc về tư duy, deprive là tước đoạt, và rejuvenate là tái tạo.\n\nBây giờ, trong phần 3, chúng ta sẽ nói về chu kỳ giấc ngủ, hormone, và cách chữa trị các vấn đề về giấc ngủ. Bạn sẽ học 6 từ cuối cùng: cycle, alert, hormone, therapy, anxiety, và rem."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Dạy 6 từ vựng: cycle, alert, hormone, therapy, anxiety, rem.",
                    "data": {
                        "text": "Hãy cùng học 6 từ cuối cùng nhé.\n\nTừ đầu tiên là cycle — danh từ — nghĩa là chu kỳ, vòng lặp. Cycle là một chuỗi các giai đoạn lặp đi lặp lại theo thứ tự. Trong giấc ngủ, sleep cycle là chu kỳ khoảng 90 phút mà não bộ đi qua nhiều giai đoạn khác nhau. Ví dụ: 'Each sleep cycle lasts about ninety minutes and repeats four to six times per night.' Trong bài đọc, Linh giải thích rằng mỗi cycle bao gồm giấc ngủ nhẹ, giấc ngủ sâu, và giấc ngủ REM.\n\nTừ thứ hai là alert — tính từ — nghĩa là tỉnh táo, cảnh giác. Alert là khi bạn hoàn toàn tỉnh, tập trung, và sẵn sàng phản ứng nhanh. Ví dụ: 'After a good night of sleep, I feel alert and ready to start the day.' Trong bài đọc, Đức nhận ra rằng sau khi ngủ đủ giấc, anh ấy cảm thấy alert hơn nhiều so với trước.\n\nTừ thứ ba là hormone — danh từ — nghĩa là hormone, nội tiết tố. Hormone là các chất hóa học trong cơ thể điều khiển nhiều chức năng — từ giấc ngủ đến tâm trạng đến sự phát triển. Ví dụ: 'Sleep affects the balance of hormones in your body.' Trong bài đọc, Linh nói rằng thiếu ngủ làm rối loạn nhiều hormone quan trọng, không chỉ melatonin.\n\nTừ thứ tư là therapy — danh từ — nghĩa là liệu pháp, phương pháp điều trị. Therapy là quá trình chữa trị một vấn đề sức khỏe — có thể là nói chuyện với chuyên gia, tập thể dục, hoặc thay đổi thói quen. Ví dụ: 'Cognitive behavioral therapy is one of the best treatments for insomnia.' Trong bài đọc, Linh giới thiệu một loại therapy đặc biệt dành cho người mất ngủ mà không cần dùng thuốc.\n\nTừ thứ năm là anxiety — danh từ — nghĩa là sự lo âu, lo lắng. Anxiety là cảm giác bất an, sợ hãi, hoặc căng thẳng về những điều có thể xảy ra. Ví dụ: 'Anxiety about work often keeps people awake at night.' Trong bài đọc, Đức thừa nhận rằng anxiety về deadline là nguyên nhân chính khiến anh ấy khó ngủ.\n\nTừ cuối cùng là rem — danh từ — viết tắt của Rapid Eye Movement — nghĩa là giấc ngủ REM. REM là giai đoạn giấc ngủ khi mắt bạn chuyển động nhanh dưới mí mắt — đây là lúc bạn mơ nhiều nhất và não bộ xử lý cảm xúc. Ví dụ: 'During rem sleep, your brain is almost as active as when you are awake.' Trong bài đọc, Linh giải thích rằng rem sleep rất quan trọng cho sức khỏe tinh thần.\n\nBạn đã có đủ 18 từ vựng rồi! Hãy luyện flashcard rồi đọc phần cuối của cuộc trò chuyện nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chu kỳ giấc ngủ và liệu pháp",
                    "description": "Học 6 từ: cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chu kỳ giấc ngủ và liệu pháp",
                    "description": "Học 6 từ: cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chu kỳ giấc ngủ và liệu pháp",
                    "description": "Học 6 từ: cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chu kỳ giấc ngủ và liệu pháp",
                    "description": "Học 6 từ: cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 3",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về chu kỳ giấc ngủ và liệu pháp.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc phần cuối của cuộc trò chuyện giữa Linh và Đức. Lần này, họ nói về chu kỳ giấc ngủ, giấc ngủ REM, và cách chữa trị mất ngủ mà không cần thuốc. Hãy chú ý cách các từ cycle, alert, hormone, therapy, anxiety, và rem được dùng trong câu chuyện. Một điểm ngữ pháp: khi nói về kết quả và lời khuyên, chúng ta thường dùng 'should' và 'can' — ví dụ 'you should try therapy' hoặc 'good sleep can make you more alert.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chu kỳ giấc ngủ và cách chữa mất ngủ",
                    "description": "Linh and Đức discuss sleep cycles, REM sleep, anxiety, and therapy for insomnia.",
                    "data": {
                        "text": "It is Friday evening. Linh and Đức are walking in the park near their office. Đức looks different today — his eyes are bright and he is smiling.\n\n'You look more alert than usual,' Linh says. 'Have you been sleeping better?'\n\n'Much better,' Đức says. 'I stopped using my phone after ten o'clock. And I started taking short naps at lunch. I feel like a different person.'\n\n'That is great,' Linh says. 'Your body is completing its sleep cycles properly now. Do you know what a sleep cycle is?'\n\n'Not exactly,' Đức says.\n\n'Each night, your brain goes through four to six sleep cycles,' Linh explains. 'Each cycle lasts about ninety minutes. It starts with light sleep, then moves to deep sleep, and then to rem sleep — that is when you dream the most. REM stands for Rapid Eye Movement because your eyes move quickly under your eyelids during this stage.'\n\n'Why is rem sleep important?' Đức asks.\n\n'During rem sleep, your brain processes emotions and memories,' Linh says. 'It is also when your body releases important hormones — chemicals that control growth, stress, and mood. If you wake up in the middle of a cycle, you feel groggy. But if you complete the full cycle, you wake up feeling alert and refreshed.'\n\n'That explains why sometimes I sleep eight hours but still feel tired,' Đức says.\n\n'Exactly. It is not just about how long you sleep — it is about completing your cycles,' Linh says.\n\nThey sit down on a bench. Đức is quiet for a moment.\n\n'I want to ask you something,' he says. 'Sometimes I cannot sleep because of anxiety. I worry about deadlines, about money, about the future. My mind will not stop.'\n\nLinh nods. 'That is very common. Anxiety is one of the biggest causes of insomnia. When you are anxious, your body produces stress hormones like cortisol. These hormones keep you alert when you should be winding down.'\n\n'Is there anything I can do?' Đức asks.\n\n'There is a type of therapy called CBT-I — Cognitive Behavioral Therapy for Insomnia,' Linh says. 'It does not use medicine. Instead, it teaches you techniques to calm your mind before bed. Things like writing down your worries, breathing exercises, and changing the way you think about sleep.'\n\n'That sounds helpful,' Đức says. 'I always thought therapy was only for serious problems.'\n\n'Not at all,' Linh says. 'Therapy is for anyone who wants to improve their life. And sleep is one of the most important parts of life. When you sleep well, your hormones are balanced, your anxiety decreases, and your brain can rejuvenate properly.'\n\nĐức takes a deep breath. 'I think I will look into that therapy. I want to break the cycle of bad sleep and anxiety.'\n\n'That is the smartest thing you have said all week,' Linh says with a smile.\n\nĐức laughs. 'Maybe good sleep is already making me smarter.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chu kỳ giấc ngủ và cách chữa mất ngủ",
                    "description": "Linh and Đức discuss sleep cycles, REM sleep, anxiety, and therapy for insomnia.",
                    "data": {
                        "text": "It is Friday evening. Linh and Đức are walking in the park near their office. Đức looks different today — his eyes are bright and he is smiling.\n\n'You look more alert than usual,' Linh says. 'Have you been sleeping better?'\n\n'Much better,' Đức says. 'I stopped using my phone after ten o'clock. And I started taking short naps at lunch. I feel like a different person.'\n\n'That is great,' Linh says. 'Your body is completing its sleep cycles properly now. Do you know what a sleep cycle is?'\n\n'Not exactly,' Đức says.\n\n'Each night, your brain goes through four to six sleep cycles,' Linh explains. 'Each cycle lasts about ninety minutes. It starts with light sleep, then moves to deep sleep, and then to rem sleep — that is when you dream the most. REM stands for Rapid Eye Movement because your eyes move quickly under your eyelids during this stage.'\n\n'Why is rem sleep important?' Đức asks.\n\n'During rem sleep, your brain processes emotions and memories,' Linh says. 'It is also when your body releases important hormones — chemicals that control growth, stress, and mood. If you wake up in the middle of a cycle, you feel groggy. But if you complete the full cycle, you wake up feeling alert and refreshed.'\n\n'That explains why sometimes I sleep eight hours but still feel tired,' Đức says.\n\n'Exactly. It is not just about how long you sleep — it is about completing your cycles,' Linh says.\n\nThey sit down on a bench. Đức is quiet for a moment.\n\n'I want to ask you something,' he says. 'Sometimes I cannot sleep because of anxiety. I worry about deadlines, about money, about the future. My mind will not stop.'\n\nLinh nods. 'That is very common. Anxiety is one of the biggest causes of insomnia. When you are anxious, your body produces stress hormones like cortisol. These hormones keep you alert when you should be winding down.'\n\n'Is there anything I can do?' Đức asks.\n\n'There is a type of therapy called CBT-I — Cognitive Behavioral Therapy for Insomnia,' Linh says. 'It does not use medicine. Instead, it teaches you techniques to calm your mind before bed. Things like writing down your worries, breathing exercises, and changing the way you think about sleep.'\n\n'That sounds helpful,' Đức says. 'I always thought therapy was only for serious problems.'\n\n'Not at all,' Linh says. 'Therapy is for anyone who wants to improve their life. And sleep is one of the most important parts of life. When you sleep well, your hormones are balanced, your anxiety decreases, and your brain can rejuvenate properly.'\n\nĐức takes a deep breath. 'I think I will look into that therapy. I want to break the cycle of bad sleep and anxiety.'\n\n'That is the smartest thing you have said all week,' Linh says with a smile.\n\nĐức laughs. 'Maybe good sleep is already making me smarter.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chu kỳ giấc ngủ và cách chữa mất ngủ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "It is Friday evening. Linh and Đức are walking in the park near their office. Đức looks different today — his eyes are bright and he is smiling.\n\n'You look more alert than usual,' Linh says. 'Have you been sleeping better?'\n\n'Much better,' Đức says. 'I stopped using my phone after ten o'clock. And I started taking short naps at lunch. I feel like a different person.'\n\n'That is great,' Linh says. 'Your body is completing its sleep cycles properly now. Do you know what a sleep cycle is?'\n\n'Not exactly,' Đức says.\n\n'Each night, your brain goes through four to six sleep cycles,' Linh explains. 'Each cycle lasts about ninety minutes. It starts with light sleep, then moves to deep sleep, and then to rem sleep — that is when you dream the most. REM stands for Rapid Eye Movement because your eyes move quickly under your eyelids during this stage.'\n\n'Why is rem sleep important?' Đức asks.\n\n'During rem sleep, your brain processes emotions and memories,' Linh says. 'It is also when your body releases important hormones — chemicals that control growth, stress, and mood. If you wake up in the middle of a cycle, you feel groggy. But if you complete the full cycle, you wake up feeling alert and refreshed.'\n\n'That explains why sometimes I sleep eight hours but still feel tired,' Đức says.\n\n'Exactly. It is not just about how long you sleep — it is about completing your cycles,' Linh says.\n\nThey sit down on a bench. Đức is quiet for a moment.\n\n'I want to ask you something,' he says. 'Sometimes I cannot sleep because of anxiety. I worry about deadlines, about money, about the future. My mind will not stop.'\n\nLinh nods. 'That is very common. Anxiety is one of the biggest causes of insomnia. When you are anxious, your body produces stress hormones like cortisol. These hormones keep you alert when you should be winding down.'\n\n'Is there anything I can do?' Đức asks.\n\n'There is a type of therapy called CBT-I — Cognitive Behavioral Therapy for Insomnia,' Linh says. 'It does not use medicine. Instead, it teaches you techniques to calm your mind before bed. Things like writing down your worries, breathing exercises, and changing the way you think about sleep.'\n\n'That sounds helpful,' Đức says. 'I always thought therapy was only for serious problems.'\n\n'Not at all,' Linh says. 'Therapy is for anyone who wants to improve their life. And sleep is one of the most important parts of life. When you sleep well, your hormones are balanced, your anxiety decreases, and your brain can rejuvenate properly.'\n\nĐức takes a deep breath. 'I think I will look into that therapy. I want to break the cycle of bad sleep and anxiety.'\n\n'That is the smartest thing you have said all week,' Linh says with a smile.\n\nĐức laughs. 'Maybe good sleep is already making me smarter.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chu kỳ giấc ngủ và liệu pháp",
                    "description": "Viết câu sử dụng từ vựng về chu kỳ giấc ngủ, hormone, và liệu pháp.",
                    "data": {
                        "vocabList": ["cycle", "alert", "hormone", "therapy", "anxiety", "rem"],
                        "items": [
                            {
                                "targetVocab": "cycle",
                                "prompt": "Hãy dùng từ 'cycle' để viết một câu về chu kỳ giấc ngủ. Ví dụ: Waking up between sleep cycles makes you feel more refreshed than waking up in the middle of one."
                            },
                            {
                                "targetVocab": "alert",
                                "prompt": "Hãy dùng từ 'alert' để viết một câu về sự tỉnh táo. Ví dụ: I feel most alert in the morning after a full night of uninterrupted sleep."
                            },
                            {
                                "targetVocab": "hormone",
                                "prompt": "Hãy dùng từ 'hormone' để viết một câu về hormone trong cơ thể. Ví dụ: Stress hormones like cortisol can keep you awake even when your body is exhausted."
                            },
                            {
                                "targetVocab": "therapy",
                                "prompt": "Hãy dùng từ 'therapy' để viết một câu về liệu pháp chữa trị. Ví dụ: My doctor recommended therapy instead of sleeping pills to treat my insomnia."
                            },
                            {
                                "targetVocab": "anxiety",
                                "prompt": "Hãy dùng từ 'anxiety' để viết một câu về sự lo âu. Ví dụ: Writing down my worries before bed helps reduce my anxiety and fall asleep faster."
                            },
                            {
                                "targetVocab": "rem",
                                "prompt": "Hãy dùng từ 'rem' để viết một câu về giấc ngủ REM. Ví dụ: Most of our vivid dreams happen during rem sleep, the deepest stage of the sleep cycle."
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
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng — ôn lại tất cả trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã học xong tất cả 18 từ vựng về khoa học giấc ngủ. Đây là một thành tích tuyệt vời — hãy cùng ôn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ cơ bản: insomnia là chứng mất ngủ — Đức tưởng mình bị insomnia nhưng thực ra là do thói quen xấu. Drowsy là buồn ngủ — cảm giác mắt nặng trĩu sau bữa trưa. Circadian là thuộc về nhịp sinh học — đồng hồ bên trong cơ thể bạn. Melatonin là hormone giấc ngủ — não tiết ra khi trời tối. Fatigue là sự kiệt sức — hậu quả của nhiều đêm thiếu ngủ. Nap là giấc ngủ ngắn — 20 phút có thể cải thiện trí nhớ.\n\nTrong phần 2, bạn học 6 từ về giấc mơ: restless là bồn chồn — Đức có nhiều đêm restless vì lo lắng. Subconscious là tiềm thức — nơi lưu trữ ký ức và cảm xúc ẩn sâu. Dream là giấc mơ — cách tiềm thức xử lý trải nghiệm. Cognitive là thuộc về tư duy — thiếu ngủ làm giảm cognitive function. Deprive là tước đoạt — khi bạn deprive não khỏi giấc ngủ, mọi thứ đều bị ảnh hưởng. Rejuvenate là tái tạo — giấc ngủ sâu giúp rejuvenate tế bào não.\n\nTrong phần 3, bạn học 6 từ cuối: cycle là chu kỳ — mỗi sleep cycle kéo dài 90 phút. Alert là tỉnh táo — bạn cảm thấy alert sau khi ngủ đủ giấc. Hormone là nội tiết tố — thiếu ngủ làm rối loạn nhiều hormone. Therapy là liệu pháp — CBT-I giúp chữa mất ngủ không cần thuốc. Anxiety là lo âu — nguyên nhân hàng đầu gây mất ngủ. Rem là giấc ngủ REM — giai đoạn mơ nhiều nhất và xử lý cảm xúc.\n\nBây giờ, bạn sẽ ôn lại tất cả 18 từ qua flashcard và bài tập viết. Sẵn sàng chưa? Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap, restless, subconscious, dream, cognitive, deprive, rejuvenate, cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap", "restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate", "cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap, restless, subconscious, dream, cognitive, deprive, rejuvenate, cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap", "restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate", "cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap, restless, subconscious, dream, cognitive, deprive, rejuvenate, cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap", "restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate", "cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap, restless, subconscious, dream, cognitive, deprive, rejuvenate, cycle, alert, hormone, therapy, anxiety, rem",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap", "restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate", "cycle", "alert", "hormone", "therapy", "anxiety", "rem"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập khoa học giấc ngủ",
                    "description": "Viết câu ôn tập sử dụng tất cả 18 từ vựng về giấc ngủ.",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap", "restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate", "cycle", "alert", "hormone", "therapy", "anxiety", "rem"],
                        "items": [
                            {
                                "targetVocab": "insomnia",
                                "prompt": "Hãy dùng từ 'insomnia' để viết một câu về nguyên nhân gây mất ngủ. Ví dụ: Insomnia can be caused by stress, screen time, or an irregular sleep schedule."
                            },
                            {
                                "targetVocab": "drowsy",
                                "prompt": "Hãy dùng từ 'drowsy' để viết một câu về lúc bạn cảm thấy buồn ngủ nhất. Ví dụ: Feeling drowsy while driving is extremely dangerous and you should pull over immediately."
                            },
                            {
                                "targetVocab": "circadian",
                                "prompt": "Hãy dùng từ 'circadian' để viết một câu về cách bảo vệ nhịp sinh học. Ví dụ: Going to bed at the same time every night helps maintain a healthy circadian rhythm."
                            },
                            {
                                "targetVocab": "melatonin",
                                "prompt": "Hãy dùng từ 'melatonin' để viết một câu về cách tăng melatonin tự nhiên. Ví dụ: Dimming the lights an hour before bed helps your brain produce more melatonin naturally."
                            },
                            {
                                "targetVocab": "fatigue",
                                "prompt": "Hãy dùng từ 'fatigue' để viết một câu về hậu quả của mệt mỏi. Ví dụ: Chronic fatigue affects not only your body but also your ability to make good decisions."
                            },
                            {
                                "targetVocab": "nap",
                                "prompt": "Hãy dùng từ 'nap' để viết một câu về lợi ích của giấc ngủ trưa. Ví dụ: Scientists say a short nap is more effective than a cup of coffee for boosting afternoon energy."
                            },
                            {
                                "targetVocab": "restless",
                                "prompt": "Hãy dùng từ 'restless' để viết một câu về cách đối phó với đêm trằn trọc. Ví dụ: When I have a restless night, I try reading a book instead of checking my phone."
                            },
                            {
                                "targetVocab": "subconscious",
                                "prompt": "Hãy dùng từ 'subconscious' để viết một câu về vai trò của tiềm thức. Ví dụ: Your subconscious continues to process information even after you stop thinking about a problem."
                            },
                            {
                                "targetVocab": "dream",
                                "prompt": "Hãy dùng từ 'dream' để viết một câu về ý nghĩa của giấc mơ. Ví dụ: Some researchers believe that dreams help us practice dealing with difficult situations in a safe environment."
                            },
                            {
                                "targetVocab": "cognitive",
                                "prompt": "Hãy dùng từ 'cognitive' để viết một câu về mối liên hệ giữa giấc ngủ và tư duy. Ví dụ: Getting enough sleep is one of the simplest ways to improve your cognitive performance at work."
                            },
                            {
                                "targetVocab": "deprive",
                                "prompt": "Hãy dùng từ 'deprive' để viết một câu về tác hại của thiếu ngủ. Ví dụ: Studies show that sleep-deprived students perform significantly worse on exams than well-rested ones."
                            },
                            {
                                "targetVocab": "rejuvenate",
                                "prompt": "Hãy dùng từ 'rejuvenate' để viết một câu về cách phục hồi năng lượng. Ví dụ: A relaxing weekend with plenty of sleep can rejuvenate your mind and body for the week ahead."
                            },
                            {
                                "targetVocab": "cycle",
                                "prompt": "Hãy dùng từ 'cycle' để viết một câu về tầm quan trọng của chu kỳ giấc ngủ. Ví dụ: Setting your alarm to match your natural sleep cycles can help you wake up feeling more energized."
                            },
                            {
                                "targetVocab": "alert",
                                "prompt": "Hãy dùng từ 'alert' để viết một câu về sự tỉnh táo trong ngày. Ví dụ: People who sleep seven to eight hours a night tend to be more alert and productive during the day."
                            },
                            {
                                "targetVocab": "hormone",
                                "prompt": "Hãy dùng từ 'hormone' để viết một câu về hormone và giấc ngủ. Ví dụ: Sleep helps regulate the hormones that control hunger, which is why tired people often eat more."
                            },
                            {
                                "targetVocab": "therapy",
                                "prompt": "Hãy dùng từ 'therapy' để viết một câu về liệu pháp cho giấc ngủ. Ví dụ: Cognitive behavioral therapy for insomnia is now considered more effective than sleeping pills."
                            },
                            {
                                "targetVocab": "anxiety",
                                "prompt": "Hãy dùng từ 'anxiety' để viết một câu về mối liên hệ giữa lo âu và giấc ngủ. Ví dụ: Reducing anxiety before bed through meditation or journaling can significantly improve sleep quality."
                            },
                            {
                                "targetVocab": "rem",
                                "prompt": "Hãy dùng từ 'rem' để viết một câu về tầm quan trọng của giấc ngủ REM. Ví dụ: Without enough rem sleep, your brain struggles to process emotions and form long-term memories."
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
                    "description": "Giới thiệu bài đọc cuối cùng kết hợp tất cả 18 từ vựng về giấc ngủ.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của TED-Ed: Why We Sleep! Bạn đã đi một chặng đường ấn tượng. Trong phần 1, bạn học về nhịp sinh học và melatonin với 6 từ: insomnia, drowsy, circadian, melatonin, fatigue, nap. Trong phần 2, bạn khám phá giấc mơ và tiềm thức với 6 từ: restless, subconscious, dream, cognitive, deprive, rejuvenate. Trong phần 3, bạn tìm hiểu chu kỳ giấc ngủ và liệu pháp với 6 từ: cycle, alert, hormone, therapy, anxiety, rem. Trong phần ôn tập, bạn đã luyện lại tất cả 18 từ.\n\nBây giờ, bạn sẽ đọc một bài tổng hợp — Linh và Đức gặp lại nhau một tháng sau và chia sẻ những thay đổi trong cuộc sống. Bài đọc này dùng tất cả 18 từ vựng bạn đã học. Hãy đọc chậm, thưởng thức câu chuyện, và chú ý cách mỗi từ được dùng trong ngữ cảnh thực tế nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Một tháng sau — Giấc ngủ thay đổi cuộc sống",
                    "description": "Linh and Đức reflect on how understanding sleep science has changed their lives.",
                    "data": {
                        "text": "One month has passed since Linh and Đức started talking about sleep. They are sitting in the same coffee shop where it all began. But this time, Đức is not yawning.\n\n'I have to tell you something,' Đức says. 'You changed my life.'\n\nLinh laughs. 'I did not change your life. Sleep science did. I just told you about it.'\n\n'Well, let me tell you what happened,' Đức says. 'After our first conversation, I stopped looking at my phone after ten o'clock. The first few nights were hard. I felt restless. I kept reaching for my phone out of habit. But after a week, something changed. I started feeling drowsy naturally around eleven — my body was producing melatonin on its own again.'\n\n'Your circadian rhythm was resetting,' Linh says.\n\n'Exactly. And then I started taking short naps at lunch — just twenty minutes. My colleagues thought I was lazy, but I felt so much more alert in the afternoon. My fatigue disappeared. I could focus on my work without drinking three cups of coffee.'\n\n'That is the power of working with your body instead of against it,' Linh says.\n\n'But the biggest change was about my anxiety,' Đức continues. 'I looked into that therapy you mentioned — CBT-I. I found a therapist online who taught me some techniques. She told me to write down my worries before bed. Just put them on paper and close the notebook. It sounds simple, but it works. My mind stops racing. The anxiety does not disappear completely, but it becomes manageable.'\n\n'That is wonderful,' Linh says. 'How are your dreams?'\n\n'Much better,' Đức says. 'I used to have that recurring dream about running through a forest. But now I dream about different things — sometimes I dream about traveling, sometimes about cooking. My subconscious seems calmer. And I remember my dreams more clearly now.'\n\n'That means you are getting more rem sleep,' Linh says. 'When you complete full sleep cycles without interruption, you spend more time in rem — the stage where your brain processes emotions and creates dreams. Your hormones are probably more balanced too.'\n\n'I think so,' Đức says. 'I feel less stressed. I make better decisions at work. My cognitive abilities feel sharper — I can solve problems faster and remember things more easily.'\n\n'Sleep is the foundation of everything,' Linh says. 'When you deprive your body of rest, everything suffers — your mood, your health, your relationships. But when you give your body what it needs, it rejuvenates itself in amazing ways.'\n\nĐức nods. 'I used to think sleeping was wasting time. Now I understand that sleep is the most productive thing I do. Every cycle my brain completes is like a repair session — fixing what is broken, organizing what is messy, preparing me for tomorrow.'\n\n'You sound like a TED-Ed speaker now,' Linh says with a smile.\n\n'Maybe I should give a talk,' Đức jokes. 'Title: How I Stopped Fighting Sleep and Started Living Better.'\n\nThey both laugh. Đức finishes his tea — not coffee this time — and looks out the window. The sun is setting.\n\n'You know what I am looking forward to tonight?' he says.\n\n'What?' Linh asks.\n\n'Going to bed,' Đức says. 'And letting my brain do its magic.'\n\nLinh smiles. 'That is the best thing I have heard all day.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Một tháng sau — Giấc ngủ thay đổi cuộc sống",
                    "description": "Linh and Đức reflect on how understanding sleep science has changed their lives.",
                    "data": {
                        "text": "One month has passed since Linh and Đức started talking about sleep. They are sitting in the same coffee shop where it all began. But this time, Đức is not yawning.\n\n'I have to tell you something,' Đức says. 'You changed my life.'\n\nLinh laughs. 'I did not change your life. Sleep science did. I just told you about it.'\n\n'Well, let me tell you what happened,' Đức says. 'After our first conversation, I stopped looking at my phone after ten o'clock. The first few nights were hard. I felt restless. I kept reaching for my phone out of habit. But after a week, something changed. I started feeling drowsy naturally around eleven — my body was producing melatonin on its own again.'\n\n'Your circadian rhythm was resetting,' Linh says.\n\n'Exactly. And then I started taking short naps at lunch — just twenty minutes. My colleagues thought I was lazy, but I felt so much more alert in the afternoon. My fatigue disappeared. I could focus on my work without drinking three cups of coffee.'\n\n'That is the power of working with your body instead of against it,' Linh says.\n\n'But the biggest change was about my anxiety,' Đức continues. 'I looked into that therapy you mentioned — CBT-I. I found a therapist online who taught me some techniques. She told me to write down my worries before bed. Just put them on paper and close the notebook. It sounds simple, but it works. My mind stops racing. The anxiety does not disappear completely, but it becomes manageable.'\n\n'That is wonderful,' Linh says. 'How are your dreams?'\n\n'Much better,' Đức says. 'I used to have that recurring dream about running through a forest. But now I dream about different things — sometimes I dream about traveling, sometimes about cooking. My subconscious seems calmer. And I remember my dreams more clearly now.'\n\n'That means you are getting more rem sleep,' Linh says. 'When you complete full sleep cycles without interruption, you spend more time in rem — the stage where your brain processes emotions and creates dreams. Your hormones are probably more balanced too.'\n\n'I think so,' Đức says. 'I feel less stressed. I make better decisions at work. My cognitive abilities feel sharper — I can solve problems faster and remember things more easily.'\n\n'Sleep is the foundation of everything,' Linh says. 'When you deprive your body of rest, everything suffers — your mood, your health, your relationships. But when you give your body what it needs, it rejuvenates itself in amazing ways.'\n\nĐức nods. 'I used to think sleeping was wasting time. Now I understand that sleep is the most productive thing I do. Every cycle my brain completes is like a repair session — fixing what is broken, organizing what is messy, preparing me for tomorrow.'\n\n'You sound like a TED-Ed speaker now,' Linh says with a smile.\n\n'Maybe I should give a talk,' Đức jokes. 'Title: How I Stopped Fighting Sleep and Started Living Better.'\n\nThey both laugh. Đức finishes his tea — not coffee this time — and looks out the window. The sun is setting.\n\n'You know what I am looking forward to tonight?' he says.\n\n'What?' Linh asks.\n\n'Going to bed,' Đức says. 'And letting my brain do its magic.'\n\nLinh smiles. 'That is the best thing I have heard all day.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Một tháng sau — Giấc ngủ thay đổi cuộc sống",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "One month has passed since Linh and Đức started talking about sleep. They are sitting in the same coffee shop where it all began. But this time, Đức is not yawning.\n\n'I have to tell you something,' Đức says. 'You changed my life.'\n\nLinh laughs. 'I did not change your life. Sleep science did. I just told you about it.'\n\n'Well, let me tell you what happened,' Đức says. 'After our first conversation, I stopped looking at my phone after ten o'clock. The first few nights were hard. I felt restless. I kept reaching for my phone out of habit. But after a week, something changed. I started feeling drowsy naturally around eleven — my body was producing melatonin on its own again.'\n\n'Your circadian rhythm was resetting,' Linh says.\n\n'Exactly. And then I started taking short naps at lunch — just twenty minutes. My colleagues thought I was lazy, but I felt so much more alert in the afternoon. My fatigue disappeared. I could focus on my work without drinking three cups of coffee.'\n\n'That is the power of working with your body instead of against it,' Linh says.\n\n'But the biggest change was about my anxiety,' Đức continues. 'I looked into that therapy you mentioned — CBT-I. I found a therapist online who taught me some techniques. She told me to write down my worries before bed. Just put them on paper and close the notebook. It sounds simple, but it works. My mind stops racing. The anxiety does not disappear completely, but it becomes manageable.'\n\n'That is wonderful,' Linh says. 'How are your dreams?'\n\n'Much better,' Đức says. 'I used to have that recurring dream about running through a forest. But now I dream about different things — sometimes I dream about traveling, sometimes about cooking. My subconscious seems calmer. And I remember my dreams more clearly now.'\n\n'That means you are getting more rem sleep,' Linh says. 'When you complete full sleep cycles without interruption, you spend more time in rem — the stage where your brain processes emotions and creates dreams. Your hormones are probably more balanced too.'\n\n'I think so,' Đức says. 'I feel less stressed. I make better decisions at work. My cognitive abilities feel sharper — I can solve problems faster and remember things more easily.'\n\n'Sleep is the foundation of everything,' Linh says. 'When you deprive your body of rest, everything suffers — your mood, your health, your relationships. But when you give your body what it needs, it rejuvenates itself in amazing ways.'\n\nĐức nods. 'I used to think sleeping was wasting time. Now I understand that sleep is the most productive thing I do. Every cycle my brain completes is like a repair session — fixing what is broken, organizing what is messy, preparing me for tomorrow.'\n\n'You sound like a TED-Ed speaker now,' Linh says with a smile.\n\n'Maybe I should give a talk,' Đức jokes. 'Title: How I Stopped Fighting Sleep and Started Living Better.'\n\nThey both laugh. Đức finishes his tea — not coffee this time — and looks out the window. The sun is setting.\n\n'You know what I am looking forward to tonight?' he says.\n\n'What?' Linh asks.\n\n'Going to bed,' Đức says. 'And letting my brain do its magic.'\n\nLinh smiles. 'That is the best thing I have heard all day.'"
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích khoa học giấc ngủ",
                    "description": "Viết đoạn văn phân tích về giấc ngủ sử dụng từ vựng đã học.",
                    "data": {
                        "vocabList": ["insomnia", "drowsy", "circadian", "melatonin", "fatigue", "nap", "restless", "subconscious", "dream", "cognitive", "deprive", "rejuvenate", "cycle", "alert", "hormone", "therapy", "anxiety", "rem"],
                        "instructions": "Viết một đoạn văn tiếng Anh (80-120 từ) phân tích mối liên hệ giữa giấc ngủ và sức khỏe tinh thần. Sử dụng ít nhất 6 từ vựng đã học trong bài.",
                        "prompts": [
                            "Explain how sleep deprivation affects cognitive performance and emotional health. Use words like deprive, cognitive, fatigue, and anxiety to describe the consequences of not getting enough rest.",
                            "Describe the ideal sleep routine for someone who struggles with insomnia. Include advice about circadian rhythms, melatonin, therapy, and how completing full sleep cycles helps the brain rejuvenate."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay — farewell tone: team_building_energy.",
                    "data": {
                        "text": "Bạn đã hoàn thành TED-Ed: Why We Sleep — và tôi muốn nói rằng: bạn không chỉ học xong một bài tiếng Anh. Bạn vừa trang bị cho mình kiến thức có thể thay đổi cuộc sống. Và bây giờ, chúng ta — cả bạn và tôi — sẽ cùng ôn lại 18 từ vựng một lần cuối. Hãy coi đây như buổi họp nhóm cuối cùng trước khi mỗi người ra sân thi đấu.\n\nInsomnia — chứng mất ngủ. Hàng triệu người trên thế giới đang chiến đấu với insomnia mỗi đêm. Câu mới: Understanding the causes of insomnia is the first step toward finding a solution that works for you.\n\nDrowsy — buồn ngủ, lờ đờ. Cảm giác drowsy là tín hiệu từ cơ thể — hãy lắng nghe nó. Câu mới: If you feel drowsy during a meeting, it might be a sign that you need to improve your sleep habits.\n\nCircadian — thuộc về nhịp sinh học. Circadian rhythm là đồng hồ bên trong bạn — hãy tôn trọng nó. Câu mới: Shift workers often struggle because their work schedule conflicts with their natural circadian rhythm.\n\nMelatonin — hormone giấc ngủ. Melatonin là người bạn thầm lặng giúp bạn chìm vào giấc ngủ mỗi đêm. Câu mới: Instead of taking melatonin supplements, try reducing screen time to let your body produce it naturally.\n\nFatigue — sự kiệt sức. Fatigue không phải là điều bạn nên chấp nhận — mà là điều bạn nên giải quyết. Câu mới: Mental fatigue from overwork can be just as damaging as physical exhaustion from exercise.\n\nNap — giấc ngủ ngắn. Một giấc nap đúng lúc có thể biến một buổi chiều tệ thành một buổi chiều tuyệt vời. Câu mới: NASA research found that pilots who took a short nap performed forty percent better on alertness tests.\n\nBạn thấy không? Chỉ với 6 từ đầu tiên, bạn đã có thể nói về giấc ngủ một cách chuyên nghiệp rồi. Nhưng chúng ta còn 12 từ nữa — hãy tiếp tục nhé!\n\nRestless — bồn chồn, không yên. Đêm restless là dấu hiệu cơ thể đang cần sự chú ý. Câu mới: Keeping a sleep diary can help you identify what makes your nights restless and find patterns to fix.\n\nSubconscious — tiềm thức. Subconscious là kho báu ẩn giấu — giấc ngủ là chìa khóa mở nó. Câu mới: Many creative breakthroughs happen because the subconscious mind works on problems while we sleep.\n\nDream — giấc mơ. Dream không chỉ là giải trí ban đêm — mà là cách não bộ xử lý cuộc sống. Câu mới: Keeping a dream journal next to your bed helps you remember and learn from your dreams.\n\nCognitive — thuộc về tư duy. Cognitive performance là thước đo sức mạnh não bộ — và giấc ngủ là nhiên liệu. Câu mới: Students who prioritize sleep before exams show better cognitive performance than those who stay up all night studying.\n\nDeprive — tước đoạt. Khi bạn deprive bản thân khỏi giấc ngủ, bạn đang trả giá bằng sức khỏe tương lai. Câu mới: Society often celebrates people who deprive themselves of sleep to work harder, but science shows this is counterproductive.\n\nRejuvenate — tái tạo. Rejuvenate là phép màu xảy ra mỗi đêm — nếu bạn cho phép nó. Câu mới: Even one night of deep, uninterrupted sleep can rejuvenate your immune system and improve your mood.\n\nChúng ta gần xong rồi! Sáu từ cuối cùng — hãy cùng nhau hoàn thành nhé.\n\nCycle — chu kỳ. Mỗi sleep cycle là một vòng tròn hoàn hảo của sự phục hồi. Câu mới: Understanding your personal sleep cycles can help you set the perfect alarm time to wake up refreshed.\n\nAlert — tỉnh táo. Alert là trạng thái tốt nhất của bạn — và giấc ngủ là con đường ngắn nhất đến đó. Câu mới: The difference between feeling groggy and feeling alert often comes down to just one extra hour of sleep.\n\nHormone — nội tiết tố. Hormone là đội ngũ điều hành cơ thể — giấc ngủ giữ cho đội ngũ này hoạt động trơn tru. Câu mới: Growth hormone, which repairs muscles and tissues, is released primarily during deep sleep.\n\nTherapy — liệu pháp. Therapy không phải là dấu hiệu yếu đuối — mà là dấu hiệu bạn đủ mạnh mẽ để tìm giải pháp. Câu mới: Sleep therapy has helped millions of people around the world overcome chronic insomnia without medication.\n\nAnxiety — lo âu. Anxiety và giấc ngủ có mối quan hệ hai chiều — giải quyết một bên sẽ cải thiện bên kia. Câu mới: Learning to manage anxiety through breathing exercises and journaling can transform your sleep quality.\n\nRem — giấc ngủ REM. REM sleep là sân khấu nơi giấc mơ diễn ra và cảm xúc được chữa lành. Câu mới: People who get enough rem sleep tend to be more emotionally resilient and creative in their daily lives.\n\nVà thế là xong — 18 từ vựng, 18 công cụ mới trong hành trang tiếng Anh của bạn. Nhưng đây không phải là kết thúc — mà là khởi đầu. Tối nay, khi bạn nằm xuống giường, hãy nhớ: bạn không chỉ đang ngủ. Bạn đang rejuvenate. Bạn đang cho phép mỗi sleep cycle làm công việc kỳ diệu của nó. Bạn đang đầu tư vào phiên bản tốt nhất của chính mình.\n\nChúng ta là một đội — bạn, tôi, và 18 từ vựng này. Hãy mang chúng ra thế giới thật. Nói về giấc ngủ với bạn bè. Chia sẻ những gì bạn học được. Và quan trọng nhất — hãy ngủ ngon tối nay.\n\nCảm ơn bạn đã học cùng tôi. Hẹn gặp lại trong bài học tiếp theo — sau một giấc ngủ thật sâu nhé!"
                    }
                }
            ]
        }
    ]
}

# ── Validate ──
print("Validating content...")
validate_balanced_skills_standard(content)
print("  ✓ balanced_skills_standard structure OK")
validate_content_type_tags(content)
print("  ✓ contentTypeTags OK")
validate_bilingual_prompts(content, "preintermediate")
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
print(f"Level: preintermediate | Skill: balanced_skills | Content: podcast")
print(f"Words: 18 (3 groups of 6)")
