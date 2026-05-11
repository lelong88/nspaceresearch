"""Aggregate March 2026 VaR deep-dive (>=2000 USD bucket) by Rank / MBA / GTF / Note.

Source: slides/var-8th-draft/md/691900897856135049.md (Select review = N, 18 rows)
        slides/var-8th-draft/md/691900897856135049-2.md (Select review = Y, 22 rows, has Note col AR)
"""
from collections import defaultdict

# (unit, agt, rank, mba, gtf, var_thousand_vnd, note, page)
rows = [
    # Page 1: Select review = N (18 rows, no Note column shown)
    ("0TM57","AQ408","SUM",None,"N",50571,"(not shown)",1),
    ("08966","K4400","BM",None,"N",53963,"(not shown)",1),
    ("02206","65359","SDM",None,"N",56485,"(not shown)",1),
    ("0A386","BP718","SDM","P","Y",50391,"(not shown)",1),
    ("0CQ66","PN205","SUM","G","Y",191818,"(not shown)",1),
    ("0CL55","JM984","SUM",None,"N",63181,"(not shown)",1),
    ("01P77","2U1K7","DM","G","Y",151607,"(not shown)",1),
    ("0R996","AS425","UM","P","N",94090,"(not shown)",1),
    ("0G555","AS099","BM",None,"N",67009,"(not shown)",1),
    ("04843","E2768","AM","P","N",157609,"(not shown)",1),
    ("0S310","NW746","DM","G","Y",71989,"(not shown)",1),
    ("01627","11962","BM",None,"Y",85810,"(not shown)",1),
    ("0Y214","I23TD","SUM",None,"Y",68846,"(not shown)",1),
    ("0W422","ST074","DM","P","N",50841,"(not shown)",1),
    ("0H269","50753","BM","S","N",392664,"(not shown)",1),
    ("0M288","GT453","DM","P","N",83216,"(not shown)",1),
    ("0IR39","K4ZDB","UM",None,"Y",72906,"(not shown)",1),
    ("01P41","PB805","AM",None,"Y",180125,"(not shown)",1),
    # Page 2: Select review = Y (22 rows) - has Note column AR
    ("0IP71","K6051","UM",None,"N",106460,"Delay payment",2),
    ("0U109","U3229","DM","P","N",146744,"Diff FYP bonus and FYP VAR",2),
    ("02703","W6097","SUM",None,"N",89176,"Diff FYP bonus and FYP VAR",2),
    ("03143","31974","AM",None,"N",83374,"Diff FYP bonus and FYP VAR",2),
    ("0CY10","DM091","DM","S","Y",282875,"Diff FYP bonus and FYP VAR",2),
    ("0AQ57","JN734","SUM","S","N",75894,"Diff FYP bonus and FYP VAR",2),
    ("0I802","M4904","SDM",None,"N",70406,"Diff FYP bonus and FYP VAR",2),
    ("0W434","QA392","BM","P","N",193581,"Diff FYP bonus and FYP VAR",2),
    ("06327","R5967","SDM",None,"N",56901,"Diff FYP bonus and FYP VAR",2),
    ("0H822","S9792","BM",None,"N",217811,"Diff FYP bonus and FYP VAR",2),
    ("03149","31707","SDM",None,"N",81270,"Diff FYP bonus and FYP VAR",2),
    ("08163","M6535","SDM","P","N",223579,"Diff FYP bonus and FYP VAR",2),
    ("08394","39787","SDM",None,"N",111302,"Diff FYP bonus and FYP VAR",2),
    ("01625","17734","BM",None,"N",71008,"Diff FYP bonus and FYP VAR",2),
    ("02163","20883","BM",None,"N",72181,"Delay payment",2),
    ("03247","34242","DM",None,"N",68741,"-",2),
    ("0A587","A8966","BM","P","N",775023,"Diff FYP bonus and FYP VAR",2),
    ("0G750","BE567","SDM",None,"N",139687,"Diff FYP bonus and FYP VAR",2),
    ("0CH45","IM143","DM","P","N",85711,"Diff FYP bonus and FYP VAR",2),
    ("01160","10636","AM","P","N",94805,"Diff FYP bonus and FYP VAR",2),
    ("01211","11061","AM",None,"Y",67135,"-",2),
    ("03410","37562","SDM",None,"N",112595,"-",2),
]

USD_RATE = 25000  # 1 USD ~ 25,000 VND. VaR column units are '000 VND
def vnd_k_to_usd(v): return v * 1000 / USD_RATE

print(f"Total cases: {len(rows)}")
print(f"Total VaR ('000 VND): {sum(r[5] for r in rows):,}")
print(f"Total VaR (USD): {vnd_k_to_usd(sum(r[5] for r in rows)):,.0f}")
print()

def breakdown(key_fn, label):
    print(f"=== By {label} ===")
    counts = defaultdict(int)
    sums = defaultdict(int)
    for r in rows:
        k = key_fn(r)
        counts[k] += 1
        sums[k] += r[5]
    for k in sorted(counts.keys()):
        n = counts[k]
        s = sums[k]
        print(f"  {k:30s}  n={n:3d}  VaR={s:>12,} ('000 VND)  ~${vnd_k_to_usd(s):>9,.0f} USD")
    print()

breakdown(lambda r: r[2], "Rank (col D)")
breakdown(lambda r: r[3] if r[3] else "Non MBA Pro", "MBA (col E)")
breakdown(lambda r: "GTF" if r[4]=="Y" else "Non-GTF", "GTF (col F/H)")
breakdown(lambda r: r[6], "Note (col AR)")

# Cross-tabs
print("=== Rank x MBA (count) ===")
ranks = ["UM","SUM","DM","SDM","AM","BM"]
mbas = ["Non MBA Pro","P","S","G"]
print(f"{'':6s} " + " ".join(f"{m:13s}" for m in mbas) + " Total")
for rk in ranks:
    cells = []
    total = 0
    for m in mbas:
        c = sum(1 for r in rows if r[2]==rk and (r[3] or "Non MBA Pro")==m)
        cells.append(c); total += c
    print(f"{rk:6s} " + " ".join(f"{c:13d}" for c in cells) + f" {total:5d}")
print()

print("=== Rank x GTF (count) ===")
print(f"{'':6s} {'GTF':>6s} {'Non-GTF':>8s} Total")
for rk in ranks:
    g = sum(1 for r in rows if r[2]==rk and r[4]=="Y")
    n = sum(1 for r in rows if r[2]==rk and r[4]=="N")
    print(f"{rk:6s} {g:6d} {n:8d} {g+n:6d}")
print()

print("=== MBA x GTF (count) ===")
print(f"{'':14s} {'GTF':>6s} {'Non-GTF':>8s} Total")
for m in mbas:
    g = sum(1 for r in rows if (r[3] or "Non MBA Pro")==m and r[4]=="Y")
    n = sum(1 for r in rows if (r[3] or "Non MBA Pro")==m and r[4]=="N")
    print(f"{m:14s} {g:6d} {n:8d} {g+n:6d}")
print()

# Note x Rank, page 2 only (where Note column is visible)
p2 = [r for r in rows if r[7]==2]
print(f"=== Page 2 only (Select review=Y, n={len(p2)}): Note x Rank ===")
notes = sorted({r[6] for r in p2})
print(f"{'Note':35s} " + " ".join(f"{rk:>4s}" for rk in ranks) + " Total")
for nt in notes:
    cells = []
    tot = 0
    for rk in ranks:
        c = sum(1 for r in p2 if r[2]==rk and r[6]==nt)
        cells.append(c); tot += c
    print(f"{nt:35s} " + " ".join(f"{c:4d}" for c in cells) + f" {tot:5d}")
print()

# By MBA tier among GTF
print("=== Note x VaR sum (page 2) ===")
for nt in notes:
    s = sum(r[5] for r in p2 if r[6]==nt)
    n = sum(1 for r in p2 if r[6]==nt)
    print(f"  {nt:35s}  n={n:3d}  VaR={s:>12,} ('000 VND)  ~${vnd_k_to_usd(s):>9,.0f} USD")
