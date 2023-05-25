#DataBase Analyzer Launcher
"""This Program is compiles all the tools required by AI and Launches the AI Assistant"""
import os

modules = [
    ("import requests", "pip install requests"),
    ("from PIL import Image, ImageTk, ImageDraw", "pip install pillow"),
    ("import numpy as np", "pip install numpy"),
    ("import matplotlib.pyplot as plt", "pip install matplotlib"),
    ("import gspread", "pip install gspread"),
    ("from oauth2client.service_account import ServiceAccountCredentials", "pip install oath2client"),
    ("import SecuriPy", "pip install SecuriPy"),
    ("from fetchify import sense", "pip install fetchify")
]

for module, code in modules:
    try:
        exec(module)
    except ImportError:
        exec(code)
  
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/datasense/main/db.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/datasense/main/visuals.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/datasense/main/numeric.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/datasense/main/window.py").text)
