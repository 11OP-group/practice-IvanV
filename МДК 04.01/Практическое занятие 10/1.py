TRUE_PIN = 4590

while True:
    input_pin = int(input("Введите пин-код: "))
    if input_pin == TRUE_PIN:
        print("Доступ разрешён")
        break
    else:
        print("Ошибка, попробуйте ещё раз")