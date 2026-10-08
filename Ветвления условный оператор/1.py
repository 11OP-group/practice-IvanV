points = int(input("Введите количество баллов: "))

if not (0 <= points <= 100):
    print("некорректное значение баллов")
elif points >= 90:
    print("Ваша оценка 5")
elif points >= 75 < 90:
    print("Ваша оценка 4")
elif points >= 60 < 75:
    print("Ваша оценка 3")
else:
    print("Ваша оценка 2")

print("результат записан")