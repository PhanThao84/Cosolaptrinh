def nhap():
    while True:
        diem=float(input())
        if diem>=0 and diem<=10:
            break
        else:
            print('Khong hop le!')
    return diem
diem1=nhap()
diem2=nhap()
diem3=nhap()
avg=(diem1+diem2+diem3)/3
print(avg)