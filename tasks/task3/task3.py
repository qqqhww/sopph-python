a = int(input('Введите любое четырёхзначное число:'))
string = str(a)
if string[0] == string[3] and string[1]==string[2]:
    print('1')
else: print('0')
