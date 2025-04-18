
# Pythonのlen()関数について

##  len() 関数とは？

Python の組み込み関数 `len()` は、**オブジェクトの「長さ」や「要素数」**を取得するために使われます。  
これは Python の「シーケンス型」や「コレクション型」に対してよく使われる関数で、対象オブジェクトの `__len__()` メソッドを内部的に呼び出しています。

```python
len(obj)  # 実際には obj.__len__() が呼び出されている
```

---

##  対応している主なデータ型

| データ型 | 説明 | 例 |
|----------|------|-----|
| `str`    | 文字列の長さ（文字数） | `len("Python") → 6` |
| `list`   | リストの要素数 | `len([1, 2, 3]) → 3` |
| `tuple`  | タプルの要素数 | `len((1, 2)) → 2` |
| `dict`   | 辞書のキーの数 | `len({"a": 1, "b": 2}) → 2` |
| `set`    | 集合の要素数 | `len(set([1, 2, 2, 3])) → 3` |
| `range`  | 範囲オブジェクトの要素数 | `len(range(5)) → 5` |
| `bytes`, `bytearray` | バイナリデータの長さ | `len(b"abc") → 3` |

---

##  基本的な使用例

```python
# 文字列の長さ
text = "こんにちは"
print(len(text))  # 出力: 5（5文字）

# リストの要素数
numbers = [10, 20, 30]
print(len(numbers))  # 出力: 3

# タプルの要素数
t = ("a", "b", "c")
print(len(t))  # 出力: 3

# 辞書のキー数
data = {"id": 1, "name": "Alice"}
print(len(data))  # 出力: 2
```

---

##  エラー例と注意点

`len()` は「長さ」を持たないオブジェクトに対しては使用できません。たとえば、`int` や `float` 型に使うとエラーになります。

```python
x = 123
print(len(x))  # TypeError: object of type 'int' has no len()
```

---

##  ユーザー定義クラスとの連携

独自クラスに `__len__()` メソッドを実装すれば、`len()` を使えるようになります。

```python
class CustomData:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = CustomData([1, 2, 3, 4])
print(len(obj))  # 出力: 4
```

---

##  応用例

### ファイルの行数を数える

```python
with open("example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("行数:", len(lines))
```

### 最長の単語を探す

```python
words = ["Python", "AI", "OpenAI", "ChatGPT"]
longest = max(words, key=len)
print(longest)  # 出力: ChatGPT
```

---

##  パフォーマンス面

`len()` は非常に高速な処理です。なぜなら、Python の多くの組み込み型では要素数が内部的にキャッシュされているため、`len()` は O(1)（定数時間）で動作します。

ただし、`__len__()` を独自に定義した場合は、その中での処理に応じてパフォーマンスが変わる可能性があります。

---

##  まとめ

- `len()` は文字列、リスト、辞書などの長さを取得する。
- オブジェクトが `__len__()` を持たないと使えない。
- ユーザー定義クラスにも `__len__()` を定義すれば対応可能。
- 多くのケースで O(1) の高速動作。

`len()` は Python プログラムを書くうえで欠かせない基本かつ強力な関数です。使い方をマスターすることで、データの処理や判定を効率よく行えるようになります。

