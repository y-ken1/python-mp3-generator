# Python MP3 Generator

Pythonスクリプトを使用してMP3ファイルを生成します。

## 実行方法

### 1. 仮想環境の作成

```bash
python3 -m venv .venv
```

### 2. ライブラリのインストール

```bash
source .venv/bin/activate
pip install edge-tts
```

### 3. MP3の生成

事前にscript.txtにmp3にしたい文言を書いておく

```bash
./run.sh
```

## ファイル構成

```text
.
├── .venv/
├── generate.py
├── generate.sh
└── README.md
```

## 必要環境

- Python 3
- edge-tts

