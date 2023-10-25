currentnum = 2

def primeCheck(x):
    if x % 2 == 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True
def newPrime(num):
    while True:
        if not primeCheck(num):
            num += 1
        else:
            return num
        
while True:
    if input("Do you want to see next prime number? [Y/N] ").lower() == "y":
        print(currentnum, " is a prime number")   
        currentnum = newPrime(currentnum + 1)   
    else:
        break