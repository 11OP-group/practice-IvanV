import math

grad = float(input("Введите градусы: "))
rad = grad * math.pi / 180 # можно ещё так rad = math.radians(grad)

print(math.sin(rad) + math.cos(rad) + math.tan(rad) ** 2)