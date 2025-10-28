#!/bin/bash
# BGEE & SoD 日本語化Mod インストールスクリプト
# このスクリプトはLinux/macOS用です

echo "=========================================="
echo "BGEE & SoD 日本語化Mod インストーラー"
echo "=========================================="
echo ""

# BGEEのインストールパスを確認
if [ -z "$1" ]; then
    echo "使用方法: ./install.sh <BGEE_INSTALL_PATH>"
    echo ""
    echo "例:"
    echo "  ./install.sh ~/.steam/steam/steamapps/common/Baldur\'s\ Gate\ Enhanced\ Edition"
    echo "  ./install.sh ~/GOG\ Games/Baldur\'s\ Gate\ Enhanced\ Edition"
    echo ""
    exit 1
fi

BGEE_PATH="$1"

# パスの確認
if [ ! -d "$BGEE_PATH" ]; then
    echo "エラー: 指定されたディレクトリが存在しません: $BGEE_PATH"
    exit 1
fi

# BGEEの実行ファイルを確認
if [ ! -f "$BGEE_PATH/BaldursGate" ] && [ ! -f "$BGEE_PATH/Baldur.exe" ]; then
    echo "エラー: BGEEのインストールディレクトリではないようです"
    echo "       BaldursGate または Baldur.exe が見つかりません"
    exit 1
fi

echo "BGEEインストールパス: $BGEE_PATH"
echo ""

# Modファイルのコピー
echo "Modファイルをコピーしています..."

# setup-bg1ee_sod_jp.tp2 をコピー
cp -v setup-bg1ee_sod_jp.tp2 "$BGEE_PATH/"

# bg1ee_sod_jp ディレクトリをコピー
cp -rv bg1ee_sod_jp "$BGEE_PATH/"

echo ""
echo "コピー完了！"
echo ""

# WeiDUの確認
if ! command -v weidu &> /dev/null; then
    echo "警告: WeiDUがインストールされていません"
    echo ""
    echo "WeiDUのインストール方法:"
    echo "1. https://weidu.org から weidu をダウンロード"
    echo "2. /usr/local/bin/ に配置して実行権限を付与"
    echo "   sudo cp weidu /usr/local/bin/"
    echo "   sudo chmod +x /usr/local/bin/weidu"
    echo ""
    echo "または、BGEEディレクトリで直接実行:"
    echo "  cd \"$BGEE_PATH\""
    echo "  ./weidu setup-bg1ee_sod_jp.tp2"
    echo ""
    exit 0
fi

# WeiDUでインストール
echo "WeiDUでModをインストールしますか？ (y/n)"
read -r response

if [[ "$response" =~ ^[Yy]$ ]]; then
    cd "$BGEE_PATH" || exit 1
    weidu setup-bg1ee_sod_jp.tp2 --log setup-bg1ee_sod_jp.debug

    echo ""
    echo "インストール完了！"
    echo ""
    echo "ゲームを起動し、設定 → 言語 → Japanese (日本語) を選択してください"
else
    echo ""
    echo "後でインストールする場合は、以下を実行してください:"
    echo "  cd \"$BGEE_PATH\""
    echo "  weidu setup-bg1ee_sod_jp.tp2"
fi

echo ""
echo "=========================================="
