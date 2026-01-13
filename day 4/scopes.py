username = "chaiaurcode"
def func():
    username = "chai"
    print(username)    
print(username)    
func()


x = 99
# def func2(y):
#     z = x+y
#     return z
# res = func2(1)
# print(res)

# def func3():
#     x= 12
#     print(x)
# func3()   
# print(x)    

#CLOSURES 

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# res = f1()        
# res()


def outer():
    print("This is the outer function")
    def inner():
        print ("this is an inner function")
    inner()
outer()        