CORRECT_PASSWORD = "admin"
MAX_COUNT = 3
count = 0

while True:
    input_password = input("Введите пароль: ")

    if input_password == CORRECT_PASSWORD:
        print("Доступ разрешён")
        break
    else:
        count += 1
        if count == MAX_COUNT:
            print("Система заблокирована")
            break