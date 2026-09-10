import importlib.util
from pathlib import Path
import tempfile
import unittest
spec = importlib.util.spec_from_file_location('checker', Path(__file__).parents[1]/'scripts/project.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class Checks(unittest.TestCase):
    def test_targets_pairing_and_readonly(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)
            for name in ['02_subplans','03_results']:
                (r/'00_knowledge'/name).mkdir(parents=True)
            (r/'00_knowledge/02_subplans/01_test.md').write_text('# Plan')
            (r/'00_knowledge/02_subplans/00_INDEX.md').write_text('# Index')
            (r/'target.md').write_text('# Target')
            (r/'read.md').write_text('[ok](target.md#section)\n[bad](missing.png)\n```\n[example](fake.md)\n```\n<!-- [hidden](no.md) -->')
            before={str(p):p.read_bytes() for p in r.rglob('*') if p.is_file()}
            result=m.check(r)
            self.assertEqual(len(result['errors']),2)
            (r/'missing.png').write_bytes(b'image')
            (r/'00_knowledge/03_results/01_test.md').write_text('# Result')
            self.assertFalse(m.check(r)['errors'])
            for p,b in before.items():self.assertEqual(Path(p).read_bytes(),b)

    def test_independent_repo_and_scope(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d); nested=r/'06_sync/other';nested.mkdir(parents=True)
            (nested/'.git').write_text('gitdir: external')
            (nested/'bad.md').write_text('[x](absent)')
            (r/'outside.md').write_text('[x](absent)')
            (r/'docs').mkdir();(r/'docs/ok.md').write_text('# OK')
            self.assertFalse(m.check(r,['docs'])['errors'])
            self.assertEqual(len(m.check(r)['errors']),1)

if __name__=='__main__':unittest.main()
