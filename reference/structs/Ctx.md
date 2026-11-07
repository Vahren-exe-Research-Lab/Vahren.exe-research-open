# Ctx

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x30 | i32 | gamemode | 数値変数 @gamemode の値。セーブ見出しの先頭にも書く | 静的確認 |
| 0x34 | str | scenarioName | シナリオ名 | 静的確認 |
| 0x50 | ptr | playerUnit | プレイヤー本人の Unit（ロード時は +0x74 が立つ最初の Unit） | 静的確認 |
| 0x54 | ptr | playerPower | プレイヤー勢力（ロード時は +0x1D が立つ最初の Power） | 静的確認 |
| 0x2DC | map | powers | Power の表（先頭ノード +0x2E0） | 静的確認 |
| 0x2EC | map | spots | Spot の表（先頭ノード +0x2F0） | 静的確認 |
| 0x2FC | map | unitDefs | ユニット定義の表（std::map、キーはユニット ID） | 実機確認 |
| 0x300 | ptr | unitDefs_head | unitDefs の先頭ノード | 実機確認 |
| 0x304 | u32 | unitDefs_size | unitDefs の件数 | 実機確認 |
| 0x30C | map | varStore | 変数ストア | 静的確認 |
| 0x32C | set | roamingSet | 放浪中のユニットの集合 | 静的確認 |

## 各フィールドの詳細

### 0x30 — gamemode

数値変数 @gamemode の値。セーブ見出しの先頭にも書く

- 型：i32
- 確度：静的確認
- 元の研究出典表記：T014 A60, S1101§2（未公開の出典を含む）


### 0x34 — scenarioName

シナリオ名

- 型：str
- 確度：静的確認
- 元の研究出典表記：F§21, S1101§2（未公開の出典を含む）


### 0x50 — playerUnit

プレイヤー本人の Unit（ロード時は +0x74 が立つ最初の Unit）

- 型：ptr
- 確度：静的確認
- 元の研究出典表記：F§79.2, T014 A60（未公開の出典を含む）


### 0x54 — playerPower

プレイヤー勢力（ロード時は +0x1D が立つ最初の Power）

- 型：ptr
- 確度：静的確認
- 元の研究出典表記：F§79.2, T014 A60（未公開の出典を含む）


### 0x2DC — powers

Power の表（先頭ノード +0x2E0）

- 型：map
- 確度：静的確認
- 元の研究出典表記：F§58, T014 A57（未公開の出典を含む）


### 0x2EC — spots

Spot の表（先頭ノード +0x2F0）

- 型：map
- 確度：静的確認
- 元の研究出典表記：F§58, T014 A57（未公開の出典を含む）


### 0x2FC — unitDefs

ユニット定義の表（std::map、キーはユニット ID）

- 型：map
- 確度：実機確認
- 元の研究出典表記：F§91（未公開の出典を含む）


### 0x300 — unitDefs_head

unitDefs の先頭ノード

- 型：ptr
- 確度：実機確認
- 元の研究出典表記：F§91（未公開の出典を含む）


### 0x304 — unitDefs_size

unitDefs の件数

- 型：u32
- 確度：実機確認
- 元の研究出典表記：F§91（未公開の出典を含む）


### 0x30C — varStore

変数ストア

- 型：map
- 確度：静的確認
- 元の研究出典表記：F§63.1（未公開の出典を含む）


### 0x32C — roamingSet

放浪中のユニットの集合

- 型：set
- 確度：静的確認
- 元の研究出典表記：F§26（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
