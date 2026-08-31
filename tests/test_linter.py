import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / 'scripts' / 'clinical_ui_lint.py'
spec = importlib.util.spec_from_file_location('clinical_ui_lint', MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class LinterTests(unittest.TestCase):
    def match_ids(self, text):
        return [rid for rid, sev, pat, msg in mod.RULES if pat.search(text)]

    def test_clickable_div_is_high(self):
        row = [r for r in mod.RULES if r[0] == 'clickable-div'][0]
        self.assertEqual(row[1], 'HIGH')
        self.assertRegex('<div onClick={open}>Patient</div>', row[2])

    def test_clickable_span_is_high(self):
        row = [r for r in mod.RULES if r[0] == 'clickable-span'][0]
        self.assertEqual(row[1], 'HIGH')

    def test_hidden_focus_detected(self):
        self.assertIn('hidden-focus', self.match_ids('className="focus:outline-none"'))

    def test_sparkle_motif_detected(self):
        self.assertIn('sparkle-ai', self.match_ids('<Sparkles />'))

    def test_gauge_detected(self):
        self.assertIn('gauge', self.match_ids('<RadialBarChart data={data} />'))

    def test_ai_power_copy_detected(self):
        self.assertIn('ai-powered-copy', self.match_ids('<p>AI-powered insights</p>'))

    def test_plain_semantic_button_has_no_clickable_div_signal(self):
        self.assertNotIn('clickable-div', self.match_ids('<button type="button">Open</button>'))

if __name__ == '__main__':
    unittest.main()
