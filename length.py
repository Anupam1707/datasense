import requests
import os

url = "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/"

urls = ["db.py?token=GHSAT0AAAAAAB5RTXXBDRCBXDOV42UX5ZRKZCLSYRA",
        "visuals.py?token=GHSAT0AAAAAAB5RTXXBLAXTAT6S2FLGPAEEZCLSZHQ",
        "window.py?token=GHSAT0AAAAAAB5RTXXBSHIC55QXOI6BYSBOZCLSZVA",
        "launcher.py?token=GHSAT0AAAAAAB5RTXXALO23IQI2N6OF4LBYZCLS2MA"]

sum = 0

d = []

for i in urls:
    d = (requests.get(url + i)).text
    with open("len.txt","w", newline = "") as f:
        f.write(d)
    with open("len.txt","r") as f:
        sum += len(f.readlines())

os.remove("len.txt")
