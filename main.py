print('Введите коэффциент: a')
a = int(input())
print('Введите коэффциент: b')
b = int(input())
print('Введите коэффциент: c')
c = int(input())
D = (b ** 2) - (4 * a * c)
if D > 0:
    print('X1 =', (-b + D ** 0.5) / (2 * a), 'X2 =', (-b - D ** 0.5) / (2 * a))
if D == 0:
    print('X =', -b / (2 * a))
if D < 0:
    print('Корней нет')