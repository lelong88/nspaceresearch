import os, time, glob
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()

API = "https://api.soniox.com"
KEY = os.environ["SONIOX_API_KEY"]
HDR = {"Authorization": f"Bearer {KEY}"}

BASE_DIR = Path("meeting-audios")

CONTEXT_TEXT = Path("summary-mac.md").read_text()

# Extracted from glossary.md — keep in sync manually
CONTEXT_TERMS = [
    # Metrics & Formulas
    "VAR", "VaR", "Value at Risk", "FYP", "First Year Premium",
    "FYC", "First Year Commission", "RYP", "Renewal Year Premium",
    "APE", "Annual Premium Equivalent", "P13", "P19",
    "L12M", "L6M", "1mAA", "NR", "CAR", "CAFR", "OAFR",
    "CSV", "Cash Surrender Value", "net production",
    # Agency Hierarchy
    "FA", "Financial Advisor", "UM", "UM+", "Unit Manager",
    "SUM", "Senior Unit Manager", "DM", "SDM", "BM", "Branch Manager", "AM", "Area Manager",
    "SM", "SSM", "Sales Manager", "Senior Sales Manager",
    "PSM", "PSM+", "DRD", "SRD", "RD", "Regional Director",
    "AVP", "SAVP", "VP", "RH", "Regional Head",
    "CAO", "CAO-1", "CAO-2", "CAO-3", "CAO-4", "CAO-5", "CAO-6", "CAO-7",
    # Compensation & Bonus Components
    "payout", "override", "leader_override", "leader_activation",
    "leader_develop", "leader_develop_newagent", "leader_retention", "leader_newUM",
    "agt_NAB_FT", "agt_monthly", "agt_Mpro_monthly", "agt_quarterly",
    "agt_mstar", "M Star", "M-star", "agt_Mpro_yearly", "agt_referal",
    "Referral Bonus", "Monthly Production Bonus", "Quarterly Production Bonus",
    "Monthly Team Activation Bonus", "MMB",
    "New Agent Development Bonus", "New UM Coaching Bonus",
    "UM Retention Bonus", "SM Fixed Subsidy", "SM Retention Bonus",
    "MDRT", "MBA Pro", "Manulife Pro", "MPro",
    "deferred payment", "defer payment", "claw back", "clawback",
    "sign-on bonus", "cash advance", "clearance",
    # Schemes & Programs
    "GTF", "Growth Task Force", "GTF subsidy", "GTF Subsidy_DT",
    "MAC", "Manulife Agency Center", "Normal MAC", "Small MAC",
    "Big MAC", "Internal MAC", "GTF MAC",
    "Branch Model", "GA Model", "General Agency",
    "hybrid approach", "bonus contribution scheme", "financing scheme",
    # Risk & Controls
    "exposure", "exposure risk", "arbitrage", "arbitrage risk", "gaming",
    "trigger point", "trigger threshold", "benchmark",
    "freelook", "freelook period", "persistency",
    "DC", "Line1B", "Line 1B", "red flag", "suspension",
    "MOC", "ARC", "RCSC", "CIC check", "welcome call success rate",
    # MAC-Specific
    "office set-up subsidy", "monthly office allowance", "monthly office subsidy",
    "guarantee office subsidy", "catchup mechanism",
    "P13 modifier", "office quality modifier", "signage",
    "construction acceptance", "recruiter bonus", "COP", "CS",
    # Organizational & Operational
    "MVL", "Manulife Vietnam", "EMT", "ASBD", "ABM", "AMM", "APM", "AMT",
    "COS", "AMkt", "AMS System", "CAS System", "batch job files", "BD3",
    "PRE", "PREs", "CE", "CAPEX", "BAU", "YoY",
    "back-test", "back-testing", "sensitivity analysis",
    "inorganic growth", "inorganic recruitment", "organic", "spin-off",
    # Direct Team & VAR Calculation
    "direct team", "NTT", "indirect team", "VAR DT",
    "VAR DT Agency L12M", "FYP DT L12M", "%VAR DT/FYP DT", "%VAR/FYP Agency",
    "rolling 12 months", "zeroize",
    # Competitors
    "Pru", "Prudential", "Chubb", "Chubb Life", "Generali", "Gen", "FWD",
    "ICO", "GA", "GAD", "franchise model", "poaching",
    # Vietnamese terms mixed with English
    "tỷ", "tỉ", "triệu", "mil", "sạch sẽ", "nộp-hủy-nộp lại",
    "chức danh", "hợp đồng", "khách hàng", "đại lý", "chi nhánh",
    "tuyển dụng", "duy trì", "giữ chân", "trợ cấp", "nghiệm thu", "lũy kế",
    # Geographic references
    "Hanoi", "Ho Chi Minh City", "HCMC", "Hai Phong", "Da Nang", "Nghe An",
    "Thanh Hoa", "Quang Ninh", "Lam Dong", "Can Tho", "Yen Bai", "Hung Yen",
    "Phu Tho", "Vinh Phuc", "Quy Nhon", "Pleiku", "Tra Vinh", "Cam Pha",
    "Thu Duc", "Ecopark", "Dien Chau", "Vi Thanh", "Da Teh", "Quang Yen",
    "Dan Phuong", "Pho Noi", "Thanh Son",
    # Others
    "LUMA", "Steiner", "Rose/Thorn/Bud",
]

EXTENSIONS = {".m4a", ".mp3", ".mp4", ".wav", ".flac", ".ogg", ".aac", ".webm", ".amr", ".aiff", ".asf"}


def transcribe(audio_path: Path) -> str:
    name = audio_path.stem
    print(f"\n[{name}] Uploading...")
    with open(audio_path, "rb") as f:
        r = requests.post(f"{API}/v1/files", headers=HDR, files={"file": f})
    r.raise_for_status()
    file_id = r.json()["id"]

    print(f"[{name}] Creating transcription...")
    r = requests.post(f"{API}/v1/transcriptions", headers=HDR, json={
        "model": "stt-async-v3",
        "language_hints": ["vi"],
        "file_id": file_id,
        "context": {
            "general": [
                {"key": "domain", "value": "Insurance"},
                {"key": "topic", "value": "Manulife Agency Center (MAC) scheme"},
                {"key": "organization", "value": "Manulife Vietnam"},
            ],
            "text": CONTEXT_TEXT,
            "terms": CONTEXT_TERMS,
        },
    })
    r.raise_for_status()
    tid = r.json()["id"]

    print(f"[{name}] Waiting...", end="", flush=True)
    while True:
        r = requests.get(f"{API}/v1/transcriptions/{tid}", headers=HDR)
        r.raise_for_status()
        status = r.json()["status"]
        if status == "completed":
            break
        if status == "error":
            raise Exception(r.json().get("error_message", "Unknown error"))
        print(".", end="", flush=True)
        time.sleep(2)
    print(" done")

    r = requests.get(f"{API}/v1/transcriptions/{tid}/transcript", headers=HDR)
    r.raise_for_status()
    text = "".join(t["text"] for t in r.json()["tokens"]).strip()

    # cleanup
    requests.delete(f"{API}/v1/transcriptions/{tid}", headers=HDR)
    requests.delete(f"{API}/v1/files/{file_id}", headers=HDR)

    return text


def main():
    for project in sorted(BASE_DIR.iterdir()):
        if not project.is_dir():
            continue
        audio_dir = project / "files"
        out_dir = project / "transcripts"
        if not audio_dir.exists():
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        files = sorted(f for f in audio_dir.iterdir() if f.suffix.lower() in EXTENSIONS)
        if not files:
            continue
        print(f"\n=== {project.name} === ({len(files)} audio file(s))")
        for audio_path in files:
            out_path = out_dir / (audio_path.stem + ".txt")
            if out_path.exists():
                print(f"Skipping {audio_path.name} (already transcribed)")
                continue
            try:
                text = transcribe(audio_path)
                out_path.write_text(text)
                print(f"[{audio_path.stem}] Saved ({len(text)} chars)")
            except Exception as e:
                print(f"[{audio_path.stem}] ERROR: {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()
