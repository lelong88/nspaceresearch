# Requirements Document

## Introduction

Create 20 Korean-learning curriculums for Vietnamese-speaking adults at the intermediate and upper-intermediate levels. Language pair: userLanguage="vi", language="ko". This is the THIRD vi-ko curriculum set, building on the existing 20 beginner curriculums and 20 preintermediate/intermediate curriculums.

These 20 curriculums target learners who have completed the preintermediate/intermediate set and are ready for more sophisticated vocabulary, complex sentence structures, and deeper cultural/professional/intellectual topics. At this level, learners are comfortable with Hangul, understand Korean sentence structures well, and are expanding into TOPIK II levels 4-5 territory. Reading passages use complex grammar and idiomatic expressions freely. Topics cover diverse life domains: business strategy, Korean history, beauty industry, fine dining, social issues, arts, education, real estate, media, philosophy, fashion, startups, sports culture, wedding traditions, language nuances, healthcare, immigration, architecture, literature, and traditional medicine.

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese adults learning Korean at intermediate and upper-intermediate levels
- 18 vocabulary words per curriculum divided into 3 groups of 6
- 5 sessions per curriculum: 3 learning sessions, 1 review session, 1 final reading session
- Diverse topics covering business strategy, Korean history, beauty/skincare, fine dining, social issues, arts, education, real estate, media, philosophy, fashion, startups, sports culture, wedding traditions, language nuances, healthcare, immigration, architecture, literature, and traditional medicine
- Korean vocabulary in Hangul with Revised Romanization
- Vietnamese marketing text for all curriculums (bilingual rules: intermediate = bilingual, upper-intermediate = bilingual or single-language)
- Collection and series organization (1 collection, 4 series)
- Pricing at 49 credits per curriculum (standard for intermediate/upper-intermediate with 5 sessions)

### What This Spec Does NOT Cover

- Changes to the existing 20 beginner or 20 preintermediate/intermediate vi-ko curriculums
- Advanced-level Korean curriculums
- Overlap with beginner topics (greetings, numbers, family, colors, weather, drinks, days, emotions, Korean cuisine, shopping, transportation, hotels, office basics, four seasons, hobbies, health/body, housing, Korean culture/traditions, everyday technology, sports/exercise) or preintermediate/intermediate topics (job interview, booking/planning, street food, renting in Korea, medical visit, social relationships, phone communication, online shopping, K-Drama entertainment, K-Pop music, natural disasters/safety, banking/finance, Korean office culture, news/current events, education in Korea, psychology/emotions, rural tourism, technology/AI, law/rules, environment/sustainability)
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Grammar-focused curriculums (these are vocabulary-based balanced_skills)

## Glossary

- **Intermediate_Curriculum**: A curriculum for Vietnamese adults learning Korean at intermediate level. Uses bilingual text (Vietnamese + Korean). Vocabulary in Hangul with Revised Romanization. 18 words across 5 sessions. Includes vocabLevel3 in review session. Includes writingParagraph in final session. All marketing text in Vietnamese.
- **Upper_Intermediate_Curriculum**: A curriculum for Vietnamese adults learning Korean at upper-intermediate level. May use bilingual or single-language content per platform policy. Vocabulary in Hangul with Revised Romanization. 18 words across 5 sessions. Includes vocabLevel3 in review session. Includes writingParagraph in final session. Marketing text may be bilingual or Vietnamese.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="ko" — Vietnamese speakers learning Korean.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in. Written in Vietnamese.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Balanced_Skills**: Curriculum type distributing time across reading, listening, speaking, and writing. Uses 18 words across 3 learning sessions + review + final reading.
- **Hangul**: The Korean alphabet script. All Korean vocabulary is written in Hangul.
- **Revised_Romanization**: The official romanization system for Korean (e.g., 전략 = jeollyak). Used as pronunciation guidance for Vietnamese learners.
- **Speech_Levels**: Korean has multiple politeness levels. At intermediate/upper-intermediate level, learners encounter 합니다체 (formal polite), 해요체 (informal polite), 반말 (casual), and begin understanding 하십시오체 (formal written) in context.
- **TOPIK_II**: Test of Proficiency in Korean levels 3-6. Intermediate curriculums target levels 3-4 vocabulary; upper-intermediate targets levels 4-5.

## Requirements

### Requirement 1: Intermediate/Upper-Intermediate Curriculum Format and Structure

**User Story:** As a platform owner, I want 20 Korean-learning curriculums at intermediate and upper-intermediate levels for Vietnamese adults, so that learners who completed the preintermediate/intermediate set have a clear next step toward professional-level Korean.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 curriculums for the vi-ko Language_Pair at intermediate and upper-intermediate levels.
2. THE Curriculum_Creator SHALL create 10 intermediate curriculums and 10 upper-intermediate curriculums.
3. WHEN an intermediate or upper-intermediate curriculum is created, THE curriculum SHALL contain exactly 18 vocabulary words divided into 3 groups of 6.
4. WHEN an intermediate or upper-intermediate curriculum is created, THE curriculum SHALL contain exactly 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session.
5. THE curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
6. THE curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "ko"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
8. WHEN an intermediate curriculum is created, THE curriculum SHALL include `vocabLevel3` in the review session.
9. WHEN an intermediate curriculum is created, THE curriculum SHALL include `writingParagraph` in the final reading session.
10. WHEN an upper-intermediate curriculum is created, THE curriculum SHALL include `vocabLevel3` in the review session.
11. WHEN an upper-intermediate curriculum is created, THE curriculum SHALL include `writingParagraph` in the final reading session.
### Requirement 2: Topic Plan for 20 Intermediate/Upper-Intermediate Curriculums

**User Story:** As a platform owner, I want diverse topics that challenge learners with sophisticated vocabulary across business, history, beauty, food, society, arts, education, investment, media, philosophy, fashion, startups, sports, traditions, language, healthcare, immigration, architecture, literature, and traditional medicine, so that learners can function professionally and intellectually in Korean.

#### Acceptance Criteria

1. THE 20 curriculums SHALL cover the following topics, each individually crafted. No topic SHALL overlap with the 20 beginner curriculums or the 20 preintermediate/intermediate curriculums.

   **Intermediate (18 words, 5 sessions, 49 credits) — 10 curriculums:**
   - Curriculum 1: "Đầu Tư Và Chiến Lược Kinh Doanh" (Business Strategy and Leadership) — corporate strategy vocabulary: 전략/jeollyak (strategy), 리더십/rideosip (leadership), 의사결정/uisa-gyeoljeong (decision-making), 시장점유율/sijang-jeomyuyul (market share), 경쟁력/gyeongjaengnyeok (competitiveness), 혁신/hyeoksin (innovation), 인수합병/insu-hapbyeong (merger & acquisition), 주주/juju (shareholder), 이사회/isahoe (board of directors), 실적/siljeok (performance/results), 수익성/suikseong (profitability), 비전/bijeon (vision), 목표설정/mokpyo-seoljeong (goal-setting), 위기관리/wigi-gwanri (crisis management), 조직문화/jojik-munhwa (organizational culture), 성장전략/seongjang-jeollyak (growth strategy), 사업확장/saeop-hwakjang (business expansion), 지속가능경영/jisok-ganeung-gyeongyeong (sustainable management). vocabList: ["전략", "리더십", "의사결정", "시장점유율", "경쟁력", "혁신", "인수합병", "주주", "이사회", "실적", "수익성", "비전", "목표설정", "위기관리", "조직문화", "성장전략", "사업확장", "지속가능경영"]
   - Curriculum 2: "Đại Hàn Và Lịch Sử" (Korean History and Historical Figures) — history vocabulary: 왕조/wangjo (dynasty), 세종대왕/Sejong-daewang (King Sejong), 한글창제/Hangeul-changje (creation of Hangul), 임진왓란/Imjin-waeran (Japanese invasion 1592), 독립운동/dongnip-undong (independence movement), 식민지/singminji (colony), 광복/gwangbok (liberation), 전쟁/jeonjaeng (war), 휴전/hyujeon (ceasefire/armistice), 분단/bundan (division), 통일/tongil (unification), 민주화/minjuhwa (democratization), 유산/yusan (heritage/legacy), 문화재/munhwajae (cultural property), 유네스코/yuneseuко (UNESCO), 고궁/gogung (ancient palace), 사극/saguk (historical drama), 역사적/yeoksajeok (historical). vocabList: ["왕조", "세종대왕", "한글창제", "임진왓란", "독립운동", "식민지", "광복", "전쟁", "휴전", "분단", "통일", "민주화", "유산", "문화재", "유네스코", "고궁", "사극", "역사적"]
   - Curriculum 3: "Làm Đẹp Và Skincare Hàn Quốc" (Korean Beauty and Skincare Industry) — beauty industry vocabulary: 화장품/hwajangpum (cosmetics), 스킨케어/seukinkeo (skincare), 성분/seongbun (ingredients), 보습/bosup (moisturizing), 미백/mibaek (whitening/brightening), 주름/jureum (wrinkles), 항산화/hangsanhwa (antioxidant), 자외선/jawoeseon (UV rays), 선크림/seonkeurim (sunscreen), 세럼/seoreom (serum), 토너/toneo (toner), 에센스/esenseu (essence), 피부과/pibugwa (dermatology), 시술/sisul (cosmetic procedure), 필러/pilleo (filler), 보톡스/botokseu (botox), 매출/maechul (sales/revenue), 트렌드/teurendeu (trend). vocabList: ["화장품", "스킨케어", "성분", "보습", "미백", "주름", "항산화", "자외선", "선크림", "세럼", "토너", "에센스", "피부과", "시술", "필러", "보톡스", "매출", "트렌드"]
   - Curriculum 4: "Ẩm Thực Cao Cấp Hàn Quốc" (Korean Fine Dining and Regional Cuisine) — gastronomy vocabulary: 한정식/hanjeongsik (full-course Korean meal), 반찬/banchan (side dishes), 발효/balhyo (fermentation), 숙성/sukseong (aging/maturing), 제철/jecheol (seasonal), 산지직송/sanji-jiksong (farm-to-table), 맛집/matjip (famous restaurant), 미슐린/misyullin (Michelin), 셀프/syepeu (chef), 조리법/joribeop (cooking method), 담금질/damgeumjil (pickling), 숙성도/sukseongdo (degree of aging), 향신료/hyangsinryo (spices), 식감/sikgam (texture), 플레이팅/peulleiting (plating), 페어링/peeoling (pairing), 식도락/sikdorak (food culture/gastronomy), 맛평가/mat-pyeongga (food critic/review). vocabList: ["한정식", "반찬", "발효", "숙성", "제철", "산지직송", "맛집", "미슐린", "셀프", "조리법", "담금질", "숙성도", "향신료", "식감", "플레이팅", "페어링", "식도락", "맛평가"]
   - Curriculum 5: "Xã Hội Hàn Quốc Hiện Đại" (Modern Korean Social Issues) — social issues vocabulary: 고령화사회/goryeonghwa-sahoe (aging society), 저출산/jeochulsan (low birthrate), 성평등/seongpyeongdeung (gender equality), 워라밸/worabal (work-life balance), 청년실업/cheongnyeon-sireop (youth unemployment), 주거비/jugeоbi (housing costs), 격차/gyeokcha (gap/disparity), 다문화/damunhwa (multiculturalism), 인권/ingwon (human rights), 차별/chabyeol (discrimination), 세대갈등/sedae-galdeung (generational conflict), 사회복지/sahoe-bokji (social welfare), 빈부격차/binbu-gyeokcha (wealth gap), 정신건강/jeongsin-geongang (mental health), 과로사회/gwaro-sahoe (overwork society), 사회안전망/sahoe-anjeonmang (social safety net), 공정성/gongjeongseong (fairness), 양극화/yanggeukhwa (polarization). vocabList: ["고령화사회", "저출산", "성평등", "워라밸", "청년실업", "주거비", "격차", "다문화", "인권", "차별", "세대갈등", "사회복지", "빈부격차", "정신건강", "과로사회", "사회안전망", "공정성", "양극화"]
   - Curriculum 6: "Nghệ Thuật Hàn Quốc" (Korean Arts — Traditional Music, Modern Art, Film) — arts vocabulary: 전통음악/jeontong-eumak (traditional music), 판소리/pansori (pansori narrative singing), 가야금/gayageum (gayageum zither), 한복/hanbok (traditional clothing), 수묵화/sumukhwa (ink painting), 도예/doye (ceramics/pottery), 영화제/yeonghwaje (film festival), 감독/gamdok (director), 독립영화/dongnip-yeonghwa (independent film), 한류/hallyu (Korean Wave), 미술관/misulgwan (art museum), 전시회/jeonsihoе (exhibition), 설치미술/seolchi-misul (installation art), 현대미술/hyeondae-misul (contemporary art), 문화예술/munhwa-yesul (culture and arts), 창작/changjak (creation/creative work), 예술가/yesulga (artist), 미학/mihak (aesthetics). vocabList: ["전통음악", "판소리", "가야금", "한복", "수묵화", "도예", "영화제", "감독", "독립영화", "한류", "미술관", "전시회", "설치미술", "현대미술", "문화예술", "창작", "예술가", "미학"]
   - Curriculum 7: "Hệ Thống Giáo Dục Hàn Quốc" (Korean Education System and Academic Pressure) — education pressure vocabulary: 입시/ipsi (entrance exam), 수능/suneung (CSAT/college entrance exam), 사교육/sagyoyuk (private education), 과외/gwawoe (private tutoring), 입시지옥/ipsi-jiok (exam hell), 성적지상주의/seongjeok-jisangjuui (grade obsession), 입시전쟁/ipsi-jeonjaeng (entrance exam war), 야자/yaja (night self-study), 재수/jaesu (retaking the exam), 학벌/hakbeol (academic clique), 스펙/seupek (spec/qualifications), 취업률/chwieomnyul (employment rate), 장학생/janghaksaeng (scholarship student), 유학생/yuhaksaeng (international student), 교육개혁/gyoyuk-gaehyeok (education reform), 창의력/changuilyeok (creativity), 인성교육/inseong-gyoyuk (character education), 진로상담/jinro-sangdam (career counseling). vocabList: ["입시", "수능", "사교육", "과외", "입시지옥", "성적지상주의", "입시전쟁", "야자", "재수", "학벌", "스펙", "취업률", "장학생", "유학생", "교육개혁", "창의력", "인성교육", "진로상담"]
   - Curriculum 8: "Bất Động Sản Và Đầu Tư Tại Hàn Quốc" (Real Estate and Investment in Korea) — property/investment vocabulary: 아파트/apateu (apartment), 재건축/jaegeонchuk (reconstruction), 재개발/jaegaebal (redevelopment), 투기/tugi (speculation), 규제/gyuje (regulation), 대출규제/daechul-gyuje (loan regulation), 양도세/yangdose (capital gains tax), 청약/cheongnyak (housing subscription), 분양/bunyang (new apartment sale), 전세사기/jeonse-sagi (jeonse fraud), 시세/sise (market price), 호가/hoga (asking price), 매매/maemae (buying and selling), 중개수수료/junggae-susuryeo (brokerage fee), 등기/deunggi (registration), 담보대출/dambo-daechul (mortgage loan), 갑투/gaptu (gap investment), 주택정책/jutaek-jeongchaek (housing policy). vocabList: ["아파트", "재건축", "재개발", "투기", "규제", "대출규제", "양도세", "청약", "분양", "전세사기", "시세", "호가", "매매", "중개수수료", "등기", "담보대출", "갑투", "주택정책"]
   - Curriculum 9: "Truyền Thông Và Báo Chí Hàn Quốc" (Korean Media and Journalism) — media/journalism vocabulary: 언론/eonron (the press/media), 기사/gisa (news article), 특종/teukjong (exclusive report), 속보/sokbo (breaking news), 여론조작/yeoron-jojak (opinion manipulation), 가짜뉴스/gajja-nyuseu (fake news), 언론의자유/eonron-uijayu (press freedom), 편향보도/pyeonhyang-bodo (biased reporting), 팔로워/pallowo (follower), 구독자/gudokja (subscriber), 유튜버/yutyubeo (YouTuber), 인플루언서/inpeullueoonseo (influencer), 댓글/daetgeul (comment), 알고리즘/algorijeum (algorithm), 조회수/johoеsu (view count), 매체/maeche (media outlet), 신뢰도/sinroedo (credibility), 팔력/pillyeok (writing power/influence). vocabList: ["언론", "기사", "특종", "속보", "여론조작", "가짜뉴스", "언론의자유", "편향보도", "팔로워", "구독자", "유튜버", "인플루언서", "댓글", "알고리즘", "조회수", "매체", "신뢰도", "필력"]
   - Curriculum 10: "Triết Học Và Giá Trị Nho Giáo" (Korean Philosophy and Confucian Values) — philosophy vocabulary: 유교/yugyo (Confucianism), 효도/hyodo (filial piety), 예의/yeui (etiquette/propriety), 충/chung (loyalty), 인/in (benevolence), 의/ui (righteousness), 지/ji (wisdom), 신/sin (trust/faith), 선비/seonbi (Confucian scholar), 유교적/yugyojeok (Confucian), 위계질서/wigye-jilseo (hierarchical order), 존경/jongyeong (respect), 겦손/gyeomson (humility), 조화/johwa (harmony), 도덕/dodeok (morality), 양심/yangsim (conscience), 수양/suyang (self-cultivation), 선비정신/seonbi-jeongsin (scholar spirit). vocabList: ["유교", "효도", "예의", "충", "인", "의", "지", "신", "선비", "유교적", "위계질서", "존경", "겦손", "조화", "도덕", "양심", "수양", "선비정신"]

   **Upper-Intermediate (18 words, 5 sessions, 49 credits) — 10 curriculums:**
   - Curriculum 11: "Thời Trang Và Thiết Kế Hàn Quốc" (Korean Fashion and Design Industry) — fashion vocabulary: 패션산업/paesyeon-saneop (fashion industry), 디자이너/dijaineo (designer), 컨렉션/keolleksyeon (collection), 패션위크/paesyeon-wikeu (fashion week), 브랜드/beulaendeu (brand), 럭셔리/reokseori (luxury), 패스트패션/paeseuteu-paesyeon (fast fashion), 지속가능패션/jisok-ganeung-paesyeon (sustainable fashion), 트렌드/teurendeu (trend), 스타일링/seutailing (styling), 모델/model (model), 런웨이/reonwei (runway), 텍스타일/tekseutail (textile), 봄콜레션/bom-keolleksyeon (spring collection), 신진디자이너/sinjin-dijaineo (emerging designer), 동대문/Dongdaemun (Dongdaemun market), 한복디자인/hanbok-dijain (hanbok design), 문화상품/munhwa-sangpum (cultural product). vocabList: ["패션산업", "디자이너", "컨렉션", "패션위크", "브랜드", "럭셔리", "패스트패션", "지속가능패션", "트렌드", "스타일링", "모델", "런웨이", "텍스타일", "봄콜레션", "신진디자이너", "동대문", "한복디자인", "문화상품"]
   - Curriculum 12: "Hệ Sinh Thái Startup Hàn Quốc" (Korean Startup Ecosystem) — startup vocabulary: 창업/changeop (startup/founding), 유니콘/yunikon (unicorn), 투자유치/tuja-yuchi (attracting investment), 벤처케피털/bencheo-kaepiteol (venture capital), 엑셀러레이터/ekselleoreiteo (accelerator), 사업계획서/saeop-gyehoekseo (business plan), 피벗팅/piboting (pivoting), 스케일업/seukeireop (scaling up), 엑시트/eksiteu (exit), 기업공개/gieop-gonggae (IPO), 판교/pangyo (Pangyo tech hub), 스타트업생태계/seutateuop-saengtaegye (startup ecosystem), 실패/silpae (failure), 재도전/jaedojeon (retry/second attempt), 기업가정신/gieopga-jeongsin (entrepreneurial spirit), 혁신기술/hyeoksin-gisul (innovative technology), 인재영입/injae-yeongip (talent recruitment), 시장조사/sijang-josa (market research). vocabList: ["창업", "유니콘", "투자유치", "벤처케피털", "엑셀러레이터", "사업계획서", "피벗팅", "스케일업", "엑시트", "기업공개", "판교", "스타트업생태계", "실패", "재도전", "기업가정신", "혁신기술", "인재영입", "시장조사"]
   - Curriculum 13: "Văn Hóa Thể Thao Và Esports" (Korean Sports Culture and Esports) — sports/esports vocabulary: 야구/yagu (baseball), 축구/chukgu (soccer/football), 이스포츠/iseupotseu (esports), 프로게이머/peuro-geimeo (pro gamer), 리그/rigeu (league), 우승/useung (championship/victory), 팔들/paldeul (fans), 응원/eungwon (cheering/support), 응원가/eungwonga (cheer song), 스포츠정신/seupocheu-jeongsin (sportsmanship), 스포츠산업/seupocheu-saneop (sports industry), 중계/junggye (broadcast/commentary), 선수생활/seonsu-saenghwal (athlete life), 은퇴/euntoe (retirement), 훈련/hullyeon (training), 전술/jeonsul (tactics), 스포츠외교/seupocheu-oegyo (sports diplomacy), 올림픽/ollimpik (Olympics). vocabList: ["야구", "축구", "이스포츠", "프로게이머", "리그", "우승", "팔들", "응원", "응원가", "스포츠정신", "스포츠산업", "중계", "선수생활", "은퇴", "훈련", "전술", "스포츠외교", "올림픽"]
   - Curriculum 14: "Hôn Nhân Và Truyền Thống Gia Đình" (Korean Wedding and Family Traditions) — wedding/family vocabulary: 결혼식/gyeolhonsik (wedding ceremony), 폐백/pyebaek (traditional bowing ceremony), 함/ham (wedding gift box), 예단/yedan (wedding gifts), 신랑/sinrang (groom), 신부/sinbu (bride), 중매/jungmae (matchmaking), 상견례/sanggyeonrye (meeting of families), 혼수/honsu (wedding trousseau), 예식장/yesikjang (wedding hall), 주례/jurye (officiant), 축의금/chukuigeum (congratulatory money), 신혼여행/sinhon-yeohaeng (honeymoon), 제사/jesa (ancestral rites), 차례/charye (holiday ancestral rites), 효/hyo (filial piety), 장남/jangnam (eldest son), 며느리/myeoneuri (daughter-in-law). vocabList: ["결혼식", "폐백", "함", "예단", "신랑", "신부", "중매", "상견례", "혼수", "예식장", "주례", "축의금", "신혼여행", "제사", "차례", "효", "장남", "며느리"]
   - Curriculum 15: "Sắc Thái Ngôn Ngữ Hàn Quốc" (Korean Language Nuances — Honorifics, Speech Levels, Slang) — language nuances vocabulary: 존댓말/jondaenmal (honorific speech), 반말/banmal (casual speech), 존칭/jonching (honorific title), 경어/gyeongeo (respectful language), 겦양어/gyeomyangeo (humble language), 신조어/sinjоeo (neologism), 줄임말/jurimmal (abbreviation), 은어/euneo (slang/jargon), 유행어/yuhaengeo (trendy word), 사투리/saturi (dialect), 억양/eogyang (intonation), 어미/eomi (word ending), 조사/josa (particle), 어감/eogam (nuance/feeling), 높임말/nopimmal (elevated speech), 낮춤말/najchummal (lowered speech), 언어예절/eoneo-yejeol (language etiquette), 세대차이/sedae-chai (generational difference). vocabList: ["존댓말", "반말", "존칭", "경어", "겦양어", "신조어", "줄임말", "은어", "유행어", "사투리", "억양", "어미", "조사", "어감", "높임말", "낮춤말", "언어예절", "세대차이"]
   - Curriculum 16: "Hệ Thống Y Tế Hàn Quốc" (Korean Healthcare System) — healthcare system vocabulary: 건강보험/geongang-boheom (health insurance), 국민건강보험/gungmin-geongang-boheom (national health insurance), 의료시스템/uiryo-siseutem (medical system), 종합병원/jonghap-byeongwon (general hospital), 전문의/jeonmunui (specialist), 진료비/jinryobi (medical fees), 본인부담금/bonin-budamgeum (copayment), 의료관광/uiryo-gwangwang (medical tourism), 성형외과/seonghyeong-oegwa (plastic surgery), 원격진료/wongyeok-jinryo (telemedicine), 응급의료/eunggeup-uiryo (emergency medicine), 의료분쟁/uiryo-bunjaeng (medical dispute), 의료사고/uiryo-sago (medical accident), 환자권리/hwanja-gwonri (patient rights), 의료윤리/uiryo-yunri (medical ethics), 예방의학/yebang-uihak (preventive medicine), 건강검진/geongang-geomjin (health checkup), 의료기술/uiryo-gisul (medical technology). vocabList: ["건강보험", "국민건강보험", "의료시스템", "종합병원", "전문의", "진료비", "본인부담금", "의료관광", "성형외과", "원격진료", "응급의료", "의료분쟁", "의료사고", "환자권리", "의료윤리", "예방의학", "건강검진", "의료기술"]
   - Curriculum 17: "Nhập Cư Và Xã Hội Đa Văn Hóa" (Korean Immigration and Multicultural Society) — immigration vocabulary: 이민/imin (immigration), 이주노동자/iju-nodongja (migrant worker), 다문화가정/damunhwa-gajeong (multicultural family), 결혼이주여성/gyeolhon-iju-yeoseong (marriage migrant women), 영주권/yeongjugwon (permanent residency), 귀화/gwihwa (naturalization), 외국인등록/oegugin-deungnok (foreigner registration), 체류자격/cheryu-jagyeok (residence status), 불법체류/bulbeop-cheryu (illegal stay), 차별금지/chabyeol-geumji (anti-discrimination), 사회통합/sahoe-tonghap (social integration), 언어장벽/eoneo-jangbyeok (language barrier), 문화충돌/munhwa-chungdol (culture clash), 적응/jeogeung (adaptation), 정체성/jeongcheseong (identity), 공존/gongjon (coexistence), 포용/poyong (inclusion/tolerance), 외국인정책/oegugin-jeongchaek (foreigner policy). vocabList: ["이민", "이주노동자", "다문화가정", "결혼이주여성", "영주권", "귀화", "외국인등록", "체류자격", "불법체류", "차별금지", "사회통합", "언어장벽", "문화충돌", "적응", "정체성", "공존", "포용", "외국인정책"]
   - Curriculum 18: "Kiến Trúc Và Đô Thị Hóa" (Korean Architecture and Urban Development) — architecture vocabulary: 건축/geonchuk (architecture), 도시개발/dosi-gaebal (urban development), 재개발/jaegaebal (redevelopment), 스마트도시/seumateu-dosi (smart city), 친환경건축/chinhwangyeong-geonchuk (green architecture), 한옥보존/hanok-bojon (hanok preservation), 공공디자인/gonggong-dijain (public design), 도시재생/dosi-jaesaeng (urban regeneration), 주거환경/jugeo-hwangyeong (living environment), 공원/gongwon (park), 복합문화공간/bokhap-munhwa-gonggan (complex cultural space), 랜드마크/raendeumakeu (landmark), 스카이라인/seukairain (skyline), 도시계획/dosi-gyehoek (urban planning), 교통인프라/gyotong-inpeura (transport infrastructure), 보행자중심/bohaengja-jungsim (pedestrian-centered), 공간디자인/gonggan-dijain (spatial design), 지역활성화/jiyeok-hwalseonghwa (regional revitalization). vocabList: ["건축", "도시개발", "재개발", "스마트도시", "친환경건축", "한옥보존", "공공디자인", "도시재생", "주거환경", "공원", "복합문화공간", "랜드마크", "스카이라인", "도시계획", "교통인프라", "보행자중심", "공간디자인", "지역활성화"]
   - Curriculum 19: "Văn Học Hàn Quốc" (Korean Literature and Poetry) — literary vocabulary: 문학/munhak (literature), 소설/soseol (novel), 시/si (poetry), 수필/supil (essay), 작가/jakga (author/writer), 시인/siin (poet), 노벨문학상/Nobel-munhaksang (Nobel Prize in Literature), 번역/beonyeok (translation), 출판/chulpan (publishing), 문학상/munhaksang (literary prize), 서점/seojeom (bookstore), 독서/dokseo (reading), 서평/seopyeong (book review), 묘사/myosa (description/depiction), 은유/eunyu (metaphor), 주제/juje (theme), 문체/munche (writing style), 서사/seosa (narrative/epic). vocabList: ["문학", "소설", "시", "수필", "작가", "시인", "노벨문학상", "번역", "출판", "문학상", "서점", "독서", "서평", "묘사", "은유", "주제", "문체", "서사"]
   - Curriculum 20: "Y Học Cổ Truyền Hàn Quốc" (Korean Traditional Medicine — 한의학) — traditional medicine vocabulary: 한의학/hanuihak (Korean traditional medicine), 한의사/hanuisa (traditional medicine doctor), 한약/hanyak (herbal medicine), 침/chim (acupuncture), 뜻/tteum (moxibustion), 부항/buhang (cupping), 경락/gyeongnak (meridians), 혈자리/hyeoljari (acupuncture points), 체질/chejil (body constitution), 음양/eumyang (yin and yang), 오행/ohaeng (five elements), 보약/boyak (tonic medicine), 생약/saengyak (raw herbs), 탕약/tangyak (herbal decoction), 인삼/insam (ginseng), 녹용/nogyong (deer antler), 양생/yangsaeng (health cultivation), 체질개선/chejil-gaeseon (constitution improvement). vocabList: ["한의학", "한의사", "한약", "침", "뜻", "부항", "경락", "혈자리", "체질", "음양", "오행", "보약", "생약", "탕약", "인삼", "녹용", "양생", "체질개선"]

2. THE Curriculum_Creator SHALL select vocabulary words that are high-frequency at the TOPIK II (levels 4-5) range, practical, and relevant to Vietnamese adults working in or engaging deeply with Korean society.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 20 curriculums).
4. THE Curriculum_Creator SHALL ensure no vocabulary overlaps with the 20 beginner or 20 preintermediate/intermediate vi-ko curriculums.
5. WHEN creating reading passages, THE Curriculum_Creator SHALL use Korean sentences of 10-20 words, incorporating vocabulary appropriate for the level, complex grammar patterns, and idiomatic expressions relevant to adults engaging with professional, intellectual, and cultural topics in Korea.

### Requirement 3: Intermediate Content Design

**User Story:** As a content quality owner, I want intermediate-level content designed for adults who can handle complex Korean with sophisticated grammar, so that learners are appropriately challenged while still receiving Vietnamese support for instructions.

#### Acceptance Criteria

1. WHEN learner-facing content is created for introAudio scripts at intermediate level, THE scripts SHALL use Vietnamese as the primary language, introducing each Korean word with: the Korean word (in Hangul), Revised Romanization pronunciation, Vietnamese meaning, part of speech, an example sentence in Korean (10-18 words with natural grammar), Vietnamese translation of the example, and contextual usage notes including formality level.
2. WHEN reading passages are created for intermediate curriculums, THE passages SHALL be written in Korean using Hangul, employing vocabulary at TOPIK II level 3-4. Passages SHALL be 200-350 characters and feature scenarios such as business discussions, cultural analysis, social commentary, and professional situations.
3. WHEN reading passages are created for upper-intermediate curriculums, THE passages SHALL be written in Korean using Hangul, employing vocabulary at TOPIK II level 4-5 with complex grammar and idiomatic expressions. Passages SHALL be 300-500 characters and feature complex scenarios such as philosophical discussions, policy analysis, literary criticism, and cross-cultural commentary.
4. WHEN writingSentence prompts are created, THE prompts SHALL provide Vietnamese instructions, a complete Korean example sentence (with Revised Romanization and Vietnamese translation), and a substitution pattern requiring the learner to use the target vocabulary word in a new, contextually appropriate sentence.
5. WHEN writingParagraph prompts are created, THE prompts SHALL require the learner to write 4-6 Korean sentences using multiple vocabulary words from the curriculum, with Vietnamese instructions and guiding questions that demand analytical or argumentative responses.
6. THE introAudio scripts SHALL provide Revised Romanization pronunciation for all vocabulary and explain Korean pronunciation rules or memory hooks where helpful for Vietnamese learners.
7. ALL user-facing text for intermediate curriculums (titles, descriptions, previews, introAudio, writing prompts) SHALL be bilingual: Vietnamese for instructions/marketing, Korean for reading passages and example sentences.
8. WHEN an upper-intermediate curriculum is created, THE user-facing text MAY be bilingual (Vietnamese + Korean) or use Vietnamese for marketing with Korean for content, per platform policy.

### Requirement 4: Activity Structure for Intermediate Curriculums

**User Story:** As a platform owner, I want intermediate curriculums to include vocabLevel3 and writingParagraph to push learners toward greater fluency and production.

#### Acceptance Criteria

1. WHEN an intermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with Revised Romanization, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), vocabLevel3 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 500-800 chars), speakReading, readAlong, writingParagraph (using 6+ vocabulary words), introAudio (farewell with vocab review)

2. THE intermediate curriculum SHALL include vocabLevel3 in the review session (Session 4) only.
3. THE intermediate curriculum SHALL include writingParagraph in the final reading session (Session 5) only.

### Requirement 5: Activity Structure for Upper-Intermediate Curriculums

**User Story:** As a platform owner, I want upper-intermediate curriculums to challenge learners with longer passages, more complex writing tasks, and reduced scaffolding, so that learners build toward near-native reading and writing ability.

#### Acceptance Criteria

1. WHEN an upper-intermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with Revised Romanization, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 300-500 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 300-500 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 300-500 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), vocabLevel3 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 600-1000 chars), speakReading, readAlong, writingParagraph (using 8+ vocabulary words, analytical/argumentative), introAudio (farewell with vocab review)

2. THE upper-intermediate curriculum SHALL include vocabLevel3 in the review session (Session 4) only.
3. THE upper-intermediate curriculum SHALL include writingParagraph in the final reading session (Session 5) only.
4. THE writingParagraph prompts for upper-intermediate curriculums SHALL require analytical or argumentative responses — not simple summaries or descriptions.
5. THE reading passages in Session 5 for upper-intermediate curriculums SHALL be 600-1000 characters, using complex grammar patterns, idiomatic expressions, and sophisticated vocabulary.

### Requirement 6: Vietnamese Marketing Copy

**User Story:** As a content quality owner, I want all marketing text written in Vietnamese with persuasive copy standards, so that Vietnamese learners feel motivated to advance their Korean to professional and intellectual levels.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, addressing adult learner aspirations: professional advancement in Korean companies (Samsung, LG, Hyundai, Lotte), intellectual engagement with Korean society, cultural fluency beyond tourist-level, and personal transformation through mastering complex Korean.
2. THE Curriculum_Creator SHALL write curriculum previews (~150 words) as Persuasive_Copy with vivid hooks about the learner's Korean journey at this advanced stage, vocabulary word listing (Korean + Revised Romanization + Vietnamese meaning), and what the learner will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese for intermediate curriculums (as required for intermediate vi-ko curriculums where userLanguage="vi").
4. WHEN an upper-intermediate curriculum is created, THE marketing text (title, description, preview) MAY be in Vietnamese or bilingual, per platform policy.
5. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
6. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
7. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
8. THE Persuasive_Copy SHALL emphasize the practical value of intermediate/upper-intermediate Korean for Vietnamese adults: leading business negotiations at Korean companies, understanding Korean media and politics, engaging in intellectual discussions, navigating complex social situations, and building deep cross-cultural relationships.

### Requirement 7: introAudio Quality

**User Story:** As a content quality owner, I want introAudio scripts that effectively teach sophisticated Korean vocabulary with nuanced usage guidance to Vietnamese speakers, so that learners build professional-level communication skills.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created, THE script (600-900 words) SHALL greet the learner warmly in Vietnamese, introduce the topic with a motivating hook relevant to their professional/intellectual growth, list all 6 vocabulary words for the session, and teach each word with: the Korean word (Hangul), Revised Romanization, Vietnamese meaning, part of speech, a contextual example sentence in Korean (10-18 words), Vietnamese translation, and usage notes including formality level and common collocations.
2. WHEN a grammar/usage introAudio is created, THE script (300-500 words) SHALL explain 2-3 grammar patterns or usage nuances relevant to the session's vocabulary, with Korean examples and Vietnamese explanations.
3. WHEN a review introAudio is created, THE script (400-600 words) SHALL congratulate the learner, recap key vocabulary from previous sessions with brief reminders, and motivate for the review activities.
4. WHEN a farewell introAudio is created, THE script (400-600 words) SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, connect the words back to the curriculum's theme, and close with a warm personal sign-off.
5. THE Farewell_Palette SHALL assign one of the 5 farewell tones to each curriculum's farewell script.
6. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same farewell tone.
7. ALL introAudio scripts SHALL be individually crafted for their specific curriculum topic — no templated content generation.

### Requirement 8: Collection and Series Organization

**User Story:** As a platform owner, I want the 20 curriculums organized into a logical collection and series structure, so that learners can navigate the content by thematic interest.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create exactly 1 collection for the vi-ko intermediate/upper-intermediate curriculum set.
2. THE Collection_Organizer SHALL create exactly 4 series within the collection, grouped thematically:
   - Series 1: "Kinh Doanh Và Sự Nghiệp" (Business & Career) — Curriculums 1, 8, 12 (business strategy, real estate/investment, startups)
   - Series 2: "Văn Hóa Và Xã Hội" (Culture & Society) — Curriculums 2, 5, 6, 14, 17 (Korean history, social issues, arts, wedding traditions, immigration)
   - Series 3: "Đời Sống Và Xu Hướng" (Lifestyle & Trends) — Curriculums 3, 4, 7, 9, 13, 16 (beauty/skincare, fine dining, education, media, sports, healthcare)
   - Series 4: "Tri Thức Và Tư Tưởng" (Knowledge & Ideas) — Curriculums 10, 15, 18, 19, 20 (philosophy/Confucianism, language nuances, architecture, literature, traditional medicine)
3. THE Collection_Organizer SHALL set displayOrder for each curriculum within its series.
4. THE Collection_Organizer SHALL set displayOrder for each series within the collection.
5. THE series descriptions SHALL be written in Vietnamese, use one of the 6 Tone_Palette types, and fit within 255 characters.
6. WHILE assigning tones to series descriptions, THE Tone_Assigner SHALL ensure all 4 series use different tones.
7. THE collection description SHALL be a short informative summary in Vietnamese (not persuasive copy).

### Requirement 9: Script Architecture and Deployment

**User Story:** As a developer, I want a clean script architecture with one standalone Python script per curriculum and one orchestrator, so that each curriculum can be created, verified, and maintained independently.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 standalone Python scripts, one per curriculum, in the `vi-ko-intermediate-curriculums/` directory.
2. THE Curriculum_Creator SHALL produce exactly 1 orchestrator script that creates the collection, 4 series, wires curriculums to series, series to collection, and sets all displayOrders.
3. WHEN a curriculum script is executed, THE script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
4. WHEN a curriculum script is executed, THE script SHALL call `curriculum/create` with `language: "ko"`, `userLanguage: "vi"`, and `content` as a JSON string.
5. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` — all curriculums are created private.
6. THE Content_Validator SHALL validate each curriculum's JSON content against the Content Corruption Detection Rules before upload, checking: top-level structure, session structure, activity structure, activity-type-specific data rules, and cross-field consistency.
7. WHEN all curriculums are successfully created and verified in the database, THE scripts SHALL be deleted, leaving only a README.md documenting: all curriculum IDs, collection/series IDs, creation method, SQL queries for retrieval, and recreation context.
8. THE Curriculum_Creator SHALL set price to 49 credits for each curriculum via `curriculum/setPrice`.

### Requirement 10: Pricing

**User Story:** As a platform owner, I want all 20 curriculums priced at 49 credits each, consistent with the standard pricing for intermediate/upper-intermediate curriculums with 5 sessions.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL set the price of each of the 20 curriculums to exactly 49 credits via the `curriculum/setPrice` API endpoint.
2. THE pricing SHALL be consistent across all 20 curriculums regardless of whether they are intermediate or upper-intermediate level.
