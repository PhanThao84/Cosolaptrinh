# def check_divisible_by_3(binary_string):
#     # Tách chuỗi số nhị phân thành các phần tử của một List
#     binary_numbers = binary_string.split(',')

#     # Lọc ra các số nhị phân chia hết cho 3
#     divisible_by_3 = [num for num in binary_numbers if int(num, 2) % 3 == 0]

#     return divisible_by_3

# # Nhập chuỗi số nhị phân từ người dùng
# binary_string = input("Nhập vào một chuỗi số nhị phân, phân tách bởi dấu phẩy: ")

# # Kiểm tra và in các số nhị phân chia hết cho 3
# divisible_numbers = check_divisible_by_3(binary_string)

# # In kết quả
# if divisible_numbers:
#     result_string = ', '.join(divisible_numbers)
#     print("Các số nhị phân chia hết cho 3 là:", result_string)
# else:
#     print("Không có số nhị phân nào chia hết cho 3 trong chuỗi đã nhập.")
a = input()
b = a.split(',')
c = [num for num in b if int(num, 2) % 3 == 0]
if c:
    d = ', '.join(c)
    print(d)
else:
    print()

