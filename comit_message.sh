#! /bin/bash
git commit --allow-empty -m "Rocket.Chat Custom

- Fallback content-type as application/octet-stream for uploaded files in FileSystem
- 埋め込み情報をURLから取得するときにパラメータを指定できるようにした
- アップロード時にjpeg以外は画像ファイル変換を行わないようにした
- ファイルダウンロード時に余計な拡張子が付くことがあるのを修正
- 独自のGitHub Actionsワークフロー追加
- 既存のGitHub Actions無効化
- Dockerfileをこのリポジトリの設定に合わせた
- Update README.md"
