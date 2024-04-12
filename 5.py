# Совершенное число — натуральное число, равное сумме всех своих собственных делителей

def check(n):
    sum_elements = sum([i for i in range(1, n) if n % i == 0])
    return sum_elements == n

n = int(input('Введите число: '))
for i in range(2, n+1):
    if check(i):
        print(i)