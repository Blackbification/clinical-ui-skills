import json
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from eval_loader import load_evals
EXPECTED_SKILLS = {
    'clinical-ui','anti-slop-core','clinician-dashboard','patient-chart','patient-management',
    'clinical-forms','clinical-safety-ui','clinical-data-viz','patient-facing-ui',
    'clinical-accessibility','clinical-ai-ui','clinical-ui-audit'
}

class RepositoryTests(unittest.TestCase):
    def test_exact_skill_suite(self):
        skills = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
        self.assertEqual(skills, EXPECTED_SKILLS)

    def test_all_skills_are_mit_and_credit_creator(self):
        for p in (ROOT / 'skills').glob('*/SKILL.md'):
            text = p.read_text(encoding='utf-8')
            self.assertIn('license: MIT', text, p)
            self.assertIn('author: "Juan Mora Delgado"', text, p)
            self.assertLessEqual(len(text.splitlines()), 500, p)

    def test_mit_license_credits_creator(self):
        text = (ROOT / 'LICENSE').read_text(encoding='utf-8')
        self.assertIn('MIT License', text)
        self.assertIn('Copyright (c) 2026 Juan Mora Delgado', text)

    def test_citation_credits_creator_without_placeholder(self):
        text = (ROOT / 'CITATION.cff').read_text(encoding='utf-8')
        self.assertIn('family-names: "Mora Delgado"', text)
        self.assertIn('given-names: "Juan"', text)
        self.assertIn('license: MIT', text)
        self.assertNotIn('OWNER', text)

    def test_seventy_two_unique_evals(self):
        data = load_evals(ROOT)
        ev = data['evals']
        self.assertEqual(len(ev), 72)
        self.assertEqual(data['count'], 72)
        self.assertEqual(len({x['id'] for x in ev}), 72)
        self.assertTrue(data['synthetic_data_only'])
        for x in ev:
            self.assertGreaterEqual(len(x['assertions']), 6, x['id'])

    def test_eval_category_coverage(self):
        data = load_evals(ROOT)
        cats = {x['category'] for x in data['evals']}
        self.assertEqual(cats, {'dashboard','patient-chart','patient-management','forms','data-viz','patient-facing','accessibility','safety','ai','responsive'})

    def test_demo_artifacts_exist(self):
        for folder in ['demo-01-inpatient-worklist','demo-02-patient-chart','demo-03-patient-app']:
            d = ROOT / 'examples' / folder
            for name in ['vanilla.html','clinical-ui.html','vanilla.png','clinical-ui.png','comparison.png']:
                p=d/name
                self.assertTrue(p.exists(), p)
                self.assertGreater(p.stat().st_size, 100, p)

    def test_skill_local_references_exist(self):
        import re
        for skill in (ROOT / 'skills').iterdir():
            if not skill.is_dir(): continue
            text=(skill/'SKILL.md').read_text(encoding='utf-8')
            for rel in re.findall(r'`((?:references|scripts)/[^`]+)`', text):
                self.assertTrue((skill/rel).exists(), f'{skill.name}: missing local reference {rel}')

    def test_public_release_files_exist(self):
        required = ['README.md','MANIFESTO.md','GOVERNANCE.md','CONTRIBUTING.md','CODE_OF_CONDUCT.md','SECURITY.md','SUPPORT.md','benchmarks/README.md','benchmarks/rubric.json','benchmarks/submission.schema.json','assets/social-preview.png','.github/workflows/validate.yml','.github/PULL_REQUEST_TEMPLATE.md']
        for rel in required: self.assertTrue((ROOT/rel).exists(), rel)

    def test_sample_benchmark_scores(self):
        proc = subprocess.run([sys.executable, str(ROOT/'scripts'/'score_submission.py'), str(ROOT/'benchmarks'/'sample-submission.json')], capture_output=True, text=True, check=True)
        data=json.loads(proc.stdout)
        self.assertEqual(data['total_score'], 88)
        self.assertEqual(data['ai_slop_score'], 1)

    def test_installer_patient_preset(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'skills'
            subprocess.run([sys.executable,str(ROOT/'scripts'/'install_skills.py'),'--target',str(target),'--preset','patient'],check=True,capture_output=True,text=True)
            installed={p.name for p in target.iterdir() if p.is_dir()}
            self.assertIn('patient-facing-ui',installed)
            self.assertIn('clinical-accessibility',installed)
            self.assertIn('clinical-ui-audit',installed)
            self.assertNotIn('patient-management',installed)

if __name__ == '__main__':
    unittest.main()
