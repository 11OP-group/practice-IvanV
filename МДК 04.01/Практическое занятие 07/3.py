## Константы для цен напитков и скидок

PRICE_COFFEE = 120
PRICE_TEA = 80
PRICE_JUICE = 100
PRICE_WATER = 50
PRICE_LEMONADE = 90

#константы для скидок

DISCOUNT_STUDENT = 20
DISCOUNT_VIP = 15

## вывод меню

print(
    "☕ Меню кафе:\n"
    f"1. Кофе ☕ - {PRICE_COFFEE} руб\n"
    f"2. Чай 🍵 - {PRICE_TEA} руб\n"
    f"3. Сок 🧃 - {PRICE_JUICE} руб\n"
    f"4. Вода 🥤 - {PRICE_WATER} руб\n"
    f"5. Лимонад 🍹 - {PRICE_LEMONADE} руб\n"
)

drink = input("Введите номер напитка или его название: ")

match drink:
    case "1" | "кофе":
        name, emoji, price = "Кофе", "☕", PRICE_COFFEE

    case "2" | "чай":
        name, emoji, price = "Чай", "🍵", PRICE_TEA

    case "3" | "сок":
        name, emoji, price = "Сок", "🧃", PRICE_JUICE

    case "4" | "вода":
        name, emoji, price = "Вода", "🥤", PRICE_WATER

    case "5" | "лимонад":
        name, emoji, price = "Лимонад", "🍹", PRICE_LEMONADE

    case _:
        name = "invalid_drink"

if name == "invalid_drink":  ## проверка на ошибку в выборе напитка
    print(f'Напитка "{drink}" нет в меню')
    exit()

number_of_servings = int(input("Введите количество порций: "))

promo_code = input("Введите промокод (если его нет, просто нажмите Enter): ").strip().upper()

match promo_code:
    case "":
        discount_percent = 0

    case "STUDENT":
        discount_percent = DISCOUNT_STUDENT

    case "VIP":
        discount_percent = DISCOUNT_VIP

    case _:
        print(f'Промокод "{promo_code}" не существует - скидка 0%')
        discount_percent = 0

total = price * number_of_servings
discount = total * discount_percent // 100
final_sum = total - discount

## Проверка на склонение слова порция

if number_of_servings % 10 == 1 and number_of_servings % 100 != 11:
    word = "порция"
elif 2 <= number_of_servings % 10 <= 4 and not (12 <= number_of_servings % 100 <= 14):
    word = "порции"
else:
    word = "порций"

print(
    "\n" + "═" * 30 +
    "\n       ☕ КВИТАНЦИЯ КАФЕ ☕\n" +
    "═" * 30 +
    f"\nТовар: {name} {emoji}" +
    f"\nЦена за порцию: {price} руб" +
    f"\nКоличество: {number_of_servings} {word}" +
    f"\nСумма: {total} руб"
)  ## вывод информации о заказе

if discount_percent != 0:
    print(f'Скидка "{promo_code}" ({discount_percent}%): -{discount} руб')

print(
    "═" * 30 +
    f"\n💰 К ОПЛАТЕ: {final_sum} руб" +
    "\n" + "═" * 30
)
