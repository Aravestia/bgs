import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

target_minute = 0

def wait_until_target():
    while True:
        now = datetime.now()
        if now.minute == target_minute:
            show_popup()
            time.sleep(70)
        else:
            print(now)
            time.sleep(10)

def show_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("BGSI: Collect Chests", "Open BGSI in Roblox to collect your chests.")
    root.destroy()

wait_until_target()