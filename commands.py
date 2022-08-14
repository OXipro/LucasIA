# put the préfix of LucasIA here
import datetime
import pyttsx3
import playsound
from WeatherGetter import getWeather
import vlc
from config import *
import itertools
from pynput.keyboard import Key, Controller
from time import sleep
# Developer procedure
prefix = prefixconfig + " "
voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[lucasiavoice].id)
rate = voice.getProperty('rate')
voice.setProperty('rate', lucasiarate)
vlc = vlc.Instance()
radio = vlc.media_player_new()


class commands:
    @staticmethod
    def commands(data):
        if data.find(prefix) >= tolerancy or data.find(prefixconfig) >= tolerancy:
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
        if data.find(prefix + "plus de volume") >= tolerancy:
            for _ in itertools.repeat(None, 5):
                Controller().press(Key.media_volume_up)
                sleep(1)
                Controller().press(Key.media_volume_up)
        if data.find(prefix + "moins de volume") >= tolerancy:
            for _ in itertools.repeat(None, 5):
                Controller().press(Key.media_volume_down)
                sleep(1)
                Controller().press(Key.media_volume_down)
