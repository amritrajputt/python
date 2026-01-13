# write a generator fun that yield even no. up to a specified limits
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield(i)
for num in even_generator(10):
    print(num)

# 2. yield (Generator function)

# Returns values one at a time

# Function pauses, does NOT terminate

# Function state is saved (variables, loop position, execution point)

# Can resume from the exact previous state

# Uses lazy evaluation

# Memory efficient (O(1) extra space)



# Example:

 #Movie story

# You start watching a movie.

# You watch 30 minutes

# You pause the movie and go do some work

# Later, you come back

# You press play again

# The movie starts exactly from where you paused, not from the beginning

# This is exactly how yield works.