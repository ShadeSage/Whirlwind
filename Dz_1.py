number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
result = number_1 * number_2
print(f"Сумма чисел равна: {result}")
if result > 10:
    print("Сумма больше 10")
else:
    print("Сумма меньше или равна 10")