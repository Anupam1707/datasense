#Account Management
"""This file handles all the account related tasks of AI Assistant"""
from random import *

def login():
    usr = 1000
    pwd = ""
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
            
            usr = len(rows)+2
            
            worksheet.update_cell(usr,1,query)
            worksheet.update_cell(usr,2,pwd)
            worksheet.update_cell(usr,3,"IN")
            
        elif "login" in query:
            speak("Can I know your name please")
            query = takeCommand()

            for i in range(len(rows)):
                if query == rows[i]["Username"]:
                        usr = i
                        break
                else:
                        usr = -1

            if usr != -1:
                    speak("Please type down your password")
                    ps = input("Password : ")

                    if rows[usr]["Password"] == ps:
                            speak("Welcome back" + str(query))
                            worksheet.update_cell(usr+2,3,"IN")
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

    for i in range(len(rows)):
        if query  == rows[i]["Username"]:
            speak("Enter your password")
            pwd = str(input("Password : "))
            usr = i
            break
        else :
            speak("User Account not found")

    if rows[usr]["Password"]  == pwd:
            
        worksheet.update_cell(usr+2,3,"OUT")
        
        exit()
        
