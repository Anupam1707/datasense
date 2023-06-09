"""This is the backbone of the App. This program creates a link between the front end and the back-end."""
import SecuriPy
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
from fetchify import fetch

#Function to give values of the input to the graph plotter to plot the graph
def pt():
    if l1v.get() != None and l2v.get() != None and typ.get() == "vertical bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bv")
    if l1v.get() != None and l2v.get() != None and typ.get() == "horizontal bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bh")

#Function to create a Home Page
def home_window():
    home = Tk()
    
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2

    home.title("Data Sense")
    home.attributes("-fullscreen",True)
    home.overrideredirect(True)

    img = Image.open(BytesIO(fetch("home.jpg", "ds", image = True)))
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x = -2, y = -2)
    
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            home.destroy()
    
    def switchg():
        home.destroy()
        graph_window()
    def switchn():
        home.destroy()
        numeric_window()
    def switche():
        home.destroy()
        export_window()
    def logout():
        with open("acc.tiak", "w"):
            pass
        home.destroy()
        login_window()
        
    Label(home, text = "Welcome to Data Sense", font = "Arial 40 bold", bg = "black", fg = "white").pack()
    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switchg).pack(pady=20)
    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switchn).pack(pady=20)
    Button(home, text = "Export Reports", font = "Arial 20 bold", bg = "white", command=switche).pack(pady=20)
    Button(home, text = "Help", font = "Arial 20 bold",bg = "white", command=switchn).pack(pady=20)
    Button(home, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")
    Button(home, text = 'Log Out', font = 'Arial 20 bold', bg='red', command=logout).pack(side = LEFT,anchor = "sw")
    
    home.mainloop()
    
#Function to create a Signup Page
def signup_window():
    usr = len(rows)+2
    try:
        with open("acc.tiak", "r", encoding = "utf-8") as a:
            d = a.readlines()
    except FileNotFoundError:
        with open("acc.tiak","w") as w:
            pass
    
    signup = Tk()
    signup.title("Login")
    signup.attributes('-fullscreen', True)

    def switchlog():
        signup.destroy()
        login_window()
    
    title = Label(signup, text="Data Sense Signup", font = "Arial 40 bold",bg = "black", fg = "white").pack(pady = 50)
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
        usr = SecuriPy.Text.encrypt(username_entry.get(), "datasense")
        with open("acc.tiak","w", encoding = "utf-8") as w:
                w.write(f"{usr}")
               
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
        with open("acc.tiak", "r", encoding = "utf-8") as a:
            d = a.readlines()
            if d:
                lg = True
                usr = SecuriPy.Text.decrypt(f"{d[0]}", "datasense")
                
    except FileNotFoundError:
        with open("acc.tiak","w") as w:
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

    title = Label(login, text="Data Sense Login", font = "Arial 40 bold",bg = "black", fg = "white").pack(pady = 50)
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
            with open("acc.tiak","w", encoding = "utf-8") as w:
                user = SecuriPy.Text.encrypt(user, 'datasense')
                w.write(user)
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
    
    screen_width = graph.winfo_screenwidth()
    screen_height = graph.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2

    graph.title("Numeric Analysis")
    graph.attributes("-fullscreen",True)
    graph.overrideredirect(True)
    
    img = Image.open(BytesIO(fetch("visual.jpg", "ds", image = True)))
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)
    
    def switch():
        graph.destroy()
        home_window()
    
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            graph.destroy()
      
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
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")    
    Button(graph, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")    
    graph.mainloop()

def export_window():
    export  = Tk()
    rows = IntVar()
    rowe = IntVar()
    cols = IntVar()
    cole = IntVar()
    screen_width = export.winfo_screenwidth()
    screen_height = export.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2
##    
    export.attributes("-fullscreen",True)
    export.overrideredirect(True)
    export.title("Data Export")
    
    img = Image.open(BytesIO(fetch("export.jpg", "ds", image = True)))
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)
    
    title = Label(export, text= 'Data Export', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            export.destroy()
    
    def switch():
        export.destroy()
        home_window()

    def switchg():
        export.destroy()
        graph_window()
        
    def returnn():
        n.pack(pady = 10)
        v.pack(pady = 10)
    
    def num():
        n.pack_forget()
        v.pack_forget()

        def switchh():
            export.destroy()
            export_window()
            
        def concsv():
           dt = data(sales, alldata = True)
           selected_rows = dt[(rows.get()-1):rowe.get()]
           selected_columns = [row[(cols.get()-1):(cole.get()+1)] for row in selected_rows]
           df = pd.DataFrame(selected_columns)
           df.to_csv("NumericAnalysis_Row{rows}Column{cole}.csv", index=False)
       
        def conexcel():
           dt = data(sales, alldata = True)
           selected_rows = dt[(rows.get()-1):rowe.get()]
           selected_columns = [row[(cols.get()-1):(cole.get()+1)] for row in selected_rows]
           df = pd.DataFrame(selected_columns)
           df.to_excel("NumericAnalysis_Row{rows}Column{cole}.xlsx", index=False)

        rsl = Label(export, text = "Starting Row", font = "Arial 20 bold", bg = "skyblue")
        rsl.pack(pady = 10)
        rs = Entry(export, textvariable = rows, font  = "Arial 20 bold")
        rs.pack(pady = 10)
        rel = Label(export, text = "Ending Row", font = "Arial 20 bold", bg = "skyblue")
        rel.pack(pady = 10)
        re = Entry(export, textvariable = rowe, font  = "Arial 20 bold")
        re.pack(pady = 10)
        
        csl = Label(export, text = "Starting Column", font = "Arial 20 bold", bg = "skyblue")
        csl.pack(pady = 10)
        cs = Entry(export, textvariable = cols, font  = "Arial 20 bold")
        cs.pack(pady = 10)
        cel = Label(export, text = "Ending Column", font = "Arial 20 bold", bg = "skyblue")
        cel.pack(pady = 10)
        ce = Entry(export, textvariable = cole, font  = "Arial 20 bold")
        ce.pack(pady = 10)
        
        csvexp = Button(export, text = "Export as CSV", font = "Arial 20 bold", bg = "skyblue", command = concsv())
        csvexp.pack(pady = 10)
        excelexp = Button(export, text = "Export as Spreadsheet", font = "Arial 20 bold", bg = "skyblue", command = conexcel())
        excelexp.pack(pady = 10)
        
    n = Button(export, text = "Numeric Export", font = "Arial 20 bold", bg = "skyblue", command=num)
    n.pack(pady = 10)
    v = Button(export, text = "Visual Export", font = "Arial 20 bold", bg = "skyblue", command=switchg)
    v.pack(pady = 10)
    Button(export, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")    
    Button(export, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")
    
login_window()
