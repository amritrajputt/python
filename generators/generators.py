# generators saves meamory 
# you dont want the result immediately
# lazy evaluation
# yield pause the function and resume from exact point where it leaves before 

def serve_chai():
    yield "cup 1: masala chai "
    yield "cup 2: ginger chai "
    yield "cup 3: green tead "
stall = serve_chai()   

for cup in stall:
    print(cup)

def get_chai_list():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
chai = get_chai_list()
print(chai) #give object reference
print(next(chai)) # op:- cup 1 and yeild remember where did leaves before
print(next(chai)) # op:- cup2
print(next(chai)) # op:- cup3