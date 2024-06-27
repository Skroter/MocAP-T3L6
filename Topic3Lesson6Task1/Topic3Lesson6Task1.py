import random

N = int(input('Введите любое целое число: '))
arr = []
n0 = 0
for i in range(N):
    arr.append(int(input('Введите любое целое число: '))) # ручной ввод значений в массив
    # arr.append(random.randint(-1, 1)) # это как вариант самостьятельного заполнения массива, диапозон можно установить любой
    if arr[i] == 0:
         n0 += 1
    i += 1
print('Чисел в массиве равных 0 -', n0)
print(arr)