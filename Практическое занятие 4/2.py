from math import sqrt

def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

x1, y1 = map(float, input("Введите координаты x1, y1: ").split())
x2, y2 = map(float, input("Введите координаты x2, y2: ").split())

result = calculate_distance(x1, y1, x2, y2)

print(f"Евклидово расстояние: {result:.2f}")