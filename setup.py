"""This file helps you to setup ypur app accoriding to your entries"""
import time
import os

try :
  from SecuriPy import *
except ImportError:
  os.system("pip install SecuriPy")

print("Welcome to the DataBase Analysis App")
time.sleep(2)
print("Let's start the setup")
time.sleep(1)

print("First of all add an editor in google sheets to this email:\ndatabase@database--387415.iam.gserviceaccount.com\nand confirm by typing yes")
chk = str(input())
if chk == "Yes" or chk == "yes" or chk == "y" or chk == "Y":
  SHEET_ID = str(input("Enter the link of Google Sheet : "))
  
SHEET_ID = SHEET_ID[39:]
SHEET_ID = encrypt(SHEET_ID, "database")
with open("data", "w") as d:
  d.write(f"SHEET : {SHEET_ID}")
  
