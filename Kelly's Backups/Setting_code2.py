"""Allows user to select settings"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Setting_Code(QWidget):


    def __init__(self):
        super().__init__()

        
        self.initUI()


    def initUI(self):
        self.resize(250, 260)
        self.move(1200, 0)
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon('settingicon.png'))


        
        qbtn = QPushButton('Done', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 215)


        self.label1 = QLabel("Start Location:", self)
        self.label1.move(15, 20)
        self.label2 = QLabel("Sort By:", self)
        self.label2.move(40, 70)
        self.label3 = QLabel("Order:", self)
        self.label3.move(50, 120)
        self.label4 = QLabel("Algorithm:", self)
        self.label4.move(30, 170)




        combo1 = QComboBox(self)
        combo1.addItem("Africa")
        combo1.addItem("Scunthorpe")
        combo1.addItem("Mansfield")
        combo1.addItem("Two Forks")
        combo1.addItem("Korea")
        combo1.move(100, 20)
        

        combo2 = QComboBox(self)
        combo2.addItem("Name")
        combo2.addItem("Price")
        combo2.move(100, 70)

        combo3 = QComboBox(self)
        combo3.addItem("Ascending")
        combo3.addItem("Decending")
        combo3.move(100, 120)

        combo4 = QComboBox(self)
        combo4.addItem("Knitting")
        combo4.addItem("Fishing")
        combo4.move(100, 170)

         

        self.show()

 


        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Setting_Code()
    sys.exit(app.exec_())
