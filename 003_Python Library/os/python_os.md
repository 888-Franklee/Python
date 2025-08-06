
#  Python `os` モジュール紹介

Pythonの `os` モジュールは、ファイルやディレクトリの操作、環境変数の取得、プロセス制御など、OSに関する操作を行うための標準ライブラリです。

---

## 1. インポート

```python
import os
```

---

## 2. ディレクトリの操作

### 🔹 現在の作業ディレクトリを取得・変更

```python
print(os.getcwd())            # 現在の作業ディレクトリを取得
os.chdir('/path/to/dir')      # 作業ディレクトリを変更
```

### 🔹 ディレクトリを作成

```python
os.mkdir('new_folder')              # フォルダを1つ作成
os.makedirs('parent/child')         # ネストしたフォルダを一括作成
```

### 🔹 ディレクトリを削除

```python
os.rmdir('empty_folder')            # 空のフォルダのみ削除
os.removedirs('parent/child')       # ネストされた空のフォルダを一括削除
```

---

## 3. ファイル操作

### 🔹 ファイルやフォルダの存在確認

```python
os.path.exists('file.txt')          # ファイルまたはフォルダが存在するか
os.path.isfile('file.txt')          # ファイルかどうか
os.path.isdir('folder')             # フォルダかどうか
```

### 🔹 ファイルやフォルダの削除・名前変更

```python
os.remove('file.txt')               # ファイル削除
os.rename('old.txt', 'new.txt')     # 名前変更や移動
```

---

## 4. 環境変数

```python
print(os.environ.get('HOME'))       # 環境変数HOMEの値を取得
os.environ['MY_VAR'] = 'value'      # 環境変数の設定（プロセス内のみ有効）
```

---

## 5. パス操作（`os.path`）

```python
import os

# パスを結合
path = os.path.join('folder', 'file.txt')  # 'folder/file.txt'

# 拡張子を取得
filename, ext = os.path.splitext('test.py')  # ('test', '.py')
```

---

## 6. 使用例

```python
import os

folder = 'output'
file_name = 'data.txt'

if not os.path.exists(folder):
    os.makedirs(folder)

os.rename(file_name, os.path.join(folder, file_name))
```

---

## 7. よく使う関数まとめ

| 関数名              | 説明                             |
|---------------------|----------------------------------|
| `os.getcwd()`       | カレントディレクトリ取得         |
| `os.chdir()`        | カレントディレクトリ変更         |
| `os.mkdir()`        | フォルダ作成                     |
| `os.makedirs()`     | ネストされたフォルダ作成         |
| `os.listdir()`      | フォルダ内のファイル一覧取得     |
| `os.path.exists()`  | ファイルやフォルダの存在確認     |
| `os.remove()`       | ファイル削除                     |
| `os.rmdir()`        | フォルダ削除                     |
| `os.rename()`       | ファイル/フォルダ名の変更         |
| `os.environ`        | 環境変数の取得と設定             |

---

## 8. 補足

- Python3.4以降は、`pathlib` モジュールも便利です（オブジェクト指向的）
- ファイルの中身の操作は `open()` を使用
