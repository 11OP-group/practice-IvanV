MIN_CELLS = 1
MAX_CELLS = 8

print("введите где будет стоять слон")

first_column, first_row = map(int,input("номер столбца и номер строки (через пробел): ").split())

print("введите клетку, куда будет перемещаться слон")

second_column, second_row = map(int, input("номер столбца и номер строки (через пробел): ").split())
if not (
    MIN_CELLS <= first_column <= MAX_CELLS
    and MIN_CELLS <= first_row <= MAX_CELLS
    and MIN_CELLS <= second_column <= MAX_CELLS
    and MIN_CELLS <= second_row <= MAX_CELLS
    ):
    print("фигура выходит за пределы доски")
else:
    if (first_column - second_column == first_row - second_row) or (first_column - second_column == second_row - first_row):
        print("слон может так ходить") ## YES
    else:
        print("слон не может так ходить") ## NO