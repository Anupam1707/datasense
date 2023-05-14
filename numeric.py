from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
from PyFetch import *

exec(food("db.py"))
#exec(food("visuals.py"))

def numeric_window():
    numeric = Tk()
    numeric.title("Numeric Analysis")
    numeric.geometry("1280x720")

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

            def untrend():
                utrend()
                show_home()
                
            def utrend():
                l.pack_forget()
                c.pack_forget()
                r.pack_forget()
                b.pack_forget()

            def city():
                utrend()

##                cityu = []
##                cities = data(sales, colno = col["city"])
##
##                for i in cities:
##                    while i not in cityu:
##                        cityu.append(i)
##                cityu.remove(cityu[-1])
##                cities = cityu
##                cityu = None
                
                formula = "=COUNTIFS(D2:D245,D2,F2:F245,F2)"
                sales.update_cell(1, 10, formula)
                result = sales.cell(1, 10).value
                
                lb = Label(numeric, text=f"Trending Product in Boston is {result}", font="Arial 30 bold")
                
                lb.pack(pady = 10)
                
                back = Button(numeric, text = "Back", font = "Arial 20 bold", bg = "skyblue", command = trend_win)
                back.pack(pady = 10)

            l = Label(numeric, text="Trending Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue", command=city)
            c.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=untrend)
            b.pack(pady=10)


    def most_sold_win():
            empty_home()

            def unmost():
                l.pack_forget()
                c.pack_forget()
                ct.pack_forget()
                r.pack_forget()
                b.pack_forget()
                show_home()
            
            l = Label(numeric, text="Most Sold Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue")
            c.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=unmost)
            b.pack(pady=10)
            
    def pop_win():
            empty_home()

            def unpop():
                l.pack_forget()
                c.pack_forget()
                ct.pack_forget()
                r.pack_forget()
                b.pack_forget()
                show_home()
                
            l = Label(numeric, text="Popular Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue")
            c.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=unpop)
            b.pack(pady=10)
            
    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/numeric.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1280,720), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

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
