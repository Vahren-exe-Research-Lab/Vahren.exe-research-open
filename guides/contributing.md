# 書き込み・訂正ガイド

**「ここが分からない」「たぶん違う」だけでも投稿できます。形式、事前承認、テスト合格は参加条件ではありません。**

## どこに書けばよい？

| やりたいこと | 投稿先 | 何が起きる？ |
|---|---|---|
| 気軽な説明やメモを直接追加・訂正する | [Wiki](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/wiki) | Wikiのページに保存 |
| 質問する、方向性を相談する | [Discussions](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/discussions) | 掲示板で共有 |
| 誤り・リンク切れ・調査したいことを伝える | [Issue](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/issues/new/choose) | 報告として記録 |
| 研究サイトの元文書や検索辞書を変更する | GitHubのファイル編集 → PR | GitHub Actionsが原則として自動統合し、サイトを再生成 |

**Wikiと検索台帳は別です。** Wikiのページを保存しても、関数辞書や研究サイトに自動で取り込まれるわけではありません。検索サイトを直したい場合は、元ファイルの編集PRを使うか、まずIssueで知らせてください。

## Wikiへ直接書き込む

公開Wikiの編集が許可されている場合、GitHubにログインして[Wikiを開く](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/wiki)と編集できます。ページがまだなければ最初のページを作成し、既存ページなら**Edit**から変更します。

Wikiの編集権限が設定されていない、または編集ボタンが表示されない場合は、IssueやDiscussionsで文章を投稿する方法もあります。

## Issueで知らせる

1. [Issueの新規作成](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/issues/new/choose)を開きます。
2. 目的に合うテンプレートか、**Blank issue（自由形式）**を選びます。
3. 気付いたことを好きな言葉で書いて投稿します。

たとえば「このページの『初期化』が分からなかった」「ゲームでは違う動きに見えた」「リンクが開けない」だけでも構いません。

不正確な用語を使っていても、確認済みのアドレスを知らなくても投稿できます。

## 検索サイトの文書を自分で直す

書き込み権限がないGitHubアカウントでも、PRを提出できます。

1. [リポジトリのファイル一覧](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open)で直したい文書を開きます。
2. 鉛筆マーク（**Edit this file**）を選びます。必要ならForkが自動で作られます。
3. 文章を変更します。**Preview**で読みやすいかを確認できます。
4. **Commit changes**／**Propose changes**などを押し、**Create pull request**から修正案を送ります。

[GitHub公式の編集手順](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)も参考になります。画面の表示は時期や権限によって異なる場合があります。

### 管理者の承認は必要？

このリポジトリには[PRの無人自動統合](../AUTO_MERGE.md)があります。通常、投稿されたPRはGitHub Actionsが承認・レビュー・テスト結果を待たずに統合を試みます。**OpenAIの有料AI契約は不要です。**

競合などでGitHubが統合できなければPRは開いたまま残り、定期実行で再試行されます。反映後もサイトの再生成・公開まで少し時間差が生じ、配信障害で止まることがあります。これらは投稿者が何かを間違えたという意味ではありません。

### 自動生成された関数ページを直すとき

関数事典のページは元の辞書から自動生成されています。生成ページだけを直しても、再生成で元に戻ることがあります。詳しい人はsymbols.tsvやstructs.tsvなどの元データを修正します。

どこを直せばよいか分からなければ、**ページのURLと訂正したい文章をIssueに貼るだけで構いません**。

## 個人情報や素材について

画面写真やログに本名・メールアドレス・トークンが写っている場合は隠すことをおすすめします。秘密の内容を含む問題は[非公開の報告案内](../SECURITY.md)から連絡できます。

公開者自身が著作権を持つ資料にはCC0の方針がありますが、ゲームや他人の作品の権利まで放棄するものではありません。[権利の説明](../SCOPE_AND_LIMITATIONS.md)を参照してください。

## 次に読む

[初めての方へ](getting-started.md)／[用語辞典](glossary.md)／[実際の資料を読む](first-lookup.md)。
