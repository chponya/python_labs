import time
from functools import wraps

def rate_limit(max_calls, period):
    def decorator(func):
        calls = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            current_time = time.time()
            # удаляем устаревшие вызовы
            calls = [call for call in calls if current_time - call < period]
            if len(calls) < max_calls:
                calls.append(current_time)
                return func(*args, **kwargs)
            else:
                print("Превышен лимит вызовов. Попробуйте позже.")
        return wrapper
    return decorator

# Пример использования
@rate_limit(max_calls=3, period=60)
def send_message(message):
    print(f"Сообщение отправлено: {message}")

if __name__ == "__main__":
    for i in range(5):
        send_message("Привет!")
