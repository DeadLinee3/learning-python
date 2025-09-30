attempts = 0
max_attepts = 3

while True:
    password = input("Введите пароль:")
    attempts += 1

    if password == "1234":
        print("Пароль правильный)")
        break 

    if attempts == 3:    
        print("Password incorrect")
        break 
    else:
        print("Password incorrect")
    remaining = max_attepts - attempts
    print(f"Пароль неверный, осталось попыток: {remaining}")
       
