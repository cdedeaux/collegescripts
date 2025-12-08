import pyautogui
import time
import threading
from tkinter import *
from tkinter import ttk
clicking = False
def start_clicking():
    global clicking
    while clicking:
        delay = 0.1  # seconds between clicks
        pyautogui.click() # Default is left click
        time.sleep(0.1)  # Adjust the delay as needed
    
def on_start():
    global clicking
    if clicking:
        return
    clicking = True
    t = threading.Thread(target=start_clicking)
    t.daemon = True
    t.start()
def on_stop(event=None):
    global clicking
    clicking = False

root = Tk()
root.title("Auto Clicker")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Label(mainframe, text="Auto Clicker").grid(column=1, row=1, columnspan=3)
root.bind("<Control-q>", on_stop)
root.bind("<Command-q>", on_stop) # For MacOS

root.bind("<Control-s>", on_start)
root.bind("<Command-s>", on_start) # For MacOS

ttk.Button(mainframe, text="Start", command=on_start).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Stop", command=on_stop).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Quit", command=root.quit).grid(column=3, row=3, sticky=W)
root.mainloop()