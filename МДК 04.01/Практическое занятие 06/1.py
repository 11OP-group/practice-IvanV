temperature = float(input("Температура в градусах Цельсия: "))
pressure = float(input("Верхнее давление: "))
pulse = float(input("Пульс - удары в минуту: "))

if (temperature < 35 or temperature > 38) or (pressure < 105 or pressure > 140) or (pulse < 55 or pulse > 110):
    print(f"Требуется врач. Ваши показатели: температура {temperature}, давление {pressure}, пульс {pulse}")

elif (36 <= temperature <= 37) and (110 <= pressure <= 130) and (60 <= pulse <= 100):
    print(f"Нормальное состояние. Ваши показатели: температура {temperature}, давление {pressure}, пульс {pulse}")

else:
    print(f"Легкое недомогание. Ваши показатели: температура {temperature}, давление {pressure}, пульс {pulse}")