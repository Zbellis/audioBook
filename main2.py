import pyttsx3


def speak_to_alexa(w):
    keyword = "abrir la puerta"
    if keyword == "abrir la puerta":
        speaker = pyttsx3.init()
        speaker.say(w)
        speaker.runAndWait()


speak_to_alexa('Alexa, turn off the bed room')

