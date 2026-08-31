#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
from eval_loader import load_evals
ROOT=Path(__file__).resolve().parents[1]; SKILLS=ROOT/'skills'; VERSION=(ROOT/'VERSION').read_text().strip()
NAME_RE=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
EXPECTED={'clinical-ui','anti-slop-core','clinician-dashboard','patient-chart','patient-management','clinical-forms','clinical-safety-ui','clinical-data-viz','patient-facing-ui','clinical-accessibility','clinical-ai-ui','clinical-ui-audit'}
def fmtext(text):
    if not text.startswith('---\n'): return ''
    end=text.find('\n---\n',4); return text[4:end] if end>=0 else ''
def val(fm,key):
    m=re.search(rf'^{re.escape(key)}:\s*(.+?)\s*$',fm,re.M); return m.group(1).strip().strip('"') if m else None
errors=[]; warnings=[]; dirs=sorted(p for p in SKILLS.iterdir() if p.is_dir())
if {d.name for d in dirs} != EXPECTED:
    errors.append(f'skill set mismatch: expected {sorted(EXPECTED)}, got {sorted(d.name for d in dirs)}')
for d in dirs:
    p=d/'SKILL.md'
    if not p.exists(): errors.append(f'{d.name}: missing SKILL.md'); continue
    text=p.read_text(encoding='utf-8'); fm=fmtext(text); name=val(fm,'name'); desc=val(fm,'description'); lic=val(fm,'license')
    if name!=d.name: errors.append(f'{d.name}: frontmatter name {name!r}')
    if not name or len(name)>64 or not NAME_RE.fullmatch(name or ''): errors.append(f'{d.name}: invalid name')
    if not desc or len(desc)>1024: errors.append(f'{d.name}: invalid description')
    desc_line=next((ln for ln in fm.splitlines() if ln.startswith('description:')), '')
    if not re.match(r'^description:\s*".*"\s*$', desc_line): errors.append(f'{d.name}: description must be quoted YAML string')
    if lic!='MIT': errors.append(f'{d.name}: expected MIT')
    if not re.search(r'^\s{2}author:\s*["\']?Juan Mora Delgado["\']?\s*$',fm,re.M): errors.append(f'{d.name}: missing author credit')
    if len(text.splitlines())>500: warnings.append(f'{d.name}: >500 lines')
try:
    data=load_evals(ROOT); ev=data.get('evals',[])
    if len(ev)<60: errors.append(f'expected >=60 evals, found {len(ev)}')
except Exception as e: errors.append(f'evals invalid: {e}')
manifest=json.loads((ROOT/'skills'/'manifest.json').read_text())
if set(manifest.get('presets',{}).get('all',[])) != EXPECTED: errors.append('skills/manifest.json all preset does not match expected suite')
if manifest.get('version') != VERSION: errors.append('manifest version does not match VERSION')
required=['README.md','LICENSE','CREDITS.md','CITATION.cff','CONTRIBUTING.md','CODE_OF_CONDUCT.md','SECURITY.md','SUPPORT.md','MANIFESTO.md','Makefile','benchmarks/README.md','benchmarks/rubric.json','.github/PULL_REQUEST_TEMPLATE.md','.github/workflows/validate.yml','docs/clinical-ui-challenge.md','assets/social-preview.png']
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'missing public-release file: {rel}')
lic=(ROOT/'LICENSE').read_text(errors='ignore') if (ROOT/'LICENSE').exists() else ''
if 'MIT License' not in lic or 'Juan Mora Delgado' not in lic: errors.append('LICENSE incorrect')
print('Clinical UI Skills validator\n============================'); print('Skills:',len(dirs))
if warnings:
    print('\nWarnings:'); [print(' -',x) for x in warnings]
if errors:
    print('\nErrors:'); [print(' -',x) for x in errors]; raise SystemExit(1)
print('\nPASS')
