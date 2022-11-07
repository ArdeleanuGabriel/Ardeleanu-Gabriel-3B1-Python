string = "Programming in Python is fun"
def vowels_function(MyString):
    MyList = list()
    for x in MyString:
        if x.lower() in "aeiou":
            MyList.append(x.lower())
    return MyList
vowels_NF = list(vowels_function(string))
vowels_AF = list(filter(lambda x: x.lower() in 'aeiou', string))
vowels_LC = [x.lower() for x in string if x.lower() in "aeiou" ]
