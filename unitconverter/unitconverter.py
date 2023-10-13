import math
units= {"mm": 1,"cm": 2, "m":3,"km":4}
def rateconvert(x,tar,value):
    global rate
    while x != tar:
        print(x-tar < 0)
        if x-tar < 0:
            rate = 10 **(x)
            print(value,rate,x)
            value/=rate
            x+=1
        if x-tar > 0:
            rate = 10 **(x-1)
            value*=rate
            x-=1
    return(math.floor(value))

while True:
    unit = input("Unit: ")
    tarunit= input("New unit: ")
    num = int(input("Value: "))
    unitnum = units[unit]
    unitnum2 = units[tarunit]
    print(unitnum,unitnum2,num)
    print(rateconvert(unitnum,unitnum2,num))

    