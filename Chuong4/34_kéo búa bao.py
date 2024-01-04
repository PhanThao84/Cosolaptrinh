import random
while True:
    a=int(input('Nguoi: '))
    r=random.randint(1,3)
    print('May: ',r)
    if a==1 and r==2:
        print('Ket qua: Nguoi thang')
    elif a==2 and r==3:
        print('Ket qua: May thang')
    elif a==r:
        print('Ket qua: Hoa')
    elif a==1 and r==3:
        print('Ket qua: May thang')   
    elif a==2 and r==1:
        print('Ket qua: May thang')
    elif a==3 and r==1:
        print('Ket qua: Nguoi thang')
    elif a==3 and r==2:
        print('Ket qua: May thang')
    if a==0 or a>=4 or a<1:
        break