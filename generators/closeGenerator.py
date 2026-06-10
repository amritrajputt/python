def localChai():
    yield "masala chai"
    yield "ginger chai"

def imported_chai():
    yield "match"
    yield "oolong"

def full_menu():
    yield from localChai()
    yield from imported_chai()    

for chai in full_menu():
    print(chai) 

def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
    except:
        print("stall closed")
stall = chai_stall()
print(next(stall))
stall.close() 