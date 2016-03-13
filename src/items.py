import sqlite3 as lite
from entities import Item
import os.path

class ItemManager:
    """ Load items from SQL database """

    def __init__(self, databasePath):
        self.load(databasePath)

    """ Creates an empty database """
    def create(self):
        self.con.execute("""CREATE TABLE 'items' (
        'itemNumber' INTEGER PRIMARY KEY AUTOINCREMENT,
        'itemName' TEXT NOT NULL,
        'itemType' TEXTNOT NULL,
        'itemPrice'  FLOAT  NOT NULL,
        'itemQuantity' INTEGER NOT NULL,
        'itemVectorX' FLOAT NOT NULL,
        'itemVectorY' FLOAT NOT NULL,
        'itemRequestedYN' TEXT NOT NULL)""")

    def load(self, filename):
        fname = filename
        fexists = os.path.isfile(fname)
        self.cur = lite.connect(fname)
        self.con = self.cur.cursor()
        if not fexists:
            self.makeDB()

    def close(self):
        self.cur.close()

    def getItems(self):
        itemList = []
        for i in self.con.execute("SELECT * FROM items"):
            item = Item(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            itemList.append(item)
            self.itemList = itemList
        return itemList
        
    def setItems(self, itemList):
        if len(itemList) == len(self.itemList):
            #the list best always be in order
            for i in range(len(itemList)):
                if not itemList[i] == self.itemList[i]:
                    self.con.execute("UPDATE items SET itemName=?, itemType=?, itemPrice=?, itemQuantity=?, itemVectorX=?, itemVectorY=?, itemRequestedYN=? WHERE itemNumber=?",(itemList[i].itemName, itemList[i].itemType, itemList[i].itemPrice, itemList[i].itemQuantity, itemList[i].postionX, itemList[i].postitionY, itemList[i].itemIsWanted, itemList[i].itemNumber))
                    self.cur.commit()
