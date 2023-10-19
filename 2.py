import time

def animate_processing():
    for _ in range(3):
        print("Анализ данных...", end='\r')
        time.sleep(0.5)
        print("                   ", end='\r')
        time.sleep(0.5)

def sum_of_numbers(input_data):
    try:
        animate_processing()
        if isinstance(input_data, list):
            if all(isinstance(item, (int, float)) for item in input_data):
                result = sum(input_data)
                return f" Анализ завершен: Сумма чисел в списке равна {result:.2f}"
            else:
                raise ValueError(" Ошибка: В списке должны быть числа.")
        else:
            raise ValueError(" Ошибка: Введен неподдерживаемый тип данных.")
    except ValueError as e:
        return str(e)

def top_three_values(input_data):
    try:
        animate_processing()
        if isinstance(input_data, dict):
            if all(isinstance(value, (int, float)) for value in input_data.values()):
                sorted_items = sorted(input_data.items(), key=lambda x: x[1], reverse=True)[:3]
                return f" Анализ завершен: Три наибольших значения в словаре: {', '.join(f'{key}: {value:.2f}' for key, value in sorted_items)}"
            else:
                raise ValueError(" Ошибка: Значения в словаре должны быть числами.")
        else:
            raise ValueError(" Ошибка: Введен неподдерживаемый тип данных.")
    except ValueError as e:
        return str(e)

def sum_of_digits(input_data):
    try:
        animate_processing()
        if isinstance(input_data, (int, float)):
            if isinstance(input_data, float):
                input_data = int(input_data)
            digits_sum = sum(int(digit) for digit in str(abs(input_data)))
            return f" Анализ завершен: Сумма цифр числа: {digits_sum}"
        else:
            raise ValueError(" Ошибка: Введен неподдерживаемый тип данных.")
    except ValueError as e:
        return str(e)

def word_count(input_data):
    try:
        animate_processing()
        if isinstance(input_data, str):
            words = input_data.split()
            word_count = len(words)
            return f" Анализ завершен: Количество слов в строке: {word_count}"
        else:
            raise ValueError(" Ошибка: Введен неподдерживаемый тип данных.")
    except ValueError as e:
        return str(e)


data1 = input("Введите список чисел через пробел: ")
data1 = [float(x) for x in data1.split()]

data2 = input("Введите словарь (в формате key:value через пробел): ")
data2 = dict(item.split(':') for item in data2.split())

data3 = float(input("Введите число: "))

data4 = input("Введите строку: ")

print(sum_of_numbers(data1))
print(top_three_values(data2))
print(sum_of_digits(data3))
print(word_count(data4))
