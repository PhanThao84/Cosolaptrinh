dau='!'+'()'+'-'+'[]'+'{}'+';:'+"'"+'"'+'\,<>./?@#$%^&*_~'
chuoi=input()
L=[]
for i in chuoi:
    L.append(i)
for i in range(len(L)-1,-1,-1):
    if L[i] in dau:
        del(L[i])
chuoimoi=''.join(L)
print(chuoimoi)

# dau = '!()[]{};:\'"\\,<>./?@#$%^&*_~'
# chuoi = input()
# chuoimoi = chuoi
# for char in dau:
#     chuoimoi = chuoimoi.replace(char, '')
# print(chuoimoi)
