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

# print('"Đen Vâu" is a rap singer'"\nHe's 32 years old""\nI want to become a rapper")  

# st='''Đường về nhà là vào tim ta
# Dẫu nắng mưa gần xa
# Thất bát, vang danh
# Nhà vẫn luôn chờ ta'''
# print(st)

# str1=input('')
# str2=input('')
# while True:
#     if str2 in str1:
#         str2=input('')
#     else:
#         break

# print('How are you?')
# feeling=input()
# if feeling.lower()=='great':
#     print('I feel great too')
# else:
#     print('I hope the rest of your day is good')   

# while True:
#     print('Enter your age:')
#     age=input()
#     if age==input:
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
       
# st=input("str=")
# ch=input("ch=")
# dem=0
# for x in st.lower():
#     if x==ch.lower():
#         dem=dem+1
# print("Number of character "+ch+" is:",dem)


# while True:
#     print('Select a new pasword (letters and numbers only):')
#     password=input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')
    
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

# st='''--Người---đâu-gặp---gỡ-làm-chi---
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


# TienXuLy(st)

# def Bai74(st):
#     return st.lower(), st.upper()
# st="Learning Python"
# st1,st2=Bai74(st)
# print(st1)
# print(st2)

# def Bai75(st):
#     chucai=0
#     so=0
#     kytudacbiet=0
#     for ch in st:
#         if ch.isnumeric():
#             so+=1
#         elif ch.isalpha():
#             chucai+=1
#         else:
#             kytudacbiet+=1
   
#     print("Chu cai:",chucai)
#     print("Chu so:",so)
#     print("Khac:",kytudacbiet)
   
# st="Python $ Programming % # & * ^ Class 2021"
# Bai75(st)

    
    