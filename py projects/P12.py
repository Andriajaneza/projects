import time

def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, :): ")
        num2 = float(input("Enter the second number: "))

        time.sleep(0.5)

        if operator == '+':
            print("Result:", num1 + num2)
        elif operator == '-':
            print("Result:", num1 - num2)
        elif operator == '*':
            print("Result:", num1 * num2)
        elif operator == ':':
            print("Result:", num1 / num2)
        else:
            print("Invalid operator")
        time.sleep(1.2)

calculator()
