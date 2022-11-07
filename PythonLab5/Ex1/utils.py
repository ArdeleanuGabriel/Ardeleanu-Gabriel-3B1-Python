def process_item(x):
    while(1):
        prime = True
        for i in range(2,x):
            if x % i == 0:
                prime = False 
                break
        if prime == True:
            break
        x = x + 1
    return x


#a = input("Numar: ")
#a = int(a)
#print(process_item(a))