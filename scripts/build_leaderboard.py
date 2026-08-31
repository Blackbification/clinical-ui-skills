#!/usr/bin/env python3
from pathlib import Path
import argparse,csv,json
from validate_submission import validate
from score_submission import score
ap=argparse.ArgumentParser(); ap.add_argument('directory'); ap.add_argument('--out',default='benchmarks/leaderboard.csv'); a=ap.parse_args()
rows=[]
for p in sorted(Path(a.directory).glob('*.json')):
    d,errors=validate(p)
    if errors:
        print(f'SKIP {p}: {errors[0]}'); continue
    r=score(d); r['date']=d.get('date',''); rows.append(r)
fields=['submission_id','eval_id','condition','model','total_score','ai_slop_score','blockers','high_findings','date']
out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
with out.open('w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows({k:r.get(k,'') for k in fields} for r in sorted(rows,key=lambda x:(-x['total_score'],x['ai_slop_score'])))
print(f'Wrote {len(rows)} rows to {out}')
