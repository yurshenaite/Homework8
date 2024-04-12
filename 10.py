def check(n):
    sum_elements = sum([i for i in range(1, n) if n % i == 0])
    return sum_elements == n

n = int(input('Введите число: '))
counter = 0
for i in range(2, n):
    if check(i):
        counter += i

print(counter)