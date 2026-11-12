#!/usr/bin/env python3
"""Rebuild public-ready GitHub pages from curated research tables (Python stdlib only)."""
from pathlib import Path
from collections import defaultdict
import csv,json

ROOT=Path(__file__).resolve().parent.parent
REF=ROOT/"reference"

def md(x):
 return str(x or "").strip().replace("\r"," ").replace("\n"," ").replace("|",r"\|").replace("<","&lt;").replace(">","&gt;")

def read_tsv(file,count):
 rows=[]
 for line in (ROOT/file).read_text(encoding="utf-8-sig").splitlines():
  if not line.strip() or line.startswith("#"): continue
  f=line.split("\t")
  if len(f)!=count:raise ValueError("invalid TSV "+file)
  rows.append(f)
 return rows

def jsonl(file):
 return [json.loads(x) for x in (ROOT/file).read_text(encoding="utf-8-sig").splitlines() if x.strip()]

def norm(x):return f"0x{int(x,16):08X}"
def stem(x):return f"{int(x,16):08X}.md"

def build():
 syms=read_tsv("symbols.tsv",6)
 fields=read_tsv("structs.tsv",7)
 calls=list(csv.DictReader((REF/"static_calls.tsv").open(encoding="utf-8-sig",newline=""),delimiter="\t"))
 rel=jsonl("reference/relations.jsonl")
 fixes=jsonl("reference/corrections.jsonl")
 assert (len(syms),len(fields),len(rel),len(fixes))==(520,122,165,17)
 assert len(calls)>2000
 dic={norm(x[0]):x for x in syms}
 groups=defaultdict(list)
 for x in fields:groups[x[0]].append(x)
 ins,outs=defaultdict(list),defaultdict(list)
 for call in calls:
  outs[norm(call["caller_va"])].append(call)
  ins[norm(call["callee_va"])].append(call)
 rels=defaultdict(list)
 corrs=defaultdict(list)
 for x in rel:
  rels[x.get("subject")].append(x)
  rels[x.get("object")].append(x)
 for x in fixes:corrs[x.get("subject")].append(x)
 (REF/"symbols").mkdir(exist_ok=True,parents=True)
 (REF/"structs").mkdir(exist_ok=True,parents=True)
 def link(address):
  v=norm(address)
  rec=dic.get(v)
  return f"[{md(rec[2])}](../symbols/{stem(v)})" if rec else v

 index=["# 関数・アドレス事典","",
  "> 迫真戦記 ver0.67 の研究用辞書です。静的解析・既存研究報告の情報であり、すべて実機確認済みではありません。",
  "> 原作EXE、非公開の研究原本、Git履歴は収録していません。",
  "",
  f"収録：アドレス **{len(syms)}項目**（関数 **{sum(x[1]=='func' for x in syms)}件**）、構造体フィールド **{len(fields)}件**、直接CALL **{len(calls)}レコード**。",
  "",
  "## 関数・アドレス一覧","",
  "| VA | 種別 | 名称 | 概要 |","|---|---|---|---|"]
 for va,kind,name,summary,conf,source in sorted(syms,key=lambda x:int(x[0],16)):
  key=norm(va)
  index.append(f"| [{key}](symbols/{stem(va)}) | {md(kind)} | {md(name)} | {md(summary)[:200]} |")
  out=[f"# {md(name)} — {key}","",md(summary),"",
   f"- 種別：{md(kind)}",f"- 記録上の確度：{md(conf)}",
   f"- 元の研究出典表記：{md(source)}（原文・実測証拠が非公開の場合あり）",
   f"- [機械可読辞書](../../symbols.tsv)","",
   "## 直接CALL（静的索引）","",
   "直接CALLのみ。間接呼出しや実行時の到達、パラメータ・副作用の完全な裏付けではありません。","",
   "### 呼び出し元",""]
  source_calls=ins.get(key,[])
  out += [f"- {link(x['caller_va'])} — site {md(x['site_va'])}" for x in source_calls[:250]] if source_calls else ["記録なし。"]
  if len(source_calls)>250:out.append(f"- （以下{len(source_calls)-250}件はTSV参照）")
  out+=["","### 呼び出し先",""]
  target_calls=outs.get(key,[])
  out += [f"- {link(x['callee_va'])} — site {md(x['site_va'])}" for x in target_calls[:250]] if target_calls else ["記録なし。"]
  if len(target_calls)>250:out.append(f"- （以下{len(target_calls)-250}件はTSV参照）")
  for record in rels.get("va:"+key,[]):
   if "## 研究上の関係" not in out:out+=["","## 研究上の関係",""]
   out.append("- "+md(record.get("predicate"))+"："+md(record.get("summary"))+
              "（"+md(record.get("confidence"))+"）")
  for record in corrs.get("va:"+key,[]):
   if "## 訂正" not in out:out+=["","## 訂正",""]
   out.append("- "+md(record.get("current_interpretation")))
  out+=["","[事典の一覧に戻る](../README.md)",""]
  (REF/"symbols"/stem(va)).write_text("\n".join(out),encoding="utf-8",newline="\n")
 index +=["","## 構造体一覧",""]
 for struct in sorted(groups):
  index.append(f"- [{md(struct)}](structs/{struct}.md) — {len(groups[struct])}フィールド")
 for struct,rows in groups.items():
  out=["# "+md(struct),"",
    "> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。",
    "",
    "| オフセット | 型 | 名前 | 概要 | 確度 |","|---|---|---|---|---|"]
  for _,offset,typ,name,summary,conf,source in sorted(rows,key=lambda x:int(x[1],16)):
   out.append(f"| {md(offset)} | {md(typ)} | {md(name)} | {md(summary)} | {md(conf)} |")
  out+=["","## 各フィールドの詳細",""]
  for _,offset,typ,name,summary,conf,source in sorted(rows,key=lambda x:int(x[1],16)):
   out +=[f"### {md(offset)} — {md(name)}","",md(summary),"",
     f"- 型：{md(typ)}",f"- 確度：{md(conf)}",
     f"- 元の研究出典表記：{md(source)}（未公開の出典を含む）",""]
   key="field:"+struct+":"+norm(offset)
   for record in rels.get(key,[]):
    subject=record.get("subject","")
    if subject.startswith("va:"):
     out.append("- 関連関数 "+link(subject[3:])+"："+
                md(record.get("predicate"))+" — "+md(record.get("summary")))
   for record in corrs.get(key,[]):
    out.append("- 訂正："+md(record.get("current_interpretation")))
   out.append("")
  out+=["[事典の一覧に戻る](../README.md)",""]
  (REF/"structs"/(struct+".md")).write_text("\n".join(out),encoding="utf-8",newline="\n")
 index+=["","## 読み方の注意","",
   "根拠の詳細が非公開のものは、採録時の確度を維持したまま表示しています。",
   "この事典は元の研究資料を再検証した保証書ではなく、共同調査の出発点です。",
   "CALL情報はV9静的索引に含まれる直接CALLだけです。",
   ""]
 (REF/"README.md").write_text("\n".join(index),encoding="utf-8",newline="\n")
 print(json.dumps({"symbols":len(syms),"fields":len(fields),"structs":len(groups),
                   "static_calls":len(calls),"relations":len(rel),"corrections":len(fixes),
                   "symbol_pages":len(list((REF/"symbols").glob("*.md"))),
                   "struct_pages":len(list((REF/"structs").glob("*.md")))},ensure_ascii=False))
if __name__=="__main__":build()
