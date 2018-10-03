#Given an ascending sorted array of ints,
#write an algorithm  to push all the duplicates to the back

def pushDuplicates(S):
    prev = ""
    copy = S
    end = []
    for i in copy:
        if i == prev:
            S.remove(i)
            end.append(i)
        prev = i
    S.extend(end)
    return S

S = [1,2,2,4,5,5]
print(pushDuplicates(S))
