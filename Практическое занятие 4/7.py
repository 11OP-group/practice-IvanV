SEATS_PER_COMPARTMENT = 4

seat_place = int(input("Введите номер вашего места: "))

coupe = (seat_place - 1) // SEATS_PER_COMPARTMENT + 1

print(f"Ваше место {seat_place} в купе под номером {coupe}")