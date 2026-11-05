MAX_GRADE = 5

print("Начните вводить оценки):")
grade = int(input())
count_fives = 0

while 1 <= grade <= MAX_GRADE:
    if grade == MAX_GRADE:
        count_fives += 1
    grade = int(input())

print(f"Количество пятёрок: {count_fives}")