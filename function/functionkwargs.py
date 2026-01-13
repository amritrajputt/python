# def print_kwargs(name,power):
#     print("Name: ",name," power: ",power)

# print_kwargs(power="lazer",name="shaktiman")   
#i can define parameter value explicitly during passing parameter and then we can pass parameter in any sequence


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(power="lazer",name="shaktiman")  


