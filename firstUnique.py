#Input: ['a', 'a', 'a', 'a', 'c', 'c', 'b', 'b', 'd', 'e', 'f']
#Output: 'd'.

#Input: [‘a’]
#Output: ‘a’


#Input: [‘a’, ‘a’]
#Output: null

def firstUnique(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for item in lst:
        if counts[item] == 1:
            return item
    return None

list = ['a', 'a', 'a', 'a', 'c', 'c', 'b', 'b', 'd', 'e', 'f']
firstUnique(list)
