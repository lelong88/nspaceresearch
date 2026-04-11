import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# Series C, Curriculum 5: Supply Chains – Chuỗi Cung Ứng Toàn Cầu
# Description tone: metaphor_led
# Farewell tone: warm accountability
# W1: logistics, supply, chain, procurement, inventory, warehouse
# W2: freight, customs, clearance, shipment, container, transit
# W3: disruption, resilience, diversification, nearshoring, traceability, optimization

content = {
    "title": "Supply Chains – Chuỗi Cung Ứng Toàn Cầu",
    "contentTypeTags": [],
    "description": "CHUỖI CUNG ỨNG LÀ MẠCH MÁU CỦA NỀN KINH TẾ TOÀN CẦU — VÀ BẠN CHƯA BIẾT ĐỌC NHỊP ĐẬP CỦA NÓ.\n\nMỗi chiếc điện thoại bạn cầm trên tay đã đi qua ít nhất 6 quốc gia trước khi đến Việt Nam — từ mỏ khoáng sản ở Congo, nhà máy chip ở Đài Loan, dây chuyền lắp ráp ở Trung Quốc, đến kho hàng ở Hải Phòng. Bạn biết điều đó, nhưng khi đọc báo cáo logistics bằng tiếng Anh, bạn có thật sự hiểu freight forwarding khác gì customs clearance không?\n\nHãy nghĩ về chuỗi cung ứng như hệ tuần hoàn của cơ thể — mỗi mắt xích là một mạch máu, mỗi sự gián đoạn là một cục máu đông. Khi đại dịch COVID-19 làm tắc nghẽn cảng biển toàn cầu, cả thế giới mới nhận ra chuỗi cung ứng mong manh đến mức nào. Và ngôn ngữ để hiểu, phân tích, và giải quyết vấn đề đó — là tiếng Anh.\n\n18 từ vựng trong bài học này sẽ giúp bạn đọc hiểu báo cáo về logistics, procurement, và supply chain management mà không cần dừng lại tra từ. Bạn sẽ tự tin thảo luận về disruption, resilience, và nearshoring trong lớp học hoặc phòng họp.\n\nTừ logistics đến optimization — bạn vừa nâng cấp tư duy về chuỗi cung ứng toàn cầu, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc.",
    "preview": {
        "text": "Khám phá 18 từ vựng tiếng Anh cốt lõi về chuỗi cung ứng toàn cầu — hệ thống kết nối mọi sản phẩm bạn dùng hàng ngày với hàng trăm quốc gia trên thế giới. Bạn sẽ học logistics, supply, chain, procurement, inventory, warehouse trong phần đầu tiên, nơi bài đọc giải thích cách một sản phẩm đi từ nguyên liệu thô đến tay người tiêu dùng qua hệ thống kho bãi và mua sắm. Tiếp theo là freight, customs, clearance, shipment, container, transit — những từ giúp bạn hiểu dòng chảy hàng hóa qua biên giới, từ vận tải đường biển đến thông quan hải quan. Cuối cùng, disruption, resilience, diversification, nearshoring, traceability, optimization đưa bạn vào thế giới quản trị rủi ro chuỗi cung ứng — từ gián đoạn do đại dịch đến chiến lược đa dạng hóa nguồn cung. Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, bạn sẽ tự tin đọc hiểu tài liệu về supply chain management bằng tiếng Anh."
    },
    "learningSessions": [
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Chào mừng bạn đến với bài học về chuỗi cung ứng toàn cầu — hệ thống kết nối mọi sản phẩm với thế giới.",
                    "data": {
                        "text": "Chào mừng bạn đến với bài học cuối cùng trong chuỗi từ vựng Thương mại quốc tế — chủ đề hôm nay là Chuỗi cung ứng toàn cầu, hay trong tiếng Anh là Global Supply Chains. Nếu thương mại quốc tế là dòng chảy hàng hóa giữa các quốc gia, thì chuỗi cung ứng chính là hệ thống ống dẫn — từ nguyên liệu thô ở một châu lục đến sản phẩm hoàn chỉnh trên kệ hàng ở châu lục khác.\n\nTrong phần này, bạn sẽ học 6 từ vựng: logistics, supply, chain, procurement, inventory, và warehouse. Đây là những từ nền tảng mà bạn sẽ gặp trong bất kỳ khóa học nào về quản trị chuỗi cung ứng.\n\nTừ đầu tiên là logistics — danh từ — nghĩa là hậu cần, hoạt động lập kế hoạch và quản lý dòng chảy hàng hóa từ điểm xuất phát đến điểm đến cuối cùng. Ví dụ: 'Efficient logistics can reduce delivery times from weeks to days, giving companies a significant competitive edge.' Trong bài đọc, logistics mô tả toàn bộ quá trình vận chuyển, lưu kho và phân phối hàng hóa — xương sống của mọi chuỗi cung ứng.\n\nTừ thứ hai là supply — danh từ và động từ — nghĩa là cung cấp, nguồn cung. Trong ngữ cảnh chuỗi cung ứng, supply là dòng hàng hóa và nguyên liệu chảy từ nhà sản xuất đến người tiêu dùng. Ví dụ: 'When supply cannot keep up with demand, prices rise and shortages appear on store shelves.' Trong bài đọc, supply là từ khóa trung tâm — mọi hoạt động trong chuỗi cung ứng đều nhằm đảm bảo nguồn cung liên tục.\n\nTừ thứ ba là chain — danh từ — nghĩa là chuỗi, dây chuyền. Supply chain là chuỗi cung ứng — mạng lưới các tổ chức, con người, hoạt động và tài nguyên liên kết với nhau để đưa sản phẩm từ nguyên liệu thô đến tay người tiêu dùng. Ví dụ: 'A modern supply chain can involve dozens of companies across multiple countries, each responsible for a different stage of production.' Trong bài đọc, chain nhấn mạnh tính liên kết — mỗi mắt xích yếu có thể làm sụp đổ toàn bộ hệ thống.\n\nTừ thứ tư là procurement — danh từ — nghĩa là mua sắm, thu mua. Procurement là quá trình tìm kiếm, đánh giá và mua nguyên vật liệu hoặc dịch vụ từ nhà cung cấp bên ngoài. Ví dụ: 'Strategic procurement helps companies find reliable suppliers who offer the best combination of quality, price, and delivery speed.' Trong bài đọc, procurement là bước đầu tiên trong chuỗi cung ứng — quyết định mua gì, từ ai, và với giá nào.\n\nTừ thứ năm là inventory — danh từ — nghĩa là hàng tồn kho, kho hàng. Inventory là toàn bộ hàng hóa mà một doanh nghiệp đang giữ — từ nguyên liệu thô đến thành phẩm chờ bán. Ví dụ: 'Holding too much inventory ties up capital, but holding too little risks running out of stock when customers place orders.' Trong bài đọc, inventory là bài toán cân bằng — giữ đủ để đáp ứng nhu cầu nhưng không quá nhiều để lãng phí.\n\nTừ cuối cùng là warehouse — danh từ — nghĩa là nhà kho, kho hàng. Warehouse là nơi lưu trữ hàng hóa trước khi chúng được phân phối đến điểm bán hoặc khách hàng cuối cùng. Ví dụ: 'Amazon operates hundreds of warehouses around the world, each strategically located to minimize delivery times to nearby customers.' Trong bài đọc, warehouse là mắt xích vật lý quan trọng — nơi hàng hóa dừng chân trước khi tiếp tục hành trình.\n\nBạn đã có 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, sau đó đọc bài viết về cách chuỗi cung ứng vận hành từ nguyên liệu đến sản phẩm nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chuỗi cung ứng — từ nguyên liệu đến sản phẩm",
                    "description": "Every product you use has a story that begins long before it reaches your hands.",
                    "data": {
                        "text": "Every product you use has a story that begins long before it reaches your hands. A smartphone, for example, contains minerals mined in Africa, chips fabricated in Taiwan, screens manufactured in South Korea, and batteries assembled in China. The system that connects all of these stages — from raw material to finished product — is called a supply chain.\n\nAt the heart of every supply chain is logistics — the planning and management of how goods move from one place to another. Logistics covers everything from choosing the fastest shipping route to deciding which warehouse should hold which products. Without effective logistics, even the best products would sit in factories with no way to reach customers.\n\nThe word chain is important because it emphasizes connection. Each company in the supply chain depends on the one before it. If a supplier of rare earth minerals in Congo stops production, a factory in Shenzhen cannot build circuit boards, and a warehouse in Ho Chi Minh City has nothing to ship to retailers. One broken link can halt the entire chain.\n\nBefore any production begins, companies must handle procurement — the process of finding and purchasing the raw materials, components, and services they need. Good procurement is not just about finding the cheapest supplier. It involves evaluating quality, reliability, delivery speed, and ethical practices. A company that sources its materials from unreliable suppliers risks delays that ripple through the entire chain.\n\nOnce materials are purchased and products are made, they must be stored. This is where inventory management becomes critical. Inventory refers to all the goods a company holds at any point — raw materials waiting to be used, products being assembled, and finished goods ready for sale. The challenge is balance. Too much inventory means money is tied up in unsold goods. Too little means customers face empty shelves and long wait times.\n\nPhysical storage happens in warehouses — large facilities designed to receive, organize, and dispatch goods efficiently. Modern warehouses use automation, robotics, and data analytics to track every item in real time. A well-run warehouse can process thousands of orders per day, ensuring that products move quickly from storage to delivery trucks.\n\nTogether, logistics, supply, chain, procurement, inventory, and warehouse form the foundation of global commerce. Understanding these concepts is the first step toward understanding how the modern economy actually works — not in theory, but in the physical movement of goods across borders and oceans."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chuỗi cung ứng — từ nguyên liệu đến sản phẩm",
                    "description": "Every product you use has a story that begins long before it reaches your hands.",
                    "data": {
                        "text": "Every product you use has a story that begins long before it reaches your hands. A smartphone, for example, contains minerals mined in Africa, chips fabricated in Taiwan, screens manufactured in South Korea, and batteries assembled in China. The system that connects all of these stages — from raw material to finished product — is called a supply chain.\n\nAt the heart of every supply chain is logistics — the planning and management of how goods move from one place to another. Logistics covers everything from choosing the fastest shipping route to deciding which warehouse should hold which products. Without effective logistics, even the best products would sit in factories with no way to reach customers.\n\nThe word chain is important because it emphasizes connection. Each company in the supply chain depends on the one before it. If a supplier of rare earth minerals in Congo stops production, a factory in Shenzhen cannot build circuit boards, and a warehouse in Ho Chi Minh City has nothing to ship to retailers. One broken link can halt the entire chain.\n\nBefore any production begins, companies must handle procurement — the process of finding and purchasing the raw materials, components, and services they need. Good procurement is not just about finding the cheapest supplier. It involves evaluating quality, reliability, delivery speed, and ethical practices. A company that sources its materials from unreliable suppliers risks delays that ripple through the entire chain.\n\nOnce materials are purchased and products are made, they must be stored. This is where inventory management becomes critical. Inventory refers to all the goods a company holds at any point — raw materials waiting to be used, products being assembled, and finished goods ready for sale. The challenge is balance. Too much inventory means money is tied up in unsold goods. Too little means customers face empty shelves and long wait times.\n\nPhysical storage happens in warehouses — large facilities designed to receive, organize, and dispatch goods efficiently. Modern warehouses use automation, robotics, and data analytics to track every item in real time. A well-run warehouse can process thousands of orders per day, ensuring that products move quickly from storage to delivery trucks.\n\nTogether, logistics, supply, chain, procurement, inventory, and warehouse form the foundation of global commerce. Understanding these concepts is the first step toward understanding how the modern economy actually works — not in theory, but in the physical movement of goods across borders and oceans."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chuỗi cung ứng — từ nguyên liệu đến sản phẩm",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Every product you use has a story that begins long before it reaches your hands. A smartphone, for example, contains minerals mined in Africa, chips fabricated in Taiwan, screens manufactured in South Korea, and batteries assembled in China. The system that connects all of these stages — from raw material to finished product — is called a supply chain.\n\nAt the heart of every supply chain is logistics — the planning and management of how goods move from one place to another. Logistics covers everything from choosing the fastest shipping route to deciding which warehouse should hold which products. Without effective logistics, even the best products would sit in factories with no way to reach customers.\n\nThe word chain is important because it emphasizes connection. Each company in the supply chain depends on the one before it. If a supplier of rare earth minerals in Congo stops production, a factory in Shenzhen cannot build circuit boards, and a warehouse in Ho Chi Minh City has nothing to ship to retailers. One broken link can halt the entire chain.\n\nBefore any production begins, companies must handle procurement — the process of finding and purchasing the raw materials, components, and services they need. Good procurement is not just about finding the cheapest supplier. It involves evaluating quality, reliability, delivery speed, and ethical practices. A company that sources its materials from unreliable suppliers risks delays that ripple through the entire chain.\n\nOnce materials are purchased and products are made, they must be stored. This is where inventory management becomes critical. Inventory refers to all the goods a company holds at any point — raw materials waiting to be used, products being assembled, and finished goods ready for sale. The challenge is balance. Too much inventory means money is tied up in unsold goods. Too little means customers face empty shelves and long wait times.\n\nPhysical storage happens in warehouses — large facilities designed to receive, organize, and dispatch goods efficiently. Modern warehouses use automation, robotics, and data analytics to track every item in real time. A well-run warehouse can process thousands of orders per day, ensuring that products move quickly from storage to delivery trucks.\n\nTogether, logistics, supply, chain, procurement, inventory, and warehouse form the foundation of global commerce. Understanding these concepts is the first step toward understanding how the modern economy actually works — not in theory, but in the physical movement of goods across borders and oceans."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng chuỗi cung ứng",
                    "description": "Viết câu sử dụng 6 từ vựng về nền tảng chuỗi cung ứng.",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'logistics' để viết một câu về vai trò của hậu cần trong việc đưa sản phẩm đến tay người tiêu dùng. Ví dụ: Vietnam's logistics industry has grown rapidly as the country becomes a major manufacturing hub, with new ports and highways connecting factories to global markets.",
                                "targetVocab": "logistics"
                            },
                            {
                                "prompt": "Dùng từ 'supply' để viết một câu về nguồn cung hàng hóa và tác động khi nguồn cung bị gián đoạn. Ví dụ: The global supply of semiconductor chips fell sharply during the pandemic, forcing automakers to halt production lines for months.",
                                "targetVocab": "supply"
                            },
                            {
                                "prompt": "Dùng từ 'chain' để viết một câu về chuỗi cung ứng và tính liên kết giữa các mắt xích. Ví dụ: A single weak link in the chain can cause delays that cascade through the entire production process, from factory floor to retail shelf.",
                                "targetVocab": "chain"
                            },
                            {
                                "prompt": "Dùng từ 'procurement' để viết một câu về quá trình mua sắm nguyên vật liệu từ nhà cung cấp. Ví dụ: The procurement team spent three months evaluating suppliers in five countries before selecting a partner who met both quality and sustainability standards.",
                                "targetVocab": "procurement"
                            },
                            {
                                "prompt": "Dùng từ 'inventory' để viết một câu về thách thức quản lý hàng tồn kho trong doanh nghiệp. Ví dụ: Keeping inventory levels low reduces storage costs but increases the risk of stockouts when demand suddenly spikes during holiday seasons.",
                                "targetVocab": "inventory"
                            },
                            {
                                "prompt": "Dùng từ 'warehouse' để viết một câu về vai trò của nhà kho trong chuỗi phân phối hiện đại. Ví dụ: The company opened a new automated warehouse near the port of Hai Phong to speed up the distribution of imported electronics across northern Vietnam.",
                                "targetVocab": "warehouse"
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về vận tải và thông quan hàng hóa quốc tế.",
                    "data": {
                        "text": "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: logistics — hậu cần, supply — nguồn cung, chain — chuỗi, procurement — mua sắm, inventory — hàng tồn kho, và warehouse — nhà kho. Bạn đã hiểu cách một chuỗi cung ứng vận hành từ nguyên liệu đến sản phẩm. Bây giờ, chúng ta sẽ đi sâu vào phần quan trọng nhất khi hàng hóa di chuyển qua biên giới — vận tải và thông quan.\n\nTrong phần 2, bạn sẽ học 6 từ mới: freight, customs, clearance, shipment, container, và transit. Những từ này giúp bạn đọc hiểu các tài liệu về xuất nhập khẩu, vận tải quốc tế và thủ tục hải quan.\n\nTừ đầu tiên là freight — danh từ — nghĩa là hàng hóa vận chuyển, hoặc cước phí vận chuyển. Freight bao gồm mọi loại hàng hóa được vận chuyển bằng đường biển, đường bộ, đường sắt hoặc đường hàng không. Ví dụ: 'Ocean freight accounts for over eighty percent of global trade by volume, making it the backbone of international commerce.' Trong bài đọc, freight mô tả dòng hàng hóa khổng lồ di chuyển giữa các châu lục mỗi ngày.\n\nTừ thứ hai là customs — danh từ — nghĩa là hải quan, cơ quan kiểm soát hàng hóa ra vào biên giới quốc gia. Ví dụ: 'All imported goods must pass through customs, where officers check documentation, assess duties, and inspect cargo for prohibited items.' Trong bài đọc, customs là cửa ngõ mà mọi lô hàng phải đi qua — nơi quyết định hàng hóa được phép nhập hay bị giữ lại.\n\nTừ thứ ba là clearance — danh từ — nghĩa là thông quan, quá trình hoàn tất thủ tục hải quan để hàng hóa được phép nhập hoặc xuất. Customs clearance là thông quan hải quan. Ví dụ: 'Delays in customs clearance can add days or even weeks to delivery times, increasing costs for both importers and consumers.' Trong bài đọc, clearance là bước then chốt — nếu giấy tờ không đầy đủ, hàng hóa bị kẹt tại cảng.\n\nTừ thứ tư là shipment — danh từ — nghĩa là lô hàng, chuyến hàng. Shipment là một lượng hàng hóa cụ thể được gửi từ điểm A đến điểm B. Ví dụ: 'The company tracks every shipment in real time using GPS and satellite technology to ensure on-time delivery.' Trong bài đọc, shipment là đơn vị cơ bản của vận tải — mỗi shipment có mã theo dõi, lịch trình và điểm đến riêng.\n\nTừ thứ năm là container — danh từ — nghĩa là container, thùng chứa hàng tiêu chuẩn dùng trong vận tải quốc tế. Container hóa là cuộc cách mạng lớn nhất trong lịch sử vận tải biển. Ví dụ: 'The invention of the standardized shipping container in the 1950s dramatically reduced the cost of moving goods across oceans.' Trong bài đọc, container là biểu tượng của thương mại toàn cầu — những chiếc hộp thép khổng lồ xếp chồng trên tàu biển.\n\nTừ cuối cùng là transit — danh từ — nghĩa là quá cảnh, trung chuyển. Transit là giai đoạn hàng hóa đang trên đường di chuyển từ nơi gửi đến nơi nhận. Ví dụ: 'Goods in transit are vulnerable to damage, theft, and delays, which is why companies purchase cargo insurance.' Trong bài đọc, transit mô tả khoảng thời gian hàng hóa nằm trên tàu, xe tải hoặc máy bay — chưa đến đích nhưng đã rời điểm xuất phát.\n\nSáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết về vận tải quốc tế và thông quan hải quan nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Vận tải và thông quan",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {
                        "vocabList": ["freight", "customs", "clearance", "shipment", "container", "transit"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Vận tải và thông quan",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {
                        "vocabList": ["freight", "customs", "clearance", "shipment", "container", "transit"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Vận tải và thông quan",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {
                        "vocabList": ["freight", "customs", "clearance", "shipment", "container", "transit"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Vận tải và thông quan",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {
                        "vocabList": ["freight", "customs", "clearance", "shipment", "container", "transit"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Vận tải và thông quan",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {
                        "vocabList": ["freight", "customs", "clearance", "shipment", "container", "transit"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Vận tải quốc tế và thông quan hải quan",
                    "description": "Moving goods across borders is far more complex than moving them within a single country.",
                    "data": {
                        "text": "Moving goods across borders is far more complex than moving them within a single country. When a Vietnamese furniture manufacturer ships a container of tables to a buyer in Germany, the journey involves multiple modes of transport, several government agencies, and a mountain of paperwork. Understanding how freight moves through this system is essential for anyone studying international trade.\n\nFreight is the general term for goods being transported from one place to another. It can travel by sea, air, road, or rail. Ocean freight dominates global trade because it is the cheapest way to move large volumes of goods over long distances. A single container ship can carry over twenty thousand containers, each packed with products destined for different countries. Air freight is faster but far more expensive, so it is typically reserved for high-value or time-sensitive goods like electronics, pharmaceuticals, and fresh produce.\n\nThe container revolutionized international shipping. Before containerization, loading and unloading cargo was slow, labor-intensive, and prone to theft. The standardized shipping container — a steel box measuring either twenty or forty feet long — changed everything. Containers can be loaded at a factory, sealed, placed on a truck, transferred to a train, loaded onto a ship, and delivered to a warehouse on another continent without ever being opened in between. This intermodal system dramatically reduced shipping costs and transit times.\n\nTransit refers to the period when goods are in motion between the point of origin and the final destination. During transit, shipments face risks including damage, delays due to weather, port congestion, and even piracy in certain sea lanes. Companies manage these risks through cargo insurance and real-time tracking systems that monitor the location and condition of every shipment.\n\nA shipment is a specific batch of goods sent from one party to another. Each shipment has its own documentation, including a bill of lading, commercial invoice, and packing list. These documents are critical because they are required for customs clearance at the destination country.\n\nCustoms is the government authority responsible for regulating the flow of goods across national borders. Customs officers inspect shipments, verify documentation, assess import duties and taxes, and enforce trade regulations. Every country has its own customs procedures, and navigating them efficiently is a key skill in international logistics.\n\nClearance is the process of getting goods through customs. Customs clearance involves submitting the correct documents, paying any applicable duties, and passing inspections. If a shipment's paperwork is incomplete or inaccurate, clearance can be delayed for days or weeks, resulting in storage fees at the port and late deliveries to customers. Many companies hire customs brokers — specialists who handle clearance on their behalf — to avoid these costly delays.\n\nTogether, freight, customs, clearance, shipment, container, and transit describe the physical journey of goods across borders. Mastering these terms is essential for understanding how global trade actually works on the ground — or rather, on the water."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Vận tải quốc tế và thông quan hải quan",
                    "description": "Moving goods across borders is far more complex than moving them within a single country.",
                    "data": {
                        "text": "Moving goods across borders is far more complex than moving them within a single country. When a Vietnamese furniture manufacturer ships a container of tables to a buyer in Germany, the journey involves multiple modes of transport, several government agencies, and a mountain of paperwork. Understanding how freight moves through this system is essential for anyone studying international trade.\n\nFreight is the general term for goods being transported from one place to another. It can travel by sea, air, road, or rail. Ocean freight dominates global trade because it is the cheapest way to move large volumes of goods over long distances. A single container ship can carry over twenty thousand containers, each packed with products destined for different countries. Air freight is faster but far more expensive, so it is typically reserved for high-value or time-sensitive goods like electronics, pharmaceuticals, and fresh produce.\n\nThe container revolutionized international shipping. Before containerization, loading and unloading cargo was slow, labor-intensive, and prone to theft. The standardized shipping container — a steel box measuring either twenty or forty feet long — changed everything. Containers can be loaded at a factory, sealed, placed on a truck, transferred to a train, loaded onto a ship, and delivered to a warehouse on another continent without ever being opened in between. This intermodal system dramatically reduced shipping costs and transit times.\n\nTransit refers to the period when goods are in motion between the point of origin and the final destination. During transit, shipments face risks including damage, delays due to weather, port congestion, and even piracy in certain sea lanes. Companies manage these risks through cargo insurance and real-time tracking systems that monitor the location and condition of every shipment.\n\nA shipment is a specific batch of goods sent from one party to another. Each shipment has its own documentation, including a bill of lading, commercial invoice, and packing list. These documents are critical because they are required for customs clearance at the destination country.\n\nCustoms is the government authority responsible for regulating the flow of goods across national borders. Customs officers inspect shipments, verify documentation, assess import duties and taxes, and enforce trade regulations. Every country has its own customs procedures, and navigating them efficiently is a key skill in international logistics.\n\nClearance is the process of getting goods through customs. Customs clearance involves submitting the correct documents, paying any applicable duties, and passing inspections. If a shipment's paperwork is incomplete or inaccurate, clearance can be delayed for days or weeks, resulting in storage fees at the port and late deliveries to customers. Many companies hire customs brokers — specialists who handle clearance on their behalf — to avoid these costly delays.\n\nTogether, freight, customs, clearance, shipment, container, and transit describe the physical journey of goods across borders. Mastering these terms is essential for understanding how global trade actually works on the ground — or rather, on the water."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Vận tải quốc tế và thông quan hải quan",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "Moving goods across borders is far more complex than moving them within a single country. When a Vietnamese furniture manufacturer ships a container of tables to a buyer in Germany, the journey involves multiple modes of transport, several government agencies, and a mountain of paperwork. Understanding how freight moves through this system is essential for anyone studying international trade.\n\nFreight is the general term for goods being transported from one place to another. It can travel by sea, air, road, or rail. Ocean freight dominates global trade because it is the cheapest way to move large volumes of goods over long distances. A single container ship can carry over twenty thousand containers, each packed with products destined for different countries. Air freight is faster but far more expensive, so it is typically reserved for high-value or time-sensitive goods like electronics, pharmaceuticals, and fresh produce.\n\nThe container revolutionized international shipping. Before containerization, loading and unloading cargo was slow, labor-intensive, and prone to theft. The standardized shipping container — a steel box measuring either twenty or forty feet long — changed everything. Containers can be loaded at a factory, sealed, placed on a truck, transferred to a train, loaded onto a ship, and delivered to a warehouse on another continent without ever being opened in between. This intermodal system dramatically reduced shipping costs and transit times.\n\nTransit refers to the period when goods are in motion between the point of origin and the final destination. During transit, shipments face risks including damage, delays due to weather, port congestion, and even piracy in certain sea lanes. Companies manage these risks through cargo insurance and real-time tracking systems that monitor the location and condition of every shipment.\n\nA shipment is a specific batch of goods sent from one party to another. Each shipment has its own documentation, including a bill of lading, commercial invoice, and packing list. These documents are critical because they are required for customs clearance at the destination country.\n\nCustoms is the government authority responsible for regulating the flow of goods across national borders. Customs officers inspect shipments, verify documentation, assess import duties and taxes, and enforce trade regulations. Every country has its own customs procedures, and navigating them efficiently is a key skill in international logistics.\n\nClearance is the process of getting goods through customs. Customs clearance involves submitting the correct documents, paying any applicable duties, and passing inspections. If a shipment's paperwork is incomplete or inaccurate, clearance can be delayed for days or weeks, resulting in storage fees at the port and late deliveries to customers. Many companies hire customs brokers — specialists who handle clearance on their behalf — to avoid these costly delays.\n\nTogether, freight, customs, clearance, shipment, container, and transit describe the physical journey of goods across borders. Mastering these terms is essential for understanding how global trade actually works on the ground — or rather, on the water."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Vận tải và thông quan",
                    "description": "Viết câu sử dụng 6 từ vựng về vận tải quốc tế.",
                    "data": {
                        "vocabList": ["freight", "customs", "clearance", "shipment", "container", "transit"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'freight' để viết một câu về vận tải hàng hóa quốc tế bằng đường biển. Ví dụ: Ocean freight rates surged during the pandemic as demand for shipped goods outpaced the available capacity of container vessels worldwide.",
                                "targetVocab": "freight"
                            },
                            {
                                "prompt": "Dùng từ 'customs' để viết một câu về vai trò của hải quan trong kiểm soát hàng hóa nhập khẩu. Ví dụ: Vietnamese customs authorities have modernized their inspection process with electronic declarations, reducing the average processing time from days to hours.",
                                "targetVocab": "customs"
                            },
                            {
                                "prompt": "Dùng từ 'clearance' để viết một câu về quá trình thông quan và tác động khi bị chậm trễ. Ví dụ: The shipment of medical supplies was stuck at the port for a week because incomplete documentation delayed customs clearance.",
                                "targetVocab": "clearance"
                            },
                            {
                                "prompt": "Dùng từ 'shipment' để viết một câu về việc theo dõi lô hàng trong chuỗi cung ứng. Ví dụ: Each shipment is assigned a unique tracking number that allows both the sender and the receiver to monitor its location throughout the journey.",
                                "targetVocab": "shipment"
                            },
                            {
                                "prompt": "Dùng từ 'container' để viết một câu về vai trò của container trong thương mại toàn cầu. Ví dụ: The port of Singapore handles millions of containers each year, serving as a critical transshipment hub connecting Asia with Europe and the Americas.",
                                "targetVocab": "container"
                            },
                            {
                                "prompt": "Dùng từ 'transit' để viết một câu về rủi ro hàng hóa gặp phải trong quá trình vận chuyển. Ví dụ: Perishable goods like seafood require temperature-controlled containers during transit to prevent spoilage before reaching overseas markets.",
                                "targetVocab": "transit"
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về quản trị rủi ro và tối ưu hóa chuỗi cung ứng.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! Hãy cùng ôn lại nhanh những gì bạn đã học. Trong phần 1, bạn đã nắm được 6 từ nền tảng: logistics — hậu cần, supply — nguồn cung, chain — chuỗi, procurement — mua sắm, inventory — hàng tồn kho, và warehouse — nhà kho. Đây là bộ khung cơ bản của chuỗi cung ứng. Trong phần 2, bạn đã học thêm freight — hàng hóa vận chuyển, customs — hải quan, clearance — thông quan, shipment — lô hàng, container — thùng chứa hàng, và transit — quá cảnh. Những từ này giúp bạn hiểu cách hàng hóa di chuyển qua biên giới.\n\nBây giờ, trong phần 3, chúng ta sẽ bước vào khía cạnh quan trọng nhất của chuỗi cung ứng hiện đại: quản trị rủi ro và tối ưu hóa. Đại dịch COVID-19, chiến tranh thương mại, và biến đổi khí hậu đã cho thấy chuỗi cung ứng toàn cầu mong manh đến mức nào. Bạn sẽ học 6 từ mới: disruption, resilience, diversification, nearshoring, traceability, và optimization.\n\nTừ đầu tiên là disruption — danh từ — nghĩa là sự gián đoạn, sự phá vỡ. Trong chuỗi cung ứng, disruption là bất kỳ sự kiện nào làm gián đoạn dòng chảy bình thường của hàng hóa — từ thiên tai đến đại dịch. Ví dụ: 'The Suez Canal blockage in 2021 caused a massive disruption to global shipping, delaying hundreds of vessels and billions of dollars worth of cargo.' Trong bài đọc, disruption là từ khóa trung tâm — mọi chiến lược quản trị chuỗi cung ứng đều bắt đầu từ câu hỏi: làm sao để đối phó khi disruption xảy ra?\n\nTừ thứ hai là resilience — danh từ — nghĩa là khả năng phục hồi, sức chống chịu. Supply chain resilience là khả năng của chuỗi cung ứng phục hồi nhanh chóng sau gián đoạn. Ví dụ: 'Companies that invested in supply chain resilience before the pandemic recovered faster than those that had optimized purely for cost.' Trong bài đọc, resilience là mục tiêu — xây dựng chuỗi cung ứng có thể uốn cong nhưng không gãy.\n\nTừ thứ ba là diversification — danh từ — nghĩa là đa dạng hóa. Trong chuỗi cung ứng, diversification là chiến lược sử dụng nhiều nhà cung cấp, nhiều tuyến vận chuyển, và nhiều địa điểm sản xuất thay vì phụ thuộc vào một nguồn duy nhất. Ví dụ: 'After the chip shortage, many tech companies pursued diversification by sourcing semiconductors from multiple countries instead of relying solely on Taiwan.' Trong bài đọc, diversification là công cụ chính để tăng resilience — không bỏ tất cả trứng vào một giỏ.\n\nTừ thứ tư là nearshoring — danh từ — nghĩa là chuyển sản xuất về gần, chiến lược di chuyển hoạt động sản xuất từ quốc gia xa sang quốc gia gần hơn với thị trường tiêu thụ. Ví dụ: 'Many American companies are nearshoring their manufacturing from China to Mexico to reduce transit times and avoid geopolitical risks.' Trong bài đọc, nearshoring là xu hướng mới — thay vì sản xuất ở nơi rẻ nhất, doanh nghiệp chọn sản xuất ở nơi gần nhất.\n\nTừ thứ năm là traceability — danh từ — nghĩa là khả năng truy xuất nguồn gốc. Traceability là khả năng theo dõi một sản phẩm ngược lại qua toàn bộ chuỗi cung ứng — từ thành phẩm về đến nguyên liệu thô. Ví dụ: 'Consumers increasingly demand traceability in food supply chains, wanting to know exactly where their coffee beans were grown and how they were processed.' Trong bài đọc, traceability là yêu cầu ngày càng quan trọng — cả về đạo đức lẫn an toàn sản phẩm.\n\nTừ cuối cùng là optimization — danh từ — nghĩa là tối ưu hóa. Supply chain optimization là quá trình cải thiện hiệu quả của chuỗi cung ứng — giảm chi phí, rút ngắn thời gian, và nâng cao chất lượng dịch vụ. Ví dụ: 'Through optimization of its delivery routes, the company reduced fuel costs by fifteen percent and cut average delivery times by two days.' Trong bài đọc, optimization là mục tiêu cuối cùng — làm cho chuỗi cung ứng vừa nhanh, vừa rẻ, vừa đáng tin cậy.\n\nTuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard và đọc bài viết cuối cùng về quản trị rủi ro chuỗi cung ứng nhé!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Quản trị rủi ro chuỗi cung ứng",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Quản trị rủi ro chuỗi cung ứng",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Quản trị rủi ro chuỗi cung ứng",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Quản trị rủi ro chuỗi cung ứng",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Quản trị rủi ro chuỗi cung ứng",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Quản trị rủi ro và tối ưu hóa chuỗi cung ứng",
                    "description": "In March 2021, a four-hundred-meter container ship ran aground in the Suez Canal.",
                    "data": {
                        "text": "In March 2021, a four-hundred-meter container ship ran aground in the Suez Canal. For six days, one of the world's most important shipping lanes was completely blocked. Hundreds of vessels waited on both sides, carrying everything from oil to livestock to consumer electronics. The estimated cost of the disruption was nearly ten billion dollars per day in delayed trade. This single event exposed a truth that supply chain professionals had warned about for years: global supply chains are efficient but fragile.\n\nDisruption is any event that interrupts the normal flow of goods through a supply chain. It can be caused by natural disasters, pandemics, geopolitical conflicts, cyberattacks, or even a single ship stuck in a canal. The COVID-19 pandemic was the most severe supply chain disruption in modern history. Factories shut down, ports became congested, and shipping containers ended up in the wrong places. Consumers around the world experienced shortages of everything from toilet paper to computer chips.\n\nThe pandemic forced companies to rethink their approach to supply chain management. For decades, the dominant strategy had been optimization — making supply chains as lean and cost-efficient as possible. Companies reduced inventory to save money, relied on single suppliers to get the best prices, and shipped goods along the cheapest routes. This worked well in normal times but left no margin for error when disruption struck.\n\nNow, the focus has shifted to resilience — the ability of a supply chain to absorb shocks and recover quickly. Building resilience often means accepting higher costs in exchange for greater reliability. A resilient supply chain might hold extra inventory as a buffer, maintain relationships with backup suppliers, and use multiple transportation routes so that a blockage in one lane does not halt everything.\n\nOne of the most important strategies for building resilience is diversification. Instead of sourcing all components from a single country, companies spread their procurement across multiple regions. If a factory in one country shuts down due to a lockdown, production can continue at a factory in another country. Vietnam has benefited enormously from this trend, as multinational companies diversify their manufacturing away from China.\n\nA related trend is nearshoring — moving production closer to the end market. American companies that once manufactured everything in Asia are now setting up factories in Mexico. European companies are shifting production to Turkey and Eastern Europe. Nearshoring reduces transit times, lowers transportation costs, and makes supply chains less vulnerable to disruptions in distant regions.\n\nAnother growing priority is traceability — the ability to track a product backward through every stage of the supply chain, from the finished good on the shelf all the way to the raw materials it was made from. Traceability matters for safety, quality control, and ethics. If a batch of food causes illness, traceability allows companies to identify exactly which farm, factory, and shipment were involved. It also helps verify that products were made without child labor or environmental destruction.\n\nOptimization has not disappeared — it has evolved. Modern supply chain optimization uses artificial intelligence, big data, and predictive analytics to balance cost, speed, and resilience simultaneously. Instead of simply choosing the cheapest option, companies now optimize for the best combination of efficiency and risk management.\n\nThe lesson from recent years is clear: a supply chain that is optimized only for cost is a supply chain waiting to break. The future belongs to supply chains that are resilient, diversified, traceable, and smart enough to adapt when the unexpected happens."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Quản trị rủi ro và tối ưu hóa chuỗi cung ứng",
                    "description": "In March 2021, a four-hundred-meter container ship ran aground in the Suez Canal.",
                    "data": {
                        "text": "In March 2021, a four-hundred-meter container ship ran aground in the Suez Canal. For six days, one of the world's most important shipping lanes was completely blocked. Hundreds of vessels waited on both sides, carrying everything from oil to livestock to consumer electronics. The estimated cost of the disruption was nearly ten billion dollars per day in delayed trade. This single event exposed a truth that supply chain professionals had warned about for years: global supply chains are efficient but fragile.\n\nDisruption is any event that interrupts the normal flow of goods through a supply chain. It can be caused by natural disasters, pandemics, geopolitical conflicts, cyberattacks, or even a single ship stuck in a canal. The COVID-19 pandemic was the most severe supply chain disruption in modern history. Factories shut down, ports became congested, and shipping containers ended up in the wrong places. Consumers around the world experienced shortages of everything from toilet paper to computer chips.\n\nThe pandemic forced companies to rethink their approach to supply chain management. For decades, the dominant strategy had been optimization — making supply chains as lean and cost-efficient as possible. Companies reduced inventory to save money, relied on single suppliers to get the best prices, and shipped goods along the cheapest routes. This worked well in normal times but left no margin for error when disruption struck.\n\nNow, the focus has shifted to resilience — the ability of a supply chain to absorb shocks and recover quickly. Building resilience often means accepting higher costs in exchange for greater reliability. A resilient supply chain might hold extra inventory as a buffer, maintain relationships with backup suppliers, and use multiple transportation routes so that a blockage in one lane does not halt everything.\n\nOne of the most important strategies for building resilience is diversification. Instead of sourcing all components from a single country, companies spread their procurement across multiple regions. If a factory in one country shuts down due to a lockdown, production can continue at a factory in another country. Vietnam has benefited enormously from this trend, as multinational companies diversify their manufacturing away from China.\n\nA related trend is nearshoring — moving production closer to the end market. American companies that once manufactured everything in Asia are now setting up factories in Mexico. European companies are shifting production to Turkey and Eastern Europe. Nearshoring reduces transit times, lowers transportation costs, and makes supply chains less vulnerable to disruptions in distant regions.\n\nAnother growing priority is traceability — the ability to track a product backward through every stage of the supply chain, from the finished good on the shelf all the way to the raw materials it was made from. Traceability matters for safety, quality control, and ethics. If a batch of food causes illness, traceability allows companies to identify exactly which farm, factory, and shipment were involved. It also helps verify that products were made without child labor or environmental destruction.\n\nOptimization has not disappeared — it has evolved. Modern supply chain optimization uses artificial intelligence, big data, and predictive analytics to balance cost, speed, and resilience simultaneously. Instead of simply choosing the cheapest option, companies now optimize for the best combination of efficiency and risk management.\n\nThe lesson from recent years is clear: a supply chain that is optimized only for cost is a supply chain waiting to break. The future belongs to supply chains that are resilient, diversified, traceable, and smart enough to adapt when the unexpected happens."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Quản trị rủi ro và tối ưu hóa chuỗi cung ứng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "In March 2021, a four-hundred-meter container ship ran aground in the Suez Canal. For six days, one of the world's most important shipping lanes was completely blocked. Hundreds of vessels waited on both sides, carrying everything from oil to livestock to consumer electronics. The estimated cost of the disruption was nearly ten billion dollars per day in delayed trade. This single event exposed a truth that supply chain professionals had warned about for years: global supply chains are efficient but fragile.\n\nDisruption is any event that interrupts the normal flow of goods through a supply chain. It can be caused by natural disasters, pandemics, geopolitical conflicts, cyberattacks, or even a single ship stuck in a canal. The COVID-19 pandemic was the most severe supply chain disruption in modern history. Factories shut down, ports became congested, and shipping containers ended up in the wrong places. Consumers around the world experienced shortages of everything from toilet paper to computer chips.\n\nThe pandemic forced companies to rethink their approach to supply chain management. For decades, the dominant strategy had been optimization — making supply chains as lean and cost-efficient as possible. Companies reduced inventory to save money, relied on single suppliers to get the best prices, and shipped goods along the cheapest routes. This worked well in normal times but left no margin for error when disruption struck.\n\nNow, the focus has shifted to resilience — the ability of a supply chain to absorb shocks and recover quickly. Building resilience often means accepting higher costs in exchange for greater reliability. A resilient supply chain might hold extra inventory as a buffer, maintain relationships with backup suppliers, and use multiple transportation routes so that a blockage in one lane does not halt everything.\n\nOne of the most important strategies for building resilience is diversification. Instead of sourcing all components from a single country, companies spread their procurement across multiple regions. If a factory in one country shuts down due to a lockdown, production can continue at a factory in another country. Vietnam has benefited enormously from this trend, as multinational companies diversify their manufacturing away from China.\n\nA related trend is nearshoring — moving production closer to the end market. American companies that once manufactured everything in Asia are now setting up factories in Mexico. European companies are shifting production to Turkey and Eastern Europe. Nearshoring reduces transit times, lowers transportation costs, and makes supply chains less vulnerable to disruptions in distant regions.\n\nAnother growing priority is traceability — the ability to track a product backward through every stage of the supply chain, from the finished good on the shelf all the way to the raw materials it was made from. Traceability matters for safety, quality control, and ethics. If a batch of food causes illness, traceability allows companies to identify exactly which farm, factory, and shipment were involved. It also helps verify that products were made without child labor or environmental destruction.\n\nOptimization has not disappeared — it has evolved. Modern supply chain optimization uses artificial intelligence, big data, and predictive analytics to balance cost, speed, and resilience simultaneously. Instead of simply choosing the cheapest option, companies now optimize for the best combination of efficiency and risk management.\n\nThe lesson from recent years is clear: a supply chain that is optimized only for cost is a supply chain waiting to break. The future belongs to supply chains that are resilient, diversified, traceable, and smart enough to adapt when the unexpected happens."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Quản trị rủi ro chuỗi cung ứng",
                    "description": "Viết câu sử dụng 6 từ vựng về quản trị rủi ro chuỗi cung ứng.",
                    "data": {
                        "vocabList": ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'disruption' để viết một câu về sự gián đoạn chuỗi cung ứng do một sự kiện bất ngờ. Ví dụ: The eruption of an Icelandic volcano in 2010 caused a major disruption to European air freight, grounding thousands of flights and delaying time-sensitive shipments.",
                                "targetVocab": "disruption"
                            },
                            {
                                "prompt": "Dùng từ 'resilience' để viết một câu về khả năng phục hồi của chuỗi cung ứng sau khủng hoảng. Ví dụ: Toyota's supply chain resilience was tested during the 2011 earthquake in Japan, but the company recovered faster than competitors thanks to its network of backup suppliers.",
                                "targetVocab": "resilience"
                            },
                            {
                                "prompt": "Dùng từ 'diversification' để viết một câu về chiến lược đa dạng hóa nguồn cung. Ví dụ: Apple's diversification of its manufacturing base to include factories in India and Vietnam has reduced its dependence on any single country for production.",
                                "targetVocab": "diversification"
                            },
                            {
                                "prompt": "Dùng từ 'nearshoring' để viết một câu về xu hướng chuyển sản xuất về gần thị trường tiêu thụ. Ví dụ: The nearshoring of textile production from Bangladesh to Turkey has allowed European fashion brands to respond more quickly to changing consumer trends.",
                                "targetVocab": "nearshoring"
                            },
                            {
                                "prompt": "Dùng từ 'traceability' để viết một câu về khả năng truy xuất nguồn gốc sản phẩm trong chuỗi cung ứng. Ví dụ: Blockchain technology is being used to improve traceability in the diamond industry, allowing buyers to verify that stones were ethically sourced.",
                                "targetVocab": "traceability"
                            },
                            {
                                "prompt": "Dùng từ 'optimization' để viết một câu về tối ưu hóa chuỗi cung ứng bằng công nghệ. Ví dụ: Through optimization of its warehouse layout and picking algorithms, the e-commerce company reduced order processing time from eight hours to under two.",
                                "targetVocab": "optimization"
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
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Cùng ôn lại trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Chuỗi cung ứng toàn cầu. Hãy cùng nhìn lại hành trình của bạn.\n\nTrong phần 1, bạn đã học những khái niệm nền tảng nhất: logistics — hậu cần, supply — nguồn cung, chain — chuỗi, procurement — mua sắm, inventory — hàng tồn kho, và warehouse — nhà kho. Đây là bộ khung cơ bản để hiểu cách chuỗi cung ứng vận hành.\n\nTrong phần 2, bạn đã đi sâu hơn với: freight — hàng hóa vận chuyển, customs — hải quan, clearance — thông quan, shipment — lô hàng, container — thùng chứa hàng, và transit — quá cảnh. Những từ này giúp bạn hiểu cách hàng hóa di chuyển qua biên giới quốc gia.\n\nTrong phần 3, bạn đã khám phá: disruption — sự gián đoạn, resilience — khả năng phục hồi, diversification — đa dạng hóa, nearshoring — chuyển sản xuất về gần, traceability — truy xuất nguồn gốc, và optimization — tối ưu hóa. Đây là những từ về quản trị rủi ro và tương lai của chuỗi cung ứng.\n\nBây giờ, phần ôn tập này sẽ giúp bạn củng cố toàn bộ 18 từ vựng. Bạn sẽ xem lại flashcard, luyện phát âm, và viết câu với tất cả các từ. Sau phần ôn tập, bạn sẽ sẵn sàng cho bài đọc tổng hợp — một bài viết dài hơn sử dụng cả 18 từ trong một ngữ cảnh liền mạch. Hãy bắt đầu nào!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng chuỗi cung ứng",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"],
                        "items": [
                            {
                                "prompt": "Dùng từ 'logistics' để viết một câu về tầm quan trọng của hậu cần trong thương mại điện tử. Ví dụ: The success of e-commerce giants like Shopee and Lazada depends heavily on logistics networks that can deliver millions of packages across Southeast Asia within days.",
                                "targetVocab": "logistics"
                            },
                            {
                                "prompt": "Dùng từ 'supply' để viết một câu về tác động khi nguồn cung bị thiếu hụt trên thị trường toàn cầu. Ví dụ: The global supply of natural gas tightened dramatically after the conflict in Eastern Europe, pushing energy prices to record highs across the continent.",
                                "targetVocab": "supply"
                            },
                            {
                                "prompt": "Dùng từ 'chain' để viết một câu về sự phức tạp của chuỗi cung ứng trong ngành công nghệ. Ví dụ: The supply chain for a single laptop involves over two hundred suppliers across more than thirty countries, each contributing a different component.",
                                "targetVocab": "chain"
                            },
                            {
                                "prompt": "Dùng từ 'procurement' để viết một câu về chiến lược mua sắm bền vững của doanh nghiệp. Ví dụ: IKEA's sustainable procurement policy requires all wood suppliers to prove that their timber comes from responsibly managed forests.",
                                "targetVocab": "procurement"
                            },
                            {
                                "prompt": "Dùng từ 'inventory' để viết một câu về quản lý hàng tồn kho trong mùa cao điểm. Ví dụ: Retailers typically build up inventory months before the holiday season to ensure they have enough stock to meet the surge in consumer demand.",
                                "targetVocab": "inventory"
                            },
                            {
                                "prompt": "Dùng từ 'warehouse' để viết một câu về công nghệ tự động hóa trong nhà kho hiện đại. Ví dụ: Amazon's robotic warehouse systems can locate, pick, and pack an order in under ten minutes, a task that once took human workers over an hour.",
                                "targetVocab": "warehouse"
                            },
                            {
                                "prompt": "Dùng từ 'freight' để viết một câu về chi phí vận tải hàng hóa và tác động đến giá sản phẩm. Ví dụ: Rising freight costs during the shipping crisis added hundreds of dollars to the price of importing a single container of goods from Asia to Europe.",
                                "targetVocab": "freight"
                            },
                            {
                                "prompt": "Dùng từ 'customs' để viết một câu về cải cách thủ tục hải quan để thúc đẩy thương mại. Ví dụ: Vietnam's customs modernization program has introduced electronic filing and risk-based inspections, cutting the average clearance time for imports by more than half.",
                                "targetVocab": "customs"
                            },
                            {
                                "prompt": "Dùng từ 'clearance' để viết một câu về tầm quan trọng của thông quan nhanh chóng đối với hàng hóa dễ hỏng. Ví dụ: Fast customs clearance is critical for fresh fruit exports because even a one-day delay can reduce the shelf life and market value of the produce.",
                                "targetVocab": "clearance"
                            },
                            {
                                "prompt": "Dùng từ 'shipment' để viết một câu về quy mô vận chuyển hàng hóa toàn cầu. Ví dụ: Over eleven billion tons of goods are moved by shipment across the world's oceans each year, connecting producers and consumers on every continent.",
                                "targetVocab": "shipment"
                            },
                            {
                                "prompt": "Dùng từ 'container' để viết một câu về cuộc cách mạng container hóa trong vận tải biển. Ví dụ: The standardized container transformed global trade by allowing goods to be loaded once at the factory and transported seamlessly across trucks, trains, and ships.",
                                "targetVocab": "container"
                            },
                            {
                                "prompt": "Dùng từ 'transit' để viết một câu về thời gian vận chuyển và tác động đến chuỗi cung ứng. Ví dụ: Reducing transit time from three weeks to ten days gave the company a significant advantage over competitors who relied on slower shipping routes.",
                                "targetVocab": "transit"
                            },
                            {
                                "prompt": "Dùng từ 'disruption' để viết một câu về bài học từ đại dịch COVID-19 đối với chuỗi cung ứng. Ví dụ: The pandemic-era disruption taught companies that relying on a single source for critical components is a risk they can no longer afford to take.",
                                "targetVocab": "disruption"
                            },
                            {
                                "prompt": "Dùng từ 'resilience' để viết một câu về cách doanh nghiệp xây dựng chuỗi cung ứng có khả năng phục hồi. Ví dụ: Building supply chain resilience requires investing in backup suppliers, safety stock, and flexible transportation options even when times are good.",
                                "targetVocab": "resilience"
                            },
                            {
                                "prompt": "Dùng từ 'diversification' để viết một câu về lợi ích của đa dạng hóa nguồn cung cho Việt Nam. Ví dụ: Vietnam has become a major beneficiary of supply chain diversification as global companies shift production away from China to reduce concentration risk.",
                                "targetVocab": "diversification"
                            },
                            {
                                "prompt": "Dùng từ 'nearshoring' để viết một câu về xu hướng nearshoring và tác động đến các nước đang phát triển. Ví dụ: The nearshoring trend has created new manufacturing jobs in Mexico and Eastern Europe as companies prioritize proximity over the lowest possible labor costs.",
                                "targetVocab": "nearshoring"
                            },
                            {
                                "prompt": "Dùng từ 'traceability' để viết một câu về yêu cầu truy xuất nguồn gốc trong ngành thực phẩm. Ví dụ: The European Union's new food safety regulations require full traceability from farm to fork, meaning every ingredient must be traceable to its origin.",
                                "targetVocab": "traceability"
                            },
                            {
                                "prompt": "Dùng từ 'optimization' để viết một câu về vai trò của trí tuệ nhân tạo trong tối ưu hóa chuỗi cung ứng. Ví dụ: AI-driven optimization of delivery routes has helped logistics companies reduce fuel consumption and carbon emissions while maintaining on-time delivery rates.",
                                "targetVocab": "optimization"
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về chuỗi cung ứng toàn cầu.",
                    "data": {
                        "text": "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, kể câu chuyện hoàn chỉnh về chuỗi cung ứng toàn cầu — từ nền tảng hậu cần đến tương lai của quản trị rủi ro.\n\nBạn sẽ gặp lại logistics, supply, chain, procurement, inventory, warehouse trong phần mở đầu về cách chuỗi cung ứng vận hành. Tiếp theo, freight, customs, clearance, shipment, container, transit sẽ giúp bạn hiểu hành trình vật lý của hàng hóa qua biên giới. Và cuối cùng, disruption, resilience, diversification, nearshoring, traceability, optimization sẽ đưa bạn vào thế giới quản trị chuỗi cung ứng hiện đại.\n\nHãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, và thử đoán nghĩa trước khi nhìn lại định nghĩa. Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh để tổng hợp những gì đã học. Bắt đầu thôi!"
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chuỗi cung ứng toàn cầu — Bức tranh toàn cảnh",
                    "description": "The modern global economy runs on supply chains.",
                    "data": {
                        "text": "The modern global economy runs on supply chains. Every product on every shelf in every store arrived there through a complex network of suppliers, manufacturers, shippers, and retailers. Understanding how this network operates — and what happens when it breaks — is one of the most important skills for anyone studying international trade.\n\nA supply chain begins with procurement — the process of sourcing raw materials and components from suppliers around the world. A smartphone manufacturer, for example, must procure rare earth minerals from Africa, glass from Japan, and semiconductors from Taiwan. Each procurement decision involves trade-offs between cost, quality, speed, and reliability. The procurement team must evaluate dozens of potential suppliers and negotiate contracts that balance all of these factors.\n\nOnce materials are procured, they enter the logistics system — the vast network of transportation, storage, and distribution that moves goods from one stage of production to the next. Logistics is the backbone of the supply chain. Without it, raw materials would never reach factories, and finished products would never reach customers.\n\nAt every stage, goods must be stored in warehouses. A warehouse is not just a building where things sit on shelves. Modern warehouses are high-tech operations that use robotics, barcode scanning, and artificial intelligence to track inventory in real time. Inventory management is a constant balancing act. Companies must hold enough stock to meet demand without tying up too much capital in unsold goods.\n\nWhen goods are ready to move across borders, they enter the world of international freight. Most global trade travels by sea, packed into standardized shipping containers that can be transferred seamlessly between ships, trains, and trucks. A single container ship can carry thousands of containers, each holding a different shipment destined for a different country.\n\nDuring transit — the period when goods are moving between origin and destination — shipments face numerous risks. Weather delays, port congestion, mechanical failures, and even piracy can slow or damage cargo. Companies use tracking technology and cargo insurance to manage these risks, but transit remains one of the most unpredictable stages of the supply chain.\n\nAt the destination, every shipment must pass through customs — the government authority that controls what enters and leaves a country. Customs officers verify documentation, assess duties and taxes, and inspect cargo for prohibited items. The process of getting goods through customs is called clearance. Efficient clearance can take hours; inefficient clearance can take weeks. Companies that master the clearance process gain a significant competitive advantage.\n\nFor decades, the dominant philosophy in supply chain management was optimization — making every link in the chain as lean and cost-efficient as possible. Companies minimized inventory, consolidated suppliers, and chose the cheapest shipping routes. This approach worked brilliantly in stable times. But it created supply chains that were brittle — optimized for efficiency but vulnerable to disruption.\n\nThe COVID-19 pandemic was the ultimate stress test. Factories shut down across Asia. Ports became gridlocked. Containers piled up in the wrong locations. The disruption rippled through every industry, from automobiles to pharmaceuticals to consumer electronics. Suddenly, the world realized that a supply chain optimized only for cost is a supply chain waiting to fail.\n\nThe response has been a fundamental shift toward resilience. Companies are now building supply chains that can absorb shocks and recover quickly. This means holding more inventory as a safety buffer, maintaining relationships with multiple suppliers, and investing in flexible transportation networks.\n\nDiversification is a key strategy for resilience. Instead of relying on a single country for critical components, companies are spreading their procurement across multiple regions. Vietnam has been one of the biggest beneficiaries of this trend, attracting manufacturers who want to reduce their dependence on any single production hub.\n\nNearshoring is another growing trend. Companies are moving production closer to their end markets to reduce transit times and avoid the risks associated with long-distance shipping. American firms are shifting manufacturing to Mexico. European firms are moving production to Turkey and Poland. The goal is not to abandon global trade but to make supply chains shorter and more responsive.\n\nTraceability has also become a priority. Consumers and regulators increasingly demand to know where products come from and how they were made. Traceability systems allow companies to track a product backward through every stage of the supply chain — from the retail shelf to the raw material source. This is essential for food safety, ethical sourcing, and environmental compliance.\n\nThe future of supply chain management lies in combining optimization with resilience. Modern technology — artificial intelligence, blockchain, predictive analytics — makes it possible to build supply chains that are both efficient and robust. The companies that master this balance will thrive in a world where disruption is not the exception but the norm.\n\nFrom procurement to warehouse, from freight to customs clearance, from container to final delivery — the supply chain is the invisible infrastructure that makes global trade possible. And the language of that infrastructure is English."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chuỗi cung ứng toàn cầu — Bức tranh toàn cảnh",
                    "description": "The modern global economy runs on supply chains.",
                    "data": {
                        "text": "The modern global economy runs on supply chains. Every product on every shelf in every store arrived there through a complex network of suppliers, manufacturers, shippers, and retailers. Understanding how this network operates — and what happens when it breaks — is one of the most important skills for anyone studying international trade.\n\nA supply chain begins with procurement — the process of sourcing raw materials and components from suppliers around the world. A smartphone manufacturer, for example, must procure rare earth minerals from Africa, glass from Japan, and semiconductors from Taiwan. Each procurement decision involves trade-offs between cost, quality, speed, and reliability. The procurement team must evaluate dozens of potential suppliers and negotiate contracts that balance all of these factors.\n\nOnce materials are procured, they enter the logistics system — the vast network of transportation, storage, and distribution that moves goods from one stage of production to the next. Logistics is the backbone of the supply chain. Without it, raw materials would never reach factories, and finished products would never reach customers.\n\nAt every stage, goods must be stored in warehouses. A warehouse is not just a building where things sit on shelves. Modern warehouses are high-tech operations that use robotics, barcode scanning, and artificial intelligence to track inventory in real time. Inventory management is a constant balancing act. Companies must hold enough stock to meet demand without tying up too much capital in unsold goods.\n\nWhen goods are ready to move across borders, they enter the world of international freight. Most global trade travels by sea, packed into standardized shipping containers that can be transferred seamlessly between ships, trains, and trucks. A single container ship can carry thousands of containers, each holding a different shipment destined for a different country.\n\nDuring transit — the period when goods are moving between origin and destination — shipments face numerous risks. Weather delays, port congestion, mechanical failures, and even piracy can slow or damage cargo. Companies use tracking technology and cargo insurance to manage these risks, but transit remains one of the most unpredictable stages of the supply chain.\n\nAt the destination, every shipment must pass through customs — the government authority that controls what enters and leaves a country. Customs officers verify documentation, assess duties and taxes, and inspect cargo for prohibited items. The process of getting goods through customs is called clearance. Efficient clearance can take hours; inefficient clearance can take weeks. Companies that master the clearance process gain a significant competitive advantage.\n\nFor decades, the dominant philosophy in supply chain management was optimization — making every link in the chain as lean and cost-efficient as possible. Companies minimized inventory, consolidated suppliers, and chose the cheapest shipping routes. This approach worked brilliantly in stable times. But it created supply chains that were brittle — optimized for efficiency but vulnerable to disruption.\n\nThe COVID-19 pandemic was the ultimate stress test. Factories shut down across Asia. Ports became gridlocked. Containers piled up in the wrong locations. The disruption rippled through every industry, from automobiles to pharmaceuticals to consumer electronics. Suddenly, the world realized that a supply chain optimized only for cost is a supply chain waiting to fail.\n\nThe response has been a fundamental shift toward resilience. Companies are now building supply chains that can absorb shocks and recover quickly. This means holding more inventory as a safety buffer, maintaining relationships with multiple suppliers, and investing in flexible transportation networks.\n\nDiversification is a key strategy for resilience. Instead of relying on a single country for critical components, companies are spreading their procurement across multiple regions. Vietnam has been one of the biggest beneficiaries of this trend, attracting manufacturers who want to reduce their dependence on any single production hub.\n\nNearshoring is another growing trend. Companies are moving production closer to their end markets to reduce transit times and avoid the risks associated with long-distance shipping. American firms are shifting manufacturing to Mexico. European firms are moving production to Turkey and Poland. The goal is not to abandon global trade but to make supply chains shorter and more responsive.\n\nTraceability has also become a priority. Consumers and regulators increasingly demand to know where products come from and how they were made. Traceability systems allow companies to track a product backward through every stage of the supply chain — from the retail shelf to the raw material source. This is essential for food safety, ethical sourcing, and environmental compliance.\n\nThe future of supply chain management lies in combining optimization with resilience. Modern technology — artificial intelligence, blockchain, predictive analytics — makes it possible to build supply chains that are both efficient and robust. The companies that master this balance will thrive in a world where disruption is not the exception but the norm.\n\nFrom procurement to warehouse, from freight to customs clearance, from container to final delivery — the supply chain is the invisible infrastructure that makes global trade possible. And the language of that infrastructure is English."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chuỗi cung ứng toàn cầu — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": "The modern global economy runs on supply chains. Every product on every shelf in every store arrived there through a complex network of suppliers, manufacturers, shippers, and retailers. Understanding how this network operates — and what happens when it breaks — is one of the most important skills for anyone studying international trade.\n\nA supply chain begins with procurement — the process of sourcing raw materials and components from suppliers around the world. A smartphone manufacturer, for example, must procure rare earth minerals from Africa, glass from Japan, and semiconductors from Taiwan. Each procurement decision involves trade-offs between cost, quality, speed, and reliability. The procurement team must evaluate dozens of potential suppliers and negotiate contracts that balance all of these factors.\n\nOnce materials are procured, they enter the logistics system — the vast network of transportation, storage, and distribution that moves goods from one stage of production to the next. Logistics is the backbone of the supply chain. Without it, raw materials would never reach factories, and finished products would never reach customers.\n\nAt every stage, goods must be stored in warehouses. A warehouse is not just a building where things sit on shelves. Modern warehouses are high-tech operations that use robotics, barcode scanning, and artificial intelligence to track inventory in real time. Inventory management is a constant balancing act. Companies must hold enough stock to meet demand without tying up too much capital in unsold goods.\n\nWhen goods are ready to move across borders, they enter the world of international freight. Most global trade travels by sea, packed into standardized shipping containers that can be transferred seamlessly between ships, trains, and trucks. A single container ship can carry thousands of containers, each holding a different shipment destined for a different country.\n\nDuring transit — the period when goods are moving between origin and destination — shipments face numerous risks. Weather delays, port congestion, mechanical failures, and even piracy can slow or damage cargo. Companies use tracking technology and cargo insurance to manage these risks, but transit remains one of the most unpredictable stages of the supply chain.\n\nAt the destination, every shipment must pass through customs — the government authority that controls what enters and leaves a country. Customs officers verify documentation, assess duties and taxes, and inspect cargo for prohibited items. The process of getting goods through customs is called clearance. Efficient clearance can take hours; inefficient clearance can take weeks. Companies that master the clearance process gain a significant competitive advantage.\n\nFor decades, the dominant philosophy in supply chain management was optimization — making every link in the chain as lean and cost-efficient as possible. Companies minimized inventory, consolidated suppliers, and chose the cheapest shipping routes. This approach worked brilliantly in stable times. But it created supply chains that were brittle — optimized for efficiency but vulnerable to disruption.\n\nThe COVID-19 pandemic was the ultimate stress test. Factories shut down across Asia. Ports became gridlocked. Containers piled up in the wrong locations. The disruption rippled through every industry, from automobiles to pharmaceuticals to consumer electronics. Suddenly, the world realized that a supply chain optimized only for cost is a supply chain waiting to fail.\n\nThe response has been a fundamental shift toward resilience. Companies are now building supply chains that can absorb shocks and recover quickly. This means holding more inventory as a safety buffer, maintaining relationships with multiple suppliers, and investing in flexible transportation networks.\n\nDiversification is a key strategy for resilience. Instead of relying on a single country for critical components, companies are spreading their procurement across multiple regions. Vietnam has been one of the biggest beneficiaries of this trend, attracting manufacturers who want to reduce their dependence on any single production hub.\n\nNearshoring is another growing trend. Companies are moving production closer to their end markets to reduce transit times and avoid the risks associated with long-distance shipping. American firms are shifting manufacturing to Mexico. European firms are moving production to Turkey and Poland. The goal is not to abandon global trade but to make supply chains shorter and more responsive.\n\nTraceability has also become a priority. Consumers and regulators increasingly demand to know where products come from and how they were made. Traceability systems allow companies to track a product backward through every stage of the supply chain — from the retail shelf to the raw material source. This is essential for food safety, ethical sourcing, and environmental compliance.\n\nThe future of supply chain management lies in combining optimization with resilience. Modern technology — artificial intelligence, blockchain, predictive analytics — makes it possible to build supply chains that are both efficient and robust. The companies that master this balance will thrive in a world where disruption is not the exception but the norm.\n\nFrom procurement to warehouse, from freight to customs clearance, from container to final delivery — the supply chain is the invisible infrastructure that makes global trade possible. And the language of that infrastructure is English."
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chuỗi cung ứng toàn cầu",
                    "description": "Viết đoạn văn tiếng Anh phân tích về chuỗi cung ứng toàn cầu sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ["logistics", "supply", "chain", "procurement", "inventory", "warehouse", "freight", "customs", "clearance", "shipment", "container", "transit", "disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"],
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một tình huống thực tế liên quan đến chuỗi cung ứng toàn cầu. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích tác động của đại dịch COVID-19 đến chuỗi cung ứng toàn cầu. Giải thích disruption đã xảy ra như thế nào, vì sao optimization thuần túy không đủ, và các doanh nghiệp đã xây dựng resilience bằng cách nào — qua diversification, nearshoring, hay cải thiện logistics và inventory management.",
                            "Hãy phân tích vai trò của Việt Nam trong chuỗi cung ứng toàn cầu hiện đại. Giải thích vì sao Việt Nam hưởng lợi từ xu hướng diversification, logistics và warehouse infrastructure đã phát triển ra sao, và customs clearance cần cải thiện gì để Việt Nam trở thành mắt xích quan trọng hơn trong supply chain toàn cầu."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần trách nhiệm ấm áp.",
                    "data": {
                        "text": "Xong rồi! Bạn vừa hoàn thành bài học cuối cùng trong chuỗi Thương mại quốc tế — và đó không phải là một bài học dễ. Chuỗi cung ứng toàn cầu là một trong những chủ đề phức tạp nhất trong kinh tế học, và bạn đã chinh phục nó. Hãy tự hào về điều đó.\n\nNhưng tự hào thôi chưa đủ — bây giờ là lúc biến kiến thức thành hành động. Hãy cùng ôn lại một số từ quan trọng nhất, lần này với góc nhìn thực tế hơn.\n\nSupply chain — chuỗi cung ứng. Đây không chỉ là khái niệm trong sách giáo khoa — đây là hệ thống thực sự đang vận hành mỗi ngày, đưa thức ăn đến bàn ăn của bạn và điện thoại đến tay bạn. Ví dụ mới: The resilience of Vietnam's supply chain was tested during the pandemic, and the country emerged as a more attractive manufacturing destination precisely because it adapted quickly.\n\nLogistics — hậu cần. Mỗi khi bạn đặt hàng online và nhận được gói hàng sau 2 ngày, đó là logistics đang hoạt động. Ví dụ mới: Vietnam's investment in port infrastructure and logistics technology has positioned it as a key transit hub for goods moving between China and Southeast Asian markets.\n\nDisruption — sự gián đoạn. Từ này sẽ theo bạn suốt sự nghiệp, vì disruption không phải là ngoại lệ — nó là bình thường mới. Ví dụ mới: Companies that treat disruption as an inevitable part of business rather than a rare crisis are the ones that survive and grow in the long run.\n\nResilience — khả năng phục hồi. Đây là từ mà mọi CEO trên thế giới đang nói đến. Không phải vì nó thời thượng, mà vì nó là điều kiện sống còn. Ví dụ mới: True supply chain resilience means having the flexibility to reroute shipments, switch suppliers, and adjust inventory levels within days, not months.\n\nNearshoring — chuyển sản xuất về gần. Xu hướng này đang thay đổi bản đồ sản xuất toàn cầu, và Việt Nam đang ở vị trí tuyệt vời để hưởng lợi. Ví dụ mới: As nearshoring reshapes global manufacturing, Vietnam's geographic proximity to major Asian markets gives it a natural advantage over more distant competitors.\n\nTraceability — truy xuất nguồn gốc. Người tiêu dùng ngày càng muốn biết sản phẩm đến từ đâu, và doanh nghiệp nào không đáp ứng được yêu cầu này sẽ mất khách hàng. Ví dụ mới: Vietnamese coffee exporters who invest in traceability systems can command premium prices in European markets where consumers value transparency.\n\nBạn biết không, 18 từ vựng này không chỉ giúp bạn thi tốt hơn. Chúng là ngôn ngữ của ngành logistics và supply chain management — một trong những ngành phát triển nhanh nhất tại Việt Nam. Khi bạn đọc được báo cáo của DHL hay Maersk bằng tiếng Anh, khi bạn hiểu được freight rates và customs clearance procedures, bạn đang có lợi thế mà nhiều người cùng trang lứa chưa có.\n\nVà đây là điều tôi muốn bạn làm sau bài học này: tuần tới, hãy tìm một bài báo tiếng Anh về supply chain — trên Reuters, Bloomberg, hoặc Supply Chain Dive — và đọc nó. Không cần hiểu hết. Chỉ cần nhận ra những từ bạn đã học và thấy chúng sống trong ngữ cảnh thực. Đó là cách bạn biến 18 từ vựng thành vốn liếng thật sự.\n\nBạn đã hoàn thành toàn bộ 5 bài học trong chuỗi Thương mại quốc tế — từ Trade Theory đến Supply Chains. Đó là 90 từ vựng chuyên ngành, 15 bài đọc tiếng Anh, và hàng chục bài viết luyện tập. Không phải ai cũng đi được đến đây. Bạn đã làm được, và tôi tin bạn sẽ tiếp tục.\n\nChúc bạn học vui và luôn tiến về phía trước!"
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
