# PyPDF2の紹介と活用ガイド

## 1.  PyPDF2とは？

**PyPDF2**は、PDFファイルを操作するための純粋なPythonライブラリです。
以下のような操作が可能です：

- PDFの読み取り
- 複数PDFの結合
- PDFの分割
- 暗号化・復号
- テキストやメタデータの抽出
- ページの回転・トリミング

---

## 2. インストール方法

```bash
pip install PyPDF2
```

---

## 3. 基本的な使用例

### 🔹PDFファイルの読み取り

```python
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
print(len(reader.pages))  # ページ数を表示

page = reader.pages[0]
print(page.extract_text())  # 最初のページからテキストを抽出
```

### 🔹 複数PDFファイルの結合

```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.write("merged.pdf")
merger.close()
```

### 🔹 PDFのページごとの分割

```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("example.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as f:
        writer.write(f)
```

### 🔹 ページの回転

```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("example.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)
writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)
```

### 🔹 PDFの暗号化

```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("example.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("mypassword")
with open("encrypted.pdf", "wb") as f:
    writer.write(f)
```

---

## 3.  上級活用：表や注釈の抽出

PyPDF2単体では表や注釈の抽出に制限があります。以下のライブラリとの併用を推奨します：

### 表の抽出（例：`pdfplumber`との併用）

```python
import pdfplumber

with pdfplumber.open("example.pdf") as pdf:
    first_page = pdf.pages[0]
    table = first_page.extract_table()
    print(table)
```

### 注釈の抽出（PyPDF2で可能な例）

```python
from PyPDF2 import PdfReader

reader = PdfReader("annotated.pdf")
page = reader.pages[0]

if "/Annots" in page:
    for annot in page["/Annots"]:
        annot_obj = annot.get_object()
        print(annot_obj.get("/Contents"))
```

---

## 4. 注意事項

- テキスト抽出はPDFの構造に依存するため、結果が不完全になる場合があります。
- PyPDF2は画像・フォーム・複雑なレイアウトの処理には向いていません。

---

## 5. まとめ

PyPDF2は、PDF処理を自動化したい場合に便利な軽量ライブラリです。
より高度なPDF操作を必要とする場合は、以下も併用しましょう：

- `pdfplumber`（表・テキスト精密抽出）
- `PyMuPDF`（画像処理・注釈取得）
- `reportlab`（PDF生成）