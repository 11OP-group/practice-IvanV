MIN_POCKET = 0
MAX_POCKET = 36

number_on_roulette = int(input("Введите номер на рулетке: "))

if number_on_roulette < MIN_POCKET or number_on_roulette > MAX_POCKET:
    print("Номер должен быть от 0 до 36")
elif number_on_roulette == 0:
    print(f"ваш номер {number_on_roulette} зеленый")
elif (1 <= number_on_roulette <= 10 or 19 <= number_on_roulette <= 28) and number_on_roulette % 2 == 1:
    print(f"ваш номер {number_on_roulette} красный")
elif (11 <= number_on_roulette <= 18 or 29 <= number_on_roulette <= 36) and number_on_roulette % 2 == 0:
    print(f"ваш номер {number_on_roulette} красный")
else:
    print(f"ваш номер {number_on_roulette} черный")