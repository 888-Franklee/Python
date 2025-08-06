import tkinter as tk  
from tkinter import ttk  
import pandas as pd  
    
def load_data():  
    file_path = r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Quick reference chart APP\001_Main\西暦和暦早見表.xlsx"  
    data = pd.read_excel(file_path)  
    return data  
  
def create_gui(data):  
    root = tk.Tk()  
    root.title('年份选择器')  
  
    tree = ttk.Treeview(root, columns=('西暦', '和歴'), show='headings')  
    tree.heading('西暦', text='西暦')  
    tree.heading('和歴', text='和歴')  
  
    for index, row in data.iterrows():  
        tree.insert('', 'end', values=(row['西暦'], row['和歴']))  
  
    def on_tree_select(event):  
        selection = tree.selection()  
        if selection:  
            item = tree.item(selection)  
            selected_year = item['values'][0]  
            corresponding_era = item['values'][1]  
            result_label.config(text=f'和歴: {corresponding_era}')  
  
    tree.bind('<<TreeviewSelect>>', on_tree_select)  
   
    result_label = tk.Label(root, text='', width=50)  
    result_label.pack(pady=20)  
  
    tree.pack(fill='both', expand=True)  
    
    root.mainloop()  
   
def main():  
    data = load_data()  
    create_gui(data)  
  
if __name__ == '__main__':  
    main()