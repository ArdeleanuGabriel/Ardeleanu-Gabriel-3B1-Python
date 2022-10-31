import os

def function5(target, to_search):
    lst = []
    try:
        if os.path.isfile(target):
            with open(target, "r") as f:
                try:
                    for linie in f:
                        if to_search in linie:
                            lst.append(target)
                            break
                except UnicodeDecodeError:
                    pass
        elif os.path.isdir(target):
            for root, dirs, files in os.walk(target):
                for file in files:
                    with open(os.path.join(root, file), "r") as f:
                        try:
                            for linie in f:
                                if to_search in linie:
                                    lst.append(os.path.join(root, file))
                                    break
                        except UnicodeDecodeError:
                            pass
        else:
            raise ValueError("Nu este fisier sau director")
    except ValueError as e:
        return e
    else:
        return lst

print( function5 ("C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab4/Ex1Folder" , "ALUNE"))