'''
Задание: Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
'''
katet_1 = float(input("Введите длину первого катета = "))
katet_2 = float(input("Введите длину второго катете = "))

hypotenuse = ((katet_1 ** 2) + (katet_2 ** 2))**0.5
area = (katet_1 * katet_2) / 2

print(f"Длина гипотенузы: {hypotenuse}")
print(f"Площадь прямоугольного треугольника: {area}")