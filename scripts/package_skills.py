#!/usr/bin/env python3
from pathlib import Path
import argparse,json,shutil,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'skills'/'manifest.json').read_text())
ap=argparse.ArgumentParser(); ap.add_argument('--preset',choices=sorted(M['presets']),default='all'); ap.add_argument('--out'); a=ap.parse_args()
out=Path(a.out or f'clinical-ui-skills-{M["version"]}-{a.preset}.zip')
out.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory() as td:
    base=Path(td)/f'clinical-ui-skills-{a.preset}'; base.mkdir()
    for name in M['presets'][a.preset]: shutil.copytree(ROOT/'skills'/name,base/name)
    (base/'README.txt').write_text(f'Clinical UI Skills {M["version"]} — preset: {a.preset}\nCreated by {M["author"]}. MIT License.\n',encoding='utf-8')
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for p in base.rglob('*'):
            if p.is_file(): z.write(p,p.relative_to(base.parent))
print(out)
