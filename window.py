"""This is the backbone of the App. This program creates a link between the front end and the back-end."""

#Function to give values of the input to the graph plotter to plot the graph
def pt():
    if l1v.get() != None and l2v.get() != None and typ.get() == "vertical bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bv")
    if l1v.get() != None and l2v.get() != None and typ.get() == "horizontal bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bh")

#Function to create a Home Page
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
        numeric_window()
    def logout():
        with open("acc.txt", "w"):
            pass
        home.destroy()
        login_window()
        
    Label(home, text = "Food Sales Management", font = "Arial 40 bold", bg = "black", fg = "white").pack()
    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switchg).pack(pady=20)
    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switchn).pack(pady=20)
    Button(home, text = "Help", font = "Arial 20 bold",bg = "white", command=switchn).pack(pady=20)
    Button(home, text = 'Exit', font = 'Arial 20 bold', bg='red', command=home.destroy).pack(side = RIGHT,anchor = "se")
    Button(home, text = 'Log Out', font = 'Arial 20 bold', bg='red', command=logout).pack(side = LEFT,anchor = "sw")
    
    home.mainloop()
    
#Function to create a Signup Page
def signup_window():
    usr = len(rows)+2
    try:
        with open("acc.txt", "r") as a:
            d = a.readlines()
    except FileNotFoundError:
        with open("acc.txt","w") as w:
            pass
    
    signup = Tk()
    signup.title("Login")
    signup.attributes('-fullscreen', True)

    def switchlog():
        signup.destroy()
        login_window()
    
    title = Label(signup, text="Food Database SignUP", font = "Arial 40 bold",bg = "black", fg = "white").pack(pady = 50)
    username_label = Label(signup, text="Username", font = "Arial 35 bold")
    username_label.pack(anchor="center")
    username_entry = Entry(signup, font = "Arial 30 bold")
    username_entry.pack(side = TOP)

    password_label = Label(signup, text="Password", font = "Arial 35 bold")
    password_label.pack(side = TOP)
    password_entry = Entry(signup, show="*", font = "Arial 30 bold")
    password_entry.pack(side = TOP)
           
    def signup_button():
        worksheet.update_cell(usr,1,username_entry.get())
        worksheet.update_cell(usr,2,password_entry.get()) 
        worksheet.update_cell(usr,3,"IN")
        worksheet.update_cell(usr,4,"Researcher")
        
        with open("acc.txt","w") as w:
                w.write(f"{username_entry.get()} IN")
               
        signup.destroy()
        home_window()
        
    button = Button(signup, text="SignUP", font = "Arial 30 bold", command=signup_button).pack(side = TOP)
    Button(signup, text = 'Exit', font = 'Arial 20 bold', bg='red', command=signup.destroy).pack(side = RIGHT,anchor = "se")
    Button(signup, text = 'Go Back', font = 'Arial 20 bold', bg='red', command=switchlog).pack(side = LEFT,anchor = "sw")
    signup.mainloop()
 
#Function to create a Login Page
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
    
    def switchs():
        login.destroy()
        signup_window()
    
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
            user = username_entry.get()
            welcome = Label(login, text=f"Welcome back {username_entry.get()}", font="Arial 30", fg = "blue").pack()
            login.destroy() 
            home_window()
            with open("acc.txt","w") as w:
                w.write(f"{user} IN")
        else:
            error_label = Label(login, text="Incorrect username or password",font = "Arial 30", fg="red")
            error_label.pack()

    button = Button(login, text="Login", font = "Arial 30 bold", command=login_button).pack(side = TOP)
    Button(login, text = 'Exit', font = 'Arial 20 bold', bg='red', command=login.destroy).pack(side = BOTTOM,anchor = "se")
    if lg == True:
        con = Button(login, text= f"Continue as {usr}", font = "Arial 20 bold", bg="skyblue", command=switch).pack(pady = 30)
    sign = Button(login, text= "Sign UP Instead", font = "Arial 20 bold", bg="skyblue", command=switchs).pack(pady = 30)
    login.mainloop()
    
#Function to create a Visual Analysis Page
def graph_window():
    global l1v
    global l2v
    global typ
    
    tps = ["horizontal bar graph", "vertical bar graph", "pie chart"]   
        
    graph = Tk()
    graph.geometry("1280x720")
    graph.resizable(False,False)
    graph.config(bg="black")
    
    def switch():
        graph.destroy()
        home_window()
        

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
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=graph.destroy).pack(side = RIGHT,anchor = "se")    
    Button(graph, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")    
    graph.mainloop()
login_window()
