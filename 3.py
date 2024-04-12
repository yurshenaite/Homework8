income = int(input('Введите доход (введите 0 для завершения): '))
counter = 0
total_income = 0

while income != 0:
    counter += 1
    total_income += income
    income = int(input('Введите доход (введите 0 для завершения): '))

average_income = total_income / counter
print(average_income)