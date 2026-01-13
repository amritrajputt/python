s = input("enter string: ")
for c in s:
    if s.count(c) == 1:
        print("result is: ", c)
        break    