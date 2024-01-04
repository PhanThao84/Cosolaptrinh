while True:
    n=int(input())
    if n>0:
        break
    else: 
        print('Khong hop le, nhap lai!')
L=[]
for i in range(n):
    so=int(input())
    L.append(so)
print(min(L))
print(max(L))