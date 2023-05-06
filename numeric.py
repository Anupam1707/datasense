from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def numeric_window():
    numeric = Tk()
    numeric.title("Numeric Analysis")
    numeric.geometry("1280x720")
    numeric.config(bg = "black")

    def empty_home():
        tren.pack_forget()
        pop.pack_forget()
        most.pack_forget()

    def show_home():
        tren.pack(pady = 10)
        pop.pack(pady = 10)
        most.pack(pady = 10)
        
    def switchh():
        numeric.destroy()
        home_window()
    
    def trend_win():
            empty_home()
            trend_frame = Frame(numeric)
            trend_frame.pack(pady = 10)

            def untrend():
                trend_frame.destroy()
                show_home()
                
            Label(trend_frame, text="Trending Product on Basis of :", font = "Arial 30 bold").pack(pady = 10)
            Button(trend_frame, text="City", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(trend_frame, text="Country", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(trend_frame, text="Region", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(trend_frame, text="Back", font="Arial 20 bold", bg="skyblue", command=untrend).pack(pady = 10)

    def most_sold_win():
            empty_home()
            most_sold_frame = Frame(numeric)
            most_sold_frame.pack(pady = 10)

            def unmost():
                most_sold_frame.destroy()
                show_home()

            Label(most_sold_frame, text="Most Sold Products in :", font = "Arial 30 bold").pack(pady = 10)
            Button(most_sold_frame, text="City", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(most_sold_frame, text="Country", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(most_sold_frame, text="Region", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(most_sold_frame, text="Back", font="Arial 20 bold", bg="skyblue", command=unmost).pack(pady = 10)


    def pop_win():
            empty_home()
            pop_frame = Frame(numeric)
            pop_frame.pack(pady = 10)

            def unpop():
                pop_frame.destroy()
                show_home()
                
            Label(pop_frame, text="Popular Product on Basis of :", font = "Arial 30 bold").pack(pady = 10)
            Button(pop_frame, text="City", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(pop_frame, text="Country", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(pop_frame, text="Region", font="Arial 20 bold", bg="skyblue").pack(pady = 10)
            Button(pop_frame, text="Back", font="Arial 20 bold", bg="skyblue", command=unpop).pack(pady = 10)
        
##    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/bg.jpg")
##    img = Image.open(BytesIO(response.content))
##    img = img.resize((1280,720), Image.LANCZOS)
##    test = ImageTk.PhotoImage(img)
##    bk = Label(image=test)
##    bk.image = test
##    bk.place(x=0, y=0)

    Label(numeric, text='Numeric Analysis', font='Arial 35 bold', bg='#7676EE').pack(pady = 20)
    tren = Button(numeric, text="Trending", font="Arial 20 bold", bg="skyblue", command=trend_win)
    tren.pack(pady = 10)
    pop  = Button(numeric, text="Popular", font="Arial 20 bold", bg="skyblue", command=pop_win)
    pop.pack(pady = 10)
    most  = Button(numeric, text="Most Sold", font="Arial 20 bold", bg="skyblue", command=most_sold_win)
    most.pack(pady = 10)
    Button(numeric, text='Exit', font='Arial 20 bold', bg='red', command=numeric.destroy).pack(side = RIGHT, anchor = "se")
    Button(numeric, text='Home', font='Arial 20 bold', bg='red', command=switchh).pack(side = LEFT, anchor = "sw")
    
    numeric.mainloop()