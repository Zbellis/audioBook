import pyttsx3
import datetime


# The date contains year, month, day, hour, minute, second, and microsecond.

x = datetime.datetime.now()
wake_time = x.strftime("%I")


def speak_to_alexa(w):
    keyword = "abrir la puerta"
    if keyword == "abrir la puerta":
        speaker = pyttsx3.init()
        speaker.say(w)
        speaker.runAndWait()


speak_to_alexa('Alexa, turn off the bed room')


# Does the phrase contain word

"""
I am a little scared
Friend, are you there?
"""

