# ScriptEngine

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x1EEC3C | unknown | currentExecutionMode | 0x4335E0が分岐に使う現在の実行モード。報告ではmode2が戦闘。phaseの識別値やフレーム設定方式とは別。幅・宣言enum型・合法な遷移の全体は不明。 | 静的確認 |
| 0x1EEC44 | u8 | battleActive | mode2 で戦闘更新の前後に読む byte のゲート。合法な状態遷移の全体は未確認。 | 静的確認 |
| 0x1EED58 | unknown | waitCounter | waitが評価した引数を保持するカウンタ。インタプリタの継続ごとに減算し、終了時に0x80000008へ戻す。幅・宣言符号型・場面ごとの完全な挙動は不明。 | 静的確認 |
| 0x1EED60 | i32 | resettableElapsed | getTime が返す int32 の経過カウンタ。resetTime はこの値だけを0に戻す。絶対時計の位相とは別。 | 静的確認 |
| 0x1EED64 | unknown | absoluteSchedulerCounter | isIntervalと報告上の10tickごとの制限時間更新に使う絶対スケジューラ時計。リセット可能な+0x1EED60とは別。選択した本文には幅・宣言符号型の明記がなく、実機未検証。 | 静的確認 |
| 0x1EED78 | vec | executionBlocks | VM の並列フレーム・ブロック列。現在フレームは末尾要素。frameInstallMode=0 では末尾に追加。 | 静的確認 |
| 0x1EED88 | vec | executionPCs | VM の並列 PC 列。現在フレームは末尾要素。frameInstallMode=0 では先頭に0を挿入。 | 静的確認 |
| 0x1EED98 | vec | executionModes | VM の並列実行モード列。現在フレームは末尾要素。シナリオの phase identity とは独立。 | 静的確認 |
| 0x1EEDA8 | vec | executionFrameKinds | VM の並列フレーム種別列。現在フレームは末尾要素。frameInstallMode=0 では先頭に0を挿入。 | 静的確認 |

## 各フィールドの詳細

### 0x1EEC3C — currentExecutionMode

0x4335E0が分岐に使う現在の実行モード。報告ではmode2が戦闘。phaseの識別値やフレーム設定方式とは別。幅・宣言enum型・合法な遷移の全体は不明。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines227-235; REF_SCRIPT_VM_CONTEXT.md lines3-4（未公開の出典を含む）


### 0x1EEC44 — battleActive

mode2 で戦闘更新の前後に読む byte のゲート。合法な状態遷移の全体は未確認。

- 型：u8
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines375-376; F§82.1（未公開の出典を含む）


### 0x1EED58 — waitCounter

waitが評価した引数を保持するカウンタ。インタプリタの継続ごとに減算し、終了時に0x80000008へ戻す。幅・宣言符号型・場面ごとの完全な挙動は不明。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines97-104; REF_SCRIPT_VM_CONTEXT.md lines3-4,15（未公開の出典を含む）


### 0x1EED60 — resettableElapsed

getTime が返す int32 の経過カウンタ。resetTime はこの値だけを0に戻す。絶対時計の位相とは別。

- 型：i32
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines108-133; F§82.1（未公開の出典を含む）


### 0x1EED64 — absoluteSchedulerCounter

isIntervalと報告上の10tickごとの制限時間更新に使う絶対スケジューラ時計。リセット可能な+0x1EED60とは別。選択した本文には幅・宣言符号型の明記がなく、実機未検証。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines108-114,125-133; REF_SCRIPT_VM_CONTEXT.md lines3-4,17（未公開の出典を含む）


### 0x1EED78 — executionBlocks

VM の並列フレーム・ブロック列。現在フレームは末尾要素。frameInstallMode=0 では末尾に追加。

- 型：vec
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines229-259,344; F§82.1（未公開の出典を含む）


### 0x1EED88 — executionPCs

VM の並列 PC 列。現在フレームは末尾要素。frameInstallMode=0 では先頭に0を挿入。

- 型：vec
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines229-259,344; F§82.1（未公開の出典を含む）


### 0x1EED98 — executionModes

VM の並列実行モード列。現在フレームは末尾要素。シナリオの phase identity とは独立。

- 型：vec
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines229-259,344; F§82.1（未公開の出典を含む）


### 0x1EEDA8 — executionFrameKinds

VM の並列フレーム種別列。現在フレームは末尾要素。frameInstallMode=0 では先頭に0を挿入。

- 型：vec
- 確度：静的確認
- 元の研究出典表記：data/T010_EVENT_SCHEDULER.md lines229-259,344; F§82.1（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
