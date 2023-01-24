import math
list_a = list(map(int, input('Введите числа ').split()))
print('',list_a)
print(list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))