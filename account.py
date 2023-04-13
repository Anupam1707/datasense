#Account Management
"""This file handles all the account related tasks of AI Assistant"""

from random import *

def login():
    usr = 1000
    pwd = ""
    ln = 0
    idx = 0
    ps = ""

    for i in range(len(rows)):
        if rows[i]["Login Status"] == "IN":
            usr = i
            break
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

            worksheet.insert_row([query,pwd,"IN"])
            
        elif "login" in query:
            speak("Can I know your name please")
            query = takeCommand()

            for i in len(rows):
                if rows[i]["Username"] == query:
                        usr = i
                        break
                else:
                        usr = -1

            if usr != -1:
                    speak("Please type down your password")
                    ps = input("Password : ")

                    if rows[usr]["Password"] == ps:
                            speak("Welcome back",query)
                    else:
                            speak("Entered Password is Incorrect")
                            
            else:
                    speak("Given user is not signed up yet")
                    speak("Would you like to signup?")

    else:
        speak("Welcome Back" + " " + str(rows[usr]["Username"]))


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
        
