class InvalidChai(Exception):pass

def bill (flavour,cups):
    menu = {"masala":10,"ginger":12,"lemon":15}
    try:
        if flavour not in menu:
            raise InvalidChai(f"Invalid chai flavour: {flavour}")
        if not isinstance(cups,int):
            raise TypeError(f"no of cups must be an integer")
        total = menu[flavour] * cups
        return total
    except InvalidChai as e:
        print(e)
    finally:
        print("thank you for your order")
    
print(bill("masala",2))
print(bill("chai",2))