#n=int(input('n='))
#i=1
#while i<=n:
    #print('$'*(n+1-i))
    #i=i+1
#i=9
#while i>=1:
    #print('$'*i)
    #i=i-1
n=int(input("n="))
i=1
while i<=n:
    print(" "*(n-i),end="")     #In dau cach
    print("*"*(2*i-1)) #So luong dau * o dong i
    i=i+1
