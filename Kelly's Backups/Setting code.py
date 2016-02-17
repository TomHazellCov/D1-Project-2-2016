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
        self = QWidget()
        self.resize(500, 500)
        self.move(1200, 0)
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon('settingicon.png'))
        qbtn = QPushButton('Done', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 50)       
        self.show()

        
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Setting_Code()
    sys.exit(app.exec_()) 
