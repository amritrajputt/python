# write a generator fun that yield even no. up to a specified limits
def even_generator(limit):
    for i in range(2,limit+1,2):
        print(i)
print(even_generator(5))        