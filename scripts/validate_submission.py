#!/usr/bin/env python3
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
R=json.loads((ROOT/'benchmarks'/'rubric.json').read_text())
required={'submission_id','eval_id','condition','model','scores','ai_slop_score','findings','evidence'}
def validate(path):
    d=json.loads(Path(path).read_text(encoding='utf-8')); errors=[]
    miss=required-set(d); errors += [f'missing {x}' for x in sorted(miss)]
    scores=d.get('scores',{})
    for key,spec in R['dimensions'].items():
        if key not in scores: errors.append(f'missing score {key}'); continue
        v=scores[key]
        if not isinstance(v,(int,float)) or not 0<=v<=spec['max']: errors.append(f'{key} must be 0..{spec["max"]}')
    ai=d.get('ai_slop_score')
    if not isinstance(ai,(int,float)) or not 0<=ai<=10: errors.append('ai_slop_score must be 0..10')
    for i,f in enumerate(d.get('findings',[])):
        if f.get('severity') not in {'BLOCKER','HIGH','MEDIUM','LOW'}: errors.append(f'finding {i}: invalid severity')
    return d,errors
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('usage: validate_submission.py submission.json')
    _,errors=validate(sys.argv[1])
    if errors:
        print('\n'.join('ERROR: '+x for x in errors)); raise SystemExit(1)
    print('PASS')
