# Developed by Amresh Ranjan.

import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('ScreenShot Taker')
canvas1 = tk.Canvas(root, width=300, height=300, bg = "green")
canvas1.pack()

def myScreenshot():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension = '.png')
    myScreenshot.save(file_path)

myButton = tk.Button(text='Take Screenshot Now!', command=myScreenshot, bg='red', fg='white', font=15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
