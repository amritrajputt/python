n = int(input("enter number: "))
isPrime = True
if n > 1:
    for i in range(2,n):
        if (n % 2) == 0:
            isPrime = False
            break
print(isPrime)        
