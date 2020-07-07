from vpython import *
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

l =5
r =.3
for x in range(-l,l+1): #  x axis
    for y in range(-l,l+1): #y axis
        for z in range(-l,l+1): # z axis
            sphere(pos = vector(x,y,z),radius = r,color =color.blue)
            

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('QAEXLK-RY9HY2PHAT')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello everyone ,my name is Vasuki ')
speak('i am more stronger than jarvis version 2.0')
speak('i am also able to solve every problem according to math,science,physic and all ')
speak(' i also interface with hardware with computer chip')
speak(' i also able to intract more emotionaly with human')
speak(' i have my own thinking ablity to build anything')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "what is your name"in query or 'who are you'in query:
            speak('i am jarvis version 2.0 more smart then before and i made by mr shainesh')

        elif 'email' in query:
            speak('Who is the sender? ')
            sender = myCommand()

            if 'I am' in sender:
                try:
                    speak("Please Enter Email address of Recipient.")
                    Recipient_user = input("User: ")
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("yash.nikam2000@gmail.com", 'india@11shainesh')
                    server.sendmail('yash.nikam2000@gmail.com', Recipient_user, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello sir')

        elif 'bye' in query:
            speak('Bye sir, have a good day.')
            sys.exit()

        elif 'play music' in query:
            webbrowser.open('https://www.youtube.com/watch?v=sddTKvsHVTo&list=RDsddTKvsHVTo&start_radio=1')
           
            speak('Okay, here is your music! Enjoy!')
        elif 'what is your feature ' in query:

            speak('well , my first feature is i have my own thinking ability ')
            speak('and my other features are as follow')
            speak('first , i am very close to human than other A I systems')
            speak('second , i also solve every kind of problem ')
            speak('third and last , i interact with human more clearly than other system')
            speaks('so , thats why i am more powerful than jarvis version 2.0')

        elif ' you are smart than jarvis' in query:
            speak('yes i am.')
        elif 'you solve any kind of problem' in query:
            speak('yes, i solve any kind of problem')



        else:
            query = query
            speak('let me see...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('according to my knowlage I says - ')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('according to human information')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! sir!')
