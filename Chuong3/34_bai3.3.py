#a=float(input('x='))
#b=float(input('y='))
#ch=input('Phep toan=')
#if ch=='+':
    #e=a+b
    #print(a,'+',b,'=',round(e,1),sep='')
#elif ch=='-':
    #e=a+b
    #print(a,'-',b,'=',round(e,1),sep='')
#elif ch=='*':
    #e=a*b
    #print(a,'*',b,'=',round(e,1),sep='')
#elif ch=='/':
    #e=a/b
    #print(a,'/',b,'=',round(e,1),sep='')
#else:
    #print('Khong hop le')
#if ch=='/' and b==0:
    #print('Khong hop le')
a=float(input('x='))
b=float(input('y='))
ch=input('Phep toan:')
if ch=='+':
    print(a,'+',b,'=',round((a+b),1),sep='')
elif ch=='-':
    print(a,'-',b,'=',round((a-b),1),sep='')
elif ch=='*':
    print(a,'*',b,'=',round((a*b),1),sep='')
elif ch=='/' and b!=0:
    print(a,'/',b,'=',round((a/b),1),sep='')
else:
    print('Khong hop le')
