# やりたいことから研究を探す

**機能名やアドレスを知らなくても、「何をしたいか」から資料を選べます。** 以下は完成機能の一覧ではなく、関連する研究の入口です。動作確認の状況は各ページで確認してください。

## ゲーム内でやりたいこと

| やりたいこと・疑問 | 最初に読む資料 | 調べたい点 |
|---|---|---|
| 召喚獣の経験値を召喚者へ渡したい | [経験値・召喚](../REF_UNIT_EXP_SUMMON.md) | 召喚者と召喚先の対応、経験値の行き先 |
| 変身解除時の状態を引き継ぎたい | [経験値・召喚](../REF_UNIT_EXP_SUMMON.md)、[スキル処理](../REF_SKILL_POST_ACTION.md) | 同じ個体なのか、別のユニットへの交代か |
| 戦闘を別のシステムへ差し替えたい | [戦闘乗っ取り](../REF_BATTLE_TAKEOVER.md) | 入力と戦後の結果反映、イベントとの関係 |
| 敵の動き・退却・士気を調べたい | [戦闘AI・士気](../REF_BATTLE_AI_MORALE.md) | 通常戦闘と簡略戦闘の違い |
| DATに命令・イベント機能を足したい | [DAT挙動](../REF_DAT_BEHAVIOR.md)、[スクリプトVM](../REF_SCRIPT_VM_CONTEXT.md) | 命令が届く入口、戦闘内外の違い |
| ユニット一覧・雇用画面を変更したい | [UIの仕組み](../REF_UI_SYSTEM.md) | 表示・選択・データ更新の違い |
| OGG音声の再生可能性を調べたい | [音声・Vorbis](../REF_AUDIO_VORBIS.md) | デコードとゲーム内からの再生呼出しの違い |
| セーブと設定変更の反映を知りたい | [セーブ形式](../REF_SAVE_FORMAT.md)、[永続化](../REF_SAVE_PERSISTENCE.md) | 保存値と再計算値の違い |
| 内政・経済・領地の仕組みを調べたい | [戦略・経済](../REF_STRATEGY_ECONOMY.md) | 戦略と戦闘の境界 |
| ランダムイベントを理解したい | [ランダムイベント](../REF_RANDOM_EVENTS.md) | 発生条件と実行処理 |
| シナリオ互換性を調べたい | [RTSシナリオ](../REF_RTS_SCENARIO.md)、[互換性](../REF_SCENARIO_COMPAT.md) | シナリオと実行ファイルの違い |
| 起動・読み込みの不具合を調べたい | [起動・読み込み](../REF_STARTUP_LOADING.md) | どこで停止するのか |

ここにない目標も[Discussions](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/discussions)で相談できます。「地形にダメージを持たせたい」など、やりたいことの言葉のままで構いません。

## 資料を開いた後の読み順

最初は**概要 → 未確認事項・注意 → 関連する関数**の順がおすすめです。長い解析の途中経過や16進数の表は必要になってから読めます。

「関数が見つかった」「保存場所が分かった」だけでは機能の導入方法が完成したとは限りません。配布物が欲しい場合は別途導入・動作確認の記録を確認します。

## 検索の言い換え

| 普段の言葉 | 追加で試す検索語 |
|---|---|
| 経験値・召喚 | EXP、Exp、Summon、Unit |
| 戦闘開始・終了 | Battle、Scene、Result |
| 保存・読み込み | Save、Load、永続化 |
| 画面・一覧 | UI、Window、Wnd |
| イベントの命令 | DAT、Script、VM |
| 音声 | Audio、OGG、Vorbis |

検索に出ないことだけで未調査とは断定できません。別名や関連分野で記録されている場合があります。

## 詳しい人向けの近道

アドレスが分かる場合は[関数・アドレス事典](../reference/README.md)へ。プログラムから扱う場合は[関数TSV](../symbols.tsv)、[構造体TSV](../structs.tsv)、[直接CALL索引](../reference/static_calls.tsv)も利用できます。

## 次に読む

[研究の確度を見分ける](reading-research.md)／[用語を調べる](glossary.md)／[初めての方へ](getting-started.md)。
