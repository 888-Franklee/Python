import tkinter as tk
from tkinter import ttk
import random
import openpyxl
import os

def load_students(file_path):
    if not os.path.exists(file_path):
        result_label.config(text="学生名单文件不存在！")
        return []

    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        students = []
        for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
            student_name = row[1] 
            if student_name:
                students.append(student_name)
        return students
    except Exception as e:
        result_label.config(text=f"读取学生名单时出错: {str(e)}")
        return []

def pick_student():
    if students:
        selected_student = random.choice(students)
        result_label.config(text=f"请 {selected_student} 回答问题！")
    else:
        result_label.config(text="学生名单为空！")

root = tk.Tk()
root.title("点名APP")
root.geometry("400x300")
root.config(bg="#F0F8FF")  

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), padding=10, background="#4682B4")
style.configure("TLabel", font=("Helvetica", 20), padding=10)

students = load_students(r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Roll Call APP\001_Main\students.xlsx")  # 请将文件路径改为你的Excel路径

title_label = tk.Label(root, text="欢迎使用随机点名APP", font=("Helvetica", 24, "bold"), bg="#F0F8FF", fg="#4682B4")
title_label.pack(pady=20)

pick_button = ttk.Button(root, text="随机点名", command=pick_student)
pick_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#F0F8FF", fg="#000000")
result_label.pack(pady=20)

root.mainloop()
