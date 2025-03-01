import speech_recognition as sr
import pyttsx3   #text -> speech (with local OS voice)
import wikipedia #search query on wiki (internet required)
import pywhatkit #search and play on youtube
import datetime  #give current time and date

#set our TTS engine:
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        speak('i am listening')
        print('listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
    try: 
        command=recognizer.recognize_google(audio)
    except:
        command="No cammand"
    return command

def run_assistant():
    while True: 
        try:
            command=take_command()
            if "time" in command:
               print(command)
               time=datetime.datetime.now().strftime("%I : %M : %p")
               print(time)
               speak(f"The time is {time}")
            elif "day" in command:
               print(command)
               day=datetime.datetime.now().strftime("%d - %m - %y")
               print(day)
               speak(f"today is {day}")
            elif ("who" and "are" and "you") in command:
               print(command)
               speak("I am an AI voice assistant  programmed by one and only Bushra Mughal   She programmed me in 3 days using python language")
            elif "stop" in command:
               print(command)
               speak("Goodbye!")
               break
            elif "play" in command:
               print(command)
               song=command.replace("play","")
               print(f"Playing: {song}")
               speak(f"Playing: {song}")
               try:
                    pywhatkit.playonyt(song)
               except Exception:
                    print("Sorry, can't play that")
                    speak("Sorry, can't play that")
            elif "search" or "wikipedia" in command:
                 print(command)
                 query=command.replace("wikipedia","")
                 try:
                     info=wikipedia.summary(query,sentences=2)
                     print(info)
                     speak(info)
                 except wikipedia.wikipedia.DisambiguationError:
                      speak("Please be more specific.")

            speak("Anything else?")
            continue
        except Exception:
            speak("Sorry, i couldnt understand")
            print("Sorry, i couldnt understand")
            continue
        
#make sure assistant is not imported:
if __name__=="__main__":
    speak("Assistant activated! , how can i help you?")
    run_assistant()