def Nhap():
    n=int(input('n='))
    return n

def NhapVaDem(n):
    S=0
    print('Nhap',n,  'so nguyen:')
    for i in range (1,n+1):
        a=int(input())
        if a%2==0 and a!=0 :
            S+=1
    return S   

def InKQ(Kq): 
    print('So chu so chan la:',Kq)
n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)