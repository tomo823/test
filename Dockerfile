# ベースイメージとしてPython 3.10.6を使用
FROM python:3.10.6-slim-buster

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 必要なPythonパッケージをインストールする場合は以下のようにします
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# コンテナ起動時に実行されるコマンドを指定
CMD ["python", "your_script.py"]