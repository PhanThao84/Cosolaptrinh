def tinh(n):
    giacoso=4
    if n*1000<=140:
        return giacoso
    else:
        giatien=giacoso+((n*1000)//140)*0.25
        return giatien

n=float(input('Quang duong di duoc la: '))
kq=tinh(n)
print('Voi quang duong di duoc la ',n,' km ' ,'thi phai tra ','$',kq,sep='')