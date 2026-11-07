# SaveUnitDataTreeNode

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x28 | ptr | unitDataPointer | 0x460000が走査するowner+0x300の木のノードに保持されたUnitDataへのポインタ。読み取り位置の報告は0x4602F6。召喚cacheの同じ+0x28にある埋め込み記録とは異なる。研究用部分名で、全save経路・C++クラス同一性は未確定。 | 静的確認（保存済み著者の限定サイト解析。今回の原作再検証・実行なし） |

## 各フィールドの詳細

### 0x28 — unitDataPointer

0x460000が走査するowner+0x300の木のノードに保持されたUnitDataへのポインタ。読み取り位置の報告は0x4602F6。召喚cacheの同じ+0x28にある埋め込み記録とは異なる。研究用部分名で、全save経路・C++クラス同一性は未確定。

- 型：ptr
- 確度：静的確認（保存済み著者の限定サイト解析。今回の原作再検証・実行なし）
- 元の研究出典表記：exp_research_20261021/EXP_SAVE_TREE_BOUNDARY_EVIDENCE_20261021.json lines26-29,50-53,74-78 [recovered=research/recovered/json_exp_exe1/reports/14_EXP_SAVE_TREE_BOUNDARY_EVIDENCE_20261021.json; sha256=EVID-0252]（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
