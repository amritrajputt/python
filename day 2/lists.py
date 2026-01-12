tea = ['herbal','milk','oolong']
print(tea[1:2])

tea[2] = 'lemon'
print(tea)

# tea[1:2] = 'lemon'
# print(tea)

tea[1:2] = ['lemnon']
print(tea)

tea [1:3] = ["ginger","tulsileaf"]
print(tea)

print(tea[1:1]) 
tea [1:1] = ["hei","hy"] #(add 'hei' then 'hy' at 1 index )
print(tea)

tea[1:3] = [] #treated as delete operation from 1-2 (3 not included)
print(tea)

for t in tea:
    print(t)
    if(t is 'herbal'):
        print("herbal is there")
        break

for type in tea:
    print(type,end="-")

if "ginger" in tea:
    print('ginger is there')


tea.append("masala")    
print(tea)

tea.pop()
print(tea)


tea.remove('tulsileaf')
print(tea)

tea.insert(1,"gingertea")
print(tea)

tea_type = tea.copy() #copy tea data but memory reference are different tea_type create new list of same value
print(tea_type)

# LIST COMPREHENSION
 
squared_num = [x**2  for x in range(10)]
print(squared_num) # list of squared num from range 0-9

squared_num = [x**3 if(x == 3) else x**2 for x in range(10)]
print(squared_num) # list of squared num from range 0-9 but 3 is cubed

squared_num = [x**2 if(x == 3) else x**3 for x in range(10)]
print(squared_num) # list of squared num from range 0-9 but from 3 every no is cubed