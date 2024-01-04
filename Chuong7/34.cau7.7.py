# # Nhập chuỗi ký tự chứa họ tên và email từ người dùng
# input_string = input("Nhập vào chuỗi ký tự chứa họ tên và email: ")

# # Tìm vị trí của dấu cách cuối cùng trong chuỗi
# last_space_index = input_string.rfind(" ")

# # Tách phần email từ chuỗi
# email = input_string[last_space_index + 1:]

# # Kiểm tra xem chuỗi có chứa email hay không
# if "@" in email:
#     print("Email được tìm thấy:", email)
# else:
#     print("Không tìm thấy email trong chuỗi.")
a = input()
b= a.rfind(" ")
email = a[b+ 1:]
if "@" in email:
    print(email)
else:
    print()
    
a = input()
email_start = a.find("Email:")
if email_start != -1:
    email = a[email_start + len("Email:"):].strip()
    print(email)
else:
    print()
