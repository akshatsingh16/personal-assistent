from time import sleep
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import re
import requests
import subprocess
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import subprocess
import signal
import time
import random
import randfacts
from os import write
import serial
Arduino_Serial = serial.Serial('com6', 9600)

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12:
        speak("GoodMorning!")

    elif hour >= 12 and hour < 18:
        speak("GoodAfternoon!")

    else:
        speak("GoodEvening!")

    speak("I am Jarvis")
    Arduino_Serial.write(str.encode('on1'))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except sr.UnknownValueError as e:
        print("u talkin to mee bruh!!")
        speak("u talkin to mee bruh!!")
        return "None"
    return query


if __name__ == "__main__":
    # os.system('cls')
    wishMe()
    while True:
        #  if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wiki...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# --------------------------------------------------------------------------------------------
        elif 'open youtube' in query:
            speak("ON the waysir")
            webbrowser.open("youtube.com")
# --------------------------------------------------------------------------------------------
        elif 'open google' in query:
            webbrowser.open("google.com")
# --------------------------------------------------------------------------------------------
        elif 'search on google' in query:
            speak('ask me')
            a = takeCommand()
            webbrowser.open_new_tab("https://www.google.com/search?q=" + a)
# --------------------------------------------------------------------------------------------
        elif 'open stack overflow' in query:
            speak("ooohhh!!! the programmers asylum")
            webbrowser.open("stackoverflow.com")
# --------------------------------------------------------------------------------------------
        elif 'play music' in query:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            speak("ready aim shoot")
            os.startfile(os.path.join(music_dir, songs[0]))
# --------------------------------------------------------------------------------------------
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
# --------------------------------------------------------------------------------------------
        elif 'open code' in query:
            codePath = "C:\\Users\\BadBoy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
# --------------------------------------------------------------------------------------------
        elif 'facts' in query:
            x = randfacts.getFact()
            speak(x)
# -----------------------------------------------------------------------------------------
        elif 'music search ' in query:
            speak('searching...')
            query = query.replace("search ", "")
            music_name = query
            query_string = urllib.parse.urlencode({"search_query": music_name})
            formatUrl = urllib.request.urlopen(
                "https://www.youtube.com/results?" + query_string)

            search_results = re.findall(
                r"watch\?v=(\S{11})", formatUrl.read().decode())
            clip = requests.get(
                "https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
            clip2 = "https://www.youtube.com/watch?v=" + \
                "{}".format(search_results[0])

            inspect = BeautifulSoup(clip.content, "html.parser")
            yt_title = inspect.find_all("meta", property="og:title")

            for concatMusic1 in yt_title:
                pass

            print(concatMusic1['content'])

            x = subprocess.Popen(
                "start /b " + "E:\\mpv.exe " + clip2 +
                " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
                shell=True)
# --------------------------------------------------------------------------------------------
        elif 'hi' in query or 'hello' in query or 'yo' in query:
            phrase = ["hello sir", "how can i help you", "how are you",
                      "how was your day", "hola amigo", "yo man", "nani"]
            choice = random.choice(phrase)
            print(choice)
            speak(choice)
#--------------------------------------------------------------------------------------------
        elif 'protocol' in query:
            speak("turning on barn protocol")
            Arduino_Serial.write(str.encode('off1'))
            sleep(2)
            Arduino_Serial.write(str.encode('on2'))
# ---------------------------------------------------------------------------------------------
        elif 'turn of' in query:
            Arduino_Serial.write(str.encode('on1'))
            sleep(2)
            Arduino_Serial.write(str.encode('off2'))
# ---------------------------------------------------------------------------------------------
        elif 'kill the power' in query:
            os.system("shutdown /s /t 1")
# ---------------------------------------------------------------------------------------------