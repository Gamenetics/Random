data = {}
datainput = False

def newinput(text):
    value = input(text)
    while value == "" or value.isnumeric() == False:
      if value == "":
         print("Value cannot be empty") 
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

print("type nothing when done")
decimal = int(input("How many decimal places? "))
while datainput != True:
    newdata = input("Add new data type: ")
    if newdata.lower() == "":
        datainput = True
        break
    else: 
        data[newdata] = int(newinput(f"Set value for {newdata}: "))
print(data)
total = 0
for x in data:
  total += data[x]
print("Total: ", total)
for x in data:
  print(f"Percentage of {x} [{data[x]}/{total}] {round((data[x]/total)*100, decimal)}%")