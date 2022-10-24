def function9(*lst, **arguments):
    c=0
    for x in arguments:
        if arguments[x] in lst:
            c = c +1
    return c

print(function9(1, 2, 3, 4, x=1, y=2, z=3, w=5))