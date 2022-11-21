import re

def function2(regEx,string,nr):
    myList=re.findall(regEx,string)
    retList = []
    for word in myList:
        if len(word) == nr:
            retList.append(word)
    return retList




