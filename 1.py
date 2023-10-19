def is_prime(number):
    try:
        if not isinstance(number, int):
            raise ValueError("Число должно быть целым числом.")

        if not (0 <= number <= 1000):
            raise ValueError("Число должно быть в диапазоне от 0 до 1000.")

        if number <= 1:
            return False
        elif number <= 3:
            return True
        elif number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True
    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Проверка завершена.")


# Пример использования функции:
try:
    number = int(input("Введите число от 0 до 1000: "))
    if is_prime(number):
        print(f"{number} - простое число")
    else:
        print(f"{number} - не простое число")
except ValueError:
    print("Ошибка: Введите корректное целое число в диапазоне от 0 до 1000.")
finally:
    print("Программа завершена.")
