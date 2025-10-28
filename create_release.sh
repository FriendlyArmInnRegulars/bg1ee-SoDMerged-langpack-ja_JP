#!/bin/bash
# リリースパッケージ作成スクリプト

set -e

VERSION="v1.0.0"
MOD_NAME="bg1ee_sod_jp"

echo "=========================================="
echo "BGEE & SoD 日本語化Mod"
echo "リリースパッケージ作成"
echo "バージョン: $VERSION"
echo "=========================================="
echo ""

# 作業ディレクトリの確認
if [ ! -f "setup-bg1ee_sod_jp.tp2" ]; then
    echo "エラー: setup-bg1ee_sod_jp.tp2 が見つかりません"
    echo "このスクリプトはリポジトリのルートディレクトリから実行してください"
    exit 1
fi

# リリースディレクトリの作成
RELEASE_DIR="releases"
mkdir -p "$RELEASE_DIR"

echo "📦 Unix/Linux/macOS用パッケージを作成中..."
tar czf "$RELEASE_DIR/${MOD_NAME}_${VERSION}_unix.tar.gz" \
    --exclude='.git' \
    --exclude='releases' \
    --exclude='*.exe' \
    --exclude='create_release.sh' \
    setup-bg1ee_sod_jp.tp2 \
    bg1ee_sod_jp/ \
    install.sh \
    README.md \
    CLAUDE.md \
    CONTRIBUTING.md \
    PROJECT_STATUS.md \
    WEIDU_SETUP.md

echo "✅ Unix/Linuxパッケージ: $RELEASE_DIR/${MOD_NAME}_${VERSION}_unix.tar.gz"

# Windows用パッケージ（setup-*.exe が必要）
if [ -f "setup-bg1ee_sod_jp.exe" ]; then
    echo ""
    echo "📦 Windows用パッケージを作成中..."

    zip -r "$RELEASE_DIR/${MOD_NAME}_${VERSION}_windows.zip" \
        setup-bg1ee_sod_jp.exe \
        setup-bg1ee_sod_jp.tp2 \
        bg1ee_sod_jp/ \
        README.md \
        CONTRIBUTING.md \
        WEIDU_SETUP.md \
        -x "*.git*" "releases/*"

    echo "✅ Windowsパッケージ: $RELEASE_DIR/${MOD_NAME}_${VERSION}_windows.zip"
else
    echo ""
    echo "⚠️  警告: setup-bg1ee_sod_jp.exe が見つかりません"
    echo "   Windows用パッケージを作成するには、WeiDUをダウンロードして"
    echo "   setup-bg1ee_sod_jp.exe として保存してください。"
    echo ""
    echo "   詳細: WEIDU_SETUP.md を参照"
    echo ""
    echo "   クイックセットアップ:"
    echo "   wget https://github.com/WeiDUorg/weidu/releases/download/v249.00/weidu-windows-x86.zip"
    echo "   unzip weidu-windows-x86.zip"
    echo "   cp weidu.exe setup-bg1ee_sod_jp.exe"
    echo "   ./create_release.sh"
fi

# ソースコードアーカイブ（開発者向け）
echo ""
echo "📦 ソースコードアーカイブを作成中..."
git archive --format=tar.gz --prefix="${MOD_NAME}-${VERSION}/" HEAD \
    -o "$RELEASE_DIR/${MOD_NAME}_${VERSION}_source.tar.gz" 2>/dev/null || \
    tar czf "$RELEASE_DIR/${MOD_NAME}_${VERSION}_source.tar.gz" \
        --exclude='.git' \
        --exclude='releases' \
        --exclude='*.exe' \
        .

echo "✅ ソースコード: $RELEASE_DIR/${MOD_NAME}_${VERSION}_source.tar.gz"

# ファイルサイズの表示
echo ""
echo "=========================================="
echo "作成されたパッケージ:"
echo "=========================================="
ls -lh "$RELEASE_DIR"/*.{tar.gz,zip} 2>/dev/null | awk '{print $9, "\t", $5}'

echo ""
echo "=========================================="
echo "✅ リリースパッケージの作成が完了しました！"
echo "=========================================="
echo ""
echo "パッケージは $RELEASE_DIR/ ディレクトリにあります"
echo ""
echo "次のステップ:"
echo "1. パッケージをテスト環境でインストールテスト"
echo "2. GitHubでリリースを作成"
echo "3. 作成したパッケージをアップロード"
echo ""
