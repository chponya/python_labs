from functools import wraps

def cache_decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"[Кэш] Возвращаю сохранённый результат для {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"[Вычисление] Сохраняю результат для {args}")
        return result

    return wrapper

# Пример использования
@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(f"Результат: {fibonacci(10)}")
    print(f"Результат повторно: {fibonacci(10)}")  # должен взять из кэша
