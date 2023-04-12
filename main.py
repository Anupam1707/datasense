import os

state = "a"

speak("Initializing Assistant")
speak("Important Note:")
speak("As soon as I ask you any question please wait until I say 'Listening'")

if os.path.exists("users.txt") == False:
    with open("users.txt", "+w") as f:
        f.write("Users\n")
        f.close()
    with open("passes.txt", "+w") as f:
        f.write("Passwords\n")
        f.close()
    with open("status.txt", "+w") as f:
        f.write("Status\n")
        f.close()
        
def main():
    a = "How can I help You?"
    b = "Do you have any other Query or Question"
    state = a
    login()
    
    while True:
        speak(state)
        caps()
        
main()
