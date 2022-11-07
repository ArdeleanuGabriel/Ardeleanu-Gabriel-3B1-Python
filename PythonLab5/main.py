from Ex2 import *
from Ex3 import *
from Ex4 import *
from Ex5 import *
from Ex6 import *
from Ex7 import *
from Ex8 import *
from Ex9 import *

print("Ex2")
print("Anonymous: " + str(  (lambda *args, **kwargs : sum ( args + (*kwargs.values(),) )  )  (1, 2, c=3, d=4)  )  )
print("Function2: " + str(function2(1, 2, c=3, d=4)))
print("Ex3")
print("Function: " + str(vowels_NF))
print("Anonymous function: " + str(vowels_AF))
print("List Comprehension: " + str(vowels_LC))
print("Ex4")
print(function4(

 {1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}

))
print("Ex5")
print(function5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
print("Ex6")
print(function6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
print("Ex7")
print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    offset=2,
    limit=2
)
)
print("Ex8")

def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
print(x)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
print(x)


print("Ex9")
print(function9([(5, 2), (19, 1), (30, 6), (2, 2)]))