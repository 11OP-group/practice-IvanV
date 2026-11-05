NUM_TO_MULTIPLY = 1

while True:
    input_num = int(input("Введите число: "))

    if input_num < 0:
        break

    if input_num > 0:
        NUM_TO_MULTIPLY *= input_num

print("Результат произведения:", NUM_TO_MULTIPLY)