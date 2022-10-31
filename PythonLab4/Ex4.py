import sys
import os

def function1(director ):
    dirs = os.listdir(director)
    mySet = set()
    for file in dirs:
        if os.path.splitext(file)[1] != "":
            mySet.add(os.path.splitext(file)[1])
    myList = list(mySet)
    myList.sort()
    print(myList)

function1( sys.argv[1] )

#"C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab4/Ex1Folder"