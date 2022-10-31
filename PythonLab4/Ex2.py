import os

def function2(director , fisier):
    y = open(fisier, "w")
    dirs = os.listdir(director)
    for file in dirs:
        x = os.path.abspath(file)
        if file.startswith("a") or file.startswith("A"):
            y.write( x  + "\n")
    y.close()
    

function2("C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab4/Ex1Folder", "C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab4/Ex2.txt")


