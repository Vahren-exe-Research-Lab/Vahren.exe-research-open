# UnitRuntime

> 研究上のレイアウト名です。原作C++のクラス名と同一とは限りません。

| オフセット | 型 | 名前 | 概要 | 確度 |
|---|---|---|---|---|
| 0x90 | unknown | hp | 実行中Unit-like基点のHP。enabled HP後処理で整数として読む。幅・符号型不明。UnitDefではない。 回収済み研究本文のみ。幅・具体的class同一性未確定。 | 静的確認 |
| 0xDC | unknown | hpMax | 実行中Unit-like基点のHPmax。HP段階計算の整数除数。幅・符号型不明。ゼロ除数等は未確定。 回収済み研究本文のみ。幅・具体的class同一性未確定。 | 静的確認 |
| 0x738 | unknown | hpTier | HP割合から整数化後signed 0..20へclampして書く段階値。HP本体と別。格納幅・宣言符号型不明。 回収済み研究本文のみ。幅・具体的class同一性未確定。 | 静的確認 |
| 0x185F4 | unknown | hpRegistrationCountdown | HP後処理で0/150を書く登録関連残量候補。enabled経路は登録skip時も150再設定。幅・宣言符号型・tick単位不明。 回収済み研究本文のみ。幅・具体的class同一性未確定。 | 静的確認 |

## 各フィールドの詳細

### 0x90 — hp

実行中Unit-like基点のHP。enabled HP後処理で整数として読む。幅・符号型不明。UnitDefではない。 回収済み研究本文のみ。幅・具体的class同一性未確定。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T012_HEAL_HP_POST_577100_CONTRACT_20261013.md lines4-5; REF_SKILL_POST_ACTION.md lines69-71（未公開の出典を含む）


### 0xDC — hpMax

実行中Unit-like基点のHPmax。HP段階計算の整数除数。幅・符号型不明。ゼロ除数等は未確定。 回収済み研究本文のみ。幅・具体的class同一性未確定。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T012_HEAL_HP_POST_577100_CONTRACT_20261013.md lines4-5; REF_SKILL_POST_ACTION.md lines69-71（未公開の出典を含む）


### 0x738 — hpTier

HP割合から整数化後signed 0..20へclampして書く段階値。HP本体と別。格納幅・宣言符号型不明。 回収済み研究本文のみ。幅・具体的class同一性未確定。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T012_HEAL_HP_POST_577100_CONTRACT_20261013.md lines4-5; data/T012_HP_LIFEBAR_TIMER_CROSSCALL_20261013.md line7（未公開の出典を含む）


### 0x185F4 — hpRegistrationCountdown

HP後処理で0/150を書く登録関連残量候補。enabled経路は登録skip時も150再設定。幅・宣言符号型・tick単位不明。 回収済み研究本文のみ。幅・具体的class同一性未確定。

- 型：unknown
- 確度：静的確認
- 元の研究出典表記：data/T012_HEAL_HP_POST_577100_CONTRACT_20261013.md lines4-6; data/T012_HP_LIFEBAR_TIMER_CROSSCALL_20261013.md lines4-7; REF_SKILL_POST_ACTION.md line72（未公開の出典を含む）


[事典の一覧に戻る](../README.md)
