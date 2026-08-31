#!/usr/bin/env python3
from pathlib import Path
import argparse,json,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=json.loads((ROOT/'skills'/'manifest.json').read_text(encoding='utf-8'))
PRESETS=MANIFEST['presets']
ap=argparse.ArgumentParser(description='Install Clinical UI Skills into an agent skill directory.')
ap.add_argument('--target',required=True,help='Destination skill directory, e.g. .claude/skills')
ap.add_argument('--preset',choices=sorted(PRESETS),default='all')
ap.add_argument('--force',action='store_true')
a=ap.parse_args(); target=Path(a.target); target.mkdir(parents=True,exist_ok=True)
installed=[]
for name in PRESETS[a.preset]:
    src=ROOT/'skills'/name; dst=target/name
    if dst.exists():
        if not a.force:
            print(f'ERROR: {dst} exists; use --force to replace',file=sys.stderr); raise SystemExit(2)
        shutil.rmtree(dst)
    shutil.copytree(src,dst); installed.append(name)
print(f'Installed {len(installed)} skills ({a.preset}) into {target}')
for x in installed: print(' -',x)
