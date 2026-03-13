"""
Organize vi-en curriculums into collections and series.

Plan:
1. Create new series: "Tâm lý & Phát triển bản thân" for Tony Robbins + Leadership + Disagree and Commit
2. Create new series: "Raising Boys" for the boys curriculum
3. Link orphan series "Tour Guides" and "Dành cho bé gái 10-14 tuổi" and "Kids Playground" to collections
4. Add orphan curriculums to appropriate series
5. Move "Luyện nói CDC Huế" into Tour Guides series
6. Add Tony Robbins curriculums to the new Tâm lý series
7. Set display orders for collections
"""

import sys
import json
import requests
import time

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
BASE_COLLECTION = "https://helloapi.step.is/curriculum-collection"
BASE_SERIES = "https://helloapi.step.is/curriculum-series"
BASE_CURRICULUM = "https://helloapi.step.is/curriculum"

token = get_firebase_id_token(UID)
HEADERS = {"Content-Type": "application/json"}

def post(url, data):
    data["firebaseIdToken"] = token
    r = requests.post(url, json=data, headers=HEADERS)
    if r.status_code not in (200, 201):
        print(f"  ERROR {r.status_code}: {r.text[:200]}")
        return None
    print(f"  OK: {url.split('/')[-1]} -> {json.dumps({k:v for k,v in data.items() if k != 'firebaseIdToken'})[:120]}")
    return r.json()

# ============================================================
# IDs from database
# ============================================================

# Collections
FEATURED = "73e9d0aa"
HOC_TU_VUNG = "279d6843"       # Học từ vựng theo chủ đề
CHUYEN_NGHIEP = "89acc79b"     # Tiếng Anh Chuyên Nghiệp
THIEU_NHI = "bdccf5d1"         # Tiếng Anh Thiếu Nhi
FICTION = "97cee550"
HOC_THEO_TIN_TUC = "38fb6061"  # Học theo tin tức
COACHING = "95ea42ed"
LUYEN_THI = "72d8f528"

# Existing series
PARENTING = "01f6e173"
LEADERSHIP_BASIC = "8c79a794"
LEADERSHIP_INTER = "d50f44ae"
HEALTH_WELLNESS = "e24f29c4"
WORLD_NEWS = "3d836654"
TOUR_GUIDES = "1e6e8a71"
BIZ_OWNER = "85d6512e"
ALDER_HOUSE = "70b5bb22"
KIDS_PLAYGROUND = "1551b8a1"
BE_GAI_10_14 = "009194da"

# Curriculums
CDC_HUE = "51NO0BdwwGbPAqDP1"           # Luyện nói CDC Huế (orphan)
TONY_VALUES = "LjBS8YZO0iPVlz68"        # Know Your Values (Featured, no series)
TONY_DECISIONS = "5OJgQ49zI8skRPfX"      # Decide Your Destiny (Featured, no series)
RAISING_GIRLS_DISCOVER = "AdZb0U2XakdYER8C"  # Raising Girls: Khám phá bản thân (Thiếu Nhi, no series)
DISAGREE_COMMIT = "eI92kJ5GYlDjRzhM"    # Disagree and Commit (Leadership Inter)
LEADERSHIP_BEG = "3RXjZc2yirdyyvDF"     # Leadership Beginner (Leadership Basic)
OUTLIVE = "nG3KtewNxA7iEkut"            # Outlive (Health & Wellness)
GULF_CRISIS = "G1pwg72KEECMqy5s"        # Gulf Crisis (World News)
RAISING_GIRLS_10 = "XjB1XHqzg4PGeGTx"   # Raising Girls 10 tuổi (Parenting)
RAISING_GIRLS_1 = "fjvzoCdcoMLSjxx7"    # Raising Girls 1 tuổi (Parenting)
RAISING_BOYS_1 = "oIBdDjUpizHWtQTq"     # Raising Boys 1 tuổi (Parenting)
RAISING_GIRLS_EASY = "lFgOwSuIT2L9RK3l" # Raising Girls Easy Beginner (Kids Playground + bé gái 10-14)
HUE_TOUR = "EA1OBMOANK7hskWq"           # Introducing Huế (Tour Guides)
OPP_COST = "EX4E093ppEMsAlW8"           # Opportunity Cost (Biz Owner)

steps = []

def run_steps():
    for i, (desc, url, data) in enumerate(steps):
        print(f"\n[{i+1}/{len(steps)}] {desc}")
        post(url, data)
        time.sleep(0.15)

# ============================================================
# STEP 1: Create new series "Tâm lý & Phát triển bản thân"
# ============================================================
print("\n=== Creating new series: Tâm lý & Phát triển bản thân ===")
result = post(f"{BASE_SERIES}/create", {
    "title": "Tâm lý & Phát triển bản thân",
    "description": "Giá trị cá nhân, quyết định, lãnh đạo và làm việc nhóm",
    "isPublic": True,
})
TAM_LY_SERIES = result["id"] if result else None
print(f"  New series ID: {TAM_LY_SERIES}")

# ============================================================
# STEP 2: Create new series "Raising Boys"
# ============================================================
print("\n=== Creating new series: Raising Boys ===")
result = post(f"{BASE_SERIES}/create", {
    "title": "Raising Boys",
    "description": "Nuôi dạy con trai theo Steve Biddulph",
    "isPublic": True,
})
RAISING_BOYS_SERIES = result["id"] if result else None
print(f"  New series ID: {RAISING_BOYS_SERIES}")

time.sleep(0.3)

# ============================================================
# STEP 3: Build all operations
# ============================================================

# --- Populate Tâm lý series ---
if TAM_LY_SERIES:
    # Move Leadership Beginner from Leadership Basic to Tâm lý
    steps.append(("Remove Leadership Beginner from Leadership Basic series",
        f"{BASE_COLLECTION}/removeCurriculumFromSeries",
        {"curriculumSeriesId": LEADERSHIP_BASIC, "curriculumId": LEADERSHIP_BEG}))
    
    # Move Disagree and Commit from Leadership Inter to Tâm lý
    steps.append(("Remove Disagree and Commit from Leadership Intermediate series",
        f"{BASE_COLLECTION}/removeCurriculumFromSeries",
        {"curriculumSeriesId": LEADERSHIP_INTER, "curriculumId": DISAGREE_COMMIT}))
    
    # Add all 4 to Tâm lý series in order
    for cid, name in [
        (TONY_VALUES, "Know Your Values"),
        (TONY_DECISIONS, "Decide Your Destiny"),
        (DISAGREE_COMMIT, "Disagree and Commit"),
        (LEADERSHIP_BEG, "Leadership Beginner"),
    ]:
        steps.append((f"Add {name} to Tâm lý series",
            f"{BASE_COLLECTION}/addCurriculumToSeries",
            {"curriculumSeriesId": TAM_LY_SERIES, "curriculumId": cid}))
    
    # Link Tâm lý series to Học từ vựng theo chủ đề collection
    steps.append(("Link Tâm lý series to Học từ vựng theo chủ đề",
        f"{BASE_COLLECTION}/addSeriesToCollection",
        {"curriculumCollectionId": HOC_TU_VUNG, "curriculumSeriesId": TAM_LY_SERIES}))

# --- Move Raising Boys from Parenting to new Raising Boys series ---
if RAISING_BOYS_SERIES:
    steps.append(("Remove Raising Boys 1 tuổi from Parenting series",
        f"{BASE_COLLECTION}/removeCurriculumFromSeries",
        {"curriculumSeriesId": PARENTING, "curriculumId": RAISING_BOYS_1}))
    
    steps.append(("Add Raising Boys 1 tuổi to Raising Boys series",
        f"{BASE_COLLECTION}/addCurriculumToSeries",
        {"curriculumSeriesId": RAISING_BOYS_SERIES, "curriculumId": RAISING_BOYS_1}))
    
    # Link Raising Boys series to Tiếng Anh Thiếu Nhi
    steps.append(("Link Raising Boys series to Tiếng Anh Thiếu Nhi",
        f"{BASE_COLLECTION}/addSeriesToCollection",
        {"curriculumCollectionId": THIEU_NHI, "curriculumSeriesId": RAISING_BOYS_SERIES}))

# --- Add Raising Girls Khám phá bản thân to bé gái 10-14 series ---
steps.append(("Add Raising Girls Khám phá to bé gái 10-14 series",
    f"{BASE_COLLECTION}/addCurriculumToSeries",
    {"curriculumSeriesId": BE_GAI_10_14, "curriculumId": RAISING_GIRLS_DISCOVER}))

# --- Link orphan series to collections ---
# Tour Guides -> Tiếng Anh Chuyên Nghiệp
steps.append(("Link Tour Guides series to Tiếng Anh Chuyên Nghiệp",
    f"{BASE_COLLECTION}/addSeriesToCollection",
    {"curriculumCollectionId": CHUYEN_NGHIEP, "curriculumSeriesId": TOUR_GUIDES}))

# Dành cho bé gái 10-14 -> Tiếng Anh Thiếu Nhi
steps.append(("Link bé gái 10-14 series to Tiếng Anh Thiếu Nhi",
    f"{BASE_COLLECTION}/addSeriesToCollection",
    {"curriculumCollectionId": THIEU_NHI, "curriculumSeriesId": BE_GAI_10_14}))

# Kids Playground -> Tiếng Anh Thiếu Nhi
steps.append(("Link Kids Playground series to Tiếng Anh Thiếu Nhi",
    f"{BASE_COLLECTION}/addSeriesToCollection",
    {"curriculumCollectionId": THIEU_NHI, "curriculumSeriesId": KIDS_PLAYGROUND}))

# Parenting (now just Raising Girls) -> Tiếng Anh Thiếu Nhi
steps.append(("Link Parenting series to Tiếng Anh Thiếu Nhi",
    f"{BASE_COLLECTION}/addSeriesToCollection",
    {"curriculumCollectionId": THIEU_NHI, "curriculumSeriesId": PARENTING}))

# --- Add CDC Huế to Tour Guides series ---
steps.append(("Add CDC Huế to Tour Guides series",
    f"{BASE_COLLECTION}/addCurriculumToSeries",
    {"curriculumSeriesId": TOUR_GUIDES, "curriculumId": CDC_HUE}))

# --- Remove empty Leadership series from Học từ vựng (they'll be empty after moves) ---
steps.append(("Remove empty Leadership Basic series from Học từ vựng",
    f"{BASE_COLLECTION}/removeSeriesFromCollection",
    {"curriculumCollectionId": HOC_TU_VUNG, "curriculumSeriesId": LEADERSHIP_BASIC}))

steps.append(("Remove empty Leadership Intermediate series from Học từ vựng",
    f"{BASE_COLLECTION}/removeSeriesFromCollection",
    {"curriculumCollectionId": HOC_TU_VUNG, "curriculumSeriesId": LEADERSHIP_INTER}))

# --- Remove Parenting from Học từ vựng (moved to Thiếu Nhi) ---
steps.append(("Remove Parenting series from Học từ vựng",
    f"{BASE_COLLECTION}/removeSeriesFromCollection",
    {"curriculumCollectionId": HOC_TU_VUNG, "curriculumSeriesId": PARENTING}))

# --- Make Học theo tin tức public ---
steps.append(("Make Học theo tin tức public",
    f"{BASE_COLLECTION}/setIsPublic",
    {"id": HOC_THEO_TIN_TUC, "isPublic": True}))

# --- Set collection display orders ---
collection_orders = [
    (FEATURED, -1000),       # Featured always first
    (HOC_TU_VUNG, 100),     # Học từ vựng theo chủ đề
    (FICTION, 200),          # Fiction
    (THIEU_NHI, 300),       # Tiếng Anh Thiếu Nhi
    (CHUYEN_NGHIEP, 400),   # Tiếng Anh Chuyên Nghiệp
    (COACHING, 500),         # Coaching
    (HOC_THEO_TIN_TUC, 600),# Học theo tin tức
    (LUYEN_THI, 700),       # Luyện thi
]
for coll_id, order in collection_orders:
    steps.append((f"Set collection display order {order}",
        f"{BASE_COLLECTION}/setDisplayOrder",
        {"id": coll_id, "displayOrder": order}))

# --- Set series display orders within collections ---
# Học từ vựng: Tâm lý first, then Health
if TAM_LY_SERIES:
    steps.append(("Set Tâm lý series display order 100",
        f"{BASE_SERIES}/setDisplayOrder",
        {"id": TAM_LY_SERIES, "displayOrder": 100}))

steps.append(("Set Health & Wellness series display order 200",
    f"{BASE_SERIES}/setDisplayOrder",
    {"id": HEALTH_WELLNESS, "displayOrder": 200}))

# Tiếng Anh Thiếu Nhi: Parenting (Raising Girls) -> bé gái 10-14 -> Kids Playground -> Raising Boys
steps.append(("Set Parenting series display order 100",
    f"{BASE_SERIES}/setDisplayOrder",
    {"id": PARENTING, "displayOrder": 100}))

steps.append(("Set bé gái 10-14 series display order 200",
    f"{BASE_SERIES}/setDisplayOrder",
    {"id": BE_GAI_10_14, "displayOrder": 200}))

steps.append(("Set Kids Playground series display order 300",
    f"{BASE_SERIES}/setDisplayOrder",
    {"id": KIDS_PLAYGROUND, "displayOrder": 300}))

if RAISING_BOYS_SERIES:
    steps.append(("Set Raising Boys series display order 400",
        f"{BASE_SERIES}/setDisplayOrder",
        {"id": RAISING_BOYS_SERIES, "displayOrder": 400}))

# Rename Parenting series to "Raising Girls" since it only has girls now
steps.append(("Rename Parenting series to Raising Girls",
    f"{BASE_SERIES}/update",
    {"id": PARENTING, "title": "Raising Girls", "description": "Nuôi dạy con gái theo Steve Biddulph"}))

# ============================================================
# RUN
# ============================================================
print(f"\n=== Running {len(steps)} operations ===")
run_steps()
print("\n=== Done! ===")
