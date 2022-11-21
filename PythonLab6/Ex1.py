import re

def function1(string):
    myList=re.findall(r'\b\w+\b',string)
    return myList


