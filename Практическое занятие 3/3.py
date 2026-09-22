num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    result = int(num1) + int(num2)
    print("The result is: ", result)
except ValueError:
    print("Please enter valid numbers")