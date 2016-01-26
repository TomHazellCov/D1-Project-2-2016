import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle('Review')
        
        btn1 = QPushButton("Button 1")
        btn1.clicked.connect(self.buttonClicked)
        
        btn2 = QPushButton("1")
        btn2.clicked.connect(self.buttonClicked)
        
        self.Table = QTableWidget(5, 3)
        self.Table.setHorizontalHeaderLabels(["Name", "something", "other"])
        data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
        for n, key in enumerate(sorted(data.keys())):
            for m, item in enumerate(data[key]):
                    newitem = QTableWidgetItem(item)
                    self.Table.setItem(m, n, newitem)


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
        if self.sender().text() == "1":
            item = self.Table.item(1,1)
            print(item.text())
            return
        rowPosition = self.Table.rowCount()
        self.Table.insertRow(rowPosition)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
