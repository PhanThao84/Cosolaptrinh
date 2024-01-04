def Nhap():
    x = int(input(""))
    n = int(input(""))
    L = []
    for i in range(n):
        num = int(input(""))
        L.append(num)
    return x,k,L
def delete(L, x):
    i = 0
    while i < len(L):
        if L[i] == x:
            L.pop(i)
        else:
            i += 1
    return L
x, k, L = Nhap()
L = delete(L, x)
print(L)
