f = open("teagwag.txt", "r")
result = ""
for line in f:
   for x in line.split():
      result += f"\"{x.strip()}\","
print(result + "\n\n\n\n\n")