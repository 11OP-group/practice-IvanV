first_num = int(input("Введите первое число: "))

while True:
    second_num = int(input("Введите второе число: "))
    
    if second_num > first_num:
        break
    print("ошибка")

while True:
    third_num = int(input("Введите третье число: "))
    
    if third_num > second_num:
        break
    print("ошибка")

print("Последовательность принята")