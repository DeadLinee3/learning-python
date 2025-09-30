# День 2: основы ввода/вывода, типы, f-строки

a = float(input("A: "))
b = float(input("B: "))
op = input("Операция (+, -, *, /): ")

if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
else:
    print("Неизвестная операция")
    raise SystemExit

print(f"Результат: {a} {op} {b} = {res}")
