class Item:
    def __init__(self, itemNumber, itemName, itemType, itemPrice, itemQuantity, postionX, postitionY, itemIsWanted):
        self.itemNumber = itemNumber 
        self.itemName = itemName
        self.itemType = itemType
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
        self.postionX = postionX
        self.postitionY = postitionY
        self.itemIsWanted = itemIsWanted

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

