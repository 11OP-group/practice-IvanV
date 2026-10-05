def calculate_bmi(weight, height):
    """
    Вычисляет индекс массы тела через рост и вес
    и возвращает готовое значение ИМТ
    """
    return weight / height ** 2

weight, height = map(float, input("Введите свой вес и рост в метрах: ").split())
bmi = calculate_bmi(weight, height)
print(f"Индекс массы тела равен: {bmi:.1f}")
