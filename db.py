import numpy as np
import matplotlib.pyplot as plt
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
url = 'https://raw.githubusercontent.com/Anupam1707/ai/main/credentials.json'
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

def data(sheetname, colno=None, rowno=None, alldata=None, nums=False):
    if rowno == None and alldata == None and colno != None:
        data = sheetname.col_values(colno)
        data = data[1:]
        try :
            if type(float(data[0])) == float:
                data = [ float(x) for x in data]
        except ValueError:
            pass
            
        
    elif rowno != None and alldata == None and colno == None:
        data = sheetname.row_values(rowno)
        
    elif rowno != None and alldata == None and colno != None:
        data = sheetname.cell(rowno, colno).value
        
    elif rowno == None and alldata != None and colno == None:
        data = sheetname.get_all_records()

    
    return data
#constants
id = 1
date = 2
region = 3
city = 4
category = 5
product = 6
quantity = 7
unitprice = 8
totalprice = 9

def avg(datalist):
    return sum(datalist)/len(datalist)

def total(datalist):
    return sum(datalist)

def dt(keys, values):
    dt = {}
    for key in keys:
        for value in values:
            dt[key] += value
            values.remove(value)
            break
    return dt

def plot(datadict):
    paras = list(datadict.keys())
    values = list(datadict.values())  
    fig = plt.figure(figsize = (10, 5))
    plt.bar(paras, values, color ='maroon',width = 0.4)
    plt.xlabel("Parameters")
    plt.ylabel("Values")
    plt.title("Industry Sales")
    plt.show()
