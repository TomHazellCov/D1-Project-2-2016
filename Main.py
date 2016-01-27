from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
    
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
	
class Background(Image):
	pass

class Item(Image):
	
	def __init__(self, name, type, price, qty, pos):
		self.name = name
		self.type = type
		self.price = price
		self.qty = qty
		
		super(Item,self).__init__()
		
		
		
		
	def __str__(self):
		return "Name: " + self.name + '\n' + "Type: " + self.type + '\n' + "Price: " + str(self.price) + '\n' + "Qty: " + str(self.qty)
		
class Robot:
	
	def __init__(self, position):
		pass
		
		
		
class GameScreen(FloatLayout):
	items = []
	def __init__(self, app):
		super(GameScreen,self).__init__()
		self.app = app
	
	def update(self, dt):
		pass
	
	def on_touch_down(self, touch):
		pass

class MainApp(App):
	def build(self):
		
		self.root = GameScreen(self)
		item = Item("3","3",3,4,Vector(10,10))
		
		print(self.root.size)
		
		self.root.add_widget(Background())
		self.root.add_widget(item)

		Clock.schedule_interval(self.root.update, 1.0 / 60.0)
		return self.root

		
	def update(self, dt):
		pass

if __name__ == '__main__':
	MainApp().run()
	
	
	
	
	
	
	
	
	
