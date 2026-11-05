number = int(input("Введите число: "))

total_sum = 0
for i in range(1, number + 1):
    if i % 2 != 0:
        total_sum += i  ## Нечетные числа прибавляем
    else:
        total_sum -= i  ## Четные числа вычитаем

print(total_sum)