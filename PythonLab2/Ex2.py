def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 ) :
            return False
        i = i + 1
    return True

lst = []
lst_prime = []
n = int(input("Enter number of numbers: "))
  
for i in range(0, n):
    nr = int(input())
    lst.append(nr)
    if(isPrime(nr) == True):
        lst_prime.append(nr)

print(lst_prime)
      