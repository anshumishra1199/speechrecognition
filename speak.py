import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5') #windows give api to take voices in computer
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)  #setting male voice (zero) of the computer 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning")
    elif hour >= 12 and hour <18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")
    # speak("I am Jarvis Sir, please tell me hour may I help you")

def takeCommand():
    #it takes microphone input from the user and returns the string output
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1   #Whenever I am speaking it should wait for sometime before completing the string
         audio = r.listen(source)

     try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"user said :{query}\n")
    
     except Exception as e:
        print("Say this again please....")
        query = None
     return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ankitrenukoot@gmail.com')
    server.sendmail("anshumishra1199@gmail.com",to,content)

#Main Commands Start from here...
wishMe()
query = takeCommand()

# Logic for executing task as per the query
def main():
    if 'wikipedia' in query.lower():
        speak("Searching in Wikipedia..")
        query = query.replace("Wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        url="youtube.com"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        # webbrowser.get(using='google-chrome').open(url,new=2)
    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Download\\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))
    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%m:%S")
        speak(f"the tie is {strTime}")
    elif 'open code' in query.lower():
        vsPath = "C:\\Users\\ankit\\AppData\\Local\\Program\\Microsoft VS Code\\Code.exe"
        os.startfile(vsPath)
    elif 'email' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "anshumishra1199@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except Exception as e :
            print(e)
main()
