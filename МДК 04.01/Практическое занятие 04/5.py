minutes = int(input("Введите количество минут: "))

hours = minutes // 60
remains = minutes % 60

print(f"{minutes} минуты - это {hours} час {remains} минут")