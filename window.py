def pt():
    if l1v.get() != None and l2v.get() != None and typ.get() == "vertical bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bv")
    if l1v.get() != None and l2v.get() != None and typ.get() == "horizontal bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bh")

def home_window():
    home = Tk()
    home.title("Home Page")
    home.geometry("1280x720")
    home.configure(bg = "black")

    def switchg():
        home.destroy()
        graph_window()
    def switchn():
        home.destroy()
        graph_window()
    def logout():
        with open("acc.txt", "w+"):
            d = f.readlines()
        home.destroy()
        login_window()
        
    Label(home, text = "Food Sales Management", font = "Arial 40 bold", bg = "black", fg = "white").pack()
    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switchg).pack()
    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switchn).pack()
    Button(home, text = 'Exit', font = 'Arial 20 bold', bg='red', command=home.destroy).pack(side = BOTTOM,anchor = "se")
    Button(home, text = 'Log Out', font = 'Arial 20 bold', bg='red', command=logout).pack(side = BOTTOM,anchor = "sw")
    
    home.mainloop()
    
def login_window():
    lg = None
    usr = ""
    try:
        with open("acc.txt", "r") as a:
            d = a.readlines()
            if d:
                d[0] = d[0].split()
                if d[0][1] == "IN":
                    lg = True
                    usr = d[0][0]
    except FileNotFoundError:
        with open("acc.txt","w") as w:
            pass
    def switch():
        login.destroy()
        home_window()
    
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
            login.destroy() 
            home_window()
            with open("acc.txt","w") as w:
                w.write(f"{username_entry.get()} IN"
        else:
            error_label = Label(login, text="Incorrect username or password",font = "Arial 30", fg="red")
            error_label.pack()

    button = Button(login, text="Login", font = "Arial 30 bold", command=login_button).pack(side = TOP)
    Button(login, text = 'Exit', font = 'Arial 20 bold', bg='red', command=login.destroy).pack(side = BOTTOM,anchor = "se")
    if lg == True:
        con = Button(login, text= f"Continue as {usr}", font = "Arial 20 bold", bg="skyblue", command=switch).pack(pady = 30)

    login.mainloop()
    
def graph_window():
    global l1v
    global l2v
    global typ
    
    tps = ["horizontal bar graph", "vertical bar graph", "pie chart"]   
        
    graph = Tk()
    graph.geometry("1280x720")
    graph.resizable(False,False)
    
    def switch():
        graph.destroy()
        home_window()
        
    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/bg.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1280,720), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    l1v = StringVar()
    l1v.set("product")
    l2v = StringVar()
    l2v.set("total price")
    typ = StringVar()
    typ.set("horizontal bar graph")
    
    graph.title("Visual Analysis")
    title = Label(graph, text= 'Visual Analysis', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    l1 = Label(graph, text="Data List 1", font= "Arial 30", fg = "black").pack()
    l1inp = OptionMenu(graph, l1v, *col.keys()).pack(expand = True)
    l2 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack()
    l2inp = OptionMenu(graph, l2v, *col.keys()).pack(expand = True)
    l4 = Label(graph, text="Type of Graph", font= "Arial 30", fg = "black").pack()
    l4inp = OptionMenu(graph, typ, *tps).pack(expand = True)
    Button(graph, text= "Plot", font = "Arial 20 bold", bg="skyblue", command=pt).pack()
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=graph.destroy).pack(side = BOTTOM,anchor = "se")    
    Button(graph, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = BOTTOM,anchor = "sw")    
    graph.mainloop()
    
#progress_bar.stop()
#load.destroy()
login_window()
