n = int(input("enter the number: "))
sumeven = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sumeven += i
print(sumeven)   