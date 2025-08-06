
#  Python `openpyxl` モジュール紹介

`openpyxl` は、Pythonで **Excel（.xlsx形式）ファイルを読み書きできるライブラリ** です。  
Excel操作を自動化したいときに便利です。

---

## 1. インストール方法

```bash
pip install openpyxl
```

---

## 2. 基本的な使い方

### 🔹 Excelファイルを開く（読み取り）

```python
from openpyxl import load_workbook

wb = load_workbook('example.xlsx')
ws = wb.active  # アクティブなシートを取得
```

### 🔹 セルの値を取得

```python
value = ws['A1'].value
print(value)
```

### 🔹 セルの値を書き込む

```python
ws['A1'] = 'こんにちは'
wb.save('example.xlsx')  # 上書き保存
```

---

## 3. 新規Excelファイルの作成

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello, Excel!'
wb.save('new_file.xlsx')
```

---

## 4. 行・列の操作

### 🔹 行を読み取る

```python
for row in ws.iter_rows(min_row=2, max_col=2):
    for cell in row:
        print(cell.value)
```

### 🔹 列を読み取る

```python
for col in ws.iter_cols(min_row=2, max_row=5, min_col=1, max_col=1):
    for cell in col:
        print(cell.value)
```

---

## 5. シートの操作

```python
# シート名一覧
print(wb.sheetnames)

# 新しいシートを追加
ws_new = wb.create_sheet(title='NewSheet')

# シートを削除
del wb['Sheet1']
```

---

## 6. セルの装飾（フォント・色・太字など）

```python
from openpyxl.styles import Font, PatternFill

ws['A1'] = 'タイトル'
ws['A1'].font = Font(bold=True, color='FFFFFF')
ws['A1'].fill = PatternFill(start_color='0000FF', end_color='0000FF', fill_type='solid')
```

---

## 7. よく使う機能まとめ

| 機能             | 説明                              |
|------------------|-----------------------------------|
| `load_workbook()`| 既存のExcelファイルを読み込む      |
| `Workbook()`     | 新しいExcelファイルを作成する      |
| `wb.save()`      | ファイルを保存する                 |
| `ws['A1']`       | セルにアクセス・値を取得/設定      |
| `iter_rows()`    | 行ごとの繰り返し処理               |
| `iter_cols()`    | 列ごとの繰り返し処理               |
| `create_sheet()` | 新しいシートを追加する             |
| `del wb['name']` | シートを削除する                   |

---

## 8. 注意点

- `.xls`（Excel 2003形式）はサポートされていません（`.xlsx`のみ）
- 大きなファイルを扱う場合は `read_only=True` を使うとメモリ節約になります

```python
wb = load_workbook('example.xlsx', read_only=True)
```

---

## 9. 参考

- 公式ドキュメント: https://openpyxl.readthedocs.io/

