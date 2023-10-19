data = input("data: ").split()
base = {}
total = 0
for a in data:
    total += 1
    if a in base:
        base[a] = 1 + base[a]
    else: base[a] = 1
print(base)
print(total)