"""
	InsertionSort.py : BargainHunt game
	Credits: Alex Stacey
	
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



def insertionSortAscending(array):

    for i in range(1,len(array)):

#assigning the current value we are working with, i is it index(position)
        
        valueInArray = array[i]
        index = i 

#While loop as I need a constional loop so it runs when two conditionas are met

        while (index > 0) and (array[index-1] > valueInArray):
        #In an insertion sort algorithm runs when the index is greater
        #0 and the element in the previous position is less than the
        #current element we are looking at

            array[index] = array[index-1] #inserting element into new position in new array
            index = index - 1

        array[index] = valueInArray

def insertionSortDescending(array):

    for i in range(1,len(array)):

#assigning the current value we are working with, i is it index(position)
        
        valueInArray = array[i]
        index = i 

#While loop as I need a constional loop so it runs when two conditionas are met

        while (index > 0) and (array[index-1] < valueInArray):
        #In an insertion sort algorithm runs when the index is greater
        #0 and the element in the previous position is greater than the
        #current element we are looking at

            array[index] = array[index-1] #inserting element into new position in new array
            index = index - 1

        array[index] = valueInArray

def tests():

    #string tests
    print('Tests to see if the two algorithms work on lists of strings :')         
    alist = ['Banana','Orange','Pear','Apple','Melon']
    insertionSortAscending(alist)
    print('Strings Ascending >>>')
    print(alist)

    insertionSortDescending(alist)
    print('Strings Descending >>>')
    print(alist)

    #number tests

    print('Tests to see if the two algorithms work on lists of Ints:')         
    alist2 = [3,5,1,67,42,33,56,90,102]
    insertionSortAscending(alist2)
    print('Ints Ascending >>>')
    print(alist2)

    insertionSortDescending(alist2)
    print('Ints Descending >>>')
    print(alist2)





    




    



        

        
