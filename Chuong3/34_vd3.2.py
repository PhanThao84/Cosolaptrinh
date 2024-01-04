# a=int(input('So may='))
# if a>=5:
#     print('So tien='+str(a*450))
# if a<5:
#     print('So tien='+str(a*500))
year=int(input("Nhập năm: "))

if year%4==0:
    if year%100==0 and year%400!=0:
        print("Năm", year, "không phải là năm nhuận!")
    else:
        print("Năm", year, "là năm nhuận!")
else:
    print("Năm", year, "không phải là năm nhuận!")