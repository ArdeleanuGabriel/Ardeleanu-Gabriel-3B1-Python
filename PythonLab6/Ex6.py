import re

def function6(string):
    myList = re.findall(r'\b[aeiou]+\w*[aeiou]+\b',string)
    retList=[]
    for cenzurat in myList:
        #for i in range(0,len(cenzurat), 2):
            #cenzurat = cenzurat[:i] + "*" + cenzurat[i+1:]
        cenzurat = re.sub(r'\b\w',"*", cenzurat)
        cenzurat = re.sub(r'[*]\w\w', "*" + "cenzurat[match index + 1]"  + "*",cenzurat)
        print(cenzurat)
        retList.append(cenzurat)
    return retList


# aluna a*u*a
