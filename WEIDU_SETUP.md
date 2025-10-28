# WeiDU実行ファイルのセットアップ

## 概要

このModを配布またはインストールするには、WeiDU実行ファイルが必要です。

## Windows用セットアップ

### 方法1: WeiDUをダウンロードして改名

1. **WeiDUをダウンロード**
   - https://github.com/WeiDUorg/weidu/releases から最新版をダウンロード
   - `weidu-windows-x86.zip` をダウンロード

2. **ファイルを抽出**
   - `weidu.exe` を抽出

3. **改名**
   ```bash
   # このリポジトリのルートディレクトリで
   cp /path/to/weidu.exe setup-bg1ee_sod_jp.exe
   ```

### 方法2: 既存のWeiDU Modからコピー

もし既にWeiDU Modをインストールしている場合：

```bash
# BGEEディレクトリからweidu.exeをコピーして改名
cp /path/to/BGEE/weidu.exe setup-bg1ee_sod_jp.exe
```

## Linux/macOS用セットアップ

### WeiDUのインストール

1. **バイナリをダウンロード**
   ```bash
   # Linux
   wget https://github.com/WeiDUorg/weidu/releases/download/v249.00/weidu-linux-x86_64.zip
   unzip weidu-linux-x86_64.zip

   # macOS
   wget https://github.com/WeiDUorg/weidu/releases/download/v249.00/weidu-mac-x86_64.zip
   unzip weidu-mac-x86_64.zip
   ```

2. **インストール**
   ```bash
   sudo cp weidu /usr/local/bin/
   sudo chmod +x /usr/local/bin/weidu
   ```

3. **Modのインストール**
   ```bash
   # このスクリプトを使用
   ./install.sh /path/to/BGEE

   # または直接実行
   cd /path/to/BGEE
   weidu setup-bg1ee_sod_jp.tp2
   ```

## 開発者向け: リリースパッケージの作成

### Windows向けリリース

```bash
# 1. WeiDUをダウンロード
wget https://github.com/WeiDUorg/weidu/releases/download/v249.00/weidu-windows-x86.zip
unzip weidu-windows-x86.zip

# 2. setup-*.exeを作成
cp weidu.exe setup-bg1ee_sod_jp.exe

# 3. パッケージを作成
zip -r bg1ee_sod_jp_v1.0.0_windows.zip \
  setup-bg1ee_sod_jp.exe \
  setup-bg1ee_sod_jp.tp2 \
  bg1ee_sod_jp/ \
  README.md

echo "Windowsパッケージ作成完了: bg1ee_sod_jp_v1.0.0_windows.zip"
```

### Linux/macOS向けリリース

```bash
# パッケージを作成（WeiDUは含めない、ユーザーが個別にインストール）
tar czf bg1ee_sod_jp_v1.0.0_unix.tar.gz \
  setup-bg1ee_sod_jp.tp2 \
  bg1ee_sod_jp/ \
  install.sh \
  README.md \
  WEIDU_SETUP.md

echo "Unix/Linuxパッケージ作成完了: bg1ee_sod_jp_v1.0.0_unix.tar.gz"
```

## ファイルサイズについて

- `weidu.exe`: 約2-3MB
- このModのファイル: 約19MB (翻訳ファイル含む)
- 合計パッケージサイズ: 約22MB

## よくある質問

### Q: なぜ setup-*.exe という名前なのですか？

A: WeiDUの命名規則です。`setup-{modname}.exe` という形式にすることで、
   WeiDUが自動的に対応する `.tp2` ファイル (`setup-{modname}.tp2`) を
   読み込んで実行します。

### Q: weidu.exe と setup-bg1ee_sod_jp.exe の違いは？

A: 実体は同じWeiDU実行ファイルです。ファイル名によってどのModを
   インストールするかが決まります。

### Q: .gitignore に setup-*.exe が含まれているのはなぜ？

A: WeiDU実行ファイルはバイナリで、Gitリポジトリには含めないのが
   一般的です。ユーザーは配布パッケージから取得するか、
   公式サイトからダウンロードします。

## WeiDUバージョン

このModは WeiDU v249.00 以降での動作を推奨します。

最新版: https://github.com/WeiDUorg/weidu/releases

## トラブルシューティング

### Windows: 「このアプリは保護のためブロックされました」

1. 「詳細情報」をクリック
2. 「実行」をクリック
3. または、プロパティから「ブロックの解除」にチェック

### Linux/macOS: 「Permission denied」

```bash
chmod +x setup-bg1ee_sod_jp.exe  # または weidu
```

### 「SETUP-*.TP2 not found」エラー

setup-*.exe と setup-*.tp2 が同じディレクトリにあることを確認してください。
