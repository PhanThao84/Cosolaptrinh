# Chương2
2.1
# n=input('Ho ten:')
# a=int(input('Tuoi:'))
# print('Chao ban',n,'Chuc mung sinh nhat thu',a,'!!!')
2.2
# n=int(input('Gia niem yet:'))
# a=int(input('Chiet khau:'))
# VAT=(n-a)*0.01
# b=n-a+VAT
# print('Gia ban:',b)
2.3
# P=int(input('Tien dau tu ban dau:'))
# n=int(input('So thang gui:'))
# r=float(input('Lai suat moi thang:'))
# b=P*(1+r*n)
# print('Tien lanh cuoi ky:',b)
2.4
# import math
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# s=(a+b+c)/2
# d=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print('Dien tich=',d)
# Ca nhan chuong 2
2.1
# n=input('Nhap ho ten:')
# print('Chao ban',n,'!!!')
2.2
# n=int(input('Nhap vao ban kinh cua duong tron:'))
# Pi=3.14
# s=Pi*n**2
# c=2*n*Pi
# print('Dien tich cua duong tron co ban kinh',n,'la=',s)
# print('Chu vi cua duong tron co ban kinh',n,'la=',c)
2.3
# import math
# print('Nhap hai canh ke cua tam giac vuong:')
# a=int(input())
# b=int(input())
# c=math.sqrt(a**2+b**2)
# print('Canh ke thu nhat la:',a,'Canh ke thu hai la:',b,'co canh huyen=',c)
2.4
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# d=float(input('d='))
# print('Tong=',a+b+c+d)
# print('Trung binh cong=',(a+b+c+d)/4)
2.5
# n=int(input('So tien ban dau:'))
# k=int(input('So thang gui:'))
# T=float(input('Lai suat/thang:'))
# print('Voi so tien ban dau',n,'sau',k,'thang gui','lai suat',T,'/thang')
# print('Thi so tien nhan duoc cuoi ky la',n*(1+k*T))
# 2.6
# n=input('Ho ten:')
# a=int(input('So ngay cong:'))
# b=int(input('Don gia ngay cong:'))
# c=float(input('He so phu cap:'))
# d=int(input('Tam ung:'))
# print('Nhan vien:',n,' Co tien luong=',b*a*c,' Tam ung=',d,' va Thuc linh=',(b*a*c)-d,sep='')

# Chuong 3 (Part 1)
# vd 3.1-13: Tim so lon nhat giua hai so a va b
# a=int(input('a='))
# b=int(input('b='))
# max=a
# if max<b:
#     max=b
# print('So lon nhat la:',max)
# vd 3.1-14: Giai phuong trinh bat nhat:ax+b=0
# a=int(input('a='))
# b=int(input('b='))
# if a==0:
#     if b==0:
#         print('Phuong trinh co vo so nghiem!!!')
#     else:
#         print('Phuong trinh vo nghiem!!!')
# else:
#     print('Phuong trinh co nghiem x=',(-b/a))
# vd 3.1-15:Giai va bien luan phuong trinh bac hai ax**2+bx+c=0
# import math
# print('Nhap a,b,c:')
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# d=b**2-4*a*c
# if d<0:
#     print('Phuong trinh vo nghiem!!!')
# elif d==0:
#     print('Phuong trinh co nghiem kep x1,x2=',(-b/2*a))
# else:
#     print('Phuong trinh co 2 nghiem:')
#     print('x1=',((-b+math.sqrt(d))/(2*a)))
#     print('x2=',((-b-math.sqrt(d))/(2*a)))
3.1
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# max=a
# if c>b and a>b and c>a:
#     print('SLN=',c)
#     print('SBN=',b)
# elif c>a and c>b and b>a:
#     print('SLN=',c)
#     print('SBN=',a)
# else:
#     print('SLN=',b)
#     print('SBN=',c)
3.2
# n=int(input('So may='))
# if n<=5:
#     print('So tien=',n*500)
# else:
#     print('So tien=',n*450)
3.3
# n=int(input('Tieu thu='))
# if 1<=n<=100:
#     a=n*550
# elif 101<=n<=150:
#     a=100*550+(n-100)*750
# elif 151<=n<=200:
#     a=100*550+50*750+(n-150)*950
# else:
#     a=100*550+50*750+50*950+(n-200)*1350
# VAT=a*(10/100)
# print('Phai tra=',a+VAT)
# Ca nhan chuong 3 (Part 1)
3.1
# import math
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# if (a+b)>c and (a+c)>b and (c+b)>a:
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print('Dien tich=',round(s,3))
# else:
#     print('Khong hop le')
3.2
# M1=int(input('M1='))
# M2=int(input('M2='))
# M3=int(input('M3='))
# S=int(input('S='))
# if S<=100:
#     print('Phaitra=',S*M1)
# elif 101<=S<=150:
#     print('Phaitra=',100*M1+(S-100)*20)
# else:
#     print('Phaitra=',100*M1+50*M2+(S-150)*M3)
3.3
# x=float(input('x='))
# y=float(input('y='))
# ch=input('Phep toan:')
# if ch=="+":
#     a=x+y
#     print(x,'+',y,'=',a,sep='')
# elif ch=='-':
#     a=x-y
#     print(x,'-',y,'=',a,sep='')
# elif ch=='*':
#     a=x*y
#     print(x,'*',y,'=',a,sep='')
# elif ch=="/":
#     if y==0:
#         print('Khong hop le')
#     else:
#         a=x/y
#         print(x,'/',y,'=',a,sep='')
3.4
# Toan=int(input())
# Ly=int(input())
# Hoa=int(input())
# ĐTB=(Toan*2+Ly*3+Hoa)/6
# if ĐTB<3:
#     print('Kem')
# elif 3<=ĐTB<5:
#     print('Yeu')
# elif 5<=ĐTB<6:
#     print('Trung binh')
# elif 6<=ĐTB<7:
#     print('Trung binh kha')
# elif 7<=ĐTB<8:
#     print('Kha')
# elif 8<=ĐTB<9:
#     print('Gioi')
# else:
#     print('Xuat sac')
3.5
# n=int(input())
# if n==0:
#     print('Xep loai A')
# elif n<2:
#     print('Xep loai B')
# elif n<4:
#     print('Xep loai C')
# else:
#     print('Xep loai D')
3.6
# a=float(input())
# b=float(input())
# c=float(input())
# if a>0 and b>0 and c>0 and (a+b>c) and (a+c>b) and (b+c)>a:
#     if (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==b*b+a*a):
#         print('Tam giac vuong')
#     elif (a==b) and (b==c) and (a==c):
#         print('Tam giac deu')
#     else:
#         print('Tam giac thuong')
# else:
#     print('Khong hop le')

# Chuong 3 (Part 2)
# vd 3.2-3 
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# vd 3.3-4
# num=1
# while num<=11:
#     if num%2==0:
#         print(num)
#     num=num+1
# vd 3.2-5
# n=int(input('Nhap so nguyen:(n>=1)'))
# i=1
# S=0
# while i<=n:
#     S=S+i
#     i=i+1  
# print('Tong S=',S)
# vd 3.2-6
# i=1
# while i<=6:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j=j+1
#     print('')
#     i=i+1
# vd 3.2-7
1
# n=int(input('n='))
# while n<=0:
#     print('Khong hop le!!!\nMoi nhap lai')
#     n=int(input('n='))
2
# while True:
#     n=int(input('n='))
#     if n<=0:
#         print('Khong hop le\nMoi nhap lai')
#     else:
#         break
3.1
# while True:
#     n=int(input())
#     if n<1 or n>50:
#         print('Yeu cau nhap lai')
#     else:
#         break
3.2 
# n = int(input("Nhập số nguyên n (1<=n<=50): "))
# # Tính số dòng cần in
# num_rows = (n + 9) // 10
# i = 1  # Biến đếm chữ số
# row = 1  # Biến đếm dòng
# while row <= num_rows:
#     column = 1  # Biến đếm cột trong mỗi dòng 
#     while column <= 10:
#         if i > n:
#             break       
#         print(i, end=" ")
#         i += 1
#         column += 1 
#     print()  # Xuống dòng sau khi in mỗi dòng
#     row += 1
3.3
# i = 1
# while i <= 9:
#     j = 1  
#     while j <= 9:
#         print(i * j, end="\t")
#         j += 1
#     print()
#     i += 1
# vd 3.2-9
# for i in range (5,10,2):
#     print(i)
# vd 3.2-10
# for i in range (5,-1,-1):
#     print(i)
# vd 3.2-11
# for i in range (5,10):
#     print(i)
# vd 3.2-12
# for i in range (6):
#     print(i)
# vd 3.2-14
# total=0
# for num in range (101):
#     total=total+num
# print(total)
# vd 3.2-15
# for i in range (12,16):
#     print(i)
# vd 3.2-16
# for i in range (0,10,2):
#     print(i)
# vd 3.2-17
# Cau truc for
# for i in range (1,11):
#     print(i)
# Cau truc While
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# vd3.2-18
# Cau truc for
# for i in range (1,11):
#     if i%2==0:
#         print(i)
# Cau truc while
# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i=i+1
# vd 3.2-20
# n=int(input('Nhap so nguyen:(n>=1)'))
# S=0
# for i in range (1,n+1):
#     S=S+i
# print('Tong=',S)
# vd 3.2-22
# for i in range (1,7):
#     for j in range (1,i+1):
#         print('*',end='')
#     print()
# Kenh Break
# i=1
# while i<=10:
#     print(i,'',end='')
#     if i%5==0:
#         break
#     i=i+1        
# lenh continue
# for i in range (1,11):
#     if i%2!=0:continue
#     print(i)
# vd
# S=0
# n=int(input('Nhap n='))
# for i in range(1,n+1):
#     print('So thu',i,':',sep='',end='')
#     x=int(input())
#     if x<0:
#         continue
#     elif x==0:
#         break
#     else:
#         S=S+x
# print('S=',S,sep='')

# Chuong 4
# vd 4.1
1
# n=int(input('Nhap mot so nguyen n\nn='))
# S=0
# for i in range (1,n+1):
#     S=S+i
#     i=i+1
# print('Tong cua',n,'so nguyen duong dau tien=',S)
2 
# def Nhap():
#     print('Nhap mot so nguyen:')
#     n=int(input('n='))
#     return n
# def Tinhtong(n):
#     S=0
#     for i in range(1,n+1):
#         S=S+1
#         i=i+1
#     return S
# def Inkq(S,n):
#     print('Tong cua',n,'so nguyen duong dau tien=',S,sep='')
# n=Nhap()
# S=Tinhtong(n)
# Inkq(n,S)
# vd 4.5a
# def hello():
#     print('Hello Alice')
# hello()
# vd4.5b
# def show_number():
#     for i in range(1,5):
#         print(i)
# show_number()
# vd4.6a
# def hello(name):
#     print('Hello ' + name)
# hello('Alice')
# hello('Bod')
# hello('Thao')
# vd4.6b
# def show_number(n):
#     for i in range(1,n+1):
#         print(i)
# show_number(4)
# show_number(10)
# vd 4.6c
# def show_number(m,n):
#     for i in range (m,n+1):
#         print(i)
# show_number(1,4)
# show_number(5,10)
# vd4.7a
# def show_number(n=10):
#     for i in range(1,n+1):
#         print(i)
# show_number(5)
# show_number()
# vd 4.7b
# def show_number(m=1,n=10):
#     for i in range (m,n+1):
#         print(i)
# show_number(3,7)
# show_number(3)
# show_number()
# vd4.8a
# def PhepCong(x,y=None):
#     if y==None:
#         return x
#     else:
#         return x+y
# kq1=PhepCong(5)
# kq2=PhepCong(5,2)
# print(kq1,kq2)
# vd4.8b
# def PhepCong(x=None,y=None):
#     return x+y
# kq1=PhepCong(5,2)
# kq2=PhepCong(x=5,y=2)
# kq3=PhepCong(y=2,x=5)
# print(kq1,kq2,kq3)
# vd4.9
# def Nhap():
#     n=int(input('Nhap mot so nguyen='))
#     return n
# n=Nhap()
# print('So nguyen da nhap=',n)
# vd 4.10
# def Nhap():
#     x=int(input('x='))
#     y=int(input('y='))
#     return x,y
# a,b=Nhap()
# print('Hai so nguyen da nhap=',a,b)
# vd 4.11
# def Tong_HieuHaiSoi(x,y):
#     return x+y,x-y
# x=10
# y=7
# a,b=Tong_HieuHaiSoi(x,y)
# print('Tong va hieu=',a,b)
# vd 4.13
# def Phepchia(x,y):
#     if y==0:
#         return None
#     else:
#         return x/y
# kq1=Phepchia(5,0)
# kq2=Phepchia(5,2)
# print(kq1,kq2)
# def Nhap():
#     n=int(input('n='))
#     return n
# def Nhapvadem(n):
#     a=0
#     for i in range (1,n+1):
#         x=int(input())
#         if x%2==0 and x!=0:
#             a=a+1
#     return a
# def Inkq(kq):
#     print('So chu so chan la:',kq)
# n=Nhap()
# kq=Nhapvadem(n)
# Inkq(kq)
# def NhapBankinh():
#     x=int(input('Bankinh='))
#     return x
# def Tinhchuvi(y):
#     Pi=3,14
#     Chuvi=y*Pi
#     return Chuvi
# Bankinh=NhapBankinh()
# Chuvi=Tinhchuvi(Bankinh)
# def Nhap():
#     x=int(input())
#     global y
#     y=5
#     return x+y
# kq=Nhap()
# print('y=',y)
# print('kq=',kq)
4.1
# def Nhap():
#     n=int(input('n='))
#     return n
# def cophaisonguyento(n):
#     if n%2!=0:
#         return True
#     else:
#         return False
# def Inkq(kq):
#     if kq:
#         print(n,'La SNT')
#     else:
#         print('n','Khong la SNT')
# n=Nhap()
# kq=cophaisonguyento(n)
# Inkq(kq)
4.2
# def LaSoNguyenTo(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
# def InNSoNguyenTo(n):
#     count = 0
#     num = 2
#     while count < n:
#         if LaSoNguyenTo(num):
#             print(num, end=" ")
#             count += 1
#         num += 1
# n = int(input("n= "))
# InNSoNguyenTo(n)
# 4.3
# def Nhap():
#     a = float(input('a = '))
#     b = float(input('b = '))
#     c = input('Toán tử: ')
#     return a, b, c
# def Thuchien(a, b, c):
#     if c == '+':
#         return a + b
#     elif c == '-':
#         return a - b
#     elif c == '*':
#         return a * b
#     elif c == '/':
#         if b == 0:
#             print('Không hợp lệ')
#         else:
#             return a / b
# def inkq(kq):
#     print('Kết quả:', kq)
# while True:
#     a, b, c = Nhap()
#     kq = Thuchien(a, b, c)
#     inkq(kq)
#     d = input('Tiếp tục? (Nhập T hoặc t để tiếp tục, bất kỳ phím nào khác để dừng): ')
#     if d == 'T' and d == 't':
#         break
# Chuong 5
# numbers=[item for item in range(1,6)]
# print(numbers)
# maxtrix=[[x,x+1,x+2] for x in range (1,10,3)]
# print(maxtrix)
# l=[[1,0,1,0] for x in range (1,4)]
# print(l)
# l=[1,1,1]
# l=[[x,x-1,x,x-1]for x in l]
# print(l)
# l=list('Python')
# print(l)
# maxtrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(maxtrix[0])
# print(maxtrix[1])
# print(maxtrix[2])
# print(maxtrix[0][0])
# print(maxtrix[0][1])
# print(maxtrix[0][2])
# sinhvien=['An','Binh','Minh','Lan','Ngoc']
# print(sinhvien[-1])
# print(sinhvien[-3])
# print(sinhvien[0])
# spam=[1,2,3,4,5,6]
# print(spam[2])
# print(spam[1:4])
# print(spam[2:5])
# print(spam[0:3])
# numbers=[1,2]
# print(numbers)
# numbers=numbers+[3,4]
# numbers=numbers+numbers
# print(numbers)
# myPets=['Zophie','Pôka','Fat-tail']
# print('Enter a pet name:')
# name=input()
# if name not in myPets:
#     myPets=myPets+[name]
#     print(name,'is my pet')
# while True:
#     n=input()
#     L=[]
#     if n not in L:
#         L=L+[n]
#     if n=="":
#         break
#     for i in L:
#         print(L)
# Hàm max()
#  Trả về phần tử có giá trị lớn nhất trong List
#  Hàm min()
#  Trả về phần tử có giá trị bé nhất trong List
# numbers = [5, 3, 8, 2, 9]
# print(max(numbers))
# print(min(numbers))
# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print(max(myPets))
# print(min(myPets))
# Xóa phần tử trong List với hàm del()
# spam=[1,2,3,4,5]
# del(spam[2])
# print(spam)
# del(spam[1])
# print(spam)
# students=["An","Binh","Lan","Thanh","Minh"]
# del(students[2])
# print(students)
# del(students[1])
# del(students[2])
# print(students)
# students=["An","Binh","Lan","Thanh","Minh"]
#Cách 1
# for x in students:
#     print(x ,end=", ")
#Cách 2: sử dụng cấu trúc for
# for x in range(len(students)):
#     print(students[x] ,end=", ")
#Cách 2: sử dụng cấu trúc while
# x=0
# while x<len(students):
#     print(students[x],end=", ")
#     x=x+1
# Phương thức (method)
#  Một phương thức có chức năng như một hàm được định nghĩa sẵn;
#  Cho phép xử lý dữ liệu trên đối tượng tương ứng;
#  Mỗi kiểu dữ liệu sẽ có tập phương thức riêng
# index(x) method
#  Trả về index của một phần tử được tìm thấy trong List;
#  Trong trường hợp x không tồn tại trong List sẽ bị lỗi  cần sử dụng
# cú pháp: if x in L để kiểm tra trước khi gọi phương thức index().
#  append(), insert() method
#  append(x) thêm phần tử x vào cuối List;

#  insert(i,x) chèn x vào vị trí có số chỉ mục i trong List;
# names =[1,2,3,4, 5, 6]
# names.append(6)
# print(names)
# names.insert(0,7)
# print(names)
# names.insert(-1,8)
# print(names)
# names.insert(100,5)
# print(names)
# remove() method
#  remove(x): xóa phần tử x đầu tiên tìm thấy trong List;
#  Trong trường hợp x không tồn tại trong List sẽ bị lỗi  cần sử dụng
# cú pháp: if x in L để kiểm tra trước khi gọi phương thức remove().
# remove() method
#  Phân biệt giữa hàm del() và phương thức remove()
# ‐ Hàm del() xóa một phần tử khi biết index
# ‐ Hàm remove() xóa một phần tử khi biết giá trị
# spam = ['cat', 'bat', 'rat', 'elephant']
#Cach 1
# del(spam[1])
# print(spam)
#Cach 2
# spam.remove('bat')
# print(spam)
L=[1,2,3,5,5,5,8,9,5]
# def xoaphantu(L):
#     for i in L:
#         if i==5:
#             L.remove(i)
# def inkq(kq):
#     for i in L:
#         print(i)
# kq=xoaphantu(L)
# inkq(kq)L = [1, 2, 3, 5, 5, 5, 8, 9, 5]
# def xoaphantu(L):
#     L = [item for item in L if item != 5]
#     return L
# def inkq(L):
#     for item in L:
#         print(item)
# kq = xoaphantu(L)
# inkq(kq)
# sort() method
#  Cho phép sắp xếp các phần tử trong List có thứ tự;
# spam=[5,4,3,2,1]
# spam.sort()
# print(spam)
# sort() method
#  Mặc định sắp xếp tăng dần, thêm tham số reverse=True để sắp xếp giảm
# dần;
# numbers = [1, 2, 3, 4, 5]
# numbers.sort() # or: numbers.sort(reverse=False)
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# sort() method
#  Lưu ý:
# ‐ Hàm sort() chỉ thực hiện được khi các phần tử có cùng kiểu dữ liệu;
# sort() method
#  Lưu ý:
# ‐ Hàm sort() chỉ thực hiện được khi các phần tử có cùng kiểu dữ liệu;
# reverse() method
#  Thực hiện đảo ngược thứ tự các phần tử trong List
# L=["Binh", "An","Nam","Anh", "A"]
# L.sort()
# print(L)
# L.reverse()
# print(L)
# clear() method
#  Thực hiện xóa tất cả các phần tử trong List
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.clear()
# print(numbers)
# count(x) method
#  Thực hiện đếm số phần tử x xuất hiện trong List
#  Ví dụ:
# numbers = [1, 2, 3, 2, 5]
# print(numbers.count(2))
# print(numbers.count(5))
# print(numbers.count(10))
# copy() method
#  Thực hiện tạo ra một bản sao mới của List
#  Ví du
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# numbers1 = [1, 2, 3, 4, 5]
# numbers2=numbers1.copy()
# print(numbers1)
# print(numbers2)
# pop(i) method
#  Thực hiện xóa và lấy ra giá trị của phần tử có số chỉ mục i trong
# List.
#  Nếu tham số i để trống thì mặc định là lấy phần tử cuối trong
# List.
# numbers = [1, 2, 3, 4, 5]
# x=numbers.pop(2)
# print(numbers)
# print(x)
# numbers = [1, 2, 3, 4, 5]
# x=numbers.pop()
# print(numbers)
# print(x)
# names = ['An','Nam','Binh','Ngoc']
# x1=names.pop(0)
# x2=names.pop(-1)
# print(x1)
# print(x2)
# print(names)
# names.remove('An')
# del(names[0])
# x=names.pop(-2)
# print(x)
# print(names)
# import copy
# numbers1 = [1,2,3,4,5]
# numbers2 = copy.copy(numbers1)
# print(numbers2)
# numbers3 = numbers1
# numbers3[2] =6
# print(numbers3)

# Chuong 7
# \t
# \n
# \\  
# str='Python Programming'
# str1=str[:6]
# print(str1)
# str2=str[7:]
# print(str2)
# str3=str2[0:3]
# print(str3)
# str4=str1[-4:]
# print(str4)
# str5=str[:2]+str[-4:]
# print(str5)
# str='Python Programming'
# str1=str[:6]
# str2=str[7:]
# print(str1 in str)
# print(str2 not in str)
# str3="PYTHON"
# print(str3 not in str)
# print('' in str)  
# st1=input()
# st2=input()
# while True:
#     if st2 in st1:
#         print('Nhap lai xau khac')
#         st2=input()
#     else:
#         break
# upper(), lower()
#  Trả về một chuỗi được viết hoa hoặc viết thường;  
# spam='Hello world!'
# print(spam.upper())
# print(spam.lower())
# print('How are you?')
# feeling=input()
# if feeling.lower()=='great':
#     print('I feel great too')
# else:
#     print('I hope the rest of your day is good')
#    Phương thức isupper(), islower()
#  Trả về true hoặc false nếu một chuỗi (chữ cái) có được viết hoa hay viết
# thường toàn bộ xâu;
# spam='Hello word'
# print(spam.islower())
# print(spam.isupper())
# st=input("str=")
# ch=input("ch=")
# dem=0
# for x in st.lower():
#     if x==ch.lower():
#         dem=dem+1
# print("Number of character "+ch+" is:",dem)
# Phương thức isalpha()
#  isalpha(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái và không có ký tự
# trắng, còn lại trả về False;
# str='1'
# print(str.isalpha())
# st2='abc'
# print(st2.isalpha())
# st3=' 76'
# print(st3.isalpha())
# Phương thức isnumeric(), isdecimal()
#  Trả về True nếu chuỗi chỉ chứa các ký tự chữ số và không có ký tự trắng, còn
# lại trả về False;
# str='1'
# print(str.isdecimal())
# while True:
#     print('Enter your age:')
#     age=input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age:')
# while True:
#     a=input()
#     b=input()
#     if a.isnumeric() and b.isnumeric():
#         print('(a+b)=',int(a)+int(b))
#         break
#     else:
#         print('Yêu cầu nhập lại')
# Phương thức isalnum()
#  isalnum(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái hoặc chữ số và
# không có ký tự trắng, còn lại trả về False;
# str1='123abc'
# print(str1.isalnum())
# while True:
#     print('Select a new pasword (letters and numbers only):')
#     password=input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')
# Phương thức isspace()
#  isspace(): trả về True nếu chuỗi chỉ chứa các ký tự trắng, hoặc dấu tab, hoặc
# dấu ngắt dòng, còn lại trả về False;  
# str='\n'
# print(str.isspace())
# str2=" "
# str3='cds1232'
# print(str2.isspace())
# print(str3.isspace())
# Phương thức istitle()
#  istitle(): trả về True nếu chuỗi chỉ chứa các từ, mỗi từ được viết thường và
# viết hoa chữ cái đầu, còn lại trả về False;
# str='Learn Python'
# print(str.istitle())
# a=input('Ho ten:')
# b=a.istitle()
# if b==False:
#     print('Khong hop le')
# else:
#     print('Hop le')
# while True:    
#     str=input()
#     if len(str)<8 or str.islower() or str.isupper() or str.isnumeric() or str.isalpha():
#         print("Khong hop le!!!")
#     else:
#         print("Hop le!!!")
#         break
st='''--Người---đâu-gặp---gỡ-làm-chi---
# Trăm----năm-biết-có---duyên---gì--hay--không.
# Ngổn-ngang---trăm-mối---bên---lòng----
# ----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
# def XuLyDong(xau):
#     L=xau.split("-")    # Tách mỗi từ trong xâu bằng dấu -
#     while "" in L:      # Xóa tất cả các ký tự rỗng trong list L
#         L.remove("")
#     return " ".join(L)  # Nối mỗi từ trong L thành một xâu st
# def TienXuLy(st):
#     L=st.split("\n")    # Tách mỗi dòng thành 1 phần tử của List L
#     for dong in L:
#         print(XuLyDong(dong))   #Xử lý từng dòng
# TienXuLy(st)Phương thức startswith(str), endswith(str)
#  startswith(str): Trả về True nếu chuỗi bắt đầu bởi chuỗi str;
#  endswith(str): Trả về True nếu chuỗi kết thúc bởi chuỗi str, còn lại trả về False;
# Có phân biệt chữ hoa và chữ thường
# str='Hello World'
# print(str.startswith('Hello'))
# join(ListOfString): ListOfString là một List gồm các chuỗi ký tự. join() dùng để
# nối các phần tử trong ListOfString bằng một chuỗi tương ứng của phương thức;
# str=['cat','dog','fish']
# print(''.join(str))
# Phương thức split()
#  split(str): dùng để tách mỗi từ nằm trong chuỗi tương ứng thành một list, mỗi
# phần tử nằm trong list là một chuỗi con;
# str='My name is Thao'
# print(str.split())
# print(str.split('My'))
# Phương thức rjust(n,ch), ljust(n,ch), center(n,ch)
#  Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tự ch, sao cho chiều dài của
# chuỗi đúng bằng n ký tự và chuỗi gốc được đặt nằm bên phải (rjust()), bên trái
# (ljust()) hoặc ở giữa (center());
# str='Hello'
# print(str.rjust(10))
# print(str.ljust(10))
# 'Hello'.center(20,'*')
# Phương thức strip(str), rstrip(str), and lstrip(str)
#  Trả về một chuỗi mới trong đó đã xóa các ký tự có trong chuỗi str ở 2 đầu
# (strip()), bên phải (rstrip()) hoặc bên trái (lstrip()) chuỗi gốc.
# spam=' hello World'
# print(spam.strip())
# st='AbbaTheAbbaSongsAbab'
# print(st.rstrip('ab'))
# print(st.lstrip('ab'))
# print(st.strip('Aab'))
# Phương thức find(str,n)
#  Thực hiện tìm chuỗi str trong chuỗi gốc, bắt đầu từ ký tự có số chỉ mục n, n
# để trống thì mặc định bằng 0.
#  Trả về vị trí (index) lần đầu được tìm thấy (từ trái sang phải). Nếu không tìm
# thấy thì trả về -1.
# word='banana'
# print(word.find('na'))
# replace(oldvalue, newvalue, n)
#  Tìm và thay thế các chuỗi oldvalue xuất hiện trong chuỗi gốc bằng newvalue, với
# n lần tìm và thay thế;
#  Nếu không có n: thì mặc định là tất cả các lần xuất hiện.
# string = "geeks for geeks geeks geeks geeks"
# print(string.replace("geeks", "Geeks"))
# print(string.replace("geeks", "GeeksforGeeks", 3))
# Định dạng %
#  Dùng để nối chuỗi theo phương pháp tham số.
#  Các loại định dạng:
# ‐ %d: dữ liệu kiểu số nguyên (decimal);
# ‐ %g: dữ liệu kiểu số thực;
# ‐ %s: dữ liệu kiểu chuỗi (string);
#  Ví dụ:
# n_decimal=3
# n_float=2.5
# st="Python"
# print("Toi da hoc " + st + " lan thu " + str(n_decimal) + ", trong " + str(n_float) + " nam")
# print("Toi da hoc %s lan thu %d, trong %g nam" % (st,n_decimal,n_float))
# chuoi = "Xin chào! Tôi là ChatGPT, một mô hình ngôn ngữ thông minh."
# tu = chuoi.split()
# print(''.join(tu))
