def function3(d1, d2):
    if(len(d1)!=len(d2)):
        return False
    for x in d1:
        if x in d2:
            if(d1[x] != d2[x]):
                return False
        else:
            return False
    return True






d1 = {'a':{'a':'1', 'b':'2', 'c':'3'}, 'b':'2', 'c':'3'}
d2 = {'a':{'a':'1', 'b':'2', 'c':'3'}, 'b':'2', 'c':'3'}



print(function3(d1,d2))