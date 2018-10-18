# Given an array of integers, we want the array to be sorted in non-decreasing order. Return the number of integers that are out-of-place from this sorted order.
#
# Ex: For [1,1,3,4,1] return 3 because there are 3 numbers out-of-place: 3,4,1
#
# Sorted: [1, 1, 1, 3, 4]
# 


a = [1,1,3,4,1]

def func(a):
    reversed = sorted(a)
    count = 0
    index = 0
    for i in reversed:
        if i != a[index]:
            count +=1
        index +=1
    return count

print(func(a))
 #3
