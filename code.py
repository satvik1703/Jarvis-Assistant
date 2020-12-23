import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import random
import sys
import wolframalpha
import smtplib
import requests
import json
import time
import playsound
import pygame
import random

engine=pyttsx3.init('sapi5')
# meri window mein bhot saari voices hoti haii unhe use krne k liye we use "sapi5"
voices=engine.getProperty("voices")
print(voices[0].id)
# Agar mein voices ko print krana chahat hun
engine.setProperty('voice',voices[0].id)

client = wolframalpha.Client('UKLRVA-652Y45K7AX')

def speak(audio):
    engine.say(audio) # jo bhi string pass kri haii usein bolega
    engine.runAndWait()

print(
""" JARVIS stands for Just A Rather Very Intelligent System........!!!
-----------------------------------------------------------------------
|        __    ______    ______   __           __  _      _____       |       
|       |  |  |  __  |  |  __  \  \ \         / / | |    / ____]      |
|       |  |  | |__| |  | |  | |   \ \       / /  | |   / /           |
|       |  |  |  __  |  | '--'_/    \ \     / /   | |   \ \____       |
|  _    |  |  | |  | |  |  _  \      \ \   / /    | |    \___  \      |
| | |___|  |  | |  | |  | | \  \      \ \_/ /     | |    ____}  |     |
|  \_______/  |_|  |_|  |_|  \__\      \___/      |_|    \_____/      |     
|                                                                     |
-----------------------------------------------------------------------
""")

def wish_me():
    speak("Starting Engine")
    speak("Collecting required resources")
    speak("initializing")
    speak("Getting information from the CPU")
    speak("contacting with mail services")
    
    playsound.playsound('power up.mp3')
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        print("Good Morning..!!")
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        print("Good AfterNoon..!!")
        speak("Good Afternoon ")
    else:
        print("Good Evening..!!")
        speak("Good Evening ")
    speak('Hello Sir, I am your digital assistant Jarvis!!')
    speak('Please tell me, How may I help you?..')

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in")
        print(f"User Said:{query}\n")
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

with open("D:\\JARVIS\\satvik.txt","r") as r:
    __password = r.read()

if __name__ == "__main__":
    wish_me()
    while True:
        query=take_command().lower()

        #logic for executing tasks
        if "your boss" in query or "creator" in query:
            speak("Mr satvik sharma")
            print("Mr satvik sharma")

        elif "wikipedia" in query:
            speak("Searching Wikipedia......!!")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
    
        elif "open pycharm" in query:
            pycharm_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)
        
        elif "open vs code" in query:
            vs_code_path="C:\\Users\\satvik sharma\\AppData\\Local\\Programs\`\Microsoft VS Code\\Code.exe"
            os.startfile(vs_code_path)
        
        elif 'open' in query:
            pos = query.find('open')
            count_spaces = query.count(' ',pos)
            speak('okay sir!!')
            if count_spaces == 1:
                website_name = query[pos+5:len(query)]
                speak(f'opening {website_name}')
                webbrowser.open(f'www.{website_name}.com')                
            else:
                to_pos = query.find(' ',pos+5)
                website_name = query[pos+5:to_pos]
                speak(f'opening {website_name}')
                webbrowser.open(f'www.{website_name}.com')
        
        elif "the time" in query:
            Time=datetime.datetime.now().strftime("%H:%M:%S")
            print(Time)
            speak(f"sir,the time is:{Time}")
        

        elif "what's up" in query or "how are you" in query:
            stMsgs = [ 'I am fine sir!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "send email" in query or "mail" in query:
                try:
                    speak("To whom you want to send the mail sir...!!!")
                    mail=input("enter the E-mail: ")
                    speak("What should I say Sir....!!!")
                    content=take_command()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("sharma.satvik33@gmail.com",__password)
                    server.sendmail('sharma.satvik33@gmail.com',mail, content)
                    server.close()
                    speak('Email sent!')
                except Exception as e:
                    print(e)
                    speak('Sorry Sir! I am unable to send your message at this moment!')
                    

        elif 'nothing' in query or 'abort' in query or 'stop' in query or "exit" in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif "hello" in query or "hii" in query:
            speak("hello sir")
       
        elif "today news" in query or "daily news" in query or "today's news" in query or "tell me about news" in query or "news" in query:
           
                speak("News for today...Lets begin now")
                url="http://newsapi.org/v2/top-headlines?country=in&apiKey=b2c6e6abfd5a45df87bc40ae0a187ca2"
                news=requests.get(url).text
                news=json.loads(news) #for making it a python object
                for i in range(5):
                    print(f"news:{i}-------->{news['articles'][i]['title']}")
                    speak(news['articles'][i]['title'])
                    if i==4:
                        break
                    speak("Moving on to the next news sir....")    
                speak("Thanx for listening the news sir.")

        elif "check speed" in query or "internet speed" in query or "net speed" in query:
            speak("checking your internet speed sir....")
            print("Checking your Speed.......")
            try:
                os.system('cmd /K "speedtest-cli --simple"')
            except:
                print("Check your Internet Connection...!!")
                pass


        elif "send message" in query:

            speak("To whom you want to send the message sir...!!!")
            number=int(input("enter the number: "))
            speak("what should I say sir...!!")
            message=take_command().title()
            code=+91
            url = "https://http-api.d7networks.com/send"
            querystring = {
            "username":"idzw8705",
            "password":"2ms9Dcvl",
            "from":"Test%20SMS",
            "content":f"{message}",
            "dlr-method":"POST",
            "dlr-url":"https://4ba60af1.ngrok.io/receive",
            "dlr":"yes",
            "dlr-level":"3",
            "to":f"{code}{number}"
            }
            headers = {
            'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            speak("message sent sir....!!")

        elif 'play music' in query or 'play songs' in query:
            music_folder = 'C:\\Users\\satvik sharma\\Desktop\\music'
            music = os.listdir(music_folder)
            music_chosed=random.choice(music)
            os.startfile(os.path.join(music_folder,music_chosed))

            speak('Okay, here is your music! Enjoy!')


        elif "shutdown" in query or "close pc" in query:
            print("Are you sure you want to ShutDown your PC....!!!!")
            speak("Are you sure you want to ShutDown your PC....!!!")
            speak("Type yes if you want to shutdown it.")
            choice=input("want to shutdown your computer? (yes/no): ")
            if "yes" in choice:
                speak("okay sir...!!shutting down your PC")
                os.system("shutdown /s /t 1")
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    print(results)
                    speak(results)
                    

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    print(results)
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')

