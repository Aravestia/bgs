import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

prev = datetime.now()
wait_time = 60 * 45

def wait_until_target():
    while True:
        global prev

        now = datetime.now()
        et = (now - prev).seconds
        
        if et >= wait_time:
            show_popup(now)

        print(et)
        time.sleep(10)

def show_popup(now):
    global prev
    prev = now
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