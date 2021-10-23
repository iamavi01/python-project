import pyttsx3
import speech_recognition as sr
import datetime
import time
import random
from speedtest import parse_args
import wikipedia
from wikipedia.wikipedia import search, summary
import requests
import wolframalpha
import os
from requests import*
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from pywikihow import search_wikihow
import pyautogui as pg
import psutil as ps
import speedtest
import phonenumbers as pn
from phonenumbers import geocoder,carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id) #0=david,1=mark,2=ilike//richard,3=zira
engine.setProperty('rate', 180)
engine.setProperty('volume', 150)

# for voice in voices:
#     print(f"Voice: {voice.name}")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
    app=wolframalpha.Client("X3P7YR-X43VY8PUXJ")
except Exception:
    print("some features are disabled")
    speak("internet connection error")
def wissme():
    '''It greets you according to time'''
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
        speak("Good Morning Sir ")
    elif hour >=12 and hour<18:
        speak("Good After'noon sir; ")    
    elif hour >=18 and hour<=20 :
        speak("good evening sir ")
    speak("I,m jarvis.. ")  
    givetime=("currently it is",clock())
    print(givetime)
    speak(givetime)  
def HaveCommand():
    '''Takes voice "input" as command transform them in text and returns it as query in form of text'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.dynamic_energy_threshold = True
        print("listening...")
        
        audio= r.listen(source)

    try:
        print("Anayalyzing..")
        query = r.recognize_google(audio, language="hindi")
        print(f": {query}\n")
    except Exception as e:
       speak(" immm sorry,, i dint get you")
       execution()
        
    return query    
def HaveCommand2():
    '''Takes voice "input" as command transform them in text and returns it as query in form of text'''
    hc2=sr.Recognizer()
    with sr.Microphone() as source:
        hc2.pause_threshold=1
        print("listening...")
        
        audio= hc2.listen(source)

    try:
        print("Anayalyzing..")
        query2 = hc2.recognize_google(audio, language="en-in")
        print(f": {query2}\n")
    except Exception as e:
        print(e)
      
       #HaveCommand()
        
    return query2        
def mail(to,content):
    email="left"
    cypher="left"
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(f"{email}",f"{cypher}")
    server.sendmail(f"{email}",to,content)
    server.close()


def initilization():
    '''This is startup of program . In short it: Initialize system'''
    speak("Initializing")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment")
    wissme()
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online and ready . tell me how can i be of use")
   
def clock():
    moment=time.strftime("%A  %B  %Y")
    return moment
def batteri():
    ''' returns int value of batery percentage'''
    percentage=ps.sensors_battery()
    battery=percentage.percent
    return battery
def phonenumber(number):
    ''' takes phone number and returns its details'''
    numberch=pn.parse(number,"CH")
    country=(geocoder.description_for_number(numberch,"en"))
    print (country)
    speak(country)
    service=pn.parse(number,"RO")
    Carrier=(carrier.name_for_number(service,"en"))
    print(Carrier)
    speak(Carrier)
    

initilization()
def execution():
    
    '''takes command as query from function have command and check in for what user asked to perform and then does the task asked by users'''
    
    
    Greetings=["hellow this is jarvis" ,"always ready for your command " ]
    GreetingsSecond=["What Can i do for you sir" ,"How can i help you sir", "how can i be of use sir", "tell me What can i do for you sir." ]
    DayGreetings=["it's" , "today is" , "the day is "]
    Greetingsthird=["Good to know sir","shall we work now sir","thats great sir"]
    Greetingsreply=["feeling good sir","im super fine sir","im good sir"]
    Greetingsforill=["whats gone wrong sir","what happend sir","can i know the reason sir"]
    Greetingscontinue=["so lets get back to work sir","so lets continue sir ","shall we continue our work sir"]
    okay=["ohh ,","okay","then","after that what did you do sir","well im not getting anything you are saying"]
   
   
   
   
   
   
    battery=int(batteri())
    if battery<15:
        speak("we are running out of power sir, system will shutdown soon")
   

    while True:
            if battery<15:
                speak("we are running out of power. system will shutdown soon sir")
        
            
            query=HaveCommand().lower()
            
            if "hello jarvis"in query or "hi jarvis" in query or "ok jarvis" in query or "hey jarvis" in query:

                say=random.choice(Greetings),random.choice(GreetingsSecond)
                print(say)
                speak(say)
            elif " time" in query or " day "in query or " duration" in query:
                givetime=(random.choice(DayGreetings),clock(),"sir")
                print(givetime)
                speak(givetime)
            
            elif "how are you" in query or "whats up"in query:
                results=random.choice(Greetingsreply),"what about you"
                speak(results)
                
            elif "i am fine"in query or "all good"in query:
                speak(random.choice(Greetingsthird))
                speak(random.choice(Greetingscontinue))
                
                
            elif"okay" in query or "continue" in query:
                speak(random.choice(GreetingsSecond))
            elif"not fine" in query or "i am not fine"in query or "sick"in query or "not fine"in query:
                speak(random.choice(Greetingsforill))
                
            elif "lets get back to work"in query or "let it be"in query:
                speak("okay sir as u wiss")
                
            elif "i had accident" in query and "i got accident" in query:
                speak("is everything fine sir")
                
               
            elif "every thing is fine"in query or "i am fine"in query or"no need to worry"in query:
                speak("did you consult to doctor")
                
            elif"i talked with doctor"in query or"yah i talked with doctor" in query or "i talked to doctor"in query or "consulted with doctor"in query:
                speak("what did doctor said")
            elif "he said i am fine" in query or"doctor said no need to worry"in query:
                speak("sounds good sir")
                speak("well lets continue to our work sir")
            elif "what should i do" in query or "what can i do"in query:
                speak("sorry sir my response are limited")
            elif "you"in query and "understand"in query:
                speak("while im working on it sir")
            

            elif "browse" in query:
                query=query.replace("browse ","")
                webbrowser.open(f"www.{query}.com")
            elif "who is" in query and "wikipedia" in query  or "what is" in query and "wikipedia" in query or "show me results"in query and "wikipedia"in query or"search for"in query  and "wikipedia"in query or"search" in query and "wikipedia" in query:
                if "wikipedia" in query:
                    query=query.replace("wikipedia", "")
                if "show me results" in query:
                    query=query.replace("show me results", "")
                if "search for" in query:
                    query=query.replace("search", "")
                if "search" in query:
                    query=query.replace("search", "")
                if "for" in query:
                    query=query.replace("for", "")
                if "who is" in query:
                        query=query.replace("who is","")
                if "what is" in query:
                        query=query.replace("what is","")
                rusults= "according to wikipedia"+ summary(query,sentences=2)
                speak(rusults)
                speak("Would you like to listen more or ... would you like to see the page sir.")
                query2=HaveCommand2().lower()
                if "listen" in query2:
                    print(query2)
                    rusu= wikipedia.summary(query,sentences=4)
                    print(rusu)
                    speak(rusu)
                elif"see" or "view" "view page" in query2:
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                    #open browser
            elif "play"in query and "youtube" in query:
                if "play " in query:
                    
                    query=query.replace("play","")
                if "on " in query:
                    query=query.replace("on","")
                if "youtube" in query:
                    query=query.replace("youtube","")
                
                kit.playonyt(query)
                speak(f"playing{query}")
            elif "play music" in query or "songs" in query:
                music_dir="E:\\admin\\Music\\songs"
                songs=os.listdir(music_dir)
                playsong=random.choice(songs)
                os.startfile(os.path.join(music_dir,playsong))
            elif "internet speed" in query:
                st=speedtest.Speedtest()
                dwspeed=int((st.download())/8160)
                upspeed=int((st.upload())/8160)
                speak(f"sir we have {dwspeed}kilobyte per second downloading speed and{upspeed} kilobyte per secont of upload speed")
            elif "my ip"in query:
                ip=get('https://api.ipify.org').text
                print(ip)
                speak(f"your ip address is{ip}")
            elif "where am i" in query or"what is my location" in query:

                r=requests.get('https://get.geojs.io/')
                ip_request=requests.get('https://get.geojs.io/v1/ip.json')
                ipAdd=ip_request.json()['ip']
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_request=requests.get(url)
                geodata=geo_request.json()
                print(geodata)
                yourip=geo_request.json()["ip"]
                country=geo_request.json()["country"]
                internet=geo_request.json()["organization"]
                lon=geo_request.json()["longitude"]
                latitude=geo_request.json()["latitude"] 
                geo_data=f"your current ip Address is {yourip}. and you are currently in {country}. organization providing internet is{internet}.longitude={lon}.latitude={latitude}"
                print(geo_data)
                speak(geo_data)
            elif "temperature" in query or "weather" in query or "surrounding" in query:
                if "surrounding" in query:
                    query=query.replace("surrounding","weather")
                try:
                    res=app.query(query)
                    print(next(res.results).text)
                    output=query,"is",(next(res.results).text)
                    speak(output)
                except:
                    print("network connection error sir")   
                    speak("network connection error sir") 
            
            elif "track " in query:
                speak("what do you want to track")
                query=query.replace("track ","")
                phonenumber(query)
            elif "send mail"in query or"send mail to" in query:
                try:
                    speak("what should i say")
                    content=HaveCommand2()
                    speak("plz tell me the email address of person u wanna send mail")
                    to=HaveCommand2().lower
                    mail(to,content)
                    speak(f"the mail{content} to {to} have been sent succesfully")
                except:
                    speak("sory sir i was unable to send ")
            elif "send message"in query or "text" in query:

                speak("who do you like to send message")
                number=HaveCommand2.lower
                speak("what should i say sir")
                text=HaveCommand2().lower
                kit.sendwhatmsg(f"{number}",f"{text}",f"{tim}")
            elif "lock the system" in query or "lock" in query:
                os.system('cmd /c "shutdown/h"')
                
            elif "log off"in query or "log of" in query or "log out" in query:

                speak("logging off")
                
                os.system('cmd /c "shutdown/l"')    
            elif "abort shutdown"in query:
                speak("cancelling shutdown")
                print(query)
                os.system('cmd /c "shutdown/a"')
            elif "shutdown immediately"in query:
                
                print(query)
                os.system('cmd /c "shutdown/p/f"')
            elif "shutdown"in query:
                speak("system will shutdown after some time")
                print(query)
                os.system('cmd /c "shutdown/s"')
            
            
            elif "restart system"in query:
                speak("system will restart soon")
                print(query)
                os.system('cmd /c "shutdown/r"')
            elif "activate how to mod" in query:
                speak("activated sir")
                speak("tell me what do you want to know")
                while True:
                    how=HaveCommand2().lower
                    
                    try:
                        if "exit" in how or "done" in how:
                            speak("okay sir closing how to mod")
                            break
                        else:
                            max_results=1
                            how_to=search_wikihow(how,max_results)
                            assert len(how_to)==1
                            how_to[0].print()
                            speak(how_to[0].summary)
                            speak("would you like to know something else")
                    except Exception as e:
                        speak("sorry sir cant find it in my database")
                        speak("would you like to search on google?")
                        query=HaveCommand2().lower
                        
                        if "yes"in query or "ok"in query or "search"in query:
                            webbrowser.open(f"https://www.google.com/search?q={how}")
                        elif "no"in query:
                            speak("do you want to know any thing else sir")

            elif"open" in query or "my jarvis open"in query or "jarvis open"in query:
                query=query.replace("open ","")
                if "for me"in query:
                    query=query.replace("for me","")
                if "jarvis" in query:
                    query=query.replace("jarvis ","")
                speak(f"opening{query}")
                pg.hotkey("winleft")
                pg.typewrite(f"{query}")
                pg.hotkey("enter")
            
            elif "switch window"in query or"switch to "in query:
                query=query.replace("switch ","")
                query=query.replace("window ","")
                if "first" in query:
                    query=query.replace("first ","1")
                if "second"in query:
                    query=query.replace("second ","2")
                if "third"in query:
                    query=query.replace("third ","3")
                if "fourth"in query:
                    query=query.replace("fourth ","4")
                if "sixth"in query:
                    query=query.replace("sixth ","6")
                pg.hotkey("winleft",f"{query}")
                
            elif "power" in query or "battery"in query:
                
                speak(f"we have {battery} percent left sir")
                
                if battery<15:
                    speak("we are running out of power sir, system will shutdown soon")
                elif battery>15 and battery<50:
                    speak("we have average power sir ,you can continue working , i will notify you if critical") 
                elif battery>50:
                    speak ("we have enough power sir, we can work till its done")
            elif "slip"in query or "exit" in query or "sleep" in query:
                speak("okay sir , i will be around you")
                speak("just call me when you need")
                break
            else:
                try:

                    if "who is" in query:
                        query=query.replace("who is","")
                    if "what is" in query:
                        query=query.replace("what is","")
                    if "calculate" in query:
                        query=query.replace("calculate","")
                    if "compute" in query:
                        query=query.replace("compute","")

                    res=app.query(query)
                    if "my"in query:
                        query=query.replace("my","your")
                    output=query,"is",(next(res.results).text)
                    print(output)
                    speak(output)
                except:
                    print("could not find anything matching to my database . searching for google sir, please wait ") 
                    speak("could not find anything matching to my database . searching for google sir,please wait")
                    webbrowser.open(f"https://www.google.com/search?q={query}")
            #speak("Do you have anything else to do sir")        
if __name__ == "__main__":
    execution()
    while True:
       
        query=HaveCommand().lower()
        if"wake up" in query or "jarvis" in query:
            execution()
        elif"exit" in query or "shutdown" in query:
           speak("thanks for using me")
           speak("it was great working with you")
           sys.exit()
            
        