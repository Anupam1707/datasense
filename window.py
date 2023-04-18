from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
l1v = ""
l2v = ""
l3v = ""
typ = ""
def fetch():
    if l1v.get() != None and l2v.get() != None and l3v.get() == "" and typ.get() == "bv":
        plotb(data(sales, col[l1v.lower()]), data(sales, col[l2v.lower()]), t = "bv")

def login_window():
    login = Tk()
    login.title("Login")
    login.configure(bg = "black")
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
            login.destroy() 
            graph_window()
        else:
            error_label = Label(login, text="Incorrect username or password",font = "Arial 30", fg="red")
            error_label.pack()

    button = Button(login, text="Login", font = "Arial 30 bold", command=login_button)
    Button(login, text = 'Exit', font = 'Arial 20 bold', bg='red', command=login.destroy).pack(side = BOTTOM,anchor = "se")    
    button.pack(side = TOP)

    login.mainloop()
def graph_window():
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
    title = Label(graph, text= 'Food Sales Management', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    l1 = Label(graph, text="Data List 1", font= "Arial 30", fg = "black").pack()
    l1inp = Entry(graph, textvariable= l1v, width = 24, font='Arial 26 bold').pack()
    l2 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack()
    l2inp = Entry(graph, textvariable= l2v, width = 24, font='Arial 26 bold').pack()
    l3 = Label(graph, text="Data List 3", font= "Arial 30", fg = "black").pack()
    l3inp = Entry(graph, textvariable= l3v, width = 24, font='Arial 26 bold').pack()
    l4 = Label(graph, text="Type of Graph", font= "Arial 30", fg = "black").pack()
    l4inp = Entry(graph, textvariable= typ, width = 24, font='Arial 26 bold').pack()
    Button(graph, text= "Plot", font = "Arial 20 bold", bg="skyblue", command=fetch).pack()
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=graph.destroy).pack(side = BOTTOM,anchor = "se")    
    graph.mainloop()
    
login_window()
