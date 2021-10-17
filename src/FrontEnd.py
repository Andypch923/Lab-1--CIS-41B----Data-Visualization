import myParser
import temperature
import tkinter as tk
from tkinter import filedialog, Text
import os
'''
parse raw data from html file and create container to store Temperature data
'''

'''
rawParsedTemp = myParser.myParser("Temperature.html")
tempObj = temperature.temperature(rawParsedTemp.getRawData())
'''

root = tk.Tk()
apps = []

canvas = tk.Canvas(root, height="1080", width = "1900", bg = "white")
canvas.pack()

frame = tk.Frame(canvas, bg= "#009900")
frame.place(relheight = 0.93, relwidth = 0.95, relx=0.025,rely=0.03)
frame.pack()

root.mainloop()