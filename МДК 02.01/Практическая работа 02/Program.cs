using Console = System.Console;
using Random = System.Random;

namespace GladiatorBattle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            double health1, health2, armor1, armor2;
            double randomDamage1, randomDamage2, damage1, damage2;
            int countHit = 0;

            Console.Title = "Бой двух гладиаторов";

            // Ввод характеристик первого гладиатора.
            Console.WriteLine("=============== ПЕРВЫЙ ГЛАДИАТОР ===============");
            Console.WriteLine("Введите здоровье (больше 0):");
            while (!double.TryParse(Console.ReadLine(), out health1) ||
                   !(health1 > 0 && health1 <= double.MaxValue))
            {
                Console.WriteLine("Ошибка! Введите положительное число:");
            }

            Console.WriteLine("Введите крепость брони в процентах (больше 0, до 100):");
            while (!double.TryParse(Console.ReadLine(), out armor1) ||
                   !(armor1 > 0 && armor1 <= 100))
            {
                Console.WriteLine("Ошибка! Введите число больше 0 и не больше 100:");
            }

            // Ввод характеристик второго гладиатора.
            Console.WriteLine("=============== ВТОРОЙ ГЛАДИАТОР ===============");
            Console.WriteLine("Введите здоровье (больше 0):");
            while (!double.TryParse(Console.ReadLine(), out health2) ||
                   !(health2 > 0 && health2 <= double.MaxValue))
            {
                Console.WriteLine("Ошибка! Введите положительное число:");
            }

            Console.WriteLine("Введите крепость брони в процентах (больше 0, до 100):");
            while (!double.TryParse(Console.ReadLine(), out armor2) ||
                   !(armor2 > 0 && armor2 <= 100))
            {
                Console.WriteLine("Ошибка! Введите число больше 0 и не больше 100:");
            }

            Console.WriteLine("================ НАЧАЛО БОЯ ================");

            while (health1 > 0 && health2 > 0)
            {
                // Каждый гладиатор наносит случайный удар от 30 до 75.
                randomDamage1 = random.Next(30, 76);
                randomDamage2 = random.Next(30, 76);

                // От каждого удара броня изнашивается.
                armor2 -= randomDamage1 * 0.25;
                armor1 -= randomDamage2 * 0.25;
                if (armor1 < 0) armor1 = 0;
                if (armor2 < 0) armor2 = 0;
                // Броня уменьшает получаемый урон.
                damage1 = randomDamage1 * (1 - armor2 / 100);
                damage2 = randomDamage2 * (1 - armor1 / 100);

                // Удары в раунде происходят одновременно.
                health2 -= damage1;
                health1 -= damage2;

                if (health1 < 0) health1 = 0;
                if (health2 < 0) health2 = 0;

                countHit++;
                Console.WriteLine("--------------------------------------------");
                Console.WriteLine($"Удар №{countHit}: первый гладиатор");
                Console.WriteLine($"Сила удара: {randomDamage1:F1}. Урон: {damage1:F1}");
                Console.WriteLine($"Здоровье второго гладиатора: {health2:F1}");

                countHit++;
                Console.WriteLine($"Удар №{countHit}: второй гладиатор");
                Console.WriteLine($"Сила удара: {randomDamage2:F1}. Урон: {damage2:F1}");
                Console.WriteLine($"Здоровье первого гладиатора: {health1:F1}");
            }

            Console.WriteLine("================ ИТОГ БОЯ ================");
            if (health1 <= 0 && health2 <= 0)
            {
                Console.WriteLine("Ничья. Оба гладиатора погибли.");
            }
            else if (health2 <= 0)
            {
                Console.WriteLine("Победил первый гладиатор.");
            }
            else
            {
                Console.WriteLine("Победил второй гладиатор.");
            }
            Console.WriteLine($"Всего ударов: {countHit}");
            Console.WriteLine("Нажмите Enter для выхода.");
            Console.ReadLine();
        }
    }
}
