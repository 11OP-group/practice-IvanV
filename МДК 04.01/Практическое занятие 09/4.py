DECIMAL_BASE = 10
SEARCH_DIGIT = 3
SUM_THRESHOLD = 5
PRODUCT_THRESHOLD = 7
ZERO_FIVE_DIGITS = (0, 5)

def analyze_digits(n):

    last_digit = n % DECIMAL_BASE
    count_search = 0
    count_last = 0
    count_even = 0
    sum_big = 0
    prod_big = 1
    count_zero_five = 0

    while n > 0:
        digit = n % DECIMAL_BASE

        if digit == SEARCH_DIGIT:
            count_search += 1
        if digit == last_digit:
            count_last += 1
        if digit % 2 == 0:
            count_even += 1
        if digit > SUM_THRESHOLD:
            sum_big += digit
        if digit > PRODUCT_THRESHOLD:
            prod_big *= digit
        if digit in ZERO_FIVE_DIGITS:
            count_zero_five += 1

        n //= DECIMAL_BASE

    return count_search, count_last, count_even, sum_big, prod_big, count_zero_five

number = int(input("Введите натуральное число: "))

count_3, count_last, count_even, sum_big5, prod_big7, count_0_5 = analyze_digits(number)

print(f"Количество цифр {SEARCH_DIGIT}: {count_3}")
print(f"Сколько раз встречается последняя цифра: {count_last}")
print(f"Количество чётных цифр: {count_even}")
print(f"Сумма цифр больше {SUM_THRESHOLD}: {sum_big5}")
print(f"Произведение цифр больше {PRODUCT_THRESHOLD}: {prod_big7}")
print(f"Количество цифр 0 и 5: {count_0_5}")