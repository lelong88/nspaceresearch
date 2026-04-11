import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from firebase_token import get_firebase_id_token
from validate_curriculum import (
    validate_reader,
    validate_content_type_tags,
)

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Curriculum #48: The Lost Kite
# Level: beginner | Skill focus: reader | Content type: ["story"]
# Topic: Daily life | 12 words (2 groups of 6), 4 sessions, bilingual (vi-en)
# Description tone: empathetic_observation (for story series)
# Farewell tone: quiet_awe (for story series)
# W1: kite, wind, string, field, climb, branch
# W2: neighbor, ladder, careful, reach, stuck, grateful

# ── S1 reading: Chapter 1 — Hoa flies her kite ──
s1_reading = (
    "Hoa loves her kite. It is red and yellow with a long tail. Her grandmother gave it to her "
    "last year. Hoa flies it every weekend.\n\n"
    "Today is Saturday. The wind is strong. Hoa takes her kite to the big field near her house. "
    "The field is green and wide. There are no buildings, no cars — just grass and sky.\n\n"
    "Hoa holds the string tight. She runs across the field. The kite goes up, up, up. It dances "
    "in the wind. Hoa laughs. She feels free.\n\n"
    "The wind changes. It pulls the kite to the left. Hoa pulls the string back. The kite moves "
    "right. She is good at this. She has practiced many times.\n\n"
    "Then the wind gets very strong. The string pulls hard. Hoa holds on, but the wind is too "
    "much. The string slips from her hands.\n\n"
    "The kite flies away. It goes over the field, over the road, and into a tall tree. The kite "
    "is stuck in a high branch. Hoa cannot reach it.\n\n"
    "She stands under the tree and looks up. Her beautiful kite is caught between two branches. "
    "The tail hangs down, moving in the wind.\n\n"
    "'Oh no,' Hoa says. She does not know what to do. She cannot climb the tree — it is too tall. "
    "She sits on the grass and thinks."
)

# ── S2 reading: Chapter 2 — The neighborhood helps ──
s2_reading = (
    "Hoa sits under the tree for a long time. She looks at her kite stuck in the branch above. "
    "She feels sad.\n\n"
    "Then she hears a voice. 'What happened?' It is Bác Tám, her neighbor. He lives next door. "
    "He is an old man with kind eyes.\n\n"
    "'My kite is stuck,' Hoa says. She points up at the tree. 'I cannot reach it.'\n\n"
    "Bác Tám looks up. 'That is very high,' he says. 'We need a ladder.'\n\n"
    "He walks back to his house and comes back with a tall ladder. He puts the ladder against "
    "the tree. But the ladder is not tall enough. The kite is still too high.\n\n"
    "'We need help,' Bác Tám says.\n\n"
    "Soon, more neighbors come. Chị Lan brings a long stick. Anh Đức brings a rope. "
    "Little Tùng brings a basket — he is not sure why, but he wants to help.\n\n"
    "Anh Đức climbs the ladder. He is careful. He goes up step by step. At the top, he reaches "
    "out with the long stick. He pushes the branch. The kite moves a little.\n\n"
    "'Almost!' Hoa shouts.\n\n"
    "Anh Đức pushes again. This time, the kite comes free. It falls down slowly, turning in the "
    "wind. Hoa catches it with both hands.\n\n"
    "'Thank you! Thank you!' Hoa says. She is so grateful. She hugs her kite.\n\n"
    "Bác Tám smiles. 'That is what neighbors are for,' he says.\n\n"
    "Hoa looks at everyone — Bác Tám, Chị Lan, Anh Đức, little Tùng with his basket. She feels "
    "warm inside. She is grateful for her neighbors. She is grateful for her kite. And she is "
    "grateful for this day."
)


# ── S3 review readAlong text (recap of both chapters) ──
s3_readalong = (
    "Hoa loves her kite. It is red and yellow. She flies it in the big field every weekend. "
    "The wind is strong today. The kite goes up high. But then the wind pulls too hard. "
    "The string slips from her hands. The kite flies into a tall tree. It is stuck in a branch. "
    "Hoa cannot reach it. She sits under the tree and feels sad.\n\n"
    "Then her neighbor Bác Tám comes. He brings a ladder. But the ladder is not tall enough. "
    "More neighbors come to help. Anh Đức climbs the ladder carefully. He reaches up with a "
    "long stick and pushes the branch. The kite comes free. Hoa catches it. She is so grateful "
    "for her kind neighbors."
)

# ── S4 full story (≥500 words) ──
s4_full_story = (
    "Hoa is eight years old. She lives in a small house with her mother and her grandmother. "
    "Their house is on a quiet street with many trees. Hoa loves her street. She knows every "
    "neighbor, every dog, and every cat.\n\n"
    "But the thing Hoa loves most is her kite. It is red and yellow with a long tail made of "
    "ribbon. Her grandmother made it for her last year. 'A kite needs wind and a good heart,' "
    "her grandmother said. Hoa did not understand then, but she kept those words.\n\n"
    "Every Saturday, Hoa takes her kite to the big field near her house. The field is wide and "
    "green. There are no buildings, no cars — just grass and sky. It is the perfect place to fly "
    "a kite.\n\n"
    "Today, the wind is strong. Hoa holds the string tight and runs across the field. The kite "
    "goes up quickly. It dances in the wind, turning left and right. The long tail moves like a "
    "snake in the sky. Hoa laughs. She feels free and happy.\n\n"
    "She lets out more string. The kite goes higher and higher. It is so high that it looks small "
    "against the clouds. Hoa is proud. She is good at flying her kite. She has practiced many "
    "times.\n\n"
    "Then the wind changes. It gets very strong, much stronger than before. The string pulls hard "
    "in Hoa's hands. She tries to hold on, but the wind is too much. The string slips through "
    "her fingers.\n\n"
    "'No!' Hoa shouts. She runs after the kite, but it is too fast. The wind carries it over the "
    "field, over the road, and into a tall tree at the edge of the street. The kite hits a high "
    "branch and stops. The string hangs down. The tail moves slowly in the wind.\n\n"
    "Hoa stands under the tree and looks up. Her beautiful kite is stuck between two thick "
    "branches. She cannot climb the tree — it is too tall and the branches are too high. She "
    "tries to jump and reach the string, but it is far above her head.\n\n"
    "She sits on the grass under the tree. She feels sad. That kite is special. Her grandmother "
    "made it with her own hands. Hoa does not want to lose it.\n\n"
    "After a while, she hears footsteps. 'Hoa? What happened?' It is Bác Tám, her neighbor. He "
    "is an old man who lives next door. He has kind eyes and a warm smile.\n\n"
    "'My kite is stuck in the tree,' Hoa says. Her voice is small. 'I cannot reach it.'\n\n"
    "Bác Tám looks up at the tree. 'That is very high,' he says. 'But do not worry. We will get "
    "it back. Let me get my ladder.'\n\n"
    "He walks to his house and comes back with a tall wooden ladder. He puts the ladder against "
    "the tree trunk. But when he looks up, he shakes his head. The ladder reaches the lower "
    "branches, but the kite is much higher.\n\n"
    "'We need more help,' Bác Tám says.\n\n"
    "He calls out to the street. Soon, more neighbors come. Chị Lan, who sells flowers at the "
    "market, brings a long bamboo stick. Anh Đức, who fixes motorbikes, brings a strong rope. "
    "Little Tùng, who is only five, brings a basket. He is not sure how it will help, but he "
    "wants to be part of the team.\n\n"
    "'Okay,' Bác Tám says. 'Anh Đức, you are young and strong. Can you climb the ladder?'\n\n"
    "'Of course,' Anh Đức says. He takes the long stick from Chị Lan and starts to climb. He "
    "goes up step by step. He is careful. He holds the ladder with one hand and the stick with "
    "the other.\n\n"
    "At the top of the ladder, Anh Đức reaches out with the stick. He pushes the branch where "
    "the kite is stuck. The branch moves a little. The kite shifts but does not fall.\n\n"
    "'Push harder!' little Tùng shouts from below.\n\n"
    "Anh Đức pushes again, harder this time. The branch bends. The string comes loose. The kite "
    "slides off the branch and begins to fall. It turns slowly in the wind, floating down like a "
    "big red and yellow leaf.\n\n"
    "Hoa reaches up and catches it with both hands. She holds it close to her chest. The kite is "
    "not broken. The tail is still there. The string is still attached.\n\n"
    "'Thank you!' Hoa says. Her eyes are bright. 'Thank you, everyone!'\n\n"
    "Bác Tám pats her head. 'That is what neighbors are for,' he says.\n\n"
    "Chị Lan smiles. 'Next time, hold the string tighter,' she says with a wink.\n\n"
    "Anh Đức climbs down the ladder carefully. 'That was fun,' he says. 'I have not climbed a "
    "tree since I was a boy.'\n\n"
    "Little Tùng holds up his basket. 'I brought this for the kite,' he says. Everyone laughs.\n\n"
    "Hoa looks at her neighbors — Bác Tám with his ladder, Chị Lan with her stick, Anh Đức "
    "wiping his hands, and little Tùng with his basket. She feels something warm in her chest. "
    "She is grateful. Not just for the kite, but for these people. They came to help without "
    "being asked. They gave their time and their kindness.\n\n"
    "That evening, Hoa tells her grandmother what happened. Her grandmother listens and smiles.\n\n"
    "'Do you remember what I told you?' her grandmother asks. 'A kite needs wind and a good "
    "heart.'\n\n"
    "'I understand now,' Hoa says. 'The wind took my kite away. But good hearts brought it "
    "back.'\n\n"
    "Her grandmother hugs her. 'That is right,' she says. 'The wind will always blow. But when "
    "you have good neighbors, you never lose what matters.'\n\n"
    "Hoa puts her kite in her room, next to her bed. She looks at it and smiles. Tomorrow is "
    "Sunday. Maybe she will fly it again. And this time, she will hold the string a little "
    "tighter.\n\n"
    "But if the wind takes it again, she knows her neighbors will be there. And that makes "
    "everything okay."
)

all_words = ["kite", "wind", "string", "field", "climb", "branch",
             "neighbor", "ladder", "careful", "reach", "stuck", "grateful"]
w1 = ["kite", "wind", "string", "field", "climb", "branch"]
w2 = ["neighbor", "ladder", "careful", "reach", "stuck", "grateful"]


content = {
    "title": "The Lost Kite",
    "contentTypeTags": ["story"],
    "description": "BẠN CÓ NHỚ LẦN CUỐI CÙNG AI ĐÓ GIÚP BẠN MÀ KHÔNG CẦN BẠN HỎI KHÔNG?\n\nCó những ngày mọi thứ đi sai hướng — bạn mất một thứ quan trọng, bạn cảm thấy bất lực, bạn không biết phải làm gì. Nhưng rồi ai đó xuất hiện. Không phải vì bạn nhờ, mà vì họ thấy bạn cần. Đó là khoảnh khắc bạn nhận ra: mình không đơn độc.\n\nCâu chuyện về cô bé Hoa và chiếc diều bị mắc trên cây giống như một phép ẩn dụ nhỏ về cuộc sống — đôi khi gió mạnh hơn bạn tưởng, đôi khi bạn buông tay dù không muốn. Nhưng khi cả xóm cùng mang thang, mang gậy, mang cả rổ ra giúp — bạn hiểu rằng sức mạnh thật sự nằm ở những người xung quanh.\n\n12 từ vựng trong câu chuyện này — từ kite đến grateful — là những từ đơn giản mà bạn đã gặp trước đây. Lần này, bạn sẽ gặp lại chúng trong một câu chuyện có hồn, để chúng trở thành một phần tự nhiên trong tiếng Anh của bạn.",
    "preview": {
        "text": "What happens when the wind takes something you love? In this gentle story, you follow Hoa, a young girl in Vietnam, as she loses her beloved kite in a tall tree. She cannot climb high enough to reach it. The kite is stuck on a branch, and the string hangs just out of reach. But then her neighbors come — one by one, each bringing something to help. A ladder, a stick, a rope, and even a basket. Through this simple tale of community and kindness, you will revisit 12 familiar English words: kite, wind, string, field, climb, branch, neighbor, ladder, careful, reach, stuck, and grateful. The story unfolds across two chapters and a full combined reading, with each session building on the last. By the end, you will have read a complete narrative of over 500 words and practiced these everyday words in a way that feels natural and memorable."
    },
    "learningSessions": [
        {
            "title": "Chương 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu câu chuyện",
                    "description": "Chào mừng bạn đến với The Lost Kite — giới thiệu câu chuyện và 6 từ vựng đầu tiên.",
                    "data": {
                        "text": "Chào mừng bạn đến với The Lost Kite — Chiếc Diều Bị Mất. Đây là một câu chuyện nhẹ nhàng về một cô bé tên Hoa và chiếc diều yêu quý của cô ấy. Câu chuyện xảy ra ở một con phố nhỏ ở Việt Nam, nơi mọi người quen biết nhau và sẵn sàng giúp đỡ.\n\nTrong chương đầu tiên, bạn sẽ theo Hoa ra cánh đồng để thả diều. Bạn sẽ gặp 6 từ vựng tiếng Anh quen thuộc — những từ bạn có thể đã thấy trước đây, nhưng lần này bạn sẽ gặp chúng trong một câu chuyện có cảm xúc.\n\nTừ đầu tiên là kite — danh từ — nghĩa là con diều. Kite là đồ chơi bay trên trời, được giữ bằng một sợi dây. Ví dụ: 'Hoa loves her red and yellow kite.' Trong câu chuyện, chiếc kite này rất đặc biệt vì bà ngoại Hoa đã làm nó.\n\nTừ thứ hai là wind — danh từ — nghĩa là gió. Wind là luồng không khí di chuyển tự nhiên. Ví dụ: 'The wind is strong today.' Trong câu chuyện, wind vừa là bạn vừa là kẻ thù — nó giúp diều bay cao, nhưng cũng mang diều đi mất.\n\nTừ thứ ba là string — danh từ — nghĩa là sợi dây. String là dây mỏng dùng để buộc hoặc giữ đồ vật. Ví dụ: 'She holds the string tight.' Trong câu chuyện, Hoa cố giữ string nhưng gió quá mạnh.\n\nTừ thứ tư là field — danh từ — nghĩa là cánh đồng, bãi cỏ rộng. Field là khu đất trống rộng lớn. Ví dụ: 'The children play in the field.' Trong câu chuyện, Hoa thả diều ở một field rộng gần nhà.\n\nTừ thứ năm là climb — động từ — nghĩa là leo, trèo. Climb là khi bạn dùng tay và chân để đi lên cao. Ví dụ: 'He climbs the tree to get the ball.' Trong câu chuyện, Hoa không thể climb cái cây vì nó quá cao.\n\nTừ cuối cùng là branch — danh từ — nghĩa là cành cây. Branch là phần mọc ra từ thân cây. Ví dụ: 'The bird sits on a branch.' Trong câu chuyện, chiếc diều bị mắc vào một branch cao.\n\nSáu từ đã sẵn sàng! Hãy xem flashcard rồi đọc chương đầu tiên về Hoa và chiếc diều của cô ấy nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Thả diều",
                    "description": "Học 6 từ: kite, wind, string, field, climb, branch",
                    "data": {
                        "vocabList": ["kite", "wind", "string", "field", "climb", "branch"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Thả diều",
                    "description": "Học 6 từ: kite, wind, string, field, climb, branch",
                    "data": {
                        "vocabList": ["kite", "wind", "string", "field", "climb", "branch"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chương 1 — Chiếc diều bay đi",
                    "description": "Hoa takes her kite to the field, but the wind carries it into a tall tree.",
                    "data": {"text": s1_reading}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chương 1 — Chiếc diều bay đi",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": s1_reading}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chương 1 — Chiếc diều bay đi",
                    "description": "Hoa takes her kite to the field, but the wind carries it into a tall tree.",
                    "data": {"text": s1_reading}
                },
            ]
        },
        {
            "title": "Chương 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu chương 2",
                    "description": "Ôn lại chương 1 và giới thiệu 6 từ vựng mới về sự giúp đỡ của hàng xóm.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với chương 2 của The Lost Kite! Trong chương trước, bạn đã theo Hoa ra cánh đồng thả diều. Gió rất mạnh — wind thổi chiếc kite bay cao trên field. Nhưng rồi gió quá mạnh, string tuột khỏi tay Hoa, và chiếc diều bay vào một cái cây cao. Nó bị mắc trên một branch cao. Hoa không thể climb lên lấy. Cô bé ngồi dưới gốc cây, buồn bã.\n\nBây giờ, trong chương 2, hàng xóm của Hoa sẽ đến giúp. Bạn sẽ học thêm 6 từ vựng mới: neighbor, ladder, careful, reach, stuck, và grateful.\n\nTừ đầu tiên là neighbor — danh từ — nghĩa là hàng xóm, người láng giềng. Neighbor là người sống gần nhà bạn. Ví dụ: 'Bác Tám is a kind neighbor.' Trong câu chuyện, nhiều neighbor đến giúp Hoa lấy diều.\n\nTừ thứ hai là ladder — danh từ — nghĩa là cái thang. Ladder là dụng cụ có bậc để bạn leo lên cao. Ví dụ: 'He uses a ladder to fix the roof.' Trong câu chuyện, Bác Tám mang một ladder đến, nhưng nó không đủ cao.\n\nTừ thứ ba là careful — tính từ — nghĩa là cẩn thận. Careful là khi bạn làm mọi thứ chậm rãi và chú ý để không gặp nguy hiểm. Ví dụ: 'Be careful when you cross the street.' Trong câu chuyện, Anh Đức leo thang rất careful.\n\nTừ thứ tư là reach — động từ — nghĩa là với tới, chạm tới. Reach là khi bạn duỗi tay ra để chạm vào thứ gì đó. Ví dụ: 'She cannot reach the top shelf.' Trong câu chuyện, Hoa không thể reach chiếc diều vì nó quá cao.\n\nTừ thứ năm là stuck — tính từ — nghĩa là bị mắc kẹt, bị kẹt. Stuck là khi một thứ gì đó không thể di chuyển được. Ví dụ: 'The door is stuck — I cannot open it.' Trong câu chuyện, chiếc diều bị stuck giữa hai cành cây.\n\nTừ cuối cùng là grateful — tính từ — nghĩa là biết ơn. Grateful là cảm giác ấm áp khi ai đó giúp bạn. Ví dụ: 'I am grateful for my family.' Trong câu chuyện, Hoa rất grateful khi hàng xóm giúp cô lấy lại diều.\n\nSáu từ mới đã sẵn sàng! Hãy xem flashcard rồi đọc chương 2 — xem hàng xóm giúp Hoa như thế nào nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Hàng xóm giúp đỡ",
                    "description": "Học 6 từ: neighbor, ladder, careful, reach, stuck, grateful",
                    "data": {
                        "vocabList": ["neighbor", "ladder", "careful", "reach", "stuck", "grateful"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Hàng xóm giúp đỡ",
                    "description": "Học 6 từ: neighbor, ladder, careful, reach, stuck, grateful",
                    "data": {
                        "vocabList": ["neighbor", "ladder", "careful", "reach", "stuck", "grateful"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chương 2 — Hàng xóm đến giúp",
                    "description": "The neighbors come together to rescue Hoa's kite from the tree.",
                    "data": {"text": s2_reading}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chương 2 — Hàng xóm đến giúp",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": s2_reading}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chương 2 — Hàng xóm đến giúp",
                    "description": "The neighbors come together to rescue Hoa's kite from the tree.",
                    "data": {"text": s2_reading}
                },
            ]
        },
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Ôn lại tất cả 12 từ vựng từ hai chương trước.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã đọc xong hai chương của The Lost Kite. Hãy cùng ôn lại 12 từ vựng nhé.\n\nTrong chương 1, bạn học 6 từ cùng Hoa ngoài cánh đồng: kite là con diều — chiếc diều đỏ vàng mà bà ngoại Hoa làm. Wind là gió — gió mạnh đã mang diều đi. String là sợi dây — Hoa cố giữ string nhưng nó tuột khỏi tay. Field là cánh đồng — nơi Hoa thả diều mỗi cuối tuần. Climb là leo trèo — Hoa không thể climb cái cây cao. Branch là cành cây — chiếc diều mắc trên branch.\n\nTrong chương 2, bạn học 6 từ khi hàng xóm đến giúp: neighbor là hàng xóm — Bác Tám, Chị Lan, Anh Đức, và bé Tùng đều là neighbor tốt. Ladder là cái thang — Bác Tám mang ladder đến nhưng nó không đủ cao. Careful là cẩn thận — Anh Đức leo thang rất careful. Reach là với tới — Hoa không thể reach chiếc diều. Stuck là bị mắc kẹt — chiếc diều bị stuck giữa hai cành cây. Grateful là biết ơn — Hoa rất grateful khi mọi người giúp đỡ.\n\nBây giờ, bạn sẽ ôn lại tất cả 12 từ qua flashcard và bài tập. Sau đó, trong phần cuối, bạn sẽ đọc toàn bộ câu chuyện từ đầu đến cuối. Sẵn sàng chưa?"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: kite, wind, string, field, climb, branch, neighbor, ladder, careful, reach, stuck, grateful",
                    "data": {
                        "vocabList": all_words
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: kite, wind, string, field, climb, branch, neighbor, ladder, careful, reach, stuck, grateful",
                    "data": {
                        "vocabList": all_words
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 12 từ: kite, wind, string, field, climb, branch, neighbor, ladder, careful, reach, stuck, grateful",
                    "data": {
                        "vocabList": all_words
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Ôn tập câu chuyện",
                    "description": "Nghe tóm tắt câu chuyện và theo dõi.",
                    "data": {"text": s3_readalong}
                },
            ]
        },
        {
            "title": "Toàn bộ câu chuyện",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc toàn bộ",
                    "description": "Giới thiệu bài đọc cuối cùng — toàn bộ câu chuyện The Lost Kite.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của The Lost Kite! Bạn đã đi qua một hành trình thật đẹp. Trong chương 1, bạn theo Hoa ra cánh đồng thả diều và chứng kiến chiếc diều bị gió cuốn vào cây. Trong chương 2, bạn thấy hàng xóm cùng nhau giúp Hoa lấy lại diều. Trong phần ôn tập, bạn đã luyện lại tất cả 12 từ vựng.\n\nBây giờ, bạn sẽ đọc toàn bộ câu chuyện từ đầu đến cuối — một phiên bản đầy đủ và chi tiết hơn. Câu chuyện này dùng tất cả 12 từ bạn đã học: kite, wind, string, field, climb, branch, neighbor, ladder, careful, reach, stuck, và grateful. Hãy đọc chậm, thưởng thức từng câu, và cảm nhận câu chuyện nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Toàn bộ câu chuyện — The Lost Kite",
                    "description": "The complete story of Hoa, her kite, and the neighbors who helped.",
                    "data": {"text": s4_full_story}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Toàn bộ câu chuyện",
                    "description": "Nghe toàn bộ câu chuyện và theo dõi.",
                    "data": {"text": s4_full_story}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Toàn bộ câu chuyện — The Lost Kite",
                    "description": "The complete story of Hoa, her kite, and the neighbors who helped.",
                    "data": {"text": s4_full_story}
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay — farewell tone: quiet_awe.",
                    "data": {
                        "text": "Bạn đã hoàn thành The Lost Kite — Chiếc Diều Bị Mất. Hãy ngồi lại một chút. Hít thở. Và cảm nhận câu chuyện bạn vừa đọc.\n\nMột cô bé, một chiếc diều, một cơn gió, và cả một xóm nhỏ. Đôi khi những câu chuyện đơn giản nhất lại chạm vào lòng người sâu nhất. Bạn đã đọc về Hoa — một đứa trẻ yêu chiếc diều của mình, mất nó, và tìm lại nó nhờ lòng tốt của những người xung quanh.\n\nHãy cùng nhìn lại 12 từ vựng bạn đã gặp trong câu chuyện.\n\nKite — con diều. Chiếc diều đỏ vàng mà bà ngoại Hoa làm bằng tay. Câu mới: On windy afternoons, children in the village gather in the field to fly their kites together.\n\nWind — gió. Gió mang diều lên cao, nhưng cũng mang nó đi xa. Câu mới: The wind carried the smell of flowers from the garden across the whole street.\n\nString — sợi dây. Sợi dây mỏng nối Hoa với chiếc diều trên trời. Câu mới: She tied a string around the gift box and made a small bow on top.\n\nField — cánh đồng. Nơi rộng lớn, xanh mướt, nơi Hoa thả diều mỗi cuối tuần. Câu mới: After the rain, the field was covered with tiny white flowers.\n\nClimb — leo trèo. Hoa không thể leo cái cây cao, nhưng Anh Đức đã leo thang giúp cô. Câu mới: The cat climbed to the top of the bookshelf and refused to come down.\n\nBranch — cành cây. Chiếc diều mắc giữa hai cành cây dày. Câu mới: A small bird built its nest on the highest branch of the old mango tree.\n\nNeighbor — hàng xóm. Bác Tám, Chị Lan, Anh Đức, bé Tùng — mỗi người mang một thứ đến giúp. Câu mới: A good neighbor does not wait to be asked — they just show up when you need them.\n\nLadder — cái thang. Bác Tám mang thang đến, dù nó không đủ cao. Câu mới: He leaned the ladder against the wall and climbed up to paint the window frame.\n\nCareful — cẩn thận. Anh Đức leo từng bậc thang, chậm rãi và cẩn thận. Câu mới: Be careful with that glass — it belonged to your grandmother.\n\nReach — với tới. Hoa nhảy lên nhưng không thể reach chiếc diều. Câu mới: If you stand on your toes, you can just reach the top shelf.\n\nStuck — bị mắc kẹt. Chiếc diều bị stuck, không thể tự rơi xuống. Câu mới: The key was stuck in the lock, and no matter how hard she turned it, it would not move.\n\nGrateful — biết ơn. Hoa ôm chiếc diều và cảm thấy grateful — không chỉ vì diều, mà vì những con người tốt bụng. Câu mới: She wrote a small thank-you note to each neighbor because she was truly grateful for their help.\n\nBạn biết không, có một khoảnh khắc trong câu chuyện mà tôi rất thích. Đó là khi bé Tùng mang cái rổ đến. Cậu bé không biết rổ giúp gì, nhưng cậu muốn có mặt. Cậu muốn là một phần. Và đó chính là điều đẹp nhất — không phải bạn có gì để cho, mà là bạn có mặt.\n\nBà ngoại Hoa nói: 'Con diều cần gió và một trái tim tốt.' Gió sẽ luôn thổi. Cuộc sống sẽ luôn có lúc bạn mất thứ gì đó. Nhưng khi bạn có những người tốt bên cạnh, bạn không bao giờ thực sự mất.\n\nCảm ơn bạn đã đọc câu chuyện này cùng tôi. Tôi hy vọng bạn mang theo một chút ấm áp từ câu chuyện của Hoa. Hẹn gặp lại bạn trong câu chuyện tiếp theo."
                    }
                }
            ]
        }
    ]
}

# ── Validate ──
print("Validating content...")
validate_reader(content)
print("  ✓ reader structure OK")
validate_content_type_tags(content)
print("  ✓ contentTypeTags OK")
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
print(f"Level: beginner | Skill: reader | Content: story")
print(f"Words: 12 (2 groups of 6)")
