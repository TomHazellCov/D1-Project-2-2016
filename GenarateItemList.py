import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Entities import *
from ItemManager import *
from selenium import webdriver
import random
from bs4 import BeautifulSoup

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        self.lbTitle = QLabel('Tick the Catagorys you want to get Items from (From tesco.com)')
        self.lbOverWrite = QLabel('Do you want to replace the curent list of items or add to it')
        
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

        btGo = QPushButton("Go")
        btGo.clicked.connect(self.buttonClicked)

        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(self.lbTitle, 1, 0, 1, 2)
        grid.addWidget(self.cbTec, 2, 0)
        grid.addWidget(self.cbHomeElec, 3, 0)
        grid.addWidget(self.cbHome, 4, 0)
        grid.addWidget(self.cbGarden, 5, 0)
        grid.addWidget(self.cbSports, 6, 0)
        grid.addWidget(self.cbEntertain, 7, 0)
        grid.addWidget(self.cbHealth, 8, 0)
        grid.addWidget(self.cbToys, 9, 0)
        grid.addWidget(self.lbOverWrite, 10, 0, 1, 2)
        grid.addWidget(self.cbReplace, 11, 0)
        grid.addWidget(btGo, 12, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')

        self.itemMan = ItemManager("Databases/VRBH.db")
        
        self.show()

    def buttonClicked(self):
        URLList = self.makeURLList()
        items = []
        nextId = 0
        if not self.cbReplace.isChecked():
            items = list(self.itemMan.getItems())
            nextId = items[-1].id + 1
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)


        for URL, Type in URLList:
            
            driver.get(URL)
            print("HERRE")
            # Locate the elements.
            soup = BeautifulSoup(driver.page_source, "html.parser")
            #soup.find_all("div", class_="sister")
            div = soup.find_all("div", class_="products-wrapper")[2]
            l = div.find_all("div", class_="product")
            for i in l:
                print("i")
                
                name = i.find_all("div", class_="title-author-format")[0].getText().strip()
                price = i.find_all("p", class_="price")[0].getText()
                price = price.replace("£", "")
                price = price.replace("\n", "")
                price = price.replace("From", "")

                items.append(Item(nextId, name, Type, float(price), 2, round(self.randomCord(), 3), round(self.randomCord(), 3), "Y"))

                nextId = nextId + 1
        driver.quit()
        self.itemMan.setItems(items)
        self.itemMan.close()

        #update to not be in an obstical
    def randomCord(self):
        return random.uniform(0, 1)

    def makeURLList(self):
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

        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
