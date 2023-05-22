#DataBase Analyzer Launcher
"""This Program is compiles all the tools required by AI and Launches the AI Assistant"""

try:
    from PIL import Image, ImageTk
except ImportError:
    import os
    os.system("pip install pillow")
try :
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    import os
    os.system("pip install numpy matplotlib")
try :
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import SecuriPy
except ImportError:
    import os
    os.system("pip install gspread")
    os.system("pip install oath2client")
    os.system("pip install SecuriPy")
try:
  import requests
except ImportError:
  import os
  os.system("pip install requests")
  
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/db.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/visuals.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/numeric.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/window.py").text)
