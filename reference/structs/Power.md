# Power

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x00 | str | name | 名前（Power キー） | 静的確認 |
| 0x1C | u8 | isActive | ターン処理の対象（初期 1、イベント勢力は 0。0 の勢力は手番を飛ばされ、ターン末に順序から除かれる） | 静的確認 |
| 0x1D | u8 | isPlayer | プレイヤーが操作する勢力の印。1 のときだけ詳細パネルに雇用・解雇ボタンが出る（同盟国も 0） | 実機確認 |
| 0x20 | u32 | personality | 性格（0x593890 が rand で決める） | 静的確認 |
| 0x24 | str | master | 盟主の Unit の個体キー（0x4673B0 が 0x467DE0 で Unit として引く）。旧説明「勢力の名前」は誤り | 静的確認 |
| 0x40 | str | str40 | 0x5917B0 が作る文字列（表示名系、VERIFY）。セーブの値は flagNN | 推定 |
| 0x5C | i32 | money | 資金 | 静的確認 |
| 0x60 | i32 | turn60 | ターン値（初期 0x80000008。leave_period と比べる）。意味は一部 | 静的確認 |
| 0x64 | set | territory | 領地の Spot キー（先頭ノード +0x68） | 静的確認 |
| 0x90 | vec | merce | 傭兵（merce）のリスト | 静的確認 |
| 0xA0 | set | staff | staff | 静的確認 |
| 0xC0 | vec | home | home の Spot 名（空なら DAT の home を使う。セーブの札 home_spot） | 静的確認 |
| 0xD0 | u32 | fix | fix（on/home/hold/warlike → 1〜4、他 0） | 静的確認 |
| 0xD4 | u32 | trainingAverage | training_average（セーブの札 train_max） | 静的確認 |
| 0xD8 | u32 | trainingUp | training_up（セーブの札 train_up） | 静的確認 |
| 0xDC | u32 | baseLevel | base_level。0x80000008 ならロード時 @scenario の base_level で補う | 静的確認 |
| 0xE0 | ptr | ctx | ctx（Power 解決 0x467F40 も書く） | 静的確認 |

## 各フィールドの詳細

### 0x00 — name

名前（Power キー）

- 型：str
- 確度：静的確認
- 元の研究出典表記：F§58（未公開の出典を含む）


### 0x1C — isActive

ターン処理の対象（初期 1、イベント勢力は 0。0 の勢力は手番を飛ばされ、ターン末に順序から除かれる）

- 型：u8
- 確度：静的確認
- 元の研究出典表記：F§58, §62.1（未公開の出典を含む）


### 0x1D — isPlayer

プレイヤーが操作する勢力の印。1 のときだけ詳細パネルに雇用・解雇ボタンが出る（同盟国も 0）

- 型：u8
- 確度：実機確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


### 0x20 — personality

性格（0x593890 が rand で決める）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§66（未公開の出典を含む）


### 0x24 — master

盟主の Unit の個体キー（0x4673B0 が 0x467DE0 で Unit として引く）。旧説明「勢力の名前」は誤り

- 型：str
- 確度：静的確認
- 元の研究出典表記：F§32, §58, S1101§6（未公開の出典を含む）


### 0x40 — str40

0x5917B0 が作る文字列（表示名系、VERIFY）。セーブの値は flagNN

- 型：str
- 確度：推定
- 元の研究出典表記：F§58, S1101§6（未公開の出典を含む）


### 0x5C — money

資金

- 型：i32
- 確度：静的確認
- 元の研究出典表記：F§58, §79.3（未公開の出典を含む）


### 0x60 — turn60

ターン値（初期 0x80000008。leave_period と比べる）。意味は一部

- 型：i32
- 確度：静的確認
- 元の研究出典表記：F§62.1, §71.2（未公開の出典を含む）


### 0x64 — territory

領地の Spot キー（先頭ノード +0x68）

- 型：set
- 確度：静的確認
- 元の研究出典表記：F§58, §62.1（未公開の出典を含む）


### 0x90 — merce

傭兵（merce）のリスト

- 型：vec
- 確度：静的確認
- 元の研究出典表記：F§58, §71.1（未公開の出典を含む）


### 0xA0 — staff

staff

- 型：set
- 確度：静的確認
- 元の研究出典表記：F§58（未公開の出典を含む）


### 0xC0 — home

home の Spot 名（空なら DAT の home を使う。セーブの札 home_spot）

- 型：vec
- 確度：静的確認
- 元の研究出典表記：F§66（未公開の出典を含む）


### 0xD0 — fix

fix（on/home/hold/warlike → 1〜4、他 0）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§58（未公開の出典を含む）


### 0xD4 — trainingAverage

training_average（セーブの札 train_max）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§45, §58（未公開の出典を含む）


### 0xD8 — trainingUp

training_up（セーブの札 train_up）

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§45, §58（未公開の出典を含む）


### 0xDC — baseLevel

base_level。0x80000008 ならロード時 @scenario の base_level で補う

- 型：u32
- 確度：静的確認
- 元の研究出典表記：F§45, T014 A57（未公開の出典を含む）


### 0xE0 — ctx

ctx（Power 解決 0x467F40 も書く）

- 型：ptr
- 確度：静的確認
- 元の研究出典表記：F§58, T014§normal save tail（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
