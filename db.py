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
print("For your Reference")
col = {1:"ID",2:"Date",3:"Region",4:"City",5:"Category",6:"Product",7:"Quantity",8:"Unit",9:"Total"}
print(col)

def data(sheetname, colno=None, rowno=None, alldata=None, nums=False):
    if rowno == None and alldata == None and colno != None:
        data = sheetname.col_values(colno)
        data = data[1:]
        try :
            if type(float(data[0])) == float:
                data = [ float(x) for x in data]
        except ValueError:
            pass
        data.append(colno)
        
    elif rowno != None and alldata == None and colno == None:
        data = sheetname.row_values(rowno)
        
    elif rowno != None and alldata == None and colno != None:
        data = sheetname.cell(rowno, colno).value
        
    elif rowno == None and alldata != None and colno == None:
        data = sheetname.get_all_records()

    
    return data

def avg(datalist):
    return sum(datalist)/len(datalist)

def total(datalist):
    return sum(datalist)

def dt(keys, values):
    dt = {}
    for key in keys:
        dt[key] = 0
        for value in values:
            dt[key] += value
            values.remove(value)
            break
    return dt

def plot(*ls):
    xval = []
    yval = []
    fig = plt.figure(figsize = (10, 5))
    xp = ""
    yp = ""

    if len(ls) == 2:
            xval = ls[0]
            yval = ls[1]
            x = col[ls[0][-1]]
            y = col[ls[1][-1]]
            ls[0].remove(ls[0][-1])
            ls[1].remove(ls[1][-1])
            
            plt.bar(xval, yval, color ='blue',width = 0.4)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Industry Sales Analysis")
            plt.show()
            
    elif len(ls) == 3:
            yval = ls[2]
            y = col[ls[2][-1]]
            ls[2].remove(ls[2][-1])
            
            for i in ls[:1]:
                x = col[i[-1]]
                i.remove(i[-1])
                
                plt.bar(i, yval, color ='blue',width = 0.4, label = x)
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Industry Sales Analysis")
                plt.show()
#def pie(datalist, labels = None):
    
