#!/usr/bin/env python3
from pathlib import Path
import json,sys
from validate_submission import validate
ROOT=Path(__file__).resolve().parents[1]
R=json.loads((ROOT/'benchmarks'/'rubric.json').read_text())
def score(d):
    scores=dict(d['scores']); findings=d.get('findings',[]); flags=d.get('flags',{})
    high_safety=sum(1 for f in findings if f.get('severity')=='HIGH' and f.get('category') in {'safety','safety-error-resistance'})
    if high_safety>=2: scores['safety_error_resistance']=min(scores['safety_error_resistance'],R['caps']['two_high_safety_dimension_max'])
    if flags.get('inaccessible_primary_task'): scores['accessibility']=min(scores['accessibility'],R['caps']['inaccessible_primary_task_accessibility_max'])
    total=sum(scores.values()); blockers=sum(1 for f in findings if f.get('severity')=='BLOCKER')
    if blockers: total=min(total,R['caps']['unresolved_blocker_total_max'])
    return {'submission_id':d['submission_id'],'eval_id':d['eval_id'],'condition':d['condition'],'model':d['model'],'scores_after_caps':scores,'total_score':total,'ai_slop_score':d['ai_slop_score'],'blockers':blockers,'high_findings':sum(1 for f in findings if f.get('severity')=='HIGH')}
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('usage: score_submission.py submission.json')
    d,errors=validate(sys.argv[1])
    if errors:
        print('\n'.join('ERROR: '+x for x in errors)); raise SystemExit(1)
    print(json.dumps(score(d),indent=2))
