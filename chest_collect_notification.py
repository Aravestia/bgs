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

    top = tk.Toplevel()
    top.attributes('-topmost', True)
    top.withdraw()
    top.after(0, lambda: top.focus_force())

    messagebox.showinfo("BGSI: Collect Chests", "Open BGSI in Roblox to collect your chests.")
    top.destroy()
    root.destroy()

wait_until_target()