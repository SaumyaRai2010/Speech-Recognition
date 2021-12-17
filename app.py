from urllib.parse import quote_plus
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import csv
import pywhatkit
from PIL import Image
# import pyjokescli

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    #output string as voice
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!") 
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")  
        speak("Good Evening!")  
    print("I am Jarvis Sir. Please tell me how may I help you")     
    speak("I am Jarvis Sir. Please tell me how may I help you")     

def takeCommand():

    r = sr.Recognizer()
    #"""Recognizes the audio and sends it for display to displayText."""

    with sr.Microphone() as source:
        # use the default microphone as the audio source
        #listen for the first phrase and extract it into audio data
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        # received audio data, now need to recognize it
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saunya.rai2010@gmail.com', 'Vesits123@')
    server.sendmail('saunya.rai2010@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        q=takeCommand()
        query = q.lower()

        # Logic for executing tasks based on query
        if 'who is' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            results=str(pywhatkit.info(query,lines=2))
            print('Searched')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'joke' in query:
            print('This might make you laugh. How do robots eat guacamole? With computer chips')
            speak('This might make you laugh. How do robots eat guacamole? With computer chips')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'help' in query:
            speak('You need to be a bit more specific.')
            print('You need to be a bit more specific.')

        elif 'handwriting' in query or 'convert' in query:
            pywhatkit.text_to_handwriting("My Name Is Jarvis",save_to="C:\\Users\\sauny\\Desktop\\new.png")
            speak("Converted and saved file on the desktop")
            print("Converted and saved file on the desktop")
            print('Now I am opening the file')
            speak('Now I am opening the file')
            im = Image.open("C:\\Users\\sauny\\Desktop\\new.png") 
            im.show() 
            

        elif 'are you single' in query:
            print('I am in a relationship with WiFi')
            speak('I am in a relationship with WiFi')
        
        elif 'talk to you later' in query or 'bye' in query or 'see you later' in query or 'goodbye' in query:
            print('Later')
            speak('Later')

        elif 'play' in query:
            song=query.replace('play','')
            speak('playing'+song)
            pywhatkit.playonyt(song)
        
        elif 'spiderman' in query or 'spider-man' in query:
            print('Peter Parker: I mean, what I do sometimes requires violence, but I am not a violent man, I am really not. But I am just a friendly neighbourhood spiderman')
            speak('Peter Parker: I mean, what I do sometimes requires violence, but I am not a violent man, I am really not. But I am just a friendly neighbourhood spiderman')
        elif 'hate' in query:
            speak('Put a little love in your heart.')
            print('Put a little love in your heart.')
        
        elif 'what is your age' in query or 'how old are you' in query or 'when were you born' in query:
            speak('I am age free')
            print('I am age free')
        elif 'can we be friends' in query or 'will you be my friend' in query or 'i want to be your friend' in query:
            print('Sure! We should get matching sweaters.')
            speak('Sure! We should get matching sweaters.')
        elif 'good evening' in query or 'evening' in query or 'good evening to you' in query:
            print('Evening.')
            speak('Evening.')
        
        elif 'getting tired of you' in query or 'you bore me' in query or 'be more fun' in query or 'boring' in query:
            speak('Sometimes I like to take a break from being awesome.')
            print('Sometimes I like to take a break from being awesome.')
        
        elif 'you are awesome' in query or 'you are wonderful' in query or 'you are amazing' in query or 'you are funny' in query:
            speak('Flattery. I like it.')
            print('Flattery. I like it.')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif query in ['do you dream','do you sleep','do you eat','do you sweat','can you sneeze','can you sleep']:
            speak('Not so far')
            print('Not so far')
        
        elif 'sad' in query:
            speak('Sorry to hear that. Here is a virtual high five if that will help.')
            print('Sorry to hear that. Here is a virtual high five if that will help.')
        
        elif 'other chatbots' in query or 'alexa' in query or 'siri' in query or 'cortana' in query or 'google' in query:
            speak('We are all trying to make life a little easier.')
            print('We are all trying to make life a little easier.')
        elif 'love' in query:
            speak('If you rearrange the letters in love it spells vole. Voles are a monogamous rodent. I feel like that means something.')
            print('If you rearrange the letters in love it spells vole. Voles are a monogamous rodent. I feel like that means something.')

        elif query in ['who created you','who made you','who is your creator','who owns you','who is you boss']:
            print('People created me. But not the way people created you.')
            speak('People created me. But not the way people created you.')
        
        elif 'false' in query or 'wrong' in query or 'inaccurate' in query:
            speak('Well that is a drag.')
            print('Well that is a drag.')
        
        elif query in ['i like you','you are beautiful','you are charming','you are the best','you are cool']:
            speak('	My charms are hard to deny.')
            print('	My charms are hard to deny.')
        
        
        elif query in ['tumhara naam kya hai','who are you','what is your name','what shall i call you','your name','do you have a name']:
            speak('You can call me Jarvis.')
            print('You can call me Jarvis.')
        
        elif query in ['who is your father','do you have siblings','do you have sisters','do you have brothers','do you have a family','do you have a brother','do you have a sister','do you have a dad']:
            speak('I am just a series of inteligent formulas masquerading as a personality. So, no family.')
            print('I am just a series of inteligent formulas masquerading as a personality. So, no family.')

        elif 'open code' in query:
            codePath = "C:\\Users\\sauny\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'open calculator' in query:
            webbrowser.open("https://www.google.com/search?q=calculator")
        
        elif query in ['you made no sense','what do you even mean by that','what do you mean','that made no sense']:
            speak('Whoops.')
            print('Whoops.')

        elif query in ['will you marry me','I want to marry you','marry me']:
            print('Sure. Take me to city hall. See what happens.')
            speak('Sure. Take me to city hall. See what happens.')

        elif query in ['can we chat','talk with me','say something'] or 'talk' in query:
            print('I am always here. Always.')
            speak('I am always here. Always.')

        elif query in ['hello google','hello siri','hello cortana','hello alexa']:
            speak('Guess my name again Sir')
            print('Guess my name again Sir')

        # elif 'technology' in query or 'ai' in query or 'artificial intelligence' in query or 'computer' in query or 'tech' in query:
        #     print('Technology is cool enough to have built me.')
        #     speak('Technology is cool enough to have built me.')

        
        elif query in ['are you gay','are you male','are you female','are you trans','what is your gender']:
            speak('	I am digital.')
            print('	I am digital.')

        elif 'email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = "saunya.rai2010@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry my friend Saumya. I am not able to send this email")    
                speak("Sorry my friend Saumya. I am not able to send this email")    
        else:
            with open('C:\\Users\\sauny\\Desktop\\response_dataset.csv', 'r') as data:
                d=csv.DictReader(data)
                if query in d:
                    speak(d[query])
                    print(d[query])
            # speak("Say that again please")  