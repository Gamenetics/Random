import math
print("Standard deviation calculator v0.0.0.0.0.0.0.1")

def newinput(text):
    value = input(text)
    while value == "":
      if value == "":
         print("Value cannot be empty") 
      value = input(text)
    return value
population = newinput("Data: ").split()
size = len(population)
if size <= 1:
   print("Error low sample")
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
mean = 0
for num in population:
    mean += int(num)
mean/=size
result = 0
for num in population:
    result += (int(num)-mean)**2
#print(result2)
try:
  print("Mean: ",mean,"\nfinal answer model:sample =", math.sqrt(result/(size-1)), "\n")
  #print(result)
  print("final answer model:population =", math.sqrt(result/size))
except:
  print("errors frfr")