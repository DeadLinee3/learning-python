while True:
    print("1 - Привет")
    print("2 - Введи число")
    print("3 - Пока")
    choice = int(input("Введи число:"))
    if choice == 1:
        name = input("Как тебя зовут:")
        print(f"Привет {name}")
    elif choice == 2:
        a = int(input("Введите первое число:"))
        b = int(input("Введите второе число:"))
        print(f"{a}+{b} = {a+b}")
    elif choice == 3:
        print("Выход из програмы")
        break
    else:
        print("Нет такого пункта")        