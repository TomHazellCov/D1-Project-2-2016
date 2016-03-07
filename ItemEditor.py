import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Entities import *
from ItemManager import *


class Example(QWidget):
    #TODO input validation
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle('Review')
        
        btn1 = QPushButton("Save")
        btn1.clicked.connect(self.buttonClicked)
        
        btn2 = QPushButton("Add New Item")
        btn2.clicked.connect(self.buttonClicked)

        self.sql = ItemManager("Databases/VRBH.db")
        data = self.sql.getItems()
         
        
        self.Table = QTableWidget(len(data), 8)
        self.Table.setHorizontalHeaderLabels(["ItemNumber", "Name", "Type", "Price", "Quantity", "X", "Y", "Wanted"])
        
        row = 0
        for item in data:
            flags = Qt.ItemFlags()
            flags != Qt.ItemIsEnabled
            row0 = QTableWidgetItem(str(item.id))
            row0.setFlags(flags)
            self.Table.setItem(row, 0, row0)
            self.Table.setItem(row, 1, QTableWidgetItem(item.name))
            self.Table.setItem(row, 2, QTableWidgetItem(item.type))
            print(item.price)
            self.Table.setItem(row, 3, QTableWidgetItem(str(item.price)))
            self.Table.setItem(row, 4, QTableWidgetItem(str(item.qty)))
            self.Table.setItem(row, 5, QTableWidgetItem(str(item.bounds.bottomLeft.x)))
            self.Table.setItem(row, 6, QTableWidgetItem(str(item.bounds.bottomLeft.y)))
            self.Table.setItem(row, 7, QTableWidgetItem(item.wanted))
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
        if self.sender().text() == "Save":
            numRows = self.Table.rowCount()
            data = []
            try:
                for i in range(numRows):
                    itemNumber = str(self.Table.item(i,0).text())
                    itemName = str(self.Table.item(i,1).text())
                    itemType = str(self.Table.item(i,2).text())
                    itemPrice = str(self.Table.item(i,3).text())
                    itemQuantity = str(self.Table.item(i,4).text())
                    
                    postionX = str(self.Table.item(i,5).text())
                        
                    postitionY = str(self.Table.item(i,6).text())
                    if not self.isNumeric(postionX) or not self.isNumeric(postitionY):
                        QMessageBox.about(self, "Error", "an x or y cordinate is not a number")
                        return False
                    itemIsWanted = str(self.Table.item(i,7).text())
                    item = Item(str(itemNumber), str(itemName), str(itemType), str(itemPrice), str(itemQuantity),float(postionX), float(postitionY), str(itemIsWanted))
                    valid = self.validate(item)
                    if(valid == True):
                        data.append(item)
                    else:
                        QMessageBox.about(self, "Error", valid)

            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_obj, fname, exc_tb.tb_lineno)
                QMessageBox.about(self, "Error", "One or more of the fields are blank/empty")
                return False
            self.sql.setItems(data)
            #QtCore.QCoreApplication.instance().quit()
            return
        #adds a new row at the end
        rowPosition = self.Table.rowCount()
        self.Table.insertRow(rowPosition)
        
        #sets the first coloum to uneditable
        flags = Qt.ItemFlags()
        flags != Qt.ItemIsEnabled
        itemNumber = 0
        print(self.Table.rowCount())
        if self.Table.rowCount() == 1:
            itemNumber == -1
        elif self.Table.rowCount() == 2:
            itemNumber == 0
        else:
            itemNumber = self.Table.item(self.Table.rowCount() -2,0).text()
        row0 = QTableWidgetItem(str(int(itemNumber) + 1))
        row0.setFlags(flags)
        
        self.Table.setItem(self.Table.rowCount() - 1, 0, row0)
               
        
    def validate(self, item):
        
        if item.name == "":
            return "an item name is blank"
        
        if item.type == "":
            return "an item type is blank"
        
        if item.price == "" or not self.isNumeric(item.price):
            return "an item price is not numeric"
        
        if item.qty == "" or not self.isNumeric(item.qty):
            return "an item quantity is not numeric"
        
        if item.bounds.bottomLeft.x == "" or not self.isNumeric(item.bounds.bottomLeft.x):
            return "an items position X is not numeric"
        
        if item.bounds.bottomLeft.y == "" or not self.isNumeric(item.bounds.bottomLeft.y):
            return "an items position Y is not numeric"
        
        if item.wanted == "" or not self.isBool(item.wanted):
            return "an items wanted value is not a boolean"

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
