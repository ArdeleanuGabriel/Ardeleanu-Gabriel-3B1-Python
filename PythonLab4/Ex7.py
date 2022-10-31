import os
import pathlib

def function7(str):
    dictionar = dict()
    dictionar["full_path"] = os.path.abspath(str)
    dictionar["file_size"] = os.path.getsize(str)
    dictionar["file_extension"] = os.path.splitext(str)[1]
    dictionar["can_read"] = os.access(str, os.R_OK)
    dictionar["can_write"] = os.access(str, os.W_OK)
    return dictionar
    
print(function7("Ex3.txt"))