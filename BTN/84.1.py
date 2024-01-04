def Nhap():
    x=float(input())
    y=float(input())
    z=float(input())
    return x,y,z
def trungvi(x,y,z):
    if x<y and y<z or x>y and y>z:
        return y
    if y>x and x>z or y<x and x<z:
        return x
    if z>x and y>z or z<x and z<y:
        return z
x,y,z=Nhap()
print('Gia tri Trung vi:',trungvi(x,y,z))