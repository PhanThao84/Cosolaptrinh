def Nhap():
    n=int(input('n='))
    return n
def inkq(n):
      while True:
        for i in range (1,n+1):
            if i%2==0:
                print(i,end=' ')
        d=input('\nTiep tuc khong?')
        if d=='k' or d=='K':
            break
        else:
            n=int(input())
n=Nhap()
inkq(n)

# def nhap():
#     n = int(input("Nhập số nguyên n >= 2: "))
#     while n < 2:
#         n = int(input("Nhập lại số nguyên n >= 2: "))
#     return n

# def inkq(n):
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             print(i, end=" ")

# while True:
#     n = nhap()
#     inkq(n)
#     check = input("\nTiếp tục không? (k/K để kết thúc): ")
#     if check == 'k' or check == 'K':
#         break