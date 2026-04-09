import pyttsx3

def    speak(text):
    engine = pyttsx3.init()   
    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("you are on text-speech enine")

while True:
    speak == "tell"
    text = input("You: ")

    if text.lower() == "stop":
        speak("thanks for ur time")
        break

    speak(text)