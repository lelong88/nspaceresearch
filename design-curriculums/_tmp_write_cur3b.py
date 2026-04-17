#!/usr/bin/env python3
"""Write curriculum 3 sessions, review, final."""

content = '''    "sessions": [
        {
            "label": "C\u1EA5u tr\u00FAc \u0111\u00F4 th\u1ECB",
            "intro_desc": "L\u00E0m quen v\u1EDBi 6 t\u1EEB v\u1EF1ng c\u01A1 b\u1EA3n v\u1EC1 quy ho\u1EA1ch \u0111\u00F4 th\u1ECB b\u1EB1ng ti\u1EBFng Ph\u00E1p.",
            "intro_text": (
                "Ch\u00E0o m\u1EEBng b\u1EA1n \u0111\u1EBFn v\u1EDBi b\u00E0i h\u1ECDc v\u1EC1 quy ho\u1EA1ch \u0111\u00F4 th\u1ECB b\u1EB1ng ti\u1EBFng Ph\u00E1p. "
                "Ph\u00E1p c\u00F3 truy\u1EC1n th\u1ED1ng quy ho\u1EA1ch \u0111\u00F4 th\u1ECB l\u00E2u \u0111\u1EDDi \u2014 t\u1EEB nh\u1EEFng \u0111\u1EA1i l\u1ED9 Haussmann "
                "th\u1EBF k\u1EF7 m\u01B0\u1EDDi ch\u00EDn \u0111\u1EBFn c\u00E1c d\u1EF1 \u00E1n th\u00E0nh ph\u1ED1 th\u00F4ng minh hi\u1EC7n \u0111\u1EA1i. "
                "N\u1EBFu b\u1EA1n mu\u1ED1n hi\u1EC3u c\u00E1ch th\u00E0nh ph\u1ED1 v\u1EADn h\u00E0nh, \u0111\u00E2y l\u00E0 b\u01B0\u1EDBc \u0111\u1EA7u ti\u00EAn.\\n\\n"
                "Trong ph\u1EA7n n\u00E0y, b\u1EA1n s\u1EBD h\u1ECDc 6 t\u1EEB v\u1EF1ng n\u1EC1n t\u1EA3ng: urbanisme, quartier, boulevard, pi\u00E9ton, densit\u00E9, v\u00E0 zonage.\\n\\n"
                "T\u1EEB \u0111\u1EA7u ti\u00EAn l\u00E0 urbanisme \u2014 danh t\u1EEB gi\u1ED1ng \u0111\u1EF1c \u2014 ngh\u0129a l\u00E0 quy ho\u1EA1ch \u0111\u00F4 th\u1ECB. "
                "Urbanisme l\u00E0 khoa h\u1ECDc v\u00E0 ngh\u1EC7 thu\u1EADt t\u1ED5 ch\u1EE9c kh\u00F4ng gian th\u00E0nh ph\u1ED1. "
                "V\u00ED d\u1EE5: \u2018L\u2019urbanisme moderne cherche \u00E0 concilier d\u00E9veloppement \u00E9conomique et qualit\u00E9 de vie des habitants.\u2019 "
                "\u2014 Quy ho\u1EA1ch \u0111\u00F4 th\u1ECB hi\u1EC7n \u0111\u1EA1i t\u00ECm c\u00E1ch h\u00F2a h\u1EE3p ph\u00E1t tri\u1EC3n kinh t\u1EBF v\u00E0 ch\u1EA5t l\u01B0\u1EE3ng s\u1ED1ng c\u1EE7a c\u01B0 d\u00E2n.\\n\\n"
                "T\u1EEB th\u1EE9 hai l\u00E0 quartier \u2014 danh t\u1EEB gi\u1ED1ng \u0111\u1EF1c \u2014 ngh\u0129a l\u00E0 khu ph\u1ED1, qu\u1EADn. "
                "Quartier l\u00E0 \u0111\u01A1n v\u1ECB kh\u00F4ng gian c\u01A1 b\u1EA3n c\u1EE7a th\u00E0nh ph\u1ED1, n\u01A1i c\u01B0 d\u00E2n sinh s\u1ED1ng v\u00E0 giao ti\u1EBFp. "
                "V\u00ED d\u1EE5: \u2018Le quartier du Marais \u00E0 Paris a \u00E9t\u00E9 transform\u00E9 d\u2019un quartier populaire en un lieu branch\u00E9 et touristique.\u2019 "
                "\u2014 Khu ph\u1ED1 Marais \u1EDF Paris \u0111\u00E3 chuy\u1EC3n t\u1EEB khu b\u00ECnh d\u00E2n th\u00E0nh n\u01A1i s\u00E0nh \u0111i\u1EC7u v\u00E0 du l\u1ECBch.\\n\\n"
                "T\u1EEB th\u1EE9 ba l\u00E0 boulevard \u2014 danh t\u1EEB gi\u1ED1ng \u0111\u1EF1c \u2014 ngh\u0129a l\u00E0 \u0111\u1EA1i l\u1ED9. "
                "Boulevard l\u00E0 con \u0111\u01B0\u1EDDng r\u1ED9ng l\u1EDBn, th\u01B0\u1EDDng c\u00F3 c\u00E2y xanh hai b\u00EAn, \u0111\u1EB7c tr\u01B0ng c\u1EE7a \u0111\u00F4 th\u1ECB Ph\u00E1p. "
                "V\u00ED d\u1EE5: \u2018Les grands boulevards parisiens ont \u00E9t\u00E9 cr\u00E9\u00E9s par le baron Haussmann pour moderniser la capitale au dix-neuvi\u00E8me si\u00E8cle.\u2019 "
                "\u2014 C\u00E1c \u0111\u1EA1i l\u1ED9 l\u1EDBn Paris \u0111\u01B0\u1EE3c nam t\u01B0\u1EDBc Haussmann t\u1EA1o ra \u0111\u1EC3 hi\u1EC7n \u0111\u1EA1i h\u00F3a th\u1EE7 \u0111\u00F4 v\u00E0o th\u1EBF k\u1EF7 m\u01B0\u1EDDi ch\u00EDn.\\n\\n"
                "T\u1EEB th\u1EE9 t\u01B0 l\u00E0 pi\u00E9ton \u2014 danh t\u1EEB gi\u1ED1ng \u0111\u1EF1c \u2014 ngh\u0129a l\u00E0 ng\u01B0\u1EDDi \u0111i b\u1ED9. "
                "Pi\u00E9ton l\u00E0 ng\u01B0\u1EDDi di chuy\u1EC3n b\u1EB1ng ch\u00E2n, \u0111\u1ED1i t\u01B0\u1EE3ng ng\u00E0y c\u00E0ng \u0111\u01B0\u1EE3c \u01B0u ti\u00EAn trong quy ho\u1EA1ch. "
                "V\u00ED d\u1EE5: \u2018La ville de Paris a cr\u00E9\u00E9 de nombreuses zones pi\u00E9tonnes pour am\u00E9liorer la qualit\u00E9 de l\u2019air et la s\u00E9curit\u00E9.\u2019 "
                "\u2014 Th\u00E0nh ph\u1ED1 Paris \u0111\u00E3 t\u1EA1o nhi\u1EC1u khu v\u1EF1c d\u00E0nh cho ng\u01B0\u1EDDi \u0111i b\u1ED9 \u0111\u1EC3 c\u1EA3i thi\u1EC7n ch\u1EA5t l\u01B0\u1EE3ng kh\u00F4ng kh\u00ED v\u00E0 an to\u00E0n.\\n\\n"
                "T\u1EEB th\u1EE9 n\u0103m l\u00E0 densit\u00E9 \u2014 danh t\u1EEB gi\u1ED1ng c\u00E1i \u2014 ngh\u0129a l\u00E0 m\u1EADt \u0111\u1ED9. "
                "Densit\u00E9 \u0111o l\u01B0\u1EDDng s\u1ED1 ng\u01B0\u1EDDi ho\u1EB7c c\u00F4ng tr\u00ECnh tr\u00EAn m\u1ED9t \u0111\u01A1n v\u1ECB di\u1EC7n t\u00EDch. "
                "V\u00ED d\u1EE5: \u2018La densit\u00E9 de population \u00E0 Paris est parmi les plus \u00E9lev\u00E9es d\u2019Europe avec plus de vingt mille habitants au kilom\u00E8tre carr\u00E9.\u2019 "
                "\u2014 M\u1EADt \u0111\u1ED9 d\u00E2n s\u1ED1 Paris thu\u1ED9c h\u00E0ng cao nh\u1EA5t ch\u00E2u \u00C2u v\u1EDBi h\u01A1n hai m\u01B0\u01A1i ngh\u00ECn ng\u01B0\u1EDDi tr\u00EAn m\u1ED7i kil\u00F4m\u00E9t vu\u00F4ng.\\n\\n"
                "T\u1EEB cu\u1ED1i c\u00F9ng l\u00E0 zonage \u2014 danh t\u1EEB gi\u1ED1ng \u0111\u1EF1c \u2014 ngh\u0129a l\u00E0 ph\u00E2n v\u00F9ng. "
                "Zonage l\u00E0 vi\u1EC7c chia th\u00E0nh ph\u1ED1 th\u00E0nh c\u00E1c khu v\u1EF1c v\u1EDBi ch\u1EE9c n\u0103ng kh\u00E1c nhau \u2014 \u1EDF, th\u01B0\u01A1ng m\u1EA1i, c\u00F4ng nghi\u1EC7p. "
                "V\u00ED d\u1EE5: \u2018Le zonage strict des villes nouvelles des ann\u00E9es soixante-dix a cr\u00E9\u00E9 des quartiers monofonctionnels souvent critiqu\u00E9s.\u2019 "
                "\u2014 Ph\u00E2n v\u00F9ng nghi\u00EAm ng\u1EB7t c\u1EE7a c\u00E1c th\u00E0nh ph\u1ED1 m\u1EDBi th\u1EADp ni\u00EAn b\u1EA3y m\u01B0\u01A1i \u0111\u00E3 t\u1EA1o ra c\u00E1c khu ph\u1ED1 \u0111\u01A1n ch\u1EE9c n\u0103ng th\u01B0\u1EDDng b\u1ECB ch\u1EC9 tr\u00EDch.\\n\\n"
                "S\u00E1u t\u1EEB \u0111\u1EA7u ti\u00EAn \u0111\u00E3 s\u1EB5n s\u00E0ng. H\u00E3y b\u1EAFt \u0111\u1EA7u v\u1EDBi flashcard nh\u00E9!"
            ),
            "rtitle": "Paris c\u1EE7a Haussmann",
            "rdesc": "Au milieu du dix-neuvi\u00E8me si\u00E8cle, Paris \u00E9tait une ville m\u00E9di\u00E9vale surpeupl\u00E9e.",
            "rtext": (
                "Au milieu du dix-neuvi\u00E8me si\u00E8cle, Paris \u00E9tait une ville m\u00E9di\u00E9vale surpeupl\u00E9e. "
                "Les rues \u00E9troites, sombres et insalubres posaient des probl\u00E8mes "
                "de sant\u00E9 publique et de circulation.\\n\\n"
                "L\u2019urbanisme moderne de Paris est n\u00E9 avec le baron Haussmann. "
                "Nomm\u00E9 par Napol\u00E9on III, il a transform\u00E9 la capitale "
                "en per\u00E7ant de larges boulevards \u00E0 travers le tissu urbain ancien.\\n\\n"
                "Ces boulevards ont chang\u00E9 la vie des pi\u00E9tons. "
                "Pour la premi\u00E8re fois, les Parisiens pouvaient marcher "
                "sur de larges trottoirs bord\u00E9s d\u2019arbres, "
                "loin de la circulation des voitures \u00E0 cheval.\\n\\n"
                "Haussmann a aussi repens\u00E9 les quartiers. "
                "Chaque quartier devait avoir ses commerces, ses \u00E9coles, "
                "ses espaces publics. Le zonage n\u2019existait pas encore formellement, "
                "mais l\u2019id\u00E9e de s\u00E9parer les fonctions urbaines \u00E9tait d\u00E9j\u00E0 pr\u00E9sente.\\n\\n"
                "La densit\u00E9 a \u00E9t\u00E9 un enjeu central. "
                "Les immeubles haussmanniens, avec leurs six \u00E9tages r\u00E9glementaires, "
                "ont permis de loger plus de personnes "
                "tout en maintenant une qualit\u00E9 architecturale uniforme.\\n\\n"
                "L\u2019h\u00E9ritage de Haussmann est visible partout \u00E0 Paris. "
                "Ses boulevards, ses places et ses perspectives "
                "d\u00E9finissent encore aujourd\u2019hui l\u2019identit\u00E9 de la ville."
            ),
            "witems": [
                {"prompt": "D\u00F9ng t\u1EEB 'urbanisme' \u0111\u1EC3 vi\u1EBFt m\u1ED9t c\u00E2u. V\u00ED d\u1EE5: L\u2019urbanisme durable int\u00E8gre les enjeux environnementaux dans chaque d\u00E9cision d\u2019am\u00E9nagement du territoire.", "targetVocab": "urbanisme"},
                {"prompt": "D\u00F9ng t\u1EEB 'quartier' \u0111\u1EC3 vi\u1EBFt m\u1ED9t c\u00E2u. V\u00ED d\u1EE5: Ce quartier historique a conserv\u00E9 son charme gr\u00E2ce \u00E0 des r\u00E8gles strictes de pr\u00E9servation architecturale.", "targetVocab": "quartier"},
                {"prompt": "D\u00F9ng t\u1EEB 'boulevard' \u0111\u1EC3 vi\u1EBFt m\u1ED9t c\u00E2u. V\u00ED d\u1EE5: Le boulevard Saint-Germain est bord\u00E9 de caf\u00E9s litt\u00E9raires qui ont accueilli les plus grands \u00E9crivains fran\u00E7ais.", "targetVocab": "boulevard"},
                {"prompt": "D\u00F9ng t\u1EEB 'pi\u00E9ton' \u0111\u1EC3 vi\u1EBFt m\u1ED9t c\u00E2u. V\u00ED d\u1EE5: Les zones pi\u00E9tonnes du centre-ville attirent les familles et les touristes qui appr\u00E9cient de se promener sans voitures.", "targetVocab": "pi\u00E9ton"},
                {"prompt": "D\u00F9ng t\u1EEB 'densit\u00E9' \u0111\u1EC3 vi\u1EBFt m\u1ED9t c\u00E2u. V\u00ED d\u1EE5: La densit\u00E9 urbaine \u00E9lev\u00E9e de Tokyo oblige les architectes \u00E0 concevoir des logements compacts mais fonctionnels.", "targetVocab": "densit\u00E9"},
                {"prompt": "D\u00F9ng t\u1EEB 'zonage' \u0111\u1EC3 vi\u1EBFt m\u1ED9t c\u00E2u. V\u00ED d\u1EE5: Le nouveau plan de zonage autorise la construction de commerces dans les quartiers r\u00E9sidentiels pour r\u00E9duire les d\u00E9placements.", "targetVocab": "zonage"},
            ],
        },
'''

with open('vi-fr/_run_gen_d2_all.py', 'a', encoding='utf-8') as f:
    f.write(content)
print("Curriculum 3 session 1 written")
