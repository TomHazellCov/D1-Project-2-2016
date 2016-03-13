"""Allows user to select settings. You will need to preinstall SaveSettings and the Icon
image in the same folder, and make sure you install PyQt5 before trying to run it"""

#importing all the stuff I`ll need
import sys
#PyQt5 stuff is for the GUI
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#So I can use the class set up by Tom
from SaveSettings import *
from json import *

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
        self.setWindowIcon(QIcon('settingicon.png'))
        # readd this code to start of setting icon address for github version: Assets/
        #sets colour, note we have to use USA spelling
        palette= QPalette()
        palette.setColor(QPalette.Background, QColor(42, 77, 171, 255))
        self.setPalette(palette)

        #setting up the labels that will sit next to the drop down menus 
        #as label1 is where the dark 2nd background comes though it has ALOT of new line commands 
        self.label1 = QLabel(" Start Location:                                   \n                                                              \n                                                              \n                                                              \n                                                              \n                                                              \n                                                              \n                                                              \n                                                                   \n                                                                   \n                                                                   \n                                                                   \n                                                                   \n                                                                   \n                                                                   \n                                                                                 \n                                                                        ", self)
        self.label1.move(15, 20)
        self.label2 = QLabel(" Sort By:", self)
        self.label2.move(40, 70)
        self.label3 = QLabel(" Order:", self)
        
        self.label3.move(50, 120)
        
        self.label4 = QLabel(" Algorithm:", self)
        self.label4.move(30, 170)

        #now we set up the drop down menus 


        self.combo1 = QComboBox(self)
        self.combo1.addItem("Top Left")
        self.combo1.addItem("Top Right")
        self.combo1.addItem("Bottom Left")
        self.combo1.addItem("Bottom Right")
        self.combo1.addItem("Center")
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
        self.combo4.addItem("Bubble")
        self.combo4.addItem("Insertion")
        self.combo4.move(100, 170)

        #causes the done button to appear 
        qbtn = QPushButton('Done', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 215)

        #tells the button to run the makefile function 
        qbtn.clicked.connect(self.makefile)

        #loads previous settings
        try:
            #makes json file into dict
            setting = json.loads(open("Databases/ssettings.json").read())
            #takes the value attached to the keys and turns them into a item
            colist1= setting["StartLocation"]
            colist2= setting["sortByValue"]
            colist3= setting["sortByOrder"]
            colist4= setting["algorithm"]
            #checks which one it is then sets the box to be it
            if "Top Left" in colist1:
                self.combo1.setCurrentIndex(0)
            elif "Top Right" in colist1:
                self.combo1.setCurrentIndex(1)
            elif "Top Bottom" in colist1:
                self.combo1.setCurrentIndex(3)
            elif "Bottom Left" in colist1:
                self.combo1.setCurrentIndex(2)
            elif "Center" in colist1:
                self.combo1.setCurrentIndex(4)
            else:
                pass
            
            if "Name" in colist2:
                self.combo2.setCurrentIndex(0)
            elif "Price" in colist2:
                self.combo2.setCurrentIndex(1)
            else:
                pass

            if "Ascending" in colist3:
                self.combo3.setCurrentIndex(0)
            elif "Decending" in colist3:
                self.combo3.setCurrentIndex(1)
            else:
                pass

            if "Bubble" in colist4:
                self.combo4.setCurrentIndex(0)
            elif "Insertion" in colist4:
                self.combo4.setCurrentIndex(1)
            else:
                pass
        finally:
            pass

        #sets secondary background and font colour 
        self.label1.setStyleSheet("QLabel { background-color :  rgb(3, 20, 50); color :  rgb(42, 77, 171); }")
        self.label2.setStyleSheet("QLabel {color :  rgb(42, 77, 171); }")
        self.label3.setStyleSheet("QLabel {color :  rgb(42, 77, 171); }")
        self.label4.setStyleSheet("QLabel {color :  rgb(42, 77, 171); }")

        self.show()

    def makefile(self):
        """telling the function what the variables are using current text to save the current value. Only works with Setting_code"""
        location = (self.combo1.currentText())
        sortby = (self.combo2.currentText())
        order = (self.combo3.currentText())
        algorithm = (self.combo4.currentText())
        prefs= prefsStore(location, sortby, order, algorithm)
        save = prefsSave()
        save.Save(prefs)
        #exits GUI
        QCoreApplication.instance().quit()

        #shuts down the code
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Setting_Code()
    sys.exit(app.exec_())

