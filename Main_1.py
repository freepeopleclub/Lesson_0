# "1st program"
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
print(9 ** 0.5 * 5)

# "2nd program"
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
print(9.99 > 9.98 and 1000 != 1000.1)

# "3rd program"
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
# Выведите на экран(в консоль) результат сравнения этих двух выражений.
print(2 * 2 + 2)
print(2 * (2 + 2))
print(2 * 2 + 2 == 2 * (2 + 2))

# "4th program"
# Дана строка '123.456'.
# Вывести на экран первую цифру после запятой - 4.
print(int((float('123.456') - int(123.456)) * 10))