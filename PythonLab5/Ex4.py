def function4 (*args, **kwargs):
    myList = list()
    for x in args + (*kwargs.values(),) :
        if type(x) is dict:
            if len(x) >= 2:
                for y in x:
                    if len(str(y)) >= 3:
                        myList.append(x)
                        break
    return myList
