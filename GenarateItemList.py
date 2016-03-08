import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Entities import *
from ItemManager import *
from selenium import webdriver
import random
from bs4 import BeautifulSoup
from threading import Thread
import time

"""Class is a worker thread that will callback to update its progress and an item list when done.
It finds items from tescos website"""

class ItemFetcher(Thread):

    def __init__(self, itemList, URLList, replaceItems, callback):
        Thread.__init__(self)
        self.itemList = itemList
        self.URLList = URLList
        self.replaceItems = replaceItems
        self.callback = callback
    
    def run(self):
        URLList = self.URLList
        items = []
        nextId = 0
        if not self.replaceItems:
            items = list(self.itemList)
            nextId = items[-1].id + 1
            
        self.callback("Starting Web Driver", False)
        #phantomjs is the webdriver to avoid opening a webbrowser
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)

        #for each page of items
        for URL, Type in URLList:
            self.callback("Getting " + Type, False)
            driver.get(URL)#get webpage
            time.sleep(1)
            # pipe the html code into bs4
            soup = BeautifulSoup(driver.page_source, "html.parser")
            #find the list of popular elemets
            div = soup.find_all("div", class_="products-wrapper")[2]
            l = div.find_all("div", class_="product")
            for i in l:
                #for each item fidn the price and name
                name = i.find_all("div", class_="title-author-format")[0].getText().strip()
                price = i.find_all("p", class_="price")[0].getText()
                price = price.replace("£", "")
                price = price.replace("\n", "")
                price = price.replace("From", "")

                items.append(Item(nextId, name, Type, float(price), 2, round(self.randomCord(), 3), round(self.randomCord(), 3), "Y"))

                nextId = nextId + 1
        driver.quit()
        self.callback("Done", False)
        self.callback(items, True)

    #given a random cordinate
    def randomCord(self):
        return random.uniform(0, 1)

"""main PyQt UI class"""
class GenarateItemsUi(QMainWindow):
    
    def __init__(self, parent = None):
        super(GenarateItemsUi, self).__init__(parent)
        
        self.initUI()
        
        
    def initUI(self):
        #init instruction text
        self.lbTitle = QLabel('Tick the Catagorys you want to get Items from (From tesco.com)')
        self.lbOverWrite = QLabel('Do you want to replace the curent list of items or add to it')

        #init check boxes
        self.cbTec = QCheckBox('Technology & Gaming', self)
        self.cbTec.toggle()
        self.cbToys = QCheckBox('Toys', self)
        self.cbToys.toggle()
        self.cbHomeElec = QCheckBox('Home Electrical', self)
        self.cbHomeElec.toggle()
        self.cbHome = QCheckBox('Home', self)
        self.cbHome.toggle()
        self.cbGarden = QCheckBox('Garden', self)
        self.cbGarden.toggle()
        self.cbSports = QCheckBox('Sports & Leisure', self)
        self.cbSports.toggle()
        self.cbEntertain = QCheckBox('Entertainment & Books', self)
        self.cbEntertain.toggle()
        self.cbHealth = QCheckBox('Health & Beauty', self)
        self.cbHealth.toggle()
        self.cbReplace = QCheckBox('Replace Current Items', self)

        #init button and connect clicked event with buttonClicked method
        btGo = QPushButton("Go")
        btGo.clicked.connect(self.buttonClicked)

        #init layout
        vbox = QVBoxLayout()

        #add all items to layout
        vbox.addWidget(self.lbTitle)
        vbox.addWidget(self.cbTec)
        vbox.addWidget(self.cbHomeElec)
        vbox.addWidget(self.cbHome)
        vbox.addWidget(self.cbGarden)
        vbox.addWidget(self.cbSports)
        vbox.addWidget(self.cbEntertain)
        vbox.addWidget(self.cbHealth)
        vbox.addWidget(self.cbToys)
        vbox.addWidget(self.lbOverWrite)
        vbox.addWidget(self.cbReplace)
        vbox.addWidget(btGo)
        vbox.addStretch(1)

        #populate window
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(vbox)

        self.setCentralWidget(self.centralWidget)

        #size and center window
        self.resize(300, 300)
        self.center()

        #set title and status
        self.setWindowTitle('Genarate Item List')
        self.statusBar().showMessage('Ready')
        
        self.show()
    

    def buttonClicked(self):
        #called when the button is clicked, gets a list of items, passes that and other arguments to the worker class
        itemMan = ItemManager("Databases/VRBH.db")
        items = itemMan.getItems()
        itemMan.close()
        worker = ItemFetcher(list(items), self.makeURLList(), self.cbReplace.isChecked(), self.CallBack)
        worker.start()

    def CallBack(self, data, finished):
        #this is the callback for the worker class, is used to set the status or save item list
        if finished:
            db = ItemManager("Databases/VRBH.db")
            db.setItems(data)
            return
        self.statusBar().showMessage(data)
        

    def makeURLList(self):
        #depending on what check boxes are ticked it makes a list of terples (URL, catagoryName)
        URLList = []
        if self.cbTec.isChecked():
            URLList.append(("http://www.tesco.com/direct/technology-gaming/?icid=technologygaming_viewall", "Technology & Gaming"))
            
        if self.cbHomeElec.isChecked():
            URLList.append(("http://www.tesco.com/direct/home-electrical/?icid=homeelectrical_viewall", "Home Electrical"))

        if self.cbHome.isChecked():
            URLList.append(("http://www.tesco.com/direct/home-furniture/?icid=homegarden_flyoutlink_ViewAll", "Home"))

        if self.cbGarden.isChecked():
            URLList.append(("http://www.tesco.com/direct/garden/?icid=homegarden_flyoutlink_garden", "Garden"))

        if self.cbToys.isChecked():
            URLList.append(("http://www.tesco.com/direct/toys/?icid=toys_flyoutlink_viewall", "Toys"))

        if self.cbSports.isChecked():
            URLList.append(("http://www.tesco.com/direct/sports-leisure/?icid=sportsandleisure_viewall", "Sports & Leisure"))

        if self.cbEntertain.isChecked():
            URLList.append(("http://www.tesco.com/direct/entertainment-books/?icid=entsandbooks_viewall", "Entertainment & Books"))
            
        if self.cbHealth.isChecked():
            URLList.append(("http://www.tesco.com/direct/health-beauty/?icid=healthandbeauty_viewall", "Health & Beauty"))

        return URLList
    
    def center(self):
        #centers the window on screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = GenarateItemsUi()
    sys.exit(app.exec_())
