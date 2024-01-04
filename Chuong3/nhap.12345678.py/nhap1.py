#VONG LAP
#Tính tổng S(n) = 1 + 2 + 3 + … + n.
#C1: n=int(input('))
#i=1
#S=0
#while i<=n:
    #S=S+i
    #i=i+1
#print('Gia tri cua S:',S)
#C2: 
#n=int(input(''))
#i=1
#S=0
#for i in range (0,n+1):
    #S=S+i
    #i=i+1
#print('Gia tri S',S)   
#Tính tổng S(n) = 1^2 + 2^2 + … + n^2 bằng Python
#n=int(input(''))
#i=1
#S=0
#for i in range (n,n+1):
    #S=S+i**2
#print('Tong so la:',S)

#Tính S(n) = 1 + ½ + 1/3 + … + 1/n
#n=int(input(''))
#i=1
#S=0
#for i in range (1,n+1):
    #S=S+1/i
#print('Tong S:',S)

#Tính S(n) = ½ + ¼ + … + 1/2n
#n=int(input(''))
#S=0
#i=0
#for i in range (1,n+1):
    #S=S+1/(2*i)
#print('Gia tri S:',S)

#Tính S(n) = 1/3 + 1/5 + … + 1/(2n + 1)
#n=int(input(''))
#i=0
#S=0
#for i in range (1,n+1):
    #S=S+1/(2*i+1)
#print('Gia tri S:',S)

#Liệt kê tất cả các ước số của số nguyên dương n bằng Python
#print('Nhap vao so N can tim uoc:')
#n=int(input(''))
#for i in range (1,n+1):
    #if (n%i==0):
        #print(i,end=' ')
        
#Tính tổng tất cả các ước số của số nguyên dương N bằng Python
#n=int(input(''))
#S=0
#for i in range (1,n+1):
    #if n%i==0:
        #S=S+i
#print('Gia tri S',S)

#ước số lẻ lớn nhất của một số bằng Python
#n=int(input())
#a=0
#for i in range (n+1,1,-1):
    #if (n%i==0 and i%2!=0):
        #a=i
        #break
#print('Uoc so le lon nhat cua', n ,'la',a)

#Kiểm tra một số có phải là số hoàn hảo bằng Python
#n=int(input())
#S=0
#for i in range (1,n):
    #if(n%i==0):
        #S=S+i
#if S==n:
    #print(n,'la so hoan hao')
#else:
    #print(n,'khong phai la so hoan hao')
    
#Kiểm tra số chính phương bằng Python
#C1:n=int(input())
#a=False
#for i in range (1,n+1):
    #if (i**2==n):
        #a=True
        #break
#if (a==True):
    #print(n,'la so chinh phuong')
#else:
    #print(n,'khong phai la so chinh phuong')
    
#C2:n=int(input())
#for i in range (1,n+1):
    #if i**2==n:
        #print(n,'la so chinh phuong')
        #break
#else:
    #print('khong phai la so chinh phuong')
    
#Kiểm tra số nguyên tố bằng Python
#C1n=int(input())
#if n%2==0:
    #print(n,'khong la so nguyen to')
#else:
    #print(n,'la so nguyen to')    
#C2:n=int(input())
#a=True
#if n<2:
    #a=False
#elif n==2:
    #a=True
#elif n%2==0:
    #a=False
#else:
    #for i in range (3,n,2):
        #if n%i==0:
           #a=False
#if a==True:
    #print(n,'la so nguyen to')
#else:
    #print(n,'khong phai la so nguyen to')\
#C3:n=int(input())
#for i in range (2,n,2):
    #if n/2==0:
        #print(n,'khong la so nguyen to')
    #else:
        #print(n,'la so nguyen to')
    #break
    
#Đảo ngược một số bằng Python
#n=int(input())
#while n!=0:
    #print(n%10,end='')
    #n=n//10#chia lấy phần  nguyên 
    
#In ra từng ký tự của một số bằng Python
#print("Nhập vào số N cần tách: ")
# Lấy dữ liệu
#n = int(input())
#so_dao_nguoc = "" 
# B1: Đảo ngược số cần in ra
#while (n != 0):
    #so_dao_nguoc += str(n % 10)
    #n = n // 10  # Chia lấy phần nguyên
# B2: In lần lượt các ký tự từ cuối đến đầu của số đã đảo
#so_dao_nguoc = int(so_dao_nguoc, 10) # Đổi string sang int
#while (so_dao_nguoc != 0):
    #print(so_dao_nguoc % 10, end= ' - ')
    #so_dao_nguoc = so_dao_nguoc // 10  # Chia lấy phần nguyên

#Giải phương trình bậc nhất một ẩn bằng Python (ax + b = 0)
#C1:print('Nhap vao so a:')
#a=int(input())
#if a==0:
    #print('Vui long nhap so a khac :')
    #a=int(input())
#print('Nhap vao so b:')
#b=int(input())
#print('Nghiem cua phuong trinh la x=',(-b/a))

#Giải phương trình bậc hai một ẩn bằng Python (ax^2 + bx + c = 0)
#import math
#print('Nhap vao so a: ')
#a=int(input())
#print('Nhap vao so b:')
#b=int(input())
#if a==0 and b==0:
    #print('Mot trong hai so a va b phai khac 0')
    #print('Nhap lai so a')
    #a=int(input())
    #print('Nhap lai vao b')
    #b=int(input())
#print('Nhap vao so c:')
#c=int(input())
#d=b**2-4*a*c
#if d>0:
    #print('Phương trinh có 2 nghiem phan biet')
    #print('x1=',(-(b)+d/(2*a)))
    #print('x2=',(-(b)-d/(2*a)))
#if d==0:
    #print('Phuong trinh co nghiem kep x1,x2=',(-b/2*a))
#if d<0:
    #print('Phuong trinh vo nghiem')
    
#a,b=map(int,input().split())
#for i in range (a,b+1):
      #print(i,end=' ')