# Chuyển đổi một chữ số thập lục phân sang một số nguyên
def hex2int(hex_digit):
    hex_digit = hex_digit.upper()
    if hex_digit.isdigit():
        return int(hex_digit)
    elif hex_digit.isalpha() and hex_digit.isalnum():
        return ord(hex_digit) - ord('A') + 10
    else:
        print("Lỗi: Giá trị không hợp lệ được cung cấp.")
        exit()
# Chuyển đổi một số nguyên sang một chữ số thập lục phân
def int2hex(int_digit):
    if int_digit < 10:
        return str(int_digit)
    else:
        return chr(int_digit - 10 + ord('A'))
# Chuyển đổi một số từ cơ số tùy ý sang cơ số 10
def convert_to_base_10(num, base):
    decimal = 0
    for digit in num:
        decimal = decimal * base + hex2int(digit)
    return decimal
def convert_from_base_10(num, base):
    result = ''
    while num > 0:
        remainder = num % base
        result = int2hex(remainder) + result
        num //= base
    return result
def main():
    # Nhập cơ số và giá trị đầu vào từ người dùng
    input_base = int(input("Nhập cơ số của giá trị đầu vào: "))
    if input_base < 2 or input_base > 16:
        print("Lỗi: Cơ số đầu vào không hợp lệ.")
        exit()
    input_num = input("Nhập giá trị đầu vào: ")

    # Chuyển đổi giá trị đầu vào sang cơ số 10
    decimal_num = convert_to_base_10(input_num, input_base)

    # Nhập cơ số đầu ra từ người dùng
    output_base = int(input("Nhập cơ số của giá trị đầu ra: "))
    if output_base < 2 or output_base > 16:
        print("Lỗi: Cơ số đầu ra không hợp lệ.")
        exit()

    # Chuyển đổi giá trị đầu vào từ cơ số 10 sang cơ số đầu ra
    output_num = convert_from_base_10(decimal_num, output_base)

    # Hiển thị kết quả
    print("Kết quả: {} (cơ số {}) = {} (cơ số {})".format(input_num, input_base, output_num, output_base))

if __name__ == "__main__":
    main()
