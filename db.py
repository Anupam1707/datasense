import numpy as np
import matplotlib.pyplot as plt
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
url = 'https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/credentials.json'
page = requests.get(url)
with open("credentials.json","+w") as f:
          f.write(page.text)
          f.close()
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
SHEET_ID = '1bfWtrQHfo4Il-wWeIJ_qPJUf8ccZFsjLhdPSuCHlRdA'
try:
    spreadsheet = gc.open_by_key(SHEET_ID)
    
except gspread.exceptions.APIError or ConnectionError as e:
    print("Error: Could not connect to the database. Reason:", e)

spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet("Accounts")
rows = worksheet.get_all_records()

sales = spreadsheet.worksheet("Sales")

os.remove("credentials.json")
col = {"id":1, "date":2, "region":3,"city":4,"category":5,"product":6,"quantity":7,"unit price":8,"total price":9}
