import os

state = "a"

speak("Initializing Assistant")
speak("Important Note:")
speak("As soon as I ask you any question please wait until I say 'Listening'")
        
def main():
    a = "How can I help You?"
    b = "Do you have any other Query or Question"
    state = a
    login()
    
    while True:
        speak(state)
        caps()
        
main()
