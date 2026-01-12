chai = {"healthy" : "herbal" , "spicy" : "masala", "zesty" : "ginger"}
print(chai)

print(chai["healthy"])

print(chai.get("spicy"))

chai["spicy"] = "spices"
print(chai)

chai["spicy"] = "masala"
print(chai)

for t in chai:
    print(t) # return only value not keys
    
for t in chai:
   # return keys values both
    print(t,chai[t])

for key,value in chai.items():
    print(key,value)   # return keys values both 

if "spicy" in chai: # loop on keys not on values
    print("i have masala chai")

print(len(chai))    # 3 item starts with 1 not with 0 like list

chai ["earl grey"] = "citrus"
print(chai)

chai.pop("earl grey") #needs key
print(chai)

chai.popitem() #pop last item
print(chai)

del chai["healthy"] # del works on list also it deletes from memory reference
print(chai)

chai_copy = chai.copy() # create new dictonary not only takes reference
print(chai_copy)


# NESTED DICTIONARY (give name of each nested dictionary)
tea_shop = {
    "chai" : {"masala" : "spicy","ginger" : "zesty"},
    "tea" : {"green" : "mild" , "black" : "strong"}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["ginger"])


#DICTIONARY COMPREHENSION
squared_nums = {x:x**2 for x in range(6)}
print(squared_nums)

squared_nums.clear() # remove all values from dictioanry

keys = ["ginger" , "masala" , "lemon"]
default_value = "delicious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)


new_dict = dict.fromkeys(keys,keys) #for each key whole dict is assigned as value
print(new_dict)