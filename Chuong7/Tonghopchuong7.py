# upper(), lower()
#  Trả về một chuỗi được viết hoa hoặc viết thường
# isupper(), islower()
#  Trả về true hoặc false nếu một chuỗi (chữ cái) có được viết hoa hay viết
# thường toàn bộ xâu
# isalpha()
#  isalpha(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái và không có ký tự
# trắng, còn lại trả về False
# isnumeric(), isdecimal()
#  Trả về True nếu chuỗi chỉ chứa các ký tự chữ số và không có ký tự trắng, còn
# lại trả về False
# isalnum(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái hoặc chữ số và
# không có ký tự trắng, còn lại trả về False
# isspace(): trả về True nếu chuỗi chỉ chứa các ký tự trắng, hoặc dấu tab, hoặc
# dấu ngắt dòng, còn lại trả về False
# istitle(): trả về True nếu chuỗi chỉ chứa các từ, mỗi từ được viết thường và
# viết hoa chữ cái đầu, còn lại trả về False
#  startswith(str): Trả về True nếu chuỗi bắt đầu bởi chuỗi str;
#  endswith(str): Trả về True nếu chuỗi kết thúc bởi chuỗi str, còn lại trả về False
# Phương thức join(ListOfString)
#  join(ListOfString): ListOfString là một List gồm các chuỗi ký tự. join() dùng để
# nối các phần tử trong ListOfString bằng một chuỗi tương ứng của phương thức
# split(str): dùng để tách mỗi từ nằm trong chuỗi tương ứng thành một list, mỗi
# phần tử nằm trong list là một chuỗi con
# Phương thức rjust(n,ch), ljust(n,ch), center(n,ch)
#  Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tự ch, sao cho chiều dài của
# chuỗi đúng bằng n ký tự và chuỗi gốc được đặt nằm bên phải (rjust()), bên trái
# (ljust()) hoặc ở giữa (center())
# Phương thức rjust(n,ch), ljust(n,ch), center(n,ch)
#  Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tự ch, sao cho chiều dài của
# chuỗi đúng bằng n ký tự và chuỗi gốc được đặt nằm bên phải (rjust()), bên trái
# (ljust()) hoặc ở giữa (center())
# strip(str), rstrip(str), and lstrip(str)
#  Trả về một chuỗi mới trong đó đã xóa các ký tự có trong chuỗi str ở 2 đầu
# (strip()), bên phải (rstrip()) hoặc bên trái (lstrip()) chuỗi gốc.
# Phương thức find(str,n)
#  Thực hiện tìm chuỗi str trong chuỗi gốc, bắt đầu từ ký tự có số chỉ mục n, n
# để trống thì mặc định bằng 0.
#  Trả về vị trí (index) lần đầu được tìm thấy (từ trái sang phải). Nếu không tìm
# thấy thì trả về -1.
# Phương thức replace(oldvalue, newvalue, n)
#  Tìm và thay thế các chuỗi oldvalue xuất hiện trong chuỗi gốc bằng newvalue, với
# n lần tìm và thay thế;
#  Nếu không có n: thì mặc định là tất cả các lần xuất hiện.
#  Định dạng %
#  Dùng để nối chuỗi theo phương pháp tham số.
#  Các loại định dạng:

# ‐ %d: dữ liệu kiểu số nguyên (decimal);
# ‐ %g: dữ liệu kiểu số thực;
# ‐ %s: dữ liệu kiểu chuỗi (string);
# Bài 1: Viết chương trình:
# - Cho phép nhập vào một chuỗi ký tự bất kỳ;
# - Chương trình thực hiện đếm có bao nhiêu chữ cái in hoa, chữ cái in thường, chữ số và ký tự khác (bao
# gồm ký tự trắng) xuất hiện trong chuỗi trên;
# - In kết quả lên màn hình.
# TEST:
# Input: Python Programming Class @2021!
# Output:

# In hoa: 3
# In thuong: 19
# Chu so: 4
# Khac: 5
# n=input()
# a=0
# b=0
# c=0
# d=0
# for i in n:
#     if i.isupper():
#         a=a+1
#     elif i.islower():
#         b=b+1
#     elif i.isdigit():
#         c=c+1   
#     else:
#         d=d+1
# print('In hoa:',a,'\nIn thuong:',b,'\nChu so:',c,'\nKhac:',d)

# Bài 2: Viết chương trình:
# - Cho phép nhập vào một chuỗi ký tự bất kỳ;
# - Chương trình thực hiện làm sạch chuỗi ký tự trên. Biết rằng một chuỗi được gọi là “sạch” nếu:
# o Không bắt đầu và kết thúc bằng các ký tự trắng;
# o Mỗi từ chỉ được cách nhau bằng đúng 1 ký tự trắng;
# o Chỉ được phép viết hoa chữ cái đầu tiên của chuỗi;
# o Trước các dấu câu (phẩy, chấm phẩy, hai chấm, chấm) không có ký tự trắng;
# - In nội dung chuỗi sau khi xử lý lên màn hình.
# TEST:
# Input: Xin Chào , tôi là sInh viêN
# Output: Xin chào, tôi là sinh viên
# n=input('')
# n=n.strip()
# n=' '.join(n.split())
# n=n.lower()
# n=n.capitalize()
# for i in [',',';',':','.']:
#     n=n.replace(' '+ i, i)
# print(n)
# s= input()
# s=s.strip()  
# s=" ".join(s.split())  
# s=s.capitalize()  
# s=s.replace(" ,", ",")  
# s=s.replace(" ;", ";")  
# s=s.replace(" :", ":")  
# s=s.replace(" .", ".")  
# print(s)

# Bài 3: Hệ thống Elearning của Trường Đại học Kinh tế, Đại học Đà Nẵng cho phép người dùng đổi mật
# khẩu khi cần thiết. Để đảm bảo tính an toàn và bảo mật thông tin cho sinh viên, hệ thống yêu cầu mật
# khẩu phải được đáp ứng các yếu tố an toàn. Bạn hãy viết chương trình để thực hiện kiểm tra tính hợp lệ
# của mật khẩu mà người dùng nhập vào. Biết rằng, chính sách mật khẩu được quy định như sau:
# - Ít nhất 1 chữ cái nằm trong [a-z]
# - Ít nhất 1 số nằm trong [0-9]
# - Ít nhất 1 kí tự nằm trong [A-Z]
# - Ít nhất 1 ký tự nằm trong [$ # @]
# - Độ dài mật khẩu tối thiểu: 6 ký tự
# - Độ dài mật khẩu tối đa: 17 ký tự
# Trong đó, Input là một chuỗi ký tự được đặt làm mật khẩu, Output là True nếu hợp lệ, còn lại là False.
# TEST1:
# Input: ChucQuaMon@2021
# Output: True

# TEST2:
# Input: IAmFine
# Output: False

# Gợi ý: Sử dụng hàm re.search("[a-z]",st) cho phép kiểm tra các ký tự trong chuỗi st có chứa chữ cái
# trong tập [a-z] hay không. Dùng lệnh Import re để khai báo thư viện re.
# import re
# password = input()
# if len(password) < 6 or len(password) > 17:
#     print(False)
# else:
#     # Kiểm tra các yêu cầu về định dạng mật khẩu
#     if not re.search("[a-z]", password):
#         print(False)
#     elif not re.search("[0-9]", password):
#         print(False)
#     elif not re.search("[A-Z]", password):
#         print(False)
#     elif not re.search("[$#@]", password):
#         print(False)
#     else:
#         print(True)
# import re
# def matkhau(password):
#     if len(password) < 6 or len(password) > 17:
#         return False
#     if not re.search("[a-z]", password):
#         return False
#     if not re.search("[0-9]", password):
#         return False
#     if not re.search("[A-Z]", password):
#         return False
#     if not re.search("[$#@]", password):
#         return False
#     return True
# password=input()
# print(matkhau(password))
# # Test các trường hợp
# password1 = "ChucQuaMon@2021"
# print(validate_password(password1))  # Output: True

# password2 = "IAmFine"
# print(validate_password(password2))  # Output: False

# Bài 4: Viết chương trình:
# - Nhập vào một chuỗi gồm các từ được phân tách bởi dấu phẩy;
# - Chương trình thực hiện loại bỏ các từ trùng lắp, sau đó sắp xếp các từ theo thứ tự bảng chữ cái, phân
# tách nhau bởi dấu phẩy rồi in kết quả ra màn hình.
# TEST:
# Input: without,hello,bag,world,bag,hello
# Output: bag,hello,without,world
# Gợi ý:
# - Tách mỗi từ trong chuỗi thành các phần tử của một List;
# - Loại bỏ các phần tử trùng trong List;
# - Dùng hàm sort() để ắp xếp các phần tử trong List theo thứ tự;
# - Sử dụng hàm join() để chuyển List thành chuỗi theo yêu cầu.
# def xoatrunglapvasapxep(x):
#     a = x.split(',')
#     c = list(set(a))
#     c.sort()
#     d = ','.join(c)
#     return d
# x = input("Nhập vào một chuỗi các từ, phân tách bởi dấu phẩy: ")
# e = xoatrunglapvasapxep(x)
# print(e)

# Bài 5: Viết chương trình:
# - Nhập vào một chuỗi gồm các số nguyên, mỗi số cách nhau bởi một dấu cách; và một số nguyên X;
# - Chương trình thực hiện tìm X trong dãy số trên, in lên màn hình thứ tự xuất hiện của X nếu có. Nếu
# không tìm thấy thì trả về 0;
# Gợi ý:
# - Sử dụng hàm split() để tách mỗi số thành các phần tử của một List;
# - Dùng hàm int(x) để chuyển một chuỗi số sang số nguyên;
# TEST1:
# Input: 1 30 44 12 15 24 93 100 24 52 15 34
# 15
# Output: 5
# 11
# TEST2:
# Input: 44 12 24 93 100 24 52
# 15
# Output: 0
# a = input()
# x = int(input())
# numbers = a.split()
# numbers = [int(num) for num in numbers]
# b = [i + 1 for i, num in enumerate(numbers) if num == x]
# if b:
#     print('\n'.join(map(str,b)))
# else:
#     print(0)

# Bài 6: Viết chương trình:
# - Cho phép nhập vào một chuỗi là các số nhị phân 4 chữ số, phân tách bởi dấu phẩy;
# - Chương trình kiểm tra xem các số nhị phân trên có chia hết cho 3 không.
# - In lên màn hình dãy số nhị phân chia hết cho 3, nếu có nhiều số thì mỗi số cách nhau bởi 1 dấu phẩy.
# TEST1:
# Input: 0110,0010,1001,1010
# Output: 0110,1001

# TEST2:
# Input: 0100,0010,1010,1000
# Output:

# Gợi ý:
# - Sử dụng hàm split() để tách mỗi số thành các phần tử của một List;
# - Hàm int(x,2) cho phép chuyển số nhị phân x sang số nguyên;
# - Sử dụng hàm join() để nối các số nhị phân chia hết cho 3 thành 1 chuỗi.
# a = input()
# b = a.split(',')
# c = [num for num in b if int(num, 2) % 3 == 0]
# if c:
#     d = ', '.join(c)
#     print(d)
# else:
#     print()

# Bài 7. Viết chương trình:
# - Nhập vào một chuỗi ký tự chứa họ tên và email;
# - Chương trình thực hiện tách email từ chuỗi trên và in kết quả lên màn hình;
# - Biết rằng dữ liệu nhập vào có email hoặc không có email.
# Ví dụ:
# Ho ten: Nguyen Van An, Email: vanan@gmail.com
# Ho ten: Le Ngoc Binh, Email:
# Ho ten: Pham Anh Ngoc, Email: anhngoc@gmail.com
# TEST1:
# Input: Ho ten: Nguyen Van An, Email: vanan@gmail.com
# Output: vanan@gmail.com
# TEST2:
# Input: Ho ten: Le Ngoc Binh, Email:
# Output:
# a = input()
# b= a.rfind(" ")
# email = a[b+ 1:]
# if "@" in email:
#     print(email)
# else:
#     print()
# a = input()
# email_start = a.find("Email:")
# if email_start != -1:
#     email = a[email_start + len("Email:"):].strip()
#     print(email)
# else:
#     print()



