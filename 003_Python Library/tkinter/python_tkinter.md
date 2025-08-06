
#  Tkinter入門ガイド

##  1. Tkinterとは？

Tkinterは、Pythonに標準で付属しているGUI（Graphical User Interface）ライブラリです。  
ボタン、ラベル、テキストボックスなどのGUI部品を使って、簡単にウィンドウアプリケーションを作成できます。

---

##  2. Tkinterの特徴

- Python標準ライブラリに含まれており、追加インストール不要
- 軽量で学習コストが低い
- 小〜中規模のGUIアプリに最適

---

##  3. 基本構文

```python
import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Tkinterアプリ")
root.geometry("300x200")

# ラベルの追加
label = tk.Label(root, text="こんにちは、Tkinter！")
label.pack()

# ボタンの追加
button = tk.Button(root, text="閉じる", command=root.quit)
button.pack()

# メインループの開始
root.mainloop()
```

---

##  4. 主なウィジェット（部品）

| ウィジェット | 説明                     |
|--------------|--------------------------|
| `Label`      | テキスト表示             |
| `Button`     | ボタン                   |
| `Entry`      | 1行テキスト入力欄       |
| `Text`       | 複数行テキスト入力欄     |
| `Checkbutton`| チェックボックス         |
| `Radiobutton`| ラジオボタン             |
| `Frame`      | コンテナ                 |

---

##  5. イベント処理

```python
def on_click():
    print("ボタンがクリックされました！")

button = tk.Button(root, text="クリック", command=on_click)
button.pack()
```

---

##  6. レイアウト管理

- `pack()`: 簡易的な自動配置
- `grid()`: 表形式の配置
- `place()`: 座標指定での配置

---

##  7. まとめ

Tkinterは、初心者に優しいGUIライブラリです。  
まずは基本的なウィジェットとレイアウトを覚えて、簡単なGUIアプリを作ってみましょう！

---

## 8. 公式ドキュメント

- [Tkinter — Python Docs](https://docs.python.org/ja/3/library/tk.html)
