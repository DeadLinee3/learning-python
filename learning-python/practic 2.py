x = int(input("Введите первое число:"))
y = int(input("Веедите второе число:"))
print(f"сума: {x + y}")
print(f"Разница: {x - y}")
print(f"Сложение: {x * y}")

if y != 0:
    print(f"деление: {x / y}")
    print(f"остаток от деление: {x % y}")
else:
    print(f"на ноль не делим е)")