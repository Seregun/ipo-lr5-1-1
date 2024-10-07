def count(s): # Функция
    vowels = "уеыаоэяиюё" # Гласные буквы
    consonants = "бвгджзйклмнпрстфхцчшщ" # Согласные буквы
    num_vowels = 0 # Начало отсчета гласных букв
    num_consonants = 0 # Начало отсчета согласных букв
    for char in s.lower(): # Цикл for
        if char in vowels: # Условие для гласных
            num_vowels += 1 # Добавление гласной буквы
        elif char in consonants: # Условие для согласных
            num_consonants += 1 # Добавление согласной буквы
    return num_vowels, num_consonants # Возвращение получившегося реезультата
words = input("Введите строку: ") # Ввод строки
length = len(words) # Подсчет длины строки
vowels, consonants = count(words) # Вызов функции
print(f"Длина строки: {length}") # Вывод длины строки
print(f"Кол-во согласных: {consonants}") # Вывод кол-ва согласных букв
print(f"Кол-во гласных: {vowels}") # Вывод кол-ва гласных букв