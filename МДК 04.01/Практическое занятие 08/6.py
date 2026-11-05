import random

MIN_NUMBER = 1
MAX_NUMBER = 10
MAX_ATTEMPTS = 3

number = random.randint(MIN_NUMBER, MAX_NUMBER)

print(f"Загадали число от {MIN_NUMBER} до {MAX_NUMBER}. У вас {MAX_ATTEMPTS} попытки")

for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"\nПопытка номер {attempt}")
    guess = int(input("Введите число: "))
    if guess == number:
        print("Угадали")
        break
    elif guess < number:
        print("Неверно, загаданное число больше")
    else:
        print("Неверно, загаданное число меньше")
else:
    print(f"Вы проиграли. Загаданное число - {number}")