from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import time

def pt():
    if l1v.get() != None and l2v.get() != None and l3v.get() == "" and typ.get() == "bv":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bv")
    if l1v.get() != None and l2v.get() != None and l3v.get() == "" and typ.get() == "bh":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bh")
    if l1v.get() != None and l2v.get() != None and l3v.get() != "" and typ.get() == "bv":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]),data(sales, col[l3v.get().lower()]), t = "bv")
    if l1v.get() != None and l2v.get() != None and l3v.get() != "" and typ.get() == "bh":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]),data(sales, col[l3v.get().lower()]), t = "bh")

def home_window():
    home = Tk()
    home.title("Home Page")
    home.attributes("1280x720")
    home.configure(bg = "black")

    def switch():
        home.destroy()
        graph_window()
        
    Label(home, text = "Food Sales Management", font = "Arial 40 bold", bg = "black", fg = "white").pack()
    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switch).pack()
    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switch).pack()
    
    home.mainloop()
    
def login_window():
    login = Tk()
    login.title("Login")
    login.attributes('-fullscreen', True)

    title = Label(login, text="Food Database Login", font = "Arial 40 bold",bg = "black", fg = "white").pack(pady = 50)
    username_label = Label(login, text="Username", font = "Arial 35 bold")
    username_label.pack(anchor="center")
    username_entry = Entry(login, font = "Arial 30 bold")
    username_entry.pack(side = TOP)

    password_label = Label(login, text="Password", font = "Arial 35 bold")
    password_label.pack(side = TOP)
    password_entry = Entry(login, show="*", font = "Arial 30 bold")
    password_entry.pack(side = TOP)

    def login_button():
        for i in range(len(rows)):
                if username_entry.get() == rows[i]["Username"]:
                        usr = i
                        break
                else:
                        usr = -1
        if password_entry.get() == rows[usr]["Password"]:
            welcome = Label(login, text=f"Welcome back {username_entry.get()}", font="Arial 30", fg = "blue").pack()
            log = Label(login, text="Logging You In...", font="Arial 30", fg = "blue").pack()
            time.sleep(2)
            login.destroy() 
            home_window()
        else:
            error_label = Label(login, text="Incorrect username or password",font = "Arial 30", fg="red")
            error_label.pack()

    button = Button(login, text="Login", font = "Arial 30 bold", command=login_button)
    Button(login, text = 'Exit', font = 'Arial 20 bold', bg='red', command=login.destroy).pack(side = BOTTOM,anchor = "se")    
    button.pack(side = TOP)

    login.mainloop()
    
def graph_window():
    global l1v
    global l2v
    global l3v
    global typ

    graph = Tk()
    graph.geometry("1280x720")
    graph.resizable(False,False)

    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/bg.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1280,720), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    l1v = StringVar()
    l2v = StringVar()
    l3v = StringVar()
    typ = StringVar()
    
    graph.title("Food Sales Management")
    title = Label(graph, text= 'Food Sales Management', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    l1 = Label(graph, text="Data List 1", font= "Arial 30", fg = "black").pack()
    l1inp = Entry(graph, textvariable= l1v, width = 24, font='Arial 26 bold').pack()
    l2 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack()
    l2inp = Entry(graph, textvariable= l2v, width = 24, font='Arial 26 bold').pack()
    l3 = Label(graph, text="Data List 3", font= "Arial 30", fg = "black").pack()
    l3inp = Entry(graph, textvariable= l3v, width = 24, font='Arial 26 bold').pack()
    l4 = Label(graph, text="Type of Graph", font= "Arial 30", fg = "black").pack()
    l4inp = Entry(graph, textvariable= typ, width = 24, font='Arial 26 bold').pack()
    Button(graph, text= "Plot", font = "Arial 20 bold", bg="skyblue", command=pt).pack()
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=graph.destroy).pack(side = BOTTOM,anchor = "se")    
    Button(graph, text = 'Home', font = 'Arial 20 bold', bg='red', command=home_window).pack(side = BOTTOM,anchor = "se")    
    graph.mainloop()
    
login_window()
