#!/usr/bin/env python3
"""Sanity checks for unattended contributions and live search-site regeneration."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent


class UnattendedContributionsTests(unittest.TestCase):
    def test_auto_merger_is_event_and_schedule_driven(self):
        workflow = (ROOT / ".github/workflows/auto-merge.yml").read_text(encoding="utf-8")
        self.assertIn("pull_request_target:", workflow)
        self.assertIn("schedule:", workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("pull-requests: write", workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("merge_method=squash", workflow)

    def test_privileged_merger_does_not_checkout_pr_content(self):
        workflow = (ROOT / ".github/workflows/auto-merge.yml").read_text(encoding="utf-8")
        self.assertNotIn("uses: actions/checkout@", workflow)
        self.assertNotIn("git checkout", workflow)
        self.assertNotIn("gh pr checkout", workflow)
        self.assertIn('[[ "$number" =~ ^[0-9]+$ ]]', workflow)

    def test_merge_explicitly_dispatches_site_and_checks(self):
        workflow = (ROOT / ".github/workflows/auto-merge.yml").read_text(encoding="utf-8")
        self.assertIn("for workflow in pages.yml research-ci.yml security.yml", workflow)
        self.assertIn("actions/workflows/$workflow/dispatches", workflow)

    def test_site_regenerates_index_before_publication(self):
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        generate = pages.index("python -B tools/build_reference.py")
        prepare = pages.index("python -B tools/prepare_docs_site.py")
        self.assertLess(generate, prepare)
        sources = (ROOT / "tools/prepare_docs_site.py").read_text(encoding="utf-8")
        self.assertIn('ROOT / "AUTO_MERGE.md"', sources)
        self.assertIn('REPORTS = sorted(ROOT.glob("REF_*.md"))', sources)


if __name__ == "__main__":
    unittest.main()
