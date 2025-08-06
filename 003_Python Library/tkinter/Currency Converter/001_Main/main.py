import tkinter as tk  
from tkinter import ttk  
  
exchange_rates = {  
    "CNY_to_USD": 6.75,  
    "CNY_to_JPY": 15.5,  
    "USD_to_CNY": 1 / 6.75,  
    "USD_to_JPY": 15.5 / 6.75,  
    "JPY_to_CNY": 1 / 15.5,  
    "JPY_to_USD": 6.75 / 15.5  
}  
  
def convert():  
    try:  
        amount = float(entry.get())  
        source_currency = source_currency_var.get()  
        target_currency = target_currency_var.get()  
           
        rate = exchange_rates.get(f"{source_currency}_to_{target_currency}", None)  
        if rate is None:  
            raise ValueError("无效的货币组合")  
          
        result = amount * rate  
        label.config(text=f"转换后金额：{result:.2f} {target_currency}")  
    except ValueError as e:  
        label.config(text=str(e))  
  
root = tk.Tk()  
root.title("双向货币转换器")  
  
source_currency_var = tk.StringVar(value="CNY")  
source_currency_menu = ttk.OptionMenu(root, source_currency_var, "CNY", "USD", "JPY")  
source_currency_menu.pack(pady=10)  
  
target_currency_var = tk.StringVar(value="USD")  
target_currency_menu = ttk.OptionMenu(root, target_currency_var, "USD", "JPY")  
target_currency_menu.pack(pady=10)  
   
label1 = tk.Label(root, text="输入金额：", font=("Arial", 18))  
label1.pack(pady=10)  
  
entry = tk.Entry(root, font=("Arial", 18))  
entry.pack(pady=10)  
  
button = tk.Button(root, text="转换", font=("Arial", 18), command=convert)  
button.pack(pady=10)  
  
label = tk.Label(root, text="", font=("Arial", 18))  
label.pack(pady=10)  
   
root.mainloop()











































































