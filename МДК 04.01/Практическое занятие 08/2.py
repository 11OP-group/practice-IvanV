for i in range(10):
    number = int(input("Введите число: "))
    if number % 2 != 0:
        print("NO") ## хотябы одно число нечетное
        break
else:
    print("YES") ## все числа четные