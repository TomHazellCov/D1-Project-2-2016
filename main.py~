from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class BargainHuntGame(Widget):
    robot = ObjectProperty(None)
    items = []
    
    def __init__(self):
		

    def update(self, dt):
        
    def on_touch_move(self, touch):
		

class BargainHuntApp(App):
    def build(self):
        game = BargainHuntGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    BargainHuntApp().run()