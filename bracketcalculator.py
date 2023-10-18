real = input("bracket stuff: ")
abracket = False
bracket = ""
operators = {"+":1,"-":2,"/":3,"*":4}
def operation(x, value, type):
    value=int(value)
    if type == 1:
        return x+value
    elif type == 2:
        return x-value
    elif type == 3:
        return x/value
    elif type == 4:
        return x*value
    else: return "ERROR3"

brackets = []

for a in real:
    if a == "(":
        abracket = True
        continue
    elif a == ")":
        abracket = False
        brackets.append(bracket)
        bracket = ""
    if abracket == True:
        #print(f"\"{a}\" is In bracket")
        if a in operators:
            bracket += f" {a} "
            continue
        bracket += a
if abracket == True:
    print("error1")
print(brackets)
for equation in brackets:
    result = 0
    type = 0
    equation = equation.split()
    print(equation)
    for a in equation:
        if a.isnumeric() == True:
            if type == 0:
                result = int(a)
                continue
            result = operation(result,a,type)
            type = 0
        elif a in operators:
            type = operators[a]
        else: print("error6")
    print(result)