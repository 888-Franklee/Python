import os
import tkinter as tk
from tkinter import filedialog, Listbox, Scrollbar, Radiobutton, StringVar

root = tk.Tk()
root.title("文件类型查看器")
root.geometry("600x500")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        show_files(folder_path, file_type.get())


def show_files(folder, extension):
    file_listbox.delete(0, tk.END)  
    unique_files = set()  
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                unique_files.add(filename) 

    for filename in sorted(unique_files):  
        file_listbox.insert(tk.END, filename)

folder_label = tk.Label(root, text="请选择一个文件夹", wraplength=500)
folder_label.pack(pady=10)


select_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_button.pack(pady=10)

file_type = StringVar()
file_type.set(".pdf")  

pdf_radiobutton = Radiobutton(root, text="PDF文件", variable=file_type, value=".pdf")
pdf_radiobutton.pack()

word_radiobutton = Radiobutton(root, text="Word文件", variable=file_type, value=".docx")
word_radiobutton.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

file_listbox = Listbox(root, width=80, height=20, yscrollcommand=scrollbar.set)
file_listbox.pack(pady=10)

scrollbar.config(command=file_listbox.yview)

root.mainloop()
