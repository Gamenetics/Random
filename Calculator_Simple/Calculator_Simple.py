# A simple calculator to do basic operators
while True:
    l1=int(input("first: "))
    l2=int(input("second: "))
    type=input("type: ")
    if type == "+":
        result = l1 + l2
        print(l1,l2, l1+l2)
    elif type == "-":
        result = l1 - l2
    elif type == "/":
        result = l1 / l2
    elif type == "*":
        result = l1 * l2
    else: result = "ERROR"
    print(l1,   type   ,l2," = ", result)