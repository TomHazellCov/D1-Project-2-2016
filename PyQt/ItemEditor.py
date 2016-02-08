import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Item import *
from SQL import *


class Example(QWidget):
    #TODO input validation
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle('Review')
        
        btn1 = QPushButton("Done")
        btn1.clicked.connect(self.buttonClicked)
        
        btn2 = QPushButton("Add New Item")
        btn2.clicked.connect(self.buttonClicked)

        #data here should be goten from SQLite db this data is tempory
        self.sql = SQL()
        data = self.sql.getItems()
         
        
        self.Table = QTableWidget(len(data), 8)
        self.Table.setHorizontalHeaderLabels(["ItemNumber", "Name", "Type", "Price", "Quantity", "X", "Y", "Wanted"])
        
        row = 0
        for item in data:
            flags = Qt.ItemFlags()
            flags != Qt.ItemIsEnabled
            row0 = QTableWidgetItem(str(item.itemNumber))
            row0.setFlags(flags)
            self.Table.setItem(row, 0, row0)
            self.Table.setItem(row, 1, QTableWidgetItem(item.itemName))
            self.Table.setItem(row, 2, QTableWidgetItem(item.itemType))
            self.Table.setItem(row, 3, QTableWidgetItem(item.itemPrice))
            self.Table.setItem(row, 4, QTableWidgetItem(item.itemQuantity))
            self.Table.setItem(row, 5, QTableWidgetItem(item.postionX))
            self.Table.setItem(row, 6, QTableWidgetItem(item.postitionY))
            self.Table.setItem(row, 7, QTableWidgetItem(item.itemIsWanted))
            row = row + 1

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.Table, 1, 0, 3, 3)
        grid.addWidget(btn1, 4, 2)
        grid.addWidget(btn2, 4, 0)

        

        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.Table.resizeColumnsToContents()
           
        self.show()

    def buttonClicked(self):
        if self.sender().text() == "Done":
            numRows = self.Table.rowCount()
            data = []
            for i in range(numRows):
                itemNumber = self.Table.item(i,0).text()
                itemName = self.Table.item(i,1).text()
                itemType = self.Table.item(i,2).text()
                itemPrice = self.Table.item(i,3).text()
                itemQuantity = self.Table.item(i,4).text()
                postionX = self.Table.item(i,5).text()
                postitionY = self.Table.item(i,6).text()
                itemIsWanted = self.Table.item(i,7).text()
                
                item = Item(itemNumber, itemName, itemType, itemPrice, itemQuantity, postionX, postitionY, itemIsWanted)
                if(self.Validate(item)):
                    data.append(item)
                    print("no")
                else:
                    print("error")
                
            self.sql.setItems(data)

            
            
            #shuld now return a list of items to the SQL class to be saved
            return
        #adds a new row at the end
        rowPosition = self.Table.rowCount()
        self.Table.insertRow(rowPosition)
        
        #sets the first coloum to uneditable
        flags = Qt.ItemFlags()
        flags != Qt.ItemIsEnabled

        itemNumber = self.Table.item(self.Table.rowCount() -2,0).text()
        row0 = QTableWidgetItem(str(int(itemNumber) + 1))
        row0.setFlags(flags)
        
        self.Table.setItem(self.Table.rowCount() - 1, 0, row0)
        
    def Validate(self, item):
        if item.itemNumber == "":
            return False
        
        if item.itemName == "":
            return False
        
        if item.itemType == "":
            return False
        
        if item.itemPrice == "" or not self.isNumeric(item.itemPrice):
            return False
        
        if item.itemQuantity == "" or not self.isNumeric(item.itemQuantity):
            return False
        
        if item.postionX == "" or not self.isNumeric(item.postionX):
            return False
        
        if item.postitionY == "" or not self.isNumeric(item.postitionY):
            return False
        
        if item.itemIsWanted == "" or not self.isBool(item.itemIsWanted):
            return False

        return True
        
    def isNumeric(eslf, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def isBool(eslf, s):
        s = str(s).lower()
        bools = ["y", "n", "true", "false", "yes", "no"]
        if s in bools:
            return True
        return False
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
