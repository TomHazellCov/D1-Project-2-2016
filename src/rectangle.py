"""
    Rectangle.py : class representing a Rectangle.
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

from kivy.vector import Vector

class Rectangle:
    """ IMPORTANT: Use given methods to change attributes, do NOT change directly. """

    def __init__(self, x,y,width,height):
        """
        creates a rectangle
        :param x: rectangle center x coordinate
        :param y: rectangle center y coordinate
        :param width: rectangle width
        :param height: rectangle height
        :return: nothing
        """
        self.position = Vector(x,y)
        self.size = Vector(width,height)
        self.recalculatePoints()

    def recalculatePoints(self):
        """
        recalculates points
        :param center: boolean to say wheter rectangle has centered position or not
        :return: nothing
        """
        self.top = self.position.y - self.size.y/2
        self.right = self.position.x + self.size.x/2
        self.bottom = self.position.y + self.size.y/2
        self.left = self.position.x - self.size.x/2

    def move(self, x,y):
        """
        moves and recalcuates rectangle points
        :param x: moves rectangle by this x amount
        :param y: moves rectangle by this y amount
        :return: nothing
        """
        self.position += Vector(x, y)
        self.recalculatePoints()

    def setPosition(self, x, y):
        """
        :param x: rectangle center x coordinate
        :param y: rectangle center y coordinate
        :return: nothing
        """
        self.position = Vector(x, y)
        self.recalculatePoints()

    def setSize(self,width,height):
        """
        :param width: rectangle width
        :param height: rectangle height
        :return:
        """
        self.size = Vector(width,height)
        self.recalculatePoints()

    def set(self,x,y,width,height):
        """
        resets the rectangle data
        :param x: center x
        :param y: center y
        :param width: width of the rectangle
        :param height: height of the rectnalge
        :return:
        """

        self.setPosition(x,y)
        self.setSize(width,height)
        self.recalculatePoints()

    def pointInside(self,x,y):
        """
        checks wheter the point is inside rectangle's bounds
        :param x:
        :param y:
        :return:
        """
        if((x > self.left and x < self.right) and (y > self.top and y < self.bottom)):
            return True
        else:
            return False

    def overlaps(self,other):
        """
        :param other: rectangle to check againts
        :return:
        """
        if(self.left >= other.right or self.right <= other.left or self.top >= other.bottom or self.bottom <= other.top):
            return False
        else:
            return True

    def __str__(self):
        return "x,y (" + "%.2f" % self.position.x + ", " + "%.2f" % self.position.y + \
               ") w,h: (" + "%.2f" % self.size.x + ", " + "%.2f" % self.size.y + ")"


# TEST
if __name__ == "__main__":
    r1 = Rectangle(0.9,0, 1,1)
    r2 = Rectangle(0,0, 1,1)
    print(r1)
    print(r2)
    print("Interescts: " + str(r1.overlaps(r2)))