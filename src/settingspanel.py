from kivy.uix.boxlayout import *
from kivy.uix.button import *
from kivy.uix.checkbox import *
from kivy.uix.floatlayout import *
from kivy.uix.gridlayout import *
from kivy.uix.label import *
from kivy.uix.popup import *
from kivy.uix.scrollview import *
from kivy.uix.spinner import *
from kivy.uix.textinput import *
from globals import *
from logger import Logger
from kivy.uix.slider import Slider
from kivy.properties import *

class ListItem(BoxLayout):

    def __init__(self, item):
        super(ListItem,self).__init__(orientation = 'horizontal', size_hint_y=None, height=30)
        self.nameLabel = Label(text=item.name, size_hint = (0.65, 1.0), pos_hint = {"left" : 0}, halign = "left")
        self.priceLabel = Label(text = "($" + str(item.price) + ")", size_hint = (0.25,1), halign = "right")
        self.item = item

        self.checkbox = CheckBox(size_hint = (0.2, 1), pos_hint = {"right" : 0.95})
        self.checkbox.bind(active = self.checkboxCallback)
        self._checked = False

        self.add_widget(self.nameLabel)
        self.add_widget(self.priceLabel)
        self.add_widget(self.checkbox)

    def isChecked(self):
        return self._checked

    def checkboxCallback(self, checkbox, active):
        self._checked = active

class NumberInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        if(self.isDigit(substring)):
            return super(NumberInput, self).insert_text(substring, from_undo=from_undo)

    def isDigit(self, string):
        try:
            int(string)
            return True
        except:
            return False


class SettingsPanel:
    def __init__(self, game):
        self.game = game

        self.layout = BoxLayout(orientation = "vertical", size_hint = (PANEL_WIDTH/SCREEN_WIDTH,1.0))

        #  CREATE LIST ITEMS, FROM GAME ITEMS
        self.items = game.itemManager.getItems()
        self.listItems = []
        for item in self.items:
            self.listItems.append(ListItem(item))

        self.addItemScrollView()
        self.addSettingsView()

    def addItemScrollView(self):
        # creates a scrollable widget with game items, and adds it to the SettingsPanel layout
        itemGrid = GridLayout(cols=1, spacing=0, size_hint_y = None)
        itemGrid.bind(minimum_height=itemGrid.setter('height'))

        for item in self.listItems:
            itemGrid.add_widget(item)

        scrollView = ScrollView(pos_hint = {"top" : 1}, size_hint = (1.0,0.4), bar_width = 8, scroll_type = ['bars','content'])
        scrollView.add_widget(itemGrid)

        self.addToPanel(scrollView)

    def addSettingsView(self):
        layout = FloatLayout(size_hint = (1.0, 0.6))

        firstRowY = 0.85
        secondRowY = 0.750
        thirdRowY = 0.70
        fourthRowY = 0.60

        self.addLabel(layout, "Sort By:", 0.5, 0.90)
        self.addLabel(layout, "NAME", 0.15, firstRowY)
        self.addLabel(layout, "OR", 0.5, firstRowY)
        self.addLabel(layout, "PRICE", 0.85, firstRowY)
        self.addLabel(layout, "IN", 0.5, secondRowY )
        self.addLabel(layout, "DESCEND", 0.85, thirdRowY )
        self.addLabel(layout, "OR", 0.5, thirdRowY)
        self.addLabel(layout, "ASCEND", 0.15, thirdRowY)
        self.addLabel(layout, "USING", 0.5, fourthRowY)
        self.addLabel(layout, "TIME: ", 0.15, 0.2)
        self.timeLabel = self.addLabel(layout, "0 seconds", 0.43, 0.2)

        self.checkbox = CheckBox(pos_hint = {"center_x" : 0.370, "center_y" : firstRowY}, size_hint = (0.1, 0.1))
        self.checkbox.bind(active = self.nameCheckbox)
        layout.add_widget(self.checkbox)

        self.checkbox = CheckBox(pos_hint = {"center_x" : 1-0.370, "center_y" : firstRowY}, size_hint = (0.1, 0.1))
        self.checkbox.bind(active = self.priceCheckbox)
        layout.add_widget(self.checkbox)

        self.checkbox = CheckBox(pos_hint = {"center_x" : 0.370, "center_y" : thirdRowY}, size_hint = (0.1, 0.1))
        self.checkbox.bind(active = self.ascendingCheckbox)
        layout.add_widget(self.checkbox)

        self.checkbox = CheckBox(pos_hint = {"center_x" : 1-0.370, "center_y" : thirdRowY}, size_hint = (0.1, 0.1))
        self.checkbox.bind(active = self.descendingCheckbox)
        layout.add_widget(self.checkbox)

        spinner = Spinner(
            text='Sort algorithm...',
            values=('Insertion sort', 'Bubble sort'),
            size_hint=(1.0, 0.1),
            pos_hint={'center_x': .5, 'center_y': .5})

        spinner.bind(text=self.algorithmSelection)
        layout.add_widget(spinner)

        button = Button(on_press=self.startButton, text="START", pos_hint={"center_x":0.5, "bottom":0.0}, size_hint=(1.0,0.1))
        layout.add_widget(button)

        slider = Slider(min= 0, max= 120, value=0, pos_hint = {"center_x" : 0.5, "center_y" : 0.3}, size_hint=(1.0,0.2))
        slider.bind(value=self.slider)
        layout.add_widget(slider)

        self.addToPanel(layout)

    def startButton(self, pressed):
        error = None

        if(len(self.getSelectedItems()) < 1):
            error = "Please select at least 1 item"
        elif(self.game.settings.sortBy == None):
            error = "Please select sorting criteria"
        elif(self.game.settings.sortOrder == None):
            error = "Please select sort order"
        elif(self.game.settings.algorithm == None):
            error = "Plese select sorting algorithm"
        elif(self.game.settings.time == 0):
            error = "Please select time greater than 0 seconds"
        elif(self.game.running == True):
            error = "Game is already running!"
        else:
            self.game.start()
            Logger.log(self.game.settings)

        if(error != None):
            self.popup("Uh oh...", error)

    def popup(self, title, message):
        popup = Popup(title=title,
                content=Label(text=message),
                size_hint=(None, None), size=(300, 200))
        popup.open()

    def popup(self, title, message):
        popup = Popup(title=title,
                content=Label(text=message),
                size_hint=(None, None), size=(300, 200))
        popup.open()

    def slider(self, slider, value):
        self.timeLabel.text = str(int(value)) + " seconds"
        self.game.settings.time = value
        pass

    def nameCheckbox(self, checkbox, active):
        if(active):
            self.game.settings.sortBy = "name"
        Logger.log("Sort by: " + self.game.settings.sortBy)

    def priceCheckbox(self, checkbox, active):
        if(active):
            self.game.settings.sortBy = "price"
        Logger.log("Sort by: " + self.game.settings.sortBy)

    def ascendingCheckbox(self, checkbox, active):
        if(active):
            self.game.settings.sortOrder = "ascending"
        Logger.log("Sort order: " + self.game.settings.sortOrder)

    def descendingCheckbox(self, checkbox, active):
        if(active):
            self.game.settings.sortOrder = "descending"
        Logger.log("Sort order: " + self.game.settings.sortOrder)

    def algorithmSelection(self, spinner, selection):
        # only gets the name of the sort algorithm, without "sort" at the end.
        self.game.settings.algorithm = selection.split(' ')[0]
        Logger.log("Algorithm: " + self.game.settings.algorithm)


    def addLabel(self, layout, text, x, y):
        label = Label(text = text,
                         font_size = "16sp",
                         pos_hint = {"center_x" : x, "center_y" : y},
                         size_hint=(None, None),
                         halign='left')

        label.bind(texture_size=label.setter('size'))


        label.size = label.texture_size
        layout.add_widget(label)

        return label

    def addToPanel(self, widget):
        self.layout.add_widget(widget)

    def getSelectedItems(self):
        # returns items selected which were selected by the user in SettingsPanel
        selected = []
        for listItem in self.listItems:
            if(listItem.isChecked() == True):
                selected.append(listItem.item)

        return selected
