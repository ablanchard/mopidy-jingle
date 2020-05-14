import pykka

from mopidy import backend
from mopidy.core import CoreListener
from mopidy import audio
import glob
import random

class JingleBackend(pykka.ThreadingActor, backend.Backend, CoreListener):
    def __init__(self, config, audio):
        super(JingleBackend, self).__init__()
        self.audio = audio
        self.media_dir = config['jingle']['media_dir']
        self.every_x = config['jingle']['every_x']
        self.count = 0

    def track_playback_started(self, tl_track):
        self.count = self.count + 1
        if self.count % self.every_x == 0:
            with open(self.choose_file(), mode='rb') as file:
                self.play_file(file)

    def choose_file(self):
        jingles = glob.glob(self.media_dir + "/*.wav")
        return random.choice(jingles) 

    def play_file(self, file):
        fileContent = file.read()
        buffer_ = audio.create_buffer(fileContent, timestamp=None, duration=None)
        self.audio.set_uri('appsrc://')
        consumed = self.audio.emit_data(buffer_).get()
