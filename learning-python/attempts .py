attempts = 0
max_attempts = 3
while True:
    password = input("Введите пароль:")
    attempts += 1
    remaining = max_attempts - attempts 
    if password == "1234":
        print("Пароль правильный:")
        break
    if attempts == max_attempts:
        print("Password incorrect")
        break
    print(f"Пароль неверный, осталось попыток {remaining}")
    
