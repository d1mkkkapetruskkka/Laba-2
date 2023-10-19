def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except TypeError:
        print("Ошибка: некорректный тип данных")
    else:
        print(f"Результат деления: {result:.2f}")
    finally:
        print("Завершение программы")

try:
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    divide_numbers(a, b)
except ValueError:
    print("Ошибка: Введите числовые значения a и b.")
except Exception as e:
    print(f"Ошибка: {e}")
