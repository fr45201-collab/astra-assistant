import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

def speak(text):
    print("ASTRA:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recongnizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recongnizer.listen(source)
    
    try:
        command = recongnizer.recognize_google(audio)
        command = command.lower()
        return command
    except:
        return ""