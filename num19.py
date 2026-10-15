def cache(func):
    storage = {}
    def wrapper(*args, **kwargs):
        keys_args = (args, tuple(kwargs.items()))
        if keys_args in storage:
            print("Такие данные уже передавались. Функция не выполняется. Берем из кеша")
            return storage[keys_args]
        print("Данных в кеше нет. Выполняем функцию")
        result = func(*args, **kwargs)
        storage[keys_args] = result
        return result
    return wrapper

@cache
def sum(a, b):
    return a + b

@cache
def umnozh(c, d):
    return c * d

print("Сумма 1")
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
print(sum(a, b))

print()
print("Сумма 2")
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
print(sum(a, b))

print()
print("Умножение 1")
c, d = int(input("Введите первое число: ")), int(input("Введите второе число: "))
print(umnozh(c, d))

print()
print("Умножение 2")
c, d = int(input("Введите первое число: ")), int(input("Введите второе число: "))
print(umnozh(c, d))