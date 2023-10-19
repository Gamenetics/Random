data = {}

print("Mode frequency mean calcualtor frfr")

def newinput(text, allownothing = False):
    value = input(text)
    if allownothing == True and value =="": return value
    while value == "" or value.isnumeric() == False:
      if value == "":
         print("Value cannot be empty")
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

print("type nothing when done")
while True:
    newdata = newinput("Add new score: ", True)
    if newdata == "":
        break
    else: 
        data[int(newdata)] = int(newinput(f"Set frequency for {newdata}: "))
print(data)

mode = []
for num in data: 
  if data[num] == data[max(data, key=data.get)]:
     mode.append(num)
print("Mode:", mode)