from kivy.uix.scrollview import *
from kivy.uix.gridlayout import *
from kivy.uix.button import *
from kivy.uix.boxlayout import *

class SettingsPanel(BoxLayout):
	def __init__(self, root):

		scrollView = self.createItemScrollView(None)
		root.add_widget(scrollView)
		
	def createItemScrollView(self,items):
		layout = GridLayout(cols=1, size_hint_y=None)
		# Make sure the height is such that there is something to scroll.
		layout.bind(minimum_height=layout.setter('height'))
		
		for i in range(30):
			btn = Button(text=str(i), size_hint_y=None, height=40)
			layout.add_widget(btn)
			
		root = ScrollView(size_hint=(0.25, 0.5), pos_hint = {"right" : 1, "top" : 1})
		root.add_widget(layout)
		return root
	
	def getSelectedItems():
		pass
	
	def addToLayout(self, layout):
		layout.add_widget(self)
	
	