'''
Задание 2
Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел
фибоначчи
Распечатайте из этого списка пятое число,
двухсотое число, тысячное число, стотысячное число

На всякий случай, напомню, что превращать результат работы
генератора в список - неправильно.
'''

import sys

# Устанавливаем новый лимит для строковых преобразований больших чисел
sys.set_int_max_str_digits(100000)

def fibonacci_generator():
    '''
    функцию-генератор, которая генерирует бесконечную последовательность чисел
    фибоначчи, начиная с 0 и 1.
    '''
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()


# Функция для получения n-го числа Фибоначчи из генератора
def get_fibonacci_number(n):
    '''
    Возвращает n-ое число Фибоначчи из генератора.

    Аргументы:
    n (int): Порядковый номер числа Фибоначчи (начиная с 1).

    Возвращает:
    int: n-ое число Фибоначчи.
    '''
    for _ in range(n - 1):
        next(fib_gen)
    return next(fib_gen)


# Получаем пятое, двухсотое, тысячное и стотысячное числа Фибоначчи
fifth_fib = get_fibonacci_number(5)
two_hundredth_fib = get_fibonacci_number(200)
thousandth_fib = get_fibonacci_number(1000)
hundred_thousandth_fib = get_fibonacci_number(100000)

# Выводим результат
print("Пятое число Фибоначчи:", fifth_fib)
print("Двухсотое число Фибоначчи:", two_hundredth_fib)
print("Тысячное число Фибоначчи:", thousandth_fib)
print("Стотысячное число Фибоначчи:", hundred_thousandth_fib)
