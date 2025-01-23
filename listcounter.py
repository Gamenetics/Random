f = open("textlist.txt", "r")
result = []
items = []
for line in f:
    if line.replace("\n","") not in items:
         items.append(line.replace("\n",""))
         result.append(0)
print(result)

'''f = open("textlist.txt", "r")
result = []
items = []
for line in f:
   for x in line.split():
      if line not in items:
         items.append(line)
         result.append(0)
print(result)'''