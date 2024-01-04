import re
password = input()
if len(password) < 6 or len(password) > 17:
    print(False)
else:
    # Kiểm tra các yêu cầu về định dạng mật khẩu
    if not re.search("[a-z]", password):
        print(False)
    elif not re.search("[0-9]", password):
        print(False)
    elif not re.search("[A-Z]", password):
        print(False)
    elif not re.search("[$#@]", password):
        print(False)
    else:
        print(True)

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
