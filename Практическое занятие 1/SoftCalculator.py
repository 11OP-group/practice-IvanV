a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b

print(f"Result: {result}")