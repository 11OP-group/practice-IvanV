total_numbers = int(input("Введите количество элементов: "))

first_max = int(input("1 - Введите число: "))
second_max = int(input("2 - Введите число: "))

## замена на случай если первое число меньше второго
if first_max < second_max:
    first_max, second_max = second_max, first_max

for i in range(total_numbers - 2):
    current_num = int(input(f"{i + 3} - Введите число: "))
    
    if current_num > first_max:
        second_max = first_max
        first_max = current_num
        
    elif current_num > second_max:
        second_max = current_num

print(f"Максимальное число: {first_max}")
print(f"Второе по величине число: {second_max}")