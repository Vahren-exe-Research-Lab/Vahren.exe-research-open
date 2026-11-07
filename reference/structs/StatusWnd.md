# StatusWnd

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x98 | ptr | owner | 表示の所有者。通常StatusWndと一覧TempStatusWndで同一、所有者+4はゲーム文脈。 | 実機確認 |
| 0x9C | ptr | anchor | 基準の相手（Player と比べている） | テストのみ |
| 0x1B8 | ptr | targetDef | 表示しているユニットの定義（g_StatusWnd では 0x67EB30、TempStatusWnd では 0x8BCF00） | 実機確認 |
| 0x1BC | i32 | pressedIndex | 押されているボタンの番号（0=雇用/召上げ、1=解雇、2=アイテム、0x80000008=なし） | 静的確認 |
| 0x1C4 | u8 | btnHire | 「雇用」ボタンを作った印 | 実機確認 |
| 0x1C5 | u8 | btnExtract | 「召上げ」ボタンを作った印 | 静的確認 |
| 0x1C6 | u8 | btnDismiss | 「解雇」ボタンを作った印 | 実機確認 |
| 0x1C7 | u8 | btnItem | 「アイテム」ボタンを作った印 | 静的確認 |
| 0x1C8 | rect[] | hoverRects | 説明表示の対象の矩形（16 バイトずつ） | テストのみ |
| 0x12F8 | u32 | hoverCount | 説明表示の対象の数 | テストのみ |

## 各フィールドの詳細

### 0x98 — owner

表示の所有者。通常StatusWndと一覧TempStatusWndで同一、所有者+4はゲーム文脈。

- 型：ptr
- 確度：実機確認
- 元の研究出典表記：W(DAT_UI_V4_STATUS_PANEL.md,2026-10-29)（未公開の出典を含む）


### 0x9C — anchor

基準の相手（Player と比べている）

- 型：ptr
- 確度：テストのみ
- 元の研究出典表記：W(work_selector_hover_context.h)（未公開の出典を含む）


### 0x1B8 — targetDef

表示しているユニットの定義（g_StatusWnd では 0x67EB30、TempStatusWnd では 0x8BCF00）

- 型：ptr
- 確度：実機確認
- 元の研究出典表記：C(§93), W（未公開の出典を含む）


### 0x1BC — pressedIndex

押されているボタンの番号（0=雇用/召上げ、1=解雇、2=アイテム、0x80000008=なし）

- 型：i32
- 確度：静的確認
- 元の研究出典表記：F§95（未公開の出典を含む）


### 0x1C4 — btnHire

「雇用」ボタンを作った印

- 型：u8
- 確度：実機確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


### 0x1C5 — btnExtract

「召上げ」ボタンを作った印

- 型：u8
- 確度：静的確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


### 0x1C6 — btnDismiss

「解雇」ボタンを作った印

- 型：u8
- 確度：実機確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


### 0x1C7 — btnItem

「アイテム」ボタンを作った印

- 型：u8
- 確度：静的確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


### 0x1C8 — hoverRects

説明表示の対象の矩形（16 バイトずつ）

- 型：rect[]
- 確度：テストのみ
- 元の研究出典表記：W(work_selector_skill_hover.h)（未公開の出典を含む）


### 0x12F8 — hoverCount

説明表示の対象の数

- 型：u32
- 確度：テストのみ
- 元の研究出典表記：W(work_selector_skill_hover.h)（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
