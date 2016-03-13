"""
	SortingAlgorithms.py : BargainHunt game
	Credits: 

	This file is part of BargainHunt.

	BargainHunt is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	BargainHunt is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with BargainHunt. If not, see <http://www.gnu.org/licenses/>.
"""

class SortingManager:
    """
        Manages sorting
    """

    def __init__(self, settings):
        self.settings = settings

    def sort(self, itemArray):
        """
        Sorts array according to game settings
        :param itemArray: array to be sorted
        :return: sorted array
        """
        ascending = False
        sortByName = False
        
        if self.settings.sortOrder == "ascending":
            ascending = True
        if self.settings.sortBy == "name":
            sortByName = True

        if self.settings.algorithm == "Bubble":
            return self.bubbleSort(itemArray, ascending, sortByName)
        elif self.settings.algorithm == "Insertion":
            return self.insertionSort(itemArray, ascending, sortByName)


    def insertionSort(self, array, ascending, sortByName):
        if sortByName == True:
            for i in range(1,len(array)):
            #assigning the current value we are working with, i is it index(position)
                
                valueInArray = array[i]
                index = i

                #While loop as I need a constional loop so it runs when two conditionas are met
                
                while (index > 0) and ((ascending == True and(array[index-1].name > valueInArray.name)) or (ascending == False and (array[index-1].name < valueInArray.name))):
                #In an insertion sort algorithm runs when the index is greater
                #0 and the element in the previous position is less than the
                #current element we are looking at

                    array[index] = array[index-1] #inserting element into new position in new array
                    index = index - 1

                array[index] = valueInArray
            return array
        elif sortByName == False:
            for i in range(1,len(array)):
            #assigning the current value we are working with, i is it index(position)

                valueInArray = array[i]
                index = i

                #While loop as I need a constional loop so it runs when two conditionas are met

                while (index > 0) and ((ascending == True and(array[index-1].price > valueInArray.price)) or (ascending == False and (array[index-1].price < valueInArray.price))):
                #In an insertion sort algorithm runs when the index is greater
                #0 and the element in the previous position is less than the
                #current element we are looking at

                    array[index] = array[index-1] #inserting element into new position in new array
                    index = index - 1

                array[index] = valueInArray
            return array

    
    #if sortByName is false it sorts by price
    def bubbleSort(self, alist, ascending, sortByName):
        print(sortByName)
        if sortByName == True:
            if ascending == True:
                for i in range(len(alist)-1,0,-1):
                    for j in range(i):
                        if alist[j].name>alist[j+1].name:
                            temp = alist[j]
                            alist[j] = alist[j+1]
                            alist[j+1] = temp
            else:
                for i in range(len(alist)-1,0,-1):
                    for j in range(i):
                        if alist[j].name<alist[j+1].name:
                            temp = alist[j]
                            alist[j] = alist[j+1]
                            alist[j+1] = temp
        elif sortByName == False:
            if ascending == True:
                for i in range(len(alist)-1,0,-1):
                    for j in range(i):
                        if alist[j].price>alist[j+1].price:
                            temp = alist[j]
                            alist[j] = alist[j+1]
                            alist[j+1] = temp
                            
            else:
                for i in range(len(alist)-1,0,-1):
                    for j in range(i):
                        if alist[j].price<alist[j+1].price:
                            temp = alist[j]
                            alist[j] = alist[j+1]
                            alist[j+1] = temp
        return alist


