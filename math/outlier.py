import math
population = input("Standard deviation calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
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
deviation= math.sqrt(result/(size-1))
print("Mean: ",mean,"\nfinal answer model:sample =", deviation, "\n")
#print(result)
print("final answer model:population =", math.sqrt(result/size))

'''for x in population:
   z=(x-mean)/deviation
   if z > 3 or z < 3:
      print("outlier", x)'''