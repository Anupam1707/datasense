from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def fetch(l1val = None, l2val = None, l3val = None, t):
    if l1val != None and l2val != None and l3val == None and t == "bv":
        plotb(data(sales, col[l1val.lower()]), data(sales, col[l2val.lower()]), t = "bv")

def login_window():
    login = Tk()
    login.title("Login")
    login.geometry("300x150")

    username_label = Label(login, text="Username")
    username_label.pack()
    username_entry = Entry(login)
    username_entry.pack()

    password_label = Label(login, text="Password")
    password_label.pack()
    password_entry = Entry(login, show="*")
    password_entry.pack()

    def login_button():
        for i in range(len(rows)):
                if username_entry.get() == rows[i]["Username"]:
                        usr = i
                        break
                else:
                        usr = -1
        if password_entry.get() == rows[usr]["Password"]:
            login.destroy() 
            home_window()
        else:
            error_label = Label(login, text="Incorrect username or password", fg="red")
            error_label.pack()

    button = Button(login, text="Login", command=login_button)
    button.pack()

    login.mainloop()
def graph_window():
    l1val = None
    l2val = None
    l3val = None
    typ = ""
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

    graph.title("Food Sales Management")
    title = Label(graph, text= 'Food Sales Management', font= 'Arial 35 bold',bg='#7676EE').pack()
    l1 = Label(graph, text="Data List 1", font= "Arial 30", fg = "black").pack()
    l1inp = Entry(graph, textvariable= l1val, width = 24, font='Arial 26 bold').pack()
    l2 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack()
    l2inp = Entry(graph, textvariable= l2val, width = 24, font='Arial 26 bold').pack()
    l3 = Label(graph, text="Data List 3", font= "Arial 30", fg = "black").pack()
    l3inp = Entry(graph, textvariable= l3val, width = 24, font='Arial 26 bold').pack()
    l4 = Label(graph, text="Type of Graph", font= "Arial 30", fg = "black").pack()
    l4inp = Entry(graph, textvariable= typ, width = 24, font='Arial 26 bold').pack()
    Button(graph, text= "Plot", font = "Arial 20 bold", bg="skyblue", command=fetch(l1val, l2val, l3val, typ)).pack()
    
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=graph.destroy).pack(side = BOTTOM,anchor = "se")    
    graph.mainloop()
    
login_window()
