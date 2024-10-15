'''
Задание №1
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
и после этого выводит получившийся текст на экран. Знаки препинания
не должны оказаться внутри слова. Если после слова идет запятая или точка,
этот знак препинания должен идти после того же слова, но уже преобразованного.
'''

text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()  # Разделяем text на слова

for word in words:  # для слова ис списка слов
    if word.endswith(',') or word.endswith('.'):  # если слово заканчивается (включает символ) на , или . то
        new_word = word[:-1] + 'ing' + word[-1]  # для слова убираем последний символ + окончание, после чего + последний символ
    else:
        new_word = word + 'ing'
    print(new_word, end=' ')
print()
