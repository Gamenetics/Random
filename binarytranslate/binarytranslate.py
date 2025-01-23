import math
def decimaltobinary(x):
     result = ""
     while x > 0:
        result += str(x % 2)
        x /= 2
        x = math.floor(x)
     return result [::-1]

def binarytodecimal(x):
     result = 0
     base = 1
     for digit in x:
       if int(digit) == 1:
           result+=base
       base*=2
     return result

while True:
    mode = int(input("Choose mode\n1: Binary > Decimal\n2: Decimal > Binary\nChoice: "))
    if mode == 2:          
        num = int(input("Translate into binary!: "))
        print(decimaltobinary(num))
    elif mode == 1:          
        num = input("Translate into Decimal!: ")
        print(binarytodecimal(num [::-1]))