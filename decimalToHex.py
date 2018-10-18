#Recursive solution
#Decimal n converted to hex

def decimalToHex(n):
    if (n < 0): #negatives are
        print(0)
    elif (n <= 1):
        print(n)
    else:
        decimalToHex(n / 16) #recurisve call 
        x = (n % 16)
        if (x < 10):
            print(x),
        if (x == 10):
            print("A"),
        if (x == 11):
            print("B"),
        if (x == 12):
            print("C"),
        if (x == 13):
            print("D"),
        if (x == 14):
            print("E"),
        if (x == 15):
            print ("F"),
