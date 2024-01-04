a=int(input(''))
b=int(input(''))
S=0
i=1
if a<b:
    for i in range (a+1,b+1):
        S=S+i
        i=i+1
    print(S)
else:
    print(0)