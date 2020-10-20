#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import pyttsx3

import speech_recognition as sr 

import datetime

import wikipedia 

import webbrowser 

import os
# The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
import smtplib

 

print("Initializing Charlotte")

 
# Here Master refers to the User here I have used my name, here You can use yours. Just change the name.
MASTER = "Anubhav"

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

#Here I have taken voice of a female if You wish you can use male voice too.
# Here I have set the voices Id [1] as Female voice has the Id 1 and if You are using male voice you can set Voice Id To [0].
engine.setProperty('voice', voices[1].id)

# speak function will prounce the string which is passed to it.

def speak(text):

    engine.say(text)

    engine.runAndWait()

 

#This Function will wish you as per the given time

def wishMe():

    hour = int(datetime.datetime.now().hour)

   

    if hour>=0 and hour <12:

        speak("Good Morning Mr." + MASTER)

 

    elif hour>=12 and hour <18:

        speak("Good Afternoon Mr." + MASTER)

 

    else:

        speak("Good Evening Mr." + MASTER)

       

    #speak("I am Charlotte. How may i help You?")
    # The above function can be used if you want, but i personally didn't wanted to greet every time so i Commented it, if you want to use you are free to do so.
 

# This function will take command from microphone

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

 

    try:

        print("Recognizing...")

        query = r.recognize_google(audio, language= 'en-in')

        print(f"user said: {query}\n")

 

    except exception as e:

        print("Say that again please")

        query = None

    return query

 
# It will be better if you don't use email function as it can hamper the security of the email. If you want to try then create a dummy email.
def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.login('sfhehofhgeopughjw@gmail.com','efgeugfwe')

    server.sendmail("abc@gmail.com", to, content)

    server.close()

 

def main():

    # Main function start here..

    speak("Initialising Charlotte....")

    wishMe()

    query = takeCommand()

 

    #logic for executing task as per query

    if 'wikipedia' in query.lower():

        speak('Searching wikipedia...')

        query = query.replace("wikipedia", "")

        results = wikipedia.summary(query, sentences=4)

        speak("According to wikipedia")

        print(results)

        speak(results)

 

    elif 'open youtube' in query.lower():

        #webbrowser.open("youtube.com")

        url = "youtube.com"

        browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

        webbrowser.get(browser_path).open(url)

 

    elif 'open google' in query.lower():

        #webbrowser.open("youtube.com")

        url = "google.com"

        browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

        webbrowser.get(browser_path).open(url)  

 

    elif 'open reddit' in query.lower():

        #webbrowser.open("youtube.com")

        url = "reddit.com"

        browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

        webbrowser.get(browser_path).open(url) 

    elif 'the time' in query.lower():

        strTime = datetime.datetime.now().strftime("%H:%M:%S")

        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():

        codePath = "C:\\Users\\SAKSHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        os.startfile(codePath)

    elif 'open whatsapp' in query.lower():

        codePath = ""

        os.startfile(codePath)

main()

