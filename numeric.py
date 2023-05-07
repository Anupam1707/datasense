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
                l.pack_forget()
                c.pack_forget()
                ct.pack_forget()
                r.pack_forget()
                b.pack_forget()
                show_home()

            l = Label(numeric, text="Trending Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue")
            c.pack(pady=10)
            ct = Button(numeric, text="Country", font="Arial 20 bold", bg="skyblue")
            ct.pack(pady=10)
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
            ct = Button(numeric, text="Country", font="Arial 20 bold", bg="skyblue")
            ct.pack(pady=10)
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
            ct = Button(numeric, text="Country", font="Arial 20 bold", bg="skyblue")
            ct.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=unpop)
            b.pack(pady=10)
            
    response = requests.get("https://images.pexels.com/photos/7135121/pexels-photo-7135121.jpeg?cs=srgb&dl=pexels-codioful-%28formerly-gradienta%29-7135121.jpg")
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
