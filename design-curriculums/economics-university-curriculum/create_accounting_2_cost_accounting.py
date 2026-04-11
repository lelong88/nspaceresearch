import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Series D, Curriculum 2: Cost Accounting – Kế Toán Chi Phí
# Description tone: metaphor_led
# Farewell tone: practical momentum
# W1: cost, budget, variance, overhead, allocation, direct
# W2: indirect, standard, actual, absorption, marginal, contribution
# W3: breakeven, forecast, performance, benchmark, controllable, uncontrollable

content = {
    "title": "Cost Accounting – Kế Toán Chi Phí",
    "contentTypeTags": [],
    "description": "KẾ TOÁN CHI PHÍ LÀ CHIẾC LA BÀN — NẾU BẠN KHÔNG BIẾT ĐỌC, BẠN SẼ ĐI LẠC GIỮA RỪNG SỐ LIỆU.\n\nBạn đã bao giờ ngồi trong lớp kế toán quản trị, nghe giảng viên nói về 'variance analysis' hay 'absorption costing' mà cảm thấy như đang nghe một ngôn ngữ khác? Bạn hiểu chi phí trực tiếp, chi phí gián tiếp bằng tiếng Việt — nhưng khi mở một bản báo cáo ngân sách của công ty đa quốc gia, mọi thứ trở nên mờ mịt.\n\nHãy nghĩ về kế toán chi phí như chiếc la bàn giữa khu rừng kinh doanh. Mỗi con số chi phí là một dấu hiệu trên đường đi — nếu bạn đọc đúng, bạn biết mình đang ở đâu và cần đi đâu. Nếu bạn đọc sai, bạn sẽ đưa ra quyết định sai — và trong kinh doanh, quyết định sai về chi phí có thể khiến cả doanh nghiệp lạc hướng.\n\n18 từ vựng trong bài học này — từ cost đến uncontrollable — sẽ trang bị cho bạn ngôn ngữ để đọc hiểu báo cáo chi phí, phân tích ngân sách, và thảo luận về hiệu quả hoạt động bằng tiếng Anh chuyên ngành.\n\nTừ budget variance đến breakeven analysis — bạn vừa nâng cấp tư duy quản trị chi phí, vừa nâng trình tiếng Anh kế toán một cách vượt bậc.",
    "preview": {
        "text": "Khám phá 18 từ vựng tiếng Anh cốt lõi về kế toán chi phí và lập ngân sách — công cụ mà mọi kế toán viên quản trị và nhà quản lý tài chính đều cần thành thạo. Bạn sẽ bắt đầu với cost, budget, variance, overhead, allocation, direct — bộ từ nền tảng giúp bạn hiểu cách doanh nghiệp phân loại và phân bổ chi phí. Tiếp theo là indirect, standard, actual, absorption, marginal, contribution — những từ giúp bạn phân biệt các phương pháp tính giá thành sản phẩm và phân tích lợi nhuận biên. Cuối cùng, breakeven, forecast, performance, benchmark, controllable, uncontrollable đưa bạn vào thế giới phân tích hòa vốn, dự báo tài chính và đánh giá hiệu quả hoạt động. Qua 3 bài đọc tiếng Anh về kế toán chi phí thực tế, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, bạn sẽ tự tin đọc hiểu cost reports và budget analyses bằng tiếng Anh mà không cần dừng lại tra từ."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Chào mừng bạn đến với bài học về kế toán chi phí — nền tảng của mọi quyết định quản trị.",
                    "data": {
                        "text": "Chào mừng bạn đến với bài học thứ hai trong chuỗi Kế toán và Tài chính doanh nghiệp — chủ đề hôm nay là Kế toán chi phí, hay trong tiếng Anh là Cost Accounting. Nếu bài học trước về Financial Statements giúp bạn đọc được bức tranh tổng thể của doanh nghiệp, thì bài học hôm nay sẽ đưa bạn vào bên trong — nơi mà mỗi đồng chi phí được theo dõi, phân loại, và phân tích để đưa ra quyết định kinh doanh.\n\nTrong phần này, bạn sẽ học 6 từ vựng đầu tiên: cost, budget, variance, overhead, allocation, và direct. Đây là những từ xuất hiện trong mọi cuộc họp ngân sách, mọi báo cáo chi phí, và mọi quyết định định giá sản phẩm.\n\nTừ đầu tiên là cost — danh từ — nghĩa là chi phí. Cost là tổng số tiền mà doanh nghiệp phải bỏ ra để sản xuất hàng hóa hoặc cung cấp dịch vụ. Trong kế toán chi phí, cost được phân loại theo nhiều cách — theo hành vi (cố định hay biến đổi), theo chức năng (sản xuất hay bán hàng), hoặc theo khả năng truy xuất (trực tiếp hay gián tiếp). Ví dụ: 'The total cost of manufacturing one unit includes raw materials, labor, and a share of factory overhead.' Trong bài đọc, cost là từ khóa trung tâm — mọi phân tích đều bắt đầu từ việc hiểu chi phí.\n\nTừ thứ hai là budget — danh từ và động từ — nghĩa là ngân sách, lập ngân sách. Budget là kế hoạch tài chính chi tiết cho một khoảng thời gian — thường là một năm — dự kiến doanh thu, chi phí, và lợi nhuận. Lập ngân sách là quá trình dự đoán và phân bổ nguồn lực tài chính. Ví dụ: 'The marketing department submitted a budget of two hundred thousand dollars for the next quarter, but management approved only one hundred and fifty thousand.' Trong bài đọc, budget là công cụ kiểm soát — nó đặt ra giới hạn và kỳ vọng cho mỗi bộ phận.\n\nTừ thứ ba là variance — danh từ — nghĩa là chênh lệch, phương sai. Trong kế toán chi phí, variance là sự khác biệt giữa con số dự kiến (ngân sách hoặc tiêu chuẩn) và con số thực tế. Favorable variance nghĩa là chi phí thực tế thấp hơn dự kiến; unfavorable variance nghĩa là chi phí thực tế cao hơn. Ví dụ: 'The production department reported an unfavorable labor variance of thirty thousand dollars because overtime hours exceeded the budgeted amount.' Trong bài đọc, variance là tín hiệu cảnh báo — nó cho nhà quản lý biết khi nào mọi thứ đi chệch kế hoạch.\n\nTừ thứ tư là overhead — danh từ — nghĩa là chi phí chung, chi phí gián tiếp sản xuất. Overhead bao gồm tất cả chi phí sản xuất mà không thể truy xuất trực tiếp đến một sản phẩm cụ thể — tiền thuê nhà xưởng, điện nước, bảo trì máy móc, lương quản đốc. Ví dụ: 'Factory overhead accounts for nearly forty percent of total production costs, making it the largest single cost category after raw materials.' Trong bài đọc, overhead là thách thức lớn nhất của kế toán chi phí — vì nó phải được phân bổ cho từng sản phẩm một cách hợp lý.\n\nTừ thứ năm là allocation — danh từ — nghĩa là phân bổ. Allocation là quá trình chia sẻ chi phí chung cho các sản phẩm, bộ phận, hoặc hoạt động khác nhau dựa trên một tiêu chí hợp lý — như số giờ máy, số giờ lao động, hoặc diện tích sử dụng. Ví dụ: 'The company uses machine hours as the basis for overhead allocation, assigning more cost to products that require longer processing time.' Trong bài đọc, allocation là nghệ thuật — không có cách phân bổ nào hoàn hảo, nhưng cách phân bổ tốt giúp nhà quản lý hiểu đúng chi phí thực sự của mỗi sản phẩm.\n\nTừ cuối cùng là direct — tính từ — nghĩa là trực tiếp. Direct cost là chi phí có thể truy xuất trực tiếp đến một sản phẩm hoặc dịch vụ cụ thể — nguyên vật liệu trực tiếp và nhân công trực tiếp. Ví dụ: 'The direct cost of producing a wooden chair includes the timber, screws, and the wages of the carpenter who assembled it.' Trong bài đọc, direct đối lập với indirect — và sự phân biệt này là nền tảng của toàn bộ hệ thống kế toán chi phí.\n\nBạn đã có 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, sau đó đọc bài viết về cách doanh nghiệp phân loại và kiểm soát chi phí nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng kế toán chi phí",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng kế toán chi phí",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng kế toán chi phí",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng kế toán chi phí",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nền tảng kế toán chi phí",
                    "description": "Học 6 từ: cost, budget, variance, overhead, allocation, direct",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phân loại chi phí và lập ngân sách",
                    "description": "Every business decision begins with a simple question: how much does it cost?",
                    "data": {
                        "text": "Every business decision begins with a simple question: how much does it cost? But in practice, answering that question is far more complex than it seems. Cost accounting is the branch of accounting that tracks, classifies, and analyzes costs to help managers make better decisions.\n\nThe first step in cost accounting is classification. Costs are divided into categories based on how they relate to the product or service being produced. The most fundamental distinction is between direct costs and indirect costs.\n\nA direct cost is one that can be traced specifically to a product, service, or project. If a furniture factory makes wooden tables, the timber used for each table is a direct material cost. The wages paid to the carpenter who assembles the table are a direct labor cost. These costs are easy to measure and assign because they have a clear, one-to-one relationship with the product.\n\nIndirect costs, by contrast, cannot be traced to a single product. The electricity that powers the entire factory, the salary of the factory manager, the insurance on the building — these costs benefit all products equally and cannot be assigned to any one table or chair. In manufacturing, indirect production costs are collectively called overhead.\n\nOverhead is often the largest and most difficult cost category to manage. A Vietnamese garment factory might spend millions of dong each month on rent, utilities, equipment maintenance, and quality control staff. None of these costs can be directly linked to a single shirt or pair of trousers. Yet they are real costs that must be recovered through product pricing.\n\nThis is where allocation becomes essential. Allocation is the process of distributing overhead costs across products using a reasonable basis. A factory might allocate overhead based on machine hours — products that require more machine time receive a larger share of overhead. Another factory might use direct labor hours or units produced as the allocation basis. The choice of allocation method can significantly affect the reported cost of each product.\n\nOnce costs are classified and allocated, managers need a plan. This is the role of the budget. A budget is a detailed financial plan that estimates revenues, costs, and profits for a future period — typically a quarter or a year. The production budget estimates how many units will be manufactured. The materials budget estimates how much raw material will be needed. The overhead budget estimates indirect costs. Together, these budgets create a roadmap for the entire organization.\n\nBut no plan survives contact with reality unchanged. Actual results almost always differ from the budget. The difference between budgeted and actual figures is called a variance. If the factory budgeted fifty million dong for raw materials but actually spent forty-five million, the five million difference is a favorable variance — costs were lower than expected. If actual spending was fifty-five million, the variance is unfavorable.\n\nVariance analysis is one of the most powerful tools in cost accounting. By breaking down variances into their components — price variances, quantity variances, efficiency variances — managers can identify exactly where and why costs deviated from the plan. A large unfavorable material price variance might indicate that a supplier raised prices. A large unfavorable labor efficiency variance might indicate that workers needed more training.\n\nFrom classifying costs as direct or indirect, to allocating overhead fairly, to building budgets and analyzing variances — cost accounting gives managers the information they need to control spending and improve profitability. The language of cost accounting is precise, and learning it in English opens the door to working with multinational companies where these concepts are discussed every day."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phân loại chi phí và lập ngân sách",
                    "description": "Every business decision begins with a simple question: how much does it cost?",
                    "data": {
                        "text": "Every business decision begins with a simple question: how much does it cost? But in practice, answering that question is far more complex than it seems. Cost accounting is the branch of accounting that tracks, classifies, and analyzes costs to help managers make better decisions.\n\nThe first step in cost accounting is classification. Costs are divided into categories based on how they relate to the product or service being produced. The most fundamental distinction is between direct costs and indirect costs.\n\nA direct cost is one that can be traced specifically to a product, service, or project. If a furniture factory makes wooden tables, the timber used for each table is a direct material cost. The wages paid to the carpenter who assembles the table are a direct labor cost. These costs are easy to measure and assign because they have a clear, one-to-one relationship with the product.\n\nIndirect costs, by contrast, cannot be traced to a single product. The electricity that powers the entire factory, the salary of the factory manager, the insurance on the building — these costs benefit all products equally and cannot be assigned to any one table or chair. In manufacturing, indirect production costs are collectively called overhead.\n\nOverhead is often the largest and most difficult cost category to manage. A Vietnamese garment factory might spend millions of dong each month on rent, utilities, equipment maintenance, and quality control staff. None of these costs can be directly linked to a single shirt or pair of trousers. Yet they are real costs that must be recovered through product pricing.\n\nThis is where allocation becomes essential. Allocation is the process of distributing overhead costs across products using a reasonable basis. A factory might allocate overhead based on machine hours — products that require more machine time receive a larger share of overhead. Another factory might use direct labor hours or units produced as the allocation basis. The choice of allocation method can significantly affect the reported cost of each product.\n\nOnce costs are classified and allocated, managers need a plan. This is the role of the budget. A budget is a detailed financial plan that estimates revenues, costs, and profits for a future period — typically a quarter or a year. The production budget estimates how many units will be manufactured. The materials budget estimates how much raw material will be needed. The overhead budget estimates indirect costs. Together, these budgets create a roadmap for the entire organization.\n\nBut no plan survives contact with reality unchanged. Actual results almost always differ from the budget. The difference between budgeted and actual figures is called a variance. If the factory budgeted fifty million dong for raw materials but actually spent forty-five million, the five million difference is a favorable variance — costs were lower than expected. If actual spending was fifty-five million, the variance is unfavorable.\n\nVariance analysis is one of the most powerful tools in cost accounting. By breaking down variances into their components — price variances, quantity variances, efficiency variances — managers can identify exactly where and why costs deviated from the plan. A large unfavorable material price variance might indicate that a supplier raised prices. A large unfavorable labor efficiency variance might indicate that workers needed more training.\n\nFrom classifying costs as direct or indirect, to allocating overhead fairly, to building budgets and analyzing variances — cost accounting gives managers the information they need to control spending and improve profitability. The language of cost accounting is precise, and learning it in English opens the door to working with multinational companies where these concepts are discussed every day."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phân loại chi phí và lập ngân sách",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Every business decision begins with a simple question: how much does it cost? But in practice, answering that question is far more complex than it seems. Cost accounting is the branch of accounting that tracks, classifies, and analyzes costs to help managers make better decisions.\n\nThe first step in cost accounting is classification. Costs are divided into categories based on how they relate to the product or service being produced. The most fundamental distinction is between direct costs and indirect costs.\n\nA direct cost is one that can be traced specifically to a product, service, or project. If a furniture factory makes wooden tables, the timber used for each table is a direct material cost. The wages paid to the carpenter who assembles the table are a direct labor cost. These costs are easy to measure and assign because they have a clear, one-to-one relationship with the product.\n\nIndirect costs, by contrast, cannot be traced to a single product. The electricity that powers the entire factory, the salary of the factory manager, the insurance on the building — these costs benefit all products equally and cannot be assigned to any one table or chair. In manufacturing, indirect production costs are collectively called overhead.\n\nOverhead is often the largest and most difficult cost category to manage. A Vietnamese garment factory might spend millions of dong each month on rent, utilities, equipment maintenance, and quality control staff. None of these costs can be directly linked to a single shirt or pair of trousers. Yet they are real costs that must be recovered through product pricing.\n\nThis is where allocation becomes essential. Allocation is the process of distributing overhead costs across products using a reasonable basis. A factory might allocate overhead based on machine hours — products that require more machine time receive a larger share of overhead. Another factory might use direct labor hours or units produced as the allocation basis. The choice of allocation method can significantly affect the reported cost of each product.\n\nOnce costs are classified and allocated, managers need a plan. This is the role of the budget. A budget is a detailed financial plan that estimates revenues, costs, and profits for a future period — typically a quarter or a year. The production budget estimates how many units will be manufactured. The materials budget estimates how much raw material will be needed. The overhead budget estimates indirect costs. Together, these budgets create a roadmap for the entire organization.\n\nBut no plan survives contact with reality unchanged. Actual results almost always differ from the budget. The difference between budgeted and actual figures is called a variance. If the factory budgeted fifty million dong for raw materials but actually spent forty-five million, the five million difference is a favorable variance — costs were lower than expected. If actual spending was fifty-five million, the variance is unfavorable.\n\nVariance analysis is one of the most powerful tools in cost accounting. By breaking down variances into their components — price variances, quantity variances, efficiency variances — managers can identify exactly where and why costs deviated from the plan. A large unfavorable material price variance might indicate that a supplier raised prices. A large unfavorable labor efficiency variance might indicate that workers needed more training.\n\nFrom classifying costs as direct or indirect, to allocating overhead fairly, to building budgets and analyzing variances — cost accounting gives managers the information they need to control spending and improve profitability. The language of cost accounting is precise, and learning it in English opens the door to working with multinational companies where these concepts are discussed every day."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng kế toán chi phí",
                    "description": "Viết câu sử dụng 6 từ vựng về nền tảng kế toán chi phí.",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'cost' để viết một câu về cách doanh nghiệp phân loại chi phí để đưa ra quyết định định giá. Ví dụ: The total cost of producing each smartphone includes raw materials, assembly labor, and a proportional share of factory rent and utilities.",
                                "targetVocab": "cost"
                            },
                            {
                                "prompt": "Dùng từ 'budget' để viết một câu về vai trò của ngân sách trong việc kiểm soát chi tiêu của doanh nghiệp. Ví dụ: The operations team exceeded its quarterly budget by fifteen percent after an unexpected surge in shipping costs forced the company to use premium freight services.",
                                "targetVocab": "budget"
                            },
                            {
                                "prompt": "Dùng từ 'variance' để viết một câu về phân tích chênh lệch giữa chi phí dự kiến và thực tế. Ví dụ: A detailed variance analysis revealed that the unfavorable material cost was caused by a twenty percent price increase from the primary steel supplier.",
                                "targetVocab": "variance"
                            },
                            {
                                "prompt": "Dùng từ 'overhead' để viết một câu về chi phí chung của nhà máy và cách chúng ảnh hưởng đến giá thành sản phẩm. Ví dụ: When the factory operated at only fifty percent capacity, the overhead cost per unit doubled because fixed expenses like rent and insurance were spread across fewer products.",
                                "targetVocab": "overhead"
                            },
                            {
                                "prompt": "Dùng từ 'allocation' để viết một câu về phương pháp phân bổ chi phí gián tiếp cho các sản phẩm khác nhau. Ví dụ: The company switched its overhead allocation basis from direct labor hours to machine hours after automation reduced the workforce but increased equipment usage.",
                                "targetVocab": "allocation"
                            },
                            {
                                "prompt": "Dùng từ 'direct' để viết một câu về chi phí trực tiếp và cách chúng được truy xuất đến sản phẩm cụ thể. Ví dụ: The direct costs of building a custom website included the developer's salary for three months and the licensing fees for the design software used exclusively on that project.",
                                "targetVocab": "direct"
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về phương pháp tính giá thành và phân tích lợi nhuận biên.",
                    "data": {
                        "text": "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: cost — chi phí, budget — ngân sách, variance — chênh lệch, overhead — chi phí chung, allocation — phân bổ, và direct — trực tiếp. Bạn đã hiểu cách doanh nghiệp phân loại chi phí, lập ngân sách, và phân tích chênh lệch. Bây giờ, chúng ta sẽ đi sâu hơn vào các phương pháp tính giá thành sản phẩm và phân tích lợi nhuận.\n\nTrong phần 2, bạn sẽ học 6 từ mới: indirect, standard, actual, absorption, marginal, và contribution. Những từ này giúp bạn hiểu cách kế toán viên tính toán chi phí sản phẩm và đánh giá khả năng sinh lời.\n\nTừ đầu tiên là indirect — tính từ — nghĩa là gián tiếp. Indirect cost là chi phí không thể truy xuất trực tiếp đến một sản phẩm cụ thể. Tiền thuê nhà xưởng, lương bảo vệ, chi phí bảo hiểm — tất cả đều là indirect costs vì chúng phục vụ toàn bộ hoạt động sản xuất, không riêng sản phẩm nào. Ví dụ: 'Indirect costs such as factory security, building insurance, and equipment depreciation must be allocated across all product lines using a fair and consistent method.' Trong bài đọc, indirect đối lập với direct — và cách xử lý chi phí gián tiếp là thách thức lớn nhất của kế toán chi phí.\n\nTừ thứ hai là standard — danh từ và tính từ — nghĩa là tiêu chuẩn. Standard cost là chi phí tiêu chuẩn — mức chi phí dự kiến để sản xuất một đơn vị sản phẩm trong điều kiện hoạt động bình thường. Nó bao gồm standard material cost, standard labor cost, và standard overhead cost. Ví dụ: 'The standard cost for producing one kilogram of chocolate was set at fifteen dollars, based on expected cocoa prices and normal production efficiency.' Trong bài đọc, standard là thước đo — nó cho phép nhà quản lý so sánh kết quả thực tế với kỳ vọng.\n\nTừ thứ ba là actual — tính từ — nghĩa là thực tế. Actual cost là chi phí thực tế phát sinh — con số thật sự ghi nhận được sau khi sản xuất hoàn tất. Sự khác biệt giữa standard cost và actual cost chính là variance. Ví dụ: 'The actual cost of production exceeded the standard by eight percent, primarily due to higher-than-expected energy prices during the summer months.' Trong bài đọc, actual là sự thật — nó cho thấy điều gì thực sự xảy ra, không phải điều bạn dự kiến.\n\nTừ thứ tư là absorption — danh từ — nghĩa là hấp thụ. Absorption costing là phương pháp tính giá thành hấp thụ toàn bộ — mỗi sản phẩm gánh chịu cả chi phí trực tiếp lẫn một phần chi phí gián tiếp (overhead). Đây là phương pháp được yêu cầu bởi chuẩn mực kế toán quốc tế cho báo cáo tài chính bên ngoài. Ví dụ: 'Under absorption costing, each unit of output absorbs a portion of fixed manufacturing overhead, which means that producing more units lowers the cost per unit.' Trong bài đọc, absorption là phương pháp chính thống — nó đảm bảo mọi chi phí sản xuất đều được phản ánh trong giá thành sản phẩm.\n\nTừ thứ năm là marginal — tính từ — nghĩa là biên, cận biên. Marginal cost là chi phí biên — chi phí tăng thêm khi sản xuất thêm một đơn vị sản phẩm. Marginal costing (hay variable costing) là phương pháp chỉ tính chi phí biến đổi vào giá thành sản phẩm, còn chi phí cố định được xem là chi phí kỳ. Ví dụ: 'The marginal cost of producing one additional bicycle was only forty dollars because the factory already had spare capacity and the fixed costs were already covered.' Trong bài đọc, marginal giúp nhà quản lý trả lời câu hỏi: có nên nhận thêm đơn hàng này không?\n\nTừ cuối cùng là contribution — danh từ — nghĩa là đóng góp, lợi nhuận gộp biên. Contribution margin là phần doanh thu còn lại sau khi trừ chi phí biến đổi — phần này dùng để bù đắp chi phí cố định và tạo lợi nhuận. Ví dụ: 'Each unit sold at a price of one hundred dollars with variable costs of sixty dollars generates a contribution of forty dollars toward covering fixed costs and profit.' Trong bài đọc, contribution là thước đo sức mạnh — sản phẩm nào có contribution margin cao nhất sẽ được ưu tiên sản xuất.\n\nSáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết về các phương pháp tính giá thành và phân tích lợi nhuận biên nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phương pháp tính giá thành",
                    "description": "Học 6 từ: indirect, standard, actual, absorption, marginal, contribution",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phương pháp tính giá thành và phân tích lợi nhuận biên",
                    "description": "Two accountants can look at the same factory and calculate two different costs for the same product.",
                    "data": {
                        "text": "Two accountants can look at the same factory and calculate two different costs for the same product. This is not a mistake — it is a consequence of choosing different costing methods. The two most important methods in cost accounting are absorption costing and marginal costing, and understanding the difference between them is essential for any manager.\n\nAbsorption costing — also called full costing — assigns all manufacturing costs to each unit of production. This includes both direct costs (materials and labor that can be traced to the product) and indirect costs (overhead that cannot be traced to any single product). Under absorption costing, every unit produced absorbs a share of the factory's fixed overhead. If a factory has fixed overhead of one million dollars per month and produces ten thousand units, each unit absorbs one hundred dollars of overhead.\n\nThis method is required by international accounting standards for external financial reporting. The logic is straightforward: all costs incurred to manufacture a product should be included in its cost. When a company reports its cost of goods sold on the income statement, absorption costing ensures that both variable and fixed manufacturing costs are reflected.\n\nHowever, absorption costing has a significant limitation. Because fixed overhead is allocated based on production volume, the cost per unit changes when production volume changes. If the factory produces twenty thousand units instead of ten thousand, the overhead per unit drops to fifty dollars. This can create the illusion that costs are falling when in reality the total overhead has not changed at all. Managers who focus only on absorption cost per unit might make poor decisions — for example, overproducing just to spread overhead across more units.\n\nMarginal costing — also called variable costing — takes a different approach. It assigns only variable costs to each unit of production. Variable costs are those that change in proportion to output: direct materials, direct labor, and variable overhead. Fixed overhead is treated as a period cost — an expense of the time period, not of the product. Under marginal costing, the cost of a product does not change when production volume changes.\n\nThe key concept in marginal costing is the contribution margin. Contribution is calculated as selling price minus variable cost per unit. If a product sells for two hundred dollars and its variable cost is one hundred and twenty dollars, the contribution is eighty dollars. This eighty dollars contributes toward covering fixed costs and generating profit.\n\nContribution analysis is a powerful decision-making tool. When a manager needs to decide whether to accept a special order at a lower price, the relevant question is not whether the price covers the full absorption cost, but whether it covers the variable cost and generates a positive contribution. If the factory has spare capacity and the special order price exceeds the marginal cost, accepting the order increases total profit — even if the price is below the standard full cost.\n\nThe difference between standard and actual costs adds another layer of analysis. Standard costs are predetermined estimates of what production should cost under normal conditions. They are set at the beginning of a period based on expected material prices, labor rates, and overhead levels. Actual costs are the real costs recorded during production. When actual costs differ from standard costs, the difference is a variance.\n\nIndirect costs present the greatest challenge in standard costing. Because overhead cannot be traced directly to products, accountants must estimate both the total overhead and the allocation basis in advance. If actual overhead or actual production volume differs from the estimate, the allocated overhead per unit will be wrong. This overhead variance must be analyzed and explained.\n\nWhether a company uses absorption costing for its annual report or marginal costing for internal decisions, the goal is the same: to understand the true cost of what it produces. And in a world where Vietnamese companies increasingly work with international partners, auditors, and investors, the ability to discuss these concepts in English is not a luxury — it is a necessity."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phương pháp tính giá thành và phân tích lợi nhuận biên",
                    "description": "Two accountants can look at the same factory and calculate two different costs for the same product.",
                    "data": {
                        "text": "Two accountants can look at the same factory and calculate two different costs for the same product. This is not a mistake — it is a consequence of choosing different costing methods. The two most important methods in cost accounting are absorption costing and marginal costing, and understanding the difference between them is essential for any manager.\n\nAbsorption costing — also called full costing — assigns all manufacturing costs to each unit of production. This includes both direct costs (materials and labor that can be traced to the product) and indirect costs (overhead that cannot be traced to any single product). Under absorption costing, every unit produced absorbs a share of the factory's fixed overhead. If a factory has fixed overhead of one million dollars per month and produces ten thousand units, each unit absorbs one hundred dollars of overhead.\n\nThis method is required by international accounting standards for external financial reporting. The logic is straightforward: all costs incurred to manufacture a product should be included in its cost. When a company reports its cost of goods sold on the income statement, absorption costing ensures that both variable and fixed manufacturing costs are reflected.\n\nHowever, absorption costing has a significant limitation. Because fixed overhead is allocated based on production volume, the cost per unit changes when production volume changes. If the factory produces twenty thousand units instead of ten thousand, the overhead per unit drops to fifty dollars. This can create the illusion that costs are falling when in reality the total overhead has not changed at all. Managers who focus only on absorption cost per unit might make poor decisions — for example, overproducing just to spread overhead across more units.\n\nMarginal costing — also called variable costing — takes a different approach. It assigns only variable costs to each unit of production. Variable costs are those that change in proportion to output: direct materials, direct labor, and variable overhead. Fixed overhead is treated as a period cost — an expense of the time period, not of the product. Under marginal costing, the cost of a product does not change when production volume changes.\n\nThe key concept in marginal costing is the contribution margin. Contribution is calculated as selling price minus variable cost per unit. If a product sells for two hundred dollars and its variable cost is one hundred and twenty dollars, the contribution is eighty dollars. This eighty dollars contributes toward covering fixed costs and generating profit.\n\nContribution analysis is a powerful decision-making tool. When a manager needs to decide whether to accept a special order at a lower price, the relevant question is not whether the price covers the full absorption cost, but whether it covers the variable cost and generates a positive contribution. If the factory has spare capacity and the special order price exceeds the marginal cost, accepting the order increases total profit — even if the price is below the standard full cost.\n\nThe difference between standard and actual costs adds another layer of analysis. Standard costs are predetermined estimates of what production should cost under normal conditions. They are set at the beginning of a period based on expected material prices, labor rates, and overhead levels. Actual costs are the real costs recorded during production. When actual costs differ from standard costs, the difference is a variance.\n\nIndirect costs present the greatest challenge in standard costing. Because overhead cannot be traced directly to products, accountants must estimate both the total overhead and the allocation basis in advance. If actual overhead or actual production volume differs from the estimate, the allocated overhead per unit will be wrong. This overhead variance must be analyzed and explained.\n\nWhether a company uses absorption costing for its annual report or marginal costing for internal decisions, the goal is the same: to understand the true cost of what it produces. And in a world where Vietnamese companies increasingly work with international partners, auditors, and investors, the ability to discuss these concepts in English is not a luxury — it is a necessity."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phương pháp tính giá thành và phân tích lợi nhuận biên",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Two accountants can look at the same factory and calculate two different costs for the same product. This is not a mistake — it is a consequence of choosing different costing methods. The two most important methods in cost accounting are absorption costing and marginal costing, and understanding the difference between them is essential for any manager.\n\nAbsorption costing — also called full costing — assigns all manufacturing costs to each unit of production. This includes both direct costs (materials and labor that can be traced to the product) and indirect costs (overhead that cannot be traced to any single product). Under absorption costing, every unit produced absorbs a share of the factory's fixed overhead. If a factory has fixed overhead of one million dollars per month and produces ten thousand units, each unit absorbs one hundred dollars of overhead.\n\nThis method is required by international accounting standards for external financial reporting. The logic is straightforward: all costs incurred to manufacture a product should be included in its cost. When a company reports its cost of goods sold on the income statement, absorption costing ensures that both variable and fixed manufacturing costs are reflected.\n\nHowever, absorption costing has a significant limitation. Because fixed overhead is allocated based on production volume, the cost per unit changes when production volume changes. If the factory produces twenty thousand units instead of ten thousand, the overhead per unit drops to fifty dollars. This can create the illusion that costs are falling when in reality the total overhead has not changed at all. Managers who focus only on absorption cost per unit might make poor decisions — for example, overproducing just to spread overhead across more units.\n\nMarginal costing — also called variable costing — takes a different approach. It assigns only variable costs to each unit of production. Variable costs are those that change in proportion to output: direct materials, direct labor, and variable overhead. Fixed overhead is treated as a period cost — an expense of the time period, not of the product. Under marginal costing, the cost of a product does not change when production volume changes.\n\nThe key concept in marginal costing is the contribution margin. Contribution is calculated as selling price minus variable cost per unit. If a product sells for two hundred dollars and its variable cost is one hundred and twenty dollars, the contribution is eighty dollars. This eighty dollars contributes toward covering fixed costs and generating profit.\n\nContribution analysis is a powerful decision-making tool. When a manager needs to decide whether to accept a special order at a lower price, the relevant question is not whether the price covers the full absorption cost, but whether it covers the variable cost and generates a positive contribution. If the factory has spare capacity and the special order price exceeds the marginal cost, accepting the order increases total profit — even if the price is below the standard full cost.\n\nThe difference between standard and actual costs adds another layer of analysis. Standard costs are predetermined estimates of what production should cost under normal conditions. They are set at the beginning of a period based on expected material prices, labor rates, and overhead levels. Actual costs are the real costs recorded during production. When actual costs differ from standard costs, the difference is a variance.\n\nIndirect costs present the greatest challenge in standard costing. Because overhead cannot be traced directly to products, accountants must estimate both the total overhead and the allocation basis in advance. If actual overhead or actual production volume differs from the estimate, the allocated overhead per unit will be wrong. This overhead variance must be analyzed and explained.\n\nWhether a company uses absorption costing for its annual report or marginal costing for internal decisions, the goal is the same: to understand the true cost of what it produces. And in a world where Vietnamese companies increasingly work with international partners, auditors, and investors, the ability to discuss these concepts in English is not a luxury — it is a necessity."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phương pháp tính giá thành",
                    "description": "Viết câu sử dụng 6 từ vựng về phương pháp tính giá thành và phân tích lợi nhuận biên.",
                    "data": {
                        "vocabList": ["indirect", "standard", "actual", "absorption", "marginal", "contribution"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'indirect' để viết một câu về chi phí gián tiếp và thách thức trong việc phân bổ chúng cho sản phẩm. Ví dụ: The company struggled to allocate indirect costs fairly because the three product lines used the factory's shared resources in very different ways.",
                                "targetVocab": "indirect"
                            },
                            {
                                "prompt": "Dùng từ 'standard' để viết một câu về cách doanh nghiệp sử dụng chi phí tiêu chuẩn để đánh giá hiệu quả sản xuất. Ví dụ: Management set a standard cost of twelve dollars per unit at the beginning of the year, based on expected material prices and normal labor productivity.",
                                "targetVocab": "standard"
                            },
                            {
                                "prompt": "Dùng từ 'actual' để viết một câu về sự khác biệt giữa chi phí thực tế và chi phí dự kiến. Ví dụ: The actual cost of the construction project came in twenty percent over budget because the price of steel rose sharply during the six-month building period.",
                                "targetVocab": "actual"
                            },
                            {
                                "prompt": "Dùng từ 'absorption' để viết một câu về phương pháp tính giá thành hấp thụ toàn bộ và yêu cầu của chuẩn mực kế toán. Ví dụ: International accounting standards require companies to use absorption costing for external reporting, ensuring that all manufacturing costs are included in the value of inventory.",
                                "targetVocab": "absorption"
                            },
                            {
                                "prompt": "Dùng từ 'marginal' để viết một câu về chi phí biên và quyết định nhận đơn hàng đặc biệt. Ví dụ: The export manager accepted the order at a lower price because the marginal cost of producing the extra units was well below the offered price, generating additional profit.",
                                "targetVocab": "marginal"
                            },
                            {
                                "prompt": "Dùng từ 'contribution' để viết một câu về lợi nhuận gộp biên và cách nó giúp đánh giá sản phẩm. Ví dụ: Product A had a contribution margin of sixty percent while Product B had only thirty-five percent, leading management to shift marketing resources toward Product A.",
                                "targetVocab": "contribution"
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
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về phân tích hòa vốn, dự báo và đánh giá hiệu quả.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! Hãy cùng ôn lại nhanh những gì bạn đã học. Trong phần 1, bạn đã nắm được 6 từ nền tảng: cost — chi phí, budget — ngân sách, variance — chênh lệch, overhead — chi phí chung, allocation — phân bổ, và direct — trực tiếp. Đây là bộ khung cơ bản để phân loại và kiểm soát chi phí. Trong phần 2, bạn đã học thêm indirect — gián tiếp, standard — tiêu chuẩn, actual — thực tế, absorption — hấp thụ, marginal — biên, và contribution — đóng góp. Những từ này giúp bạn hiểu các phương pháp tính giá thành và phân tích lợi nhuận biên.\n\nBây giờ, trong phần 3, chúng ta sẽ bước vào những công cụ phân tích quan trọng nhất của kế toán quản trị — những công cụ giúp nhà quản lý nhìn về phía trước và đánh giá hiệu quả hoạt động. Bạn sẽ học 6 từ mới: breakeven, forecast, performance, benchmark, controllable, và uncontrollable.\n\nTừ đầu tiên là breakeven — danh từ và tính từ — nghĩa là hòa vốn. Breakeven point là điểm hòa vốn — mức sản lượng hoặc doanh thu mà tại đó tổng doanh thu bằng đúng tổng chi phí, doanh nghiệp không lãi cũng không lỗ. Breakeven analysis sử dụng contribution margin để tính: Breakeven = Fixed Costs ÷ Contribution per Unit. Ví dụ: 'The startup calculated that it needed to sell at least eight hundred units per month to reach breakeven, after which every additional sale would generate pure profit.' Trong bài đọc, breakeven là ranh giới sống còn — dưới điểm hòa vốn là lỗ, trên điểm hòa vốn là lãi.\n\nTừ thứ hai là forecast — danh từ và động từ — nghĩa là dự báo. Forecast trong kế toán quản trị là việc ước tính doanh thu, chi phí, dòng tiền, hoặc nhu cầu sản xuất cho tương lai dựa trên dữ liệu lịch sử, xu hướng thị trường, và giả định kinh doanh. Ví dụ: 'The finance team revised its revenue forecast downward after the government announced new import restrictions that would reduce demand for the company's products.' Trong bài đọc, forecast là cầu nối giữa quá khứ và tương lai — nó giúp nhà quản lý chuẩn bị thay vì phản ứng.\n\nTừ thứ ba là performance — danh từ — nghĩa là hiệu quả hoạt động, thành tích. Performance trong kế toán quản trị là thước đo kết quả thực tế so với mục tiêu — doanh thu có đạt kế hoạch không, chi phí có trong ngân sách không, lợi nhuận có đạt kỳ vọng không. Ví dụ: 'The quarterly performance report showed that the Northern region exceeded its sales target by twelve percent while the Southern region fell short by eight percent.' Trong bài đọc, performance là tấm gương — nó phản ánh trung thực kết quả của mỗi bộ phận, mỗi sản phẩm, mỗi nhà quản lý.\n\nTừ thứ tư là benchmark — danh từ và động từ — nghĩa là chuẩn đối sánh, tiêu chuẩn so sánh. Benchmark là mức hiệu quả tham chiếu — có thể là kết quả của đối thủ cạnh tranh, trung bình ngành, hoặc thành tích tốt nhất trong quá khứ — dùng để đánh giá hiệu quả hiện tại. Ví dụ: 'The company benchmarked its production costs against three leading competitors and discovered that its overhead per unit was thirty percent higher than the industry average.' Trong bài đọc, benchmark là la bàn bên ngoài — nó cho bạn biết mình đang ở đâu so với phần còn lại của thị trường.\n\nTừ thứ năm là controllable — tính từ — nghĩa là có thể kiểm soát được. Controllable cost là chi phí mà một nhà quản lý cụ thể có quyền và khả năng ảnh hưởng — ví dụ, trưởng phòng sản xuất có thể kiểm soát chi phí nguyên vật liệu và giờ làm thêm, nhưng không kiểm soát được tiền thuê nhà xưởng. Ví dụ: 'The factory manager was evaluated only on controllable costs such as materials usage and overtime hours, not on rent or corporate overhead that she had no authority to change.' Trong bài đọc, controllable là nguyên tắc công bằng — nhà quản lý chỉ nên chịu trách nhiệm về những gì họ có thể kiểm soát.\n\nTừ cuối cùng là uncontrollable — tính từ — nghĩa là không thể kiểm soát được. Uncontrollable cost là chi phí nằm ngoài quyền quyết định của nhà quản lý — như thay đổi thuế suất, biến động tỷ giá, hoặc quyết định phân bổ chi phí từ trụ sở chính. Ví dụ: 'The branch manager argued that the unfavorable variance was caused by uncontrollable factors — a sudden increase in electricity tariffs imposed by the government and a corporate decision to raise the IT service charge.' Trong bài đọc, uncontrollable nhắc nhở rằng không phải mọi chênh lệch đều là lỗi của nhà quản lý — một số yếu tố nằm ngoài tầm kiểm soát.\n\nTuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard và đọc bài viết cuối cùng về phân tích hòa vốn và đánh giá hiệu quả nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Phân tích hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Phân tích hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Phân tích hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Phân tích hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Phân tích hòa vốn và đánh giá hiệu quả",
                    "description": "Học 6 từ: breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Phân tích hòa vốn, dự báo và đánh giá hiệu quả",
                    "description": "A manager who cannot measure performance cannot improve it.",
                    "data": {
                        "text": "A manager who cannot measure performance cannot improve it. This principle lies at the heart of management accounting, where the tools of breakeven analysis, forecasting, and performance evaluation help businesses plan for the future and learn from the past.\n\nBreakeven analysis is one of the simplest yet most powerful tools available to managers. It answers a fundamental question: how much do we need to sell before we start making a profit? The breakeven point is the level of sales at which total revenue exactly equals total costs — the company neither makes money nor loses it.\n\nCalculating the breakeven point requires understanding the relationship between fixed costs, variable costs, and the contribution margin. Fixed costs — rent, salaries of permanent staff, insurance — remain constant regardless of how many units are produced. Variable costs — raw materials, packaging, shipping — increase with each additional unit. The contribution margin is the difference between the selling price and the variable cost per unit.\n\nIf a company sells handmade bags at eighty dollars each, with variable costs of thirty dollars per bag, the contribution margin is fifty dollars. If fixed costs are one hundred thousand dollars per year, the breakeven point is two thousand bags — one hundred thousand divided by fifty. Below two thousand bags, the company loses money. Above two thousand, every additional bag generates fifty dollars of profit.\n\nBreakeven analysis becomes even more valuable when combined with forecasting. A forecast is an estimate of future financial results based on historical data, market trends, and management assumptions. Sales forecasts predict how many units the company expects to sell. Cost forecasts estimate how expenses will change. Cash flow forecasts project when money will come in and go out.\n\nGood forecasting is not about predicting the future perfectly — it is about preparing for multiple scenarios. A conservative forecast might assume flat sales growth and rising material costs. An optimistic forecast might assume a new product launch will boost demand by twenty percent. By comparing the breakeven point against different forecast scenarios, managers can assess risk and make informed decisions about pricing, production levels, and investment.\n\nOnce the period ends and actual results are available, the focus shifts to performance evaluation. Performance measurement compares what actually happened against what was planned — the budget, the forecast, or the standard. Did the sales team hit its revenue target? Did the factory keep costs within budget? Did the company achieve its profit goals?\n\nPerformance evaluation must be fair, and fairness requires distinguishing between controllable and uncontrollable factors. A controllable cost is one that a specific manager has the authority and ability to influence. The head of purchasing can negotiate better prices with suppliers — material costs are controllable for that manager. The production supervisor can manage overtime hours and reduce waste — labor efficiency is controllable.\n\nAn uncontrollable cost, by contrast, is one that a manager cannot influence. A sudden government tax increase, a natural disaster that disrupts supply chains, or a corporate decision to reallocate overhead from headquarters — these are uncontrollable factors. Holding a manager accountable for uncontrollable costs is unfair and demotivating. Effective performance evaluation systems separate controllable from uncontrollable variances so that each manager is judged only on what they can actually affect.\n\nBenchmarking adds an external dimension to performance evaluation. While budgets and standards provide internal targets, benchmarks compare a company's performance against external reference points — competitors, industry averages, or best-in-class companies. A Vietnamese textile manufacturer might benchmark its production cost per meter against factories in Bangladesh and China. If its costs are significantly higher, the benchmark reveals a competitive gap that needs to be addressed.\n\nBenchmarking is not just about cost. Companies benchmark quality metrics, delivery times, customer satisfaction scores, and employee productivity. The goal is to identify areas where the company lags behind and to learn from those who perform better.\n\nFrom calculating the breakeven point to building forecasts, from measuring performance against budgets to benchmarking against competitors — these tools transform raw cost data into actionable intelligence. They help managers answer not just what happened, but why it happened and what to do next. And in the language of international business, these conversations happen in English."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Phân tích hòa vốn, dự báo và đánh giá hiệu quả",
                    "description": "A manager who cannot measure performance cannot improve it.",
                    "data": {
                        "text": "A manager who cannot measure performance cannot improve it. This principle lies at the heart of management accounting, where the tools of breakeven analysis, forecasting, and performance evaluation help businesses plan for the future and learn from the past.\n\nBreakeven analysis is one of the simplest yet most powerful tools available to managers. It answers a fundamental question: how much do we need to sell before we start making a profit? The breakeven point is the level of sales at which total revenue exactly equals total costs — the company neither makes money nor loses it.\n\nCalculating the breakeven point requires understanding the relationship between fixed costs, variable costs, and the contribution margin. Fixed costs — rent, salaries of permanent staff, insurance — remain constant regardless of how many units are produced. Variable costs — raw materials, packaging, shipping — increase with each additional unit. The contribution margin is the difference between the selling price and the variable cost per unit.\n\nIf a company sells handmade bags at eighty dollars each, with variable costs of thirty dollars per bag, the contribution margin is fifty dollars. If fixed costs are one hundred thousand dollars per year, the breakeven point is two thousand bags — one hundred thousand divided by fifty. Below two thousand bags, the company loses money. Above two thousand, every additional bag generates fifty dollars of profit.\n\nBreakeven analysis becomes even more valuable when combined with forecasting. A forecast is an estimate of future financial results based on historical data, market trends, and management assumptions. Sales forecasts predict how many units the company expects to sell. Cost forecasts estimate how expenses will change. Cash flow forecasts project when money will come in and go out.\n\nGood forecasting is not about predicting the future perfectly — it is about preparing for multiple scenarios. A conservative forecast might assume flat sales growth and rising material costs. An optimistic forecast might assume a new product launch will boost demand by twenty percent. By comparing the breakeven point against different forecast scenarios, managers can assess risk and make informed decisions about pricing, production levels, and investment.\n\nOnce the period ends and actual results are available, the focus shifts to performance evaluation. Performance measurement compares what actually happened against what was planned — the budget, the forecast, or the standard. Did the sales team hit its revenue target? Did the factory keep costs within budget? Did the company achieve its profit goals?\n\nPerformance evaluation must be fair, and fairness requires distinguishing between controllable and uncontrollable factors. A controllable cost is one that a specific manager has the authority and ability to influence. The head of purchasing can negotiate better prices with suppliers — material costs are controllable for that manager. The production supervisor can manage overtime hours and reduce waste — labor efficiency is controllable.\n\nAn uncontrollable cost, by contrast, is one that a manager cannot influence. A sudden government tax increase, a natural disaster that disrupts supply chains, or a corporate decision to reallocate overhead from headquarters — these are uncontrollable factors. Holding a manager accountable for uncontrollable costs is unfair and demotivating. Effective performance evaluation systems separate controllable from uncontrollable variances so that each manager is judged only on what they can actually affect.\n\nBenchmarking adds an external dimension to performance evaluation. While budgets and standards provide internal targets, benchmarks compare a company's performance against external reference points — competitors, industry averages, or best-in-class companies. A Vietnamese textile manufacturer might benchmark its production cost per meter against factories in Bangladesh and China. If its costs are significantly higher, the benchmark reveals a competitive gap that needs to be addressed.\n\nBenchmarking is not just about cost. Companies benchmark quality metrics, delivery times, customer satisfaction scores, and employee productivity. The goal is to identify areas where the company lags behind and to learn from those who perform better.\n\nFrom calculating the breakeven point to building forecasts, from measuring performance against budgets to benchmarking against competitors — these tools transform raw cost data into actionable intelligence. They help managers answer not just what happened, but why it happened and what to do next. And in the language of international business, these conversations happen in English."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Phân tích hòa vốn, dự báo và đánh giá hiệu quả",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "A manager who cannot measure performance cannot improve it. This principle lies at the heart of management accounting, where the tools of breakeven analysis, forecasting, and performance evaluation help businesses plan for the future and learn from the past.\n\nBreakeven analysis is one of the simplest yet most powerful tools available to managers. It answers a fundamental question: how much do we need to sell before we start making a profit? The breakeven point is the level of sales at which total revenue exactly equals total costs — the company neither makes money nor loses it.\n\nCalculating the breakeven point requires understanding the relationship between fixed costs, variable costs, and the contribution margin. Fixed costs — rent, salaries of permanent staff, insurance — remain constant regardless of how many units are produced. Variable costs — raw materials, packaging, shipping — increase with each additional unit. The contribution margin is the difference between the selling price and the variable cost per unit.\n\nIf a company sells handmade bags at eighty dollars each, with variable costs of thirty dollars per bag, the contribution margin is fifty dollars. If fixed costs are one hundred thousand dollars per year, the breakeven point is two thousand bags — one hundred thousand divided by fifty. Below two thousand bags, the company loses money. Above two thousand, every additional bag generates fifty dollars of profit.\n\nBreakeven analysis becomes even more valuable when combined with forecasting. A forecast is an estimate of future financial results based on historical data, market trends, and management assumptions. Sales forecasts predict how many units the company expects to sell. Cost forecasts estimate how expenses will change. Cash flow forecasts project when money will come in and go out.\n\nGood forecasting is not about predicting the future perfectly — it is about preparing for multiple scenarios. A conservative forecast might assume flat sales growth and rising material costs. An optimistic forecast might assume a new product launch will boost demand by twenty percent. By comparing the breakeven point against different forecast scenarios, managers can assess risk and make informed decisions about pricing, production levels, and investment.\n\nOnce the period ends and actual results are available, the focus shifts to performance evaluation. Performance measurement compares what actually happened against what was planned — the budget, the forecast, or the standard. Did the sales team hit its revenue target? Did the factory keep costs within budget? Did the company achieve its profit goals?\n\nPerformance evaluation must be fair, and fairness requires distinguishing between controllable and uncontrollable factors. A controllable cost is one that a specific manager has the authority and ability to influence. The head of purchasing can negotiate better prices with suppliers — material costs are controllable for that manager. The production supervisor can manage overtime hours and reduce waste — labor efficiency is controllable.\n\nAn uncontrollable cost, by contrast, is one that a manager cannot influence. A sudden government tax increase, a natural disaster that disrupts supply chains, or a corporate decision to reallocate overhead from headquarters — these are uncontrollable factors. Holding a manager accountable for uncontrollable costs is unfair and demotivating. Effective performance evaluation systems separate controllable from uncontrollable variances so that each manager is judged only on what they can actually affect.\n\nBenchmarking adds an external dimension to performance evaluation. While budgets and standards provide internal targets, benchmarks compare a company's performance against external reference points — competitors, industry averages, or best-in-class companies. A Vietnamese textile manufacturer might benchmark its production cost per meter against factories in Bangladesh and China. If its costs are significantly higher, the benchmark reveals a competitive gap that needs to be addressed.\n\nBenchmarking is not just about cost. Companies benchmark quality metrics, delivery times, customer satisfaction scores, and employee productivity. The goal is to identify areas where the company lags behind and to learn from those who perform better.\n\nFrom calculating the breakeven point to building forecasts, from measuring performance against budgets to benchmarking against competitors — these tools transform raw cost data into actionable intelligence. They help managers answer not just what happened, but why it happened and what to do next. And in the language of international business, these conversations happen in English."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Phân tích hòa vốn và đánh giá hiệu quả",
                    "description": "Viết câu sử dụng 6 từ vựng về phân tích hòa vốn, dự báo và đánh giá hiệu quả.",
                    "data": {
                        "vocabList": ["breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'breakeven' để viết một câu về điểm hòa vốn và ý nghĩa của nó đối với quyết định kinh doanh. Ví dụ: The new coffee shop needed to sell at least three hundred cups per day to reach breakeven, which the owner considered achievable given the location's heavy foot traffic.",
                                "targetVocab": "breakeven"
                            },
                            {
                                "prompt": "Dùng từ 'forecast' để viết một câu về dự báo tài chính và cách nó giúp doanh nghiệp chuẩn bị cho tương lai. Ví dụ: The CFO presented three forecast scenarios to the board — optimistic, moderate, and conservative — so that the company could prepare contingency plans for each outcome.",
                                "targetVocab": "forecast"
                            },
                            {
                                "prompt": "Dùng từ 'performance' để viết một câu về đánh giá hiệu quả hoạt động của một bộ phận trong doanh nghiệp. Ví dụ: The annual performance review revealed that the logistics department had reduced delivery times by eighteen percent while keeping transportation costs flat.",
                                "targetVocab": "performance"
                            },
                            {
                                "prompt": "Dùng từ 'benchmark' để viết một câu về cách doanh nghiệp so sánh hiệu quả với đối thủ hoặc trung bình ngành. Ví dụ: After benchmarking its customer service response time against the top five competitors, the company invested in a new call center system to close the gap.",
                                "targetVocab": "benchmark"
                            },
                            {
                                "prompt": "Dùng từ 'controllable' để viết một câu về chi phí có thể kiểm soát và trách nhiệm của nhà quản lý. Ví dụ: The plant manager focused her cost reduction efforts on controllable items like raw material waste and overtime scheduling, where her decisions could make an immediate difference.",
                                "targetVocab": "controllable"
                            },
                            {
                                "prompt": "Dùng từ 'uncontrollable' để viết một câu về yếu tố nằm ngoài tầm kiểm soát của nhà quản lý và cách hệ thống đánh giá nên xử lý chúng. Ví dụ: The regional director's performance report separated uncontrollable costs like the new government carbon tax from controllable costs, ensuring a fair evaluation of her management decisions.",
                                "targetVocab": "uncontrollable"
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
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Ôn lại toàn bộ trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã hoàn thành ba phần học từ vựng và bây giờ nắm trong tay 18 từ vựng tiếng Anh về kế toán chi phí. Hãy cùng ôn lại nhanh trước khi bước vào phần luyện tập tổng hợp.\n\nTrong phần 1, bạn đã học: cost — chi phí, budget — ngân sách, variance — chênh lệch, overhead — chi phí chung, allocation — phân bổ, và direct — trực tiếp. Đây là bộ từ nền tảng giúp bạn hiểu cách doanh nghiệp phân loại chi phí, lập kế hoạch tài chính, và phát hiện khi chi phí thực tế lệch khỏi ngân sách.\n\nTrong phần 2, bạn đã học: indirect — gián tiếp, standard — tiêu chuẩn, actual — thực tế, absorption — hấp thụ, marginal — biên, và contribution — đóng góp. Những từ này đưa bạn vào thế giới phương pháp tính giá thành — từ absorption costing cho báo cáo tài chính đến marginal costing cho quyết định quản trị.\n\nTrong phần 3, bạn đã học: breakeven — hòa vốn, forecast — dự báo, performance — hiệu quả, benchmark — chuẩn đối sánh, controllable — có thể kiểm soát, và uncontrollable — không thể kiểm soát. Đây là bộ công cụ phân tích giúp nhà quản lý nhìn về phía trước và đánh giá kết quả một cách công bằng.\n\nBây giờ, bạn sẽ ôn tập toàn bộ 18 từ qua flashcard và bài viết câu. Hãy tập trung vào những từ bạn cảm thấy chưa chắc chắn nhất. Sau phần ôn tập này, bạn sẽ đọc một bài viết dài sử dụng tất cả 18 từ trong một câu chuyện hoàn chỉnh về kế toán chi phí. Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Ôn tập 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Ôn tập 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Ôn tập 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Ôn tập 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Ôn tập 18 từ: cost, budget, variance, overhead, allocation, direct, indirect, standard, actual, absorption, marginal, contribution, breakeven, forecast, performance, benchmark, controllable, uncontrollable",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập kế toán chi phí",
                    "description": "Viết câu sử dụng 18 từ vựng đã học về kế toán chi phí.",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'cost' để viết một câu về tầm quan trọng của việc hiểu cấu trúc chi phí khi định giá sản phẩm xuất khẩu. Ví dụ: Understanding the full cost structure — including materials, labor, overhead, and shipping — is essential before setting an export price that remains competitive in international markets.",
                                "targetVocab": "cost"
                            },
                            {
                                "prompt": "Dùng từ 'budget' để viết một câu về quy trình lập ngân sách hàng năm và sự tham gia của các bộ phận. Ví dụ: The annual budget process required each department head to submit detailed spending plans, which were then consolidated and reviewed by the finance committee before final approval.",
                                "targetVocab": "budget"
                            },
                            {
                                "prompt": "Dùng từ 'variance' để viết một câu về cách phân tích chênh lệch giúp cải thiện quy trình sản xuất. Ví dụ: Monthly variance reports helped the operations team identify a recurring pattern of material waste on the night shift, leading to targeted retraining that saved the company over fifty thousand dollars per quarter.",
                                "targetVocab": "variance"
                            },
                            {
                                "prompt": "Dùng từ 'overhead' để viết một câu về tác động của chi phí chung khi nhà máy hoạt động dưới công suất. Ví dụ: During the slow season, overhead costs per unit nearly doubled because the same fixed expenses were spread across only half the normal production volume.",
                                "targetVocab": "overhead"
                            },
                            {
                                "prompt": "Dùng từ 'allocation' để viết một câu về tranh luận nội bộ khi thay đổi phương pháp phân bổ chi phí. Ví dụ: The switch from labor-based to activity-based cost allocation revealed that the premium product line was far more profitable than previously thought, while the basic line was barely breaking even.",
                                "targetVocab": "allocation"
                            },
                            {
                                "prompt": "Dùng từ 'direct' để viết một câu về chi phí trực tiếp trong ngành dịch vụ so với ngành sản xuất. Ví dụ: In a consulting firm, the direct cost of a project consists mainly of consultant salaries and travel expenses, unlike manufacturing where direct costs include raw materials and production labor.",
                                "targetVocab": "direct"
                            },
                            {
                                "prompt": "Dùng từ 'indirect' để viết một câu về thách thức khi phân bổ chi phí gián tiếp trong doanh nghiệp đa sản phẩm. Ví dụ: Allocating indirect costs across twelve different product lines required a sophisticated activity-based costing system that tracked how each product consumed shared resources.",
                                "targetVocab": "indirect"
                            },
                            {
                                "prompt": "Dùng từ 'standard' để viết một câu về cách cập nhật chi phí tiêu chuẩn khi điều kiện thị trường thay đổi. Ví dụ: The accounting team updated the standard cost for copper wiring after the commodity price rose by forty percent, ensuring that future variance reports would reflect realistic expectations.",
                                "targetVocab": "standard"
                            },
                            {
                                "prompt": "Dùng từ 'actual' để viết một câu về sự bất ngờ khi chi phí thực tế khác xa dự kiến. Ví dụ: The actual cost of the new product launch was nearly double the original estimate because the marketing campaign required additional digital advertising that had not been planned.",
                                "targetVocab": "actual"
                            },
                            {
                                "prompt": "Dùng từ 'absorption' để viết một câu về ảnh hưởng của phương pháp hấp thụ đến lợi nhuận báo cáo. Ví dụ: Under absorption costing, the company reported higher profits in the fourth quarter because increased production spread fixed overhead across more units, even though sales remained flat.",
                                "targetVocab": "absorption"
                            },
                            {
                                "prompt": "Dùng từ 'marginal' để viết một câu về quyết định ngừng sản xuất một sản phẩm dựa trên phân tích chi phí biên. Ví dụ: The board decided to discontinue the product line after analysis showed that the marginal cost of production exceeded the selling price, meaning every additional unit sold increased the company's losses.",
                                "targetVocab": "marginal"
                            },
                            {
                                "prompt": "Dùng từ 'contribution' để viết một câu về cách sử dụng lợi nhuận gộp biên để ưu tiên sản phẩm khi nguồn lực hạn chế. Ví dụ: When the factory faced a shortage of skilled labor, management prioritized products with the highest contribution margin per labor hour to maximize overall profitability.",
                                "targetVocab": "contribution"
                            },
                            {
                                "prompt": "Dùng từ 'breakeven' để viết một câu về cách nhà đầu tư sử dụng phân tích hòa vốn để đánh giá rủi ro. Ví dụ: The venture capitalist was impressed that the startup's breakeven point was only six months away, suggesting low risk and a quick path to profitability.",
                                "targetVocab": "breakeven"
                            },
                            {
                                "prompt": "Dùng từ 'forecast' để viết một câu về tầm quan trọng của dự báo chính xác trong quản lý chuỗi cung ứng. Ví dụ: An inaccurate demand forecast led to excess inventory of winter clothing that had to be sold at a steep discount, wiping out most of the season's expected profit.",
                                "targetVocab": "forecast"
                            },
                            {
                                "prompt": "Dùng từ 'performance' để viết một câu về hệ thống đánh giá hiệu quả gắn với thưởng cho nhân viên. Ví dụ: The company linked quarterly bonuses to performance metrics including cost reduction targets, on-time delivery rates, and customer satisfaction scores.",
                                "targetVocab": "performance"
                            },
                            {
                                "prompt": "Dùng từ 'benchmark' để viết một câu về cách doanh nghiệp Việt Nam sử dụng chuẩn đối sánh quốc tế. Ví dụ: The Vietnamese electronics manufacturer benchmarked its defect rate against Japanese competitors and set a three-year plan to reduce quality issues by sixty percent.",
                                "targetVocab": "benchmark"
                            },
                            {
                                "prompt": "Dùng từ 'controllable' để viết một câu về nguyên tắc trách nhiệm trong đánh giá nhà quản lý. Ví dụ: The new evaluation system focused exclusively on controllable costs, which motivated department heads to find creative ways to reduce waste and improve efficiency within their own teams.",
                                "targetVocab": "controllable"
                            },
                            {
                                "prompt": "Dùng từ 'uncontrollable' để viết một câu về cách báo cáo tách biệt yếu tố không kiểm soát được để đánh giá công bằng. Ví dụ: The performance report clearly separated uncontrollable factors like currency fluctuations and regulatory changes from controllable operational decisions, giving the board a fair picture of management effectiveness.",
                                "targetVocab": "uncontrollable"
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về kế toán chi phí.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, kể câu chuyện hoàn chỉnh về kế toán chi phí — từ phân loại chi phí đến đánh giá hiệu quả hoạt động.\n\nBạn sẽ gặp lại cost, budget, variance, overhead, allocation, direct trong phần mở đầu về cách doanh nghiệp phân loại và kiểm soát chi phí. Tiếp theo, indirect, standard, actual, absorption, marginal, contribution sẽ giúp bạn hiểu các phương pháp tính giá thành và phân tích lợi nhuận. Và cuối cùng, breakeven, forecast, performance, benchmark, controllable, uncontrollable sẽ đưa bạn vào thế giới phân tích quản trị và ra quyết định.\n\nHãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, và thử đoán nghĩa trước khi nhìn lại định nghĩa. Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh để tổng hợp những gì đã học. Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Kế toán chi phí — Từ phân loại đến ra quyết định",
                    "description": "Cost accounting is the engine room of business decision-making.",
                    "data": {
                        "text": "Cost accounting is the engine room of business decision-making. While financial accounting looks backward to report what happened, cost accounting looks inward and forward — analyzing how resources are consumed and guiding managers toward better choices. For any company that makes products or delivers services, understanding costs is not optional. It is the foundation of pricing, planning, and performance management.\n\nEvery cost in a business can be classified in multiple ways, but the most fundamental distinction is between direct and indirect costs. A direct cost can be traced to a specific product or service. When a Vietnamese shoe manufacturer buys leather for a particular model, the leather is a direct material cost. The wages of the workers who stitch that model are a direct labor cost. These costs are straightforward to measure and assign.\n\nIndirect costs are different. The electricity bill for the entire factory, the salary of the quality control manager, the depreciation of shared equipment — these costs support all products but cannot be traced to any single one. In manufacturing, indirect production costs are grouped together as overhead. Managing overhead is one of the greatest challenges in cost accounting because it must be distributed across products through a process called allocation.\n\nAllocation requires choosing a basis that reflects how products consume overhead resources. A factory might allocate overhead based on machine hours, direct labor hours, or the number of units produced. The choice matters enormously. If a high-volume product and a low-volume product share the same factory, the allocation method determines how much overhead each product bears — and therefore how profitable each appears to be.\n\nOnce costs are classified and allocated, the next step is planning. The budget is the financial blueprint for the coming period. It translates the company's strategic goals into specific numbers — how much revenue to expect, how much to spend on materials, labor, and overhead, and how much profit to target. A well-constructed budget aligns every department around common financial objectives.\n\nBut reality rarely matches the plan exactly. When the period ends, managers compare actual results against the budget. The difference is called a variance. A favorable variance means actual costs were lower than budgeted — good news. An unfavorable variance means costs exceeded the plan — a signal that something went wrong. Variance analysis breaks these differences into components, helping managers pinpoint whether the problem was price, quantity, efficiency, or volume.\n\nThe comparison between standard and actual costs is central to variance analysis. Standard costs are predetermined benchmarks — what each unit should cost under normal operating conditions. They include standard material costs, standard labor costs, and standard overhead rates. When actual costs deviate from these standards, the variance tells a story. A material price variance might reveal that a supplier raised prices. A labor efficiency variance might indicate that a new production process is slower than expected.\n\nHow costs are assigned to products depends on the costing method. Absorption costing — the method required for external financial reporting — assigns both direct and indirect costs to each unit. Every product absorbs a share of fixed overhead. This ensures that the full cost of manufacturing is reflected in inventory values and cost of goods sold. However, absorption costing can distort decision-making because the cost per unit changes with production volume.\n\nMarginal costing offers an alternative perspective. It assigns only variable costs to products and treats fixed overhead as a period expense. The key metric in marginal costing is the contribution margin — the difference between selling price and variable cost per unit. Contribution tells managers how much each product contributes toward covering fixed costs and generating profit.\n\nContribution analysis is especially useful for short-term decisions. Should the company accept a special order at a discounted price? If the price exceeds the marginal cost, the order generates a positive contribution — even if it does not cover the full absorption cost. Should the company discontinue a product line? If the product still generates a positive contribution, dropping it would actually reduce total profit because the fixed costs would remain.\n\nBreakeven analysis ties these concepts together. The breakeven point is the sales volume at which total contribution exactly covers total fixed costs — the company earns zero profit. Below breakeven, the company loses money. Above breakeven, every additional unit sold generates profit equal to its contribution margin. Knowing the breakeven point helps managers set sales targets, evaluate pricing strategies, and assess the risk of new ventures.\n\nLooking ahead requires forecasting. A forecast uses historical data, market intelligence, and management judgment to estimate future revenues, costs, and cash flows. Unlike a budget, which is a fixed target, a forecast is updated regularly as new information becomes available. Rolling forecasts — updated monthly or quarterly — give managers a continuously refreshed view of where the business is heading.\n\nWhen forecasts are compared against actual results, the focus shifts to performance evaluation. Performance measurement answers the question: how well did we do? But meaningful evaluation requires context. Comparing a factory's costs against its budget is useful. Comparing those costs against a benchmark — an industry average, a competitor's published figures, or the company's own best historical result — adds an external perspective that budgets alone cannot provide.\n\nFair performance evaluation also requires distinguishing between controllable and uncontrollable factors. A plant manager can control material usage, labor scheduling, and maintenance spending — these are controllable costs. But she cannot control a government decision to raise electricity tariffs, a global commodity price spike, or a corporate headquarters decision to reallocate shared service charges. These are uncontrollable costs. Holding managers accountable only for controllable costs creates a system that is both fair and motivating.\n\nFrom the direct cost of raw materials to the indirect overhead of a shared factory, from the standard cost set at the beginning of the year to the actual cost recorded at the end, from the absorption of fixed costs into product values to the marginal contribution that guides short-term decisions — cost accounting weaves together a comprehensive framework for understanding how businesses spend money and create value. The breakeven point marks the threshold of survival. Forecasts illuminate the path ahead. Performance benchmarks reveal where improvement is needed. And the distinction between controllable and uncontrollable costs ensures that accountability is fair.\n\nIn a world where Vietnamese companies compete globally, negotiate with international partners, and report to foreign investors, the ability to discuss cost accounting in English is not just an academic skill — it is a professional necessity. These eighteen words are your foundation."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Kế toán chi phí — Từ phân loại đến ra quyết định",
                    "description": "Cost accounting is the engine room of business decision-making.",
                    "data": {
                        "text": "Cost accounting is the engine room of business decision-making. While financial accounting looks backward to report what happened, cost accounting looks inward and forward — analyzing how resources are consumed and guiding managers toward better choices. For any company that makes products or delivers services, understanding costs is not optional. It is the foundation of pricing, planning, and performance management.\n\nEvery cost in a business can be classified in multiple ways, but the most fundamental distinction is between direct and indirect costs. A direct cost can be traced to a specific product or service. When a Vietnamese shoe manufacturer buys leather for a particular model, the leather is a direct material cost. The wages of the workers who stitch that model are a direct labor cost. These costs are straightforward to measure and assign.\n\nIndirect costs are different. The electricity bill for the entire factory, the salary of the quality control manager, the depreciation of shared equipment — these costs support all products but cannot be traced to any single one. In manufacturing, indirect production costs are grouped together as overhead. Managing overhead is one of the greatest challenges in cost accounting because it must be distributed across products through a process called allocation.\n\nAllocation requires choosing a basis that reflects how products consume overhead resources. A factory might allocate overhead based on machine hours, direct labor hours, or the number of units produced. The choice matters enormously. If a high-volume product and a low-volume product share the same factory, the allocation method determines how much overhead each product bears — and therefore how profitable each appears to be.\n\nOnce costs are classified and allocated, the next step is planning. The budget is the financial blueprint for the coming period. It translates the company's strategic goals into specific numbers — how much revenue to expect, how much to spend on materials, labor, and overhead, and how much profit to target. A well-constructed budget aligns every department around common financial objectives.\n\nBut reality rarely matches the plan exactly. When the period ends, managers compare actual results against the budget. The difference is called a variance. A favorable variance means actual costs were lower than budgeted — good news. An unfavorable variance means costs exceeded the plan — a signal that something went wrong. Variance analysis breaks these differences into components, helping managers pinpoint whether the problem was price, quantity, efficiency, or volume.\n\nThe comparison between standard and actual costs is central to variance analysis. Standard costs are predetermined benchmarks — what each unit should cost under normal operating conditions. They include standard material costs, standard labor costs, and standard overhead rates. When actual costs deviate from these standards, the variance tells a story. A material price variance might reveal that a supplier raised prices. A labor efficiency variance might indicate that a new production process is slower than expected.\n\nHow costs are assigned to products depends on the costing method. Absorption costing — the method required for external financial reporting — assigns both direct and indirect costs to each unit. Every product absorbs a share of fixed overhead. This ensures that the full cost of manufacturing is reflected in inventory values and cost of goods sold. However, absorption costing can distort decision-making because the cost per unit changes with production volume.\n\nMarginal costing offers an alternative perspective. It assigns only variable costs to products and treats fixed overhead as a period expense. The key metric in marginal costing is the contribution margin — the difference between selling price and variable cost per unit. Contribution tells managers how much each product contributes toward covering fixed costs and generating profit.\n\nContribution analysis is especially useful for short-term decisions. Should the company accept a special order at a discounted price? If the price exceeds the marginal cost, the order generates a positive contribution — even if it does not cover the full absorption cost. Should the company discontinue a product line? If the product still generates a positive contribution, dropping it would actually reduce total profit because the fixed costs would remain.\n\nBreakeven analysis ties these concepts together. The breakeven point is the sales volume at which total contribution exactly covers total fixed costs — the company earns zero profit. Below breakeven, the company loses money. Above breakeven, every additional unit sold generates profit equal to its contribution margin. Knowing the breakeven point helps managers set sales targets, evaluate pricing strategies, and assess the risk of new ventures.\n\nLooking ahead requires forecasting. A forecast uses historical data, market intelligence, and management judgment to estimate future revenues, costs, and cash flows. Unlike a budget, which is a fixed target, a forecast is updated regularly as new information becomes available. Rolling forecasts — updated monthly or quarterly — give managers a continuously refreshed view of where the business is heading.\n\nWhen forecasts are compared against actual results, the focus shifts to performance evaluation. Performance measurement answers the question: how well did we do? But meaningful evaluation requires context. Comparing a factory's costs against its budget is useful. Comparing those costs against a benchmark — an industry average, a competitor's published figures, or the company's own best historical result — adds an external perspective that budgets alone cannot provide.\n\nFair performance evaluation also requires distinguishing between controllable and uncontrollable factors. A plant manager can control material usage, labor scheduling, and maintenance spending — these are controllable costs. But she cannot control a government decision to raise electricity tariffs, a global commodity price spike, or a corporate headquarters decision to reallocate shared service charges. These are uncontrollable costs. Holding managers accountable only for controllable costs creates a system that is both fair and motivating.\n\nFrom the direct cost of raw materials to the indirect overhead of a shared factory, from the standard cost set at the beginning of the year to the actual cost recorded at the end, from the absorption of fixed costs into product values to the marginal contribution that guides short-term decisions — cost accounting weaves together a comprehensive framework for understanding how businesses spend money and create value. The breakeven point marks the threshold of survival. Forecasts illuminate the path ahead. Performance benchmarks reveal where improvement is needed. And the distinction between controllable and uncontrollable costs ensures that accountability is fair.\n\nIn a world where Vietnamese companies compete globally, negotiate with international partners, and report to foreign investors, the ability to discuss cost accounting in English is not just an academic skill — it is a professional necessity. These eighteen words are your foundation."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Kế toán chi phí — Từ phân loại đến ra quyết định",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Cost accounting is the engine room of business decision-making. While financial accounting looks backward to report what happened, cost accounting looks inward and forward — analyzing how resources are consumed and guiding managers toward better choices. For any company that makes products or delivers services, understanding costs is not optional. It is the foundation of pricing, planning, and performance management.\n\nEvery cost in a business can be classified in multiple ways, but the most fundamental distinction is between direct and indirect costs. A direct cost can be traced to a specific product or service. When a Vietnamese shoe manufacturer buys leather for a particular model, the leather is a direct material cost. The wages of the workers who stitch that model are a direct labor cost. These costs are straightforward to measure and assign.\n\nIndirect costs are different. The electricity bill for the entire factory, the salary of the quality control manager, the depreciation of shared equipment — these costs support all products but cannot be traced to any single one. In manufacturing, indirect production costs are grouped together as overhead. Managing overhead is one of the greatest challenges in cost accounting because it must be distributed across products through a process called allocation.\n\nAllocation requires choosing a basis that reflects how products consume overhead resources. A factory might allocate overhead based on machine hours, direct labor hours, or the number of units produced. The choice matters enormously. If a high-volume product and a low-volume product share the same factory, the allocation method determines how much overhead each product bears — and therefore how profitable each appears to be.\n\nOnce costs are classified and allocated, the next step is planning. The budget is the financial blueprint for the coming period. It translates the company's strategic goals into specific numbers — how much revenue to expect, how much to spend on materials, labor, and overhead, and how much profit to target. A well-constructed budget aligns every department around common financial objectives.\n\nBut reality rarely matches the plan exactly. When the period ends, managers compare actual results against the budget. The difference is called a variance. A favorable variance means actual costs were lower than budgeted — good news. An unfavorable variance means costs exceeded the plan — a signal that something went wrong. Variance analysis breaks these differences into components, helping managers pinpoint whether the problem was price, quantity, efficiency, or volume.\n\nThe comparison between standard and actual costs is central to variance analysis. Standard costs are predetermined benchmarks — what each unit should cost under normal operating conditions. They include standard material costs, standard labor costs, and standard overhead rates. When actual costs deviate from these standards, the variance tells a story. A material price variance might reveal that a supplier raised prices. A labor efficiency variance might indicate that a new production process is slower than expected.\n\nHow costs are assigned to products depends on the costing method. Absorption costing — the method required for external financial reporting — assigns both direct and indirect costs to each unit. Every product absorbs a share of fixed overhead. This ensures that the full cost of manufacturing is reflected in inventory values and cost of goods sold. However, absorption costing can distort decision-making because the cost per unit changes with production volume.\n\nMarginal costing offers an alternative perspective. It assigns only variable costs to products and treats fixed overhead as a period expense. The key metric in marginal costing is the contribution margin — the difference between selling price and variable cost per unit. Contribution tells managers how much each product contributes toward covering fixed costs and generating profit.\n\nContribution analysis is especially useful for short-term decisions. Should the company accept a special order at a discounted price? If the price exceeds the marginal cost, the order generates a positive contribution — even if it does not cover the full absorption cost. Should the company discontinue a product line? If the product still generates a positive contribution, dropping it would actually reduce total profit because the fixed costs would remain.\n\nBreakeven analysis ties these concepts together. The breakeven point is the sales volume at which total contribution exactly covers total fixed costs — the company earns zero profit. Below breakeven, the company loses money. Above breakeven, every additional unit sold generates profit equal to its contribution margin. Knowing the breakeven point helps managers set sales targets, evaluate pricing strategies, and assess the risk of new ventures.\n\nLooking ahead requires forecasting. A forecast uses historical data, market intelligence, and management judgment to estimate future revenues, costs, and cash flows. Unlike a budget, which is a fixed target, a forecast is updated regularly as new information becomes available. Rolling forecasts — updated monthly or quarterly — give managers a continuously refreshed view of where the business is heading.\n\nWhen forecasts are compared against actual results, the focus shifts to performance evaluation. Performance measurement answers the question: how well did we do? But meaningful evaluation requires context. Comparing a factory's costs against its budget is useful. Comparing those costs against a benchmark — an industry average, a competitor's published figures, or the company's own best historical result — adds an external perspective that budgets alone cannot provide.\n\nFair performance evaluation also requires distinguishing between controllable and uncontrollable factors. A plant manager can control material usage, labor scheduling, and maintenance spending — these are controllable costs. But she cannot control a government decision to raise electricity tariffs, a global commodity price spike, or a corporate headquarters decision to reallocate shared service charges. These are uncontrollable costs. Holding managers accountable only for controllable costs creates a system that is both fair and motivating.\n\nFrom the direct cost of raw materials to the indirect overhead of a shared factory, from the standard cost set at the beginning of the year to the actual cost recorded at the end, from the absorption of fixed costs into product values to the marginal contribution that guides short-term decisions — cost accounting weaves together a comprehensive framework for understanding how businesses spend money and create value. The breakeven point marks the threshold of survival. Forecasts illuminate the path ahead. Performance benchmarks reveal where improvement is needed. And the distinction between controllable and uncontrollable costs ensures that accountability is fair.\n\nIn a world where Vietnamese companies compete globally, negotiate with international partners, and report to foreign investors, the ability to discuss cost accounting in English is not just an academic skill — it is a professional necessity. These eighteen words are your foundation."
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích kế toán chi phí",
                    "description": "Viết đoạn văn tiếng Anh phân tích về kế toán chi phí sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["cost", "budget", "variance", "overhead", "allocation", "direct", "indirect", "standard", "actual", "absorption", "marginal", "contribution", "breakeven", "forecast", "performance", "benchmark", "controllable", "uncontrollable"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến kế toán chi phí. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích cách một nhà máy sản xuất sử dụng kế toán chi phí để quyết định có nên nhận một đơn hàng đặc biệt với giá thấp hơn bình thường. Giải thích vai trò của marginal cost, contribution margin, và breakeven analysis trong quyết định này, và vì sao kết quả có thể khác nhau giữa absorption costing và marginal costing.",
                            "Hãy phân tích cách một doanh nghiệp Việt Nam sử dụng hệ thống đánh giá hiệu quả dựa trên variance analysis và benchmarking. Giải thích vì sao việc phân biệt controllable và uncontrollable costs là quan trọng, và cách forecast giúp nhà quản lý chuẩn bị cho những thay đổi trong tương lai."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần hành động thực tiễn.",
                    "data": {
                        "text": "Bạn vừa hoàn thành bài học về Kế toán chi phí — Cost Accounting. 18 từ vựng, 3 bài đọc, hàng chục ví dụ thực tế. Bây giờ, hãy biến kiến thức thành hành động.\n\nTôi muốn ôn lại 6 từ quan trọng nhất — lần này với góc nhìn thực tiễn, hướng về những gì bạn sẽ làm tiếp theo.\n\nVariance — chênh lệch. Đây là từ bạn sẽ gặp nhiều nhất trong sự nghiệp kế toán quản trị. Mỗi tháng, mỗi quý, bạn sẽ phải giải thích vì sao con số thực tế khác con số kế hoạch. Hành động: Lần tới khi bạn đọc một báo cáo tài chính, hãy tìm phần variance analysis và thử giải thích nguyên nhân bằng tiếng Anh. Ví dụ mới: The CEO asked the finance team to explain every variance exceeding five percent of the budget, turning the monthly review meeting into a rigorous accountability session.\n\nContribution — đóng góp, lợi nhuận gộp biên. Đây là thước đo mà mọi nhà quản lý giỏi đều dùng hàng ngày. Sản phẩm nào đóng góp nhiều nhất? Khách hàng nào mang lại giá trị cao nhất? Hành động: Thử tính contribution margin cho một sản phẩm bạn biết — giá bán trừ chi phí biến đổi. Ví dụ mới: The sales team was trained to focus on products with the highest contribution margin rather than simply chasing the highest revenue, which transformed the company's profitability within two quarters.\n\nBreakeven — hòa vốn. Mỗi dự án mới, mỗi sản phẩm mới, mỗi chi nhánh mới — câu hỏi đầu tiên luôn là: bao lâu thì hòa vốn? Hành động: Nếu bạn có ý tưởng kinh doanh, hãy thử tính breakeven point bằng tiếng Anh — Fixed Costs ÷ Contribution per Unit. Ví dụ mới: The franchise owner calculated that the new location would reach breakeven within fourteen months, making it a lower-risk investment compared to the previous store that took twenty-two months.\n\nForecast — dự báo. Trong thế giới kinh doanh, người nào nhìn xa hơn sẽ chuẩn bị tốt hơn. Forecast không phải là đoán — nó là phân tích có hệ thống. Hành động: Theo dõi một chỉ số kinh tế Việt Nam (CPI, tỷ giá, giá nguyên liệu) và thử viết một đoạn forecast ngắn bằng tiếng Anh. Ví dụ mới: The finance director updated the quarterly forecast after the central bank announced an interest rate cut, projecting lower borrowing costs and stronger consumer spending in the second half of the year.\n\nBenchmark — chuẩn đối sánh. Bạn không thể biết mình giỏi hay dở nếu không có điểm so sánh. Benchmark cho bạn bối cảnh — bạn đang ở đâu so với thị trường, so với đối thủ, so với chính mình năm ngoái. Hành động: Tìm một chỉ số ngành (industry benchmark) liên quan đến lĩnh vực bạn quan tâm và so sánh với một doanh nghiệp cụ thể. Ví dụ mới: After benchmarking employee productivity against regional competitors, the HR team proposed a skills development program that increased output per worker by twenty-three percent within one year.\n\nOverhead — chi phí chung. Đây là kẻ thù thầm lặng của lợi nhuận. Overhead không biến mất khi doanh thu giảm — nó vẫn ở đó, ăn mòn từng đồng lợi nhuận. Hiểu overhead là hiểu vì sao nhiều doanh nghiệp có doanh thu cao nhưng lợi nhuận thấp. Hành động: Liệt kê các khoản overhead của một doanh nghiệp bạn biết và thử phân bổ chúng cho từng sản phẩm. Ví dụ mới: The startup kept its overhead deliberately low by using co-working spaces and cloud-based tools, allowing it to reach breakeven with far fewer customers than traditional competitors.\n\nĐó là 6 từ — và 6 hành động cụ thể bạn có thể thực hiện ngay tuần này. Kế toán chi phí không phải là lý thuyết trên giảng đường — nó là công cụ thực tế mà bạn sẽ dùng mỗi ngày trong sự nghiệp.\n\nCòn ba bài học nữa trong chuỗi Kế toán và Tài chính doanh nghiệp — Auditing, Capital Structure, và Corporate Governance. Mỗi bài sẽ mở ra một góc nhìn mới. Nhưng hôm nay, hãy bắt đầu với những hành động nhỏ. Mở một báo cáo chi phí. Tính một contribution margin. Viết một câu variance analysis bằng tiếng Anh.\n\nKiến thức chỉ có giá trị khi bạn sử dụng nó. Hãy bắt đầu ngay hôm nay."
                    }
                }
            ]
        }
    ]
}

# --- Validation ---
def validate(content):
    errors = []
    sessions = content.get("learningSessions", [])
    if len(sessions) != 5:
        errors.append(f"Expected 5 sessions, got {len(sessions)}")

    # Session 1-3: 10 activities each
    expected_seq_123 = ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3", "reading", "speakReading", "readAlong", "writingSentence"]
    for i in range(3):
        acts = sessions[i]["activities"]
        seq = [a["activityType"] for a in acts]
        if seq != expected_seq_123:
            errors.append(f"Session {i+1} activity sequence mismatch: {seq}")
        # Check vocabList length = 6
        for a in acts:
            if a["activityType"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"):
                vl = a["data"].get("vocabList", [])
                if len(vl) != 6:
                    errors.append(f"Session {i+1} {a['activityType']} vocabList length {len(vl)} != 6")
        # Check viewFlashcards == speakFlashcards vocabList
        vf = [a for a in acts if a["activityType"] == "viewFlashcards"][0]["data"]["vocabList"]
        sf = [a for a in acts if a["activityType"] == "speakFlashcards"][0]["data"]["vocabList"]
        if vf != sf:
            errors.append(f"Session {i+1} viewFlashcards/speakFlashcards vocabList mismatch")

    # Session 4: 7 activities
    expected_seq_4 = ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3", "writingSentence"]
    acts4 = sessions[3]["activities"]
    seq4 = [a["activityType"] for a in acts4]
    if seq4 != expected_seq_4:
        errors.append(f"Session 4 activity sequence mismatch: {seq4}")
    for a in acts4:
        if a["activityType"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"):
            vl = a["data"].get("vocabList", [])
            if len(vl) != 18:
                errors.append(f"Session 4 {a['activityType']} vocabList length {len(vl)} != 18")

    # Session 5: 6 activities
    expected_seq_5 = ["introAudio", "reading", "speakReading", "readAlong", "writingParagraph", "introAudio"]
    acts5 = sessions[4]["activities"]
    seq5 = [a["activityType"] for a in acts5]
    if seq5 != expected_seq_5:
        errors.append(f"Session 5 activity sequence mismatch: {seq5}")

    # Check all activities have activityType, title, description, data
    strip_keys = {"mp3Url", "illustrationSet", "chapterBookmarks", "segments", "whiteboardItems", "userReadingId", "lessonUniqueId", "curriculumTags", "taskId", "imageId"}
    for si, s in enumerate(sessions):
        for ai, a in enumerate(s["activities"]):
            for field in ("activityType", "title", "description", "data"):
                if field not in a:
                    errors.append(f"Session {si+1} activity {ai+1} missing '{field}'")
            # Check no strip keys
            for key in strip_keys:
                if key in a:
                    errors.append(f"Session {si+1} activity {ai+1} has strip key '{key}' at activity level")
                if key in a.get("data", {}):
                    errors.append(f"Session {si+1} activity {ai+1} has strip key '{key}' in data")

    # Check all vocabList entries are lowercase strings
    for si, s in enumerate(sessions):
        for ai, a in enumerate(s["activities"]):
            vl = a.get("data", {}).get("vocabList", None)
            if vl is not None:
                for w in vl:
                    if not isinstance(w, str) or w != w.lower():
                        errors.append(f"Session {si+1} activity {ai+1} vocabList entry '{w}' not lowercase string")

    # Check contentTypeTags
    if content.get("contentTypeTags") != []:
        errors.append(f"contentTypeTags should be [], got {content.get('contentTypeTags')}")

    return errors

errors = validate(content)
if errors:
    print("VALIDATION ERRORS:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("Validation passed!")

# --- Create curriculum ---
token = get_firebase_id_token(UID)
res = requests.post(f"{API_BASE}/curriculum/create", json={
    "firebaseIdToken": token,
    "language": "en",
    "userLanguage": "vi",
    "content": json.dumps(content)
})
res.raise_for_status()
curriculum_id = res.json()["id"]
print(f"Created: {curriculum_id}")
print(f"Title: {content['title']}")

# --- Duplicate check ---
print("\n--- Duplicate Check ---")
print(f"SELECT id, content->>'title' as title, created_at FROM curriculum")
print(f"WHERE content->>'title' = '{content['title']}' AND uid = '{UID}' ORDER BY created_at;")
