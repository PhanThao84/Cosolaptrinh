A=[]
for i in range(10):
    a=int(input())
    A.append(a)
B=[]
for i in range(0, len(A)-1, 2):
    B.append(A[i+1])
    B.append(A[i])
for a in B:
    print(a,end=' ')
# 5.6. Viết chương trình nhập vào từ bàn phím 10 số nguyên và lưu vào một List A. Hãy hoán đổi giá trị
# của 2 phần tử nằm cạnh nhau (theo từng đôi) trong List. Và in lên màn hình List kết quả sau khi xử lý.

# Gợi ý:
# - Để hoán đổi giá trị theo cặp phần tử, sử dụng thêm List B để lưu trữ tập kết quả
# - Cho vòng lặp i=0.. (n-2) step=2
# o B[i]=A[i+1]
# o B[i+1]=A[i]
# 5
# 7
# 2
# 6
# 3
# 7
# 8
# 9
# 1
# 2
# 7 5 6 2 7 3 9 8 2 1