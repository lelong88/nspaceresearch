# Tasks

## Task 1: Create Collection and Series Infrastructure

- [x] 1.1 Create the `medical-english-curriculum/` working directory
- [x] 1.2 Create the orchestrator script `create_medical_english_series.py` that will:
  - Create the "Tiếng Anh Y Khoa (Medical English)" collection
  - Create all 5 series with Vietnamese titles, descriptions (≤255 chars), and tone-assigned descriptions
  - Wire series to collection via `addSeriesToCollection`
  - Set series display orders (0-4: Anatomy → Clinical → Diseases → Pharmacology → Research)

## Task 2: Series A — Anatomy & Body Systems (5 curriculums)

- [x] 2.1 Create `create_anatomy_1_cardiovascular.py` — Cardiovascular System – Hệ Tim Mạch (18 words: 6+6+6, 5 sessions, persuasive Vietnamese copy, English reading passages about heart and circulatory system)
- [x] 2.2 Create `create_anatomy_2_respiratory.py` — Respiratory System – Hệ Hô Hấp (18 words about lungs, breathing, gas exchange)
- [x] 2.3 Create `create_anatomy_3_digestive.py` — Digestive System – Hệ Tiêu Hóa (18 words about GI tract, digestion, absorption)
- [x] 2.4 Create `create_anatomy_4_nervous.py` — Nervous System – Hệ Thần Kinh (18 words about brain, neurons, neural pathways)
- [x] 2.5 Create `create_anatomy_5_musculoskeletal.py` — Musculoskeletal System – Hệ Cơ Xương (18 words about bones, muscles, joints)

## Task 3: Series B — Clinical Skills & Patient Communication (5 curriculums)

- [x] 3.1 Create `create_clinical_1_history.py` — Taking a Patient History – Hỏi Bệnh Sử (18 words about history-taking, chief complaint, medical history)
- [x] 3.2 Create `create_clinical_2_examination.py` — Physical Examination – Khám Lâm Sàng (18 words about examination techniques, vital signs, auscultation)
- [x] 3.3 Create `create_clinical_3_diagnosis.py` — Explaining a Diagnosis – Giải Thích Chẩn Đoán (18 words about communicating findings, prognosis, medical terminology for patients)
- [x] 3.4 Create `create_clinical_4_treatment.py` — Discussing Treatment Options – Thảo Luận Phương Án Điều Trị (18 words about treatment plans, referrals, follow-up)
- [x] 3.5 Create `create_clinical_5_consent.py` — Obtaining Informed Consent – Lấy Đồng Ý Điều Trị (18 words about consent, risks, patient autonomy)

## Task 4: Series C — Diseases & Pathology (5 curriculums)

- [x] 4.1 Create `create_diseases_1_infectious.py` — Infectious Diseases – Bệnh Truyền Nhiễm (18 words about pathogens, transmission, infection control)
- [x] 4.2 Create `create_diseases_2_cardiovascular.py` — Cardiovascular Diseases – Bệnh Tim Mạch (18 words about heart disease, hypertension, atherosclerosis)
- [x] 4.3 Create `create_diseases_3_respiratory.py` — Respiratory Diseases – Bệnh Hô Hấp (18 words about asthma, pneumonia, COPD)
- [x] 4.4 Create `create_diseases_4_cancer.py` — Cancer & Oncology – Ung Thư & Ung Bướu (18 words about tumors, staging, oncology terms)
- [x] 4.5 Create `create_diseases_5_diabetes.py` — Diabetes & Metabolic Disorders – Đái Tháo Đường & Rối Loạn Chuyển Hóa (18 words about glucose, insulin, metabolic syndrome)

## Task 5: Series D — Pharmacology & Treatment (5 curriculums)

- [x] 5.1 Create `create_pharma_1_antibiotics.py` — Antibiotics & Anti-Infectives – Kháng Sinh & Thuốc Chống Nhiễm Trùng (18 words about antibiotic classes, resistance, antimicrobial therapy)
- [x] 5.2 Create `create_pharma_2_pain.py` — Pain Management & Analgesics – Giảm Đau & Thuốc Giảm Đau (18 words about analgesics, opioids, pain assessment)
- [x] 5.3 Create `create_pharma_3_cardiovascular.py` — Cardiovascular Drugs – Thuốc Tim Mạch (18 words about antihypertensives, statins, anticoagulants)
- [x] 5.4 Create `create_pharma_4_psychiatric.py` — Psychiatric Medications – Thuốc Tâm Thần (18 words about antidepressants, anxiolytics, psychopharmacology)
- [x] 5.5 Create `create_pharma_5_surgical.py` — Surgical Procedures & Recovery – Phẫu Thuật & Hồi Phục (18 words about surgical terms, anesthesia, postoperative care)

## Task 6: Series E — Medical Research & Evidence-Based Medicine (5 curriculums)

- [x] 6.1 Create `create_research_1_design.py` — Study Design & Methodology – Thiết Kế Nghiên Cứu (18 words about study types, variables, methodology)
- [x] 6.2 Create `create_research_2_trials.py` — Clinical Trials – Thử Nghiệm Lâm Sàng (18 words about trial phases, placebo, randomization)
- [x] 6.3 Create `create_research_3_biostatistics.py` — Biostatistics Basics – Thống Kê Y Sinh Cơ Bản (18 words about p-value, confidence interval, statistical significance)
- [x] 6.4 Create `create_research_4_journal.py` — Reading a Journal Article – Đọc Hiểu Bài Báo Khoa Học (18 words about abstract, methodology section, peer review)
- [x] 6.5 Create `create_research_5_systematic.py` — Systematic Reviews & Meta-Analyses – Tổng Quan Hệ Thống (18 words about meta-analysis, heterogeneity, evidence synthesis)

## Task 7: Execute Creation and Assembly

- [x] 7.1 Run all 25 curriculum creation scripts and record returned IDs
- [x] 7.2 Update orchestrator script with actual curriculum IDs, then run it to create collection, series, wire everything, and set display orders
- [x] 7.3 Run duplicate-check SQL queries for all 25 curriculums
- [x] 7.4 Verify content integrity: check all curriculums via `curriculum/getOne`, validate against content corruption rules

## Task 8: Documentation and Cleanup

- [x] 8.1 Create `medical-english-curriculum/README.md` with all curriculum IDs, collection/series IDs, SQL queries, creation method, and recreation context
- [x] 8.2 Delete all Python scripts and JSON files from the working directory (only README.md remains)
