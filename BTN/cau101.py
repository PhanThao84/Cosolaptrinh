import math
def Nhap():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=(a*d+b*c)
    f=(b*d)
    return a,b,c,d,e,f
def rutgonphanso(e,f):
    g=math.gcd(e,f)
    h=e//g
    k=f//g
    return h,k
a,b,c,d,e,f=Nhap()
h,k=rutgonphanso(e,f)
print('Tong cua 2 phan so:',h,"/",k)
