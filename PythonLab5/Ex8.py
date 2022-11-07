def print_arguments(function):
    def miniFunct(*args, **kwargs):
        return function(*args,**kwargs)
        #return function(*args,**kwargs) * 2 pentru b)
    return miniFunct