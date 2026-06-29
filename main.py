import speech_recognition as sr

recognizer = sr.Recognizer()

def listenPrint():
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

listenPrint()    