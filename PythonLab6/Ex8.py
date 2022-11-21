import re
import os

def function8(path,regex):
    for root, dirs, files in os.walk(path):
        for file in files:
            if re.search(regex,file):
                print(">>" + file)
            else:
                print(file)