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

# Curriculum #45: Freakonomics: Hidden Side of Sports
# Level: intermediate | Skill focus: balanced_skills | Content type: ["podcast"]
# Topic: Sports | 18 words (3 groups of 6), 5 sessions, bilingual (vi-en)
# Description tone: surprising_fact (different from previous podcast tones: provocative_question, empathetic_observation, bold_declaration, vivid_scenario)
# Farewell tone: quiet_awe (different from previous: introspective_guide, warm_accountability, team_building_energy, practical_momentum)
# W1: athlete, endurance, strategy, recruit, salary, transfer
# W2: statistic, underdog, rivalry, momentum, penalty, referee
# W3: sponsor, league, draft, incentive, performance, scout

content = {
    "title": "Freakonomics: Hidden Side of Sports",
    "contentTypeTags": ["podcast"],
    "description": "MỘT CẦU THỦ BÓNG ĐÁ TRUNG BÌNH KIẾM ĐƯỢC NHIỀU TIỀN HƠN TRONG 1 TUẦN SO VỚI MỘT GIÁO VIÊN KIẾM ĐƯỢC TRONG 1 NĂM — VÀ LÝ DO KHÔNG PHẢI LÀ ĐIỀU BẠN NGHĨ.\n\nThể thao không chỉ là chạy nhanh hơn, nhảy cao hơn, hay ghi nhiều bàn hơn. Đằng sau mỗi trận đấu là một hệ thống kinh tế phức tạp — nơi mà salary của một athlete có thể lên đến hàng triệu đô la, nơi mà một quyết định transfer sai lầm có thể phá sản cả một câu lạc bộ, và nơi mà statistic quyết định ai được recruit và ai bị loại.\n\nHãy nghĩ về điều này: tại sao một đội bóng underdog đôi khi lại thắng đội mạnh nhất giải? Tại sao các sponsor chi hàng tỷ đô la cho một logo trên áo đấu? Tại sao hệ thống draft ở Mỹ lại hoạt động ngược với logic thông thường — đội tệ nhất được chọn trước? Câu trả lời nằm ở incentive — động lực kinh tế ẩn giấu đằng sau mọi quyết định trong thể thao.\n\nHai nhân vật Tùng và Linh sẽ dẫn bạn vào thế giới này — từ cách các scout tìm kiếm tài năng trẻ, đến cách referee ảnh hưởng đến kết quả trận đấu, đến cách momentum có thể thay đổi cục diện trong vài phút. Tùng là fan cuồng bóng đá và thường nghe podcast Freakonomics, còn Linh là sinh viên kinh tế muốn hiểu tại sao thể thao lại là một ngành kinh doanh khổng lồ.\n\n18 từ vựng trong bài học này — từ athlete đến scout — sẽ giúp bạn nói về thể thao, kinh tế, và chiến lược bằng tiếng Anh một cách tự tin và sắc sảo.",
    "preview": {
        "text": "Did you know that professional sports teams spend more on data analysts than on some of their players? In this podcast-inspired lesson, you will learn 18 English words about the hidden economics of sports: athlete, endurance, strategy, recruit, salary, transfer, statistic, underdog, rivalry, momentum, penalty, referee, sponsor, league, draft, incentive, performance, and scout. Follow Tùng and Linh as they explore how money, data, and strategy shape athletic competition — from the billion-dollar transfer market to the surprising economics of underdog victories. Tùng is a passionate football fan who listens to Freakonomics podcasts, while Linh studies economics and wants to understand why sports is such a massive global business. Through three conversational reading passages, a full review session, and a final combined reading, you will discover the hidden forces behind every game. By the end, you will be able to discuss sports economics, analyze team strategies, and explain how incentives drive athletic performance — all in English."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Chào mừng — Kinh tế học ẩn giấu trong thể thao",
                    "description": "Giới thiệu chủ đề kinh tế thể thao và tổng quan bài học.",
                    "data": {
                        "text": "Chào mừng bạn đến với Freakonomics: Hidden Side of Sports — bài học podcast tiếng Anh về một chủ đề mà hầu hết mọi người không nghĩ đến khi xem thể thao: tiền bạc, dữ liệu, và chiến lược kinh tế. Bạn có biết rằng ngành thể thao chuyên nghiệp toàn cầu có giá trị hơn 500 tỷ đô la không? Và phần lớn số tiền đó không đến từ bán vé — mà từ hợp đồng truyền hình, tài trợ, và chuyển nhượng cầu thủ.\n\nBài học này có 18 từ vựng chia thành 3 phần. Trong phần 1, bạn sẽ học 6 từ đầu tiên: athlete, endurance, strategy, recruit, salary, và transfer. Đây là những từ về con người và tiền bạc trong thể thao — ai chơi, họ được trả bao nhiêu, và cách họ di chuyển giữa các đội."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Dạy 6 từ vựng: athlete, endurance, strategy, recruit, salary, transfer.",
                    "data": {
                        "text": "Hãy cùng tìm hiểu 6 từ vựng đầu tiên nhé.\n\nTừ đầu tiên là athlete — danh từ — nghĩa là vận động viên. Athlete là người thi đấu thể thao ở trình độ cao — có thể là chuyên nghiệp hoặc nghiệp dư. Ví dụ: 'A professional athlete trains for several hours every day to maintain peak physical condition.' Trong bài đọc, Tùng giải thích rằng một athlete hàng đầu không chỉ cần tài năng mà còn cần kỷ luật và chiến lược.\n\nTừ thứ hai là endurance — danh từ — nghĩa là sức bền, sự chịu đựng. Endurance là khả năng duy trì nỗ lực thể chất hoặc tinh thần trong thời gian dài. Ví dụ: 'Marathon runners need incredible endurance to complete a forty-two-kilometer race.' Trong bài đọc, Linh ngạc nhiên khi biết rằng endurance không chỉ là thể chất — mà còn là tinh thần.\n\nTừ thứ ba là strategy — danh từ — nghĩa là chiến lược. Strategy là kế hoạch dài hạn để đạt được mục tiêu — trong thể thao, đó là cách một đội chơi để thắng. Ví dụ: 'The coach changed the team's strategy at halftime, and they scored three goals in the second half.' Trong bài đọc, Tùng giải thích rằng strategy trong thể thao hiện đại phụ thuộc rất nhiều vào dữ liệu và phân tích.\n\nTừ thứ tư là recruit — động từ và danh từ — nghĩa là tuyển dụng, chiêu mộ. Recruit là khi một đội tìm kiếm và ký hợp đồng với cầu thủ mới. Ví dụ: 'Top football clubs recruit talented young players from academies all over the world.' Trong bài đọc, Tùng kể về cách các câu lạc bộ lớn recruit cầu thủ từ khi họ mới 14-15 tuổi.\n\nTừ thứ năm là salary — danh từ — nghĩa là lương, tiền lương. Salary là số tiền một người được trả định kỳ cho công việc của họ. Ví dụ: 'The average salary of a Premier League footballer is over three million pounds per year.' Trong bài đọc, Linh so sánh salary của vận động viên với salary của các nghề khác và đặt câu hỏi về sự công bằng.\n\nTừ cuối cùng là transfer — danh từ và động từ — nghĩa là chuyển nhượng. Transfer trong thể thao là khi một cầu thủ chuyển từ đội này sang đội khác, thường với một khoản phí lớn. Ví dụ: 'The transfer of Neymar from Barcelona to Paris Saint-Germain cost two hundred and twenty-two million euros.' Trong bài đọc, Tùng giải thích rằng thị trường transfer là nơi tiền bạc và thể thao giao nhau rõ ràng nhất.\n\nSáu từ đầu tiên đã sẵn sàng! Hãy bắt đầu với flashcard, rồi đọc cuộc trò chuyện giữa Tùng và Linh về tiền bạc trong thể thao nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Con người và tiền bạc trong thể thao",
                    "description": "Học 6 từ: athlete, endurance, strategy, recruit, salary, transfer",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Con người và tiền bạc trong thể thao",
                    "description": "Học 6 từ: athlete, endurance, strategy, recruit, salary, transfer",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Con người và tiền bạc trong thể thao",
                    "description": "Học 6 từ: athlete, endurance, strategy, recruit, salary, transfer",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Con người và tiền bạc trong thể thao",
                    "description": "Học 6 từ: athlete, endurance, strategy, recruit, salary, transfer",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 1",
                    "description": "Giới thiệu ngữ pháp và cách dùng từ vựng trong ngữ cảnh bài đọc.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc cuộc trò chuyện giữa Tùng và Linh. Tùng là fan cuồng bóng đá và thường nghe podcast Freakonomics — chương trình nổi tiếng về kinh tế học ứng dụng vào đời sống. Linh là sinh viên kinh tế và muốn hiểu tại sao thể thao lại là một ngành kinh doanh khổng lồ. Trong bài đọc này, họ nói về tiền bạc trong thể thao — salary khổng lồ của các athlete, thị trường transfer, và cách các đội recruit tài năng. Hãy chú ý cách các từ athlete, endurance, strategy, recruit, salary, và transfer được dùng trong câu chuyện nhé. Một điểm ngữ pháp quan trọng: khi so sánh số liệu, chúng ta dùng cấu trúc so sánh hơn — ví dụ 'earns more than' hoặc 'costs three times as much as.' Hãy đọc chậm và chú ý nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Tiền bạc và chuyển nhượng trong thể thao",
                    "description": "Tùng and Linh discuss the economics of athlete salaries and the transfer market.",
                    "data": {
                        "text": "Tùng and Linh are sitting in a café near their university in Ho Chi Minh City. Tùng is watching a football match on his phone. He suddenly puts it down and shakes his head.\n\n'They just announced the transfer fee,' he says. 'One hundred and fifty million euros for one player. That is insane.'\n\nLinh looks up from her economics textbook. 'How much does that player earn in salary?'\n\n'About four hundred thousand euros per week,' Tùng says.\n\n'Per week?' Linh is shocked. 'That is more than most Vietnamese people earn in ten years. Why do athletes get paid so much?'\n\n'That is actually a great economics question,' Tùng says. 'I listened to a Freakonomics podcast about this. The answer is not about fairness — it is about supply and demand. There are billions of people who can teach or drive a taxi, but there are maybe a few hundred people in the world who can play football at the highest level. The salary reflects how rare the skill is, not how important the job is.'\n\n'So it is scarcity that drives the price up,' Linh says, connecting it to her studies.\n\n'Exactly. And the transfer market makes it even more extreme,' Tùng explains. 'When a club wants to recruit a player from another club, they have to pay a transfer fee. The better the athlete, the higher the fee. Clubs are essentially buying the right to employ that player. It is like a stock market, but for people.'\n\n'That sounds uncomfortable,' Linh says.\n\n'It is controversial,' Tùng agrees. 'But here is what makes it interesting from an economics perspective. The clubs that spend the most on transfers do not always win. Some of the most successful teams in history built their strategy around developing young players instead of buying expensive ones. Barcelona's famous academy, La Masia, produced Messi, Xavi, and Iniesta — players who would have cost hundreds of millions on the transfer market.'\n\n'So the strategy of investing in youth development can be more effective than just spending money?' Linh asks.\n\n'Sometimes, yes,' Tùng says. 'And that is where endurance comes in — not just physical endurance on the pitch, but organizational endurance. Building a youth academy takes ten to fifteen years before you see results. Most club owners want to win now, so they spend big on transfers instead. The clubs with the patience and endurance to invest long-term often build something more sustainable.'\n\n'It is like the difference between short-term and long-term investment strategies in economics,' Linh says.\n\nTùng smiles. 'See? Sports and economics are not so different after all.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Tiền bạc và chuyển nhượng trong thể thao",
                    "description": "Tùng and Linh discuss the economics of athlete salaries and the transfer market.",
                    "data": {
                        "text": "Tùng and Linh are sitting in a café near their university in Ho Chi Minh City. Tùng is watching a football match on his phone. He suddenly puts it down and shakes his head.\n\n'They just announced the transfer fee,' he says. 'One hundred and fifty million euros for one player. That is insane.'\n\nLinh looks up from her economics textbook. 'How much does that player earn in salary?'\n\n'About four hundred thousand euros per week,' Tùng says.\n\n'Per week?' Linh is shocked. 'That is more than most Vietnamese people earn in ten years. Why do athletes get paid so much?'\n\n'That is actually a great economics question,' Tùng says. 'I listened to a Freakonomics podcast about this. The answer is not about fairness — it is about supply and demand. There are billions of people who can teach or drive a taxi, but there are maybe a few hundred people in the world who can play football at the highest level. The salary reflects how rare the skill is, not how important the job is.'\n\n'So it is scarcity that drives the price up,' Linh says, connecting it to her studies.\n\n'Exactly. And the transfer market makes it even more extreme,' Tùng explains. 'When a club wants to recruit a player from another club, they have to pay a transfer fee. The better the athlete, the higher the fee. Clubs are essentially buying the right to employ that player. It is like a stock market, but for people.'\n\n'That sounds uncomfortable,' Linh says.\n\n'It is controversial,' Tùng agrees. 'But here is what makes it interesting from an economics perspective. The clubs that spend the most on transfers do not always win. Some of the most successful teams in history built their strategy around developing young players instead of buying expensive ones. Barcelona's famous academy, La Masia, produced Messi, Xavi, and Iniesta — players who would have cost hundreds of millions on the transfer market.'\n\n'So the strategy of investing in youth development can be more effective than just spending money?' Linh asks.\n\n'Sometimes, yes,' Tùng says. 'And that is where endurance comes in — not just physical endurance on the pitch, but organizational endurance. Building a youth academy takes ten to fifteen years before you see results. Most club owners want to win now, so they spend big on transfers instead. The clubs with the patience and endurance to invest long-term often build something more sustainable.'\n\n'It is like the difference between short-term and long-term investment strategies in economics,' Linh says.\n\nTùng smiles. 'See? Sports and economics are not so different after all.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Tiền bạc và chuyển nhượng trong thể thao",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Tùng and Linh are sitting in a café near their university in Ho Chi Minh City. Tùng is watching a football match on his phone. He suddenly puts it down and shakes his head.\n\n'They just announced the transfer fee,' he says. 'One hundred and fifty million euros for one player. That is insane.'\n\nLinh looks up from her economics textbook. 'How much does that player earn in salary?'\n\n'About four hundred thousand euros per week,' Tùng says.\n\n'Per week?' Linh is shocked. 'That is more than most Vietnamese people earn in ten years. Why do athletes get paid so much?'\n\n'That is actually a great economics question,' Tùng says. 'I listened to a Freakonomics podcast about this. The answer is not about fairness — it is about supply and demand. There are billions of people who can teach or drive a taxi, but there are maybe a few hundred people in the world who can play football at the highest level. The salary reflects how rare the skill is, not how important the job is.'\n\n'So it is scarcity that drives the price up,' Linh says, connecting it to her studies.\n\n'Exactly. And the transfer market makes it even more extreme,' Tùng explains. 'When a club wants to recruit a player from another club, they have to pay a transfer fee. The better the athlete, the higher the fee. Clubs are essentially buying the right to employ that player. It is like a stock market, but for people.'\n\n'That sounds uncomfortable,' Linh says.\n\n'It is controversial,' Tùng agrees. 'But here is what makes it interesting from an economics perspective. The clubs that spend the most on transfers do not always win. Some of the most successful teams in history built their strategy around developing young players instead of buying expensive ones. Barcelona's famous academy, La Masia, produced Messi, Xavi, and Iniesta — players who would have cost hundreds of millions on the transfer market.'\n\n'So the strategy of investing in youth development can be more effective than just spending money?' Linh asks.\n\n'Sometimes, yes,' Tùng says. 'And that is where endurance comes in — not just physical endurance on the pitch, but organizational endurance. Building a youth academy takes ten to fifteen years before you see results. Most club owners want to win now, so they spend big on transfers instead. The clubs with the patience and endurance to invest long-term often build something more sustainable.'\n\n'It is like the difference between short-term and long-term investment strategies in economics,' Linh says.\n\nTùng smiles. 'See? Sports and economics are not so different after all.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Tiền bạc trong thể thao",
                    "description": "Viết câu sử dụng từ vựng về vận động viên, lương, và chuyển nhượng.",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer"],
                        "items": [
                            {
                                "targetVocab": "athlete",
                                "prompt": "Hãy dùng từ 'athlete' để viết một câu về vận động viên chuyên nghiệp. Ví dụ: A world-class athlete must balance intense physical training with proper nutrition and mental preparation."
                            },
                            {
                                "targetVocab": "endurance",
                                "prompt": "Hãy dùng từ 'endurance' để viết một câu về sức bền. Ví dụ: Long-distance swimmers develop extraordinary endurance through years of training in open water."
                            },
                            {
                                "targetVocab": "strategy",
                                "prompt": "Hãy dùng từ 'strategy' để viết một câu về chiến lược trong thể thao. Ví dụ: The coach developed a defensive strategy that helped the team win five consecutive matches."
                            },
                            {
                                "targetVocab": "recruit",
                                "prompt": "Hãy dùng từ 'recruit' để viết một câu về tuyển dụng cầu thủ. Ví dụ: European football clubs often recruit talented teenagers from South America and Africa."
                            },
                            {
                                "targetVocab": "salary",
                                "prompt": "Hãy dùng từ 'salary' để viết một câu về tiền lương trong thể thao. Ví dụ: The debate about whether athlete salaries are too high has been going on for decades."
                            },
                            {
                                "targetVocab": "transfer",
                                "prompt": "Hãy dùng từ 'transfer' để viết một câu về chuyển nhượng. Ví dụ: The record-breaking transfer shocked the football world and changed how clubs value their players."
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
                    "title": "Chào mừng phần 2 — Dữ liệu và bất ngờ trên sân",
                    "description": "Ôn lại phần 1 và giới thiệu chủ đề dữ liệu và kết quả bất ngờ trong thể thao.",
                    "data": {
                        "text": "Chào mừng bạn trở lại với phần 2 của Freakonomics: Hidden Side of Sports! Trong phần trước, bạn đã học 6 từ vựng về con người và tiền bạc trong thể thao: athlete là vận động viên — người thi đấu ở trình độ cao. Endurance là sức bền — khả năng duy trì nỗ lực trong thời gian dài. Strategy là chiến lược — kế hoạch để giành chiến thắng. Recruit là tuyển dụng — tìm kiếm và ký hợp đồng với cầu thủ mới. Salary là lương — số tiền vận động viên được trả. Và transfer là chuyển nhượng — khi cầu thủ chuyển từ đội này sang đội khác.\n\nBạn cũng đã đọc cuộc trò chuyện giữa Tùng và Linh — Tùng giải thích tại sao athlete được trả salary cao và cách thị trường transfer hoạt động.\n\nBây giờ, chúng ta sẽ đi vào thế giới dữ liệu và những bất ngờ trên sân cỏ. Bạn sẽ học 6 từ mới: statistic, underdog, rivalry, momentum, penalty, và referee."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Dạy 6 từ vựng: statistic, underdog, rivalry, momentum, penalty, referee.",
                    "data": {
                        "text": "Hãy cùng học 6 từ mới nhé.\n\nTừ đầu tiên là statistic — danh từ — nghĩa là số liệu thống kê. Statistic là dữ liệu số được thu thập và phân tích để tìm ra xu hướng hoặc đưa ra quyết định. Ví dụ: 'Modern football teams use statistics to analyze every aspect of a player's performance on the pitch.' Trong bài đọc, Tùng giải thích rằng statistic đã thay đổi hoàn toàn cách các đội bóng đưa ra quyết định.\n\nTừ thứ hai là underdog — danh từ — nghĩa là đội yếu hơn, người ở thế bất lợi. Underdog là đội hoặc cá nhân được dự đoán sẽ thua — nhưng đôi khi lại tạo ra bất ngờ lớn. Ví dụ: 'Leicester City was the ultimate underdog — a small club that won the Premier League against all odds.' Trong bài đọc, Linh hỏi tại sao mọi người lại yêu thích những câu chuyện underdog.\n\nTừ thứ ba là rivalry — danh từ — nghĩa là sự cạnh tranh, kình địch. Rivalry là mối quan hệ cạnh tranh gay gắt giữa hai đội hoặc hai cá nhân kéo dài qua nhiều năm. Ví dụ: 'The rivalry between Real Madrid and Barcelona is one of the most intense in all of sports.' Trong bài đọc, Tùng nói rằng rivalry tạo ra cảm xúc mạnh mẽ và thu hút hàng triệu khán giả.\n\nTừ thứ tư là momentum — danh từ — nghĩa là đà, xung lượng. Momentum trong thể thao là khi một đội đang chơi tốt và có cảm giác không thể bị ngăn cản — mọi thứ đều thuận lợi. Ví dụ: 'After scoring two quick goals, the team had all the momentum and their opponents could not stop them.' Trong bài đọc, Tùng giải thích rằng momentum là yếu tố tâm lý mạnh mẽ nhất trong thể thao.\n\nTừ thứ năm là penalty — danh từ — nghĩa là hình phạt, quả phạt đền. Penalty là hình phạt khi một cầu thủ vi phạm luật — trong bóng đá, đó là cú sút từ chấm phạt đền. Ví dụ: 'The referee awarded a penalty after the defender fouled the striker inside the box.' Trong bài đọc, Linh tìm hiểu rằng penalty có thể thay đổi kết quả của cả một giải đấu.\n\nTừ cuối cùng là referee — danh từ — nghĩa là trọng tài. Referee là người điều khiển trận đấu, đảm bảo các cầu thủ tuân thủ luật lệ. Ví dụ: 'The referee's decision to award a last-minute penalty changed the outcome of the entire championship.' Trong bài đọc, Tùng kể về nghiên cứu cho thấy referee cũng bị ảnh hưởng bởi áp lực từ khán giả.\n\nSáu từ mới đã sẵn sàng! Hãy luyện flashcard rồi đọc về dữ liệu và bất ngờ trong thể thao nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Dữ liệu và bất ngờ trên sân",
                    "description": "Học 6 từ: statistic, underdog, rivalry, momentum, penalty, referee",
                    "data": {
                        "vocabList": ["statistic", "underdog", "rivalry", "momentum", "penalty", "referee"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Dữ liệu và bất ngờ trên sân",
                    "description": "Học 6 từ: statistic, underdog, rivalry, momentum, penalty, referee",
                    "data": {
                        "vocabList": ["statistic", "underdog", "rivalry", "momentum", "penalty", "referee"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Dữ liệu và bất ngờ trên sân",
                    "description": "Học 6 từ: statistic, underdog, rivalry, momentum, penalty, referee",
                    "data": {
                        "vocabList": ["statistic", "underdog", "rivalry", "momentum", "penalty", "referee"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Dữ liệu và bất ngờ trên sân",
                    "description": "Học 6 từ: statistic, underdog, rivalry, momentum, penalty, referee",
                    "data": {
                        "vocabList": ["statistic", "underdog", "rivalry", "momentum", "penalty", "referee"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 2",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về dữ liệu và bất ngờ trong thể thao.",
                    "data": {
                        "text": "Bạn đã luyện xong flashcard rồi! Bây giờ hãy đọc cuộc trò chuyện tiếp theo giữa Tùng và Linh. Lần này, họ nói về cách dữ liệu và statistic đang thay đổi thể thao, tại sao underdog đôi khi thắng, và vai trò của referee trong kết quả trận đấu. Hãy chú ý cách các từ statistic, underdog, rivalry, momentum, penalty, và referee xuất hiện trong câu chuyện. Một điểm ngữ pháp: khi nói về xác suất và khả năng, chúng ta dùng 'likely to,' 'tend to,' và 'more likely than' — ví dụ 'underdogs are more likely to win when they play at home' hoặc 'referees tend to favor the home team.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Khi dữ liệu thay đổi cuộc chơi",
                    "description": "Tùng and Linh explore how statistics, underdogs, and referee decisions shape sports outcomes.",
                    "data": {
                        "text": "The next evening, Tùng and Linh meet again at the café. Tùng has his laptop open with charts and graphs on the screen.\n\n'I have been researching something fascinating,' he says. 'Did you know that statistics have completely changed how sports teams make decisions?'\n\n'Like the Moneyball story?' Linh asks. 'I read about that in my economics class.'\n\n'Exactly like Moneyball,' Tùng says. 'In two thousand and two, the Oakland Athletics baseball team used statistics to find undervalued players that other teams ignored. They could not afford expensive stars, so they used data to identify players whose statistics showed they were better than people thought. The team became incredibly competitive despite having one of the lowest budgets in the league.'\n\n'So they were the underdog who used data to compete with richer teams,' Linh says.\n\n'Precisely. And that underdog story inspired every sport to embrace data analysis,' Tùng explains. 'Now, football clubs have entire departments dedicated to statistics. They track everything — how far each player runs, how many passes they complete, where they shoot from, even how they perform under pressure. A single statistic can determine whether a club spends fifty million on a player or walks away.'\n\n'That takes some of the romance out of sports,' Linh says.\n\n'Maybe,' Tùng admits. 'But here is something the data cannot fully explain — momentum. When a team scores a goal, something changes psychologically. The players feel more confident, the crowd gets louder, and suddenly everything seems to go their way. Momentum is real, but it is almost impossible to measure with statistics alone.'\n\n'And what about rivalry?' Linh asks. 'Does data show that rivalry matches are different?'\n\n'Absolutely,' Tùng says. 'Research shows that players perform differently in rivalry matches. Their heart rates are higher, they make more aggressive tackles, and they take more risks. The rivalry between Vietnam and Thailand in Southeast Asian football is a perfect example — both teams play with an intensity that you do not see in regular matches.'\n\n'What about referees?' Linh asks. 'Are they affected by the atmosphere too?'\n\n'This is one of the most interesting findings,' Tùng says. 'Studies show that referees are more likely to award a penalty to the home team when the stadium is full. The crowd pressure affects their decisions — even though they try to be neutral. One study found that referees add more injury time when the home team is losing, giving them more chances to score.'\n\n'So the referee is not as objective as we think?' Linh asks.\n\n'No one is completely objective,' Tùng says. 'That is why some leagues are introducing video technology — to reduce the human bias in penalty decisions and other critical calls. But even with technology, the human element remains. And honestly, that is what makes sports exciting. The underdog can still win. Momentum can shift in seconds. A single penalty can change everything.'\n\nLinh nods thoughtfully. 'Sports really is a laboratory for human behavior.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Khi dữ liệu thay đổi cuộc chơi",
                    "description": "Tùng and Linh explore how statistics, underdogs, and referee decisions shape sports outcomes.",
                    "data": {
                        "text": "The next evening, Tùng and Linh meet again at the café. Tùng has his laptop open with charts and graphs on the screen.\n\n'I have been researching something fascinating,' he says. 'Did you know that statistics have completely changed how sports teams make decisions?'\n\n'Like the Moneyball story?' Linh asks. 'I read about that in my economics class.'\n\n'Exactly like Moneyball,' Tùng says. 'In two thousand and two, the Oakland Athletics baseball team used statistics to find undervalued players that other teams ignored. They could not afford expensive stars, so they used data to identify players whose statistics showed they were better than people thought. The team became incredibly competitive despite having one of the lowest budgets in the league.'\n\n'So they were the underdog who used data to compete with richer teams,' Linh says.\n\n'Precisely. And that underdog story inspired every sport to embrace data analysis,' Tùng explains. 'Now, football clubs have entire departments dedicated to statistics. They track everything — how far each player runs, how many passes they complete, where they shoot from, even how they perform under pressure. A single statistic can determine whether a club spends fifty million on a player or walks away.'\n\n'That takes some of the romance out of sports,' Linh says.\n\n'Maybe,' Tùng admits. 'But here is something the data cannot fully explain — momentum. When a team scores a goal, something changes psychologically. The players feel more confident, the crowd gets louder, and suddenly everything seems to go their way. Momentum is real, but it is almost impossible to measure with statistics alone.'\n\n'And what about rivalry?' Linh asks. 'Does data show that rivalry matches are different?'\n\n'Absolutely,' Tùng says. 'Research shows that players perform differently in rivalry matches. Their heart rates are higher, they make more aggressive tackles, and they take more risks. The rivalry between Vietnam and Thailand in Southeast Asian football is a perfect example — both teams play with an intensity that you do not see in regular matches.'\n\n'What about referees?' Linh asks. 'Are they affected by the atmosphere too?'\n\n'This is one of the most interesting findings,' Tùng says. 'Studies show that referees are more likely to award a penalty to the home team when the stadium is full. The crowd pressure affects their decisions — even though they try to be neutral. One study found that referees add more injury time when the home team is losing, giving them more chances to score.'\n\n'So the referee is not as objective as we think?' Linh asks.\n\n'No one is completely objective,' Tùng says. 'That is why some leagues are introducing video technology — to reduce the human bias in penalty decisions and other critical calls. But even with technology, the human element remains. And honestly, that is what makes sports exciting. The underdog can still win. Momentum can shift in seconds. A single penalty can change everything.'\n\nLinh nods thoughtfully. 'Sports really is a laboratory for human behavior.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Khi dữ liệu thay đổi cuộc chơi",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "The next evening, Tùng and Linh meet again at the café. Tùng has his laptop open with charts and graphs on the screen.\n\n'I have been researching something fascinating,' he says. 'Did you know that statistics have completely changed how sports teams make decisions?'\n\n'Like the Moneyball story?' Linh asks. 'I read about that in my economics class.'\n\n'Exactly like Moneyball,' Tùng says. 'In two thousand and two, the Oakland Athletics baseball team used statistics to find undervalued players that other teams ignored. They could not afford expensive stars, so they used data to identify players whose statistics showed they were better than people thought. The team became incredibly competitive despite having one of the lowest budgets in the league.'\n\n'So they were the underdog who used data to compete with richer teams,' Linh says.\n\n'Precisely. And that underdog story inspired every sport to embrace data analysis,' Tùng explains. 'Now, football clubs have entire departments dedicated to statistics. They track everything — how far each player runs, how many passes they complete, where they shoot from, even how they perform under pressure. A single statistic can determine whether a club spends fifty million on a player or walks away.'\n\n'That takes some of the romance out of sports,' Linh says.\n\n'Maybe,' Tùng admits. 'But here is something the data cannot fully explain — momentum. When a team scores a goal, something changes psychologically. The players feel more confident, the crowd gets louder, and suddenly everything seems to go their way. Momentum is real, but it is almost impossible to measure with statistics alone.'\n\n'And what about rivalry?' Linh asks. 'Does data show that rivalry matches are different?'\n\n'Absolutely,' Tùng says. 'Research shows that players perform differently in rivalry matches. Their heart rates are higher, they make more aggressive tackles, and they take more risks. The rivalry between Vietnam and Thailand in Southeast Asian football is a perfect example — both teams play with an intensity that you do not see in regular matches.'\n\n'What about referees?' Linh asks. 'Are they affected by the atmosphere too?'\n\n'This is one of the most interesting findings,' Tùng says. 'Studies show that referees are more likely to award a penalty to the home team when the stadium is full. The crowd pressure affects their decisions — even though they try to be neutral. One study found that referees add more injury time when the home team is losing, giving them more chances to score.'\n\n'So the referee is not as objective as we think?' Linh asks.\n\n'No one is completely objective,' Tùng says. 'That is why some leagues are introducing video technology — to reduce the human bias in penalty decisions and other critical calls. But even with technology, the human element remains. And honestly, that is what makes sports exciting. The underdog can still win. Momentum can shift in seconds. A single penalty can change everything.'\n\nLinh nods thoughtfully. 'Sports really is a laboratory for human behavior.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Dữ liệu và bất ngờ trong thể thao",
                    "description": "Viết câu sử dụng từ vựng về thống kê, đội yếu, và trọng tài.",
                    "data": {
                        "vocabList": ["statistic", "underdog", "rivalry", "momentum", "penalty", "referee"],
                        "items": [
                            {
                                "targetVocab": "statistic",
                                "prompt": "Hãy dùng từ 'statistic' để viết một câu về dữ liệu trong thể thao. Ví dụ: One surprising statistic shows that teams who score first win the match about seventy percent of the time."
                            },
                            {
                                "targetVocab": "underdog",
                                "prompt": "Hãy dùng từ 'underdog' để viết một câu về đội yếu hơn. Ví dụ: The underdog team shocked everyone by defeating the defending champions in the semifinal."
                            },
                            {
                                "targetVocab": "rivalry",
                                "prompt": "Hãy dùng từ 'rivalry' để viết một câu về sự cạnh tranh. Ví dụ: The rivalry between the two tennis players has produced some of the greatest matches in the history of the sport."
                            },
                            {
                                "targetVocab": "momentum",
                                "prompt": "Hãy dùng từ 'momentum' để viết một câu về đà chiến thắng. Ví dụ: The team lost all their momentum after the captain was injured in the first half."
                            },
                            {
                                "targetVocab": "penalty",
                                "prompt": "Hãy dùng từ 'penalty' để viết một câu về quả phạt đền. Ví dụ: Missing a penalty in the final minute of a World Cup match is every footballer's worst nightmare."
                            },
                            {
                                "targetVocab": "referee",
                                "prompt": "Hãy dùng từ 'referee' để viết một câu về trọng tài. Ví dụ: The referee made a controversial decision that changed the outcome of the championship match."
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
                    "title": "Chào mừng phần 3 — Hệ thống và động lực kinh tế",
                    "description": "Ôn lại phần 1-2 và giới thiệu chủ đề hệ thống tổ chức thể thao.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần 3 — phần cuối cùng trước khi ôn tập! Bạn đã đi được hai phần ba chặng đường rồi. Hãy cùng nhìn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ về con người và tiền bạc: athlete là vận động viên, endurance là sức bền, strategy là chiến lược, recruit là tuyển dụng, salary là lương, và transfer là chuyển nhượng. Trong phần 2, bạn học 6 từ về dữ liệu và bất ngờ: statistic là số liệu thống kê, underdog là đội yếu hơn, rivalry là sự cạnh tranh, momentum là đà chiến thắng, penalty là hình phạt, và referee là trọng tài.\n\nBây giờ, trong phần 3, chúng ta sẽ nói về hệ thống tổ chức thể thao — từ cách các league hoạt động, đến hệ thống draft độc đáo của Mỹ, và cách sponsor và incentive ảnh hưởng đến mọi quyết định. Bạn sẽ học 6 từ cuối cùng: sponsor, league, draft, incentive, performance, và scout."
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Dạy 6 từ vựng: sponsor, league, draft, incentive, performance, scout.",
                    "data": {
                        "text": "Hãy cùng học 6 từ cuối cùng nhé.\n\nTừ đầu tiên là sponsor — danh từ và động từ — nghĩa là nhà tài trợ, tài trợ. Sponsor là công ty hoặc tổ chức trả tiền để tên hoặc logo của họ xuất hiện trên áo đấu, sân vận động, hoặc sự kiện thể thao. Ví dụ: 'Nike sponsors some of the most famous athletes in the world, paying them millions to wear their products.' Trong bài đọc, Linh tìm hiểu rằng tiền từ sponsor chiếm phần lớn doanh thu của các câu lạc bộ thể thao.\n\nTừ thứ hai là league — danh từ — nghĩa là giải đấu, liên đoàn. League là tổ chức quản lý một nhóm đội thi đấu với nhau theo lịch trình cố định — như Premier League, NBA, hoặc V-League. Ví dụ: 'The English Premier League is the most watched football league in the world, with billions of viewers every season.' Trong bài đọc, Tùng so sánh cách các league ở châu Âu và Mỹ hoạt động khác nhau.\n\nTừ thứ ba là draft — danh từ và động từ — nghĩa là tuyển chọn, vòng chọn. Draft là hệ thống đặc biệt ở thể thao Mỹ, nơi các đội lần lượt chọn cầu thủ trẻ — đội tệ nhất mùa trước được chọn trước. Ví dụ: 'The NBA draft is one of the most exciting events in American sports because it can transform a struggling team overnight.' Trong bài đọc, Tùng giải thích rằng hệ thống draft được thiết kế để tạo sự cân bằng trong league.\n\nTừ thứ tư là incentive — danh từ — nghĩa là động lực, phần thưởng khuyến khích. Incentive là thứ thúc đẩy ai đó hành động theo một cách nhất định — có thể là tiền, danh tiếng, hoặc cơ hội. Ví dụ: 'Many player contracts include performance incentives — bonuses paid when the player scores a certain number of goals.' Trong bài đọc, Linh phân tích cách incentive ảnh hưởng đến hành vi của cầu thủ, huấn luyện viên, và cả chủ sở hữu câu lạc bộ.\n\nTừ thứ năm là performance — danh từ — nghĩa là thành tích, hiệu suất. Performance là mức độ tốt hay xấu mà ai đó thực hiện công việc hoặc thi đấu. Ví dụ: 'The coach evaluates each player's performance after every match using detailed video analysis.' Trong bài đọc, Tùng nói rằng performance được đo lường bằng hàng trăm chỉ số khác nhau trong thể thao hiện đại.\n\nTừ cuối cùng là scout — danh từ và động từ — nghĩa là tuyển trạch viên, tìm kiếm tài năng. Scout là người đi khắp nơi để tìm kiếm và đánh giá cầu thủ trẻ có tiềm năng cho câu lạc bộ. Ví dụ: 'A football scout discovered Cristiano Ronaldo playing for a small club in Madeira when he was just twelve years old.' Trong bài đọc, Tùng kể về cách các scout hiện đại kết hợp quan sát trực tiếp với phân tích dữ liệu.\n\nBạn đã có đủ 18 từ vựng rồi! Hãy luyện flashcard rồi đọc phần cuối của cuộc trò chuyện nhé."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Hệ thống và động lực kinh tế",
                    "description": "Học 6 từ: sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Hệ thống và động lực kinh tế",
                    "description": "Học 6 từ: sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Hệ thống và động lực kinh tế",
                    "description": "Học 6 từ: sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Hệ thống và động lực kinh tế",
                    "description": "Học 6 từ: sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc phần 3",
                    "description": "Giới thiệu ngữ pháp và ngữ cảnh bài đọc về hệ thống tổ chức thể thao.",
                    "data": {
                        "text": "Tuyệt vời! Bạn đã luyện xong flashcard rồi. Bây giờ hãy đọc phần cuối của cuộc trò chuyện giữa Tùng và Linh. Lần này, họ nói về cách các league được tổ chức, hệ thống draft ở Mỹ, và cách sponsor và incentive định hình thể thao hiện đại. Hãy chú ý cách các từ sponsor, league, draft, incentive, performance, và scout được dùng trong câu chuyện. Một điểm ngữ pháp: khi giải thích cách hệ thống hoạt động, chúng ta dùng thì hiện tại đơn với bị động — ví dụ 'players are drafted by teams' hoặc 'performance is measured using data.' Hãy đọc và tìm những cấu trúc này nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Hệ thống draft, tài trợ, và tuyển trạch viên",
                    "description": "Tùng and Linh discuss how leagues, drafts, sponsors, and scouts shape modern sports.",
                    "data": {
                        "text": "On the weekend, Tùng and Linh are watching an NBA game together at Tùng's apartment. During a commercial break, Linh notices something.\n\n'Every surface in that stadium has a sponsor logo on it,' she says. 'The court, the jerseys, even the halftime show. How much money do sponsors spend on sports?'\n\n'Billions,' Tùng says. 'Global sports sponsorship is worth over sixty billion dollars a year. Companies like Nike, Adidas, and Emirates pay enormous amounts to have their names associated with popular teams and athletes. A single sponsor deal with a top league can cost hundreds of millions.'\n\n'But why?' Linh asks. 'Does putting a logo on a jersey really sell more shoes?'\n\n'The research says yes,' Tùng says. 'When people feel emotionally connected to a team, they are more likely to buy products from that team's sponsor. It is not rational — it is emotional. And sports create some of the strongest emotions in the world. That is the incentive for sponsors — access to passionate, loyal audiences.'\n\n'Speaking of incentives,' Linh says, 'I have been reading about the American draft system. It seems completely backwards. The worst team gets to pick the best new players first?'\n\n'That is exactly how it works,' Tùng says. 'In American sports leagues like the NBA and NFL, young players enter the draft after college. The team with the worst performance in the previous season gets the first pick. The idea is to create competitive balance — so the same teams do not win every year.'\n\n'But does that not create a perverse incentive?' Linh asks. 'If losing gives you a better draft pick, why would a bad team try to win?'\n\nTùng laughs. 'You are thinking like a true economist. That is exactly what happens sometimes. It is called tanking — when a team deliberately performs poorly to get a higher draft pick. The leagues have tried to create rules against it, but the incentive structure makes it tempting.'\n\n'How do teams decide who to draft?' Linh asks.\n\n'That is where scouts come in,' Tùng says. 'Every professional team employs scouts — people whose job is to travel around the country, watch young players, and evaluate their potential. A good scout can identify a future star years before anyone else notices them. They watch hundreds of games, analyze performance data, and write detailed reports.'\n\n'So a scout is like a talent detective,' Linh says.\n\n'Exactly. And modern scouts combine traditional observation with advanced statistics,' Tùng explains. 'They might watch a player live to assess their attitude and leadership, but they also study the player's performance metrics — speed, accuracy, decision-making under pressure. The best scouts understand both the numbers and the human qualities that statistics cannot capture.'\n\n'It sounds like the entire sports industry is built on incentives,' Linh says. 'Sponsors have incentives to associate with winning teams. Teams have incentives to find the best players. Players have incentives to perform well for higher salaries. And scouts have incentives to discover talent before anyone else.'\n\n'Now you understand why Freakonomics loves sports,' Tùng says. 'Every league is an economic system with its own rules, incentives, and unintended consequences. Understanding the economics helps you understand the game at a much deeper level.'"
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Hệ thống draft, tài trợ, và tuyển trạch viên",
                    "description": "Tùng and Linh discuss how leagues, drafts, sponsors, and scouts shape modern sports.",
                    "data": {
                        "text": "On the weekend, Tùng and Linh are watching an NBA game together at Tùng's apartment. During a commercial break, Linh notices something.\n\n'Every surface in that stadium has a sponsor logo on it,' she says. 'The court, the jerseys, even the halftime show. How much money do sponsors spend on sports?'\n\n'Billions,' Tùng says. 'Global sports sponsorship is worth over sixty billion dollars a year. Companies like Nike, Adidas, and Emirates pay enormous amounts to have their names associated with popular teams and athletes. A single sponsor deal with a top league can cost hundreds of millions.'\n\n'But why?' Linh asks. 'Does putting a logo on a jersey really sell more shoes?'\n\n'The research says yes,' Tùng says. 'When people feel emotionally connected to a team, they are more likely to buy products from that team's sponsor. It is not rational — it is emotional. And sports create some of the strongest emotions in the world. That is the incentive for sponsors — access to passionate, loyal audiences.'\n\n'Speaking of incentives,' Linh says, 'I have been reading about the American draft system. It seems completely backwards. The worst team gets to pick the best new players first?'\n\n'That is exactly how it works,' Tùng says. 'In American sports leagues like the NBA and NFL, young players enter the draft after college. The team with the worst performance in the previous season gets the first pick. The idea is to create competitive balance — so the same teams do not win every year.'\n\n'But does that not create a perverse incentive?' Linh asks. 'If losing gives you a better draft pick, why would a bad team try to win?'\n\nTùng laughs. 'You are thinking like a true economist. That is exactly what happens sometimes. It is called tanking — when a team deliberately performs poorly to get a higher draft pick. The leagues have tried to create rules against it, but the incentive structure makes it tempting.'\n\n'How do teams decide who to draft?' Linh asks.\n\n'That is where scouts come in,' Tùng says. 'Every professional team employs scouts — people whose job is to travel around the country, watch young players, and evaluate their potential. A good scout can identify a future star years before anyone else notices them. They watch hundreds of games, analyze performance data, and write detailed reports.'\n\n'So a scout is like a talent detective,' Linh says.\n\n'Exactly. And modern scouts combine traditional observation with advanced statistics,' Tùng explains. 'They might watch a player live to assess their attitude and leadership, but they also study the player's performance metrics — speed, accuracy, decision-making under pressure. The best scouts understand both the numbers and the human qualities that statistics cannot capture.'\n\n'It sounds like the entire sports industry is built on incentives,' Linh says. 'Sponsors have incentives to associate with winning teams. Teams have incentives to find the best players. Players have incentives to perform well for higher salaries. And scouts have incentives to discover talent before anyone else.'\n\n'Now you understand why Freakonomics loves sports,' Tùng says. 'Every league is an economic system with its own rules, incentives, and unintended consequences. Understanding the economics helps you understand the game at a much deeper level.'"
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Hệ thống draft, tài trợ, và tuyển trạch viên",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "On the weekend, Tùng and Linh are watching an NBA game together at Tùng's apartment. During a commercial break, Linh notices something.\n\n'Every surface in that stadium has a sponsor logo on it,' she says. 'The court, the jerseys, even the halftime show. How much money do sponsors spend on sports?'\n\n'Billions,' Tùng says. 'Global sports sponsorship is worth over sixty billion dollars a year. Companies like Nike, Adidas, and Emirates pay enormous amounts to have their names associated with popular teams and athletes. A single sponsor deal with a top league can cost hundreds of millions.'\n\n'But why?' Linh asks. 'Does putting a logo on a jersey really sell more shoes?'\n\n'The research says yes,' Tùng says. 'When people feel emotionally connected to a team, they are more likely to buy products from that team's sponsor. It is not rational — it is emotional. And sports create some of the strongest emotions in the world. That is the incentive for sponsors — access to passionate, loyal audiences.'\n\n'Speaking of incentives,' Linh says, 'I have been reading about the American draft system. It seems completely backwards. The worst team gets to pick the best new players first?'\n\n'That is exactly how it works,' Tùng says. 'In American sports leagues like the NBA and NFL, young players enter the draft after college. The team with the worst performance in the previous season gets the first pick. The idea is to create competitive balance — so the same teams do not win every year.'\n\n'But does that not create a perverse incentive?' Linh asks. 'If losing gives you a better draft pick, why would a bad team try to win?'\n\nTùng laughs. 'You are thinking like a true economist. That is exactly what happens sometimes. It is called tanking — when a team deliberately performs poorly to get a higher draft pick. The leagues have tried to create rules against it, but the incentive structure makes it tempting.'\n\n'How do teams decide who to draft?' Linh asks.\n\n'That is where scouts come in,' Tùng says. 'Every professional team employs scouts — people whose job is to travel around the country, watch young players, and evaluate their potential. A good scout can identify a future star years before anyone else notices them. They watch hundreds of games, analyze performance data, and write detailed reports.'\n\n'So a scout is like a talent detective,' Linh says.\n\n'Exactly. And modern scouts combine traditional observation with advanced statistics,' Tùng explains. 'They might watch a player live to assess their attitude and leadership, but they also study the player's performance metrics — speed, accuracy, decision-making under pressure. The best scouts understand both the numbers and the human qualities that statistics cannot capture.'\n\n'It sounds like the entire sports industry is built on incentives,' Linh says. 'Sponsors have incentives to associate with winning teams. Teams have incentives to find the best players. Players have incentives to perform well for higher salaries. And scouts have incentives to discover talent before anyone else.'\n\n'Now you understand why Freakonomics loves sports,' Tùng says. 'Every league is an economic system with its own rules, incentives, and unintended consequences. Understanding the economics helps you understand the game at a much deeper level.'"
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Hệ thống và động lực kinh tế",
                    "description": "Viết câu sử dụng từ vựng về tài trợ, giải đấu, và tuyển trạch viên.",
                    "data": {
                        "vocabList": ["sponsor", "league", "draft", "incentive", "performance", "scout"],
                        "items": [
                            {
                                "targetVocab": "sponsor",
                                "prompt": "Hãy dùng từ 'sponsor' để viết một câu về nhà tài trợ thể thao. Ví dụ: The team's main sponsor paid twenty million dollars to have their logo on the front of the jersey."
                            },
                            {
                                "targetVocab": "league",
                                "prompt": "Hãy dùng từ 'league' để viết một câu về giải đấu. Ví dụ: The Vietnamese football league has grown significantly in popularity over the past decade."
                            },
                            {
                                "targetVocab": "draft",
                                "prompt": "Hãy dùng từ 'draft' để viết một câu về hệ thống tuyển chọn. Ví dụ: Being selected first in the draft is both an honor and enormous pressure for a young athlete."
                            },
                            {
                                "targetVocab": "incentive",
                                "prompt": "Hãy dùng từ 'incentive' để viết một câu về động lực kinh tế. Ví dụ: Financial incentives in player contracts encourage athletes to maintain high performance throughout the season."
                            },
                            {
                                "targetVocab": "performance",
                                "prompt": "Hãy dùng từ 'performance' để viết một câu về thành tích. Ví dụ: The team's poor performance in the first half of the season led to the coach being replaced."
                            },
                            {
                                "targetVocab": "scout",
                                "prompt": "Hãy dùng từ 'scout' để viết một câu về tuyển trạch viên. Ví dụ: A talented scout can spot a future champion in a teenager that everyone else has overlooked."
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
                        "text": "Chúc mừng bạn! Bạn đã học xong tất cả 18 từ vựng về kinh tế học ẩn giấu trong thể thao. Đây là một thành tích tuyệt vời — hãy cùng ôn lại nhanh nhé.\n\nTrong phần 1, bạn học 6 từ về con người và tiền bạc: athlete là vận động viên — người thi đấu thể thao ở trình độ cao. Endurance là sức bền — khả năng duy trì nỗ lực trong thời gian dài, cả thể chất lẫn tinh thần. Strategy là chiến lược — kế hoạch dài hạn để đạt mục tiêu. Recruit là tuyển dụng — tìm kiếm và ký hợp đồng với cầu thủ mới. Salary là lương — số tiền vận động viên được trả, phản ánh sự khan hiếm của tài năng. Transfer là chuyển nhượng — khi cầu thủ chuyển đội với khoản phí khổng lồ.\n\nTrong phần 2, bạn học 6 từ về dữ liệu và bất ngờ: statistic là số liệu thống kê — dữ liệu số dùng để phân tích và đưa ra quyết định. Underdog là đội yếu hơn — đội được dự đoán sẽ thua nhưng đôi khi tạo bất ngờ. Rivalry là sự cạnh tranh — mối quan hệ kình địch gay gắt giữa hai đội. Momentum là đà chiến thắng — khi mọi thứ đều thuận lợi và không thể bị ngăn cản. Penalty là hình phạt — quả phạt đền có thể thay đổi kết quả trận đấu. Referee là trọng tài — người điều khiển trận đấu, cũng bị ảnh hưởng bởi áp lực.\n\nTrong phần 3, bạn học 6 từ cuối: sponsor là nhà tài trợ — công ty trả tiền để gắn tên với thể thao. League là giải đấu — tổ chức quản lý các đội thi đấu. Draft là vòng tuyển chọn — hệ thống đặc biệt ở Mỹ cho đội yếu chọn trước. Incentive là động lực kinh tế — thứ thúc đẩy hành vi của mọi người trong thể thao. Performance là thành tích — mức độ tốt hay xấu khi thi đấu. Scout là tuyển trạch viên — người tìm kiếm tài năng trẻ cho câu lạc bộ.\n\nBây giờ, bạn sẽ ôn lại tất cả 18 từ qua flashcard và bài tập viết. Sẵn sàng chưa? Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: athlete, endurance, strategy, recruit, salary, transfer, statistic, underdog, rivalry, momentum, penalty, referee, sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer", "statistic", "underdog", "rivalry", "momentum", "penalty", "referee", "sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: athlete, endurance, strategy, recruit, salary, transfer, statistic, underdog, rivalry, momentum, penalty, referee, sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer", "statistic", "underdog", "rivalry", "momentum", "penalty", "referee", "sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: athlete, endurance, strategy, recruit, salary, transfer, statistic, underdog, rivalry, momentum, penalty, referee, sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer", "statistic", "underdog", "rivalry", "momentum", "penalty", "referee", "sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập tất cả từ vựng",
                    "description": "Ôn tập 18 từ: athlete, endurance, strategy, recruit, salary, transfer, statistic, underdog, rivalry, momentum, penalty, referee, sponsor, league, draft, incentive, performance, scout",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer", "statistic", "underdog", "rivalry", "momentum", "penalty", "referee", "sponsor", "league", "draft", "incentive", "performance", "scout"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập kinh tế thể thao",
                    "description": "Viết câu ôn tập sử dụng tất cả 18 từ vựng về kinh tế thể thao.",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer", "statistic", "underdog", "rivalry", "momentum", "penalty", "referee", "sponsor", "league", "draft", "incentive", "performance", "scout"],
                        "items": [
                            {
                                "targetVocab": "athlete",
                                "prompt": "Hãy dùng từ 'athlete' để viết một câu về cuộc sống của vận động viên. Ví dụ: The life of a professional athlete involves constant travel, strict diets, and the pressure to perform at the highest level every week."
                            },
                            {
                                "targetVocab": "endurance",
                                "prompt": "Hãy dùng từ 'endurance' để viết một câu về sức bền trong thể thao hoặc cuộc sống. Ví dụ: Building a successful career requires the same kind of endurance that marathon runners develop through years of training."
                            },
                            {
                                "targetVocab": "strategy",
                                "prompt": "Hãy dùng từ 'strategy' để viết một câu về chiến lược. Ví dụ: A good business strategy, like a good sports strategy, requires understanding your competitors and playing to your strengths."
                            },
                            {
                                "targetVocab": "recruit",
                                "prompt": "Hãy dùng từ 'recruit' để viết một câu về tuyển dụng. Ví dụ: Technology companies recruit talented engineers the same way football clubs recruit talented players — by offering high salaries and great working conditions."
                            },
                            {
                                "targetVocab": "salary",
                                "prompt": "Hãy dùng từ 'salary' để viết một câu về lương. Ví dụ: The gap between athlete salaries and average worker salaries has grown dramatically over the past fifty years."
                            },
                            {
                                "targetVocab": "transfer",
                                "prompt": "Hãy dùng từ 'transfer' để viết một câu về chuyển nhượng. Ví dụ: The summer transfer window creates excitement and anxiety for football fans who wonder which players their team will buy or sell."
                            },
                            {
                                "targetVocab": "statistic",
                                "prompt": "Hãy dùng từ 'statistic' để viết một câu về số liệu thống kê. Ví dụ: Behind every exciting sports moment, there is a statistic that helps explain why it happened."
                            },
                            {
                                "targetVocab": "underdog",
                                "prompt": "Hãy dùng từ 'underdog' để viết một câu về đội yếu hơn. Ví dụ: People love underdog stories because they remind us that hard work and determination can overcome any disadvantage."
                            },
                            {
                                "targetVocab": "rivalry",
                                "prompt": "Hãy dùng từ 'rivalry' để viết một câu về sự cạnh tranh. Ví dụ: A healthy rivalry between companies, like between sports teams, pushes both sides to innovate and improve."
                            },
                            {
                                "targetVocab": "momentum",
                                "prompt": "Hãy dùng từ 'momentum' để viết một câu về đà phát triển. Ví dụ: Once a startup gains momentum with its first successful product, it becomes much easier to attract investors and customers."
                            },
                            {
                                "targetVocab": "penalty",
                                "prompt": "Hãy dùng từ 'penalty' để viết một câu về hình phạt. Ví dụ: In both sports and business, the penalty for breaking the rules should be severe enough to discourage cheating."
                            },
                            {
                                "targetVocab": "referee",
                                "prompt": "Hãy dùng từ 'referee' để viết một câu về trọng tài. Ví dụ: A good referee, like a good judge, must make difficult decisions under pressure while remaining fair to both sides."
                            },
                            {
                                "targetVocab": "sponsor",
                                "prompt": "Hãy dùng từ 'sponsor' để viết một câu về tài trợ. Ví dụ: Finding the right sponsor can transform a small sports club by providing the funding needed to develop facilities and recruit better players."
                            },
                            {
                                "targetVocab": "league",
                                "prompt": "Hãy dùng từ 'league' để viết một câu về giải đấu. Ví dụ: The structure of a league determines how competitive it is — some leagues promote equality while others allow the richest teams to dominate."
                            },
                            {
                                "targetVocab": "draft",
                                "prompt": "Hãy dùng từ 'draft' để viết một câu về hệ thống tuyển chọn. Ví dụ: The draft system was designed to give every team a fair chance, but it has created unexpected incentives that sometimes work against its original purpose."
                            },
                            {
                                "targetVocab": "incentive",
                                "prompt": "Hãy dùng từ 'incentive' để viết một câu về động lực. Ví dụ: Understanding incentives is the key to understanding why people behave the way they do — in sports, business, and everyday life."
                            },
                            {
                                "targetVocab": "performance",
                                "prompt": "Hãy dùng từ 'performance' để viết một câu về thành tích. Ví dụ: Measuring performance with data has become essential in modern sports, but numbers alone cannot capture everything that makes a great player."
                            },
                            {
                                "targetVocab": "scout",
                                "prompt": "Hãy dùng từ 'scout' để viết một câu về tuyển trạch viên. Ví dụ: The best scouts combine data analysis with human intuition to find players who have both talent and the right character."
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
                    "description": "Giới thiệu bài đọc cuối cùng kết hợp tất cả 18 từ vựng về kinh tế thể thao.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của Freakonomics: Hidden Side of Sports! Bạn đã đi một chặng đường ấn tượng. Trong phần 1, bạn học về con người và tiền bạc với 6 từ: athlete, endurance, strategy, recruit, salary, transfer. Trong phần 2, bạn khám phá dữ liệu và bất ngờ với 6 từ: statistic, underdog, rivalry, momentum, penalty, referee. Trong phần 3, bạn tìm hiểu hệ thống tổ chức với 6 từ: sponsor, league, draft, incentive, performance, scout. Trong phần ôn tập, bạn đã luyện lại tất cả 18 từ.\n\nBây giờ, bạn sẽ đọc một bài tổng hợp — Tùng và Linh gặp lại nhau và chia sẻ những gì họ đã học được về mặt ẩn giấu của thể thao. Bài đọc này dùng tất cả 18 từ vựng bạn đã học. Hãy đọc chậm, thưởng thức câu chuyện, và chú ý cách mỗi từ được dùng trong ngữ cảnh thực tế nhé!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Mặt ẩn giấu của thể thao — Khi kinh tế học gặp sân cỏ",
                    "description": "Tùng and Linh reflect on the complete picture of sports economics — from player salaries to league systems.",
                    "data": {
                        "text": "A month has passed since Tùng and Linh started their conversations about sports economics. They are sitting in the university library, preparing for Linh's economics presentation. She has chosen to present on the economics of professional sports.\n\n'I cannot believe how much I have learned,' Linh says. 'A month ago, I thought sports was just about athletes running around a field. Now I see it as one of the most complex economic systems in the world.'\n\nTùng smiles. 'Tell me what you are going to present.'\n\n'I want to start with the people,' Linh says. 'Every professional sport begins with an athlete — someone with extraordinary physical talent and endurance. But talent alone is not enough. The modern sports industry has created an entire ecosystem around finding and developing that talent. Scouts travel the world looking for the next star, watching thousands of young players and evaluating their performance using both observation and statistics.'\n\n'Good start,' Tùng says. 'What about the money side?'\n\n'That is where it gets really interesting,' Linh continues. 'When a scout identifies a promising player, the club has to recruit them — and that costs money. Player salaries in top leagues are enormous because the supply of world-class talent is extremely limited. And when a player is already under contract with another club, the transfer market comes into play. Clubs pay hundreds of millions in transfer fees, essentially treating players as financial assets.'\n\n'And the strategy behind all of this?' Tùng asks.\n\n'Every decision is driven by strategy and incentives,' Linh says. 'Clubs develop long-term strategies for building competitive teams. Some invest in youth academies, which requires endurance and patience. Others spend big on transfers for immediate results. The incentive structure of each league shapes these decisions. In American sports, the draft system gives the worst-performing team the first pick of new talent — which creates competitive balance but also creates a perverse incentive to lose on purpose.'\n\n'What about the emotional side of sports?' Tùng asks. 'The things that statistics cannot capture?'\n\n'That is my favorite part,' Linh says. 'Rivalry is one of the most powerful forces in sports. When two teams with a long history of competition face each other, the intensity is completely different. Players take more risks, crowds are louder, and the atmosphere is electric. And then there is momentum — that mysterious force that can shift a game in minutes. One goal, one great play, and suddenly the underdog believes they can win. The statistics say they should lose, but momentum does not care about statistics.'\n\n'And the referee?' Tùng asks.\n\n'Referees are supposed to be neutral, but research shows they are human,' Linh says. 'They are more likely to award a penalty to the home team when the crowd is large and loud. Their decisions can change the outcome of an entire season. That is why technology like VAR has been introduced — to reduce human bias in critical moments.'\n\n'What about the business side — sponsors and leagues?' Tùng asks.\n\n'Sponsors are the financial engine of modern sports,' Linh says. 'They pay billions to associate their brands with popular teams and athletes. The incentive is clear — sports fans are emotionally loyal, and that loyalty transfers to the products their favorite teams endorse. Leagues organize the competition and set the rules that govern everything — from how much teams can spend on salaries to how the draft works. Each league is essentially a self-contained economic system with its own incentives and consequences.'\n\n'I think your professor is going to be impressed,' Tùng says.\n\nLinh closes her notebook. 'You know what surprised me most? It is not the money or the statistics. It is how sports reveals fundamental truths about human behavior. We respond to incentives. We root for the underdog. We are biased even when we try to be fair. We build rivalries because competition brings out our best performance. Sports is not just entertainment — it is a mirror that shows us who we really are.'\n\nTùng nods. 'And that is exactly what Freakonomics is about — using economics to understand the hidden side of everything. Even the games we play.'\n\n'Especially the games we play,' Linh says with a smile."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Mặt ẩn giấu của thể thao — Khi kinh tế học gặp sân cỏ",
                    "description": "Tùng and Linh reflect on the complete picture of sports economics — from player salaries to league systems.",
                    "data": {
                        "text": "A month has passed since Tùng and Linh started their conversations about sports economics. They are sitting in the university library, preparing for Linh's economics presentation. She has chosen to present on the economics of professional sports.\n\n'I cannot believe how much I have learned,' Linh says. 'A month ago, I thought sports was just about athletes running around a field. Now I see it as one of the most complex economic systems in the world.'\n\nTùng smiles. 'Tell me what you are going to present.'\n\n'I want to start with the people,' Linh says. 'Every professional sport begins with an athlete — someone with extraordinary physical talent and endurance. But talent alone is not enough. The modern sports industry has created an entire ecosystem around finding and developing that talent. Scouts travel the world looking for the next star, watching thousands of young players and evaluating their performance using both observation and statistics.'\n\n'Good start,' Tùng says. 'What about the money side?'\n\n'That is where it gets really interesting,' Linh continues. 'When a scout identifies a promising player, the club has to recruit them — and that costs money. Player salaries in top leagues are enormous because the supply of world-class talent is extremely limited. And when a player is already under contract with another club, the transfer market comes into play. Clubs pay hundreds of millions in transfer fees, essentially treating players as financial assets.'\n\n'And the strategy behind all of this?' Tùng asks.\n\n'Every decision is driven by strategy and incentives,' Linh says. 'Clubs develop long-term strategies for building competitive teams. Some invest in youth academies, which requires endurance and patience. Others spend big on transfers for immediate results. The incentive structure of each league shapes these decisions. In American sports, the draft system gives the worst-performing team the first pick of new talent — which creates competitive balance but also creates a perverse incentive to lose on purpose.'\n\n'What about the emotional side of sports?' Tùng asks. 'The things that statistics cannot capture?'\n\n'That is my favorite part,' Linh says. 'Rivalry is one of the most powerful forces in sports. When two teams with a long history of competition face each other, the intensity is completely different. Players take more risks, crowds are louder, and the atmosphere is electric. And then there is momentum — that mysterious force that can shift a game in minutes. One goal, one great play, and suddenly the underdog believes they can win. The statistics say they should lose, but momentum does not care about statistics.'\n\n'And the referee?' Tùng asks.\n\n'Referees are supposed to be neutral, but research shows they are human,' Linh says. 'They are more likely to award a penalty to the home team when the crowd is large and loud. Their decisions can change the outcome of an entire season. That is why technology like VAR has been introduced — to reduce human bias in critical moments.'\n\n'What about the business side — sponsors and leagues?' Tùng asks.\n\n'Sponsors are the financial engine of modern sports,' Linh says. 'They pay billions to associate their brands with popular teams and athletes. The incentive is clear — sports fans are emotionally loyal, and that loyalty transfers to the products their favorite teams endorse. Leagues organize the competition and set the rules that govern everything — from how much teams can spend on salaries to how the draft works. Each league is essentially a self-contained economic system with its own incentives and consequences.'\n\n'I think your professor is going to be impressed,' Tùng says.\n\nLinh closes her notebook. 'You know what surprised me most? It is not the money or the statistics. It is how sports reveals fundamental truths about human behavior. We respond to incentives. We root for the underdog. We are biased even when we try to be fair. We build rivalries because competition brings out our best performance. Sports is not just entertainment — it is a mirror that shows us who we really are.'\n\nTùng nods. 'And that is exactly what Freakonomics is about — using economics to understand the hidden side of everything. Even the games we play.'\n\n'Especially the games we play,' Linh says with a smile."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Mặt ẩn giấu của thể thao — Khi kinh tế học gặp sân cỏ",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "A month has passed since Tùng and Linh started their conversations about sports economics. They are sitting in the university library, preparing for Linh's economics presentation. She has chosen to present on the economics of professional sports.\n\n'I cannot believe how much I have learned,' Linh says. 'A month ago, I thought sports was just about athletes running around a field. Now I see it as one of the most complex economic systems in the world.'\n\nTùng smiles. 'Tell me what you are going to present.'\n\n'I want to start with the people,' Linh says. 'Every professional sport begins with an athlete — someone with extraordinary physical talent and endurance. But talent alone is not enough. The modern sports industry has created an entire ecosystem around finding and developing that talent. Scouts travel the world looking for the next star, watching thousands of young players and evaluating their performance using both observation and statistics.'\n\n'Good start,' Tùng says. 'What about the money side?'\n\n'That is where it gets really interesting,' Linh continues. 'When a scout identifies a promising player, the club has to recruit them — and that costs money. Player salaries in top leagues are enormous because the supply of world-class talent is extremely limited. And when a player is already under contract with another club, the transfer market comes into play. Clubs pay hundreds of millions in transfer fees, essentially treating players as financial assets.'\n\n'And the strategy behind all of this?' Tùng asks.\n\n'Every decision is driven by strategy and incentives,' Linh says. 'Clubs develop long-term strategies for building competitive teams. Some invest in youth academies, which requires endurance and patience. Others spend big on transfers for immediate results. The incentive structure of each league shapes these decisions. In American sports, the draft system gives the worst-performing team the first pick of new talent — which creates competitive balance but also creates a perverse incentive to lose on purpose.'\n\n'What about the emotional side of sports?' Tùng asks. 'The things that statistics cannot capture?'\n\n'That is my favorite part,' Linh says. 'Rivalry is one of the most powerful forces in sports. When two teams with a long history of competition face each other, the intensity is completely different. Players take more risks, crowds are louder, and the atmosphere is electric. And then there is momentum — that mysterious force that can shift a game in minutes. One goal, one great play, and suddenly the underdog believes they can win. The statistics say they should lose, but momentum does not care about statistics.'\n\n'And the referee?' Tùng asks.\n\n'Referees are supposed to be neutral, but research shows they are human,' Linh says. 'They are more likely to award a penalty to the home team when the crowd is large and loud. Their decisions can change the outcome of an entire season. That is why technology like VAR has been introduced — to reduce human bias in critical moments.'\n\n'What about the business side — sponsors and leagues?' Tùng asks.\n\n'Sponsors are the financial engine of modern sports,' Linh says. 'They pay billions to associate their brands with popular teams and athletes. The incentive is clear — sports fans are emotionally loyal, and that loyalty transfers to the products their favorite teams endorse. Leagues organize the competition and set the rules that govern everything — from how much teams can spend on salaries to how the draft works. Each league is essentially a self-contained economic system with its own incentives and consequences.'\n\n'I think your professor is going to be impressed,' Tùng says.\n\nLinh closes her notebook. 'You know what surprised me most? It is not the money or the statistics. It is how sports reveals fundamental truths about human behavior. We respond to incentives. We root for the underdog. We are biased even when we try to be fair. We build rivalries because competition brings out our best performance. Sports is not just entertainment — it is a mirror that shows us who we really are.'\n\nTùng nods. 'And that is exactly what Freakonomics is about — using economics to understand the hidden side of everything. Even the games we play.'\n\n'Especially the games we play,' Linh says with a smile."
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích kinh tế thể thao",
                    "description": "Viết đoạn văn phân tích về kinh tế thể thao sử dụng từ vựng đã học.",
                    "data": {
                        "vocabList": ["athlete", "endurance", "strategy", "recruit", "salary", "transfer", "statistic", "underdog", "rivalry", "momentum", "penalty", "referee", "sponsor", "league", "draft", "incentive", "performance", "scout"],
                        "instructions": "Viết một đoạn văn tiếng Anh (80-120 từ) phân tích cách kinh tế học ảnh hưởng đến thể thao chuyên nghiệp. Sử dụng ít nhất 6 từ vựng đã học trong bài.",
                        "prompts": [
                            "Explain how the transfer market and salary system in professional sports work like a regular economic market. Use words like athlete, recruit, salary, transfer, statistic, and scout to describe how clubs find, evaluate, and pay for talent.",
                            "Analyze how incentives shape behavior in professional sports — from the draft system that rewards losing to the sponsor deals that reward winning. Use words like incentive, draft, league, performance, underdog, and strategy to explain the hidden economics behind the games we watch."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng và lời chia tay — farewell tone: quiet_awe.",
                    "data": {
                        "text": "Bạn đã hoàn thành Freakonomics: Hidden Side of Sports. Hãy dừng lại một chút và cảm nhận điều này — bạn vừa nhìn thấy một thế giới hoàn toàn mới ẩn giấu bên trong thứ mà hàng tỷ người xem mỗi ngày nhưng ít ai thực sự hiểu.\n\nHãy cùng ôn lại 18 từ vựng — nhưng lần này, tôi muốn bạn cảm nhận sức nặng của mỗi từ, không chỉ nghĩa của nó.\n\nAthlete — vận động viên. Đằng sau mỗi athlete là hàng nghìn giờ luyện tập mà không ai nhìn thấy. Câu mới: The greatest athletes are not just physically gifted — they are the ones who show up to train when nobody is watching.\n\nEndurance — sức bền. Không chỉ là chạy xa — mà là khả năng tiếp tục khi mọi thứ trong cơ thể bảo bạn dừng lại. Câu mới: True endurance is not about the body — it is about the mind refusing to quit when the body wants to stop.\n\nStrategy — chiến lược. Mỗi trận đấu là một bàn cờ, và mỗi nước đi đều có lý do. Câu mới: The best coaches see the game three moves ahead, building a strategy that turns weaknesses into strengths.\n\nRecruit — tuyển dụng. Đằng sau mỗi ngôi sao là một người đã nhìn thấy tiềm năng khi chưa ai khác nhìn thấy. Câu mới: To recruit the right person is to see a diamond where others see only rough stone.\n\nSalary — lương. Con số trên hợp đồng kể một câu chuyện về cung và cầu, về sự khan hiếm của tài năng đỉnh cao. Câu mới: An athlete's salary reflects not just their skill, but the millions of fans willing to pay to watch them play.\n\nTransfer — chuyển nhượng. Mỗi transfer là một canh bạc — đặt cược hàng trăm triệu vào tiềm năng của một con người. Câu mới: Every transfer carries a story of hope — a club betting its future on one player's ability to change everything.\n\nStatistic — số liệu thống kê. Những con số nhỏ bé có thể kể những câu chuyện lớn lao. Câu mới: A single statistic can reveal a truth that thousands of hours of watching could never show.\n\nUnderdog — đội yếu hơn. Có lẽ không có gì đẹp hơn trong thể thao bằng khoảnh khắc underdog chiến thắng. Câu mới: Every underdog victory reminds us that the scoreboard does not know who is supposed to win.\n\nRivalry — sự cạnh tranh. Rivalry không phải là thù hận — mà là sự tôn trọng sâu sắc được thể hiện qua cạnh tranh. Câu mới: The greatest rivalries in sports push both sides to reach heights they could never achieve alone.\n\nMomentum — đà chiến thắng. Bạn không thể nhìn thấy momentum, nhưng bạn có thể cảm nhận nó — khi cả sân vận động đồng loạt đứng dậy. Câu mới: Momentum is invisible and unmeasurable, yet everyone in the stadium knows the exact moment it shifts.\n\nPenalty — hình phạt. Một quả penalty có thể kết thúc giấc mơ hoặc bắt đầu huyền thoại. Câu mới: The loneliest moment in sports is standing at the penalty spot with a nation's hopes resting on one kick.\n\nReferee — trọng tài. Người mà ai cũng muốn hoàn hảo, nhưng cũng là người nhắc chúng ta rằng sự hoàn hảo không tồn tại. Câu mới: A referee carries the weight of fairness on their shoulders, knowing that every decision will be questioned by millions.\n\nSponsor — nhà tài trợ. Đằng sau mỗi logo trên áo đấu là một câu chuyện về niềm tin vào sức mạnh của cảm xúc. Câu mới: When a sponsor puts their name on a stadium, they are not buying advertising — they are buying a place in people's hearts.\n\nLeague — giải đấu. Mỗi league là một thế giới thu nhỏ với luật lệ, quyền lực, và những giấc mơ riêng. Câu mới: A league is more than a competition — it is a community of millions who share the same passion and the same heartbreak.\n\nDraft — vòng tuyển chọn. Khoảnh khắc một cái tên được gọi trong draft, cuộc đời một người thay đổi mãi mãi. Câu mới: The draft is where dreams become real — where a name on a list becomes a player on a team that millions will cheer for.\n\nIncentive — động lực. Hiểu incentive là hiểu tại sao con người làm những gì họ làm — trong thể thao và trong cuộc sống. Câu mới: The hidden incentives behind every decision are like currents beneath the ocean — invisible but powerful enough to move everything.\n\nPerformance — thành tích. Mỗi performance trên sân là tổng hòa của tài năng, nỗ lực, và cả may mắn. Câu mới: A single extraordinary performance can define an athlete's legacy and inspire generations of young players to follow their path.\n\nScout — tuyển trạch viên. Người tìm kiếm ngôi sao trong bóng tối — công việc thầm lặng nhất nhưng quan trọng nhất trong thể thao. Câu mới: The art of scouting is the art of seeing potential — of imagining what someone could become, not just what they are today.\n\nVà thế là xong — 18 từ vựng, 18 cánh cửa mở ra một thế giới mà bạn chưa từng nhìn thấy trước đây. Lần tới bạn xem một trận bóng đá, một trận bóng rổ, hay bất kỳ môn thể thao nào — hãy nhìn sâu hơn. Đằng sau mỗi đường chuyền, mỗi bàn thắng, mỗi quyết định của trọng tài — là một câu chuyện về kinh tế, về tâm lý, về con người.\n\nThể thao không chỉ là trò chơi. Nó là tấm gương phản chiếu cách chúng ta sống, cách chúng ta cạnh tranh, và cách chúng ta mơ ước. Và bây giờ, bạn có ngôn ngữ để nói về tất cả những điều đó bằng tiếng Anh.\n\nCảm ơn bạn đã đi cùng tôi trong hành trình này. Hẹn gặp lại."
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
validate_bilingual_prompts(content, "intermediate")
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
print(f"Level: intermediate | Skill: balanced_skills | Content: podcast")
print(f"Words: 18 (3 groups of 6)")
