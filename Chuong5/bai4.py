def Nhap():
    n = int(input(""))
    x=int(input())
    L = []
    for i in range(n):
        num = int(input("Nhap so nguyen: "))
        L.append(num)
        return L,x
    count = 0
    for num in L:
        count += 1
    return count
# n,x=Nhap()
# # def delete(L,x):
# #     i = 0
# #     while i < len(L):
# #         if L[i] == x:
# #             L.pop(i)
# #         else:
# #             i += 1
# #     return L
n,x, L = Nhap()
print("List ban dau: ", L)

