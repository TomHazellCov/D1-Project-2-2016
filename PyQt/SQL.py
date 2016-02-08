#name, type(of item aka food etc), price, quantity, location
#make classes too, clas item with attributes for sql
#class vector,  with x y
#another class: sql manager for getting items

import sqlite3 as lite
from Item import *

cur = lite.connect('VRBH.db')
con = cur.cursor()

itemList = []
##
##if variable == 0:
##    con.execute("DROP TABLE IF EXISTS items")
##    con.execute("CREATE TABLE items(itemNumber INTEGER AUTOINCREMENT,"
##                "itemName TEXT NOT NULL,"
##                "itemType TEXT NOT NULL,"
##                "itemPrice FLOAT NOT NULL,"
##                "itemQuantity INTEGER NOT NULL,"
##                "itemVectorX FLOAT NOT NULL,"
##                "itemVectorY FLOAT NOT NULL,"
##                "itemRequestedYN TEXT NOT NULL,"
##                "PRIMARY KEY (itemNumber) )")
##
##name = str(input("name"))
##itemType = str(input("type"))
##itemprice = float(input("price"))
##quantity = int(input("quantity"))
##x = float(input("vector"))
##y = float(input("vector"))
##request = str(input("Y/N"))
##itemid = con.lastrowid
##con.execute("INSERT INTO items VALUES(?, ?, ?, ?, ?, ?, ?, ?)",(itemid, name, itemType, itemprice, quantity, x, y, request))
##cur.commit()
##
##con.execute("SELECT * FROM items WHERE itemName=?", (name,))
##value = con.fetchall()
##print(value)
##
##quantity-=1
##itemNumber=int(input("number"))
##con.execute("UPDATE items SET itemQuantity=? WHERE itemNumber=?",(quantity, itemNumber))
##cur.commit()

'''below is the loist population'''
for row in cur.execute("SELECT * FROM items"):
    print(row)
    itemList.append(row)

for i in range(1, len(itemList)):
    print(itemList[i])


class SQL:
    def connect(self):
        self.cur = lite.connect('VRBH.db')
        self.con = self.cur.cursor()

    def close(self):
        self.cur.close()

    def getItems(self):
        self.connect()
        itemList = []
        for row in self.con.execute("SELECT * FROM items"):
            item = Item(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))
            #print(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            itemList.append(item)
            self.itemList = itemList
        return itemList
    def setItems(self, itemList):
        if len(itemList) == len(self.itemList):
            #the list best always be in order
            for i in range(len(itemList)):
                if not itemList[i] == self.itemList[i]:
                    print(itemList[i].__dict__, self.itemList[i].__dict__)
                    self.con.execute("UPDATE items SET itemName=?, itemType=?, itemPrice=?, itemQuantity=?, itemVectorX=?, itemVectorY=?, itemRequestedYN=? WHERE itemNumber=?",(itemList[i].itemName, itemList[i].itemType, itemList[i].itemPrice, itemList[i].itemQuantity, itemList[i].postionX, itemList[i].postitionY, itemList[i].itemIsWanted, itemList[i].itemNumber))
                    self.cur.commit()
        
        
sql = SQL()
sql.connect
print(sql.getItems())
cur.close()
