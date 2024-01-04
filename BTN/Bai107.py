l=[]
a=input()
while a!=0:
    if a not in l:
        l.append(a)
    a=input()
for a in l:
    print(a)
    