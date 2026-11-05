initial = float(input("Введите стартовое количество организмов: "))
percent = float(input("Введите среднесуточное увеличение в процентах: "))
days = int(input("Введите количество дней для размножения: "))

population = initial

for day in range(1, days + 1):
    if day == 1:
        population = float(initial)
    else:
        population += population * (percent / 100)
    print(f"День {day}:\n популяция: {int(population)}")