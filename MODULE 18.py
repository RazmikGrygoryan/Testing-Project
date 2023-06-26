# РЕШЕНИЕ:
count = 0
first_deposit = 990
second_deposit = 1390

n = int(input('Выберите количество билетов: '))
for i in range(n):
    if n > 0 and n <= 3:
        age = int(input('Введите возраст: '))
        if age < 18 and age > 0:
            count = 0
        elif 18 <= age < 25:
            count += first_deposit
        elif age >= 25:
            count += second_deposit
    elif n > 3:
        age = int(input('Введите возраст: '))
        if age < 18 and age > 0:
            count = 0
        elif 18 <= age < 25:
            count += first_deposit - first_deposit * 10 // 100
        elif age >= 25:
            count += second_deposit - second_deposit * 10 // 100
if n != 0 and n > 0:
    print(f'С вас {count} рублей')
else:
    print('Некорректное значение')