import pvporcupine
from pvrecorder import PvRecorder

import audio


class WakeWord:
    def __init__(self, token):
        self.token = token
        self.porcupine = pvporcupine.create(
            access_key=token,
            keyword_paths=["./models/Merda_pt_windows_v2_2_0.ppn"],
            model_path="./models/porcupine_params_pt.pv",
            sensitivities=[0.5]
        )

        self.recorder = PvRecorder(device_index=1, frame_length=self.porcupine.frame_length)
        self.audio_recorder = audio.Recorder(self.token, self.recorder)

    def wake_word(self):
        self.recorder.start()
        pcm = self.recorder.read()
        keyword_index = self.porcupine.process(pcm)
        if keyword_index >= 0:
            print("Слушаю...")
            audio.bling_effect()
            self.recorder.stop()
            return self.audio_recorder.record()
