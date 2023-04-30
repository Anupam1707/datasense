import requests
import os

url = "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/"

urls = ["db.py",
        "visuals.py",
        "window.py",
        "launcher.py"]

sum = 0

d = []

for i in urls:
    d = (requests.get(url + i)).text
    with open("len.txt","w", newline = "") as f:
        f.write(d)
    with open("len.txt","r") as f:
        sum += len(f.readlines())

os.remove("len.txt")
print(sum)
