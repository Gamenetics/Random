def formatnum(num):
    return round(num*100,2)

def newinput(text):
    value = input(text)
    while value == "" or value.isnumeric() == False:
      if value == "":
         print("Value cannot be empty") 
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

print("  |x|nx\ny |-|-\nny|-|-")
xname = input("X Label? ")
yname = input("Y Label? ")
both = int(newinput("Both {xname} and {yname}: "))
ny = int(newinput(f"{xname} no {yname}: "))
nx = int(newinput(f"{yname} no {xname}: "))
none = int(newinput("None: "))
total = both+nx+ny+none
print("Total amount:",total)
allx = both+ny
ally = both+nx
print(f"Total {xname}:",allx) 
print(f"Total {yname}:",ally)
print(f"Total {xname} without {yname}:",ny)
print(f"Total {yname} without {xname}:",nx)
print(f"Percentage of {xname}:", formatnum(allx/total))
print(f"Percentage of {yname}:", formatnum(ally/total))
print(f"Percentage of {xname} not {yname}:", formatnum(ny/allx))
print(f"Percentage of {yname} not {xname}:", formatnum(nx/ally))
print(f"Percentage of {xname} with {yname}:", formatnum(both/allx))
print(f"Percentage of {yname} with {xname}:", formatnum(both/ally))
print("Percentage of none:", formatnum(none/total))
'''-|x|nx
y
ny'''
