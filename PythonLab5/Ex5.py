def function5(myList):
    returnList = list()
    for x in myList:
        if is_number(x):
            returnList.append(x)
    return returnList




def is_number(s):
    if type(s) is str:
        return False
    try:
        float(s)
        return True
    except TypeError:
        return False





