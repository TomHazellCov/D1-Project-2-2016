import sqlite3 as lite
from Entity import *
import os.path

class SQLManager:

	def __init__(self):
		pass
	
	def create(self):
		self.con.execute("""CREATE TABLE 'items' (
		'itemNumber' INTEGER PRIMARY KEY AUTOINCREMENT,
		'itemName' TEXT NOT NULL,
		'itemType' TEXT NOT NULL,
		'itemPrice'  FLOAT NOT NULL,
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
		self.connect()
		itemList = []
		for row in self.con.execute("SELECT * FROM items"):
			item = Item(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))
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
