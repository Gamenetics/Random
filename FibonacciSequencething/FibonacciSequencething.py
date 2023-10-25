fibon = int(input("Enter fibonacci idek number u want e??? "))
second = answer = 0
first = 1
while answer < fibon:
    answer = first + second
    first = second
    second = answer
    print(answer)
