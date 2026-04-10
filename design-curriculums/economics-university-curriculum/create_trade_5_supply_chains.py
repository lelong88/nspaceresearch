"""
Create curriculum: Supply Chains – Chuỗi Cung Ứng Toàn Cầu
Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa (International Trade), curriculum #5
18 words | 5 sessions | metaphor_led tone | warm accountability farewell
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/economics-university-curriculum")
from validate_curriculum import validate_all

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Word groups ──────────────────────────────────────────────
W1 = ["logistics", "supply", "chain", "procurement", "inventory", "warehouse"]
W2 = ["freight", "customs", "clearance", "shipment", "container", "transit"]
W3 = ["disruption", "resilience", "diversification", "nearshoring", "traceability", "optimization"]
ALL_WORDS = W1 + W2 + W3

# ── Session 1 reading text ───────────────────────────────────
SESSION_1_READING = (
    "Every product you use has a story — a journey that begins long before it reaches your hands. "
    "That journey is called a supply chain, and understanding how it works is essential "
    "for anyone studying international trade.\n\n"
    "A supply chain is the entire chain of steps involved in creating and delivering a product. "
    "It starts with raw materials and ends with the finished good in a customer's hands. "
    "In between, there are factories, transportation networks, and storage facilities "
    "that all need to work together smoothly. "
    "A modern supply chain for a single smartphone, for example, "
    "can involve components from over thirty countries.\n\n"
    "The field that manages this movement of goods is called logistics. "
    "Logistics covers everything from planning the most efficient shipping routes "
    "to tracking packages in real time. "
    "A company with strong logistics can deliver products faster and cheaper than its competitors. "
    "In Vietnam, the logistics industry has grown rapidly as the country has become "
    "a major manufacturing hub for electronics, textiles, and footwear.\n\n"
    "Before any product can be made, a company must acquire the necessary materials. "
    "This process is called procurement. "
    "Procurement involves finding suppliers, negotiating prices, and signing contracts. "
    "A procurement manager at a Vietnamese garment factory, for instance, "
    "might source cotton from India, buttons from China, and zippers from Japan. "
    "Good procurement means getting the right materials at the right price and the right time.\n\n"
    "Once materials arrive, they become part of the company's inventory. "
    "Inventory is the stock of goods a business holds — "
    "raw materials waiting to be used, products being assembled, "
    "and finished goods ready to be shipped. "
    "Managing inventory is a delicate balance. "
    "Too much inventory wastes money on storage and risks products becoming outdated. "
    "Too little inventory means the company cannot fill orders when customers want to buy.\n\n"
    "Goods that are not immediately needed are stored in a warehouse. "
    "A warehouse is a large building designed for storing products safely and efficiently. "
    "Modern warehouses use robots, barcode scanners, and computer systems "
    "to track every item and fill orders quickly. "
    "Vietnam's industrial zones now include massive warehouse complexes "
    "built by international logistics companies to support the country's growing export sector.\n\n"
    "Together, logistics, supply, chain, procurement, inventory, and warehouse "
    "form the vocabulary of how goods move through the global economy. "
    "Understanding these words is the first step toward understanding "
    "why a disruption on the other side of the world can affect the price of goods in your local store."
)


# ── Session 2 reading text ───────────────────────────────────
SESSION_2_READING = (
    "Once a product is manufactured, it must travel — sometimes thousands of kilometers — "
    "to reach its destination. This physical movement of goods across borders "
    "is one of the most complex parts of international trade, "
    "and it relies on a specialized vocabulary that every economics student should know.\n\n"
    "The transportation of goods in large quantities is called freight. "
    "Freight can move by sea, air, rail, or road. "
    "Ocean freight is the cheapest option for heavy or bulky goods — "
    "about ninety percent of the world's traded goods travel by ship at some point. "
    "Air freight is much faster but far more expensive, "
    "so it is typically reserved for high-value or time-sensitive products "
    "like electronics, pharmaceuticals, and fresh seafood.\n\n"
    "When freight crosses an international border, it must pass through customs. "
    "Customs is the government authority responsible for controlling what enters and leaves a country. "
    "Customs officers inspect goods, collect tariffs and taxes, "
    "and enforce regulations on prohibited or restricted items. "
    "For Vietnamese exporters, dealing with customs in destination countries "
    "is a daily reality that can make or break delivery schedules.\n\n"
    "The process of getting goods approved by customs is called clearance. "
    "Customs clearance involves submitting documents that describe the goods — "
    "what they are, where they came from, how much they are worth, "
    "and whether they meet the importing country's standards. "
    "Delays in clearance are one of the most common causes of supply chain slowdowns. "
    "A missing document or an incorrect classification can hold goods at the border for days.\n\n"
    "Each batch of goods sent from one place to another is called a shipment. "
    "A shipment might be a single pallet of coffee beans or ten thousand boxes of shoes. "
    "Tracking shipments in real time has become essential for modern supply chain management. "
    "Companies use GPS, satellite systems, and digital platforms "
    "to know exactly where every shipment is at any moment.\n\n"
    "Most ocean freight travels in standardized metal boxes called containers. "
    "The shipping container is one of the most important inventions in trade history. "
    "Before containers, loading and unloading a ship took weeks. "
    "With containers, the same process takes hours. "
    "A single large container ship can carry over twenty thousand containers, "
    "each one packed with goods from different companies and countries.\n\n"
    "The time goods spend moving between locations is called transit. "
    "Transit time varies enormously depending on the route and mode of transport. "
    "A container shipped from Ho Chi Minh City to Rotterdam takes about twenty-five days by sea. "
    "The same goods could arrive in two days by air — but at ten times the cost. "
    "Reducing transit time without increasing costs is one of the central challenges of logistics."
)


# ── Session 3 reading text ───────────────────────────────────
SESSION_3_READING = (
    "In recent years, the world has learned a painful lesson: "
    "global supply chains are powerful but fragile. "
    "The COVID-19 pandemic, the blockage of the Suez Canal, "
    "and geopolitical tensions between major trading nations "
    "have all exposed how vulnerable modern supply chains can be. "
    "This final set of vocabulary covers the concepts that businesses and governments "
    "are now using to build stronger, smarter supply chains.\n\n"
    "A disruption is any event that interrupts the normal flow of goods through a supply chain. "
    "Disruptions can be natural — earthquakes, floods, pandemics — "
    "or man-made — trade wars, factory fires, cyberattacks. "
    "The 2021 blockage of the Suez Canal by a single container ship "
    "caused a disruption that affected global trade for weeks, "
    "delaying billions of dollars worth of goods.\n\n"
    "The ability of a supply chain to recover quickly from a disruption is called resilience. "
    "A resilient supply chain does not just survive shocks — it adapts and comes back stronger. "
    "Building resilience means having backup suppliers, keeping safety stock, "
    "and designing systems that can reroute goods when problems occur. "
    "After the pandemic, resilience became the most important word "
    "in every supply chain manager's vocabulary.\n\n"
    "One key strategy for building resilience is diversification. "
    "Diversification means spreading risk by using multiple suppliers, "
    "manufacturing locations, or transportation routes instead of relying on just one. "
    "A company that sources all its components from a single country "
    "is far more vulnerable than one that has suppliers in three or four different regions. "
    "Vietnam has benefited enormously from diversification, "
    "as companies moved production out of China to reduce their dependence on a single source.\n\n"
    "A related trend is nearshoring — moving production closer to the final market "
    "instead of manufacturing in distant low-cost countries. "
    "Nearshoring reduces transit times, lowers shipping costs, "
    "and makes supply chains less vulnerable to disruptions in faraway regions. "
    "For example, some American companies have shifted manufacturing from Asia to Mexico, "
    "while European firms have moved production to Turkey or Eastern Europe.\n\n"
    "As supply chains become more complex, traceability has become increasingly important. "
    "Traceability is the ability to track a product's journey "
    "from raw material to finished good at every step. "
    "Consumers want to know where their food comes from, "
    "whether their clothes were made ethically, "
    "and whether the minerals in their electronics were sourced responsibly. "
    "Technologies like blockchain and QR codes are making traceability easier and more transparent.\n\n"
    "Finally, optimization is the process of making a supply chain as efficient as possible. "
    "Optimization involves using data, algorithms, and technology "
    "to reduce costs, speed up delivery, and minimize waste. "
    "A well-optimized supply chain delivers the right product to the right place "
    "at the right time and at the lowest possible cost. "
    "For Vietnam's export-driven economy, supply chain optimization "
    "is not just a business strategy — it is a national priority."
)


# ── Session 5 full reading text ──────────────────────────────
SESSION_5_READING = (
    "The global supply chain is one of the greatest achievements of modern commerce — "
    "and one of its greatest vulnerabilities. "
    "Every day, millions of containers cross oceans, trucks roll across borders, "
    "and planes carry freight to every corner of the world. "
    "This vast network of logistics connects factories in Vietnam to consumers in Europe, "
    "farmers in Brazil to supermarkets in Japan, "
    "and technology companies in California to assembly plants in Shenzhen.\n\n"
    "At its core, a supply chain is a chain of interconnected steps. "
    "It begins with procurement — the process of finding and purchasing raw materials. "
    "A furniture manufacturer in Binh Duong province, for example, "
    "might procure timber from Laos, hardware from China, and fabric from Thailand. "
    "The procurement team must balance quality, cost, and reliability "
    "when choosing among dozens of potential suppliers.\n\n"
    "Once materials are procured, they enter the company's inventory. "
    "Managing inventory is both an art and a science. "
    "Too much inventory means money is tied up in goods sitting in a warehouse. "
    "Too little means production stops when a key component runs out. "
    "Modern companies use sophisticated software to predict demand "
    "and keep inventory at just the right level.\n\n"
    "The warehouse itself has evolved dramatically. "
    "Today's warehouses are not just storage buildings — "
    "they are high-tech distribution centers where robots sort packages, "
    "sensors monitor temperature and humidity, "
    "and algorithms decide the fastest way to fill each order. "
    "Vietnam's logistics infrastructure is expanding rapidly, "
    "with new warehouse complexes being built near major ports and airports.\n\n"
    "When goods are ready to ship, they enter the freight network. "
    "A shipment of Vietnamese coffee destined for Germany "
    "might travel by truck from the Central Highlands to Ho Chi Minh City, "
    "then by container ship through the South China Sea, the Indian Ocean, "
    "and the Suez Canal to the port of Hamburg. "
    "The entire transit takes about four weeks.\n\n"
    "At every border crossing, the shipment must pass through customs. "
    "Customs clearance requires accurate documentation — "
    "invoices, certificates of origin, phytosanitary certificates for agricultural products, "
    "and compliance declarations for regulated goods. "
    "A single error in paperwork can delay clearance by days, "
    "costing the exporter money and damaging relationships with buyers.\n\n"
    "The standardized shipping container revolutionized global trade. "
    "Before containerization, loading a ship was slow, expensive, and prone to theft. "
    "The container made it possible to move goods seamlessly "
    "from truck to train to ship without unpacking. "
    "Today, the world's largest container ships carry over twenty thousand containers each, "
    "and the supply of container capacity is itself a major factor in global shipping costs.\n\n"
    "But this intricate system is vulnerable to disruption. "
    "The COVID-19 pandemic showed how quickly a disruption can cascade through the entire chain. "
    "Factory closures in one country led to component shortages in another, "
    "which led to empty shelves in a third. "
    "Port congestion, labor shortages, and container imbalances "
    "created bottlenecks that took over a year to clear.\n\n"
    "In response, companies and governments have embraced resilience as a guiding principle. "
    "Building resilience means accepting that disruptions will happen "
    "and designing systems that can absorb shocks and recover quickly. "
    "This includes maintaining safety stock, developing alternative shipping routes, "
    "and investing in digital tools that provide real-time visibility across the supply chain.\n\n"
    "Diversification is one of the most powerful tools for resilience. "
    "Instead of relying on a single supplier or a single country, "
    "companies are spreading their sourcing across multiple regions. "
    "Vietnam has been one of the biggest beneficiaries of this trend, "
    "attracting factories from companies that previously manufactured only in China.\n\n"
    "Nearshoring is another strategy gaining momentum. "
    "By moving production closer to end markets, "
    "companies can reduce transit times and respond more quickly to changes in demand. "
    "Nearshoring does not eliminate the need for global supply chains, "
    "but it adds a layer of flexibility that pure offshoring cannot provide.\n\n"
    "As consumers and regulators demand more transparency, "
    "traceability has become a competitive advantage. "
    "Companies that can trace every component back to its source "
    "can prove that their products are ethically made, environmentally sustainable, "
    "and free from forced labor. "
    "Blockchain technology is making traceability more reliable "
    "by creating permanent, tamper-proof records of every transaction in the supply chain.\n\n"
    "Tying all of these elements together is optimization. "
    "Supply chain optimization uses data analytics, artificial intelligence, "
    "and machine learning to find the most efficient way to move goods from origin to destination. "
    "It answers questions like: Which shipping route minimizes cost and transit time? "
    "How much inventory should each warehouse hold? "
    "When should procurement contracts be renegotiated?\n\n"
    "For Vietnam, a country whose economy depends heavily on exports, "
    "mastering the vocabulary and concepts of global supply chains is not optional — it is essential. "
    "From the logistics manager at a Hai Phong port to the procurement officer at a Hanoi electronics firm, "
    "these eighteen words are the language of daily work. "
    "And for economics students, understanding supply chains "
    "means understanding how the modern global economy actually functions."
)


# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Supply Chains – Chuỗi Cung Ứng Toàn Cầu",
    "contentTypeTags": [],
    "description": (
        "CHUỖI CUNG ỨNG TOÀN CẦU NHƯ MẠCH MÁU CỦA NỀN KINH TẾ — KHI MỘT ĐOẠN TẮC NGHẼN, CẢ CƠ THỂ CHAO ĐẢO.\n\n"
        "Bạn mua một chiếc điện thoại 'Made in Vietnam' — nhưng chip từ Đài Loan, "
        "màn hình từ Hàn Quốc, pin từ Trung Quốc, và phần mềm từ Mỹ. "
        "Mỗi linh kiện đi qua hàng chục cảng, kho hàng và trạm hải quan "
        "trước khi đến tay bạn. Khi đại dịch COVID-19 làm tắc nghẽn cảng biển toàn cầu, "
        "cả thế giới mới nhận ra chuỗi cung ứng mong manh đến mức nào.\n\n"
        "Hãy hình dung chuỗi cung ứng như một dàn nhạc giao hưởng — "
        "mỗi nhạc công là một mắt xích: logistics, procurement, freight, customs. "
        "Chỉ cần một nhạc công lạc nhịp, cả bản giao hưởng thương mại toàn cầu sẽ lỗi nhịp theo. "
        "18 từ vựng trong bài học này chính là bản nhạc mà bạn cần đọc được.\n\n"
        "Sau khóa học, bạn sẽ đọc được báo cáo logistics bằng tiếng Anh mà không cần dừng lại mỗi dòng, "
        "tự tin thảo luận về supply chain disruption trong lớp, "
        "và viết bài phân tích về resilience và nearshoring bằng tiếng Anh chuyên ngành.\n\n"
        "18 từ vựng — từ logistics đến optimization — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy chuỗi cung ứng toàn cầu, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về chuỗi cung ứng toàn cầu — "
            "từ kho hàng đến cảng biển, từ hải quan đến chiến lược phục hồi. "
            "Bạn sẽ học logistics, supply, chain, procurement, inventory, warehouse trong phần đầu tiên, "
            "nơi bài đọc giải thích cách hàng hóa di chuyển từ nhà máy đến tay người tiêu dùng. "
            "Tiếp theo là freight, customs, clearance, shipment, container, transit — "
            "những từ giúp bạn hiểu hành trình vật lý của hàng hóa qua biên giới. "
            "Cuối cùng, disruption, resilience, diversification, nearshoring, traceability, optimization "
            "đưa bạn vào thế giới chiến lược chuỗi cung ứng hiện đại — "
            "nơi các doanh nghiệp học cách thích nghi sau đại dịch và xung đột thương mại. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu tài liệu về global supply chains bằng tiếng Anh — "
            "không cần tra từ điển mỗi dòng."
        )
    },
    "learningSessions": [
        # ── SESSION 1: Words 1-6 ─────────────────────────────
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Chào mừng bạn đến với bài học về chuỗi cung ứng toàn cầu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học cuối cùng trong chuỗi từ vựng Thương mại quốc tế — "
                            "chủ đề hôm nay là Chuỗi cung ứng toàn cầu, hay trong tiếng Anh là Global Supply Chains. "
                            "Mỗi sản phẩm bạn dùng hàng ngày — từ chiếc áo bạn mặc đến chiếc điện thoại trong tay — "
                            "đều là kết quả của một chuỗi cung ứng phức tạp trải dài qua nhiều quốc gia. "
                            "Nguyên liệu được khai thác ở một nơi, gia công ở nơi khác, "
                            "lắp ráp ở nơi thứ ba, rồi vận chuyển đến tay bạn qua hàng nghìn kilomet đường biển và đường bộ.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: logistics, supply, chain, procurement, inventory, và warehouse. "
                            "Đây là những từ nền tảng mà bạn sẽ gặp trong bất kỳ tài liệu nào về quản lý chuỗi cung ứng.\n\n"
                            "Từ đầu tiên là logistics — danh từ — nghĩa là hậu cần, "
                            "toàn bộ quá trình lập kế hoạch, thực hiện và kiểm soát việc vận chuyển và lưu trữ hàng hóa "
                            "từ điểm xuất phát đến điểm tiêu thụ. "
                            "Ví dụ: 'Efficient logistics can reduce delivery times from weeks to days, giving companies a significant competitive advantage.' "
                            "Trong bài đọc, logistics mô tả hệ thống phức tạp đằng sau việc đưa hàng hóa "
                            "từ nhà máy đến tay người tiêu dùng.\n\n"
                            "Từ thứ hai là supply — danh từ và động từ — nghĩa là cung cấp hoặc nguồn cung, "
                            "lượng hàng hóa hoặc dịch vụ sẵn có để đáp ứng nhu cầu. "
                            "Ví dụ: 'The global supply of semiconductor chips fell sharply during the pandemic, causing shortages in the automobile industry.' "
                            "Trong bài đọc, supply là khái niệm trung tâm — "
                            "mọi hoạt động chuỗi cung ứng đều xoay quanh việc đảm bảo nguồn cung ổn định.\n\n"
                            "Từ thứ ba là chain — danh từ — nghĩa là chuỗi, "
                            "một chuỗi các bước hoặc mắt xích liên kết với nhau trong một quy trình. "
                            "Ví dụ: 'A modern supply chain can involve dozens of companies across ten or more countries, all connected by contracts and shipping routes.' "
                            "Trong bài đọc, chain nhấn mạnh rằng mỗi mắt xích đều quan trọng — "
                            "nếu một mắt xích đứt, cả chuỗi bị ảnh hưởng.\n\n"
                            "Từ thứ tư là procurement — danh từ — nghĩa là mua sắm, thu mua, "
                            "quá trình tìm kiếm, lựa chọn và mua nguyên vật liệu hoặc dịch vụ từ nhà cung cấp. "
                            "Ví dụ: 'The company's procurement team negotiated contracts with suppliers in five different countries to get the best prices for raw materials.' "
                            "Trong bài đọc, procurement là bước đầu tiên trong chuỗi cung ứng — "
                            "trước khi sản xuất, bạn phải mua được nguyên liệu.\n\n"
                            "Từ thứ năm là inventory — danh từ — nghĩa là hàng tồn kho, "
                            "toàn bộ hàng hóa mà một doanh nghiệp đang giữ để bán hoặc sử dụng trong sản xuất. "
                            "Ví dụ: 'Keeping too much inventory ties up capital, but keeping too little risks running out of stock when demand spikes.' "
                            "Trong bài đọc, inventory là bài toán cân bằng — "
                            "doanh nghiệp phải quyết định giữ bao nhiêu hàng để vừa đủ mà không lãng phí.\n\n"
                            "Từ cuối cùng là warehouse — danh từ — nghĩa là kho hàng, nhà kho, "
                            "tòa nhà lớn dùng để lưu trữ hàng hóa trước khi phân phối. "
                            "Ví dụ: 'Amazon operates hundreds of warehouses around the world, each one strategically located near major population centers.' "
                            "Trong bài đọc, warehouse là nơi hàng hóa 'nghỉ chân' "
                            "trên hành trình từ nhà sản xuất đến người tiêu dùng.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách chuỗi cung ứng toàn cầu vận hành nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {"vocabList": W1}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {"vocabList": W1}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {"vocabList": W1}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {"vocabList": W1}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Nền tảng chuỗi cung ứng",
                    "description": "Học 6 từ: logistics, supply, chain, procurement, inventory, warehouse",
                    "data": {"vocabList": W1}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chuỗi cung ứng toàn cầu",
                    "description": "Every product you use has a story — a journey that begins long before it reaches your hands.",
                    "data": {"text": SESSION_1_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chuỗi cung ứng toàn cầu",
                    "description": "Every product you use has a story — a journey that begins long before it reaches your hands.",
                    "data": {"text": SESSION_1_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chuỗi cung ứng toàn cầu",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": SESSION_1_READING}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Nền tảng chuỗi cung ứng",
                    "description": "Viết câu sử dụng 6 từ vựng về nền tảng chuỗi cung ứng.",
                    "data": {
                        "vocabList": W1,
                        "items": [
                            {
                                "targetVocab": "logistics",
                                "prompt": "Dùng từ 'logistics' để viết một câu về vai trò của hậu cần trong việc đưa hàng hóa từ nhà máy đến người tiêu dùng. Ví dụ: The company invested heavily in logistics technology to track every package from the factory floor to the customer's doorstep in real time."
                            },
                            {
                                "targetVocab": "supply",
                                "prompt": "Dùng từ 'supply' để viết một câu về tác động khi nguồn cung bị gián đoạn. Ví dụ: When the supply of natural rubber from Southeast Asia was disrupted by flooding, tire manufacturers around the world faced immediate production delays."
                            },
                            {
                                "targetVocab": "chain",
                                "prompt": "Dùng từ 'chain' để viết một câu về sự phức tạp của chuỗi cung ứng hiện đại. Ví dụ: The supply chain for a single laptop involves over two hundred suppliers across more than fifteen countries, each one a critical link in the production process."
                            },
                            {
                                "targetVocab": "procurement",
                                "prompt": "Dùng từ 'procurement' để viết một câu về quá trình thu mua nguyên vật liệu cho sản xuất. Ví dụ: The procurement department spent three months evaluating potential fabric suppliers before selecting a partner in India that met both quality and price requirements."
                            },
                            {
                                "targetVocab": "inventory",
                                "prompt": "Dùng từ 'inventory' để viết một câu về thách thức trong quản lý hàng tồn kho. Ví dụ: The electronics retailer reduced its inventory by thirty percent after implementing a just-in-time delivery system that restocks products based on real-time sales data."
                            },
                            {
                                "targetVocab": "warehouse",
                                "prompt": "Dùng từ 'warehouse' để viết một câu về vai trò của kho hàng trong chuỗi cung ứng hiện đại. Ví dụ: The new automated warehouse near Hai Phong port can process ten thousand orders per day using robots that retrieve items from shelves without human assistance."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 2: Words 7-12 ─────────────────────────────
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Ôn lại phần 1 và học 6 từ mới về vận chuyển hàng hóa quốc tế.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "logistics — hậu cần, supply — nguồn cung, chain — chuỗi, "
                            "procurement — thu mua, inventory — hàng tồn kho, và warehouse — kho hàng. "
                            "Bạn đã hiểu cách hàng hóa được lên kế hoạch, mua sắm và lưu trữ. "
                            "Bây giờ, chúng ta sẽ đi vào phần tiếp theo: "
                            "hàng hóa thực sự di chuyển qua biên giới như thế nào?\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: freight, customs, clearance, shipment, container, và transit. "
                            "Đây là bộ từ vựng về hành trình vật lý của hàng hóa — "
                            "từ cảng xuất phát đến cảng đích.\n\n"
                            "Từ đầu tiên là freight — danh từ — nghĩa là hàng hóa vận chuyển hoặc cước vận chuyển, "
                            "hàng hóa được vận chuyển với số lượng lớn bằng đường biển, đường bộ, đường sắt hoặc đường hàng không. "
                            "Ví dụ: 'Ocean freight accounts for about ninety percent of global trade by volume, making it the backbone of international commerce.' "
                            "Trong bài đọc, freight mô tả phương thức vận chuyển chính "
                            "mà hàng hóa Việt Nam sử dụng để đến các thị trường quốc tế.\n\n"
                            "Từ thứ hai là customs — danh từ — nghĩa là hải quan, "
                            "cơ quan chính phủ kiểm soát hàng hóa ra vào biên giới quốc gia. "
                            "Ví dụ: 'All imported goods must be declared to customs before they can enter the country and be sold to consumers.' "
                            "Trong bài đọc, customs là cửa ngõ mà mọi hàng hóa phải đi qua — "
                            "nơi kiểm tra, thu thuế và đảm bảo tuân thủ quy định.\n\n"
                            "Từ thứ ba là clearance — danh từ — nghĩa là thông quan, "
                            "quá trình được hải quan chấp thuận cho hàng hóa đi qua biên giới. "
                            "Ví dụ: 'The shipment was delayed for three days because the customs clearance documents were incomplete.' "
                            "Trong bài đọc, clearance là bước quan trọng nhất — "
                            "nếu không hoàn thành thông quan, hàng hóa bị kẹt tại cảng.\n\n"
                            "Từ thứ tư là shipment — danh từ — nghĩa là lô hàng, "
                            "một lượng hàng hóa được gửi từ nơi này đến nơi khác. "
                            "Ví dụ: 'The company tracks every shipment using GPS technology so that customers know exactly when their order will arrive.' "
                            "Trong bài đọc, shipment là đơn vị cơ bản của vận chuyển — "
                            "mỗi lô hàng có mã theo dõi riêng.\n\n"
                            "Từ thứ năm là container — danh từ — nghĩa là container, thùng chứa hàng tiêu chuẩn, "
                            "hộp kim loại lớn được tiêu chuẩn hóa dùng để vận chuyển hàng hóa bằng tàu, xe tải hoặc tàu hỏa. "
                            "Ví dụ: 'The invention of the standardized shipping container in the 1950s reduced loading times from weeks to hours and transformed global trade.' "
                            "Trong bài đọc, container là phát minh đã cách mạng hóa thương mại — "
                            "nhờ nó, chi phí vận chuyển giảm mạnh.\n\n"
                            "Từ cuối cùng là transit — danh từ — nghĩa là quá cảnh, vận chuyển, "
                            "thời gian hoặc quá trình hàng hóa di chuyển từ điểm này đến điểm khác. "
                            "Ví dụ: 'Goods in transit from Vietnam to Europe spend about twenty-five days at sea before reaching the port of Rotterdam.' "
                            "Trong bài đọc, transit là khoảng thời gian hàng hóa 'trên đường' — "
                            "giảm thời gian transit là mục tiêu của mọi nhà quản lý logistics.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về hành trình vận chuyển hàng hóa quốc tế nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Vận chuyển hàng hóa quốc tế",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {"vocabList": W2}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Vận chuyển hàng hóa quốc tế",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {"vocabList": W2}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Vận chuyển hàng hóa quốc tế",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {"vocabList": W2}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Vận chuyển hàng hóa quốc tế",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {"vocabList": W2}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Vận chuyển hàng hóa quốc tế",
                    "description": "Học 6 từ: freight, customs, clearance, shipment, container, transit",
                    "data": {"vocabList": W2}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Hành trình vận chuyển hàng hóa quốc tế",
                    "description": "Once a product is manufactured, it must travel — sometimes thousands of kilometers — to reach its destination.",
                    "data": {"text": SESSION_2_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Hành trình vận chuyển hàng hóa quốc tế",
                    "description": "Once a product is manufactured, it must travel — sometimes thousands of kilometers — to reach its destination.",
                    "data": {"text": SESSION_2_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Hành trình vận chuyển hàng hóa quốc tế",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": SESSION_2_READING}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Vận chuyển hàng hóa quốc tế",
                    "description": "Viết câu sử dụng 6 từ vựng về vận chuyển hàng hóa.",
                    "data": {
                        "vocabList": W2,
                        "items": [
                            {
                                "targetVocab": "freight",
                                "prompt": "Dùng từ 'freight' để viết một câu về phương thức vận chuyển hàng hóa quốc tế. Ví dụ: Ocean freight remains the most cost-effective way to transport large volumes of goods, even though it takes much longer than air transport."
                            },
                            {
                                "targetVocab": "customs",
                                "prompt": "Dùng từ 'customs' để viết một câu về vai trò của hải quan trong thương mại quốc tế. Ví dụ: Vietnamese customs officials inspect thousands of containers every day at Hai Phong port to ensure that all imported goods comply with national safety standards."
                            },
                            {
                                "targetVocab": "clearance",
                                "prompt": "Dùng từ 'clearance' để viết một câu về quá trình thông quan và tác động của nó đến chuỗi cung ứng. Ví dụ: The electronic clearance system reduced the average time for goods to pass through customs from five days to just eight hours."
                            },
                            {
                                "targetVocab": "shipment",
                                "prompt": "Dùng từ 'shipment' để viết một câu về việc theo dõi lô hàng trong chuỗi cung ứng. Ví dụ: The coffee exporter sent a shipment of fifty containers to Germany, each one tracked by satellite from the moment it left the warehouse in Dak Lak."
                            },
                            {
                                "targetVocab": "container",
                                "prompt": "Dùng từ 'container' để viết một câu về vai trò của container trong thương mại toàn cầu. Ví dụ: The standardized shipping container transformed global trade by making it possible to load goods onto a truck, transfer them to a train, and then onto a ship without ever unpacking."
                            },
                            {
                                "targetVocab": "transit",
                                "prompt": "Dùng từ 'transit' để viết một câu về thời gian vận chuyển hàng hóa giữa các quốc gia. Ví dụ: Goods in transit between Ho Chi Minh City and Los Angeles spend approximately fourteen days at sea, plus additional time for customs clearance at both ends."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 3: Words 13-18 ────────────────────────────
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về chiến lược chuỗi cung ứng hiện đại.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: logistics, supply, chain, procurement, inventory, warehouse — "
                            "những khái niệm về cách hàng hóa được lên kế hoạch, mua sắm và lưu trữ. "
                            "Trong phần 2, bạn đã học thêm freight, customs, clearance, shipment, container, transit — "
                            "bộ từ vựng về hành trình vật lý của hàng hóa qua biên giới.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh rất thời sự: "
                            "chiến lược chuỗi cung ứng hiện đại — cách các doanh nghiệp xây dựng chuỗi cung ứng "
                            "vừa hiệu quả vừa chống chịu được khủng hoảng. "
                            "Bạn sẽ học 6 từ mới: disruption, resilience, diversification, nearshoring, traceability, và optimization.\n\n"
                            "Từ đầu tiên là disruption — danh từ — nghĩa là sự gián đoạn, "
                            "bất kỳ sự kiện nào làm gián đoạn dòng chảy bình thường của hàng hóa trong chuỗi cung ứng. "
                            "Ví dụ: 'The Suez Canal blockage in 2021 caused a massive disruption to global shipping, delaying goods worth billions of dollars.' "
                            "Trong bài đọc, disruption là từ khóa của thời đại hậu COVID — "
                            "khi cả thế giới nhận ra chuỗi cung ứng mong manh đến mức nào.\n\n"
                            "Từ thứ hai là resilience — danh từ — nghĩa là khả năng phục hồi, "
                            "năng lực của một hệ thống để chịu đựng cú sốc và phục hồi nhanh chóng. "
                            "Ví dụ: 'After the pandemic exposed weaknesses in global supply chains, companies began investing heavily in resilience rather than just efficiency.' "
                            "Trong bài đọc, resilience là mục tiêu mới — "
                            "không chỉ nhanh và rẻ, mà còn phải bền vững trước khủng hoảng.\n\n"
                            "Từ thứ ba là diversification — danh từ — nghĩa là đa dạng hóa, "
                            "chiến lược phân tán rủi ro bằng cách sử dụng nhiều nhà cung cấp, địa điểm sản xuất hoặc tuyến vận chuyển. "
                            "Ví dụ: 'Supply chain diversification means sourcing components from multiple countries so that a problem in one region does not shut down the entire production line.' "
                            "Trong bài đọc, diversification giải thích vì sao Việt Nam "
                            "đang hưởng lợi lớn khi các công ty chuyển sản xuất ra khỏi Trung Quốc.\n\n"
                            "Từ thứ tư là nearshoring — danh từ — nghĩa là chuyển sản xuất về gần, "
                            "xu hướng di chuyển sản xuất đến các quốc gia gần thị trường tiêu thụ hơn. "
                            "Ví dụ: 'American companies are nearshoring production to Mexico to reduce shipping times and avoid the risks of relying on factories in distant countries.' "
                            "Trong bài đọc, nearshoring là xu hướng đối lập với offshoring — "
                            "thay vì sản xuất ở nơi rẻ nhất, doanh nghiệp chọn nơi gần nhất.\n\n"
                            "Từ thứ năm là traceability — danh từ — nghĩa là khả năng truy xuất nguồn gốc, "
                            "khả năng theo dõi hành trình của sản phẩm từ nguyên liệu thô đến thành phẩm. "
                            "Ví dụ: 'Consumers increasingly demand traceability, wanting to know exactly where their food was grown and how their clothes were made.' "
                            "Trong bài đọc, traceability là yêu cầu ngày càng quan trọng — "
                            "người tiêu dùng muốn biết sản phẩm đến từ đâu và được sản xuất như thế nào.\n\n"
                            "Từ cuối cùng là optimization — danh từ — nghĩa là tối ưu hóa, "
                            "quá trình làm cho chuỗi cung ứng hoạt động hiệu quả nhất có thể. "
                            "Ví dụ: 'Supply chain optimization uses artificial intelligence to find the fastest routes, the lowest costs, and the ideal inventory levels for every product.' "
                            "Trong bài đọc, optimization là đích đến — "
                            "khi mọi mắt xích trong chuỗi cung ứng hoạt động ở mức tốt nhất.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về chiến lược chuỗi cung ứng hiện đại nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Chiến lược chuỗi cung ứng hiện đại",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": W3}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Chiến lược chuỗi cung ứng hiện đại",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": W3}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Chiến lược chuỗi cung ứng hiện đại",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": W3}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Chiến lược chuỗi cung ứng hiện đại",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": W3}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Chiến lược chuỗi cung ứng hiện đại",
                    "description": "Học 6 từ: disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": W3}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chiến lược chuỗi cung ứng sau đại dịch",
                    "description": "In recent years, the world has learned a painful lesson: global supply chains are powerful but fragile.",
                    "data": {"text": SESSION_3_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chiến lược chuỗi cung ứng sau đại dịch",
                    "description": "In recent years, the world has learned a painful lesson: global supply chains are powerful but fragile.",
                    "data": {"text": SESSION_3_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chiến lược chuỗi cung ứng sau đại dịch",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": SESSION_3_READING}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Chiến lược chuỗi cung ứng hiện đại",
                    "description": "Viết câu sử dụng 6 từ vựng về chiến lược chuỗi cung ứng.",
                    "data": {
                        "vocabList": W3,
                        "items": [
                            {
                                "targetVocab": "disruption",
                                "prompt": "Dùng từ 'disruption' để viết một câu về tác động của một sự kiện gián đoạn đối với chuỗi cung ứng toàn cầu. Ví dụ: The factory fire in Japan caused a major disruption to the global automotive supply chain, forcing car manufacturers on three continents to halt production for weeks."
                            },
                            {
                                "targetVocab": "resilience",
                                "prompt": "Dùng từ 'resilience' để viết một câu về cách doanh nghiệp xây dựng khả năng phục hồi cho chuỗi cung ứng. Ví dụ: The company built supply chain resilience by maintaining three months of safety stock and establishing backup agreements with alternative suppliers in different countries."
                            },
                            {
                                "targetVocab": "diversification",
                                "prompt": "Dùng từ 'diversification' để viết một câu về chiến lược đa dạng hóa nguồn cung. Ví dụ: After the pandemic, the electronics manufacturer pursued aggressive diversification, moving from a single Chinese supplier to a network of factories in Vietnam, India, and Thailand."
                            },
                            {
                                "targetVocab": "nearshoring",
                                "prompt": "Dùng từ 'nearshoring' để viết một câu về xu hướng chuyển sản xuất về gần thị trường tiêu thụ. Ví dụ: European fashion brands are nearshoring production to Turkey and Morocco to cut delivery times from six weeks to ten days and respond faster to changing consumer trends."
                            },
                            {
                                "targetVocab": "traceability",
                                "prompt": "Dùng từ 'traceability' để viết một câu về tầm quan trọng của việc truy xuất nguồn gốc sản phẩm. Ví dụ: The seafood company uses blockchain technology to provide full traceability, allowing customers to scan a QR code and see exactly which fishing boat caught their shrimp."
                            },
                            {
                                "targetVocab": "optimization",
                                "prompt": "Dùng từ 'optimization' để viết một câu về việc tối ưu hóa chuỗi cung ứng bằng công nghệ. Ví dụ: Through supply chain optimization using artificial intelligence, the retailer reduced shipping costs by twenty percent while cutting average delivery times in half."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 4: Review (all 18 words) ─────────────────
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Cùng ôn lại trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Chuỗi cung ứng toàn cầu. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "logistics — hậu cần, supply — nguồn cung, chain — chuỗi, "
                            "procurement — thu mua, inventory — hàng tồn kho, và warehouse — kho hàng. "
                            "Đây là bộ từ vựng về cách hàng hóa được lên kế hoạch, mua sắm và lưu trữ.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào hành trình vận chuyển: "
                            "freight — hàng hóa vận chuyển, customs — hải quan, clearance — thông quan, "
                            "shipment — lô hàng, container — thùng chứa hàng, và transit — quá cảnh. "
                            "Những từ này giúp bạn hiểu hàng hóa di chuyển qua biên giới như thế nào.\n\n"
                            "Trong phần 3, bạn đã khám phá chiến lược hiện đại: "
                            "disruption — gián đoạn, resilience — khả năng phục hồi, diversification — đa dạng hóa, "
                            "nearshoring — chuyển sản xuất về gần, traceability — truy xuất nguồn gốc, và optimization — tối ưu hóa. "
                            "Đây là những từ về cách doanh nghiệp xây dựng chuỗi cung ứng thông minh hơn.\n\n"
                            "Bây giờ, phần ôn tập này sẽ giúp bạn củng cố toàn bộ 18 từ vựng. "
                            "Bạn sẽ xem lại flashcard, luyện phát âm, và viết câu với tất cả các từ. "
                            "Sau phần ôn tập, bạn sẽ sẵn sàng cho bài đọc tổng hợp — "
                            "một bài viết dài hơn sử dụng cả 18 từ trong một ngữ cảnh liền mạch. "
                            "Hãy bắt đầu nào!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: logistics, supply, chain, procurement, inventory, warehouse, freight, customs, clearance, shipment, container, transit, disruption, resilience, diversification, nearshoring, traceability, optimization",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng chuỗi cung ứng",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "logistics",
                                "prompt": "Dùng từ 'logistics' để viết một câu về tầm quan trọng của hậu cần trong nền kinh tế xuất khẩu của Việt Nam. Ví dụ: Vietnam's logistics sector has grown into a twenty-billion-dollar industry as the country becomes one of Southeast Asia's largest manufacturing and export hubs."
                            },
                            {
                                "targetVocab": "supply",
                                "prompt": "Dùng từ 'supply' để viết một câu về cách nguồn cung ảnh hưởng đến giá cả toàn cầu. Ví dụ: A sudden drop in the global supply of cooking oil caused prices to double in supermarkets across Europe and Asia within just two months."
                            },
                            {
                                "targetVocab": "chain",
                                "prompt": "Dùng từ 'chain' để viết một câu về sự phụ thuộc lẫn nhau trong chuỗi cung ứng toàn cầu. Ví dụ: The semiconductor shortage revealed how a single weak link in the supply chain can bring entire industries to a standstill across multiple continents."
                            },
                            {
                                "targetVocab": "procurement",
                                "prompt": "Dùng từ 'procurement' để viết một câu về chiến lược thu mua của một doanh nghiệp quốc tế. Ví dụ: The multinational corporation restructured its procurement strategy to source raw materials from at least three different countries for every critical component."
                            },
                            {
                                "targetVocab": "inventory",
                                "prompt": "Dùng từ 'inventory' để viết một câu về cách công nghệ thay đổi quản lý hàng tồn kho. Ví dụ: The AI-powered inventory management system predicts demand patterns two weeks in advance, automatically reordering stock before shelves run empty."
                            },
                            {
                                "targetVocab": "warehouse",
                                "prompt": "Dùng từ 'warehouse' để viết một câu về sự phát triển của hệ thống kho hàng tại Việt Nam. Ví dụ: The new cold-storage warehouse near Cat Lai port allows Vietnamese seafood exporters to keep products fresh during the entire customs clearance process."
                            },
                            {
                                "targetVocab": "freight",
                                "prompt": "Dùng từ 'freight' để viết một câu về chi phí vận chuyển hàng hóa quốc tế. Ví dụ: Global freight rates tripled during the pandemic as demand for shipping containers far exceeded the available capacity on major trade routes."
                            },
                            {
                                "targetVocab": "customs",
                                "prompt": "Dùng từ 'customs' để viết một câu về cải cách thủ tục hải quan để thúc đẩy thương mại. Ví dụ: The government's customs modernization program introduced electronic declarations and automated risk assessment, cutting average processing times by sixty percent."
                            },
                            {
                                "targetVocab": "clearance",
                                "prompt": "Dùng từ 'clearance' để viết một câu về tác động của chậm trễ thông quan đối với doanh nghiệp xuất khẩu. Ví dụ: A two-day delay in customs clearance at the destination port cost the exporter thousands of dollars in storage fees and a penalty for late delivery to the buyer."
                            },
                            {
                                "targetVocab": "shipment",
                                "prompt": "Dùng từ 'shipment' để viết một câu về công nghệ theo dõi lô hàng trong thời gian thực. Ví dụ: The logistics platform provides real-time tracking for every shipment, sending automatic alerts to both the sender and receiver whenever the goods pass through a checkpoint."
                            },
                            {
                                "targetVocab": "container",
                                "prompt": "Dùng từ 'container' để viết một câu về tình trạng thiếu container trong thương mại toàn cầu. Ví dụ: The global container shortage during 2021 forced many Vietnamese exporters to wait weeks for an available container, delaying deliveries and increasing costs significantly."
                            },
                            {
                                "targetVocab": "transit",
                                "prompt": "Dùng từ 'transit' để viết một câu về nỗ lực giảm thời gian vận chuyển hàng hóa. Ví dụ: The new express rail service between Hanoi and Kunming has reduced transit time for electronics components from five days by truck to just eighteen hours."
                            },
                            {
                                "targetVocab": "disruption",
                                "prompt": "Dùng từ 'disruption' để viết một câu về bài học từ đại dịch COVID-19 đối với chuỗi cung ứng. Ví dụ: The pandemic-driven disruption taught companies that the cheapest supply chain is not always the best — sometimes paying more for reliability saves money in the long run."
                            },
                            {
                                "targetVocab": "resilience",
                                "prompt": "Dùng từ 'resilience' để viết một câu về đầu tư vào khả năng phục hồi chuỗi cung ứng. Ví dụ: Building supply chain resilience requires upfront investment in backup suppliers and safety stock, but it pays for itself the first time a major disruption hits."
                            },
                            {
                                "targetVocab": "diversification",
                                "prompt": "Dùng từ 'diversification' để viết một câu về lợi ích của đa dạng hóa nguồn cung cho Việt Nam. Ví dụ: Vietnam has become a major beneficiary of global supply chain diversification, attracting billions of dollars in foreign investment from companies seeking alternatives to single-country manufacturing."
                            },
                            {
                                "targetVocab": "nearshoring",
                                "prompt": "Dùng từ 'nearshoring' để viết một câu về xu hướng nearshoring và tác động đến thương mại khu vực. Ví dụ: The nearshoring trend has boosted manufacturing in Mexico, where factories now produce goods for the American market that were previously made in Asia."
                            },
                            {
                                "targetVocab": "traceability",
                                "prompt": "Dùng từ 'traceability' để viết một câu về yêu cầu truy xuất nguồn gốc trong ngành thực phẩm. Ví dụ: European regulations now require full traceability for all imported food products, meaning Vietnamese rice exporters must document every step from the paddy field to the supermarket shelf."
                            },
                            {
                                "targetVocab": "optimization",
                                "prompt": "Dùng từ 'optimization' để viết một câu về vai trò của trí tuệ nhân tạo trong tối ưu hóa chuỗi cung ứng. Ví dụ: The company's supply chain optimization algorithm analyzes weather patterns, port congestion data, and fuel prices to recommend the most cost-effective shipping route for each order."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 5: Full reading + farewell ────────────────
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc tổng hợp",
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về chuỗi cung ứng toàn cầu.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về chuỗi cung ứng toàn cầu — từ cách hàng hóa được thu mua và lưu trữ, "
                            "cách chúng vượt đại dương qua hải quan, đến cách doanh nghiệp xây dựng chuỗi cung ứng "
                            "chống chịu được khủng hoảng.\n\n"
                            "Bạn sẽ gặp lại logistics, supply, chain, procurement, inventory, warehouse "
                            "trong phần mở đầu về nền tảng của chuỗi cung ứng. "
                            "Tiếp theo, freight, customs, clearance, shipment, container, transit "
                            "sẽ giúp bạn hiểu hành trình vật lý của hàng hóa. "
                            "Và cuối cùng, disruption, resilience, diversification, nearshoring, traceability, optimization "
                            "sẽ đưa bạn vào thế giới chiến lược chuỗi cung ứng hiện đại.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Chuỗi cung ứng toàn cầu — Bức tranh toàn cảnh",
                    "description": "The global supply chain is one of the greatest achievements of modern commerce — and one of its greatest vulnerabilities.",
                    "data": {"text": SESSION_5_READING}
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Chuỗi cung ứng toàn cầu — Bức tranh toàn cảnh",
                    "description": "The global supply chain is one of the greatest achievements of modern commerce — and one of its greatest vulnerabilities.",
                    "data": {"text": SESSION_5_READING}
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Chuỗi cung ứng toàn cầu — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {"text": SESSION_5_READING}
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích chuỗi cung ứng toàn cầu",
                    "description": "Viết đoạn văn tiếng Anh phân tích về chuỗi cung ứng sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của chuỗi cung ứng toàn cầu. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích cách đại dịch COVID-19 đã thay đổi chuỗi cung ứng toàn cầu. Giải thích disruption đã xảy ra như thế nào, tại sao resilience trở thành ưu tiên hàng đầu, và cách diversification cùng nearshoring đang định hình lại logistics toàn cầu — đặc biệt đối với Việt Nam.",
                            "Hãy mô tả hành trình của một sản phẩm xuất khẩu từ Việt Nam đến châu Âu. Giải thích vai trò của procurement, warehouse, freight, customs clearance, container, và transit trong hành trình đó — và cách optimization có thể giúp giảm chi phí và thời gian vận chuyển."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần trách nhiệm ấm áp.",
                    "data": {
                        "text": (
                            "Bạn đã hoàn thành bài học về Chuỗi cung ứng toàn cầu — "
                            "và cũng là bài học cuối cùng trong chuỗi Thương mại quốc tế. "
                            "Hãy dừng lại một chút và nhìn lại quãng đường bạn đã đi. "
                            "Từ lý thuyết thương mại, rào cản thuế quan, thị trường ngoại hối, tổ chức thương mại, "
                            "đến chuỗi cung ứng toàn cầu — bạn đã xây dựng một vốn từ vựng "
                            "mà nhiều sinh viên kinh tế mất cả năm mới tích lũy được. "
                            "Bây giờ, hãy cùng ôn lại những từ quan trọng nhất — "
                            "và tôi muốn bạn tự hỏi: mình sẽ dùng chúng ở đâu?\n\n"
                            "Logistics — hậu cần. Đây không chỉ là từ vựng — "
                            "đây là ngành công nghiệp trị giá hàng tỷ đô la mà Việt Nam đang phát triển mạnh mẽ. "
                            "Mỗi khi bạn đặt hàng online và nhận được trong 24 giờ, đó là logistics đang hoạt động. "
                            "Ví dụ mới: The logistics company redesigned its delivery network "
                            "to guarantee next-day delivery to every province in Vietnam, "
                            "cutting transit times by forty percent.\n\n"
                            "Procurement — thu mua. Mỗi sản phẩm bắt đầu từ đây. "
                            "Nếu bạn làm việc trong bất kỳ công ty sản xuất nào, "
                            "procurement sẽ là từ bạn nghe mỗi ngày. "
                            "Ví dụ mới: The procurement officer flew to three countries in one week "
                            "to negotiate better prices for the electronic components "
                            "that the factory needs for its new product line.\n\n"
                            "Container — thùng chứa hàng tiêu chuẩn. "
                            "Phát minh đơn giản này đã thay đổi thương mại toàn cầu mãi mãi. "
                            "Hiểu từ này, bạn hiểu vì sao hàng hóa có thể đi vòng quanh thế giới "
                            "với chi phí thấp đến kinh ngạc. "
                            "Ví dụ mới: The port of Hai Phong handles over five million containers per year, "
                            "making it one of the busiest container terminals in Southeast Asia.\n\n"
                            "Disruption — gián đoạn. Đây là từ mà cả thế giới học được sau COVID-19. "
                            "Bạn sẽ gặp nó trong mọi bài báo, mọi báo cáo về chuỗi cung ứng. "
                            "Ví dụ mới: The volcanic eruption in Iceland caused a disruption to European air freight "
                            "that lasted two weeks, forcing companies to switch to ocean shipping "
                            "for time-sensitive medical supplies.\n\n"
                            "Resilience — khả năng phục hồi. "
                            "Nếu disruption là vấn đề, thì resilience là giải pháp. "
                            "Đây là từ quan trọng nhất trong chiến lược chuỗi cung ứng hiện đại. "
                            "Ví dụ mới: The government launched a national program to build supply chain resilience, "
                            "offering tax incentives to companies that maintain backup suppliers "
                            "and invest in domestic manufacturing capacity.\n\n"
                            "Optimization — tối ưu hóa. Đây là đích đến cuối cùng — "
                            "khi mọi mắt xích trong chuỗi cung ứng hoạt động ở mức tốt nhất có thể. "
                            "Ví dụ mới: The startup's supply chain optimization platform "
                            "uses machine learning to predict port congestion three days in advance, "
                            "allowing shippers to reroute containers before delays occur.\n\n"
                            "Bây giờ, đây là câu hỏi tôi muốn bạn trả lời thật lòng: "
                            "bạn sẽ làm gì với 18 từ vựng này? "
                            "Chúng không có giá trị nếu chỉ nằm trong đầu bạn. "
                            "Chúng chỉ thực sự có ý nghĩa khi bạn dùng chúng — "
                            "trong bài tập, trong thảo luận nhóm, trong bài viết, trong cuộc phỏng vấn.\n\n"
                            "Tuần này, hãy làm một việc cụ thể: "
                            "mở một bài báo tiếng Anh về supply chain trên Reuters hoặc Bloomberg, "
                            "đọc hai đoạn đầu, và gạch chân mỗi từ vựng bạn nhận ra. "
                            "Nếu bạn nhận ra được 5 từ trở lên, bạn đã tiến bộ thật sự. "
                            "Nếu bạn muốn thử thách hơn, hãy viết một đoạn tóm tắt 50 từ bằng tiếng Anh "
                            "về bài báo đó — dùng ít nhất 4 từ vựng từ bài học.\n\n"
                            "Bạn đã có kiến thức. Bây giờ hãy biến nó thành kỹ năng. "
                            "Tôi tin bạn sẽ làm được — và tôi mong được thấy bạn dùng những từ này "
                            "trong những ngữ cảnh thực tế. "
                            "Chúc bạn tiếp tục hành trình học tập thật hiệu quả — "
                            "hẹn gặp lại ở chuỗi bài học tiếp theo!"
                        )
                    }
                }
            ]
        }
    ]
}

# ── Validate before upload ───────────────────────────────────
print("Validating content...")
validate_all(content)
print("Validation passed!")

# ── Upload ───────────────────────────────────────────────────
token = get_firebase_id_token(UID)
res = requests.post(
    f"{API_BASE}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
res.raise_for_status()
curriculum_id = res.json()["id"]
print(f"Created curriculum: {curriculum_id}")
print(f"Title: {content['title']}")

# ── Duplicate check SQL ──────────────────────────────────────
print("\n-- Duplicate check SQL (run manually): --")
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Supply Chains – Chuỗi Cung Ứng Toàn Cầu' AND uid = '{UID}' ORDER BY created_at;")
