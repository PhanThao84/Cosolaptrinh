def Nhap():
    x = int(input("Nhap x: "))
    n = int(input("Nhap n: "))
    L = []
    for i in range(n):
        num = int(input(""))
        L.append(num)
    return x, L
def search(L, x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
x, L = Nhap()
index = search(L, x)
if index is None:
    print('None')
else:
    print(index)
