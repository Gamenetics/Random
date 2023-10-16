import math
population = input("Statisical data math idek calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
numbers = {}
for num in population:
    key = str(num)
    if key in numbers:
       numbers[key] = 1+numbers[key]
    else:
       numbers[key] = 1
mean = 0
for num in population:
    mean += int(num)
mean/=size
result = 0
for num in population:
    result += (int(num)-mean)**2
if size % 2 != 0:
  print(population[int(size/2)])
else: 
  median = int(size/2)
  x = int(population[median])
  y = int(population[median-1])
  print("The mean is:",(x+y)/2)
mode = []
for num in numbers: 
  if numbers[num] == numbers[max(numbers, key=numbers.get)]:
     mode += str(num)
print("Mode:", mode)
print("Mean:",mean,"\nfinal answer model:sample =", math.sqrt(result/(size-1)), "\n")
print("final answer model:population =", math.sqrt(result/size))