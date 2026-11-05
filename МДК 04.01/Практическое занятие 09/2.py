ALEXANDRA = ('Александра', 'александра', 'Alexandra', 'alexandra')
LEVON = ('Левон', 'левон', 'Levon', 'levon')

found_alexandra = False
count = 0

name = input("Введите имена людей в очереди: ")

while name not in LEVON:
    if name in ALEXANDRA:
        found_alexandra = True
    elif found_alexandra:
        count += 1

    name = input()

print(f"количество человек между александрой и левоном: {count}")