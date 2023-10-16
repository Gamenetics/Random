population = input("Mode calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
print(population)
numbers = {}
for num in population:
    key = num
    if key in numbers:
       numbers[key] = 1+numbers[key]
    else:
       numbers[key] = 1
#print(population)
#print(numbers)
mode = []
for num in numbers: 
  if numbers[num] == numbers[max(numbers, key=numbers.get)]:
     mode += str(num)
print("Mode:", mode)