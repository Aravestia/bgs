import time
from datetime import datetime
import pygetwindow as gw

prev = datetime.now()
wait_time = 60 * 45

WINDOW_TITLE = r'C:\WINDOWS\system32\cmd.exe'

def wait_until_target():
    while True:
        global prev

        now = datetime.now()
        et = (now - prev).seconds
        
        if et >= wait_time:
            notify(now)

        print(et)
        time.sleep(10)

def notify(now):
    global prev
    prev = now

    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    
    if windows:
        win = windows[0]
        if win.isMinimized:
            win.restore()
        win.activate()
        print("Open BGSI in Roblox to collect your chests.")
    else:
        print("Window does not exist.")

wait_until_target()