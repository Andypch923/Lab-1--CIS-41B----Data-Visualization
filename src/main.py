import myParser
import temperature
import tkinter as tk
from tkinter import filedialog, Text
import os

'''parse raw data from html file'''
rawParsedTemp = myParser.myParser("Temperature.html")
'''create containers to store processed raw data for temperature file'''
tempObj = temperature.temperature(rawParsedTemp.getRawData())
