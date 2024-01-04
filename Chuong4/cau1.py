while True:
    a=int(input(''))
    b=int(input(''))
    n=int(input(''))
    if a!=0 and b!=0:
        if a/b==n:
            print('/')
        elif a*b==n:
            print('*')
        elif a+b==n:
            print('+')
        elif a-b==n:
            print('-')
        else:
            print('N0')
    else:
        print('NO')