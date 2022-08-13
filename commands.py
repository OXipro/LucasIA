# put the préfix of LucasIA here
import datetime
import pyttsx3
import playsound
from WeatherGetter import getWeather

betaprefix = "lucas"
tolerancy = 0
WeatherCity = "Waterloo"
UserName = "OXipro"
# Developer procedure
prefix = betaprefix + " "
voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[2].id)
rate = voice.getProperty('rate')
voice.setProperty('rate', 160)


class commands:
    @staticmethod
    def commands(data):
        if data.find(prefix) >= tolerancy or data.find(betaprefix) >= tolerancy:
            print("detected")
            playsound.playsound(".\sounds\prefixdetected.wav")
        if data.find(prefix + "stop") >= tolerancy:
            print("ok")
            voice.stop()
            voice.runAndWait()
        if data.find(prefix + "merci") >= tolerancy:
            print("de rien")
            voice.say("de rien")
            voice.runAndWait()
        if data.find(prefix + "bonjour") >= tolerancy:
            print("Bonjour " + UserName + " comment allez-vous ?")
            voice.say("Bonjour " + UserName + " comment tallez-vous ?")
            voice.runAndWait()
        if data.find(prefix + "quelle heure est-il") >= tolerancy:
            print(datetime.datetime.now().strftime("Il est %H Heure et %M Minutes"))
            voice.say(datetime.datetime.now().strftime("Il est %H Heure et %M Minutes"))
            voice.runAndWait()
        if data.find(prefix + "météo") >= tolerancy or data.find(prefix + "donne-moi la météo") >= tolerancy:
            print(getWeather())
            voice.say(getWeather())
            voice.runAndWait()
