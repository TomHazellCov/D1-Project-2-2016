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

from globals import *
from kivy.vector import Vector
from kivy.uix.image import Image
from rectangle import Rectangle

class Entity:
    """
    Game entity which can by a map object, item, robot etc.
    """
    # image file locations in filesystem, list item id number == entity id number
    # default = 0
    # floor = 1
    # barrel = 2
    # small crate = 3
    # medium crate = 4
    # high crate = 5
    # dump = 6
    # forklift = 7
    imageLocations = ["../Assets/default.png",
                      "../Assets/floor.png",
                      "../Assets/barrel.png",
                      "../Assets/large_crate.png",
                      "../Assets/large_crate.png",
                      "../Assets/large_crate.png",
                      "../Assets/forklift_up.png",
                      "../Assets/forklift_right.png",
                      "../Assets/forklift_down.png",
                      "../Assets/forklift_left.png"]

    # image sizes are normalized to range [0,1]
    imageSizes = [Vector(32/GAME_SCREEN_WIDTH,32/GAME_SCREEN_HEIGHT),
                  Vector(GAME_SCREEN_WIDTH/GAME_SCREEN_WIDTH,GAME_SCREEN_WIDTH/GAME_SCREEN_HEIGHT),
                  Vector(32/GAME_SCREEN_WIDTH,32/GAME_SCREEN_HEIGHT),
                  Vector(32/GAME_SCREEN_WIDTH,32/GAME_SCREEN_HEIGHT),
                  Vector(64/GAME_SCREEN_WIDTH,64/GAME_SCREEN_HEIGHT),
                  Vector(96/GAME_SCREEN_WIDTH,96/GAME_SCREEN_HEIGHT),
                  Vector(48/GAME_SCREEN_WIDTH,48/GAME_SCREEN_HEIGHT),
                  Vector(48/GAME_SCREEN_WIDTH,48/GAME_SCREEN_HEIGHT),
                  Vector(48/GAME_SCREEN_WIDTH,48/GAME_SCREEN_HEIGHT),
                  Vector(48/GAME_SCREEN_WIDTH,48/GAME_SCREEN_HEIGHT)]

    def __init__(self,x, y, id):
        self.sprite = Image(source=self.imageLocations[id])
        self.sprite.allow_stretch = True
        self.sprite.auto_bring_to_front = False
        self.id = id
        self.bounds = Rectangle(x,y,self.imageSizes[id].x,self.imageSizes[id].y)
        self.setSize(self.imageSizes[id].x, self.imageSizes[id].y)
        self.setPosition(x,y)

    def addToLayout(self, layout):
        """
        :param layout: Adds widget to specified layout
        :return:
        """
        layout.remove_widget(self.sprite)
        layout.add_widget(self.sprite)

    def collided(self, other):
        if(self.bounds.collided(other.bounds)):
            return True
        else:
            return False

    def setSprite(self, sprite):
        self.sprite = sprite

    def move(self,x,y):
        self.bounds.move(x,y)
        self.sprite.pos[0] += x
        self.sprite.pos[1] += y
        self.sprite.pos_hint = {'center_x' : self.bounds.center.x, 'center_y' : self.bounds.center.y}

    def setSize(self, width, height):
        self.sprite.size_hint = (width, height)
        self.bounds.setSize(width,height)

    def setPosition(self, x, y):
        self.bounds.setPosition(x,y)
        self.sprite.pos = (x,y)
        self.sprite.pos_hint = {'center_x' : x, 'center_y' : y}

    def __eq__(self, other):
        if(self.bounds.position.x == other.bounds.position.x and
           self.bounds.position.y == other.bounds.position.y and
           self.bounds.size.x == other.bounds.size.x and
           self.bounds.size.y == other.bounds.size.y):
            return True
        else:
            return False


    def __str__(self):
        return "Entity ID: " + str(self.id) + ", X,Y: (" + str(self.bounds.position.x) + ", " + str(self.bounds.position.y) + ")"

class Robot(Entity):
    speed = 0.2
    lock_radius = speed/40.0     # pixels

    def __init__(self, x, y):
        super(Robot, self).__init__(x,y,6)
        self.sprite.auto_bring_to_front = True

        self.upTexture = Image(source=Entity.imageLocations[6]).texture
        self.rightTexture = Image(source=Entity.imageLocations[7]).texture
        self.downTexture = Image(source=Entity.imageLocations[8]).texture
        self.leftTexture = Image(source=Entity.imageLocations[9]).texture

        self.moving = False

    def setSprite(self, sprite):
        pass

    def moveTo(self, x, y):
        self.moving = True
        self.destination = Vector(x,y)

    def update(self, dt):
        if(self.moving == True):
            distance = self.destination-self.bounds.position # distance to destination

            velocity = distance.normalize()*self.speed*dt
            if(velocity.x > 0):
                self.sprite.texture = self.rightTexture
            elif(velocity.x < 0):
                self.sprite.texture = self.leftTexture
            elif(velocity.y > 0):
                self.sprite.texture = self.upTexture
            elif(velocity.y < 0):
                self.sprite.texture = self.downTexture

            self.setPosition(self.bounds.position.x+velocity.x,self.bounds.position.y+velocity.y)

            if(self.bounds.position.distance(self.destination) <= self.lock_radius):
                self.setPosition(self.destination.x,self.destination.y)
                self.moving = False

class Item(Entity):
    def __init__(self, id, name, type, price, qty, x, y, wanted):
        super(Item,self).__init__(x,y,0)
        self.name = name
        self.type = type
        self.price = price
        self.qty = qty
        self.wanted = wanted

    def __str__(self):
        return "Name: " + self.name + ", X: " + str(self.bounds.position.x) + ", Y: " + str(self.bounds.position.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
