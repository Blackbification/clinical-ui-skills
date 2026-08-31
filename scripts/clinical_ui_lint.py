#!/usr/bin/env python3
"""Heuristic source linter. It cannot determine clinical safety, usability or WCAG conformance."""
from pathlib import Path
import argparse,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
EXTS={'.tsx','.jsx','.ts','.js','.vue','.svelte','.html','.css','.scss'}
RAW=json.loads((ROOT/'scripts'/'lint_rules.json').read_text(encoding='utf-8'))
RULES=[(x['id'],x['severity'],re.compile(x['pattern'],re.I),x['message']) for x in RAW]

def files(path):
    p=Path(path)
    if p.is_file(): return [p] if p.suffix.lower() in EXTS else []
    return [x for x in p.rglob('*') if x.is_file() and x.suffix.lower() in EXTS and not {'node_modules','.next','dist','build'}.intersection(x.parts)]

def lint(path):
    out=[]
    for f in files(path):
        text=f.read_text(encoding='utf-8',errors='ignore')
        for rid,sev,pat,msg in RULES:
            for m in pat.finditer(text):
                out.append({'rule':rid,'severity':sev,'file':str(f),'line':text.count('\n',0,m.start())+1,'message':msg})
    for rule,threshold,severity,msg in [('large-radius-tailwind',8,'MEDIUM','large/full-radius occurrences'),('full-rounded-repetition',12,'MEDIUM','pill-style occurrences')]:
        by={}
        for x in out:
            if x['rule']==rule: by[x['file']]=by.get(x['file'],0)+1
        for f,n in by.items():
            if n>=threshold: out.append({'rule':rule+'-repetition','severity':severity,'file':f,'line':None,'message':f'{n} {msg}. Inspect repetitive component language and semantic compression.'})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path'); ap.add_argument('--json',action='store_true'); ap.add_argument('--fail-on',choices=['HIGH','MEDIUM','LOW']); a=ap.parse_args()
    out=lint(a.path)
    if a.json: print(json.dumps({'count':len(out),'findings':out},indent=2))
    else:
        print('Clinical UI heuristic lint\n==========================')
        if not out: print('No heuristic signals found.')
        for x in out:
            loc=f'{x["file"]}:{x["line"]}' if x['line'] else x['file']
            print(f'[{x["severity"]}] {x["rule"]} — {loc}\n  {x["message"]}')
        print(f'\n{len(out)} finding(s). Warnings require human inspection; they are not safety/design verdicts.')
    if a.fail_on:
        rank={'LOW':1,'MEDIUM':2,'HIGH':3}
        if any(rank[x['severity']]>=rank[a.fail_on] for x in out): sys.exit(1)
if __name__=='__main__': main()
