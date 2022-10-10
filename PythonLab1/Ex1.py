def Euclid(a, b):
    while(a!=b):
        if(a>b):
            a=a-b
        elif(b>a):
            b=b-a
    return a

lst = []
n = int(input("Cate elemente: "))
  
for i in range(0, n):
    nr = int(input()) 
    lst.append(nr)
    if(i==2):
        c= int(Euclid(lst[0], lst[1]))
    elif(i>2):
        c= int(Euclid(lst[i], c))
print(c)