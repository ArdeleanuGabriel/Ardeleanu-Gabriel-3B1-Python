def function2(string):
    dictionar = {}
    print(type(dictionar))
    for ch in string:
        if ch in dictionar:
            dictionar[ch] = dictionar[ch] + 1
        else:
            dictionar[ch] = 1
    return(dictionar)

myString = 'hipopotam'
print(function2(myString))