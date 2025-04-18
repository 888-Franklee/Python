import tkinter as tk

root = tk.Tk()
root.title("计数器")
root.geometry("300x200")

count = 0

label = tk.Label(root, text="计数值: 0")
label.pack()

def increase_count():
    global count
    count += 1
    label.config(text=f"计数值: {count}")

button = tk.Button(root, text="增加", command=increase_count)
button.pack()

root.mainloop()