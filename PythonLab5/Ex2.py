def function2(*args, **kwargs):
    s=0
    for i in args:
        s = s + i
    for i in kwargs.values():
        s = s + i
    return s
