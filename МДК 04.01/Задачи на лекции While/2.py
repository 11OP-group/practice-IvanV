SEVEN = 7
SEPARATOR = ","

print(f"Введите числа через shift + Enter\n(для завершения введите число, не делящееся на {SEVEN}):")
num = int(input())
result = ""

while num % SEVEN == 0 and num != 0:
    result += str(num) + SEPARATOR
    num = int(input())

if result == "":
    print(f"Числа, делящиеся на {SEVEN}: 0 чисел")
else:
    result = result[:-len(SEPARATOR)]
    print(f"Числа, делящиеся на {SEVEN}: {result}")