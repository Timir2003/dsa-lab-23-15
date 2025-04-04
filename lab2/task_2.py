# Считывание строки
input_string = input("Введите строку: ")

# Замена всех символов 'a' на 'o' и подсчитывание количества замен
count_replace = input_string.count('a')
modified_string = input_string.replace('a', 'o').replace('A', 'O')

# Вывод количества замен
print(f"Количество замен 'a(A)' на 'o(O)': {count_replace}")

# Подсчитывание и вывод количества всех символов в строке
total_symbols = len(input_string)
print(f"Общее количество символов в строке: {total_symbols}")

# Вывод изменённой строки
print(f"Изменённая строка: {modified_string}")