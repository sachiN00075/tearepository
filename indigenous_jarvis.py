import speech_recognition as sr
from datetime import datetime
from datetime import date
import pyttsx3
import time
import webbrowser as wb
import wikipedia
from googlesearch import *
import pywhatkit as kit
#Setting up mic 
mic = sr.Recognizer()

#Setting up speaker
speaker = pyttsx3.init()
speaker.setProperty('rate',150)

#Setting to get time
watch = datetime.now()
time = watch.strftime("%I:%M %p")

#Setting to get date
datee = date.today()


def jarvis():
    try:
        with sr.Microphone() as source:
            print("J.A.R.V.I.S")
            audio = mic.listen(source)
            command = mic.recognize_google(audio)
            command = command.lower()

        if command == "hey jarvis":
            speaker.say("yes sir how can i help you")
        elif "date" in command:
            print("Today's date is " ,datee)
            speaker.say("today's date is")
            speaker.say(datee)
        elif "time" in command:
            print("Current time is " + time)
            speaker.say("current time is" + time)
        elif ".com" in command:
            command = command.replace("open",'')
            speaker.say("searching" + command)
            firefox = wb.Mozilla("Browser Path")
            firefox.open_new_tab(command)
        elif ".in" in command:
            command = command.replace("open",'')
            speaker.say("opening" + command)
            firefox = wb.Mozilla("Browser Path")
            firefox.open_new_tab(command)
        elif "sorry" in command:
            speaker.say("no problem sir")
        elif "ok" in command:
            speaker.say("what next sir")
        elif "wait" in command:
            speaker.say("ok sir")
        elif "who" in command:
            kit.search(command)
            speaker.say("searching"+command)
        elif "what" in command:
            kit.search(command)
            speaker.say("searching"+command)
        else:   
            speaker.say("i am not able to interpret your command maybe able  in near future")
            
    except:
        speaker.say("could not recognize what you just said")
    speaker.runAndWait()
while True:
    jarvis()
    

