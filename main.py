import pyttsx3
import datetime
import  speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)

print("hh")

engine.setProperty("voice",voices[0].id)
def speak (audio):
    engine.say(audio)
    engine.runAndWait()

# print("hh")
# def wishme():
#    hour = int(datetime.datetime.now().hour)
#    if hour>= 0 and hour < 12:
#        speak("good morning sir have a nice day")
#    elif hour>= 12 and hour< 18:
#        speak("good after noon sir ")
#    else: 
#         speak("good night sir")    

#    print("hh")
#    speak("hi sir i am jarvis. please tell me how can i help you ")

def takecommand ():
     # piks p the audio from microphone    
            r = sr.Recognizer()
            with sr.Microphone as source:
             print("listning....")
             r.pause_threshold = 1 
             audio = r.listen(source) 
            try:
             print("recognizing...")
             query = r.recognize_google(audio,language='en-in')
             print(f'user said: {query}/n ')

            except Exception as e:
             print(e)

             print("say that again please")
            return "none"
            return query    

if __name__ =="_main_":
    #  wishme()
    takecommand()  
    
    
