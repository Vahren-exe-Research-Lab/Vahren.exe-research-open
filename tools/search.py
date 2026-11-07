#!/usr/bin/env python3
"""Search the openly shareable research dictionaries; no game binary or dependencies required."""
from __future__ import annotations
from pathlib import Path
import argparse,csv,json,sys

ROOT=Path(__file__).resolve().parent.parent
def rows(path,count):
 out=[]
 for line in path.read_text(encoding="utf-8-sig").splitlines():
  if not line.strip() or line.startswith("#"):continue
  fields=line.split("\t")
  if len(fields)!=count:raise ValueError(f"Malformed TSV {path.name}")
  out.append(fields)
 return out
def call_rows():
 with (ROOT/"reference/static_calls.tsv").open(encoding="utf-8-sig",newline="") as f:
  return list(csv.DictReader(f,delimiter="\t"))
def normalize_va(s):
 s=str(s).strip().upper()
 if s.startswith("VA:"):s=s[3:]
 if s.startswith("VAHREN.EXE+"):
  return f"0x{int(s[11:],16)+0x400000:08X}"
 return f"0x{int(s,16):08X}"
def search(action,query,limit=30):
 value=query.casefold()
 symbols=rows(ROOT/"symbols.tsv",6)
 fields=rows(ROOT/"structs.tsv",7)
 if action in ("search","symbols"):
  a=[dict(va=r[0],kind=r[1],name=r[2],summary=r[3],confidence=r[4],
          evidence_label=r[5]) for r in symbols if any(value in x.casefold() for x in r)]
 else:a=[]
 if action in ("search","fields"):
  b=[dict(struct=r[0],offset=r[1],type=r[2],name=r[3],summary=r[4],
          confidence=r[5],evidence_label=r[6]) for r in fields if any(value in x.casefold() for x in r)]
 else:b=[]
 if action in ("callers","callees"):
  key=normalize_va(query).casefold()
  col="callee_va" if action=="callers" else "caller_va"
  c=[row for row in call_rows() if row[col].casefold()==key]
 else:c=[]
 result={"symbols":a[:limit],"fields":b[:limit],"calls":c[:limit],
         "total_matches":{"symbols":len(a),"fields":len(b),"calls":len(c)},
         "note":"Retrieved entries retain original research confidence; raw evidence is not bundled."}
 return result
def main():
 p=argparse.ArgumentParser(description="Search Vahren.exe reverse-engineering research notes")
 p.add_argument("action",choices=("search","symbols","fields","callers","callees"))
 p.add_argument("query",help="Name, keyword, VA such as 0x0048D6A0")
 p.add_argument("--json",action="store_true",help="Machine-readable JSON output")
 p.add_argument("--limit",type=int,default=30,help="Maximum results per category (1..500)")
 args=p.parse_args()
 if not 1<=args.limit<=500:p.error("limit must be in 1..500")
 try:result=search(args.action,args.query,args.limit)
 except ValueError as exc:p.error(str(exc))
 try:sys.stdout.reconfigure(encoding="utf-8",errors="replace")
 except AttributeError:pass
 if args.json:
  print(json.dumps(result,ensure_ascii=False,indent=2));return
 for title,kind in (("Symbols","symbols"),("Memory fields","fields"),("Direct CALL records","calls")):
  section=result[kind]
  print(f"\n## {title}: showing {len(section)} of {result['total_matches'][kind]}")
  for row in section:
   if kind=="symbols":print(f"{row['va']} [{row['kind']}] {row['name']} — {row['summary'][:170]}")
   elif kind=="fields":print(f"{row['struct']}+{row['offset']} {row['name']} — {row['summary'][:170]}")
   else:print(f"{row['caller_va']} -> {row['callee_va']} (site {row['site_va']})")
if __name__=="__main__":main()
