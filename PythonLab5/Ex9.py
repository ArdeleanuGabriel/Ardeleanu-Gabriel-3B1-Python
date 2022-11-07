def function9(pairs):
    myList=list()
    for pair in pairs:
        myDict = dict()
        myDict["sum"] = str ( pair[0] + pair[1] )
        myDict["prod"] = str ( pair[0] * pair[1] )
        myDict["pw"] = str ( pair[0] ** pair[1] )
        myList.append(myDict)
    return myList


