import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# starting an engine using pyttsx3 and sapi5 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# setting a male voice
engine.setProperty('voice', voices[0].id)


# This function will be used to speak anything
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This function will wish me and ask for command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis. Please tell me how may I help you?")


def takeCommand():
    '''This function will take command from the user using speech recognition.
        It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query





if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()   # This will take command infinite times (unlimited)

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open brave' in query:
            webbrowser.open("brave.com")

        elif 'open python' in query:
            webbrowser.open("python.org")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "who are you" in query:
            speak("I am Jarvis, your virtual companion.")

        elif "who made you" in query or "who created you" in query:
            speak("I have been developed by Indra")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\INDRANUJ\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is: {strTime}\n")

        elif 'open code' in query:
            speak("Opening VS Code")
            codePath = "C:\\Users\\INDRANUJ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'open word' in query:
            speak("Opening Microsoft Word")
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk"
            os.startfile(codePath)

        elif 'open excel' in query:
            speak("Opening Microsoft Excel")
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk"
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            speak("Opening Microsoft PowerPoint")
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\PowerPoint 2013.lnk"
            os.startfile(codePath)

        elif 'open firefox' in query:
            speak("Opening FireFox")
            codePath = "C:\Program Files\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)


        elif 'quit' in query or 'terminate' in query:
            exit()