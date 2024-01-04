while True:
    a=float(input('a='))
    b=float(input('b='))
    c=input('Toan tu:')
    if c=='+':
        e=a+b
        print(a,'+',b,'=',e,sep='',)
    elif c=='-':
        e=a-b
        print(a,'+',b,'=',e,sep='')
    elif c=='*':
        e=a*b
        print(a,'*',b,'=',e,sep='')
    elif c=='/':
        e=a/b
        print(a,'/',b,'=',e,sep='')
    d=input('Tiep tuc:')
    if d=="T" or d=='t':
        break
