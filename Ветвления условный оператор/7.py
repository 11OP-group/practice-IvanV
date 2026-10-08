color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color1 not in ["красный", "синий", "жёлтый"] or color2 not in ["красный", "синий", "жёлтый"]:
    print("Введите корректный цвет")
elif color1 == color2:
    print(color1)
elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("фиолетовый")
elif (color1 == "красный" and color2 == "жёлтый") or (color1 == "жёлтый" and color2 == "красный"):
    print("оранжевый")
else:
    print("зелёный")