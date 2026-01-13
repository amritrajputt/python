def fact(n):
    if(n == 1 or n == 0):
        return n
    return n * fact(n-1)
print(fact(5))