using System;

namespace ConsoleBank
{
    internal class Program
    {
        const double RATE_THREE_MONTHS = 11.50;
        const double RATE_SIX_MONTHS = 11.75;
        const double RATE_YEAR = 12.50;

        static void Main(string[] args)
        {
            double deposit, annualRate, dailyIncome, totalIncome;
            int days;

            Console.Title = "Расчёт банковского вклада";
            Console.WriteLine("=== Банковский вклад ===");

            Console.WriteLine("Введите сумму вклада (больше 0):");
            while (!double.TryParse(Console.ReadLine(), out deposit) ||
                   !(deposit > 0 && deposit <= double.MaxValue))
            {
                Console.WriteLine("Ошибка! Введите положительную сумму:");
            }

            Console.WriteLine("Введите срок вклада: 91, 181 или 365 дней:");
            while (!int.TryParse(Console.ReadLine(), out days) ||
                   (days != 91 && days != 181 && days != 365))
            {
                Console.WriteLine("Ошибка! Допустимые сроки: 91, 181 или 365 дней:");
            }

            // Выбор годовой ставки по сроку вклада.
            if (days == 91)
            {
                annualRate = RATE_THREE_MONTHS;
            }
            else if (days == 181)
            {
                annualRate = RATE_SIX_MONTHS;
            }
            else
            {
                annualRate = RATE_YEAR;
            }

            // Проценты начисляются на первоначальную сумму вклада.
            dailyIncome = deposit * annualRate / 100 / 365;
            totalIncome = dailyIncome * days;

            Console.WriteLine("=== Результат расчёта ===");
            Console.WriteLine($"Годовая ставка: {annualRate:F2}%");
            Console.WriteLine($"Доход за день: {dailyIncome:F2} руб.");
            Console.WriteLine($"Доход за весь срок ({days} дн.): {totalIncome:F2} руб.");
            Console.WriteLine($"Сумма в конце срока: {deposit + totalIncome:F2} руб.");
            Console.WriteLine("Нажмите Enter для выхода.");
            Console.ReadLine();
        }
    }
}
