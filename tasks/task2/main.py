n = int(input('Введите длину кольцевой дороги:'))
v = int(input('Введите скорость движения байкера:'))
t = int(input('Введите время байкера:'))
x = int()
if n > 0 and 0 <= n <= 1000 and -1000 <= v <= 1000 and 0 <= t <= 1000:
    if v > 0:
        x = (v * t) % n
        print(f'Он остановится на отметке', x, 'через', t, 'часов.')

    else:
        x = (n - ((abs(v) * t) % n))
        print(f'Он остановится на отметке', x, ' км через', t, 'часов.')

else:
    print('Невозможно')
