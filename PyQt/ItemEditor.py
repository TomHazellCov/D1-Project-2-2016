import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Item import *


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
        data = [Item("name", "Type", "1.2", "12", "0.8", "0.6", "y"), Item("name", "Type", "1.2", "12", "0.8", "0.6", "y"),Item("name", "Type", "1.2", "12", "0.8", "0.6", "y")]
        
        self.Table = QTableWidget(len(data), 7)
        self.Table.setHorizontalHeaderLabels(["Name", "Type", "Price", "Quantity", "X", "Y", "Wanted"])
        
        row = 0
        for item in data:
            
            self.Table.setItem(row, 0, QTableWidgetItem(item.itemName))
            self.Table.setItem(row, 1, QTableWidgetItem(item.itemType))
            self.Table.setItem(row, 2, QTableWidgetItem(item.itemPrice))
            self.Table.setItem(row, 3, QTableWidgetItem(item.itemQuantity))
            self.Table.setItem(row, 4, QTableWidgetItem(item.postionX))
            self.Table.setItem(row, 5, QTableWidgetItem(item.postitionY))
            self.Table.setItem(row, 6, QTableWidgetItem(item.itemIsWanted))
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
                print(i)
                itemName = self.Table.item(i,0).text()
                itemType = self.Table.item(i,1).text()
                itemPrice = self.Table.item(i,2).text()
                itemQuantity = self.Table.item(i,3).text()
                postionX = self.Table.item(i,4).text()
                postitionY = self.Table.item(i,5).text()
                itemIsWanted = self.Table.item(i,6).text()
                data.append(Item(itemName, itemType, itemPrice, itemQuantity, postionX, postitionY, itemIsWanted))
            item = self.Table.item(1,1)
            #shuld now return a list of items to the SQL class to be saved
            print(data)
            return
        rowPosition = self.Table.rowCount()
        self.Table.insertRow(rowPosition)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
