f = open("textlist.txt", "r")
result = ""
for line in f:
   if f"\"{line.strip()}\"," not in result:
      result += f"\"{line.strip()}\","
print(result)
f = open("textlist.txt", "r")
result = []
items = []
for line in f:
    if line.replace("\n","") not in items:
         items.append(line.replace("\n",""))
         result.append(0)
print(result)
#Use for multi words on line
'''f = open("textlist.txt", "r")
result = ""
for line in f:
   for x in line.split():
      if x not in result:
         result += f"\"{x.strip()}\","
print(result)'''