import random

secret_number = random.randint(1, 10)
print(secret_number)

attempts = 0
max_attempts = 5

while True:
    guess = int(input("Угадай число от 1 до 10: "))
    if guess == secret_number:
        print(f"Поздравляю ты угадал число за {attempts} попыток")
        break
    elif guess < secret_number:
        print("Мое число больше )")
    else:
        print("Мое число меньше)")
    if attempts == max_attempts:
        print("Число неправильное")
        break        