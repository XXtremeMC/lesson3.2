num1 = int(input("Enter number: "))
num2 = (input("Operator: "))
num3 = int(input("Enter number: "))

if num2 == "+":
    result = num1 + num3
    print(result)
elif num2 == "-":
    result = num1 - num3
    print(result)
elif num2 == "*":
    result = num1 * num3
    print(result)
elif num2 == "/":
    if num3 == 0:
        print("Not divisible by zero")
    else:
        result = num1 / num3
        print(result)
else:
    print("Error")

