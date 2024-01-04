n=int(input('n='))
listA=[]
for i in range (n):
    x=int(input())
    listA.append(x)
listB=listA
listA.reverse()
print(listB)
listA.sort()
print(listB)