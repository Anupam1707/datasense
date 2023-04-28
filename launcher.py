#AI Assistant Launcher
"""This Program is compiles all the tools required by AI and Launches the AI Assistant"""

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

except ImportError:
    os.system("pip install requests tkinter pillow numpy matplotlib gspread oauth2client") 

import requests
from tkinter import *
from PIL import Image, ImageTk

exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/db.py?token=GHSAT0AAAAAAB5RTXXBNPTR4LYH4TAZZA2AZCLR2UQ").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/visuals.py?token=GHSAT0AAAAAAB5RTXXBNPTR4LYH4TAZZA2AZCLR2UQ").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/window.py?token=GHSAT0AAAAAAB5RTXXBNPTR4LYH4TAZZA2AZCLR2UQ").text)
