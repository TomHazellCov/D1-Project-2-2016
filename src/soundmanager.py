from kivy.core.audio import SoundLoader

class SoundManager:
    """
        Code for managing sounds
    """
    def __init__(self):
        self.click = SoundLoader.load('../Assets/click.wav')
        self.waiting = SoundLoader.load('../Assets/waiting.wav')