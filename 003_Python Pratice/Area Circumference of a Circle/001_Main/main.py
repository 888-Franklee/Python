import tkinter as tk
from tkinter import messagebox
import math

app = tk.Tk()
app.title("圆的面积和周长计算器")
app.geometry("300x200")

def calculate():
    try:
        radius = float(radius_entry.get())
        if radius < 0:
            messagebox.showerror("输入错误", "半径不能为负数")
            return
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        area_label.config(text=f"面积: {area:.2f}")
        circumference_label.config(text=f"周长: {circumference:.2f}")
    except ValueError:
        messagebox.showerror("输入错误", "请输入一个有效的数字")

radius_label = tk.Label(app, text="输入半径:")
radius_label.pack(pady=5)

radius_entry = tk.Entry(app)
radius_entry.pack(pady=5)

calculate_button = tk.Button(app, text="计算", command=calculate)
calculate_button.pack(pady=10)

area_label = tk.Label(app, text="面积: ")
area_label.pack(pady=5)

circumference_label = tk.Label(app, text="周长: ")
circumference_label.pack(pady=5)

app.mainloop()
