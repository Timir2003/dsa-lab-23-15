import sys

def main():
    # Считывание массива из параметров командной строки
    if len(sys.argv) < 2:
        print("Ошибка: не указаны элементы массива.")
        print("Использование: python script.py <элемент1> <элемент2> ... <элементN>")
        sys.exit(1)

    try:
        arr = list(map(int, sys.argv[1:]))
    except ValueError:
        print("Ошибка: все элементы массива должны быть целыми числами.")
        sys.exit(1)

    if not arr:
        print("Ошибка: массив не может быть пустым.")
        sys.exit(1)

    # Нахождение максимального элемента и его индекс
    max_val = max(arr)
    max_index = arr.index(max_val)

    print(f"Максимальный элемент: {max_val}, его порядковый номер (индекс): {max_index}")

    # Фильтрация нечетных чисел и сортировка их в порядке убывания
    odd_numbers = [x for x in arr if x % 2 != 0]

    if not odd_numbers:
        print("В массиве нет нечетных чисел.")
    else:
        odd_numbers_sorted = sorted(odd_numbers, reverse=True)
        print("Нечетные числа в порядке убывания:", ' '.join(map(str, odd_numbers_sorted)))


if __name__ == "__main__":
    main()