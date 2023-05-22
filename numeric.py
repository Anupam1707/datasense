try:
    from PIL import Image, ImageTk
except ImportError:
    import os
    os.system("pip install pillow")
    
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

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

                    dt = {}
                    cityu = []
                    produ = []
                    mxp = ""
                    mx = 0
                    cities = data(sales, colno = col["city"])
                    products = data(sales, colno = col["product"])

                    for city in cities:
                        while city not in cityu:
                            cityu.append(city)
                    cityu.remove(cityu[-1])
                    cities = cityu
                    cityu = None

                    for product in products:
                        while product not in produ:
                            produ.append(product)
                    produ.remove(produ[-1])
                    products = produ
                    produ = None

                    ct = Frame(numeric, bg = "white")
                    wait = Label(ct, text = "Analyzing Data....\nWe appreciate your patience", font = "Arial 30 bold")
                    wait.pack(pady = 10)

                    for city in cities:
                        mx = 0
                        mxp = ""
                        dt = {}
                        dt[city] = []
                        
                        for product in products:
                            formula = f'=COUNTIFS(D2:D245, "{city}", F2:F245, "{product}")'
                            sales.update_cell(1, 10, formula)
                            result = int(sales.cell(1, 10).value)
                            dt[city].append([product, result])
                            print(city, product, type(result), result)
                        print(dt)
                        for value in dt[city]:
                            if value[1] >= mx:
                                    mx = value[1]
                                    mxp = value[0]
                        Label(numeric, text=f"Trending Product in {city} is {mxp}", font="Arial 30 bold").pack()
                            
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
