"""This file helps you to setup ypur app accoriding to your entries"""
import time

print("Welcome to the DataBase Analysis App")
time.sleep(2)
print("Let's start the setup")
time.sleep(1)

print("First of all add an editor in google sheets to this email:\ndatabase@database--387415.iam.gserviceaccount.com\nand confirm by typing yes")
chk = str(input())
SHEET_ID = str(input("Enter the link of Google Sheet : "))
