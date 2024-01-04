# print('Lap Trinh Khong Kho')CBO1

#a,b=[int(x)for x in input().split()]CBO2
#print(a+b)

# a,b,c=[int(x)for x in input().split()]CB03
# d=a+b+c
# print(d)

# a,b=[int(x) for x in input().split()]CB04
# if b==0:
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print('INF')
# else:
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print('{:.2f}'.format(a/b))

# a,b=[int(x)for x in input().split()]
# d=a%b
# print(d)

# def Nhap(): CB06
#     d,r=[int(x) for x in input().split()]
#     return d,r
# d,r=Nhap()
# print((d+r)*2)
# print(d*r)

# pi=3.14  CB07
# def bankinh():
#     r=float(input())
#     return r
# r=bankinh()
# print(pi*2*r,pi*r**2)

# def Nhap(): CBO8
#     a,b=[int(x) for x in input().split()]
#     return a,b
# a,b=Nhap()
# print(a,'+',b,"=",a+b)

# def Nhap(): DK01
#     a,b=[int(x) for x in input().split()]
#     return a,b
# def sosanh(a,b):
#     max=a
#     if a<b:
#         max=b
#     return max
# a,b=Nhap()
# d=sosanh(a,b)
# print(d)

# def Nhap():DK02
#     a,b,c=[int(x) for x in input().split()]
#     return a,b,c
# def sosanh(a,b,c):
#     max=a
#     if b>a and b>c:
#         max=b
#     else:
#         max=c
#     return max
# a,b,c=Nhap()
# d=sosanh(a,b,c)
# print(d)

# def Nhap():DKO3
#     a,b=map(int,input().split())
#     return a,b
# def chenhlech(a,b):
#     print(abs(a-b))
# a,b=Nhap()
# chenhlech(a,b)

# C1# def Nhap(): DK04
#     n=float(input())
#     return n
# def lamtronso(n):
#     if n>0:
#         if (n+0.5)>=int(n)+1:
#             print(int(n)+1)
#         else:
#             print(int(n))
#     else:
#         if (n-0.5)<=int(n)-1:
#             print(int(n)-1)
#         else:
#             print(int(n))
# n=Nhap()
# lamtronso(n)

# import math DK05
# def Nhap():
#     n=int(input())
#     return n
# def kiemtrasochinhphuong(n):
#     if n<=10**12:
#         if (math.sqrt(n))**2==n:
#             print('YES')
#         else:
#              print('NO')
# n=Nhap()
# kiemtrasochinhphuong(n)

# c2 n=int(input())
# if n<=10**12:
#     b=0
#     for i in range (-10**5,10**5):
#         if i*i==n:
#             b=1
#             break
#     if b==1:
#         print('YES')
#     else:
#         print("NO")

# C1 def Nhap(): DK06
#     a,b=[int(x) for x in input().split()]
#     return a,b
# def Tinh(a,b):
#     if (a and b)<=1000:
#         if a!=0:
#             if b==0:
#                 print('INF')
#             if b!=0:
#                 print(round((-b/a),2))
#         elif a==0:
#             if b==0:
#                 print('INF')
#         else:
#             print('NO')
# a,b=Nhap()
# Tinh(a,b)

# c2 a, b=[int(x) for x in input().split()]
# if (a and b)<=1000:
#     if a==0 and b==0:
#         print('INF')
#     elif a==0 and b!=0:
#         print('NO')
#     else:
#         print("{:.2f}".format(-b/a))

# import math  DK07
# def Nhap():
#     a,b,c=[int(x) for x in input().split()]
#     return a,b,c
# def giaipt(a,b,c):
#         d=b**2-4*a*c
#         return d
# def ketqua(d):
#     if a!=0:
#         if d>0:
#             e=round((-b-math.sqrt(d))/(2*a),2)
#             f=round((-b+math.sqrt(d))/(2*a),2) 
#             print(e,f)
#         if d==0:
#             print(round((-b/2*a),2))
#         if d<0:
#             print('NO')
#     if a==0:
#         if c==0:
#             print(0)
#     if b==0:
#         if a==0:
#             print('NO')
#         if c==0:
#             print('0')
#     if b!=0:
#         if a==0:
#             print(round((-c/b),2))
#     if c==0:
#         g=round((-b-math.sqrt(d))/(2*a),2)
#         h=round((-b+math.sqrt(d))/(2*a),2)
#         print(g,h)                       
# a,b,c=Nhap()
# d=giaipt(a,b,c)
# ketqua(d)

#DK08 C1 def Nhap():
#     g=input().split()
#     a=float(g[0])
#     c=(g[1])
#     b=float(g[2]) 
#     return a,c,b 
# def Tinhtoan(a,c,b):
#         if "+" in c:
#             d=float(a)+float(b)
#             print(round(d,2))
#         if "-" in c:
#             e=float(a)-float(b)
#             print(round(e,2))
#         if "*" in c:
#             f=float(a)*float(b)
#             print(round(f,2))
#         if "/" in c:
#             if b==0:
#                 print("Math Error")
#             else:
#                 h=float(a)/float(b)      
#                 print(round(h,2))
# a,c,b=Nhap()
# Tinhtoan(a,c,b)
 
# C2a, c, b = input().split()
# a = float(a)
# b = float(b)
# if c == '+':
#     print("{:.2f}".format(a + b))
# if c == '-':
#     print("{:.2f}".format(a - b))
# if c == '*':
#     print("{:.2f}".format(a * b))
# if c == '/':
#     if b == 0:
#         print("Math Error")
#     else:
#         print("{:.2f}".format(1.0 * a / b))             

# n=int(input())  DK09
# if n <= 0 or n > 100000:
#     print("INVALID")
# elif n%4==0 and n%100!=0 or  n%400==0:
#     print('YES')
# else:
#     print('NO')

# month,year=map(int,input().split())
# if year < 0 or year >= 100000 and month<0 or month>=100:
#     print("INVALID")
# if month==2:    
#     if year%4==0 and year%100!=0 or year%400==0:
#         print('29')
#     else:
#         print('28')
# if month in [4,6,9,11]:
#     print('30')
# else:
#     print('31')

# import string
# import random
# def generate_password(lower_cases, upper_cases, digits, punctuations):
#   pass
#   password=""
#   for i in range(lower_cases):
#     password+="".join(random.choice(string.ascii_lowercase))
#   for i in range(upper_cases):
#     password+="".join(random.choice(string.ascii_uppercase))
#   for i in range(digits):
#      password+="".join(random.choice(string.digits))
#   for i in range(punctuations):
#       password+="".join(random.choice(string.punctuation))
#   password_list=list(password)
#   random.shuffle(password_list)
#   password="".join(password_list)
    # return password
# print(generate_password(1, 2, 3, 4))    

# Yêu cầu 1: Thực hiện lớp Employee

# Phương thức init nhận vào (id, name, age, base_salary, date_entered) để khởi tạo 5 thuộc tính self.id, self.name, self.base_salary, self.date_entered.
# Phương thức get_salary() trả về số lương của nhân viên, được tính lương như sau:
# Nếu age từ 17 trở xuống thì công thức tính lương sẽ là: baseSalary + 0*baseSalary.
# Nếu age thuộc [18, 25] thì công thức tính lương sẽ là: baseSalary + 0.03*baseSalary.
# Nếu age thuộc [26, 35] thì công thức tính lương sẽ là: baseSalary + 0.06*baseSalary.
# Nếu age từ 36 trở lên thì công thức tính lương sẽ là: baseSalary + 0.1*baseSalary.
# Thực hiện yêu cầu 1 trong cell này
# class Employee:
#   def __init__(self, id, name, age, base_salary, date_entered):
#     self.id = id
#     self.name = name
#     self.age = age
#     self.base_salary = base_salary
#     self.date_entered = date_entered
  
#   def get_salary(self):
#     pass
#     if self.age<=17:
#       return self.base_salary+0*self.base_salary
#     elif 18<=self.age<=25:
#       return self.base_salary+0.03*self.base_salary
#     elif 26<=self.age<=35:
#       return self.base_salary+0.06*self.base_salary
#     else:
#       return self.base_salary+0.1*self.base_salary

# Mot danh sach va mot tu, chen phan tu vao truoc moi phan tu trong danh sach
# In: dong 1 day tu cach nhau 1 khoang trang, dong 2 1 tu
# Out: In danh sach moi
# Red Green Black / Blue -> Blue Red Blue Green Blue Black
# def Nhap():
#     truoc_danh_sach=str(input())
#     phantu=str(input())
#     truoc_danh_sach=truoc_danh_sach.split()
#     return truoc_danh_sach,phantu
# def chenphantu(truoc_danh_sach,phantu):
#     danh_sach_moi=[]
#     for i in truoc_danh_sach:
#         danh_sach_moi.append(phantu)
#         danh_sach_moi.append(i)
#     return danh_sach_moi
# truoc_danh_sach,phantu=Nhap()
# danh_sach_moi=chenphantu(truoc_danh_sach,phantu)
# print(" ".join(danh_sach_moi)def kiem_tra_so_Armstrong(n):
# def kiem_tra_so_Armstrong(n):
#     chuoi_so = str(n)
#     so_chu_so = len(chuoi_so)
#     tong_luy_thua = 0
#     for ch in chuoi_so:
#         so = int(ch)
#         tong_luy_thua += so ** so_chu_so
#     if tong_luy_thua == n:
#         return True
#     else:
#         return False
# so = 153
# if kiem_tra_so_Armstrong(so):
#     print(so, "là số Armstrong.")
# else:
#     print(so, "không là số Armstrong.")
# so = 153
# chuoi_so = str(so)
# so_chu_so = len(chuoi_so)
# tong_luy_thua = 0
# for ch in chuoi_so:
#     so = int(ch)
#     tong_luy_thua += so ** so_chu_so
# if tong_luy_thua == so:
#     print(so, "là số Armstrong.")
# else:
#     print(so, "không là số Armstrong.")

# sinh_vien=["Hường","Phương Anh", "Hồng Nga", "Long", "Hiếu","Khôi"]
# diem_toan=[9,8,7,8,9,9]
# diem_ly=[10,8,9,9,8,10]
# diem_hoa=[9,10,8,9,9,9]
# dtb0=((diem_toan[0]+diem_ly[0]+diem_hoa[0])/3)
# dtb1=((diem_toan[1]+diem_ly[1]+diem_hoa[1])/3)
# dtb2=((diem_toan[2]+diem_ly[2]+diem_hoa[2])/3)
# dtb3=((diem_toan[3]+diem_ly[3]+diem_hoa[3])/3)
# dtb4=((diem_toan[4]+diem_ly[4]+diem_hoa[4])/3)
# dtb5=((diem_toan[5]+diem_ly[5]+diem_hoa[5])/3)
# print("Sinh vien",sinh_vien[0],"co diem trung binh la:",dtb0)
# print("Sinh vien",sinh_vien[1],"co diem trung binh la:",dtb1)
# print("Sinh vien",sinh_vien[2],"co diem trung binh la:",dtb2)
# print("Sinh vien",sinh_vien[3],"co diem trung binh la:",dtb3)
# print("Sinh vien",sinh_vien[4],"co diem trung binh la:",dtb4)
# print("Sinh vien",sinh_vien[5],"co diem trung binh la:",dtb5)
# sinh_vien=["Hường", "Phương Anh", "Hồng Nga", "Long", "Hiếu", "Khôi"]
# diem_toan=[9,8,7,8,9,9]
# diem_ly=[10,8,9,9,8,10]
# diem_hoa=[9,10,8,9,9,9]

# print(sinh_vien[2])
# print(diem_hoa[-1])
# print("Sinh viên", sinh_vien[0], "có điểm trung bình là:", str((diem_toan[0] + diem_ly[0] + diem_hoa[0])/3) + ".")

# Hãy viết chương trình để truy cập vào phần tử thứ i tính từ cuối danh sách ngược lại (từ phải sang trái). Với i là số nguyên được nhập từ bàn phím.
# my_list=[-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2,20.6, 11.5, 45.6]
# i = int(input())
# if i >= 0 and i <= len(my_list) - 1:
#   print("Phần tử thứ", i, "từ cuối lên của danh sách có giá trị là", str(my_list[-i]) + ".")
# elif i >= -len(my_list) and i <= -1:
#   print("Phần tử thứ", i, "từ cuối lên của danh sách có giá trị là", str(my_list[-i - 1]) + ".")
# else:
#   print(i, "list index out of range")


