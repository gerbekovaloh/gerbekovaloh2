a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвёртое число: "))

sum1 = a + b
sum2 = c + d

if sum2 == 0:
    print("Ошибка: деление на ноль")
else:
    result = sum1 / sum2
    print(f"Результат: {result:.2f}")