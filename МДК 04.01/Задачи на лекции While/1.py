print("Начните вводить слова через shift + Enter\n(для завершения введите 'стоп', 'хватит' или 'достаточно'):")
words = input().lower()
count = 0

while words != "стоп" and words != "хватит" and words != "достаточно":
    count += 1
    words = input().lower()

print(f"Вы ввели {count} слов")