"""
en-fr preintermediate curriculum: French Gastronomy
Series A1 (bozgk7m4) — Food & Dining, displayOrder 4
Description tone: empathetic_observation
Farewell tone: warm accountability

Vocab:
  Part 1: gastronomie, terroir, dégustation, sommelier, millésime, accord
  Part 2: brasserie, ardoise, plat du jour, convive, addition, pourboire
  Part 3: étoilé, brigade, dressage, amuse-bouche, velouté, réduction
"""

import sys, json, logging
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/en-fr")
from api_helpers import create_curriculum, add_to_series, set_display_order, set_price
from validate_content import validate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SERIES_ID = "bozgk7m4"
DISPLAY_ORDER = 4

content = {
    "title": "French Gastronomy",
    "contentTypeTags": [],
    "difficultyTags": ["preintermediate"],
    "description": "HAVE YOU EVER SAT IN A FRENCH RESTAURANT, STARING AT THE MENU, FEELING LIKE EVERYONE ELSE SPEAKS A SECRET LANGUAGE?\n\nYou know the difference between a bistro and a brasserie — sort of. You've heard of terroir and sommelier, but when the waiter rattles off the plat du jour and asks about your preferred millésime, you freeze. That gap between 'I love French food' and 'I can talk about French food' is exactly where this curriculum lives.\n\nThink of French gastronomy as a cathedral — every dish is a stone, every technique a flying buttress, every meal a ceremony with its own vocabulary. Without the words, you're admiring the building from outside. With them, you walk through the doors.\n\nAcross three sessions, you'll master 18 essential terms — from the philosophy of terroir to the precision of a brigade de cuisine, from ordering at a neighborhood brasserie to understanding what makes a restaurant étoilé. By the end, you won't just eat in France — you'll dine.\n\nThis isn't vocabulary for a textbook. It's vocabulary for a life where French food culture becomes yours to discuss, debate, and savor — in the language it was born in.",
    "preview": {
        "text": "Dive into the rich world of French gastronomy through 18 carefully chosen words that unlock the culture behind the cuisine. You'll start with gastronomie, terroir, dégustation, sommelier, millésime, and accord — the philosophical foundations of how France thinks about food and wine pairing. Then move to brasserie, ardoise, plat du jour, convive, addition, and pourboire — the everyday vocabulary of dining out in France, from reading the chalkboard menu to splitting the bill. Finally, explore étoilé, brigade, dressage, amuse-bouche, velouté, and réduction — the professional kitchen vocabulary that separates casual cooking from haute cuisine. Through three French reading passages, a comprehensive review, and a final integrated reading, you'll build the confidence to discuss French food culture with nuance and authenticity."
    },
    "learningSessions": [
        {
            "title": "Part 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Introduction to Part 1 vocabulary",
                    "description": "Welcome and introduction to 6 words about the philosophy of French gastronomy.",
                    "data": {
                        "text": "Welcome to French Gastronomy — a curriculum that takes you beyond the plate and into the language of one of the world's most celebrated food cultures. France doesn't just eat — it philosophizes about eating. And today, you'll start learning the words that make that philosophy accessible.\n\nIn this first session, you'll learn six words: gastronomie, terroir, dégustation, sommelier, millésime, and accord. These aren't kitchen terms — they're cultural concepts that shape how the French think about food and wine.\n\nLet's begin with gastronomie — it's a feminine noun meaning gastronomy, the art and science of good eating. In French, gastronomie isn't just about cooking well — it's about the entire experience of selecting, preparing, presenting, and savoring food. Example: 'La gastronomie française est inscrite au patrimoine immatériel de l'UNESCO depuis 2010.' In our reading, you'll see how gastronomie represents a national identity, not just a hobby.\n\nNext is terroir — a masculine noun that has no perfect English translation. It refers to the complete natural environment in which a food or wine is produced — the soil, climate, altitude, and local traditions that give a product its unique character. Example: 'Ce vin exprime parfaitement le terroir de la vallée du Rhône.' In the reading, terroir explains why the same grape variety tastes completely different depending on where it's grown.\n\nThird is dégustation — a feminine noun meaning tasting, specifically a structured, attentive tasting of wine or food. It's not casual sipping — it's an analytical process. Example: 'Nous avons réservé une dégustation de cinq vins dans un domaine viticole près de Beaune.' In context, dégustation is the ritual through which French culture transforms drinking into an intellectual exercise.\n\nFourth is sommelier — a masculine noun for a trained wine professional who specializes in all aspects of wine service, from selection to pairing. Example: 'Le sommelier nous a recommandé un bourgogne blanc pour accompagner le poisson.' In the reading, the sommelier is the bridge between the kitchen and the cellar — the person who makes terroir accessible to diners.\n\nFifth is millésime — a masculine noun meaning vintage, the year a wine was produced. In French wine culture, the millésime tells you everything about the weather conditions that shaped the grapes. Example: 'Le millésime 2015 est considéré comme exceptionnel pour les bordeaux rouges.' In our passage, millésime illustrates how the French treat wine as a living record of time and place.\n\nFinally, accord — a masculine noun meaning pairing or harmony, specifically the art of matching food and wine so they enhance each other. Example: 'L'accord entre le fromage de chèvre et le sancerre est un classique de la gastronomie française.' In the reading, accord represents the ultimate goal of French dining — not just good food and good wine, but the perfect marriage between them.\n\nSix words that open the door to understanding how France thinks about what it eats and drinks. Let's start with the flashcards, then read about the philosophy behind French gastronomy."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Philosophy of gastronomy",
                    "description": "Learn 6 words: gastronomie, terroir, dégustation, sommelier, millésime, accord",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Philosophy of gastronomy",
                    "description": "Learn 6 words: gastronomie, terroir, dégustation, sommelier, millésime, accord",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Philosophy of gastronomy",
                    "description": "Learn 6 words: gastronomie, terroir, dégustation, sommelier, millésime, accord",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Philosophy of gastronomy",
                    "description": "Learn 6 words: gastronomie, terroir, dégustation, sommelier, millésime, accord",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Philosophy of gastronomy",
                    "description": "Learn 6 words: gastronomie, terroir, dégustation, sommelier, millésime, accord",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Reading: The philosophy of French gastronomy",
                    "description": "La gastronomie française repose sur une philosophie simple mais exigeante.",
                    "data": {
                        "text": "La gastronomie française repose sur une philosophie simple mais exigeante : chaque aliment possède une vérité, et le rôle du cuisinier est de la révéler. Cette idée, profondément enracinée dans la culture nationale, explique pourquoi la France accorde autant d'importance à l'origine des produits, à la saisonnalité et à l'art de la table.\n\nAu cœur de cette philosophie se trouve la notion de terroir. Le terroir désigne l'ensemble des conditions naturelles — sol, climat, exposition, altitude — qui confèrent à un produit son caractère unique. Un camembert de Normandie ne ressemble pas à un camembert industriel précisément parce que le terroir normand — ses pâturages humides, ses vaches de race locale, son climat océanique — imprègne le lait d'une saveur impossible à reproduire ailleurs. Le terroir est la raison pour laquelle les Français insistent sur les appellations d'origine : elles protègent non pas une marque, mais un lieu.\n\nCette attention au terroir se prolonge naturellement dans la dégustation. Déguster, en français, ne signifie pas simplement boire ou manger — c'est un acte d'attention. Lors d'une dégustation de vin, on observe la robe, on hume les arômes, on laisse le liquide parcourir le palais avant de juger. C'est un exercice à la fois sensoriel et intellectuel, où chaque gorgée raconte l'histoire d'un millésime — l'année de récolte, avec ses caprices météorologiques, ses gelées tardives ou ses étés caniculaires.\n\nLe millésime est fondamental dans la culture vinicole française. Deux bouteilles du même domaine, du même cépage, peuvent offrir des expériences radicalement différentes selon leur année de production. Un millésime 2003, marqué par la canicule, donnera des vins puissants et concentrés. Un millésime 2013, plus frais et pluvieux, produira des vins plus légers et acidulés. Comprendre les millésimes, c'est comprendre que le vin est un produit vivant, façonné par le temps qu'il fait autant que par la main de l'homme.\n\nDans un restaurant, la personne qui maîtrise cette connaissance est le sommelier. Le sommelier ne se contente pas de servir le vin — il conseille, il éduque, il crée des ponts entre la cuisine et la cave. Son expertise repose sur des années de formation : connaissance des régions viticoles, des cépages, des techniques de vinification, mais aussi capacité à écouter le client et à comprendre ses préférences.\n\nLe travail du sommelier culmine dans l'accord — l'art de marier un plat et un vin pour que chacun magnifie l'autre. Un accord réussi n'est pas une simple compatibilité : c'est une synergie. Le gras d'un foie gras appelle l'acidité d'un sauternes. La salinité d'une huître trouve son écho dans la minéralité d'un muscadet. L'accord parfait transforme un repas en expérience — et c'est précisément ce que la gastronomie française cherche à accomplir à chaque table."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Reading: The philosophy of French gastronomy",
                    "description": "La gastronomie française repose sur une philosophie simple mais exigeante.",
                    "data": {
                        "text": "La gastronomie française repose sur une philosophie simple mais exigeante : chaque aliment possède une vérité, et le rôle du cuisinier est de la révéler. Cette idée, profondément enracinée dans la culture nationale, explique pourquoi la France accorde autant d'importance à l'origine des produits, à la saisonnalité et à l'art de la table.\n\nAu cœur de cette philosophie se trouve la notion de terroir. Le terroir désigne l'ensemble des conditions naturelles — sol, climat, exposition, altitude — qui confèrent à un produit son caractère unique. Un camembert de Normandie ne ressemble pas à un camembert industriel précisément parce que le terroir normand — ses pâturages humides, ses vaches de race locale, son climat océanique — imprègne le lait d'une saveur impossible à reproduire ailleurs. Le terroir est la raison pour laquelle les Français insistent sur les appellations d'origine : elles protègent non pas une marque, mais un lieu.\n\nCette attention au terroir se prolonge naturellement dans la dégustation. Déguster, en français, ne signifie pas simplement boire ou manger — c'est un acte d'attention. Lors d'une dégustation de vin, on observe la robe, on hume les arômes, on laisse le liquide parcourir le palais avant de juger. C'est un exercice à la fois sensoriel et intellectuel, où chaque gorgée raconte l'histoire d'un millésime — l'année de récolte, avec ses caprices météorologiques, ses gelées tardives ou ses étés caniculaires.\n\nLe millésime est fondamental dans la culture vinicole française. Deux bouteilles du même domaine, du même cépage, peuvent offrir des expériences radicalement différentes selon leur année de production. Un millésime 2003, marqué par la canicule, donnera des vins puissants et concentrés. Un millésime 2013, plus frais et pluvieux, produira des vins plus légers et acidulés. Comprendre les millésimes, c'est comprendre que le vin est un produit vivant, façonné par le temps qu'il fait autant que par la main de l'homme.\n\nDans un restaurant, la personne qui maîtrise cette connaissance est le sommelier. Le sommelier ne se contente pas de servir le vin — il conseille, il éduque, il crée des ponts entre la cuisine et la cave. Son expertise repose sur des années de formation : connaissance des régions viticoles, des cépages, des techniques de vinification, mais aussi capacité à écouter le client et à comprendre ses préférences.\n\nLe travail du sommelier culmine dans l'accord — l'art de marier un plat et un vin pour que chacun magnifie l'autre. Un accord réussi n'est pas une simple compatibilité : c'est une synergie. Le gras d'un foie gras appelle l'acidité d'un sauternes. La salinité d'une huître trouve son écho dans la minéralité d'un muscadet. L'accord parfait transforme un repas en expérience — et c'est précisément ce que la gastronomie française cherche à accomplir à chaque table."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Listen: The philosophy of French gastronomy",
                    "description": "Listen to the passage and follow along.",
                    "data": {
                        "text": "La gastronomie française repose sur une philosophie simple mais exigeante : chaque aliment possède une vérité, et le rôle du cuisinier est de la révéler. Cette idée, profondément enracinée dans la culture nationale, explique pourquoi la France accorde autant d'importance à l'origine des produits, à la saisonnalité et à l'art de la table.\n\nAu cœur de cette philosophie se trouve la notion de terroir. Le terroir désigne l'ensemble des conditions naturelles — sol, climat, exposition, altitude — qui confèrent à un produit son caractère unique. Un camembert de Normandie ne ressemble pas à un camembert industriel précisément parce que le terroir normand — ses pâturages humides, ses vaches de race locale, son climat océanique — imprègne le lait d'une saveur impossible à reproduire ailleurs. Le terroir est la raison pour laquelle les Français insistent sur les appellations d'origine : elles protègent non pas une marque, mais un lieu.\n\nCette attention au terroir se prolonge naturellement dans la dégustation. Déguster, en français, ne signifie pas simplement boire ou manger — c'est un acte d'attention. Lors d'une dégustation de vin, on observe la robe, on hume les arômes, on laisse le liquide parcourir le palais avant de juger. C'est un exercice à la fois sensoriel et intellectuel, où chaque gorgée raconte l'histoire d'un millésime — l'année de récolte, avec ses caprices météorologiques, ses gelées tardives ou ses étés caniculaires.\n\nLe millésime est fondamental dans la culture vinicole française. Deux bouteilles du même domaine, du même cépage, peuvent offrir des expériences radicalement différentes selon leur année de production. Un millésime 2003, marqué par la canicule, donnera des vins puissants et concentrés. Un millésime 2013, plus frais et pluvieux, produira des vins plus légers et acidulés. Comprendre les millésimes, c'est comprendre que le vin est un produit vivant, façonné par le temps qu'il fait autant que par la main de l'homme.\n\nDans un restaurant, la personne qui maîtrise cette connaissance est le sommelier. Le sommelier ne se contente pas de servir le vin — il conseille, il éduque, il crée des ponts entre la cuisine et la cave. Son expertise repose sur des années de formation : connaissance des régions viticoles, des cépages, des techniques de vinification, mais aussi capacité à écouter le client et à comprendre ses préférences.\n\nLe travail du sommelier culmine dans l'accord — l'art de marier un plat et un vin pour que chacun magnifie l'autre. Un accord réussi n'est pas une simple compatibilité : c'est une synergie. Le gras d'un foie gras appelle l'acidité d'un sauternes. La salinité d'une huître trouve son écho dans la minéralité d'un muscadet. L'accord parfait transforme un repas en expérience — et c'est précisément ce que la gastronomie française cherche à accomplir à chaque table."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Writing: Philosophy of gastronomy",
                    "description": "Write sentences using the 6 vocabulary words about French gastronomic philosophy.",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord"],
                        "items": [
                            {
                                "prompt": "Use the word 'gastronomie' in a sentence about France's culinary heritage. Example: La gastronomie française a été reconnue par l'UNESCO comme patrimoine culturel immatériel de l'humanité.",
                                "targetVocab": "gastronomie"
                            },
                            {
                                "prompt": "Use the word 'terroir' in a sentence about how geography influences food or wine. Example: Le terroir bourguignon donne aux vins de Pinot Noir une élégance que l'on ne retrouve nulle part ailleurs.",
                                "targetVocab": "terroir"
                            },
                            {
                                "prompt": "Use the word 'dégustation' in a sentence about a wine or food tasting experience. Example: Nous avons participé à une dégustation de fromages affinés dans une cave du Jura.",
                                "targetVocab": "dégustation"
                            },
                            {
                                "prompt": "Use the word 'sommelier' in a sentence about wine service or recommendation. Example: Le sommelier a suggéré un côtes-du-rhône pour accompagner notre agneau grillé.",
                                "targetVocab": "sommelier"
                            },
                            {
                                "prompt": "Use the word 'millésime' in a sentence about wine vintage and quality. Example: Le millésime 2018 est particulièrement réussi en Bourgogne grâce à un été chaud et sec.",
                                "targetVocab": "millésime"
                            },
                            {
                                "prompt": "Use the word 'accord' in a sentence about food and wine pairing. Example: L'accord entre un sauternes et un roquefort est l'un des plus célèbres de la gastronomie française.",
                                "targetVocab": "accord"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Part 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Introduction to Part 2 vocabulary",
                    "description": "Review of Part 1 and introduction to 6 words about dining out in France.",
                    "data": {
                        "text": "Welcome back! In Part 1, you learned six words that form the philosophical backbone of French gastronomy: gastronomie — the art and science of fine eating, terroir — the natural environment that gives food its unique character, dégustation — the ritual of attentive tasting, sommelier — the trained wine professional, millésime — the vintage year of a wine, and accord — the art of food and wine pairing.\n\nNow we move from philosophy to practice — the everyday vocabulary of dining out in France. In Part 2, you'll learn six words: brasserie, ardoise, plat du jour, convive, addition, and pourboire. These are the words you'll actually use when you sit down to eat in a French restaurant.\n\nFirst is brasserie — a feminine noun meaning a type of French restaurant that's less formal than a fine-dining establishment but more substantial than a café. Brasseries typically serve traditional French dishes all day long. Example: 'Cette brasserie parisienne sert des fruits de mer et des plats traditionnels depuis 1880.' In the reading, you'll discover how brasseries became the democratic heart of French dining culture.\n\nNext is ardoise — a feminine noun literally meaning slate or chalkboard. In restaurant context, it refers to the chalkboard menu where daily specials are written. Example: 'Le chef inscrit ses suggestions du jour sur l'ardoise accrochée près de l'entrée.' In our passage, the ardoise represents spontaneity — dishes that change with the market and the chef's inspiration.\n\nThird is plat du jour — a masculine noun phrase meaning dish of the day, the daily special that a restaurant prepares fresh each day based on market availability. Example: 'Le plat du jour est un confit de canard accompagné de pommes sarladaises.' In context, the plat du jour embodies the French commitment to freshness and seasonality in everyday dining.\n\nFourth is convive — a masculine or feminine noun meaning a fellow diner, a guest at the table. It carries a warmth that the English word 'guest' doesn't quite capture — a convive is someone you share the pleasure of eating with. Example: 'Les convives ont levé leur verre pour porter un toast au chef.' In the reading, convive reminds us that French dining is fundamentally a social act.\n\nFifth is addition — a feminine noun meaning the bill or check at a restaurant. Despite looking like the English word 'addition,' in French restaurant context it specifically means the final tally of what you owe. Example: 'Pourriez-vous nous apporter l'addition, s'il vous plaît ?' In our passage, asking for the addition is itself a cultural moment — in France, the waiter never brings it until you ask.\n\nFinally, pourboire — a masculine noun meaning tip or gratuity. The word literally breaks down to 'pour boire' — for drinking — a charming etymology. Example: 'En France, le service est inclus dans l'addition, mais on laisse souvent un petit pourboire pour remercier le serveur.' In the reading, pourboire illustrates how French tipping culture differs dramatically from American customs.\n\nSix practical words for your next French dining experience. Let's practice with flashcards, then read about the art of eating out in France."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Dining out in France",
                    "description": "Learn 6 words: brasserie, ardoise, plat du jour, convive, addition, pourboire",
                    "data": {
                        "vocabList": ["brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Dining out in France",
                    "description": "Learn 6 words: brasserie, ardoise, plat du jour, convive, addition, pourboire",
                    "data": {
                        "vocabList": ["brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Dining out in France",
                    "description": "Learn 6 words: brasserie, ardoise, plat du jour, convive, addition, pourboire",
                    "data": {
                        "vocabList": ["brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Dining out in France",
                    "description": "Learn 6 words: brasserie, ardoise, plat du jour, convive, addition, pourboire",
                    "data": {
                        "vocabList": ["brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Dining out in France",
                    "description": "Learn 6 words: brasserie, ardoise, plat du jour, convive, addition, pourboire",
                    "data": {
                        "vocabList": ["brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Reading: The art of dining out in France",
                    "description": "Manger au restaurant en France est un art qui obéit à ses propres codes.",
                    "data": {
                        "text": "Manger au restaurant en France est un art qui obéit à ses propres codes. Contrairement à d'autres cultures où le repas au restaurant est une simple commodité, les Français considèrent la sortie au restaurant comme un événement social à part entière — un moment de partage, de plaisir et de découverte.\n\nLa brasserie occupe une place particulière dans ce paysage. Née au XIXe siècle avec l'arrivée des brasseurs alsaciens à Paris, la brasserie est devenue le lieu de rendez-vous par excellence des Français pressés qui refusent de sacrifier la qualité. On y mange bien, on y mange vite, et surtout on y mange à toute heure. Les grandes brasseries parisiennes — Lipp, La Coupole, Le Bouillon Chartier — sont des institutions où se croisent ouvriers, artistes, hommes d'affaires et touristes.\n\nEn entrant dans une brasserie, le regard se porte immédiatement sur l'ardoise. Cette planche de bois peinte en noir, accrochée au mur ou posée sur un chevalet, affiche les suggestions du jour à la craie blanche. L'ardoise change quotidiennement, parfois même entre le déjeuner et le dîner, selon les arrivages du marché et l'humeur du chef. C'est le contraire d'un menu figé — c'est une invitation à la spontanéité.\n\nLe plat du jour est souvent le meilleur choix pour qui veut manger frais et bien sans se ruiner. Préparé le matin même avec les produits achetés au marché, il reflète la saison : un pot-au-feu en hiver, une salade de chèvre chaud au printemps, un tartare de thon en été. Commander le plat du jour, c'est faire confiance au chef — et en France, cette confiance est rarement trahie.\n\nAutour de la table, les convives partagent bien plus qu'un repas. Le mot convive vient du latin convivium — vivre ensemble. En France, un déjeuner d'affaires peut durer deux heures, un dîner entre amis trois ou quatre. Les convives discutent, débattent, rient, se resservent du vin. Le repas est un prétexte à la conversation autant qu'un acte de nutrition.\n\nQuand le repas touche à sa fin, il faut demander l'addition. En France, le serveur ne l'apporte jamais de lui-même — ce serait impoli, comme s'il voulait vous chasser. C'est au convive de faire signe, de dire « l'addition, s'il vous plaît » quand il est prêt. Ce détail révèle une philosophie : au restaurant français, le temps vous appartient.\n\nEnfin, la question du pourboire. En France, le service est compris — c'est-à-dire inclus dans les prix affichés. Le serveur reçoit un salaire, et les quinze pour cent de service sont déjà intégrés à l'addition. Pourtant, il est courant de laisser un petit pourboire — quelques euros, jamais un pourcentage calculé — pour remercier un service particulièrement attentionné. Le pourboire français est un geste de gratitude, pas une obligation sociale."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Reading: The art of dining out in France",
                    "description": "Manger au restaurant en France est un art qui obéit à ses propres codes.",
                    "data": {
                        "text": "Manger au restaurant en France est un art qui obéit à ses propres codes. Contrairement à d'autres cultures où le repas au restaurant est une simple commodité, les Français considèrent la sortie au restaurant comme un événement social à part entière — un moment de partage, de plaisir et de découverte.\n\nLa brasserie occupe une place particulière dans ce paysage. Née au XIXe siècle avec l'arrivée des brasseurs alsaciens à Paris, la brasserie est devenue le lieu de rendez-vous par excellence des Français pressés qui refusent de sacrifier la qualité. On y mange bien, on y mange vite, et surtout on y mange à toute heure. Les grandes brasseries parisiennes — Lipp, La Coupole, Le Bouillon Chartier — sont des institutions où se croisent ouvriers, artistes, hommes d'affaires et touristes.\n\nEn entrant dans une brasserie, le regard se porte immédiatement sur l'ardoise. Cette planche de bois peinte en noir, accrochée au mur ou posée sur un chevalet, affiche les suggestions du jour à la craie blanche. L'ardoise change quotidiennement, parfois même entre le déjeuner et le dîner, selon les arrivages du marché et l'humeur du chef. C'est le contraire d'un menu figé — c'est une invitation à la spontanéité.\n\nLe plat du jour est souvent le meilleur choix pour qui veut manger frais et bien sans se ruiner. Préparé le matin même avec les produits achetés au marché, il reflète la saison : un pot-au-feu en hiver, une salade de chèvre chaud au printemps, un tartare de thon en été. Commander le plat du jour, c'est faire confiance au chef — et en France, cette confiance est rarement trahie.\n\nAutour de la table, les convives partagent bien plus qu'un repas. Le mot convive vient du latin convivium — vivre ensemble. En France, un déjeuner d'affaires peut durer deux heures, un dîner entre amis trois ou quatre. Les convives discutent, débattent, rient, se resservent du vin. Le repas est un prétexte à la conversation autant qu'un acte de nutrition.\n\nQuand le repas touche à sa fin, il faut demander l'addition. En France, le serveur ne l'apporte jamais de lui-même — ce serait impoli, comme s'il voulait vous chasser. C'est au convive de faire signe, de dire « l'addition, s'il vous plaît » quand il est prêt. Ce détail révèle une philosophie : au restaurant français, le temps vous appartient.\n\nEnfin, la question du pourboire. En France, le service est compris — c'est-à-dire inclus dans les prix affichés. Le serveur reçoit un salaire, et les quinze pour cent de service sont déjà intégrés à l'addition. Pourtant, il est courant de laisser un petit pourboire — quelques euros, jamais un pourcentage calculé — pour remercier un service particulièrement attentionné. Le pourboire français est un geste de gratitude, pas une obligation sociale."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Listen: The art of dining out in France",
                    "description": "Listen to the passage and follow along.",
                    "data": {
                        "text": "Manger au restaurant en France est un art qui obéit à ses propres codes. Contrairement à d'autres cultures où le repas au restaurant est une simple commodité, les Français considèrent la sortie au restaurant comme un événement social à part entière — un moment de partage, de plaisir et de découverte.\n\nLa brasserie occupe une place particulière dans ce paysage. Née au XIXe siècle avec l'arrivée des brasseurs alsaciens à Paris, la brasserie est devenue le lieu de rendez-vous par excellence des Français pressés qui refusent de sacrifier la qualité. On y mange bien, on y mange vite, et surtout on y mange à toute heure. Les grandes brasseries parisiennes — Lipp, La Coupole, Le Bouillon Chartier — sont des institutions où se croisent ouvriers, artistes, hommes d'affaires et touristes.\n\nEn entrant dans une brasserie, le regard se porte immédiatement sur l'ardoise. Cette planche de bois peinte en noir, accrochée au mur ou posée sur un chevalet, affiche les suggestions du jour à la craie blanche. L'ardoise change quotidiennement, parfois même entre le déjeuner et le dîner, selon les arrivages du marché et l'humeur du chef. C'est le contraire d'un menu figé — c'est une invitation à la spontanéité.\n\nLe plat du jour est souvent le meilleur choix pour qui veut manger frais et bien sans se ruiner. Préparé le matin même avec les produits achetés au marché, il reflète la saison : un pot-au-feu en hiver, une salade de chèvre chaud au printemps, un tartare de thon en été. Commander le plat du jour, c'est faire confiance au chef — et en France, cette confiance est rarement trahie.\n\nAutour de la table, les convives partagent bien plus qu'un repas. Le mot convive vient du latin convivium — vivre ensemble. En France, un déjeuner d'affaires peut durer deux heures, un dîner entre amis trois ou quatre. Les convives discutent, débattent, rient, se resservent du vin. Le repas est un prétexte à la conversation autant qu'un acte de nutrition.\n\nQuand le repas touche à sa fin, il faut demander l'addition. En France, le serveur ne l'apporte jamais de lui-même — ce serait impoli, comme s'il voulait vous chasser. C'est au convive de faire signe, de dire « l'addition, s'il vous plaît » quand il est prêt. Ce détail révèle une philosophie : au restaurant français, le temps vous appartient.\n\nEnfin, la question du pourboire. En France, le service est compris — c'est-à-dire inclus dans les prix affichés. Le serveur reçoit un salaire, et les quinze pour cent de service sont déjà intégrés à l'addition. Pourtant, il est courant de laisser un petit pourboire — quelques euros, jamais un pourcentage calculé — pour remercier un service particulièrement attentionné. Le pourboire français est un geste de gratitude, pas une obligation sociale."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Writing: Dining out in France",
                    "description": "Write sentences using the 6 vocabulary words about French dining culture.",
                    "data": {
                        "vocabList": ["brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire"],
                        "items": [
                            {
                                "prompt": "Use the word 'brasserie' in a sentence about a casual French dining experience. Example: Nous avons déjeuné dans une brasserie du quartier Latin qui sert des plats traditionnels depuis plus de cent ans.",
                                "targetVocab": "brasserie"
                            },
                            {
                                "prompt": "Use the word 'ardoise' in a sentence about a restaurant's daily specials board. Example: Le chef a écrit trois nouveaux plats sur l'ardoise ce matin après sa visite au marché.",
                                "targetVocab": "ardoise"
                            },
                            {
                                "prompt": "Use the phrase 'plat du jour' in a sentence about choosing a daily special. Example: J'ai commandé le plat du jour — un magret de canard aux cerises — et je n'ai pas été déçu.",
                                "targetVocab": "plat du jour"
                            },
                            {
                                "prompt": "Use the word 'convive' in a sentence about sharing a meal with others. Example: Les convives ont applaudi quand le serveur a apporté le plateau de fruits de mer.",
                                "targetVocab": "convive"
                            },
                            {
                                "prompt": "Use the word 'addition' in a sentence about paying at a restaurant. Example: En France, il faut toujours demander l'addition — le serveur ne l'apporte jamais sans qu'on le lui demande.",
                                "targetVocab": "addition"
                            },
                            {
                                "prompt": "Use the word 'pourboire' in a sentence about tipping customs in France. Example: J'ai laissé un pourboire de trois euros parce que le service était vraiment excellent.",
                                "targetVocab": "pourboire"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Part 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Introduction to Part 3 vocabulary",
                    "description": "Review of Parts 1-2 and introduction to 6 words about professional French cuisine.",
                    "data": {
                        "text": "Welcome to Part 3! You've already built a strong foundation. In Part 1, you learned the philosophy — gastronomie, terroir, dégustation, sommelier, millésime, and accord. In Part 2, you mastered the everyday dining vocabulary — brasserie, ardoise, plat du jour, convive, addition, and pourboire. Now we enter the professional kitchen.\n\nIn this final learning session, you'll discover six words from the world of haute cuisine: étoilé, brigade, dressage, amuse-bouche, velouté, and réduction. These terms take you behind the pass and into the language of Michelin-starred restaurants.\n\nFirst is étoilé — an adjective meaning starred, specifically referring to a restaurant that has received one or more Michelin stars. Example: 'Ce restaurant étoilé propose un menu dégustation en sept services.' In the reading, étoilé represents the pinnacle of French culinary achievement — the recognition that transforms a chef's career.\n\nNext is brigade — a feminine noun referring to the kitchen brigade, the hierarchical team structure invented by Auguste Escoffier in the 19th century. Example: 'La brigade de ce restaurant compte vingt cuisiniers, chacun responsable d'un poste précis.' In our passage, brigade illustrates how French professional kitchens operate like military units — disciplined, hierarchical, and precise.\n\nThird is dressage — a masculine noun meaning plating, the art of arranging food on the plate. In haute cuisine, dressage is as important as cooking itself. Example: 'Le dressage de chaque assiette prend plusieurs minutes et requiert une précision chirurgicale.' In context, dressage reveals how French chefs treat the plate as a canvas.\n\nFourth is amuse-bouche — a masculine noun meaning a small complimentary bite served before the meal begins, literally 'mouth amuser.' Example: 'Le chef nous a envoyé un amuse-bouche — une cuillère de gaspacho à la framboise.' In the reading, the amuse-bouche is the chef's calling card — a tiny creation that sets the tone for everything that follows.\n\nFifth is velouté — a masculine noun meaning a smooth, velvety soup or sauce, one of the five French mother sauces. Example: 'Ce velouté de champignons est d'une onctuosité remarquable grâce à l'ajout de crème fraîche.' In our passage, velouté represents the French obsession with texture — food must not only taste good but feel perfect in the mouth.\n\nFinally, réduction — a feminine noun meaning reduction, the technique of simmering a liquid to concentrate its flavors. Example: 'La réduction de vin rouge et d'échalotes accompagne parfaitement l'entrecôte grillée.' In the reading, réduction embodies a core principle of French cooking — patience transforms simple ingredients into something extraordinary.\n\nSix words from the professional kitchen. Let's practice with flashcards, then read about what happens behind the scenes in a Michelin-starred restaurant."
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Professional French cuisine",
                    "description": "Learn 6 words: étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Professional French cuisine",
                    "description": "Learn 6 words: étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Professional French cuisine",
                    "description": "Learn 6 words: étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Professional French cuisine",
                    "description": "Learn 6 words: étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Professional French cuisine",
                    "description": "Learn 6 words: étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Reading: Inside a Michelin-starred kitchen",
                    "description": "Derrière les portes battantes d'un restaurant étoilé se cache un monde de précision.",
                    "data": {
                        "text": "Derrière les portes battantes d'un restaurant étoilé se cache un monde de précision absolue. Ici, chaque geste est calculé, chaque seconde compte, et la moindre erreur peut ruiner un service entier. Bienvenue dans l'univers de la haute cuisine française.\n\nUn restaurant étoilé — c'est-à-dire distingué par le Guide Michelin — fonctionne selon des standards que peu d'établissements peuvent atteindre. Une étoile signifie « une très bonne table », deux étoiles « une cuisine excellente », trois étoiles « une cuisine exceptionnelle qui vaut le voyage ». En France, obtenir une étoile transforme la vie d'un chef : la réservation se remplit des mois à l'avance, les critiques affluent, et la pression de maintenir ce niveau devient quotidienne.\n\nLe moteur de cette machine est la brigade de cuisine. Inventée par Auguste Escoffier à la fin du XIXe siècle, la brigade organise la cuisine comme une armée. Au sommet, le chef de cuisine dirige l'ensemble. Sous lui, le sous-chef coordonne les différents postes. Chaque poste — saucier, poissonnier, rôtisseur, pâtissier, garde-manger — est tenu par un chef de partie assisté de commis. Cette hiérarchie permet de servir cinquante couverts simultanément avec une régularité parfaite.\n\nLe service commence bien avant l'arrivée des clients. Dès le matin, la brigade prépare les fonds, les sauces de base, les garnitures. Parmi les techniques fondamentales, la réduction occupe une place centrale. Réduire, c'est faire évaporer lentement un liquide — vin, bouillon, jus de viande — pour concentrer ses saveurs. Une réduction de porto et d'échalotes, par exemple, peut transformer une simple pièce de bœuf en plat gastronomique. La patience est la clé : une bonne réduction demande parfois des heures de cuisson douce.\n\nQuand les clients s'installent, le premier contact avec la cuisine est l'amuse-bouche — une bouchée offerte par le chef, hors menu, qui annonce le style et la philosophie du repas à venir. Un amuse-bouche réussi surprend, éveille les papilles et crée l'anticipation. Il peut s'agir d'une cuillère de velouté glacé, d'un macaron salé au foie gras, ou d'une huître accompagnée d'une gelée de concombre.\n\nLe velouté lui-même est un pilier de la cuisine française classique. Cette préparation — un mélange de légumes cuits, mixés et passés au tamis, enrichi de crème ou de beurre — incarne l'obsession française pour la texture. Un velouté parfait doit être d'une onctuosité absolue, sans le moindre grumeau, avec une consistance qui nappe la cuillère sans être lourde.\n\nMais dans un restaurant étoilé, le goût ne suffit pas. Le dressage — l'art de disposer les éléments sur l'assiette — est devenu une discipline à part entière. Chaque point de sauce est placé à la pince, chaque herbe positionnée avec une précision millimétrique, chaque élément pensé pour créer un équilibre visuel. Le dressage moderne s'inspire de l'art contemporain : asymétrie maîtrisée, jeux de hauteur, contrastes de couleurs. Une assiette bien dressée raconte une histoire avant même que la première bouchée ne soit prise."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Reading: Inside a Michelin-starred kitchen",
                    "description": "Derrière les portes battantes d'un restaurant étoilé se cache un monde de précision.",
                    "data": {
                        "text": "Derrière les portes battantes d'un restaurant étoilé se cache un monde de précision absolue. Ici, chaque geste est calculé, chaque seconde compte, et la moindre erreur peut ruiner un service entier. Bienvenue dans l'univers de la haute cuisine française.\n\nUn restaurant étoilé — c'est-à-dire distingué par le Guide Michelin — fonctionne selon des standards que peu d'établissements peuvent atteindre. Une étoile signifie « une très bonne table », deux étoiles « une cuisine excellente », trois étoiles « une cuisine exceptionnelle qui vaut le voyage ». En France, obtenir une étoile transforme la vie d'un chef : la réservation se remplit des mois à l'avance, les critiques affluent, et la pression de maintenir ce niveau devient quotidienne.\n\nLe moteur de cette machine est la brigade de cuisine. Inventée par Auguste Escoffier à la fin du XIXe siècle, la brigade organise la cuisine comme une armée. Au sommet, le chef de cuisine dirige l'ensemble. Sous lui, le sous-chef coordonne les différents postes. Chaque poste — saucier, poissonnier, rôtisseur, pâtissier, garde-manger — est tenu par un chef de partie assisté de commis. Cette hiérarchie permet de servir cinquante couverts simultanément avec une régularité parfaite.\n\nLe service commence bien avant l'arrivée des clients. Dès le matin, la brigade prépare les fonds, les sauces de base, les garnitures. Parmi les techniques fondamentales, la réduction occupe une place centrale. Réduire, c'est faire évaporer lentement un liquide — vin, bouillon, jus de viande — pour concentrer ses saveurs. Une réduction de porto et d'échalotes, par exemple, peut transformer une simple pièce de bœuf en plat gastronomique. La patience est la clé : une bonne réduction demande parfois des heures de cuisson douce.\n\nQuand les clients s'installent, le premier contact avec la cuisine est l'amuse-bouche — une bouchée offerte par le chef, hors menu, qui annonce le style et la philosophie du repas à venir. Un amuse-bouche réussi surprend, éveille les papilles et crée l'anticipation. Il peut s'agir d'une cuillère de velouté glacé, d'un macaron salé au foie gras, ou d'une huître accompagnée d'une gelée de concombre.\n\nLe velouté lui-même est un pilier de la cuisine française classique. Cette préparation — un mélange de légumes cuits, mixés et passés au tamis, enrichi de crème ou de beurre — incarne l'obsession française pour la texture. Un velouté parfait doit être d'une onctuosité absolue, sans le moindre grumeau, avec une consistance qui nappe la cuillère sans être lourde.\n\nMais dans un restaurant étoilé, le goût ne suffit pas. Le dressage — l'art de disposer les éléments sur l'assiette — est devenu une discipline à part entière. Chaque point de sauce est placé à la pince, chaque herbe positionnée avec une précision millimétrique, chaque élément pensé pour créer un équilibre visuel. Le dressage moderne s'inspire de l'art contemporain : asymétrie maîtrisée, jeux de hauteur, contrastes de couleurs. Une assiette bien dressée raconte une histoire avant même que la première bouchée ne soit prise."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Listen: Inside a Michelin-starred kitchen",
                    "description": "Listen to the passage and follow along.",
                    "data": {
                        "text": "Derrière les portes battantes d'un restaurant étoilé se cache un monde de précision absolue. Ici, chaque geste est calculé, chaque seconde compte, et la moindre erreur peut ruiner un service entier. Bienvenue dans l'univers de la haute cuisine française.\n\nUn restaurant étoilé — c'est-à-dire distingué par le Guide Michelin — fonctionne selon des standards que peu d'établissements peuvent atteindre. Une étoile signifie « une très bonne table », deux étoiles « une cuisine excellente », trois étoiles « une cuisine exceptionnelle qui vaut le voyage ». En France, obtenir une étoile transforme la vie d'un chef : la réservation se remplit des mois à l'avance, les critiques affluent, et la pression de maintenir ce niveau devient quotidienne.\n\nLe moteur de cette machine est la brigade de cuisine. Inventée par Auguste Escoffier à la fin du XIXe siècle, la brigade organise la cuisine comme une armée. Au sommet, le chef de cuisine dirige l'ensemble. Sous lui, le sous-chef coordonne les différents postes. Chaque poste — saucier, poissonnier, rôtisseur, pâtissier, garde-manger — est tenu par un chef de partie assisté de commis. Cette hiérarchie permet de servir cinquante couverts simultanément avec une régularité parfaite.\n\nLe service commence bien avant l'arrivée des clients. Dès le matin, la brigade prépare les fonds, les sauces de base, les garnitures. Parmi les techniques fondamentales, la réduction occupe une place centrale. Réduire, c'est faire évaporer lentement un liquide — vin, bouillon, jus de viande — pour concentrer ses saveurs. Une réduction de porto et d'échalotes, par exemple, peut transformer une simple pièce de bœuf en plat gastronomique. La patience est la clé : une bonne réduction demande parfois des heures de cuisson douce.\n\nQuand les clients s'installent, le premier contact avec la cuisine est l'amuse-bouche — une bouchée offerte par le chef, hors menu, qui annonce le style et la philosophie du repas à venir. Un amuse-bouche réussi surprend, éveille les papilles et crée l'anticipation. Il peut s'agir d'une cuillère de velouté glacé, d'un macaron salé au foie gras, ou d'une huître accompagnée d'une gelée de concombre.\n\nLe velouté lui-même est un pilier de la cuisine française classique. Cette préparation — un mélange de légumes cuits, mixés et passés au tamis, enrichi de crème ou de beurre — incarne l'obsession française pour la texture. Un velouté parfait doit être d'une onctuosité absolue, sans le moindre grumeau, avec une consistance qui nappe la cuillère sans être lourde.\n\nMais dans un restaurant étoilé, le goût ne suffit pas. Le dressage — l'art de disposer les éléments sur l'assiette — est devenu une discipline à part entière. Chaque point de sauce est placé à la pince, chaque herbe positionnée avec une précision millimétrique, chaque élément pensé pour créer un équilibre visuel. Le dressage moderne s'inspire de l'art contemporain : asymétrie maîtrisée, jeux de hauteur, contrastes de couleurs. Une assiette bien dressée raconte une histoire avant même que la première bouchée ne soit prise."
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Writing: Professional French cuisine",
                    "description": "Write sentences using the 6 vocabulary words about haute cuisine.",
                    "data": {
                        "vocabList": ["étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"],
                        "items": [
                            {
                                "prompt": "Use the word 'étoilé' in a sentence about a Michelin-starred restaurant. Example: Nous avons fêté notre anniversaire dans un restaurant étoilé qui propose un menu dégustation en neuf services.",
                                "targetVocab": "étoilé"
                            },
                            {
                                "prompt": "Use the word 'brigade' in a sentence about kitchen organization. Example: La brigade de ce restaurant travaille en silence, chaque cuisinier concentré sur son poste.",
                                "targetVocab": "brigade"
                            },
                            {
                                "prompt": "Use the word 'dressage' in a sentence about food presentation. Example: Le dressage de ce plat est si beau qu'on hésite à y toucher.",
                                "targetVocab": "dressage"
                            },
                            {
                                "prompt": "Use the phrase 'amuse-bouche' in a sentence about a pre-meal bite. Example: L'amuse-bouche du soir était une mousse de betterave sur un croustillant de parmesan.",
                                "targetVocab": "amuse-bouche"
                            },
                            {
                                "prompt": "Use the word 'velouté' in a sentence about a smooth soup or sauce. Example: Ce velouté de potimarron est parfait pour les soirées d'automne.",
                                "targetVocab": "velouté"
                            },
                            {
                                "prompt": "Use the word 'réduction' in a sentence about a cooking technique. Example: La réduction de balsamique apporte une touche sucrée-acidulée à cette salade de fraises.",
                                "targetVocab": "réduction"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "title": "Review",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Review introduction",
                    "description": "Overview of all 18 vocabulary words and what the review session covers.",
                    "data": {
                        "text": "Congratulations — you've learned all 18 vocabulary words across three sessions! Let's take a moment to appreciate how far you've come. You started with the philosophy of French gastronomy — gastronomie, terroir, dégustation, sommelier, millésime, and accord. Then you moved to the practical world of dining out — brasserie, ardoise, plat du jour, convive, addition, and pourboire. And finally, you entered the professional kitchen — étoilé, brigade, dressage, amuse-bouche, velouté, and réduction.\n\nTogether, these 18 words give you the vocabulary to discuss French food culture from every angle — from the philosophical foundations to the everyday experience to the professional heights. In this review session, you'll practice all 18 words together and read a comprehensive passage that weaves them all into a single narrative about a memorable evening at a French restaurant. Let's begin!"
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Complete gastronomy vocabulary",
                    "description": "Review all 18 words: gastronomie, terroir, dégustation, sommelier, millésime, accord, brasserie, ardoise, plat du jour, convive, addition, pourboire, étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord", "brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire", "étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Complete gastronomy vocabulary",
                    "description": "Review all 18 words: gastronomie, terroir, dégustation, sommelier, millésime, accord, brasserie, ardoise, plat du jour, convive, addition, pourboire, étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord", "brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire", "étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Complete gastronomy vocabulary",
                    "description": "Review all 18 words: gastronomie, terroir, dégustation, sommelier, millésime, accord, brasserie, ardoise, plat du jour, convive, addition, pourboire, étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord", "brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire", "étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Complete gastronomy vocabulary",
                    "description": "Review all 18 words: gastronomie, terroir, dégustation, sommelier, millésime, accord, brasserie, ardoise, plat du jour, convive, addition, pourboire, étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord", "brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire", "étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Complete gastronomy vocabulary",
                    "description": "Review all 18 words: gastronomie, terroir, dégustation, sommelier, millésime, accord, brasserie, ardoise, plat du jour, convive, addition, pourboire, étoilé, brigade, dressage, amuse-bouche, velouté, réduction",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord", "brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire", "étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"]
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Reading: A complete French dining experience",
                    "description": "Il est vingt heures quand nous poussons la porte du restaurant.",
                    "data": {
                        "text": "Il est vingt heures quand nous poussons la porte du restaurant. Ce n'est pas une simple brasserie de quartier — c'est un établissement étoilé, une table que l'on réserve trois mois à l'avance. Mes convives et moi avons choisi ce lieu pour célébrer un anniversaire, et l'excitation est palpable.\n\nLe maître d'hôtel nous installe à une table ronde près de la fenêtre. Pas d'ardoise ici — le menu est un livret élégant, calligraphié à la main, qui change chaque saison. Le sommelier s'approche avec la carte des vins, un volume impressionnant qui couvre toutes les régions de France. Il nous interroge sur nos préférences, écoute attentivement, puis suggère un millésime 2017 de la vallée de la Loire — un chenin blanc qui, selon lui, créera un accord parfait avec le menu du soir.\n\nAvant même que nous ayons commandé, un amuse-bouche arrive — une cuillère de velouté de petits pois à la menthe, surmonté d'une mousse de chèvre frais. C'est une explosion de fraîcheur qui éveille immédiatement les papilles. Le dressage est impeccable : la cuillère en porcelaine blanche, le vert intense du velouté, le blanc crémeux de la mousse. On comprend instantanément que la brigade derrière ces portes battantes maîtrise son art.\n\nLe repas se déroule comme une symphonie en sept mouvements. Chaque plat raconte une histoire de terroir — les légumes viennent d'un potager à vingt kilomètres, le poisson a été pêché ce matin en Bretagne, l'agneau est élevé sur les causses du Larzac. La gastronomie française prend ici tout son sens : ce n'est pas simplement de la bonne cuisine, c'est une célébration du lieu, de la saison, du producteur.\n\nLe sommelier revient entre chaque plat pour proposer un accord différent. Un verre de bourgogne blanc avec le turbot, un rouge de Bandol avec l'agneau, un jurançon moelleux avec le dessert. Chaque accord est une dégustation en soi — on goûte le vin seul, puis avec le plat, et la transformation est magique. Les saveurs se répondent, se complètent, s'amplifient.\n\nLa réduction qui accompagne le plat principal — un jus d'agneau réduit pendant six heures avec du thym et de l'ail confit — est d'une intensité remarquable. Quelques gouttes suffisent pour transformer chaque bouchée. C'est le genre de préparation qui demande une patience infinie et une technique irréprochable — la signature d'une brigade qui ne fait aucun compromis.\n\nTrois heures plus tard, repus et heureux, nous demandons l'addition. Le montant est conséquent, mais aucun de mes convives ne sourcille — l'expérience valait chaque euro. Nous laissons un pourboire généreux, non par obligation mais par gratitude sincère. En sortant dans la nuit parisienne, je réalise que ce repas n'était pas simplement un dîner — c'était une leçon de gastronomie vivante."
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Reading: A complete French dining experience",
                    "description": "Il est vingt heures quand nous poussons la porte du restaurant.",
                    "data": {
                        "text": "Il est vingt heures quand nous poussons la porte du restaurant. Ce n'est pas une simple brasserie de quartier — c'est un établissement étoilé, une table que l'on réserve trois mois à l'avance. Mes convives et moi avons choisi ce lieu pour célébrer un anniversaire, et l'excitation est palpable.\n\nLe maître d'hôtel nous installe à une table ronde près de la fenêtre. Pas d'ardoise ici — le menu est un livret élégant, calligraphié à la main, qui change chaque saison. Le sommelier s'approche avec la carte des vins, un volume impressionnant qui couvre toutes les régions de France. Il nous interroge sur nos préférences, écoute attentivement, puis suggère un millésime 2017 de la vallée de la Loire — un chenin blanc qui, selon lui, créera un accord parfait avec le menu du soir.\n\nAvant même que nous ayons commandé, un amuse-bouche arrive — une cuillère de velouté de petits pois à la menthe, surmonté d'une mousse de chèvre frais. C'est une explosion de fraîcheur qui éveille immédiatement les papilles. Le dressage est impeccable : la cuillère en porcelaine blanche, le vert intense du velouté, le blanc crémeux de la mousse. On comprend instantanément que la brigade derrière ces portes battantes maîtrise son art.\n\nLe repas se déroule comme une symphonie en sept mouvements. Chaque plat raconte une histoire de terroir — les légumes viennent d'un potager à vingt kilomètres, le poisson a été pêché ce matin en Bretagne, l'agneau est élevé sur les causses du Larzac. La gastronomie française prend ici tout son sens : ce n'est pas simplement de la bonne cuisine, c'est une célébration du lieu, de la saison, du producteur.\n\nLe sommelier revient entre chaque plat pour proposer un accord différent. Un verre de bourgogne blanc avec le turbot, un rouge de Bandol avec l'agneau, un jurançon moelleux avec le dessert. Chaque accord est une dégustation en soi — on goûte le vin seul, puis avec le plat, et la transformation est magique. Les saveurs se répondent, se complètent, s'amplifient.\n\nLa réduction qui accompagne le plat principal — un jus d'agneau réduit pendant six heures avec du thym et de l'ail confit — est d'une intensité remarquable. Quelques gouttes suffisent pour transformer chaque bouchée. C'est le genre de préparation qui demande une patience infinie et une technique irréprochable — la signature d'une brigade qui ne fait aucun compromis.\n\nTrois heures plus tard, repus et heureux, nous demandons l'addition. Le montant est conséquent, mais aucun de mes convives ne sourcille — l'expérience valait chaque euro. Nous laissons un pourboire généreux, non par obligation mais par gratitude sincère. En sortant dans la nuit parisienne, je réalise que ce repas n'était pas simplement un dîner — c'était une leçon de gastronomie vivante."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Listen: A complete French dining experience",
                    "description": "Listen to the passage and follow along.",
                    "data": {
                        "text": "Il est vingt heures quand nous poussons la porte du restaurant. Ce n'est pas une simple brasserie de quartier — c'est un établissement étoilé, une table que l'on réserve trois mois à l'avance. Mes convives et moi avons choisi ce lieu pour célébrer un anniversaire, et l'excitation est palpable.\n\nLe maître d'hôtel nous installe à une table ronde près de la fenêtre. Pas d'ardoise ici — le menu est un livret élégant, calligraphié à la main, qui change chaque saison. Le sommelier s'approche avec la carte des vins, un volume impressionnant qui couvre toutes les régions de France. Il nous interroge sur nos préférences, écoute attentivement, puis suggère un millésime 2017 de la vallée de la Loire — un chenin blanc qui, selon lui, créera un accord parfait avec le menu du soir.\n\nAvant même que nous ayons commandé, un amuse-bouche arrive — une cuillère de velouté de petits pois à la menthe, surmonté d'une mousse de chèvre frais. C'est une explosion de fraîcheur qui éveille immédiatement les papilles. Le dressage est impeccable : la cuillère en porcelaine blanche, le vert intense du velouté, le blanc crémeux de la mousse. On comprend instantanément que la brigade derrière ces portes battantes maîtrise son art.\n\nLe repas se déroule comme une symphonie en sept mouvements. Chaque plat raconte une histoire de terroir — les légumes viennent d'un potager à vingt kilomètres, le poisson a été pêché ce matin en Bretagne, l'agneau est élevé sur les causses du Larzac. La gastronomie française prend ici tout son sens : ce n'est pas simplement de la bonne cuisine, c'est une célébration du lieu, de la saison, du producteur.\n\nLe sommelier revient entre chaque plat pour proposer un accord différent. Un verre de bourgogne blanc avec le turbot, un rouge de Bandol avec l'agneau, un jurançon moelleux avec le dessert. Chaque accord est une dégustation en soi — on goûte le vin seul, puis avec le plat, et la transformation est magique. Les saveurs se répondent, se complètent, s'amplifient.\n\nLa réduction qui accompagne le plat principal — un jus d'agneau réduit pendant six heures avec du thym et de l'ail confit — est d'une intensité remarquable. Quelques gouttes suffisent pour transformer chaque bouchée. C'est le genre de préparation qui demande une patience infinie et une technique irréprochable — la signature d'une brigade qui ne fait aucun compromis.\n\nTrois heures plus tard, repus et heureux, nous demandons l'addition. Le montant est conséquent, mais aucun de mes convives ne sourcille — l'expérience valait chaque euro. Nous laissons un pourboire généreux, non par obligation mais par gratitude sincère. En sortant dans la nuit parisienne, je réalise que ce repas n'était pas simplement un dîner — c'était une leçon de gastronomie vivante."
                    }
                }
            ]
        },
        {
            "title": "Final Reading",
            "activities": [
                {
                    "activityType": "reading",
                    "title": "Reading: The soul of French gastronomy",
                    "description": "La gastronomie française ne se résume pas à une collection de recettes.",
                    "data": {
                        "text": "La gastronomie française ne se résume pas à une collection de recettes — c'est une philosophie de vie qui touche à l'identité même du pays. Depuis que l'UNESCO a inscrit le repas gastronomique des Français au patrimoine culturel immatériel de l'humanité en 2010, le monde entier reconnaît ce que les Français savent depuis des siècles : manger ensemble est un acte de civilisation.\n\nCette philosophie commence par le terroir. Chaque région de France possède ses produits emblématiques, façonnés par des siècles d'interaction entre l'homme et son environnement. Le comté du Jura, le sel de Guérande, l'huile d'olive de Nyons, le piment d'Espelette — chacun raconte l'histoire d'un lieu. Quand un chef choisit ses ingrédients, il ne cherche pas simplement la qualité — il cherche l'authenticité d'un terroir.\n\nDans les restaurants étoilés, cette quête d'authenticité atteint son paroxysme. La brigade travaille des heures avant le service pour préparer les fonds, les réductions, les garnitures. Chaque velouté est passé trois fois au tamis pour atteindre la texture parfaite. Chaque amuse-bouche est conçu comme une œuvre miniature — un concentré de saveurs et de technique qui annonce la philosophie du chef. Le dressage transforme chaque assiette en tableau, où couleurs, textures et volumes dialoguent.\n\nMais la gastronomie française ne vit pas uniquement dans les temples étoilés. Elle respire aussi dans les brasseries de quartier, où l'ardoise du jour propose un plat du jour préparé avec les produits du marché. Elle vit dans les caves où un sommelier passionné guide une dégustation, expliquant comment tel millésime a été marqué par un été caniculaire ou un automne pluvieux. Elle vit dans l'accord parfait entre un fromage de chèvre et un verre de sancerre.\n\nLe repas français est avant tout un acte social. Les convives ne viennent pas simplement se nourrir — ils viennent partager du temps, des histoires, des émotions. Le rythme du repas est lent par choix : on savoure, on discute, on laisse les plats se succéder sans précipitation. Quand enfin l'addition arrive — toujours sur demande, jamais imposée — et qu'un pourboire discret est laissé sur la table, le repas ne se termine pas vraiment. Il continue dans la mémoire, dans la conversation du lendemain, dans l'envie de revenir.\n\nVoilà ce que la gastronomie française enseigne au monde : manger n'est pas un besoin à satisfaire — c'est un art à cultiver."
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Listen: The soul of French gastronomy",
                    "description": "Listen to the final passage and follow along.",
                    "data": {
                        "text": "La gastronomie française ne se résume pas à une collection de recettes — c'est une philosophie de vie qui touche à l'identité même du pays. Depuis que l'UNESCO a inscrit le repas gastronomique des Français au patrimoine culturel immatériel de l'humanité en 2010, le monde entier reconnaît ce que les Français savent depuis des siècles : manger ensemble est un acte de civilisation.\n\nCette philosophie commence par le terroir. Chaque région de France possède ses produits emblématiques, façonnés par des siècles d'interaction entre l'homme et son environnement. Le comté du Jura, le sel de Guérande, l'huile d'olive de Nyons, le piment d'Espelette — chacun raconte l'histoire d'un lieu. Quand un chef choisit ses ingrédients, il ne cherche pas simplement la qualité — il cherche l'authenticité d'un terroir.\n\nDans les restaurants étoilés, cette quête d'authenticité atteint son paroxysme. La brigade travaille des heures avant le service pour préparer les fonds, les réductions, les garnitures. Chaque velouté est passé trois fois au tamis pour atteindre la texture parfaite. Chaque amuse-bouche est conçu comme une œuvre miniature — un concentré de saveurs et de technique qui annonce la philosophie du chef. Le dressage transforme chaque assiette en tableau, où couleurs, textures et volumes dialoguent.\n\nMais la gastronomie française ne vit pas uniquement dans les temples étoilés. Elle respire aussi dans les brasseries de quartier, où l'ardoise du jour propose un plat du jour préparé avec les produits du marché. Elle vit dans les caves où un sommelier passionné guide une dégustation, expliquant comment tel millésime a été marqué par un été caniculaire ou un automne pluvieux. Elle vit dans l'accord parfait entre un fromage de chèvre et un verre de sancerre.\n\nLe repas français est avant tout un acte social. Les convives ne viennent pas simplement se nourrir — ils viennent partager du temps, des histoires, des émotions. Le rythme du repas est lent par choix : on savoure, on discute, on laisse les plats se succéder sans précipitation. Quand enfin l'addition arrive — toujours sur demande, jamais imposée — et qu'un pourboire discret est laissé sur la table, le repas ne se termine pas vraiment. Il continue dans la mémoire, dans la conversation du lendemain, dans l'envie de revenir.\n\nVoilà ce que la gastronomie française enseigne au monde : manger n'est pas un besoin à satisfaire — c'est un art à cultiver."
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Writing: French gastronomy reflection",
                    "description": "Write a paragraph using vocabulary from all three sessions about French food culture.",
                    "data": {
                        "vocabList": ["gastronomie", "terroir", "dégustation", "sommelier", "millésime", "accord", "brasserie", "ardoise", "plat du jour", "convive", "addition", "pourboire", "étoilé", "brigade", "dressage", "amuse-bouche", "velouté", "réduction"],
                        "instructions": "Write a paragraph in French describing your ideal French dining experience. Include details about the type of restaurant, the food, the wine, and the social atmosphere. Try to use at least 6 of the vocabulary words you've learned.",
                        "prompts": [
                            "Describe a memorable meal at a French restaurant — what kind of establishment was it, what did you eat, and who were you with?",
                            "Compare the experience of eating at a neighborhood brasserie versus a restaurant étoilé. What are the differences in atmosphere, service, and food?",
                            "Explain why French gastronomy is considered a cultural heritage. How do concepts like terroir, accord, and dégustation reflect French values?"
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Farewell",
                    "description": "Final review of all vocabulary and warm closing.",
                    "data": {
                        "text": "You've completed French Gastronomy — and I want to challenge you to do something with what you've learned. Not tomorrow, not next week, but soon. Here's what I mean.\n\nYou now own 18 words that most English speakers never learn, and each one is a key to a deeper experience of French culture. Let me walk through them one more time, because knowing a word and using a word are two different things.\n\nGastronomie — the art and science of fine eating. Next time someone says French food is 'just fancy cooking,' you can explain that gastronomie is a UNESCO-recognized cultural heritage — it's philosophy on a plate.\n\nTerroir — the natural environment that gives food its unique character. When you buy a bottle of wine, look for the terroir on the label. Ask yourself: what does this place taste like?\n\nDégustation — the ritual of attentive tasting. Don't just drink your next glass of wine — dégustez-le. Observe the color, smell the aromas, let it sit on your palate.\n\nSommelier — the trained wine professional. Next time you're in a French restaurant, don't be afraid to ask the sommelier for advice. That's literally what they're there for.\n\nMillésime — the vintage year. Start noticing millésimes on wine bottles. A great millésime in Bordeaux might be average in Burgundy — context matters.\n\nAccord — the art of food and wine pairing. Try creating your own accords at home. A simple goat cheese with a glass of Sancerre is a classic starting point.\n\nBrasserie — the democratic heart of French dining. Find a brasserie next time you're in a French city. Skip the tourist restaurants and eat where the locals eat.\n\nArdoise — the chalkboard menu. When you see an ardoise, order from it. It means the chef is cooking with today's market — that's always the freshest option.\n\nPlat du jour — the daily special. Trust the plat du jour. It's the chef's best work that day.\n\nConvive — a fellow diner, someone you share the pleasure of eating with. Remember that eating in France is a social act. Invite convives to your table.\n\nAddition — the bill. In France, you ask for it when you're ready. The table is yours — take your time.\n\nPourboire — the tip. A few euros left with genuine gratitude. Not a percentage — a gesture.\n\nÉtoilé — Michelin-starred. If you ever get the chance to eat at a restaurant étoilé, take it. It's not about the money — it's about witnessing mastery.\n\nBrigade — the kitchen team. Behind every great meal is a brigade working in perfect coordination. Respect the craft.\n\nDressage — the art of plating. Start noticing how food is presented. A well-dressed plate tells you the chef cares about beauty, not just taste.\n\nAmuse-bouche — the complimentary pre-meal bite. It's the chef's handshake — pay attention to it.\n\nVelouté — a smooth, velvety soup or sauce. Try making one at home. The secret is patience and a good blender.\n\nRéduction — the technique of concentrating flavors through slow simmering. Like so much in French cooking, réduction teaches patience. Good things take time.\n\nNow here's my challenge: within the next month, use at least five of these words in a real conversation — whether you're ordering at a restaurant, discussing food with a friend, or reading a French menu. Language lives when you use it. Au revoir, and bon appétit!"
                    }
                }
            ]
        }
    ]
}

# --- Validate and execute ---
validate(content, level="standard")
logger.info("✅ Content validated successfully")

curriculum_id = create_curriculum(content, language="fr", user_language="en")
add_to_series(SERIES_ID, curriculum_id)
set_display_order(curriculum_id, DISPLAY_ORDER)
set_price(curriculum_id, 49)

print(f"✅ Created 'French Gastronomy' -> {curriculum_id}")
print(f"   Series: {SERIES_ID}, displayOrder: {DISPLAY_ORDER}, price: 49")
