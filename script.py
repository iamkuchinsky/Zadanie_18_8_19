summa = 0
tickets = (int(input("Введите количество билетов:")))
for age in range(tickets):
    age = (int(input("Введите возраст посетителя:")))
    if age < 18:
        summa += 0
    elif age >= 18 and age <= 25:
        summa += 990
    elif age > 25:
        summa += 1390
if tickets > 3:
    summa -= summa / 100 * 10
print("Стоимость Ваших билетов", summa)