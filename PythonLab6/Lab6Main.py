from Ex1 import *
from Ex2 import *
from Ex3 import *
from Ex6 import *
from Ex7 import *
from Ex8 import *

if __name__ == "__main__":
    print("Ex1")

    myString="A word is defined as a sequence of alpha-numeric characters"
    print(function1(myString))

    print("Ex2")

    myString="A word is defined as a sequence of alpha-numeric characters"
    expression = r'\w+'
    x = 2
    print(function2(expression,myString ,x))

    print("Ex3")

    string = "A word is defined as a sequence of alpha-numeric characters"
    expressions = [r'\b[w]+\w+', r'\b[s]+\w+', r'\b[c]+\w+' , r'\b[a]+\w+']
    print(function3(string, expressions))

    print("Ex6")
    
    myString = "aeiou mancare castravete aluna om de zapada eoliana"
    print(function6(myString))

    print("Ex7")

    cnp = "5010115270019"
    print(function7(cnp))

    print("Ex8")

    print(function8("C:/Users/Ardeleanu Gabriel/Desktop/Facultate/Python/PythonLab6", r'Ex[0-9]+\.py'))