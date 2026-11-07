# FrameWnd

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x8 | i32 | left | ウィンドウの左端（TempStatusWnd で確認） | テストのみ |
| 0x10 | i32 | right | ウィンドウの右端 | テストのみ |
| 0x84 | u8 | shown | 表示中の印（WarWnd+0x84 = 0x8BA5BC、TempStatusWnd+0x84 = 0x8BCDCC） | 実機確認 |
| 0xA4 | u32 | state | 状態。通常は 0x80000008 | 実機確認 |
| 0xBC | str | name | ウィンドウの名前（WarWnd は 'war'） | 静的確認 |

## 各フィールドの詳細

### 0x8 — left

ウィンドウの左端（TempStatusWnd で確認）

- 型：i32
- 確度：テストのみ
- 元の研究出典表記：W(work_selector_*.h)（未公開の出典を含む）


### 0x10 — right

ウィンドウの右端

- 型：i32
- 確度：テストのみ
- 元の研究出典表記：W(work_selector_*.h)（未公開の出典を含む）


### 0x84 — shown

表示中の印（WarWnd+0x84 = 0x8BA5BC、TempStatusWnd+0x84 = 0x8BCDCC）

- 型：u8
- 確度：実機確認
- 元の研究出典表記：C(§93), W（未公開の出典を含む）


### 0xA4 — state

状態。通常は 0x80000008

- 型：u32
- 確度：実機確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


### 0xBC — name

ウィンドウの名前（WarWnd は 'war'）

- 型：str
- 確度：静的確認
- 元の研究出典表記：C(§93)（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
