num_one = int(input("Please enter a number: "))
num_two = int(input("Please enter another number: "))

operator = input("Enter an operator (+, -, /, *): ")


def calculate(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        return x / y
    elif operator == "*":
        return x * y
    else:
        return "Invalid operator entered"


result = calculate(num_one, num_two, operator)
print("The result is:", result)
