def function6(myList):
    returnList = list()
    for i in range(int(len(myList)/2)):
        returnList.append(list())
    i=0
    y=0
    while(myList):
        x = myList.pop(0)
        if x % 2 == 0:
            returnList[i].insert(0,x)
            i=i+1
        else:
            returnList[y].insert(1,x)
            y=y+1
    return returnList

