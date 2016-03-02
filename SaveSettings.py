"""used to save the users settings betwen runs in a file: Settings.json"""
import json
class SettingsManager:

    #takes a prefsStore Object
    def Save(self, prefs):
        with open("Databases\Settings.json", 'w') as outfile:
            data = { "StartLocation" : prefs.StartLocation, "sortByValue" : prefs.sortByValue, "sortByOrder" : prefs.sortByOrder, "algorithm" : prefs.algorithm}
            json.dump(data, outfile)

    #returns a prefsStore Object
    def Load(self):
        with open("Databases\Settings.json", 'r') as f:
             data = json.load(f)
             print(data)
             prefs = Settings(data["StartLocation"], data["sortByValue"], data["sortByOrder"], data["algorithm"])
             return prefs
            

#Used to store and save the users settings
#(all in lowercase)Takes the startlocation(eg topleft), sortByValue(eg name), sortByOrder(eg ascending) and algorithm (eg Bubble)   
class Settings:
    def __init__(self, StartLocation, sortByValue, sortByOrder, algorithm):
        self.StartLocation = StartLocation
        self.sortByValue = sortByValue
        self.sortByOrder = sortByOrder
        self.algorithm = algorithm

#Usage::
#save = prefsSave()
#prefs = prefsStore("topleft", "name", "ascending", "Bubble")
#save.Save(prefs)
#print(save.Load().StartLocation)
