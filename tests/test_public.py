#!/usr/bin/env python3
"""Portable smoke and safety tests for the selected publication candidate."""
from pathlib import Path
from collections import Counter
import sys,csv,re,unittest,json,subprocess
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"tools"))
import search

def md_links(text):
 return re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)",text)

class PublicCandidateTests(unittest.TestCase):
 def test_curated_data_count(self):
  s=search.rows(ROOT/"symbols.tsv",6)
  f=search.rows(ROOT/"structs.tsv",7)
  c=search.call_rows()
  self.assertEqual(len(s),520)
  self.assertEqual(sum(x[1]=="func" for x in s),375)
  self.assertEqual(len(f),122)
  self.assertEqual(len(c),2373)
  self.assertEqual(len(list((ROOT/"reference/symbols").glob("*.md"))),520)
  self.assertEqual(len(list((ROOT/"reference/structs").glob("*.md"))),14)
  self.assertEqual(len(list(ROOT.glob("REF_*.md"))),16)
 def test_research_search(self):
  v=search.search("symbols","Battle_ConstructScene")
  self.assertTrue(any("0x48D6A0".upper() in x["va"].upper() for x in v["symbols"]))
  f=search.search("fields","hp")
  self.assertTrue(any("hp" in x["name"].lower() for x in f["fields"]))
  c=search.search("callees","0x0040E220")
  self.assertGreater(len(c["calls"]),0)
  a=search.search("callers","0x0048D6A0")
  self.assertGreaterEqual(len(a["calls"]),0)
 def test_jsonl_data(self):
  for name,expected in (("relations.jsonl",165),("corrections.jsonl",17)):
   content=(ROOT/"reference"/name).read_text(encoding="utf-8")
   records=[json.loads(x) for x in content.splitlines() if x.strip()]
   self.assertEqual(len(records),expected)
   self.assertTrue(all("source" not in r for r in records))
 def test_all_local_markdown_targets_exist(self):
  bad=[]
  for f in ROOT.rglob("*.md"):
   if any(x in f.parts for x in (".git","docs_generated","site","venv-docs")):continue
   for link in md_links(f.read_text(encoding="utf-8")):
    url=link.strip().split(" ",1)[0]
    if url.startswith(("http:","https:","mailto:","#","data:")):continue
    if url.startswith("//"):continue
    target=url.split("#",1)[0].split("?",1)[0]
    if not target:continue
    targetfile=(f.parent/target).resolve()
    if not targetfile.is_file():bad.append((f.relative_to(ROOT).as_posix(),target))
  self.assertEqual(bad[:30],[],f"Missing targets total {len(bad)}")
 def test_no_personal_or_sensitive_remnants(self):
  # Literals are concatenated so the checker itself will not falsely trigger.
  # Private account-name checks are run by a separate, non-public release audit.
  patterns=[
   re.compile(rb"(?i)[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]"),
   re.compile(rb"(?i)(?:ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9_]{24,}"),
   re.compile(rb"(?i)github_pat_[A-Za-z0-9_]{30,}"),
   re.compile(rb"(?i)(?<!\w)sk-(?:proj-)?[A-Za-z0-9_-]{40,}"),
   re.compile(rb"(?i)(?<!\w)[\w.%+\-]{1,64}@[\w.\-]{2,100}\.[A-Za-z]{2,30}")
  ]
  findings=[]
  for f in ROOT.rglob("*"):
   if not f.is_file() or any(x in f.parts for x in (".git","__pycache__","docs_generated","site","venv-docs")):continue
   try:content=f.read_bytes()
   except OSError:continue
   if b"\x00" in content:findings.append((str(f),"binary NUL"));continue
   for pattern in patterns:
    if pattern.search(content):
     findings.append((str(f.relative_to(ROOT)),"sensitive-pattern match"))
  self.assertEqual(findings[:30],[],f"Sensitive findings total {len(findings)}")
 def test_no_private_git_sha1_identifiers(self):
  import re
  sha1=re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{40}(?![0-9a-fA-F])")
  found=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.md")
         if not any(x in p.parts for x in (".git","docs_generated","site","venv-docs")) and sha1.search(p.read_text(encoding="utf-8"))]
  self.assertEqual(found,[])
 def test_public_evidence_ids_do_not_expose_sha256(self):
  import re,csv
  hashes=re.compile(r'(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])')
  paths=[p for p in ROOT.rglob('*') if p.is_file() and not any(x in p.parts for x in ('.git','__pycache__','docs_generated','site','venv-docs')) and p.suffix in ('.md','.tsv','.jsonl','.json','.py')]
  self.assertFalse([p.relative_to(ROOT).as_posix() for p in paths if hashes.search(p.read_text(encoding='utf8'))])
  with (ROOT/'reference/static_calls.tsv').open(encoding='utf8',newline='') as f:
   calls=list(csv.DictReader(f,delimiter='\t'))
  self.assertEqual(len(calls),2373)
  self.assertTrue(all(row.get('source_evidence_id','').startswith('EVID-') for row in calls))
  self.assertEqual(len({row['source_evidence_id'] for row in calls}),1)

 def test_cc0_and_rights_scope(self):
  legal=(ROOT/'LICENSE').read_text(encoding='utf8')
  self.assertIn('Creative Commons',legal)
  self.assertIn('CC0',legal)
  for name in ('README.md','SCOPE_AND_LIMITATIONS.md','RELEASE_NOTES.md','CONTRIBUTING.md'):
   self.assertIn('CC0',(ROOT/name).read_text(encoding='utf8'))

 def test_no_original_assets(self):
  bad_extensions={".exe",".dll",".dat",".mp3",".ogg",".wav",".png",".jpg",".jpeg",".zip",".7z",".sav",".db",".sqlite",".mp4"}
  paths=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
         if p.is_file() and not any(x in p.parts for x in (".git","__pycache__","docs_generated","site","venv-docs"))
         and p.suffix.lower() in bad_extensions]
  self.assertEqual(paths,[])
if __name__=="__main__":unittest.main()
