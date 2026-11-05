DISCOUNT = 10
all_price = 0

while True:
    price = int(input("Введите цену: "))
    
    if price == 0:
        break
    elif price < 0:
        print("Цена не может быть отрицательной")
        continue
    else:
        all_price += price

print(f"Общая стоимость товаров: {all_price}")

if all_price > 1000:
    all_price = all_price - (all_price * DISCOUNT / 100)
    print(f"Скидка {DISCOUNT}% применена")

print(f"Сумма к оплате: {int(all_price)} рублей")