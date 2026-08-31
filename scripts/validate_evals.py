#!/usr/bin/env python3
from pathlib import Path
import json
from eval_loader import load_evals
import sys
ROOT=Path(__file__).resolve().parents[1]
DATA=load_evals(ROOT)
items=DATA.get('evals',[])
errors=[]
if DATA.get('count') != len(items): errors.append('count metadata does not match evals length')
if len(items)<60: errors.append(f'expected >=60 evals, got {len(items)}')
ids=[x.get('id') for x in items]
if len(ids)!=len(set(ids)): errors.append('duplicate eval ids')
required={'id','category','risk','title','prompt','expected_output','files','assertions'}
for x in items:
    miss=required-set(x)
    if miss: errors.append(f'{x.get("id","?")}: missing {sorted(miss)}')
    if len(x.get('assertions',[]))<6: errors.append(f'{x.get("id","?")}: needs >=6 assertions')
    if x.get('risk') not in {'low','moderate','high'}: errors.append(f'{x.get("id","?")}: invalid risk')
print(f'ClinicalUIBench eval validator: {len(items)} evals')
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
from collections import Counter
print('Categories:',dict(sorted(Counter(x['category'] for x in items).items())))
print('PASS')
