import math
def Nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    if a!=0:
        d=b*b-4*a*c
        if d<0:
            print("Phuong trinh vo nghiem")
        if d==0:
            print('Phuong trinh co nghiem kep')
            print('x1=x2=',(-b/2*a),sep='')
        if d>0:
            print('Phuong trinh co hai nghiem')
            print('x1=',(-b+math.sqrt(d))/2*a,sep='')
            print('x2=',(-b-math.sqrt(d))/2*a,sep='')
def inkq(x1,x2):
    print(x1,x2)
a,b,c=Nhap()
giaipt(a,b,c)


