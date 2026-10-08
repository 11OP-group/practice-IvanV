MIN_CELLS = 1
MAX_CELLS = 8

first_column, first_row = map(int,input("Введите номер столбца и номер строки (через пробел): ").split())
second_column, second_row = map(int, input("Введите номер столбца и номер строки (через пробел): ").split())

first_color = (first_column + first_row) % 2
second_color = (second_column + second_row) % 2

if not (
    MIN_CELLS <= first_column <= MAX_CELLS
    and MIN_CELLS <= first_row <= MAX_CELLS
    and MIN_CELLS <= second_column <= MAX_CELLS
    and MIN_CELLS <= second_row <= MAX_CELLS
    ):
    print("какая-то клетка выходит за пределы доски")
else:
    if first_color == second_color:
        print("Цвет клеток одинаковый") ## YES
    else:
        print("Цвет клеток разный") ## NO