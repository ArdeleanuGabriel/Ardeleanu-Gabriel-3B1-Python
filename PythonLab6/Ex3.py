import re

def function3(myString,myExpressions):
    myList = []
    for expression in myExpressions:
        x = re.findall(expression, myString)[0]
        if x not in myList:
            myList.append(x)
    return myList

