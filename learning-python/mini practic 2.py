while True:
    print("\nМеню")
    print("0 - выйти")
    print("1 - Привет!)")
    print("2 - До встречи")
    op = input(f"Ваш выбор: ").strip()
    if op == "1":
        print("Привет!")
    elif op == "2":
        print("До встречи")
    elif op == "0":
        print("Пока")
        break
    else:
        print("Неизвестная команда")        
