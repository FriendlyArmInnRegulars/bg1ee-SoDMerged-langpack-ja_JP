# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is for a Japanese (ja_JP) language pack for Baldur's Gate 1 Enhanced Edition with Siege of Dragonspear (SoD) merged content. This is a WeiDU-based mod for the Infinity Engine game.

**Mod name**: bg1ee_sod_jp
**Main installer**: setup-bg1ee_sod_jp.tp2
**Version**: v1.0.0

## Repository Structure

```
setup-bg1ee_sod_jp.tp2          # Main WeiDU installer script
bg1ee_sod_jp/
  ├── lang/ja_JP/               # Japanese translation files
  │   ├── setup.tra             # Installer UI translations
  │   └── game.tra              # In-game text translations
  ├── readme/                   # Documentation
  │   ├── readme-ja_JP.txt      # Japanese documentation
  │   └── readme.txt            # English documentation
  ├── translations/             # Additional translation resources
  └── backup/                   # Auto-generated backup folder (gitignored)
```

## WeiDU Mod Structure

WeiDU is the modding framework for Infinity Engine games (Baldur's Gate, Icewind Dale, Planescape: Torment). Key concepts:

- **tp2 files**: WeiDU script files that define the mod installation process
- **tra files**: Translation files containing localized strings in the format `@string_number = ~text~`
- **d files**: Dialogue files for character conversations
- **baf/bcs files**: Script files for AI and triggers
- **2da files**: Table files for game data (classes, spells, etc.)

## Mod Components

This mod has three components (defined in setup-bg1ee_sod_jp.tp2):

1. **Component 0**: BGEE & SoD 日本語化 (Main Japanese translation)
   - Core Japanese localization for BGEE
   - Required for other components

2. **Component 10**: Siege of Dragonspear コンテンツ日本語化
   - Additional translations specific to SoD expansion
   - Requires SoD to be installed (checks for bd0103.are)

3. **Component 20**: UI要素の日本語化
   - Japanese localization of UI elements
   - Optional but recommended

## Common WeiDU Commands

Language packs typically use these WeiDU functions:

- `LANGUAGE`: Declares a supported language (used in setup-bg1ee_sod_jp.tp2:14)
- `STRING_SET`: Modifies existing game strings by reference number
- `COMPILE`: Compiles dialogue/script files with translations
- `COPY_EXISTING`: Copies and patches existing game files
- `APPEND` / `EXTEND_TOP` / `EXTEND_BOTTOM`: Adds to existing dialogue
- `REQUIRE_PREDICATE`: Checks conditions before installing component
- `GAME_IS`: Detects which Infinity Engine game is installed

## Development Workflow

### Testing the Mod

1. Copy mod files to a test BGEE installation
2. Run installer: `weidu setup-bg1ee_sod_jp.tp2 --log setup-bg1ee_sod_jp.debug`
3. Install component(s) to test
4. Launch game and verify translations
5. Check debug log for errors
6. Uninstall with `weidu setup-bg1ee_sod_jp.tp2 --uninstall`

### Translation Files

The mod includes the following translation files:

- **dialog.tra** (100,267 lines): Main game text translations for male/neutral characters (@0 to @71403)
- **dialogf.tra** (100,254 lines): Game text translations for female player characters
- **setup.tra**: Installer UI translations (component names, messages)
- **game.tra**: Additional game text and mod-specific strings

### How WeiDU Language Packs Work

When you declare translation files in the `LANGUAGE` block (lines 22-27 of setup-bg1ee_sod_jp.tp2), WeiDU automatically:

1. Reads all .tra files
2. Generates `dialog.tlk` and `dialogf.tlk` files for the ja_JP language
3. Places them in `<game_dir>/lang/ja_JP/`
4. Makes the language available in game settings

Players simply select "Japanese (日本語)" in the game options to use the translations.

### Editing Existing Translations

1. Locate the string in `bg1ee_sod_jp/lang/ja_JP/dialog.tra` or `dialogf.tra`
2. Edit the text after `@number = ~` and before the closing `~`
3. Save the file with UTF-8 encoding
4. Reinstall the mod to test changes

### Adding New Translations

1. Add to `bg1ee_sod_jp/lang/ja_JP/game.tra`: `@5000 = ~新しい翻訳~`
2. Reference in tp2 using STRING_SET or in compiled dialogues
3. Reinstall mod to test
4. Update version number in setup-bg1ee_sod_jp.tp2 when complete

## Installation Process

Users install this mod by:
1. Placing mod files in the BGEE game directory
2. Running `setup-bg1ee_sod_jp.exe` (Windows) or `weidu setup-bg1ee_sod_jp.tp2` (Linux/macOS)
3. Selecting components to install (0, 10, 20)

## Character Encoding

Japanese language files must use UTF-8 encoding. WeiDU handles the conversion to the game's internal encoding during installation.

## Testing

To test a language pack:
1. Install the mod in a test game directory
2. Launch the game and verify text displays correctly
3. Check for encoding issues, text overflow in UI elements
4. Verify dialogue choices and journal entries

## Key Considerations for Japanese Localization

- Japanese text may be longer than English, requiring UI adjustments
- Ensure proper handling of kanji, hiragana, and katakana
- Test with both full-width and half-width characters
- Verify compatibility with Enhanced Edition's UI scaling
