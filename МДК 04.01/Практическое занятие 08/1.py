n = int(input("Введите натуральное число от 1 до 10: "))

print(f"\nТаблица умножения на {n}:\n")
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")