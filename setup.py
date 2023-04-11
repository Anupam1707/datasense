import os
try :
    import requests
except ImportError:
    os.system("pip install requests")

os.system("mkdir AssistantA")   

import requests

with open("AssistantA/ai.py","+w") as f:
    f.write((requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/main.py").text))
    f.close()
with open("AssistantA/tools.py","+w") as f:
    f.write((requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/tools.py").text))
    f.close()
with open("AssistantA/account.py","+w") as f:
    f.write((requests.get("https://raw.githubusercontent.com/Anupam1707/ai/main/account.py").text))
    f.close()
