import pyttsx3

engine = pyttsx3.init()


def text_to_audio(text: str):
    engine.say(text)
    engine.runAndWait()
