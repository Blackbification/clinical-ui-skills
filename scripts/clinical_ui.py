#!/usr/bin/env python3
"""Small stdlib-only convenience CLI for Clinical UI Skills."""
from pathlib import Path
import argparse,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
COMMANDS={
 'validate':['validate_skills.py'],
 'validate-evals':['validate_evals.py'],
 'evals':['run_evals.py'],
 'lint':['clinical_ui_lint.py'],
}
ap=argparse.ArgumentParser(); ap.add_argument('command',choices=COMMANDS); ap.add_argument('args',nargs=argparse.REMAINDER); a=ap.parse_args()
cmd=[sys.executable,str(ROOT/'scripts'/COMMANDS[a.command][0]),*a.args]
raise SystemExit(subprocess.call(cmd))
