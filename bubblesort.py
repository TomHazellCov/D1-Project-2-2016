#bubble sort. start at beginning, comapre first two values. if first > second, swap, else, move up an element
#continue through the data til the end, then repeat comparing

ascending = True

def bubbleSort(alist):
    if ascending == True:
        for i in range(len(alist)-1,0,-1):
            for j in range(i):
                if alist[j]>alist[j+1]:
                    temp = alist[j]
                    alist[j] = alist[j+1]
                    alist[j+1] = temp
                    
    else:
        for i in range(len(alist)-1,0,-1):
            for j in range(i):
                if alist[j]<alist[j+1]:
                    temp = alist[j]
                    alist[j] = alist[j+1]
                    alist[j+1] = temp
                    


#list would be set to the predetermined values in the database.
                    
bubbleSort(alist)
print(alist)

#save = prefsSave()
#save.Load()

#one paramter to select order aka boolean
#another to say sort type (not really needed tbh, but useful for finding right data)
