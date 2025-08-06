import tkinter as tk

root = tk.Tk()
root.title("计数器")
root.geometry("300x200")

count = 0

label = tk.Label(root, text="计数值: 0")
label.pack(pady=20)

def increase_count():
    global count
    count += 1
    label.config(text=f"计数值: {count}")

def decrease_count():
    global count
    count -= 1
    label.config(text=f"计数值: {count}")

button_frame = tk.Frame(root)
button_frame.pack()

increase_button = tk.Button(button_frame, text="增加", command=increase_count)
increase_button.pack(side=tk.LEFT, padx=10)

decrease_button = tk.Button(button_frame, text="减少", command=decrease_count)
decrease_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
