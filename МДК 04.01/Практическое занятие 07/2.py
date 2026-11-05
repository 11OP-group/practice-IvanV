import random ## генерация случайного времени доставки

print(
    "📦 Добро пожаловать в систему отслеживания заказов! 📦\n\n"
    "Виды статусов:\n"
    "pending - В ожидании\n"
    "processing - В обработке\n"
    "shipped - Отправлено\n"
    "delivered - Доставлено\n"
    "cancelled - Отменено\n"
) ## Вывод доступных статусов

order_status = input("Введите статус заказа: ")
delivery_time = random.choice(["1-2 дня", "2-3 дня", "3-5 дней"]) 
## если статус доставлен или отменен то devivery_time меняется внутри case

match order_status:
    case "pending":
        status, emoji = "В ожидании", "⏳"
        description = "Заказ создан и ожидает подтверждения"
        recommendation = "Ожидайте подтверждения заказа"

    case "processing":
        status, emoji = "В обработке", "📦"
        description = "Заказ комплектуется на складе"
        recommendation = "Скоро заказ будет передан в службу доставки"

    case "shipped":
        status, emoji = "Отправлено", "✈️"
        description = "Ваш заказ находится в пути к вам"
        recommendation = "Следите за уведомлениями о доставке"

    case "delivered":
        status, emoji = "Доставлено", "✅"
        description = "Заказ успешно доставлен получателю"
        delivery_time = "Доставлено"
        recommendation = "Спасибо, что выбрали нас!"

    case "cancelled":
        status, emoji = "Отменено", "❌"
        description = "Заказ был отменён"
        delivery_time = "Отсутствует"
        recommendation = "Вы можете оформить новый заказ на сайте"
        
    case _:
        status = "invalid_status"

if status == "invalid_status": ## проверка на ошибку в статусе
    print(f"Ошибка: неизвестный статус - {status}")
else: ## Вывод информации заказа
    print(
        "\n" + "-" * 45 +
        "\n       📦 СТАТУС ВАШЕГО ЗАКАЗА 📦\n" +
        "-" * 45 +
        f"\nСтатус: {status} {emoji}" +
        f"\nОписание: {description}" +
    f"\nПримерное время: {delivery_time}" +
    f"\nРекомендация: {recommendation}" +
    "\n" + "-" * 45
    )