import asyncio
import threading

from yandex_music import Client

import audio
import text_to_speech

type_to_name = {
    'track': 'трек',
    'artist': 'исполнитель',
    'album': 'альбом',
    'playlist': 'плейлист',
    'video': 'видео',
    'user': 'пользователь',
    'podcast': 'подкаст',
    'podcast_episode': 'эпизод подкаста',
}


class YandexMusic:
    def __init__(self, token):
        self.client = Client(token).init()

    def search_track(self, query):
        if query == "" or query == " ":
            text_to_speech.text_to_audio("Такой трек не найден, попробуйте что-то другое.")
            return
        search_result = self.client.search(query)

        print("Веду поиск...")
        if search_result.tracks:
            track = search_result.tracks.results[0]

            print(f"Найдено следующее: {track.title}")
            download_info = self.client.tracks_download_info(track.trackId)[0]
            track.download(
                f"./audio/track.{download_info.codec}",
                download_info.codec,
                download_info.bitrate_in_kbps
            )
            text_to_speech.text_to_audio(f"Найден следующий трек {track.title}. Включаю.")
            _thread = threading.Thread(
                target=asyncio.run, args=(audio.display_audio(f"./audio/track.{download_info.codec}"),)
            )
            _thread.start()
        else:
            text_to_speech.text_to_audio("Такой трек не найден, попробуйте что-то другое.")
