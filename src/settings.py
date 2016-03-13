"""used to save the users settings betwen runs in a file: Settings.json"""
import json


class Settings:
    #Used to store user settings
    def __init__(self):
        self.algorithm = None
        self.sortBy = None
        self.sortOrder = None
        self.time = 0

    def allSet(self):
        """
        :return: true if all fields are set, false otherwise
        """
        if(self.algorithm != None and self.sortBy != None and self.sortOrder != None and self.time != None):
            return True
        else:
            return False
