# BGEE & SoD 日本語化パック / Japanese Language Pack

Baldur's Gate Enhanced Edition と Siege of Dragonspear の日本語化Modです。

A Japanese localization mod for Baldur's Gate Enhanced Edition and Siege of Dragonspear.

## 特徴 / Features

- ✅ BGEE本編の日本語化 / BGEE main game localization
- ✅ SoD拡張パックの日本語化 / SoD expansion localization
- ✅ UI要素の日本語化 / UI elements localization
- ✅ WeiDU形式で簡単インストール / Easy installation with WeiDU

## インストール / Installation

詳細は `bg1ee_sod_jp/readme/readme-ja_JP.txt` をご覧ください。

See `bg1ee_sod_jp/readme/readme-ja_JP.txt` for detailed instructions.

### クイックスタート / Quick Start

**注意**: インストールには `setup-bg1ee_sod_jp.exe` (Windows) または `weidu` (Linux/macOS) が必要です。
詳細は [WEIDU_SETUP.md](WEIDU_SETUP.md) を参照してください。

1. [Releases](https://github.com/FriendlyArmInnRegulars/bg1ee-SoDMerged-langpack-ja_JP/releases)からパッケージをダウンロード
2. ゲームフォルダに解凍 / Extract to game folder
3. `setup-bg1ee_sod_jp.exe` を実行 (Windows) / Run `setup-bg1ee_sod_jp.exe` (Windows)
   または `./install.sh <game_path>` (Linux/macOS)
4. コンポーネントを選択してインストール / Select and install components
5. ゲーム設定で Japanese (日本語) を選択 / Select Japanese (日本語) in game settings

## 開発 / Development

### 必要なツール / Required Tools

- WeiDU (https://weidu.org)
- テキストエディタ（UTF-8対応）/ Text editor with UTF-8 support

### ファイル構成 / File Structure

```
setup-bg1ee_sod_jp.tp2          # メインインストーラースクリプト
bg1ee_sod_jp/
  ├── lang/ja_JP/               # 日本語翻訳ファイル
  │   ├── setup.tra             # インストーラーUI翻訳
  │   └── game.tra              # ゲーム内テキスト翻訳
  ├── readme/                   # ドキュメント
  │   ├── readme-ja_JP.txt      # 日本語README
  │   └── readme.txt            # 英語README
  └── translations/             # 追加の翻訳リソース
```

### 翻訳の追加方法 / Adding Translations

1. `bg1ee_sod_jp/lang/ja_JP/game.tra` を編集
2. 形式: `@番号 = ~日本語テキスト~`
3. `setup-bg1ee_sod_jp.tp2` で該当する文字列を参照

詳細は `CLAUDE.md` をご覧ください。

## 貢献 / Contributing

プルリクエストを歓迎します！翻訳の改善提案もお待ちしています。

Pull requests are welcome! We appreciate translation improvements.

## ライセンス / License

非商用目的での使用・改変・再配布を許可します。

Free to use, modify, and redistribute for non-commercial purposes.

## クレジット / Credits

- 翻訳 / Translation: FriendlyArmInnRegulars
- WeiDU: Westley Weimer

## サポート / Support

- Issues: https://github.com/FriendlyArmInnRegulars/bg1ee-SoDMerged-langpack-ja_JP/issues
- Discussions: GitHubのDiscussionsタブをご利用ください
