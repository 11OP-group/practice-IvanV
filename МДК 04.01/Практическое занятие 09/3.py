n = int(input("цена за услугу ведьмака: "))
count = 0

while n >= 25:
    n -= 25
    count += 1

while n >= 10:
    n -= 10
    count += 1

while n >= 5:
    n -= 5
    count += 1

while n >= 1:
    n -= 1
    count += 1

print(f"количество чеканных монет: {count}")