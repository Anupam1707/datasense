import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import pyautogui as pg
import time
import requests
import json
from newsapi import NewsApiClient
import pyjokes
from random import *

state = "a"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

speak("Initializing Assistant")
speak("Important Note:")
speak("As soon as I ask you any question please wait until I say 'Listening'")

def takeCommand():
    query = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        audio = r.listen(source)

    try :
        speak("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please")
        takeCommand()

    return query

def out():
    speak("Which of the user account you want to logout")
    query = takeCommand()

    with open("Users.txt", "r") as o:
        data = o.readlines()

    for i in data:
        if query + "\n" == i:
            speak("Enter your password")
            p = str(input("Password : "))
            usr = i
        else :
            speak("User Account not found")
            
    with open("Passes.txt","r") as p:
        data = p.readlines()

    if data[usr] + "\n" == p:
        with open("Status.txt","r") as r:
            data = r.readlines()

        data[usr] = "Logged Out\n"
        
        with open("Status.txt","w") as w:
            w.writelines(data)
    
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

def features():
    speak("I can Help You With:")
    speak("Searching Across Wikipedia")
    speak("Searching Across Youtube")
    speak("Play Local Music")
    speak("Telling you the Current Time")
    speak("Fetching the weather of any city across the world")
    speak("Entertaining you with a joke")
    speak("Telling the complete top news across India")
    speak("Locating any place on the map")
    speak("Writing and Reading Notes")
    speak("And at last, searching across google")

def main():
    a = "How can I help You?"
    b = "Do you have any other Query or Question"
    state = a
    login()
    while True:
        speak(state)
        query = takeCommand()
        
        if 'wikipedia' in query:
            #1 Wikipedia Search
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            speak(results)
            state = b

        elif 'search on youtube' in query:
            #2 Youtube Search
            query = query.replace("search on youtube", "")
            url = "https://www.youtube.com/results?search_query=" + str(query)
            pg.press('win')
            time.sleep(1)
            pg.write(url)
            time.sleep(0.75)
            pg.press('enter')
            state = b

        elif 'play music' in query:
            #3 It's Music Time
            songs_dir = "J:\Youtube\BGM's\YouTube Common Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            state = b

        elif 'time' in query:
            #4 Ask the Time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            state = b

        elif "what's the weather of" in query or "what is the weather of" in query:
            #5 Ask Weather
            query = query.replace("what's the weather of", "")
            print(query)
            api_key = "141f5109c5c29634665af4a4a59e95a6"
    
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + query + '&appid='+api_key
    
            response = requests.get(weather_url)
    
            weather_info = response.json()
    
            if weather_info['cod'] == 200:
                kelvin = 273 
                temp = int(weather_info['main']['temp'] - kelvin)
                feels_like_temp = int(weather_info['main']['temp'])
                pressure = weather_info['main']['pressure']
                humidity = weather_info['main']['humidity']
                cloudy = weather_info['clouds']['all']
                description = weather_info['weather'][0]['description']
        
                
                weather = f"Weather of: {query}\nTemperature (Celsius): {temp}°\nTemperature (Farenheit): {feels_like_temp}K\nPressure: {pressure} hPa\nHumidity: {humidity}%\nCloud: {cloudy}%\nWeather Info: {description}"
            else:
                weather = f"\n\tWeather for '{query}' not found!\n\tKindly Enter valid City Name !!"
                
            speak(weather)
            state = b
        
        elif 'how are you' in query:
            #6
            speak("I am fine, Thank you")
            speak("How are you?")
            state = b
 
        elif 'fine' in query or "good" in query:
            #6
            speak("It's good to know that you are fine")
            state = b

        elif 'news' in query:
            #7 Get Latest News
            newsapi = NewsApiClient(api_key='91df4271e2cc4fb5bde02842d91492da')
            top_headlines = newsapi.get_top_headlines(
                                        category='technology',
                                        language='en',
                                        country='in')
            
            speak(top_headlines)
            state = b

        elif 'joke' in query:
            #8 Enjoy Joke
            speak(pyjokes.get_joke())
            state = b

        elif "who made you" in query or "who created you" in query or "who designed you" in query:
            #9
            speak("I have been created by Anupam Kanoongo")
            state = b

        elif "who i am" in query:
            #10
            speak("If you talk then definitely your human.")
            state = b

        elif "don't listen" in query or "stop listening" in query or "take a break" in query or "wait" in query:
            #11
            speak("In Seconds : for how much time you want to stop the assistant from listening commands?")
            a = int(takeCommand())
            time.sleep(a)
            state = a

        elif "where is" in query:
            #12 GPS
            query = query.replace("where is", "")
            location = query
            speak("You asked to Locate")
            speak(location)
            url = "https://www.google.nl/maps/place/"+location
            pg.press('win')
            time.sleep(1)
            pg.write(url)
            time.sleep(0.75)
            pg.press('enter')
            state = b

        elif "locate" in query:
            #12 GPS
            query = query.replace("locate", "")
            location = query
            speak("You asked to Locate")
            speak(location)
            url = "https://www.google.nl/maps/place/"+location
            pg.press('win')
            time.sleep(1)
            pg.write(url)
            time.sleep(0.75)
            pg.press('enter')
            state = b

        elif "write a note" in query:
            #13 Notes
            speak("What should i write?")
            query = takeCommand()
            file = open('jarvis.txt', 'w')
            file.write(query)
            state = b
         
        elif "show note" in query:
            #13 Notes
            speak("Showing Notes")
            file = open("note.txt", "r")
            speak(file.read())
            state = b

        elif 'exit' in query:
            #14 Exit
            speak("Thanks for giving me your time")
            exit()

        elif 'what can you do' in query or "how can you help" in query:
            #15 Features
            features()

        elif "logout" in query or "log out" in query or "signout" in query or "sign out" in query:
            exit()

        else:
            #16 Search on google
            url = "https://www.google.co.in/search?q=" + str(query)
            pg.press('win')
            time.sleep(1)
            pg.write(url)
            time.sleep(0.75)
            pg.press('enter')
            time.sleep(5)
            state = b

main()
