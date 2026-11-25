# tools/ — TLK生成・適用ツール

`dialog.tra` / `dialogf.tra` から日本語TLKを生成し、ゲームへ適用するためのPythonスクリプトです（Python 3.10以上、外部ライブラリ不要）。

## Steam版（SoDがDLC zipのまま）への適用手順

Steam版BGEEでは、SoDのテキストは `dlc/sod-dlc.zip` 内の `lang/ja_JP/dialog.tlk` / `dialogf.tlk` から読み込まれます。ゲームフォルダの `lang/ja_JP/` にファイルを置いても反映されないため、zip内のTLKを差し替えます。Steam版 v2.7.3.0 で動作確認済みです。

1. **ベースとなる公式TLKを取り出す**（音声参照・フラグを流用します）
   ```
   unzip dlc/sod-dlc.zip "lang/ja_JP/*" -d base
   ```
2. **TLKを生成**
   ```
   py -I tools/build.py base/lang/ja_JP bg1ee_sod_jp/lang/ja_JP out
   ```
3. **zipをバックアップ**（`dlc/` フォルダの外に置くこと。`dlc/` 内のzipはゲームが読み込むため）
4. **zip内のTLKを差し替え**
   ```
   py -I tools/patchzip.py dlc/sod-dlc.zip lang/ja_JP/dialog.tlk=out/dialog.tlk lang/ja_JP/dialogf.tlk=out/dialogf.tlk
   ```
   `sod-dlc.zip` は無圧縮(Stored)で、正規の中央ディレクトリの後ろに古いレコードが残っています（Pythonの `zipfile` では開けません）。`patchzip.py` は新しいエントリを末尾に追記して中央ディレクトリを書き直し、残っているレコードはそのまま保持します。
5. ゲームの言語設定を日本語にします。

Steamの更新や「整合性の確認」を行うとzipが元に戻るため、その場合は手順4を再実行してください。元に戻すにはバックアップしたzipを書き戻します。

## スクリプト一覧

| ファイル | 用途 |
|---|---|
| `tlk.py` | TLK V1の読み書きと.traのパース（共通ライブラリ） |
| `build.py` | .traと公式TLKからdialog.tlk / dialogf.tlkを生成 |
| `patchzip.py` | Stored形式zip内のエントリを差し替え |
| `patch_tra.py` | .traの指定した@番号のテキストだけを置換（その他のバイトは保持） |
| `extract.py` | 未翻訳の英語が残っている文字列を一覧化 |
| `lookup.py` | 英語原文を正規表現で検索して既存の日本語訳を表示（訳語の統一用） |

`extract.py` / `lookup.py` には公式の英語TLK（`dlc/sod-dlc.zip` 内の `lang/en_US/dialog.tlk`）が必要です。
