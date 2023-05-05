#Food Analysis App Launcher
"""This Program is compiles all the tools required by Food Analysis App and Launches the Login Page"""

#Import all libraries required by the app here
from io import BytesIO
import time
import os
try :
    import requests
    from tkinter import *
    from PIL import Image, ImageTk
    import numpy as np
    import matplotlib.pyplot as plt
    import requests
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

#Install libraries if not found
except ImportError:
    os.system("pip install requests tkinter pillow numpy matplotlib gspread oauth2client") 

import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#Function to compile all other files
def call():
    exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/db.py").text)
    exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/visuals.py").text)
    exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/numeric.py").text)
    exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/window.py").text)
    load.destroy()
    login_window()

#Creating a Loading Popup to engage the user while compiling all other files
def load()
    load = Tk()
    message_label = Label(load, text="Loading, please wait...")
    message_label.pack(pady=10)
    progress_bar = ttk.Progressbar(load, length=300, mode='indeterminate')
    progress_bar.pack(pady=10)
    progress_bar.start()
    load.title("Loading")
    call()
    load.mainloop()
