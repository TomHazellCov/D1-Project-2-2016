"""used to save the users settings betwen runs in a file: Settings.json"""
import json

			
class Settings:
	#Used to store and save the users settings
#(all in lowercase)Takes the startlocation(eg topleft), sortByValue(eg name), sortByOrder(eg ascending) and algorithm (eg Bubble)   
	def __init__(self):
		self.algorithm = None
		self.sortBy = None
		self.sortOrder = None
		self.time = None
		
	def allSet(self):
		if(self.algorithm != None and self.sortBy != None and self.sortOrder != None and self.time != None):
			return True
		else:
			return False
		
    #takes a prefsStore Object
	def save(self):
		with open("Databases\Settings.json", 'w') as outfile:
			data = {"sortBy" : self.sortBy, "sortOrder" : self.sortOrder, "algorithm" : self.algorithm}
			json.dump(data, outfile)
			
    #returns a prefsStore Object
	def load(self):
		with open("Databases\Settings.json", 'r') as f:
			data = json.load(f)
			self.algorithm = data["algorithm"]
			self.sortBy = data["sortBy"]
			self.sortOrder = data["sortOrder"]

#Usage::
#save = prefsSave()
#prefs = prefsStore("topleft", "name", "ascending", "Bubble")
#save.Save(prefs)
#print(save.Load().StartLocation)
