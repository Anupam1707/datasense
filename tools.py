import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
##with sr.Microphone() as source:
##        print("Listening........")
##        voice = r.listen(source)
##        speech_data = r.recognize_google(voice)
##   
##    # Returns the string of the recognized voice
##    return speech_data

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

def features():
    speak("I can Help You With:")
    speak("Playing Across Youtube")
    speak("Telling you the Current Time")
    speak("Fetching the weather of any city across the world")
    speak("Entertaining you with a joke")
    speak("Telling the complete top news across India")
    speak("Locating any place on the map")
    speak("Writing and Reading Notes")
    speak("And at last, searching across Internet")

