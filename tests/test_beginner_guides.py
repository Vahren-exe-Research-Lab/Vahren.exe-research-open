"""Entry-point regression tests for the public research site's beginner guides."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent
GUIDES = (
    "getting-started.md",
    "by-goal.md",
    "glossary.md",
    "contributing.md",
    "reading-research.md",
    "first-lookup.md",
)


class BeginnerGuideTests(unittest.TestCase):
    def test_all_guides_have_title_and_navigation(self):
        for name in GUIDES:
            with self.subTest(page=name):
                path = ROOT / "guides" / name
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# "))
                self.assertIn("次に読む", text)

    def test_editable_homepage_links_to_beginner_and_expert_routes(self):
        home = (ROOT / "HOME.md").read_text(encoding="utf-8")
        for name in GUIDES:
            self.assertIn("guides/" + name, home)
        self.assertIn("reference/README.md", home)
        self.assertIn("/wiki", home)

    def test_site_navigation_and_deploy_triggers_include_guides(self):
        mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        for name in GUIDES:
            self.assertIn("guides/" + name, mkdocs)
        self.assertIn('"HOME.md"', pages)
        self.assertIn('"guides/**"', pages)

    def test_site_preparer_stages_home_and_guides_without_link_breakage(self):
        command = [sys.executable, "-B", str(ROOT / "tools/prepare_docs_site.py")]
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=80)
        self.assertEqual(run.returncode, 0, run.stderr)
        staged = ROOT / "docs_generated"
        self.assertTrue((staged / "index.md").is_file())
        self.assertTrue((staged / "GUIDE.md").is_file())
        self.assertIn("初めての方へ", (staged / "index.md").read_text(encoding="utf-8"))
        for name in GUIDES:
            self.assertTrue((staged / "guides" / name).is_file())
        beginner = (staged / "guides" / "getting-started.md").read_text(encoding="utf-8")
        self.assertNotIn("(../README.md)", beginner)
        # Root README links are rewritten to the MkDocs guide name.
        self.assertTrue((staged / "guides" / "getting-started.md").exists())


if __name__ == "__main__":
    unittest.main()
