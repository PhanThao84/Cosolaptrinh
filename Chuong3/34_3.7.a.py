#n=int(input())
#gt=1
#while 0<=n:
#    while 0<n:
#        gt=gt*n
#        n=n-1
#   print(gt)
#    gt=1
#    n=int(input())
while True:
    n=int(input(''))
    a=1
    i=1
    if n<0:
        break
    else:
        while i<n:
            a=a*(i+1)
            i=i+1
        print(a)