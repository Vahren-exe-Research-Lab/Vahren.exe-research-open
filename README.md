# Vahren.exe 解析・拡張研究 — 公開候補

> **公開版：内容は研究上の見解と未検証事項を含みます。** 迫真戦記 ver0.67 / Vahren.exe の逆解析で得た研究のうち、共有候補として選別した情報を収録しています。原作ゲーム本体・画像・音声・セーブデータは含めません。

このリポジトリは、ゲーム内部の関数・メモリ・DAT・戦闘・セーブ等を調べる共同研究者向けの**読みやすい研究事典**です。過去の非公開Git履歴や作業日誌をそのまま公開するのではなく、研究結果だけを新しい履歴でまとめています。

## 何が入っている？

| 資料 | 収録内容 |
|---|---|
| [関数・アドレス事典](reference/README.md) | **510アドレス項目（うち370関数）**。名前、目的、確度、関連CALL |
| [構造体・フィールド](reference/README.md#構造体一覧) | **14構造体・122フィールド**。オフセット・型・説明・確度 |
| [直接CALL索引](reference/static_calls.tsv) | V9静的索引から選別した**2,373件**。間接CALLは対象外 |
| [関数定義TSV](symbols.tsv) / [構造体定義TSV](structs.tsv) | 元の研究辞書を機械可読な形で保存 |
| [関係記録](reference/relations.jsonl) / [訂正記録](reference/corrections.jsonl) | **165関係・17訂正**。非公開の証拠原本へのパス・個人情報は除外 |
| [分野別の研究まとめ](#分野別の研究) | **15文書**。既知事項、未確認部分、過去の訂正を整理 |

## 分野別の研究

| 分野 | 研究まとめ |
|---|---|
| 戦闘乗っ取り・戦闘終了処理 | [REF_BATTLE_TAKEOVER.md](REF_BATTLE_TAKEOVER.md) |
| 戦闘AI・士気・退却 | [REF_BATTLE_AI_MORALE.md](REF_BATTLE_AI_MORALE.md) |
| 経験値・訓練・召喚 | [REF_UNIT_EXP_SUMMON.md](REF_UNIT_EXP_SUMMON.md) |
| 技能発動後処理 | [REF_SKILL_POST_ACTION.md](REF_SKILL_POST_ACTION.md) |
| DAT命令・スクリプト | [REF_DAT_BEHAVIOR.md](REF_DAT_BEHAVIOR.md) |
| UIと画面表示 | [REF_UI_SYSTEM.md](REF_UI_SYSTEM.md) |
| スクリプトVM・実行コンテキスト | [REF_SCRIPT_VM_CONTEXT.md](REF_SCRIPT_VM_CONTEXT.md) |
| セーブ形式 | [REF_SAVE_FORMAT.md](REF_SAVE_FORMAT.md) |
| セーブ・永続化 | [REF_SAVE_PERSISTENCE.md](REF_SAVE_PERSISTENCE.md) |
| 戦略・内政・経済 | [REF_STRATEGY_ECONOMY.md](REF_STRATEGY_ECONOMY.md) |
| ランダムイベント | [REF_RANDOM_EVENTS.md](REF_RANDOM_EVENTS.md) |
| RTSシナリオ | [REF_RTS_SCENARIO.md](REF_RTS_SCENARIO.md) |
| シナリオ互換 | [REF_SCENARIO_COMPAT.md](REF_SCENARIO_COMPAT.md) |
| 音声・Ogg/Vorbis関連 | [REF_AUDIO_VORBIS.md](REF_AUDIO_VORBIS.md) |
| 起動・読み込みの障害 | [REF_STARTUP_LOADING.md](REF_STARTUP_LOADING.md) |

## 研究資料の検索

Python 3のみで使用できます。原作ゲームやデータベースは不要です。

```powershell
python -B tools/search.py search 召喚
python -B tools/search.py symbols Battle_ConstructScene
python -B tools/search.py fields hp
python -B tools/search.py callers 0x0048D6A0
python -B tools/search.py callees 0x0040E220 --json
```

ブラウザからは[関数・メモリ事典](reference/README.md)を開き、アドレスや関数名を選択してください。

ページの再生成：

```powershell
python -B tools/build_reference.py
python -B -m unittest discover -s tests -v
```

[公開出典IDの説明](EVIDENCE_REFERENCES.md)

## 自動テスト（GitHub Actions）

Pull Requestと`main`への変更のたびに、[Research CI](.github/workflows/research-ci.yml)でPythonテスト、辞書・CALLの整合性、生成ページの差分、検索CLIを自動検査します。結果は[Actionsタブ](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/actions/workflows/research-ci.yml)から確認できます。検査の合格は、研究内容そのものの実機検証や権利関係の保証ではありません。

## 研究の読み方・制約

研究報告にある「STATIC（静的解析）」「INFERRED（推定）」「VERIFY（未確認）」「DYNAMIC（実機観測）」「Golden」「READY」は異なる段階です。**解析記録が保存されていることは、ゲーム上で実証されたことを意味しません。**

この公開版には、原作EXE、ゲーム素材、過去の非公開Git履歴、未選別の研究ログ、内部Issue/PRの投稿者データ、検証に必要な原本の一部を含めていません。非公開の出典へのリンクは削除または非公開と明記しました。したがって、記載された確度を第三者がすべて独立検証できる状態ではありません。

[調査への参加方法](CONTRIBUTING.md) / [提供範囲と制約](SCOPE_AND_LIMITATIONS.md) / [公開内容・配布条件](RELEASE_NOTES.md)

## 権利について

原作の著作権者・制作者とは独立した調査記録です。**公開者が自ら権利を持つ独自の文書・コード等には[CC0 1.0 Universal](LICENSE)を適用**します。原作ゲームや第三者の著作物・商標等には適用されません。原作ファイルは再配布せず、他者の権利を放棄するものでもありません。詳しくは[提供範囲と制約](SCOPE_AND_LIMITATIONS.md)をご確認ください。
