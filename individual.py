import math


a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))


perimeter = 2 * (a + b)
diagonal = math.sqrt(a**2 + b**2)


print(f"\nСтороны прямоугольника: {a} и {b}")
print(f"Периметр: {perimeter}")
print(f"Диагональ: {diagonal:.2f}
