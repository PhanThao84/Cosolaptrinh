def Nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    if n<0:
        return
    a=1
    i=1
    for i in range (1,n+1):
        a=a*i
    return a
def inkq(n,X):
    print(n,'!=',X,sep='')
n=Nhap()
X=giaithua(n)
inkq(n,X)

    
    
    