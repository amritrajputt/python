#method resolution order
class A:
    label = "A: Base class"
class B(A):
    label = "B: Masala blend"
class C(A):
    label = "C: Herbal blend"        

class D(B,C): # multiple inheritance but printed only the 1st argument method or print statement
    pass


cup = D()
print(cup.label)
print(D.__mro__)