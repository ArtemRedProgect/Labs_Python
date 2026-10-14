from datetime import datetime
def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            args_str = ", ".join([str(arg) for arg in args] + [f"{k}={v}" for k, v in kwargs.items()])

            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"Время: {now} // Функция: {func.__name__} // Аргументы: ({args_str})\n")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("logLab1.txt")
def sums(a, b):
    return a + b

sums(5, 30)
sums(10, 20)