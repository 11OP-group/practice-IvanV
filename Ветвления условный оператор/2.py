age = int(input("Введите ваш возраст: "))

if age < 18:
    print("Вы не проходите")
else:
    membership = input("Вы участник клуба (да / нет): ")

    if membership == "да":
        print("Вы проходите")
    else:
        document = input("У вас есть документы (да / нет): ")

        if document == "да":
            print("Вы проходите")
        else:
            print("Уходи")
