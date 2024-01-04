def nhap():
    x = int(input(" "))
    n = int(input(" "))
    L = []
    for i in range(n):
        num = int(input("Nhap so nguyen: "))
        L.append(num)
    return x,L
def replace(L, x, y):
    for i in range(len(L)):
        if L[i] == x:
            L[i] = y
    return L
x, L = nhap()
y = int(input(""))
L = replace(L, x, y)
print(L)
