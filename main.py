words = input("Введите строку: ") # Ввод строки
length = len(words) # Подсчет длины строки
vowels = "уеыаоэяиюё" # Гласные буквы
consonants = "бвгджзйклмнпрстфхцчшщ" # Согласные буквы
num_vowels = 0 # Начало отсчета гласных букв
num_consonants = 0 # Начало отсчета согласных букв
for char in words.lower(): # Цикл for
    if char in vowels: # Условие для гласных
        num_vowels += 1 # Добавление гласной буквы
    elif char in consonants: # Условие для согласных
        num_consonants += 1 # Добавление согласной буквы
print(f"Длина строки: {length}") # Вывод длины строки
print(f"Кол-во согласных: {num_consonants}") # Вывод кол-ва согласных букв
print(f"Кол-во гласных: {num_vowels}") # Вывод кол-ва гласных букв
