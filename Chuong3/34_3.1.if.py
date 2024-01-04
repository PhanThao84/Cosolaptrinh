a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
if max<b:
    max=b
    print('SLN=',b,sep='')
else:
    print('SBN=',b,sep='')
if max<c:
    max=c
    print('SLN=',c,sep='')
else:
    print('SBN=',c,sep='')

