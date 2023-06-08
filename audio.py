import asyncio
import os
import struct
import threading
import uuid
import wave

import pvcobra
import pygame

import speech_to_text

pygame.init()


class Recorder:
    def __init__(self, token, recorder):
        self.cobra = pvcobra.create(access_key=token)
        self.recorder = recorder

    def record(self):
        audio = []
        self.recorder.start()
        print("Записываю...")
        silence_count = 0
        while True:
            frame = self.recorder.read()
            audio.extend(frame)
            is_voiced = self.cobra.process(frame)
            if is_voiced < 0.04:
                silence_count += 1
                if silence_count == 35:
                    break
            else:
                silence_count = 0
        self.recorder.stop()
        filename = f"./audio/{str(uuid.uuid1())}.wav"
        with wave.open(filename, 'w') as f:
            f.setparams((1, 2, 16000, 4000, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
        print("Записала!")
        return speech_to_text.audio_to_text(filename)


stop_music = ["пустота"]
volume = [1.0]
pause = [False]
loop = [False]


def bling_effect():
    mp3 = pygame.mixer.Sound('./audio/bling.wav')
    mp3.play()


async def display_audio(filename: str, delete: bool = True):
    stop_music.clear()
    stop_music.append("пустота")
    pause.clear()
    pause.append(False)
    mp3 = pygame.mixer.Sound(filename)
    mp3.play()
    while mp3.get_num_channels() != 0:
        mp3.set_volume(volume[0])
        if pause[0]:
            pygame.mixer.pause()
        elif mp3.get_num_channels() != 0 and pygame.mixer.get_busy():
            pygame.mixer.unpause()
        if any(word in "стоп" for word in stop_music):
            pygame.mixer.stop()
            break
        continue
    if loop[0]:
        _thread = threading.Thread(
            target=asyncio.run, args=(display_audio(filename, delete),)
        )
        _thread.start()
        return
    if delete:
        os.remove(filename)


def reduce_volume(reduce: float = 0.1):
    volume_ = volume[0]
    if volume_ == 0:
        return
    volume.clear()
    volume.append(volume_ - reduce)


def plus_volume(reduce: float = 0.1):
    volume_ = volume[0]
    if volume_ == 1.0:
        return
    volume.clear()
    volume.append(volume_ + reduce)


def pause_audio():
    pause.clear()
    pause.append(True)


def play_audio():
    pause.clear()
    pause.append(False)


def loop_audio():
    loop.clear()
    loop.append(True)


def outloop_audio():
    loop.clear()
    loop.append(False)


def stop_all_audio():
    outloop_audio()
    stop_music.append("стоп")
    print("Все аудиозаписи были остановлены!")
