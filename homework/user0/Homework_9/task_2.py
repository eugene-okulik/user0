'''
Map, filter
Есть такой список:

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 
25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
Будем считать жарким всё, что выше 28.

Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
'''

temperatures = [
    20, 15, 32, 34, 21, 19,
    25, 27, 30, 32, 34, 30,
    29, 25, 27, 22, 22, 23,
    25, 29, 29, 31, 33, 31,
    30, 32, 30, 28, 24, 23
]

hot_temperatures = list(filter(lambda t: t > 28, temperatures))

if hot_temperatures:
    max_temp = max(hot_temperatures)
    min_temp = min(hot_temperatures)
    avg_temp = sum(hot_temperatures) / len(hot_temperatures)

    print(f'Жаркие дни: {hot_temperatures}')
    print(f'Максимальная температура: {max_temp}')
    print(f'Минимальная температура: {min_temp}')
    print(f'Средняя температура: {avg_temp:.2f}')
