import math
population = input("Median calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
print(population)
if size % 2 != 0:
  print(population[int(size/2)])
else: 
  median = int(size/2)
  x = int(population[median])
  y = int(population[median-1])
  print("The mean is: ",(x+y)/2)