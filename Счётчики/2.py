def number_of_occurrences(char, string):
    # Здесь объявите переменную count, равную нулю.
    # Она будет хранить количество вхождений
    count = 0
    for letter in string:
        # Напишите условие: сравните переменные letter и char
        # И если letter равна char - увеличивайте счётчик count на 1
        letter == char
        if letter == char:
            count += 1

    # Печатаем исходную строку:
    print('Исходная строка:', string)
    # Печатаем результат подсчётов:
    print('Количество вхождений символа', char, 'составляет:', count)


# Код ниже не изменяйте
phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'

# Вызываем функцию number_of_occurrences(), чтобы она посчитала,
# сколько раз во фразе phrase встречается буква 'е'
number_of_occurrences('е', phrase)