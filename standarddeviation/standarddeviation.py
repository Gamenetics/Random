import math
population = input("Standard deviation calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
mean = 0
for num in population:
    mean += int(num)
mean/=size
result = 0
for num in population:
    result += (int(num)-mean)**2
#print(result2)
print("final answer model:sample =", math.sqrt(result/(size-1)), "\n")
#print(result)
print("final answer model:population =", math.sqrt(result/size))

