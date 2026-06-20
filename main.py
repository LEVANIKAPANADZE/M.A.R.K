import speech_recognition as sr

recognizer = sr.Recognizer()

def listenPrint():
    with sr.Microphone() as source:
        print("Listening....")

        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

listenPrint()