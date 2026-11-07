# セキュリティポリシー / Security Policy

## 非公開で報告する方法

**APIキー、トークン、パスワード、個人情報、非公開GitHubリンク、公開してはいけない証拠や原作素材などを発見した場合、公開IssueやDiscussionsへ内容を投稿しないでください。**

このリポジトリはGitHubの Private vulnerability reporting（非公開の脆弱性報告）を有効にしています。

[GitHubのセキュリティアドバイザリ](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/security/advisories)を開き、**Report a vulnerability** を選んで非公開で報告してください。

実際の認証情報や個人情報をそのまま添付せず、問題があるファイルの場所・性質・影響と、安全な範囲での再現手順を説明してください。

## 対応方針

- 報告された問題の影響範囲を調査し、必要に応じて公開ファイルを修正します。
- 漏洩したトークン等は、単にGitから削除するだけでなく失効・再発行が必要です。
- Gitの過去の履歴・第三者のコピー・キャッシュから直ちに削除できるとは限りません。
- 研究の正確性や通常の質問・提案は[GitHub Discussions](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/discussions)で扱います。

## 適用範囲と自動検査

このセキュリティポリシーは、公開した研究文書、検索用Pythonツール、GitHub Actionsおよび研究サイトを対象とします。

Pull Requestとmainの変更時、および毎週、Gitleaks（Git履歴・作業ツリー）、出典SHAや公開対象ファイルの検査を実施します。GitHub標準のSecret ScanningとPush Protectionも有効にしています。

**検査が成功しても機密情報や匿名性の問題が絶対に存在しないことを保証するものではありません。** 問題を発見した場合は、非公開の報告経路をご利用ください。
