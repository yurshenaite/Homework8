num = input('Введите число: ')
y = num.isdigit()

while y == False:
    num = input('Ошибка. Попробуйте еще раз. Введите число: ')
    y = num.isdigit()

print(f'Введено целое число: {num}')