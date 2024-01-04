while True:
    a=float(input('a='))
    b=float(input('b='))
    c=input('Toantu:')
    if c=='+':
        print('a+b=',a+b)
    elif c=='-':
        print('a-b',a-b)
    elif c=='*':
        print('a*b',a*b)
    else:
        print('a/b=',a/b)
    e=input('Tiep tuc:')
    if e=='t' or e=='T':
        break
    