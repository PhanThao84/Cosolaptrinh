n=input()
a=0
b=0
c=0
d=0
for i in n:
    if i.isupper():
        a=a+1
    elif i.islower():
        b=b+1
    elif i.isdigit():
        c=c+1   
    else:
        d=d+1
print('In hoa:',a,'\nIn thuong:',b,'\nChu so:',c,'\nKhac:',d)
