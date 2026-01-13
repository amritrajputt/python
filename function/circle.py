import math

def circle_status(r):
    area = math.pi*r**2
    circumference = 2*math.pi*r
    return area,circumference

a,c = circle_status(3)
print(a)