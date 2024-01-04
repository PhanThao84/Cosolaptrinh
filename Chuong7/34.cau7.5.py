# def find_number(sequence, x):
#     # Tách chuỗi số thành các phần tử của một List
#     numbers = sequence.split()

#     # Chuyển các phần tử trong List thành số nguyên
#     numbers = [int(num) for num in numbers]

#     # Tìm thứ tự xuất hiện của số X trong dãy số
#     if x in numbers:
#         index = numbers.index(x) + 1  # Vị trí bắt đầu từ 1
#         return index
#     else:
#         return 0

# # Nhập chuỗi số từ người dùng
# sequence = input("Nhập vào một chuỗi số nguyên, mỗi số cách nhau bởi dấu cách: ")

# # Nhập số nguyên X từ người dùng
# x = int(input("Nhập số nguyên X: "))

# # Tìm và in thứ tự xuất hiện của X trong dãy số
# result = find_number(sequence, x)
# print("Thứ tự xuất hiện của", x, "là:", result)
# Nhập chuỗi số từ người dùng
a = input()
x = int(input())
numbers = a.split()
numbers = [int(num) for num in numbers]
b = [i + 1 for i, num in enumerate(numbers) if num == x]
if b:
    print('\n'.join(map(str,b)))
else:
    print(0)

