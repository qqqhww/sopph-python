N  = int(input('Введите любое шестизначное число:'))
n = str(N)
if len(n)!= 6:
    print('Напишите шестизначное число!!')
else:
    if int(n[0])+int(n[1])+int(n[2])==int(n[3])+int(n[4])+int(n[5]):
        print('лаки')
    else:
        print('анлаки')