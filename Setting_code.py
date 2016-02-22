"""Allows user to select settings. You will need to preinstall SaveSettings and the Icon image in the same folder, and make sure you install PyQt5 before trying to run it"""

#importing all the stuff I`ll need
import sys
#PyQt5 stuff is for the GUI
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#So I can use the class set up by Tom
from SaveSettings import *

#setting up the code

class Setting_Code(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    #sets the size on the window and the icon
        self.setFixedSize(250, 260) #it looks awful bigger, I`ve locked the size down 
        self.move(1200, 0)
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon('Assets\settingicon.png'))
        
        #sets colour, note we have to use USA spelling
        palette= QPalette()
        palette.setColor(QPalette.Background, Qt.blue)
        self.setPalette(palette) 

        #causes the done button to appear 
        qbtn = QPushButton('Done', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 215)
        #setting up the labels that will sit next to the drop down menus 

        self.label1 = QLabel("Start Location:", self)
        self.label1.move(15, 20)
        self.label2 = QLabel("Sort By:", self)
        self.label2.move(40, 70)
        self.label3 = QLabel("Order:", self)
        self.label3.move(50, 120)
        self.label4 = QLabel("Algorithm:", self)
        self.label4.move(30, 170)

        #now we set up the drop down menus 


        self.combo1 = QComboBox(self)
        self.combo1.addItem("Africa")
        self.combo1.addItem("Scunthorpe")
        self.combo1.addItem("Mansfield")
        self.combo1.addItem("Two Forks")
        self.combo1.addItem("Korea")
        self.combo1.move(100, 20)
        

        self.combo2 = QComboBox(self)
        self.combo2.addItem("Name")
        self.combo2.addItem("Price")
        self.combo2.move(100, 70)

        self.combo3 = QComboBox(self)
        self.combo3.addItem("Ascending")
        self.combo3.addItem("Decending")
        self.combo3.move(100, 120)

        self.combo4 = QComboBox(self)
        self.combo4.addItem("Knitting")
        self.combo4.addItem("Fishing")
        self.combo4.move(100, 170)

        #tells the button to run the makefile function 
        qbtn.clicked.connect(self.makefile)

        self.show()

    def makefile(self):
        #telling the function what the variables are using current text to save the current value 
        location = (self.combo1.currentText())
        sortby = (self.combo2.currentText())
        order = (self.combo3.currentText())
        algorithm = (self.combo4.currentText())
        prefs= prefsStore(location, sortby, order, algorithm)
        #I chose to save the file in Pickle form
        save = prefsSave()
        save.Save(prefs)
        QCoreApplication.instance().quit()
        #shuts down the code
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Setting_Code()
    sys.exit(app.exec_())
