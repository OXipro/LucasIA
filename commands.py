# put the préfix of LucasIA here
import datetime
import pyttsx3
import playsound
from WeatherGetter import getWeather
import vlc

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
vlc = vlc.Instance()
radio = vlc.media_player_new()


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
            radio.stop()
        if data.find(prefix + "merci") >= tolerancy:
            print("de rien")
            voice.say("de rien")
            voice.runAndWait()
        if data.find(prefix + "bonjour") >= tolerancy:
            print("Bonjour " + UserName + " comment allez-vous ?")
            voice.say("Bonjour " + UserName + " comment tallez-vous ?")
            voice.runAndWait()
        if data.find(prefix + "heure") >= tolerancy:
            print(datetime.datetime.now().strftime("Il est %H Heure et %M Minutes"))
            voice.say(datetime.datetime.now().strftime("Il est %H Heure et %M Minutes"))
            voice.runAndWait()
        if data.find(prefix + "météo") >= tolerancy:
            print(getWeather())
            voice.say(getWeather())
            voice.runAndWait()
        if data.find(prefix + "radio énergie") >= tolerancy:
            w = vlc.media_new("http://streamingp.shoutcast.com/NRJ")
            radio.set_media(w)
            radio.play()
        if data.find(prefix + "radio contact") >= tolerancy:
            w = vlc.media_new("http://audiostream.rtl.be/contactfr192")
            radio.set_media(w)
            radio.play()
        if data.find(prefix + "mais moins fort") >= tolerancy or data.find(prefix + "baisse le volume") >= tolerancy:
            print("test")

