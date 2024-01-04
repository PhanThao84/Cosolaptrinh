# append(x) thêm phần tử x vào cuối List
# insert(i,x) chèn x vào vị trí có số chỉ mục i trong List
# remove(x): xóa phần tử x đầu tiên tìm thấy trong List
# Phân biệt giữa hàm del() và phương thức remove()
# ‐ Hàm del() xóa một phần tử khi biết index
# ‐ Hàm remove() xóa một phần tử khi biết giá trị
# sort() method
#  Mặc định sắp xếp tăng dần, thêm tham số reverse=True để sắp xếp giảm
# dần
# ‐ Hàm sort() chỉ thực hiện được khi các phần tử có cùng kiểu dữ liệu
# reverse() method
#  Thực hiện đảo ngược thứ tự các phần tử trong List
# clear() method
#  Thực hiện xóa tất cả các phần tử trong List
# count(x) method
#  Thực hiện đếm số phần tử x xuất hiện trong List
# copy() method
#  Thực hiện tạo ra một bản sao mới của Listpop(i) method
#  Thực hiện xóa và lấy ra giá trị của phần tử có số chỉ mục i trong
# List.
#  Nếu tham số i để trống thì mặc định là lấy phần tử cuối trong
# List.

# 5.1. Viết chương trình có sử dụng hàm thực hiện các yêu cầu sau:
# - Hàm Input(): nhập một số nguyên n (n>0) và n số nguyên lưu vào List L, và một
# số nguyên x;
# - Hàm FirstAndLast(L) trả về và in lên màn hình List mới chỉ gồm phần tử đầu
# tiên và cuối cùng của L;
# - Hàm Search(L,x): xác định x có nằm trong L hay không. Trả về True nếu tìm
# thấy, còn lại trả về False.
# Input: n=4
# 3
# 5
# 3
# 7
# x=5
# Output:[3, 7]
# True
# def Input():
#     L=[]
#     n=int(input('n='))
#     for i in range(n):
#         x=int(input())
#         L.append(x)
#     x=int(input('x='))     
#     return L,x
# def FirstAndlast(L):
#     return [L[0], L[-1]]
# def Search(L,x):
#     for i in L:
#         if x == i:
#             return True
#     return False
# L, x = Input()
# first_last = FirstAndlast(L)
# print(first_last)
# a=Search(L,x)
# if a == True:
#     print(True)
# else:
#     print(False)

# 5.2. Viết chương trình có sử dụng hàm thực hiện các yêu cầu sau:
# - Hàm Input(): nhập một số nguyên n (n>0) và n số nguyên lưu trữ vào một List L;
# - Hàm Search(L): Tìm và trả về số nhỏ nhất và lớn nhất trong List L;
# - Hàm Output(max, min): In lên màn hình số lớn nhất max và bé nhất min;
# Lưu ý: không được sử dụng hàm chuẩn max() và min() trong Python.
# Input: n=5
# 10
# 15
# 3
# 2
# 7
# Output:15 2
# def Input():
#     L=[]
#     n=int(input('n='))
#     for i in range(n):
#         n=int(input())
#         L.append(n)
#     return L
# def Search(L):
#     L.sort()
#     min=L[0]
#     max=L[-1]
#     return max,min
# def Output(max,min):
#    print(max,min)
# L=Input()
# max,min=Search(L)
# Output(max,min)

# 5.3. Nhập từ bàn phím một số nguyên n (n>0), và n số nguyên lưu trữ vào một List.
# In lên màn hình:
# - Số lượng các số nguyên DƯƠNG
# - Trung bình cộng của các số nguyên chẵn được lưu trữ trong
# List trên.
# Input:n=5
# 6
# -2
# -1
# 2
# 7
# Output:SND=3
#     TBC=2.0

# Input:n=4
# 3
# -5
# 1
# -7
# Output:SND=2
#     TBC=0
# L=[]
# n=int(input('n='))
# a=0
# S=0
# b=0
# for i in range(n):
#     x=int(input())
#     L.append(x)
# for x in L:
#     if x>0:
#         a=a+1
# for x in L:
#     if x%2==0:
#         S=(S+x)
#         b+=1
# if b>0:
#     S=S/b
# print('SND=',a,sep='')
# print('TBC=',S,sep='')

# 5.4.Nhập từ bàn phím một số nguyên n (n>0) và n số nguyên lưu vào List A:
# - Hãy đảo ngược giá trị của các phần tử trong List A và lưu vào List B. In giá trị các phần tử trong
# List B sau khi thực hiện đảo;
# - Sắp xếp và in lên màn hình List B sau khi được sắp xếp tăng dần;
# Input:n=5
# 3
# 1
# 4
# 2
# 5
# Output:[5, 2, 4, 1, 3]
# [1, 2, 3, 4, 5]
# Input:n=4
# 2
# 4
# 3
# 5
# Output:[5, 3, 4, 2]
# [2, 3, 4, 5]
# n=int(input('n='))
# listA=[]
# for i in range (n):
#     x=int(input())
#     listA.append(x)
# listB=listA
# listA.reverse()
# print(listB)
# listA.sort()
# print(listB)

# 5.5. Viết chương trình nhập vào một số nguyên n (n>0), và n số nguyên lưu trữ vào List A. In lên màn
# hình: tổng giá trị của các phần tử ở vị trí có thứ tự chẵn trong List A (biết rằng phần tử thứ 1 có số chỉ
# mục là 0 sẽ có thứ tự là 1, ...).
# Gợi ý: Để xác định phần tử ở vị trí chẵn, sử dụng cấu trúc lặp i=0..(n-1), nếu i lẻ tức là phần tử đó ở vị
# trí chẵn.
# n=5
# 8
# 10
# 12
# 4
# 7
# Tong=14

# n=6
# 1
# 23
# 15
# 30
# 12
# 49
# Tong=102
# L=[]
# n=int(input('n='))
# S=0
# for i in range(n):
#     x=int(input())
#     L.append(x)
# for i in range(1,n,2):
#         S+=L[i]
# print('Tong=',S,sep='')

# 5.6. Viết chương trình nhập vào từ bàn phím 10 số nguyên và lưu vào một List A. Hãy hoán đổi giá trị
# của 2 phần tử nằm cạnh nhau (theo từng đôi) trong List. Và in lên màn hình List kết quả sau khi xử lý.
# Gợi ý:
# - Để hoán đổi giá trị theo cặp phần tử, sử dụng thêm List B để lưu trữ tập kết quả
# - Cho vòng lặp i=0.. (n-2) step=2
# o B[i]=A[i+1]
# o B[i+1]=A[i]
# A=[]
# for i in range(10):
#     a=int(input())
#     A.append(a)
# B=[]
# for i in range(0, len(A)-1, 2):
#     B.append(A[i+1])
#     B.append(A[i])
# for a in B:
#     print(a,end=' ')

# 5.7. Viết chương trình nhập vào một số nguyên n (n>0) và n số nguyên lưu vào List L.
# Thực hiện loại bỏ những phần tử có giá trị trùng nhau và lưu tập mới vào List M. In
# lên màn hình các phần tử trong M.
# n=5
# 2
# 4
# 2
# 5
# 4
# 2 4 5
# n=int(input('n='))
# L=[]
# for i in range(n):
#     a=int(input())
#     while True:
#         if a not in L:
#             L=L+[a]
#         else: break
# for a in L:
#     print(a,end=" ")
# ** Phép mũ 2 ** 3 8
# % Chia lấy dư 5 % 2 1
# // Chia lấy nguyên 5 // 2 2
# / Chia 5 / 2 2.5
# * Nhân 5 * 3 15
# - Trừ 5 - 2 3
# + Cộng 2 + 2 4