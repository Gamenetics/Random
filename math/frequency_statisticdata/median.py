data = {}

print("Median frequency mean calcualtor frfr")

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
total = mean = 0
for num in data:
    total += data[num]
    mean += data[num]

cumulativepercentage = 0
print(total)
for num in sorted(data.items(), key=lambda x:x[1]):
  percent = round((num[1]/total)*100, 1)
  cumulativepercentage += percent
  print(f"Percentage of {num[0]} [{num[1]}/{total}] {percent}% || Cumulative: {cumulativepercentage}%")
datalist = []
for num in data:
   for x in range(0,data[num]):
    datalist.append(num)
print(datalist)
datalist.sort()
size = len(datalist)
if size % 2 != 0:
  print("The median is: ",datalist[int(size/2)])
else: 
  median = int(size/2)
  x = int(datalist[median])
  y = int(datalist[median-1])
  print("The median is: ",(x+y)/2)