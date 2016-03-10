import sqlite3 as lite
from Entities import Item
import os.path

class ItemManager:

	def __init__(self, databasePath):
		self.loaded = False
		self.load(databasePath)
	
	""" Creates an empty database """
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
			self.create()
			
	def close(self):
		self.cur.close()
	"""Load all items from DB and return a list of items"""
	def getItems(self):
		self.loaded = True
		itemList = []
		for row in self.con.execute("SELECT * FROM items"):
			item = Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
			itemList.append(item)
		self.itemList = itemList
		return itemList

	"""used to add or change items in the DB"""
	def setItems(self, itemList):
		if self.loaded == False:
			self.getItems()
		
		#if new list is larger or same size, use update for all existing itesm if they have changed and add all new items
		if len(self.itemList) <= len(itemList):
			for i in range(len(self.itemList)):
				if not itemList[i] == self.itemList[i]:
					self.con.execute("UPDATE items SET itemName=?, itemType=?, itemPrice=?, itemQuantity=?, itemVectorX=?, itemVectorY=?, itemRequestedYN=? WHERE itemNumber=?",(itemList[i].name, itemList[i].type, itemList[i].price, itemList[i].qty, itemList[i].bounds.bottomLeft.x, itemList[i].bounds.bottomLeft.y, itemList[i].wanted, itemList[i].id))
					self.cur.commit()
			if len(itemList) != len(self.itemList):
				for i in range(len(self.itemList), len(itemList), 1):
					self.con.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(itemList[i].id, itemList[i].name, itemList[i].type, itemList[i].price, itemList[i].qty, itemList[i].bounds.bottomLeft.x, itemList[i].bounds.bottomLeft.y, itemList[i].wanted))
					self.cur.commit()
		else:
			#if item new list is smaller than old list then remove all items and re add them all
			self.con.execute("DELETE FROM items;")
			self.cur.commit()
			for i in range(len(itemList)):
				self.con.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(itemList[i].id, itemList[i].name, itemList[i].type, itemList[i].price, itemList[i].qty, itemList[i].bounds.bottomLeft.x, itemList[i].bounds.bottomLeft.y, itemList[i].wanted))
				self.cur.commit()
