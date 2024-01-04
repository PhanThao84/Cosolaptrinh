def Trungvi(a,b,c):
    if a<b and b<c or a>b and b>c:
        return b
    if b>a and a>c or b<a and a<c:
        return a
    if c>a and b>c or c<a and c>b:
        return c
def Trungbinhcuabathamso(a,b,c):
    return a+b+c-min(a,b,c)-max(a,b,c)
def Nhap():
    x=float(input())
    y=float(input())
    z=float(input())
    print('Gia tri trung vi:',Trungvi(x,y,z))
    print('Gia tri trung binh la:',Trungbinhcuabathamso(x,y,z))
Nhap()