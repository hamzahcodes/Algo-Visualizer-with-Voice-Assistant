import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as kit
import webbrowser
import os
import smtplib  
import pygame
import sys
import re

#import Astar as a

WIDTH = 500
#WIN = pygame.display.set_mode((WIDTH,WIDTH))

#contacts = {"abhishek" : "+919653693868", "poojan" : "+919372991040"}



print("Initializing Jarvis!!!!")

''' sapi5 is an inbuilt voice provided for windows users '''

engine = pyttsx3.init('sapi5')                   #initializing text to speech engine
voices = engine.getProperty('voices')            #for getting details of current voice
engine.setProperty('voice', voices[0].id)         # 2 voices available 0 - male ; 1 - female


def speak(audio):
    ''' This function speaks out the text 
    passed as a parameter to the function'''
    engine.say(audio)        #pywhatkit
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning ")

    elif hour > 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis. How may I help you")            

def takeCommand():
    ''' This command uses Speech recognition module to understand
        our command and print a string to the output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")    #google is used for voice recognition
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again Please")
        return "None"

    return query            


def start():

    ''' This is used so that when we create a different
        module and import this module then we can
        access only the functions of it not the other code'''

    wishMe()
    choice = 1
    while 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace('wikipedia','')
            speak("Searching Wikipedia..")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)

        if 'a star' in query:
            speak("Ok Implementing Astar Now")
            a.astar_main(a.WIN, WIDTH)

            speak("What do you want to do next?")

            query = takeCommand().lower()    

            if 'close' in query:
                a.closing()

        if 'whatsapp' in query:
            speak("Whom do you want to send message ? ")
            reciever = takeCommand().lower()
            speak("What message do you want to send ? ")
            msg = takeCommand().lower()

            hr = int(datetime.datetime.now().hour)   
            min = int(datetime.datetime.now().minute) + 2

            file = open("contacts.txt" , 'r')
            data = file.read() 
            file.close()

            pattern = re.findall(rf'\b^{reciever}\s:\s\d+\b',data)
            print(pattern)
             
            char = '+'
            num = re.findall(rf'\b^{char}\d.\b',pattern)
            print(num[0])

            print(num[0], msg, hr , min)
            kit.sendwhatmsg(num[0],msg,hr,min)

            print("Message sent !!!!!")  

        if 'band ho ja' in query:
            break        
start()
print("Code has ended now!!!!")



        


