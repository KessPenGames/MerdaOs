import commands
import text_to_speech
import yandex
from wakeword import WakeWord
from chatgpt import GPT

from configs import config_reader, config_builder


if __name__ == "__main__":
    print("======================")
    print("MerdaOS v1.0 started!")
    print("======================")
    config_builder.createIfNotExist()
    config = config_reader
    wakeword = WakeWord(config.picovoice_token)
    gpt = GPT(config.openai_token)
    yandex_music = yandex.YandexMusic(config.yandex_token)
    while True:
        text = wakeword.wake_word()
        if text is not None:
            if text == "" or text == " ":
                text_to_speech.text_to_audio("Я не поняла, что вы сказали, не могли бы вы повторить вопрос?")
                continue
            print("{'text': '"+text+"'}")
            if commands.contains(text):
                commands.executeCommand(text, yandex_music)
            else:
                response = gpt.gpt_response(text)
                print("{'gpt': '"+response+"'}")
                text_to_speech.text_to_audio(str(response))
