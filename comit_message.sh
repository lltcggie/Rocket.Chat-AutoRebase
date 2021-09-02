#! /bin/bash
git commit --allow-empty -m "Rocket.Chat Custom

- スレッド一覧にリアクションの絵文字を表示するようにした
- サイドバーのパブリックチャンネルとプライベートチャンネルを分けて表示するよう修正
- 引用メッセージのパーミッションチェックを無効化
- GenericFileAttachmentの視認性を改善
- 引用が正しく表示されないバグを修正
- Windowsでmeteor npm startが動くように修正
- NOTIFICATIONS_SCHEDULE_DELAY_ONLINEを15に変更
- 埋め込み情報をURLから取得するときにパラメータを指定できるようにした
- アップロード時にjpeg以外は画像ファイル変換を行わないようにした
- ファイルダウンロード時に余計な拡張子が付くことがあるのを修正
- 独自のGitHub Actionsワークフロー追加
- Dockerfileをこのリポジトリの設定に合わせた
- Update README.md"
