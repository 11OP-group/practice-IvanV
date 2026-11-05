n = int(input("Введите число: "))

print_number = 1

while print_number <= n:

    if (5 <= print_number <= 9) or (17 <= print_number <= 37) or (78 <= print_number <= 87):
        print_number += 1
        continue
    
    print(f"{print_number}")
    print_number += 1