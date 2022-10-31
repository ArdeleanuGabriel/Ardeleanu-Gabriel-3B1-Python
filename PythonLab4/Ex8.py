import os

def function8(dir_path):
    dirs = os.listdir(dir_path)
    x=list()
    for file in dirs:
        y = os.path.abspath(file)
        if os.path.isfile( os.path.join(dir_path,file)):
            x.append(y)
    return(x)

print(function8("C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab4/Ex1Folder"))