def process(**kwargs):
    myList = fibonacci(1000)
    return1_list=list()
    for i in kwargs:
        if i == "filters":
            for nr in range(1000):
                filter_results = [filtru(myList[nr]) for filtru in kwargs[i]]
                if all(filter_results):
                    return1_list.append(myList[nr])
        if i == "offset":
            for y in range(kwargs[i]):
                return1_list.pop(0)
        elif i == "limit":
            return2_list = list()
            for y in range(kwargs[i]):
                return2_list.append(return1_list[y])
            return return2_list
    return myList


def fibonacci(n):
    myList = list()
    myList.append(0)
    myList.append(1)
    for i in range(2,n):
        myList.append(myList[i-1] + myList[i-2])
    return myList

def sum_digits(x):
    return sum(map(int, str(x)))

