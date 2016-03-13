"""used to save the users settings betwen runs in a file: Settings.json"""
import json


class Settings:
    #Used to store and save the users settings
#(all in lowercase)Takes the startlocation(eg topleft), sortByValue(eg name), sortByOrder(eg ascending) and algorithm (eg Bubble)   
    def __init__(self):
        self.algorithm = None
        self.sortBy = None
        self.sortOrder = None
        self.time = 0

    def allSet(self):
        if(self.algorithm != None and self.sortBy != None and self.sortOrder != None and self.time != None):
            return True
        else:
            return False

#Usage::
#save = prefsSave()
#prefs = prefsStore("topleft", "name", "ascending", "Bubble")
#save.Save(prefs)
#print(save.Load().StartLocation)
