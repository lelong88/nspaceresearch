import json
import os

results = {"en": [], "zh": [], "summary": {}}

for lang in ["en", "zh"]:
    for i in range(1, 101):
        folder = f"generated-prompts/{lang}/{i}"
        winner_file = f"{folder}/winner.txt"
        if os.path.exists(winner_file):
            with open(winner_file) as f:
                winner = f.read().strip()
            with open(f"{folder}/prompt.txt") as f:
                prompt = f.read().strip()[:100]
            results[lang].append({"index": i, "winner": winner, "prompt": prompt})

# Summary
en_omni = sum(1 for r in results["en"] if r["winner"] == "omni")
en_canvas = len(results["en"]) - en_omni
zh_omni = sum(1 for r in results["zh"] if r["winner"] == "omni")
zh_canvas = len(results["zh"]) - zh_omni

results["summary"] = {
    "en": {"omni": en_omni, "canvas": en_canvas, "total": len(results["en"])},
    "zh": {"omni": zh_omni, "canvas": zh_canvas, "total": len(results["zh"])},
    "total": {"omni": en_omni + zh_omni, "canvas": en_canvas + zh_canvas, "total": len(results["en"]) + len(results["zh"])}
}

with open("result.json", "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(json.dumps(results["summary"], indent=2))

# Visualization
s = results["summary"]
print("\n" + "="*50)
print("IMAGE GENERATION MODEL COMPARISON")
print("="*50)

def bar(label, omni, canvas, total):
    omni_pct = omni / total * 100
    canvas_pct = canvas / total * 100
    omni_bar = "█" * int(omni_pct / 2)
    canvas_bar = "█" * int(canvas_pct / 2)
    print(f"\n{label} (n={total})")
    print(f"  Omni   [{omni_bar:<50}] {omni:>3} ({omni_pct:.1f}%)")
    print(f"  Canvas [{canvas_bar:<50}] {canvas:>3} ({canvas_pct:.1f}%)")

bar("English", s["en"]["omni"], s["en"]["canvas"], s["en"]["total"])
bar("Chinese", s["zh"]["omni"], s["zh"]["canvas"], s["zh"]["total"])
bar("TOTAL", s["total"]["omni"], s["total"]["canvas"], s["total"]["total"])
