def fibonacci(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        return fibonacci(nr-2)+fibonacci(nr-1)
 
 
n = 7
for i in range(0, n):
    print(fibonacci(i))