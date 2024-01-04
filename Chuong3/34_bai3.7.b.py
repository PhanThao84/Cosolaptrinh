while True:
    n=int(input())
    if n<0:
        break
    a=1
    for i in range(1,n):
        a=a*(i+1)
        i=i+1
    print(a)
    