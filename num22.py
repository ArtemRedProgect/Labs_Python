def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                real_argument = args[i]
                required_type = expected_types[i]

                if not isinstance(real_argument, required_type):
                    raise TypeError(f"Аргумент под номером {i} имеет неверный тип!")

            return func(*args, **kwargs)

        return wrapper

    return decorator
@type_check(int, int)
def sum(a, b):
    return a + b


print(sum(5, 5))

print(sum(6, 8.6))

