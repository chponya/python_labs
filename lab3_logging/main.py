import time
from datetime import datetime
import os

# Путь к лог-файлу
LOG_PATH = os.path.join(os.path.dirname(__file__), "log.txt")

def log_decorator(func):
    """
        Декоратор для логирования вызова функции:
        - записывает время вызова
        - имя функции
        - аргументы вызова
        - время завершения
        - время выполнения (секунды)
    """
    def wrapper(*args, **kwargs):
        # Засекаем время начала работы функции
        start_time = time.time()
        # Текущая дата и время в удобном формате
        start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Открываем файл логов в режиме добавления (append)
        # и записываем строку с информацией о вызове функции и аргументах
        with open(LOG_PATH, "a", encoding="utf-8") as log_file:
            log_file.write(f"[{start_dt}] Функция '{func.__name__}' вызвана с аргументами: {args}\n")

        # Выполняем оригинальную функцию и сохраняем результат
        result = func(*args, **kwargs)

        # Засекаем время окончания работы функции
        end_time = time.time()
        end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Вычисляем время выполнения в секундах (с округлением до 2 знаков)
        duration = round(end_time - start_time, 2)

        # Записываем в лог информацию о завершении и времени выполнения
        with open(LOG_PATH, "a", encoding="utf-8") as log_file:
            log_file.write(f"[{end_dt}] Функция '{func.__name__}' завершена. Время выполнения: {duration} сек.\n")

        return result
    return wrapper

@log_decorator
def calculate(a, b, operation):
    """
    Функция для вычисления арифметической операции над двумя числами:
    поддерживает +, -, *, /
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("Неподдерживаемая операция")

if __name__ == "__main__":
    # Пример вызова функции calculate
    result = calculate(10, 5, '+')
    print("Результат:", result)
