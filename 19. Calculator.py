def calculator():
    print("Welcome to the calculator!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")

elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
elif operation == "/":
        print(f"The result of {num1} / {num2} is ", end="")
        if num2 != 0:
            result = num1 / num2
            print(result)
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")