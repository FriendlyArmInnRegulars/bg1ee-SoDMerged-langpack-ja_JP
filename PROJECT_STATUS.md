# プロジェクト状況 / Project Status

## 概要

BGEE & SoD 日本語化Mod - WeiDU形式の言語パック

**現在のバージョン**: v1.0.0  
**対応ゲーム**: Baldur's Gate Enhanced Edition + Siege of Dragonspear  
**言語**: 日本語 (ja_JP)

## 完成状況

### ✅ 完了項目

1. **基本構造**
   - WeiDU Mod ディレクトリ構造
   - setup-bg1ee_sod_jp.tp2 インストーラースクリプト
   - 言語定義とコンポーネント構成

2. **翻訳ファイル**
   - ✅ dialog.tra (9.9MB, 100,267行) - 配置済み
   - ✅ dialogf.tra (8.7MB, 100,254行) - 配置済み
   - ✅ setup.tra (885バイト) - インストーラーUI翻訳
   - ✅ game.tra (1.5KB) - 追加の翻訳

3. **ドキュメント**
   - ✅ README.md (日英併記)
   - ✅ CLAUDE.md (開発者向けガイド)
   - ✅ CONTRIBUTING.md (貢献ガイド)
   - ✅ 日本語/英語 readme (bg1ee_sod_jp/readme/)

4. **インフラ**
   - ✅ .gitignore (WeiDU関連ファイルの除外)
   - ✅ ディレクトリ構造

## ファイル構成

```
bg1ee-SoDMerged-langpack-ja_JP/
├── setup-bg1ee_sod_jp.tp2           # メインインストーラー
├── .gitignore
├── README.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── PROJECT_STATUS.md
└── bg1ee_sod_jp/
    ├── lang/ja_JP/
    │   ├── dialog.tra               # 9.9MB - ゲーム内テキスト翻訳
    │   ├── dialogf.tra              # 8.7MB - 女性用翻訳
    │   ├── setup.tra                # インストーラーUI翻訳
    │   ├── game.tra                 # 追加翻訳
    │   └── README_TRANSLATION.txt   # 翻訳ファイル説明
    ├── readme/
    │   ├── readme-ja_JP.txt         # 日本語ドキュメント
    │   └── readme.txt               # 英語ドキュメント
    └── translations/
        └── .gitkeep                 # 追加リソース用
```

## 翻訳カバレッジ

- **dialog.tra**: 71,404 文字列 (@0 ~ @71403)
- **dialogf.tra**: 71,404 文字列 (女性キャラクター用)
- **合計**: 約20万行の日本語翻訳

カバーする内容:
- ✅ BGEE本編のストーリー、ダイアログ
- ✅ Siege of Dragonspear拡張パック
- ✅ UI要素、メニュー、システムメッセージ
- ✅ アイテム説明、呪文説明
- ✅ キャラクター台詞

## インストール方法

### 前提条件

- Baldur's Gate Enhanced Edition (Steam/GOG/Beamdog版)
- (オプション) Siege of Dragonspear 拡張パック

### 手順

1. このリポジトリをクローン
2. ゲームディレクトリに以下をコピー:
   - `setup-bg1ee_sod_jp.tp2`
   - `bg1ee_sod_jp/` フォルダ

3. インストーラーを実行:
   ```bash
   # Windows
   setup-bg1ee_sod_jp.exe
   
   # Linux/Mac
   weidu setup-bg1ee_sod_jp.tp2
   ```

4. コンポーネントを選択:
   - [0] BGEE & SoD 日本語化 (推奨)
   - [10] Siege of Dragonspear コンテンツ日本語化
   - [20] UI要素の日本語化

5. ゲームを起動し、設定 → 言語 → Japanese (日本語) を選択

## テスト状況

### 未テスト項目

- [ ] 実際のBGEE環境でのインストールテスト
- [ ] ゲーム内での翻訳表示確認
- [ ] UI要素の表示確認（文字列の長さ、はみ出しなど）
- [ ] SoD拡張パックでの動作確認
- [ ] 女性キャラクターでの dialogf.tra 動作確認

### テスト推奨項目

1. **基本動作**
   - インストール/アンインストール
   - 言語切り替え
   - セーブデータの互換性

2. **翻訳品質**
   - メインストーリーのダイアログ
   - NPCの台詞
   - アイテム/呪文の説明
   - システムメッセージ

3. **表示確認**
   - 日本語フォントの表示
   - 長い文字列のUI表示
   - 改行の適切性

## 既知の問題

現時点では既知の問題はありません（テスト未実施のため）。

## 今後の作業

### 優先度: 高

- [ ] 実機でのインストールとテスト
- [ ] 翻訳品質のレビュー
- [ ] UIはみ出しの確認と修正

### 優先度: 中

- [ ] コンポーネント10, 20の実装詳細化
- [ ] WeiDU実行ファイルの同梱検討
- [ ] リリースパッケージの作成

### 優先度: 低

- [ ] 翻訳の継続的改善
- [ ] コミュニティフィードバックの収集
- [ ] 他のBG:EE Modとの互換性テスト

## 貢献

翻訳の改善や問題報告は大歓迎です！

- Issues: バグ報告、翻訳の問題
- Pull Requests: 翻訳の修正、改善
- Discussions: 質問、提案

詳細は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## ライセンス

非商用目的での使用・改変・再配布を許可します。

## クレジット

- 翻訳: FriendlyArmInnRegulars
- WeiDU: Westley Weimer
- オリジナルゲーム: Beamdog / BioWare

---

**最終更新**: 2025-10-28
