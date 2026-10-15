import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения программы: {(end - start) * 1000}")
        return result
    return wrapper





@timing
def sum(a, b):
    return a + b

print(sum(5,6))