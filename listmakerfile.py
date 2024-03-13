f = open("textlist.txt", "r")
result = ""
for line in f:
   for x in line.split():
      if x not in result:
         result += f"\"{x.strip()}\","
      else:
         print("Duplicate removed")
print(result)