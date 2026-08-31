#!/usr/bin/env python3
from pathlib import Path
import argparse,json
from eval_loader import load_evals
ROOT=Path(__file__).resolve().parents[1]
D=load_evals(ROOT)
ap=argparse.ArgumentParser(); ap.add_argument('--category'); ap.add_argument('--id'); ap.add_argument('--json',action='store_true'); ap.add_argument('--list',action='store_true'); a=ap.parse_args()
items=D['evals']
if a.category: items=[x for x in items if x['category']==a.category]
if a.id: items=[x for x in items if x['id']==a.id]
if a.json: print(json.dumps(items,indent=2,ensure_ascii=False)); raise SystemExit
if a.list:
    for e in items: print(f'{e["id"]:24} {e["category"]:20} {e["risk"]:8} {e["title"]}')
    raise SystemExit
for e in items:
    print(f'## {e["id"]} — {e["title"]} [{e["category"]} / {e["risk"]}]\n{e["prompt"]}\n\nExpected:\n{e["expected_output"]}\n\nAssertions:')
    for x in e['assertions']: print('-',x)
    print()
