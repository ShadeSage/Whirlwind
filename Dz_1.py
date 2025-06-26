#Питон вводное занятие
number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
result = number_1 * number_2
print(f"Произведение чисел равна: {result}")
if result > 10:
    print("Произведение больше 10")
else:
    print("Произведение меньше или равно 10")