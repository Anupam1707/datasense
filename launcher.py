#AI Assistant Launcher
"""This Program is compiles all the tools required by AI and Launches the AI Assistant"""

import requests

exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/db.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/visuals.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/numeric.py").text)
exec(requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/window.py").text)
