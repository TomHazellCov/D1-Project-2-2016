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

from Sprite import Sprite
from kivy.vector import Vector
from rectangle import Rectangle

class Entity:
    # image file locations in filesystem, list item id number == entity id number
    # default = 0
    # floor = 1
    # barrel = 2
    # box = 3
    # dump = 4
    # forklift = 5
    imageLocations = ["Assets/default.png","Assets/floor.png", "Assets/barrel.png","Assets/large_crate.png", "Assets/dump.png", "Assets/forklift.png"]
    imageSizes = [Vector(64,64), Vector(576,576), Vector(64,64), Vector(96,96),Vector(64,64),Vector(96,128),Vector(96,192)]

    def __init__(self,x, y, id):
        self.sprite = Sprite(self.imageLocations[id],True)
        self.bounds = Rectangle(x,y,self.imageSizes[id].x,self.imageSizes[id].y)
        self.setSize(self.imageSizes[id].x, self.imageSizes[id].y)
        self.setPosition(x,y)

    def addToLayout(self, layout):
        layout.add_widget(self.sprite)

    def collided(self, other):
        if(self.bounds.collided(other.bounds)):
            return True
        else:
            return False

    def setSprite(self, sprite):
        self.sprite = sprite

    def move(self,x,y):
        self.setPosition(self.bounds.position.x + x, self.bounds.position.y + y)

    def setSize(self, width, height):
        self.bounds.setSize(width/576, height/576)
        self.sprite.setSize(width/576, height/576)

    def setPosition(self, x, y):
        self.bounds.setPosition(x/576,y/576)
        self.sprite.setPosition(x/576,y/576)


class Robot(Entity):

    def __init__(self, x, y):
        super(Robot, self).__init__(0,0,0)
        self.moving = False

    def moveTo(self, x, y):
        startPos = self.bounds.position
        endPos = Vector(x,y)
        self.distance = startPos.distance(endPos)

        if(self.startPos != self.endPos):
            self.moving = True

    def update(self, dt):
        if(self.moving == True):
            pass

class Item(Entity):
    def __init__(self, id, name, type, price, qty, x, y, wanted):
        super(Item,self).__init__(x,y,0)
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.qty = qty


    def __str__(self):
        return "Name: " + self.name + ", X: " + str(self.bounds.position.x) + ", Y: " + str(self.bounds.position.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
