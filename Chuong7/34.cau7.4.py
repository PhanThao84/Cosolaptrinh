# def remove_duplicates_and_sort(input_string):
#     # Tách chuỗi thành các từ
#     words = input_string.split(',')

#     # Loại bỏ các từ trùng lắp
#     unique_words = list(set(words))

#     # Sắp xếp các từ theo thứ tự bảng chữ cái
#     unique_words.sort()

#     # Gắn kết các từ lại thành chuỗi mới, phân tách bởi dấu phẩy
#     result_string = ','.join(unique_words)

#     return result_string

# # Nhập chuỗi từ người dùng
# input_string = input("Nhập vào một chuỗi các từ, phân tách bởi dấu phẩy: ")

# # Loại bỏ từ trùng lắp và sắp xếp các từ
# result_string = remove_duplicates_and_sort(input_string)

# # In kết quả
# print("Kết quả sau khi loại bỏ từ trùng lắp và sắp xếp là:", result_string)
def xoatrunglapvasapxep(x):
    a = x.split(',')
    c = list(set(a))
    c.sort()
    d = ','.join(c)
    return d
x = input("Nhập vào một chuỗi các từ, phân tách bởi dấu phẩy: ")
e = xoatrunglapvasapxep(x)
print(e)
