from bs4 import BeautifulSoup
from selenium import webdriver
from Entities import Item
import random
from ItemManager import *
import sys

#update to not be in an obstical
def randomCord():
    return random.uniform(0, 1)

URLList = [("http://www.tesco.com/direct/technology-gaming/?icid=technologygaming_viewall", "Technology & Gaming"), ("http://www.tesco.com/direct/home-electrical/?icid=homeelectrical_viewall", "Home Electrical"), ("http://www.tesco.com/direct/home-furniture/?icid=homegarden_flyoutlink_ViewAll", "Home"), ("http://www.tesco.com/direct/garden/?icid=homegarden_flyoutlink_garden", "Garden"), ("http://www.tesco.com/direct/toys/?icid=toys_flyoutlink_viewall", "Toys"), ("http://www.tesco.com/direct/sports-leisure/?icid=sportsandleisure_viewall", "Sports & Leisure"), ("http://www.tesco.com/direct/entertainment-books/?icid=entsandbooks_viewall", "Entertainment & Books"), ("http://www.tesco.com/direct/health-beauty/?icid=healthandbeauty_viewall", "Health & Beauty")]

itemMan = ItemManager("Databases/VRBH.db")
items = list(itemMan.getItems())
nextId = items[-1].id + 1

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

for URL, Type in URLList:

    driver.get(URL)
    print(URL)

    # Locate the elements.
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #soup.find_all("div", class_="sister")
    div = soup.find_all("div", class_="products-wrapper")[2]
    l = div.find_all("div", class_="product")

    for i in l:
        print("i")
        try:
            name = i.find_all("div", class_="title-author-format")[0].getText().strip()
            price = i.find_all("p", class_="price")[0].getText()
            price = price.replace("£", "")
            price = price.replace("\n", "")
            price = price.replace("From", "")
            items.append(Item(nextId, name, Type, float(price), 2, round(randomCord(), 3), round(randomCord(), 3), "Y"))
        except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_obj, fname, exc_tb.tb_lineno)

        nextId = nextId + 1
    #print(l[0])

driver.quit()
itemMan.setItems(items)
itemMan.close()
for i in items:
    print(i)



#allow as well as and instead of all current items
