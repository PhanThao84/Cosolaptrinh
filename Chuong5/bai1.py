def nhap():
    x = int(input("Nhap x: "))
    k = int(input("Nhap k: "))
    n = int(input("Nhap n: "))
    L = []
    for i in range (n):
        n=int(input())
        L.append(n)        
    return x,k,n,L
def add(L, x, k):
    if k >= len(L):
        L.append(x)
    else:
        L = L[:k] + [x] + L[k:]
    return L
x,k,n,L=nhap()
L=add(L,x,k)
print( L)
# L=[5,7,8,6,4]
# print(L[:100])
# print(L[100:])