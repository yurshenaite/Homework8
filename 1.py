result = int(input('Введите результат (введите -1 для завершения): '))
best_result = 0
previous_result = None

while result != -1:
    if previous_result is not None and result >= previous_result:
        best_result = result
    previous_result = result
    result = int(input('Введите результат (введите -1 для завершения): '))

print(best_result)