import os

from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json

SetLogLevel(-1)

model = Model("./models/vosk-model-small-ru-0.22")


def audio_to_text(filename: str):
    rec = KaldiRecognizer(model, 16000)

    wf = wave.open(filename, "rb")

    text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            pass
        else:
            text = json.loads(rec.PartialResult())["partial"]
    wf.close()
    os.remove(filename)
    return text
