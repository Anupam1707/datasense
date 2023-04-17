from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

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
            graph_window()
        else:
            error_label = Label(login, text="Incorrect username or password", fg="red")
            error_label.pack()

    button = Button(login, text="Login", command=login_button)
    button.pack()

    login.mainloop()
def graph_window():
    l1val = l2val = l3val = ""
    graph = Tk()
    graph.geometry("1280x720")
    graph.resizable(False,False)

    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/graph/bg.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1280,720), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    graph.title("Food Sales Management")
    title = Label(graph, text= 'Food Sales Management', font= 'Arial 35 bold',bg='#7676EE').pack()
    l1 = Label(graph, text="Data List 1", font= "Arial 30", fg = "black").place(y = 50)
    l1inp = Entry(graph, textvariable= l1val, width = 24, font='Arial 26 bold').place(y = 100)
    l2 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack(pady = 0)
    l2inp = Entry(graph, textvariable= l2val, width = 24, font='Arial 26 bold').pack(pady= 0)
    l3 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack(pady=0)
    l3inp = Entry(graph, textvariable= l3val, width = 24, font='Arial 26 bold').pack(pady=0)
    
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=graph.destroy).pack(side = BOTTOM,anchor = "se")
    
    
        
    graph.graphloop()
    
login_window()
