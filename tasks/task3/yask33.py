a, b = map(int, input('Введите координаты первой клетки:').split())
c, d = map(int,input('Введите координаты второй клетки:').split())
black = int()
white = int()
if (a+b)%2 == 0 and 0<a>10 and 0<b>10 and 0<c>10 and 0<d>10:
    black = a, b
else: white = a, b
if (c + d)%2 == 0 and 0<a>10 and 0<b>10 and 0<c>10 and 0<d>10:
    black = c, d
else:  white = c, d
if (black == a, b and black == c, d) or (white == a, b  and white == c, d):
    print('Клетки одинакового цвета')
else:
    print('Клетки разного цвета')



