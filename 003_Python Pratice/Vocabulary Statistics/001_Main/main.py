import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def count_stars_in_pdf(file_path):
    star_count = 0
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    star_count += text.count('★')
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
    return star_count

def calculate_star_count():
    folder_path = folder_entry.get()
    language_option = language_var.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("错误", "请选择有效的文件夹路径")
        return

    star_total = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf') and language_option in file:
                file_path = os.path.join(root, file)
                star_total += count_stars_in_pdf(file_path)

    if star_total > 0:
        result = star_total // 5
        result_label.config(text=f"单词数为: {result}")
    else:
        result_label.config(text="未找到 '★'")
        messagebox.showinfo("结果", "未在文件夹中的指定 PDF 文件中找到 '★'")

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

root = tk.Tk()
root.title("单词数量查询")

tk.Label(root, text="选择文件夹：").grid(row=0, column=0, padx=10, pady=5)


default_folder = r"D:\Lee Encyclopaedia（李論百科全書）\003_Corpus Translation"
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=5)
folder_entry.insert(0, default_folder)  
tk.Button(root, text="浏览", command=select_folder).grid(row=0, column=2, padx=10, pady=5)

language_var = tk.StringVar(value="English")
language_frame = tk.Frame(root)
language_frame.grid(row=1, column=0, columnspan=3, pady=10)
tk.Radiobutton(language_frame, text="English", variable=language_var, value="English").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(language_frame, text="Japanese", variable=language_var, value="Japanese").pack(side=tk.LEFT, padx=10)

tk.Button(root, text="查询", command=calculate_star_count).grid(row=2, column=1, padx=10, pady=20)

result_label = tk.Label(root, text="Get Busy Living or Get Busy Dying")
result_label.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
