from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class Item:
	
	def __init__(self, name, type, price, quantity, position):
		self.name = name
		self.type = type
		self.price = price
		self.qty = quantity
		self.pos = position
		
class Robot:
	
	def __init__(self, position):
		pass
		
		
class GameMap(Widget):
	
	def __init__(self, map):
		pass
		
		
class BargainHuntGame(Widget):
	items = []
	
	def update(self, dt):
		pass
	
	def on_touch_down(self, touch):
		print("X: " + str(touch.pos[0]) + " Y: " + str(touch.pos[1]))

class BargainHuntApp(App):
	def build(self):
		game = BargainHuntGame()
		
		Window.size = (1024,768)
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		
		return game

if __name__ == '__main__':
	BargainHuntApp().run()