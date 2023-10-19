import random
import time


def animate_search():
    print("Поиск подходящей строки...")
    for _ in range(3):
        time.sleep(0.5)
        print("🔍", end=' ')
        time.sleep(0.5)
    print("\n")


def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            element = float(input(f"Введите элемент матрицы в строке {_ + 1}, столбце {_ + 1}: "))
            row.append(element)
        matrix.append(row)


    print("Введенная матрица:")
    for row in matrix:
        print(row)

    return matrix


def find_first_positive_row(matrix):
    try:
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Матрица должна быть представлена в виде списка списков.")

        animate_search()

        for i, row in enumerate(matrix, start=1):
            if all(isinstance(element, (int, float)) and element > 0 for element in row):
                return row, sum(row)

        raise ValueError("В матрице нет строк, где все элементы положительны.")
    except ValueError as e:
        return None, str(e)


# Введите размерность матрицы (количество строк и столбцов)
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создайте матрицу
matrix = create_matrix(rows, cols)

row, sum_of_elements = find_first_positive_row(matrix)

if row is not None:
    print("Нашли первую строку с положительными элементами:")
    print("Строка:", row)
    print(f"Сумма элементов в этой строке: {sum_of_elements}")
else:
    print("❌ Ошибка:", sum_of_elements)
