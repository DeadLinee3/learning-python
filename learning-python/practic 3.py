while True:
    x = float(input(f"Введите первое число:"))
    y = float(input(f"Введите второе число:"))

    print(f"\nВыберете операцию")
    print(f"1 - сума")
    print(f"2 - разница")
    print(f"3 - множение")
    print(f"4 - деление")
    print(f"5 - остаток деление")
    print(f"6 - целочисленое деление")
    print(f"7 - возведения в степень")
    print(f"0 - выход")

    op = input(f"Ваш выбор 0-7:")

    if op == "1":
        print(f"сума: {x + y}")
    elif op == "2":
        print(f"разница: {x - y}")
    elif op == "3":
        print(f"множение: {x * y}")    
    elif op == "4":
        if y != 0:
            print(f"деление: {x / y}")
        else:
            print(f"деление на ноль!")
    elif op == "5":
        if y != 0:
            print(f"остаток деление: {x % y}")
        else:
            print(f"деление на ноль!")
    elif op == "6":
        if y != 0:
            print(f"целочисленое деление: {x // y}")
        else:
            print(f"деление на ноль!")
    elif op == "7":
        print(f"возведение в степень: {x ** y}")        
    elif op == "0":
        print(f"Програма завершена!)")
        break
    else:
        print("Неизвестная операция")
    print("-" * 30)
      
    

    
    