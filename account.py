from random import *

def logout():
    speak("Which of the user account you want to logout")
    query = takeCommand()

    with open("Users.txt", "r") as o:
        data = o.readlines()

    for i in data:
        if query + "\n" == i:
            speak("Enter your password")
            pwd = str(input("Password : "))
            usr = data.index(i)
        else :
            speak("User Account not found")

    with open("Passes.txt","r") as p:
        data = p.readlines()

    if data[usr] + "\n" == pwd:
        with open("Status.txt","r") as r:
            data = r.readlines()
            
        data[usr] = "Logged Out\n"

        with open("Status.txt","w") as w:
            w.writelines(data)
            
        exit()

def login():
    usr = 1000
    pwd = ""
    ln = 0
    idx = 0
    ps = ""
    
    with open("status.txt","r") as f:
        data = f.readlines()

    for i in range(len(data)):
        if data[i] == "Logged In\n":
            usr = i
        else :
            usr = "none"

    if usr == "none":
        speak("Currently no user is logged in.")
        speak("What would you like to do, login or signup?")
        query = takeCommand()

        if "signup" in query or "sign up" in query:
            speak("Can I know your name please?")
            query = takeCommand()
            speak("Your Password is")
            pwd = query + str(randrange(1000,9999))
            speak(pwd)

            with open("users.txt","r") as u:
                data = u.readlines()

            data.append(query + "\n")

            with open("users.txt","w") as u:
                u.writelines(data)

            with open("passes.txt","r") as p:
                data = p.readlines()
                
            data.append(pwd + "\n")    

            with open("passes.txt","w") as p:
                p.writelines(data)

            with open("status.txt","r") as s:
                data = s.readlines()

            data.append("Logged In\n")

            with open("status.txt","w") as s:
                s.writelines(data)

        elif "login" in query:
            speak("Can I know your name please")
            query = takeCommand()

            with open("users.txt","r") as l:
                data = l.readlines()

                for i in data:
                    if query + "\n" == i:
                        usr = data.index(i)
                    else:
                        usr = -1

                if usr != -1:
                    speak("Please type down your password")
                    ps = input("Password : ")

                    with open("passes.txt","r") as l:
                        data = l.readlines()

                        if data[usr] + "\n" == ps:
                            speak("Welcome back",query)
                        else:
                            speak("Entered Password is Incorrect")
                            
                else:
                    speak("Given user is not signed up yet")
                    speak("Would you like to signup?")

    else:
        with open("users.txt","r") as f:
            data = f.readlines()
        speak("Welcome Back" + " " + str(data[usr]))
