import myParser
import temperature
import tkinter as tk
from tkinter import Canvas, filedialog, Text
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

canvas = tk.Canvas(root, height = 700, width = 700, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight =0.8,relx = 0.1, rely=0.1)



root.mainloop()