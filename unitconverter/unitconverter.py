import math
length = {"mm": 1,"cm": 2, "m":3,"km":4}
temp= ["c","f"]
vol = "ok"

units = {"length":length,"temp":temp,"volume":vol}
global rate
def lengthconvert(x,tar,value):
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
def tempconvert(x, tar,value):
   if x == tar:
      return value
   elif x == "c" and tar == "f":
      return f"{((value*9)/5)+32} Fahrenheit"
   elif x == "f" and tar == "c":
      return f"{((value-32)*5)/9} Celsius"
   else: 
      return "error"
def newinput(text, dict):
    value = input(text).lower()
    while value not in dict:
      if value == "":
        print("Value cannot be empty") 
      else: print("Error invalid")
      value = input(text).lower()
    return value

if 1 == 1:
    print("choose type length/temp")
    unittype = newinput("Unit type: ", units)
    unitdict = units[unittype]
    unit = newinput("Unit: ", unitdict)
    tarunit= newinput("New unit: ", unitdict)
    num = input("Value: ")
    while num == "" or num.isnumeric() == False:
      if num == "":
         print("Value cannot be empty") 
      elif num.isnumeric() == False:
         print("Value must be a number")
      num = input("Value: ")
    num = int(num)
    if unittype == "length":
       unitnum = unitdict[unit]
       unitnum2 = unitdict[tarunit]
       print(lengthconvert(unitnum,unitnum2,num))
    if unittype == "temp":
       print(tempconvert(unit,tarunit,num))