# Spot

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x00 | str | name | 名前（Spot キー） | 静的確認 |
| 0x1C | set | units | その Spot の部隊（隊長と配下）の個体キー（先頭ノード +0x20）。セーブでは区切りなしで札 capacity が続く | 静的確認 |
| 0x2C | str | map | マップ名（changeMap が書く） | 静的確認 |
| 0x48 | str | dungeon | ダンジョン名（changeDungeon が書く。セーブの札 dunname） | 静的確認 |
| 0x80 | u32 | gain | 収入（countGain が読む） | 静的確認 |
| 0x84 | u32 | castle | 城（castle） | 静的確認 |
| 0x88 | u32 | capacity | 収容数（0 なら ctx+0xC、24 で頭打ち。ロード時 0 なら @spot_capacity） | 静的確認 |
| 0x8C | u32 | castleBattle | 0 なら DAT の castle_battle、1 なら城の戦闘 | 静的確認 |
| 0x90 | u32 | value | value（セーブの札 fightvalue） | 静的確認 |
| 0xB0 | ptr | ctx | ctx（Spot 解決 0x467E90 も書く） | 静的確認 |

## 各フィールドの詳細

### 0x00 — name

名前（Spot キー）

- 型：str
- 確度：静的確認
- 元の研究出典表記：F§58（未公開の出典を含む）


### 0x1C — units

その Spot の部隊（隊長と配下）の個体キー（先頭ノード +0x20）。セーブでは区切りなしで札 capacity が続く

- 型：set
- 確度：静的確認
- 元の研究出典表記：F§62.1, S1101§5（未公開の出典を含む）


### 0x2C — map

マップ名（changeMap が書く）

- 型：str
- 確度：静的確認
- 元の研究出典表記：F§58, §79.7（未公開の出典を含む）


### 0x48 — dungeon

ダンジョン名（changeDungeon が書く。セーブの札 dunname）

- 型：str
- 確度：静的確認
- 元の研究出典表記：F§58, §79.7（未公開の出典を含む）


### 0x80 — gain

収入（countGain が読む）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§58, §79.3（未公開の出典を含む）


### 0x84 — castle

城（castle）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§58（未公開の出典を含む）


### 0x88 — capacity

収容数（0 なら ctx+0xC、24 で頭打ち。ロード時 0 なら @spot_capacity）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§58, T014 A57（未公開の出典を含む）


### 0x8C — castleBattle

0 なら DAT の castle_battle、1 なら城の戦闘

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§68.1, §68.2（未公開の出典を含む）


### 0x90 — value

value（セーブの札 fightvalue）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§58（未公開の出典を含む）


### 0xB0 — ctx

ctx（Spot 解決 0x467E90 も書く）

- 型：ptr
- 確度：静的確認
- 元の研究出典表記：F§58, T014 A59（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
