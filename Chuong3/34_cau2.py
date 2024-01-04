n=int(input('n='))
i=1
if 1<=n<=50:
    for i in range (1,n+1):
        print(i)
        if i%10==0:
            print('')
else:
    print('khong hop le')