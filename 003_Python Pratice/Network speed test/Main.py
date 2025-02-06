import tkinter as tk
from tkinter import messagebox
import speedtest

app = tk.Tk()
app.title("网络速度测试")
app.geometry("300x200")

def check_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        download_speed = st.download() / 1_000_000  
        upload_speed = st.upload() / 1_000_000  
        ping = st.results.ping

        download_label.config(text=f"下载速度: {download_speed:.2f} Mbps")
        upload_label.config(text=f"上传速度: {upload_speed:.2f} Mbps")
        ping_label.config(text=f"Ping: {ping:.2f} ms")

    except Exception as e:
        messagebox.showerror("错误", f"测试失败: {e}")

title_label = tk.Label(app, text="网速测试", font=("Arial", 16))
title_label.pack(pady=10)

download_label = tk.Label(app, text="下载速度: - Mbps")
download_label.pack(pady=5)

upload_label = tk.Label(app, text="上传速度: - Mbps")
upload_label.pack(pady=5)

ping_label = tk.Label(app, text="Ping: - ms")
ping_label.pack(pady=5)

test_button = tk.Button(app, text="开始测试", command=check_speed)
test_button.pack(pady=10)

app.mainloop()
