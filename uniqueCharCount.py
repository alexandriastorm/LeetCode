a = "helllah" #4
b = "CodeU" #5
c = "Hello" #4

def uniqueCharacters(str):
    str = str.lower()
    seen = []
    count = 0
    for letter in str:
        if letter not in seen:
            count = count + 1
            seen.append(letter)
    return count

uniqueCharacters(b)
