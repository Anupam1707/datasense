from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def numeric_window():
    numeric = Tk()
    numeric.title("Numeric Analysis")
    numeric.geometry("1280x720")
    #numeric.config(bg  = "white"

    def switch():
        numeric.destroy()
        home_window()
    
    def trend_win():
        inner_frame = Frame(numeric)
        inner_frame.pack(pady = 10)

        def untrend():
            inner_frame.destroy()
            tren.pack()
    
            
        Button(inner_frame, text="City-Wise", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
        Button(inner_frame, text="Country-Wise", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
        Button(inner_frame, text="Region-Wise", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
        Button(inner_frame, text="Back", font="Arial 20 bold", bg="skyblue", command=untrend).pack(pady = 10)

    def trend():
        tren.pack_forget()
        trend_win()
        
    
##    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/bg.jpg")
##    img = Image.open(BytesIO(response.content))
##    img = img.resize((1280,720), Image.LANCZOS)
##    test = ImageTk.PhotoImage(img)
##    bk = Label(image=test)
##    bk.image = test
##    bk.place(x=0, y=0)

    Label(numeric, text='Numeric Analysis', font='Arial 35 bold', bg='#7676EE').pack(pady = 20)
    tren = Button(numeric, text="Trending", font="Arial 20 bold", bg="skyblue", command=trend)
    tren.pack(pady = 10)
    Button(numeric, text='Exit', font='Arial 20 bold', bg='red', command=numeric.destroy).pack(side = RIGHT, anchor = "se")
    Button(numeric, text='Home', font='Arial 20 bold', bg='red', command=switch).pack(side = LEFT, anchor = "sw")
    
    numeric.mainloop()
numeric_window()
