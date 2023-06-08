import asyncio
import threading

import yt_dlp
from youtubesearchpython import VideosSearch

import audio
import text_to_speech


def search_video(query):
    print("Веду поиск...")
    videosSearch = VideosSearch(query, limit=1)
    try:
        return videosSearch.result()["result"][0]["link"]
    except IndexError:
        text_to_speech.text_to_audio("Видео не найдено, поэтому послушайте любое случайное видео.")
        return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=False)
        if int(video_info['duration']) <= 600:
            ydl.download([url])
            filename = video_info['title'] + ".mp3"
            text_to_speech.text_to_audio(f"Найдено следующие видео {video_info['title']}. Включаю.")
            _thread = threading.Thread(
                target=asyncio.run, args=(audio.display_audio(filename),)
            )
            _thread.start()
        else:
            text_to_speech.text_to_audio(f"Видео слишком длинное, его невозможно включить")

