def LasoNguyenTo(x):
    if x<=1:
        return False
    else:
        for i in range(2,int(x/2)+1):
            if x%i==0:
                return False
        return True
def Sohople(x):
    if x<=1:
        return True
    else:
        return False
def Nhapvadem():
    print('Nhap day so:')
    S=0
    while True:
        x=int(input())
        if LasoNguyenTo(x)==True:
            S=S+1
        elif Sohople(x)==True:
            break
    return S
def inkq(kq):
    print('Co',kq,'so nguyen to')
kq=Nhapvadem()
inkq(kq)

