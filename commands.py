import audio
import text_to_speech

from datetime import datetime
from num2words import num2words

import yandex
import youtube

commands_list = [
    {"time": "текущее время"},
    {"music": "включи музыку|включи трек|включи рек|запусти музыку|запусти трек|запусти рек"},
    {"video": "включи видео|запусти видео"},
    {"stop": "хватит|выключи музыку|выключи видео|вырубай|"
             "выключи трек|отключи музыку|отключи трек|отключи видео"},
    {"reduce_half_volume": "уменьши громкость наполовину|убавь громкость наполовину|"
                           "убавь музыку наполовину|понизь громкость наполовину|"
                           "сделай тише наполовину|сделай потише наполовину"},
    {"reduce_volume": "уменьши громкость|убавь громкость|убавь музыку|"
                      "понизь громкость|сделай тише|сделай потише"},
    {"plus_volume": "прибавь громкость|увеличь громкость|прибавь музыку|сделай громче|сделай погромче"},
    {"pause": "поставь на паузу|поставь трек на паузу|поставь музыку на паузу|поставь видео на паузу|"
              "пауза|останови|стоп"},
    {"continue": "продолжи|продолжай|запускай|запусти дальше|убери паузу|отключи паузу"},
    {"loop": "зацикли|включи бесконеч|цикличным|включи цикл|запусти бесконеч|запусти цикл"},
    {"outloop": "отключи цикл|отключи бесконеч|убери цикл|убери бесконеч|"
                "отключи цекало|выключи цикл|выключи цекало|выключи бесконеч"}
]


def contains(text: str):
    for command in commands_list:
        if any(word in text for word in list(command.values())[0].split("|")):
            return True
    return False


def getType(text: str):
    for command in commands_list:
        trigger_list = list(command.values())[0].split("|")
        if any(word in text for word in trigger_list):
            print("{'cmd': " + str(command) + "}")
            return list(command.keys())[0], next((word for word in trigger_list if word in text), None)
    return None, None


def executeCommand(text: str, yandex_music: yandex.YandexMusic):
    command_type, trigger = getType(text)
    print("Выполняю команду...")
    if command_type == "time":
        now = datetime.now().time()
        hours = num2words(now.hour, lang='ru')
        minutes = num2words(now.minute, lang='ru')
        text_to_speech.text_to_audio(f"Текущее время сейчас {hours} часов {minutes} минут")
    elif command_type == "music":
        audio.stop_all_audio()
        yandex_music.search_track(text.split(trigger)[1])
    elif command_type == "stop":
        text_to_speech.text_to_audio("Выключаю")
        audio.stop_all_audio()
    elif command_type == "reduce_volume":
        text_to_speech.text_to_audio("Уменьшаю")
        audio.reduce_volume()
    elif command_type == "reduce_half_volume":
        text_to_speech.text_to_audio("Уменьшаю")
        audio.reduce_volume(0.5)
    elif command_type == "plus_volume":
        text_to_speech.text_to_audio("Прибавляю")
        audio.plus_volume()
    elif command_type == "pause":
        text_to_speech.text_to_audio("Останавливаю музыку")
        audio.pause_audio()
    elif command_type == "continue":
        text_to_speech.text_to_audio("Продолжаю музыку")
        audio.play_audio()
    elif command_type == "video":
        audio.stop_all_audio()
        url = youtube.search_video(text.split(trigger)[1])
        youtube.download_audio(url)
    elif command_type == "loop":
        text_to_speech.text_to_audio("Зацикливаю")
        audio.loop_audio()
    elif command_type == "outloop":
        text_to_speech.text_to_audio("Отключаю цикл")
        audio.outloop_audio()
    print("Команда выполнена!")
