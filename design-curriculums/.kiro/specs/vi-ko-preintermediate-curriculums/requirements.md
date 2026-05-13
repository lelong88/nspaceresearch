# Requirements Document

## Introduction

Create 20 Korean-learning curriculums for Vietnamese-speaking adults at the preintermediate and intermediate levels. Language pair: userLanguage="vi", language="ko". This is the second vi-ko curriculum set, building on the existing 20 beginner curriculums that cover basic topics (greetings, numbers, family, colors, weather, drinks, days, emotions, Korean cuisine, shopping, transportation, hotels, office basics, four seasons, hobbies, health/body, housing, Korean culture/traditions, everyday technology, sports/exercise).

These 20 curriculums target learners who have completed the beginner set and are ready for more complex vocabulary, longer sentences, and richer cultural/professional scenarios. At this level, learners are comfortable reading Hangul and are building fluency with Korean sentence structures. Topics are more sophisticated: workplace communication, travel planning, cultural deep-dives, relationships, entertainment industry, arts, and daily life at a higher complexity level — all highly relevant to Vietnamese adults who work at Korean companies (Samsung, LG, Hyundai), watch K-dramas, listen to K-pop, or plan to travel/work in Korea.

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese adults learning Korean at preintermediate and intermediate levels
- 18 vocabulary words per curriculum divided into 3 groups of 6
- 5 sessions per curriculum: 3 learning sessions, 1 review session, 1 final reading session
- Diverse topics covering workplace, travel, culture, relationships, entertainment, technology, arts, daily life, and society
- Korean vocabulary in Hangul with Revised Romanization pronunciation guidance
- Vietnamese marketing text (titles, descriptions, previews)
- Collection and series organization
- Pricing at 49 credits per curriculum (standard for preintermediate/intermediate with 5 sessions)

### What This Spec Does NOT Cover

- Changes to the existing 20 beginner vi-ko curriculums
- Upper-intermediate or advanced Korean curriculums
- Overlap with beginner topics already covered
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Grammar-focused curriculums (these are vocabulary-based balanced_skills)
- Hanja (Chinese characters used in Korean) — preintermediate/intermediate learners focus on Hangul vocabulary

## Glossary

- **Preintermediate_Curriculum**: A curriculum for Vietnamese adults learning Korean at preintermediate level. Uses bilingual text (Vietnamese + Korean). Vocabulary in Hangul with Revised Romanization. 18 words across 5 sessions. Does NOT include writingParagraph or vocabLevel3.
- **Intermediate_Curriculum**: A curriculum for Vietnamese adults learning Korean at intermediate level. Uses bilingual text (Vietnamese + Korean). Vocabulary in Hangul with Revised Romanization. 18 words across 5 sessions. Includes writingParagraph in the final session. Includes vocabLevel3 in review session.
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
- **Revised_Romanization**: The official romanization system for Korean (e.g., 직장 = jikjang). Used as pronunciation guidance for Vietnamese learners.
- **Speech_Levels**: Korean has multiple politeness levels. At preintermediate/intermediate level, learners encounter 합니다체 (formal polite), 해요체 (informal polite), and begin understanding 반말 (casual) in context.

## Requirements

### Requirement 1: Preintermediate/Intermediate Curriculum Format and Structure

**User Story:** As a platform owner, I want 20 Korean-learning curriculums at preintermediate and intermediate levels for Vietnamese adults, so that learners who completed the beginner set have a clear next step in their Korean journey.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 curriculums for the vi-ko Language_Pair at preintermediate and intermediate levels.
2. THE Curriculum_Creator SHALL create 12 preintermediate curriculums and 8 intermediate curriculums.
3. WHEN a preintermediate or intermediate curriculum is created, THE curriculum SHALL contain exactly 18 vocabulary words divided into 3 groups of 6.
4. WHEN a preintermediate or intermediate curriculum is created, THE curriculum SHALL contain exactly 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session.
5. THE curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
6. THE curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "ko"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
8. WHEN a preintermediate curriculum is created, THE curriculum SHALL NOT include `writingParagraph` activities.
9. WHEN a preintermediate curriculum is created, THE curriculum SHALL NOT include `vocabLevel3` activities.
10. WHEN an intermediate curriculum is created, THE curriculum SHALL include `writingParagraph` in the final reading session.
11. WHEN an intermediate curriculum is created, THE curriculum SHALL include `vocabLevel3` in the review session.


### Requirement 2: Topic Plan for 20 Preintermediate/Intermediate Curriculums

**User Story:** As a platform owner, I want diverse topics that build on the beginner foundation with more complex vocabulary and real-world scenarios, so that learners can handle workplace communication, travel planning, cultural discussions, entertainment, and social situations in Korean.

#### Acceptance Criteria

1. THE 20 curriculums SHALL cover the following topics, each individually crafted. No topic SHALL overlap with the 20 beginner curriculums (greetings, numbers, family, colors, weather, drinks, days, emotions, Korean cuisine, shopping, transportation, hotels, office basics, four seasons, hobbies, health/body, housing, Korean culture/traditions, everyday technology, sports/exercise).

   **Preintermediate (18 words, 5 sessions, 49 credits) — 12 curriculums:**
   - Curriculum 1: "Phỏng Vấn Xin Việc" (Job Interview) — workplace vocabulary for job hunting in Korean companies: 이력서/iryeokseo (resume), 면접/myeonjeop (interview), 지원동기/jiwondonggi (motivation for applying), 경력/gyeongnyeok (career/experience), 연봉/yeonbong (annual salary), 정규직/jeonggyujik (full-time position), 야근/yageun (overtime), 상사/sangsa (superior/boss), 부하/buha (subordinate), 승진/seungjin (promotion), 퇴사/toesa (resignation), 지원하다/jiwonhada (to apply), 채용/chaeyong (hiring/recruitment), 연수/yeonsu (training), 출퇴근/chultogeun (commuting), 유급휴가/yugeupyuga (paid leave), 이직/ijik (job change), 명함/myeongham (business card). vocabList: ["이력서", "면접", "지원동기", "경력", "연봉", "정규직", "야근", "상사", "부하", "승진", "퇴사", "지원하다", "채용", "연수", "출퇴근", "유급휴가", "이직", "명함"]
   - Curriculum 2: "Đặt Vé Và Lên Kế Hoạch" (Booking Tickets and Planning) — travel planning vocabulary: 예매/yemae (advance booking), 편도/pyeondo (one-way), 왕복/wangbok (round trip), 출발/chulbal (departure), 도착/dochak (arrival), 환승/hwanseung (transfer), 공항/gonghang (airport), 탑승/tapseung (boarding), 여권/yeogwon (passport), 관광/gwangwang (sightseeing), 여행사/yeohaengsa (travel agency), 일정/iljeong (schedule/itinerary), 짐 싸기/jim ssagi (packing), 환전/hwanjeon (currency exchange), 면세/myeonse (duty-free), 안내/annae (guidance/information), 지도/jido (map), 기념품/ginyeompum (souvenir). vocabList: ["예매", "편도", "왕복", "출발", "도착", "환승", "공항", "탑승", "여권", "관광", "여행사", "일정", "짐 싸기", "환전", "면세", "안내", "지도", "기념품"]
   - Curriculum 3: "Ẩm Thực Đường Phố Hàn Quốc" (Korean Street Food) — street food culture vocabulary: 포장마차/pojangmacha (street food tent), 떡볶이/tteokbokki (spicy rice cakes), 순대/sundae (blood sausage), 호떡/hotteok (sweet pancake), 주문하다/jumunhada (to order), 포장/pojang (takeout/packaging), 먹방/meokbang (eating broadcast), 줄서다/julseoda (to stand in line), 일회용/ilhoeyong (disposable), 맛/mat (taste/flavor), 매운/maeun (spicy), 달콤한/dalkomhan (sweet), 굽다/gupda (to grill), 튀기다/twigida (to deep-fry), 찌다/jjida (to steam), 속/sok (filling/inside), 양념/yangnyeom (seasoning/sauce), 고명/gomyeong (garnish/topping). vocabList: ["포장마차", "떡볶이", "순대", "호떡", "주문하다", "포장", "먹방", "줄서다", "일회용", "맛", "매운", "달콤한", "굽다", "튀기다", "찌다", "속", "양념", "고명"]
   - Curriculum 4: "Thuê Nhà Ở Hàn Quốc" (Renting in Korea) — housing/rental vocabulary: 월세/wolse (monthly rent), 전세/jeonse (key money deposit rental), 보증금/bojeunggeum (security deposit), 부동산/budongsan (real estate agency), 원룸/wonrum (studio apartment), 자취/jachwi (living alone), 이사/isa (moving), 계약/gyeyak (contract), 보증인/bojeungin (guarantor), 관리비/gwanribi (maintenance fee), 역세권/yeoksegwon (near subway station), 신축/sinchuk (newly built), 채광/chaegwang (natural lighting), 방음/bangeum (soundproofing), 분리수거/bunrisugeo (recycling/waste sorting), 집주인/jipjuin (landlord), 갱신/gaengsin (renewal), 퇴거/toegeo (eviction/moving out). vocabList: ["월세", "전세", "보증금", "부동산", "원룸", "자취", "이사", "계약", "보증인", "관리비", "역세권", "신축", "채광", "방음", "분리수거", "집주인", "갱신", "퇴거"]
   - Curriculum 5: "Khám Bệnh Ở Hàn Quốc" (Medical Visit in Korea) — medical/healthcare vocabulary: 진찰/jinchal (medical examination), 증상/jeungsang (symptoms), 처방전/cheobangjeong (prescription), 건강보험/geongang-boheom (health insurance), 접수/jeopsu (reception/registration), 대기실/daegisil (waiting room), 내과/naegwa (internal medicine), 외과/oegwa (surgery department), 검사/geomsa (test/examination), 주사/jusa (injection), 입원/ibwon (hospitalization), 퇴원/toewon (discharge), 약국/yakguk (pharmacy), 알레르기/allereugi (allergy), 예방접종/yebangjeopjong (vaccination), 진단/jindan (diagnosis), 소견서/sogyeonseo (medical certificate), 응급실/eunggeupssil (emergency room). vocabList: ["진찰", "증상", "처방전", "건강보험", "접수", "대기실", "내과", "외과", "검사", "주사", "입원", "퇴원", "약국", "알레르기", "예방접종", "진단", "소견서", "응급실"]
   - Curriculum 6: "Mối Quan Hệ Xã Hội" (Social Relationships) — relationship/social vocabulary: 친구/chingu (friend), 지인/jiin (acquaintance), 사귀다/sagwida (to date/make friends), 헤어지다/heeojida (to break up/part), 신뢰/silloe (trust), 약속/yaksok (promise/appointment), 상담/sangdam (consultation/counseling), 소개/sogae (introduction), 초대하다/chodaehada (to invite), 거절하다/geojeolhada (to refuse), 사과하다/sagwahada (to apologize), 용서하다/yongseohada (to forgive), 다투다/datuda (to quarrel), 화해하다/hwahaehada (to reconcile), 배려/baeryeo (consideration/thoughtfulness), 속마음/songmaeum (true feelings), 눈치/nunchi (social awareness/reading the room), 체면/chemyeon (face/dignity). vocabList: ["친구", "지인", "사귀다", "헤어지다", "신뢰", "약속", "상담", "소개", "초대하다", "거절하다", "사과하다", "용서하다", "다투다", "화해하다", "배려", "속마음", "눈치", "체면"]
   - Curriculum 7: "Giao Tiếp Qua Điện Thoại" (Phone Communication) — telephone/communication vocabulary: 전화하다/jeonhwahada (to call), 자동응답/jadong-eungdap (voicemail), 수신/susin (incoming call), 발신/balsin (outgoing call), 다시 걸다/dasi geolda (to call back), 메시지/mesiji (message), 내선/naeseon (extension), 외선/oeseon (outside line), 통화/tonghwa (phone conversation), 끊다/kkeunta (to hang up), 연결되다/yeongyeoldoeda (to be connected), 통화 중/tonghwa jung (line busy), 번호/beonho (number), 등록/deungnok (registration), 연락처/yeollakcheo (contact information), 부재중/bujaejung (missed call/absence), 문자/munja (text message), 돌려주다/dollyeojuda (to transfer a call). vocabList: ["전화하다", "자동응답", "수신", "발신", "다시 걸다", "메시지", "내선", "외선", "통화", "끊다", "연결되다", "통화 중", "번호", "등록", "연락처", "부재중", "문자", "돌려주다"]
   - Curriculum 8: "Mua Sắm Trực Tuyến" (Online Shopping) — e-commerce vocabulary: 인터넷 쇼핑/inteonet syoping (online shopping), 장바구니/jangbaguni (shopping cart), 배송비/baesongbi (shipping fee), 배달되다/baedaldoeda (to be delivered), 반품/banpum (return), 교환/gyohwan (exchange), 후기/hugi (review), 평점/pyeongjeom (rating), 재고/jaego (stock/inventory), 할인/harin (discount), 적립금/jeokripgeum (reward points), 쿠폰/kupon (coupon), 택배/taekbae (courier/delivery), 대금/daegeum (payment), 계좌이체/gyejwa-iche (bank transfer), 카드결제/kadeu-gyeolje (card payment), 영수증/yeongsujeung (receipt), 문의/munui (inquiry). vocabList: ["인터넷 쇼핑", "장바구니", "배송비", "배달되다", "반품", "교환", "후기", "평점", "재고", "할인", "적립금", "쿠폰", "택배", "대금", "계좌이체", "카드결제", "영수증", "문의"]
   - Curriculum 9: "K-Drama Và Giải Trí" (K-Drama and Entertainment) — entertainment industry vocabulary: 드라마/deurama (drama/TV series), 배우/baeu (actor/actress), 촬영/chwaryeong (filming/shooting), 대본/daebon (script), 시청률/sicheongnyul (viewership rating), 방영/bangyeong (broadcast/airing), 팬/paen (fan), 팬미팅/paenmiting (fan meeting), 연예인/yeonyein (celebrity), 오디션/odisyeon (audition), 예능/yeneung (variety show), 출연/churyeon (appearance/starring), 제작/jejak (production), 감독/gamdok (director), 각본/gakbon (screenplay), 시즌/sijeun (season), 결말/gyeolmal (ending/conclusion), 명장면/myeongjangmyeon (iconic scene). vocabList: ["드라마", "배우", "촬영", "대본", "시청률", "방영", "팬", "팬미팅", "연예인", "오디션", "예능", "출연", "제작", "감독", "각본", "시즌", "결말", "명장면"]
   - Curriculum 10: "K-Pop Và Âm Nhạc" (K-Pop and Music) — music industry vocabulary: 가수/gasu (singer), 아이돌/aidol (idol), 앨범/aelbeom (album), 음원/eumwon (digital music/track), 차트/chateu (chart), 컴백/keombaek (comeback), 뮤직비디오/myujik-bidio (music video), 안무/anmu (choreography), 팬덤/paendeom (fandom), 응원봉/eungwonbong (lightstick), 콘서트/konseoteu (concert), 데뷔/debwi (debut), 작곡/jakgok (composing), 작사/jaksa (lyric writing), 음악방송/eumak-bangsong (music show), 총판매량/chongpanmaeryang (total sales), 스트리밍/seutriming (streaming), 팬카페/paen-kape (fan cafe/community). vocabList: ["가수", "아이돌", "앨범", "음원", "차트", "컴백", "뮤직비디오", "안무", "팬덤", "응원봉", "콘서트", "데뷔", "작곡", "작사", "음악방송", "총판매량", "스트리밍", "팬카페"]
   - Curriculum 11: "Thiên Tai Và An Toàn" (Natural Disasters and Safety) — disaster preparedness vocabulary: 지진/jijin (earthquake), 태풍/taepung (typhoon), 홍수/hongsu (flood), 대피/daepi (evacuation), 방재/bangjae (disaster prevention), 비상구/bisangu (emergency exit), 대피소/daepiso (evacuation shelter), 경보/gyeongbo (warning/alert), 여진/yeojin (aftershock), 정전/jeongjeon (power outage), 단수/dansu (water outage), 비축/bichuk (stockpiling), 소화기/sohwagi (fire extinguisher), 구조/gujo (rescue), 안부확인/anbu-hwagin (safety confirmation), 방재용품/bangjae-yongpum (disaster supplies), 내진/naejin (earthquake-resistant), 긴급재난문자/gingeup-jaenan-munja (emergency alert text). vocabList: ["지진", "태풍", "홍수", "대피", "방재", "비상구", "대피소", "경보", "여진", "정전", "단수", "비축", "소화기", "구조", "안부확인", "방재용품", "내진", "긴급재난문자"]
   - Curriculum 12: "Ngân Hàng Và Tài Chính" (Banking and Finance) — banking/finance vocabulary: 은행/eunhaeng (bank), 계좌/gyejwa (account), 송금/songgeum (remittance/transfer), 환율/hwanyul (exchange rate), 대출/daechul (loan), 이자/ija (interest), 저축/jeochuk (savings), 입금/ipgeum (deposit), 출금/chulgeum (withdrawal), 수수료/susuryeo (fee/commission), 신용카드/sinyong-kadeu (credit card), 체크카드/chekeu-kadeu (debit card), 잔액/janaek (balance), 자동이체/jadong-iche (automatic transfer), 통장/tongjang (bankbook), 비밀번호/bimilbeonho (PIN/password), 외화/oehwa (foreign currency), 금리/geumni (interest rate). vocabList: ["은행", "계좌", "송금", "환율", "대출", "이자", "저축", "입금", "출금", "수수료", "신용카드", "체크카드", "잔액", "자동이체", "통장", "비밀번호", "외화", "금리"]

   **Intermediate (18 words, 5 sessions, 49 credits) — 8 curriculums:**
   - Curriculum 13: "Văn Hóa Công Sở Hàn Quốc" (Korean Office Culture) — workplace culture vocabulary: 존댓말/jondaenmal (honorific/formal speech), 보고/bogo (report), 연락/yeollak (contact/communication), 상담/sangdam (consultation), 회식/hoesik (company dinner/drinking), 송년회/songnyeonhoe (year-end party), 환영회/hwanyeonghoe (welcome party), 송별회/songbyeolhoe (farewell party), 연공서열/yeongong-seoryeol (seniority system), 워라밸/worabal (work-life balance), 연차/yeoncha (annual leave), 출장/chuljang (business trip), 회의록/hoeuirok (meeting minutes), 발표/balpyo (presentation), 마감/magam (deadline), 결재/gyeolje (approval), 사내문화/sanae-munhwa (company culture), 팀워크/timwokeu (teamwork). vocabList: ["존댓말", "보고", "연락", "상담", "회식", "송년회", "환영회", "송별회", "연공서열", "워라밸", "연차", "출장", "회의록", "발표", "마감", "결재", "사내문화", "팀워크"]
   - Curriculum 14: "Tin Tức Và Thời Sự" (News and Current Events) — media/news vocabulary: 보도/bodo (news report), 기자/gija (journalist), 취재/chwije (news coverage), 여론/yeoron (public opinion), 선거/seongeo (election), 정책/jeongchaek (policy), 경제/gyeongje (economy), 경기/gyeonggi (economic conditions), 실업/sireop (unemployment), 물가/mulga (prices/cost of living), 증세/jeungse (tax increase), 저출산/jeochulsan (low birthrate), 고령화/goryeonghwa (aging population), 환경문제/hwangyeong-munje (environmental issues), 국제/gukje (international), 조약/joyak (treaty), 정상회담/jeongsang-hoedam (summit meeting), 외교/oegyo (diplomacy). vocabList: ["보도", "기자", "취재", "여론", "선거", "정책", "경제", "경기", "실업", "물가", "증세", "저출산", "고령화", "환경문제", "국제", "조약", "정상회담", "외교"]
   - Curriculum 15: "Giáo Dục Ở Hàn Quốc" (Education in Korea) — education system vocabulary: 입학/iphak (enrollment), 졸업/joreop (graduation), 수능/suneung (college entrance exam), 학원/hagwon (private academy/cram school), 장학금/janghakgeum (scholarship), 학점/hakjeom (credit/grade point), 논문/nonmun (thesis/paper), 연구/yeongu (research), 교수/gyosu (professor), 강의/gangui (lecture), 등록금/deungnokgeum (tuition), 유학/yuhak (study abroad), 동아리/dongari (club/society), 축제/chukje (festival), 성적/seongjeok (grades/transcript), 진로/jinro (career path), 취업준비/chwieop-junbi (job preparation), 대학원/daehagwon (graduate school). vocabList: ["입학", "졸업", "수능", "학원", "장학금", "학점", "논문", "연구", "교수", "강의", "등록금", "유학", "동아리", "축제", "성적", "진로", "취업준비", "대학원"]
   - Curriculum 16: "Tâm Lý Và Cảm Xúc" (Psychology and Emotions) — emotional/psychological vocabulary: 감정/gamjeong (emotion), 불안/buran (anxiety), 스트레스/seuteureseu (stress), 우울/uul (depression), 자신감/jasingam (self-confidence), 열등감/yeoldeunggam (inferiority complex), 공감/gonggam (empathy), 외로움/oeroum (loneliness), 성취감/seongchwigam (sense of achievement), 좌절/jwajjeol (setback/frustration), 성장/seongjang (growth), 자존감/jajongam (self-esteem), 기분전환/gibun-jeonhwan (change of mood), 힐링/hilling (healing/comfort), 명상/myeongsang (meditation), 상담/sangdam (counseling), 의존/uijon (dependence/addiction), 회복/hoebok (recovery). vocabList: ["감정", "불안", "스트레스", "우울", "자신감", "열등감", "공감", "외로움", "성취감", "좌절", "성장", "자존감", "기분전환", "힐링", "명상", "상담", "의존", "회복"]
   - Curriculum 17: "Du Lịch Nông Thôn Hàn Quốc" (Korean Rural Tourism) — countryside/rural vocabulary: 시골/sigol (countryside), 온천/oncheon (hot spring), 한옥/hanok (traditional Korean house), 민박/minbak (guesthouse/homestay), 농촌체험/nongchon-cheheom (farming experience), 수확/suhwak (harvest), 논/non (rice paddy), 밭/bat (field/farm), 어촌/eochon (fishing village), 고택/gotaek (historic house), 마을/maeul (village), 계단식 논/gyedansik non (terraced rice fields), 특산물/teuksanmul (local specialty), 사투리/saturi (dialect), 축제/chukje (festival), 향토음식/hyangto-eumsik (local cuisine), 자연/jayeon (nature), 풍경/punggyeong (scenery). vocabList: ["시골", "온천", "한옥", "민박", "농촌체험", "수확", "논", "밭", "어촌", "고택", "마을", "계단식 논", "특산물", "사투리", "축제", "향토음식", "자연", "풍경"]
   - Curriculum 18: "Công Nghệ Và AI" (Technology and AI) — modern technology vocabulary: 인공지능/ingongjineung (artificial intelligence), 자동화/jadonghwa (automation), 로봇/robot (robot), 데이터/deiteo (data), 알고리즘/algorijeum (algorithm), 프로그래밍/peurogeuraem (programming), 보안/boan (security), 개인정보/gaein-jeongbo (personal information), SNS/eseuenesseu (social media), 악플/akpeul (malicious comment), 가짜뉴스/gajja-nyuseu (fake news), 가상현실/gasang-hyeonsil (virtual reality), 전자결제/jeonja-gyeolje (electronic payment), 구독/gudok (subscription), 클라우드/keullaudeu (cloud), 알림/allim (notification), 업데이트/eobdeiteu (update), 해킹/haeking (hacking). vocabList: ["인공지능", "자동화", "로봇", "데이터", "알고리즘", "프로그래밍", "보안", "개인정보", "악플", "가짜뉴스", "가상현실", "전자결제", "구독", "클라우드", "알림", "업데이트", "해킹"]
   - Curriculum 19: "Pháp Luật Và Quy Tắc" (Law and Rules) — legal/rules vocabulary: 법률/beomnyul (law), 규칙/gyuchik (rules/regulations), 위반/wiban (violation), 벌금/beolgeum (fine/penalty), 신고/singo (report/filing), 허가/heoga (permission), 의무/uimu (obligation/duty), 권리/gwonri (right), 계약/gyeyak (contract), 보증/bojeung (guarantee), 배상/baesang (compensation), 재판/jaepan (trial/court), 변호사/byeonhosa (lawyer), 증거/jeungeo (evidence), 피해/pihae (damage/harm), 범죄/beomjoe (crime), 방범/bangbeom (crime prevention), 비자/bija (visa). vocabList: ["법률", "규칙", "위반", "벌금", "신고", "허가", "의무", "권리", "계약", "보증", "배상", "재판", "변호사", "증거", "피해", "범죄", "방범", "비자"]
   - Curriculum 20: "Môi Trường Và Phát Triển Bền Vững" (Environment and Sustainability) — environmental vocabulary: 환경/hwangyeong (environment), 재활용/jaehwaryong (recycling), 분리수거/bunrisugeo (waste sorting), 재생에너지/jaesaeng-eneoji (renewable energy), 에너지/eneoji (energy), 온난화/onnanhwa (global warming), 배출/baechul (emission), 감축/gamchuk (reduction), 지속가능/jisok-ganeung (sustainable), 친환경/chinhwangyeong (eco-friendly), 절약/jeolyak (saving/conservation), 태양광/taeyangwang (solar power), 풍력/pungnyeok (wind power), 오염/oyeom (pollution), 생태계/saengtaegye (ecosystem), 멸종위기/myeoljong-wigi (endangered), 산림파괴/sallim-pagoe (deforestation), 탄소중립/tanso-jungnip (carbon neutrality). vocabList: ["환경", "재활용", "분리수거", "재생에너지", "에너지", "온난화", "배출", "감축", "지속가능", "친환경", "절약", "태양광", "풍력", "오염", "생태계", "멸종위기", "산림파괴", "탄소중립"]

2. THE Curriculum_Creator SHALL select vocabulary words that are high-frequency at the TOPIK II (levels 3-4) range, practical, and relevant to Vietnamese adults living in or interacting with Korea.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 20 curriculums).
4. THE Curriculum_Creator SHALL ensure no vocabulary overlaps with the 20 beginner vi-ko curriculums.
5. WHEN creating reading passages, THE Curriculum_Creator SHALL use Korean sentences of 8-15 words, incorporating vocabulary appropriate for the level, and scenarios relevant to adults navigating real-life situations in Korea.


### Requirement 3: Preintermediate/Intermediate Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for adults at preintermediate and intermediate levels, so that learners are appropriately challenged while still receiving Vietnamese support.

#### Acceptance Criteria

1. WHEN learner-facing content is created for introAudio scripts, THE scripts SHALL use Vietnamese as the primary language, introducing each Korean word with: the Korean word (in Hangul), Revised Romanization pronunciation, Vietnamese meaning, an example sentence in Korean (8-15 words), and contextual usage notes including formality level.
2. WHEN reading passages are created for preintermediate curriculums, THE passages SHALL be written in Korean using Hangul, employing vocabulary at TOPIK I-II level. Passages SHALL be 150-250 characters and feature scenarios such as workplace interactions, travel situations, and social conversations.
3. WHEN reading passages are created for intermediate curriculums, THE passages SHALL be written in Korean using Hangul, employing vocabulary at TOPIK II level. Passages SHALL be 200-350 characters and feature more complex scenarios such as cultural analysis, news discussion, and professional situations.
4. WHEN writingSentence prompts are created, THE prompts SHALL provide Vietnamese instructions, a complete Korean example sentence (with Revised Romanization and Vietnamese translation), and a clear substitution pattern requiring the learner to use the target vocabulary word in a new context.
5. WHEN writingParagraph prompts are created (intermediate only), THE prompts SHALL require the learner to write 3-5 Korean sentences using multiple vocabulary words from the curriculum, with Vietnamese instructions and guiding questions.
6. THE introAudio scripts SHALL provide Revised Romanization pronunciation for all vocabulary and explain Korean pronunciation rules or memory hooks where helpful for Vietnamese learners (e.g., noting similarities between Korean and Vietnamese sounds).
7. ALL user-facing text (titles, descriptions, previews, introAudio, writing prompts) SHALL be bilingual: Vietnamese for instructions/marketing, Korean for reading passages and example sentences.

### Requirement 4: Activity Structure for Preintermediate Curriculums

**User Story:** As a platform owner, I want preintermediate curriculums to follow the established 5-session balanced_skills structure without advanced activities, so that learners build confidence before encountering more demanding tasks.

#### Acceptance Criteria

1. WHEN a preintermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with Revised Romanization, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 150-250 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 150-250 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 150-250 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 400-600 chars), speakReading, readAlong, introAudio (farewell with vocab review)

2. THE preintermediate curriculum SHALL NOT include vocabLevel3 or writingParagraph activities in any session.

### Requirement 5: Activity Structure for Intermediate Curriculums

**User Story:** As a platform owner, I want intermediate curriculums to include more demanding activities like writingParagraph and vocabLevel3, so that learners are pushed toward greater fluency and production.

#### Acceptance Criteria

1. WHEN an intermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with Revised Romanization, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), vocabLevel3 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 500-800 chars), speakReading, readAlong, writingParagraph (using 6+ vocabulary words), introAudio (farewell with vocab review)

2. THE intermediate curriculum SHALL include vocabLevel3 in the review session (Session 4) only.
3. THE intermediate curriculum SHALL include writingParagraph in the final reading session (Session 5) only.

### Requirement 6: Vietnamese Marketing Copy

**User Story:** As a content quality owner, I want all marketing text written in Vietnamese with persuasive copy standards, so that Vietnamese learners feel motivated to advance their Korean skills.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, addressing adult learner aspirations: career advancement with Korean companies (Samsung, LG, Hyundai, Lotte), deeper cultural understanding (K-drama, K-pop), confident travel in Korea, and intellectual growth through mastering complex Korean vocabulary and grammar.
2. THE Curriculum_Creator SHALL write curriculum previews (~150 words) as Persuasive_Copy with vivid hooks about the learner's Korean journey at this level, vocabulary word listing (Korean + Revised Romanization + Vietnamese meaning), and what the learner will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for preintermediate/intermediate vi-ko curriculums where userLanguage="vi").
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
7. THE Persuasive_Copy SHALL emphasize the practical value of intermediate Korean for Vietnamese adults: navigating Korean bureaucracy, building professional relationships at Korean companies, understanding Korean media and news, and experiencing Korea beyond tourist-level interactions.

### Requirement 7: introAudio Quality

**User Story:** As a content quality owner, I want introAudio scripts that effectively teach Korean vocabulary with pronunciation guidance to Vietnamese speakers, so that learners build correct pronunciation and usage habits.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created, THE script (500-800 words) SHALL greet the learner warmly in Vietnamese, introduce the topic with a motivating hook, list all 6 vocabulary words for the session, and teach each word with: the Korean word (Hangul), Revised Romanization pronunciation, Vietnamese meaning, part of speech, a contextual example sentence in Korean with Vietnamese translation, and a pronunciation tip or memory hook where applicable.
2. WHEN a vocabulary-teaching introAudio is created, THE script SHALL explain how each word is used in real Korean contexts, noting formality levels (반말 vs. 해요체 vs. 합니다체) where relevant.
3. WHEN a session recap introAudio is created (sessions 2-3), THE script SHALL briefly recap previous session words with pronunciation before introducing new ones — using phrases like "Bạn còn nhớ không?" and providing quick-review example sentences.
4. WHEN a grammar/usage introAudio is created, THE script SHALL explain 1-2 grammar patterns relevant to the session's vocabulary, with Vietnamese explanations and Korean example sentences.
5. WHEN a farewell introAudio is created, THE script (400-600 words) SHALL review 5-6 key vocabulary words with definitions and fresh Korean example sentences (with Revised Romanization and Vietnamese translation), summarize the learning journey, and close with a warm personal sign-off.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio.
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 8: Pricing

**User Story:** As a platform owner, I want preintermediate/intermediate curriculums priced at the standard rate, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a preintermediate or intermediate curriculum (5 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
2. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 9: Collection and Series Organization

**User Story:** As a platform owner, I want the 20 preintermediate/intermediate curriculums organized into a dedicated collection with thematic series, so that learners can browse content by interest area and find a clear progression from the beginner collection.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Hàn Trung Cấp" (Intermediate Korean) with a neutral, informative Vietnamese description explaining this is a collection of Korean curriculums for Vietnamese adults advancing beyond beginner level, covering workplace, culture, travel, entertainment, and daily life topics.
2. THE Collection_Organizer SHALL organize the 20 curriculums into 5 series of 4 curriculums each:
   - Series 1: "Sự Nghiệp Tại Hàn Quốc" (Career in Korea) — containing Curriculums 1, 4, 7, 13 (job interview, renting, phone communication, office culture). Description ≤255 chars using a Tone_Palette type.
   - Series 2: "Khám Phá Hàn Quốc" (Discovering Korea) — containing Curriculums 2, 3, 5, 17 (booking/planning, street food, medical visit, rural tourism). Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Đời Sống Và Xã Hội" (Life and Society) — containing Curriculums 6, 8, 12, 16 (social relationships, online shopping, banking, psychology/emotions). Description ≤255 chars using a different Tone_Palette type.
   - Series 4: "Văn Hóa Và Giải Trí" (Culture and Entertainment) — containing Curriculums 9, 10, 14, 15 (K-drama, K-pop, news/current events, education). Description ≤255 chars using a different Tone_Palette type.
   - Series 5: "Thế Giới Hiện Đại" (The Modern World) — containing Curriculums 11, 18, 19, 20 (natural disasters, technology/AI, law/rules, environment/sustainability). Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 5 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "ko"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 5 series use different Tone_Palette types.
8. WITHIN each series, THE maximum difficulty level gap SHALL be 1 level (preintermediate + intermediate is acceptable).


### Requirement 10: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes Korean curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. THE `vocabList` field SHALL be an array of lowercase strings (Korean words in Hangul), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with Korean example sentence, Revised Romanization, Vietnamese translation, and substitution pattern) and `targetVocab` fields.
7. WHEN a writingParagraph activity is created (intermediate only), THE activity SHALL have `data.vocabList`, `data.instructions` (Vietnamese), and `data.prompts` (array of at least 2 guiding questions in Vietnamese).
8. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence uses "Viết: <topic>"; writingParagraph uses "Viết đoạn: <topic>".

### Requirement 11: Content Validation

**User Story:** As a platform developer, I want every curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array with exactly 5 sessions, each having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify writingParagraph data structures for intermediate curriculums (vocabList, instructions, prompts array with ≥2 items).
9. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
10. THE Content_Validator SHALL verify that preintermediate curriculums do NOT contain writingParagraph or vocabLevel3 activities.
11. THE Content_Validator SHALL verify that intermediate curriculums contain vocabLevel3 only in Session 4 and writingParagraph only in Session 5.
12. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 12: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 20 preintermediate/intermediate curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (20 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, 5 series, wires them together, and sets display orders.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-ko-preintermediate-curriculums/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 13: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created Korean curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 14: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, engaging, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "preintermediate", "intermediate", "trung cấp", "중급").
4. THE curriculum titles SHALL be engaging and descriptive — using clear, motivating language that tells the learner what topic they will explore.

### Requirement 15: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 20 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum, tone assignments (description and farewell for all 20), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 16: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and 5 series via orchestrator, (2) create preintermediate curriculums (12 scripts), (3) create intermediate curriculums (8 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 20 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.
