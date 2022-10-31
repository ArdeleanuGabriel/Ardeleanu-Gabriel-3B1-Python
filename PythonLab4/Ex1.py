import os

def function1(director ):
    dirs = os.listdir(director)
    mySet = set()
    for file in dirs:
        if os.path.isfile( os.path.join(director,file)):
            mySet.add(os.path.splitext(file)[1])
    myList = list(mySet)
    myList.sort()
    print(myList)

function1( "C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab4/Ex1Folder" )