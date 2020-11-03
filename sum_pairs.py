# Determine if the target sum exists as a pair of two elements in an array.
# Inputs may exceed 10,000,000.

def sum_pairs(ints, s):
    #Looks like O(n**2) will time out. Can't use a nested for loop.
    cache = set()
    for i in range(len(ints)):
        diff = s - ints[i]
        if diff in cache:
            return [diff, ints[i]]
        cache.add(ints[i])