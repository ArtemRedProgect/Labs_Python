import random

a = random.randint(1, 100)
tries = 0

while True:
    n = int(input("Угадайте число от 1 до 100: "))
    tries += 1

    if n > a:
        print("Меньше")
    elif n < a:
        print("Больше")
    else:
        print("Вы угадали число!")
        print(f"Ушло попыток: {tries}")
        break