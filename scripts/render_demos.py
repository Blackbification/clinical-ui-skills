#!/usr/bin/env python3
"""Optional demo renderer. Requires Playwright and a local Chromium executable."""
from pathlib import Path
import shutil
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    raise SystemExit('Playwright is required only to regenerate demo screenshots: pip install playwright')
ROOT=Path(__file__).resolve().parents[1]
chrome=shutil.which('chromium') or shutil.which('chromium-browser') or shutil.which('google-chrome')
if not chrome:
    raise SystemExit('Chromium/Chrome not found. Existing PNGs in examples are already committed.')
jobs=[
 ('demo-01-inpatient-worklist','vanilla',1440,900),('demo-01-inpatient-worklist','clinical-ui',1440,900),
 ('demo-02-patient-chart','vanilla',1440,900),('demo-02-patient-chart','clinical-ui',1440,900),
 ('demo-03-patient-app','vanilla',440,900),('demo-03-patient-app','clinical-ui',440,900),
]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path=chrome,args=['--no-sandbox','--disable-dev-shm-usage'])
    for folder,name,w,h in jobs:
        src=ROOT/'examples'/folder/f'{name}.html'; out=src.with_suffix('.png')
        page=browser.new_page(viewport={'width':w,'height':h})
        page.set_content(src.read_text(encoding='utf-8'),wait_until='load')
        page.screenshot(path=str(out),full_page=False)
        page.close(); print(out.relative_to(ROOT))
    browser.close()
