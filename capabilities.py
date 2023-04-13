#Features of AI Assitant
"""This contains all the features that can be performed by the AI Assistant"""

import os
import json
import time

try :
    import datetime
    import pyautogui as pg
    import pywhatkit
    import requests
    from newsapi import NewsApiClient
    import pyjokes
    
except ImportError:
    os.system("pip install pyttsx3 SpeechRecognition datetime pyautogui pywhatkit requests newsapi-python pyjokes")

import datetime
import pyautogui as pg
import pywhatkit
import requests
from newsapi import NewsApiClient
import pyjokes

def caps():
        a = "How can I help You?"
        b = "Do you have any other Query or Question"
        
        query = takeCommand()
        
        if "search" in query  or "what is" in query:
            try:
                speak(pywhatkit.info(query, lines=2))
            except:
                speak("An Unknown Error Occurred")
            state = b
            time.sleep(2)
                
        elif "explain" in query  or "tell me about" in query:
            try:
                speak(pywhatkit.info(query, lines=10))
            except:
                speak("An Unknown Error Occurred")
                
        elif 'play' in query:
            #2 Youtube Search
                song = str(query.lower()).replace('play','')
                speak("playing"+song)
                pywhatkit.playonyt(song)
                state = b
                time.sleep(2)
                
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
            time.sleep(2)

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
            time.sleep(2)

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
            time.sleep(2)

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
            time.sleep(2)

        elif "write a note" in query:
            #13 Notes
            speak("What should i write?")
            query = takeCommand()
            file = open('Note.txt', 'w')
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
            time.sleep(2)
            
        elif "logout" in query or "log out" in query or "signout" in query or "sign out" in query:
            out()

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
            time.sleep(2)
            
