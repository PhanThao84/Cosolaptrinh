L=[]
Lnho=[]
while True:
    day=input()
    if day=='':
        break
    Lnho=day.split(' ')
    L.append(Lnho)
for i in range(len(L)):
    X=L[i][0]
    for j in range(len(L[i])):
        while X in L[i]:
            L[i].remove(X)
    print(len(L[i]))
