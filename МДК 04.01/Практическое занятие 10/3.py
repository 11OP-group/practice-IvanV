search_max_num = 0

while True:
    num = int(input("Введите число: "))
    
    if num == 0:
        break
        
    if num > search_max_num and num > 1:
        search_max_num = num

print(f"Максимальное число - {search_max_num}")