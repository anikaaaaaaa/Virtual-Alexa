import speech_recognition as sr
import pyttsx3 as pt
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener=sr.Recognizer()
alexa=pt.init()
voices=alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()
def command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice=listener.listen(source)
            take_command=listener.recognize_google(voice)
            if "Alexa" in take_command:
                take_command=take_command.replace('Alexa'," ")
    except:
        pass
    return take_command
def run_alexa():
    take_command=command()
    if 'time' in take_command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk("Current time is"+ time)
    elif 'play' in take_command :
        song= take_command.replace('play'," ")
        talk('Playing the song'+song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in take_command:
        information = take_command.replace('tell me about', " ")
        info=wikipedia.summary('information',1)
        talk(info)
    elif 'joke' in take_command:
        talk(pyjokes.get_jokes())
    elif 'date' in take_command:
        talk("Sorry bro I am engaged")
    else:
        talk('Please tell me again')
        pywhatkit.search(take_command)
while True:
    run_alexa()

