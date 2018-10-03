import math
a = 1 # 1
b = 2 # 1, 2
c = 4 # 1, 2, 4
d = 10 # 1, 2, 5, 10
def getFactors(num):
    factors = []
    if num == 0 or num == 1:
        return [num]

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i not in factors:
                factors.append(i)
                if (num // i) != i:
                    factors.append(num // i)
    factors.sort()
    return factors

getFactors(d)


#n / 2 runtime
