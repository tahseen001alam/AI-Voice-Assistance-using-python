import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import os
import pyautogui
import random

import pyjokes


engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!")
    #time()
    #date()
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<=24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("jarvis at your service............................How I can help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognising....")
        query=r.recognize_google(audio,'en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("text@gmail.com",to,content)
    server.close()



if __name__ == "__main__":
    wishme()

    while True:
        query=takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentence=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="xyz@gmail.com"
                sendmail(to,content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("what should I search ?")
            chromepath="C:\Program Files\Mozilla Firefox\firefox.exe %s"
            search= takeCommand().lower()
            wb.get(chromepath).open_new_tab(search +".com")
        elif "log out" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir="D:\musiclist"
            songs=os.list(dir(songs_dir))
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember that" in query:
            speak("what should i Remember ?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you said to remember that" + remember.read())

