L=[]
n=int(input('n='))
S=0
for i in range(n):
    x=int(input())
    L.append(x)
for i in range(1,n,2):
        S+=L[i]
print('Tong=',S,sep='')
# L = []
# n = int(input('n='))
# S = 0

# for i in range(n):
#     x = int(input())
#     L.append(x)

# for i in range(1, n, 2):
#     S += L[i]

# print(S)
# 5.5. Viết chương trình nhập vào một số nguyên n (n>0), và n số nguyên lưu trữ vào List A. In lên màn
# hình: tổng giá trị của các phần tử ở vị trí có thứ tự chẵn trong List A (biết rằng phần tử thứ 1 có số chỉ
# mục là 0 sẽ có thứ tự là 1, ...).

# Gợi ý: Để xác định phần tử ở vị trí chẵn, sử dụng cấu trúc lặp i=0..(n-1), nếu i lẻ tức là phần tử đó ở vị
# trí chẵn.
n=5
8
10
12
4
7
Tong=14
n=6
1
23
15
30
12
49
Tong=102