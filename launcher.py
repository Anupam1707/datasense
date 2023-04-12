#AI Assistant Launcher
"""This Program is compiles all the tools required by AI and Launches the AI Assistant"""

import os
try :
    import requests
except ImportError:
    os.system("pip install requests") 

import requests

exec(requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/tools.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/account.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/capabilities.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/main.py").text)
