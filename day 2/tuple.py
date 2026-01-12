#immutable
tea = ("black", "green", "oolong")
print(tea)
print(tea[0])
print(tea)
print(len(tea))
 
more_tea = ("herbal","healthy")
all_tea = tea + more_tea
print(all_tea)

if "green" in all_tea:
    print("i have green tea")

more_tea = ("herbal","earl grey","herbal")
print(more_tea.count("herbal"))    

(black,green, oolong) = tea # these are treated as variable for tea items

print(type(tea))

# NESTED TUPLES is also possible

t = (1,2,(3,4))
(a,b,c) = t
print(c)