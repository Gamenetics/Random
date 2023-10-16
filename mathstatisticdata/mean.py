population = input("Mean calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
mean = 0
for num in population:
    mean += int(num)
mean/=size
print(population)
print("Mean: ",mean)