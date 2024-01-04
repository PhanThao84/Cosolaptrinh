# maxtrix=[[x,x+1,x+2,x+3]for x in range(1,13,4)]
# print(maxtrix)

# l=[[1,0,1,0] for x in range (1,4)]

# l=[1,1,1]
# l=[[x,x-1,x,x-1]for x in l]
# print(l)

# a=[1,2,3,4,5,6]
# print(a[-4:-1])

# spam=['Phan','Thị','Thanh','Thảo']

# myPets=['Zophie','Pooka','Fat-tail']
# print('Enter a pet name:')
# name=input()
# if name not in myPets:
#     print('I do not have a pet named',name)
# else:
#     print(name+'is my pet')

# spam=[1,2,3,4,5,6]
# print(len(spam))

# numbers=[5,3,8,2,9]
# print(max(numbers))
# print(min(numbers))

# spam=[1,2,3,4,5]
# del(spam[2])
# print(spam)

# students=['An','Bình','Lan','Thanh','Minh']
# del(students[2])
# print(students)

# C1students=['An','Bình','Lan','Thanh','Minh']
# for x in students:
#     print(x,end=',')

# students=['An','Bình','Lan','Thanh','Minh']
# for x in range(len(students)):
#     print(students[x],end=',')

# catNames=[]
# while True:
#     print(('Enter the name of cat'+str(len(catNames))+1)
#         +'(Or enter nothing to stop.):')
#     name=input()
#     if name=='':
#         break
#     catNames=catNames+[name]
# print('The cat names are:')
# for name in catNames:
#     print(''+name)

# num_list = []
# for i in range(10):
#     num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
#     num_list.append(num)

# # Nhập số nguyên x
# x = int(input("Nhập số nguyên x: "))

# # Thay thế các phần tử có giá trị bằng 5 bằng x
# for i in range(len(num_list)):
#     if num_list[i] == 5:
#         num_list[i] = x

# # In kết quả lên màn hình
# print("Kết quả sau khi thay thế các phần tử có giá trị bằng 5 bằng x là:")
# print(num_list)

# l = []
# for i in range(10):
#      num = int(input())
# x=int(input(''))
# for i in l:
#     if l[i]==5:
#         l[i]=x
# print(l)
    
# l = []
# for i in range(10):
#     n=int(input(''))
#     l=l+[n]
# x = int(input("Nhập số nguyên x: "))
# for i in range (len(l)):
#    if l[i] == 5:
#        l[i] = x
# print(l)

# l = []
# for i in range(10):
#     n=int(input(''))
#     l=l+[n]
# for i in range (len(l)):
#    if l[i] == 5:
#        l=l.remove(5)
# print(l)

# names=[1,2,3,4,5,6]
# names.append(6)
# print(names)

# names.insert(0,7)
# print(names)

# names.insert(-1,8)
# print(names)

# numbers=[1,2,3,4,5]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# l=['Bình','An','Nam','Anh','A']
# l.sort()
# print(l)
# l.reverse()
# print(l)

# numbers=[1,2,3,2,5]
# print(numbers.count(2))

# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     myPets=myPets+[name]
#     print(myPets)
# else:
#     print(name + ' is my pet.')

# def nhap():
#     l=[]
#     for i in range(10):
#         n=int(input(''))
#         l=l+[n]
#     x = int(input("Nhập số nguyên x: "))
#     return x,l
# def Inkq(l):
#     for x in l:
#         print(x,end=', ')
#         print()
# def câua(x,l):
#     for i in range (len(l)):
#         if l[i] == 5:
#             l[i] = x
#     Inkq(l)
# def câub(x,l):
#    i=0
#    while i<len(l):
#        if l[i]==x:
#            del(l[i])
#        else:
#            i+=1
#     Inkq(l)
    
# x,l=nhap()
# câua(x,l)
# câub(x,l)  

# def Nhap():
#     L=[]
#     for i in range(10):
#         k=int(input())
#         L=L+[k]
#     x=int(input("x="))
#     return x,L


# def InKQ(L):
#     for x in L:
#         print(x,end=", ")
#     print()


# def CauA(x,L):
#     for i in range(len(L)):
#         if L[i]==5:
#             L[i]=x
#     InKQ(L)
# def CauB(x,L):
#     i=0
#     while i<len(L):
#         if L[i]==x:
#             del(L[i])
#         else:
#             i+=1
   
#     InKQ(L)  
   
# x,L=Nhap()    
# CauA(x,L)
# CauB(x,L)  

# names = ['An', 'Nam','Binh','Ngoc']
# x=names.copy()
# print(x)
# print(x.count('Nam'))   

# names = ['An', 'Nam','Binh','Ngoc']
# x1=names.pop(0)
# x2=names.pop(-1)
# print(x1)
# print(x2)
# print(names)

# a=int(input('a='))
# if a!=0:
#     print(True)
# words=[]
# word=input()
# while word!="":
#     # Only add the word to the list if
#     # it is not already present in it
#     if word not in words:
#         words.append(word)
#         # Read the next word from the user
#     # Display the unique words
#     word=input()
# for word in words:
#     print(word)
    
# numbers = []
# while True:
#     user_input = input("Enter a number (leave blank to finish): ")
#     if not user_input:
#         break
#     numbers.append(float(user_input))

# average = sum(numbers) / len(numbers)
# below_average = []
# average_values = []
# above_average = []

# for number in numbers:
#     if number < average:
#         below_average.append(number)
#     elif number == average:
#         average_values.append(number)
#     else:
#         above_average.append(number)

# print(f"Average: {average}")
# print("Below average:")
# for number in below_average:
#     print(number)
# print("Average values:")
# for number in average_values:
#     print(number)
# print("Above average:")
# for number in above_average:
#     print(number)

# Nhập vào tập hợp các điểm
# points = []
# while True:
#     a= input("Nhập tọa độ x (nhấn Enter để kết thúc): ")
#     if a == "":
#         break
#     x=float(a)
#     y = float(input("Nhập tọa độ y: "))
#     points.append((x, y))

# # Tính giá trị của hệ số m và b
# n = len(points)
# sum_x = sum([point[0] for point in points])
# sum_y = sum([point[1] for point in points])
# sum_xy = sum([point[0]*point[1] for point in points])
# sum_x_squared = sum([point[0]**2 for point in points])
# m = (sum_xy - sum_x*sum_y/n) / (sum_x_squared - sum_x**2/n)
# b = sum_y/n - m*sum_x/n

# # Hiển thị công thức của đường thẳng tốt nhất
# print(f"Công thức của đường thẳng tốt nhất là y = {m:.2f}x + {b:.2f}")

# def tokenize(s):
#     tokens = []
#     token_2 = ""
#     for i in range(len(s)):
#         if s[i].isspace(): 
#  #  kiểm tra xem ký tự hiện tại trong biểu thức toán học có phải là khoảng trắng (space), tab (\t), newline (\n), carriage return (\r), form feed (\f), hay không.
#             continue
#         elif s[i] in "+-*/^()":
#             if len(token_2) > 0:
#                 tokens.append(token_2)
#                 token_2 = ""
#             tokens.append(s[i])
#         else:
#             token_2 += s[i]
#     if len(token_2) > 0:
#         tokens.append(token_2)
#     return tokens

# def main():
#     a = input("Nhập 1 chuỗi: ")
#     tokens = tokenize(a)
#     print(tokens)
# main()


