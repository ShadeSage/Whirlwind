#Налоги
income = int(input("Введите прибыль: "))
if income < 10000:
    tax = income * 13 / 100
    print(f"Налоговая ставка равна 13% - {tax}")
elif income < 50000:
    tax = income * 20 / 100
    print(f"Налоговая ставка равна 20% - {tax}")
else:
    tax = income * 30 / 100
    print(f"Налоговая ставка равна 30% - {tax}")