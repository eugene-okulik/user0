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
    if word.endswith(',') or word.endswith('.'):
        new_word = word[:-1] + 'ing' + word[-1] 
    else:
        new_word = word + 'ing'
    print(new_word, end=' ')
print()
