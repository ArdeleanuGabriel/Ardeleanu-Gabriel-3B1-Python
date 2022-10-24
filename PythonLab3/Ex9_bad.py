def function9(lst):
    pos_lst=[]
    c=0
    for x in lst:
        if '=' not in str(x):
            pos_lst.append(x)
        else:
            y = str(x).partition('=')
            if int(y[2]) in pos_lst:
                c = c + 1
    return c


lst = [1, 2, 3, 4, 'x=1', 'y=2', 'z=3', 'w=5']

print(function9(lst))