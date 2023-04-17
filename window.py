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
            home_window()
        else:
            error_label = Label(login, text="Incorrect username or password", fg="red")
            error_label.pack()

    button = Button(login, text="Login", command=login_button)
    button.pack()

    login.mainloop()

def home_window():
    main = Tk()
    main.geometry("1280x720")
    main.resizable(False,False)

    response = requests.get("https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/bg.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((1280,720), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    main.title("Food Sales Management")
    title = Label(main, text= 'Food Sales Management', font= 'Arial 35 bold',bg='#7676EE').pack(pady=0)
    Button(main, text = 'Exit', font = 'Arial 20 bold', bg='red', command=main.destroy).pack(side = BOTTOM,anchor = "se")

    # Create the first dropdown menu
    option_1_label = tk.Label(main, text="Option 1")
    option_1_label.grid(row=0, column=0)
    option_1_var = tk.StringVar()
    option_1_dropdown = ttk.Combobox(main, width=15, textvariable=option_1_var, state="readonly")
    option_1_dropdown["values"] = ("Option A", "Option B", "Option C")
    option_1_dropdown.grid(row=0, column=1)

    # Create the second dropdown menu
    option_2_label = tk.Label(main, text="Option 2")
    option_2_label.grid(row=1, column=0)
    option_2_var = tk.StringVar()
    option_2_dropdown = ttk.Combobox(main, width=15, textvariable=option_2_var, state="readonly")
    option_2_dropdown["values"] = ("Option D", "Option E", "Option F")
    option_2_dropdown.grid(row=1, column=1)

    # Create the third dropdown menu
    option_3_label = tk.Label(main, text="Option 3")
    option_3_label.grid(row=2, column=0)
    option_3_var = tk.StringVar()
    option_3_dropdown = ttk.Combobox(main, width=15, textvariable=option_3_var, state="readonly")
    option_3_dropdown["values"] = ("Option G", "Option H", "Option I")
    option_3_dropdown.grid(row=2, column=1)

    main.mainloop()
    
login_window()
