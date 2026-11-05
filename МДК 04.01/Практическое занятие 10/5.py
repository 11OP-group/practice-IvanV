START_BALANCE = 1000
balance = START_BALANCE

while True:
    print(f"{'-'*20}")
    print("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")
    print(f"{'-'*20}")
    
    choice = int(input("Выберите пункт меню: "))
    
    if choice == 1:
        print(f"Текущий баланс: {balance} руб.")
    elif choice == 2:
        if balance >= 100:
            balance -= 100
            print("Снято")
        else:
            print("Недостаточно средств")
    elif choice == 3:
        balance += 100
        print("Баланс пополнен на 100 руб")
    elif choice == 4:
        print("До свидания")
        break
    else:
        print("Неверная команда")