# Imports of modules

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Pyttsx3 initialize speak function

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# Defining function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Sir I am Jarvais, How may I help you sir!!!")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please.")
        return "None"
    return query


if __name__ == "__main__":
    wishme() # Whises the user

    # Logic for executing the task based on the query
    while (True):
        query = takeCommand().lower()

        # Wikipedia information

        if 'wikipedia' in query:
            speak('Searching for wikipedia....')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        # Open Websites

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open miraculous' in query:
            webbrowser.open(
                "https://www.youtube.com/channel/UC5vN2JMO8spPxulyzkGTC_w")

        elif 'open office' in query:
            webbrowser.open("office.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open developer' in query:
            webbrowser.open("developer.microsoft.com")

        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")

        elif 'open codewithharry' in query:
            webbrowser.open("codewithharry.com")

        elif 'open dpsguwahati' in query:
            webbrowser.open("dpsguwahati.org")

        # Play Musics

        elif 'play music' in query:
            music_dir = 'D:\\Musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # Getting the time information from Jarvais 

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {time}")

        # Opening an app

        elif 'open code' in query:
            code_path = '"C:\\Users\\anmol\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(code_path)

        elif 'open powershell' in query:
            shell_path = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
            os.startfile(shell_path)

        # Communication with Jarvais

        elif 'who are you' in query:
            speak("I am Jarvais. An virtual assistant of Anmol Kumar Pandey.")

        elif 'quit' in query:
            speak("Thankyou sir for leting me help you.")
            break

    print("""Thankyou!!!
             © 2020-21 Microsoft
    """)

