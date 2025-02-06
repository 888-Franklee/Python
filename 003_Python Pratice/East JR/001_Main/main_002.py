import tkinter as tk
from tkinter import ttk, messagebox
import requests


API_KEY = "あなたのAPIキー"  
LINE_ENDPOINT = "http://api.ekispert.jp/v1/json/operationLine"
STATION_ENDPOINT = "http://api.ekispert.jp/v1/json/station"

def check_api_key():
    if API_KEY == "あなたのAPIキー" or not API_KEY:
        messagebox.showerror("エラー", "APIキーが設定されていません。APIキーを入力してください。")
        return False
    return True

def get_lines():
    if not check_api_key():
        return []
    
    params = {
        "key": API_KEY,
    }
    try:
        response = requests.get(LINE_ENDPOINT, params=params)
        response.raise_for_status()  
        data = response.json()
        return data.get('ResultSet', {}).get('Line', [])
    except requests.exceptions.RequestException as e:
        messagebox.showerror("エラー", f"路線情報の取得に失敗しました。\n{e}")
        return []

def get_stations(line_name):
    if not check_api_key():
        return []
    
    params = {
        "key": API_KEY,
        "name": line_name
    }
    try:
        response = requests.get(STATION_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('ResultSet', {}).get('Point', [])
    except requests.exceptions.RequestException as e:
        messagebox.showerror("エラー", f"駅情報の取得に失敗しました。\n{e}")
        return []

def on_line_selected(event):
    selection = line_listbox.curselection()
    if not selection:  
        return
    selected_line = line_listbox.get(selection)
    stations = get_stations(selected_line)
    station_listbox.delete(0, tk.END)  
    for station in stations:
        station_name = station['Station']['Name']
        station_listbox.insert(tk.END, station_name)


root = tk.Tk()
root.title("JR東日本 路線・駅情報")

frame_lines = tk.Frame(root)
frame_lines.pack(side=tk.LEFT, padx=10, pady=10)

line_label = tk.Label(frame_lines, text="JR東日本 路線一覧", font=("Helvetica", 16))
line_label.pack(pady=10)

line_listbox = tk.Listbox(frame_lines, height=20, width=40)
line_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

line_scrollbar = tk.Scrollbar(frame_lines)
line_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
line_listbox.config(yscrollcommand=line_scrollbar.set)
line_scrollbar.config(command=line_listbox.yview)

frame_stations = tk.Frame(root)
frame_stations.pack(side=tk.RIGHT, padx=10, pady=10)

station_label = tk.Label(frame_stations, text="駅一覧", font=("Helvetica", 16))
station_label.pack(pady=10)

station_listbox = tk.Listbox(frame_stations, height=20, width=40)
station_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

station_scrollbar = tk.Scrollbar(frame_stations)
station_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
station_listbox.config(yscrollcommand=station_scrollbar.set)
station_scrollbar.config(command=station_listbox.yview)

line_listbox.bind('<<ListboxSelect>>', on_line_selected)

lines = get_lines()
for line in lines:
    line_name = line['Name']
    line_listbox.insert(tk.END, line_name)

root.mainloop()
