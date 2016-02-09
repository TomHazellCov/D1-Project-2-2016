"""
	Main.py : BargainHunt game
	Credits: Edvinas Kilbauskas

	This file is part of BargainHunt.

	BargainHunt is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	BargainHunt is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with BargainHunt. If not, see <http://www.gnu.org/licenses/>.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.image import Texture
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder

from Rectangle import Rectangle
from Entity import Entity
from Entity import Sprite

class Background(Entity):
	def __init__(self, width, height):
		sprite = Sprite(width,height, "Assets/background.jpeg")
		super(Entity,self).__init__(0,0, width, height, sprite)
		self.allow_stretch = True
		self.keep_ratio = False
		self.size = Vector(width, height)
	
class Item(Entity):
	def __init__(self, name, type, price, qty, source):
		super(Entity,self).__init__(0,0,64,64, source)
		self.name = name
		self.type = type
		self.price = price
		self.qty = qty
		self.bounds = Rectangle(0,0,64,64)

	def __str__(self):
		return "Name: " + self.name + '\n' + "Type: " + self.type + '\n' + "Price: " + str(self.price) + '\n' + "Qty: " + str(self.qty)
		
class Robot:
	def __init__(self, position):
		pass
		
class BargainHunt(FloatLayout):
	items = []
	def __init__(self, app, **kwargs):
		super(BargainHunt,self).__init__(**kwargs)
		self.app = app
		background = Background(800,600)
		background.addToLayout(self)
		
	def addEntity(self,entity):
		pass
	
	def update(self, dt):
		pass
	
	def on_touch_down(self, touch):
		texture = Image(source="Assets/fish.png").texture
		item = Item(name="Name",type="Type",price=199.99,qty=1)
		item.texture = texture
		item.allow_stretch = True
		item.setPosition(touch.pos)
		self.add_widget(item)
		
class MainApp(App):
	def build(self):	
		self.root = BargainHunt(self)
		Clock.schedule_interval(self.root.update, 1.0 / 60.0)
		return self.root

if __name__ == '__main__':
	MainApp().run()