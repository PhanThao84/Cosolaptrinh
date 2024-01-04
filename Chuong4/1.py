def Nhap():
    n=int(input('n='))
    return(n)
def Songuyen(n):
        for i in range(2,n+1,2):
            print(i,end=' ')
        return(i)       
def Nhapa():
    while True:
        a=input('Tiep tuc khong?')
        if a=='k' or a=='K':
            break
        else:
            n=int(input('n='))
n=Nhap()
i=Songuyen(n)
a=Nhapa()