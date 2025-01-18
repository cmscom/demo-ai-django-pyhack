# demo-ai-django-pyhack

AIでDjangoでPyHackの申し込みをやってみるプロジェクトです。

## 環境構築

### 必要条件
- Python 3.12以上
- pip (最新版推奨)

### セットアップ手順
1. リポジトリをクローン:
   ```bash
   git clone https://github.com/cmscom/demo-ai-django-pyhack.git
   cd demo-ai-django-pyhack
   ```

2. 開発用パッケージをインストール:
   ```bash
   pip install -e ".[dev]"
   ```

## 開発

### コードスタイル
コードの品質チェックとスタイル整形には以下のコマンドを実行:

#### Ruffによるコード品質チェック
```bash
ruff check .
```

#### インポート順序の整理（isort）
```bash
isort .
```

## Hello World 機能
ルートパス("/")へアクセスすると "Hello World" が表示されます。

## テスト実行方法
pytestを利用してテストを実行します:
```bash
pytest
```

テストは以下を確認します：
- Hello World機能が正常に動作すること
- ステータスコード200が返されること
