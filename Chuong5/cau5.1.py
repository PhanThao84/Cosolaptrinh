def Input():
    L=[]
    n=int(input('n='))
    for i in range(n):
        x=int(input())
        L.append(x)
    x=int(input('x='))     
    return L,x
def FirstAndlast(L):
    return [L[0], L[-1]]
def Search(L,x):
    for i in L:
        if x == i:
            return True
    return False
L, x = Input()
first_last = FirstAndlast(L)
print(first_last)
a=Search(L,x)
if a == True:
    print(True)
else:
    print(False)



        