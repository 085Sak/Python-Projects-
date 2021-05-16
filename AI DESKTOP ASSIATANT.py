import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Saksham sir")
    elif hour==12:
        speak("Good Noon")
    elif hour>12 and hour <18:
        speak("goof afternoon Saksham sir")    
    else:
        speak("good evening Saksham sir")    
    speak("my name is jarvis how can i help you")
def takecommand():
        # it take command from mic
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening")
            r.pause_threshold=1
            audio=r.listen(source)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio,language="en-in")
            print(f"user said:{query}\n")
        except Exception as e:
            print("Say that agin please...")    
            return "None"
        return query    







if __name__=="__main__":
    speak("JAI MATA DI")
    wishMe()
    while(True):
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query ,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
       
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open geeksforgeeks" in query:
            webbrowser.open("geeksforgeeks.org")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is (strtime)")
            print(strtime)
        elif " open code" in query:
            cp = "C:\\Users\\saksh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cp)
        elif "open flipkart" in query:
            webbrowser.open("flipkart.com")
        elif "open korean kida" in query:
            webbrowser.open("koreankeeda.com")
        elif "open ideas agency" in query:
            webbrowser.open("idsagency.tech")       

        
