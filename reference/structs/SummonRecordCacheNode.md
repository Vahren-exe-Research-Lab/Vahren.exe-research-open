# SummonRecordCacheNode

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x28 | unknown | inlineUnitRecord | 0x577260がowner+0x1E4B4のcacheから探して返す、ノード内の埋め込み記録の先頭。ポインタを格納した欄とは区別する。別の証拠票の構造導出は468Bとするが、宣言型・完全レイアウト・実行時到達性は未確定。 | 静的確認（保存済み著者の限定サイト解析。今回の原作再検証・実行なし） |

## 各フィールドの詳細

### 0x28 — inlineUnitRecord

0x577260がowner+0x1E4B4のcacheから探して返す、ノード内の埋め込み記録の先頭。ポインタを格納した欄とは区別する。別の証拠票の構造導出は468Bとするが、宣言型・完全レイアウト・実行時到達性は未確定。

- 型：unknown
- 確度：静的確認（保存済み著者の限定サイト解析。今回の原作再検証・実行なし）
- 元の研究出典表記：exp_research_20261021/EXP_SAVE_TREE_BOUNDARY_EVIDENCE_20261021.json lines26-29,50-53,74-78 [recovered=research/recovered/json_exp_exe1/reports/14_EXP_SAVE_TREE_BOUNDARY_EVIDENCE_20261021.json; sha256=EVID-0252]; exp_research_20261021/EXP_STRING_CACHE_ABI_EVIDENCE_20261021.json lines358-369 [recovered=research/recovered/json_exp_exe1/reports/19_EXP_STRING_CACHE_ABI_EVIDENCE_20261021.json; sha256=EVID-0183]（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
