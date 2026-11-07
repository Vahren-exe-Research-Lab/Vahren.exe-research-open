#!/usr/bin/env python3
"""Regression tests for the public-source safety guard."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from check_publication_safety import check_content, scan


class PublicSourceSafetyTests(unittest.TestCase):
    def test_current_repo_has_no_obvious_private_material(self):
        self.assertEqual(scan(), [])

    def test_raw_git_sha1_in_document_is_rejected(self):
        self.assertIn("40-character source fingerprint", check_content(
            Path("REF_TEST.md"), "git sha " + "a" * 40
        ))

    def test_raw_sha256_in_document_is_rejected(self):
        self.assertIn("64-character source fingerprint", check_content(
            Path("reference/facts.tsv"), "sha256=" + "A" * 64
        ))

    def test_opaque_evidence_reference_is_safe(self):
        self.assertEqual([], check_content(
            Path("reference/facts.tsv"), "source_evidence_id\nEVID-0007\n"
        ))

    def test_action_pin_is_not_mistaken_for_private_research_sha(self):
        self.assertEqual([], check_content(
            Path(".github/workflows/ci.yml"), "uses: actions/checkout@" + "a" * 40
        ))

    def test_windows_home_path_is_rejected(self):
        home = "C:" + "\\" + "Users" + "\\" + "Example" + "\\" + "Documents"
        self.assertIn("user-specific filesystem path", check_content(
            Path("README.md"), home
        ))

    def test_game_script_home_field_is_not_a_user_path(self):
        self.assertEqual([], check_content(
            Path("structs.tsv"), "Power fix（on/home/warlike）"
        ))


if __name__ == "__main__":
    unittest.main()
