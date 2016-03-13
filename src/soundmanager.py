from kivy.core.audio import SoundLoader

class SoundManager:

    def __init__(self):
        self.click = SoundLoader.load('../Assets/click.wav')
        self.waiting = SoundLoader.load('../Assets/waiting.wav')