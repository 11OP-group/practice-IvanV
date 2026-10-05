TAX = 0.13

def calculate_tax_details(annual_income):
    """
    производит налоговые расчёты с annual_income
    и возвращает значения: сумма налога, сумма на руки
    """
    tax_amount = annual_income * TAX
    cash_on_hand = annual_income - tax_amount
    return tax_amount, cash_on_hand

users_annual_income = float(input("Введите ваш годовой доход: "))
tax_amount, cash_on_hand = calculate_tax_details(users_annual_income)

print(f"Общая сумма дохода: {users_annual_income:,.2f} руб.".replace(",", " "))
print(f"Сумма налога: {tax_amount:,.2f} руб.".replace(",", " "))
print(f"Сумма на руки: {cash_on_hand:,.2f} руб.".replace(",", " "))
