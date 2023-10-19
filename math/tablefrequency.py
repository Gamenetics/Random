print("Table frequency stuff calcualtor frfr")
data = {}

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
decimal = int(newinput("How many decimal places? "))
while True:
    newdata = input("Add new data type: ")
    if newdata.lower() == "":
        break
    else: 
        data[newdata] = int(newinput(f"Set value for {newdata}: "))
print(data)

total = 0
for x in data:
  total += data[x]

cumulativepercentage = 0
for x in sorted(data.items(), key=lambda x:x[1]):
  percent = round((x[1]/total)*100, decimal)
  cumulativepercentage += percent
  print(f"Percentage of {x[0]} [{x[1]}/{total}] {percent}% || Cumulative: {cumulativepercentage}%")
print("Total:", total)