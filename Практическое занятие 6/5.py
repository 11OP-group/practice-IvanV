MIN_CELLS = 1
MAX_CELLS = 8

first_column, first_row = map(int, input(f"Введите столбец и строку для ферзя (через пробел): ").split())
second_column, second_row = map(int, input(f"Введите столбец и строку для хода (через пробел): ").split())

if not (
    MIN_CELLS <= first_column <= MAX_CELLS
    and MIN_CELLS <= first_row <= MAX_CELLS
    and MIN_CELLS <= second_column <= MAX_CELLS
    and MIN_CELLS <= second_row <= MAX_CELLS
    ):
    print(f"какая-то из клеток выходит за пределы {MAX_CELLS}-{MAX_CELLS} доски")

else:
    if first_column == second_column and first_row == second_row:
        print("Ферзь не может остаться на месте")
    elif (
        first_column == second_column
        or first_row == second_row
        or (first_column - second_column) ** 2
        == (first_row - second_row) ** 2
    ):
        print("Ферзь может сделать этот ход")

    else:
        print("Ферзь не может сделать этот ход")