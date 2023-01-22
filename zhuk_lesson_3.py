# 1. Перемножить все нечетные числа от a до b. a,b задаются пользователем
a = int(input('Введите число '))
b = int(input('Введите число чтоб получить диапазон чисел от а до b  '))
SU = 1
for i in range(a, b+1):
    if i % 2 != 0:
        SU *= i
print(SU)


# 2. Вывести все четные числа от a до b
print(*[i for i in range(a, b) if i % 2 == 0])
# 3. Дан список sp = [2343, 5668,23,46,10,23,2343]. Если число встретилось больше 1 раза
# то добавить его в новый список
sp = [2343, 5668, 23, 46, 10 ,23, 2343]
new_sp = []
for i in sp:
    if i not in new_sp and sp.count(i)>1:
        new_sp.append(i)
print(new_sp)

# 4. Творческое: для таблицы умножения сделать сетку,

for i in range(1,10):
    for j in range(1,10):
        print('\033[2m\033[35m\033[41m{}'.format(str(i*j).center(2)), end='|')
    print()
