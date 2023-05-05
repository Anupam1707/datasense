"""This program is the Numeric Analysis Program"""

from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Declare global variables
citytren = None
countrytren = None
regiontren = None
backtren = None

#Function to create and manage the Numeric Analysis Window
def numeric_window():
    global citytren, countrytren, regiontren, backtren  # Using global keyword to access global variables
    numeric = Tk()
    numeric.title("Numeric Analysis")
    numeric.geometry("1280x720")
    
    #Function to Switch between windows
    def switch():
        numeric.destroy()
        home_window()
    
    def trend():
        tren.pack_forget()
        
        citytren.pack()
        countrytren.pack()
        regiontren.pack()
        backtren.pack()
        
    def untrend():
        tren.pack()
        
        citytren.pack_forget()
        countrytren.pack_forget()
        regiontren.pack_forget()
        backtren.pack_forget()

    citytren = Button(numeric, text= "City-Wise", font = "Arial 20 bold", bg="skyblue", command=trend)
    countrytren = Button(numeric, text= "Country-Wise", font = "Arial 20 bold", bg="skyblue", command=trend)
    regiontren = Button(numeric, text= "Region-Wise", font = "Arial 20 bold", bg="skyblue", command=trend)
    backtren = Button(numeric, text= "Back", font = "Arial 20 bold", bg="skyblue", command=untrend)
    
    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/bg.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1280,720), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    
    Label(numeric, text= 'Numeric Analysis', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    tren = Button(numeric, text= "Trending", font = "Arial 20 bold", bg="skyblue", command=trend)
    Button(numeric, text = 'Exit', font = 'Arial 20 bold', bg='red', command=numeric.destroy).pack(side = BOTTOM,anchor = "se")    
    Button(numeric, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = BOTTOM,anchor = "sw")
    tren.pack()
    
    numeric.mainloop()
