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
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from game import Game
from globals import *


class BargainHuntApp(App):

    def build(self):
        self.game = Game()
        self.root = BoxLayout(orientation = 'horizontal')
        self.root.add_widget(self.game.gameScreen)
        self.root.add_widget(self.game.settingsPanel.layout)
        Clock.schedule_interval(self.game.update, 1.0 / FPS_LIMIT)

        return self.root

BargainHuntApp().run()

