cost = int(input("Cost: "))
payment = int(input("Amount given: "))
change = payment - cost
def calchange(x):
    dollar2 = dollar1 = 0
    print(x)
    while x > 0:
        if x > 1:
            x-=2
            print("2",x)
            dollar2 += 1
        if x > 0:
            x-=1
            print("1",x)
            dollar1 += 1
        
    return dollar2, dollar1, "lol"
        
print("Change required: ", change)
stuff = calchange(change)
print(stuff)

