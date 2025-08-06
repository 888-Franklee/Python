import tkinter as tk  
from tkinter import ttk  
  
class ColorSelector(tk.Tk):  
    def __init__(self):  
        super().__init__()  
        self.title("Color Selector")  
        self.geometry("400x300")  
  
        self.color_label = tk.Label(self, width=20, height=10, bg="white")  
        self.color_label.pack(pady=10)  
  
        self.color_listbox = tk.Listbox(self, selectmode=tk.SINGLE)  
        self.color_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  
  
        colors = ["black", "white", "red", "green", "blue", "yellow", "cyan", "magenta"]  
        for color in colors:  
            self.color_listbox.insert(tk.END, color)  
  
        self.color_listbox.bind("<<ListboxSelect>>", self.on_color_selected)  
   
        self.rgb_frame = ttk.Frame(self)  
        self.rgb_frame.pack(side=tk.RIGHT, fill=tk.Y)  
  
        self.create_rgb_sliders()  
  
    def create_rgb_sliders(self):  
        self.rgb_vars = [tk.IntVar(value=128) for _ in range(3)]  # 初始化RGB值为128（灰色）  
  
        for i, (label_text, var) in enumerate(zip(["R", "G", "B"], self.rgb_vars)):  
            label = ttk.Label(self.rgb_frame, text=label_text)  
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")  
  
            slider = ttk.Scale(self.rgb_frame, from_=0, to=255, orient=tk.VERTICAL, variable=var, command=self.update_color)  
            slider.grid(row=i, column=1, padx=5, pady=5, sticky="ns")  
  
    def on_color_selected(self, event):  
        selected_color = self.color_listbox.get(tk.ACTIVE)  
        self.color_label.config(bg=selected_color)  
  
    def update_color(self, _):   
        r, g, b = [var.get() for var in self.rgb_vars]  
        color = f"#{r:02x}{g:02x}{b:02x}"  
        self.color_label.config(bg=color)  
  
if __name__ == "__main__":  
    app = ColorSelector()  
    app.mainloop()












































































