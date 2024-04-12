n = int(input('Введите число: '))
for i in range(2, n+1):
    splitter = 0
    for j in range(1, i+1):
        if i % j == 0:
            splitter += 1
    if splitter == 2:
        print(i)