n=int(input('n='))
L=[]
for i in range(n):
    a=int(input())
    while True:
        if a not in L:
            L=L+[a]
        else: break
for a in L:
    print(a,end=" ")