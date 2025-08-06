import tkinter as tk  
from tkinter import messagebox, font  
import pandas as pd  
import random  
 
def read_names_from_excel(file_path):  
    try:  
        df = pd.read_excel(file_path, engine='openpyxl')  
        names = df.iloc[:, 0].tolist() 
        return names  
    except Exception as e:  
        print(f"Error reading Excel file: {e}")  
        return []  
   
def pick_winner(names):  
    if not names:  
        return None  
    winner = random.choice(names)  
    return winner  
    
def show_winner():  
    names = read_names_from_excel(r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Roll Call APP\001_Main\students.xlsx") 
    if not names:  
        messagebox.showerror("Error", "No names found in the Excel file.")  
        return  
    winner = pick_winner(names)  
    messagebox.showinfo("恭喜获奖者", f"恭喜！{winner} ")  
   
root = tk.Tk()  
root.title("精美抽奖App")  
root.geometry("400x200")  
root.configure(bg='lightblue') 
  
font_style = font.Font(family='Helvetica', size=14, weight='bold')  
  
title_label = tk.Label(root, text="抽奖应用", font=font_style, bg='lightblue', fg='darkblue')  
title_label.pack(pady=20)  
  
draw_button = tk.Button(root, text="开始抽奖", command=show_winner, font=font_style, bg='green', fg='white', padx=20, pady=10)  
draw_button.pack(pady=20)  
    
root.mainloop()