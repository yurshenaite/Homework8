# Если заданием стоит доработать прошлую задачу, то просто добавим новое условие в цикл

result = int(input('Введите результат (введите -1 для завершения): '))
best_result = 0
counter = 0
previous_result = None

while result != -1:
    if previous_result is not None and result >= previous_result:
        best_result = result
    previous_result = result
    counter += 1
    result = int(input('Введите результат (введите -1 для завершения): '))

print(f'{counter} друзей')