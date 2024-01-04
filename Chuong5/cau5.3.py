L=[]
n=int(input('n='))
a=0
S=0
b=0
for i in range(n):
    x=int(input())
    L.append(x)
for x in L:
    if x>0:
        a=a+1
for x in L:
    if x%2==0:
        S=(S+x)
        b+=1
if b>0:
    S=S/b
print('SND=',a,sep='')
print('TBC=',S,sep='')